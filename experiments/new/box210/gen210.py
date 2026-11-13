#!/usr/bin/env python3
"""Box 210 (L-NEW successor 72): Lemma GEN-LEVEL (CANDIDATE) on GENERAL parity games in split form, state by state.
Split form of a game: every vertex i becomes P_i (one successor, priority prio_i + 2) -> C_i (owner_i, priority 0, i's successors
P_j). Choice vertices are then never cycle nodes and never in a set Pi. Run: Howard for Even (every Even choice vertex goes to a
best successor under the Voege-Jurdzinski values and keeps a best current one; among several best non-current ones the larger
index), Odd's reply optimal (Odd-side iteration to local optimality). Engine: box208/rv208.Val (valuation, order, Odd's reply);
--xcheck compares its values and Odd's reply's values with experiments/si si.Engine on the split game, state by state.
H := the P-vertices of EVEN priority above every odd priority (GEN_H=none: H empty). class(v) := (reward(Lambda(v)), Pi(v) & H).
Reference state b = the last state (GEN_ALLB=1: every b = 1, ..., T in turn; the counts then add up over b). LAG_t, m_t (the lowest lagging class), FRONT_t, Phi_t = (m_t, -|FRONT_t|), stall, plateau as in
box 208. Must-0 counters (a counter that is 0 is not printed):
  F1  (unit (vertex, step)): a value falls                                    K1 (unit (vertex, step)): a class falls
  K3  (unit (vertex, state)): a vertex outside H whose class differs from its successor's, or a vertex of H whose class is below it
  K4  (unit (Odd choice vertex, state)): its class is not the lowest class of its successors
  K5  (unit (Even choice vertex, successor, step)): class_(t+1)(x) < class_t(y)
  L1  (unit steps): Phi falls, or stays equal at a non-stall step, or changes at a stall
  L3  (unit states): neither (alpha) an Even choice vertex of FRONT_t whose successor does not lag, nor (beta) a play cycle inside FRONT_t
  L3m (unit states): (alpha) holds for z and m_t != class_b(sigma_t(z))
  L4  (unit (vertex of FRONT_t, stall)): the map s (Even choice vertex -> its successor at b; other -> its successor at t) leaves FRONT_t
  L4c (unit stalls): s has no cycle inside FRONT_t                            L5 (unit games): more than 2 |P| n values of Phi
  P1  (unit (vertex, state of a plateau)): a class of Y changes, or Y is not {class <= m}
  P2  (unit (vertex of Y, state)): its successor on the play is outside Y
  P3  (unit (Even choice vertex of Y, successor, state)): the successor is outside Y
  P4w (unit (Odd choice vertex of Y, state)): its chosen successor has a class other than its own, or a successor has a lower class
Descriptive: games, Tmax, Tsum, Hsize, nonstalls, stalls, plateaus, platmax, tailmax (steps after LAG is empty), oddflipY (Odd choice
vertices of Y that change successor inside a plateau), oddflipQ (Odd choice vertices that change successor at a step where NO class
changes), capped (runs cut at the cap; not analysed).
Controls: GEN_CTRL=1 FRONT_t := the lagging vertices of the HIGHEST lagging class (L3, L4 must fire); GEN_CTRL=2 H := the P-vertices
of ODD priority above every even priority, same order on classes (on games with an odd top priority K3 / K1 must fire);
GEN_CTRL=3 the game is NOT split (random mode only; DOM can fail: K5 or K4 may fire).
Usage: gen210.py --pg FILE.pg ... (start: si.Engine.initial("best"), as box191 brseg_gen191.py) | gen210.py --xcheck FILE.pg ... |
       gen210.py SEED COUNT N0 D DEG EVTOP (random games: N0 vertices, priorities 1..D, out-degree 1..DEG, EVTOP=1: the top priority even)"""
import sys, os, random, collections
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.environ.get("ROOT") or os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [os.path.join(ROOT, "experiments/new/box208"), os.path.join(ROOT, "experiments/si"), os.path.join(ROOT, "experiments/harness")]
import rv208
CTRL = os.environ.get("GEN_CTRL", "0"); GENH = os.environ.get("GEN_H", "top"); ALLB = os.environ.get("GEN_ALLB") == "1"
MUST0 = ("F1", "K1", "K3", "K4", "K5", "L1", "L3", "L3m", "L4", "L4c", "L5", "P1", "P2", "P3", "P4w")
DESC = ("games", "Tmax", "Tsum", "Hsize", "nonstalls", "stalls", "plateaus", "platmax", "tailmax", "oddflipY", "oddflipQ", "capped")
def show(c): return " ".join("%s %d" % (k, c[k]) for k in MUST0) + " | " + " ".join("%s %d" % (k, c[k]) for k in DESC)
def split(prio, own, succ0):
    n0 = len(prio)
    if CTRL == "3": return n0, n0, list(prio), list(own), [list(s) for s in succ0]
    return 2 * n0, n0, [0] * n0 + [p + 2 for p in prio], list(own) + [0] * n0, [[n0 + j for j in succ0[i]] for i in range(n0)] + [[i] for i in range(n0)]
def gen(rng, n0, d, deg, evtop):
    while True:
        prio = [rng.randint(1, d) for _ in range(n0)]
        if (max(prio) % 2 == 0) == bool(evtop): break
    return split(prio, [rng.randrange(2) for _ in range(n0)], [sorted(rng.sample(range(n0), rng.randint(1, min(deg, n0)))) for _ in range(n0)])
def frompg(fn):
    import pg
    from si import Engine
    g = pg.read(fn); s0 = Engine(g).initial("best"); n, n0, pr, ow, succ = split(list(g.prio), list(g.owner), [list(s) for s in g.succ])
    return n, n0, pr, ow, succ, [(n0 + s0[i]) if g.owner[i] == 0 else -1 for i in range(n0)] + list(range(n0))
def howard(n, n0, pr, ow, succ, start, cap):
    E = rv208.Val(n, pr, ow, succ); sigma = list(start); hist = []; tau = None; ch = [v for v in range(n) if ow[v] == 0 and len(succ[v]) > 1]
    while True:
        val, tau, nxt = E.best_response(sigma, tau); hist.append((list(sigma), val, dict(tau), nxt)); ns = list(sigma)
        for x in ch:
            cur = sigma[x]; bst = cur
            for w in succ[x]:
                cm = E.cmp(val[w], val[bst])
                if cm > 0 or (cm == 0 and bst != cur and w > bst): bst = w
            if E.cmp(val[bst], val[cur]) == 0: bst = cur
            ns[x] = bst
        if ns == sigma or len(hist) > cap: break
        sigma = ns
    return E, hist
def run(n, n0, pr, ow, succ, start, c, cap=20000):
    E, hist = howard(n, n0, pr, ow, succ, start, cap); rank, rew = E.rank, E.rew; T = len(hist) - 1
    Pv = [v for v in range(n) if len(succ[v]) == 1] if CTRL == "3" else list(range(n0, n))
    if CTRL == "2":
        evmax = max([pr[v] for v in Pv if pr[v] % 2 == 0] + [0]); H = [v for v in Pv if pr[v] % 2 == 1 and pr[v] > evmax]
    else:
        oddmax = max([pr[v] for v in range(n) if pr[v] % 2] + [0]); H = [] if GENH == "none" else [v for v in Pv if pr[v] % 2 == 0 and pr[v] > oddmax]
    hmask = sum(1 << rank[v] for v in H); Hs = set(H)
    c["games"] += 1; c["Tmax"] = max(c["Tmax"], T); c["Tsum"] += T; c["Hsize"] += len(H)
    if len(hist) > cap: c["capped"] += 1; return
    val = [h[1] for h in hist]; nxt = [h[3] for h in hist]; sig = [h[0] for h in hist]; tau = [h[2] for h in hist]
    cls = [[(rew[val[t][v][0]], val[t][v][1] & hmask) for v in range(n)] for t in range(T + 1)]
    oddc = [v for v in range(n) if ow[v] == 1 and len(succ[v]) > 1]; evc = [v for v in range(n) if ow[v] == 0 and len(succ[v]) > 1]; evs = set(evc)
    for t in range(T + 1):
        for v in range(n):
            w = nxt[t][v]
            if (v in Hs and cls[t][v] < cls[t][w]) or (v not in Hs and cls[t][v] != cls[t][w]): c["K3"] += 1
        for g in oddc:
            if cls[t][g] != min(cls[t][y] for y in succ[g]): c["K4"] += 1
        if t < T:
            for v in range(n):
                if E.cmp(val[t][v], val[t + 1][v]) > 0: c["F1"] += 1
                if cls[t + 1][v] < cls[t][v]: c["K1"] += 1
            for x in evc: c["K5"] += sum(1 for y in succ[x] if cls[t + 1][x] < cls[t][y])
            if cls[t + 1] == cls[t]: c["oddflipQ"] += sum(1 for g in oddc if tau[t][g] != tau[t + 1][g])
    for b in (range(1, T + 1) if ALLB else [T]): level(b, n, c, cls, nxt, sig, tau, succ, evc, evs, oddc, Pv)
def level(b, n, c, cls, nxt, sig, tau, succ, evc, evs, oddc, Pv):
    fr = []
    for t in range(b + 1):
        lag = [v for v in range(n) if cls[t][v] != cls[b][v]]
        if not lag: fr.append(None); continue
        m = (max if CTRL == "1" else min)(cls[t][v] for v in lag); fr.append((set(lag), m, frozenset(v for v in lag if cls[t][v] == m)))
    phis = set(); first_empty = next(t for t in range(b + 1) if fr[t] is None); c["tailmax"] = max(c["tailmax"], b - first_empty)
    for t in range(b):
        if fr[t] is None: continue
        lag, m, F = fr[t]; phis.add((m, len(F))); stall = all(cls[t + 1][v] == cls[t][v] for v in F)
        if fr[t + 1] is not None:
            p1, p2 = (m, -len(F)), (fr[t + 1][1], -len(fr[t + 1][2]))
            if p2 < p1 or (stall and (p2 != p1 or fr[t + 1][2] != F)) or (not stall and p2 == p1): c["L1"] += 1
        elif stall: c["L1"] += 1
        alpha = [z for z in F if z in evs and nxt[t][z] not in lag]
        c["L3m"] += sum(1 for z in alpha if m != cls[b][nxt[t][z]])
        beta = False
        for v0 in F:
            seen = set(); v = v0
            while v in F and v not in seen: seen.add(v); v = nxt[t][v]
            if v in F: beta = True; break
        if not alpha and not beta: c["L3"] += 1
        if stall:
            c["stalls"] += 1; smap = {z: (sig[b][z] if z in evs else nxt[t][z]) for z in F}
            c["L4"] += sum(1 for z in F if smap[z] not in F)
            z = next(iter(F)); seen = set()
            while z in F and z not in seen: seen.add(z); z = smap[z]
            if z not in F: c["L4c"] += 1
        else: c["nonstalls"] += 1
    if len(phis) > 2 * len(Pv) * n: c["L5"] += 1
    t = 0
    while t < b:
        if fr[t] is None: t += 1; continue
        u = t
        while t + 1 < b and fr[t + 1] is not None and (fr[t + 1][1], fr[t + 1][2]) == (fr[u][1], fr[u][2]): t += 1
        v = t; t += 1
        if v == u: continue
        c["plateaus"] += 1; c["platmax"] = max(c["platmax"], v - u); m = fr[u][1]; Y = set(x for x in range(n) if cls[u][x] <= m)
        for s in range(u, v + 1):
            for x in range(n):
                if (x in Y) != (cls[s][x] <= m) or (x in Y and cls[s][x] != cls[u][x]): c["P1"] += 1
                if x in Y and nxt[s][x] not in Y: c["P2"] += 1
            for x in evc:
                if x in Y: c["P3"] += sum(1 for y in succ[x] if y not in Y)
            for g in oddc:
                if g in Y and (cls[s][tau[s][g]] != cls[s][g] or any(cls[s][y] < cls[s][g] for y in succ[g])): c["P4w"] += 1
        for s in range(u, v): c["oddflipY"] += sum(1 for g in oddc if g in Y and tau[s][g] != tau[s + 1][g])
def xcheck(fn):
    import pg
    from si import Engine
    n, n0, pr, ow, succ, start = frompg(fn); g = pg.Game(pr, ow, succ); Er = Engine(g); E, hist = howard(n, n0, pr, ow, succ, start, 20000)
    for t, (sigma, val, tau, nxt) in enumerate(hist):
        vs, tb = Er.evaluate(tuple(sigma[v] if ow[v] == 0 else -1 for v in range(n)))
        for v in range(n):
            assert vs[v][0] == val[v][0] and vs[v][1] == val[v][1] and vs[v][2] == val[v][2], ("value differs", fn, t, v)
    return len(hist) - 1
if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "--pg":
        for fn in a[1:]:
            c = collections.Counter(); n, n0, pr, ow, succ, start = frompg(fn); run(n, n0, pr, ow, succ, start, c)
            print("gen210 pg", os.path.basename(fn), "ctrl", CTRL, "H", GENH, "n", n, show(c), flush=True)
    elif a[0] == "--xcheck":
        for fn in a[1:]: print("gen210 xcheck", os.path.basename(fn), "T", xcheck(fn), "OK", flush=True)
    else:
        seed, cnt, n0, d, deg, evtop = (int(x) for x in a[:6]); rng = random.Random(seed); c = collections.Counter()
        for i in range(cnt):
            n, n0_, pr, ow, succ = gen(rng, n0, d, deg, evtop)
            run(n, n0_, pr, ow, succ, [rng.choice(succ[v]) if ow[v] == 0 else -1 for v in range(n)], c, cap=3000)
        print("gen210 rand seed", seed, "games", cnt, "n0", n0, "d", d, "deg", deg, "evtop", evtop, "ctrl", CTRL, "H", GENH, show(c), flush=True)
