#!/usr/bin/env python3
"""Box 28 (CYC'): per (w, u*)-run (maximal run of consecutive states in one joint λ-phase with τ, w, u* fixed, θ ◁ w, (h) at every
state; u* = top of P(θ) Δ P(w) by Engine rank, or None): θ-changes, fallbacks, leaves by kind (arena / fallback), re-entries by the
kind of the vertex's last leave inside the run (ARE = after an S4a leave, XA's case; FBRE = after a fallback leave), first entries.
Usage: fbre.py game.pg [start]  |  fbre.py --rand N lo hi seed [--randstart]   (prints totals and the max FBRE per run)"""
import sys, os, random
from nhprof import *

def reach_o(g, s, t, o):
    nxt = [s[v] if g.owner[v] == 0 else t[v] for v in range(g.n)]; R = set()
    for v in range(g.n):
        x, seen = v, set()
        while x not in seen and x != o: seen.add(x); x = nxt[x]
        if x == o and v != o: R.add(v)
    return R

def runs_of(g, start=None):
    rows, ph = profile(g, start); E = Engine(g); o = odd_choice(g); out = []
    for r in rows:
        Xi, _ = E.evaluate(tuple(r["s"])); _, W = wvals(g, r["s"], r["t"])
        a, b = vset(E, Xi[o]), vset(E, W[o]); d = a[1] ^ b[1]
        r["u"] = max(d, key=lambda v: E.rank[v]) if d else None
        r["R"] = reach_o(g, r["s"], r["t"], o)
        r["thr"] = all(r["h"]) and r["th"] != r["w"]
    for (x, y) in ph:
        k = x
        while k <= y:
            if not rows[k]["thr"]: k += 1; continue
            j = k
            while j + 1 <= y and rows[j + 1]["thr"] and (rows[j + 1]["w"], rows[j + 1]["u"], rows[j + 1]["t"]) == (rows[j]["w"], rows[j]["u"], rows[j]["t"]): j += 1
            out.append((k, j, rows)); k = j + 1
    return out

def stats(k, j, rows):
    st = dict(states=(k, j), u=rows[k]["u"], tc=0, fb=0, leaveA=0, leaveF=0, ARE=0, FBRE=0, first=0)
    last, seen = {}, set(rows[k]["R"])
    for i in range(k, j):
        A, B = rows[i]["R"], rows[i + 1]["R"]; fb = rows[i]["fb"]
        st["tc"] += rows[i]["th"] != rows[i + 1]["th"]; st["fb"] += bool(fb)
        for v in A - B:
            last[v] = "F" if fb else "A"; st["leaveF" if fb else "leaveA"] += 1
        for v in B - A:
            if v not in seen: st["first"] += 1; seen.add(v)
            elif last.get(v) == "F": st["FBRE"] += 1
            else: st["ARE"] += 1
    return st

if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] != "--rand":
        g = load(a[0])
        for (k, j, rows) in runs_of(g, readstart(a[1]) if len(a) > 1 else None):
            if j > k: print(os.path.basename(a[0]), stats(k, j, rows))
        sys.exit()
    RS = "--randstart" in a; N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); tot = {}; mx = (0, None); mxf = (0, None); runs = nr = 0
    for i in range(N):
        g = rand_c1o(rng, lo, hi, forced=0.0)
        if g is None: continue
        start = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                 {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
        runs += 1
        for (k, j, rows) in runs_of(g, start):
            if j == k: continue
            s = stats(k, j, rows); nr += 1
            for key in ("tc", "fb", "leaveA", "leaveF", "ARE", "FBRE", "first"): tot[key] = tot.get(key, 0) + s[key]
            if s["FBRE"] > mx[0]: mx = (s["FBRE"], g.n)
            if s["fb"] > mxf[0]: mxf = (s["fb"], g.n)
    print(f"games {runs}, (w,u*)-runs with ≥ 1 transition {nr}, totals {tot}, max FBRE per run {mx}, max fallbacks per run {mxf}")
