#!/usr/bin/env python3
"""Box 199 (L-NEW successor 66): the SPLIT vertex of every e-set change on the Gamma3 Howard run (box 196-198 engine).
For a vertex v, a Lambda-interval I of v and a change t-1 -> t in I (E_(t-1)(v) != E_t(v)), the split u is the first vertex of v's play
where the plays at t-1 and t leave by different edges. Counters (unit: one change at one (v, I), unless said):
  playfail : the e-set read off the play (sigma_t, Odd's best reply tau_t) differs from the engine's value   [0: plays are the values]
  kindfail : u is neither a mover with sigma changed nor an Odd vertex with tau changed                       [0: Lemma SPLIT (i)]
  hwfail   : u a mover, Om_(t-1)(new) not > Om_(t-1)(old)                                                     [0: SPLIT (ii), F5]
  gtfail   : u Odd, not (Om_(t-1)(old) < Om_(t-1)(new) and Om_t(new) < Om_t(old))                             [0: SPLIT (iii)]
  trfail   : Lambda_(t-1)(u) != w or Lambda_t(u) != w or the change of E(u) has another symmetric difference [0: SPLIT (iv)]
  y-tops (top y = e_(x,k) entering), by split kind: own (u = x), gate (u = gate of y), route (u upstream, mover), routeO (upstream Odd).
  Consecutive y-tops t1 < t2 of (v, I) = a re-entry; m := wt(y) (y's one successor); U_y := the e-vertices more relevant than y.
  rewin    : re-entry with the same split u and the same new successor b at u (rewin_mover / rewin_gate by the kind of u)
  dnfail   : rewin where Om(b) did not rise strictly from t1 to t2-1                                         [0: Lemma REWIN]
  rhfail   : rewin where E_t2(b) cap U_y is not lex-larger than E_t1(b) cap U_y                              [0: Lemma REWIN-HI]
  rwfail   : rewin where E(m) cap U_y takes one value on [t1, t2]                                           [0 on data: CONJECTURE RW-WT]
  wlamfail : Lambda_t1(m) or Lambda_t2(m) differs from w                                                    [0: m is on v's play]
  wcfail   : re-entry (any) where E(m) cap U_y takes one value on [t1, t2]                                  [W-target charge for all re-entries]
  wbfail   : (v, I, y) with c_y > #values of E(m) cap U_y on [first, last y-top]                            [W-target bound]
  dn_nobelow_all : rewin where no vertex of b's play at t2 changes Lambda or its e-letters less relevant than y on [t1, t2-1]
  premono_no : (v, I, y) whose prefix part (letters of U_y before y on v's play at the y-tops) is not lex-nondecreasing
  dnhi/dnlo/dnlam, zbefore/zafter, dn_ywt: where the rise of b sits (top above / below y, Lambda; before / after y; m changed class)
  maxc, maxW (non-rewin re-entries), maxSPL (distinct (u, b)): per (v, I, y), maxima over the genome.
Usage: split199.py G.json ...  (ROOT: repo root, default from this file's place).
Controls (S199_CTRL): 1 Howard direction reversed (hwfail fires); 2 W-target bound with 1 value (wbfail fires); 3 REWIN strict rise on
[t1, t1] (dnfail fires); 4 U_y := empty (rhfail, rwfail, wcfail fire); 5 gate test negated (gtfail fires)."""
import sys, os, json, collections
ROOT = os.environ.get("ROOT") or os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
os.environ.setdefault("EG195_ROOT", ROOT)
sys.path[:0] = [os.path.join(ROOT, p) for p in ("experiments/new/box195", "experiments/new/box191", "experiments/new/box189",
                "experiments/new/box190", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
import eg195, gamma3, n5v, n5x
CTRL = os.environ.get("S199_CTRL", "0")

def run(G, cap=20000):
    g0, _, _, V = gamma3.build(G, eg195.PADS); g = eg195.topg(g0); n = g.n; name = {v: k for k, v in V.items()}
    E, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None)
    evs = [v for v in range(n) if isinstance(name[v], tuple) and name[v][0] == "e"]; ES = sum(E.bit[v] for v in evs)
    H = []                                     # (sigma, values, Odd best reply)
    while len(H) <= cap:
        vs, tb = E.evaluate(tuple(sigma)); H.append((tuple(sigma), vs, tb))
        res = n5v.step(g, E, Ed, sigma, tau, "xi")
        if res is None or res[4]: break
        sigma, tau = res[0], res[1]
    c = collections.Counter()
    def nx(t, x): s, _, tb = H[t]; return s[x] if g.owner[x] == 0 else tb[x]
    def play(t, v):
        P = [v]; seen = {v}
        while True:
            y = nx(t, P[-1])
            if y in seen: return P
            P.append(y); seen.add(y)
    def eset(P, w): return sum(E.bit[z] for z in P if E.bit[z] & ES and E.rank[z] > E.rank[w])
    def top(a, b): return max((f for f in evs if (a ^ b) & E.bit[f]), key=lambda f: E.rank[f])
    K = lambda t, x: E.key(H[t][1][x])
    for t in range(len(H)):
        for v in range(n):
            w = H[t][1][v][0]
            if eset(play(t, v), w) != H[t][1][v][1] & ES: c["playfail"] += 1
    for v in range(n):
        t = 0
        while t < len(H):
            s = t
            while t + 1 < len(H) and H[t + 1][1][v][0] == H[s][1][v][0]: t += 1
            w = H[s][1][v][0]; ytops = collections.defaultdict(list)
            for u_t in range(s + 1, t + 1):
                a, b = H[u_t - 1][1][v][1] & ES, H[u_t][1][v][1] & ES
                if a == b: continue
                c["changes"] += 1; P0, P1 = play(u_t - 1, v), play(u_t, v); i = 0
                while i + 1 < min(len(P0), len(P1)) and P0[i + 1] == P1[i + 1]: i += 1
                u = P1[i]; old, new = P0[i + 1] if i + 1 < len(P0) else None, P1[i + 1] if i + 1 < len(P1) else None
                kind = name[u][0] if isinstance(name[u], tuple) else name[u]
                if old is None or new is None or old == new: c["kindfail"] += 1; continue
                if g.owner[u] == 0:
                    if kind != "x" or H[u_t - 1][0][u] == H[u_t][0][u]: c["kindfail"] += 1
                    ok = K(u_t - 1, new) > K(u_t - 1, old) if CTRL != "1" else K(u_t - 1, new) < K(u_t - 1, old)
                    if not ok: c["hwfail"] += 1
                else:
                    c["oddsplit_" + str(kind)] += 1
                    ok = K(u_t - 1, old) < K(u_t - 1, new) and K(u_t, new) < K(u_t, old)
                    if (not ok) if CTRL != "5" else ok: c["gtfail"] += 1
                if H[u_t - 1][1][u][0] != w or H[u_t][1][u][0] != w or (H[u_t - 1][1][u][1] ^ H[u_t][1][u][1]) & ES != (a ^ b): c["trfail"] += 1
                y = top(a, b)
                if b & E.bit[y]:
                    x, k = name[y][1]
                    if u == V[("x", x)]: cl = "own"
                    elif name[u] == ("g", (x, k)): cl = "gate"
                    elif g.owner[u] == 0: cl = "route"
                    else: cl = "routeO"
                    c["ytop_" + cl] += 1; ytops[y].append((u_t, u, new))
            for y, L in ytops.items():
                hiy = sum(E.bit[f] for f in evs if E.rank[f] > E.rank[y]) if CTRL != "4" else 0; m = g.succ[y][0]
                if L:
                    pre = []
                    for (tq, _, _) in L:
                        P = play(tq, v); P = P[:P.index(y)]; pre.append(sum(E.bit[f] for f in P if E.bit[f] & hiy))
                    keyl = lambda msk: sorted((E.rank[f] for f in evs if msk & E.bit[f]), reverse=True)
                    if any(keyl(a) > keyl(b) for a, b in zip(pre, pre[1:])): c["premono_no"] += 1; c.setdefault("pmex", (v, y))
                    elif len(L) >= 2: c["premono_yes"] += 1
                    t0, tl = L[0][0], L[-1][0]
                    dm = len({H[q][1][m][1] & hiy for q in range(t0, tl + 1)}) if CTRL != "2" else 1
                    if len(L) > dm: c["wbfail"] += 1
                    c["wtight"] += len(L) == dm >= 2
                nw = sum((p1[1], p1[2]) != (p2[1], p2[2]) for p1, p2 in zip(L, L[1:])); c["maxW"] = max(c["maxW"], nw)
                c["maxSPL"] = max(c["maxSPL"], len({(p[1], p[2]) for p in L})); c["maxc"] = max(c["maxc"], len(L))
                for (t1, u1, b1), (t2, u2, b2) in zip(L, L[1:]):
                    c["reentry"] += 1
                    if H[t1][1][m][0] != w or H[t2][1][m][0] != w: c["wlamfail"] += 1
                    hm = {H[q][1][m][1] & hiy for q in range(t1, t2 + 1)}
                    if len(hm) < 2: c["wcfail"] += 1; c.setdefault("wcex", (v, y, t1, t2))
                    else: c["wc_ok"] += 1
                    if (u1, b1) != (u2, b2): continue
                    c["rewin"] += 1
                    if len(hm) < 2: c["rwfail"] += 1
                    kl = lambda msk: sorted((E.rank[f] for f in evs if msk & E.bit[f]), reverse=True)
                    if not kl(H[t2][1][b1][1] & hiy) > kl(H[t1][1][b1][1] & hiy): c["rhfail"] += 1
                    c["rewin_" + ("mover" if g.owner[u1] == 0 else "gate")] += 1
                    lo = sum(E.bit[f] for f in evs if E.rank[f] < E.rank[y])
                    if not any(H[t1][1][q][0] != H[t2 - 1][1][q][0] or (H[t1][1][q][1] ^ H[t2 - 1][1][q][1]) & lo for q in play(t2, b1)):
                        c["dn_nobelow_all"] += 1; c.setdefault("nbex", (v, y, t1, t2, u1, b1))
                    if not (K(t2 - 1, b1) > K(t1, b1) if CTRL != "3" else K(t1, b1) > K(t1, b1)): c["dnfail"] += 1; continue
                    v1, v2 = H[t1][1][b1], H[t2 - 1][1][b1]
                    if v1[0] != v2[0]: c["dnlam"] += 1
                    elif (v1[1] ^ v2[1]) & ES:
                        z = top(v1[1] & ES, v2[1] & ES); c["dnhi" if E.rank[z] > E.rank[y] else "dnlo"] += 1
                        Q = play(t2 - 1, b1)
                        if y in Q and z in Q: c["zbefore" if Q.index(z) < Q.index(y) else "zafter"] += 1
                        else: c["z_" + ("y" if y in Q else "") + ("z" if z in Q else "") + "_offplay"] += 1
                        R2 = play(t2, b1); yi = R2.index(y); wt = R2[yi + 1]
                        cls = lambda q: (H[t1][1][q][0], H[t1][1][q][1] & ES) != (H[t2 - 1][1][q][0], H[t2 - 1][1][q][1] & ES)
                        lo = sum(E.bit[f] for f in evs if E.rank[f] < E.rank[y])
                        if not any(H[t1][1][q][0] != H[t2 - 1][1][q][0] or (H[t1][1][q][1] ^ H[t2 - 1][1][q][1]) & lo for q in R2[:yi + 1]):
                            c["dn_nobelow"] += 1
                        if cls(wt): c["dn_ywt"] += 1
                        elif any(cls(q) for q in R2[:yi + 1]): c["dn_routeonly"] += 1
                        else: c["dn_none"] += 1; c.setdefault("ex", (v, y, t1, t2, u1, b1))
                    else: c["dnnone_e"] += 1
            t += 1
    return len(H) - 1, c

if __name__ == "__main__":
    for fn in sys.argv[1:]:
        G = json.load(open(fn)); G = G.get("genome", G) if isinstance(G, dict) else G
        if not (isinstance(G, dict) and "opts" in G and "start" in G): print(os.path.basename(fn), "skipped"); continue
        T, c = run(G)
        F = ("playfail", "kindfail", "hwfail", "gtfail", "trfail", "dnfail", "rhfail", "rwfail", "wlamfail", "wcfail", "wbfail", "dn_nobelow_all", "premono_no")
        print(os.path.basename(fn), "T3", T, " ".join(f"{k} {c[k]}" for k in F), "|", " ".join(f"{k} {c[k]}" for k in sorted(c) if k not in F and not k.endswith("ex")),
              *[f"{k} {c[k]}" for k in ("wcex", "nbex", "pmex") if k in c], flush=True)
