"""L-ALG succ. 9 (box 11, produced on Opus 5.5), (FIX-d) scoping: does L-RED's lagfam (experiments/red/lag/lagfam.py, d = 3D+14)
keep its growing steal depth when its priority levels are COLLAPSED to a fixed number of values?
Construction: build lagfam(D); renumber the vertex ids by (original priority, original id), so that the stable index order of
equal-priority vertices after collapsing is the original priority order; then map priorities:
  MODE clock : clock x_1..x_k -> 0                               (chainfam's "all x_j at 0", GAP-A-M §21b)
  MODE levels: every T_j -> pr(T_{-1}), every tau_j -> pr(tau_D)  (relay tops share one even value each)
  MODE both  : clock and levels
  MODE flat  : clock -> 0, and every T_j, tau_j -> pr(S) (relay tops and S share one even value)
  MODE flat2 : flat, but clock -> pr(b) (clock shares b/z's even value)
  MODE flat3 : flat2, and b, z, clock -> pr(S)
  MODE flat4 : flat2, and a -> pr(W);  flat5: flat2, and w, y, v, f -> pr(a);  flat6: flat2, and w, y, v, f -> pr(W)
  MODE flat7 : flat5, and W -> pr(a)
  MODE none  : only the id renumbering
Priorities are then compressed order- and parity-preserving (gaps closed, same rule as game.cpp renumber).
Usage: fixd_lagcollapse.py D MODE OUT.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "red", "lag"))
import lagfam


def collapse(D, mode):
    g = lagfam.build(D)
    names = {i: n for n, i in g.ids.items()}
    n = len(g.pr)
    order = sorted(range(n), key=lambda v: (g.pr[v], v))
    new = {v: i for i, v in enumerate(order)}
    pr = list(g.pr)
    k = sum(1 for nm in g.ids if nm.startswith("x"))
    if mode in ("clock", "both"):
        for j in range(1, k + 1): pr[g.ids[f"x{j}"]] = 0
    if mode in ("levels", "both") or mode.startswith("flat"):
        tt = g.pr[g.ids["T-1"]]; ta = g.pr[g.ids[f"tau{D}"]]
        if mode.startswith("flat"): tt = ta = g.pr[g.ids["S"]]
        for j in range(-1, D + 1):
            pr[g.ids[f"T{j}"]] = tt; pr[g.ids[f"tau{j}"]] = ta
    if mode.startswith("flat"):
        for j in range(1, k + 1): pr[g.ids[f"x{j}"]] = 0
    if mode in ("flat2", "flat3", "flat4", "flat5", "flat6", "flat7"):
        for j in range(1, k + 1): pr[g.ids[f"x{j}"]] = g.pr[g.ids["b"]]
    if mode == "flat4":
        pr[g.ids["a"]] = g.pr[g.ids["W"]]
    if mode in ("flat5", "flat7"):
        for j in range(-1, D + 1):
            for c in "wyvf": pr[g.ids[f"{c}{j}"]] = g.pr[g.ids["a"]]
    if mode == "flat6":
        for j in range(-1, D + 1):
            for c in "wyvf": pr[g.ids[f"{c}{j}"]] = g.pr[g.ids["W"]]
    if mode == "flat7":
        pr[g.ids["W"]] = g.pr[g.ids["a"]]
    if mode == "flat3":
        for nm in ("b", "z"): pr[g.ids[nm]] = g.pr[g.ids["S"]]
        for j in range(1, k + 1): pr[g.ids[f"x{j}"]] = g.pr[g.ids["S"]]
    # compress: walk distinct values ascending; parity change +1, same parity +2 (game.cpp renumber), start at parity of min
    vals = sorted(set(pr)); m = {}; cur = None
    for x in vals:
        if cur is None: cur = x % 2
        elif (x % 2) != (m[prev] % 2): cur = m[prev] + 1
        else: cur = m[prev] + 2
        m[x] = cur; prev = x
    P = [None] * n; O = [None] * n; E = [None] * n; L = [None] * n
    for v in range(n):
        i = new[v]; P[i] = m[pr[v]]; O[i] = g.ow[v]; E[i] = sorted(new[w] for w in g.out[v]); L[i] = names[v]
    return P, O, E, L


def write(P, O, E, L, path):
    with open(path, "w") as f:
        f.write(f"parity {len(P) - 1};\n")
        for i in range(len(P)):
            f.write(f"{i} {P[i]} {O[i]} {','.join(map(str, E[i]))} \"{L[i]}\";\n")


if __name__ == "__main__":
    D, mode, out = int(sys.argv[1]), sys.argv[2], sys.argv[3]
    P, O, E, L = collapse(D, mode); write(P, O, E, L, out)
    print(out, "n", len(P), "d", len(set(P)))
