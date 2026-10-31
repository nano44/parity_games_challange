#!/usr/bin/env python3
"""L-NEW box 113 (DESC*, proof side). Built on box 111 desc.py (same engine, same oriented unary-bit CS, same W-run split).
Per W-run F, with switches read from sigma (Even y switched at k iff sigma_(k+1)(y) != sigma_k(y)):
  SW    = |S_F|, S_F := vertices switched at some transition of F; DESC_S, WITVIOL_S (STAIR-U needs 0).
  SWC   = |S*_F|, S*_F := vertices switched at some k WITH a W-change at k; DESC_S*, WITVIOL_S*.
  RD    = root descents: (y, k) with y switched at k, W(y) changed at k, and the change a descent of y.
  CPD   = descents at non-switched (v, k); CPD_PURE = those whose v-play prefix to the first switched vertex y was unswitched on
          [k'_v, k] (k'_v = v's previous change) -- DESC-COPY then forces y's change at k to be a ROOT descent; CPD_BLK = the rest.
  RDT   = W-changing transitions containing a root descent.  WCT = W-changing transitions.  ROOTMISS = W-changing vertices whose
          first switched vertex on the new play has no W-change (lemma SW-WIT says 0).
Usage: desc3.py G.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 else None; n = g.n; own = g.owner
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st); S, TAU, FB = [tuple(s)], [tuple(t)], []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
Wc, Wm = {}, {}
def Wraw(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
def bits(x):
    c, m, l = x; sl = l if E.par[c] == 1 else -l
    rb = tuple((1 if (m >> r) & 1 else 0) if E.rankpar[r] == 0 else (0 if (m >> r) & 1 else 1) for r in range(n - 1, -1, -1))
    return rb + tuple(int(sl >= j) for j in range(-n, n + 1))
def W(k, tau):
    if (k, tau) not in Wm: Wm[(k, tau)] = [bits(x) for x in Wraw(k, tau)]
    return Wm[(k, tau)]
def succ(k, tau, v): return tau[v] if own[v] == 1 else S[k][v]
runs = []
for k in range(len(S) - 1):
    if TAU[k + 1] != TAU[k] or FB[k] or [x[0] for x in Wraw(k, TAU[k])] != [x[0] for x in Wraw(k + 1, TAU[k])]: continue
    if runs and runs[-1][-1] == k - 1: runs[-1].append(k)
    else: runs.append([k])
T = dict(DR=0, DT_=0, DS=0, DMISS=0, MAPMAX=0, TIESW=0, ROOTCH=0, RD_ORIG=0, RD_RELAY=0, NRUN=len(runs), WT=0, WCT=0, DESC=0, SW=0, DESC_S=0, WITVIOL_S=0, SWC=0, DESC_SC=0, WITVIOL_SC=0, RD=0, RDT=0, CPD=0,
         CPD_PURE=0, CPD_BLK=0, SWD_NONROOT=0, ROOTMISS=0, MAXRD_RUN=0, MAXWCT_RUN=0, MAXSW_RUN=0)
VERB = os.environ.get("VERB")
for run in runs:
    tau = TAU[run[0]]; C = {x for x in range(n) if Wraw(run[0], tau)[x][0] == x}
    swk = {k: {y for y in range(n) if own[y] == 0 and S[k + 1][y] != S[k][y]} for k in run}
    lastsw = {}  # vertex -> list of switch times
    for k in run:
        for y in swk[k]: lastsw.setdefault(y, []).append(k)
    chg = {k: {v for v in range(n) if W(k, tau)[v] != W(k + 1, tau)[v]} for k in run}
    SF = set().union(*swk.values()); SC = {y for k in run for y in swk[k] & chg[k]}
    T["SW"] += len(SF); T["SWC"] += len(SC); T["MAXSW_RUN"] = max(T["MAXSW_RUN"], len(SF))
    last = {}; rd_run = 0; wct = 0
    for k in run:
        A, B = W(k, tau), W(k + 1, tau)
        if chg[k]: wct += 1
        T["WITVIOL_S"] += bool(chg[k]) and not (chg[k] & SF); T["WITVIOL_SC"] += bool(chg[k]) and not (chg[k] & SC)
        hasrd = False; dk = {}
        for v in sorted(chg[k]):
            q = next(i for i in range(len(A[v])) if A[v][i] != B[v][i])
            # first switched vertex on v's new play
            x, path, seen = v, [], set()
            while x not in swk[k] and x not in seen and x not in C: seen.add(x); path.append(x); x = succ(k + 1, tau, x)
            y = x if x in swk[k] else None
            if y is None: T["ROOTMISS"] += 1
            elif y not in chg[k]: T["ROOTMISS"] += 1
            isdesc = v in last and q > last[v][0]
            dk[v] = last[v][1] if isdesc else None
            if isdesc:
                T["DESC"] += 1; T["DESC_S"] += v in SF; T["DESC_SC"] += v in SC
                if v in swk[k]:
                    if v in chg[k]: T["RD"] += 1; hasrd = True; rd_run += 1
                    else: T["SWD_NONROOT"] += 1
                else:
                    T["CPD"] += 1; kp = last[v][1]
                    blk = any(kp <= j <= k for p in path for j in lastsw.get(p, []))
                    T["CPD_BLK" if blk else "CPD_PURE"] += 1
                    if VERB: print("CPD", k, v, "y", y, "kprev", kp, "blk", blk, "q", last[v][0], "->", q)
            last[v] = (q, k)
        T["RDT"] += hasrd
        # DESC-ROOT map: each descent (v, k) -> (x, k), x = first vertex on v's new play switched somewhere in [k'_v, k]
        T["ROOTCH"] += len(swk[k] & chg[k]); T["TIESW"] += len(swk[k] - chg[k])
        for y in swk[k] & chg[k]:
            if dk.get(y) is not None:
                z = S[k + 1][y]; T["RD_RELAY" if z in chg[k] else "RD_ORIG"] += 1
        img = {}
        for v, kp in dk.items():
            if kp is None: continue
            x, seen = v, set()
            while True:
                sws = [j for j in lastsw.get(x, []) if kp <= j <= k]
                if sws: break
                if x in C or x in seen: x = None; break
                seen.add(x); x = succ(k + 1, tau, x)
            if x is None or dk.get(x) is None: T["DMISS"] += 1; continue
            img[x] = img.get(x, 0) + 1
        for x, c in img.items():
            T["MAPMAX"] = max(T["MAPMAX"], c); kx = dk[x]; sws = [j for j in lastsw.get(x, []) if kx <= j <= k]
            if k in sws: T["DR"] += 1
            elif any(kx < j < k for j in sws): T["DT_"] += 1
            else: T["DS"] += 1
    T["WT"] += len(run); T["WCT"] += wct; T["MAXRD_RUN"] = max(T["MAXRD_RUN"], rd_run); T["MAXWCT_RUN"] = max(T["MAXWCT_RUN"], wct)
print(f"DESC3 {os.path.basename(sys.argv[1])} n {n} " + " ".join(f"{a} {b}" for a, b in T.items()))
