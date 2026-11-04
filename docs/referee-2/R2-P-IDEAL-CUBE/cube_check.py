#!/usr/bin/env python3
r"""REFEREE-2 successor 26 (Opus 5.5, D15): own check of packet P-IDEAL-CUBE (docs/new/P-IDEAL-CUBE.md, sha1 366afedc @ l-new d97555d4).
Written from the packet text. Model and values: my own R2-P-IDEAL-RED/ideal_check.Gen (Xi-values as SETS, top-rank rule; keys under the
new state). The lane's box153/decomp.py, box153/longpath.py and box154/ladder.py are NOT imported.
Checks (violation counters, all must be 0):
  ORI   (o) o(b)_x != o(b + e_x)_x for every vertex and degree-2 coordinate
  USO   (a) every face (all 3^|D2| of them) has exactly one sink
  COMB  (c) in every face of dim >= 1, the free coordinate of largest pi is combed (for 3 random topological orders)
  ACYC  (b) the orientation has no directed cycle (Kahn on the whole cube)
  MS    MULTI->SINGLE: each step's movers, switched in increasing pi, give directed edges ending at s_t; T <= sum |Mv_t| <= LP(s_0)
  LAD   LADDER-LP: L_K built from §4; the UP procedure's path: every switch directed, length 2^(K+1)-2, consecutive; DP LP(b_0) (K <= 8)
  LADF  facts F0-F3 at every state of the path
Usage: cube_check.py random COUNT NMAX DMAX SEED | files G.json ... | ladder KMAX"""
import sys, os, json, random, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "R2-P-IDEAL-RED"))
import ideal_check as IC
from collections import deque

class St(IC.St): pass

def cube(G):
    g = IC.Gen(G); D2 = [x for x in range(g.N) if g.deg[x] == 2]
    base = [0] * g.N
    def state(bits):
        s = list(base)
        for i, x in enumerate(D2): s[x] = (bits >> i) & 1
        return tuple(s)
    def C(s, x): return 0 if g.better(g.val(s, x, 0), g.val(s, x, 1)) else 1
    n = len(D2); out = {}
    for bits in range(1 << n):
        s = state(bits); out[bits] = sum(1 << i for i, x in enumerate(D2) if s[x] != C(s, x))
    return g, D2, out, state

def LP(out, n, start):
    """longest directed path from start (acyclic: memoised DFS order via Kahn reverse)"""
    succ = {b: [b ^ (1 << i) for i in range(n) if out[b] >> i & 1] for b in out}
    indeg = {b: 0 for b in out}
    for b in out:
        for c in succ[b]: indeg[c] += 1
    q = deque(b for b in out if indeg[b] == 0); order = []
    while q:
        b = q.popleft(); order.append(b)
        for c in succ[b]:
            indeg[c] -= 1
            if indeg[c] == 0: q.append(c)
    if len(order) < len(out): return None
    best = {}
    for b in reversed(order): best[b] = max([1 + best[c] for c in succ[b]], default=0)
    return best[start]

def check_genome(G, st, name, rng, runs=True):
    g, D2, out, state = cube(G); n = len(D2); st.inc("genomes"); st.inc("vertices", 1 << n)
    for b in out:
        for i in range(n):
            if (out[b] >> i & 1) == (out[b ^ (1 << i)] >> i & 1): st.bad("ORI", name)
    pis = IC.topo_orders(G, rng, 3)
    for free in range(1, 1 << n):          # faces: free mask, fixed values on the rest
        fixed_bits = [i for i in range(n) if not free >> i & 1]
        for fv in range(1 << len(fixed_bits)):
            basev = 0
            for j, i in enumerate(fixed_bits):
                if fv >> j & 1: basev |= 1 << i
            fr = [i for i in range(n) if free >> i & 1]; verts = []
            for sub in range(1 << len(fr)):
                v = basev
                for j, i in enumerate(fr):
                    if sub >> j & 1: v |= 1 << i
                verts.append(v)
            sinks = sum(1 for v in verts if out[v] & free == 0)
            if sinks != 1: st.bad("USO", f"{name} face {free}:{fv}")
            for pi in pis:
                y = max(fr, key=lambda i: pi[D2[i]])
                dirs = {(v >> y & 1, out[v] >> y & 1) for v in verts}
                if len({d[0] ^ d[1] for d in dirs}) != 1: st.bad("COMB", f"{name}")
            st.inc("faces")
    st.inc("faces0", 1 << n)   # dimension-0 faces trivially have one sink
    if LP(out, n, 0) is None: st.bad("ACYC", name); return
    if not runs: return
    idx = {x: i for i, x in enumerate(D2)}
    def bits_of(s): return sum((s[x] & 1) << i for x, i in idx.items())
    for s0 in itertools.product(*[range(d) for d in g.deg]):
        S, _ = g.run(list(s0)); T = len(S) - 1; tot = 0
        for t in range(1, T + 1):
            Mv = sorted([x for x in range(g.N) if S[t][x] != S[t - 1][x]], key=lambda x: pis[0][x])
            b = bits_of(S[t - 1])
            for x in Mv:
                if not out[b] >> idx[x] & 1: st.bad("MS", f"{name} step {t} x={x}")
                b ^= 1 << idx[x]
            if b != bits_of(S[t]): st.bad("MS", f"{name} end of step {t}")
            tot += len(Mv)
        lp = LP(out, n, bits_of(S[0]))
        if not (T <= tot <= lp): st.bad("MS", f"{name} T {T} sum {tot} LP {lp}")
        st.inc("runs"); st.inc("steps", T); st.inc("LP_sum", lp)

def ladder(K):
    """L_K from packet §4. Movers: u_i = 2i, v_i = 2i+1. ranks: pair i gets ranks 4(K-1-i) .. 4(K-1-i)+3 (pair 0 the top four)."""
    N = 2 * K; opts = []; br = []; bp = []; gate = []; M = 0
    rank = {}
    for i in range(K):
        r0 = 4 * (K - 1 - i)
        if i == 0: order = [(0, 0), (1, 0), (0, 1), (1, 1)]   # (mover u=0/v=1, option): u0,0 < v0,0 < u0,1 < v0,1
        else: order = [(0, 0), (0, 1), (1, 0), (1, 1)]        # u_i,0 < u_i,1 < v_i,0 < v_i,1
        for j, (m, k) in enumerate(order): rank[(2 * i + m, k)] = r0 + j
    for x in range(N):
        i = x // 2; o = []
        for k in range(2):
            xt = -1 if i == 0 else (2 * (i - 1) if k == 0 else 2 * (i - 1) + 1)
            o.append([-1, xt, M]); br.append(rank[(x, k)]); bp.append(0); M += 1
        opts.append(o); gate.append([2 * x, 2 * x + 1])
    start = [0, 0] + [1] * (N - 2)
    return dict(N=N, lev=[0] * N, opts=opts, gate=gate, br=br, bp=bp, start=start)

def check_ladder(K, st):
    G = ladder(K); g = IC.Gen(G); N = g.N
    def C(s, x): return 0 if g.better(g.val(s, x, 0), g.val(s, x, 1)) else 1
    def B(s, j): return 0 if g.better(g.val(s, 2 * j, s[2 * j]), g.val(s, 2 * j + 1, s[2 * j + 1])) else 1
    s = list(G["start"]); path = [tuple(s)]
    def sw(x):
        if s[x] == C(s, x): st.bad("LAD", f"K={K} non-improving switch of {x}")
        s[x] ^= 1; path.append(tuple(s))
    def facts():
        for j in range(K):
            u, v = 2 * j, 2 * j + 1
            if j == 0:
                if C(s, u) != 1 or C(s, v) != 1: st.bad("LADF", "F0 C")
                want = {(0, 0): 1, (1, 1): 1, (1, 0): 0}.get((s[u], s[v]))
                if want is not None and B(s, 0) != want: st.bad("LADF", "F0 B")
            else:
                if C(s, u) != B(s, j - 1) or C(s, v) != B(s, j - 1): st.bad("LADF", "F1")
                if s[u] == s[v] and B(s, j) != 1: st.bad("LADF", "F2")
                if s[u] != s[v] and (B(s, j) == 0) != (s[u] == B(s, j - 1)): st.bad("LADF", "F3")
    def UP(i, b):
        facts(); u, v = 2 * i, 2 * i + 1
        if s[u] != b or s[v] != b: st.bad("LAD", f"UP({i}) precondition")
        sw(u); facts()
        if i + 1 <= K - 1: UP(i + 1, 1)
        sw(v); facts()
        if i + 1 <= K - 1: UP(i + 1, 0)
    facts(); sw(0)
    if K >= 2: UP(1, 1)
    sw(1)
    if K >= 2: UP(1, 0)
    facts()
    L = len(path) - 1
    if L != 2 ** (K + 1) - 2: st.bad("LAD", f"K={K} length {L}")
    if len(set(path)) != len(path): st.bad("LAD", f"K={K} repeated vertex")
    lp = None
    if K <= 8:
        _, D2, out, _ = cube(G); lp = LP(out, len(D2), sum((G["start"][x] & 1) << x for x in range(N)))
        if lp is None or lp < L: st.bad("LAD", f"K={K} DP {lp}")
    S, _ = g.run(G["start"])
    print(f"LADDER K {K} N {N} path {L} target {2 ** (K + 1) - 2} DP_LP {lp} ideal_T {len(S) - 1}")
    st.inc("ladders")

def main():
    a = sys.argv[1:]; st = St(); rng = random.Random(154)
    if a[0] == "ladder":
        for K in range(1, int(a[1]) + 1): check_ladder(K, st)
    elif a[0] == "random":
        cnt, Nmax, dmax, seed = map(int, a[1:5]); r = random.Random(seed)
        for i in range(cnt):
            G = IC.rand_genome(r, Nmax, dmax, 2)
            if sum(1 for o in G["opts"] if len(o) == 2) <= 8: check_genome(G, st, f"r{seed}_{i}", rng, runs=G["N"] <= 8)
    else:
        for f in a[1:]:
            G = json.load(open(f))
            if max(len(o) for o in G["opts"]) <= 2 and sum(1 for o in G["opts"] if len(o) == 2) <= 9:
                check_genome(G, st, os.path.basename(f), rng, runs=G["N"] <= 9)
            else: st.inc("skipped_files")
    viol = {k: v for k, v in st.c.items() if k.startswith("VIOL_")}
    print("CUBE-CHECK", " ".join(f"{k} {v}" for k, v in sorted(st.c.items()) if not k.startswith("VIOL_")))
    print("VIOLATIONS", sum(viol.values()), " ".join(f"{k[5:]} {v}" for k, v in sorted(viol.items())))
    for k, m in st.ex.items(): print("  first", k, m)

if __name__ == "__main__":
    main()
