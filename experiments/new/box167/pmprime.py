#!/usr/bin/env python3
"""L-NEW box 167: per-mover W-side quantities and the PM' screens on real IDEAL runs.
  W(x)    := movers reachable from x along W-targets of ANY option, transitively (the W-closure below x; static)
  KF_x    := R105 KEYFLIP key flips (dynamic)
  WE_x    := #{t : some mover of W(x) moves at step t} (dynamic: the steps at which a key flip of x is possible)
  WM_x    := #{y in W(x) : y moves at least once} (dynamic, a set size)
Screens (deg = number of options of x, desc = strict Xi-descendants):
  S  (static)  moves(x) <= (deg-1)(1 + desc(x) + |W(x)|)
  M  (movers)  moves(x) <= (deg-1)(1 + desc(x) + WM_x)
  E  (events)  moves(x) <= (deg-1)(1 + desc(x) + WE_x)      [implied by KEYFLIP-type facts? reported, not assumed]
  K  (flips)   moves(x) <= (deg-1)(1 + desc(x) + KF_x)      [deg 2: implied by R105 KEYFLIP]
Also checks the chain KF_x <= WE_x (a key flip of x needs a move in W(x) at that step) on every mover.
Usage: pmprime.py [-v] file.json ..."""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(H, "..", "box165", "permover.py")).read().split("\nif __name__")[0])

def wclos(G):
    N = G["N"]; adj = [set(o[0] for o in G["opts"][x] if o[0] >= 0) for x in range(N)]; R = []
    for x in range(N):
        seen, st = set(), list(adj[x])
        while st:
            y = st.pop()
            if y not in seen: seen.add(y); st.extend(adj[y])
        R.append(seen)
    return R

def analyse(G):
    g = Gen(G); S, _ = g.run(G["start"]); N = G["N"]; r = measure(G); W = wclos(G)
    mvset = [set(y for y in range(N) if S[t][y] != S[t - 1][y]) for t in range(1, len(S))]
    out = []
    for x in range(N):
        we = sum(1 for m in mvset if m & W[x]); wm = sum(1 for y in W[x] if r["mv"][y] > 0); D = len(G["opts"][x]) - 1
        out.append(dict(x=x, lev=G["lev"][x], mv=r["mv"][x], kf=r["kf"][x], desc=r["desc"][x], W=len(W[x]), WM=wm, WE=we, D=D))
    return r["T"], out

if __name__ == "__main__":
    v = "-v" in sys.argv; tot = {"S": 0, "M": 0, "E": 0, "K": 0, "KFWE": 0}; files = 0; worst = {k: (-99, None) for k in "SMEK"}
    for f in [a for a in sys.argv[1:] if a != "-v"]:
        try: G = json.load(open(f)); assert "N" in G; T, out = analyse(G)
        except Exception: continue
        files += 1
        for o in out:
            for k, extra in (("S", o["W"]), ("M", o["WM"]), ("E", o["WE"]), ("K", o["kf"])):
                ex = o["mv"] - o["D"] * (1 + o["desc"] + extra)
                if ex > worst[k][0]: worst[k] = (ex, (os.path.basename(f), o["x"]))
                if ex > 0:
                    tot[k] += 1
                    if tot[k] <= 3: print(k, "VIOL", os.path.basename(f), o)
            if o["kf"] > o["WE"]: tot["KFWE"] += 1; print("KF>WE", os.path.basename(f), o)
        if v:
            print(os.path.basename(f), "T", T)
            for o in out: print("  ", o)
    print("files", files, "violations", tot, "worst excess", worst)
