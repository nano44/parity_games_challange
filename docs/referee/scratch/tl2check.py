#!/usr/bin/env python3 -I
"""REFEREE scratch tool for R-TL2 (L-RED transfer lemma, docs/red/R2-RAR.md at claude/l-red 0d50d4a).
My own code: G_{n,r,s,t} from FHZ arXiv 1410.7530 Table 1 (costs scaled by rs to integers; eps = 1/(rs)); the sink parity
encoding P as described in R2-RAR.md (relay per edge copy; class A -> shared even g_i; class B -> nothing; class C offset
d -> shared odd o_{i,d}; bands by level); the VJ valuation of a 1-player sink game from Friedmann 1106.0778 section 3
(set of priority->=2 vertices on the path, Friedmann's set order via the max of the symmetric difference, then LONGER is
better because the sink is odd); EXHAUSTIVE check over ALL trees B of G and all non-tree edges e: the three-way verdict
(e better / tie / worse than B(x)) must agree in G and in P.  Also: my own Random-Facet (errata 1410.7871 Fig. 1) on G and
my own Rand-Act-Rem (Zwick 2607.06334 Fig. 1) on P fed the same random stream must perform the same switches.
Optionally the same exhaustive check on the LANE's objects (experiments/red/fhz.py build(), its G and P and improving()).
Usage: tl2check.py exhaustive n r s t [LANE_RED_DIR] | tl2check.py lockstep n r s t seeds"""
import sys, os, random, itertools

def build_G(n, r, s, t):
    """vertices: names; edges: list of (src, dst, cost, name). t = target. Returns (names, edges, out)."""
    names = ["t"]; vid = {"t": 0}
    def V(nm):
        if nm not in vid: vid[nm] = len(names); names.append(nm)
        return vid[nm]
    for i in range(1, n + 1):
        V(f"u{i}"); V(f"w{i}")
        for j in range(1, r + 1):
            for k in range(1, s + 1): V(f"a{i}_{j}_{k}")
        for j in range(1, r * s + 1): V(f"b{i}_{j}")
    rs = r * s
    U = lambda i: 0 if i == n + 1 else vid[f"u{i}"]; W = lambda i: 0 if i == n + 1 else vid[f"w{i}"]
    edges = []
    def E(src, dst, cost, nm, copies):
        for l in range(copies): edges.append((src, dst, cost, nm, l))
    for i in range(1, n + 1):
        big = rs * 2 ** (2 * i + 1); small = rs * 2 ** (2 * i)
        for j in range(1, r + 1):
            for k in range(1, s + 1):
                nxt = vid[f"a{i}_{j}_{k+1}"] if k < s else vid[f"b{i}_1"]
                E(vid[f"a{i}_{j}_{k}"], nxt, 0, f"a1_{i},{j},{k}", 1)
                E(vid[f"a{i}_{j}_{k}"], U(i + 1), big + (k - 1), f"a0_{i},{j},{k}", t)      # 2^{2i+1} + (k-1) eps
        for j in range(1, rs + 1):
            nxt = vid[f"b{i}_{j+1}"] if j < rs else W(i + 1)
            E(vid[f"b{i}_{j}"], nxt, 0, f"b1_{i},{j}", 1)
            E(vid[f"b{i}_{j}"], U(i + 1), big + rs + (j - 1), f"b0_{i},{j}", t)             # 2^{2i+1} + 1 + (j-1) eps
        E(vid[f"u{i}"], vid[f"b{i}_1"], 0, f"u1_{i}", t); E(vid[f"u{i}"], U(i + 1), small, f"u0_{i}", t)
        for j in range(1, r + 1): E(vid[f"w{i}"], vid[f"a{i}_{j}_1"], 0, f"w{j}_{i}", t)
        E(vid[f"w{i}"], W(i + 1), small, f"w0_{i}", t)
    out = [[] for _ in names]
    for e, (src, dst, c, nm, l) in enumerate(edges): out[src].append(e)
    return names, edges, out

def build_P(n, r, s, t, names, edges):
    """My encoding. For each G-edge e: gadget = list of P-vertices (priorities) traversed before reaching dst:
    [relay(0)] or [relay(0), class vertex]. Class vertices are shared: key -> priority. Returns gadget[e] = (count of
    P-vertices, frozenset of class keys), prio of class keys, with all class priorities distinct and >= 2."""
    rs = r * s; prio = {}
    base = lambda i: 2 + (i - 1) * (4 * rs + 2)
    gadget = []
    for (src, dst, c, nm, l) in edges:
        cls = frozenset()
        if c == 0:
            if nm.startswith("b1_") and names[dst].startswith("w") or (nm.startswith("b1_") and dst == 0 and nm.split(",")[1] == str(rs)):
                i = int(nm[3:].split(",")[0]); key = ("g", i); prio[key] = base(i) + 4 * rs; cls = frozenset([key])
        else:
            i = None
            for ii in range(1, n + 1):
                if c == rs * 2 ** (2 * ii): i, kind, d = ii, "B", 0
                if rs * 2 ** (2 * ii + 1) <= c < rs * 2 ** (2 * ii + 1) + 2 * rs: i, kind, d = ii, "C", c - rs * 2 ** (2 * ii + 1)
            assert i is not None
            if kind == "C":
                key = ("o", i, d); prio[key] = base(i) + 1 + 2 * d; cls = frozenset([key])
        gadget.append((1 + len(cls), cls))     # relay + class vertex
    assert len(set(prio.values())) == len(prio) and all(p >= 2 for p in prio.values())
    return gadget, prio

def better_set(M, N, prio):
    """Friedmann set order for Even: M better than N iff max(M Δ N) is (even and in M) or (odd and in N). 0 if equal."""
    D = M ^ N
    if not D: return 0
    top = max(D, key=lambda k: prio[k])
    good = (prio[top] % 2 == 0)
    return 1 if (top in M) == good else -1

def values(names, edges, out, gadget, B):
    """tree B: dict vertex -> edge id. dist[v] (G), and val[v] = (class set, length) for the P-path from v (v's own
    P-vertex counted; the sink not counted)."""
    N = len(names); dist = {0: 0}; val = {0: (frozenset(), 0)}
    order = []
    def go(v):
        if v in dist: return
        src, dst, c, nm, l = edges[B[v]]
        go(dst)
        dist[v] = c + dist[dst]
        cnt, cls = gadget[B[v]]; S, L = val[dst]; val[v] = (S | cls, L + 1 + cnt)
    for v in range(1, N): go(v)
    return dist, val

def verdict_G(edges, dist, B, e):
    src, dst, c, nm, l = edges[e]; new = c + dist[dst]; old = dist[src]
    return 1 if new < old else (0 if new == old else -1)

def verdict_P(edges, gadget, val, B, e, prio):
    src, dst, c, nm, l = edges[e]
    cnt, cls = gadget[e]; S1, L1 = val[dst]; S1 = S1 | cls; L1 = L1 + cnt
    cnt0, cls0 = gadget[B[src]]; S0, L0 = val[edges[B[src]][1]]; S0 = S0 | cls0; L0 = L0 + cnt0
    b = better_set(S1, S0, prio)
    if b: return b
    return 1 if L1 > L0 else (0 if L1 == L0 else -1)     # sink odd: longer is better for Even

def all_trees(names, out):
    N = len(names)
    for choice in itertools.product(*[out[v] for v in range(1, N)]):
        yield {v + 1: e for v, e in enumerate(choice)}

def exhaustive(n, r, s, t, lane=None):
    names, edges, out = build_G(n, r, s, t); gadget, prio = build_P(n, r, s, t, names, edges)
    trees = tests = 0; mism = 0; ties = 0
    for B in all_trees(names, out):
        trees += 1
        dist, val = values(names, edges, out, gadget, B)
        inB = set(B.values())
        for e in range(len(edges)):
            if e in inB: continue
            vg = verdict_G(edges, dist, B, e); vp = verdict_P(edges, gadget, val, B, e, prio)
            tests += 1; ties += (vg == 0)
            if vg != vp:
                mism += 1
                if mism <= 3: print(f"  MISMATCH tree {B} edge {edges[e][3]}#{edges[e][4]}: G {vg} P {vp}")
    print(f"mine: (n,r,s,t)=({n},{r},{s},{t}) |V|={len(names)} |E|={len(edges)} trees {trees} tests {tests} (ties in G {ties}) mismatches {mism}", flush=True)
    if lane:
        sys.path.insert(0, lane); import fhz
        G, P, B0, B0P, lnames, ename, pid = fhz.build(n, r, s, t)
        # map my edges to the lane's by (name, copy)
        lid = {k: e for e, k in enumerate(ename)}
        emap = [lid[(nm, l)] for (src, dst, c, nm, l) in edges]
        # the lane's G must have the same (src name, dst name, cost) per edge name
        inv = {}
        for e, (nm, l) in enumerate(ename):
            s_, d_, c_ = G.edges[e]
            inv[(nm, l)] = (lnames[list(range(1, G.N)) [s_]] if s_ < G.N - 1 else "t", lnames[list(range(1, G.N))[d_]] if d_ < G.N - 1 else "t", c_)
        mism2 = 0; trees2 = 0; tests2 = 0
        for B in all_trees(names, out):
            trees2 += 1
            LB = {}; LBP = {}
            for v, e in B.items():
                le = emap[e]; LB[G.edges[le][0]] = le; LBP[P.edge_src[le]] = le
            vg = G.values(LB); vp = P.values(LBP)
            inB = set(LB.values())
            for le in range(len(G.edges)):
                if le in inB: continue
                tests2 += 1
                ig = G.improving(LB, vg, le); ip = P.improving(LBP, vp, le)
                if ig != ip:
                    mism2 += 1
                    if mism2 <= 3: print(f"  LANE MISMATCH edge {ename[le]}: G {ig} P {ip}")
        print(f"lane objects: trees {trees2} tests {tests2} improving-verdict mismatches {mism2}", flush=True)

# ---- Random-Facet on G (errata Fig. 1) and Rand-Act-Rem on P (Zwick Fig. 1), same random stream ----
def random_facet(edges, out, names, gadget, prio, F, B, rng, log):
    inB = set(B.values()); cand = sorted(F - inB)
    if not cand: return B
    e = rng.choice(cand)
    B1 = random_facet(edges, out, names, gadget, prio, F - {e}, B, rng, log)
    dist, _ = values(names, edges, out, gadget, B1)
    if verdict_G(edges, dist, B1, e) == 1:
        B2 = dict(B1); B2[edges[e][0]] = e; log.append(e)
        return random_facet(edges, out, names, gadget, prio, F, B2, rng, log)
    return B1

def rand_act_rem(edges, out, names, gadget, prio, H, a, rng, log):
    """Zwick Fig. 1 on the sink game P: actions = relay edges of the G-vertices (every other Even vertex has one action).
    r random action not in a; b = RAR(H minus r, a); c = b[r]; if VAL_c prec VAL_b (b better: r not improving) return b, else RAR(H, c)."""
    ina = set(a.values()); cand = sorted(H - ina)
    if not cand: return a
    rr = rng.choice(cand)
    b = rand_act_rem(edges, out, names, gadget, prio, H - {rr}, a, rng, log)
    _, val = values(names, edges, out, gadget, b)
    if verdict_P(edges, gadget, val, b, rr, prio) == 1:       # VAL_b prec VAL_c: r improving
        c = dict(b); c[edges[rr][0]] = rr; log.append(rr)
        return rand_act_rem(edges, out, names, gadget, prio, H, c, rng, log)
    return b

def lockstep(n, r, s, t, seeds):
    sys.setrecursionlimit(100000)
    names, edges, out = build_G(n, r, s, t); gadget, prio = build_P(n, r, s, t, names, edges)
    B0 = {v: [e for e in out[v] if edges[e][2] > 0][0] for v in range(1, len(names))}     # zero-edges = costly, first copy
    F = set(range(len(edges)))
    for seed in range(seeds):
        lg, lp = [], []
        BG = random_facet(edges, out, names, gadget, prio, F, dict(B0), random.Random(seed), lg)
        BP = rand_act_rem(edges, out, names, gadget, prio, F, dict(B0), random.Random(seed), lp)
        same = (lg == lp) and (BG == BP)
        print(f"lockstep ({n},{r},{s},{t}) seed {seed}: RF switches {len(lg)}, RAR switches {len(lp)}, identical sequence and final tree: {same}")
        assert same
        # final tree optimal in G?
        dist, _ = values(names, edges, out, gadget, BG)
        for e in range(len(edges)):
            assert verdict_G(edges, dist, BG, e) != 1, "RF ended non-optimal"

if __name__ == "__main__":
    if sys.argv[1] == "exhaustive":
        n, r, s, t = map(int, sys.argv[2:6]); exhaustive(n, r, s, t, sys.argv[6] if len(sys.argv) > 6 else None)
    else:
        n, r, s, t, seeds = map(int, sys.argv[2:7]); lockstep(n, r, s, t, seeds)
