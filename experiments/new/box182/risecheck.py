#!/usr/bin/env python3
"""L-NEW box 182 (packet P-IDEAL-RISE): frozen checks. Deterministic (seed 182); simulator box150/check.py (Gen); no numpy / scipy.
 PHIK : PHIK-DESCENT, Phi_K(s) - Phi_K(step(s)) >= 1 at every step s -> step(s) != s on L^R_d. Scope: every state of 200 random L^R_d
        genomes (d 1-4; box162 rand_lr, iso and non-iso), and every step of the runs from the stored start of the in-tree L^R_d genome
        files of experiments/new/box150 .. box181 (corpus frozen: never add genome JSON under those boxes).
 OPTK : OPT-K forcing transitions tau(l, p) built by the packet's construction (§3) for d = 1..8, every l, both p; checks that the first
        step moves p only, that k(p) goes 1 -> 0, both level-(l+1) movers go k 0 -> 1, no other k bit changes; and that the
        all-misaligned and all-aligned states exist (built level by level) in each tau genome.
 RISE : RISE-EQUIV (a) no option value falls, (b) R(x, k) <= T, (c) T <= 1 + #{t <= T-1 with a rise} <= 1 + sum R; MOVE-RISE: every
        move of z strictly raises cv(z). Scope: the corpus runs above and the stored-start runs of the 200 random genomes.
 CERT : exact rational check of the four pinned LP certificates in box182/cert (features recomputed here in Fractions, multipliers
        re-solved exactly on the certificate's support, nonnegativity and dual equalities checked; every genome checked in L^R_d and
        Xi-acyclic). Prints the exact bound.
Usage: risecheck.py   (run from experiments/new or anywhere)"""
import os, sys, json, random, itertools, glob
from fractions import Fraction as Fr
H = os.path.dirname(os.path.abspath(__file__)); P0 = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": P0, "__name__": "lib"}; exec(open(P0).read().split("\nif __name__")[0], ns); Gen, topo = ns["Gen"], ns["topo"]
fl = {"__file__": os.path.join(H, "..", "box162", "flipcheck.py"), "__name__": "lib"}; exec(open(fl["__file__"]).read().split("\nif __name__")[0], fl)
rand_lr, is_lr = fl["rand_lr"], fl["is_lr"]

def kbits(g, s):
    K = g.keys(s); return [int(s[x] != min((0, 1), key=lambda j: g.optkey(K, x, j))) for x in range(g.N)]
def phik(g, d, s): return sum(((1 << (d - x // 2)) - 1) * b for x, b in enumerate(kbits(g, s)))
def acyclic(G):
    try: return len(topo(G)) == G["N"]
    except Exception: return False

# ---------------- corpus and random genomes
ROOT = os.path.join(H, "..")
files = []
for b in range(150, 182):
    for f in sorted(glob.glob(os.path.join(ROOT, "box%d" % b, "**", "*.json"), recursive=True)):
        try: G = json.load(open(f))
        except Exception: continue
        if isinstance(G, dict) and "opts" in G and "start" in G and is_lr(G) and acyclic(G): files.append((os.path.relpath(f, ROOT), G))
rng = random.Random(182); RG = [rand_lr(rng.randint(1, 4), rng, iso=rng.random() < 0.3) for _ in range(200)]
C = dict(PHIK=0, OPTK=0, RISE_A=0, RISE_B=0, RISE_C=0, MOVERISE=0, CERT=0)
N_ = dict(corpus_files=len(files), random=len(RG), phik_steps=0, phik_tight=0, optk_transitions=0, rise_runs=0, rise_moves=0)

# ---------------- PHIK
def phik_step(g, d, s):
    n, _ = g.step(s)
    if n is None: return
    a, b = phik(g, d, s), phik(g, d, n); N_["phik_steps"] += 1; N_["phik_tight"] += a - b == 1
    if a - b < 1: C["PHIK"] += 1
for G in RG:
    g = Gen(G); d = G["N"] // 2
    for s in itertools.product((0, 1), repeat=2 * d): phik_step(g, d, tuple(s))
for _, G in files:
    g = Gen(G); d = G["N"] // 2; S, _ = g.run(tuple(G["start"]))
    for s in S: phik_step(g, d, s)

# ---------------- OPT-K construction (packet §3)
def tau(d, l, p):
    N = 2 * d; q = p ^ 1; lev = [x // 2 for x in range(N)]
    gates = {}; nxt = [0]
    def newg():
        nxt[0] += 10; return nxt[0]
    s = [0] * N
    G = {"N": N, "lev": lev, "opts": [[[2 * (lev[x] - 1) + k if lev[x] else -1, -1, 2 * x + k] for k in (0, 1)] for x in range(N)],
         "gate": [[None, None] for _ in range(N)], "br": [0] * (2 * N), "bp": [0] * (2 * N), "start": None}
    # gates level by level; the level-l pair's gates are placed to force the flip; all others increasing (any distinct values work)
    for x in range(N):
        if lev[x] != l: G["gate"][x] = [newg(), newg()]
    def cur_keys(st): return Gen(dict(G, gate=[gg if None not in gg else [0, 0] for gg in G["gate"]])).keys(st)
    # states below l: all option 0; level l: q aligned, p misaligned; level l+1: both aligned; above: option 0
    if l == 0:
        # keys at level 0 are the gates: p on its higher-gate option, q's current gate strictly between p's two gates
        a, mid, b_ = newg(), newg(), newg(); G["gate"][p] = [b_, a]; G["gate"][q] = [mid, newg()]; s[p] = 0; s[q] = 0
    else:
        Kb = cur_keys(s)  # lower levels fixed (option 0 everywhere below l); c_l from the order of the lower pair
        c = 0 if Kb[2 * l - 2] < Kb[2 * l - 1] else 1; s[q] = c; s[p] = 1 - c
        # before: ord(2l, 2l+1) = [s(2l) = c] (different options); after p moves to c: ord = gamma_l(c) = [g(2l, c) < g(2l+1, c)]
        before = int(s[2 * l] == c); g1, g2 = newg(), newg(); G["gate"][2 * l] = [None, None]; G["gate"][2 * l + 1] = [None, None]
        lo, hi = (g1, g2) if before == 0 else (g2, g1)  # want gamma_l(c) = 1 - before
        G["gate"][2 * l][c] = lo; G["gate"][2 * l + 1][c] = hi; G["gate"][2 * l][1 - c] = newg(); G["gate"][2 * l + 1][1 - c] = newg()
    if l + 1 < d:
        Kb = Gen(G).keys(s); c1 = 0 if Kb[2 * l] < Kb[2 * l + 1] else 1; s[2 * l + 2] = s[2 * l + 3] = c1
    # ranks: the option s(x) is the better one (larger rank, even parity) at every x != p; at p the other option is better
    for x in range(N):
        best = (1 - s[x]) if x == p else s[x]
        for k in (0, 1): G["br"][2 * x + k] = 2 * x + (1 if k == best else 0)
    G["start"] = list(s); return G
def extreme(g, N, want):  # state with every k bit = want, built level by level from the bottom
    s = [0] * N
    for x in sorted(range(N), key=lambda x: x // 2):
        K = g.keys(tuple(s)); kp = min((0, 1), key=lambda j: g.optkey(K, x, j)); s[x] = kp if want == 0 else 1 - kp
    return tuple(s)
for d in range(1, 9):
    for l in range(d):
        for p in (2 * l, 2 * l + 1):
            G = tau(d, l, p); g = Gen(G); s = tuple(G["start"]); n, _ = g.step(s); ok = n is not None and is_lr(G) and acyclic(G)
            if ok:
                k0, k1 = kbits(g, s), kbits(g, n); mv = [x for x in range(2 * d) if n[x] != s[x]]; ok = mv == [p]
                for x in range(2 * d):
                    if x == p: ok &= k0[x] == 1 and k1[x] == 0
                    elif l + 1 < d and x // 2 == l + 1: ok &= k0[x] == 0 and k1[x] == 1
                    else: ok &= k0[x] == k1[x]
                ok &= set(kbits(g, extreme(g, 2 * d, 1))) == {1} and set(kbits(g, extreme(g, 2 * d, 0))) == {0}
            N_["optk_transitions"] += 1; C["OPTK"] += not ok

# ---------------- RISE-EQUIV, MOVE-RISE
def rise_run(G, st):
    g = Gen(G); S, _ = g.run(tuple(st)); T = len(S) - 1; N = G["N"]; N_["rise_runs"] += 1
    opts = [(x, k) for x in range(N) for k in range(len(G["opts"][x]))]
    V = [[g.face(s, x, k) for (x, k) in opts] for s in S]; R = [0] * len(opts); rs = 0
    for t in range(1, T + 1):
        anyr = False
        for i in range(len(opts)):
            if V[t][i] > V[t - 1][i]: R[i] += 1; anyr = True
            elif V[t][i] < V[t - 1][i]: C["RISE_A"] += 1
        rs += anyr and t <= T - 1
        for z in range(N):
            if S[t][z] != S[t - 1][z]:
                N_["rise_moves"] += 1
                if not g.face(S[t], z, S[t][z]) > g.face(S[t - 1], z, S[t - 1][z]): C["MOVERISE"] += 1
    if max(R + [0]) > T: C["RISE_B"] += 1
    if not (T <= 1 + rs <= 1 + sum(R)) and T >= 1: C["RISE_C"] += 1
for _, G in files: rise_run(G, G["start"])
for G in RG: rise_run(G, G["start"])

# ---------------- CERT
def xheight(G):
    h = {}
    def hh(v):
        if v < 0: return 0
        if v not in h: h[v] = 1 + max(hh(o[1]) for o in G["opts"][v])
        return h[v]
    return [hh(v) for v in range(G["N"])]
def pathvals(g, G, x, memo):
    if x not in memo:
        out = set()
        for k in range(len(G["opts"][x])):
            e = g.eps(x, k); xt = G["opts"][x][k][1]
            out |= {e} if xt < 0 else {e + w for w in pathvals(g, G, xt, memo)}
        memo[x] = sorted(out)
    return memo[x]
def feats(cls, G, s):
    """the feature classes of docs/new/P-IDEAL-RISE.md §5 (identical to experiments/new/box179/lpot.py, classes P, H, X, B, G)"""
    g = Gen(G); N = G["N"]; d = N // 2; K = g.keys(s); hx = xheight(G); memo = {}; F = {}
    z = [int(g.face(s, x, 1 - s[x]) > g.face(s, x, s[x])) for x in range(N)]
    k = [int(s[x] != min((0, 1), key=lambda j: g.optkey(K, x, j))) for x in range(N)]
    if "B" in cls or "G" in cls:
        for x in range(N):
            pv = pathvals(g, G, x, memo); ic, io = pv.index(g.face(s, x, s[x])), pv.index(g.face(s, x, 1 - s[x])); P = len(pv)
            if "B" in cls:
                F["bud%d" % x] = Fr(P - 1 - ic); F["budn%d" % x] = Fr(P - 1 - ic, max(1, P - 1))
                F["budL%d" % (x // 2)] = F.get("budL%d" % (x // 2), 0) + (P - 1 - ic)
            if "G" in cls:
                F["gap%d" % x] = Fr(io - ic); F["gapp%d" % x] = Fr(max(0, io - ic)); F["gapn%d" % x] = Fr(max(0, io - ic), max(1, P - 1))
                F["kgapp%d" % x] = Fr(k[x] * max(0, io - ic))
    for x in range(N):
        l = x // 2; F["z%d" % x] = z[x]; F["k%d" % x] = k[x]; F["u%d" % x] = z[x] & k[x]
        if "H" in cls:
            F["zH%d_%d" % (l, hx[x])] = F.get("zH%d_%d" % (l, hx[x]), 0) + z[x]
            F["uH%d_%d" % (l, hx[x])] = F.get("uH%d_%d" % (l, hx[x]), 0) + (z[x] & k[x])
    for l in range(d):
        p, q = 2 * l, 2 * l + 1
        if "P" in cls: F["pair%d_%d%d%d%d" % (l, k[p], k[q], z[p], z[q])] = 1; F["ord%d" % l] = int(K[p] < K[q])
        if "X" in cls and l + 1 < d:
            for a in (p, q):
                for b in (2 * l + 2, 2 * l + 3): F["zk%d_%d" % (a, b)] = z[a] * k[b]; F["kz%d_%d" % (a, b)] = k[a] * z[b]
    return {key: Fr(v) for key, v in F.items()}
def certcheck(path):
    c = json.load(open(path)); cls, d = c["cls"], c["d"]; cols = []; bad = 0
    for r in c["dec"] + c["lo"] + c["hi"]:
        G = r["genome"]
        if not (is_lr(G) and G["N"] == 2 * d and acyclic(G)): bad += 1
    for r in c["dec"]:
        g = Gen(r["genome"]); n, _ = g.step(tuple(r["s"]))
        if n is None or list(n) != r["next"]: bad += 1; continue
        a, b = feats(cls, r["genome"], tuple(r["s"])), feats(cls, r["genome"], n)
        v = {key: a.get(key, 0) - b.get(key, 0) for key in set(a) | set(b)}; v["__b"] = Fr(0); cols.append(("dec", r["y"], v))
    for tag, sg in (("lo", 1), ("hi", -1)):
        for r in c[tag]:
            a = feats(cls, r["genome"], tuple(r["s"])); v = {key: sg * x for key, x in a.items()}; v["__const"] = Fr(sg)
            v["__b"] = Fr(1 if tag == "hi" else 0); cols.append((tag, r["y"], v))
    rows = sorted(set(key for _, _, v in cols for key in v)); n = len(cols)
    A = [[cols[j][2].get(key, Fr(0)) for j in range(n)] + [Fr(1) if key == "__b" else Fr(0)] for key in rows]
    piv, r0 = [], 0
    for col in range(n):
        pr = next((i for i in range(r0, len(A)) if A[i][col] != 0), None)
        if pr is None: continue
        A[r0], A[pr] = A[pr], A[r0]; pv = A[r0][col]; A[r0] = [x / pv for x in A[r0]]
        for i in range(len(A)):
            if i != r0 and A[i][col] != 0:
                f = A[i][col]; A[i] = [x - f * y for x, y in zip(A[i], A[r0])]
        piv.append(col); r0 += 1
    incons = any(all(x == 0 for x in row[:n]) and row[n] != 0 for row in A)
    free = [j for j in range(n) if j not in piv]; val = [None] * n
    for j in free: val[j] = Fr(cols[j][1]).limit_denominator(10 ** 6)
    for i, col in enumerate(piv): val[col] = A[i][n] - sum(A[i][j] * val[j] for j in free)
    neg = sum(1 for j in range(n) if val[j] < 0); bound = sum(val[j] for j in range(n) if cols[j][0] == "dec")
    ok = bad == 0 and not incons and neg == 0 and len(free) == 0
    C["CERT"] += not ok
    print("CERT %s class %s d %d rows %d (dec %d lo %d hi %d) bad %d inconsistent %s negative %d free %d bound %.6f%s %s" % (
        os.path.basename(path), cls, d, n, len(c["dec"]), len(c["lo"]), len(c["hi"]), bad, incons, neg, len(free), float(bound),
        " (= %s)" % bound, "CERTIFIED" if ok else "NOT CERTIFIED"))
for f in ("cert_PHX_d3_s1793.json", "cert_PBG_d2_s179.json", "cert_PBG_d3_s1793.json", "cert_PBG_d4_s1794.json"):
    certcheck(os.path.join(H, "cert", f))
print("SCOPE " + " ".join("%s %d" % kv for kv in N_.items()))
print(" ".join("%s %d" % kv for kv in C.items()))
