#!/usr/bin/env python3
"""L-RED successor 38 (R162): copy of L-NEW box 111 desc.py (l-new ffe347ee), unchanged except: DT = W-changing transitions that
contain >= 1 descent, DTMAX = max over runs, NRUN, LONGEST (longest W-run), DVERT = vertices with a descent; with env EXCL (regex on labels) also
DESC_U / DT_U over U = vertices whose label does NOT match EXCL, and WITVIOL = W-changing transitions with no W-change on U (STAIR-U
needs WITVIOL 0); env UIN=1 sets U = vertices with in-degree >= 1 (self-loops count). Original docstring:
L-NEW box 111: DESCENTS. Per W-run and vertex v, the first-difference positions q_1, q_2, ... of v's successive W-changes (oriented
unary-bit CS as box 110; 0 = most significant). A DESCENT is q_(j+1) > q_j (a change strictly LESS significant than the previous one).
Lemma ASC-RUN: WCH_F(v) <= (3n + 1)(1 + DESC_F(v)). Prints WCH, DESC, max ascending run, VIOL (ASC-RUN), and for each descent whether
its transition, or some transition since v's previous change, is a source event (R97): DSRC_NOW / DSRC_SINCE. Usage: desc.py G.pg [START]"""
import sys, os
HERE = os.environ.get("LNEW", os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(HERE, "new", "box21")); sys.path.insert(0, os.path.join(HERE, "harness")); sys.path.insert(0, os.path.join(HERE, "new"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg, re
EXCL = os.environ.get("EXCL")
LAB = [l.split('"')[1] if '"' in l else "" for l in open(sys.argv[1]) if re.match(r"\s*\d", l)]
INU = [not (EXCL and re.fullmatch(EXCL, LAB[v])) for v in range(len(LAB))]
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 else None; n = g.n; own = g.owner
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st); S, TAU, FB = [tuple(s)], [tuple(t)], []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
Wc, Wm = {}, {}
if os.environ.get("UIN") == "1": INU = [False] * n; [INU.__setitem__(w, True) for v in range(n) for w in g.succ[v]]
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
def src(k, tau):
    X0, sb0 = E.evaluate(S[k]); X1, sb1 = E.evaluate(S[k + 1]); C = {x for x in range(n) if Wraw(k, tau)[x][0] == x}
    Sk = {o for o in range(n) if own[o] == 1 and (sb0[o] != tau[o] or sb1[o] != tau[o])} | C
    return any(X0[x] != X1[x] for x in Sk)
runs = []
for k in range(len(S) - 1):
    if TAU[k + 1] != TAU[k] or FB[k] or [x[0] for x in Wraw(k, TAU[k])] != [x[0] for x in Wraw(k + 1, TAU[k])]: continue
    if runs and runs[-1][-1] == k - 1: runs[-1].append(k)
    else: runs.append([k])
T = dict(DESC_U=0, DT_U=0, WITVIOL=0, DT=0, DTMAX=0, NRUN=len(runs), LONGEST=max([len(r) for r in runs] or [0]), DVERT=0, WCH=0, DESC=0, VIOL=0, DSRC_NOW=0, DSRC_SINCE=0, MAXRUN=0, MAXDESCV=0, MAXWCHV=0)
for run in runs:
    tau = TAU[run[0]]; SRC = {k: src(k, tau) for k in run}
    last = {}; desc = {}; wch = {}; runlen = {}; dt = 0
    for k in run:
        A, B = W(k, tau), W(k + 1, tau); hasd = False; hasdu = False; chu = False; chany = False
        for v in range(n):
            if A[v] == B[v]: continue
            chany = True; chu = chu or INU[v]
            q = next(i for i in range(len(A[v])) if A[v][i] != B[v][i]); wch[v] = wch.get(v, 0) + 1
            if v in last and q > last[v][0]:
                desc[v] = desc.get(v, 0) + 1; T["DESC"] += 1; runlen[v] = 1; hasd = True
                if INU[v]: T["DESC_U"] += 1; hasdu = True
                T["DSRC_NOW"] += SRC[k]; T["DSRC_SINCE"] += any(SRC[j] for j in run if last[v][1] < j <= k)
            else: runlen[v] = runlen.get(v, 0) + 1
            T["MAXRUN"] = max(T["MAXRUN"], runlen[v]); last[v] = (q, k)
        dt += hasd; T["DT_U"] += hasdu; T["WITVIOL"] += chany and not chu
    T["DT"] += dt; T["DTMAX"] = max(T["DTMAX"], dt); T["DVERT"] += len(desc)
    for v in wch:
        T["WCH"] += wch[v]; T["VIOL"] += wch[v] > (3 * n + 1) * (1 + desc.get(v, 0))
        T["MAXDESCV"] = max(T["MAXDESCV"], desc.get(v, 0)); T["MAXWCHV"] = max(T["MAXWCHV"], wch[v])
print(f"DESC {os.path.basename(sys.argv[1])} n {n} WT {sum(len(r) for r in runs)} " + " ".join(f"{a} {b}" for a, b in T.items()))
