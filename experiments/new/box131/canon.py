#!/usr/bin/env python3
"""L-NEW box 131 CANON: which W-optimal arena option does S4a's procedure pick?  (SPEC S1 (iv) on the dual arena: Even = dual-Odd.)
For every transition j-1 -> j that is not an S4c fallback, with tau_(j-1) = tau_j and Is_(j-1) nonempty, and every Even x:
  A(x)   := {sigma_(j-1)(x)} u {w : (x, w) in Is_(j-1)}   (exactly n5x.step's arena; Is from si.Engine.improving on G)
  TIE(x) := {y in A(x) : key W_j(y) = key W_j(sigma_j(x))}, W_j := val(sigma_j, tau) (only |TIE| >= 2 is a real tie)
  NC     : y's W_j-play avoids x for every y in TIE (non-corner tie)
Predicates, split by the parity of the cycle node c of W_j(x) (Even's rule: c odd -> LONGEST path, first strict maximum in list
order; c even -> SHORTEST path, BFS over predecessors in list order):
  MINIDX : sigma_j(x) = min TIE(x)
  DEC    : at a move of x (sigma_j(x) != sigma_(j-1)(x)) with sigma_(j-1)(x) in TIE(x): index decreases
KEYMIN (c even): sigma_j(x) = the TIE member with the lex-smallest BFS key (play path from c, c excluded, under sigma_j);
FLKEYDEC: at an FL move with c even, x's own key strictly decreases (FLKEYEQ: equal; FLKEYEQ_CYCNODE: equal because x is the cycle node c itself, key ()).
FL transitions (W_j = W_(j-1)) are counted separately (FLMOVES_ODD / FLMOVES_EVEN, FLDEC_*). MAXFLMV := most moves of one vertex inside
one maximal run of consecutive FL transitions, by parity.
Usage: canon.py G.pg [START|-]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "red", "r170")); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, start_pair, readstart, Engine, dual
import pg
from freeze import run

def pkey(succ1, y, c):
    """BFS key of y: the play path from c's side, c excluded (SPEC S1 (iv) shortest case: discovery order = lex order of these)."""
    p = []; v = y; seen = set()
    while v != c and v not in seen: seen.add(v); p.append(v); v = succ1[v]
    return tuple(reversed(p)) if v == c else None

def play(succ1, x):
    s = set(); v = x
    while v not in s: s.add(v); v = succ1[v]
    return s

g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
E0, Ed0 = Engine(g), Engine(dual(g)); s, t = start_pair(g, E0, Ed0, st)
S, T, F, E = run(g, s, t); n, own, pr = g.n, g.owner, g.prio
Wc = {}
def weng(tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(pr), list(own), [list(g.succ[v]) if own[v] == 0 else [tau[v]] for v in range(n)]))
    return Wc[tau]
R = {}
def inc(k, d=1): R[k] = R.get(k, 0) + d
flrun = {}  # vertex -> moves in current FL run, per parity
for j in range(1, len(S)):
    if F[j] or T[j] != T[j - 1]: flrun = {}; continue
    sig0, sig1, tau = S[j - 1], S[j], T[j]
    vs, _ = E.evaluate(sig0); Is = E.improving(sig0, vs)
    if not Is: continue
    EW = weng(tau)
    W0 = EW.evaluate(tuple(sig0[v] if own[v] == 0 else -1 for v in range(n)))[0]
    W1 = EW.evaluate(tuple(sig1[v] if own[v] == 0 else -1 for v in range(n)))[0]
    fl = W0 == W1
    if not fl: flrun = {}
    A = {x: {sig0[x]} for x in range(n) if own[x] == 0}
    for x, w in Is: A[x].add(w)
    succ1 = [sig1[v] if own[v] == 0 else tau[v] for v in range(n)]
    for x in A:
        k1 = EW.key(W1[sig1[x]])
        tie = sorted(y for y in A[x] if EW.key(W1[y]) == k1)
        par = "ODD" if pr[W1[x][0]] % 2 == 1 else "EVEN"
        moved = sig1[x] != sig0[x]
        if moved and fl:
            inc("FLMOVES_" + par); inc("FLDEC_" + par, sig1[x] < sig0[x])
            if par == "EVEN":
                succ0 = [sig0[v] if own[v] == 0 else tau[v] for v in range(n)]
                ka, kb = pkey(succ1, x, W1[x][0]), pkey(succ0, x, W0[x][0])
                if ka is None or kb is None: inc("FLKEY_NOPATH")
                else: inc("FLKEYDEC", ka < kb); inc("FLKEYEQ", ka == kb); inc("FLKEYEQ_CYCNODE", ka == kb and x == W1[x][0])
            flrun[(x, par)] = flrun.get((x, par), 0) + 1
            R["MAXFLMV_" + par] = max(R.get("MAXFLMV_" + par, 0), flrun[(x, par)])
        if len(tie) < 2: continue
        nc = all(x not in play(succ1, y) for y in tie)
        tag = par + ("" if nc else "_CORNER")
        inc("TIES_" + tag); inc("MINIDX_" + tag, sig1[x] == tie[0])
        if par == "EVEN":
            ks = {y: pkey(succ1, y, W1[x][0]) for y in tie}
            if all(k is not None for k in ks.values()):
                inc("KEYMIN_" + tag, sig1[x] == min(tie, key=lambda y: ks[y])); inc("KEYTIES_" + tag)
        if moved and sig0[x] in tie:
            inc("MOVETIE_" + tag); inc("DEC_" + tag, sig1[x] < sig0[x])
keys = sorted(R)
print(f"CANON {os.path.basename(sys.argv[1])} n {n} K {len(S) - 1} " + " ".join(f"{k} {R[k]}" for k in keys))
