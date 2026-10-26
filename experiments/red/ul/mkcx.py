#!/usr/bin/env python3
"""L-RED successor 22: construction against CONJECTURE C-ONCE_X (docs/si/N5-GCX-box21.md §4: X-migrations INTO a D-direct gate at most once
per vertex per C-interval). One class (cycle node b). Clock C1 = mkreader's Bellman-Ford chain v_0 .. v_L (wave from G back to v_0).
Rungs j = 0 .. k: Odd D-DIRECT gate d_j -> {h_j (sigma-bar), h'_j (tau)}, h_j -> {w_j, u_0}, h'_j -> w_j, w_j = v_{L+1-j} (j >= 1), w_0 = p0;
rank(h'_j) > rank(h_j), so Odd's best reply is h_j and the offset Delta(d_j) = w(h'_j) - w(h_j) is constant (both exits read w_j).
x -> {d_0 .. d_k}; Xi(x via d_j) jumps when the wave reaches w_j; rung weights rise with j, so x climbs one rung per tick: k X-migrations
into D-direct gates inside ONE C-interval. tau is Odd-optimal: Even's best reply from h_j escapes to u_0 of a slower chain C2 (u_0 .. u_L2,
top G2 above every h'), whose early values (o'-level) sit below C1's, so (h_j, u_0) is not Xi-improving during the run.
Usage: mkcx.py k OUT.pg"""
import sys

def build(k):
    L = k + 1; L2 = k + 6; V = {}; order = []
    def add(nm, ow): V[nm] = [len(V), ow]; order.append(nm)
    low = ["v%d" % i for i in range(L + 1)] + ["u%d" % i for i in range(L2 + 1)] + ["x"]
    for nm in low: add(nm, 0)
    high = ["b"] + ["op%d" % i for i in range(L2, -1, -1)] + ["p0"] + ["o%d" % i for i in range(L, -1, -1)]
    for j in range(k + 1): high += ["h%d" % j, "hp%d" % j]
    high += ["d%d" % j for j in range(k + 1)] + ["G", "G2"]
    for nm in high: add(nm, 1 if nm.startswith("d") else 0)
    E = {}
    for i in range(L): E["v%d" % i] = ["o%d" % i, "v%d" % (i + 1)]
    E["v%d" % L] = ["o%d" % L, "G"]
    for i in range(L2): E["u%d" % i] = ["op%d" % i, "u%d" % (i + 1)]
    E["u%d" % L2] = ["op%d" % L2, "G2"]
    for i in range(L + 1): E["o%d" % i] = ["b"]
    for i in range(L2 + 1): E["op%d" % i] = ["b"]
    E.update({"b": ["b"], "G": ["b"], "G2": ["b"], "p0": ["b"], "x": ["d%d" % j for j in range(k + 1)]})
    for j in range(k + 1):
        w = "p0" if j == 0 else "v%d" % (L + 1 - j)
        E["d%d" % j] = ["h%d" % j, "hp%d" % j]; E["h%d" % j] = [w, "u0"]; E["hp%d" % j] = [w]
    prio = {}; p = 1
    for nm in low: prio[nm] = p; p += 1
    p += p % 2
    for nm in high: prio[nm] = p; p += 2
    sigma = {"v%d" % i: "o%d" % i for i in range(L + 1)}; sigma.update({"u%d" % i: "op%d" % i for i in range(L2 + 1)})
    sigma.update({"x": "d0"}); sigma.update({"h%d" % j: E["h%d" % j][0] for j in range(k + 1)})
    tau = {"d%d" % j: "hp%d" % j for j in range(k + 1)}
    return V, order, E, prio, sigma, tau

def main():
    k = int(sys.argv[1]); out = sys.argv[2]
    V, order, E, prio, sigma, tau = build(k); idx = {nm: V[nm][0] for nm in order}
    with open(out, "w") as f:
        f.write("parity %d;\n" % (len(order) - 1))
        for nm in order: f.write("%d %d %d %s \"%s\";\n" % (idx[nm], prio[nm], V[nm][1], ",".join(str(idx[x]) for x in E[nm]), nm))
    fs = {nm: E[nm][0] for nm in order if V[nm][1] == 0}; fs.update(sigma)
    ft = {nm: E[nm][0] for nm in order if V[nm][1] == 1}; ft.update(tau)
    with open(out[:-3] + ".start", "w") as f:
        f.write("SIGMA0 " + " ".join("%d:%d" % (idx[a], idx[b]) for a, b in sorted(fs.items(), key=lambda t: idx[t[0]])) + "\n")
        f.write("TAU0 " + " ".join("%d:%d" % (idx[a], idx[b]) for a, b in sorted(ft.items(), key=lambda t: idx[t[0]])) + "\n")
    print(out, "n", len(order), {nm: idx[nm] for nm in ("x", "d0", "d1", "b", "G", "G2", "u0", "v0")})

if __name__ == "__main__":
    main()
