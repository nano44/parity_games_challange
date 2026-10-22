#!/usr/bin/env python3
"""Box 8 (Lead 00:52Z): can a varying/frozen τ make N5's Even steps emulate gen(m)? Search space: CDAG_n (Even vertices 1..n, sink 0
priority 0 self-loop; vertex v priority 2(n+1-v)+P0) where some edges v->u run through an Odd gadget o_{v,u} with choices
[u, ladder_l] (the ladder is a shared Odd/Even out-degree-1 path L_K -> ... -> L_1 -> T, T = Even self-loop of top even priority, so
ladder_l is at distance l from T: an Even GIFT whose length the adversary sets). Climb over (gadget set, l per gadget, τ0 per gadget,
σ0) for N5 iterations from the given start (n5.run, unmodified). Every improved best is checked (zielonka + verify.py) and written.
Usage: cdag_mask.py n K steps seed DIR"""
import sys, os, random, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..")); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import pg, n5, zielonka, verify
def build(n, K, cfg):
    gad, ln, t0, s0 = cfg      # gad: set of (v,u); ln[(v,u)] in 1..K; t0[(v,u)] in {0 honest, 1 gift}; s0[v] = u
    prio, owner, succ = [0], [0], [[0]]; idx = {}
    for v in range(1, n + 1): idx[v] = len(prio); prio.append(None); owner.append(0); succ.append(None)
    T = len(prio); prio.append(4 * n * n + 8 * K + 100); owner.append(0); succ.append([T])
    L = {}
    for l in range(1, K + 1): L[l] = len(prio); prio.append(None); owner.append(1); succ.append(None)
    for l in range(1, K + 1): succ[L[l]] = [T if l == 1 else L[l - 1]]
    O = {}
    for (v, u) in sorted(gad): O[(v, u)] = len(prio); prio.append(None); owner.append(1); succ.append([idx[u] if u else 0, L[ln[(v, u)]]])
    for v in range(1, n + 1): succ[idx[v]] = sorted(O[(v, u)] if (v, u) in O else (idx[u] if u else 0) for u in range(v))
    # priorities: CDAG vertices high and distinct, gadgets/ladder low and distinct (odd and even mixed: low relevance, length only)
    p = 2 * (len(L) + len(O)) + 2
    for v in range(1, n + 1): prio[idx[v]] = p + 2 * (n + 1 - v)
    q = 1
    for x in list(L.values()) + list(O.values()): prio[x] = q; q += 1
    g = pg.Game(prio, owner, succ)
    sig = {idx[v]: (O[(v, s0[v])] if (v, s0[v]) in O else (idx[s0[v]] if s0[v] else 0)) for v in range(1, n + 1)}
    sig[T] = T
    tau = {O[e]: succ[O[e]][t0[e]] for e in O}
    return g, (sig, tau)
def fit(n, K, cfg):
    g, st = build(n, K, cfg); it, fb, win, ws, ev = n5.run(g, "n5", st, cap=20000); return it, fb, g, st, win, ws
if __name__ == "__main__":
    n, K, steps, seed, d = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]; os.makedirs(d, exist_ok=True)
    rng = random.Random(seed); E = [(v, u) for v in range(2, n + 1) for u in range(1, v)]
    gad = set(e for e in E if rng.random() < 0.7); ln = {e: rng.randint(1, K) for e in E}; t0 = {e: rng.randrange(2) for e in E}
    s0 = {v: rng.randrange(v) for v in range(1, n + 1)}
    cfg = (gad, ln, t0, s0); best = fit(n, K, cfg)[:2]; print("start", best, flush=True)
    for s_ in range(steps):
        gad2, ln2, t02, s02 = set(gad), dict(ln), dict(t0), dict(s0); k = rng.random(); e = rng.choice(E)
        if k < 0.25: gad2 ^= {e}
        elif k < 0.6: ln2[e] = rng.randint(1, K)
        elif k < 0.85: t02[e] ^= 1
        else: v = rng.randint(1, n); s02[v] = rng.randrange(v)
        r = fit(n, K, (gad2, ln2, t02, s02))
        if r[:2] >= best:
            if r[:2] > best:
                it, fb, g, st, win, ws = r; zw, _ = zielonka.solve_with_strategy(g); ok = list(win) == list(zw) and not verify.check(g, win, ws)
                txt = pg.dumps(g); fn = os.path.join(d, f"mask_n{n}_K{K}_seed{seed}.pg"); open(fn, "w").write(txt)
                open(fn + ".start", "w").write("SIGMA0 " + " ".join(f"{a}:{b}" for a, b in sorted(st[0].items())) + "\nTAU0 " + " ".join(f"{a}:{b}" for a, b in sorted(st[1].items())) + "\n")
                print(f"step {s_} iterations {it} fallback {fb} n={g.n} check {'OK' if ok else 'FAIL'} sha1 {hashlib.sha1(txt.encode()).hexdigest()}", flush=True)
            best = r[:2]; gad, ln, t0, s0 = gad2, ln2, t02, s02
    print("best", best)
