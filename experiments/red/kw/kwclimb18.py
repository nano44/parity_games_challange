#!/usr/bin/env python3
"""Box 43: hill-climb against the N5-KW notes with kw18.analyse (S3 start). Modes (objective, then tie-breakers):
  frzu  FRZU_margin_changed (last κ-change index − (|R| − 1), runs with a change)   [FRZ-U kill if > 0]
  kwf   KWF_margin_changed  (last COARSE_h change index − (n − 1))                     [KW-FREEZE (a) kill if > 0]
  kwfr  KWF_margin_r_changed (same against |R| − 1; not a claim, a probe)
  km    KM_postfreeze_kindchanges, U3x_kindchange_transitions                          [KIND-MONO regime]
  cw    CWINT_max, CW_switches                                                          [CW-INT / CW regime]
  cascb CASCB_slack (kind-B switch step − (|π_v| − 2) in W-flat kind-stable runs), CASCB_switches   [CASC-B kill if > 0]
Fitness = (#FAIL, objective, secondary). Any FAIL is saved as OUT_viol<k>.pg. Usage: kwclimb18.py mode seed secs OUT seed.pg"""
import sys, os, random, time, io, contextlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "so"))
import kw18, sox, pg
from soclimb import mutate, dump
NEG = (-1, -10 ** 9, -10 ** 9)
OBJ = {"frzu": ("FRZU_margin_changed", "FRZU_runs_with_change"), "kwf": ("KWF_margin_changed", "KWF_runs_with_change"),
       "kwfr": ("KWF_margin_r_changed", "KWF_runs_with_change"), "km": ("KM_postfreeze_kindchanges", "U3x_kindchange_transitions"),
       "cw": ("CWINT_max", "CW_switches"), "cascb": ("CASCB_slack", "CASCB_switches")}
def fit(G, mode):
    try:
        g = pg.Game(*G)
        if any(not s for s in G[2]) or len(sox.oddchoice(g)) != 1: return NEG, {}
        acc = {}
        with contextlib.redirect_stdout(io.StringIO()): kw18.analyse(g, acc, "c", cap=400)
    except AssertionError: return NEG, {}
    except Exception: return NEG, {}
    a, b = OBJ[mode]
    return (sum(v for k, v in acc.items() if k.startswith("FAIL")), acc.get(a, -10 ** 6), acc.get(b, 0)), acc
mode, seed, secs, out = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
g = sox.load(sys.argv[5]); G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f, _ = fit(G, mode)
t0 = time.time(); it = 0; nh = 0; print("start", f, flush=True); dump(G, out + ".pg")
while time.time() - t0 < secs:
    H = mutate(rng, G); it += 1; fh, ah = fit(H, mode)
    if fh[0] > 0 and nh < 5:
        nh += 1; dump(H, out + f"_viol{nh}.pg"); print("HIT", it, {k: v for k, v in ah.items() if k.startswith("FAIL")}, flush=True)
    if fh >= f:
        if fh > f: print(f"{time.time()-t0:7.0f}s it {it} fit {fh}", flush=True); dump(H, out + ".pg")
        G, f = H, fh
print("FINAL", f, it, flush=True)
