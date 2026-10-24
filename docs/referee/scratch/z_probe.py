#!/usr/bin/env python3
"""REFEREE probe for packet P-N5-Z (docs/si/P-N5-Z-box5.md, pin fba7177). n5x.step read-only. Phase = (λ_Ξ, λ_U, τ) constant.
R excludes o (packet convention). Checks:
 ACT    every crossing transition inside a phase has an active entrant (i) / active leaver or o-free S-cycle inside R_k (ii)
 LOOP   with H1 at k inside a phase: no o-free (σ_{k+1}, τ)-cycle inside R_k containing a switched vertex
 NOFE   at fallbacks inside a phase: every switched edge y -> z, y in F_k, z in R̄_k, has y on o's W-play at k
 NOFLE  at fallbacks inside a phase with Ξ_k = W_k and H2 at k: no switched edge R_k -> F_k
 GAP    at fallbacks inside a phase with (h) at k: every switched R_k -> F_k edge has Ξ_k(σ_k y) ◁ Ξ_k(z) ⊴ W_k(σ_k y)
 WM     at non-fallback transitions inside a phase: W_{k+1} ⊵ W_k
 LV     per phase: X <= (n-1)(Z+1) + Z, with '±' crossings breaking runs
Usage: z_probe.py game.pg [start] | z_probe.py N nmin nmax seed [--randstart]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments/new/box25"))
from common import *
from thtrace import Rset
from wdrop_h import oncycle
from collections import Counter

def oplay(nxt, o):
    seen, x = [o], nxt[o]
    while x not in seen: seen.append(x); x = nxt[x]
    return set(seen)

def cycles_avoiding_o(nxt, o, within):
    out = []
    for v in within:
        seen, x = [], v
        while x not in seen and x != o: seen.append(x); x = nxt[x]
        if x != o: out.append(set(seen[seen.index(x):]))
    return out

def run(g, start, cnt):
    assert sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1) == 1, "not in C^1O: exactly one Odd choice vertex required"
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, start); rows = []; n = g.n
    while True:
        Xi, sb = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t)); _, W = wvals(g, s, t)
        Rb = set(Rset(g, s, t, o)); R = Rb - {o}
        nxt = [s[v] if g.owner[v] == 0 else t[v] for v in range(n)]
        rows.append(dict(s=tuple(s), t=tuple(t), Xi=Xi, W=W, Xk=tuple(E.key(x) for x in Xi), Wk=tuple(E.key(x) for x in W), R=R, Rb=Rb, nxt=nxt,
                         H1=not oncycle(g, s, sb, o), H2=not oncycle(g, s, t, o), H3=Xi[o][0] == W[o][0], fb=0,
                         ph=(tuple(x[0] for x in Xi), tuple(y[0] for y in U), tuple(t))))
        r = step(g, E, Ed, s, t)
        if r is None: break
        rows[-1]["fb"] = r[4]; s, t = list(r[0]), list(r[1])
    signs = []
    for k in range(len(rows) - 1):
        a, b = rows[k], rows[k + 1]
        if a["ph"] != b["ph"]:
            lv(signs, n, cnt); signs = []; continue
        S = [v for v in range(n) if g.owner[v] == 0 and a["s"][v] != b["s"][v]]
        F = set(range(n)) - a["Rb"]
        if b["R"] - a["R"]:
            cnt["ACTi_checks"] += 1
            if not any(v in F and b["nxt"][v] in a["Rb"] and v in b["R"] for v in S): cnt["ACTi_FAIL"] += 1
        if a["R"] - b["R"]:
            cnt["ACTii_checks"] += 1
            leaver = any(v in a["R"] and b["nxt"][v] in F and v not in b["R"] for v in S)
            loops = [C for C in cycles_avoiding_o(b["nxt"], o, a["R"]) if C <= a["R"] and set(S) & C]
            if not leaver and not loops: cnt["ACTii_FAIL"] += 1
            if loops and a["H1"]: cnt["LOOP_FAIL"] += 1
            if loops: cnt["ACTii_loop_case"] += 1
        if a["R"] != b["R"]:
            signs.append("+" if a["R"] < b["R"] else ("-" if b["R"] < a["R"] else "±"))
        if a["fb"]:
            cnt["fallbacks"] += 1; op = oplay(a["nxt"], o)
            for y in S:
                z = b["s"][y]
                if y in F and z in a["Rb"]:
                    cnt["NOFE_checks"] += 1
                    if y not in op: cnt["NOFE_FAIL"] += 1
                if y in a["R"] and z in F:
                    if a["Xk"] == a["Wk"] and a["H2"]: cnt["NOFLE_FAIL"] += 1
                    if a["H1"] and a["H2"] and a["H3"]:
                        cnt["GAP_checks"] += 1
                        sy = a["s"][y]
                        if not (a["Xk"][sy] < a["Xk"][z] <= a["Wk"][sy]): cnt["GAP_FAIL"] += 1
        else:
            cnt["WM_checks"] += 1
            if any(b["Wk"][v] < a["Wk"][v] for v in range(n)): cnt["WM_FAIL"] += 1
    lv(signs, n, cnt)

def lv(signs, n, cnt):
    if not signs: return
    X = len(signs); Z = 0; prev = None
    for sg in signs:
        if sg == "±": Z += 1
        else:
            if prev is not None and sg != prev: Z += 1
            prev = sg
    cnt["LV_phases"] += 1; cnt["LV_maxX"] = max(cnt["LV_maxX"], X); cnt["LV_maxZ"] = max(cnt["LV_maxZ"], Z)
    if X > (n - 1) * (Z + 1) + Z: cnt["LV_FAIL"] += 1

if __name__ == "__main__":
    a = sys.argv[1:]; cnt = Counter()
    if a[0].endswith(".pg"):
        g = load(a[0]); run(g, readstart(a[1]) if len(a) > 1 and not a[1].startswith("-") else None, cnt)
        print(a[0], "n", g.n, dict(sorted(cnt.items()))); sys.exit()
    N, lo, hi, seed = map(int, a[0:4]); RS = "--randstart" in a; rng = random.Random(seed)
    for _ in range(N):
        g = rand_c1o(rng, lo, hi, forced=0.1)
        if g is None: continue
        st = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
              {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
        cnt["runs"] += 1; run(g, st, cnt)
    print(dict(sorted(cnt.items())))
