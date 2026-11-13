#!/usr/bin/env python3
"""L-LOWER 19: replay of an enc19 decode with box 217's simulator (independent of enc19): T_key (one217.OneP key run), switches per
mover, |K(x)| by box 217 §5's DP (|K| = degree at level 0, sum over options of |K(wt)| above), the enumeration depth
k(G) = max{k : some level-(k-1) mover has sw = |K| - 1} (box 217 §5 A6), N, M, d, N + M; with --n5 also N5 itself on Gamma3
(one217.report --check: n5 steps and mism). Usage: rep19.py ONE217_DIR [--n5] G.json [STATES]  (STATES: enc19's state file, compared
with the simulator's run on the first L + 1 states, padded with the fixed point)."""
import sys, os, json
a = sys.argv[1:]; d217 = a.pop(0); n5 = '--n5' in a; a = [x for x in a if x != '--n5']
sys.path.insert(0, d217); import one217
G = json.load(open(a[0])); G = G.get('genome', G); N = G['N']; lev = G['lev']; opts = G['opts']; M = sum(len(o) for o in opts)
S = one217.OneP(G).run('key'); T = len(S) - 1
sw = [sum(1 for t in range(T) if S[t][x] != S[t + 1][x]) for x in range(N)]
K = [0] * N
for x in sorted(range(N), key=lambda x: lev[x]):
    K[x] = len(opts[x]) if lev[x] == 0 else sum(K[o[0]] for o in opts[x])
full = [x for x in range(N) if sw[x] == K[x] - 1]
kG = max([lev[x] + 1 for x in full], default=0)
out = f"REP {os.path.basename(a[0])} N {N} M {M} N+M {N + M} d {max(lev) + 1} T_key {T} k(G) {kG} sw/|K|-1 by level " + \
      ' '.join(f"L{l}:{max(sw[x] for x in range(N) if lev[x] == l)}/{max(K[x] for x in range(N) if lev[x] == l) - 1}" for l in range(max(lev) + 1))
if len(a) > 1:
    enc = [tuple(int(c) for c in l.strip()) for l in open(a[1]) if l.strip()]
    ref = [tuple(s) for s in S][:len(enc)]; ref += [ref[-1]] * (len(enc) - len(ref))
    out += f" | enc states (L {len(enc) - 1}) == sim {int(enc == ref)}"
if n5:
    r = one217.report(os.path.basename(a[0]), G, True); out += ' | ' + r[r.index('key'):]
print(out)
