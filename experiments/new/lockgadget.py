#!/usr/bin/env python3
"""Box 4 killer attempt 5: structured lock search ("the lock must read the counter", K3). A gadget of K vertices attached to
Friedmann's switchallexp(N) (pgsolver_port.py) ONLY through label templates that exist for every N: global labels
q s p t x y w d, and per-bit labels (k l e h f g m z v r: bit 0 or the top bit; a b: index 0 or 2N-1). The genome is therefore
N-independent and the same gadget is built at N = 2, 3, 4, ... Original priorities are scaled by 4 (gadget priorities interleave).
Fitness = (longest lock at N=3, longest lock at N=2, fallbacks at N=3); with NS=a,b: (min of the two locks, lock at b, lock at a); every improved best is re-run through n5.run UNMODIFIED
(counts asserted) and checked (zielonka.py + verify.py) at N = 2, 3. Usage: lockgadget.py K steps seed DIR"""
import sys, os, random, subprocess, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "harness")); sys.path.insert(0, HERE)
import pg, zielonka, verify, n5
from n5_lock import step
from n5 import Engine, dual
GL = "q s p t x y w d".split(); BL = "k l e h f g m z v r a b".split()
ANCH = [(a, None) for a in GL] + [(b, w) for b in BL for w in ("lo", "hi")]
BASE = {}
def base(N):
    if N not in BASE:
        txt = subprocess.run([sys.executable, os.path.join(HERE, "..", "hard-families", "pgsolver_port.py"), "switchallexp", str(N)],
                             capture_output=True, text=True).stdout
        BASE[N] = (pg.parse(txt), txt)
    return BASE[N]
def anchor_vertex(g, N, a):
    name, w = a
    lab = name if w is None else name + str(0 if w == "lo" else (2 * N - 1 if name in "ab" else N - 1))
    for v in range(g.n):
        if g.labels and g.labels[v] == lab: return v
    return None
def build(N, gen):
    g, _ = base(N); n0 = g.n; K = len(gen["prio"])
    prio = [4 * p + 2 for p in g.prio] + list(gen["prio"]); owner = list(g.owner) + list(gen["owner"]); succ = [list(s) for s in g.succ]
    def tgt(t):
        if t[0] == "g": return n0 + t[1]
        v = anchor_vertex(g, N, tuple(t[1])); return v
    for k in range(K):
        s = sorted(set(x for x in (tgt(t) for t in gen["succ"][k]) if x is not None)); succ.append(s or [n0 + k])
    for a, k in gen["inedges"]:
        v = anchor_vertex(g, N, tuple(a))
        if v is not None and n0 + k not in succ[v]: succ[v] = sorted(succ[v] + [n0 + k])
    return pg.Game(prio, owner, succ)
def lockrun(g):
    E, Ed = Engine(g), Engine(dual(g)); s, t = list(E.initial("best")), list(Ed.initial("best")); it = fb = run = cur = 0
    while it < 20000:
        r = step(g, E, Ed, s, t)
        if r is None: break
        s, t, f, _, _ = r; it += 1; fb += f; cur = cur + 1 if f else 0; run = max(run, cur)
    return run, fb, it
def rtarget(rng, K): return ["g", rng.randrange(K)] if rng.random() < 0.5 else ["a", list(rng.choice(ANCH))]
def main():
    K, steps, seed, d = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; os.makedirs(d, exist_ok=True)
    rng = random.Random(seed); top = 4 * max(base(4)[0].prio) + 8
    gen = {"prio": [rng.randrange(top) for _ in range(K)], "owner": [rng.randrange(2) for _ in range(K)],
           "succ": [[rtarget(rng, K) for _ in range(rng.randint(1, 3))] for _ in range(K)],
           "inedges": [[list(rng.choice(ANCH)), rng.randrange(K)] for _ in range(rng.randint(1, 4))]}
    NA, NB = map(int, os.environ.get("NS", "2,3").split(","))
    def fit(gn):
        rb = lockrun(build(NB, gn)); ra = lockrun(build(NA, gn))
        return ((min(rb[0], ra[0]), rb[0], ra[0]) if "NS" in os.environ else (rb[0], ra[0], rb[1])), ra, rb
    best = fit(gen)
    print("start", best[0], flush=True)
    for s in range(steps):
        gn = json.loads(json.dumps(gen)); k = rng.random(); i = rng.randrange(K)
        if k < 0.35: gn["succ"][i][rng.randrange(len(gn["succ"][i]))] = rtarget(rng, K)
        elif k < 0.45 and len(gn["succ"][i]) < 3: gn["succ"][i].append(rtarget(rng, K))
        elif k < 0.65: gn["prio"][i] = rng.randrange(top)
        elif k < 0.75: gn["owner"][i] = 1 - gn["owner"][i]
        elif k < 0.9 and gn["inedges"]: gn["inedges"][rng.randrange(len(gn["inedges"]))] = [list(rng.choice(ANCH)), rng.randrange(K)]
        elif len(gn["inedges"]) < 8: gn["inedges"].append([list(rng.choice(ANCH)), rng.randrange(K)])
        f = fit(gn)
        if f[0] >= best[0]:
            if f[0] > best[0]:
                ok = True
                for N in (NA, NB):
                    g = build(N, gn); it, fb, win, ws, _ = n5.run(g, cap=20000)
                    r = f[1] if N == NA else f[2]; assert (it, fb) == (r[2], r[1])
                    ok &= win == zielonka.solve(g) and not verify.check(g, win, list(ws))
                print(f"step {s} fitness {f[0]} (N{NA}: lock {f[1][0]} fb {f[1][1]} it {f[1][2]}; N{NB}: lock {f[2][0]} fb {f[2][1]} it {f[2][2]}) check {'OK' if ok else 'FAIL'}", flush=True)
                json.dump(gn, open(os.path.join(d, f"gadget_K{K}_seed{seed}{os.environ.get('NS', '').replace(',', '_')}.json"), "w"))
            best, gen = f, gn
    print("best", best[0])
if __name__ == "__main__": main()
