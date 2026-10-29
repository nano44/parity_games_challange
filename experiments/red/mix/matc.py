#!/usr/bin/env python3
"""L-RED successor 30: matched P-changes (#MAT, R85 MATCHED) and carries (NM) per vertex per lambda-run on an N5 run (n5b SPEC),
written from RESULTS R85's definition (not from L-SI's carx.py). SIDE=E (default): Even's Xi_sigma on G; SIDE=O: Odd's Xi_tau on G^d.
lambda-run = maximal run of states with the cycle-node map constant. For each transition inside a run and each vertex x with the
same cycle node c and P_t != P_(t+1): w(r) = +(r - rank c) for even ranks, -(r - rank c) for odd ranks; MATCHED iff a matching
M of out = A\\B to in = B\\A with w(i) > w(o) covers every odd incoming and every even outgoing rank (Mendelsohn-Dulmage: two
one-sided matchings suffice). Prints the top vertices by #MAT and by NM, with n. Usage: matc.py GAME.pg [START]"""
import sys, os
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
sys.path.insert(0, R + "/experiments/n5-second"); sys.path.insert(0, R + "/experiments/hard-families"); sys.path.insert(0, R + "/experiments/harness")
import n5b, pg

def covers(left, right, ok, need):
    """Is there a matching left -> right (edges ok(l, r)) covering every l in need?"""
    match = {}
    def aug(l, seen):
        for r in right:
            if ok(l, r) and r not in seen:
                seen.add(r)
                if r not in match or aug(match[r], seen):
                    match[r] = l; return True
        return False
    return all(aug(l, set()) for l in need)

def matched(A, B, w, odd):
    out, inn = sorted(A - B), sorted(B - A)
    need_out = [o for o in out if not odd(o)]; need_in = [i for i in inn if odd(i)]
    return covers(out, inn, lambda o, i: w(i) > w(o), need_out) and covers(inn, out, lambda i, o: w(i) > w(o), need_in)

def main():
    g = pg.read(sys.argv[1]); s0, t0 = n5b.read_start(sys.argv[2], g) if len(sys.argv) > 2 else (None, None)
    side = os.environ.get("SIDE", "E")
    N = n5b.N5(g, mode="spec"); tr = []; N.run(s0, t0, trace=tr)
    si = N.SG if side == "E" else N.SD; gg = si.g
    rank = {v: r for r, v in enumerate(sorted(range(g.n), key=lambda v: (gg.prio[v], v)))}
    odd = lambda v: gg.prio[v] % 2 == 1
    U = [si.evaluate(list(st[0] if side == "E" else st[1])) for st in tr]
    lam = [tuple(u[v][0] for v in range(g.n)) for u in U]
    runs = [0] + [k + 1 for k in range(len(U) - 1) if lam[k + 1] != lam[k]] + [len(U)]
    rows = []
    for a, b in zip(runs, runs[1:]):
        mat = [0] * g.n; car = [0] * g.n
        for t in range(a, b - 1):
            for x in range(g.n):
                (c, A, _), (c2, B, _) = U[t][x], U[t + 1][x]
                if c != c2 or A == B: continue
                rc = rank[c]; w = lambda v: (rank[v] - rc) if not odd(v) else -(rank[v] - rc)
                if matched(set(A), set(B), w, odd): mat[x] += 1
                else: car[x] += 1
        for x in range(g.n):
            if mat[x] or car[x]: rows.append((mat[x], car[x], x, a, b))
    print(f"MATC {os.path.basename(sys.argv[1])} side {side} n {g.n} states {len(tr)} lambda-runs {len(runs) - 1}")
    print("  top #MAT: " + " ".join(f"v{x}:{m}/{c}@[{a},{b})" for m, c, x, a, b in sorted(rows, reverse=True)[:6]))
    print("  top NM:   " + " ".join(f"v{x}:{c}/{m}@[{a},{b})" for m, c, x, a, b in sorted(rows, key=lambda r: (-r[1], -r[0]))[:6]))
    mx = max((r[0] for r in rows), default=0); print(f"  max #MAT {mx}  max #MAT / n {mx / g.n:.3f}")

if __name__ == "__main__":
    main()
