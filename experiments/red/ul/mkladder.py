#!/usr/bin/env python3
"""L-RED successor 22: the LADDER family against the long-phase side of L-NEW 28's QP_c (docs/new/N5-NCONF-box48.md §11-§12): ONE class S
(cycle node c_s, cycle c_s <-> u1 as in mkreader.py) holding k + 2 Odd gates that all disagree with tau during one long phase, and that are all
USED: x climbs a ladder of gated rungs g_1 .. g_k (sigma-bar(g_j) = c_s, tau(g_j) = the chain vertex v_{L+1-j} of class B), one rung per tick
of B's Bellman-Ford wave. Ranks: chain / gates / x low or as below; Xi(x via g_j) rises with j (gate ranks above c_s); W(x via g_j) = g_j + W(v):
received rungs carry G (top), the highest received rung wins. tau is Odd-optimal (Even's best reply to tau runs c_s -> q -> v_0 .. -> G).
ENT mode (mkladder.py k OUT.pg ent): the rungs live in class B and ENTER D during the phase: g_j -> {v_{L+1-j} (= tau), q}; while the
wave has not reached v_{L+1-j}, Odd's best reply sigma-bar(g_j) = tau(g_j) (o-level < q-level); once it has, sigma-bar(g_j) = q (q < G), so
g_j joins D at the wave's j-th tick (ENT = k). tau stays Odd-optimal (Even's best reply from q runs q -> v_0 .. -> G).
Usage: mkladder.py k OUT.pg [ent]   (L = k; writes OUT.pg and OUT.start)"""
import sys

def build(k, ent=False):
    L = k; V = {}; order = []
    def add(name, owner): V[name] = [len(V), owner]; order.append(name)
    low = ["v%d" % i for i in range(L + 1)] + ["u1", "x", "g0", "p0"]
    for nm in low: add(nm, 1 if nm in ("u1", "g0") else 0)
    mid = ["c_s", "b"]
    high = ["o%d" % i for i in range(L, -1, -1)] + ["ql", "q", "p1"] + ["g%d" % j for j in range(1, k + 1)] + ["G"]
    for nm in mid + high: add(nm, 1 if nm.startswith("g") else 0)
    E = {}
    for i in range(L): E["v%d" % i] = ["o%d" % i, "v%d" % (i + 1)]
    E["v%d" % L] = ["o%d" % L, "G"]
    for i in range(L + 1): E["o%d" % i] = ["b"]
    E.update({"ql": ["b"], "q": ["ql", "v0"], "p1": ["b"], "p0": ["b"], "G": ["b"], "b": ["b"],
              "c_s": ["u1", "q"], "u1": ["c_s", "p1"], "g0": ["c_s", "p0"], "x": ["g0"] + ["g%d" % j for j in range(1, k + 1)]})
    for j in range(1, k + 1): E["g%d" % j] = ["q" if ent else "c_s", "v%d" % (L + 1 - j)]
    prio = {}; p = 1
    for nm in low: prio[nm] = p; p += 1
    p += p % 2
    for nm in mid + high: prio[nm] = p; p += 2
    sigma = {"v%d" % i: "o%d" % i for i in range(L + 1)}; sigma.update({"q": "ql", "c_s": "u1", "x": "g0"})
    tau = {"u1": "p1", "g0": "p0"}; tau.update({"g%d" % j: "v%d" % (L + 1 - j) for j in range(1, k + 1)})
    return V, order, E, prio, sigma, tau

def main():
    k = int(sys.argv[1]); out = sys.argv[2]
    V, order, E, prio, sigma, tau = build(k, len(sys.argv) > 3 and sys.argv[3] == "ent"); idx = {nm: V[nm][0] for nm in order}
    with open(out, "w") as f:
        f.write("parity %d;\n" % (len(order) - 1))
        for nm in order: f.write("%d %d %d %s \"%s\";\n" % (idx[nm], prio[nm], V[nm][1], ",".join(str(idx[x]) for x in E[nm]), nm))
    fs = {nm: E[nm][0] for nm in order if V[nm][1] == 0}; fs.update(sigma)
    ft = {nm: E[nm][0] for nm in order if V[nm][1] == 1}; ft.update(tau)
    with open(out[:-3] + ".start", "w") as f:
        f.write("SIGMA0 " + " ".join("%d:%d" % (idx[a], idx[b]) for a, b in sorted(fs.items(), key=lambda t: idx[t[0]])) + "\n")
        f.write("TAU0 " + " ".join("%d:%d" % (idx[a], idx[b]) for a, b in sorted(ft.items(), key=lambda t: idx[t[0]])) + "\n")
    print(out, "n", len(order), {nm: idx[nm] for nm in ("c_s", "u1", "x", "g0", "b", "q", "v0", "G")})

if __name__ == "__main__":
    main()
