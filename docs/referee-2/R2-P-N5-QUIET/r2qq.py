#!/usr/bin/env python3
"""REFEREE-2 succ. 33: every «…» quote in P-N5-QUIET §1, fixes entry 1 ([OPT], G-2) and line L-1, located verbatim (whitespace-
normalised; «…» elisions matched in order) in: trunk docs/RESULTS.md (entry and line), frozen P-N5-XICYC.md (fd1266a5, sha1 149e2414),
frozen docs/red/P-N5-REALIZE.md (e609c5d2), the packet itself (self-quotes). Nested «» are flattened by taking innermost-first spans.
Usage: r2qq.py PACKET FIXES L1 RESULTS XICYC REALIZE"""
import sys, re
P, F, L, R, X, Z = (open(p, encoding='utf-8').read() for p in sys.argv[1:7])
n = lambda t: ' '.join(t.split())
RL = R.split('\n'); NR = n(R)
heads = [(i + 1, l.split(' ')[1]) for i, l in enumerate(RL) if l.startswith('### R')]
def where(frag):
    k = frag[:50]; NL = [n(l) for l in RL]
    for w in (1, 2, 3):           # the line where the fragment STARTS: smallest window first, then its first line
      for i in range(len(RL)):
        j = ' '.join(NL[i:i + w])
        if k in j and (w == 1 or k not in ' '.join(NL[i + 1:i + w])):
            e = [h for h in heads if h[0] <= i + 1]; return f"RESULTS l. {i + 1} ({e[-1][1] if e else '?'})"
    return 'RESULTS (spans lines)'
src = [('RESULTS', NR), ('XICYC', n(X)), ('REALIZE', n(Z)), ('PACKET', n(P)), ('FIXES', n(F))]
def find(q):
    parts = [p.strip() for p in n(q).replace('…', '\x00').split('\x00') if p.strip()]
    for name, E in src:
        pos = 0; ok = True
        for p in parts:
            k = E.find(p, pos)
            if k < 0: ok = False; break
            pos = k + len(p)
        if ok: return name, parts[0]
    return None, None
def quotes(t):  # innermost «…» spans, then outer spans with inner quote marks stripped
    out = []; st = []
    for i, c in enumerate(t):
        if c == '«': st.append(i)
        elif c == '»' and st:
            a = st.pop(); out.append(t[a + 1:i].replace('«', '').replace('»', ''))
    return out
secs = [('PACKET §1', P[P.index('## 1. Premises'):P.index('## 2. Lemma CN2')]),
        ('FIXES [OPT]+G-2', F[F.index('### G-2'):F.index('### DATA added')]), ('L-1', L)]
miss = 0; tot = 0
for nm, t in secs:
    for q in quotes(t):
        if len(q.strip()) < 8: continue
        tot += 1; s, first = find(q)
        loc = where(first) if s == 'RESULTS' else s
        if s is None: miss += 1
        print(f"{nm:16} {'OK  ' if s else 'MISS'} {loc or '-':28} | {n(q)[:100]}")
print('quotes', tot, 'missing', miss)
