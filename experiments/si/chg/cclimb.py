#!/usr/bin/env python3
"""L-SI box 28: kill search for the charging lemmas of note §3 (lemma kills, not SEG-COUNT kills; L-RED owns those).
OBJ=IE: kill = INTER-JOINT failure (chg/suffix.py INTEREARLY_V: an H-sink, not a W-sink, makes an intermediate switch and later
finalizes before its W-chain settles), shaping 3 * (H-sink intermediate switches) + EARLY_V (early H-sinks of any kind, capped 20).
OBJ=GP: kill = DL-SEP / DL-NOCONSEC / FROZEN-COUNT / GROWFIN failure (shaping also 30 * (max frozen-run excess + 9)) (DL-RUN, DL-FIRST died on L-RED's segcount_kill_n20) (GROW-PERSIST died: chg/instances/growpers_kill_n73) (chg/dlock.py), shaping 5 * deadlock steps + non-growth steps + 3 * sum over non-growth steps t > r0 of 12 // (finalizers at t).
OBJ=LE: kill = LENE failure (a maximal REL segment with b - a > |E_b|; third component = excess, > 0 a kill), shaping 30 (b - a - |E_b|) + 10 (b - a - SW) + 3 deadlocks.
Third component = failures (> 0 is a kill). Mutations and acceptance as lay/wclimb.py. Usage: cclimb.py SEED.pg SEED.start|- STEPS RNGSEED NMAX OUT"""
import sys, os, random
os.environ["PMODE"] = "1"
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(HERE, "..", "lwp")); sys.path.insert(0, HERE)
for p in (os.path.join(HERE, "..", "root"), os.path.join(ROOT, "experiments", "new", "box43"), os.path.join(HERE, "..", "runlin")): sys.path.insert(0, p)
from common import rows, load, readstart
import climb
climb.DEG2 = False
from multi import odd_choices
from growclimb import clone, save, mkst
from suffix import cscore
from dlock import dscore
from lenstat import lscore
OBJ = os.environ.get("OBJ", "IE")

def sc(g, st):
    try: E, R = rows(g, st, cap=1500)
    except (RecursionError, RuntimeError): return None
    if len(R) > 1500: return None
    if OBJ == "LE":                       # kill = a REL segment longer than |E_b| (LENE); shaping: (b - a) - SW, deadlocks
        xe, xs, dl = lscore(g, R)
        return (1000 * max(xe + 1, 0) + 30 * xe + 10 * xs + 3 * min(dl, 30), xs, max(xe, -1) + 1)
    if OBJ == "GP":                       # kill = GROW-PERSIST or DL-FIRST failure; shaping = non-growth steps and deadlock steps
        d = dscore(g, R); f = d.get("DLSEP_V", 0) + d.get("DLCONSEC_V", 0) + d.get("GROWFIN_V", 0) + d.get("FRZLEN_V", 0)
        ng = sum(k * d.get("ngrun_%d" % k, 0) for k in range(1, 10))
        return (1000 * f + 5 * min(d.get("deadlock", 0), 10) + min(ng, 40) + 3 * min(d.get("zlate_ng_inv", 0), 120) + 30 * d.get("zfrozen_excess_plus9", 9), d.get("zlate_ng", 0), f)
    d = cscore(g, R); f = d.get("INTEREARLY_V", 0) + d.get("JOINTX_V", 0) + d.get("BND_V", 0) + d.get("SUFFIX_V", 0)
    return (1000 * f + 3 * min(d.get("hsink_inter", 0), 30) + min(d.get("EARLY_V", 0), 20), d.get("hsink_inter", 0), f)

def main():
    gp, sp, steps, seed, nmax, out = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
    rng = random.Random(seed); g = load(gp); O = sorted(odd_choices(g)); st = None
    if sp != "-":
        s, t = readstart(sp); st = [s.get(v, t.get(v)) for v in range(g.n)]
    cur = sc(g, mkst(g, st)); print("seed", cur, "n", g.n, flush=True); bestk = cur[2]
    for it in range(steps):
        res = clone(rng, g, O, nmax, st) if rng.random() < 0.25 else climb.mutate(rng, g, O, nmax, st)
        if res is None: continue
        g2, O2, st2 = res; s2 = sc(g2, mkst(g2, st2))
        if s2 is None or s2[0] < cur[0]: continue
        if s2[0] > cur[0]: print("step", it, "score", s2, "n", g2.n, flush=True); save(out, g2, st2)
        if s2[2] > bestk: bestk = s2[2]; save(out + "_k", g2, st2); print("step", it, "KILLSCORE", s2[2], "n", g2.n, flush=True)
        g, O, st, cur = g2, O2, st2, s2
    print("final", cur, "n", g.n, "best kill score", bestk)

if __name__ == "__main__":
    main()
