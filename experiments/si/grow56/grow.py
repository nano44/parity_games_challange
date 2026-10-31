#!/usr/bin/env python3
"""L-SI box 56: how a deviator's first segment changes inside a W-run (note docs/si/N5-GROW-box56.md). For Odd o in D_k n D_(k+1),
FS_k(o) := the (sigma_k, sigmabar_k)-play from sigmabar_k(o) up to (excluding) its first vertex in D_k u C (box 54 §3), and END_k(o) := that
first vertex. A change FS_k(o) -> FS_(k+1)(o) is classified at the FIRST position i where the two plays [o] + FS + [END] differ:
  CHOICE  i = 1: sigmabar(o) changed;
  ESW     the vertex at i - 1 is Even and switched at k (a re-route at an Even switch on the segment);
  OSW     the vertex at i - 1 is Odd and its sigmabar changed (an Odd on the segment; it enters D or re-chooses);
  ENDX    the plays agree vertex by vertex but END moved: the old END left D (the segment EXTENDS through it) or a segment vertex
          entered D_(k+1) or C (the segment is CUT).
Within each class, LONGER / SHORTER / EQUAL compares the lengths of the new and the old segment. For ESW, the switched vertex y is
classified: SRC (k is a source event), y's own switch count so far in the W-run, and whether y's new edge was new in the arena H_k.
ESW_PREVFREE / ESW_PREVSRC / ESW_PREVNONE: the transition k - 1 -> k before the re-route is source-free / a source event / outside the
W-run; ESW_ZROSE / ESW_ZFLAT: Xi of y's new target z rose / did not rise at k - 1 -> k (L-NEW OVERTAKE-W predicts a rise when the
edge is new). FUEL: per (selector y, new target z) and W-run, the sequence of keys of z's Xi-rise at k - 1 -> k (cycle-node change
(2, 0), path-set change (1, top rank of the difference), length (0, 0)), one entry per distinct re-route (k, y); FUEL_TURN counts
direction reversals, FUEL_EQ equal consecutive keys. Per game: counts per class, and per W-run the max number of ESW re-routes at one deviator. -v O prints o's segment per state.
Usage: grow.py GAME.pg [START] [-v O]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
args = sys.argv[1:]; VO = None
if "-v" in args: i = args.index("-v"); VO = int(args[i + 1]); del args[i:i + 2]
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
runs = []; cur = None
for k in range(len(S) - 1):
    if TAU[k + 1] != TAU[k] or FB[k] or [x[0] for x in Wv(k, TAU[k])] != [x[0] for x in Wv(k + 1, TAU[k])]:
        cur = None; continue
    if cur is None: cur = []; runs.append(cur)
    cur.append(k)
def seg(k, o, tau, C):
    X, sb = Xv(k); D = {z for z in range(n) if own[z] == 1 and sb[z] != tau[z]}
    y, out, seen = sb[o], [o], {o}
    while y not in seen and y not in D and y not in C:
        seen.add(y); out.append(y); y = S[k][y] if own[y] == 0 else sb[y]
    return out, y
T = {}
def inc(key, d=1): T[key] = T.get(key, 0) + d
inc('WRUNS', len(runs)); mx = 0; maxswy = 0
for run in runs:
    tau = TAU[run[0]]; C = {v for v in range(n) if Wv(run[0], tau)[v][0] == v}
    esw = [0] * n; swc = [0] * n; fuel = {}; seenev = set()
    for k in run:
        (X0, b0), (X1, b1) = Xv(k), Xv(k + 1); s0, s1 = S[k], S[k + 1]
        D0 = {z for z in range(n) if own[z] == 1 and b0[z] != tau[z]}; D1 = {z for z in range(n) if own[z] == 1 and b1[z] != tau[z]}
        src = any(X0[v] != X1[v] for v in (D0 | D1 | C))
        Hp = ({(v, S[k - 1][v]) for v in range(n) if own[v] == 0} | IS[k - 1]) if k - 1 in run else None
        for o in sorted(D0 & D1):
            (q0, e0), (q1, e1) = seg(k, o, tau, C), seg(k + 1, o, tau, C)
            if VO == o: print(f"  k {k} {'SRC' if src else '   '} seg {q0[1:]} end {e0}")
            if q0 == q1 and e0 == e1: inc('SAME'); continue
            a0, a1 = q0 + [e0], q1 + [e1]; i = 0
            while i < min(len(a0), len(a1)) and a0[i] == a1[i]: i += 1
            ln = 'LONGER' if len(q1) > len(q0) else 'SHORTER' if len(q1) < len(q0) else 'EQUAL'
            if i == 1: cl = 'CHOICE'
            elif i >= min(len(a0), len(a1)) or i == len(q0) or i == len(q1): cl = 'ENDX'
            else:
                y = a0[i - 1]
                if own[y] == 0 and s0[y] != s1[y]:
                    cl = 'ESW'; esw[o] += 1; inc('ESW_SRC' if src else 'ESW_FREE')
                    inc('ESW_NEWEDGE' if (Hp is not None and (y, s1[y]) not in Hp) else 'ESW_OLDEDGE')
                    z = s1[y]
                    if k - 1 in run:
                        Xp, bp = Xv(k - 1); Dp = {u for u in range(n) if own[u] == 1 and bp[u] != tau[u]}
                        psrc = any(Xp[v] != X0[v] for v in (Dp | D0 | C))
                        inc('ESW_PREVSRC' if psrc else 'ESW_PREVFREE')
                        inc('ESW_ZROSE' if Xp[z] != X0[z] else 'ESW_ZFLAT')
                        if Xp[z] != X0[z] and (k, y) not in seenev:
                            seenev.add((k, y)); a, b = Xp[z], X0[z]
                            fr = (2, 0) if a[0] != b[0] else (1, (a[1] ^ b[1]).bit_length() - 1) if a[1] != b[1] else (0, 0)
                            fuel.setdefault((y, z), []).append(fr)
                    else: inc('ESW_PREVNONE')
                elif own[y] == 1 and b0[y] != b1[y]: cl = 'OSW'
                else: cl = 'ENDX'
            inc(cl); inc(cl + '_' + ln)
        for y in range(n):
            if own[y] == 0 and s0[y] != s1[y]: swc[y] += 1
    mx = max(mx, max(esw)); maxswy = max(maxswy, max(swc))
    for (y, z), fl in fuel.items():
        tr = sum(1 for i in range(1, len(fl) - 1) if (fl[i] > fl[i - 1]) != (fl[i + 1] > fl[i]) and fl[i] != fl[i - 1] and fl[i + 1] != fl[i])
        eq = sum(1 for i in range(1, len(fl)) if fl[i] == fl[i - 1])
        inc('FUEL_EV', len(fl)); inc('FUEL_TURN', tr); inc('FUEL_EQ', eq)
        T['MAXFUELEV'] = max(T.get('MAXFUELEV', 0), len(fl)); T['MAXFUELTURN'] = max(T.get('MAXFUELTURN', 0), tr)
        if VO is not None: print("FUEL", y, z, fl)
T['MAXESW'] = mx; T['MAXSWV'] = maxswy
print(f"GROW {os.path.basename(args[0])} n {n} iters {len(S) - 1} " + " ".join(f"{a} {b}" for a, b in sorted(T.items())))
