#!/usr/bin/env python3
"""L-NEW box 188: independent replay of a candidate MOVES-2D kill with L-NEW's own tools.
(1) Membership, condition by condition, from RESULTS R104's definition of an IDEAL genome and R110's definition of L^R_d:
    N = 2d movers, lev(v) = v // 2 (levels 0..d-1, movers 2l, 2l+1 on level l), every mover of degree 2, option k of a mover of level
    l >= 1 W-pointing to 2(l-1)+k, no W-target at level 0, beta ranks distinct over all options, parities in {0, 1}, gate indices
    distinct over all options, every Xi-target a mover index or X (-1), no self-target, Xi-graph acyclic (Kahn), a start of length N.
(2) Runs with box150/check.py Gen (L-NEW's own IDEAL simulator): every start if N <= MAXN (default 12), else the stored start and the
    starts given on the command line. Reports T, moves(x) per mover (mu's unit: steps t with x in Mv_t, in one run), Z membership.
(3) Runs box187/movescheck.py's check_run on every replayed run (its counters must stay 0).
Usage: replay.py genome.json [start ...]   (run from anywhere; never copy the genome under experiments/new/box150-187)"""
import os, sys, json, itertools
H = os.path.dirname(os.path.abspath(__file__)); P0 = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": P0, "__name__": "lib"}; exec(open(P0).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
mc = {"__file__": os.path.join(H, "..", "box187", "movescheck.py"), "__name__": "lib"}
exec(open(mc["__file__"]).read().split("\nif __name__")[0], mc)
MAXN = int(os.environ.get("MAXN", "12"))

def membership(G):
    out = []; N = G.get("N"); ok = True
    def cond(name, val):
        nonlocal ok; ok &= bool(val); out.append("%s %s" % (name, "OK" if val else "FAIL"))
    cond("N_even", isinstance(N, int) and N >= 2 and N % 2 == 0)
    d = N // 2
    cond("levels", G["lev"] == [v // 2 for v in range(N)])
    cond("degree2", all(len(G["opts"][x]) == 2 for x in range(N)))
    cond("Wwiring", all(G["opts"][x][k][0] == (2 * (x // 2 - 1) + k if x >= 2 else -1) for x in range(N) for k in range(2)))
    br = [G["br"][G["opts"][x][k][2]] for x in range(N) for k in range(2)]
    cond("ranks_distinct", len(set(br)) == 2 * N)
    cond("beta_ids_distinct", len({G["opts"][x][k][2] for x in range(N) for k in range(2)}) == 2 * N)
    cond("parities", all(G["bp"][G["opts"][x][k][2]] in (0, 1) for x in range(N) for k in range(2)))
    gates = [G["gate"][x][k] for x in range(N) for k in range(2)]
    cond("gates_distinct", len(set(gates)) == 2 * N and all(len(G["gate"][x]) == 2 for x in range(N)))
    xt = [G["opts"][x][k][1] for x in range(N) for k in range(2)]
    cond("xt_range", all(t == -1 or (isinstance(t, int) and 0 <= t < N) for t in xt))
    cond("no_self_target", all(G["opts"][x][k][1] != x for x in range(N) for k in range(2)))
    indeg = [0] * N
    for x in range(N):
        for k in range(2):
            t = G["opts"][x][k][1]
            if t >= 0: indeg[t] += 1
    q = [v for v in range(N) if indeg[v] == 0]; seen = 0
    while q:
        v = q.pop(); seen += 1
        for k in range(2):
            t = G["opts"][v][k][1]
            if t >= 0:
                indeg[t] -= 1
                if indeg[t] == 0: q.append(t)
    cond("Xi_acyclic", seen == N)
    cond("start", len(G["start"]) == N and all(s in (0, 1) for s in G["start"]))
    return ok, d, out

def main():
    f = sys.argv[1]; G = json.load(open(f)); ok, d, out = membership(G)
    print("FILE", f); print("MEMBERSHIP", "L^R_%d IDEAL-ACYC" % d if ok else "FAIL", " ".join(out))
    if not ok: return
    g = Gen(G); N = G["N"]
    Z = {G["opts"][x][k][1] for x in range(N) for k in range(2)} - {-1}
    starts = list(itertools.product((0, 1), repeat=N)) if N <= MAXN else []
    starts += [tuple(G["start"])] + [tuple(int(c) for c in s) for s in sys.argv[2:]]
    for k in mc["C"]: mc["C"][k] = 0
    best = {}; Tmax = (0, None)
    for st in starts:
        S, _ = g.run(st); T = len(S) - 1; mc["check_run"](g, G, S)
        if T > Tmax[0]: Tmax = (T, st)
        for x in range(N):
            m = sum(S[t][x] != S[t - 1][x] for t in range(1, T + 1))
            if m > best.get(x, (-1,))[0]: best[x] = (m, T, "".join(map(str, st)))
    print("STARTS", len(starts), "(all)" if N <= MAXN else "(stored + given)", "Tmax", Tmax[0], "at", "".join(map(str, Tmax[1])))
    for x in range(N):
        m, T, st = best[x]
        print("MOVER %d level %d Xi-target %s max moves %d (run T %d, start %s)%s" % (x, x // 2, x in Z, m, T, st, "  > 2d = %d" % (2 * d) if m > 2 * d else ""))
    mu = max((best[x][0] for x in Z if x // 2 >= 1), default=0)
    print("MU (max moves of a Xi-target of level >= 1) %d ; 2d = %d ; %s" % (mu, 2 * d, "MOVES-2D VIOLATED" if mu > 2 * d else "no violation"))
    print("MOVESCHECK " + " ".join("%s %d" % kv for kv in mc["C"].items()))

if __name__ == "__main__":
    main()
