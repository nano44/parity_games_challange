#!/usr/bin/env python3
"""L-NEW box 117: the squeeze. For a run of VARIANT (N5, TBR, ARSB as box115/abl.py; O_k = tau_k for N5 / TBR, sigma-bar_k for ARSB):
LO_k(v) := Xi_(sigma_k)(v) (G valuation, Odd optimal), HI_k(v) := Xi^d_(O_k)(v) (the same (c, P, l) triple of the play of O_k against Even's
optimal counterstrategy on G^d). Checks SANDWICH LO <= HI (Even's order, E.key), counts per transition: LO drops, HI rises (= dual drops),
the settled set SET_k := {v : LO_k(v) = HI_k(v)}, UNSET events (v settled at k, not at k + 1), the settle times and the longest gap between
growths of SET; the BRACKET potential B_k := sum_v lcp(cs(LO_k(v)), cs(HI_k(v))) (cs = box107/finpot.py's digit vector), its drops,
increases and longest gap between increases (bgap); CSV = disagreements of cs's lexicographic order with E.key (sanity, must be 0);
W_k := the (sigma_k, O_k)-play valuation, SANDW = violations of LO <= W <= HI; C_k := sum_v lcp(cs(W_k(v)), cs(HI_k(v))), its drops (all /
at O-constant transitions), increases, longest gap between increases (cgap). Usage: squeeze.py G.pg VARIANT [START|-] [cap] [v]  (v: also print the per-k |SET| line)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); VAR = sys.argv[2]
st = readstart(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3] != "-" else None
cap = int(sys.argv[4]) if len(sys.argv) > 4 else 100000; VERB = len(sys.argv) > 5
n = g.n; own = g.owner; E, Ed = Engine(g), Engine(dual(g))
def even_opt(sig, odd, Is):
    opt = {v: {sig[v]} for v in range(n) if own[v] == 0}
    for v, w in Is: opt[v].add(w)
    succ = [sorted(opt[v]) if own[v] == 0 else [odd[v]] for v in range(n)]
    Er = Engine(dual(pg.Game(list(g.prio), list(own), succ)))
    _, best = Er.evaluate(tuple(odd[v] if own[v] == 1 else -1 for v in range(n)))
    return tuple(best[v] if own[v] == 0 else sig[v] for v in range(n))
s0, t0 = start_pair(g, E, Ed, st); S, T, SB = [tuple(s0)], [tuple(t0)], []
while len(S) <= cap:
    sig, tau = S[-1], T[-1]
    vs, sb = E.evaluate(sig); Is = E.improving(sig, vs); SB.append(tuple(sb))
    if VAR == "ARSB":
        if not Is: break
        S.append(even_opt(sig, sb, Is)); T.append(tau)
    elif VAR == "TBR":
        vt, tb = Ed.evaluate(tau); It = Ed.improving(tau, vt)
        if not Is and not It: break
        ns = even_opt(sig, tau, Is) if Is else sig
        nt = tuple(sb[v] if own[v] == 1 else tau[v] for v in range(n))
        if ns == sig and nt == tau: break
        S.append(ns); T.append(nt)
    elif VAR == "N5":
        r = step(g, E, Ed, list(sig), list(tau))
        if r is None: break
        S.append(tuple(r[0])); T.append(tuple(r[1]))
K = len(S) - 1
O = (SB + [tuple(E.evaluate(S[K])[1])])[:K + 1] if VAR == "ARSB" else T[:K + 1]
odd = lambda s: tuple(s[v] if own[v] == 1 else -1 for v in range(n))
LO = [E.evaluate(S[k])[0] for k in range(K + 1)]
HI = [Ed.evaluate(odd(O[k]))[0] for k in range(K + 1)]
ek = E.key
SANDV = sum(1 for k in range(K + 1) for v in range(n) if ek(LO[k][v]) > ek(HI[k][v]))
LODROP = sum(1 for k in range(K) if any(ek(LO[k + 1][v]) < ek(LO[k][v]) for v in range(n)))
HIRISE = sum(1 for k in range(K) if any(ek(HI[k + 1][v]) > ek(HI[k][v]) for v in range(n)))
SET = [frozenset(v for v in range(n) if LO[k][v] == HI[k][v]) for k in range(K + 1)]
UNSET = sum(len(SET[k] - SET[k + 1]) for k in range(K))
grow = [k for k in range(K) if SET[k + 1] - SET[k]]
pts = [0] + [k + 1 for k in grow] + ([K] if not grow or grow[-1] + 1 != K else [])
gap = max((b - a for a, b in zip(pts, pts[1:])), default=0)
fin = len(SET[K])
def cs(v):
    c, m, l = v
    return (E.rew[c],) + tuple(((1 if E.rankpar[r] == 0 else -1) if (m >> r) & 1 else 0) for r in range(n - 1, -1, -1)) + ((l if E.par[c] == 1 else -l),)
def lcp(a, b):
    i = 0
    while i < len(a) and a[i] == b[i]: i += 1
    return i
# W_k := valuation of the (sigma_k, O_k)-play (one-player engine with Odd fixed to O_k, as box107/finpot.py Weng)
Wc = {}
def Wv(k):
    o = O[k]
    if o not in Wc: Wc[o] = Engine(pg.Game(list(g.prio), list(own), [[o[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[o].evaluate(S[k])[0]
W = [Wv(k) for k in range(K + 1)]
SANDW = sum(1 for k in range(K + 1) for v in range(n) if not (ek(LO[k][v]) <= ek(W[k][v]) <= ek(HI[k][v])))
# consistency of cs with E.key (lexicographic order of cs = Even's order)
CSV = sum(1 for k in range(K + 1) for v in range(n) if (cs(LO[k][v]) < cs(HI[k][v])) != (ek(LO[k][v]) < ek(HI[k][v])))
B = [sum(lcp(cs(LO[k][v]), cs(HI[k][v])) for v in range(n)) for k in range(K + 1)]
BDROP = sum(1 for k in range(K) if B[k + 1] < B[k])
binc = [k for k in range(K) if B[k + 1] > B[k]]
bp = [0] + [k + 1 for k in binc] + ([K] if not binc or binc[-1] + 1 != K else [])
bgap = max((b - a for a, b in zip(bp, bp[1:])), default=0)
C = [sum(lcp(cs(W[k][v]), cs(HI[k][v])) for v in range(n)) for k in range(K + 1)]
CDROP = sum(1 for k in range(K) if C[k + 1] < C[k]); CDROPT = sum(1 for k in range(K) if C[k + 1] < C[k] and O[k + 1] == O[k])
cinc = [k for k in range(K) if C[k + 1] > C[k]]
cp_ = [0] + [k + 1 for k in cinc] + ([K] if not cinc or cinc[-1] + 1 != K else [])
cgap = max((b - a for a, b in zip(cp_, cp_[1:])), default=0)
if VERB:
    print("SETSIZE", " ".join(str(len(s)) for s in SET)); print("B", " ".join(map(str, B))); print("C", " ".join(map(str, C)))
print(f"SQZ {os.path.basename(sys.argv[1])} {VAR} n {n} iters {K}{' CAPPED' if K >= cap else ''} SANDV {SANDV} LODROP {LODROP} HIRISE {HIRISE} UNSET {UNSET} set0 {len(SET[0])} setK {fin} growths {len(grow)} maxgap {gap} CSV {CSV} B0 {B[0]} BK {B[K]} BDROP {BDROP} binc {len(binc)} bgap {bgap} SANDW {SANDW} CDROP {CDROP} CDROPtauconst {CDROPT} cinc {len(cinc)} cgap {cgap}")
