#!/usr/bin/env python3
"""REFEREE-2 succ. 31: every «…» quote of P-N5-ASC §1 (and §3's [DEF] quote) located verbatim (whitespace-normalised; «…» elisions
matched in order) in trunk RESULTS R104 / R118 entries or in the frozen P-N5-XICYC.md; prints the RESULTS line number of each hit.
Usage: r2q.py ASC.md RESULTS.md XICYC.md"""
import sys, re
A, R, X = (open(p, encoding='utf-8').read() for p in sys.argv[1:4])
n = lambda t: ' '.join(t.split())
RL = R.split('\n')
def entry(tag):
    i = R.index('### ' + tag + ' '); j = R.find('\n### ', i + 1); return R[i:j]
def lineof(frag):
    for k, l in enumerate(RL, 1):
        if frag[:40] in n(l): return k
    return None
src = {'R104': n(entry('R104')), 'R118': n(entry('R118')), 'P-N5-XICYC': n(X)}
def find(q):
    parts = [p.strip() for p in n(q).split('…') if p.strip()]
    for name, E in src.items():
        pos = 0; ok = True
        for p in parts:
            k = E.find(p, pos)
            if k < 0: ok = False; break
            pos = k + len(p)
        if ok: return name
    return None
sec = A[A.index('## 1. Premises'):A.index('## 2. Definitions')] + A[A.index('**Lemma CHAIN-DECOMP'):A.index('## 4.')]
for q in re.findall(r'«(.*?)»', sec, re.S):
    if q.startswith('DECISION') or len(q) < 6: continue
    hit = find(q); print(('OK   ' + hit).ljust(16) if hit else 'MISS'.ljust(16), 'line', lineof(n(q).split('…')[0].strip()) if hit in ('R104', 'R118') else '-', '|', n(q)[:110])
# the packet's line numbers
for tag, ln in [('R104 heading', 9864), ('R118 heading', 13607)]:
    print(tag, 'at l.', ln, ':', RL[ln - 1][:24])
for ln, frag in [(13677, '(a) Definitions'), (13682, '(b) Facts F1-F6'), (13691, '(e) Lemma CYC-COUNT'), (10085, 'the exact e-priorities to packet §3.1')]:
    print('l.', ln, 'contains', repr(frag), ':', frag in RL[ln - 1])
XL = X.split('\n')
for ln in range(69, 75): print('XICYC l.', ln, ':', XL[ln - 1][:150])
