#!/usr/bin/env python3
"""Box 33: O-rises (rises k < k' of the used level, no fallback in [k, k'], L_{k'} attained by σ̄(o)) and Lemma OR (docs/new/N5-K-box33.md):
at each O-rise, check (i) x0 := σ̄_{k'}(o) has its H_{k'+1}-path through o and x0 ∈ R_{k'+1}; under H1 at k', x0 ∈ F_{k'} (a crossing);
(ii) lev(θ_{k'}, θ_{k'+1}) = L_{k'} and θ rises. Per phase: O-rises, d_o, exit joins / leaves of R. Usage: orise2.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box32"))
from dormant import *

def hpath_visits_o(nxt, v, o, c):
    seen = set(); u = v
    while u not in seen:
        if u == c: return False
        if u == o: return True
        seen.add(u); u = nxt[u]
    return False

def run(g, acc, name):
    rows, o = rows_w(g); E = Engine(g); ev = [E.evaluate(tuple(r["s"])) for r in rows]; n = g.n; so = sorted(set(g.succ[o]))
    Ls = [relL(g, ev, rows, k) if rows[k]["ph"] == rows[k + 1]["ph"] else None for k in range(len(rows) - 1)]
    prev = None; cnt = 0; ej = el = 0
    def flush():
        nonlocal cnt, ej, el
        if cnt > acc.get("max_orise", (0,))[0]: acc["max_orise"] = (cnt, dict(n=n, d_o=len(so), exit_joins=ej, exit_leaves=el), name)
        cnt = ej = el = 0
    for k in range(len(Ls)):
        if Ls[k] is None: prev = None; flush(); continue
        R0, R1 = set(rows[k]["R"]) | {o}, set(rows[k + 1]["R"]) | {o}
        ej += sum(1 for x in so if x not in R0 and x in R1); el += sum(1 for x in so if x in R0 and x not in R1)
        if Ls[k] == -2: continue
        if prev is not None and Ls[k] > Ls[prev] and not any(rows[j]["fb"] for j in range(prev, k + 1)):
            X0, X1, sb0, sb1 = ev[k][0], ev[k + 1][0], ev[k][1], ev[k + 1][1]
            if sb0[o] != sb1[o] and X0[o][0] != o and lev(X0[sb0[o]], X0[sb1[o]]) == Ls[k]:
                cnt += 1; acc["orise"] = acc.get("orise", 0) + 1; x0 = sb0[o]; c = X0[o][0]
                nxt1 = [rows[k + 1]["s"][v] if g.owner[v] == 0 else sb1[v] for v in range(n)]
                if not hpath_visits_o(nxt1, x0, o, c): acc["OR_i_path_FAIL"] = acc.get("OR_i_path_FAIL", 0) + 1
                if x0 not in R1: acc["OR_i_R_FAIL"] = acc.get("OR_i_R_FAIL", 0) + 1
                if rows[k]["h1"] and x0 in R0: acc["OR_i_F_FAIL"] = acc.get("OR_i_F_FAIL", 0) + 1
                if lev(X0[o], X1[o]) != Ls[k] or E.key(X1[o]) <= E.key(X0[o]): acc["OR_ii_FAIL"] = acc.get("OR_ii_FAIL", 0) + 1
                acc["orise_" + ("H1" if rows[k]["h1"] else "nH1")] = acc.get("orise_" + ("H1" if rows[k]["h1"] else "nH1"), 0) + 1
        prev = k
    flush()

if __name__ == "__main__":
    acc = {}
    for f in sys.argv[1:]:
        g = load(f)
        if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) != 1: continue
        try: run(g, acc, os.path.basename(f))
        except Exception as e: acc["ERR"] = acc.get("ERR", 0) + 1; acc.setdefault("ex_ERR", (f, repr(e)))
    for k in sorted(acc): print(k, acc[k])
