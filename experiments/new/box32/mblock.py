#!/usr/bin/env python3
"""Box 32: coarse freeze at L-SI's gate level M (RESULTS R25) for the open cores (E), (K_W) of (NH') (docs/new/N5-U23-box31.md §3).
Per phase: M_k = max gate level at k (R25), tame_k iff COARSE_{M_k}(Ξ) unchanged. An M-BLOCK = maximal run of consecutive tame
transitions of a phase with M constant. For every transition inside a U2 / U3 / U23 stretch (classes KW, EV, FLAT as tamecheck.py),
record: tame?, M-drop at it?, and the level of each W-change on R relative to M_k (lev(W_k(v), W_{k+1}(v)) <= M_k ?), likewise for Ξ.
Counts per M-block: KW, EV transitions, against |R|. Usage: mblock.py game.pg ... | --rand N lo hi seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "si", "coarse"))
sys.path.insert(0, os.path.join(HERE, "..", "box31"))
from mono import lev, coarse
from u23check import *

def rows_w(g):
    E, Ed = Engine(g), Engine(dual(g)); o = odd1(g); s, t = start_pair(g, E, Ed, None); rows = []
    while True:
        Xi, sb = E.evaluate(tuple(s)); _, W = wvals(g, s, t); Is = E.improving(tuple(s), Xi)
        h1, h2 = not oncycle(g, s, sb, o), not oncycle(g, s, t, o); U, _ = Ed.evaluate(tuple(t))
        M = max([lev(Xi[s[y]], Xi[z]) for y, z in Is]) if Is else -3
        rows.append(dict(ph=(tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), R=reach_o(g, s, t, o), th=E.key(Xi[o]),
                         w=E.key(W[o]), h1=h1, rfX=h1 or Xi[o][0] == o, rfW=h2 or W[o][0] == o, cw=W[o][0], Xi=Xi, W=W, M=M, s=list(s),
                         nxt=[s[v] if g.owner[v] == 0 else t[v] for v in range(g.n)], fb=0))
        r = step(g, E, Ed, s, t)
        if r is None: break
        rows[-1]["fb"] = r[4]; s, t = r[0], r[1]
    return rows, o

def analyse(g, acc, name=""):
    rows, o = rows_w(g); n = g.n; E = Engine(g)
    tame = [all(coarse(rows[i + 1]["Xi"][v], rows[i]["M"]) == coarse(rows[i]["Xi"][v], rows[i]["M"]) for v in range(n))
            for i in range(len(rows) - 1)]
    blk = [0] * max(1, len(rows) - 1); b = 0
    for i in range(len(rows) - 1):
        if i and not (tame[i] and tame[i - 1] and rows[i]["M"] == rows[i - 1]["M"] and rows[i]["ph"] == rows[i - 1]["ph"]): b += 1
        blk[i] = b
    per = {}
    k = 0
    while k < len(rows):
        j = k
        while j + 1 < len(rows) and all(rows[j + 1][f] == rows[k][f] for f in ("ph", "R", "th", "w")): j += 1
        r0 = rows[k]; kind = "U2" if (not r0["rfX"] and r0["rfW"]) else ("U3" if (r0["rfX"] and not r0["rfW"]) else ("U23" if not r0["rfX"] else None))
        if kind:
            Rs = [v for v in r0["R"] if v != o]; cw = r0["cw"]
            for i in range(k, j):
                a, c = rows[i], rows[i + 1]
                if a["fb"]: continue
                wch = [v for v in Rs if E_key(a["W"][v]) != E_key(c["W"][v])]
                sw = [v for v in Rs if g.owner[v] == 0 and a["s"][v] != c["s"][v]]
                if wch: cl = "KW"
                elif sw:
                    ev = kind != "U2" and any(v == cw or ((cw in route(a["nxt"], v, o)) != (cw in route(c["nxt"], v, o))) for v in sw)
                    cl = "EV" if ev else "FLAT"
                else: continue
                M = a["M"]; key = f"{kind}_{cl}"
                xch = any(a["Xi"][v] != c["Xi"][v] for v in range(n)); acc[key + ("_Xichg" if xch else "_XiFLAT")] = acc.get(key + ("_Xichg" if xch else "_XiFLAT"), 0) + 1
                hM = acc.setdefault(key + "_Mhist", {}); hM[M] = hM.get(M, 0) + 1
                ct = E.rank[a["Xi"][o][0]]; cwr = E.rank[cw]
                for v in wch:
                    L = lev(a["W"][v], c["W"][v]); tag = "vis" if L <= M else ("hidden<cθ" if L < ct else "ABOVE_BOTH")
                    acc[key + "_" + tag] = acc.get(key + "_" + tag, 0) + 1
                acc[key] = acc.get(key, 0) + 1
                if not tame[i]: acc[key + "_nontame"] = acc.get(key + "_nontame", 0) + 1
                if c["M"] < M: acc[key + "_Mdrop"] = acc.get(key + "_Mdrop", 0) + 1
                for v in wch:
                    L = lev(a["W"][v], c["W"][v]); t2 = "Wbelow" if L <= M else "WABOVE"
                    acc[key + "_" + t2] = acc.get(key + "_" + t2, 0) + 1
                    if L > M: acc.setdefault("ex_WABOVE", (name, i, v, L, M))
                pb = per.setdefault((blk[i], kind), dict(KW=0, EV=0, FLAT=0, R=len(Rs) + 1, vc={}))
                pb[cl] += 1
                for v in wch: pb["vc"][v] = pb["vc"].get(v, 0) + 1
        k = j + 1
    for (bb, kind), pb in per.items():
        for cl in ("KW", "EV"):
            if pb[cl] > acc.get(f"max_{kind}_{cl}_perblock", (0,))[0]: acc[f"max_{kind}_{cl}_perblock"] = (pb[cl], pb["R"], name)
        mv = max(pb["vc"].values()) if pb["vc"] else 0
        if mv > acc.get(f"max_{kind}_Wchanges_per_vertex_block", (0,))[0]: acc[f"max_{kind}_Wchanges_per_vertex_block"] = (mv, pb["R"], name, bb)

def E_key(x): return x

if __name__ == "__main__":
    acc = {}; a = sys.argv[1:]
    if a[0] == "--rand":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); d = 0
        while d < N:
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            analyse(g, acc, f"rand{d}"); d += 1
    else:
        for f in a:
            g = load(f)
            if len([v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1]) != 1: continue
            analyse(g, acc, os.path.basename(f))
    for k in sorted(acc): print(k, acc[k])
