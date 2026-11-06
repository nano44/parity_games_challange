#!/usr/bin/env python3
"""L-NEW box 172 (packet P-IDEAL-KEYS): machine checks of the key-side lemmas on IDEAL-ACYC runs (RESULTS R104 model; simulator
box150/check.py Gen, whose step rule is the R104 step: A-sets under the old state, keys under the new state, lowest level first).
Checks (counts are violations unless named as a control):
  LOCALKP  key_s(x, k) = key_s'(x, k) for all k when s, s' agree on W(x)            [random state pairs, every mover]
  LOCALCTL control: s' agrees on W(x) minus one mover y with s'(y) != s(y) -> some key differs (must be > 0)
  KFWE     KF_x <= WE_x on every run
  PAIRKF   degree-2 mover x of level >= 1: KF_x = flips(wt(x,0), wt(x,1)) (0 if the two W-targets are equal)
  CASCADE  every flip of a same-level pair at step t is (own) or (below) with the stated conditions
  LADDER   on R197 ladders (2-wide, degree 2): F(l) <= moves(2l) + moves(2l+1) + F(l-1), F(0) <= moves(0) + moves(1)
  FLET     flips(p, q) <= T
  RENEW    top-only step t >= 2: every h in Mv_t: w not in A_(s_(t-2))(h), value of (h, w) rose at step t-1, Z_t nonempty
  RENEWB   on a maximal top-only interval [a, b], KP of every top mover is the same at s_(a-1), ..., s_b
  MERGE    random states: the order of (x, a), (x, b) is unchanged when s is changed off the two pre-merge prefixes
  MERGECTL control: changing one pre-merge prefix mover changes the difference v(x,a) - v(x,b) somewhere (must be > 0)
  RETURN   degree-2 x, consecutive moves t_(i-1) < t_i: cv(xt(x, o')) rose strictly between s_(t_(i-1)-1) and s_(t_i - 1)
  RETCNT   moves(x) <= 1 + R(x, 0) + R(x, 1) at degree 2
  KEYFLIP  moves(x) <= 1 + KF_x on degree-<=-2 genomes (R105, sanity)
Then the DEAD instances: PM (KILL_PM_compose_dd_d5_F14, mover 12), PMV (dd_d5_F14, mover 6), tower (dd_d5_F14 level-3 pair F = T).
Usage: keycheck.py   (no arguments; deterministic)"""
import os, sys, json, glob, random
H = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": P, "__name__": "lib"}; exec(open(P).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]; topo = ns["topo"]

def wclos(G):
    N = G["N"]; out = []
    for x in range(N):
        seen, st = set(), [o[0] for o in G["opts"][x] if o[0] >= 0]
        while st:
            y = st.pop()
            if y not in seen: seen.add(y); st.extend(o[0] for o in G["opts"][y] if o[0] >= 0)
        out.append(seen)
    return out

def xdesc(G):
    N = G["N"]; out = []
    for x in range(N):
        seen, st = set(), [o[1] for o in G["opts"][x] if o[1] >= 0]
        while st:
            y = st.pop()
            if y not in seen: seen.add(y); st.extend(o[1] for o in G["opts"][y] if o[1] >= 0)
        out.append(seen)
    return out

def kp(g, key, x): return min(range(len(g.opts[x])), key=lambda k: g.optkey(key, x, k))

def acyclic(G):
    try: topo(G); return True
    except Exception: return False

def valid(G):
    if not ("N" in G and "opts" in G and "gate" in G and "br" in G and "bp" in G and "lev" in G): return False
    N = G["N"]
    for x in range(N):
        for o in G["opts"][x]:
            if (G["lev"][x] == 0) != (o[0] < 0): return False
            if o[0] >= 0 and G["lev"][o[0]] != G["lev"][x] - 1: return False
    gs = [q for gg in G["gate"] for q in gg]
    return len(set(gs)) == len(gs) and len(set(G["br"])) == len(G["br"]) and acyclic(G)

def rand_gen(rng):
    d = rng.randint(1, 4); D = rng.choice([2, 2, 3]); lev = []
    for l in range(d): lev += [l] * rng.randint(1, 3)
    N = len(lev); order = list(range(N)); rng.shuffle(order); pos = {v: i for i, v in enumerate(order)}
    opts, M = [], 0
    for x in range(N):
        o = []
        for k in range(rng.randint(1, D) if rng.random() < 0.2 else D):
            low = [v for v in range(N) if lev[v] == lev[x] - 1]
            wt = rng.choice(low) if lev[x] > 0 else -1
            later = [v for v in range(N) if pos[v] > pos[x]]
            xt = rng.choice(later) if later and rng.random() < 0.8 else -1
            o.append([wt, xt, M]); M += 1
        opts.append(o)
    g = list(range(M)); rng.shuffle(g); it = iter(g); gate = [[next(it) for _ in o] for o in opts]
    br = list(range(M)); rng.shuffle(br); bp = [rng.randint(0, 1) for _ in range(M)]
    return {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": bp, "start": [rng.randrange(len(o)) for o in opts]}

def is_lr(G):
    N = G["N"]
    if N % 2 or G["lev"] != [v // 2 for v in range(N)]: return False
    return all(len(G["opts"][x]) == 2 and all(G["opts"][x][k][0] == (2 * (G["lev"][x] - 1) + k if G["lev"][x] > 0 else -1)
                                               for k in (0, 1)) for x in range(N))

C = {k: 0 for k in "LOCALKP LOCALCTL KFWE PAIRKF CASCADE LADDER FLET RENEW RENEWB MERGE MERGECTL RETURN RETCNT KEYFLIP".split()}
N_ = {"runs": 0, "steps": 0, "pairs_local": 0, "kf_movers": 0, "pair_flips": 0, "own": 0, "below": 0, "toponly_first": 0,
      "renew_h": 0, "renew_first_h": 0, "intervals": 0, "merge_states": 0, "returns": 0, "ladder_runs": 0, "pairkf_movers": 0, "keyflip_movers": 0, "retcnt_movers": 0}

def static_checks(G, g, rng, W):
    N = G["N"]
    for _ in range(6):
        s = [rng.randrange(len(o)) for o in G["opts"]]
        for x in range(N):
            s2 = [s[y] if y in W[x] else rng.randrange(len(G["opts"][y])) for y in range(N)]
            k1, k2 = g.keys(s), g.keys(s2); N_["pairs_local"] += 1
            if any(g.optkey(k1, x, k) != g.optkey(k2, x, k) for k in range(len(g.opts[x]))): C["LOCALKP"] += 1
            for y in W[x]:
                if len(G["opts"][y]) < 2: continue
                s3 = list(s); s3[y] = (s[y] + 1) % len(G["opts"][y]); k3 = g.keys(s3)
                if any(g.optkey(k1, x, k) != g.optkey(k3, x, k) for k in range(len(g.opts[x]))): C["LOCALCTL"] += 1
        for x in range(N):
            if len(G["opts"][x]) != 2: continue
            pa, pb = g.play(s, x, 0), g.play(s, x, 1); common = [y for y in pa if y in pb]
            m = common[0] if common else None
            pre = set(pa[:pa.index(m)] if m is not None else pa) | set(pb[:pb.index(m)] if m is not None else pb)
            d0 = g.face(s, x, 0) - g.face(s, x, 1); N_["merge_states"] += 1
            s2 = [s[y] if (y in pre or y == x) else rng.randrange(len(G["opts"][y])) for y in range(N)]
            if (g.face(s2, x, 0) > g.face(s2, x, 1)) != (d0 > 0) or g.face(s2, x, 0) - g.face(s2, x, 1) != d0: C["MERGE"] += 1
            for y in pre:
                if len(G["opts"][y]) < 2: continue
                s3 = list(s); s3[y] = (s[y] + 1) % len(G["opts"][y])
                if g.face(s3, x, 0) - g.face(s3, x, 1) != d0: C["MERGECTL"] += 1

def run_checks(G, g, start, W, top):
    N = G["N"]; S, AS = g.run(start); T = len(S) - 1; N_["runs"] += 1; N_["steps"] += T
    deg2 = max(len(o) for o in G["opts"]) <= 2
    K = [g.keys(st) for st in S]; KP = [[kp(g, K[t], x) for x in range(N)] for t in range(T + 1)]
    Mv = [None] + [set(x for x in range(N) if S[t][x] != S[t - 1][x]) for t in range(1, T + 1)]
    mv = [sum(1 for t in range(1, T + 1) if x in Mv[t]) for x in range(N)]
    KF = [sum(1 for t in range(1, T + 1) if KP[t][x] != KP[t - 1][x]) for x in range(N)]
    WE = [sum(1 for t in range(1, T + 1) if Mv[t] & W[x]) for x in range(N)]
    for x in range(N):
        N_["kf_movers"] += 1
        if KF[x] > WE[x]: C["KFWE"] += 1
        N_["keyflip_movers"] += deg2
        if deg2 and mv[x] > 1 + KF[x]: C["KEYFLIP"] += 1
    def order(t, p, q): return K[t][p] < K[t][q]
    flips = {}
    for p in range(N):
        for q in range(p + 1, N):
            if G["lev"][p] != G["lev"][q]: continue
            F = 0
            for t in range(1, T + 1):
                if order(t, p, q) == order(t - 1, p, q): continue
                F += 1; N_["pair_flips"] += 1
                if p in Mv[t] or q in Mv[t]: N_["own"] += 1; continue
                ok = G["lev"][p] >= 1
                if ok:
                    wp, wq = G["opts"][p][S[t][p]][0], G["opts"][q][S[t][q]][0]
                    ok = wp != wq and order(t, wp, wq) != order(t - 1, wp, wq)
                if ok: N_["below"] += 1
                else: C["CASCADE"] += 1
            flips[(p, q)] = F
            if F > T: C["FLET"] += 1
    for x in range(N):
        if len(G["opts"][x]) == 2 and G["lev"][x] >= 1:
            a, b = G["opts"][x][0][0], G["opts"][x][1][0]
            want = 0 if a == b else flips[(min(a, b), max(a, b))]; N_["pairkf_movers"] += 1
            if KF[x] != want: C["PAIRKF"] += 1
    if is_lr(G):
        N_["ladder_runs"] += 1; d = N // 2
        for l in range(d):
            Fl = flips[(2 * l, 2 * l + 1)]; prev = flips[(2 * l - 2, 2 * l - 1)] if l else 0
            if Fl > mv[2 * l] + mv[2 * l + 1] + prev: C["LADDER"] += 1
    # RENEW / RENEWB
    toponly = [None] + [bool(Mv[t]) and all(G["lev"][x] == top for x in Mv[t]) for t in range(1, T + 1)]
    D = xdesc(G)
    for t in range(2, T + 1):
        if not toponly[t]: continue
        if not toponly[t - 1]: N_["toponly_first"] += 1
        for h in Mv[t]:
            N_["renew_h"] += 1; N_["renew_first_h"] += not toponly[t - 1]; w = S[t][h]; A2 = AS[t - 2][h]
            rose = g.face(S[t - 1], h, w) > g.face(S[t - 2], h, w)
            Z = [z for z in g.play(S[t - 2], h, w) if z != h and z in Mv[t - 1]]
            if w in A2 or not rose or not Z or not all(z in D[h] for z in Z): C["RENEW"] += 1
    t = 1
    while t <= T:
        if toponly[t]:
            a = t
            while t + 1 <= T and toponly[t + 1]: t += 1
            b = t; N_["intervals"] += 1
            for h in range(N):
                if G["lev"][h] == top and any(KP[u][h] != KP[a - 1][h] for u in range(a - 1, b + 1)): C["RENEWB"] += 1
        t += 1
    # RETURN / RETCNT
    for x in range(N):
        if len(G["opts"][x]) != 2: continue
        tm = [t for t in range(1, T + 1) if x in Mv[t]]
        R = [0, 0]
        for k in (0, 1):
            z = G["opts"][x][k][1]
            if z >= 0: R[k] = sum(1 for t in range(1, T + 1) if g.face(S[t], z, S[t][z]) > g.face(S[t - 1], z, S[t - 1][z]))
        for i in range(1, len(tm)):
            o2 = S[tm[i]][x]; z = G["opts"][x][o2][1]; N_["returns"] += 1
            if z < 0 or not g.face(S[tm[i] - 1], z, S[tm[i] - 1][z]) > g.face(S[tm[i - 1] - 1], z, S[tm[i - 1] - 1][z]): C["RETURN"] += 1
        N_["retcnt_movers"] += 1
        if len(tm) > 1 + R[0] + R[1]: C["RETCNT"] += 1

def all_starts(G, rng, cap=64):
    import itertools
    sizes = [len(o) for o in G["opts"]]; tot = 1
    for s in sizes: tot *= s
    if tot <= cap: return [list(t) for t in itertools.product(*[range(s) for s in sizes])]
    return [list(G["start"])] + [[rng.randrange(s) for s in sizes] for _ in range(cap - 1)]

def main():
    rng = random.Random(172)
    files = sorted(f for f in glob.glob(os.path.join(H, "..", "box1[5-7][0-9]", "**", "*.json"), recursive=True)
                   if os.path.relpath(f, os.path.join(H, "..")).split(os.sep)[0] <= "box172")   # frozen corpus: boxes 150-172
    corpus = []
    for f in files:
        try: G = json.load(open(f))
        except Exception: continue
        if isinstance(G, dict) and valid(G) and "start" in G and G["N"] <= 30: corpus.append((os.path.relpath(f, os.path.join(H, "..")), G))
    ncorp = len(corpus); nrand = 0
    for f, G in corpus:
        g = Gen(G); W = wclos(G); top = max(G["lev"]); static_checks(G, g, rng, W)
        run_checks(G, g, G["start"], W, top)
    while nrand < 400:
        G = rand_gen(rng)
        if not valid(G): continue
        nrand += 1; g = Gen(G); W = wclos(G); top = max(G["lev"]); static_checks(G, g, rng, W)
        for st in all_starts(G, rng): run_checks(G, g, st, W, top)
    print("SCOPE corpus %d random %d runs %d steps %d" % (ncorp, nrand, N_["runs"], N_["steps"]))
    print("COUNTS " + " ".join("%s %d" % kv for kv in N_.items()))
    print(" ".join("%s %d" % kv for kv in C.items()))
    dead()

def dead():
    E = os.path.join(H, "..")
    G = json.load(open(os.path.join(E, "box166/out/KILL_PM_compose_dd_d5_F14.json"))); g = Gen(G); S, _ = g.run(G["start"])
    D = xdesc(G); x = 12; mv = sum(1 for t in range(1, len(S)) if S[t][x] != S[t - 1][x])
    print("DEAD PM KILL_PM_compose_dd_d5_F14 valid %s deg %d N %d T %d mover %d desc %d moves %d bound %d" % (valid(G),
          max(len(o) for o in G["opts"]), G["N"], len(S) - 1, x, len(D[x]), mv, (len(G["opts"][x]) - 1) * (1 + len(D[x]))))
    G = json.load(open(os.path.join(E, "box172/inst/dd_d5_F14.json"))); g = Gen(G); S, _ = g.run(G["start"]); D = xdesc(G); x = 6
    VR = sum(1 for t in range(1, len(S)) if g.face(S[t], x, S[t][x]) > g.face(S[t - 1], x, S[t - 1][x]))
    print("DEAD PMV dd_d5_F14 valid %s LR %s N %d T %d mover %d desc %d VR %d bound %d" % (valid(G), is_lr(G), G["N"], len(S) - 1, x,
          len(D[x]), VR, 1 + len(D[x])))
    K = [g.keys(st) for st in S]; T = len(S) - 1
    F = [sum(1 for t in range(1, T + 1) if (K[t][2 * l] < K[t][2 * l + 1]) != (K[t - 1][2 * l] < K[t - 1][2 * l + 1])) for l in range(5)]
    mvs = [sum(1 for t in range(1, T + 1) if S[t][y] != S[t - 1][y]) for y in range(G["N"])]
    print("DEAD TOWER dd_d5_F14 T %d pair flips by level %s moves %s doubling F(3) = 2(1 + F(2)) %s next 2(1 + F(3)) = %d > T %s" % (
          T, F, mvs, F[3] == 2 * (1 + F[2]), 2 * (1 + F[3]), 2 * (1 + F[3]) > T))
    for f in ("box166/out/KILL_PM_compose_dd_d5_F14.json", "box170/out/T1_dd_top8.json"):
        G = json.load(open(os.path.join(E, f))); g = Gen(G); S, _ = g.run(G["start"]); T = len(S) - 1; K = [g.keys(st) for st in S]
        mf = max(sum(1 for t in range(1, T + 1) if (K[t][p] < K[t][q]) != (K[t - 1][p] < K[t - 1][q])) for p in range(G["N"])
                 for q in range(p + 1, G["N"]) if G["lev"][p] == G["lev"][q])
        print("TOWER composition %s valid %s N %d T %d max pair flips %d" % (os.path.basename(f), valid(G), G["N"], T, mf))

if __name__ == "__main__":
    main()
