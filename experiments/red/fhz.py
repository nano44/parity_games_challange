#!/usr/bin/env python3
r"""L-RED: Friedmann-Hansen-Zwick shortest-path lower bound for Random-Facet (arXiv 1410.7530, section 5 Table 1, Thm 6.3)
and its transfer to sink parity games.

Weighted graph G_{n,r,s,t} (Table 1, eps = 1/(rs); all costs here are scaled by rs to integers):
  a_{i,j,k} -> a_{i,j,k+1} (0, 'a1'), -> u_{i+1} (2^{2i+1} + (k-1) eps, 'a0', t copies);  a_{i,j,s} -> b_{i,1} (0)
  b_{i,j} -> b_{i,j+1} (0, 'b1'), -> u_{i+1} (2^{2i+1} + 1 + (j-1) eps, 'b0', t copies);  b_{i,rs} -> w_{i+1} (0)
  u_i -> b_{i,1} (0, 'u1', t copies), -> u_{i+1} (2^{2i}, 'u0', t copies)
  w_i -> a_{i,j,1} (0, 'w' j, t copies), -> w_{i+1} (2^{2i}, 'w0', t copies);  target t = u_{n+1} = w_{n+1}.
Initial tree B0: FHZ's 'zero-edges' = the bit-0 edges a0, b0, u0, w0 (the NON-zero-cost ones; p.14: 'any tree composed
entirely of one-edges is optimal'), first copy of each.  Random-Facet (errata 1410.7871 section 2 / Zwick 2607.06334
Fig. 1): RF(F, B): pick a uniformly random e in F \ B, B' = RF(F \ {e}, B); if e improves B' then RF(F, B'[e]) else B'.

Parity encoding P (one player, sink 0 of priority 1, Odd, self-loop; every other vertex Even):
  structural vertices a, b, u, w: priority 0 (below the sink: never in a path set; they only count in the length);
  every edge copy x -> y becomes x -> m (priority 0, one relay per copy) -> [class vertex] -> y, with the class vertices
  SHARED by every entry into the level (see build()): class A (the 0-cost chain exit b_{i,rs} -> w_{i+1}) -> even g_i of
  priority base_i + 4rs; class B (u0_i, w0_i, cost 2^{2i}) -> no class vertex; class C (escape with offset d in [0, 2rs))
  -> odd o_{i,d} of priority base_i + 1 + 2d; base_i = 2 + (i-1)(4rs+2).  Level-i sets A {g_i} > B {} > C {o_{i,d}} for Even,
  so the path-set order is lexicographic by level on the class {0, 2^{2i}, 2^{2i+1}+delta}, then by delta within a level,
  which is exactly how the path costs of G compare (docs/red/R2-RAR.md, Transfer Lemma).
Usage: fhz.py lockstep n r s t seeds   |   fhz.py table n_list r s t seeds   |   fhz.py export n r s t out.pg (prints start)"""
import sys, random
sys.setrecursionlimit(1 << 20)


class Weighted:
    """vertices 0..N-1 (target = N-1); edges: list of (src, dst, cost); out[v] = edge ids."""
    def __init__(self, N, edges):
        self.N = N; self.edges = edges; self.out = [[] for _ in range(N)]
        for i, (s, d, c) in enumerate(edges):
            self.out[s].append(i)

    def values(self, B):
        """B: dict vertex -> edge id (tree). Returns dist[v] (acyclic graph: memoised walk)."""
        dist = {self.N - 1: 0}
        def d(v):
            if v in dist: return dist[v]
            s, w, c = self.edges[B[v]]; dist[v] = c + d(w); return dist[v]
        for v in range(self.N - 1): d(v)
        return dist

    def improving(self, B, vals, e):
        s, w, c = self.edges[e]
        return c + vals[w] < vals[s]            # strictly shorter


class Parity:
    """one-player sink parity game; value of v = (set of odd-priority vertices on the path as a bitmask over ranks, length).
    Better for Even: lexicographically smaller set (the max of the symmetric difference is odd, so the set without it wins),
    then LONGER path (odd cycle node).  edge id -> (src, first gadget vertex); strategy = choice per Even vertex."""
    def __init__(self, prio, succ, edge_src, edge_head):
        self.prio = prio; self.succ = succ; self.N = len(prio); self.edge_src = edge_src; self.edge_head = edge_head
        order = sorted(range(self.N), key=lambda v: (prio[v], v)); self.rank = [0] * self.N
        for r, v in enumerate(order): self.rank[v] = r
        self.bit = [(1 << self.rank[v]) if prio[v] >= 2 else 0 for v in range(self.N)]   # priority-0 vertices invisible
        self.sgn = [(1 if prio[v] % 2 == 0 else -1) * self.bit[v] for v in range(self.N)]  # signed weight: even good

    def values(self, B):
        """B: dict edge-src vertex -> edge id. Other Even vertices have a single successor."""
        val = {0: (0, 0)}
        def f(v):
            if v in val: return val[v]
            w = self.edge_head[B[v]] if v in B else self.succ[v][0]
            S, L = f(w); val[v] = (S + self.sgn[v], L + 1); return val[v]
        for v in range(self.N): f(v)
        return val

    def improving(self, B, vals, e):
        s = self.edge_src[e]; S1, L1 = vals[self.edge_head[e]]; S0, L0 = vals[s]
        S1 += self.sgn[s]; L1 += 1                 # value of s if it used e
        if S1 != S0: return S1 > S0               # larger signed weight = better for Even (1106.0778 set order)
        return L1 > L0                            # equal sets: longer is better (odd cycle node)


def build(n, r, s, t):
    """Returns (Weighted G, Parity P, B0 dict, names, meta) with common edge ids."""
    names = []; vid = {}
    def V(name):
        if name not in vid: vid[name] = len(names); names.append(name)
        return vid[name]
    T = V("t")
    for i in range(1, n + 1):
        V(f"u{i}"); V(f"w{i}")
        for j in range(1, r + 1):
            for k in range(1, s + 1): V(f"a{i},{j},{k}")
        for j in range(1, r * s + 1): V(f"b{i},{j}")
    U = lambda i: T if i == n + 1 else vid[f"u{i}"]; W = lambda i: T if i == n + 1 else vid[f"w{i}"]
    A = lambda i, j, k: vid[f"a{i},{j},{k}"]; Bv = lambda i, j: vid[f"b{i},{j}"]
    rs = r * s; edges = []; ename = []
    def E(src, dst, cost, name, copies):
        for l in range(copies):
            edges.append((src, dst, cost)); ename.append((name, l))
    for i in range(1, n + 1):
        big = rs * (1 << (2 * i + 1)); small = rs * (1 << (2 * i))
        for j in range(1, r + 1):
            for k in range(1, s + 1):
                E(A(i, j, k), A(i, j, k + 1) if k < s else Bv(i, 1), 0, f"a1_{i},{j},{k}", 1)
                E(A(i, j, k), U(i + 1), big + (k - 1), f"a0_{i},{j},{k}", t)
        for j in range(1, rs + 1):
            E(Bv(i, j), Bv(i, j + 1) if j < rs else W(i + 1), 0, f"b1_{i},{j}", 1)
            E(Bv(i, j), U(i + 1), big + rs + (j - 1), f"b0_{i},{j}", t)
        E(U(i), Bv(i, 1), 0, f"u1_{i}", t); E(U(i), U(i + 1), small, f"u0_{i}", t)
        for j in range(1, r + 1):
            E(W(i), A(i, j, 1), 0, f"w{j}_{i}", t)
        E(W(i), W(i + 1), small, f"w0_{i}", t)
    N = len(names)
    # target last: renumber so that t = N-1 (Weighted assumes it)
    perm = list(range(1, N)) + [0]; inv = {old: new for new, old in enumerate(perm)}
    edgesW = [(inv[s_], inv[d_], c) for s_, d_, c in edges]
    G = Weighted(N, edgesW)
    B0 = {}
    for v in range(N - 1):
        costly = [e for e in G.out[v] if G.edges[e][2] > 0]
        B0[v] = costly[0]
    # ---- parity encoding ----
    # level i band: base_i = 2 + (i-1)(4rs+2); class C escape with offset d in [0, 2rs) -> shared odd vertex o_{i,d} of
    # priority base_i + 1 + 2d (-> u_{i+1}); class A (the 0-cost chain exit b_{i,rs} -> w_{i+1}) -> shared EVEN vertex g_i of
    # priority base_i + 4rs (-> w_{i+1}); class B (u0_i, w0_i, cost 2^{2i}) -> no cost vertex.  Level-i sets: A {g_i} > B {} >
    # C {o_{i,d}} for Even, identical for every entry into the level, so two paths with the same class sequence are compared
    # by the single within-level offset where they merge, exactly as the costs of G compare.
    prio = [1]; succ = [[0]]; pid = {}          # parity vertex 0 = sink = target
    def PV(key, p):
        if key not in pid: pid[key] = len(prio); prio.append(p); succ.append([])
        return pid[key]
    for v in range(N - 1): PV(("v", v), 0)
    edge_src = [None] * len(edges); edge_head = [None] * len(edges)
    def classify(c):
        for i in range(1, n + 1):
            if c == rs * (1 << (2 * i)): return i, "B", 0
            if rs * (1 << (2 * i + 1)) <= c < rs * (1 << (2 * i + 1)) + 2 * rs: return i, "C", c - rs * (1 << (2 * i + 1))
        raise ValueError(c)
    base = lambda i: 2 + (i - 1) * (4 * rs + 2)
    for e, (s_, d_, c) in enumerate(edgesW):
        src = pid[("v", s_)] if s_ != N - 1 else 0; dst = pid[("v", d_)] if d_ != N - 1 else 0
        m = PV(("m", e), 0)
        nm = ename[e][0]
        if c == 0:
            if nm.startswith("b1_") and d_ != s_ and (d_ == N - 1 or names[perm[d_]].startswith("w")):   # chain exit to w_{i+1}
                i = int(nm[3:].split(",")[0]); g = PV(("g", i), base(i) + 4 * rs); succ[g] = [dst]; succ[m] = [g]
            else:
                succ[m] = [dst]
        else:
            i, cls, d = classify(c)
            if cls == "B":
                succ[m] = [dst]
            else:
                o = PV(("o", i, d), base(i) + 1 + 2 * d); succ[o] = [dst]; succ[m] = [o]
        succ[src].append(m); edge_src[e] = src; edge_head[e] = m
    P = Parity(prio, succ, edge_src, edge_head)
    B0P = {pid[("v", v)]: e for v, e in B0.items()}
    return G, P, B0, B0P, names, ename, pid


class RF:
    """Random-Facet driver; models: list of (model, tree). All models receive the same random edge sequence; every
    improving test must agree (lockstep), otherwise AssertionError."""
    def __init__(self, G, trees, rng, m):
        self.G = G; self.models = list(zip(G, trees)); self.rng = rng; self.m = m; self.switches = 0; self.tests = 0

    def run(self):
        F = set(range(self.m)); trees = [dict(t) for _, t in self.models]
        return self._rf(F, trees)

    def _rf(self, F, trees):
        inB = set(trees[0].values())
        cand = sorted(F - inB)
        if not cand: return trees
        e = self.rng.choice(cand)
        F.discard(e); trees2 = self._rf(F, trees); F.add(e)
        verdicts = []
        for (model, _), B in zip(self.models, trees2):
            vals = model.values(B); verdicts.append(model.improving(B, vals, e))
        self.tests += 1
        assert all(v == verdicts[0] for v in verdicts), f"models disagree on edge {e}: {verdicts}"
        if verdicts[0]:
            src = self.models[0][0].edges[e][0] if hasattr(self.models[0][0], "edges") else self.models[0][0].edge_src[e]
            new = []
            for (model, _), B in zip(self.models, trees2):
                B = dict(B); s = model.edges[e][0] if hasattr(model, "edges") else model.edge_src[e]; B[s] = e; new.append(B)
            self.switches += 1
            return self._rf(F, new)
        return trees2


def export_pg(P, B0P, names, path):
    with open(path, "w") as f:
        f.write(f"parity {P.N - 1};\n")
        for v in range(P.N):
            f.write(f"{v} {P.prio[v]} {1 if v == 0 else 0} {','.join(map(str, P.succ[v]))};\n")
    return "spec:" + " ".join(f"{v}:{P.edge_head[e]}" for v, e in sorted(B0P.items()))


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "lockstep":
        n, r, s, t, seeds = map(int, sys.argv[2:7])
        G, P, B0, B0P, names, ename, pid = build(n, r, s, t)
        for seed in range(seeds):
            drv = RF([G, P], [B0, B0P], random.Random(seed), len(G.edges)); drv.run()
            print(f"n={n} r={r} s={s} t={t} seed={seed}: {drv.switches} switches, {drv.tests} improving tests, models agree "
                  f"(|V|={G.N}, |E|={len(G.edges)}, parity |V|={P.N})")
    elif cmd == "table":
        ns = [int(x) for x in sys.argv[2].split(",")]; r, s, t, seeds = map(int, sys.argv[3:7])
        for n in ns:
            G, P, B0, B0P, names, ename, pid = build(n, r, s, t)
            xs = []
            for seed in range(seeds):
                drv = RF([G], [B0], random.Random(seed), len(G.edges)); drv.run(); xs.append(drv.switches)
            print(f"n={n} r={r} s={s} t={t}: |V|={G.N} |E|={len(G.edges)} parity|V|={P.N} mean switches {sum(xs)/len(xs):.1f} "
                  f"max {max(xs)} min {min(xs)} (seeds {seeds})", flush=True)
    elif cmd == "export":
        n, r, s, t = map(int, sys.argv[2:6]); G, P, B0, B0P, names, ename, pid = build(n, r, s, t)
        print(export_pg(P, B0P, names, sys.argv[6]))


# ---- extra checks ------------------------------------------------------------------------------------------------
class VJModel:
    """Third model for the lockstep: the exported parity game evaluated by the generic VJ engine (experiments/red/vj.py)."""
    def __init__(self, P, B0P):
        import vj
        self.P = P; self.e = vj.VJ(list(P.prio), [1 if v == 0 else 0 for v in range(P.N)], [list(s) for s in P.succ])
        self.edge_src = P.edge_src; self.edge_head = P.edge_head

    def values(self, B):
        sigma = [-1 if v == 0 else self.P.succ[v][0] for v in range(self.P.N)]
        for v, e in B.items(): sigma[v] = self.edge_head[e]
        val, tau = self.e.evaluate(tuple(sigma)); return [self.e.key(x) for x in val]

    def improving(self, B, vals, e):
        return vals[self.edge_head[e]] > vals[self.edge_src[e]] and not (vals[self.edge_head[e]] == vals[self.edge_src[e]])


def relation_check(n, r, s, t, samples, seed=0):
    """Random functional F (every multi-edge keeps >= 1 copy, every vertex keeps an out-edge) and random tree B in F:
    the sets of improving edges of B within F must coincide in G and P."""
    import vj
    G, P, B0, B0P, names, ename, pid = build(n, r, s, t); rng = random.Random(seed); bad = 0; tot = 0
    groups = {}
    for e, (nm, l) in enumerate(ename): groups.setdefault(nm, []).append(e)
    for _ in range(samples):
        F = set()
        for nm, es in groups.items():
            k = rng.randint(1, len(es)); F.update(rng.sample(es, k))
        B = {}; BP = {}
        for v in range(G.N - 1):
            e = rng.choice([x for x in G.out[v] if x in F]); B[v] = e; BP[P.edge_src[e]] = e
        vg = G.values(B); vp = P.values(BP)
        ig = {e for e in F if e not in B.values() and G.improving(B, vg, e)}
        ip = {e for e in F if e not in B.values() and P.improving(BP, vp, e)}
        tot += 1; bad += (ig != ip)
    return tot, bad


if __name__ == "__main__" and sys.argv[1] == "relation":
    n, r, s, t, samples = map(int, sys.argv[2:7]); tot, bad = relation_check(n, r, s, t, samples)
    print(f"relation n={n} r={r} s={s} t={t}: {tot} random (F, B) pairs, improving sets differ in {bad}")
if __name__ == "__main__" and sys.argv[1] == "lockstep3":
    n, r, s, t, seeds = map(int, sys.argv[2:7]); sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
    G, P, B0, B0P, names, ename, pid = build(n, r, s, t); V = VJModel(P, B0P)
    for seed in range(seeds):
        drv = RF([G, P, V], [B0, B0P, dict(B0P)], random.Random(seed), len(G.edges)); drv.run()
        print(f"lockstep3 n={n} r={r} s={s} t={t} seed={seed}: {drv.switches} switches, {drv.tests} tests, all three models agree")
