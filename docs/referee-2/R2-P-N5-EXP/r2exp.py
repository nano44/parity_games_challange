#!/usr/bin/env python3
"""REFEREE-2 successor 41: own checker for the SECOND REVIEW of P-N5-EXP (L-RED-B 5, claude/l-red-b 350d84eb, docs/red-b/P-N5-EXP.md,
sha1 c0449b17…). Own code: the generator below is written from the TABLE of §3 (not from gk.py's code path: one row list, one
resolver); the model is r2unit217.M1P (1P(G) = R104's IDEAL model, R2-key-preread Addendum 3) and r2unit217.ideal_states (R104's
words). Nothing of the lane is imported.

For each k:
  build     G_k from §3's table; N = 9k − 16, M = 2N, levels k + 1                                        size [k]  must 0
  lane      (with --lane DIR holding the lane's G_k.json files) my G_k ≠ the lane's file as a dictionary    lanediff [k]  must 0
  MEMBER    R104's clauses c1-c8 (P-N5-REALIZE §2): levels, GRADED, Ξ-target, β-id / gate / rank bijections onto 0..M − 1, parities,
            start, acyclic                                                                                 member [clause, k]  must 0
            tie [k]: number of pairs of β's with EQUAL (−depth, δ) keys (§3's br rule is not injective on wires: info, item M-1)
  RUN       T = 2^k − 2 (tfail), stop by «stuck» (stopfail), per mover sw = 2^(j−1) in unit j, v_0 once, u_0 and wires never
            (swfail [mover]), total 11·2^(k−2) − 9 (totfail), ID with R104's IDEAL run (idfail)             must 0
  STATIC    at every state of the run and at RAND random states with every wire and u_0 at option 0: V1 (E_j), V2 (EY_j), V3 (EY′_j),
            K1 (C_j), K2 (D_j), K3 (Z_j) as formulas against the model's own value / key comparison (v1..k3 [(state, j)]); V4 and K4:
            the enabling predicates against the model's A_s and key comparison (v4, k4 [(state, mover)]); MOVE-2: a mover moves iff
            value-enabled under s and key-enabled in the step (move2 [(step, mover)])                        must 0
  RESPONSE  the moves of every step predicted by the RESPONSE LEMMA (recursively, from (j, a, t) = (1, 0, 1)) against the run:
            resp [step]: the set of (mover, new option) differs; rest [response]: (H1) fails at its start or REST_j(c) / REST_i(0)
            fails at its end; inp [(response, τ)]: the input of unit j is not (c, c) on its window          must 0
  also      leadsha [k]: sha1 of json.dumps of my RAW-gate G_k ≠ the Lead's sha1 (k = 3, 4, 8, 10; 12:25Z message); depth [option]: a
            Ξ-target's Ξ-depth is not strictly smaller than its source's; rawdiff [k]: the 1P run under the raw gates 100·level + ε
            differs from the run under the ranked gates; tiebreak [k]: the run with the ties of §3's br clause broken the other
            way (decreasing β-id) differs, or (k ≥ 4) that genome has the same br (the tie-break changes nothing)   must 0
Controls (--ctrl NAME): start (ȳ_1's start flipped: tfail must fire), eps (ε of u_1 and v_1 swapped: tfail), rank (δ of y_1's two
options swapped: tfail), sched (the predicted schedule shifted by one step: resp), form (V2's formula negated: v2), mv2 (MOVE-2 without
its key half: move2), stuck (stopfail), mem2 / mem4 / mem5 / mem6 / mem8 (one R104 clause broken each; mem5 = the RAW gate numbering,
which is not onto 0..M − 1: member_c5), and with --lane: start fires lanediff.
--exh (k ≤ 4): the static facts V1-V4, K1-K4 at EVERY state with the wires and u_0 at option 0 (2^9 states at k = 3, 2^16 at k = 4)
instead of the run's and the random states.
--bounds: no run; prints the first k with 2^k − 1 > n^c and > (n + m)^c for c = 2, 3, 4 (n = 135k − 230, n + m = 311k − 530).
Usage: r2exp.py [--lane DIR] [--ctrl NAME] [--rand COUNT] [--dump DIR] [--exh] K...  |  r2exp.py --bounds"""
import sys, os, json, random
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE, os.path.join(HERE, "..", "R2-key"), os.path.join(HERE, "..", "R2-P-N5-END")]
import r2unit217 as U

def rows(k):
    """§3's table: (name, level, (W0, W1), (X0, X1), start, (eps0, eps1), depth, (delta0, delta1)); names as in the packet"""
    E = lambda j: f"e{j}" if j <= k - 2 else f"u{j}"
    R = [("u0", 0, (None, None), (None, None), 0, (2, 5), 0, (2, 0)), ("v0", 0, (None, None), (None, None), 0, (3, 1), 0, (1, 3))]
    for j in range(1, k):
        lo = (f"u{j-1}", f"v{j-1}")
        R.append((f"u{j}", j, lo, (f"yb{j}", f"y{j}"), 0, (2, 3), 2 * j, (1, 0)))
        R.append((f"v{j}", j, lo, (f"y{j}", f"yb{j}"), 0, (4, 5), 2 * j, (3, 2)))
    for j in range(2, k - 1):
        R.append((f"e{j}", j, (f"u{j-1}", f"v{j-1}"), (f"ypb{j}", f"yp{j}"), 0, (0, 1), 2 * j + 1, (4, 5)))
    for j in range(1, k - 1): R.append((f"wv{j}", j + 1, (f"v{j}", f"v{j}"), (None, None), 0, (6, 7), "wire", (1, 0)))
    for j in range(2, k - 1): R.append((f"wu{j}", j + 1, (f"u{j}", f"u{j}"), (None, None), 0, (8, 9), "wire", (3, 2)))
    for j in range(1, k):
        lo = (f"u{j-1}", f"v{j-1}")
        if j <= k - 2: lv, W, e0 = j + 2, (f"wv{j}", E(j + 1)), 10
        else: lv, W, e0 = k, (f"u{j}", f"v{j}"), 20
        R.append((f"y{j}", lv, W, (lo[0], lo[1]), 0, (e0, e0 + 1), 2 * j - 1, (1, 3)))
        R.append((f"yb{j}", lv, W, (lo[1], lo[0]), 1, (e0 + 2, e0 + 3), 2 * j - 1, (0, 2)))
    for j in range(2, k - 1):
        W = (f"wu{j}", E(j + 1))
        R.append((f"yp{j}", j + 2, W, (f"yb{j}", f"y{j}"), 0, (14, 15), 2 * j, (5, 7)))
        R.append((f"ypb{j}", j + 2, W, (f"y{j}", f"yb{j}"), 1, (16, 17), 2 * j, (4, 6)))
    return R

def build(k, ctrl="", raw=False, tb=1):
    R = rows(k); names = [r[0] for r in R]; ix = {n: i for i, n in enumerate(names)}; N = len(R); M = 2 * N
    if ctrl == "eps":
        R = [(r[0], r[1], r[2], r[3], r[4], {"u1": (4, 5), "v1": (2, 3)}.get(r[0], r[5]), r[6], r[7]) for r in R]
    if ctrl == "rank":
        R = [(r[0], r[1], r[2], r[3], r[4], r[5], r[6], (3, 1) if r[0] == "y1" else r[7]) for r in R]
    if ctrl == "start":
        R = [(r[0], r[1], r[2], r[3], 0 if r[0] == "yb1" else r[4], r[5], r[6], r[7]) for r in R]
    gkey = {}; bkey = {}
    for i, (n, lv, W, X, st, ep, dep, dl) in enumerate(R):
        for o in range(2):
            gkey[(i, o)] = 100 * lv + ep[o]
            bkey[(i, o)] = (-(2 * k + 5 if dep == "wire" else dep), dl[o])
    assert len(set(gkey.values())) == M, "gate keys not injective"
    gs = sorted(gkey.values()); grank = {g: r for r, g in enumerate(gs)}
    # br: rank of (−depth, δ); §3 names no tie-break; ties (wires only) are broken by β-id, as gk.py does
    order = sorted(bkey, key=lambda io: (bkey[io], tb * (2 * io[0] + io[1])))
    brank = {io: r for r, io in enumerate(order)}
    ties = M - len(set(bkey.values()))
    G = dict(N=N, lev=[r[1] for r in R], deg=2,
             opts=[[[ix[r[2][o]] if r[2][o] else -1, ix[r[3][o]] if r[3][o] else -1, 2 * i + o] for o in range(2)] for i, r in enumerate(R)],
             gate=[[gkey[(i, o)] if raw else grank[gkey[(i, o)]] for o in range(2)] for i in range(N)],
             br=[brank[(b // 2, b % 2)] for b in range(M)], bp=[0] * M, start=[r[4] for r in R])
    if ctrl == "mem2": G["opts"][ix["y1"]][0][0] = ix["u1"]                 # y_1 (level 3) gets a level-1 W-target
    if ctrl == "mem4": G["opts"][1][0][2] = 0                              # β-id 0 twice
    if ctrl == "mem6": G["br"] = [min(r, M - 2) for r in G["br"]]          # two β's share a rank
    if ctrl == "mem8": G["opts"][ix["u0"]][0][1] = ix["u1"]                # Ξ-cycle u_0 → u_1 → ȳ_1 → v_0 / u_0
    return G, names, ix, ties

def sha(G):
    import hashlib
    return hashlib.sha1(json.dumps(G).encode()).hexdigest()

LEADRAW = {3: "cd3cd7e361dfe16482bbe56eb87d3e3decf9e6af", 4: "7a2218bfa94e37f85b3fc60d874030aeba8ca848",
           8: "d3ad8e2e6f202eb17e66d04dad77de1a33e74eb2", 10: "da29d33ecaf20cb777650729e54acb1dad17cfd9"}

def member(G, k, C):
    N, M = G["N"], 2 * G["N"]; lev = G["lev"]; opts = G["opts"]
    if N != 9 * k - 16 or max(lev) != k or set(lev) != set(range(k + 1)) or any(len(o) != 2 for o in opts): C["member_c1"] += 1
    for x in range(N):
        for (wt, xt, b) in opts[x]:
            if (lev[x] == 0 and wt != -1) or (lev[x] > 0 and not (0 <= wt < N and lev[wt] == lev[x] - 1)): C["member_c2"] += 1
            if not (xt == -1 or 0 <= xt < N): C["member_c3"] += 1
    if sorted(b for o in opts for (_, _, b) in o) != list(range(M)): C["member_c4"] += 1
    if sorted(g for r in G["gate"] for g in r) != list(range(M)): C["member_c5"] += 1
    if sorted(G["br"]) != list(range(M)) or any(p not in (0, 1) for p in G["bp"]): C["member_c6"] += 1
    if len(G["start"]) != N or any(s not in (0, 1) for s in G["start"]): C["member_c7"] += 1
    col = {}
    def dfs(x):
        col[x] = 1
        for (_, y, _) in opts[x]:
            if y >= 0 and (col.get(y) == 1 or (y not in col and not dfs(y))): return False
        col[x] = 2; return True
    if not all(x in col or dfs(x) for x in range(N)): C["member_c8"] += 1

def schedule(k, ix):
    """the RESPONSE LEMMA's move list: dict step -> set of (mover, new option); and the list of responses (j, a, t, last)"""
    P = {k - 1: 3}
    for j in range(k - 2, 0, -1): P[j] = 2 * P[j + 1] + 1
    mv = defaultdict(set); resp = []
    E = lambda j: f"e{j}" if j <= k - 2 else f"u{j}"
    def R(j, a, t):
        c = 1 - a
        F, B = (f"yb{j}", f"y{j}") if a == 0 else (f"y{j}", f"yb{j}")
        if j == k - 1:
            mv[t].add((ix[f"v{j}"], c)); mv[t + 1].add((ix[B], 1)); mv[t + 2].add((ix[f"u{j}"], c)); mv[t + 2].add((ix[F], 0))
            resp.append((j, a, t, t + 2)); return
        mv[t].add((ix[f"v{j}"], c)); R(j + 1, 0, t); mv[t + 1].add((ix[F], 0))
        t1 = t + P[j + 1] - 1; mv[t1].add((ix[B], 1))
        mv[t1 + 1].add((ix[f"u{j}"], c)); R(j + 1, 1, t1 + 1)
        t2 = t1 + P[j + 1]
        if j >= 2:
            Fp, Bp = (f"ypb{j}", f"yp{j}") if a == 0 else (f"yp{j}", f"ypb{j}")
            mv[t1 + 1].add((ix[Fp], 0)); mv[t2].add((ix[Bp], 1)); mv[t2 + 1].add((ix[f"e{j}"], c)); resp.append((j, a, t, t2 + 1))
        else: resp.append((j, a, t, t2))
    R(1, 0, 1); mv[1].add((ix["v0"], 1))
    return mv, resp, P

def check(k, C, ctrl, rand, lane, dump, exh=False):
    G, names, ix, ties = build(k, ctrl if ctrl in ("eps", "rank", "start", "mem2", "mem4", "mem6", "mem8") else "")
    Graw = build(k, ctrl if ctrl in ("eps", "rank", "start") else "", raw=True)[0]
    if ctrl == "mem5": G = Graw                                            # the raw gate numbering is not onto 0..M − 1
    C["k_done"] += 1; N = G["N"]; M = 2 * N; info = {}
    if N != 9 * k - 16 or M != 18 * k - 32 or max(G["lev"]) + 1 != k + 1: C["size"] += 1
    if lane:
        f = os.path.join(lane, f"G_{k}.json")
        if os.path.exists(f):
            C["lane_files"] += 1
            if json.load(open(f)) != G: C["lanediff"] += 1
        f = os.path.join(lane, "..", "raw", f"G_{k}.json")
        if os.path.exists(f):
            C["lane_raw_files"] += 1
            if json.load(open(f)) != Graw: C["lanediff"] += 1
    if k in LEADRAW:
        C["lead_sha"] += 1
        if sha(Graw) != LEADRAW[k]: C["leadsha"] += 1
    if dump: os.makedirs(dump, exist_ok=True); json.dump(G, open(os.path.join(dump, f"r2_G_{k}.json"), "w"))
    member(G, k, C); info["ties"] = ties
    if ctrl.startswith("mem"): return dict(T=-1, maxsw=-1, total=-1, ties=ties)
    # depth-major ranks: every Ξ-target has a strictly smaller Ξ-depth than its source (so a higher rank block)
    dep = {r[0]: (2 * k + 5 if r[6] == "wire" else r[6]) for r in rows(k)}
    for r in rows(k):
        for xt in r[3]:
            if xt is not None and not dep[xt] < dep[r[0]]: C["depth"] += 1
    m = U.M1P(G); S = m.run(cap=10 ** 7); T = len(S) - 1
    if U.M1P(Graw).run(cap=10 ** 7) != S: C["rawdiff"] += 1                # the run does not see the gate renumbering
    Gtb = build(k, tb=-1)[0]                                               # the other tie-break of §3's br clause (ties by decreasing β-id)
    if k >= 4 and Gtb["br"] == G["br"]: C["tiebreak"] += 1
    if not ctrl and U.M1P(Gtb).run(cap=10 ** 7) != S: C["tiebreak"] += 1
    sw = [sum(S[t + 1][x] != S[t][x] for t in range(T)) for x in range(N)]
    if T != 2 ** k - 2: C["tfail"] += 1
    _, Xf = m.vals(S[-1]); A = m.avail(S[-1], Xf)
    if all(len(a) == 1 for a in A) or ctrl == "stuck": C["stopfail"] += 1            # «stuck» needs a non-singleton availability set at the last state
    unit = {}
    for n in names:
        if n[0] in "uve" and n not in ("u0", "v0"): unit[n] = int(n[1:])
        elif n.startswith("ypb"): unit[n] = int(n[3:])
        elif n.startswith("yp") or n.startswith("yb"): unit[n] = int(n[2:])
        elif n.startswith("y"): unit[n] = int(n[1:])
    for n in names:
        want = 2 ** (unit[n] - 1) if n in unit else (1 if n == "v0" else 0)
        if sw[ix[n]] != want: C["swfail"] += 1
    if sum(sw) != 11 * 2 ** (k - 2) - 9: C["totfail"] += 1
    if k <= 12 and U.ideal_states(G) != S: C["idfail"] += 1
    info.update(T=T, maxsw=max(sw), total=sum(sw))
    # ---- static facts
    mover = lambda n: ix[n]
    def facts(s):
        V, X = m.vals(s); mu, key = m.keys(s)
        cmpv = lambda p, q: X[(p, s[p])] > X[(q, s[q])]            # p value-ahead of q (movers, current options)
        cmpk = lambda p, q: mu[p] < mu[q]                           # p key-ahead of q
        Ef = {0: s[mover("v0")]}; Cf = {0: s[mover("v0")]}; EY = {}; EYp = {}
        for j in range(1, k):
            u, v, y, yb = mover(f"u{j}"), mover(f"v{j}"), mover(f"y{j}"), mover(f"yb{j}")
            EY[j] = s[yb] if s[y] != s[yb] else int(s[y] != Ef[j - 1])
            if ctrl == "form": EY[j] = 1 - EY[j]
            Ef[j] = 1 if s[u] != s[v] else int(EY[j] == s[v])
            Cf[j] = int(s[v] == Cf[j - 1]) if s[u] != s[v] else 0
            C["v2"] += EY[j] != int(cmpv(yb, y)); C["v1"] += Ef[j] != int(cmpv(v, u)); C["k1"] += Cf[j] != int(cmpk(v, u))
            if 2 <= j <= k - 2:
                yp, ypb = mover(f"yp{j}"), mover(f"ypb{j}")
                EYp[j] = s[ypb] if s[yp] != s[ypb] else int(1 - s[yp] != EY[j])
                C["v3"] += EYp[j] != int(cmpv(ypb, yp))
        C["v1"] += Ef[0] != int(cmpv(mover("v0"), mover("u0"))); C["k1"] += Cf[0] != int(cmpk(mover("v0"), mover("u0")))
        Ej = lambda j: mover(f"e{j}") if j <= k - 2 else mover(f"u{j}")
        D = {}; Z = {}
        for j in range(1, k - 1):
            D[j] = int(s[Ej(j + 1)] == 1 or Cf[j] == 0); C["k2"] += D[j] != int(cmpk(Ej(j + 1), mover(f"wv{j}")))
            if j >= 2: Z[j] = int(s[Ej(j + 1)] == 0 or Cf[j] == 1); C["k3"] += Z[j] != int(cmpk(Ej(j + 1), mover(f"wu{j}")))
        # V4 / K4 as predicates, against the model
        ven = {}; ken = {}
        for j in range(1, k):
            for n, pred in ((f"v{j}", EY[j] == 1 - s[mover(f"v{j}")]), (f"u{j}", EY[j] == s[mover(f"u{j}")])):
                ven[n] = pred; ken[n] = s[mover(n)] != Cf[j - 1]
            y, yb = f"y{j}", f"yb{j}"
            ven[y] = (Ef[j - 1] == 1) if s[mover(y)] == 0 else (Ef[j - 1] == 0)
            ven[yb] = (Ef[j - 1] == 0) if s[mover(yb)] == 0 else (Ef[j - 1] == 1)
            kb = (D[j] == 1) if j <= k - 2 else (Cf[k - 1] == 1)
            for n in (y, yb): ken[n] = kb if s[mover(n)] == 0 else not kb
            if 2 <= j <= k - 2:
                e, yp, ypb = f"e{j}", f"yp{j}", f"ypb{j}"
                ven[e] = EYp[j] == s[mover(e)]; ken[e] = s[mover(e)] != Cf[j - 1]
                ven[yp] = (EY[j] == 0) if s[mover(yp)] == 0 else (EY[j] == 1)
                ven[ypb] = (EY[j] == 1) if s[mover(ypb)] == 0 else (EY[j] == 0)
                for n in (yp, ypb): ken[n] = (Z[j] == 1) if s[mover(n)] == 0 else (Z[j] == 0)
        ven["u0"] = False; ven["v0"] = s[mover("v0")] == 0
        ken["u0"] = False; ken["v0"] = s[mover("v0")] == 0
        for n in ven:
            x = mover(n); o = s[x]
            C["v4"] += ven[n] != (X[(x, 1 - o)] > X[(x, o)])
            C["k4"] += ken[n] != (key[(x, 1 - o)] < key[(x, o)])
        return ven, ken
    rng = random.Random(1000 + k); wires = [mover(n) for n in names if n[0] == "w"]
    states = list(S[:400]) + list(S[-200:]) if T > 600 else list(S)
    for _ in range(rand):
        s = [rng.randrange(2) for _ in range(N)]
        for w in wires: s[w] = 0
        s[mover("u0")] = 0; states.append(tuple(s))
    if exh and k <= 4:                                                    # EVERY state with the wires and u_0 at option 0
        free = [x for x in range(N) if x not in wires and x != mover("u0")]; states = []
        for bits in range(2 ** len(free)):
            s = [0] * N
            for i, x in enumerate(free): s[x] = (bits >> i) & 1
            states.append(tuple(s))
        C["exh_states"] += len(states)
    for s in states: facts(s)
    C["static_states"] += len(states)
    # MOVE-2 along the run: a mover moves iff value-enabled under s and key-enabled in the step (model's own A_s and keys of s')
    for t in range(min(T, 600)):
        _, X = m.vals(S[t]); _, key2 = m.keys(S[t + 1])
        for x in range(N):
            o = S[t][x]; ve = X[(x, 1 - o)] > X[(x, o)]; ke = key2[(x, 1 - o)] < key2[(x, o)]
            if ctrl == "mv2": ke = True
            C["move2"] += (S[t + 1][x] != o) != (ve and ke)
    # ---- RESPONSE LEMMA
    mv, resp, P = schedule(k, ix); sh = 1 if ctrl == "sched" else 0
    for t in range(1, T + 1):
        act = {(x, S[t][x]) for x in range(N) if S[t][x] != S[t - 1][x]}
        if act != mv.get(t + sh, set()): C["resp"] += 1
    if max(mv) != T + 0: C["resp"] += 1
    def rest(s, j, a):
        ok = s[mover(f"u{j}")] == a and s[mover(f"v{j}")] == a and (s[mover(f"y{j}")], s[mover(f"yb{j}")]) == (a, 1 - a)
        if 2 <= j <= k - 2:
            ok = ok and s[mover(f"e{j}")] == a and (s[mover(f"yp{j}")], s[mover(f"ypb{j}")]) == (a, 1 - a)
        return ok
    def inp(s, j):
        mu, _ = m.keys(s); _, X = m.vals(s); u, v = mover(f"u{j-1}"), mover(f"v{j-1}")
        return (int(mu[v] < mu[u]), int(X[(v, s[v])] > X[(u, s[u])]))
    lim = 4000
    for (j, a, t, last) in resp[:lim] + resp[-lim:] if len(resp) > 2 * lim else resp:
        if t - 1 > T or last > T: C["rest"] += 1; continue
        c = 1 - a; C["resp_units"] += 1
        if not (rest(S[t - 1], j, a) and all(rest(S[t - 1], i, 0) for i in range(j + 1, k)) and inp(S[t - 1], j) == (a, a)): C["rest"] += 1
        if not (rest(S[last], j, c) and all(rest(S[last], i, 0) for i in range(j + 1, k))): C["rest"] += 1
        for tau in range(t, min(last, t + 64) + 1):
            if inp(S[tau], j) != (c, c): C["inp"] += 1
    return info

MUST0 = ["size", "lanediff", "leadsha", "depth", "rawdiff", "tiebreak", "member_c1", "member_c2", "member_c3", "member_c4", "member_c5", "member_c6", "member_c7", "member_c8",
         "tfail", "stopfail", "swfail", "totfail", "idfail", "v1", "v2", "v3", "v4", "k1", "k2", "k3", "k4", "move2", "resp", "rest", "inp"]

def main(a):
    lane = None; ctrl = ""; rand = 200; dump = None; ks = []; i = 0; exh = "--exh" in a; a = [x for x in a if x != "--exh"]
    while i < len(a):
        if a[i] == "--lane": lane = a[i + 1]; i += 2
        elif a[i] == "--ctrl": ctrl = a[i + 1]; i += 2
        elif a[i] == "--rand": rand = int(a[i + 1]); i += 2
        elif a[i] == "--dump": dump = a[i + 1]; i += 2
        elif a[i] == "--bounds": i += 1
        else: ks.append(int(a[i])); i += 1
    if "--bounds" in a:                                                   # exact integers; the first k and that the bound then stays
        for c in (2, 3, 4):
            for name, f in (("n", lambda k: 135 * k - 230), ("n+m", lambda k: 311 * k - 530)):
                k = 3
                while not 2 ** k - 1 > f(k) ** c: k += 1
                stays = int(all(2 ** j - 1 > f(j) ** c for j in range(k, k + 1000)))
                print(f"first k with 2^k - 1 > ({name})^{c}: k {k} size {f(k)} iterations_bound {2 ** k - 1} poly {f(k) ** c} holds_for_the_next_1000_k {stays}")
        return
    C = defaultdict(int)
    for k in ks:
        before = dict(C); info = check(k, C, ctrl, rand, lane, dump, exh)
        print(f"k {k} N {9 * k - 16} T {info['T']} (2^k − 2 = {2 ** k - 2}) maxsw {info['maxsw']} total {info['total']} br-key ties {info['ties']} | "
              + " ".join(f"{c} {C[c] - before.get(c, 0)}" for c in MUST0 if C[c] - before.get(c, 0)) , flush=True)
    print(f"TOTAL ctrl {ctrl or '-'}: " + " ".join(f"{c} {C[c]}" for c in MUST0))
    print(f"INFO k_done {C['k_done']} lane_files {C['lane_files']} lane_raw_files {C['lane_raw_files']} lead_sha1s {C['lead_sha']} exhaustive_states {C['exh_states']} static_states {C['static_states']} responses {C['resp_units']}")
    print("FIRED " + (" ".join(c for c in MUST0 if C[c]) or "none"))

if __name__ == "__main__":
    main(sys.argv[1:])
