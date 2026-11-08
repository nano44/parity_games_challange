#!/usr/bin/env python3
"""L-LOWER 12 (BOX L12): a NON-minimal re-timing of a capped run's pairs 0..H-2 with the least retrigger bill, and the level-H core
target on it (pair H-1 added as in l10/build.core8).
- Core steps: the steps of the run at which a mover of pairs 0..H-2 moves (as l10/stretch.py). Gap i = before core step i.
- Bill of gap i, b(i) = movers x of pairs 0..H-2 that are FREE at the pre-state of step i (level 0: gate allows; level >= 1:
  s_x != c_x at the pre-state keys) and MOVE at step i. Inserting >= 1 idle step in gap i makes each of them hold, then move:
  each needs a non-core mover (pair H-1 or a helper) on its chain to change at the last idle step (l10/need.py's bill, here
  with level 0 included). Inserting k >= 1 idle steps costs b(i), independent of k.
- Constraints: l10/stretch.stretch's difference constraints tau(b) - tau(a) >= k (P-TOWER-FUEL Lemmas 2, 3 at H; level-(H-1)
  windows >= 2 steps, first o(H-2) change at tau >= 3), plus the tail window >= 2 steps.
- Solve: gaps with b = 0 are free. Each constraint whose interval (a, b] holds no free gap forces one costly gap: chosen by an exact
  weighted interval hitting DP (min total bill). Then the least number of idle steps in the allowed gaps (free + chosen) by the
  right-endpoint greedy, optimal for interval multi-cover.
Writes the level-H target in l10 core-file format («rows K», bit strings) and a tsat-format copy. Usage: slackt.py GENOME H OUTPREFIX"""
import sys, os
from collections import Counter
here = os.path.dirname(os.path.abspath(__file__))
for p in ('../l10', '../l6', '../l9'): sys.path.insert(0, os.path.join(here, p))
from sim6 import rd, run, okeys
from stretch import stretch
D = rd(sys.argv[1]); H = int(sys.argv[2]); outp = sys.argv[3]; S, O = run(D); T = len(S) - 1; J = H - 1; g = D['gate']
keep = [0] + [t for t in range(1, T + 1) if S[t][:2 * J] != S[t - 1][:2 * J]]
S2 = [S[t][:2 * J] for t in keep]; O2 = [O[t][:J] for t in keep]; n = len(S2) - 1
tau0, Tp0, need = stretch(S2, O2, H)
def bill(i):
    pre, post, o = S2[i - 1], S2[i], O2[i - 1]; M = []
    for x in range(2 * J):
        l = x // 2
        free = (g[2 * x + 1 - pre[x]] < g[2 * x + pre[x]]) if l == 0 else (pre[x] != o[l - 1])
        if free and post[x] != pre[x]: M.append(x)
    return M
B = {i: bill(i) for i in range(1, n + 1)}
cons = [(a, b, k - (b - a)) for (a, b), k in need.items() if k - (b - a) > 0]   # need r >= 1 insertions in gaps a+1..b
ch = [i for i in range(1, n + 1) if O2[i][H - 2] != O2[i - 1][H - 2]]
free = [i for i in range(1, n + 1) if not B[i]]
fset = set(free)
hard = [(a, b) for a, b, r in cons if not any(i in fset for i in range(a + 1, b + 1))]
# exact min-weight hitting of the hard intervals by costly gaps (points): DP over sorted right ends
hard = sorted(set(hard), key=lambda ab: ab[1]); chosen = set()
if hard:
    pts = sorted(set(i for a, b in hard for i in range(a + 1, b + 1)))
    w = {i: len(B[i]) for i in pts}
    # dp over points in increasing order: best[i] = min cost covering all intervals with b < next uncovered, last chosen point i
    import functools
    best = {}
    for p in pts:
        # intervals that must be hit by p or later and end before p are already handled: predecessor q must hit all intervals
        # with b < p, and every interval with a < q ... standard: choose q < p such that no hard interval lies strictly in (q, p)
        cand = [(w[p], None)]
        for q in best:
            if not any(q < a + 1 and b < p for a, b in hard): cand.append((best[q][0] + w[p], q))
        if any(b < p for a, b in hard):   # p cannot be the first chosen point if an interval ends before it
            cand = [c for c in cand if c[1] is not None]
        if cand: best[p] = min(cand)
    ends = [p for p in best if not any(a + 1 > p for a, b in hard)]
    p = min(ends, key=lambda q: best[q][0])
    while p is not None: chosen.add(p); p = best[p][1]
allowed = sorted(fset | chosen)
# greedy multi-cover: by right end, add the deficit at the rightmost allowed gap in (a, b]
ins = Counter()
for a, b, r in sorted(cons, key=lambda c: c[1]):
    have = sum(ins[i] for i in range(a + 1, b + 1))
    if have < r:
        gaps = [i for i in allowed if a < i <= b]
        if not gaps: raise SystemExit(f'constraint ({a},{b}) has no allowed gap')
        ins[gaps[-1]] += r - have
tau = [0] * (n + 1)
for i in range(1, n + 1): tau[i] = tau[i - 1] + 1 + ins[i]
ok = all(tau[b] - tau[a] >= k for (a, b), k in need.items())
Tp = max(tau[n], tau[ch[-1]] + 1)
# stretched core on the new axis
Sc = []; Oc = []
for i in range(n + 1):
    while len(Sc) < tau[i]: Sc.append(S2[i - 1]); Oc.append(O2[i - 1])
    Sc.append(S2[i]); Oc.append(O2[i])
while len(Sc) <= Tp: Sc.append(S2[-1]); Oc.append(O2[-1])
c = [o[H - 2] for o in Oc]; f = q = 1 - c[0]; pend = None; LS = []
for t in range(len(Sc)):
    if t >= 1:
        if t == 1 or c[t] != c[t - 1]: f = c[t]; pend = t + 1
        elif pend == t: q = c[t]; pend = None
    LS.append(tuple(Sc[t]) + (q, f))
cg = list(g[:4 * J]) + [4 * J + 1000 + k for k in range(4)]
Of = [okeys({'d': H, 'gate': cg}, list(s)) for s in LS]
F = [sum(1 for t in range(1, len(Of)) if Of[t][l] != Of[t - 1][l]) for l in range(H)]
bill_tot = sum(len(B[i]) for i in range(1, n + 1) if ins[i])
idle = sum(ins.values())
print(f'core steps {n}; minimal stretch T\' {Tp0}; constraints needing insertions {len(cons)}; free gaps {len(free)}; hard intervals {len(hard)}; chosen costly gaps {sorted(chosen)} (bill {sum(len(B[i]) for i in chosen)})')
print(f'new T\' {Tp} (idle steps {idle} in {sum(1 for i in ins if ins[i])} gaps), constraints all met {ok}, total retrigger bill {bill_tot}; F(0..{H-1}) {F}; slack steps (o({H-1}) unchanged) {sum(1 for t in range(1, len(Of)) if Of[t][H-1] == Of[t-1][H-1])}')
with open(outp + '_core.txt', 'w') as fo:
    fo.write(f'{len(LS)} {2 * H}\n'); fo.writelines(''.join(map(str, s)) + '\n' for s in LS)
with open(outp + '_tsat.txt', 'w') as fo:
    fo.write(f'# slackt.py {sys.argv[1]} {H}: least-bill re-timing, T {len(LS) - 1}\ngate ' + ' '.join(map(str, cg)) + '\n')
    fo.writelines(' '.join(map(str, s)) + '\n' for s in LS)
