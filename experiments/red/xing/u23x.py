#!/usr/bin/env python3
"""Box 35: independent check of P-N5-U23 (docs/new/P-N5-U23-box31.md, sha1 ee3e5d1e, trunk 7666336) EXACTLY as frozen, on 𝒞^1O.
Differences from L-NEW's experiments/new/box31/u23check.py (which is NOT edited): U23 stretches are checked too; CASC-U3 (iii) uses
the stated threshold 2|R| − 4 with o ∈ R (u23check uses 2|R|); CASC-U3 (ii) (kind A) is checked; both corollaries are checked.
Objects as in the packet §0: stretch = maximal run of a phase with R, θ, w constant (phase key and R = L-NEW's otherx/fbre
definitions, R plus o); W-flat run = maximal run of consecutive non-fallback transitions of a stretch with W unchanged on R;
π_v = v's (σ, τ)-path before its first visit of o; ℓ(v) = |π_v|; U2: ¬H1, c_θ ≠ o, W frame in route form (H2 or λ_W(o) = o);
U3: ¬H2, c_w ≠ o, honest frame in route form; U23: ¬H1, ¬H2, c_θ ≠ o, c_w ≠ o. Kind A: c_w ∈ π_v; event = a switch changing the
switcher's kind, or a switch of c_w. λ(v) = steps from v along its σ-path to c_w (kind A).
Checks: CASC-U2 (switch at run step > ℓ(v) − 2), CASC-U3 (i) (kind B, sub-run step > |π_v| − 2), (ii) (kind A, step > L_B + λ(v) − 3,
L_B = max |π| over kind B at that state; never allowed if λ = 1), (iii) (any R switch at sub-run step ≥ 2|R| − 4); corollaries:
U2: #transitions changing Ξ, W or σ on R ≤ f + K_W + (K_W + f + 1)(|R| − 2); U3/U23: ≤ f + K_W + E + (K_W + f + E + 1)(2|R| − 4).
Usage: u23x.py game.pg ... | u23x.py --climb mode seed secs out seed.pg   (mode: viol | u2 | kw | e | slack)"""
import sys, os, random, time
B = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "new"); sys.path.insert(0, os.path.join(B, "box29")); sys.path.insert(0, os.path.join(B, "box21"))
from otherx import *
from climb_fix import mutate

def route(nxt, v, o):
    p = []
    while v != o and v not in p: p.append(v); v = nxt[v]
    return p

def lam_to(nxt, v, c, o):
    k = 0; seen = set()
    while v != c and v not in seen and v != o: seen.add(v); v = nxt[v]; k += 1
    return k if v == c else None

def rows_x(g, cap=400):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, None); rows = []
    while len(rows) < cap:
        Xi, sb = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t)); _, W = wvals(g, s, t)
        h1, h2 = not oncycle(g, s, sb, o), not oncycle(g, s, t, o)
        rows.append(dict(ph=(tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), R=frozenset(reach_o(g, s, t, o)) | {o},
                         th=E.key(Xi[o]), w=E.key(W[o]), H1=h1, H2=h2, ct=Xi[o][0], cw=W[o][0], Xk=[E.key(Xi[v]) for v in range(g.n)],
                         Wk=[E.key(W[v]) for v in range(g.n)], s=list(s), nxt=[s[v] if g.owner[v] == 0 else t[v] for v in range(g.n)], fb=0))
        r = step(g, E, Ed, s, t)
        if r is None: break
        rows[-1]["fb"] = int(bool(r[4])); s, t = list(r[0]), list(r[1])
    return rows, o

def analyse(g):
    assert sum(1 for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1) == 1, "not one Odd choice vertex"
    rows, o = rows_x(g); A = dict(U2_st=0, U3_st=0, U23_st=0, U2_sw=0, U3_sw=0, U2_viol=0, U3i_viol=0, U3ii_viol=0, U3iii_viol=0,
                                  cor_viol=0, maxKW=0, maxE=0, maxf=0, maxchg=0, maxslack=-10 ** 9, ex=[])
    k = 0
    while k < len(rows):
        j = k
        while j + 1 < len(rows) and all(rows[j + 1][f] == rows[k][f] for f in ("ph", "R", "th", "w")): j += 1
        r0 = rows[k]; R = r0["R"]; Rs = sorted(R - {o}); kind = None
        rX = r0["H1"] or r0["ct"] == o; rW = r0["H2"] or r0["cw"] == o
        if not r0["H1"] and r0["ct"] != o and rW: kind = "U2"
        elif not r0["H2"] and r0["cw"] != o and rX: kind = "U3"
        elif not r0["H1"] and not r0["H2"] and r0["ct"] != o and r0["cw"] != o: kind = "U23"
        if kind and j > k:
            A[kind + "_st"] += 1; cw = r0["cw"]; f = KW = Ev = chg = 0; i = k
            for q in range(k, j):
                a, b = rows[q], rows[q + 1]
                if a["fb"]: f += 1
                elif any(a["Wk"][v] != b["Wk"][v] for v in R): KW += 1
                if any(a["Xk"][v] != b["Xk"][v] or a["Wk"][v] != b["Wk"][v] or a["s"][v] != b["s"][v] for v in R): chg += 1
            while i < j:
                if rows[i]["fb"] or any(rows[i]["Wk"][v] != rows[i + 1]["Wk"][v] for v in R): i += 1; continue
                a0 = i; c0 = i
                while i < j and not rows[i]["fb"] and all(rows[i]["Wk"][v] == rows[i + 1]["Wk"][v] for v in R):
                    a, b = rows[i], rows[i + 1]
                    pi = {v: route(a["nxt"], v, o) for v in Rs}
                    KA = {v for v in Rs if cw in pi[v]}; KA1 = {v for v in Rs if cw in route(b["nxt"], v, o)}
                    LB = max([len(pi[v]) for v in Rs if v not in KA] or [0]); evt = False
                    for v in Rs:
                        if g.owner[v] != 0 or a["s"][v] == b["s"][v]: continue
                        if kind == "U2":
                            A["U2_sw"] += 1
                            if i - a0 > len(pi[v]) - 2: A["U2_viol"] += 1; A["ex"].append(("U2", k, i, v, i - a0, len(pi[v])))
                            continue
                        A["U3_sw"] += 1
                        if v == cw or ((v in KA) != (v in KA1)): evt = True; continue
                        st = i - c0
                        if st >= 2 * len(R) - 4: A["U3iii_viol"] += 1; A["ex"].append(("U3iii", k, i, v, st, len(R)))
                        if v not in KA and st > len(pi[v]) - 2: A["U3i_viol"] += 1; A["ex"].append(("U3i", k, i, v, st, len(pi[v])))
                        if v in KA:
                            lv = lam_to(a["nxt"], v, cw, o)
                            if lv is not None and (lv == 1 or st > LB + lv - 3): A["U3ii_viol"] += 1; A["ex"].append(("U3ii", k, i, v, st, LB, lv))
                    i += 1
                    if evt: Ev += 1; c0 = i
            bound = f + KW + (KW + f + 1) * (len(R) - 2) if kind == "U2" else f + KW + Ev + (KW + f + Ev + 1) * (2 * len(R) - 4)
            if chg > bound: A["cor_viol"] += 1; A["ex"].append(("COR", kind, k, j, chg, bound))
            A["maxKW"] = max(A["maxKW"], KW); A["maxE"] = max(A["maxE"], Ev); A["maxf"] = max(A["maxf"], f); A["maxchg"] = max(A["maxchg"], chg)
            if chg > 0: A["maxslack"] = max(A["maxslack"], chg - bound)   # only stretches with a change (empty ones are trivially tight)
        k = j + 1
    A["ex"] = A["ex"][:5]; return A

def fitv(A, mode):
    v = A["U2_viol"] + A["U3i_viol"] + A["U3ii_viol"] + A["U3iii_viol"] + A["cor_viol"]
    return {"viol": (v, A["U2_sw"] + A["U3_sw"], A["maxslack"]), "u2": (v, A["U2_sw"], A["U2_st"]),
            "kw": (v, A["maxKW"], A["maxchg"]), "e": (v, A["maxE"], A["U3_sw"]), "slack": (v, A["maxslack"], A["U2_sw"] + A["U3_sw"])}[mode]

def fit(G, mode):
    BAD = (-10 ** 9,) * 3
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(G[2][v]) > 1]
    if len(odd) != 1 or any(not x for x in G[2]): return BAD, None
    try: A = analyse(pg.Game(*G))
    except Exception: return BAD, None
    return fitv(A, mode), A

if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "--climb":
        mode, seed, secs, out, sp = a[1], int(a[2]), float(a[3]), a[4], a[5]; rng = random.Random(seed)
        g = load(sp); G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f, c = fit(G, mode); print("START", f, c, flush=True)
        t0 = time.time(); it = 0
        while time.time() - t0 < secs:
            H = mutate(rng, G); it += 1; fh, ch = fit(H, mode)
            if fh >= f:
                if fh > f:
                    print(f"{time.time()-t0:7.0f}s it {it} fit {fh} {ch}", flush=True)
                    open(out + ".pg", "w").write(f"parity {g.n-1};\n" + "".join(f"{v} {H[0][v]} {H[1][v]} {','.join(map(str, H[2][v]))};\n" for v in range(g.n)))
                G, f = H, fh
        print("FINAL", f, it, flush=True)
    else:
        for p in a:
            try: print(os.path.basename(p), analyse(load(p)), flush=True)
            except AssertionError as e: print(os.path.basename(p), "SKIP", e)
