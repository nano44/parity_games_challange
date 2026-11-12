#!/usr/bin/env python3
"""DATA beside the Lean statements of PGLemmas/GenomeLevelStatement.lean (box 208 on the genome).

Not a proof and not the Lean code: the script evaluates, in Python, the conclusions of `L2Statement`,
`L3Statement`, `L5Statement`, `PlateauGStatement`, `QuietStatement`, `AllTCycSharpStatement` and of
(K1) on keys, as the Lean file states them, along the fleet's IDEAL-CYC run of a genome
(experiments/new/box191/idealcyc.py run(G) with experiments/si/si.py; the same run and the same
valuation transcription as check/idealcheck.py), for EVERY reference state b = 0, …, T.  The Lean
theorems prove these conclusions for every run; the script shows that the statements, read as written,
are not empty on real runs (fronts, stalls and plateaus occur) and counts them.

Objects, transcribed from GenomeClass.lean / GenomeOrderStatement.lean / LevelCountStatement.lean:
  cls_t(v) = (lam, the e-vertices of pset);  clsKey(Λ, E) = (rew Λ, Σ_{x ∈ E} 2^(pr x)), compared
  lexicographically;  ck t v = clsKey(cls_t(v));
  FrontAt b t v:  ck t v ≠ ck b v  and  ck t v ≤ ck t u for every u with ck t u ≠ ck b u;
  StallAt b t:    something lags at t, and every front vertex has ck (t+1) v = ck t v.

Counters (all must be 0 without a control); units as printed:
  keyfail     the key order differs from `clsLt` (the definition, with the symmetric difference) on a
              pair of classes that occur; unit: ordered pair of distinct occurring classes of a genome
  k1fail      ck t v > ck (t+1) v; unit: (step, vertex)
  l2fail      a front vertex is not a mover, a gate or a β-vertex with a mover successor;
              unit: (b, t, front vertex)
  l3fail      neither clause (α) nor clause (β) of `L3Statement` holds; unit: (b, t) with a lagging vertex
  l5fail      a front vertex's class is neither the class at b of a gate nor (β, ∅) for a β-vertex, or
              the front has more than N + 2M vertices; unit: (b, t) with a lagging vertex
  platfail    a maximal interval of consecutive stalls (reference b) has more than N steps;
              unit: (b, maximal interval of stalls)
  quietfail   a maximal window of the run on which no class changes has more than N steps;
              unit: maximal window
  boundfail   T > 2M(N + 2M)(N + 1) + N; unit: genome
Descriptive (not must-0): lagpairs = pairs (b, t) with a lagging vertex; alpha / beta = how often clause
(α) / clause (β) holds; stalls = stall steps over all b; maxplat = the longest interval of stalls;
maxquiet = the longest window of constant classes; maxfront = the largest front.

Control LEVEL_CTRL=1: the front is taken at the HIGHEST lagging key instead of the lowest; l2fail,
l3fail or l5fail must fire.

Usage (from the repository root):
    python3 -I lean/lemmas/check/levelcheck.py experiments/new/box191/inst/*.json
Exit code 0: without the control every counter is 0; with it, one of l2fail, l3fail, l5fail fired.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path[:0] = [HERE, os.path.join(ROOT, "experiments", "new", "box191"),
                os.path.join(ROOT, "experiments", "red", "r187")]
import crosscheck as cc  # noqa: E402
import idealcheck as ic  # noqa: E402  (vals: the valuation of Defs.lean by walking the play)
import idealcyc  # noqa: E402
import gamma3  # noqa: E402
import si  # noqa: E402
import stab  # noqa: E402

cc.CTRL = False
CTRL = os.environ.get("LEVEL_CTRL") == "1"
NAMES = ["keyfail", "k1fail", "l2fail", "l3fail", "l5fail", "platfail", "quietfail", "boundfail"]
DESC = ["states", "lagpairs", "alpha", "beta", "stalls", "maxplat", "maxquiet", "maxfront"]


def cls_lt(pr, c, d):
    """clsLt (GenomeClass.lean): rew Λ < rew Λ′, or Λ = Λ′ and the most relevant element of E Δ E′ is in E′."""
    if cc.rew(pr, c[0]) != cc.rew(pr, d[0]):
        return cc.rew(pr, c[0]) < cc.rew(pr, d[0])
    D = c[1] ^ d[1]
    return bool(D) and max(D, key=lambda x: pr[x]) in d[1]


def check(path):
    G = json.load(open(path))
    N = G["N"]
    c = dict.fromkeys(NAMES + DESC, 0)
    ref = stab.build(G, 0, kgad=True, esc=True)[0]
    n = ref.n
    M = (n - N - 6) // 3
    odd = [ref.owner[v] == 1 for v in range(n)]
    order = sorted(range(n), key=lambda v: (ref.prio[v], v))
    pr = [0] * n
    for r, v in enumerate(order):
        pr[v] = 2 * r + ref.prio[v] % 2
    V = gamma3.build(G, set())[3]
    kind = {}
    for key, v in V.items():
        kind[v] = key[0] if isinstance(key, tuple) else key
    xt_some = {V[("b", (x, k))]: G["opts"][x][k][1] >= 0 for x in range(N) for k in range(len(G["opts"][x]))}
    gates = [v for v in range(n) if kind[v] == "g"]
    betas = [v for v in range(n) if kind[v] == "b"]
    h, s0, movers, _ = idealcyc.build(G)
    eng = si.Engine(h)
    run = idealcyc.run(G)
    T = len(run) - 1
    c["states"] = T + 1
    s, cl, ck = [], [], []
    for t in range(T + 1):
        strat = list(s0)
        for x in movers:
            strat[x] = V[("g", (x, run[t][x]))]
        tau = eng.evaluate(tuple(strat))[1]
        st = [tau[v] if odd[v] else strat[v] for v in range(n)]
        vt = ic.vals(pr, st)
        ct = [(vt[v][0], frozenset(u for u in vt[v][1] if kind[u] == "e")) for v in range(n)]
        s.append(st)
        cl.append(ct)
        ck.append([(cc.rew(pr, a), sum(1 << pr[x] for x in e)) for a, e in ct])
    # the key order is clsLt on the classes that occur
    occ = sorted({cl[t][v] for t in range(T + 1) for v in range(n)}, key=lambda q: (q[0], sorted(q[1])))
    key = lambda q: (cc.rew(pr, q[0]), sum(1 << pr[x] for x in q[1]))
    for a in occ:
        for b in occ:
            if a != b:
                c["keyfail"] += (key(a) < key(b)) != cls_lt(pr, a, b)
    for t in range(T):
        c["k1fail"] += sum(ck[t][v] > ck[t + 1][v] for v in range(n))
    for b in range(T + 1):
        stall = [False] * (T + 1)
        for t in range(b + 1):
            lag = [v for v in range(n) if ck[t][v] != ck[b][v]]
            if not lag:
                continue
            c["lagpairs"] += 1
            m = (max if CTRL else min)(ck[t][v] for v in lag)
            front = [v for v in lag if ck[t][v] == m]
            fset = set(front)
            c["maxfront"] = max(c["maxfront"], len(front))
            # (L2)
            c["l2fail"] += sum(not (kind[v] in ("x", "g") or (kind[v] == "b" and xt_some[v])) for v in front)
            # (L3)
            lagset = set(lag)
            alpha = any(kind[x] == "x" and s[t][x] not in lagset and cl[t][x] == cl[b][s[t][x]] for x in front)
            beta = False
            for v in front:                                   # a play at t whose cycle lies in the front
                seq, pos, u = [], {}, v
                while u not in pos:
                    pos[u] = len(seq)
                    seq.append(u)
                    u = s[t][u]
                cyc = seq[pos[u]:]
                lam = max(cyc, key=lambda w: pr[w])
                if (kind[lam] == "b" and all(w in fset and kind[w] in ("x", "g", "b") for w in cyc)
                        and cl[t][lam] == (lam, frozenset())):
                    beta = True
                    break
            c["alpha"] += alpha
            c["beta"] += beta
            c["l3fail"] += not (alpha or beta)
            # (L5)
            allowed = {cl[b][g] for g in gates} | {(q, frozenset()) for q in betas}
            c["l5fail"] += (any(cl[t][v] not in allowed for v in front) or len(front) > N + 2 * M)
            # StallAt b t
            stall[t] = t < T and all(ck[t + 1][v] == ck[t][v] for v in front)
        # maximal intervals of consecutive stalls
        t = 0
        while t <= b:
            if stall[t]:
                u = t
                while t <= b and stall[t]:
                    t += 1
                c["stalls"] += t - u
                c["maxplat"] = max(c["maxplat"], t - u)
                c["platfail"] += (t - u) > N
            else:
                t += 1
    # maximal windows of constant classes
    u = 0
    for t in range(1, T + 2):
        if t == T + 1 or cl[t] != cl[u]:
            c["maxquiet"] = max(c["maxquiet"], t - 1 - u)
            c["quietfail"] += (t - 1 - u) > N
            u = t
    c["boundfail"] = int(T > 2 * M * (N + 2 * M) * (N + 1) + N)
    return c, N, M, n, T


def main():
    total = dict.fromkeys(NAMES + DESC, 0)
    for path in sys.argv[1:]:
        c, N, M, n, T = check(path)
        for k in total:
            total[k] = max(total[k], c[k]) if k.startswith("max") else total[k] + c[k]
        print(f"{os.path.basename(path)}: N {N} M {M} n {n} T {T} " + " ".join(f"{k} {c[k]}" for k in NAMES)
              + " | " + " ".join(f"{k} {c[k]}" for k in DESC))
    print(f"levelcheck ctrl {int(CTRL)}: genomes {len(sys.argv) - 1} " + " ".join(f"{k} {total[k]}" for k in NAMES)
          + " | " + " ".join(f"{k} {total[k]}" for k in DESC))
    if CTRL:
        return 0 if total["l2fail"] + total["l3fail"] + total["l5fail"] > 0 else 1
    return 0 if all(total[k] == 0 for k in NAMES) else 1


if __name__ == "__main__":
    sys.exit(main())
