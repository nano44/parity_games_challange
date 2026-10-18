#!/usr/bin/env python3
"""L-RED box 11 (produced on Opus 5.5): memory-light ctxfit.py. Same model and the same first-difference rule (L-ALG
dtl_rootmono.RM, dtl_fdlcheck.reduce_log imported UNMODIFIED), but each tattr log entry keeps hashes of its input and output
sets instead of the sets: (who, depth, hash(Z in), hash(Z out), maxpr). Comparison is on the first 4 fields, as in ctxtrace;
a hash collision could only hide a difference. VALIDATED against ctxfit.py (full sets) before use: see R40.
Usage: ctxlight.py G.pg"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ctxfit as CF
RMo = CF.RMo; FC = CF.FC; D = FC.D; FD = CF.FD
class LRM(RMo.RM):
    def tattr(s, p, Z, R, Gx, maxpr, consume):
        who = sys._getframe(1).f_code.co_name
        if who == "best_vertices": who = "bv-thr" if consume is None else "bv-reg"
        zin = hash(frozenset(Z)); s.used = set()
        D.DTL.tattr(s, p, Z, R, Gx, maxpr, consume)
        s.log.append((who, s.dep, zin, hash(frozenset(Z)), maxpr))
CF.RMo.RM = LRM
if __name__ == "__main__":
    ph = CF.run(CF.pg.read(sys.argv[1]))
    for i, (S, nG, c, o) in enumerate(ph):
        if S > 1: print(f"phase {i}: S {S} |G'| {nG} contexts {c}:", " ".join("none" if x is None else f"{x[0]}/{x[1]}/C{x[2]}/{x[3]}" for x in o))
    print("SUMMARY transitions %d max-contexts %d e*-at-depth>=1 %d" % CF.summary(ph))
