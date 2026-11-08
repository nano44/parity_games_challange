#!/usr/bin/env python3
"""REFEREE successor 27: P-N5-ASC game-side DATA with my own engine (xicyc_vj.VJ, xicyc_replay.build/howard from successor 26; built
from R104's text; e-priorities ordered by (level, gate index), i.e. [E-LEV] holds by construction). No L-NEW code imported.
Per state t of the IDEAL-CYC Howard run from the stored start and every vertex v: seq_t(v) = the e-vertices of Pi_t(v) in play order
under (sigma_t, sigma-bar_t). Counters: max ascents vs U(G) (UP-B); E-MON on consecutive states with equal Lambda; CHAIN-DECOMP;
UP-JUMP (each ascent's play segment holds a beta whose Xi-target mover has level > its own mover's level and >= l); distinct e-sets per
(vertex, Lambda-interval). Usage: asc_game.py FILE.json..."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xicyc_replay import howard

def analyse(G):
    E, lab, ties, states, movers, idx = howard(G)
    inv = {v: k for k, v in idx.items()}
    evs = {v for v, k in inv.items() if isinstance(k, tuple) and k[0] == "e"}
    lev = G["lev"]; N = G["N"]
    U = sum(1 for x in range(N) for o in G["opts"][x] if o[1] >= 0 and lev[o[1]] > lev[x])
    rk = E.rk
    def play(st, v):
        seen = []; s = set()
        while v not in s: s.add(v); seen.append(v); v = st[v]
        return seen
    C = dict(maxasc=0, emon_units=0, emon_viol=0, cd_units=0, cd_viol=0, uj_units=0, uj_viol=0, maxDE=0, ties=ties, T=len(lab))
    prevE = None; DE = {}
    for t, (s, st, val) in enumerate(states):
        Et = {}
        for v in range(E.n):
            L, P, k = val[v]; pl = play(st, v)
            seq = [u for u in pl if u in evs and u in P]
            Et[v] = (L, frozenset(seq))
            a = [i for i in range(len(seq) - 1) if rk[seq[i + 1]] > rk[seq[i]]]
            C["maxasc"] = max(C["maxasc"], len(a))
            if seq:   # CHAIN-DECOMP: successor of the first e is a mover with the same Lambda and E(v) = {f} + E(y_f)
                f = seq[0]; y = st[f]; C["cd_units"] += 1
                ok = y in movers and val[y][0] == L and set(seq) == {f} | {u for u in play(st, y) if u in evs and u in val[y][1]}
                C["cd_viol"] += not ok
            for i in a:   # UP-JUMP
                C["uj_units"] += 1; ia, ib = pl.index(seq[i]), pl.index(seq[i + 1]); x0 = inv[seq[i]][1][0]; l0 = lev[x0]; hit = False
                for p in range(ia, ib):
                    u = pl[p]; ku = inv.get(u)
                    if isinstance(ku, tuple) and ku[0] == "b" and p + 1 < len(pl) and pl[p + 1] in movers:
                        xm = ku[1][0]; ym = movers.index(pl[p + 1])
                        if lev[ym] > lev[xm] and lev[ym] >= l0: hit = True
                C["uj_viol"] += not hit
            key = (v, L); DE.setdefault(key, set()).add(frozenset(seq))
        if prevE is not None:
            for v in range(E.n):
                if prevE[v][0] == Et[v][0]:
                    C["emon_units"] += 1
                    A, B = prevE[v][1], Et[v][1]; d = A ^ B
                    C["emon_viol"] += bool(d) and max(d, key=lambda u: rk[u]) not in B
        prevE = Et
    C["maxDE"] = max(len(x) for x in DE.values()); C["U"] = U
    return C

if __name__ == "__main__":
    for f in sys.argv[1:]:
        C = analyse(json.load(open(f)))
        print(os.path.basename(f), "U(G)", C["U"], "max ascents", C["maxasc"], "OK" if C["maxasc"] <= C["U"] else "VIOLATION", "|", C, flush=True)
