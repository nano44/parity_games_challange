#!/usr/bin/env python3
"""L-RED 58 R224 (Lead item 6): independent check of L-LOWER 10's minimal STRETCH of HIT7 for h = 8 (claude/l-lower 1802a93f,
docs/lower/L10-design.md §1a). Run of HIT7 from L-LOWER's simulator sim6 (env LOW = worktree of l-lower 1802a93f); everything else is
mine, from P-TOWER-FUEL §1-§2 definitions: j-windows (cuts at changes of o_(j-1)), PULSE / GAP >= H - j for j = 1..H-2 (Lemmas 2, 3),
7-windows (cuts at changes of o_(H-2)) each with >= 2 steps (Lemma 1 (E1), (E3), (E4) for a doubling level H-1: both members move,
at distinct steps, in EVERY window, the first [1, b_1 - 1] and the last included). Minimal tau by longest path.
VARIANT=lower: L-LOWER's constraint set (first o_(H-2) change at tau >= 2, i.e. first window >= 1 step). VARIANT=fix: first >= 3.
Prints T', window-length histogram, idle placement and the retrigger bill (need.py's definition) on the result; writes the target.
Usage: stack224.py GENOME H OUT_TARGET"""
import sys, os
from collections import Counter, defaultdict
LOW = os.environ["LOW"]; sys.path[:0] = [os.path.join(LOW, "experiments/lower/l6")]
from sim6 import rd, run
D = rd(sys.argv[1]); H = int(sys.argv[2]); S, O = run(D); T = len(S) - 1; J = H - 1; var = os.environ.get("VARIANT", "fix")
e3 = sum(1 for t in range(1, T + 1) for j in range(1, J) if (O[t][j] != O[t - 1][j]) != (S[t][2 * j:2 * j + 2] != S[t - 1][2 * j:2 * j + 2]))
keep = [0] + [t for t in range(1, T + 1) if S[t][:2 * J] != S[t - 1][:2 * J]]; S2 = [S[t] for t in keep]; O2 = [O[t] for t in keep]; n = len(S2) - 1
need = defaultdict(int)
for j in range(1, J):
    b = [i for i in range(1, n + 1) if O2[i][j - 1] != O2[i - 1][j - 1]]; cuts = [1] + b + [n + 1]; W = []
    for a, e in zip(cuts, cuts[1:]): W.append(sorted(i for i in range(a, e) for x in (2 * j, 2 * j + 1) if S2[i][x] != S2[i - 1][x]))
    for k, mv in enumerate(W):
        if len(mv) == 2:
            need[(mv[0], mv[1])] = max(need[(mv[0], mv[1])], H - j)
            if k + 1 < len(W) and len(W[k + 1]) == 2: need[(mv[1], W[k + 1][0])] = max(need[(mv[1], W[k + 1][0])], H - j)
ch = [i for i in range(1, n + 1) if O2[i][J - 1] != O2[i - 1][J - 1]]
for a, c in zip(ch, ch[1:]): need[(a, c)] = max(need[(a, c)], 2)
need[(0, ch[0])] = max(need[(0, ch[0])], 2 if var == "lower" else 3)
inc = defaultdict(list)
for (a, c), k in need.items(): inc[c].append((a, k))
tau = [0] * (n + 1)
for i in range(1, n + 1): tau[i] = max([tau[i - 1] + 1] + [tau[a] + k for a, k in inc[i]])
Tp = max(tau[n], tau[ch[-1]] + 1)
# build the target on the new axis
Snew = [None] * (Tp + 1); idle = [False] * (Tp + 1)
for i in range(n + 1): Snew[tau[i]] = S2[i][:2 * J]
for t in range(1, Tp + 1):
    if Snew[t] is None: Snew[t] = Snew[t - 1]; idle[t] = True
chn = [t for t in range(1, Tp + 1) if Snew[t][2 * (J - 1):2 * J] != Snew[t - 1][2 * (J - 1):2 * J]]
cuts = [1] + chn + [Tp + 1]; lens = [e - a for a, e in zip(cuts, cuts[1:])]
bad = sum(1 for L in lens if L < 2)
Mc = Counter(); Hc = Counter(); sizes = Counter(); gaps = 0
for i in range(1, n + 1):
    if tau[i] - tau[i - 1] < 2: continue
    gaps += 1; pre, post, o = S2[i - 1], S2[i], O2[i - 1]
    free = [x for x in range(2, 2 * J) if pre[x] != o[x // 2 - 1]]
    M = [x for x in free if post[x] != pre[x]]
    for x in M: Mc[x] += 1
    for x in free:
        if post[x] == pre[x]: Hc[x] += 1
    sizes[len(M)] += 1
open(sys.argv[3], "w").write(f"# L-RED R224 stretched core target VARIANT={var}, H={H}\n" + "".join(f"{t} {"".join(map(str, Snew[t]))}{' *' if idle[t] else ''}\n" for t in range(Tp + 1)))
print(f"VARIANT {var}: T {T} core steps {n} E3-mismatches {e3} T' {Tp} idle {sum(idle)} gaps-with-idle {gaps} first-o{J-1}-change {chn[0]} "
      f"{J}-windows {len(lens)} length-hist {sorted(Counter(lens).items())} windows<2 {bad} first-window {lens[0]} last-window {lens[-1]}")
print(f"  bill: gaps {gaps} |M| hist {sorted(sizes.items())} events {sum(Mc.values())} per mover {sorted(Mc.items())}")
print(f"  free-and-holding per mover {sorted(Hc.items())}")
