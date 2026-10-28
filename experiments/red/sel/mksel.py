#!/usr/bin/env python3
"""L-RED successor 23: Odd-minimum next-top selector (R94 design (a)). Two-way chain v_1..v_L (Even, low) between Odd selectors
x_L = v_0 and x_R = v_{L+1}. Stage values a_k = {H_1..H_k} (spine H_k -> H_{k-1} -> .. -> H_1 -> b, high even, ranks
H_1 > R_1 > H_2 > R_2 > .. > H_M > R_M > b). Stage k: Even y_k -> {H_k, R_k}; odd k on x_R, even k on x_L. R_k reads the far chain
end (odd k: v_L, even k: v_1), so y_k is Xi-improving exactly when the opposite stage value a_{k+1} has arrived, and then
R_k u a_{k+1} > a_{k+2}: x's minimum moves to y_{k+2}. Usage: mksel.py L M OUT.pg [--neg: R_k Odd-priority]  (writes OUT.start; tau = an Odd-optimal pair)"""
import sys, os, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "..", "..", "..")
sys.path.insert(0, os.path.join(ROOT, "experiments", "si")); sys.path.insert(0, os.path.join(ROOT, "experiments", "harness"))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new"))

def build(L, M, neg=False):
    order = []; own = {}; E = {}
    def add(nm, ow, succ): order.append(nm); own[nm] = ow; E[nm] = succ
    ch = lambda i: "xL" if i == 0 else ("xR" if i == L + 1 else "v%d" % i)
    for i in range(1, L + 1): add("v%d" % i, 0, [ch(i - 1), ch(i + 1)])
    add("xL", 1, ["y%d" % k for k in range(2, M + 1, 2)]); add("xR", 1, ["y%d" % k for k in range(1, M + 1, 2)])
    for k in range(1, M + 1): add("y%d" % k, 0, ["H%d" % k, "R%d" % k])
    add("b", 0, ["b"])
    for k in range(1, M + 1):
        add("H%d" % k, 0, ["b" if k == 1 else "H%d" % (k - 1)]); add("R%d" % k, 0, ["v%d" % L if k % 2 else "v1"])
    prio = {nm: 1 for nm in order}
    hi = ["b"] + sum([["R%d" % k, "H%d" % k] for k in range(M, 0, -1)], [])
    for j, nm in enumerate(hi): prio[nm] = 2 + 2 * j + (1 if neg and nm.startswith("R") else 0)
    sigma = {"v%d" % i: ch(i + 1) for i in range(1, L + 1)}; sigma.update({"y%d" % k: "H%d" % k for k in range(1, M + 1)})
    return order, own, E, prio, sigma

def write(order, own, E, prio, sigma, tau, out):
    idx = {nm: i for i, nm in enumerate(order)}
    with open(out, "w") as f:
        f.write("parity %d;\n" % (len(order) - 1))
        for nm in order: f.write('%d %d %d %s "%s";\n' % (idx[nm], prio[nm], own[nm], ",".join(str(idx[x]) for x in E[nm]), nm))
    fs = {nm: E[nm][0] for nm in order if own[nm] == 0}; fs.update(sigma)
    ft = {nm: E[nm][0] for nm in order if own[nm] == 1}; ft.update(tau)
    with open(out[:-3] + ".start", "w") as f:
        f.write("SIGMA0 " + " ".join("%d:%d" % (idx[a], idx[b]) for a, b in sorted(fs.items(), key=lambda t: idx[t[0]])) + "\n")
        f.write("TAU0 " + " ".join("%d:%d" % (idx[a], idx[b]) for a, b in sorted(ft.items(), key=lambda t: idx[t[0]])) + "\n")
    return idx

def odd_optimal(order, own, E, prio, out):
    import pg
    from si import Engine
    from n5 import dual
    idx = {nm: i for i, nm in enumerate(order)}
    g = pg.Game([prio[nm] for nm in order], [own[nm] for nm in order], [[idx[x] for x in E[nm]] for nm in order])
    Ed = Engine(dual(g)); odd = [nm for nm in order if own[nm] == 1]
    for ch in itertools.product(*[E[nm] for nm in odd]):
        t = list(Ed.initial("best"))
        for nm, c in zip(odd, ch): t[idx[nm]] = idx[c]
        vt, _ = Ed.evaluate(tuple(t))
        if not Ed.improving(tuple(t), vt): return dict(zip(odd, ch))
    raise SystemExit("no Odd-optimal tau found")

if __name__ == "__main__":
    L, M, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    order, own, E, prio, sigma = build(L, M, "--neg" in sys.argv)
    tau = odd_optimal(order, own, E, prio, out)
    idx = write(order, own, E, prio, sigma, tau, out)
    print(out, "n", len(order), "tau", tau)
