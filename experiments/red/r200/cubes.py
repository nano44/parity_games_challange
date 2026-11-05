#!/usr/bin/env python3
"""L-RED R200/R202 CUBES: resumable exact cube-and-conquer for all-free ladder queries (xmax.py model: d levels, horizon t, env flags as
xmax: TMIN, SYMB, CMIN, SEG). Cubes = first-move times of chosen movers (0 = never within the horizon): a complete partition. Level 1:
the two level-0 movers (movers 0, 1); a cube that exceeds TL seconds is split on the two level-1 movers (2, 3), then on 4, 5. Finished
cubes (UNSAT, or SAT with a replayed witness) are appended to <state>.json after each cube; a relaunch with the same command skips them.
Answer: SAT as soon as one cube is SAT (witness replayed under r187/ideal.py); UNSAT when every cube of the partition is UNSAT.
Usage: cubes.py d t state_prefix    (env TL seconds per cube attempt, default 1200; SOLVER)"""
import sys, os, json, time, threading
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
os.environ.setdefault("TMIN", "1")
import xcnf, ideal
from pysat.solvers import Solver
d, t, pre = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]; TL = float(os.environ.get("TL", "1200"))
T = dict(movers=[], gate=[], states=[[] for _ in range(t + 1)])
C, I = xcnf.build(T, d); mv, N, L = I["mv"], I["N"], I["L"]
GROUPS = [(0, 1), (2, 3), (4, 5)]
def lits(key):   # key: tuple of (mover, first move time or 0 = never)
    a = []
    for v, ft in key:
        for u in range(1, L + 1):
            x = mv[(u, v)]
            want = (u == ft) if ft else False
            if ft and u > ft: continue
            if isinstance(x, bool):
                if x != want: return None
                continue
            a.append(x if want else -x)
    return a
def children(key):
    g = GROUPS[len(key) // 2]
    return [key + ((g[0], f0), (g[1], f1)) for f0 in range(L + 1) for f1 in range(L + 1)]
sf = pre + "_state.json"; st = json.load(open(sf)) if os.path.exists(sf) else {"done": {}, "split": []}
def save(): json.dump(st, open(sf + ".tmp", "w")); os.replace(sf + ".tmp", sf)
ks = lambda k: ";".join(f"{v}:{f}" for v, f in k)
print(f"CUBES d {d} t {t} N {N} vars {C.n} clauses {len(C.cl)}; state: {len(st['done'])} done, {len(st['split'])} split", flush=True)
import multiprocessing as mp
ctx = mp.get_context("fork"); P = int(os.environ.get("P", "1"))
def work(a, q):
    with Solver(name=os.environ.get("SOLVER", "cadical195"), bootstrap_with=C.cl) as S:
        r = S.solve(assumptions=a); q.put((r, S.get_model() if r else None))
stack = children(()); t00 = time.time(); running = {}; answer = None
while (stack or running) and answer is None:
    while stack and len(running) < P:
        k = stack.pop(0); s = ks(k)
        if s in st["done"]: continue
        if s in st["split"] and len(k) // 2 < len(GROUPS): stack = children(k) + stack; continue
        a = lits(k)
        if a is None: st["done"][s] = "unsat-trivial"; continue
        q = ctx.Queue(); pr = ctx.Process(target=work, args=(a, q)); pr.start(); running[s] = (k, pr, q, time.time())
    time.sleep(0.2)
    for s, (k, pr, q, t0) in list(running.items()):
        dt = time.time() - t0; deep = len(k) // 2 >= len(GROUPS)
        if not q.empty():
            r, model = q.get(); pr.join(); del running[s]
            if r:
                G = xcnf.decode(model, I); json.dump(G, open(pre + "_genome.json", "w")); Sx, why = ideal.traj(G)
                st["done"][s] = f"SAT L {len(Sx) - 1}"; save(); answer = "SAT"
                print(f"CUBE {s} SAT {dt:.0f} s -> {pre}_genome.json replay L {len(Sx) - 1} {why}; CUBES ANSWER: SAT", flush=True)
            else:
                st["done"][s] = f"unsat {dt:.1f}"; save(); print(f"CUBE {s} UNSAT {dt:.1f} s", flush=True)
        elif dt > TL and not deep:
            pr.kill(); pr.join(); del running[s]; st["split"].append(s); save()
            print(f"CUBE {s} TIMEOUT {dt:.0f} s -> split", flush=True); stack = children(k) + stack
for s, (k, pr, q, t0) in running.items(): pr.kill()
if answer is None: print(f"CUBES ANSWER: UNSAT (all cubes; this run {time.time() - t00:.0f} s; done {len(st['done'])}, split {len(st['split'])})", flush=True)
