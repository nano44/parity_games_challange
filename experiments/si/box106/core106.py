#!/usr/bin/env python3
"""L-SI box 106 §3d, step 1 (SEARCH; no certificate here): the cores of the query «some G* in 𝓛*_2 has L* >= LEN».
A CORE is a short list of availability literals (σ, x, bit) that NO genome realises (the AV-CNF cnf106.build(None, states=the core's
states, run=False) plus the core's units is UNSAT). Loop (counterexample-guided):
  1. RUN-CNF = cnf106.build_run(LEN, cores): GO, the KEY run with L* >= LEN, AV FREE, every known core forbidden. UNSAT: stop (the
     cores cover the query: every run of length >= LEN needs some core).
  2. SAT: read the run's states R[0..LEN-1] and the AV bits used there (all 4 movers at each visited state) = a PATTERN.
  3. Solve the AV-CNF of the pattern's states with the pattern as assumptions. SAT: a genome realises the pattern: with the RUN model's
     start and gate order it has L* >= LEN: decoded to best/kill106_<i>.json and the loop STOPS (a kill candidate of KEY2-5; replay on
     N5 is run106.sh's job). UNSAT: the solver's core, minimised by deletion (each literal dropped if the rest stays UNSAT), is added.
Solver: python-sat «cadical195» (search only; every core and the coverage are certified separately with Glucose 4 DRUP, cert step).
Resumable: cores in out/cores106_L<LEN>.json (rewritten after each core); one line per core in out/core106_L<LEN>.out.
Usage: core106.py LEN"""
import sys, os, json, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "box105"))
import cnf106 as C
from pysat.solvers import Solver

def av_cnf(states):
    return C.build(None, states=sorted(set(tuple(s) for s in states)), run=False)

def main():
    LEN = int(sys.argv[1]); jf = "out/cores106_L%d.json" % LEN; of = "out/core106_L%d.out" % LEN
    cores = json.load(open(jf)) if os.path.exists(jf) else []
    while True:
        t0 = time.time(); R = C.build_run(LEN, cores); s = Solver(name="cadical195", bootstrap_with=R.cl); r = s.solve()
        if not r:
            print("CORE106 L* >= %d: RUN-CNF with %d cores UNSAT (covered) | %.1f s" % (LEN, len(cores), time.time() - t0), flush=True); return
        m = set(l for l in s.get_model() if l > 0); s.delete()
        states = [tuple(int(R.names[("R", j, x)] in m) for x in range(4)) for j in range(LEN + 1)]
        pat = [(list(S), x, int(R.names[("AV", S, x)] in m)) for S in sorted(set(states[:LEN])) for x in range(4)]
        E = av_cnf([p[0] for p in pat]); lit = lambda p: E.names[("AV", tuple(p[0]), p[1])] * (1 if p[2] else -1)
        sv = Solver(name="cadical195", bootstrap_with=E.cl)
        if sv.solve(assumptions=[lit(p) for p in pat]):
            import solve106
            go = {(q, rr): R.names[("GO", q, rr)] in m for q in range(4) for rr in range(q + 1, 4)}
            st = solve106.decode_av(E, sv.get_model(), states[0], go)
            k = len([f for f in os.listdir("best") if f.startswith("kill106_L%d_" % LEN)]); fn = "best/kill106_L%d_%d.json" % (LEN, k)
            json.dump({"mode": "free", "d": 2, "state": st, "L": None}, open(fn, "w"))
            print("CORE106 L* >= %d: PATTERN REALISED (kill candidate) %s states %s | written %s" % (LEN, pat, states, fn), flush=True); sys.exit(7)
        core = [l for l in sv.get_core()]; inv = {v: k for k, v in E.names.items()}
        cur = list(core)
        for l in list(core):
            if l not in cur: continue
            trial = [x for x in cur if x != l]
            if not sv.solve(assumptions=trial): cur = [x for x in sv.get_core() if x in trial] or trial
        sv.delete()
        cr = sorted([(list(inv[abs(l)][1]), inv[abs(l)][2], int(l > 0)) for l in cur])
        cores.append(cr); json.dump(cores, open(jf + ".tmp", "w")); os.replace(jf + ".tmp", jf)
        line = "CORE106 L* >= %d core %d: %s | from run %s | %.1f s" % (LEN, len(cores), " ".join("%sAV[%s][%d]" % ("" if b else "¬", "".join(map(str, S)), x) for S, x, b in cr),
                                                                       " ".join("".join(map(str, S)) for S in states), time.time() - t0)
        open(of, "a").write(line + "\n"); print(line, flush=True)

if __name__ == "__main__":
    main()
