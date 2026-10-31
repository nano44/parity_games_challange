#!/usr/bin/env python3
"""L-SI box 58: key ancestry of Xi-changes along an N5 run (note docs/si/N5-ANC-box58.md).
KEY of a change a -> b: (2, 0) cycle node, (1, r) top rank of the path-set difference, (0, 0) length; None = no change. Checks (all
expected 0 by the note's lemmas; every N5 transition, not only W-runs):
  PREFV  KEY-PREF: a change at z has the same key as at the first vertex s of z's OLD play whose choice changes.
  OLDV   OLD-PLAY (packet §2): z's old play has a changed vertex.
  EVENV  EVEN-SPLIT: Even s switching w -> z': key(s) <= max(gain, key(z')), gain := key(Xi_u(w), Xi_u(z')).
  ODDV   ODD-KEY case I (Odd s with a changed choice, s not on its old choice x's NEW play): key(s) <= key(x); the walk goes to x
         (with --newpref: to the new choice x2 when key(x2) >= key(s), else to x).
  ODD2   case II count (s on x's new play); the walk goes to the NEW choice x2; ODD2V violations of ODD-SPLIT
         key(s) <= max(og, key(x2)), og := key(Xi_u(x), Xi_u(x2)) (Odd's swap key).
  ARMV   ARM: an Even switch s -> z' at u with gain g, armed at t (last t < u with Xi_t(z') <= Xi_t(sigma_t(s))), has a change of Xi(z') at
         some t' in [t, u) with key >= g.  INIT = switches with no arming time (<= one per edge per run).
  ROOTS  same-transition walk from every change to its root: EROOT (Even switch, gain >= key), OROOT (Odd case II with og >= key,
         or a case I violation), LOOP (walk revisits a vertex; LOOP2 those at key (2, 0)).
Pairs (inside W-runs, as srcfuel.py box 56/57 but every Even switch, not only FS-selectors): FUEL re-route (y, z) at k with key a.
  GAINV  GAIN-DOWN: gain of the re-route > a.
  HC     changes of Xi(z) in the window (k, k'] (k' the next re-route of the pair, or the run end) with key > a.
  SELF1  HC changes whose root switch is a switch of y itself.   CHAINV  an ancestry chain of an HC change whose root switch is a fuel
         re-route of (y, z) with fuel key <= a (NO-SELF-GAIN: 0).  MAXDEPTH  longest ancestry chain (ARM links) of an HC change;
         LEVELS distinct key levels on it. HC windows include the re-route's own transition k.
  SELFESC HC changes rooted at an Odd escape (OROOT) whose escaped cycle contains y and y switches at that transition (SELFESC0: at k).
  AMP    Odd escape roots whose swap key exceeds the gain of every Even switch on the escaped cycle (ONOCL: no Even switch on it).
  MAXFUEL / MAXHC / MAXSELF per pair and W-run.
  ESCREP repeat escapes of one (s, x) in one W-run (SI: the run); ESCNODESC those whose swap key og does not strictly descend from the
         previous one (CONJECTURE ESC-DESC: 0 under N5); ESCEQ equal swap keys; ESCASC
         strict ascents; ESCNONMONO (s, x, W-run) sequences that both ascend and descend; MAXPLAT the longest
         run of consecutive equal swap keys (PLAT). --exdesc prints the longest sequence.
  MAXESC_SX / MAXESC_S / MAXESC_RUN  per W-run (SI: the whole run): max escapes of one Odd s from one old choice x / of one s / in all.
  WESC   distinct escapes (Odd s, transition u) with u in a W-run: ESC_LEAVE_TAU old choice = tau(s); ESC_TO_TAU new choice = tau(s);
         ESC_ZD the escaped cycle Z (s, x, ..., back to s, under the NEW strategies) has an Odd vertex off tau; ESC_WCYC old choice
         tau(s) and every other Odd vertex of Z on tau at u + 1 (Z is then a W-cycle at u + 1). LOOPC1: loops whose walk took a case I (old-choice) Odd step;
           LOOPLOW0 loops below key (2, 0) without a case I step (Prop LOOP-NEW: 0).
  SOURCES  distinct ultimate sources of all changes (follow walk root -> ARM ancestor until INIT / escape / loop; SRC_I, SRC_O, SRC_L);
           MAXDESC  the largest number of changes with one ultimate source.
Usage: anc.py GAME.pg [START]   |   anc.py --si GAME.pg (classical switch-all SI; the whole run is the one "W-run"; the barrier
check of note §5: every lemma above uses only R15a, R57 and improving switches, so it holds on this run too)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
EXDESC = "--exdesc" in sys.argv
if EXDESC: sys.argv.remove("--exdesc")
NEWPREF = "--newpref" in sys.argv
if NEWPREF: sys.argv.remove("--newpref")
SI = sys.argv[1] == "--si"
if SI: sys.argv.pop(1)
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 else None; n = g.n; own = g.owner
sys.path.insert(0, os.path.join(HERE, "..")); from startcheck import check_start; check_start(g, st, sys.argv[2] if len(sys.argv) > 2 else "")  # P-N5-ODD fixes entry 4
E, Ed = Engine(g), Engine(dual(g))
if SI:   # classical switch-all SI (si.py rule_switch_all, best-reward start): sigma only, Odd's optimal counterstrategy; ONE run
    S, IS = [tuple(E.initial("best"))], []
    while True:
        v_ = E.evaluate(S[-1])[0]; I_ = E.improving(S[-1], v_)
        if not I_: break
        IS.append(set(I_)); S.append(E.rule_switch_all(S[-1], v_, I_, None))
    IS.append(set()); TAU = [None] * len(S); FB = [0] * len(S)
else:
    s, t = start_pair(g, E, Ed, st); S, TAU, FB, IS = [tuple(s)], [tuple(t)], [], []
    while True:
        r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
        if r is None: break
        S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4]); IS.append(set(r[2]))
K = len(S) - 1
XX = [E.evaluate(S[k]) for k in range(K + 1)]
X = [x[0] for x in XX]; B = [x[1] for x in XX]
def key(a, b):
    if a == b: return None
    return (2, 0) if a[0] != b[0] else (1, (a[1] ^ b[1]).bit_length() - 1) if a[1] != b[1] else (0, 0)
def kmax(*ks):
    ks = [k for k in ks if k is not None]; return max(ks) if ks else None
def kge(a, b): return a is not None and (b is None or a >= b)
def le(a, b): return E.key(a) <= E.key(b)
def nxt(k, x): return S[k][x] if own[x] == 0 else B[k][x]
KEY = [[key(X[k][v], X[k + 1][v]) for v in range(n)] for k in range(K)]
T = dict(iters=K, CHG=0, PREFV=0, OLDV=0, EVENV=0, ODDV=0, ODD2=0, ODD2V=0, ARM=0, ARMV=0, INIT=0, EROOT=0, OROOT=0, LOOP=0, LOOP2=0, LOOPC1=0, LOOPLOW0=0, ONOCL=0, AMP=0,
         FUELEV=0, GAINV=0, HC=0, SELF1=0, CHAINV=0, MAXDEPTH=0, LEVELS=0, YONZ=0, SELFLEAVE=0, SELFESC=0, SELFESC0=0, MAXHC=0, MAXSELF=0, MAXFUEL=0, WESC=0, ESC_LEAVE_TAU=0, ESC_TO_TAU=0, ESC_ZD=0, ESC_WCYC=0)
EX = []
def changed(k, x): return S[k][x] != S[k + 1][x] if own[x] == 0 else B[k][x] != B[k + 1][x]
def onplay(k1, start, v):
    x, seen = start, set()
    while x not in seen:
        if x == v: return True
        seen.add(x); x = nxt(k1, x)
    return False
ROOT, ROOT_CL = {}, {}
def walk(u, z):
    """Root of the change of Xi(z) at u: ('E', s, z', gain) / ('O', s) / ('L', v) / ('X',) on an OLD-PLAY violation."""
    if (u, z) in ROOT: return ROOT[(u, z)]
    v, vis, kap, res, c1 = z, set(), KEY[u][z], None, False
    while res is None:
        if v in vis:
            res = ('L', v); T['LOOP'] += 1; T['LOOP2'] += KEY[u][v] == (2, 0); T['LOOPC1'] += c1; T['LOOPLOW0'] += (KEY[u][v] != (2, 0)) and not c1; break
        vis.add(v)
        x, seen = v, set()
        while not changed(u, x):
            seen.add(x); x = nxt(u, x)
            if x in seen: break
        if not changed(u, x): T['OLDV'] += 1; res = ('X',); break
        if KEY[u][x] != KEY[u][v]: T['PREFV'] += 1
        if own[x] == 0:
            w, zz = S[u][x], S[u + 1][x]; gn = key(X[u][w], X[u][zz])
            if not (kmax(gn, KEY[u][zz]) is not None and KEY[u][x] <= kmax(gn, KEY[u][zz])): T['EVENV'] += 1
            if kge(gn, KEY[u][x]): res = ('E', x, zz, gn); T['EROOT'] += 1; break
            v = zz
        else:
            xo = B[u][x]
            if not onplay(u + 1, xo, x):
                if not kge(KEY[u][xo], KEY[u][x]): T['ODDV'] += 1; res = ('O', x, None); T['OROOT'] += 1; break
                if NEWPREF and kge(KEY[u][B[u + 1][x]], KEY[u][x]): v = B[u + 1][x]; continue
                v = xo; c1 = True; continue
            T['ODD2'] += 1; x2 = B[u + 1][x]; og = key(X[u][xo], X[u][x2])
            if not (kmax(og, KEY[u][x2]) is not None and KEY[u][x] <= kmax(og, KEY[u][x2])): T['ODD2V'] += 1
            if kge(og, KEY[u][x]):
                cl, q = [], xo
                while q != x: cl.append(q); q = nxt(u + 1, q)
                res = ('O', x, og, cl); T['OROOT'] += 1; ROOT_CL[(u, x)] = cl
                eg = [key(X[u][S[u][e]], X[u][S[u + 1][e]]) for e in cl if own[e] == 0 and S[u][e] != S[u + 1][e]]
                if not eg: T['ONOCL'] += 1
                elif og > max(eg): T['AMP'] += 1
                break
            v = x2
    ROOT[(u, z)] = res; return res
ARMC = {}
def arm(u, s_, zz, gn):
    """ARM: latest t' in [t_arm, u) with key_t'(zz) >= gn; None if INIT; 'V' on a violation."""
    if (u, s_) in ARMC: return ARMC[(u, s_)]
    ta = None
    for t_ in range(u - 1, -1, -1):
        if S[t_][s_] == zz or le(X[t_][zz], X[t_][S[t_][s_]]): ta = t_; break
    if ta is None: res = None; T['INIT'] += 1
    else:
        cand = [t_ for t_ in range(ta, u) if kge(KEY[t_][zz], gn)]
        res = cand[-1] if cand else 'V'
        if not cand: T['ARMV'] += 1
    T['ARM'] += 1; ARMC[(u, s_)] = res; return res
for u in range(K):
    for z in range(n):
        if KEY[u][z] is not None: T['CHG'] += 1; walk(u, z)
for u in range(K):
    for s_ in range(n):
        if own[s_] == 0 and S[u][s_] != S[u + 1][s_]:
            zz = S[u + 1][s_]; arm(u, s_, zz, key(X[u][S[u][s_]], X[u][zz]))
SRC = {}
def source(u, z):
    """Ultimate source of the change (z, u) along the ancestry (walk root, then ARM ancestor, repeated)."""
    path = []
    while (u, z) not in SRC:
        path.append((u, z)); r = walk(u, z)
        if r[0] != 'E': src = (r[0], u, r[1]); break
        tt = arm(u, r[1], r[2], r[3])
        if tt is None or tt == 'V': src = ('I' if tt is None else 'V', u, r[1]); break
        u, z = tt, r[2]
    else: src = SRC[(u, z)]
    for p in path: SRC[p] = src
    return src
from collections import Counter
DESC = Counter(source(u, z) for u in range(K) for z in range(n) if KEY[u][z] is not None)
T['SOURCES'] = len(DESC); T['MAXDESC'] = max(DESC.values()) if DESC else 0
T['SRC_O'] = sum(1 for d in DESC if d[0] == 'O'); T['SRC_I'] = sum(1 for d in DESC if d[0] == 'I'); T['SRC_L'] = sum(1 for d in DESC if d[0] == 'L')
# W-runs as srcfuel.py
Wc, WX = {}, {}
def Wv(k, tau):
    if (k, tau) not in WX:
        if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
        WX[(k, tau)] = Wc[tau].evaluate(S[k])[0]
    return WX[(k, tau)]
runs, cur = ([list(range(K))] if SI else []), None
for k in (range(0) if SI else range(K)):
    if TAU[k + 1] != TAU[k] or FB[k] or [x[0] for x in Wv(k, TAU[k])] != [x[0] for x in Wv(k + 1, TAU[k])]:
        cur = None; continue
    if cur is None: cur = []; runs.append(cur)
    cur.append(k)
inrun = {k for r_ in runs for k in r_}
ESCS = {(r_[1], u_) for (u_, z_), r_ in ROOT.items() if r_[0] == 'O' and r_[2] is not None}
from collections import Counter as _C
runof = {k: i for i, r_ in enumerate(runs) for k in r_}
ESX = _C((runof[u_], s_, B[u_][s_]) for s_, u_ in ESCS if u_ in runof); ESS = _C((runof[u_], s_) for s_, u_ in ESCS if u_ in runof)
ESR = _C(runof[u_] for s_, u_ in ESCS if u_ in runof)
OGK = {}
for (u_, z_), r_ in ROOT.items():
    if r_[0] == 'O' and r_[2] is not None and u_ in runof: OGK[(r_[1], u_)] = r_[2]
seqs = {}
for (s_, u_), og in sorted(OGK.items(), key=lambda t: t[0][1]): seqs.setdefault((runof[u_], s_, B[u_][s_]), []).append((u_, og))
T['ESCREP'] = sum(len(v) - 1 for v in seqs.values()); T['ESCNODESC'] = sum(1 for v in seqs.values() for i in range(len(v) - 1) if not v[i + 1][1] < v[i][1])
T['ESCEQ'] = sum(1 for v in seqs.values() for i in range(len(v) - 1) if v[i + 1][1] == v[i][1])
def _plat(v):
    best = cur = 0
    for i in range(len(v) - 1):
        cur = cur + 1 if v[i + 1][1] == v[i][1] else 0; best = max(best, cur)
    return best
T['MAXPLAT'] = max((_plat(v) for v in seqs.values()), default=0)
T['ESCNONMONO'] = sum(1 for v in seqs.values() if len({(v[i + 1][1] > v[i][1]) for i in range(len(v) - 1)}) > 1)
T['ESCASC'] = sum(1 for v in seqs.values() for i in range(len(v) - 1) if v[i + 1][1] > v[i][1])
if EXDESC and T['ESCNODESC']: print("ESCSEQ", max(seqs.values(), key=len)[:8])
T['MAXESC_SX'] = max(ESX.values(), default=0); T['MAXESC_S'] = max(ESS.values(), default=0); T['MAXESC_RUN'] = max(ESR.values(), default=0)
for s_, u_ in ESCS:
    if SI or u_ not in inrun: continue
    tau = TAU[u_]; xo, x2 = B[u_][s_], B[u_ + 1][s_]; T['WESC'] += 1
    Z = [s_] + ROOT_CL[(u_, s_)]
    T['ESC_LEAVE_TAU'] += xo == tau[s_]; T['ESC_TO_TAU'] += x2 == tau[s_]
    T['ESC_ZD'] += any(own[q] == 1 and B[u_ + 1][q] != tau[q] for q in Z)
    T['ESC_WCYC'] += xo == tau[s_] and not any(own[q] == 1 and B[u_ + 1][q] != tau[q] for q in Z[1:])
def chain(u, z, a, y, zt):
    """Follow the ancestry of the change (z, u): root switch -> ARM ancestor, until a source. Returns (depth, levels, bad)."""
    depth, levels, bad, seen = 0, set(), False, set()
    while (u, z) not in seen:
        seen.add((u, z)); levels.add(KEY[u][z]); r = walk(u, z)
        if r[0] != 'E': break
        _, s_, zz, gn = r
        if s_ == y and zz == zt and (u, y) in FUELK and FUELK[(u, y)] <= a: bad = True
        tt = arm(u, s_, zz, gn)
        if tt is None or tt == 'V': break
        depth += 1; u, z = tt, zz
    return depth, len(levels), bad
FUELK = {}
pairs = []
for run in runs:
    rs = set(run); ev = {}
    for k in run:
        if k - 1 not in rs: continue
        Hp = {(v, S[k - 1][v]) for v in range(n) if own[v] == 0} | IS[k - 1]
        for y in range(n):
            if own[y] == 0 and S[k][y] != S[k + 1][y]:
                z = S[k + 1][y]
                if (y, z) not in Hp and X[k - 1][z] != X[k][z]:
                    a = KEY[k - 1][z]; FUELK[(k, y)] = a; ev.setdefault((y, z), []).append((k, a)); T['FUELEV'] += 1
                    gn = key(X[k][S[k][y]], X[k][z])
                    if gn is None or gn > a: T['GAINV'] += 1
                    T['YONZ'] += onplay(k, z, y)
    pairs.append((run, ev))
for run, ev in pairs:
    for (y, z), L in ev.items():
        h0, e0 = T['HC'], T['SELFESC']
        for i, (k, a) in enumerate(L):
            k2 = L[i + 1][0] if i + 1 < len(L) else run[-1] + 1
            for u in range(k, k2):
                if KEY[u][z] is not None and KEY[u][z] > a:
                    T['HC'] += 1; r = walk(u, z)
                    if r[0] == 'E' and r[1] == y:
                        T['SELF1'] += 1
                        if S[u][y] == z: T['SELFLEAVE'] += 1
                    if r[0] == 'O' and y in r[3] and S[u][y] != S[u + 1][y]:
                        T['SELFESC'] += 1; T['SELFESC0'] += u == k
                        if len(EX) < 6: EX.append(('SELFESC', 'pair', y, z, 'k', k, 'a', a, 'u', u, 'key', KEY[u][z], 'odd', r[1], 'og', r[2]))
                    d, lv, bad = chain(u, z, a, y, z)
                    T['MAXDEPTH'] = max(T['MAXDEPTH'], d); T['LEVELS'] = max(T['LEVELS'], lv)
                    if bad:
                        T['CHAINV'] += 1
                        if len(EX) < 3: EX.append(('CHAINV', y, z, k, a, u))
        T['MAXHC'] = max(T['MAXHC'], T['HC'] - h0); T['MAXSELF'] = max(T['MAXSELF'], T['SELFESC'] - e0); T['MAXFUEL'] = max(T['MAXFUEL'], len(L))
for e in EX: print(*e)
print(f"ANC{'-SI' if SI else ''} {os.path.basename(sys.argv[1])} n {n} " + " ".join(f"{a} {b}" for a, b in T.items()))
