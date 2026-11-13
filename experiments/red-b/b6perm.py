#!/usr/bin/env python3
"""L-RED-B B6 attempt 2 (for the referees): does the run depend on anything but the orders P-N5-EXP §8 names?

§8 lists the ε (gate) comparisons the proof uses: inside a level, eps(u_j, o) < eps(v_j, o) for o = 0, 1; eps(E(j+1), 1) <
eps(wv_j, 0); eps(E(j+1), 0) < eps(wu_j, 0); eps(wire, 0) < eps(wire, 1); eps(u_0, 0) < eps(u_0, 1); eps(v_0, 1) < eps(u_0, 0) <
eps(v_0, 0). Everything else is free, including the order of a mover's own two gates when its two W-targets differ.
This script draws RANDOM LINEAR EXTENSIONS of the partial order those comparisons define (a random topological order of the
option set, so the gate numbers stay a bijection onto 0..M-1 and the genome stays a genome of R104's class), and, for each, a
BROKEN variant: the same relabeling with one listed comparison reversed (a random one, by swapping the two gate numbers).
  keep  (unit permutations): a relabeling that preserves every listed comparison gives T != 2^k - 2        (MUST BE 0)
  Reported, not constrained: brokeT = how many of the broken variants still give T = 2^k - 2, and the range of their T.
Control B6P_CTRL=1: the list is read with eps(u_j, o) > eps(v_j, o) (a wrong list), so the sampled relabelings are no longer the
rule's: keep must fire.
Usage: b6perm.py k count seed"""
import sys, os, random
import onep, gk
CTRL = os.environ.get("B6P_CTRL", "0")


def pairs(k, names, ix, G):
    """the comparisons of P-N5-EXP par. 8, as (option a, option b) meaning gate(a) < gate(b); options are (mover index, option)"""
    E = lambda j: f"e{j}" if j <= k - 2 else f"u{j}"
    P = []
    for j in range(1, k):
        for o in (0, 1):
            a, b = (ix[f"u{j}"], o), (ix[f"v{j}"], o)
            P.append((b, a) if CTRL == "1" else (a, b))
    for j in range(1, k - 1):
        P.append(((ix[E(j + 1)], 1), (ix[f"wv{j}"], 0)))
        P.append(((ix[f"wv{j}"], 0), (ix[f"wv{j}"], 1)))
    for j in range(2, k - 1):
        P.append(((ix[E(j + 1)], 0), (ix[f"wu{j}"], 0)))
        P.append(((ix[f"wu{j}"], 0), (ix[f"wu{j}"], 1)))
    P += [((ix["u0"], 0), (ix["u0"], 1)), ((ix["v0"], 1), (ix["u0"], 0)), ((ix["u0"], 0), (ix["v0"], 0))]
    return P


def run(k, cnt, seed):
    G, names = gk.build(k)
    ix = {n: i for i, n in enumerate(names)}
    P = pairs(k, names, ix, G)
    M = sum(len(o) for o in G["opts"])
    base = 2 ** k - 2
    rng = random.Random(seed)
    opts = [(x, o) for x in range(G["N"]) for o in range(len(G["opts"][x]))]
    succ = {q: [] for q in opts}
    indeg = {q: 0 for q in opts}
    for a_, b_ in P:                      # a_ must get the smaller gate number
        succ[a_].append(b_)
        indeg[b_] += 1

    def sample():
        """a random linear extension of the partial order: gate numbers 0, 1, ... in a random topological order"""
        deg = dict(indeg)
        ready = [q for q in opts if deg[q] == 0]
        gate = {}
        for i in range(len(opts)):
            j = rng.randrange(len(ready))
            ready[j], ready[-1] = ready[-1], ready[j]
            q = ready.pop()
            gate[q] = i
            for r in succ[q]:
                deg[r] -= 1
                if deg[r] == 0:
                    ready.append(r)
        return gate

    def T_of(gate):
        H = dict(G)
        H["gate"] = [[gate[(x, o)] for o in range(len(G["opts"][x]))] for x in range(G["N"])]
        return len(onep.OneP(H).run("key")) - 1

    bad = brokeT = 0
    mn, mx = 10 ** 9, -1
    for _ in range(cnt):
        gate = sample()
        assert all(gate[a_] < gate[b_] for a_, b_ in P)
        bad += int(T_of(gate) != base)
        a_, b_ = P[rng.randrange(len(P))]          # break exactly one listed comparison
        g2 = dict(gate)
        g2[a_], g2[b_] = gate[b_], gate[a_]
        T2 = T_of(g2)
        brokeT += int(T2 == base)
        mn, mx = min(mn, T2), max(mx, T2)
    print(f"G_{k} ctrl {CTRL} perms {cnt} seed {seed} base {base} keep {bad} brokeT {brokeT} broken_minT {mn} broken_maxT {mx} "
          f"listed_comparisons {len(P)}", flush=True)


if __name__ == "__main__":
    run(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
