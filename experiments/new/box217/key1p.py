#!/usr/bin/env python3
"""Packet P-N5-KEY1P (L-NEW successor 77): DATA tool for docs/new/P-N5-KEY1P.md. One line of counters per genome.
The model 1P(G) is one217.OneP (key rule); every counter below must be 0 unless a control is on.
  ideq   the key run of 1P(G) differs from R104's reference IDEAL simulator (experiments/red/r187/ideal.traj) at some state, or in length
  l0     Lemma 0 (c): at some state two options of one mover have equal value (integer weight), or one217's (weight, hops) pair order
         on the options of one mover differs from the integer order
  a1mu   A1 (mu): mu_(t+1)(x) > mu_t(x), or x switches at t and mu_(t+1)(x) is not < mu_t(x)
  a1v    A1 (V): V_(t+1)(x) < V_t(x), or x switches at t and V_(t+1)(x) is not > V_t(x)
  a2     A2: sw(x) > min(|K(x)|, |PXi(x)|) - 1, or T > sum_x sw(x), or max_x sw(x) > T
  a3     A3: a degree-2 mover with equal W-targets (or of level 0) or with equal Xi-targets that switches more than once
  a4h    A4 (i)-(ii): a mover x with sw(x) = |K(x)| - 1 whose mu(x) changes at a step where x does not switch, or misses a key of K(x),
         or one of whose options k has mu(wt(x, k)) missing a key of K(wt(x, k))
  a4x    A4 (iii): a degree-2 mover with sw(x) > 1 + XF_x (XF_x: the number of t in [1, T] at which the order of x's two option values
         differs from the order at t - 1); in particular sw(x) = |K(x)| - 1 with XF_x < |K(x)| - 2
With --n5 (slow): mism (the key run differs from N5 itself, n5v spec from S3 on Gamma3(G) (box 189), read at the movers, state by state
  up to N5's first fallback) and nofb (N5's transition T + 1 is NOT a fallback: Theorem RED-1P's F = T_key + 1).
Also printed (not counters): T, N, M, D, mindeg, maxsw, k (1 + the largest level of a mover with |K| >= 2 and sw = |K| - 1; 0 if
  none) and k34 (the same with sw + 1 >= |K|^(3/4)); k and k34 are the packet's diagnostics only when mindeg >= 2 (with degree-1 movers
  they can grow while T stays fixed: --lift); with --levels one line per level: the largest sw of a level-l mover and its |K| - 1.
Controls (KEY1P_CTRL): perm  = the keys of 1P use a fixed random permutation of the gate indices (seed 5): ideq (and mism) must fire;
  howard = the Howard rule in place of KEY: a1mu must fire;   down = every mover with an option outside A_s(x) takes one: a1v must fire;
  a2half = A2 tested with |K(x)| / 2 in place of |K(x)|: a2 must fire;   a3all = A3's test on every degree-2 mover: a3 must fire;
  a4any  = A4 (i)-(ii) tested on every mover with sw >= 1, A4 (iii) as XF_x >= |K(x)| - 2 on every degree-2 mover: a4h, a4x must fire;
  w0     = every beta weight of 1P set to 0 (all option values equal): l0 must fire;
  fbearly (with --n5) = N5's fallback flag read at transition T instead of T + 1: nofb must fire (the flag is not constantly set).
Random sets: --rand SEED COUNT = eg195.gen "acyc" (box 195; short runs); --randlad SEED COUNT = climb217.rand_genome with w in {2, 3}
  movers per level, d in 3..8 levels, degree in {2, 3}, random W-targets one level down, random acyclic Xi-targets (longer runs).
  --mut SEED COUNT G.json ... = COUNT genomes per file, each the genome with 1 to 4 random mutations of climb217.mutate (one option's
  W-target or Xi-target, a beta-rank swap, a parity flip, a gate swap, a start flip; Xi-acyclic kept): long runs off the hand-built towers.
  --lift D G.json ... = LIFT(G, D) (REFEREE-2 41's family): a chain of D degree-1 movers c_0, ..., c_(D-1) (level i, W-target c_(i-1),
  Xi-target the exit, a new beta of even parity ranked above every old one, a new gate index above every old one, start 0) put under G:
  every old level-0 option gets W-target c_(D-1) and every old level rises by D. T and every sw are those of G; k grows by D.
Usage: key1p.py [--n5] [--levels] G.json ... | key1p.py [--n5] --rand SEED COUNT | key1p.py [--n5] --randlad SEED COUNT
       | key1p.py [--n5] --mut SEED COUNT G.json ... | key1p.py [--n5] --lift D G.json ..."""
import sys, os, json, random, collections
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [HERE, os.path.join(ROOT, "experiments", "red", "r187"), os.path.join(ROOT, "experiments", "new", "box195")]
os.environ.setdefault("EG195_ROOT", ROOT)
CTRL = os.environ.get("KEY1P_CTRL", "")
if CTRL == "perm": os.environ["ONE217_CTRL"] = "1"
import one217, ideal
NAMES = ["ideq", "l0", "a1mu", "a1v", "a2", "a3", "a4h", "a4x"]

def sizes(G):
    """|K(x)| and |PXi(x)| (exact integers), and the key set K(x) as a count only"""
    N, lev, opts = G["N"], G["lev"], G["opts"]; K = [0] * N; P = [None] * N
    for x in sorted(range(N), key=lambda x: lev[x]):
        K[x] = len(opts[x]) if lev[x] == 0 else sum(K[wt] for (wt, _, _) in opts[x])
    def px(x):
        if P[x] is None: P[x] = sum(1 if y < 0 else px(y) for (_, y, _) in opts[x])
        return P[x]
    for x in range(N): px(x)
    return K, P

def keys_of(P, s):
    """mu_s(x) for every mover: root-first tuple of (possibly permuted) gate indices"""
    mu = {}
    for x in P.bylev:
        wt = P.opts[x][s[x]][0]
        mu[x] = (mu[wt] if wt >= 0 and P.lev[x] > 0 else ()) + (P.gate[x][s[x]],)
    return mu

def down_step(P, s):
    """control: every mover with an option outside A_s(x) takes the first one"""
    _, ov = P.values(s); t = list(s); ch = False
    for x in range(P.N):
        out = [k for k in range(len(P.opts[x])) if k != s[x] and ov[(x, k)] < ov[(x, s[x])]]
        if out: t[x] = out[0]; ch = True
    return tuple(t) if ch else None

def run(P, G):
    if CTRL == "howard": return P.run("howard")
    if CTRL == "down":
        s = tuple(G["start"]); S = [s]
        for _ in range(3):
            t = down_step(P, s)
            if t is None: break
            s = t; S.append(s)
        return S
    return P.run("key")

def n5run(G):
    """N5 (n5v spec) from S3 on Gamma3(G): mover states up to the first fallback, and whether the run ended in a fallback"""
    sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box215")); os.environ.setdefault("KM_MODE", "spec")
    import keyside215 as ks
    g0, _, _, V = ks.gamma3.build(G, ks.eg195.PADS); g = ks.eg195.topg(g0)
    E, Ed = ks.n5v.Engine(g), ks.n5v.Engine(ks.n5v.dual(g)); sigma, tau = ks.n5x.start_pair(g, E, Ed, None)
    S = [tuple(ks.gamma3.mover_state(G, V, sigma, ks.eg195.PADS))]; flags = []
    while len(S) <= 20000:
        res = ks.n5v.step(g, E, Ed, sigma, tau, "spec")
        if res is None: break
        flags.append(bool(res[4]))
        if res[4]: break
        sigma, tau = list(res[0]), list(res[1]); S.append(tuple(ks.gamma3.mover_state(G, V, sigma, ks.eg195.PADS)))
    T = len(S) - 1                                    # flags[j - 1] = «transition j is a fallback», j = 1..len(flags)
    if CTRL == "fbearly": return S, (T >= 1 and flags[T - 1])
    return S, (len(flags) == T + 1 and flags[T])

def one(G, n5=False, levels=None):
    c = collections.Counter(); N, lev, opts = G["N"], G["lev"], G["opts"]
    P = one217.OneP(G)
    if CTRL == "w0": P.bw = {b: 0 for b in P.bw}
    S = run(P, G); T = len(S) - 1; K, PX = sizes(G)
    if CTRL in ("", "perm", "a2half", "a3all", "a4any"):
        R, _ = ideal.traj(G); c["ideq"] += int([tuple(r) for r in R] != S)
    sw = [0] * N; xf = [0] * N; seenmu = [set() for _ in range(N)]; quiet = [0] * N
    mu = keys_of(P, S[0]); mv, ov = P.values(S[0])
    def order2(ov, x): return ov[(x, 0)][0] > ov[(x, 1)][0]
    for x in range(N):
        seenmu[x].add(mu[x]); w = [ov[(x, k)] for k in range(len(opts[x]))]
        c["l0"] += int(len({v[0] for v in w}) < len(w)) + int(sorted(range(len(w)), key=lambda k: w[k]) != sorted(range(len(w)), key=lambda k: w[k][0]))
    for t in range(T):
        mu2 = keys_of(P, S[t + 1]); mv2, ov2 = P.values(S[t + 1])
        for x in range(N):
            moved = S[t + 1][x] != S[t][x]; sw[x] += moved
            c["a1mu"] += int(mu2[x] > mu[x] or (moved and not mu2[x] < mu[x]))
            c["a1v"] += int(mv2[x][0] < mv[x][0] or (moved and not mv2[x][0] > mv[x][0]))
            quiet[x] += int(mu2[x] != mu[x] and not moved); seenmu[x].add(mu2[x])
            w = [ov2[(x, k)] for k in range(len(opts[x]))]
            c["l0"] += int(len({v[0] for v in w}) < len(w)) + int(sorted(range(len(w)), key=lambda k: w[k]) != sorted(range(len(w)), key=lambda k: w[k][0]))
            if len(opts[x]) == 2: xf[x] += int(order2(ov2, x) != order2(ov, x))
        mu, mv, ov = mu2, mv2, ov2
    for x in range(N):
        kb = K[x] // 2 if CTRL == "a2half" else K[x]
        c["a2"] += int(sw[x] > min(kb, PX[x]) - 1)
        if len(opts[x]) == 2:
            (wa, ya, _), (wb, yb, _) = opts[x]
            hyp = lev[x] == 0 or wa == wb or ya == yb
            c["a3"] += int((hyp or CTRL == "a3all") and sw[x] > 1)
            c["a4x"] += int(sw[x] > 1 + xf[x]) + int(CTRL == "a4any" and xf[x] < K[x] - 2)
        if (sw[x] == K[x] - 1) or (CTRL == "a4any" and sw[x] >= 1):
            bad = quiet[x] > 0 or len(seenmu[x]) != K[x]
            if lev[x] > 0: bad = bad or any(len(seenmu[wt]) != K[wt] for (wt, _, _) in opts[x])
            c["a4h"] += int(bad)
    c["a2"] += int(T > sum(sw)) + int(max(sw, default=0) > T)
    full = [lev[x] for x in range(N) if K[x] >= 2 and sw[x] == K[x] - 1]
    c34 = [lev[x] for x in range(N) if K[x] >= 2 and (sw[x] + 1) ** 4 >= K[x] ** 3]
    info = {"N": N, "M": sum(len(o) for o in opts), "D": max(len(o) for o in opts), "mindeg": min(len(o) for o in opts), "T": T,
            "k": 1 + max(full) if full else 0, "k34": 1 + max(c34) if c34 else 0, "maxsw": max(sw, default=0)}
    if n5:
        R, fb = n5run(G); info["n5"] = len(R) - 1; c["mism"] += int(R != S); c["nofb"] += int(not fb)
    if levels is not None:
        for l in sorted(set(lev)):
            xs = [x for x in range(N) if lev[x] == l]; b = max(xs, key=lambda x: (sw[x], -K[x]))
            levels.append(f"level {l} maxsw {sw[b]} of |K|-1 {K[b] - 1} movers {len(xs)}")
    return c, info

def lift(G, D):
    H = json.loads(json.dumps(G)); N = H["N"]; M = len(H["br"]); gmax = max(v for row in H["gate"] for v in row)
    if D == 0: return H
    for x in range(N):
        if H["lev"][x] == 0:
            for o in H["opts"][x]: o[0] = N + D - 1
        H["lev"][x] += D
    for i in range(D):
        H["opts"].append([[N + i - 1 if i else -1, -1, M + i]]); H["lev"].append(i); H["gate"].append([gmax + 1 + i])
        H["br"].append(M + i); H["bp"].append(0); H["start"].append(0)
    H["N"] = N + D
    return H

def line(name, c, info, n5):
    names = NAMES + (["mism", "nofb"] if n5 else [])
    return f"{name} " + " ".join(f"{k} {info[k]}" for k in info) + " | " + " ".join(f"{k} {c[k]}" for k in names) + f" ctrl {CTRL or 0}"

if __name__ == "__main__":
    a = sys.argv[1:]; n5 = "--n5" in a; lv = "--levels" in a; a = [x for x in a if x not in ("--n5", "--levels")]
    if a and a[0] in ("--rand", "--randlad"):
        import eg195, climb217
        seed, cnt = int(a[1]), int(a[2]); rng = random.Random(seed); tot = collections.Counter(); k = 0; mx = 0; sumT = 0
        while k < cnt:
            G = eg195.gen(rng, "acyc") if a[0] == "--rand" else climb217.rand_genome(rng, rng.choice([2, 3]), rng.randrange(3, 9), rng.choice([2, 3]))
            if G is None or G["N"] < 2: continue
            k += 1; c, info = one(G, n5); tot.update(c); mx = max(mx, info["T"]); sumT += info["T"]
        names = NAMES + (["mism", "nofb"] if n5 else [])
        print(f"{a[0][2:]} seed {seed} genomes {k} maxT {mx} sumT {sumT} | " + " ".join(f"{n} {tot[n]}" for n in names) + f" ctrl {CTRL or 0}", flush=True)
    elif a and a[0] == "--lift":
        D = int(a[1])
        for fn in a[2:]:
            G = json.load(open(fn)); G = lift(G.get("genome", G), D); c, info = one(G, n5)
            print(line(f"lift {D} {os.path.basename(fn)}", c, info, n5), flush=True)
    elif a and a[0] == "--mut":
        import climb217
        seed, cnt = int(a[1]), int(a[2]); names = NAMES + (["mism", "nofb"] if n5 else [])
        for fn in a[3:]:
            G0 = json.load(open(fn)); G0 = G0.get("genome", G0); rng = random.Random(seed); tot = collections.Counter(); k = 0; mx = 0; sumT = 0
            while k < cnt:
                G = G0
                for _ in range(rng.randrange(1, 5)):
                    H = climb217.mutate(rng, G)
                    if H is not None: G = H
                k += 1; c, info = one(G, n5); tot.update(c); mx = max(mx, info["T"]); sumT += info["T"]
            print(f"mut {os.path.basename(fn)} seed {seed} genomes {k} maxT {mx} sumT {sumT} | " + " ".join(f"{n} {tot[n]}" for n in names) + f" ctrl {CTRL or 0}", flush=True)
    else:
        for fn in a:
            G = json.load(open(fn)); G = G.get("genome", G); L = [] if lv else None
            c, info = one(G, n5, L); print(line(os.path.basename(fn), c, info, n5), flush=True)
            for l in L or []: print(f"  {os.path.basename(fn)} {l}", flush=True)
