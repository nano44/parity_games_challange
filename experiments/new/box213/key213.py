#!/usr/bin/env python3
"""Box 213 KEY-WINDOW (L-NEW successor 75): the tau-arena question of REFEREE-2 40's gap G-1 (claude/referee-2 8e075239,
R2-box212-preread.md §7). N5 (SPEC S1-S5, box190 n5v.step mode "spec") from S3 on Gamma3(G) up to its first fallback; classes as box 208's
level208.prep; windows = the plateaus of plat208 (reference b = T; Y = {x : class_u(x) <= m}) and the TAIL [b', T] (Y = V).
At every step s -> s + 1 inside a window (u <= s < v; tail: b' <= s < T), with tau_s = N5's Odd strategy and A_s(x) = {sigma_s(x)} +
{w : (x, w) in I_sigma_s} (SPEC S2):
  tauclos   (unit (window step, Odd vertex o of Y)): tau_s(o) not in Y                          [(P2^tau): Y closed under the tau-arena]
  tauclosg  the same, gates only (Odd vertices with two successors)
  undef     (unit window steps): H^tau_Y not defined (some Odd vertex of Y leaves Y under tau)
  n5out     (unit (window step, Even vertex of Y)): N5's sigma_(s+1)(x) not in Y                 [(P2) at s + 1; must be 0 by RF-B]
  keytau    (unit (window step, Even vertex of Y)): N5's sigma_(s+1)(x) != the S1 optimum of H^tau_Y (Even x of Y keeps A_s(x) n Y,
            Odd o of Y keeps tau_s(o); SPEC S4a's computation on the dual, sub-game indexed in increasing order of V)   [(P5^tau) exact]
  keytauval the same where the VALUE (in H^tau_Y) of N5's choice differs from the optimum's value (tie-free part of keytau)
  keysig    (descriptive, the reading REFEREE-2 refuted; unit (window step, MOVER of Y)): N5's choice != the optimum with Odd fixed at
            sigma-bar_u on Y (SPEC run on H_Y); on the towers it must reproduce REFEREE-2's 7,358 (DBL4 178)
Descriptive: T, plats, platsteps (window steps with Y != V), tailsteps, ysz (sum |Y| over Y != V steps), outA ((window step, mover of Y)
  with an improving gate outside Y), moversY.
Built-in check (must be 0): keytau_tail = keytau on tail steps (Y = V: H^tau_V is S4a's own arena, so the recomputation must equal N5).
Control KEY_CTRL=1: on plateaus, Y minus the new successors sigma_(u+1)(x) of the movers x of Y that switch at the window's first step;
  n5out must fire on every plateau whose first step switches a mover of Y.
Usage: key213.py G.json ... | key213.py --rand SEED COUNT MODE (eg195.gen modes)   (run from any directory)"""
import sys, os, json, random, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box208"))
import level208
import n5v, eg195, gamma3, n5x, pg
from si import Engine
CTRL = os.environ.get("KEY_CTRL") == "1"
KEYS = ("tauclos", "tauclosg", "undef", "n5out", "keytau", "keytauval", "keytau_tail", "keysig", "T", "plats", "platsteps",
        "tailsteps", "ysz", "outA", "moversY")
MAXK = ("T",)

def history(G):
    g0, _, _, V = gamma3.build(G, eg195.PADS); g = eg195.topg(g0); n = g.n
    E, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None); H = []
    while len(H) <= 20000:
        vs, tb = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs); H.append((list(sigma), list(tau), vs, tb, Is))
        res = n5v.step(g, E, Ed, sigma, tau, "spec")
        if res is None or res[4]: break
        sigma, tau = list(res[0]), list(res[1])
    kind = [None] * n
    for k, v in V.items(): kind[v] = k[0] if isinstance(k, tuple) else k
    evs = [v for v in range(n) if kind[v] == "e"]; ebits = sorted(E.rank[v] for v in evs); pos = {rk: i for i, rk in enumerate(ebits)}
    def es(mask):
        x = 0
        for rk in ebits:
            if (mask >> rk) & 1: x |= 1 << pos[rk]
        return x
    rew = lambda v: g.prio[v] if g.prio[v] % 2 == 0 else -g.prio[v]
    cls = [[(rew(h[2][v][0]), es(h[2][v][1])) for v in range(n)] for h in H]
    return g, E, H, cls, set(V[("x", x)] for x in range(G["N"]))

def windows(n, T, cls):
    """plat208's plateaus (u, v, Y) with Y per KEY_CTRL, then the tail (b', T, None = all of V)"""
    phis = []
    for t in range(T):
        lag = [x for x in range(n) if cls[t][x] != cls[T][x]]
        if not lag: phis.append(None); continue
        m = min(cls[t][x] for x in lag); phis.append((m, frozenset(x for x in lag if cls[t][x] == m)))
    out = []; t = 0
    while t < T:
        if phis[t] is None: t += 1; continue
        u = t
        while t + 1 < T and phis[t + 1] == phis[u]: t += 1
        v = t; t += 1
        if v == u: continue
        m, J = phis[u]; out.append((u, v, set(x for x in range(n) if cls[u][x] <= m)))
    bp = next(t for t in range(T + 1) if all(cls[t][x] == cls[T][x] for x in range(n)))
    if bp < T: out.append((bp, T, None))
    return out

def optimum(g, Y, sigma, Is, odd_at):
    """S4a's computation on the sub-game Y (indices in increasing order): Even y keeps (A(y) n Y), Odd o keeps odd_at[o].
    Returns (map V -> sub index, best (sub indices), vh (sub valuations), Er)"""
    Ys = sorted(Y); ix = {v: i for i, v in enumerate(Ys)}; A = {}
    for v, w in Is: A.setdefault(v, set()).add(w)
    succ = []
    for v in Ys:
        if g.owner[v] == 0: succ.append(sorted(ix[w] for w in ({sigma[v]} | A.get(v, set())) if w in ix))
        else: succ.append([ix[odd_at[v]]])
    sub = pg.Game([g.prio[v] for v in Ys], [g.owner[v] for v in Ys], succ)
    Er = Engine(n5v.dual(sub)); vh, best = Er.evaluate(tuple(succ[i][0] if g.owner[v] == 1 else -1 for i, v in enumerate(Ys)))
    return ix, best, vh, Er

def one(G):
    g, E, H, cls, mv = history(G); n, T = g.n, len(H) - 1; c = collections.Counter(); c["T"] = T
    for (u, v, Y) in windows(n, T, cls):
        tail = Y is None
        if tail: Y = set(range(n))
        else:
            c["plats"] += 1
            if CTRL: Y = Y - {H[u + 1][0][x] for x in Y if x in mv and H[u + 1][0][x] != H[u][0][x]}
        for s in range(u, v):
            sigma, tau, vs, tb, Is = H[s]; ns = H[s + 1][0]
            if tail: c["tailsteps"] += 1
            else: c["platsteps"] += 1; c["ysz"] += len(Y)
            esc = [o for o in Y if g.owner[o] == 1 and tau[o] not in Y]
            c["tauclos"] += len(esc); c["tauclosg"] += sum(1 for o in esc if len(g.succ[o]) == 2)
            evY = [x for x in Y if g.owner[x] == 0]
            out = [x for x in evY if ns[x] not in Y]; c["n5out"] += len(out)
            c["moversY"] += sum(1 for x in evY if x in mv)
            c["outA"] += sum(1 for x in evY if x in mv and any(w not in Y for (y, w) in Is if y == x))
            if esc or out or any(sigma[x] not in Y for x in evY): c["undef"] += 1; continue
            ix, best, vh, Er = optimum(g, Y, sigma, Is, tau)
            for x in evY:
                i = ix[x]
                if best[i] != ix[ns[x]]:
                    c["keytau_tail" if tail else "keytau"] += 1
                    if Er.extend(i, vh[ix[ns[x]]]) != vh[i]: c["keytauval"] += 1
            if not any(H[u][3][o] not in Y for o in Y if g.owner[o] == 1):
                ix2, best2, _, _ = optimum(g, Y, sigma, Is, H[u][3])
                c["keysig"] += sum(1 for x in evY if x in mv and best2[ix2[x]] != ix2[ns[x]])
    return c

def fmt(c): return " ".join("%s %d" % (k, c[k]) for k in KEYS)

if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--rand":
        seed, cnt, mode = int(a[1]), int(a[2]), a[3]; rng = random.Random(seed); k = 0; tot = collections.Counter()
        while k < cnt:
            G = eg195.gen(rng, mode)
            if G is None or G["N"] < 2: continue
            k += 1; c = one(G)
            for key in KEYS: tot[key] = max(tot[key], c[key]) if key in MAXK else tot[key] + c[key]
        print("rand", mode, "seed", seed, "genomes", k, "ctrl", int(CTRL), fmt(tot), flush=True)
    else:
        for fn in a:
            G = json.load(open(fn)); G = G.get("genome", G)
            print(os.path.basename(fn), "ctrl", int(CTRL), fmt(one(G)), flush=True)
