#!/usr/bin/env python3
"""Box 49 climber (DATA, successor 29, queue item 3 (a)): games with many TIE / ODDC cycle changes in one phase and class
(P-N5-OFFMONO-add-box49 §3). Genome: game + start pair; mutations as qpcclimb.py (box43 climb.mutate with prob. 0.85, O-move 0.15).
OBJ oddc: (max ODDC_c, max ZCH_c); tie: (max TIE_c, max ZCH_c); both: (max TIE_c + ODDC_c, max ZCH_c). Every scored game also runs
tie.charcheck: any CHAR_V / FT_V / FTB_V is printed with the game saved as viol_*.pg (must not happen).
Usage: tieclimb.py NMAX STEPS SEED OBJ OUTDIR --seed GAME.pg [--start GAME.start]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
for p in ("../box43", "../box21"): sys.path.insert(0, os.path.join(HERE, p))
sys.path.insert(0, HERE)
import climb, tie
from multi import odd_choices
from qpcclimb import omove
from n5x import load, readstart
from common import rows, phases
climb.DEG2 = False
def score(g, st, obj):
    sp = ({v: st[v] for v in range(g.n) if g.owner[v] == 0}, {v: st[v] for v in range(g.n) if g.owner[v] == 1})
    E, R = rows(g, sp)
    Q = {v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2}
    before = {k: tie.C.get(k, 0) for k in ("CHAR_V", "FT_V", "FTB_V")}
    best, info = (0, 0), None
    for i, j in phases(R):
        tie.charcheck(g, E, R, i, j)
        for c, t_, o_, z_, ev in tie.phase_events(g, E, R, i, j, Q, ""):
            sc = {"oddc": (o_, z_), "tie": (t_, z_), "both": (t_ + o_, z_)}[obj]
            if sc > best: best = sc; info = dict(TIE=t_, ODDC=o_, ZCH=z_, len=j - i, c=c)
    viol = {k: tie.C.get(k, 0) - before[k] for k in before}
    return best, info, viol
if __name__ == "__main__":
    NMAX, STEPS, SEED = map(int, sys.argv[1:4]); OBJ, OUT = sys.argv[4], sys.argv[5]; os.makedirs(OUT, exist_ok=True); rng = random.Random(SEED)
    gpath = sys.argv[sys.argv.index("--seed") + 1]; g = load(gpath)
    if "--start" in sys.argv:
        sp = readstart(sys.argv[sys.argv.index("--start") + 1]); st = [sp[0][v] if g.owner[v] == 0 else sp[1][v] for v in range(g.n)]
    else: st = [g.succ[v][0] for v in range(g.n)]
    NMAX = max(NMAX, g.n); O = odd_choices(g); tag = os.path.basename(gpath)[:-3]
    best, info, viol = score(g, st, OBJ); print("start", best, info, "n", g.n, viol, flush=True); nviol = 0
    for t in range(STEPS):
        r = omove(rng, g, O, st) if rng.random() < 0.15 else climb.mutate(rng, g, O, NMAX, st)
        if r is None: continue
        h, O2, st2 = r
        try: sc, inf, viol = score(h, st2, OBJ)
        except (RecursionError, RuntimeError, KeyError): continue
        if any(viol.values()):
            nviol += 1; print("VIOLATION", t, viol, flush=True)
            if nviol <= 5: climb.save(os.path.join(OUT, f"viol_{tag}_s{SEED}_{nviol}.pg"), h, st2, inf)
        if sc >= best:
            if sc > best:
                print(t, sc, inf, "n", h.n, flush=True)
                climb.save(os.path.join(OUT, f"best_{OBJ}_{tag}_s{SEED}.pg"), h, st2, inf)
            g, O, st, best, info = h, O2, st2, sc, inf
    print("done", best, info, "violations", nviol, "charchecks", tie.C.get("char_checks", 0), flush=True)
