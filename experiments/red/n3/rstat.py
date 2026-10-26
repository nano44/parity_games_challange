#!/usr/bin/env python3
"""Per fallback-free run S of each phase (RESULTS R67 setting): |S| (transitions), N_split(S), |U(S)| at L = -1, and SPLIT-RED's bound
N_split + (N_split + 1)(n + m - 1). Definitions (R67, P-N5-RUND): Even edge (x, z), a := sigma_k(x); SPLIT at k if
[Xi_k(z) > Xi_k(a)] != [W_k(z) > W_k(a)]; ALIGNED state = no split edge; N_split = transitions of S with a non-aligned source.
FORBIDDEN at k (L = -1; my reading of COARSE_{-1}: the valuation key without the length component) if COARSE(W_k(z)) > COARSE(W_k(a)) and
not Xi_k(z) > Xi_k(a). U(S) = S4a switch events (k', (y, z)) of S into an edge forbidden at some state of [k' - n + 1, k' - 1] cap S.
W_k = sigma_k's valuation in G_tau (Odd fixed to tau). A run S = maximal consecutive states of one phase joined by S4a transitions.
Usage: rstat.py GAME [START]   (prints the runs; summary line RMAX)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "hff"))
import n3x, faulthandler
if os.environ.get("FH"): faulthandler.dump_traceback_later(int(os.environ["FH"]))
from hffx import playval

def runs_stats(g, st, verbose=True):
    E, rows = n3x.trace(g, st); n = g.n; m = sum(len(set(s)) for s in g.succ)
    for r in rows:
        nx = [r["nxt"][v] if g.owner[v] == 0 else r["tau"][v] for v in range(n)]
        r["W"] = [playval(E, g, nx, v) for v in range(n)]
    key = E.key; ck = lambda val: key(val)[:2]
    def info(k):
        r = rows[k]; split = False; forb = set()
        for x in range(n):
            if g.owner[x] != 0: continue
            a = r["nxt"][x]
            for z in set(g.succ[x]):
                if z == a: continue
                xi = key(r["vs"][z]) > key(r["vs"][a]); w = key(r["W"][z]) > key(r["W"][a])
                if xi != w: split = True
                if ck(r["W"][z]) > ck(r["W"][a]) and not xi: forb.add((x, z))
        return split, forb
    I = [info(k) for k in range(len(rows))]
    keys = [(r["lam"], r["tau"]) for r in rows]; out = []; i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and keys[j + 1] == keys[i]: j += 1
        a = i
        while a <= j:
            b = a
            while b < j and not rows[b]["fb"]: b += 1      # states a..b, transitions a..b-1 are S4a
            T = b - a
            if T > 0:
                nsp = sum(1 for k in range(a, b) if I[k][0]); U = 0
                for k2 in range(a + 1, b + 1):
                    for x in range(n):
                        if g.owner[x] == 0 and rows[k2]["nxt"][x] != rows[k2 - 1]["nxt"][x]:
                            e = (x, rows[k2]["nxt"][x])
                            if any(e in I[k][1] for k in range(max(a, k2 - n + 1), k2)): U += 1
                bound = nsp + (nsp + 1) * (n + m - 1)
                out.append((i, a, T, nsp, U, bound))
                if verbose: print(f"phase@{i} run@{a} |S|={T} N_split={nsp} |U(S)|={U} SPLIT-RED bound={bound}")
            a = b + 1
        i = j + 1
    return out

if __name__ == "__main__":
    g = n3x.load(sys.argv[1]); st = n3x.readstart(sys.argv[2]) if len(sys.argv) > 2 else None
    o = runs_stats(g, st)
    mx = max(o, key=lambda r: r[2]); print(f"RMAX n={g.n} |S|={mx[2]} N_split={mx[3]} |U|={mx[4]} max N_split={max(r[3] for r in o)} max U={max(r[4] for r in o)}")
