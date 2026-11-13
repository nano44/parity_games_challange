#!/usr/bin/env python3
"""Box 216 V2 XFLIP and V3 JOINT (L-NEW successor 76). N5 (box 190 n5v.step, mode X216_MODE = spec (default) | xi) from SPEC's start.
V2, on N5's WHOLE run (fallbacks included), every Even vertex x with >= 2 successors. Xi_t := the si.Engine key of Xi_(sigma_t) (SPEC S1,
against sigma-bar_t). Degree 2, successors y0 < y1 (index order): d_t(x) = 0 / 1 if Xi_t(y0) / Xi_t(y1) is strictly larger, '=' on a tie;
ties deleted, XF_x := #alternations of the remaining sequence over the states 0..T. Degree d >= 3: OC_x := #t >= 1 whose weak order of
x's successors (rank vector under Xi_t) differs from t - 1's. moves(x) := #steps changing sigma(x).
  xmove  (unit (step, Even vertex)): sigma(x) changes to a successor that is not strictly Xi_(t-1)-better than the old one    [SPEC S2, S4a, S4c]
  xflip  (unit Even vertex of degree 2): moves(x) > 1 + XF_x                                                                [XFLIP]
  xflipd (unit Even vertex of degree d >= 3): moves(x) > (d - 1)(1 + OC_x)                                                 [XFLIP, degree d]
V3, on genomes (Gamma3, all pads): the key run = the steps before the first fallback (states 0..Tk); for every MOVER x of degree 2: KP_t(x)
the key-least option under s_t (box 215's keys from the genome: key_s(x, k) = (gate) at level 0 or wt < 0, else key_s(wt, s(wt)) + (gate),
lexicographic); KF_x = #t in 1..Tk with KP_t != KP_(t-1); XFm_x = XF of x's two options over the states 0..Tk; J_t(x) = k iff option k is
strictly Xi_(t-1)-better than the other AND KP_t(x) = k (t = 1..Tk); JF_x = #alternations of the non-none J values.
  jmove (unit degree-2 mover): moves_key(x) > 1 + JF_x                                                                     [JOINT, first part]
  jfmin (unit degree-2 mover): JF_x > min(KF_x, XFm_x)                                                                     [JOINT, second part]
Descriptive: T (whole run), Tk, fb (fallbacks), deg2, degd, moves, xfsum, ties (states x degree-2 vertex with a tie), and on genomes
  m2 (degree-2 movers), kfsum, xfmsum, jfsum, jfmax, mvkey (moves before the first fallback, summed over degree-2 movers).
Controls: X216_CTRL=1 swaps the two successors' Xi values at degree-2 vertices in xmove's test (the Lead's «swap the gates' Xi values»):
  xmove must fire at every degree-2 move; X216_CTRL=2 tests xflip / xflipd with XF := 0, OC := 0 (fires where a vertex moves twice);
  X216_CTRL=3 permutes the gate indices in the keys (fixed random permutation, seed 5, as box 215's KS_CTRL=1): jmove must fire.
Usage: xflip216.py G.json ... | xflip216.py --pg GAME.pg ... | xflip216.py --rand SEED COUNT MODE [cyc]"""
import sys, os, json, random, collections
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [os.path.join(ROOT, p) for p in ("experiments/new/box195", "experiments/new/box189", "experiments/new/box190",
                "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
os.environ.setdefault("EG195_ROOT", ROOT)
import eg195, gamma3, n5v, n5x, pg
MODE = os.environ.get("X216_MODE", "spec"); CTRL = os.environ.get("X216_CTRL", "0"); CAP = 20000
KEYS = ("xmove", "xflip", "xflipd", "jmove", "jfmin", "T", "Tk", "fb", "deg2", "degd", "moves", "xfsum", "ties",
        "m2", "kfsum", "xfmsum", "jfsum", "jfmax", "mvkey")
MAXK = ("T", "Tk", "jfmax")

def cyclic(G):
    adj = {x: [xt for (_, xt, _) in G["opts"][x] if xt >= 0] for x in range(G["N"])}; col = {}
    def dfs(x):
        col[x] = 1
        for y in adj[x]:
            if col.get(y) == 1 or (y not in col and not dfs(y)): return False
        col[x] = 2; return True
    return int(not all(x in col or dfs(x) for x in adj))

def sgn(a, b): return 0 if a > b else (1 if b > a else None)

def run(g, G=None, V=None):
    """one N5 run; V2 counters always, V3 counters when a genome G (with Gamma3's V) is given"""
    c = collections.Counter(); n = g.n
    E, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None)
    ev = [v for v in range(n) if g.owner[v] == 0 and len(g.succ[v]) >= 2]
    d2 = [v for v in ev if len(g.succ[v]) == 2]; dd = [v for v in ev if len(g.succ[v]) >= 3]; c["deg2"] = len(d2); c["degd"] = len(dd)
    last = {}; XF = collections.Counter(); OC = collections.Counter(); prevord = {}; moves = collections.Counter()
    # V3 state
    g3 = G is not None
    if g3:
        N, lev, opts = G["N"], G["lev"], G["opts"]; gate = G["gate"]
        if CTRL == "3":
            M = sum(len(o) for o in opts); perm = list(range(M)); random.Random(5).shuffle(perm); gate = [[perm[gk] for gk in row] for row in gate]
        order = sorted(range(N), key=lambda x: lev[x])
        def KPof(s):
            K = {}
            for x in order:
                for k, (wt, _, _) in enumerate(opts[x]):
                    K[(x, k)] = ((gate[x][k],) if wt < 0 or lev[x] == 0 else K[(wt, s[wt])] + (gate[x][k],))
            return [min(range(len(opts[x])), key=lambda k: K[(x, k)]) for x in range(N)]
        mv2 = [x for x in range(N) if len(opts[x]) == 2]; c["m2"] = len(mv2)
        optv = {x: {g.succ[x][i]: gamma3.mover_state(G, V, [g.succ[x][i] if y == x else -1 for y in range(n)], eg195.PADS)[x] for i in range(2)} for x in mv2}
        s0 = gamma3.mover_state(G, V, sigma, eg195.PADS); KPp = KPof(s0); keyrun = True
        KF = collections.Counter(); XFm = collections.Counter(); lastm = {}; lastJ = {}; JF = collections.Counter(); mvk = collections.Counter()
    t = 0
    while True:
        vs, _ = E.evaluate(tuple(sigma)); key = [E.key(vs[v]) for v in range(n)]
        for v in d2:
            a, b = g.succ[v]; d = sgn(key[a], key[b])
            if d is None: c["ties"] += 1; continue
            if v in last and last[v] != d: XF[v] += 1
            last[v] = d
            if g3 and keyrun and v in optv:
                dk = optv[v][a] if d == 0 else optv[v][b]          # the strictly better OPTION index
                if v in lastm and lastm[v] != dk: XFm[v] += 1
                lastm[v] = dk
        for v in dd:
            ks = sorted(set(key[w] for w in g.succ[v])); od = tuple(ks.index(key[w]) for w in g.succ[v])
            if v in prevord and prevord[v] != od: OC[v] += 1
            prevord[v] = od
        if t >= CAP: break
        res = n5v.step(g, E, Ed, sigma, tau, MODE)
        if res is None: break
        ns, nt, fb = list(res[0]), list(res[1]), res[4]; c["fb"] += fb
        if fb and g3: keyrun = False
        for v in ev:
            if ns[v] == sigma[v]: continue
            moves[v] += 1; old, new = sigma[v], ns[v]
            better = key[new] > key[old]
            if CTRL == "1" and len(g.succ[v]) == 2: better = key[old] > key[new]
            if not better: c["xmove"] += 1
        if g3 and keyrun:
            s1 = gamma3.mover_state(G, V, ns, eg195.PADS); KPn = KPof(s1)
            for x in mv2:
                if KPn[x] != KPp[x]: KF[x] += 1
                a, b = g.succ[x]; d = sgn(key[a], key[b])
                J = None if d is None else (optv[x][a] if d == 0 else optv[x][b])
                if J is not None and KPn[x] != J: J = None
                if J is not None:
                    if x in lastJ and lastJ[x] != J: JF[x] += 1
                    lastJ[x] = J
                if ns[x] != sigma[x]: mvk[x] += 1
            KPp = KPn; c["Tk"] = t + 1
        sigma, tau = ns, nt; t += 1
    c["T"] = t; c["moves"] = sum(moves.values()); c["xfsum"] = sum(XF.values())
    for v in d2:
        if moves[v] > 1 + (0 if CTRL == "2" else XF[v]): c["xflip"] += 1
    for v in dd:
        if moves[v] > (len(g.succ[v]) - 1) * (1 + (0 if CTRL == "2" else OC[v])): c["xflipd"] += 1
    if g3:
        for x in mv2:
            if mvk[x] > 1 + JF[x]: c["jmove"] += 1
            if JF[x] > min(KF[x], XFm[x]): c["jfmin"] += 1
            c["kfsum"] += KF[x]; c["xfmsum"] += XFm[x]; c["jfsum"] += JF[x]; c["jfmax"] = max(c["jfmax"], JF[x]); c["mvkey"] += mvk[x]
    return c

def genome(G):
    g0, _, _, V = gamma3.build(G, eg195.PADS); g = eg195.topg(g0)
    assert all(V[("x", x)] == x for x in range(G["N"])), "movers are vertices 0..N-1"
    return run(g, G, V)

def fmt(c): return " ".join("%s %d" % (k, c[k]) for k in KEYS)

if __name__ == "__main__":
    a = sys.argv[1:]; tag = "mode %s ctrl %s" % (MODE, CTRL)
    if a and a[0] == "--rand":
        seed, cnt, mode = int(a[1]), int(a[2]), a[3]; only = len(a) > 4 and a[4] == "cyc"; rng = random.Random(seed); k = 0; tot = collections.Counter()
        while k < cnt:
            G = eg195.gen(rng, mode)
            if G is None or G["N"] < 2 or (only and not cyclic(G)): continue
            k += 1; cc = genome(G)
            for key in KEYS: tot[key] = max(tot[key], cc[key]) if key in MAXK else tot[key] + cc[key]
        print("rand", mode, "seed", seed, "genomes", k, "cyconly", int(only), tag, fmt(tot), flush=True)
    elif a and a[0] == "--pg":
        for fn in a[1:]:
            print(os.path.basename(fn), tag, fmt(run(pg.parse(open(fn).read()))), flush=True)
    else:
        for fn in a:
            G = json.load(open(fn)); G = G.get("genome", G)
            print(os.path.basename(fn), tag, fmt(genome(G)), flush=True)
