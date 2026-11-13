#!/usr/bin/env python3
"""Box 213 KEY-TAU DATA (L-NEW successor 75). N5 (box190 n5v.step, mode KM_MODE = spec (default) | xi | idx) from S3 on Gamma3(G) up to
its first fallback. At each state t (sigma_t, tau_t; A_t(x) = {sigma_t(x)} + {w : (x, w) in I_sigma_t}) this tool computes, WITHOUT
the S1 engine, the TAU-GRAPH X_t: every Even vertex keeps A_t, every Odd vertex keeps tau_t, and runs its own BFS from c_W over
predecessors in increasing index order (FIFO; first discovery sets the choice) = SPEC S1 (iv)'s odd branch read on S4a's dual arena.
The root-first KEY of a vertex = the tuple of indices of the e-vertices on its BFS-tree path, read from c_W; compared by (length, lex).
mu_t(x) := the key of x's OWN play under (sigma_t, tau_t) if that play reaches c_W through movers / pads / gates / e-vertices only
(else INF). Must-0 counters (unit (step, mover) unless said):
  tau3     (unit states): tau_t differs from S3's tau_0 at some Odd vertex, or tau_t(g) is not g's pe pad at some gate      [TAU3]
  kp       N5's sigma_(t+1)(x) != the BFS choice of X_t, for a mover x reached by the BFS                                   [KEY-TAU (i)]
  kpn      the same for an Even NON-mover (must be 0: they keep sigma_t)
  muinc    mu_(t+1)(x) > mu_t(x)                                                                                           [(ii)]
  muflat   sigma_(t+1)(x) != sigma_t(x) but mu_(t+1)(x) = mu_t(x)                                                          [(ii) strict]
  mukappa  mu_(t+1)(x) != kappa_t(x) (the BFS key of x in X_t) for a reached mover                                         [(ii) proof step]
Descriptive: T, unreach ((state, mover) not reached by the BFS), switches, hdec (switches that shorten the key), lexdec (same length),
  infdec (INF -> finite), maxlen (longest key), wacyc (1 if the W-graph x -> wt (the e-targets, = the tau-graph's mover graph) is acyclic), xacyc (1 if
  R104's Xi-graph x -> xt (the beta-targets) is acyclic).
CONTROL: KM_MODE=xi (N5'-xi: Howard's tie rule) must fire kp; KM_CTRL=1 reverses the predecessor order of the BFS (kp must fire).
Usage: keymu213.py G.json ... | keymu213.py --rand SEED COUNT MODE"""
import sys, os, json, random, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box208"))
import level208
import n5v, eg195, gamma3, n5x
MODE = os.environ.get("KM_MODE", "spec"); CTRL = os.environ.get("KM_CTRL") == "1"
KEYS = ("tau3", "kp", "kpn", "muinc", "muflat", "mukappa", "T", "unreach", "switches", "hdec", "lexdec", "infdec", "maxlen", "wacyc", "xacyc")
MAXK = ("T", "maxlen")
INF = (10 ** 9,)

def cmpkey(k): return (len(k), k) if k is not None else (10 ** 9, ())

def bfs(n, succ, cW, ekind):
    """own BFS from cW over predecessors (increasing index; KM_CTRL reverses); returns choice[v] (first discovery) and key[v]"""
    pred = [[] for _ in range(n)]
    for v in range(n):
        for w in succ[v]:
            if v != w: pred[w].append(v)
    for p in pred: p.sort(reverse=CTRL)
    choice = {}; key = {cW: ()}; q = collections.deque([cW])
    while q:
        w = q.popleft()
        for v in pred[w]:
            if v in key: continue
            key[v] = key[w] + ((v,) if ekind[v] else ()); choice[v] = w; q.append(v)
    return choice, key

def mu(x, s, cW, okind, ekind, n):
    """key of x's own play under the positional pair s (one successor per vertex) if it reaches cW through allowed kinds, else None"""
    path = []; seen = set(); v = x
    while v != cW:
        if v in seen or not okind[v]: return None
        seen.add(v); path.append(v); v = s[v]
    return tuple(reversed([u for u in path if ekind[u]]))

def one(G):
    g0, _, _, V = gamma3.build(G, eg195.PADS); g = eg195.topg(g0); n = g.n
    kind = [None] * n
    for k, v in V.items(): kind[v] = k[0] if isinstance(k, tuple) else k
    cW = V["cW"]; mv = [V[("x", x)] for x in range(G["N"])]; mvs = set(mv)
    ekind = [kind[v] == "e" for v in range(n)]; okind = [kind[v] in ("x", "m", "g", "pe", "e") for v in range(n)]
    pe_of = {V[("g", q)]: V[("pe", q)] for k2, q in [(k, k[1]) for k in V if isinstance(k, tuple) and k[0] == "g"]}
    E, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None); tau0 = list(tau)
    c = collections.Counter()
    def acyclic(adj):
        col = {}
        def dfs(x):
            col[x] = 1
            for y in adj[x]:
                if col.get(y) == 1 or (y not in col and not dfs(y)): return False
            col[x] = 2; return True
        return int(all(x in col or dfs(x) for x in adj))
    c["wacyc"] = acyclic({x: [w for (w, _, _) in G["opts"][x] if w >= 0] for x in range(G["N"])})
    c["xacyc"] = acyclic({x: [xt for (_, xt, _) in G["opts"][x] if xt >= 0] for x in range(G["N"])})
    t = 0
    while t <= 20000:
        vs, _ = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
        res = n5v.step(g, E, Ed, sigma, tau, MODE)
        if res is None or res[4]: break
        ns = list(res[0])
        if tau != tau0 or any(tau[gg] != pe for gg, pe in pe_of.items()): c["tau3"] += 1
        A = {}
        for v, w in Is: A.setdefault(v, set()).add(w)
        succ = [sorted({sigma[v]} | A.get(v, set())) if g.owner[v] == 0 else [tau[v]] for v in range(n)]
        choice, key = bfs(n, succ, cW, ekind)
        cur = [sigma[v] if g.owner[v] == 0 else tau[v] for v in range(n)]; nxt = [ns[v] if g.owner[v] == 0 else tau[v] for v in range(n)]
        for v in range(n):
            if g.owner[v] != 0: continue
            if v in mvs:
                if v not in choice: c["unreach"] += 1; continue
                if ns[v] != choice[v]: c["kp"] += 1
                m0, m1 = mu(v, cur, cW, okind, ekind, n), mu(v, nxt, cW, okind, ekind, n)
                if cmpkey(m1) > cmpkey(m0): c["muinc"] += 1
                if m1 != key[v]: c["mukappa"] += 1
                if ns[v] != sigma[v]:
                    c["switches"] += 1
                    if m1 == m0: c["muflat"] += 1
                    elif m0 is None: c["infdec"] += 1
                    elif m1 is not None and len(m1) < len(m0): c["hdec"] += 1
                    else: c["lexdec"] += 1
                if m1 is not None: c["maxlen"] = max(c["maxlen"], len(m1))
            elif v in choice and ns[v] != sigma[v]: c["kpn"] += 1
        sigma, tau = ns, list(res[1]); t += 1
    c["T"] = t
    return c

def fmt(c): return " ".join("%s %d" % (k, c[k]) for k in KEYS)

if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--rand":
        seed, cnt, mode = int(a[1]), int(a[2]), a[3]; rng = random.Random(seed); k = 0; tot = collections.Counter()
        while k < cnt:
            G = eg195.gen(rng, mode)
            if G is None or G["N"] < 2: continue
            k += 1; cc = one(G)
            for key in KEYS: tot[key] = max(tot[key], cc[key]) if key in MAXK else tot[key] + cc[key]
        print("rand", mode, "seed", seed, "genomes", k, "KM_MODE", MODE, "ctrl", int(CTRL), fmt(tot), flush=True)
    else:
        for fn in a:
            G = json.load(open(fn)); G = G.get("genome", G)
            print(os.path.basename(fn), "KM_MODE", MODE, "ctrl", int(CTRL), fmt(one(G)), flush=True)
