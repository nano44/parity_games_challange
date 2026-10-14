#!/usr/bin/env python3
"""CEGAR search for a weak (n,d)-separator with exactly k states (convention E), own encoding (enc.py), own checker.
Usage: search.py n d k [--solver cadical153] [--cnf-out FILE] [--assume a,b,...]
  SAT: prints the automaton (re-verified by check.py against the full graph family).
  UNSAT: prints the graph subset used; with --cnf-out writes the final CNF (that subset) for proof generation.
  --assume q:a:x,...  fixes delta(q, a) = x (x = k for bottom) as unit clauses (cube-and-conquer)."""
import sys, os, time, json, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import graphs, enc, check
from pysat.solvers import Solver


def run(n, d, k, solver="cadical153", cnf_out=None, assume=(), log=print, init_graphs=None, extra=(), w2="rank"):
    evens, odds = graphs.family(n, d, 0), graphs.family(n, d, 1)
    e = enc.Encoding(n, d, k)
    e.binary = (w2 == "binary")
    for (q, a, x) in assume:
        e.add([e.t[q][a - 1][x]])
    for cl in extra:  # clauses over transition literals ('t', q, a, x)
        e.add([e.t[q][a - 1][x] for (_, q, a, x) in cl])
    used = set(init_graphs or [])
    for kind, gi in used:
        (e.add_even if kind == "even" else e.add_odd)((evens if kind == "even" else odds)[gi])
    S = Solver(name=solver, bootstrap_with=e.clauses)
    nsent = len(e.clauses)
    t0, rounds = time.time(), 0
    lassos = []
    while True:
        rounds += 1
        if not S.solve():
            log(f"UNSAT n={n} d={d} k={k} w2={w2} assume={list(assume)} rounds={rounds} graphs={len(used)} lassos={len(lassos)} vars={e.nv} "
                f"clauses={len(e.clauses)} {time.time()-t0:.1f}s")
            if cnf_out:
                e.dimacs(cnf_out)
            S.delete()
            return None, sorted(used)
        aut = e.decode(S.get_model())
        bad = check.violations(aut, evens, odds)
        if not bad:
            log(f"SAT n={n} d={d} k={k} w2={w2} {time.time()-t0:.1f}s rounds={rounds} lassos={len(lassos)} {json.dumps(aut)}")
            S.delete()
            return aut, sorted(used)
        if w2 == "lasso":  # noqa (binary uses the graph branch below)
            badE = [b for b in bad if b[0] == "even" and b not in used][:3]
            badO = [b for b in bad if b[0] == "odd"][:6]
            for kind, gi in badE:
                e.add_even(evens[gi]); used.add((kind, gi))
            nl = 0
            for kind, gi in badO:
                las = check.odd_lasso(aut, odds[gi])
                assert las is not None and check.accepts_lasso(aut, *las)
                enc.add_reject_lasso(e, *las); nl += 1
                lassos.append(las)
            assert badE or nl, "checker rejects but nothing to add"
        else:
            add = [b for b in bad if b not in used][:3]
            assert add, "checker rejects but all violated graphs are already encoded: encoding bug"
            for kind, gi in add:
                (e.add_even if kind == "even" else e.add_odd)((evens if kind == "even" else odds)[gi])
                used.add((kind, gi))
        for c in e.clauses[nsent:]:
            S.add_clause(c)
        nsent = len(e.clauses)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("n", type=int); ap.add_argument("d", type=int); ap.add_argument("k", type=int)
    ap.add_argument("--solver", default="cadical153"); ap.add_argument("--cnf-out")
    ap.add_argument("--assume", default="")
    ap.add_argument("--w2", choices=["rank", "lasso", "binary"], default="rank")
    a = ap.parse_args()
    assume = [tuple(map(int, x.split(":"))) for x in a.assume.split(",") if x]
    aut, used = run(a.n, a.d, a.k, a.solver, a.cnf_out, assume, w2=a.w2)
    print("GRAPHS", json.dumps(used))
