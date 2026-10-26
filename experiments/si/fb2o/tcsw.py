#!/usr/bin/env python3
"""L-SI box 16: DATA for docs/si/N5-2O-T-box16.md. Per N5 run (n5x.py step, read-only), inside each phase ((lambda_Xi, tau) constant)
and each fallback-free run S (maximal run of consecutive non-fallback transitions), with D_k := {Odd u : sigma-bar_k(u) != tau_k(u)}
(RESULTS R55), u_k(v) := first vertex of D_k on v's (sigma_k, tau_k)-play (v included), R_D := {v : u(v) exists}:
  TC     transitions k -> k+1 of S at which some v in R_D(k) n R_D(k+1) has u_{k+1}(v) != u_k(v) (a TERMINAL CHANGE); TCMAX: max TC over runs; per vertex, max terminal changes per run (TCV)
  HD     states with (h_D) (no u in D_k whose honest or W-play visits D_k after leaving u), H3D: (h3_D) (lambda_Xi(u) = lambda_W(u))
  ROUTEW states with |D_k| = 2: violation if neither D-vertex is W-direct (on its own W-cycle, or its W-play never meets the other)
Usage: tcsw.py --list FILE [KMIN]   (games with at least KMIN Odd choice vertices, default 2; n <= 48)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import step, start_pair, Engine, dual, load
C = dict(games=0, phases=0, runs=0, trans=0, TC=0, TCMAX=0, TCV=0, states=0, D2=0, HD=0, H3D=0, ROUTEW_n=0, ROUTEW_V=0)

def play(nxt, v):
    seen, out = set(), []
    while v not in seen: seen.add(v); out.append(v); v = nxt(v)
    return out, v

def check(g):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, None); rows = []
    while len(rows) <= 3000:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        D = {u for u in range(g.n) if g.owner[u] == 1 and sb[u] != t[u]}
        wn = lambda v, s=s, t=t: s[v] if g.owner[v] == 0 else t[v]
        hn = lambda v, s=s, sb=sb: s[v] if g.owner[v] == 0 else sb[v]
        uu = {}
        for v in range(g.n):
            pl, _ = play(wn, v); uu[v] = next((x for x in pl if x in D), None)
        W = {}
        for v in range(g.n):
            pl, rep = play(wn, v); i = pl.index(rep); cyc = pl[i:]; c = max(cyc, key=lambda x: E.rank[x]); W[v] = c
        rows.append(dict(s=list(s), t=tuple(t), sb=list(sb), vs=vs, lam=tuple(x[0] for x in vs), D=D, uu=uu, lamW=W,
                         fb=r[4] if r else 0, wn=wn, hn=hn))
        if r is None: break
        s, t = r[0], r[1]
    C["games"] += 1
    for k, row in enumerate(rows):
        C["states"] += 1; D = row["D"]
        hd = True
        for u in D:
            for nx in (row["wn"], row["hn"]):
                pl, _ = play(nx, nx(u))
                if any(x in D for x in pl): hd = False
        C["HD"] += hd
        C["H3D"] += all(row["lam"][u] == row["lamW"][u] for u in D)
        if len(D) == 2:
            C["D2"] += 1; a, b = sorted(D); C["ROUTEW_n"] += 1
            pa, ra = play(row["wn"], a); pb, rb = play(row["wn"], b)
            cyc = lambda pl, rep: pl[pl.index(rep):]
            direct_a = a in cyc(pa, ra) or b not in pa[1:]      # on its own W-cycle, or its W-play never meets b
            direct_b = b in cyc(pb, rb) or a not in pb[1:]
            if not (direct_a or direct_b): C["ROUTEW_V"] += 1
    a = 0
    for k in range(1, len(rows) + 1):
        if k == len(rows) or (rows[k]["lam"], rows[k]["t"]) != (rows[a]["lam"], rows[a]["t"]):
            C["phases"] += 1
            run_tc, per_v = 0, {}
            for j in range(a, k - 1):
                if rows[j]["fb"]:
                    C["runs"] += 1; C["TCMAX"] = max(C["TCMAX"], run_tc); run_tc = 0; per_v = {}; continue
                C["trans"] += 1
                r0, r1 = rows[j], rows[j + 1]
                ch = [v for v in range(g.n) if r0["uu"][v] is not None and r1["uu"][v] is not None and r0["uu"][v] != r1["uu"][v]]
                if ch:
                    C["TC"] += 1; run_tc += 1
                    for v in ch: per_v[v] = per_v.get(v, 0) + 1; C["TCV"] = max(C["TCV"], per_v[v])
            C["runs"] += 1; C["TCMAX"] = max(C["TCMAX"], run_tc); a = k

def main():
    kmin = int(sys.argv[3]) if len(sys.argv) > 3 else 2
    for line in open(sys.argv[2]):
        f = line.strip()
        if not f: continue
        g = load(os.path.join(ROOT, f))
        if g.n > 48: continue
        if sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2) < kmin: continue
        check(g)
    print(" ".join(f"{k}={v}" for k, v in C.items()))

if __name__ == "__main__":
    main()
