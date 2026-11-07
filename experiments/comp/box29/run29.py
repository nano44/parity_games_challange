#!/usr/bin/env python3
"""L-COMP box 29 (Lead 07:08Z): N5 end-to-end on Gamma3(G) of L-LOWER 4's tower genomes. Runs MY n5b (experiments/n5-second/n5b.py,
SPEC mode, default start S3 = best reward for Even on G and for Odd on the dual, n5b.N5.run with sigma = tau = None), recording every
state (trace hook) and fallback flag (fbtrace hook); neither hook changes the run. Then, from the states, with n5b's own SpecSI:
- FL runs (RESULTS R104 / P-N5-REACH l. 39: «a maximal set of consecutive non-fallback transitions that keep τ, change σ and keep that
  valuation everywhere», «that valuation» = the valuation of the (σ, τ)-play): transition j (state j-1 -> j) is FL iff fbtrace[j-1] = 0,
  τ_j = τ_(j-1), σ_j ≠ σ_(j-1), and W_j = W_(j-1) at every vertex, W = SpecSI(G with σ and τ fixed).evaluate(σ).
- bit cost (TARGET.md §3): per state, over all vertices of Even's valuation of σ (SpecSI(G).evaluate(σ)) and of the dual valuation of τ,
  the largest |P| (the path set) and the largest distance; size in bits := (|P| + 2) · ceil(log2 n) (cycle vertex + P + distance).
Writes OUT.sol (n5b's solution, pg.write_sol) and OUT.json (per-run record). Usage: run29.py GAME.pg OUT"""
import sys, os, json, math, time
HERE = os.path.dirname(os.path.abspath(__file__)); N5D = os.path.join(HERE, "..", "..", "n5-second"); sys.path.insert(0, N5D)
import n5b
from n5b import N5, SpecSI, restrict, dual, pg, EVEN, ODD
n5b.MODE = "spec"
gpath, out = sys.argv[1], sys.argv[2]; g = pg.read(gpath); t0 = time.time()
s = N5(g, mode="spec"); tr, fbt = [], []
win, strat, it, fb = s.run(trace=tr, fbtrace=fbt)
pg.write_sol(win, out + ".sol", strat)
t1 = time.time()
SG, SD = SpecSI(g), SpecSI(dual(g)); lb = math.ceil(math.log2(g.n))
def playval(sig, tau):
    allow = [[sig[v]] if g.owner[v] == EVEN else [tau[v]] for v in range(g.n)]
    return SpecSI(restrict(g, allow)).evaluate(list(sig))
W = [playval(sg, tu) for sg, tu in tr]
fl = [fbt[j - 1] == 0 and tr[j][1] == tr[j - 1][1] and tr[j][0] != tr[j - 1][0] and W[j] == W[j - 1] for j in range(1, len(tr))]
runs, a = [], None
for j, f in enumerate(fl + [False], 1):
    if f and a is None: a = j - 1
    if not f and a is not None: runs.append([a, j - 1, j - 1 - a]); a = None
size = []
for sg, tu in tr:
    vs, vt = SG.evaluate(list(sg)), SD.evaluate(list(tu)); P = max(len(x[1]) for x in list(vs) + list(vt)); Dm = max(x[2] for x in list(vs) + list(vt))
    size.append([P, Dm, (P + 2) * lb])
rec = dict(game=os.path.basename(gpath), n=g.n, max_prio=max(g.prio), distinct_prios=len(set(g.prio)), iterations=it, fallbacks=fb,
           fallback_transitions=[j + 1 for j, f in enumerate(fbt) if f], fl_runs=runs, longest_fl=max([r[2] for r in runs], default=0),
           max_P=max(x[0] for x in size), max_dist=max(x[1] for x in size), max_bits=max(x[2] for x in size), per_state_size=size,
           n5_seconds=round(t1 - t0, 1), total_seconds=round(time.time() - t0, 1))
json.dump(rec, open(out + ".json", "w"))
print(f"{rec['game']} n {g.n} prios {rec['distinct_prios']} (max {rec['max_prio']}): n5b SPEC from S3: iterations {it} fallbacks {fb} "
      f"(at transitions {rec['fallback_transitions']}); FL runs {[tuple(r) for r in runs]}, longest {rec['longest_fl']}; "
      f"max |P| {rec['max_P']} max dist {rec['max_dist']} max bits {rec['max_bits']}; {rec['n5_seconds']} s", flush=True)
