"""REFEREE successor 29: box 196 (P-N5-CHAIN, not yet frozen) DATA replay with the referee's own code only.
HOW3(G) = Howard model on Gamma3(G): my builder xicyc_replay.build(G, pad=True) freezes every non-mover Even vertex at the standard
state's choice (beta -> xt or pb, K0 -> pA, K1 -> s, K3 -> K2, pads forced); Odd unrestricted (xicyc_vj best_reply); Howard steps at
the movers from the stored start (= S3's mover choice); MY tie rule (keep if best, else the largest index), ties counted.
Counters per state t (Omega_t = values under sigma_t and sigma-bar_t; classes (Lambda, e-part of Pi)):
  cnlow    (state, v != cX) pairs whose cycle node has priority < 3, or a mover / gate / pad in Pi_t(v)       [CN2-3]
  gst/ties/locfail  (state, gate) pairs / Omega(pe) == Omega(pbeta) / sigma-bar not the strictly smaller face  [NO-TIE3, LOC-GATE3]
  k2fail   states with sigma-bar(K2) != r or not Omega(r) < Omega(K2)                                            [LOC-K2-3]
  bfail    (state, v) pairs, v not cW, not a level-0 e, not the pe in front of one, Lambda at least as relevant as the least e [B-ONLY3]
  Q, W, wfail (W > L3), Tfail (T > Q + (Q+1) L3), tqfail (T > (1 + sum_v (DEtot(v) - 1))(L3 + 1)), crossflip    [QUIET3, T-QUIET3]
  emon     (step, v) pairs with equal Lambda whose e-set falls (top differing e in the earlier set)            [E-MON3]
  cdfail   CHAIN-DECOMP3 violations; ujfail UP-JUMP3 violations; upfail (state, v) with ascents > U(G)          [§4]
  lamvals  max over v of the number of distinct Lambda_t(v) vs 2M + 3                                              [HUB-ASC-G3 count]
REACH3-ALL (my N5'-xi engine end_replay, mode xi, my S4a tie choice): on every pre-fallback iteration: nonstd = states with a non-mover
Even vertex off the standard choice or tau != tau0; nohoward = (iteration, mover) pairs where the move is not a Howard step under Xi_sigma
(a mover with a strictly better successor that does not move to a best one, or a mover that moves without a strictly better one);
fbpos = runs whose first fallback is not at iteration T3 + 1 (T3 = first state with no strictly improvable mover).
Controls: CTRL=1 (L3 := 0, U := -1), CTRL=2 (LOC-GATE3 with the order reversed).
Usage: chain_replay.py gen FAMILY SEED COUNT | files G.json ..."""
import sys, os, json, random, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xicyc_replay import howard
import end_replay as er
CTRL = os.environ.get("CTRL")

def how3(G):
    E, lab, ties, states, movers, idx = howard(G, True)
    inv = {v: k for k, v in idx.items()}; n = E.n; N = G["N"]; lev = G["lev"]
    O = [(x, k) for x in range(N) for k in range(len(G["opts"][x]))]; M = len(O)
    evs = {idx[("e", q)] for q in O}; cW, cX = idx["cW"], idx["cX"]; K1, K2 = idx[("K", 1)], idx[("K", 2)]; r_ = idx["r"]
    gates = [(idx[("g", q)], idx[("pe", q)], idx[("pbeta", q)], idx[("e", q)]) for q in O]
    low = set(movers) | {g for g, _, _, _ in gates} | {v for v, k in inv.items() if (isinstance(k, tuple) and k[0] in ("pe", "pbeta", "pb", "m")) or k in ("pA", "s", "q", "r")}
    lvl0 = {idx[("e", q)] for q in O if G["opts"][q[0]][q[1]][0] < 0}
    excl = {cW} | lvl0 | {idx[("pe", q)] for q in O if G["opts"][q[0]][q[1]][0] < 0}
    leaste = min(E.rk[e] for e in evs)
    U = -1 if CTRL == "1" else sum(1 for x in range(N) for o in G["opts"][x] if o[1] >= 0 and lev[o[1]] > lev[x])
    L3 = 0 if CTRL == "1" else (M + 1) * (2 * M + 1) * (N + 1) + N * (n - 1)
    C = collections.Counter(); C["T"] = len(lab); C["howties"] = ties
    def play(st, v):
        seen = []; s = set()
        while v not in s: s.add(v); seen.append(v); v = st[v]
        return seen
    hist = []; prevE = None; lam = collections.defaultdict(set); DE = collections.defaultdict(set)
    for t, (s, st, val) in enumerate(states):
        Et = {}
        for v in range(n):
            L, P, k = val[v]
            if v != cX: C["cnlow"] += E.prio[L] < 3 or bool(P & low)
            if v not in excl: C["bpairs"] += 1; C["bfail"] += E.rk[L] >= leaste
            pl = play(st, v); seq = [u for u in pl if u in evs and u in P]; Et[v] = (L, frozenset(seq))
            lam[v].add(L); DE[v].add((L, frozenset(seq)))
            a = [i for i in range(len(seq) - 1) if E.rk[seq[i + 1]] > E.rk[seq[i]]]
            C["upfail"] += len(a) > U; C["maxasc"] = max(C["maxasc"], len(a))
            if seq:
                f = seq[0]; y = st[f]
                C["cdfail"] += not (y in movers and val[y][0] == L and set(seq) == {f} | {u for u in play(st, y) if u in evs and u in val[y][1]})
            for i in a:
                ia, ib = pl.index(seq[i]), pl.index(seq[i + 1]); x0 = inv[seq[i]][1][0]; hit = False
                for p in range(ia, ib):
                    ku = inv.get(pl[p])
                    if isinstance(ku, tuple) and ku[0] == "b" and p + 1 < len(pl) and pl[p + 1] in movers:
                        if lev[movers.index(pl[p + 1])] > lev[ku[1][0]] and lev[movers.index(pl[p + 1])] >= lev[x0]: hit = True
                C["ujfail"] += not hit
        for g, pe, pb, e in gates:
            C["gst"] += 1; c = E.cmp(val[pe], val[pb])
            if CTRL == "2": c = -c
            if c == 0: C["ties"] += 1
            elif st[g] != (pe if c < 0 else pb): C["locfail"] += 1
        C["k2fail"] += not (st[K2] == r_ and E.cmp(val[r_], val[K2]) < 0)
        if prevE is not None:
            for v in range(n):
                if prevE[v][0] == Et[v][0]:
                    d = prevE[v][1] ^ Et[v][1]
                    C["emon"] += bool(d) and max(d, key=lambda u: E.rk[u]) not in Et[v][1]
        prevE = Et
        hist.append(([Et[v] for v in range(n)], [st[g] for g, _, _, _ in gates]))
    Q = W = cur = 0
    for t in range(1, len(hist)):
        (c0, g0), (c1, g1) = hist[t - 1], hist[t]
        if c0 != c1: Q += 1; cur = 0
        else:
            cur += 1; W = max(W, cur)
            if cur == L3 + 1: C["wfail"] += 1
            for i, (g, pe, pb, e) in enumerate(gates):
                if g0[i] != g1[i] and c1[pe] != c1[pb]: C["crossflip"] += 1
    T = C["T"]; sDE = sum(len(DE[v]) - 1 for v in range(n))
    C["Tfail"] += T > Q + (Q + 1) * L3; C["tqfail"] += T > (1 + sDE) * (L3 + 1)
    C["lamfail"] += max(len(lam[v]) for v in range(n)) > 2 * M + 3
    C["Q"] = Q; C["W"] = W; C["maxDEtot"] = max(len(DE[v]) for v in range(n)); C["U"] = U
    return C, T

def reach(G):
    C = collections.Counter(); info = {"pre": [], "fb": None}
    def hook(sig, tau, val, Is, sn, tn, fb, idx, movers, succ, g):
        if info["fb"] is not None: return
        n = len(sig); own = g.own
        _, _, _, sig0, _, _, _ = er.build(G, True)
        std = all(sig[v] == sig0[v] for v in range(n) if own[v] == 0 and v not in movers and len(succ[v]) > 1)
        improv = [x for x in movers if any(g.E.cmp(val[w], val[sig[x]]) > 0 for w in succ[x])]
        info["pre"].append((std, bool(improv)))
        if fb: info["fb"] = len(info["pre"]); return
        for x in movers:
            best = [w for w in succ[x] if all(g.E.cmp(val[w], val[u]) >= 0 for u in succ[x])]
            if x in improv: C["nohoward"] += sn[x] not in best
            else: C["nohoward"] += sn[x] != sig[x]
    c, i = er.run(G, "xi", hook=hook)
    C.update({k: c[k] for k in ("e0fail", "nfb")})
    C["nonstd"] += sum(not s for s, _ in info["pre"])
    T3 = next((t for t, (_, imp) in enumerate(info["pre"]) if not imp), None)
    C["fbpos"] += info["fb"] is None or T3 is None or info["fb"] != T3 + 1
    return C, (T3 if T3 is not None else -1)

def main():
    if sys.argv[1] == "gen":
        fam, seed, cnt = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]); rng = random.Random(seed)
        gl = [(f"{fam}{seed}#{i}", er.gen(rng, fam)) for i in range(cnt)]
    else:
        gl = [(os.path.basename(f), json.load(open(f))) for f in sys.argv[2:]]
        gl = [(a, b) for a, b in gl if isinstance(b, dict) and "N" in b]
    tot = collections.Counter(); mx = collections.Counter(); tdiff = 0; cyc = 0
    for name, G in gl:
        C, T = how3(G); R, T3 = reach(G); tot.update(C); tot.update(R); cyc += not er.acyclic(G)
        for k in ("T", "W", "maxasc", "maxDEtot"): mx[k] = max(mx[k], C[k])
        tdiff += T3 != T
        if sys.argv[1] == "files": print(" ", name, "T", T, "T3(xi)", T3, "Q", C["Q"], "W", C["W"], "U", C["U"], "maxasc", C["maxasc"])
    keys = ["cnlow", "ties", "locfail", "k2fail", "bfail", "wfail", "Tfail", "tqfail", "crossflip", "emon", "cdfail", "ujfail", "upfail",
            "lamfail", "nonstd", "nohoward", "fbpos", "e0fail", "nfb"]
    print(f"{'ctrl' + CTRL + ' ' if CTRL else ''}{' '.join(sys.argv[1:5]) if sys.argv[1] == 'gen' else 'files ' + str(len(gl))}: runs {len(gl)} (Xi-cyclic {cyc}) |",
          " ".join(f"{k} {tot[k]}" for k in keys), f"| units: states {tot['T'] + len(gl)}, gate-states {tot['gst']}, bpairs {tot['bpairs']}",
          f"| howties {tot['howties']} | T3(xi) != T(HOW3, my ties) {tdiff} | max {dict(mx)}")

if __name__ == "__main__":
    main()
