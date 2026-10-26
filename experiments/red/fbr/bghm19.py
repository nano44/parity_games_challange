#!/usr/bin/env python3
"""Box 45b: the BGHM Fig. 2(a) obstruction of N5-FBF §7.3 built as N5 games, and N5 run on them from EVERY start pair (small) or random
start pairs. Gadget i (i = 1..k), inside one honest class with cycle node c (Even, self-loop, top even priority):
  v1_i  Odd choice: -> v2_i (the 2-cycle) or -> h_i (exit);  h_i  Even forced, even rank R_i, -> c;
  v2_i  Even: -> l_i (into the cycle) or -> x_i (Even's alternative exit, forced to c, odd rank) [variant A] / -> c directly [variant B];
  l_i   Even forced, even rank r_i < R_i, -> v1_i.
  Chaining (k >= 2): c_i := v1_{i+1} replaces c as the exit target of gadget i (so terminal values route through the next Odd choice).
Rank gaps: R − r is widened by isolated filler vertices (self-loop, priorities in between, unreachable): ranks change, the reachable
part does not. Priorities: c gets the top even priority. Usage: bghm19.py k gapmax variant [starts]   (starts = 'all' or a number)"""
import sys, os, itertools, random, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import fbr19, pg

def build(k, gap, variant):
    prio, owner, succ = [], [], []
    def add(p, o, s): prio.append(p); owner.append(o); succ.append(s); return len(prio) - 1
    base = 2
    c = add(0, 0, None)
    G = []
    for i in range(k):
        r = base; R = base + 2 * (gap + 1); base = R + 2
        v1 = add(1, 1, None); v2 = add(0, 0, None); l = add(r, 0, None); h = add(R, 0, None)
        x = add(R + 1, 0, None) if variant == "A" else None
        G.append((v1, v2, l, h, x))
    top = base + 2
    prio[c] = top; succ[c] = [c]
    for i, (v1, v2, l, h, x) in enumerate(G):
        tgt = G[i + 1][0] if i + 1 < k else c
        succ[v1] = [v2, h]; succ[l] = [v1]; succ[h] = [tgt]
        if variant == "A": succ[x] = [tgt]; succ[v2] = [l, x]
        else: succ[v2] = [l, tgt]
    # fillers: one isolated self-loop vertex per unused priority value below top, so ranks spread
    used = set(prio)
    for p in range(top):
        if p not in used: add(p, p % 2, None); succ[-1] = [len(prio) - 1]
    # vertices with priorities 0/1 duplicates are fine (ranks break ties by id)
    return pg.Game(prio, owner, succ)

if __name__ == "__main__":
    k, gapmax, variant = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]; starts = sys.argv[4] if len(sys.argv) > 4 else "all"
    rng = random.Random(1)
    for gap in range(0, gapmax + 1):
        g = build(k, gap, variant); n = g.n
        choice = [v for v in range(n) if len(set(g.succ[v])) > 1]
        if starts == "all":
            combos = itertools.product(*[sorted(set(g.succ[v])) for v in choice])
        else:
            combos = ([rng.choice(g.succ[v]) for v in choice] for _ in range(int(starts)))
        best = None; runs = 0; fails = 0
        for comb in combos:
            st = [g.succ[v][0] for v in range(n)]
            for v, w in zip(choice, comb): st[v] = w
            r = fbr19.analyse(g, st); runs += 1; fails += bool(r["fails"])
            key = (r["fmax"], r["ITER"])
            if best is None or key > best[0]: best = (key, r, st)
        r = best[1]
        print(f"k {k} gap {gap} variant {variant} n {n} |Q| {r['Q']} runs {runs} FAILruns {fails} | max fmax {r['fmax']} ITER {r['ITER']} rho {r['rho_at']} phases {r['phases']}", flush=True)
