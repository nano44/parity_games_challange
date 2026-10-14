#!/usr/bin/env python3
"""Cube-and-conquer for 'is there a k-state weak (n,d)-separator?' Splits on delta(0, 1..L).
Cubes: every assignment of delta(0,a), a = 1..L, to {bottom, 0, 1, ..., m+1} where m is the largest state used so far
(states first reached from 0 get the next free number: implied by the BFS symmetry breaking of enc.py). Values larger
than m+1 contradict BFS numbering and are covered by one extra 'rest' cube per position (asserting
delta(0,a) in {m+2..k-1}), so the cubes cover all assignments. Each cube is solved by search.run (CEGAR, own encoder,
checker re-verification); UNSAT cubes write their CNF (with the cube as unit / clause constraints) for proof generation.
Usage: cube.py n d k L [--jobs 4]    -> out/cubes_n{n}_d{d}_k{k}/cube_XX.{cnf,log}, summary on stdout."""
import sys, os, json, time, argparse
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import search


def cubes(k, L):
    """Yields lists of constraints: ('eq', a, x) or ('in', a, [xs])."""
    def rec(a, m, acc):
        if a > L:
            yield acc; return
        for x in [k, *range(0, min(m + 2, k))]:  # k = bottom
            m2 = max(m, x) if x < k else m
            yield from rec(a + 1, m2, acc + [("eq", a, x)])
        rest = list(range(m + 2, k))
        if rest:
            yield acc + [("in", a, rest)]  # BFS-violating; expected trivially UNSAT
    yield from rec(1, 0, [])


def solve_cube(args):
    n, d, k, idx, cube, outdir = args
    base = os.path.join(outdir, f"cube_{idx:03d}")
    log = open(base + ".log", "w")
    eqs = [(0, a, x) for (kind, a, x) in cube if kind == "eq"]
    ins = [(a, xs) for (kind, a, xs) in cube if kind == "in"]
    t = time.time()
    # 'in' constraints are passed as extra clauses through the encoding hook
    aut, used = search.run(n, d, k, cnf_out=base + ".cnf", assume=eqs, log=lambda s: log.write(s + "\n"),
                           extra=[[("t", 0, a, x) for x in xs] for (a, xs) in ins])
    log.write(json.dumps({"cube": cube, "sat": aut is not None, "aut": aut, "graphs": used, "s": time.time() - t}) + "\n")
    log.close()
    return idx, cube, aut, time.time() - t


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("n", type=int); ap.add_argument("d", type=int); ap.add_argument("k", type=int); ap.add_argument("L", type=int)
    ap.add_argument("--jobs", type=int, default=4)
    a = ap.parse_args()
    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out", f"cubes_n{a.n}_d{a.d}_k{a.k}")
    os.makedirs(outdir, exist_ok=True)
    cs = list(cubes(a.k, a.L))
    print(f"{len(cs)} cubes", flush=True)
    t0 = time.time(); found = None
    with Pool(a.jobs) as pool:
        for idx, cube, aut, s in pool.imap_unordered(solve_cube, [(a.n, a.d, a.k, i, c, outdir) for i, c in enumerate(cs)]):
            print(f"cube {idx} {'SAT' if aut else 'UNSAT'} {s:.0f}s {cube}", flush=True)
            if aut:
                found = aut; print("FOUND", json.dumps(aut), flush=True); pool.terminate(); break
    print(f"RESULT n={a.n} d={a.d} k={a.k}: {'SAT' if found else 'all cubes UNSAT'} ({time.time()-t0:.0f}s)")
