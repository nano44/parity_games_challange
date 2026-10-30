#!/usr/bin/env python3
"""L-SI box 53: checks of the lemmas behind Theorem ROOT-FLIP (docs/si/N5-SBF-box53.md §2), at EVERY state / transition of the N5 run
(not only W-runs). Xi_k, sbar_k := E.evaluate(sigma_k). o is NON-OWN at k if Xi_k(o) has cycle node != o. T_k(o) := the tight
successors {t : o (+) Xi_k(t) = Xi_k(o)}.
Per state, per non-own Odd o:  NOTT sbar(o) not in T_k(o);  SELX the selection rule fails (cycle node c even: sbar(o) = least index
of T_k(o); c odd: sbar(o) = the element of T_k(o) with the least key, key(t) = indices of t's (sigma, sbar)-path to c read from c's
end);  NCX Lemma NOCLOSE fails (a successor y whose play path contains o with NOT Xi(y) > Xi(sbar(o)) for Even).
Per transition, flips at o non-own at k and k+1:  TIEX Lemma TIE fails (old target's Xi fixed, but Xi(o) or Xi(new) changes, or the
new target is not tied at k);  EVENX a tie flip (old target fixed) in an even-cycle-node round;  DESCX a tie flip with no flipping
non-own w, Xi(w) fixed, on t1's or t2's k-path or (k+1)-path;  ROOTX2 a transition with a non-own flip but no non-own flip whose old
target's Xi changed.  MUT=1 (control): SEL checked against max in place of min; SELX must become > 0.  Counts: STATES, NONOWN (pairs), FLIPS (non-own), TIES.  Usage: rootflip.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
a = sys.argv[1:]; g = load(a[0]); n = g.n; own = g.owner
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, readstart(a[1]) if len(a) > 1 else None)
S = [tuple(s)]; TA = list(t)
while True:
    r = step(g, E, Ed, list(S[-1]), TA)
    if r is None: break
    S.append(tuple(r[0])); TA = list(r[1])
MUT = os.environ.get('MUT') == '1'  # control: the selection rule with max in place of min must fail
EV = [E.evaluate(x) for x in S]; ODD = [o for o in range(n) if own[o] == 1]; SU = [sorted(set(x)) for x in g.succ]
def path(k, y):
    val, sb = EV[k]; c = val[y][0]; p = [y]; x = y
    while x != c:
        x = S[k][x] if own[x] == 0 else sb[x]; p.append(x)
        if len(p) > n + 1: raise RuntimeError("no cycle node")
    return p
def key(k, y): return tuple(reversed(path(k, y)[:-1]))
def nonown(k, o): return EV[k][0][o][0] != o
c = dict(STATES=len(S), NONOWN=0, NOTT=0, SELX=0, NCX=0, FLIPS=0, TIES=0, TIEX=0, EVENX=0, DESCX=0, ROOTX2=0)
for k in range(len(S)):
    val, sb = EV[k]
    for o in ODD:
        if not nonown(k, o): continue
        c['NONOWN'] += 1; T = [x for x in SU[o] if E.extend(o, val[x]) == val[o]]
        if sb[o] not in T: c['NOTT'] += 1; continue
        cn = val[o][0]
        best = min(T) if E.par[cn] == 0 else min(T, key=lambda x: key(k, x))
        if MUT: best = max(T) if E.par[cn] == 0 else max(T, key=lambda x: key(k, x))
        if best != sb[o]: c['SELX'] += 1
        for y in SU[o]:
            if o in path(k, y)[1:] and not E.key(val[y]) > E.key(val[sb[o]]): c['NCX'] += 1
for k in range(len(S) - 1):
    (v0, b0), (v1, b1) = EV[k], EV[k + 1]
    fl = [o for o in ODD if b0[o] != b1[o] and nonown(k, o) and nonown(k + 1, o)]
    if not fl: continue
    if not any(v0[b0[o]] != v1[b0[o]] for o in fl): c['ROOTX2'] += 1
    for o in fl:
        c['FLIPS'] += 1; t1, t2 = b0[o], b1[o]
        if v0[t1] != v1[t1]: continue
        c['TIES'] += 1
        if v0[o] != v1[o] or v0[t2] != v1[t2] or v0[t2] != v0[t1]: c['TIEX'] += 1; continue
        if E.par[v0[o][0]] == 0: c['EVENX'] += 1
        P = set(path(k, t1) + path(k, t2) + path(k + 1, t1) + path(k + 1, t2))
        if not any(w in P and w != o and v0[w] == v1[w] for w in fl): c['DESCX'] += 1
print(f"ROOTFLIP {os.path.basename(a[0])} n {n} " + " ".join(f"{k} {v}" for k, v in c.items()))
