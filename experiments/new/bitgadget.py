#!/usr/bin/env python3
"""Box 4 killer attempt 6: per-bit replicated lock gadget on switchallexp(N). The genome describes K vertices; one copy G_i is
built for EVERY bit i = 0..N-1. A copy's edges go to: its own vertices, the next copy G_{i+1} (if any), bit-relative labels of F
(name + index i or i+1: k l e h f g m z v r; a b at 2i, 2i+1), or global labels (q s p t x y w d). In-edges: from bit-relative
labels of bit i into G_i. Original priorities are scaled by 4; a gadget priority is (base + 4*i*stride) so copies stay ordered
by bit. Fitness = (min(lock at N=3, lock at N=4), lock at N=4, iterations at N=4); with THREE=1: (min lock over N=3,4,5, sum of the locks, iterations at N=5). Step = n5_lock.step; every improved best is
re-run through n5.run UNMODIFIED (counts asserted) and checked (zielonka.py + verify.py) at N = 3, 4. Usage: bitgadget.py K steps seed DIR"""
import sys, os, random, json, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "harness")); sys.path.insert(0, HERE)
import pg, zielonka, verify, n5
from lockgadget import base, lockrun
GL = "q s p t x y w d".split(); BL = "k l e h f g m z v r".split()
def lab(g, name):
    for v in range(g.n):
        if g.labels[v] == name: return v
    return None
def rel(g, N, i, t):
    kind = t[0]
    if kind == "G": return None                      # handled by caller
    if kind == "gl": return lab(g, t[1])
    name, off = t[1], t[2]
    if name in ("a", "b"): idx = 2 * (i + off // 2) + off % 2       # off in 0..3: a_{2i}, a_{2i+1}, a_{2i+2}, a_{2i+3}
    else: idx = i + off
    return lab(g, f"{name}{idx}")
def build(N, gen):
    g, _ = base(N); n0 = g.n; K = len(gen["prio"]); top = 4 * max(g.prio) + 4
    prio = [4 * p + 2 for p in g.prio]; owner = list(g.owner); succ = [list(s) for s in g.succ]
    gid = lambda i, k: n0 + i * K + k
    for i in range(N):
        for k in range(K):
            prio.append(gen["prio"][k] + 8 * i * gen["stride"]); owner.append(gen["owner"][k]); succ.append([])
    for i in range(N):
        for k in range(K):
            out = set()
            for t in gen["succ"][k]:
                if t[0] == "G":
                    j = i + t[2]
                    if j < N: out.add(gid(j, t[1]))
                else:
                    v = rel(g, N, i, t)
                    if v is not None: out.add(v)
            succ[gid(i, k)] = sorted(out) or [gid(i, k)]
        for t, k in gen["inedges"]:
            v = rel(g, N, i, t)
            if v is not None and gid(i, k) not in succ[v]: succ[v] = sorted(succ[v] + [gid(i, k)])
    return pg.Game(prio, owner, succ)
def rtarget(rng, K):
    x = rng.random()
    if x < 0.4: return ["G", rng.randrange(K), rng.choice([0, 0, 1])]
    if x < 0.55: return ["gl", rng.choice(GL)]
    nm = rng.choice(BL + ["a", "b"]); return ["b", nm, rng.randrange(4) if nm in "ab" else rng.choice([0, 0, 1])]
def rin(rng):
    nm = rng.choice(BL + ["a", "b"]); return ["b", nm, rng.randrange(2) if nm in "ab" else 0]
def main():
    K, steps, seed, d = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; os.makedirs(d, exist_ok=True)
    rng = random.Random(seed)
    gen = {"prio": [rng.randrange(400) for _ in range(K)], "owner": [rng.randrange(2) for _ in range(K)], "stride": rng.choice([0, 1, 2]),
           "succ": [[rtarget(rng, K) for _ in range(rng.randint(1, 3))] for _ in range(K)],
           "inedges": [[rin(rng), rng.randrange(K)] for _ in range(rng.randint(1, 3))]}
    def fit(gn):
        r3 = lockrun(build(3, gn)); r4 = lockrun(build(4, gn))
        if os.environ.get("THREE"):
            r5 = lockrun(build(5, gn)); return (min(r3[0], r4[0], r5[0]), r3[0] + r4[0] + r5[0], r5[2]), r3, r4
        return (min(r3[0], r4[0]), r4[0], r4[2]), r3, r4
    best = fit(gen); print("start", best[0], flush=True)
    for s in range(steps):
        gn = json.loads(json.dumps(gen)); k = rng.random(); i = rng.randrange(K)
        if k < 0.35: gn["succ"][i][rng.randrange(len(gn["succ"][i]))] = rtarget(rng, K)
        elif k < 0.45 and len(gn["succ"][i]) < 3: gn["succ"][i].append(rtarget(rng, K))
        elif k < 0.62: gn["prio"][i] = rng.randrange(400)
        elif k < 0.70: gn["owner"][i] = 1 - gn["owner"][i]
        elif k < 0.73: gn["stride"] = rng.choice([0, 1, 2])
        elif k < 0.88 and gn["inedges"]: gn["inedges"][rng.randrange(len(gn["inedges"]))] = [rin(rng), rng.randrange(K)]
        elif len(gn["inedges"]) < 6: gn["inedges"].append([rin(rng), rng.randrange(K)])
        f = fit(gn)
        if f[0] >= best[0]:
            if f[0] > best[0]:
                ok = True
                for N, r in ((3, f[1]), (4, f[2])):
                    g = build(N, gn); it, fb, win, ws, _ = n5.run(g, cap=20000); assert (it, fb) == (r[2], r[1])
                    ok &= win == zielonka.solve(g) and not verify.check(g, win, list(ws))
                print(f"step {s} fitness {f[0]} (N3 lock {f[1][0]} fb {f[1][1]} it {f[1][2]}; N4 lock {f[2][0]} fb {f[2][1]} it {f[2][2]}) check {'OK' if ok else 'FAIL'}", flush=True)
                json.dump(gn, open(os.path.join(d, f"bit_K{K}_seed{seed}{'_345' if os.environ.get('THREE') else ''}.json"), "w"))
            best, gen = f, gn
    print("best", best[0])
if __name__ == "__main__": main()
