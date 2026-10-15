#!/usr/bin/env python3
"""Can pads make S7 follow a longest downstream-first run on FHZ's G_{n,1,1,1}? (L-RED, Question DF, second half.)
1. Longest DF run restricted to BEST-EDGE switches (S7 switches a vertex to its best successor), by DP over all trees of G.
2. For every step k (chosen vertex v_k) and every other improving vertex u that is not downstream of v_k (downstream ones are
   outranked automatically, Lemma D): count_k(v_k) >= count_k(u) + 1, where count_k(x) in the parity encoding P (R2) is
   base_k(x) + sum of pads of G-vertices whose play passes x; base_k(x) = number of unpadded P-vertices whose play passes x.
   Linear feasibility in the pad variables (scipy linprog), pads >= 0.
3. Rounds a feasible solution to integers (scaled) and verifies by running vjfast most-improved on the padded P.
Usage: df_lp.py VJFAST n [--scale 1000]"""
import sys, os, itertools, subprocess, tempfile, argparse
sys.setrecursionlimit(1 << 20); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import fhz
ap = argparse.ArgumentParser(); ap.add_argument("vjfast"); ap.add_argument("n", type=int); ap.add_argument("--scale", type=float, default=1000)
ap.add_argument("--samples", type=int, default=1); ap.add_argument("--prefix", action="store_true"); ap.add_argument("--anyrun", type=int, default=0); ap.add_argument("--seed", type=int, default=0); ap.add_argument("--r", type=int, default=1); ap.add_argument("--s", type=int, default=1); ap.add_argument("--t", type=int, default=1); a = ap.parse_args()
n = a.n; G, P, B0, B0P, names, ename, pid = fhz.build(n, a.r, a.s, a.t); N = G.N; out = G.out
trees = list(itertools.product(*[out[v] for v in range(N - 1)]))


def analyse(B):
    dist = [None] * N; dist[N - 1] = 0
    def d(v):
        if dist[v] is None:
            sv, w, c = G.edges[B[v]]; dist[v] = c + d(w)
        return dist[v]
    for v in range(N - 1): d(v)
    imp = [(v, e) for v in range(N - 1) for e in out[v] if e != B[v] and G.edges[e][2] + dist[G.edges[e][1]] < dist[v]]
    impv = {v for v, _ in imp}
    best = {}
    for v, e in imp:
        val = G.edges[e][2] + dist[G.edges[e][1]]
        if v not in best or val < best[v][1]: best[v] = (e, val)
    dfs = []
    for v, (e, val) in best.items():
        x = G.edges[B[v]][1]; ok = True
        while x != N - 1:
            if x in impv: ok = False; break
            x = G.edges[B[x]][1]
        if ok:
            T = list(B); T[v] = e; dfs.append((tuple(T), v, e))
    return imp, impv, dfs


nxt = {B: analyse(B)[2] for B in trees}; memo = {}
def longest(B):
    if B in memo: return memo[B]
    memo[B] = 0; memo[B] = max([longest(T) + 1 for T, v, e in nxt[B]] + [0]); return memo[B]
start = max(trees, key=longest); L = memo[start]
print(f"n={n}: longest best-edge DF run {L} (trees {len(trees)})", flush=True)
import random
rng = random.Random(a.seed)
starts = [B for B in trees if memo[B] == L]


def extract(randomised):
    run = []; B = rng.choice(starts) if randomised else start
    while nxt[B]:
        cands = [x for x in nxt[B] if memo[x[0]] + 1 == memo[B]]
        if not cands: break
        T, v, e = rng.choice(cands) if randomised else cands[0]
        run.append((B, v, e)); B = T
    return run
# constraints
gv = list(range(N - 1))


def upstream(B, v):
    """G-vertices whose tree path passes v (including v)"""
    up = set()
    for x in gv:
        y = x
        while y != N - 1:
            if y == v: up.add(x); break
            y = G.edges[B[y]][1]
    return up


def base_count(B, v):
    """unpadded P-vertices whose play passes the P-vertex of v: for each upstream G-vertex x, itself + its relay (+ class vertex)"""
    cnt = 0
    for x in upstream(B, v):
        cnt += 1                                  # x itself (as P-vertex)
        if x != v:
            e = B[x]; cnt += 1                    # relay of the edge x uses
            if G.edges[e][2] > 0: cnt += 1        # class vertex (shared; counted once per path, approximate upper use)
    return cnt


def constraints(run):
  rows = []; rhs = []; meta = []
  for k, (B, v, e) in enumerate(run):
    imp, impv, dfs = analyse(B)
    upv = upstream(B, v); bv = base_count(B, v)
    for u in impv:
        if u == v: continue
        # u downstream of v (on v's path)? then skipped by DF; u upstream of v? automatically outranked
        if v in upstream(B, u): continue
        upu = upstream(B, u); bu = base_count(B, u)
        row = [0.0] * len(gv)
        for x in upu: row[x] += 1.0
        for x in upv: row[x] -= 1.0
        nm = lambda x: names[x + 1]
        rows.append(row); rhs.append(bv - bu - 1.0); meta.append((k, nm(v), nm(u), sorted(nm(x) for x in upv), sorted(nm(x) for x in upu)))
  return rows, rhs, meta


from scipy.optimize import linprog
import numpy as np
feasible = 0; shown = False
for smp in range(a.samples):
    run = extract(a.samples > 1); rows, rhs, meta = constraints(run)
    res = linprog(c=np.ones(len(gv)), A_ub=np.array(rows) if rows else None, b_ub=np.array(rhs) if rows else None, bounds=[(0, None)] * len(gv), method="highs")
    if smp == 0: print(f"constraints: {len(rows)} over {len(gv)} pad variables; LP status {res.status} ({res.message[:40]})", flush=True)
    if res.status != 0:
        if smp == 0 and a.samples == 1:
            # show direct contradictions: same (v,u) pair with swapped roles and identical upstream sets
            seen = {}
            for (k, vn, un, upv, upu), r in zip(meta, rhs): seen.setdefault((vn, un, tuple(upv), tuple(upu)), []).append((k, r))
            for key in list(seen):
                vn, un, upv, upu = key; rev = (un, vn, upu, upv)
                if rev in seen: print(f"  conflict: step {seen[key][0][0]} needs {vn} > {un}; step {seen[rev][0][0]} needs {un} > {vn}; up({vn})={list(upv)} up({un})={list(upu)}")
        continue
    feasible += 1
    if not shown:
        shown = True; start = run[0][0]
        pads = [int(round(x * a.scale)) + (1 if x > 1e-9 else 0) for x in res.x]
        with tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False) as f: fhz.export_pg(P, B0P, names, f.name); base = open(f.name).read().splitlines(); os.unlink(f.name)
        lines = list(base[1:]); nx = P.N
        for x in gv:
            for _ in range(pads[x]): lines.append(f"{nx} 0 0 {pid[('v', x)]};"); nx += 1
        with tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False) as f: f.write(f"parity {nx - 1};\n" + "\n".join(lines) + "\n"); p = f.name
        st = "spec:" + " ".join(f"{pid[('v', x)]}:{P.edge_head[start[x]]}" for x in gv)
        r = subprocess.run([a.vjfast, "most-improved", p, "--start", st], capture_output=True, text=True); os.unlink(p)
        print("feasible run found (sample", smp, "); vjfast S7 on the padded P from the run's start:", [l for l in r.stderr.splitlines() if l.startswith("solved")][0], "| DF run length", L)
        print("pads:", {names[x + 1]: pads[x] for x in gv if pads[x]})
print(f"feasible longest DF runs: {feasible} of {a.samples} sampled")


def lp_ok(rows, rhs):
    if not rows: return True
    res = linprog(c=np.ones(len(gv)), A_ub=np.array(rows), b_ub=np.array(rhs), bounds=[(0, None)] * len(gv), method="highs")
    return res.status == 0


if a.prefix:
    run = extract(False); rows, rhs, meta = constraints(run)
    lo, hi = 0, len(run)
    while lo < hi:                      # smallest k such that steps 0..k are infeasible
        mid = (lo + hi) // 2
        idx = [i for i, m in enumerate(meta) if m[0] <= mid]
        if lp_ok([rows[i] for i in idx], [rhs[i] for i in idx]): lo = mid + 1
        else: hi = mid
    k = lo; print(f"first infeasible prefix ends at step {k}: switch {ename[run[k][2]][0]} at {names[run[k][1] + 1]}")
    print("  run so far:", " ".join(ename[e][0] for B, v, e in run[:k + 1]))
    for m, r in zip(meta, rhs):
        if m[0] == k: print(f"  step {k}: need count({m[1]}) > count({m[2]}): up({m[1]})={m[3]} up({m[2]})={m[4]} base diff {r + 1:.0f}")
    # which earlier constraints conflict with step k: drop step k's constraints one at a time? instead list all constraints involving the same pair
    for m, r in zip(meta, rhs):
        if m[0] < k: print(f"  step {m[0]} ({ename[run[m[0]][2]][0]}): need count({m[1]}) > count({m[2]}): up({m[1]})={m[3]} up({m[2]})={m[4]} base diff {r + 1:.0f}")

if a.anyrun:
    best_len = 0; best_run = None
    for smp in range(a.anyrun):
        B = rng.choice(trees); run = []
        while nxt[B]:
            cands = nxt[B]; w = [memo[x[0]] + 1 for x in cands]
            T, v, e = rng.choices(cands, weights=[x ** 2 for x in w])[0]
            run.append((B, v, e)); B = T
        if len(run) <= best_len: continue
        rows, rhs, meta = constraints(run)
        if lp_ok(rows, rhs): best_len = len(run); best_run = run; print(f"  feasible DF run of length {best_len} (sample {smp})", flush=True)
    print(f"longest pad-feasible DF run found: {best_len} (DF longest {L}) in {a.anyrun} samples")

