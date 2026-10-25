#!/usr/bin/env python3
"""L-SI box 7: adversarial climb on J = #non-tame transitions per joint λ-phase (docs/si/N5-C-box7.md §7, OPEN (J-poly)).
Fitness = (max J in one phase, total in-phase J, in-phase fallbacks); with JMODE=REL, (#in-scope non-tame transitions whose argmin was
released into D at an earlier fallback of the same scope run, J_in, releases into D) (dpot.py; the part of Corollary JD paid by releases). o-cyclic 𝒞^1O only (one Odd choice vertex, asserted; mutation
operator and o-cyclicity test from experiments/new/box21/climb_fix.py and box25/pureY.py, read-only, as in xing/clclimb.py).
Box 9: JMODE=HEQ (FBW violations; in-scope u* = none / EQ fallbacks; Even fallbacks), JMODE=REP (reltrace.py violations;
tail repeats + θ-changes above M inside a level-M block; block fallbacks).
JMODE=NORF (norf.py violations + fallbacks after a rise; states checked after a rise; rises).
JMODE=MINSET (NJB violations = Mn emptied inside a block; Mn absorptions + intervals reaching |Mn| = 1; intervals).
Usage: [JMODE=REL|CLS|CLS2|RF|HEQ|REP|NORF|MINSET] jclimb.py seed secs OUT seed.pg      (writes OUT.pg on every improvement; re-verify bests with xing/reverify.sh)"""
import sys, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tame import *
from dpot import scan_d
from clscope import scan_c
from cls2 import scan2
from rfinv import scan_r
from fbw import scan_w
from reltrace import scan_rel
from norf import scan_n
from minset import scan_m
MODE = os.environ.get("JMODE", "J")   # J: (max J per phase, J, fb); REL: (#jumps paid by a release (REL-NJ failures), J_in, releases)
sys.path.insert(0, os.path.join(ROOT, "experiments/new/box21")); sys.path.insert(0, os.path.join(ROOT, "experiments/new/box25"))
from climb_fix import mutate
from pureY import split

def fit(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(set(G[2][v])) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return (-10 ** 9, -1, -1)
    g = pg.Game(*G)
    if not any(w in split(g, odd[0]) for w in G[2][odd[0]]): return (-10 ** 9, -1, -1)
    try:
        if MODE == "CLS":   # adversarial against CONJECTURE (CL-S): (violations, fallbacks in scope runs, jumps in one scope run)
            c, _ = scan_c(g, "climb")
            return (c["mono_viol"] + c["perlevel_viol"], c["fb"], c["maxJ_run"])
        if MODE == "CLS2":  # (CL-S) violations, then MF rises inside scope runs (the mechanism that could break it), then fallbacks
            c, _ = scan_c(g, "climb"); c2, _ = scan2(g, "climb")
            return (c["mono_viol"] + c["perlevel_viol"], c["maxgap"], c["fb"] + c2.get("MF_up", 0))
        if MODE == "RF":    # invariant violations, then preconditions of the open case (high gates into R̄, arena leaves) after a fallback
            c, _ = scan_c(g, "climb"); r, _ = scan_r(g, "climb")
            v = c["mono_viol"] + c["perlevel_viol"] + r.get("RF_viol", 0) + r.get("FF_viol", 0) + r.get("F_viol", 0) + r.get("LEAVE_viol", 0)
            return (v, min(r.get("highRbar", 0), 20) + 5 * min(r.get("leave_ar", 0), 4), c["fb"])
        if MODE == "HEQ":
            c, _ = scan_w(g, "climb")
            v = c.get("a_viol", 0) + c.get("b_viol", 0) + c.get("W_viol", 0) + c.get("premise_fail", 0) + c.get("scope_viol", 0)
            return (v, 5 * c.get("scope_THR0", 0) + c.get("scope_EQ", 0), c.get("fbE", 0))
        if MODE == "REP":
            c, _ = scan_rel(g, "climb")
            v = sum(c.get(k, 0) for k in ("absl_viol", "rela_viol", "flat_viol", "onerise_viol", "consec_viol"))
            return (v, max(c.get("max_rep", 0) - 1, 0) + c.get("blk_A", 0), c.get("blk_fb", 0))
        if MODE == "NORF":
            c, _ = scan_n(g, "climb")
            return (c.get("old_viol", 0) + c.get("new_viol", 0) + c.get("fb_after_rise", 0), c.get("chk", 0), c.get("rises", 0))
        if MODE == "MINSET":
            c, _ = scan_m(g, "climb")
            return (c.get("njb_viol", 0) + c.get("minset_c_mismatch", 0), 5 * c.get("absorbed", 0) + c.get("min_le1", 0), c.get("intervals", 0))
        if MODE == "REL":
            c, _ = scan_d(g)
            return (c["relnj_viol"], c["J_in"], c["rel_fb"])
        c, _ = scan_t(g)
        return (c["maxJ_phase"], c["J"], c["fb"])
    except AssertionError: raise
    except Exception: return (-10 ** 9, -1, -1)

def write(path, G):
    n = len(G[0])
    open(path, "w").write(f"parity {n-1};\n" + "".join(f"{v} {G[0][v]} {G[1][v]} {','.join(map(str, G[2][v]))};\n" for v in range(n)))

if __name__ == "__main__":
    seed, secs, out = int(sys.argv[1]), float(sys.argv[2]), sys.argv[3]; rng = random.Random(seed)
    g = load(sys.argv[4]); G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f = fit(G)
    t0 = time.time(); it = 0; print("start", f, flush=True)
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh = fit(H)
        if fh >= f:
            if fh > f:
                print(f"{time.time()-t0:7.0f}s it {it} fit {fh}", flush=True); write(out + ".pg", H)
            G, f = H, fh
    print("FINAL", f, it, flush=True)
