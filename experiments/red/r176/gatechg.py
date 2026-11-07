#!/usr/bin/env python3
# COPY of claude/l-new 1ebdae81 experiments/new/box129/gatechg.py (L-NEW box 129), path line adapted for experiments/red/r176/; read-only use by L-RED R176.
"""L-NEW box 129 GATE-CHARGE: the charge graph behind STRICT-PAY (box 128), per TWO-FIX window and fallback-free stretch.
For every non-first W-strict move m of an Even h (consecutive moves i0 -> i1 at j1, i1 -> i2 at j2; W-strict: key W_j2(i2) > key W_j2(i1)),
STRICT-PAY gives a change of Xi(i1), Xi(i2) on [j1-1, j2-1] or of W(i1), W(i2) on [j1, j2]. The EARLIEST such change (x, k, world) is
traced to its ORIGIN: walk x's play at state k-1 in that world (Odd: sbar for Xi, tau for W) to the first vertex v switched at k.
The payer of m is the move p = (v, k). Kinds: PAYXI / PAYW; the payer is FIRST / STRICT (non-first W-strict) / FLAT / WEAK (non-first,
not W-strict); CYC := no switched vertex on the play (the change enters through the play's cycle; no payer).
Charge chains: m -> p -> payer(p) -> ... while the payer is itself a charged (non-first W-strict) move. DEPTH := the longest chain;
FANIN := the most charged moves with one payer; SELFPAY := payer is h itself (h on its option's play, route (C)).
MAXSCC := largest strongly connected component (size >= 2, or a self-loop) of the vertex graph h -> payer vertex (mutual payment);
REVISIT := charge chains that return to a vertex already on them.
Windows are split by ODIFF (number of Odd vertices with sbar != tau): totals for ODIFF 0 and ODIFF >= 1 are printed separately.
Usage: gatechg.py G.pg [START|-]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "red", "r170")); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, start_pair, readstart, Engine, dual
import pg
from freeze import run, windows

g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
E0, Ed0 = Engine(g), Engine(dual(g)); s, t = start_pair(g, E0, Ed0, st)
S, T, F, E = run(g, s, t); W, SB = windows(g, S, T, E)
n, own, pr = g.n, g.owner, g.prio
def blank(): return dict(win=0, strict=0, charged=0, payxi=0, payw=0, cyc=0, p_first=0, p_strict=0, p_flat=0, p_weak=0, selfpay=0,
                         depth=0, fanin=0, maxstrict_h=0, maxscc=0, revisit=0)
TOT = {0: blank(), 1: blank()}
for a, b in W:
    if b - a < 1: continue
    tau, sb = T[a], SB[a]; od = sum(own[v] == 1 and sb[v] != tau[v] for v in range(n)); R = TOT[min(od, 1)]; R["win"] += 1
    EW = Engine(pg.Game(list(pr), list(own), [list(g.succ[v]) if own[v] == 0 else [tau[v]] for v in range(n)]))
    EX = Engine(pg.Game(list(pr), list(own), [list(g.succ[v]) if own[v] == 0 else [sb[v]] for v in range(n)]))
    WV = {j: EW.evaluate(tuple(S[j][v] if own[v] == 0 else -1 for v in range(n)))[0] for j in range(a, b + 1)}
    XV = {j: EX.evaluate(tuple(S[j][v] if own[v] == 0 else -1 for v in range(n)))[0] for j in range(a, b + 1)}
    stl = []; p = a
    for j in range(a + 1, b + 1):
        if F[j]: stl.append((p, j - 1)); p = j
    stl.append((p, b))
    for p, q in stl:
        if q - p < 1: continue
        moved = {k: {v for v in range(n) if own[v] == 0 and S[k][v] != S[k - 1][v]} for k in range(p + 1, q + 1)}
        kind = {}; prev = {}; payer = {}; strict_h = {}
        for k in range(p + 1, q + 1):
            for h in sorted(moved[k]):
                o, w = S[k - 1][h], S[k][h]
                isst = EW.key(WV[k][w]) > EW.key(WV[k][o])
                if h not in prev: kind[(h, k)] = "first"
                else: kind[(h, k)] = "strict" if isst else ("flat" if EW.key(WV[k][w]) == EW.key(WV[k][o]) else "weak")
                R["strict"] += isst; strict_h[h] = strict_h.get(h, 0) + isst
                if kind[(h, k)] == "strict":
                    R["charged"] += 1; j1, j2, i1, i2 = prev[h], k, o, w
                    ev = [(kk + 1, x, "X") for kk in range(j1 - 1, j2 - 1) for x in (i1, i2) if XV[kk][x] != XV[kk + 1][x]] + \
                         [(kk + 1, x, "W") for kk in range(j1, j2) for x in (i1, i2) if WV[kk][x] != WV[kk + 1][x]]
                    if not ev: continue   # STATIC-TIE case: impossible outside the corner (box 128 STATVIOL 0)
                    kk, x, wd = min(ev)
                    R["payxi" if wd == "X" else "payw"] += 1
                    v, seen = x, set()
                    while v not in moved[kk] and v not in seen:
                        seen.add(v); v = S[kk - 1][v] if own[v] == 0 else (sb[v] if wd == "X" else tau[v])
                    if v in seen: R["cyc"] += 1; continue
                    payer[(h, k)] = (v, kk); R["selfpay"] += v == h
                prev[h] = k
        for m, pm in payer.items():
            R["p_" + kind.get(pm, "first")] += 1
        cnt = {}
        for pm in payer.values(): cnt[pm] = cnt.get(pm, 0) + 1
        R["fanin"] = max(R["fanin"], max(cnt.values(), default=0))
        memo = {}
        def depth(m, guard=0):
            if m in memo: return memo[m]
            if m not in payer or guard > 10 ** 4: return 0
            memo[m] = -1   # cycle guard (a payer chain cannot repeat a move: payers are at earlier or equal transitions)
            d = 1 + (depth(payer[m], guard + 1) if payer[m] in payer and memo.get(payer[m]) != -1 else 0)
            memo[m] = d; return d
        for m in payer: R["depth"] = max(R["depth"], depth(m))
        if os.environ.get("VERB") == "1" and payer:   # L-RED R176 addition: per-stretch line
            print(f"  WIN [{a}, {b}] ODIFF {od} stretch charged {len(payer)} depth {max(depth(m) for m in payer)} fanin {max(cnt.values(), default=0)}")
        # vertex-level charge graph h -> payer vertex; its largest strongly connected component (mutual payment) and longest chain revisit
        adj = {}
        for (h, k), (v, kk) in payer.items(): adj.setdefault(h, set()).add(v)
        idx, low, onst, stk, cnt_ = {}, {}, set(), [], [0]
        def scc(u):
            idx[u] = low[u] = cnt_[0]; cnt_[0] += 1; stk.append(u); onst.add(u)
            for w_ in adj.get(u, ()):
                if w_ not in idx: scc(w_); low[u] = min(low[u], low[w_])
                elif w_ in onst: low[u] = min(low[u], idx[w_])
            if low[u] == idx[u]:
                c = 0; mem = []
                while True:
                    x_ = stk.pop(); onst.discard(x_); c += 1; mem.append(x_)
                    if x_ == u: break
                R["maxscc"] = max(R["maxscc"], c if c > 1 or u in adj.get(u, ()) else 0)
                if os.environ.get("VERB") == "1" and c > 1: print("  SCC window", (a, b), "stretch", (p, q), "size", c, "members", sorted(mem), "owners/deg", [(own[z], len(g.succ[z])) for z in sorted(mem)])
        sys.setrecursionlimit(100000)
        for u in list(adj):
            if u not in idx: scc(u)
        for m in payer:
            seen_v, c = set(), m
            while c in payer:
                if c[0] in seen_v: R["revisit"] += 1; break
                seen_v.add(c[0]); c = payer[c]
        R["maxstrict_h"] = max([R["maxstrict_h"]] + list(strict_h.values()))
for od in (0, 1):
    R = TOT[od]
    print(f"GATECHG {os.path.basename(sys.argv[1])} n {n} ODIFF{'0' if od == 0 else '1+'} " + " ".join(f"{k.upper()} {v}" for k, v in R.items()))
