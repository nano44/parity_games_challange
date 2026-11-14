#!/usr/bin/env python3
"""Box 196 (L-NEW successor 64): the box-194 / P-N5-ASC lemmas checked NATIVELY on the Gamma3 run, i.e. on the states 0..T3 of N5'-xi
(box 190 n5v.step, mode xi; or N5 with Q196_MODE=spec) from S3 on Gamma3(G) (box 189 gamma3.build, all pads), up to its first fallback.
Values: Xi_sigma on Gamma3 (si.Engine, sigma-bar = Odd's optimal counterstrategy). Per run, counters (unit in brackets):
  nonstd    states 0..T3 that are not standard: sigma off the movers != S3's, or tau != tau0                    [states]   (REACH3-CYC)
  nohoward  (state, mover) pairs where the next sigma(x) is not a best option, or leaves a best sigma(x)          [pairs]    (REACH3-CYC)
  cnlow     (state, vertex) pairs, vertex != c_X, whose cycle node has priority < 3, or whose P-set holds a pad, mover or gate    [pairs]    (CN2-3)
  locfail   (state, gate) pairs where sigma-bar's face has a strictly LARGER value than the other face             [pairs]    (LOC-GATE3)
  ties      (state, gate) pairs with equal face values                                                            [pairs]    (NO-TIE3)
  bonly     (state, vertex) pairs, vertex not c_W, not a level-0 e or its pe pad, whose cycle node is an e-vertex or
            at least as relevant as the least relevant e-vertex                                                    [pairs]    (B-ONLY3)
  k2fail    states with sigma-bar(K2) != r                                                                       [states]   (LOC-K2-3)
  wfail     quiet windows longer than L3 := (M+1)(2M+1)(N+1) + N(n3-1)                                            [windows]  (QUIET3)
  crossflip sigma-bar flips on quiet steps at gates whose faces (pe, pbeta) are in different classes at both states [flips] (QUIET3 Q1)
  Tfail     runs with T3 > Q + (Q+1) L3                                                                           [runs]     (T-QUIET3)
  upfail    (state, vertex) pairs whose e-sequence (e-vertices of Pi in play order) has more than U(G) ascents     [pairs]    (UP-B3)
  emon      (step, vertex) pairs with Lambda kept and the e-set lex-decreasing                                    [pairs]    (E-MON3)
Record only: T3, T_CYC (box191 idealcyc on Gamma(G), its own tie rule), tdiff (runs with T3 != T_CYC), seqdiff (runs whose mover
sequences differ), Q, W (longest quiet window), maxasc, sumDE. class(v) := (Lambda(v), e-vertices of Pi(v)).
Controls: Q196_CTRL=1 (L3 := 0 and U(G) := -1: wfail, Tfail, upfail must fire); Q196_CTRL=2 (locfail tested with the order reversed); Q196_CTRL=3 (B-ONLY3 tested with no excluded vertex: c_W and the level-0 e must fire).
Usage: qt3_196.py FAMILY SEED COUNT (families of box195 eg195.gen) | qt3_196.py --files G.json ..."""
import sys, os, json, random, collections
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.environ.get("Q196_ROOT") or os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [os.path.join(ROOT, p) for p in ("experiments/new/box195", "experiments/new/box191", "experiments/new/box189",
                "experiments/new/box190", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
os.environ.setdefault("EG195_ROOT", ROOT)
import eg195, gamma3, n5v, n5x, idealcyc
MODE = os.environ.get("Q196_MODE", "xi"); CTRL = os.environ.get("Q196_CTRL", "0")

def ascents(seq, rank): return sum(1 for a, b in zip(seq, seq[1:]) if rank[b] > rank[a])

def check(G, cap=20000):
    g0, _, _, V = gamma3.build(G, eg195.PADS); g = eg195.topg(g0); n = g.n; name = {v: k for k, v in V.items()}
    K2, r, cX = V[("K", 2)], V["r"], V["cX"]
    N = G["N"]; O = [(x, k) for x in range(N) for k in range(len(G["opts"][x]))]; M = len(O)
    lev = G["lev"]; UG = sum(1 for x, k in O if G["opts"][x][k][1] >= 0 and lev[G["opts"][x][k][1]] > lev[x])
    L3 = (M + 1) * (2 * M + 1) * (N + 1) + N * (n - 1)
    if CTRL == "1": L3, UG = 0, -1
    E, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None)
    tau0 = list(tau); s0 = list(sigma)
    movers = [V[("x", x)] for x in range(N)]; mset = set(movers)
    kind = {v: (name[v][0] if isinstance(name[v], tuple) else name[v]) for v in range(n)}
    low = {v for v in range(n) if kind[v] in ("x", "g", "m", "pe", "pbeta", "pb", "pA", "s", "q", "r")}
    lowmask = sum(E.bit[v] for v in low); evs = [v for v in range(n) if kind[v] == "e"]; ES = sum(E.bit[v] for v in evs)
    gates = [(V[("g", o)], V[("pe", o)], V[("pbeta", o)]) for o in O]
    cW = V["cW"]; emin = min(E.rank[v] for v in evs)
    excl = {cW} | {V[("e", o)] for o in O if G["opts"][o[0]][o[1]][0] < 0} | {V[("pe", o)] for o in O if G["opts"][o[0]][o[1]][0] < 0}
    if CTRL == "3": excl = set()
    c = collections.Counter(); hist = []; seqs = []
    it = 0
    while it < cap:
        vs, sb = E.evaluate(tuple(sigma)); hist.append((vs, sb)); seqs.append(tuple(sigma[x] for x in movers))
        if [sigma[v] for v in range(n) if g.owner[v] == 0 and v not in mset] != [s0[v] for v in range(n) if g.owner[v] == 0 and v not in mset] or list(tau) != tau0: c["nonstd"] += 1
        for v in range(n):
            if (v != cX and g.prio[vs[v][0]] < 3) or vs[v][1] & lowmask: c["cnlow"] += 1
        for gt, pe, pb in gates:
            a = sb[gt]; b = pb if a == pe else pe; ka, kb = E.key(vs[a]), E.key(vs[b])
            if ka == kb: c["ties"] += 1
            elif (ka > kb) != (CTRL == "2"): c["locfail"] += 1
        if sb[K2] != r: c["k2fail"] += 1
        for v in range(n):
            if v not in excl and E.rank[vs[v][0]] >= emin: c["bonly"] += 1
        for v in range(n):                                    # e-sequence of Pi_t(v) in play order
            seq = []; seen = set(); u = v
            while u not in seen:
                seen.add(u)
                if kind[u] == "e" and vs[v][1] & E.bit[u]: seq.append(u)
                u = sigma[u] if g.owner[u] == 0 else sb[u]
            a = ascents(seq, E.rank); c["maxasc"] = max(c["maxasc"], a)
            if a > UG: c["upfail"] += 1
        res = n5v.step(g, E, Ed, sigma, tau, MODE)
        if res is None or res[4]: break                       # stop at the first fallback (or the end)
        ns, nt = res[0], res[1]
        for x in movers:
            best = max(E.key(vs[w]) for w in g.succ[x])
            if E.key(vs[ns[x]]) != best or (E.key(vs[sigma[x]]) == best and ns[x] != sigma[x]): c["nohoward"] += 1
        sigma, tau = ns, nt; it += 1
    T3 = len(hist) - 1
    cls = [[(vs[v][0], vs[v][1] & ES) for v in range(n)] for vs, _ in hist]
    Q = W = cur = 0
    for t in range(1, T3 + 1):
        pv, vv = hist[t - 1][0], hist[t][0]
        for v in range(n):
            if pv[v][0] == vv[v][0] and E.key((0, pv[v][1] & ES, 0))[1:2] > E.key((0, vv[v][1] & ES, 0))[1:2]: c["emon"] += 1
        if cls[t] != cls[t - 1]: Q += 1; cur = 0; continue
        cur += 1; W = max(W, cur)
        if cur > L3: c["wfail"] += 1
        for gt, pe, pb in gates:
            if hist[t][1][gt] != hist[t - 1][1][gt] and cls[t][pe] != cls[t][pb] and cls[t - 1][pe] != cls[t - 1][pb]: c["crossflip"] += 1
    if T3 > Q + (Q + 1) * L3: c["Tfail"] += 1
    sumDE = sum(len({cls[t][v] for t in range(T3 + 1)}) - 1 for v in range(n))
    st = idealcyc.run(G); Tc = len(st) - 1
    inv = {V[("m", (x, k))]: k for x, k in O}
    s3 = [tuple(inv[m] for m in s) for s in seqs]
    return dict(T3=T3, Tcyc=Tc, tdiff=int(T3 != Tc), seqdiff=int(s3 != [tuple(s) for s in st]), Q=Q, W=W, L3=L3, UG=UG, sumDE=sumDE, **c)

KEYS = ("nonstd", "nohoward", "cnlow", "locfail", "ties", "bonly", "k2fail", "wfail", "crossflip", "Tfail", "upfail", "emon", "tdiff", "seqdiff")
def summarize(name, rows):
    tot = collections.Counter()
    for rw in rows:
        for k in KEYS: tot[k] += rw.get(k, 0)
    mx = {k: max(rw.get(k, 0) for rw in rows) for k in ("T3", "Tcyc", "W", "maxasc", "UG", "sumDE", "Q")}
    print(f"{os.environ.get('Q196_TAG', '')}{name} mode {MODE} ctrl {CTRL} runs {len(rows)} " + " ".join(f"{k} {tot[k]}" for k in KEYS)
          + " max " + " ".join(f"{k} {v}" for k, v in mx.items()), flush=True)

if __name__ == "__main__":
    if sys.argv[1] == "--files":
        for fn in sys.argv[2:]:
            G = json.load(open(fn))
            if isinstance(G, dict) and "genome" in G: G = G["genome"]
            if not (isinstance(G, dict) and "opts" in G and "start" in G): print(os.path.basename(fn), "skipped"); continue
            summarize(os.path.basename(fn), [check(G)])
    else:
        fam, seed, cnt = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed)
        summarize(f"{fam} seed {seed}", [check(eg195.gen(rng, fam)) for _ in range(cnt)])
