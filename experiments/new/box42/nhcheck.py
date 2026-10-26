#!/usr/bin/env python3
"""Box 42 (P-N5-NH-box42): checks every intermediate inequality of Theorem NH on N5 runs (𝒞^1O, one Odd choice vertex asserted).
Per phase ((λ_Ξ, λ_U, τ(o)) constant): crossing-free intervals I, stretches S (R, θ, w constant), OTHER (= (h) fails, Ξ ≠ W).
Checks: (ST) OTHER status constant on each stretch; (CL) class of an OTHER stretch (P3'/U1/U2/U3/U23) and c_θ ≠ c_w in route form;
(TH) θ-changes per I ≤ n − 1, ⊆ F-changes under H1; (WC) w-changes ⊆ F-changes under H2, ≤ (f^O_I + 1)(|R|² − 1) + f^O_I under ¬H2;
(NR) Ξ-changes on R per OTHER stretch ≤ the class bound; (OB) O ≤ the assembled bound and O ≤ 11n⁷(1 + X + f^O) + 8n³(K_W + E);
(SW) a Ξ- or W-change on R inside an OTHER stretch has an Even σ-switch in R; (TX) T ≤ 156 n¹¹(1 + X + f^O) + 104 n⁷(K_W + E). R includes o (R22 convention).
Usage: nhcheck.py file.pg ... | nhcheck.py --list FILE | nhcheck.py --rand N lo hi seed [--randstart]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "box28"))
from fbre import *   # profile (box28/nhprof), reach_o, Engine, dual, load, odd_choice, rand_c1o, wvals, step, start_pair

def route(nxt, v, o):
    p = []
    while v != o and v not in p: p.append(v); v = nxt[v]
    return p

def run_rows(g, start=None):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, start); rows = []
    while True:
        Xi, sb = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t)); _, W = wvals(g, s, t)
        h1, h2 = not oncycle(g, s, sb, o), not oncycle(g, s, t, o); h3 = Xi[o][0] == W[o][0]
        Xk = tuple(E.key(Xi[v]) for v in range(g.n)); Wk = tuple(E.key(W[v]) for v in range(g.n))
        R = frozenset(reach_o(g, s, t, o)) | {o}
        rows.append(dict(ph=(tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), h1=h1, h2=h2, other=(not (h1 and h2 and h3)) and Xk != Wk,
                         R=R, th=Xk[o], w=Wk[o], ct=Xi[o][0], cw=W[o][0], Xk=Xk, Wk=Wk, s=tuple(s),
                         nxt=[s[v] if g.owner[v] == 0 else t[v] for v in range(g.n)], fb=0))
        r = step(g, E, Ed, s, t)
        if r is None: break
        rows[-1]["fb"] = 1 if r[4] else 0; s, t = r[0], r[1]
    return rows, o, E

def cls(r, o, rank):
    rfX = r["h1"] or r["ct"] == o; rfW = r["h2"] or r["cw"] == o
    if rfX and rfW:
        if r["ct"] == r["cw"]: return "SAME"
        return "P3" if rank[r["ct"]] > rank[r["cw"]] else "U1"
    if not rfX and rfW: return "U2"
    if rfX and not rfW: return "U3"
    return "U23"

def check_phase(g, rows, o, E, x, y, acc, tag):
    n = g.n; rank = E.rank; D = 4 * n * (n - 1) + 1
    bad = lambda key, info: (acc.__setitem__(key, acc.get(key, 0) + 1), acc.setdefault("ex_" + key, (tag, info)))
    T = y - x; X = sum(rows[k]["R"] != rows[k + 1]["R"] for k in range(x, y))
    O = sum(rows[k]["other"] or rows[k + 1]["other"] for k in range(x, y))
    fO = sum(rows[k]["fb"] and rows[k]["other"] for k in range(x, y))
    # crossing-free intervals
    ivs, a = [], x
    for k in range(x, y):
        if rows[k]["R"] != rows[k + 1]["R"]: ivs.append((a, k)); a = k + 1
    ivs.append((a, y))
    KW = EV = 0; sumN = 0; sumF = 0; nstO = 0; sumNR = 0
    for (a, b) in ivs:
        R = rows[a]["R"]; F = [v for v in range(n) if v not in R]; r0 = rows[a]
        Fch = [k for k in range(a, b) if any(rows[k]["Xk"][v] != rows[k + 1]["Xk"][v] for v in F)]
        if len(Fch) > max(0, len(F) - 1): bad("F1deg", (a, b))
        sumF += max(0, len(F) - 1)
        thc = [k for k in range(a, b) if rows[k]["th"] != rows[k + 1]["th"]]; wc = [k for k in range(a, b) if rows[k]["w"] != rows[k + 1]["w"]]
        fOI = sum(rows[k]["fb"] and rows[k]["other"] for k in range(a, b))
        if len(thc) > n - 1: bad("TH", (a, b, len(thc)))
        if r0["h1"] and not set(thc) <= set(Fch): bad("TH_H1", (a, b))
        if r0["h2"] and not set(wc) <= set(Fch): bad("W_H2", (a, b))
        if not r0["h2"] and len(wc) > (fOI + 1) * (len(R) ** 2 - 1) + fOI: bad("WC", (a, b, len(wc), fOI))
        if any(rows[k]["h1"] != r0["h1"] or rows[k]["h2"] != r0["h2"] for k in range(a, b + 1)): bad("TCi", (a, b))
        if 1 + len(thc) + len(wc) > n - 1 + (fOI + 1) * n * n: bad("SI", (a, b))
        sumN += 1 + len(thc) + len(wc)
        # stretches
        k = a
        while k <= b:
            j = k
            while j + 1 <= b and rows[j + 1]["th"] == rows[k]["th"] and rows[j + 1]["w"] == rows[k]["w"]: j += 1
            if len({rows[i]["other"] for i in range(k, j + 1)}) > 1: bad("ST", (k, j))
            if rows[k]["other"]:
                nstO += 1; c = cls(rows[k], o, rank); acc["cls_" + c] = acc.get("cls_" + c, 0) + 1
                if c == "SAME": bad("CL_same", (k, j))
                Rl = len(R); fS = sum(rows[i]["fb"] for i in range(k, j))
                NR = sum(any(rows[i]["Xk"][v] != rows[i + 1]["Xk"][v] for v in R) for i in range(k, j))
                KS = sum((not rows[i]["fb"]) and any(rows[i]["Wk"][v] != rows[i + 1]["Wk"][v] for v in R) for i in range(k, j))
                ES = 0
                if c in ("U3", "U23"):
                    cw = rows[k]["cw"]
                    for i in range(k, j):
                        A0 = {v for v in R if v != o and cw in route(rows[i]["nxt"], v, o)}; A1 = {v for v in R if v != o and cw in route(rows[i + 1]["nxt"], v, o)}
                        sw = [v for v in R if g.owner[v] == 0 and rows[i]["s"][v] != rows[i + 1]["s"][v]]
                        if any(v == cw or ((v in A0) != (v in A1)) for v in sw): ES += 1
                if c in ("U2", "U3", "U23"): KW += KS
                EV += ES
                if c == "P3": bd = (n + 1) * Rl
                elif c == "U1":
                    K = (fS + 1) * (Rl - 1) * (Rl - 2); bd = Rl + fS + K + (K + fS + 1) * (Rl - 2)
                elif c == "U2": bd = fS + KS + (KS + fS + 1) * (Rl - 2)
                elif c in ("U3", "U23"): bd = fS + KS + ES + (KS + fS + ES + 1) * (2 * Rl - 4)
                else: bd = 0
                if NR > max(bd, 0): bad("NR_" + c, (k, j, NR, bd))
                if NR > n ** 3 * (1 + fS) + 2 * n * (KS + ES): bad("NRcrude", (k, j))
                for i in range(k, j):
                    if any(rows[i]["Xk"][v] != rows[i + 1]["Xk"][v] or rows[i]["Wk"][v] != rows[i + 1]["Wk"][v] for v in R) and \
                       not any(g.owner[v] == 0 and rows[i]["s"][v] != rows[i + 1]["s"][v] for v in R): bad("SW", (k, i))
                acc["maxNR_" + c] = max(acc.get("maxNR_" + c, 0), NR); sumNR += NR
                acc["stretch_T_max"] = max(acc.get("stretch_T_max", 0), j - k)
                if j - k > (sum(any(rows[i]["Xk"][v] != rows[i + 1]["Xk"][v] for v in range(n)) for i in range(k, j)) + 1) * D: bad("R15d", (k, j))
            k = j + 1
    asm = X + sumN + D * (n * (X + 1) + (n ** 3 + 1) * sumN + n ** 3 * fO + 2 * n * (KW + EV))
    if O > asm: bad("OB_asm", (x, y, O, asm))
    if O > 11 * n ** 7 * (1 + X + fO) + 8 * n ** 3 * (KW + EV): bad("OB", (x, y))
    if T > 156 * n ** 11 * (1 + X + fO) + 104 * n ** 7 * (KW + EV): bad("TX", (x, y))
    if sumN > n * n * (2 * X + 2 + fO): bad("Nst", (x, y))
    for key, val in (("O", O), ("X", X), ("fO", fO), ("KW", KW), ("E", EV), ("T", T)):
        acc["max_" + key] = max(acc.get("max_" + key, 0), val)
    acc["phases"] = acc.get("phases", 0) + 1; acc["phases_O>0"] = acc.get("phases_O>0", 0) + (O > 0)
    acc["sum_O"] = acc.get("sum_O", 0) + O; acc["sum_fO"] = acc.get("sum_fO", 0) + fO; acc["sum_KW"] = acc.get("sum_KW", 0) + KW; acc["sum_E"] = acc.get("sum_E", 0) + EV

def analyse(g, acc, tag, start=None):
    if sum(1 for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1) != 1: acc["skipped"] = acc.get("skipped", 0) + 1; return
    rows, o, E = run_rows(g, start); acc["runs"] = acc.get("runs", 0) + 1
    a = 0
    for i in range(1, len(rows) + 1):
        if i == len(rows) or rows[i]["ph"] != rows[i - 1]["ph"]:
            check_phase(g, rows, o, E, a, i - 1, acc, tag); a = i

if __name__ == "__main__":
    args = sys.argv[1:]; acc = {}
    if args and args[0] == "--rand":
        RS = "--randstart" in args; N, lo, hi, seed = map(int, args[1:5]); rng = random.Random(seed)
        for i in range(N):
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            st = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                  {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
            analyse(g, acc, ("rand", seed, i), st)
    else:
        files = [l.strip() for l in open(args[1])] if args and args[0] == "--list" else args
        root = os.path.join(HERE, "..", "..", "..")
        for f in files:
            p = f if os.path.exists(f) else os.path.join(root, f)
            try: g = load(p)
            except Exception as e: acc["loadfail"] = acc.get("loadfail", 0) + 1; continue
            analyse(g, acc, os.path.basename(f))
    viol = {k: v for k, v in acc.items() if not k.startswith(("ex_", "max", "cls_", "sum_", "phases", "runs", "skipped", "loadfail", "stretch"))}
    print("violations:", viol if viol else 0)
    print({k: v for k, v in sorted(acc.items()) if not k.startswith("ex_") and k not in viol})
    for k, v in acc.items():
        if k.startswith("ex_"): print(k, v)
