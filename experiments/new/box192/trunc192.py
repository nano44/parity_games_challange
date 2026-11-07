#!/usr/bin/env python3
r"""Box 192: check TRUNC-CHOICE: at a gate g with Lambda(e_g) = Lambda(beta_g) = w and e_g more relevant than w,
Odd's optimal choice is e iff trunc_{>e_g}(Pi(B)) beats trunc_{>e_g}(Pi(A)) for Even, where trunc keeps the path-set bits above rank(e_g);
on truncated equality: e_g in Pi(A)\Pi(B) => beta. Also count per-vertex value changes (all vertices) and truncated changes."""
import sys, os, json
ROOT = "/home/user/parity_games_challange"
sys.path.insert(0, os.path.join(ROOT, "experiments/new/box191")); sys.path.insert(0, os.path.join(ROOT, "experiments/new/box189"))
import idealcyc, gamma3

def run(G):
    h, s0, movers, inv = idealcyc.build(G); E = idealcyc.Engine(h); st = idealcyc.run(G)
    _, _, _, V = gamma3.build(G, set()); name = {v: k for k, v in V.items()}
    gi = {}
    for x in range(G["N"]):
        for v in h.succ[movers[x]]: gi[(x, inv[v])] = v
    gates = [v for v in range(h.n) if h.owner[v] == 1 and name[v][0] == "g"]
    ok = bad = tie = 0; hist = []
    for s in st:
        cur = list(s0)
        for x in range(G["N"]): cur[movers[x]] = gi[(x, s[x])]
        vs, sb = E.evaluate(tuple(cur)); hist.append(vs)
        for gv in gates:
            q = name[gv][1]; e, b = V[("e", q)], V[("b", q)]
            A, B = vs[e], vs[b]
            if A[0] != B[0] or E.rank[e] <= E.rank[A[0]]: continue
            hi = ~((1 << (E.rank[e] + 1)) - 1)
            ta, tb = A[1] & hi, B[1] & hi
            wa, wb = E.weight(ta), E.weight(tb)
            if wa != wb: pred = e if wb > wa else b
            else:
                tie += 1; pred = b if (A[1] >> E.rank[e]) & 1 and not (B[1] >> E.rank[e]) & 1 else None
            if pred is None: continue
            if pred == sb[gv]: ok += 1
            else: bad += 1
    # per-vertex distinct values
    n = h.n; ch = [sum(1 for t in range(1, len(hist)) if hist[t][v] != hist[t - 1][v]) for v in range(n)]
    mv = max(ch[x] for x in movers)
    return len(st) - 1, ok, bad, tie, mv

if __name__ == "__main__":
    for f in sys.argv[1:]:
        G = json.load(open(f)); T, ok, bad, tie, mv = run(G)
        print(f"{os.path.basename(f)} N {G['N']} T {T} TRUNC-CHOICE ok {ok} bad {bad} (trunc-ties {tie}); max mover value changes {mv}")
