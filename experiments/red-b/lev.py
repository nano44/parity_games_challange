#!/usr/bin/env python3
"""L-RED-B's own counters for box 208 (claude/l-new 8db300fe, docs/new/N5-LEVEL-box208.md), on eng.py's run.
Every counter is a must-0 counter for one sentence of the box; the unit is given with each. Written from the box's
statements, not from the lane's tool.

Premise counters (landed RESULTS, re-tested here):
  f1      (vertex, step): Omega_t(v) > Omega_(t+1)(v)                                   [R118 (b) F1]
  cn2     (vertex, state): cycle node of priority < 2                                   [R123 CN2]
  bonly   (vertex, state): Lambda not less relevant than every e (v not c_W, not an e -> c_W)   [R123 B-ONLY]
  notie   (gate, state): Omega(e_g) = Omega(beta_g)                                     [R123 NO-TIE]
  locgate (gate, state): the chosen face is not the strictly smaller one                [R123 LOC-GATE]
  lock2   (state): sbar(K2) != K1                                                       [R123 LOC-K2]
  howard  (mover, step): the new successor is not a best one under Omega_t, or a best current one was left
Class facts of box 208 par. 2:
  k1 (vertex, step) class falls; k2 (pair of non-core vertices, state; sampled: all faces/gates pairs) Omega <= Omega'
  but class > class'; k3 (vertex, state) (a), (c), (d), (e); k4 (gate, state); k5 (mover, gate, step).
Lemma LEVEL (par. 3), for each reference b used:
  l1 (step t < b with LAG_t nonempty): LAG grows, or stall with Phi changed / FRONT changed / LAG_(t+1) empty,
     or non-stall with LAG_(t+1) nonempty and Phi not strictly larger
  l2 (vertex of FRONT_t, state): not a mover, gate, or beta with a mover successor
  l3 (state): neither (alpha) nor (beta) as stated
  l4map (vertex of FRONT_t, stall): the map s of the proof leaves FRONT_t, or a gate of FRONT_t is on its e-face
  l4cyc (stall): no cycle x_1 -> ... -> x_r of Xi_(sigma_b) with x_i, their b-gates and beta-faces in FRONT_t, sbar_t = beta
  l5 (reference): more than 2M values of m, or more than P values of Phi, or (no case beta) more than M(N+2M)
Counting (par. 4): c4 (reference): a class changes after LAG is empty, or more than N steps after b'.
Lemma PLATEAU (Addendum A), for each maximal interval [u, v] of constant Phi with u < v:
  p1 (vertex, state): Y changes or a class changes on Y;  p2 (vertex of Y, state): play successor outside Y
  p3 (mover of Y, gate, state): class(gate) > class(mover) or gate outside Y
  p4 (Odd vertex of Y, step inside): sbar changes, or the chosen face is outside Y
  p6 (step s -> s+1, u <= s <= v): no mover of Y switches
  p7 (plateau): v - u > number of Even vertices in Y;   plat (plateau): v - u > N + 2M + 5
Theorem ALL-TCYC: tbound (run): T_CYC > P (N + 2M + 6) + N.
Descriptive: T, phivals, mvals, stalls, stallloud, plateaus, platmax, platY (movers in Y at the longest plateau),
  alpha / beta case counts.
"""
import sys

def classes(g, st):
    rew = g.rew; em = g.emask; lam = st["lam"]; pim = st["pim"]
    return [(rew[lam[v]], pim[v] & em) for v in range(g.n)]

def nxt_of(g, st):
    n = g.n; nx = [0] * n
    for v in range(n):
        if g.owner[v] == 1: nx[v] = st["sbar"][v]
        elif v < g.N: nx[v] = g.succ[v][st["sig"][v]]
        else: nx[v] = g.succ[v][0]
    return nx

CNT = ["f1", "cn2", "bonly", "notie", "locgate", "lock2", "howard", "k1", "k2", "k3", "k4", "k5",
       "l1", "l2", "l3", "l4map", "l4cyc", "l5", "c4", "p1", "p2", "p3", "p4", "p6", "p7", "plat", "tbound"]

def check_run(g, hist, refs="T", ctrl=0, want_detail=False):
    """refs: "T" (reference b = last state) or "all" (every state b >= 1 as reference).
    ctrl: 0 none; 1 FRONT := the HIGHEST lagging class (control for l1-l4); 2 Y := FRONT alone (control for p2/p7)."""
    N, M, n = g.N, g.M, g.n
    T = len(hist) - 1
    c = {k: 0 for k in CNT}
    d = {"T": T, "phivals": 0, "mvals": 0, "stalls": 0, "stallloud": 0, "plateaus": 0, "platmax": 0, "platY": 0,
         "alpha": 0, "beta": 0, "nonstall": 0, "platmaxE": 0,
         # coverage (reference T only, except ties): how often the cases of the proofs occur
         "cov_tie": 0, "cov_bothY": 0, "cov_bothYeq": 0, "cov_frontg": 0, "cov_frontb": 0, "cov_flipinplat": 0,
         "cov_efaceY": 0, "platsharp": 0}
    cls = [classes(g, st) for st in hist]
    nx = [nxt_of(g, st) for st in hist]
    kind = g.kind; K0, K1, K2, K3 = g.K; core = set(g.K)
    gates = [v for v in range(n) if kind[v] == "g"]
    evs = [v for v in range(n) if kind[v] == "e"]
    betas = [v for v in range(n) if kind[v] == "b"]
    emin = min((g.rank[e] for e in evs), default=None)
    face_e = {gv: g.succ[gv][0] for gv in gates}; face_b = {gv: g.succ[gv][1] for gv in gates}
    # ---- premises and class facts, state by state
    for t, st in enumerate(hist):
        val, lam, pim = st["val"], st["lam"], st["pim"]; cl = cls[t]; nxt = nx[t]
        if st["sbar"][K2] != K1: c["lock2"] += 1
        for v in range(n):
            L = lam[v]
            if g.prio[L] < 2: c["cn2"] += 1
            if v != g.cW and not (kind[v] == "e" and g.succ[v][0] == g.cW):
                if emin is not None and g.rank[L] >= emin: c["bonly"] += 1
            w = nxt[v]
            if lam[w] != L: c["k3"] += 1                      # (K3 a)
            if kind[v] != "e":
                if cl[v] != cl[w]: c["k3"] += 1               # (K3 c)
            elif w != g.cW:
                eb = 1 << g.rank[v]
                if cl[v] != (cl[w][0], cl[w][1] | eb) or (cl[w][1] & eb): c["k3"] += 1    # (K3 d)
            if t > 0 and (v in core or v == g.cW or v == g.cX or (kind[v] == "e" and g.succ[v][0] == g.cW)):
                if cl[v] != cls[0][v]: c["k3"] += 1           # (K3 e)
        for gv in gates:
            e, b = face_e[gv], face_b[gv]
            if val[e] == val[b]: c["notie"] += 1
            a = st["sbar"][gv]; o = b if a == e else e
            if not (val[a] < val[o]): c["locgate"] += 1
            if cl[gv] != min(cl[e], cl[b]): c["k4"] += 1
            # (K2) on the pair of faces and on gate pairs of one mover
            if (val[e] <= val[b]) and not (cl[e] <= cl[b]): c["k2"] += 1
            if (val[b] <= val[e]) and not (cl[b] <= cl[e]): c["k2"] += 1
        if t < T:
            st2 = hist[t + 1]; val2 = st2["val"]; cl2 = cls[t + 1]
            for v in range(n):
                if val[v] > val2[v]: c["f1"] += 1
                if cl[v] > cl2[v]: c["k1"] += 1
                if v not in core and (val[v] <= val2[v]) and not (cl[v] <= cl2[v]): c["k2"] += 1
            for x in range(N):
                vals = [val[w] for w in g.succ[x]]; bv = max(vals)
                if vals[st["sig"][x]] != bv and sum(1 for q in vals if q == bv) > 1: d["cov_tie"] += 1
                if vals[st2["sig"][x]] != bv: c["howard"] += 1
                if vals[st["sig"][x]] == bv and st2["sig"][x] != st["sig"][x]: c["howard"] += 1
                for y in g.succ[x]:
                    if not (cl2[x] >= cl[y]): c["k5"] += 1
    # ---- LEVEL and PLATEAU per reference
    P = 2 * M * (N + 2 * M)
    if T > P * (N + 2 * M + 6) + N: c["tbound"] += 1
    reflist = [T] if refs == "T" else list(range(1, T + 1))
    detail = []
    for b in reflist:
        clb = cls[b]; sigb = hist[b]["sig"]
        gate_classes_b = set(clb[gv] for gv in gates)
        beta_classes = set((g.rew[bv], 0) for bv in betas)
        phis = []; fronts = []; lags = []
        for t in range(0, b + 1):
            cl = cls[t]
            lag = [v for v in range(n) if cl[v] != clb[v]]
            if not lag:
                phis.append(None); fronts.append(None); lags.append(set()); continue
            if ctrl == 1: m = max(cl[v] for v in lag)
            else: m = min(cl[v] for v in lag)
            fr = set(v for v in lag if cl[v] == m)
            phis.append((m, -len(fr))); fronts.append(fr); lags.append(set(lag))
        bprime = next(t for t in range(b + 1) if phis[t] is None)
        # (C4)
        for t in range(bprime, b):
            if cls[t] != cls[t + 1]: c["c4"] += 1; break
        if b - bprime > N: c["c4"] += 1
        mvals = set(); phivals = set(); sawbeta = False
        stall_flags = []
        for t in range(0, bprime):
            cl = cls[t]; fr = fronts[t]; m = phis[t][0]; st = hist[t]; nxt = nx[t]
            mvals.add(m); phivals.add(phis[t])
            # (L2)
            for v in fr:
                if not (kind[v] == "m" or kind[v] == "g" or (kind[v] == "b" and g.succ[v][0] < N)): c["l2"] += 1
            # (L3)
            alpha = any(kind[z] == "m" and (nxt[z] not in lags[t]) and m == clb[nxt[z]] for z in fr)
            beta = False
            if not alpha or True:
                # a play at t whose cycle lies in FRONT_t, made of movers, chosen gates, beta-faces; m = (c, {}) for a beta c
                for v in fr:
                    L = st["lam"][v]
                    if L in fr and kind[L] == "b" and m == (g.rew[L], 0):
                        u = nxt[L]; ok = True; steps = 0
                        while u != L and steps <= n:
                            if u not in fr or kind[u] not in ("m", "g", "b"): ok = False; break
                            u = nxt[u]; steps += 1
                        if ok and steps <= n: beta = True; break
            if alpha: d["alpha"] += (1 if b == T else 0)
            if beta and not alpha: d["beta"] += (1 if b == T else 0); sawbeta = True
            if not (alpha or beta): c["l3"] += 1
            if not (m in gate_classes_b or m in beta_classes): c["l3"] += 1
            # (L1) and stall
            cl2 = cls[t + 1]
            stall = all(cl2[v] == cl[v] for v in fr)
            stall_flags.append(stall)
            if not lags[t + 1] <= lags[t]: c["l1"] += 1
            if stall:
                if b == T:
                    d["stalls"] += 1
                    if cl2 != cl: d["stallloud"] += 1
                if phis[t + 1] is None or phis[t + 1] != phis[t] or fronts[t + 1] != fr: c["l1"] += 1
                # (L4): the map s
                okmap = True
                for z in fr:
                    if kind[z] == "m":
                        w = g.succ[z][sigb[z]]
                        if w not in fr: okmap = False
                    elif kind[z] == "g":
                        r = st["sbar"][z]
                        if r != face_b[z] or r not in fr: okmap = False
                    else:
                        if g.succ[z][0] not in fr: okmap = False
                    if not okmap: c["l4map"] += 1; okmap = True
                # (L4): the cycle
                found = False
                for z in fr:
                    if kind[z] != "m": continue
                    x = z; seen = []; good = True
                    while x not in seen:
                        seen.append(x)
                        gv = g.succ[x][sigb[x]]; bv = face_b[gv]
                        if not (x in fr and gv in fr and bv in fr and st["sbar"][gv] == bv): good = False; break
                        y = g.succ[bv][0]
                        if y >= N: good = False; break
                        x = y
                    if good: found = True; break
                if not found: c["l4cyc"] += 1
            else:
                if b == T: d["nonstall"] += 1
                if phis[t + 1] is not None and not (phis[t + 1] > phis[t]): c["l1"] += 1
        if len(mvals) > 2 * M or len(phivals) > P: c["l5"] += 1
        if not sawbeta and len(phivals) > M * (N + 2 * M): c["l5"] += 1
        if b == T: d["phivals"] = len(phivals); d["mvals"] = len(mvals)
        # ---- plateaus: maximal intervals of constant Phi
        t = 0
        while t < bprime:
            u = t
            while t + 1 < bprime and phis[t + 1] == phis[u]: t += 1
            v = t; t += 1
            if v == u: continue
            m = phis[u][0]; J = fronts[u]
            if ctrl == 2: Y = set(J)
            else: Y = set(x for x in range(n) if cls[u][x] <= m)
            nE = sum(1 for x in Y if g.owner[x] == 0); nmov = sum(1 for x in Y if x < N)
            L = v - u
            if b == T:
                d["plateaus"] += 1
                if L > d["platmax"]: d["platmax"] = L; d["platY"] = nmov; d["platmaxE"] = nE
            if L > N + 2 * M + 5: c["plat"] += 1
            if b == T:
                if L > nmov: d["platsharp"] += 1
                d["cov_frontg"] += sum(1 for x in J if kind[x] == "g"); d["cov_frontb"] += sum(1 for x in J if kind[x] == "b")
                for gv in gates:
                    if gv in Y:
                        e, bb = face_e[gv], face_b[gv]
                        if e in Y and bb in Y:
                            d["cov_bothY"] += 1
                            if cls[u][e] == cls[u][bb]: d["cov_bothYeq"] += 1
                        if hist[u]["sbar"][gv] == e: d["cov_efaceY"] += 1
                for s in range(u, v):
                    if any(hist[s]["sbar"][o] != hist[s + 1]["sbar"][o] for o in g.odd): d["cov_flipinplat"] += 1
            if L > nE: c["p7"] += 1
            for s in range(u, v + 1):
                cl = cls[s]; nxt = nx[s]
                for x in range(n):
                    if (cl[x] <= m) != (x in Y): c["p1"] += 1
                    elif x in Y and cl[x] != cls[u][x]: c["p1"] += 1
                for x in Y:
                    if nxt[x] not in Y: c["p2"] += 1
                    if x < N:
                        for y in g.succ[x]:
                            if y not in Y or not (cl[y] <= cl[x]): c["p3"] += 1
                    if g.owner[x] == 1:
                        if hist[s]["sbar"][x] not in Y: c["p4"] += 1
                        if s > u and hist[s]["sbar"][x] != hist[s - 1]["sbar"][x]: c["p4"] += 1
                # (P6): the step s -> s+1 switches a mover of Y   (s + 1 <= b always: v < bprime <= b)
                if not any(hist[s + 1]["sig"][x] != hist[s]["sig"][x] for x in Y if x < N): c["p6"] += 1
            if want_detail: detail.append((b, u, v, L, nmov, nE))
    if want_detail: return c, d, detail
    return c, d

def fmt(name, g, c, d):
    return (name + " N %d M %d | " % (g.N, g.M) + " ".join("%s %d" % (k, c[k]) for k in CNT) + " | " +
            " ".join("%s %d" % (k, d[k]) for k in ("T", "phivals", "mvals", "nonstall", "stalls", "stallloud", "plateaus",
                                                     "platmax", "platY", "platmaxE", "alpha", "beta")))

if __name__ == "__main__":
    import os, eng
    args = sys.argv[1:]; refs = "T"; tie = "keep-low"; ctrl = int(os.environ.get("RB_CTRL", "0"))
    files = []
    for a in args:
        if a == "--all": refs = "all"
        elif a.startswith("--tie="): tie = a[6:]
        else: files.append(a)
    tot = {k: 0 for k in CNT}
    import random
    for f in files:
        g = eng.build(eng.load(f)); h = eng.howard_run(g, tie=tie, rng=random.Random(1))
        c, d = check_run(g, h, refs=refs, ctrl=ctrl)
        for k in CNT: tot[k] += c[k]
        print(fmt(os.path.basename(f), g, c, d), flush=True)
    print("TOTAL files %d refs %s tie %s ctrl %d | " % (len(files), refs, tie, ctrl) + " ".join("%s %d" % (k, tot[k]) for k in CNT))
