#!/usr/bin/env python3
"""L-RED-B: counters and climb objectives for the pressure points named by the Lead (13:47Z, from L-LIT T69):
(a) «Odd's choices are decided at class level»: an Odd flip needs a class change at a face (R126 GATE-CLASS), a quiet step
    has no flip (R126 QUIET-N), a plateau has no flip inside Y (box 208 (P4));
(b) «the class of a cycle inside FRONT takes at most M values» ((L3) case (beta) with (L5)).
Must-0 counters (unit):
  gclass    (gate, step): sbar flips and neither face changes class                         [R126 GATE-CLASS]
  quietflip (step): no vertex changes class and some Odd vertex flips                       [R126 QUIET-N, first clause]
  gflip     (gate): flips(g) > D^tot(e_g) + D^tot(beta_g) - 2                               [R126 GATE-FLIP (a)]
  betaclass (state, reference T): case (beta) only, and m_t is not (c, {}) for a beta-vertex c that is the cycle node of a
            play at t                                                                       [box 208 (L3) (beta)]
  lamk      (state): more distinct cycle nodes (over vertices other than c_W, c_X, e -> c_W) than 1 + the number of cycles
            of the functional graph Xi_sigma on the movers                                  [R126 (k+1)-Lambda, per state]
Descriptive (the climb objectives): R (steps with a flip), flips (gate flips in all), maxgate (most flips of one gate),
  stallflips (flips at stall steps, reference T: Odd moves while the lowest lagging class stands still), minch (least
  number of vertices that change class at a step with a flip), betavals (distinct m_t over beta-only states), lamvals
  (distinct cycle nodes over the run), Q (loud steps), C (steps where some cycle node changes)."""
import lev

def stats(g, hist):
    N, M, n = g.N, g.M, g.n; T = len(hist) - 1
    kind = g.kind
    cls = [lev.classes(g, st) for st in hist]
    gates = [v for v in range(n) if kind[v] == "g"]
    c = {"gclass": 0, "quietflip": 0, "gflip": 0, "betaclass": 0, "lamk": 0}
    d = {"R": 0, "flips": 0, "maxgate": 0, "stallflips": 0, "minch": -1, "betavals": 0, "lamvals": 0, "Q": 0, "C": 0, "T": T}
    gfl = {gv: 0 for gv in gates}
    clT = cls[T]
    lamset = set()
    excl = set([g.cW, g.cX] + [v for v in range(n) if kind[v] == "e" and g.succ[v][0] == g.cW])
    bvals = set()
    for t in range(T + 1):
        st = hist[t]
        lams = set(st["lam"][v] for v in range(n) if v not in excl)
        lamset |= lams
        # cycles of Xi_sigma on the movers
        nxt = {}
        for x in range(N):
            y = g.xt[(x, st["sig"][x])]
            nxt[x] = y if y >= 0 else None
        seen = {}; ncyc = 0
        for x in range(N):
            path = []; u = x
            while u is not None and u not in seen:
                seen[u] = x; path.append(u); u = nxt[u]
            if u is not None and seen[u] == x: ncyc += 1
        if len(lams) > ncyc + 1: c["lamk"] += 1
        if t == T: break
        st2 = hist[t + 1]; cl = cls[t]; cl2 = cls[t + 1]
        nch = sum(1 for v in range(n) if cl[v] != cl2[v])
        if nch: d["Q"] += 1
        if any(st["lam"][v] != st2["lam"][v] for v in range(n)): d["C"] += 1
        fl = [gv for gv in gates if st["sbar"][gv] != st2["sbar"][gv]]
        if st["sbar"][g.K[2]] != st2["sbar"][g.K[2]]: fl.append(g.K[2])
        if fl:
            d["R"] += 1; d["flips"] += len(fl)
            if nch == 0: c["quietflip"] += 1
            if d["minch"] < 0 or nch < d["minch"]: d["minch"] = nch
            for gv in fl:
                if gv in gfl:
                    gfl[gv] += 1
                    e, b = g.succ[gv]
                    if cl[e] == cl2[e] and cl[b] == cl2[b]: c["gclass"] += 1
        # reference T: stall?  beta-only?
        lag = [v for v in range(n) if cl[v] != clT[v]]
        if lag:
            m = min(cl[v] for v in lag); fr = set(v for v in lag if cl[v] == m); lagset = set(lag)
            if fl and all(cl2[v] == cl[v] for v in fr): d["stallflips"] += len(fl)
            nx = lev.nxt_of(g, st)
            alpha = any(kind[z] == "m" and nx[z] not in lagset and m == clT[nx[z]] for z in fr)
            if not alpha:
                bvals.add(m)
                ok = any(kind[L] == "b" and m == (g.rew[L], 0) for L in set(st["lam"][v] for v in fr))
                if not ok: c["betaclass"] += 1
    for gv in gates:
        e, b = g.succ[gv]
        De = len(set(cls[t][e] for t in range(T + 1))); Db = len(set(cls[t][b] for t in range(T + 1)))
        if gfl[gv] > De + Db - 2: c["gflip"] += 1
    d["maxgate"] = max(gfl.values()) if gfl else 0
    d["betavals"] = len(bvals); d["lamvals"] = len(lamset)
    return c, d

PCNT = ["gclass", "quietflip", "gflip", "betaclass", "lamk"]

if __name__ == "__main__":
    import sys, os, eng
    tot = {k: 0 for k in PCNT}
    for f in sys.argv[1:]:
        g = eng.build(eng.load(f)); h = eng.howard_run(g)
        c, d = stats(g, h)
        for k in PCNT: tot[k] += c[k]
        print("PRESS %s N %d M %d | " % (os.path.basename(f), g.N, g.M) + " ".join("%s %d" % (k, c[k]) for k in PCNT) + " | " +
              " ".join("%s %d" % (k, d[k]) for k in ("T", "Q", "C", "R", "flips", "maxgate", "stallflips", "minch", "betavals", "lamvals")), flush=True)
    print("PRESSTOTAL files %d | " % len(sys.argv[1:]) + " ".join("%s %d" % (k, tot[k]) for k in PCNT))
