#!/usr/bin/env python3
"""ai_tell_lint.py - flag mechanical AI-writing fingerprints in .md/.docx.
Free, local, stdlib-only. Not a detector; a stylometric linter that catches
what detectors AND human editors catch. Goal: reduce tells, not hit 0%.

Usage:  python ai_tell_lint.py "file.docx"
        python ai_tell_lint.py "file.md"
"""
import sys, re, zipfile, statistics
try:
    from defusedxml.ElementTree import fromstring as _fromstring  # XXE-safe if installed
except ImportError:
    from xml.etree.ElementTree import fromstring as _fromstring  # ponytail: local self-authored docx only; upgrade path is `pip install defusedxml`

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

# ponytail: hardcoded lists, not a config file. Edit inline when a new tell shows up.
BANNED = ("delve tapestry boasts realm testament navigating landscape robust seamless "
          "leverage underscore multifaceted crucial pivotal foster nuanced intricate "
          "elevate embark unlock harness bustling meticulous").split()
EMDASH = ('—', '–')

def get_text(path):
    if path.lower().endswith('.docx'):
        z = zipfile.ZipFile(path)
        root = _fromstring(z.read('word/document.xml'))
        paras = []
        for p in root.iter(W+'p'):
            t = ''.join(x.text or '' for x in p.iter(W+'t')).strip()
            if t: paras.append(t)
        return paras
    with open(path, encoding='utf-8') as f:
        raw = f.read()
    # strip md frontmatter/self-check/refs so we lint prose only
    raw = re.sub(r'^---.*?---', '', raw, count=1, flags=re.S)
    raw = re.split(r'## References|## Self-check', raw)[0]
    return [ln.strip() for ln in raw.splitlines() if ln.strip() and not ln.startswith('#')]

def lint(path):
    paras = get_text(path)
    body = ' '.join(p for p in paras if len(p.split()) > 12)  # skip headings/byline
    sents = [s.strip() for s in re.split(r'(?<=[.?!])\s+', body) if s.strip()]
    lens = [len(s.split()) for s in sents]
    findings = []

    def flag(sev, name, val, ceiling, note):
        if val > ceiling:
            findings.append((sev, f"{name}: {val} (aim <= {ceiling}) - {note}"))

    # 1. burstiness (LOW stdev is the tell; here we flag if TOO uniform)
    sd = round(statistics.pstdev(lens), 1) if lens else 0
    if sd < 7:
        findings.append(('HIGH', f"Burstiness stdev {sd} - too uniform, vary sentence length"))
    else:
        findings.append(('ok', f"Burstiness stdev {sd} - fine (>=7)"))

    # 2. negation-contrast tic ("is not X. It is Y", "not A but B")
    neg = len(re.findall(r'\b(is not|are not|does not|do not|will not|not because|rather than|instead of)\b', body, re.I))
    flag('HIGH', "Negation/contrast constructions", neg, 6,
         "the #1 GPT rhythm; keep 1-2 for effect, rewrite the rest")

    # 3. copula sentence-openers
    cop = sum(1 for s in sents if re.match(r'(it|that|this|there)\s+(is|are|was)\b', s, re.I))
    flag('MED', "Copula openers (It is/That is/There are)", cop, 3, "start with a noun/verb instead")

    # 4. article-opener monotony
    art = sum(1 for s in sents if s.split() and s.split()[0].lower() in ('the', 'a', 'an'))
    pct = round(100*art/len(sents)) if sents else 0
    flag('MED', f"Article-opener sentences ({pct}%)", art, len(sents)//3,
         "vary openers: names, dates, clauses, verbs")

    # 5. banned AI vocab
    hits = sorted({w for w in BANNED if re.search(rf'\b{w}\w*\b', body, re.I)})
    if hits: findings.append(('HIGH', f"Banned vocab: {', '.join(hits)}"))
    else: findings.append(('ok', "Banned vocab: none"))

    # 6. em/en dashes (house rule)
    dash = sum(body.count(d) for d in EMDASH)
    if dash: findings.append(('HIGH', f"Em/en dashes in body: {dash} (must be 0)"))
    else: findings.append(('ok', "Em/en dashes: 0"))

    # 7. triads (word. word. word. fragment stacking) - templated cadence
    triads = len(re.findall(r'(?<=[.?!])\s+\w[\w\s]{1,18}\.\s+\w[\w\s]{1,18}\.\s+\w[\w\s]{1,18}\.', body))
    flag('LOW', "Short-fragment triads", triads, 2, "signature list cadence; break one up")

    # --- Evidence-based features (from AI-detector research 2026-07-27) ---
    words = re.findall(r"[a-z']+", body.lower())
    nwords = max(1, len(words))

    # 7b. hedging density (RAISE=more AI: RLHF over-hedges). per 1000 words.
    HEDGE = r'\b(may|might|could|perhaps|possibly|potentially|arguably|somewhat|relatively|generally|tends? to|to some extent|in some ways|it seems|likely|often|usually|typically)\b'
    hedges = len(re.findall(HEDGE, body, re.I))
    hp = round(1000*hedges/nwords, 1)
    flag('MED', f"Hedging density {hp}/1000w ({hedges})", hp, 12, "AI over-hedges; assert positively, hedge only where truly uncertain")

    # 7c. lexical diversity / type-token ratio (RAISE=more human). LOW is the tell.
    ttr = round(len(set(words))/nwords, 3)
    if ttr < 0.40 and nwords > 200:
        findings.append(('MED', f"Lexical diversity (TTR) {ttr} - low, AI reuses words; vary vocabulary"))
    else:
        findings.append(('ok', f"Lexical diversity (TTR) {ttr} (>=0.40 good)"))

    # 7d. weak-verb / nominalization density (RAISE=dull+AI-ish). per 1000 words.
    NOMINAL = r'\b\w{4,}(tion|ment|ance|ence|ility|ization|isation)s?\b'
    WEAKVERB = r'\b(is|are|was|were|be|been|being|has|have|had|make|makes|made|do|does|did|provide[sd]?)\b'
    noms = len(re.findall(NOMINAL, body, re.I))
    np_ = round(1000*noms/nwords, 1)
    flag('LOW', f"Nominalization density {np_}/1000w ({noms})", np_, 25, "put the action in the verb (Williams/Gopen-Swan); '-tion' nouns hide it")

    # 8. per-sentence hotspot pass. Real detectors (Turnitin) score overlapping
    #    5-10 sentence windows and average; GPTZero adds perplexity (word-choice
    #    predictability). We cannot run an LLM locally, so proxy predictability by
    #    formulaic-phrase density + template shape, then surface the riskiest sents.
    FORMULAIC = [
        r'\bit is (important|worth|clear|essential|crucial) to\b', r'\bin conclusion\b',
        r'\bplays? a (key|vital|crucial|significant) role\b', r'\bwhen it comes to\b',
        r'\bin today\'?s (world|landscape|environment)\b', r'\bat the end of the day\b',
        r'\bnot only\b.*\bbut also\b', r'\bmore than just\b', r'\bthe key to\b',
        r'\bis (not|never) (just )?about\b', r'\bthe reality is\b', r'\bmake no mistake\b',
    ]
    def score(s):
        v = 0
        sw = s.split()
        if re.match(r'(it|that|this|there)\s+(is|are|was)\b', s, re.I): v += 1
        if sw and sw[0].lower() in ('the','a','an'): v += 1
        if re.search(r'\b(is not|are not|does not|do not|will not|not because|rather than|instead of)\b', s, re.I): v += 1
        v += sum(1 for p in FORMULAIC if re.search(p, s, re.I)) * 2
        return v
    scored = sorted(((score(s), s) for s in sents), key=lambda x: -x[0])
    hot = [(v, s) for v, s in scored if v >= 2]
    if hot:
        findings.append(('MED', f"Hotspot sentences (score>=2): {len(hot)} - see below"))
    else:
        findings.append(('ok', "Hotspot sentences: none (no single sentence stacks tells)"))

    # report
    order = {'HIGH':0,'MED':1,'LOW':2,'ok':3}
    findings.sort(key=lambda f: order[f[0]])
    print(f"\n=== AI-tell lint: {path} ===")
    mean_w = round(statistics.mean(lens), 1) if lens else 0
    print(f"{len(sents)} sentences, mean {mean_w}w\n")
    for sev, msg in findings:
        tag = {'HIGH':'[!]','MED':'[.]','LOW':'[ ]','ok':' ok'}[sev]
        print(f"  {tag} {msg}")
    if hot:
        print("\n  Riskiest sentences (rewrite these first, Turnitin scores per-sentence):")
        for v, s in hot[:5]:
            print(f"    [{v}] {s[:100]}{'...' if len(s)>100 else ''}")
    hi = sum(1 for s,_ in findings if s=='HIGH')
    print(f"\n  {hi} high-severity tell(s). Fix these first.\n")
    return findings

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("usage: python ai_tell_lint.py <file.md|file.docx>"); sys.exit(1)
    lint(sys.argv[1])

# demo self-check: synthetic AI-ish text must trip the negation + copula flags.
def _demo():
    import tempfile, os
    # >6 negations + copula openers + a formulaic phrase, so every layer must trip.
    txt = ("It is not a tool. It is not a trend. It is a philosophy. This does not scale "
           "and will not last, not because it fails but because people do not trust it. "
           "That is not the point, rather than the truth. When it comes to change, it is "
           "important to note that success is not about speed instead of depth.")
    f = tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8')
    f.write("---\nx\n---\n"+txt); f.close()
    fs = lint(f.name); os.unlink(f.name)
    assert any('Negation' in m and s=='HIGH' for s,m in fs), "should flag negation tic"
    assert any('Copula' in m for s,m in fs), "should flag copula openers"
    assert any('Hotspot' in m and s=='MED' for s,m in fs), "should surface per-sentence hotspots"
    print("demo ok")
