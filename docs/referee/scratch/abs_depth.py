#!/usr/bin/env python3
"""REFEREE succ. 16: ABS-DEPTH and N-MONO of P-N5-DEPTH-box22 §1 (sha1 549c7fb7) on my own model simulator abs_model.py (P-N5-GCX §4's
model, cyclic digraphs). No lane code. Per run that reaches a fixed point s*: d*(v) := non-terminals on v's s*-play;
 GEN    every v: all simple plays from v to a terminal have distinct N-values (exhaustive enumeration)
 DEP    ABS-DEPTH per vertex: play_t(v) = play*(v) for every t >= d*(v)   (counted separately for GEN / non-GEN runs)
 FIX    fixed after <= max d* steps                                       NMONO  N_{t+1} >= N_t (abs_model's MONO covers it)
Mutation MUT=1: per vertex from d*(v) - 1 (must bite). Usage: abs_depth.py N nmin nmax seed [wmax]   (weights in [-wmax, wmax], default 3)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import abs_model as A
MUT = int(os.environ.get("MUT", "0"))
EX = []
EXF = []


def plays_from(g, v):
    out = []; stack = [(v, (v,))]
    while stack:
        x, p = stack.pop()
        for y in g.succ[x]:
            if g.term(y): out.append(p + (y,))
            elif y not in p: stack.append((y, p + (y,)))
    return out


def nval(g, p): return sum(g.w[u] for u in p[:-1]) + g.T[p[-1] - g.n]


def main(a):
    N, lo, hi, seed = map(int, a[:4]); wmax = int(a[4]) if len(a) > 4 else 3
    r = random.Random(seed); cnt = Counter()
    for i in range(N):
        n = r.randint(lo, hi)
        g = A.gen(r, n, 1)
        g.w = [r.randint(-wmax, wmax) for _ in range(n)]
        s0 = A.start(g, r, 1)
        if s0 is None: cnt["nostart"] += 1; continue
        for rule in A.RULES:
            seq = [s0]; ok = True
            for _ in range(4 * (n + sum(len(x) for x in g.succ)) + 10):
                s2, status, _ = A.step(g, seq[-1], rule, cnt)
                if s2 is None: cnt[status] += 1; ok = False; break
                seq.append(s2)
                if s2 == seq[-2]: break
            else: cnt["NOFIX"] += 1; ok = False
            if not ok: continue
            cnt["RUNS_fixed"] += 1
            gen = all(len({nval(g, p) for p in plays_from(g, v)}) == len(plays_from(g, v)) for v in range(n))
            tag = "GEN" if gen else "NONGEN"
            cnt["runs_" + tag] += 1
            sstar = seq[-1]
            pstar = {v: g.play(sstar, v) for v in range(n)}
            dstar = {v: len(pstar[v][0]) for v in range(n)}
            T = len(seq) - 1
            fixed = next(t for t in range(T + 1) if seq[t] == sstar)
            cnt["FIX_chk_" + tag] += 1
            if fixed > max(dstar.values()):
                cnt["FIX_" + tag + "_FAIL"] += 1; cnt["FIXFAIL_rule_" + rule] += 1
                EXF.append(("FIX", tag, seed, i, rule, "fixed", fixed, "maxd*", max(dstar.values()), "n", n))
            if fixed == max(dstar.values()): cnt["FIX_sharp_" + tag] += 1
            for v in range(n):
                cnt["DEP_chk_" + tag] += 1
                for t in range(max(dstar[v] - (1 if MUT == 1 else 0), 0), T + 1):
                    if g.play(seq[t], v) != pstar[v]:
                        cnt["DEP_" + tag + "_FAIL"] += 1
                        if len(EX) < 20: EX.append(("DEP", tag, i, rule, v, t, dstar[v]))
                        break
            for t in range(T):
                N0 = g.vals(seq[t])[1]; N1 = g.vals(seq[t + 1])[1]
                cnt["NMONO_chk"] += 1
                if any(N1[x] < N0[x] for x in range(n)): cnt["NMONO_FAIL"] += 1
    for k in sorted(cnt): print(k, cnt[k])
    for e in EXF[:30]: print("EXF", e)
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
