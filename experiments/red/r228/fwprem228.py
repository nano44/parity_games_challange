#!/usr/bin/env python3
"""R228 item 2 (L-RED successor 62): premise check of a genome as a GAME input of RESULTS R117 / R118 (Gamma3(G), N5'-xi from S3).
Own code except the objects under test: L-NEW's gamma3.build (the Gamma3 builder, all pads) and n5v.step (the N5'-xi step) and
n5x.start_pair (the engine's S3), read from ROOT (an l-new tree, e.g. git archive fcba92fc). Per genome, counters:
  formfail  R104 genome form (W-target level lev(x) - 1, none exactly at level 0; Xi-target a mover or X (-1); distinct gate indices;
            distinct beta ranks; parity in {0,1}; one beta index per option; start in range)
  xicyc     the cyclic SCCs of the Xi-graph (a self-loop counts), by mover name
  elevfail  [E-LEV] on the built Gamma3: pairs of e-vertices with lev(x) < lev(x') but pr(e) >= pr(e')
  s3own     my own FIX-1 start (Even: highest even priority, else lowest odd; ties largest index if even, smallest if odd; Odd: the same
            rule on the dual, i.e. highest odd, else lowest even; ties largest index if odd, smallest if even) vs (a) the engine's
            n5x.start_pair, (b) the standard state of Gamma3 for the genome start (gamma3's transported start): #vertices that differ
  ties      #vertices where FIX 1 had to break a priority tie (0 means the start does not depend on the tie rule)
  T3        iterations before the first fallback of N5'-xi from S3;  nonstd = states 0..T3 that are not a standard state
            (sigma off the movers or tau differ from the standard state);  badmover = states where a mover's sigma is not a pad m_(x,k)
  noncore   #iterations in 1..T3 that change sigma at a non-mover Even vertex or change tau
Controls (each must make its counter fire): FWP_CTRL=form (q-level W-target moved to level 1 -> formfail), elev (the e-priorities of
the first level-0 and the last level-1 option swapped in Gamma3 -> elevfail), s3 (my FIX-1 start flipped at one Odd gate -> s3own > 0),
std (the standard state flipped at one beta with a mover Xi-target -> nonstd > 0).
Usage: ROOT=<l-new tree> fwprem228.py G.json ..."""
import sys, os, json
ROOT = os.environ["ROOT"]
sys.path[:0] = [os.path.join(ROOT, p) for p in ("experiments/new/box189", "experiments/new/box190", "experiments/new/box21",
                "experiments/new", "experiments/si", "experiments/harness")]
import gamma3, n5v, n5x, pg

def form(G):
    N, lev, opts, gate, br, bp, st = G["N"], G["lev"], G["opts"], G["gate"], G["br"], G["bp"], G["start"]
    bad = 0; gs = []; bs = []
    for x in range(N):
        if not (0 <= st[x] < len(opts[x])): bad += 1
        for k, (wt, xt, b) in enumerate(opts[x]):
            if lev[x] == 0: bad += wt != -1
            else: bad += not (0 <= wt < N and lev[wt] == lev[x] - 1)
            bad += not (xt == -1 or 0 <= xt < N)
            gs.append(gate[x][k]); bs.append(b)
    M = len(bs); bad += len(set(gs)) != M or len(set(bs)) != M or sorted(bs) != list(range(M))
    bad += len(set(br)) != len(br) or any(p not in (0, 1) for p in bp)
    return bad

def xicycles(G, names):
    N, opts = G["N"], G["opts"]; adj = [[o[1] for o in opts[x] if o[1] >= 0] for x in range(N)]
    idx = {}; low = {}; stk = []; on = set(); out = []; c = [0]
    sys.setrecursionlimit(100000)
    def sc(v):
        idx[v] = low[v] = c[0]; c[0] += 1; stk.append(v); on.add(v)
        for w in adj[v]:
            if w not in idx: sc(w); low[v] = min(low[v], low[w])
            elif w in on: low[v] = min(low[v], idx[w])
        if low[v] == idx[v]:
            comp = []
            while True:
                w = stk.pop(); on.discard(w); comp.append(w)
                if w == v: break
            if len(comp) > 1 or v in adj[v]: out.append(sorted(names.get(w, str(w)) for w in comp))
    for v in range(N):
        if v not in idx: sc(v)
    return out

def fix1(g):
    sig, tau, ties = {}, {}, 0
    for v in range(g.n):
        S = g.succ[v]
        if len(S) == 1: (sig if g.owner[v] == 0 else tau)[v] = S[0]; continue
        good = 0 if g.owner[v] == 0 else 1                     # the owner's parity
        G_ = [w for w in S if g.prio[w] % 2 == good]
        if G_:
            p = max(g.prio[w] for w in G_); C = [w for w in G_ if g.prio[w] == p]; pick = max(C)
        else:
            p = min(g.prio[w] for w in S); C = [w for w in S if g.prio[w] == p]; pick = min(C)
        ties += len(C) > 1
        (sig if g.owner[v] == 0 else tau)[v] = pick
    return sig, tau, ties

def main(path, cap=20000):
    G = json.load(open(path)); CT = os.environ.get("FWP_CTRL", ""); nm = path[:-5] + ".names.json"
    names = {v: k for k, v in json.load(open(nm)).items()} if os.path.exists(nm) else {}
    g0, sig0, tau0, V = gamma3.build(G, {"K", "pe", "pb", "m"})
    g = pg.parse(f"parity {g0.n - 1};\n" + "".join(f"{v} {g0.prio[v]} {g0.owner[v]} {','.join(map(str, g0.succ[v]))};\n" for v in range(g0.n)))
    N, lev, opts = G["N"], G["lev"], G["opts"]
    if CT == "form":
        x = next(x for x in range(N) if lev[x] == 1); G = json.loads(json.dumps(G)); G["opts"][x][0][0] = x; opts = G["opts"]
    O = [(x, k) for x in range(N) for k in range(len(opts[x]))]
    ev = [(lev[x], g.prio[V[("e", (x, k))]]) for (x, k) in O]
    if CT == "elev":
        a = min((q for q in O if lev[q[0]] == 0), key=lambda q: g.prio[V[("e", q)]]); b = max((q for q in O if lev[q[0]] == 1), key=lambda q: g.prio[V[("e", q)]])
        i, j = (O.index(a), O.index(b)); ev[i], ev[j] = (ev[i][0], ev[j][1]), (ev[j][0], ev[i][1])
    elev = sum(1 for a in ev for b in ev if a[0] < b[0] and a[1] >= b[1])
    s, t, ties = fix1(g)
    if CT == "s3":
        v = next(v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1); t[v] = [w for w in g.succ[v] if w != t[v]][0]
    if CT == "std":
        q = next(q for q in O if opts[q[0]][q[1]][1] >= 0); sig0 = dict(sig0); sig0[V[("b", q)]] = V[("pb", q)]
    E, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None)
    ev_ = [v for v in range(g.n) if g.owner[v] == 0]; od_ = [v for v in range(g.n) if g.owner[v] == 1]
    d_eng = sum(sigma[v] != s[v] for v in ev_) + sum(tau[v] != t[v] for v in od_)
    d_std = sum(sig0.get(v, g.succ[v][0]) != s[v] for v in ev_) + sum(tau0.get(v, g.succ[v][0]) != t[v] for v in od_)
    movers = set(range(N)); mpads = {V[("m", q)] for q in O}
    std_off = {v: sig0.get(v, g.succ[v][0]) for v in ev_ if v not in movers}
    def isstd(sg, tu): return all(sg[v] == w for v, w in std_off.items()) and all(tu[v] == tau0.get(v, g.succ[v][0]) for v in od_)
    nonstd = badm = noncore = 0; T3 = None; it = 0; prev = (list(sigma), list(tau))
    nonstd += not isstd(sigma, tau); badm += any(sigma[x] not in mpads for x in movers)
    while it < cap:
        r = n5v.step(g, E, Ed, sigma, tau, "xi")
        if r is None: break
        it += 1
        if r[4]: T3 = it - 1; break
        sigma, tau = list(r[0]), list(r[1])
        noncore += any(sigma[v] != prev[0][v] for v in std_off) or any(tau[v] != prev[1][v] for v in od_)
        nonstd += not isstd(sigma, tau); badm += any(sigma[x] not in mpads for x in movers); prev = (list(sigma), list(tau))
    print(f"{os.path.basename(path)} N {N} M {len(O)} n3 {g.n} (N+7M+10 = {N + 7 * len(O) + 10}) formfail {form(G)} "
          f"xicyc {xicycles(G, names)} elevfail {elev} s3own: vs engine {d_eng}, vs standard {d_std}, ties {ties} "
          f"T3 {T3} nonstd {nonstd} badmover {badm} noncore {noncore} iters {it}")

for f in sys.argv[1:]: main(f)
