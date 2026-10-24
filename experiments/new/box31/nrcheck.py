#!/usr/bin/env python3
"""Box 31 (b): runs outside route form. A run = maximal stretch of a phase with R, θ, w constant where NOT both frames are in route
form: U2 (honest frame not in route form), U3 (W frame not in route form; both = U23). Inside, W-flat runs (non-fallback, W unchanged
on R). Counts: switches; CASC-style violations with level := W-length (distance to the W cycle node); switches of the frame cycles
(C_Ξ = honest cycle through o for U2, C_W = W cycle through o for U3) inside W-flat runs; length of W-flat runs; w-changes under
¬H1 ∧ ¬H2 per interval (W-CYC) with fallbacks. Usage: nrcheck.py game.pg | --rand N lo hi seed"""
import sys, os, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box29"))
from otherx import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tbcheck import odd1

def cyc(g, s, t, o):
    seq = [o]; x = o
    while True:
        x = s[x] if g.owner[x] == 0 else t[x]
        if x == o: return set(seq)
        if x in seq: return set()
        seq.append(x)

def rows_nr(g, cap=10 ** 6):
    E, Ed = Engine(g), Engine(dual(g)); o = odd1(g); s, t = start_pair(g, E, Ed, None); rows = []
    while len(rows) < cap:
        Xi, sb = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t)); _, W = wvals(g, s, t)
        h1, h2 = not oncycle(g, s, sb, o), not oncycle(g, s, t, o)
        hon = list(t); hon[o] = sb[o]
        rows.append(dict(ph=(tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), R=reach_o(g, s, t, o), th=E.key(Xi[o]), w=E.key(W[o]),
                         rfX=h1 or Xi[o][0] == o, rfW=h2 or W[o][0] == o, h12=(h1, h2), CX=cyc(g, s, hon, o), CW=cyc(g, s, t, o),
                         Wk=[E.key(W[v]) for v in range(g.n)], Wl=[W[v][2] for v in range(g.n)], s=list(s), sbo=sb[o], fb=0))
        r = step(g, E, Ed, s, t)
        if r is None: break
        rows[-1]["fb"] = r[4]; s, t = r[0], r[1]
    return rows, o

def analyse(g, acc):
    rows, o = rows_nr(g); k = 0
    while k < len(rows):
        j = k
        while j + 1 < len(rows) and all(rows[j + 1][f] == rows[k][f] for f in ("ph", "R", "th", "w")): j += 1
        r0 = rows[k]
        if not (r0["rfX"] and r0["rfW"]) and j > k:
            kind = ("U2" if not r0["rfX"] else "") + ("U3" if not r0["rfW"] else ""); acc[kind + "_runs"] = acc.get(kind + "_runs", 0) + 1
            Rs = [v for v in r0["R"] if v != o]; i = k
            while i < j:
                if rows[i]["fb"] or any(rows[i]["Wk"][v] != rows[i + 1]["Wk"][v] for v in Rs): i += 1; continue
                a = i; c0 = i; per = {}
                while i < j and not rows[i]["fb"] and all(rows[i]["Wk"][v] == rows[i + 1]["Wk"][v] for v in Rs):
                    C = (rows[i]["CX"] if "U2" in kind else set()) | (rows[i]["CW"] if "U3" in kind else set())
                    if "U2" in kind and rows[i]["sbo"] != rows[i + 1]["sbo"]: acc["cyc_sw"] = acc.get("cyc_sw", 0) + 1
                    csw = "U2" in kind and rows[i]["sbo"] != rows[i + 1]["sbo"]
                    for v in Rs:
                        if g.owner[v] == 0 and rows[i]["s"][v] != rows[i + 1]["s"][v]:
                            acc["sw_" + kind] = acc.get("sw_" + kind, 0) + 1; per[v] = per.get(v, 0) + 1
                            if v in C: acc["cyc_sw"] = acc.get("cyc_sw", 0) + 1; csw = True; continue
                            if i - a > rows[i]["Wl"][v] - 2: acc["lvlviol_" + kind] = acc.get("lvlviol_" + kind, 0) + 1
                            if i - c0 > rows[i]["Wl"][v] - 2: acc["cascC_viol"] = acc.get("cascC_viol", 0) + 1; acc.setdefault("ex", (i, v))
                    i += 1
                    if csw: c0 = i
                acc["maxflat"] = max(acc.get("maxflat", 0), i - a); acc["maxper"] = max(acc.get("maxper", 0), max(per.values()) if per else 0)
        k = j + 1
    # W-CYC: per crossing-free interval with ¬H1 ∧ ¬H2: w-changes and fallbacks
    k = 0
    while k < len(rows):
        j = k
        while j + 1 < len(rows) and rows[j + 1]["ph"] == rows[k]["ph"] and rows[j + 1]["R"] == rows[k]["R"]: j += 1
        if rows[k]["h12"] == (False, False):
            wc = sum(rows[i]["w"] != rows[i + 1]["w"] for i in range(k, j)); fb = sum(rows[i]["fb"] for i in range(k, j)); n = g.n
            acc["wcyc_int"] = acc.get("wcyc_int", 0) + 1; acc["wcyc_max"] = max(acc.get("wcyc_max", 0), wc)
            if wc > (fb + 1) * n * n: acc["wcyc_viol"] = acc.get("wcyc_viol", 0) + 1
        k = j + 1

if __name__ == "__main__":
    acc = {}; a = sys.argv[1:]
    if a[0] == "--rand":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); d = 0
        while d < N:
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            analyse(g, acc); d += 1
    else: analyse(load(a[0]), acc)
    print("NR", acc)
