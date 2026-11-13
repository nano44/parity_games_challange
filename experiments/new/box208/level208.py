#!/usr/bin/env python3
"""Box 208 (L-NEW successor 72): the lowest-lagging-class potential (Lemma LEVEL, Theorem WIN, Theorems R-HEIGHT / K1-TCYC / FVS-TCYC of
docs/new/N5-LEVEL-box208.md). All statements there are CANDIDATES on IDEAL-CYC(G) (RESULTS R118 (a)) only.
Model: IDEAL-CYC(G) (default; box203 gfc203.hist_ideal / box191 idealcyc). With --g3: N5'-xi from S3 on Gamma3(G) up to its first
fallback (engine as box203 gfc203.hist_g3, with the Even strategy kept); DATA only, nothing is claimed on Gamma3.
class_t(v) := (reward(Lambda_t(v)), E_t(v)): reward = the priority of the cycle node, negated if odd; E_t(v) = the e-vertices of Pi_t(v)
as a number (bit i = the i-th least relevant e-vertex). The order on classes is the order on these pairs.
Reference state b (default: the last state). For a <= t <= b:
  LAG_t = {v : class_t(v) != class_b(v)}; m_t = the lowest class of a lagging vertex; FRONT_t = the lagging vertices of class m_t;
  Phi_t = (m_t, -|FRONT_t|). A step t -> t+1 (t < b, LAG_t nonempty) is a STALL if no vertex of FRONT_t changes class at it.
Must-0 counters (unit: states t < b with LAG_t nonempty, unless stated):
  monofail  (unit (vertex, step)): a class falls                                                                        [(K1)]
  k3fail    (unit (vertex, state)): a vertex that is not an e-vertex whose class differs from its successor's on the play, or an
              e-vertex e with a mover successor w whose class is not (Lambda(w), {e} + E(w)) or is not above class(w)   [(K3)]
  k4fail    (unit (Odd vertex with two successors, state)): its class is not the lower of its successors' classes       [(K4)]
  k5fail    (unit (mover, successor, step)): class_(t+1)(x) < class_t(y)                                                [(K5)]
  einF      : FRONT_t contains an e-vertex (on Gamma3: or a pad pe_g)                                                   [(L2)]
  l3fail    : neither (alpha) a mover in FRONT_t whose successor does not lag, nor (beta) the cycle of some play inside FRONT_t  [(L3)]
  phifail   : Phi_(t+1) < Phi_t, or Phi_(t+1) = Phi_t at a non-stall step, or Phi_(t+1) != Phi_t at a stall             [(L1)]
  stallnocyc: a stall, and the map s (mover -> its successor at b; Odd vertex -> its successor at t; other -> its successor) has no
              cycle inside FRONT_t                                                                                      [(L4)]
  nofvs     (unit stalls, reference the last state): the s-cycle found contains no mover of the feedback set F0 (k <= KMAX only)
  rstall    (unit steps, k = 1 only, reference the last state): a stall at which the class of a feedback vertex changes  [R-HEIGHT]
  boundfail (unit genomes): more than 2M(N + 2M) values of Phi (Gamma3: 2M(N + 4M)), or at k = 1 T > P(A + 1) + N       [(L5), K1-TCYC]
  For the feedback sets S tried (at k = 1: every single feedback vertex; at 2 <= k <= KMAX: one minimum feedback set F0; k = 0: the
  empty set) and every maximal interval [a, b] of states on which every mover of S keeps its class (reference b):
  winstall  (unit steps): stalls before LAG becomes empty                                                               [WIN (i)]
  wbeta     (unit states): case (beta) of (L3) without case (alpha)                                                     [WIN (ii)]
  wl3fail   (unit states): (L3) fails inside the interval
  wmid      (unit intervals): a step that changes a class after LAG became empty                                        [WIN (iii)]
  wbound    (unit intervals): more than M(N + 2M) steps before LAG is empty (Gamma3: M(N + 4M)), or more than N after   [WIN]
Descriptive: T, k (99 = above fvs202's cap), levels (#values of m_t), phivals (#values of Phi), stalls, stallloud (stalls at which
some vertex changes class), plat (#maximal runs of stalls), platmax (longest), windows, wmax (most steps of one interval before LAG
is empty), wlev (most values of m in one interval), DR (#classes of the first feedback vertex over the run; k = 1 only).
Controls LV_CTRL: 1 = S := one mover that is NOT a feedback vertex (winstall or wbeta must fire on some genome);
                  2 = FRONT_t := the lagging vertices of the HIGHEST lagging class (l3fail and stallnocyc must fire).
Other engines: --dump OUT.json G.json writes this engine's history {genome, g3, n, T, movers, kind, owner, succ, ebit, nxt, cls};
               --hist HIST.json runs every counter on a history in that format (nxt[t][v] = the successor of v on its play at t,
               cls[t][v] = [reward, E]), so a second engine only has to produce that file.
Usage: level208.py [--g3] G.json ... | level208.py [--g3] --rand SEED COUNT MODE | level208.py [--g3] --dump OUT.json G.json | level208.py --hist HIST.json ...
       (MODE: k1 = box202 k1srch202.mk at k = 1; else an eg195.gen mode: rand, dense, deep, noesc, ...)"""
import sys, os, json, random, collections, itertools
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.environ.get("ROOT") or os.path.abspath(os.path.join(HERE, "..", "..", ".."))
os.environ.setdefault("EG195_ROOT", ROOT)
sys.path[:0] = [os.path.join(ROOT, p) for p in ("experiments/new/box203", "experiments/new/box202", "experiments/new/box195", "experiments/new/box191",
                "experiments/new/box189", "experiments/new/box190", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
import fvs202
CTRL = os.environ.get("LV_CTRL", "0"); KMAX = 3

def prep(G, g3=False):
    """this engine's history: n, T, nxt[t][v] (the successor of v on its play at t), cls[t][v], kind[v], movers, succ, owner, ebit"""
    N = G["N"]
    if not g3:
        import gfc203, idealcyc
        H, n, E, V, gates = gfc203.hist_ideal(G); ST = idealcyc.run(G); h, s0, mv, inv = idealcyc.build(G); T = len(H) - 1
        prio, gsucc, owner = h.prio, h.succ, h.owner; nxt = []
        for t in range(T + 1):
            s = list(s0)
            for x in range(N): s[mv[x]] = V[("g", (x, ST[t][x]))]
            nxt.append([s[v] if h.owner[v] == 0 else H[t][1][v] for v in range(n)])
        vals = [H[t][0] for t in range(T + 1)]
    else:
        import eg195, gamma3, n5v, n5x
        g0, _, _, V = gamma3.build(G, eg195.PADS); g = eg195.topg(g0); n = g.n
        E, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None); vals = []; nxt = []
        while len(vals) <= 20000:
            vs, tb = E.evaluate(tuple(sigma)); vals.append(vs); nxt.append([sigma[v] if g.owner[v] == 0 else tb[v] for v in range(n)])
            res = n5v.step(g, E, Ed, sigma, tau, "xi")
            if res is None or res[4]: break
            sigma, tau = res[0], res[1]
        T = len(vals) - 1; prio, gsucc, owner = g.prio, g.succ, g.owner
    kind = [None] * n
    for k, v in V.items(): kind[v] = k[0] if isinstance(k, tuple) else k
    evs = [v for v in range(n) if kind[v] == "e"]; ebits = sorted(E.rank[v] for v in evs); pos = {rk: i for i, rk in enumerate(ebits)}
    def es(mask):
        x = 0
        for rk in ebits:
            if (mask >> rk) & 1: x |= 1 << pos[rk]
        return x
    rew = lambda v: prio[v] if prio[v] % 2 == 0 else -prio[v]
    cls = [[(rew(vals[t][v][0]), es(vals[t][v][1])) for v in range(n)] for t in range(T + 1)]
    return dict(genome=G, g3=g3, n=n, T=T, movers=[V[("x", x)] for x in range(N)], kind=kind, owner=list(owner), succ=[list(s) for s in gsucc],
                ebit={v: 1 << pos[E.rank[v]] for v in evs}, nxt=nxt, cls=cls)

def load(fn):
    P = json.load(open(fn)); P["ebit"] = {int(k): v for k, v in P["ebit"].items()}; P["cls"] = [[tuple(c) for c in row] for row in P["cls"]]
    return P

def scycle(F, s):
    """a cycle of the map s inside the set F, or None"""
    state = {}
    for v0 in sorted(F):
        path = []; v = v0
        while v in F and v not in state:
            state[v] = 1; path.append(v); v = s(v)
        if v in F and state.get(v) == 1:
            return path[path.index(v):]
        for u in path: state[u] = 2
    return None

def potential(P, a, b, c, F0=None, watch=()):
    """Lemma LEVEL on the states a..b with reference b; counters into c; returns (kinds per step, #levels, #Phi values)"""
    n, cls, nxt, kind = P["n"], P["cls"], P["nxt"], P["kind"]; mvset = set(P["movers"]); kinds = []; levels = set(); phis = set()
    def front(t):
        lag = [v for v in range(n) if cls[t][v] != cls[b][v]]
        if not lag: return None, None, None
        m = (max if CTRL == "2" else min)(cls[t][v] for v in lag)
        return set(lag), m, set(v for v in lag if cls[t][v] == m)
    cur = front(a) if a < b else (None, None, None)
    for t in range(a, b):
        lagset, m, F = cur; cur = front(t + 1)
        if lagset is None:
            kinds.append("q" if cls[t + 1] == cls[t] else "X"); continue
        phi = (m, -len(F)); levels.add(m); phis.add(phi)
        stall = not any(cls[t + 1][v] != cls[t][v] for v in F)
        if cur[0] is not None and CTRL != "2":
            phi2 = (cur[1], -len(cur[2]))
            if phi2 < phi or (phi2 == phi) != stall: c["phifail"] += 1
        if any(kind[v] in ("e", "pe") for v in F): c["einF"] += 1
        alpha = any(nxt[t][z] not in lagset for z in F if z in mvset); beta = False
        if not alpha:
            for v0 in sorted(F):
                seen = {}; v = v0
                while v not in seen: seen[v] = len(seen); v = nxt[t][v]
                if all(u in F for u, i in seen.items() if i >= seen[v]): beta = True; break
        if not (alpha or beta): c["l3fail"] += 1
        if beta and not alpha: c["beta"] += 1
        if not stall: kinds.append("P"); continue
        kinds.append("S"); c["stalls"] += 1
        if cls[t + 1] != cls[t]: c["stallloud"] += 1
        if any(cls[t + 1][v] != cls[t][v] for v in watch): c["rstall"] += 1
        cyc = scycle(F, lambda v: nxt[b][v] if v in mvset else nxt[t][v])
        if cyc is None: c["stallnocyc"] += 1
        elif F0 is not None and not (set(cyc) & F0): c["nofvs"] += 1
    return kinds, len(levels), len(phis)

def xiparts(G, removed=()):
    adj = fvs202.xigraph(G); nodes = set(adj) - set(removed)
    return fvs202.cyclic_parts({x: [y for y in adj[x] if y in nodes] for x in nodes}, nodes)

def minfvs(G, k):
    """one minimum feedback vertex set of the Xi-graph (genome indices), by search over the movers on Xi-cycles"""
    parts = xiparts(G); cand = sorted(set().union(*parts)) if parts else []
    for S in itertools.combinations(cand, k):
        if not xiparts(G, S): return list(S)
    return None

def census(P):
    G = P["genome"]; g3 = P["g3"]; c = collections.Counter(); N = G["N"]; M = sum(len(o) for o in G["opts"])
    n, T, cls, nxt, kind, ebit, gsucc, owner, mv = P["n"], P["T"], P["cls"], P["nxt"], P["kind"], P["ebit"], P["succ"], P["owner"], P["movers"]
    k = fvs202.kfvs(G)[0]; c["T"] = T; c["k"] = k if isinstance(k, int) else 99
    for t in range(T + 1):
        for v in range(n):
            w = nxt[t][v]
            if kind[v] == "e":
                if kind[w] == "x" and not (cls[t][v] == (cls[t][w][0], cls[t][w][1] | ebit[v]) and cls[t][v] > cls[t][w]): c["k3fail"] += 1
            elif cls[t][v] != cls[t][w]: c["k3fail"] += 1
            if owner[v] == 1 and len(gsucc[v]) == 2 and cls[t][v] != min(cls[t][u] for u in gsucc[v]): c["k4fail"] += 1
        if t < T:
            c["monofail"] += sum(1 for v in range(n) if cls[t + 1][v] < cls[t][v])
            for x in mv: c["k5fail"] += sum(1 for y in gsucc[x] if cls[t + 1][x] < cls[t][y])
    F0 = minfvs(G, k) if isinstance(k, int) and k <= KMAX else None
    fv = [x for x in range(N) if not xiparts(G, [x])] if k == 1 else []
    kinds, lv, ph = potential(P, 0, T, c, set(mv[x] for x in F0) if F0 is not None else None, [mv[x] for x in fv])
    c["levels"], c["phivals"] = lv, ph; s = "".join(kinds)
    runs = [len(r) for r in s.replace("P", " ").replace("q", " ").replace("X", " ").split()]; c["plat"] = len(runs); c["platmax"] = max(runs, default=0)
    width = N + (4 if g3 else 2) * M; Pc = 2 * M * width; A = M * width + N
    if ph > Pc or (k == 1 and not g3 and T > Pc * (A + 1) + N): c["boundfail"] += 1
    Ss = []
    if k == 1:
        Ss = [[x] for x in fv]; c["DR"] = len(set(cls[t][mv[fv[0]]] for t in range(T + 1)))
        if CTRL == "1": Ss = [[next((y for y in list(range(fv[0] + 1, N)) + list(range(fv[0])) if y not in fv), fv[0])]]
    elif F0 is not None: Ss = [F0]
    for S in Ss:
        sv = [mv[x] for x in S]; a = 0
        for t in range(1, T + 2):
            if t == T + 1 or any(cls[t][v] != cls[t - 1][v] for v in sv):
                b = t - 1; c["windows"] += 1
                if b > a:
                    cw = collections.Counter(); kd, lv, ph = potential(P, a, b, cw); s = "".join(kd)
                    c["winstall"] += cw["stalls"]; c["wbeta"] += cw["beta"]; c["wl3fail"] += cw["l3fail"]
                    pre = len(s.rstrip("qX")); tail = len(s) - pre
                    if "X" in s: c["wmid"] += 1
                    if pre > M * width or tail > N: c["wbound"] += 1
                    c["wmax"] = max(c["wmax"], pre); c["wlev"] = max(c["wlev"], lv)
                a = t
    return c

MUST0 = ("monofail", "k3fail", "k4fail", "k5fail", "einF", "l3fail", "phifail", "stallnocyc", "nofvs", "rstall", "boundfail",
         "winstall", "wbeta", "wl3fail", "wmid", "wbound")
DESC = ("T", "k", "levels", "phivals", "stalls", "stallloud", "plat", "platmax", "windows", "wmax", "wlev", "DR")
def line(name, P, c):
    G = P["genome"]
    return "%s %s ctrl %s N %d M %d %s | %s" % (name, "g3" if P["g3"] else "ideal", CTRL, G["N"], sum(len(o) for o in G["opts"]),
            " ".join("%s %d" % (key, c[key]) for key in MUST0), " ".join("%s %d" % (key, c[key]) for key in DESC))
if __name__ == "__main__":
    a = sys.argv[1:]; g3 = bool(a) and a[0] == "--g3"
    if g3: a = a[1:]
    if a and a[0] == "--rand":
        seed, cnt, mode = int(a[1]), int(a[2]), a[3]; rng = random.Random(seed); g = 0; tot = collections.Counter(); mx = collections.Counter()
        if mode == "k1":
            os.environ["K1_MODE"] = "1"; import k1srch202
            mk = lambda: k1srch202.mk(rng)
        else:
            import eg195
            mk = lambda: eg195.gen(rng, mode)
        while g < cnt:
            G = mk()
            if G is None or G["N"] < 2: continue
            if mode == "k1" and fvs202.kfvs(G)[0] != 1: continue
            g += 1; c = census(prep(G, g3))
            for key in MUST0 + ("stalls", "stallloud", "plat", "windows"): tot[key] += c[key]
            for key in ("T", "k", "levels", "phivals", "platmax", "wmax", "wlev", "DR"): mx[key] = max(mx[key], c[key])
        print("rand", mode, "g3" if g3 else "ideal", "ctrl", CTRL, "seed", seed, "genomes", g, "TOTALS", " ".join("%s %d" % (key, tot[key]) for key in MUST0 + ("stalls", "stallloud", "plat", "windows")),
              "MAX", " ".join("%s %d" % (key, mx[key]) for key in ("T", "k", "levels", "phivals", "platmax", "wmax", "wlev", "DR")), flush=True)
    elif a and a[0] == "--dump":
        P = prep(json.load(open(a[2])), g3); json.dump(P, open(a[1], "w")); print("dumped", os.path.basename(a[2]), "n", P["n"], "T", P["T"])
    elif a and a[0] == "--hist":
        for fn in a[1:]:
            P = load(fn); print(line(os.path.basename(fn), P, census(P)), flush=True)
    else:
        for fn in a:
            P = prep(json.load(open(fn)), g3); print(line(os.path.basename(fn), P, census(P)), flush=True)
