#!/usr/bin/env python3
"""L-ALG (produced on Opus 5.5, 2026-10-16 box 4): hill-climb on ACTUAL A_DTL runs for a (LEX) violation or a DEF-down step at
a fixed context (GAP-A-M §18c/§18f realised by DTL itself). Fitness (lexicographic, DOWN_MODE=down): (U-MONO_DTL) violations (same round input, union
shrinks), DEF-down steps, LEX violations, fall steps; DOWN_MODE=lex (found lex_viol_oink_n20): LEX violations (top changed
vertex falls), DEF-down steps at ideal-stable contexts (actual stable result shrinks or stable -> -1 with the ideal fixed), fall
steps (some death drops), max falls in one step. Order datum from DTL_ORDER.
Usage: DTL_ORDER=oink dtl_downclimb.py OUTDIR SEED STEPS --seed-game G.pg"""
import sys, os, argparse, random, signal
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_regvec as RV, dtl_ideal as I
from dtl_mclimb import mutate, TO
from dtl_nestclimb import write

INF = 10 ** 6
MODE = os.environ.get("DOWN_MODE", "down")   # down: U-shrinks, DEF-down, LEX, falls; lex: the box-4 order (LEX first)

def deaths(rounds):
    V0 = rounds[0]
    return {v: next((i for i in range(len(rounds)) if v not in rounds[i]), INF) for v in V0}

def measure(g, limit=20):
    d = RV.build(g)
    def h(*_): raise TO()
    signal.signal(signal.SIGALRM, h); signal.alarm(limit)
    try:
        d.run()
    except TO:
        return (-1,), None
    finally:
        signal.alarm(0)
    lexv = defdown = fallsteps = maxfall = ushrink = 0; ex = None
    for key, occ in d.calls.items():
        for (s1, r1, v1, h1, t1), (s2, r2, v2, h2, t2) in zip(occ, occ[1:]):
            if not set(t1) <= set(t2): continue
            for r in range(min(len(r1), len(r2), len(v1), len(v2))):     # (U-MONO_DTL): same round input, union shrinks?
                if r1[r] == r2[r] and r1[r] and v1[r] != v2[r]:
                    UA = set().union(*[z for _, z in v1[r]]); UB = set().union(*[z for _, z in v2[r]])
                    if not UA <= UB: ushrink += 1; ex = ("USHRINK", len(key[1]), s1, s2, r)
            if r1 == r2: continue
            D1, D2 = deaths(r1), deaths(r2)
            ch = [v for v in sorted(D1, reverse=True) if D1[v] != D2[v]]
            if not ch: continue
            falls = [v for v in ch if D2[v] < D1[v]]
            if falls: fallsteps += 1; maxfall = max(maxfall, len(falls))
            if D2[ch[0]] < D1[ch[0]]:
                lexv += 1; ex = ex or ("LEX", len(key[1]), s1, s2, d.idx[ch[0]])
            if h1 == h2 and h1[0] == 1:
                stab1 = not r1[-1] == frozenset(); stab2 = not r2[-1] == frozenset()
                if (stab1 and not stab2) or (stab1 and stab2 and r2[-1] < r1[-1]):
                    defdown += 1; ex = ex or ("DEFDOWN", len(key[1]), s1, s2)
    return ((ushrink, defdown, lexv, fallsteps, maxfall) if MODE == "down" else (lexv, defdown, fallsteps, maxfall)), (ex, d.iterations)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("out"); ap.add_argument("seed", type=int); ap.add_argument("steps", type=int); ap.add_argument("--seed-game", required=True)
    a = ap.parse_args(); os.makedirs(a.out, exist_ok=True); rnd = random.Random(a.seed); sys.setrecursionlimit(100000)
    g = pg.read(a.seed_game); f, info = measure(g); best = f
    print("start", f, info, flush=True)
    for step in range(a.steps):
        h = mutate(g, rnd, set()); fh, ih = measure(h)
        if fh >= f:
            g, f, info = h, fh, ih
            if f > best:
                best = f; write(g, os.path.join(a.out, f"down_s{a.seed}.pg"))
                print(f"step {step} n={g.n} fitness {f} {ih}", flush=True)
    print("done best", best, flush=True)
