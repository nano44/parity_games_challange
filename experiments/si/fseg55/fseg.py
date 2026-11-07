#!/usr/bin/env python3
"""L-SI box 55: first-segment (FS) Even selectors inside W-runs (note docs/si/N5-FSEG-box55.md).
For a state k of a W-run and an Odd vertex o, the FIRST SEGMENT FS_k(o) is the (sigma_k, sigmabar_k)-play from sigmabar_k(o) up to
(excluding) its first vertex in D_k u C (box 54 §3). An Even vertex y is an FS-SELECTOR at k if y in FS_k(o) for some o in D_k u D_(k+1)
(a deviator now or next). Per W-run transition: the switches, which switches are at FS-selectors (and of which deviators), whether
the transition is a source event (R97), and whether a switch uses an arena edge new at k (not in H_(k-1); L-NEW NEW-EDGE).
Summary per game: SW (switches in W-runs), FSSW (switches at FS-selectors), SRCEV, SRCFS (source events carrying an FS switch), SRCNOFS
(the others) split into _CSW (an Even C-node switches), _DIN (some Odd vertex enters D), _OTHER,
MAXFSV (max switches of one vertex while an FS-selector, per W-run), MAXSWV (max switches of one vertex per W-run).
Flags: -t prints the per-transition timeline. Usage: fseg.py GAME.pg [START] [-t]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
args = [a for a in sys.argv[1:] if a != "-t"]; TL = "-t" in sys.argv
g = load(args[0]); st = readstart(args[1]) if len(args) > 1 else None; n = g.n; own = g.owner
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st); S, TAU, FB, IS = [tuple(s)], [tuple(t)], [], []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4]); IS.append(set(r[2]))
Wc, WX, XX = {}, {}, {}
def Wv(k, tau):
    if (k, tau) not in WX:
        if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
        WX[(k, tau)] = Wc[tau].evaluate(S[k])[0]
    return WX[(k, tau)]
def Xv(k):
    if k not in XX: XX[k] = E.evaluate(S[k])
    return XX[k]
def arena(k):
    H = {(v, S[k][v]) for v in range(n) if own[v] == 0}
    return H | set(IS[k])
runs = []; cur = None
for k in range(len(S) - 1):
    if TAU[k + 1] != TAU[k] or FB[k] or [x[0] for x in Wv(k, TAU[k])] != [x[0] for x in Wv(k + 1, TAU[k])]:
        cur = None; continue
    if cur is None: cur = []; runs.append(cur)
    cur.append(k)
T = dict(WRUNS=len(runs), SW=0, FSSW=0, SRCEV=0, SRCFS=0, SRCNOFS=0, SRCNOFS_CSW=0, SRCNOFS_DIN=0, SRCNOFS_OTHER=0, MAXFSV=0, MAXSWV=0)
for run in runs:
    tau = TAU[run[0]]; C = {v for v in range(n) if Wv(run[0], tau)[v][0] == v}
    fsc = [0] * n; swc = [0] * n
    if TL: print(f"WRUN {run[0]}..{run[-1] + 1} C {sorted(C)}")
    for k in run:
        X0, sb0 = Xv(k); X1, sb1 = Xv(k + 1); s0, s1 = S[k], S[k + 1]
        D0 = {o for o in range(n) if own[o] == 1 and sb0[o] != tau[o]}; D1 = {o for o in range(n) if own[o] == 1 and sb1[o] != tau[o]}
        nxt = lambda v: s0[v] if own[v] == 0 else sb0[v]
        fsof = {}
        for o in sorted(D0 | D1):
            y, seen = sb0[o], set()
            while y not in seen and y not in D0 and y not in C:
                seen.add(y)
                if own[y] == 0: fsof.setdefault(y, []).append(o)
                y = nxt(y)
        sw = [y for y in range(n) if own[y] == 0 and s0[y] != s1[y]]
        src = any(X0[v] != X1[v] for v in (D0 | D1 | C))
        Hprev = arena(k - 1) if k - 1 in run else None
        T['SW'] += len(sw); T['SRCEV'] += src
        fs_here = [y for y in sw if y in fsof]
        T['FSSW'] += len(fs_here)
        if src: T['SRCFS' if fs_here else 'SRCNOFS'] += 1
        if src and not fs_here:
            if any(y in C for y in sw): T['SRCNOFS_CSW'] += 1
            elif any(own[z] == 1 and z in D1 - D0 for z in range(n)): T['SRCNOFS_DIN'] += 1
            else: T['SRCNOFS_OTHER'] += 1
        for y in sw:
            swc[y] += 1
            if y in fsof: fsc[y] += 1
        if TL:
            parts = []
            for y in sw:
                ne = "" if Hprev is None else ("N" if (y, s1[y]) not in Hprev else "")
                parts.append(f"{y}:{s0[y]}>{s1[y]}{ne}" + (f"[FS{fsof[y]}]" if y in fsof else ""))
            xs = [v for v in sorted(D0 | D1 | C) if X0[v] != X1[v]]
            print(f"  k {k} {'SRC' if src else '   '} D {sorted(D0)} sw {' '.join(parts)} srcXch {xs}")
    T['MAXFSV'] = max(T['MAXFSV'], max(fsc)); T['MAXSWV'] = max(T['MAXSWV'], max(swc))
print(f"FSEG {os.path.basename(args[0])} n {n} iters {len(S) - 1} " + " ".join(f"{a} {b}" for a, b in T.items()))
