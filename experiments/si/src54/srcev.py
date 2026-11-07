#!/usr/bin/env python3
"""L-SI box 54 (HXS-POLY proof side): per W-run (R89 / R97: tau fixed, no S4c fallback, lambda_W fixed) the SOURCE EVENTS of R97
(Xi changes at S_k = D_k u D_(k+1) u C), classified per changing source v:
  kind  D (Odd v in D_k u D_(k+1)) / C (v in C) / DC (both);
  coord c / P / l (first coordinate of Xi(v) that changes: cycle node, path set, length);
  ARG   (Odd v) sigma-bar(v) changed at k -> k + 1 (KEEP: unchanged); RET: the new sigma-bar(v) was already used earlier in this W-run (a return);
  EQW   Xi_(k+1)(v) == W_(k+1)(v) (the ceiling is reached);
  LEAVE / ENTER: v in D_k \\ D_(k+1) / D_(k+1) \\ D_k.
Per W-run: LEN (transitions), ES (source events), HXSMAX (max_v HXS_F(v)) at vertex VMAX, and the cause split at VMAX.
Prints one line per W-run with LEN >= 1 and a SUMMARY line. -v VERTEX prints that vertex's Xi trajectory in each W-run.
Usage: srcev.py GAME.pg [START] [-v V]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
args = [a for a in sys.argv[1:]]
VV = None
if "-v" in args:
    i = args.index("-v"); VV = int(args[i + 1]); del args[i:i + 2]
g = load(args[0]); st = readstart(args[1]) if len(args) > 1 else None; n = g.n; own = g.owner
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st); S, TAU, FB = [tuple(s)], [tuple(t)], []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
Wc, Xc = {}, {}
def Wv(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
def Xv(k):
    if k not in Xc: Xc[k] = E.evaluate(S[k])
    return Xc[k]
runs = []; cur = None
for k in range(len(S) - 1):
    if TAU[k + 1] != TAU[k] or FB[k] or [x[0] for x in Wv(k, TAU[k])] != [x[0] for x in Wv(k + 1, TAU[k])]:
        cur = None; continue
    if cur is None: cur = []; runs.append(cur)
    cur.append(k)
tot = dict(WRUNS=0, LEN=0, ES=0, MAXLEN=0, MAXES=0, MAXHXS=0, D=0, C=0, DC=0, Dc=0, DP=0, Dl=0, ARG=0, RET=0, KEEP=0, EQW=0, LEAVE=0, ENTER=0)
for run in runs:
    tau = TAU[run[0]]; W0 = Wv(run[0], tau); C = {v for v in range(n) if W0[v][0] == v}
    hxs = [0] * n; cause = [dict(ARG=0, RET=0, KEEP=0, c=0, P=0, l=0, EQW=0) for _ in range(n)]; used = [set() for _ in range(n)]
    es = 0; traj = []
    for k in run:
        X0, sb0 = Xv(k); X1, sb1 = Xv(k + 1); W1 = Wv(k + 1, tau)
        for o in range(n):
            if own[o] == 1 and sb0[o] != tau[o]: used[o].add(sb0[o])
        D0 = {o for o in range(n) if own[o] == 1 and sb0[o] != tau[o]}; D1 = {o for o in range(n) if own[o] == 1 and sb1[o] != tau[o]}
        Sk = D0 | D1 | C; ev = False
        if VV is not None: traj.append((k, X0[VV], sb0[VV] if own[VV] else S[k][VV], VV in D0, X0[VV] == Wv(k, tau)[VV]))
        tot['LEAVE'] += len(D0 - D1); tot['ENTER'] += len(D1 - D0)
        for v in Sk:
            if X0[v] == X1[v]: continue
            ev = True; hxs[v] += 1
            kd = 'DC' if (v in C and v in (D0 | D1)) else 'C' if v in C else 'D'; tot[kd] += 1
            co = 'c' if X0[v][0] != X1[v][0] else 'P' if X0[v][1] != X1[v][1] else 'l'
            cause[v][co] += 1
            if kd != 'C': tot['D' + co] += 1
            if own[v] == 1:
                if sb0[v] != sb1[v]:
                    cause[v]['ARG'] += 1; tot['ARG'] += 1
                    if sb1[v] != tau[v] and sb1[v] in used[v]: cause[v]['RET'] += 1; tot['RET'] += 1
                else: cause[v]['KEEP'] += 1; tot['KEEP'] += 1
            if X1[v] == W1[v]: cause[v]['EQW'] += 1; tot['EQW'] += 1
        es += ev
    vm = max(range(n), key=lambda v: hxs[v])
    tot['WRUNS'] += 1; tot['LEN'] += len(run); tot['ES'] += es; tot['MAXLEN'] = max(tot['MAXLEN'], len(run))
    tot['MAXES'] = max(tot['MAXES'], es); tot['MAXHXS'] = max(tot['MAXHXS'], hxs[vm])
    if len(run) >= 3 or VV is not None:
        print(f"WRUN k {run[0]}-{run[-1] + 1} LEN {len(run)} ES {es} HXSMAX {hxs[vm]} VMAX {vm} own {own[vm]} inC {vm in C} prio {g.prio[vm]} deg {len(g.succ[vm])} "
              + " ".join(f"{a} {b}" for a, b in cause[vm].items()) + f" NSRCV {sum(1 for h in hxs if h)}")
    if VV is not None:
        for row in traj: print("  TRAJ", *row)
print(f"SUMMARY {os.path.basename(args[0])} n {n} iters {len(S) - 1} " + " ".join(f"{a} {b}" for a, b in tot.items()))
