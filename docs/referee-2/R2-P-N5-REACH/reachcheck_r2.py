#!/usr/bin/env python3
"""P-N5-REACH machine checks (L-NEW successor 58; numpy-free). Every DATA clause of docs/new/P-N5-REACH.md §8 is one counter line here.
Sets: C14 = the 14 genomes box189/corpus/*.json (4 L-RED r187 A_* genomes, 10 L-LOWER l3/kill genomes normalised by norm.py);
R440 = 440 random IDEAL-ACYC genomes gen(Random(seed)), seed = 1..440 (gen below). Games: Gamma = gamma3.build(G, {}) (= R104's
Gamma(G)); Gamma3 = gamma3.build(G, {"K", "pe", "pb", "m"}). Engine: box21/n5x (SPEC S1-S5). IDEAL run: ideal_traj (R104's definition).
Usage: reachcheck.py            (C14 + R440 + the SUBDIV instance; ~1 min)
       reachcheck.py --approx   (also the SUBDIV-APPROX histogram; CONJECTURE data, not signed)"""
import sys, os, json, glob, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [HERE, os.path.join(ROOT, "experiments/new/box21"), os.path.join(ROOT, "experiments/new"), os.path.join(ROOT, "experiments/si"), os.path.join(ROOT, "experiments/harness")]
import gamma3, n5x, n5, pg
from si import Engine
PADS = {"K", "pe", "pb", "m"}

def chainB(G, s, x, k):
    B = []
    while True:
        B.append(G["opts"][x][k][2]); xt = G["opts"][x][k][1]
        if xt < 0: return B
        x, k = xt, s[xt]
def better(G, s, x, k, k2):
    A, B = set(chainB(G, s, x, k)), set(chainB(G, s, x, k2)); D = A ^ B
    if not D: return False
    t = max(D, key=lambda b: G["br"][b]); return (G["bp"][t] == 0) == (t in A)
def ideal_traj(G):
    N, lev, opts, gate = G["N"], G["lev"], G["opts"], G["gate"]; s = list(G["start"]); S = [tuple(s)]
    order = sorted(range(N), key=lambda x: lev[x])
    while True:
        A = [[k for k in range(len(opts[x])) if k == s[x] or better(G, s, x, k, s[x])] for x in range(N)]
        if all(len(a) == 1 for a in A): return S
        key = [None] * N; ns = list(s)
        for x in order:
            key[x], ns[x] = min(((gate[x][k],) if opts[x][k][0] < 0 else key[opts[x][k][0]] + (gate[x][k],), k) for k in A[x])
        if ns == s: return S
        s = ns; S.append(tuple(s))
def acyclic(G):
    N = G["N"]; adj = [[o[1] for o in G["opts"][x] if o[1] >= 0] for x in range(N)]; col = [0] * N
    def dfs(x):
        col[x] = 1
        for y in adj[x]:
            if col[y] == 1 or (col[y] == 0 and not dfs(y)): return False
        col[x] = 2; return True
    return all(col[x] or dfs(x) for x in range(N))
def gen(rng):
    d = rng.randint(1, 4); lev = []
    for l in range(d): lev += [l] * rng.randint(1, 3)
    N = len(lev); order = list(range(N)); rng.shuffle(order); pos = {x: i for i, x in enumerate(order)}; opts = []
    for x in range(N):
        o = []
        for k in range(rng.randint(2, 3)):
            wt = rng.choice([y for y in range(N) if lev[y] == lev[x] - 1]) if lev[x] > 0 else -1
            later = [y for y in range(N) if pos[y] > pos[x]]
            o.append([wt, rng.choice(later) if later and rng.random() < 0.7 else -1, None])
        opts.append(o)
    M = sum(len(o) for o in opts); bids = list(range(M)); rng.shuffle(bids); i = 0
    for o in opts:
        for q in o: q[2] = bids[i]; i += 1
    gl = list(range(M)); rng.shuffle(gl); i = 0; gate = []
    for o in opts: gate.append(gl[i:i + len(o)]); i += len(o)
    br = list(range(M)); rng.shuffle(br)
    return {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": [rng.randint(0, 1) for _ in range(M)],
            "start": [rng.randrange(len(o)) for o in opts]}

def playval(g, sigma, tau):
    succ = [[sigma[v]] if g.owner[v] == 0 else [tau[v]] for v in range(g.n)]
    return tuple(Engine(pg.Game(list(g.prio), list(g.owner), succ)).evaluate(tuple(sigma))[0])
def standard(g, V, G, s, pads):
    """Gamma(3)'s standard state for mover state s (R104 packet §3.1, transported through the pads)."""
    G2 = dict(G); G2["start"] = list(s); _, sig, tau, _ = gamma3.build(G2, pads)
    if "m" in pads:   # the pad priorities depend on G's start only; the standard state for s points movers at s's pads
        sig = dict(sig)
        for x in range(G["N"]): sig[x] = V[("m", (x, s[x]))]
    return sig, tau
def matches(g, state, sig, tau):
    s, t = state
    return all(s[v] == w for v, w in sig.items()) and all(t[v] == w for v, w in tau.items())

def gamma_counts(G, C):
    """NO-REACH counters on Gamma from S3."""
    g, sig0, tau0, V = gamma3.build(G, set()); N = G["N"]
    K0, K1, K2, K3, cX = V[("K", 0)], V[("K", 1)], V[("K", 2)], V[("K", 3)], V["cX"]
    betas = [v for k, v in V.items() if isinstance(k, tuple) and k[0] == "b"]
    E = Engine(g); bmask = 0
    for b in betas: bmask |= E.bit[b]
    maxb = max(E.rank[b] for b in betas)
    states, fb = n5x.trace(g, None, check=False); C["NR-RUNS"] += 1; C["NR-STATES"] += len(states)
    C.setdefault("NR-IT", {}); C["NR-IT"][len(states) - 1] = C["NR-IT"].get(len(states) - 1, 0) + 1
    for s, t in states:
        C["NR-STD"] += all(s[v] == w for v, w in sig0.items() if v >= N) and all(t[v] == w for v, w in tau0.items())
        C["NR-CORE"] += not (s[K0] == K1 and s[K1] == K0)
        vs, _ = E.evaluate(tuple(s)); C["NR-LAM"] += vs[K0][0] != K0
        C["X-NR-ALL"] = C.get("X-NR-ALL", 0) + g.n
        for v in (K2, K3, cX):
            c_, P_, _ = vs[v]; C["X-NR-EXCL-BETA-IN-P"] = C.get("X-NR-EXCL-BETA-IN-P", 0) + bool(P_ & bmask)
        for v in range(g.n):
            if v in (K2, K3, cX): continue
            C["NR-PAIRS"] += 1; c, P, _ = vs[v]
            C["NR-BETA"] += bool(P & bmask) or E.rank[c] <= maxb
    return states

def gamma3_counts(G, C, S):
    g, sig, tau, V = gamma3.build(G, PADS); L = len(S) - 1; N = G["N"]
    E, Ed = Engine(g), Engine(n5.dual(g)); s3, t3 = n5x.start_pair(g, E, Ed, None)
    C["S3-GENOMES"] += 1; C["S3-START"] += not matches(g, (s3, t3), sig, tau)
    pads = [v for k, v in V.items() if (k[0] if isinstance(k, tuple) else k) in ("pA", "s", "q", "r", "pe", "pbeta", "pb", "m")]
    pmask = 0
    for p in pads: pmask |= E.bit[p]
    states, fbs = n5x.trace(g, None, check=False); cX = V["cX"]
    # PAD on the S3 run: both worlds, every vertex but c_X
    for s, t in states:
        vs, _ = E.evaluate(tuple(s)); vt, _ = Ed.evaluate(tuple(t))
        C["X-PAD-ALL"] = C.get("X-PAD-ALL", 0) + 2 * g.n
        for vv, ww in ((vs[cX], 0), (vt[cX], 1)):
            C["X-CX-PAD-IN-P-OR-PAD-NODE"] = C.get("X-CX-PAD-IN-P-OR-PAD-NODE", 0) + (bool(vv[1] & pmask) or vv[0] in pads)
            C["X-CX-NODE-NOT-CX"] = C.get("X-CX-NODE-NOT-CX", 0) + (vv[0] != cX)
        for v in range(g.n):
            if v == cX: continue
            C["PAD-PAIRS"] += 2
            C["PAD"] += (g.prio[vs[v][0]] < 3 or bool(vs[v][1] & pmask)) + (g.prio[vt[v][0]] < 3 or bool(vt[v][1] & pmask))
    # REACH3: states 0..L standard for s_0..s_L, transitions 1..L FL, transition L+1 a fallback
    ok = len(states) >= L + 2
    W = [playval(g, s, t) for s, t in states[:L + 2]] if ok else []
    for j in range(L + 1):
        if not ok: break
        sg, tg = standard(g, V, G, S[j], PADS); ok &= matches(g, states[j], sg, tg)
    for j in range(1, L + 2):
        if not ok: break
        (s0, t0), (s1, t1) = states[j - 1], states[j]; fb = n5x.step(g, E, Ed, list(s0), list(t0))[4]
        fl = (not fb) and t0 == t1 and s0 != s1 and W[j] == W[j - 1]
        ok &= fl if j <= L else bool(fb)
    C["R3-GENOMES"] += 1; C["R3-FAIL"] += not ok; C["R3-STATES"] += L + 1
    # W3 (lengths): W at movers in every standard state 0..L equals (c_W, empty, 5 lev + 5)
    cW = V["cW"]
    for j in range(min(L + 1, len(W))):
        for x in range(N):
            C["W3-PAIRS"] += 1; c, P, ln = W[j][x]; C["W3"] += not (c == cW and P == 0 and ln == 5 * G["lev"][x] + 5)
    return L, len(states) - 1, fbs, ok

def main():
    C = {k: 0 for k in ("NR-RUNS", "NR-STATES", "NR-STD", "NR-CORE", "NR-LAM", "NR-PAIRS", "NR-BETA", "S3-GENOMES", "S3-START",
                        "PAD-PAIRS", "PAD", "R3-GENOMES", "R3-FAIL", "R3-STATES", "W3-PAIRS", "W3", "BLIND-GENOMES", "BLIND")}
    rows = []
    corpus = sorted(glob.glob(os.path.join(HERE, "corpus", "*.json")))
    for f in corpus:
        G = json.load(open(f)); assert acyclic(G); S = ideal_traj(G)
        gamma_counts(G, C); L, it, fb, ok = gamma3_counts(G, C, S)
        rows.append(f"C14 {os.path.basename(f)} N {G['N']} M {sum(len(o) for o in G['opts'])} L {L} Gamma3 n {gamma3.build(G, PADS)[0].n} "
                    f"S3-iterations {it} fallbacks {fb} REACH3 {'ok' if ok else 'FAIL'}")
    CC = dict(C); CC["NR-IT"] = dict(C["NR-IT"])
    for seed in range(1, 441):
        rng = random.Random(seed); G = gen(rng); assert acyclic(G); S = ideal_traj(G)
        st = gamma_counts(G, C); gamma3_counts(G, C, S)
        G2 = dict(G); br = list(G["br"]); rng.shuffle(br); G2["br"] = br; G2["bp"] = [rng.randint(0, 1) for _ in br]
        g2 = gamma3.build(G2, set())[0]; st2, _ = n5x.trace(g2, None, check=False)
        C["BLIND-GENOMES"] += 1; C["BLIND"] += st != st2
    for r in rows: print(r)
    for tag, D in (("C14", CC), ("C14+R440", C)):
        print(f"{tag} NO-REACH runs {D['NR-RUNS']} states {D['NR-STATES']}: standard {D['NR-STD']}, core-not-(K0->K1,K1->K0) {D['NR-CORE']}, "
              f"cycle-node(K0)!=K0 {D['NR-LAM']}; (state, vertex) pairs {D['NR-PAIRS']}: beta-in-P-or-low-cycle-node {D['NR-BETA']}; "
              f"iterations histogram {dict(sorted(D['NR-IT'].items()))}")
        print(f"{tag} S3-START genomes {D['S3-GENOMES']}: S3 != stated start {D['S3-START']}")
        print(f"{tag} PAD (state, vertex, world) triples {D['PAD-PAIRS']}: pad-in-P-or-cycle-node-Om<3 {D['PAD']}")
        print(f"{tag} REACH3 genomes {D['R3-GENOMES']} (states 0..L checked {D['R3-STATES']}): failures {D['R3-FAIL']}")
        print(f"{tag} W3 (state, mover) pairs {D['W3-PAIRS']}: W(x) != (c_W, empty, 5 lev + 5) {D['W3']}")
    print("R2X", {k: v for k, v in C.items() if k.startswith("X-")}, "NR-STATES", C["NR-STATES"])
    print(f"R440 BLIND (CONJECTURE, not signed) genomes {C['BLIND-GENOMES']}: S3 run changed by redrawing (br, bp) {C['BLIND']}")
    # SUBDIV instance (DEAD)
    import subdiv
    for tag, g, s0, t0 in (("A n 3", pg.Game([3, 3, 1], [1, 0, 1], [[1], [0, 1, 2], [0]]), {1: 1}, {0: 1, 2: 0}),
                           ("B n 5", pg.Game([3, 2, 4, 0, 0], [1, 1, 0, 1, 0], [[1, 3, 4], [2, 3], [3, 4], [0, 2, 3], [1, 4]]),
                            {2: 4, 4: 1}, {0: 4, 1: 2, 3: 2})):
        A, fa = n5x.trace(g, (s0, t0), check=False); h, P = subdiv.pad(g, s0, t0); B, fb = n5x.trace(h, None, check=False)
        inv = {p: b for (a, b), p in P.items()}
        Bp = [tuple(inv[s[v]] if g.owner[v] == 0 else inv[t[v]] for v in range(g.n)) for s, t in B]
        Ap = [tuple(s[v] if g.owner[v] == 0 else t[v] for v in range(g.n)) for s, t in A]
        print(f"SUBDIV-DEAD instance {tag}: G from (s0, t0): iterations {len(A) - 1} fallbacks {fa}; G^pad (n {h.n}) from S3: "
              f"iterations {len(B) - 1} fallbacks {fb}; S3 start = transported (s0, t0) {Bp[0] == Ap[0]}; projected state sequences equal {Ap == Bp}")
    if "--approx" in sys.argv:
        from collections import Counter
        H = Counter(); tot = 0
        for seed, cnt, nmax in ((7, 400, 10), (8, 150, 16)):
            rng = random.Random(seed)
            for i in range(cnt):
                g = subdiv.rgame(rng, rng.randint(3, nmax))
                s0 = {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}; t0 = {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}
                A, _ = n5x.trace(g, (s0, t0), check=False); h, _ = subdiv.pad(g, s0, t0); B, _ = n5x.trace(h, None, check=False)
                H[(len(B) - 1) - (len(A) - 1)] += 1; tot += 1
        print(f"SUBDIV-APPROX (CONJECTURE, not signed) games {tot}: T(G^pad from S3) - T(G from (s0, t0)) histogram {dict(sorted(H.items()))}")

if __name__ == "__main__":
    main()
