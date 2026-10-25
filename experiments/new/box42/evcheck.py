#!/usr/bin/env python3
"""Box 42 (2): Theorem E-HI checks on U3 / U23 stretches (¬H2, c_w ≠ o) with c_w ≻ c_θ. W-FLAT transition: non-fallback, W unchanged
at every vertex of R. KIND(v) = A iff c_w on π_v. Checks:
(DIR) at a W-flat transition no vertex changes kind against the honest preference (A -> B if c_w even, B -> A if c_w odd);
(KC)  kind-changing transitions ≤ (Q − 1) + |R|·Q, Q := K_S + f_S + 1;
(CB)  CASC-B: in a maximal W-flat segment with no kind change at all, a kind-B vertex switches only at segment step ≤ |π_v| − 2;
(CW)  c_w-switch transitions ≤ f_S + (deg(c_w) − 1)(1 + B + κ), B := transitions with a switch of a kind-B vertex, κ := kind-changing;
(ES)  event transitions ≤ κ + c_w-switch transitions (definition check).
Usage: evcheck.py --list FILE | --rand N lo hi seed [--randstart]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from kwfreeze import *

def go4(g, acc, tag, start=None):
    if sum(1 for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1) != 1: return
    rows, o, E = rows_raw(g, start); n = g.n; rk = E.rank; acc["runs"] = acc.get("runs", 0) + 1
    bad = lambda key, info: (acc.__setitem__(key, acc.get(key, 0) + 1), acc.setdefault("ex_" + key, (tag, info)))
    a = 0
    for i in range(1, len(rows) + 1):
        if not (i == len(rows) or rows[i]["ph"] != rows[i - 1]["ph"]): continue
        x, y_ = a, i - 1; a = i; k = x
        while k <= y_:
            j = k
            while j + 1 <= y_ and all(rows[j + 1][f] == rows[k][f] for f in ("R", "th", "w")): j += 1
            r0 = rows[k]; R = r0["R"]; Rv = [v for v in R if v != o]; ct, cw = r0["ct"], r0["cw"]
            if r0["h2"] or cw == o or rk[cw] <= rk[ct] or j == k: k = j + 1; continue
            even = E.par[cw] == 0; acc["stretches_" + ("even" if even else "odd")] = acc.get("stretches_" + ("even" if even else "odd"), 0) + 1
            kind = lambda q, v: cw in route(rows[q]["nxt"], v, o) or v == cw
            KS = fS = kc = Bsw = cws = ev = 0
            seg_start = None
            for q in range(k, j):
                fb = rows[q]["fb"]; fS += fb
                wch = any(rows[q]["W"][v] != rows[q + 1]["W"][v] for v in R)
                if not fb and wch: KS += 1
                ch = [(v, kind(q, v), kind(q + 1, v)) for v in Rv if kind(q, v) != kind(q + 1, v)]
                sw = [v for v in Rv if g.owner[v] == 0 and rows[q]["s"][v] != rows[q + 1]["s"][v]]
                if ch: kc += 1
                if any(not kind(q, v) for v in sw if v != cw): Bsw += 1
                if cw in sw: cws += 1
                if any(v == cw or kind(q, v) != kind(q + 1, v) for v in sw): ev += 1
                wflat = not fb and not wch
                if wflat:
                    for (v, k0, k1) in ch:
                        if (even and k0 and not k1) or ((not even) and (not k0) and k1): bad("DIR", (q, v))
                # CASC-B segments
                if wflat and not ch:
                    if seg_start is None: seg_start = q
                    for v in sw:
                        if v != cw and not kind(q, v):
                            if q - seg_start > len(route(rows[q]["nxt"], v, o)) - 2: bad("CB", (seg_start, q, v))
                else:
                    seg_start = None
            Q = KS + fS + 1
            if kc > (Q - 1) + len(R) * Q: bad("KC", (k, j, kc, Q))
            dcw = len(g.succ[cw])
            if cws > fS + (dcw - 1) * (1 + Bsw + kc): bad("CW", (k, j, cws))
            if ev > kc + cws: bad("ES", (k, j))
            acc["sum_kc"] = acc.get("sum_kc", 0) + kc; acc["sum_cws"] = acc.get("sum_cws", 0) + cws; acc["sum_ev"] = acc.get("sum_ev", 0) + ev
            acc["max_ev"] = max(acc.get("max_ev", 0), ev)
            k = j + 1

if __name__ == "__main__":
    args = sys.argv[1:]; acc = {}; root = os.path.join(HERE, "..", "..", "..")
    if args[0] == "--rand":
        RS = "--randstart" in args; N, lo, hi, seed = map(int, args[1:5]); rng = random.Random(seed)
        for i in range(N):
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            st = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
            go4(g, acc, ("rand", seed, i), st)
    else:
        for f in [l.strip() for l in open(args[1])]:
            p = f if os.path.exists(f) else os.path.join(root, f)
            try: g = load(p)
            except Exception: continue
            go4(g, acc, f)
    viol = {k: v for k, v in acc.items() if k in ("DIR", "KC", "CB", "CW", "ES")}
    print("violations:", viol if viol else 0); print({k: v for k, v in sorted(acc.items()) if not k.startswith("ex_") and k not in viol})
    for k, v in acc.items():
        if k.startswith("ex_"): print(k, v)
