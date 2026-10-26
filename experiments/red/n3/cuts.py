#!/usr/bin/env python3
"""Cuts of L-SI 16's Corollary ROOT-PIECE (docs/si/N5-ROOT-box20.md §0, §4, l-si 21ce0034), written from its §0 text.
D_t = {Odd u : sigma-bar_t(u) != tau(u)}; F_D(t) = vertices whose (sigma_t, tau)-play meets no vertex of D_t; per class c of the phase,
U = lambda^-1(c), A_t = F_D(t) cap U; an A-GAIN = in-phase S4a transition with A_{t+1} not a subset of A_t. Cut each phase at its fallbacks
and A-gains. Reports per phase and class (classes containing an Odd choice vertex): T, f, G_c, A-gains with some D-vertex leaving D
(D_t - D_{t+1} nonempty) vs not, the longest cut-free piece, and for each Odd choice q of the class rho^P_q(A) (M changes while its choice
lies in A at both ends) against the bound (f + G_c + 1)(|U| - 1 + deg(q) - 1) + f + G_c, plus rho_q (all Xi changes).
Usage: cuts.py GAME [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import n3x

def plays_avoid(nxt, S, n):
    """vertices whose play under nxt meets no vertex of S"""
    res = [None] * n
    for v in range(n):
        path, x = [], v; seen = set()
        while res[x] is None and x not in seen and x not in S: seen.add(x); path.append(x); x = nxt[x]
        ok = res[x] if res[x] is not None else (x not in S)
        for y in path: res[y] = ok
    return res

def main():
    g = n3x.load(sys.argv[1]); st = n3x.readstart(sys.argv[2]) if len(sys.argv) > 2 else None
    E, rows = n3x.trace(g, st); n = g.n
    Q = [v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2]
    for r in rows:
        D = {u for u in range(n) if g.owner[u] == 1 and r["nxt"][u] != r["tau"][u]}
        nxW = [r["nxt"][v] if g.owner[v] == 0 else r["tau"][v] for v in range(n)]
        r["D"] = D; r["FD"] = plays_avoid(nxW, D, n)
    keys = [(r["lam"], r["tau"]) for r in rows]; i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and keys[j + 1] == keys[i]: j += 1
        if j > i:
            lam = rows[i]["lam"]
            for c in sorted({lam[q] for q in Q if lam[q] != q}):
                U = [v for v in range(n) if lam[v] == c]
                A = [{v for v in U if rows[k]["FD"][v]} for k in range(i, j + 1)]
                f = sum(rows[k]["fb"] for k in range(i, j)); G = 0; Gleave = 0; cuts = []
                for k in range(i, j):
                    if rows[k]["fb"]: cuts.append(k); continue
                    if not A[k + 1 - i] <= A[k - i]:
                        G += 1; cuts.append(k); Gleave += bool(rows[k]["D"] - rows[k + 1]["D"])
                pieces, last = [], i
                for k in cuts: pieces.append(k - last); last = k + 1
                pieces.append(j - last)
                qs = [q for q in Q if lam[q] == c and q != c]
                line = f"phase@{i} c={c} |U|={len(U)} T={j-i} f={f} G_c={G} (D-leave {Gleave}, other {G-Gleave}) longest_piece={max(pieces)} pieces={pieces}"
                for q in qs:
                    rho = sum(1 for k in range(i, j) if E.key(rows[k]["vs"][q]) != E.key(rows[k + 1]["vs"][q]))
                    def M(k): return E.weight(rows[k]["vs"][q][1])
                    rhoP = sum(1 for k in range(i, j) if rows[k]["nxt"][q] in A[k - i] and rows[k + 1]["nxt"][q] in A[k + 1 - i] and M(k) != M(k + 1))
                    bnd = (f + G + 1) * (len(U) - 1 + len(set(g.succ[q])) - 1) + f + G
                    line += f" | q={q} rho={rho} rhoP_A={rhoP} bound={bnd}" + (" VIOLATION" if rhoP > bnd else "")
                print(line)
        i = j + 1

if __name__ == "__main__":
    main()
