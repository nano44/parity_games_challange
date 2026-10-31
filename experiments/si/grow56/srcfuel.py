#!/usr/bin/env python3
"""L-SI box 56: classify the SOURCE EVENTS of every W-run (R97) by what carries them (note docs/si/N5-GROW-box56.md §3).
FS-selector switch at k: an Even y on FS_k(o) for some o in D_k u D_(k+1) (box 55) with sigma_(k+1)(y) != sigma_k(y); z := sigma_(k+1)(y).
  FUEL   some FS-selector switch at k is a FUEL RE-ROUTE: k - 1 is in the W-run, (y, z) is not in H_(k-1) (a new arena edge) and
         Xi(z) rose at k - 1 -> k (L-NEW OVERTAKE-W);
  OLDE   not FUEL, and some FS-selector switch at k uses an edge already in H_(k-1);
  FIRST  not FUEL / OLDE, and k is the first transition of the W-run;
  CSW    none of the above, and an Even C-node switches at k;
  OTHER  none of the above.
Also FUELPAIRS: per W-run and (y, z), the number of distinct transitions with a fuel re-route y -> z; MAXPAIR its maximum; KEYTURN /
KEYEQ the direction reversals / repeats of the rise keys of z along those transitions (FUEL-MONO, strict: DEAD on so_th_n32).
CONJECTURE FUEL-DESC: for consecutive fuel re-routes y -> z at k_i < k_(i+1) with keys a, b: b < a (strictly less significant), or Xi(z)
changes at some u in [k_i, k_(i+1) - 2] with key >= a (a RESET). DESCV counts violations; RESET the resets; MAXSTRETCH the longest
strictly descending run of fuel keys between resets (<= n + 2 when DESCV = 0).
Usage: srcfuel.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 else None; n = g.n; own = g.owner
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
def key(a, b): return (2, 0) if a[0] != b[0] else (1, (a[1] ^ b[1]).bit_length() - 1) if a[1] != b[1] else (0, 0)
T = dict(WRUNS=len(runs), SRCEV=0, FUEL=0, OLDE=0, FIRST=0, CSW=0, OTHER=0, FUELPAIRS=0, MAXPAIR=0, KEYTURN=0, KEYEQ=0, RESET=0, DESCV=0, MAXSTRETCH=0)
EX = []
for run in runs:
    tau = TAU[run[0]]; C = {v for v in range(n) if Wv(run[0], tau)[v][0] == v}; fuel = {}
    for k in run:
        (X0, b0), (X1, b1) = Xv(k), Xv(k + 1); s0, s1 = S[k], S[k + 1]
        D0 = {z for z in range(n) if own[z] == 1 and b0[z] != tau[z]}; D1 = {z for z in range(n) if own[z] == 1 and b1[z] != tau[z]}
        if not any(X0[v] != X1[v] for v in (D0 | D1 | C)): continue
        T['SRCEV'] += 1
        fs = set()
        for o in D0 | D1:
            y, seen = b0[o], set()
            while y not in seen and y not in D0 and y not in C:
                seen.add(y)
                if own[y] == 0: fs.add(y)
                y = s0[y] if own[y] == 0 else b0[y]
        sw = [y for y in fs if s0[y] != s1[y]]
        Hp = ({(v, S[k - 1][v]) for v in range(n) if own[v] == 0} | IS[k - 1]) if k - 1 in run else None
        fu = []
        if Hp is not None:
            Xp = Xv(k - 1)[0]
            fu = [y for y in sw if (y, s1[y]) not in Hp and Xp[s1[y]] != X0[s1[y]]]
            for y in fu: fuel.setdefault((y, s1[y]), []).append((key(Xp[s1[y]], X0[s1[y]]), k))
        if fu: T['FUEL'] += 1
        elif sw and Hp is not None: T['OLDE'] += 1
        elif k == run[0]: T['FIRST'] += 1
        elif any(own[c] == 0 and s0[c] != s1[c] for c in C): T['CSW'] += 1
        else: T['OTHER'] += 1
    for (y, z), ev in fuel.items():
        fl = [e[0] for e in ev]; stretch = 1
        for i in range(len(ev) - 1):
            (ka, ta), (kb, tb) = ev[i], ev[i + 1]
            if kb < ka: stretch += 1; continue
            rs = [key(Xv(u)[0][z], Xv(u + 1)[0][z]) for u in range(ta, tb - 1) if Xv(u)[0][z] != Xv(u + 1)[0][z]]
            if any(r >= ka for r in rs): T['RESET'] += 1; stretch = 1
            else:
                T['DESCV'] += 1
                if len(EX) < 3: EX.append((os.path.basename(sys.argv[1]), y, z, ev[i], ev[i + 1]))
            T['MAXSTRETCH'] = max(T['MAXSTRETCH'], stretch)
        T['MAXSTRETCH'] = max(T['MAXSTRETCH'], stretch)
        T['FUELPAIRS'] += 1; T['MAXPAIR'] = max(T['MAXPAIR'], len(fl))
        T['KEYEQ'] += sum(1 for i in range(1, len(fl)) if fl[i] == fl[i - 1])
        T['KEYTURN'] += sum(1 for i in range(1, len(fl) - 1) if fl[i] != fl[i - 1] and fl[i + 1] != fl[i] and (fl[i] > fl[i - 1]) != (fl[i + 1] > fl[i]))
for e in EX: print("DESCV", *e)
print(f"SRCFUEL {os.path.basename(sys.argv[1])} n {n} iters {len(S) - 1} " + " ".join(f"{a} {b}" for a, b in T.items()))
