#!/usr/bin/env python3
"""Box 216 V1 (L-NEW successor 76): run facts and RESULTS R128's lemmas checked on N5's KEY RUN (box 190 n5v.step, mode G216_MODE = spec
(default, N5) | xi (N5'-xi = Howard)) from S3 on Gamma3(G) (box 189 gamma3.build, all pads) up to its first fallback, states 0..Tk.
Values: si.Engine's Xi_sigma (VJ value against sigma-bar = Odd's optimal reply, tb); key = Engine.key; plays follow sigma and tb.
Must-0 (RF items of the box 216 table; unit in brackets):
  f1      [(step, vertex)]   key_(t+1)(v) < key_t(v)                                                          (F1)
  strict  [(step, mover)]    sigma(x) changes and key_(t+1)(x) <= key_t(x)                                     (STRICT)
  imp     [(step, mover)]    sigma(x) changes to a successor not strictly key_t-better; or a non-mover Even vertex changes   ([IMP3] / F5's 2nd half)
  grfail  [flip]             gate o flips at t from p to q and key_t(p) == key_(t-1)(p)                        (GATE-RACE (a))
  gr2fail [gate]             flips(o) > min(ch_p + ch_q, 2 min(ch_p, ch_q) + 1)                                (GATE-RACE (b))
  efp     [gate]             relocks > ch_pe, or unlocks > 1 + relocks, or unlocks > ch_pb                     (E-FACE-PAYS (a))
  npshape [(state, gate)]    e_o in E_t(pb) but not (tb(o) = pe, Lambda(pb) = Lambda(pe), E(pe) subset of E(pb))   (NP-SHAPE (a))
  stepb   [(step, vertex)]   Omega(x) changes at t but no vertex of P_(t-1)(x) changes successor at t          (STEP-BOUND)
  par     [change of E(b) in a Lambda-interval] the top x is not on the new play only and after the split, or an expelled z is not
                             on the old play only, below x and after the split                                 (PARALLEL (i)-(iii))
  pexp    [same-pair couple] two expulsions of z at b through the same split pair (u', b') inside one Lambda-interval of b,
                             E_s'(b') cap U_z not lex-larger than E_s(b') cap U_z                              (PAIR-EXPEL)
  ssimp   [(mover, window)]  more than deg - 1 moves of x on a maximal window of constant weak order of x's successors   (SAME-SUFFIX-IMP)
  loud    [run]              Q > sum_v (D^tot_E(v) - 1), Q = #steps at which some vertex changes class (Lambda, E)   (F-cls3 / LOUD-RF)
HOW items, descriptive (expected > 0 for N5 where its rule differs from Howard's; must be 0 in xi mode):
  f5best  [(step, mover)]    sigma_(t+1)(x) not key_t-best, or a key_t-best sigma_t(x) left                     (F5's first half)
  dom     [(step, mover, successor y)]  key_(t+1)(x) < key(ext(x, Omega_t(y)))                                  (DOM)
Descriptive: Tk, Q, Wq (longest quiet window, steps), sumD, flips, couples (same-pair expulsion couples), moves.
Controls: G216_CTRL=1: f1 tested with the order reversed (fires); G216_CTRL=2: Odd's face read as the LARGER face in grfail / gr2fail /
  efp (grfail fires); G216_CTRL=3: pexp tested with the order reversed (fires where couples exist).
Usage: gate216.py G.json ... | gate216.py --rand SEED COUNT MODE [cyc]"""
import sys, os, json, random, collections
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [os.path.join(ROOT, p) for p in ("experiments/new/box195", "experiments/new/box189", "experiments/new/box190",
                "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
os.environ.setdefault("EG195_ROOT", ROOT)
import eg195, gamma3, n5v, n5x
MODE = os.environ.get("G216_MODE", "spec"); CTRL = os.environ.get("G216_CTRL", "0")
MUST0 = ("f1", "strict", "imp", "grfail", "gr2fail", "efp", "npshape", "stepb", "par", "pexp", "ssimp", "loud")
DESC = ("f5best", "dom", "Tk", "Q", "Wq", "sumD", "flips", "couples", "moves")
MAXK = ("Tk", "Wq")

def cyclic(G):
    adj = {x: [xt for (_, xt, _) in G["opts"][x] if xt >= 0] for x in range(G["N"])}; col = {}
    def dfs(x):
        col[x] = 1
        for y in adj[x]:
            if col.get(y) == 1 or (y not in col and not dfs(y)): return False
        col[x] = 2; return True
    return int(not all(x in col or dfs(x) for x in adj))

def one(G, cap=20000):
    g0, _, _, V = gamma3.build(G, eg195.PADS); g = eg195.topg(g0); n = g.n; name = {v: k for k, v in V.items()}
    E, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None)
    s0 = list(sigma); movers = [V[("x", x)] for x in range(G["N"])]; mset = set(movers)
    evs = [v for v in range(n) if isinstance(name[v], tuple) and name[v][0] == "e"]; ES = sum(E.bit[v] for v in evs)
    O = [(x, k) for x in range(G["N"]) for k in range(len(G["opts"][x]))]
    gates = [(V[("g", o)], V[("pe", o)], V[("pbeta", o)], V[("e", o)]) for o in O]
    H = []
    while len(H) <= cap:
        vs, tb = E.evaluate(tuple(sigma)); H.append((tuple(sigma), vs, tb))
        res = n5v.step(g, E, Ed, sigma, tau, MODE)
        if res is None or res[4]: break
        sigma, tau = list(res[0]), list(res[1])
    T = len(H) - 1; c = collections.Counter(); c["Tk"] = T
    K = [[E.key(H[t][1][v]) for v in range(n)] for t in range(T + 1)]
    nx = [[H[t][0][v] if g.owner[v] == 0 else H[t][2][v] for v in range(n)] for t in range(T + 1)]
    lam = lambda t, v: H[t][1][v][0]
    es = lambda t, v: H[t][1][v][1] & ES
    def play(t, v):
        P = [v]; seen = {v}
        while True:
            y = nx[t][P[-1]]
            if y in seen: return P
            P.append(y); seen.add(y)
    kl = lambda msk: sorted((E.rank[f] for f in evs if msk & E.bit[f]), reverse=True)
    # run facts
    for t in range(T):
        for v in range(n):
            bad = K[t + 1][v] > K[t][v] if CTRL == "1" else K[t + 1][v] < K[t][v]
            if bad: c["f1"] += 1
        for x in range(n):
            if g.owner[x] != 0: continue
            old, new = H[t][0][x], H[t + 1][0][x]
            if x not in mset:
                if old != new: c["imp"] += 1
                continue
            best = max(K[t][y] for y in g.succ[x])
            if old != new:
                c["moves"] += 1
                if not K[t][new] > K[t][old]: c["imp"] += 1
                if not K[t + 1][x] > K[t][x]: c["strict"] += 1
            if K[t][new] != best or (K[t][old] == best and new != old): c["f5best"] += 1
            for y in g.succ[x]:
                if K[t + 1][x] < E.key(E.extend(x, H[t][1][y])): c["dom"] += 1
    # GATE-RACE, E-FACE-PAYS, NP-SHAPE
    ch = lambda v: sum(1 for t in range(1, T + 1) if K[t][v] != K[t - 1][v])
    for (o, pe, pb, e) in gates:
        if CTRL == "2": ch_ = [pe if K[t][pe] > K[t][pb] else pb for t in range(T + 1)]
        else: ch_ = [nx[t][o] for t in range(T + 1)]
        fl = rel = unl = 0
        for t in range(1, T + 1):
            if ch_[t] == ch_[t - 1]: continue
            fl += 1; p = ch_[t - 1]
            if K[t][p] == K[t - 1][p]: c["grfail"] += 1
            if ch_[t] == pb: rel += 1
            else: unl += 1
        c["flips"] += fl; cp, cq = ch(pe), ch(pb)
        if fl > min(cp + cq, 2 * min(cp, cq) + 1): c["gr2fail"] += 1
        if rel > cp or unl > 1 + rel or unl > cq: c["efp"] += 1
        for t in range(T + 1):
            if es(t, pb) & E.bit[e]:
                if not (nx[t][o] == pe and lam(t, pb) == lam(t, pe) and es(t, pe) & ~es(t, pb) == 0): c["npshape"] += 1
    # STEP-BOUND: reverse reachability from the changed vertices in the functional graph nx[t-1]
    for t in range(1, T + 1):
        chg = [v for v in range(n) if nx[t][v] != nx[t - 1][v]]
        pred = collections.defaultdict(list)
        for v in range(n): pred[nx[t - 1][v]].append(v)
        reach = set(chg); st = list(chg)
        while st:
            y = st.pop()
            for v in pred[y]:
                if v not in reach: reach.add(v); st.append(v)
        for v in range(n):
            if K[t][v] != K[t - 1][v] and v not in reach: c["stepb"] += 1
    # SAME-SUFFIX-IMP: moves on maximal windows of constant weak order
    for x in movers:
        if len(g.succ[x]) < 2: continue
        def wo(t):
            ks = sorted(set(K[t][y] for y in g.succ[x])); return tuple(ks.index(K[t][y]) for y in g.succ[x])
        cur = None; mv = 0
        for t in range(T):
            o = wo(t)
            if o != cur: cur = o; mv = 0
            if H[t + 1][0][x] != H[t][0][x]:
                mv += 1
                if mv == len(g.succ[x]): c["ssimp"] += 1
    # LOUD-RF: classes (Lambda, E)
    cls = [[(lam(t, v), es(t, v)) for v in range(n)] for t in range(T + 1)]
    c["sumD"] = sum(len({cls[t][v] for t in range(T + 1)}) - 1 for v in range(n))
    loud = [any(cls[t + 1][v] != cls[t][v] for v in range(n)) for t in range(T)]
    c["Q"] = sum(loud); run = 0
    for l in loud:
        run = 0 if l else run + 1; c["Wq"] = max(c["Wq"], run)
    if c["Q"] > c["sumD"]: c["loud"] += 1
    # PAIR-EXPEL: expulsions of z at b inside one Lambda-interval of b, grouped by split pair
    for b in range(n):
        ex = collections.defaultdict(list)
        for s in range(1, T + 1):
            if lam(s, b) != lam(s - 1, b): ex.clear(); continue
            a0, a1 = es(s - 1, b), es(s, b)
            if a0 == a1: continue
            P0, P1 = play(s - 1, b), play(s, b); i = 0
            while i + 1 < min(len(P0), len(P1)) and P0[i + 1] == P1[i + 1]: i += 1
            if i + 1 >= len(P1): continue
            u, bb = P1[i], P1[i + 1]
            x = max((f for f in evs if (a0 ^ a1) & E.bit[f]), key=lambda f: E.rank[f]); S0, S1 = set(P0), set(P1)
            if not (a1 & E.bit[x] and x in S1 and x not in S0 and x in P1[i + 1:]): c["par"] += 1
            for z in evs:
                if a0 & E.bit[z] and not a1 & E.bit[z] and not (z in S0 and z not in S1 and E.rank[z] < E.rank[x] and z in P0[i + 1:]): c["par"] += 1
            for z in evs:
                if a0 & E.bit[z] and not a1 & E.bit[z]: ex[(z, u, bb)].append(s)
            for (z, u_, b_), L in ex.items():
                if len(L) < 2 or L[-1] != s: continue
                hz = sum(E.bit[f] for f in evs if E.rank[f] > E.rank[z])
                for s1 in L[:-1]:
                    c["couples"] += 1; A, B = kl(es(s1, b_) & hz), kl(es(s, b_) & hz)
                    if (not B > A) if CTRL != "3" else B > A: c["pexp"] += 1
    return c

def fmt(c): return "MUST0 " + " ".join("%s %d" % (k, c[k]) for k in MUST0) + " DESC " + " ".join("%s %d" % (k, c[k]) for k in DESC)

if __name__ == "__main__":
    a = sys.argv[1:]; tag = "mode %s ctrl %s" % (MODE, CTRL)
    if a and a[0] == "--rand":
        seed, cnt, mode = int(a[1]), int(a[2]), a[3]; only = len(a) > 4 and a[4] == "cyc"; rng = random.Random(seed); k = 0; tot = collections.Counter()
        while k < cnt:
            G = eg195.gen(rng, mode)
            if G is None or G["N"] < 2 or (only and not cyclic(G)): continue
            k += 1; cc = one(G)
            for key in MUST0 + DESC: tot[key] = max(tot[key], cc[key]) if key in MAXK else tot[key] + cc[key]
        print("rand", mode, "seed", seed, "genomes", k, "cyconly", int(only), tag, fmt(tot), flush=True)
    else:
        for fn in a:
            G = json.load(open(fn)); G = G.get("genome", G)
            print(os.path.basename(fn), tag, fmt(one(G)), flush=True)
