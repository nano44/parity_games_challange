#!/usr/bin/env python3
"""L-NEW box 119: blocked edges inside N5's tau-stretches (box118/gate.py's definitions). G_tau, W_k, IW_k (W-improving), Is_k
(Xi-improving); BL_k := IW_k minus Is_k (blocked). INCONSISTENT transition: Is_k != IW_k or a fallback (box 118).
Per stretch transition k: SW_k := Even switches (y, sigma_(k+1)(y)); a switch is RELEASED if its edge was blocked at some earlier
transition of the same stretch (and has not been used since). An UNBLOCK EVENT of an edge e at j: e in BL_j and e in Is_(j+1); its
CAUSE is «target» if Xi(z) changes at j (Xi_j(z) != Xi_(j+1)(z)), «source» if only Xi(sigma_j(y)) / sigma(y) changes, «both».
Prints: INC; inconsistent transitions with no released switch (UNPAID); released switches REL; distinct released edges DREL; max releases
of one edge; unblock events UNB by cause; distinct (z, j) target Xi-changes that cause some unblock (TGT: the per-target charge, no
degree factor) and the max number of edges unblocked by one (z, j) (FAN).
OLDFED: inconsistent transitions (with a predecessor in the same stretch) none of whose switches is fresh, i.e. every switched edge
was already in Is_(k-1).
Usage: unblock.py G.pg [START|-]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
n = g.n; own = g.owner; E, Ed = Engine(g), Engine(dual(g))
s, t = start_pair(g, E, Ed, st); S, T, FB = [tuple(s)], [tuple(t)], []
while True:
    r = step(g, E, Ed, list(S[-1]), list(T[-1]))
    if r is None: break
    S.append(tuple(r[0])); T.append(tuple(r[1])); FB.append(r[4])
K = len(S) - 1; Wc = {}
def weng(tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau]
XI = [None] * (K + 1)
def xi(k):
    if XI[k] is None: vs, _ = E.evaluate(S[k]); XI[k] = (vs, set(E.improving(S[k], vs)))
    return XI[k]
INC = UNPAID = REL = UNB = OLDFED = 0; cause = {"target": 0, "source": 0, "both": 0}; RELE = {}; TGT = {}
blocked_since = {}  # edge -> stretch id while pending (blocked earlier, not used since)
sid = 0
for k in range(K):
    if k == 0 or T[k] != T[k - 1]: sid += 1; blocked_since = {}
    if T[k + 1] != T[k]: continue
    W0 = weng(T[k]).evaluate(S[k])[0]; IW = set(weng(T[k]).improving(S[k], W0)); Xk, Is = xi(k)
    BL = IW - Is; inc = bool(BL) or bool(Is - IW) or FB[k]
    sw = [(y, S[k + 1][y]) for y in range(n) if own[y] == 0 and S[k + 1][y] != S[k][y]]
    rel = [e for e in sw if e in blocked_since]
    REL += len(rel)
    for e in rel: RELE[e] = RELE.get(e, 0) + 1; del blocked_since[e]
    # fresh-fed: some switch (y, z) of this transition was not in Is_(k-1) (box 113 NEW-FUEL: then Xi(z) changed at k - 1)
    fresh = k >= 1 and T[k - 1] == T[k] and any(e not in xi(k - 1)[1] for e in sw)
    if inc:
        INC += 1; UNPAID += not rel; OLDFED += (k >= 1 and T[k - 1] == T[k] and not fresh)
    # unblock events at k: e in BL_k and e in Is_(k+1) (same stretch)
    if T[k + 1] == T[k] and k + 1 < K + 1:
        Xn, Isn = xi(k + 1)
        for (y, z) in BL:
            if (y, z) in Isn:
                UNB += 1
                tc = Xk[z] != Xn[z]; sc = (Xk[S[k][y]] != Xn[S[k + 1][y]]) or S[k + 1][y] != S[k][y]
                cause["both" if tc and sc else "target" if tc else "source"] += 1
                if tc: TGT[(z, k)] = TGT.get((z, k), 0) + 1
    for e in BL: blocked_since.setdefault(e, k)
mx = max(RELE.values()) if RELE else 0
print(f"UNBLOCK {os.path.basename(sys.argv[1])} n {n} iters {K} INC {INC} UNPAID {UNPAID} REL {REL} DREL {len(RELE)} maxrel {mx} UNB {UNB} "
      f"target {cause['target']} source {cause['source']} both {cause['both']} TGT {len(TGT)} FAN {max(TGT.values()) if TGT else 0} OLDFED {OLDFED}")
