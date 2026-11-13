#!/usr/bin/env python3
"""L-SI box 106 §3.3 audit of cnf106.py against mg106.py (the audited mover-game evaluator, §2):
for random free genomes of 𝓛*_2 (ladder105's generator) the free data are fixed by assumptions in the CNF without the length constraint;
counters (must be 0): avfail (unit (genome, state, mover): the CNF model's AV bit differs from mg106's), avfree (unit (genome, state,
mover): the opposite AV bit is also satisfiable, i.e. the CNF does not determine it), runfail (unit genomes: R[0..6] differs from
mg106.abstract_run's states, padded with the last), unsat (genomes whose free data have no model).
Usage: aud106.py SEED COUNT [--full]   (--full: the avfree test, 64 extra solves per genome)
       aud106.py json [--full] FILE.json...   (genomes saved by mg106.py climb / ladder105.py: {"state": st, ...})"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "box105"))
import cnf106 as C
import mg106 as MG, ladder105 as LD
from pysat.solvers import Solver

def assumptions(E, st):
    a = []
    for q in range(8):
        t = st["xt"][q]; t = 4 if t == -1 else t
        for j in range(5): a.append(E.names[("XT", q, j)] * (1 if j == t else -1))
    g = st["gate"]
    for q in range(4):
        for r in range(q + 1, 4): a.append(E.names[("GO", q, r)] * (1 if g[q] < g[r] else -1))
    rk, par = st["rank"], st["par"]
    for c in range(16):
        a.append(E.names[("PAR", c)] * (1 if par[c] else -1))
        for d in range(c + 1, 16): a.append(E.names[("ORD", c, d)] * (1 if rk[c] < rk[d] else -1))
    for x in range(4): a.append(E.names[("R", 0, x)] * (1 if st["start"][x] else -1))
    return a

def main():
    full = "--full" in sys.argv
    if sys.argv[1] == "json":
        import json
        files = [f for f in sys.argv[2:] if f != "--full"]; sts = [json.load(open(f))["state"] for f in files]
        seed, count = "json", len(sts); gen = iter(sts)
    else:
        seed, count = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed); gen = None
    E = C.build(None)
    sol = Solver(name="cadical195", bootstrap_with=E.cl)
    c = dict(avfail=0, avfree=0, runfail=0, unsat=0); units = 0; mx = 0; first = None
    for i in range(count):
        st = next(gen) if gen else LD.init(rng, 2); G, pb, pe = MG.gp(st); a = assumptions(E, st)
        if not sol.solve(assumptions=a): c["unsat"] += 1; continue
        m = set(l for l in sol.get_model() if l > 0)
        for s in C.STATES:
            mg = MG.mg_values(G, pb, pe, s)
            for x in range(4):
                units += 1; want = mg[(x, 1 - s[x])] > mg[(x, s[x])]; v = E.names[("AV", s, x)]
                if (v in m) != want:
                    c["avfail"] += 1; first = first or (i, s, x)
                if full and sol.solve(assumptions=a + [(-v if want else v)]):
                    c["avfree"] += 1; first = first or (i, s, x, "free")
        run = MG.abstract_run(G, pb, pe); mx = max(mx, len(run) - 1)
        run = (run + [run[-1]] * 7)[:7]
        got = [tuple(int(E.names[("R", j, x)] in m) for x in range(4)) for j in range(7)]
        if got != [tuple(s) for s in run]: c["runfail"] += 1; first = first or (i, "run")
    print("AUD106 seed %s genomes %d%s%s: (genome, state, mover) units %d avfail %d avfree %s runfail %d unsat %d | max L* %d%s" % (
        seed, count, " CTRL %d" % C.CTRL if C.CTRL else "", " full" if full else "", units, c["avfail"], c["avfree"] if full else "-",
        c["runfail"], c["unsat"], mx, "" if first is None else " | first %s" % (first,)))

main()
