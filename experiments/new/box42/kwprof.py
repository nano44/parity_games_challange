#!/usr/bin/env python3
"""Box 42 (2): profile of K_W and E transitions in OTHER stretches of class U2/U3/U23 (P-N5-NH-box42 §0 definitions).
For each K_W transition k -> k+1 (non-fallback, W changes on R, inside an OTHER U2/U3/U23 stretch): is k-1 -> k an S4a step of the same
stretch (then σ_k is the arena optimum of H_{k-1}); the W_k-improving edges (y, z) of H_k (gate at k) that were not in H_{k-1}; why
each entered the gate: Ξ(z) rose (z in R / F), σ(y) changed, or Ξ(σ_k y) fell; y in R or F; the band: c_w more relevant than every R
vertex (length-only) or not. Usage: kwprof.py --list FILE | files..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from nhcheck import *

def gate(E, g, s, Xi, y, z):
    return E.key(Xi[z]) > E.key(Xi[s[y]])

def prof(g, acc, tag):
    if sum(1 for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1) != 1: return
    rows, o, E = run_rows(g); Ed = Engine(dual(g))
    # recompute full valuations for gate tests
    vals = []
    for r in rows:
        Xi, _ = E.evaluate(tuple(r["s"])); vals.append(Xi)
    t = [None] * len(rows)
    for i in range(len(rows)): t[i] = [rows[i]["nxt"][v] for v in range(g.n)]
    a = 0; phases = []
    for i in range(1, len(rows) + 1):
        if i == len(rows) or rows[i]["ph"] != rows[i - 1]["ph"]: phases.append((a, i - 1)); a = i
    for (x, y_) in phases:
        k = x; KWp = 0; Ep = 0
        while k < y_:
            j = k
            while j + 1 <= y_ and rows[j + 1]["R"] == rows[k]["R"] and rows[j + 1]["th"] == rows[k]["th"] and rows[j + 1]["w"] == rows[k]["w"]: j += 1
            r0 = rows[k]
            if r0["other"]:
                c = cls(r0, o, E.rank)
                if c in ("U2", "U3", "U23"):
                    R = r0["R"]; cw = r0["cw"]; band = all(E.rank[cw] > E.rank[v] for v in R if v != cw)
                    for i in range(k, j):
                        if rows[i]["fb"] or not any(rows[i]["Wk"][v] != rows[i + 1]["Wk"][v] for v in R): continue
                        KWp += 1; key = (c, "LEN" if band else "SET")
                        acc[key] = acc.get(key, 0) + 1
                        prev_s4a = i > k and not rows[i - 1]["fb"]
                        if not prev_s4a: acc["kw_first_or_afterfb"] = acc.get("kw_first_or_afterfb", 0) + 1; continue
                        # W_i-improving edges in gate at i not gate at i-1
                        Wk = rows[i]["Wk"]; s = rows[i]["s"]; sp = rows[i - 1]["s"]; Xi, Xp = vals[i], vals[i - 1]
                        new = []
                        for yv in range(g.n):
                            if g.owner[yv] != 0: continue
                            for z in g.succ[yv]:
                                if z == s[yv] or not gate(E, g, s, Xi, yv, z): continue
                                if Wk[z] <= Wk[s[yv]]: continue
                                if z == sp[yv] or gate(E, g, sp, Xp, yv, z): continue
                                why = []
                                if E.key(Xi[z]) != E.key(Xp[z]): why.append("Xz_up_" + ("R" if z in R else "F"))
                                if s[yv] != sp[yv]: why.append("sig_y")
                                elif E.key(Xi[s[yv]]) != E.key(Xp[s[yv]]): why.append("Xsy_chg")
                                new.append((yv in R, tuple(why)))
                        if not new: acc["kw_no_new_gate"] = acc.get("kw_no_new_gate", 0) + 1; acc.setdefault("ex_nonew", (tag, i))
                        for (inR, why) in new:
                            kk = ("new", "yR" if inR else "yF") + why; acc[kk] = acc.get(kk, 0) + 1
                    if c in ("U3", "U23"):
                        for i in range(k, j):
                            A0 = {v for v in R if v != o and cw in route(rows[i]["nxt"], v, o)}; A1 = {v for v in R if v != o and cw in route(rows[i + 1]["nxt"], v, o)}
                            sw = [v for v in R if g.owner[v] == 0 and rows[i]["s"][v] != rows[i + 1]["s"][v]]
                            if any(v == cw for v in sw): acc["ev_cw"] = acc.get("ev_cw", 0) + 1; Ep += 1
                            elif any((v in A0) != (v in A1) for v in sw): acc["ev_kind"] = acc.get("ev_kind", 0) + 1; Ep += 1
            k = j + 1
        if KWp + Ep > acc.get("best", (0,))[0]: acc["best"] = (KWp + Ep, KWp, Ep, tag, g.n, x, y_)
        acc.setdefault("top", []).append((KWp, Ep, tag, g.n))

if __name__ == "__main__":
    args = sys.argv[1:]; acc = {}; root = os.path.join(HERE, "..", "..", "..")
    files = [l.strip() for l in open(args[1])] if args[0] == "--list" else args
    for f in files:
        p = f if os.path.exists(f) else os.path.join(root, f)
        try: g = load(p)
        except Exception: continue
        prof(g, acc, f)
    top = sorted(acc.pop("top", []), reverse=True)[:12]
    for k, v in sorted(acc.items(), key=lambda kv: str(kv[0])): print(k, v)
    print("top phases (K_W, E, file, n):"); [print(" ", t) for t in top]
