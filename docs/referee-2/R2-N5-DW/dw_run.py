#!/usr/bin/env python3
r"""REFEREE-2 successor 20: on a game file (S3 start, SPEC S3 = Engine.initial('best') both sides), run MY N5-SF (R2-N5-SF/sf_check.run_sf on
si.py) and MY plain N5 (R2-N5-DUAL/dual_check.Runner on si.py). Print iterations, #sigma - 1, SBC_sigma, LAM_sigma (on the distinct-sigma
sequence, as P-N5-SF §0), the same for tau, fallback counts, and the final lambda-parity regions of both (for the WIN check against Oink).
Usage: dw_run.py game.pg [sf|n5|both]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-SF")); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-DUAL"))
import sf_check as SF
import dual_check as DC
pg, Engine, dual = DC.pg, DC.Engine, DC.dual
g = pg.read(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else "both"; n = g.n
s0, t0 = list(Engine(g).initial("best")), list(Engine(dual(g)).initial("best"))
def regions(states):
    E = Engine(g); xe, _ = E.evaluate(tuple(states[-1][0][v] if g.owner[v] == 0 else -1 for v in range(n)))
    return "".join("E" if g.prio[x[0]] % 2 == 0 else "O" for x in xe)
if mode in ("sf", "both"):
    SE, SO = SF.Side(g), SF.Side(dual(g))
    st, fbs = SF.run_sf(g, SE, SO, s0, t0)
    def side(S, seq):
        d = SF.dedup([SF.own(S.X, x) for x in seq]); reps = []
        prev = None
        for x in seq:
            o = SF.own(S.X, x)
            if o != prev: reps.append(list(x)); prev = o
        inf = [S.info(r) for r in reps]
        sbc = sum(inf[j + 1][2] != inf[j][2] for j in range(len(inf) - 1))
        lam = sum([z[0] for z in inf[j + 1][0]] != [z[0] for z in inf[j][0]] for j in range(len(inf) - 1))
        return len(d) - 1, sbc, lam
    pE, sbE, lamE = side(SE, [x for x, _ in st]); pO, sbO, lamO = side(SO, [y for _, y in st])
    print(f"SF n {n} iterations {len(st)-1} sigma_changes {pE} SBC_sigma {sbE} LAM_sigma {lamE} tau_changes {pO} SBC_tau {sbO} LAM_tau {lamO} "
          f"fallbacks_E {sum(f==1 for f in fbs)} fallbacks_O {sum(f==2 for f in fbs)}")
    print("SF_REGIONS", regions(st))
if mode in ("n5", "both"):
    st, fbs = DC.Runner(g).run(list(s0), list(t0))
    print(f"N5 n {n} iterations {len(st)-1} fallbacks {sum(1 for f in fbs if f)}")
    print("N5_REGIONS", regions(st))
