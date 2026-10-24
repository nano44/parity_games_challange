"""L-RED box 30 (produced on Opus 5.5): hill climb toward an (ACYC) counterexample (STEP5.md §6.1, GAPS G-S5-6) with a graded
fitness and mutations FOCUSED on the straddling tangles. Runs A_DTL's Python reference via probe.run (L-ALG's dtl_yzclimb.Y,
read-only). For each straddling Dom acceptance (tangle t, new part N): gap = the least number of
vertices OUTSIDE N on a cycle of t's tangle graph (p-vertex: its strategy edge; opponent vertex: its edges inside t) through a
vertex of N (0-1 BFS); gap = 0 is exactly an (ACYC) failure. Fitness (lexicographic): (ACYC failures, YZ excess, -min gap,
max |N|, straddles). Mutations as L-ALG's
dtl_fmclimb.mutate (add/remove edge, priority +-1, owner flip), but with probability FOCUS the vertex is drawn from the straddling
tangles (original ids). Writes acyc_viol_*.pg on a hit. Usage: focusclimb.py START.pg SEED SECONDS OUTDIR [FOCUS]"""
import os, random, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import probe  # noqa: E402
import pg  # noqa: E402
start, seed, secs, out = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
FOCUS = float(sys.argv[5]) if len(sys.argv) > 5 else 0.7
rnd = random.Random(seed); os.makedirs(out, exist_ok=True)


def fit(g):
    try:
        d, ev = probe.run(g)
    except Exception:
        return (-1,), set()
    if not all(w is not None for w in d.win): return (99,), set()
    gap, nmax, foc = 99, 0, set()
    for e in ev:
        T = dict(e["tv"]); N = set(e["N"]); p = e["p"]
        succ = lambda v: [T[v]] if d.ow[v] == p else [w for w in d.outs[v] if w in T]
        for s0 in N:                                   # 0-1 BFS: cost of entering a vertex = 0 if in N else 1
            from collections import deque
            dist = {s0: 0}; dq = deque([s0]); best = 99
            while dq:
                v = dq.popleft()
                for w in succ(v):
                    if w == s0: best = min(best, dist[v]); continue
                    c = dist[v] + (0 if w in N else 1)
                    if c < dist.get(w, 99): dist[w] = c; (dq.appendleft if w in N else dq.append)(w)
            gap = min(gap, best)
        nmax = max(nmax, len(N)); foc |= {d.idx[v] for v in T}
    return (d.acyc_fail, d.excess, -gap, nmax, len(ev)), foc


def mutate(g, focus):
    pr, ow, su = list(g.prio), list(g.owner), [list(s) for s in g.succ]; n = g.n; k = rnd.randrange(4)
    v = rnd.choice(sorted(focus)) if focus and rnd.random() < FOCUS else rnd.randrange(n)
    tgt = rnd.choice(sorted(focus)) if focus and rnd.random() < FOCUS else rnd.randrange(n)
    if k == 0: su[v] = sorted(set(su[v]) | {tgt})
    elif k == 1 and len(su[v]) > 1: su[v].remove(rnd.choice(su[v]))
    elif k == 2: pr[v] = max(0, pr[v] + rnd.choice([-1, 1]))
    else: ow[v] = 1 - ow[v]
    return pg.Game(pr, ow, su)


g = pg.read(start); fg, foc = fit(g); t0 = time.time(); it = 0
print("start", fg, flush=True)
while time.time() - t0 < secs:
    it += 1; h = mutate(g, foc); fh, fo = fit(h)
    if fh[0] >= 99: pg.write(h, os.path.join(out, f"incomplete_{seed}_{it}.pg")); print("INCOMPLETE RUN", it, flush=True); continue
    if fh >= fg:
        if fh > fg: print(f"step {it} t {time.time() - t0:.0f}s fitness {fh}", flush=True)
        g, fg, foc = h, fh, (fo or foc)
        if fg[0] >= 1 or fg[1] >= 1:
            pg.write(g, os.path.join(out, f"acyc_viol_{seed}_{it}.pg")); print("HIT", it, fg, flush=True); break
pg.write(g, os.path.join(out, f"last_{seed}.pg")); print("end", fg, it, "steps", flush=True)
