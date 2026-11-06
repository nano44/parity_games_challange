#!/usr/bin/env python3
"""L-RED R208 COUPEXT: adversarial top extensions with exactly C Xi-couplings. Base genome G0 (levels 0..d0-1, kept fixed). New top
level d0: two two-option movers u0, u1 (W-targets: any level-(d0-1) mover per option), A one-option top movers (env AUX, default 0).
Couplings: C distinct old options (x, k) whose Xi-target is re-pointed to a top mover. New options: Xi-target X or an old mover (acyclic
check), beta rank / gate inserted at any position of the old orders (floats), parity, start of the top movers. Everything old fixed.
gain(G) := T(G) - T(G^-), G^- := G with the top level deleted and every Xi-target in it replaced by X (Lemma TOP-ADD: C = 0 => gain <= 2).
Also reported: T(G) - T(G0). Score (gain, T); GAIN=best (default): gain' := T(G) - max over re-routings of the C coupled Xi-targets (X or any old
mover, acyclic; exhaustive for C <= 2, coordinate ascent for C >= 3) of T of the d0-level genome; GAIN=x: the X-routing gain above. Usage: coupext.py base.json C iters seed out.json"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178"), os.path.join(H, "..", "r207")]
import ideal
AUX = int(os.environ.get("AUX", "0"))
def build(G0, P):
    N0 = G0["N"]; d0 = max(G0["lev"]) + 1; nt = 2 + AUX; N = N0 + nt
    lev = list(G0["lev"]) + [d0] * nt
    opts = [[list(o) for o in oo] for oo in G0["opts"]]
    M0 = sum(len(o) for o in opts)
    br = [float(r) for r in G0["br"]]; bp = list(G0["bp"]); gate = [[float(g) for g in gg] for gg in G0["gate"]]
    for (x, k, u) in P["coup"]: opts[x][k][1] = N0 + u
    b = len(br)
    for i in range(nt):
        deg = 2 if i < 2 else 1; o = []; g = []
        for k in range(deg):
            o.append([P["wt"][i][k], P["xt"][i][k], b]); br.append(P["rk"][i][k]); bp.append(P["par"][i][k]); g.append(P["gt"][i][k]); b += 1
        opts.append(o); gate.append(g)
    start = list(G0["start"]) + [P["st"][i] if i < 2 else 0 for i in range(nt)]
    # acyclicity + pi by topological order (Xi-target after source)
    adj = [[o[1] for o in oo if o[1] >= 0] for oo in opts]; indeg = [0] * N
    for v in range(N):
        for w in adj[v]: indeg[w] += 1
    order = [v for v in range(N) if indeg[v] == 0]; i = 0
    while i < len(order):
        for w in adj[order[i]]:
            indeg[w] -= 1
            if indeg[w] == 0: order.append(w)
        i += 1
    if len(order) < N: return None
    pi = [0] * N
    for j, v in enumerate(order): pi[v] = j
    rr = sorted(range(len(br)), key=lambda j: br[j]); brn = [0] * len(br)
    for j, q in enumerate(rr): brn[q] = j
    flat = sorted([(gate[v][k], v, k) for v in range(N) for k in range(len(opts[v]))]); gn = [[0] * len(opts[v]) for v in range(N)]
    for j, (_, v, k) in enumerate(flat): gn[v][k] = j
    return dict(N=N, lev=lev, deg=2, opts=opts, gate=gn, br=brn, bp=bp, start=start, pi=pi)
def minus(G, N0):
    opts = [[[o[0], -1 if o[1] >= N0 else o[1], o[2]] for o in G["opts"][v]] for v in range(N0)]
    return dict(N=N0, lev=G["lev"][:N0], opts=opts, gate=G["gate"][:N0], br=G["br"], bp=G["bp"], start=G["start"][:N0])
def T(G): return len(ideal.traj(G, cap=100000)[0]) - 1
GD = os.environ.get("GAIN", "best")
def acyc(opts):
    N = len(opts); col = [0] * N
    def dfs(v):
        col[v] = 1
        for o in opts[v]:
            w = o[1]
            if w >= 0 and (col[w] == 1 or (col[w] == 0 and not dfs(w))): return False
        col[v] = 2; return True
    return all(col[v] or dfs(v) for v in range(N))
def bestlow(G, G0, P):
    """max T over re-routings of the coupled options (each: X or any old mover, acyclic), top level deleted; coordinate ascent from
    the X routing, exhaustive when C <= 2"""
    import itertools
    N0 = G0["N"]; base = minus(G, N0); cs = [(c[0], c[1]) for c in P["coup"]]; tg = list(range(N0)) + [-1]
    def ev(choice):
        H2 = json.loads(json.dumps(base))
        for (x, k), y in zip(cs, choice): H2["opts"][x][k][1] = y
        if not acyc(H2["opts"]): return -1
        return T(H2)
    if len(cs) <= 2: return max(ev(ch) for ch in itertools.product(tg, repeat=len(cs)))
    ch = [-1] * len(cs); bv = ev(ch); imp = True
    while imp:
        imp = False
        for i in range(len(cs)):
            for y in tg:
                c2 = list(ch); c2[i] = y; v = ev(c2)
                if v > bv: bv, ch, imp = v, c2, True
    return bv
def score(G0, P):
    G = build(G0, P)
    if G is None: return None, None
    t = T(G)
    if GD == "x": return (t - T(minus(G, G0["N"])), t), G
    if GD == "t": return (t, 0), G   # proxy: gain' <= T(G) - T(G0) (the old routing is one of the re-routings); gain.py computes gain'

    return (t - bestlow(G, G0, P), t), G
def rand(G0, C, rng):
    N0 = G0["N"]; d0 = max(G0["lev"]) + 1; top = [v for v in range(N0) if G0["lev"][v] == d0 - 1]; nt = 2 + AUX; M0 = len(G0["br"])
    allo = [(x, k) for x in range(N0) for k in range(len(G0["opts"][x]))]; cs = rng.sample(allo, C)
    return dict(coup=[(x, k, rng.randrange(nt)) for (x, k) in cs],
                wt=[[rng.choice(top) for _ in range(2)] for _ in range(nt)], xt=[[rng.choice(list(range(N0)) + [-1]) for _ in range(2)] for _ in range(nt)],
                rk=[[rng.uniform(-1, M0) for _ in range(2)] for _ in range(nt)], par=[[rng.randint(0, 1) for _ in range(2)] for _ in range(nt)],
                gt=[[rng.uniform(-1, 3 * M0) for _ in range(2)] for _ in range(nt)], st=[rng.randint(0, 1) for _ in range(nt)])
def mutate(G0, P, rng):
    Q = json.loads(json.dumps(P)); N0 = G0["N"]; d0 = max(G0["lev"]) + 1; top = [v for v in range(N0) if G0["lev"][v] == d0 - 1]
    nt = 2 + AUX; i = rng.randrange(nt); k = rng.randrange(2 if i < 2 else 1); r = rng.random(); M0 = len(G0["br"])
    if r < 0.2 and Q["coup"]:
        j = rng.randrange(len(Q["coup"]))
        if rng.random() < 0.5: Q["coup"][j][2] = rng.randrange(nt)
        else:
            used = {(c[0], c[1]) for c in Q["coup"]}; x = rng.randrange(N0); kk = rng.randrange(len(G0["opts"][x]))
            if (x, kk) in used: return P
            Q["coup"][j][0], Q["coup"][j][1] = x, kk
    elif r < 0.3: Q["wt"][i][k] = rng.choice(top)
    elif r < 0.5: Q["xt"][i][k] = rng.choice(list(range(N0)) + [-1])
    elif r < 0.65: Q["rk"][i][k] = rng.uniform(-1, M0)
    elif r < 0.72: Q["par"][i][k] ^= 1
    elif r < 0.9: Q["gt"][i][k] = rng.uniform(-1, 3 * M0)
    else: Q["st"][i] ^= 1
    return Q
if __name__ == "__main__":
    G0 = json.load(open(sys.argv[1])); C, it, seed = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]); out = sys.argv[5]; rng = random.Random(seed)
    T0 = T(G0); P = rand(G0, C, rng); sc, G = score(G0, P)
    while sc is None: P = rand(G0, C, rng); sc, G = score(G0, P)
    best = (sc, G, P); stale = 0
    for _ in range(it):
        Q = mutate(G0, P, rng); s2, G2 = score(G0, Q)
        if s2 is None: continue
        if s2 >= sc: P, sc = Q, s2
        if s2 > best[0]: best = (s2, G2, Q); json.dump(dict(G2, coup=Q["coup"]), open(out, "w")); stale = 0
        stale += 1
        if stale > 8000: P, sc, stale = best[2], best[0], 0
    json.dump(dict(best[1], coup=best[2]["coup"]), open(out, "w"))
    print(f"COUPEXT base {os.path.basename(sys.argv[1])} T0 {T0} C {C} AUX {AUX} seed {seed} best gain {best[0][0]} T {best[0][1]} T-T0 {best[0][1] - T0}")
