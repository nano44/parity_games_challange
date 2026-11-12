#!/usr/bin/env python3
"""L-SI P-N5-GATE fixes entry 3, item D-4 (REFEREE 31): the copy rows of box 94 re-measured as SETS. For each level j >= 2 of a nested
genome (gennest94 names v, Q, R with prefix l<j>_), copy_j := [S(R_j) == S(R_(j-1))] as sets of steps (S(x) := steps t with the value of x
changed), next to |S(R_j)|. Engines and the level / name maps are box94/lev94.py's (its code up to its argument parsing, copied verbatim
below the header; lev94.py compares SIZES only). Usage: copy95.py own|g3 G.json NAMES.json ..."""

import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "box91")); import mult91
def g3_with_map(G, cap=20000):
    R = os.environ["ROOT"]; os.environ.setdefault("EG195_ROOT", R)
    sys.path[:0] = [os.path.join(R, p) for p in ("experiments/new/box195", "experiments/new/box191", "experiments/new/box189",
                    "experiments/new/box190", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
    import eg195, gamma3, n5v, n5x
    g0, _, _, V = gamma3.build(G, eg195.PADS); g = eg195.topg(g0)
    E_, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g)); sigma, tau = n5x.start_pair(g, E_, Ed, None); Hs = []
    while len(Hs) <= cap:
        vs, tb = E_.evaluate(tuple(sigma)); Hs.append((tuple(sigma), vs, tb))
        res = n5v.step(g, E_, Ed, sigma, tau, "xi")
        if res is None or res[4]: break
        sigma, tau = res[0], res[1]
    T = len(Hs) - 1
    val = lambda t, v: E_.key(Hs[t][1][v]); nx = lambda t, x: Hs[t][0][x] if g.owner[x] == 0 else Hs[t][2][x]
    return T, val, nx, (lambda x: V[("x", x)]), (lambda q: V[("g", q)])
def own_with_map(G):
    sys.path.insert(0, os.environ["OWN_DIR"]); import own
    T, n, nx, lam, E, rk, evs, odd2, val = mult91.eng_own(G); _, _, _, _, V, O = own.build(G)
    return T, val, nx, (lambda x: V[("x", x)]), (lambda q: V[("g", q)])

eng = sys.argv[1]; fs = sys.argv[2:]
for f, nf in zip(fs[0::2], fs[1::2]):
    G = json.load(open(f)); names = json.load(open(nf))
    T, val, nx, X, Gt = own_with_map(G) if eng == "own" else g3_with_map(G)
    S = lambda v: {t for t in range(1, T + 1) if val(t, v) != val(t - 1, v)}
    out = [f"{eng} {os.path.basename(f)} T {T}"]; j = 1; prev = None
    while True:
        p = "" if j == 1 else f"l{j}_"
        if p + "Q" not in names: break
        sr = S(X(names[p + "R"]))
        out.append(f"L{j} R {len(sr)}" + ("" if prev is None else f" copy {int(sr == prev)}"))
        prev = sr; j += 1
    print(" | ".join(out), flush=True)
