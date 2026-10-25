#!/usr/bin/env python3
"""Box 42 (2): Lemma WLAG check. Inside a phase, if k-1 -> k and k -> k+1 are both S4a steps (no fallback) and W_{k+1} != W_k, then
some Even y has z := σ_{k+1}(y) outside the arena H_{k-1}(y) = {σ_{k-1}(y)} ∪ gate_{k-1}(y), and Ξ_k(z) > Ξ_{k-1}(z) (strict).
Also: per event-free, fallback-free sub-run of an OTHER U3/U23 stretch, the R-changing transitions (Ξ, W or σ change on R) and the
changes of Ξ(c_w) (DATA for route R-KW). Usage: wlag.py --list FILE | --rand N lo hi seed [--randstart]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from nhcheck import *

def arena(E, g, s, Xi, y):
    kc = E.key(Xi[s[y]]); return {s[y]} | {z for z in g.succ[y] if E.key(Xi[z]) > kc}

def go(g, acc, tag, start=None):
    if sum(1 for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1) != 1: return
    rows, o, E = run_rows(g, start); acc["runs"] = acc.get("runs", 0) + 1
    vals = [E.evaluate(tuple(r["s"]))[0] for r in rows]
    for k in range(1, len(rows) - 1):
        if rows[k - 1]["ph"] != rows[k]["ph"] or rows[k]["ph"] != rows[k + 1]["ph"]: continue
        if rows[k - 1]["fb"] or rows[k]["fb"]: continue
        if rows[k]["Wk"] == rows[k + 1]["Wk"]: continue
        acc["wchg_after_s4a"] = acc.get("wchg_after_s4a", 0) + 1
        sp, s1 = rows[k - 1]["s"], rows[k + 1]["s"]; ok = False; inR = None
        for y in range(g.n):
            if g.owner[y] != 0: continue
            z = s1[y]
            if z in arena(E, g, sp, vals[k - 1], y): continue
            if E.key(vals[k][z]) > E.key(vals[k - 1][z]): ok = True; inR = z in rows[k]["R"]; break
        if not ok: acc["WLAG_viol"] = acc.get("WLAG_viol", 0) + 1; acc.setdefault("ex", (tag, k))
        else: acc["z_in_R" if inR else "z_in_F"] = acc.get("z_in_R" if inR else "z_in_F", 0) + 1
    # sub-runs
    a = 0
    for i in range(1, len(rows) + 1):
        if i == len(rows) or rows[i]["ph"] != rows[i - 1]["ph"]:
            x, y_ = a, i - 1; a = i; k = x
            while k < y_:
                j = k
                while j + 1 <= y_ and all(rows[j + 1][f] == rows[k][f] for f in ("R", "th", "w")): j += 1
                r0 = rows[k]
                if r0["other"] and cls(r0, o, E.rank) in ("U3", "U23"):
                    R = r0["R"]; cw = r0["cw"]; st = k
                    for t in range(k, j + 1):
                        end = t == j
                        if not end:
                            A0 = {v for v in R if v != o and cw in route(rows[t]["nxt"], v, o)}; A1 = {v for v in R if v != o and cw in route(rows[t + 1]["nxt"], v, o)}
                            sw = [v for v in R if g.owner[v] == 0 and rows[t]["s"][v] != rows[t + 1]["s"][v]]
                            end = rows[t]["fb"] or any(v == cw or ((v in A0) != (v in A1)) for v in sw)
                        if end:
                            sub = range(st, t)
                            rc = sum(any(rows[q]["Xk"][v] != rows[q + 1]["Xk"][v] or rows[q]["Wk"][v] != rows[q + 1]["Wk"][v] or rows[q]["s"][v] != rows[q + 1]["s"][v] for v in R) for q in sub)
                            cwc = sum(rows[q]["Xk"][cw] != rows[q + 1]["Xk"][cw] for q in sub)
                            acc["subruns"] = acc.get("subruns", 0) + 1
                            if rc > acc.get("max_rc", (0,))[0]: acc["max_rc"] = (rc, len(R), cwc, tag, st, t)
                            acc["max_cwchg"] = max(acc.get("max_cwchg", 0), cwc)
                            st = t + 1
                k = j + 1

if __name__ == "__main__":
    args = sys.argv[1:]; acc = {}; root = os.path.join(HERE, "..", "..", "..")
    if args[0] == "--rand":
        RS = "--randstart" in args; N, lo, hi, seed = map(int, args[1:5]); rng = random.Random(seed)
        for i in range(N):
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            st = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
            go(g, acc, ("rand", seed, i), st)
    else:
        for f in [l.strip() for l in open(args[1])]:
            p = f if os.path.exists(f) else os.path.join(root, f)
            try: g = load(p)
            except Exception: continue
            go(g, acc, f)
    print(acc)
