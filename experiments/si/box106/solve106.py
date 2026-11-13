#!/usr/bin/env python3
"""L-SI box 106 §3.4: solve one cnf106 query and keep its certificate.
Usage: solve106.py LEN TAG [--genome FILE.json] [--solver cadical153|glucose4]
  Builds cnf106.build(LEN) («some G* in 𝓛*_2 has L* >= LEN»); with --genome the genome's free data are added as UNIT CLAUSES (so a proof
  refers to the DIMACS file alone). Writes dump/TAG.cnf (DIMACS); solves with pysat's solver (version printed) with proof output;
  on UNSAT writes dump/TAG.drup; on SAT decodes the model into a genome (ladder105's «state» format) best/TAG.json and replays it with
  mg106.abstract_run (L* of the abstract run) — the N5 replay is val105.py's job (run106.sh).
Output: one line «SOLVE106 TAG L* >= LEN [genome …]: SAT|UNSAT | vars V clauses C | cnf sha1 … | solver … | t s [| proof lines …, sha1 …]
[| decoded L* (mg106) …]»."""
import sys, os, json, time, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "box105"))
import cnf106 as C
from pysat.solvers import Solver
import pysat

def units_of(E, st):
    import aud106
    return aud106.assumptions(E, st)

def decode(E, model):
    m = set(l for l in model if l > 0); val = lambda name: E.names[name] in m
    xt = []
    for q in range(8):
        t = [j for j in range(5) if val(("XT", q, j))]; assert len(t) == 1; xt.append(-1 if t[0] == 4 else t[0])
    def below(c, d): return val(("ORD", c, d)) if c < d else not val(("ORD", d, c))
    rank_order = sorted(range(16), key=lambda c: sum(1 for d in range(16) if d != c and below(d, c)))
    for a, b in zip(rank_order, rank_order[1:]): assert below(a, b)
    rank = [0] * 16
    for r, c in enumerate(rank_order): rank[c] = r
    def gb(q, r): return val(("GO", q, r)) if q < r else not val(("GO", r, q))
    g0 = sorted(range(4), key=lambda q: sum(1 for r in range(4) if r != q and gb(r, q)))
    gate = [0] * 8
    for r, q in enumerate(g0): gate[q] = r
    for q in range(4, 8): gate[q] = q      # level-1 gates: only their relative position to nothing matters (box 106 §1)
    par = [int(val(("PAR", c))) for c in range(16)]
    start = [int(val(("R", 0, x))) for x in range(4)]
    return {"xt": xt, "gate": gate, "rank": rank, "par": par, "start": start}

def main():
    LEN, tag = int(sys.argv[1]), sys.argv[2]; args = sys.argv[3:]
    gfile = args[args.index("--genome") + 1] if "--genome" in args else None
    sname = args[args.index("--solver") + 1] if "--solver" in args else "cadical153"
    os.makedirs("dump", exist_ok=True); os.makedirs("best", exist_ok=True)
    E = C.build(LEN)
    if gfile:
        st = json.load(open(gfile))["state"]
        for a in units_of(E, st): E.add([a])
    path = "dump/%s.cnf" % tag
    C.dimacs(E, path, ["L-SI box 106 cnf106.py: some G* in L*_2 has L* >= %d%s (CTRL %d)" % (LEN, " ; genome %s as unit clauses" % os.path.basename(gfile) if gfile else "", C.CTRL)])
    sha = hashlib.sha1(open(path, "rb").read()).hexdigest()
    t0 = time.time(); s = Solver(name=sname, with_proof=True, bootstrap_with=E.cl); r = s.solve(); dt = time.time() - t0
    out = "SOLVE106 %s L* >= %d%s%s: %s | vars %d clauses %d | cnf sha1 %s | solver %s (python-sat %s) | %.1f s" % (
        tag, LEN, " genome %s" % os.path.basename(gfile) if gfile else "", " CTRL %d" % C.CTRL if C.CTRL else "",
        "SAT" if r else "UNSAT", E.n, len(E.cl), sha, sname, pysat.__version__, dt)
    if not r:
        pf = s.get_proof() or []; pp = "dump/%s.drup" % tag
        with open(pp, "w") as f:
            for line in pf: f.write(line + "\n")
        out += " | proof lines %d sha1 %s" % (len(pf), hashlib.sha1(open(pp, "rb").read()).hexdigest())
    else:
        st = decode(E, s.get_model()); json.dump({"mode": "free", "d": 2, "state": st, "L": None}, open("best/%s.json" % tag, "w"))
        import mg106 as MG
        G, pb, pe = MG.gp(st); run = MG.abstract_run(G, pb, pe)
        mrun = [tuple(int(E.names[("R", j, x)] in set(l for l in s.get_model() if l > 0)) for x in range(4)) for j in range(LEN + 1)]
        out += " | decoded L* (mg106) %d | model run = mg106 run prefix %s" % (len(run) - 1, mrun == [tuple(t) for t in run[:LEN + 1]])
    print(out, flush=True)

main()
