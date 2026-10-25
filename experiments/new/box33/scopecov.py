#!/usr/bin/env python3
"""Box 33: which ε-transitions (O_k > E_k) and which θ-changes above the last fallback level lie in a CLS1 "case 2" interval of an L-SI
scope run (docs/si/P-N5-CLS-box8.md §0, §6): scope-run transitions j have (h) at j (H1, H2, c_θ = c_w), H2 at j+1, w_{j+1} = w_j; k0 =
the last fallback of the scope run before k; L = M_{k0}; case 2 = r_j := lev(θ_j, w_j) > L on [k0+1, k]. There Lemma NL (ii) gives no
leave at S4a steps, so EXIT-R holds. Also checks Lemma TC-SPLIT (docs/new/N5-K-box33.md §9): every θ-change at a phase transition has
level <= E_k or is an ε-transition with level O_k. Usage: scopecov.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box32"))
from dormant import *

def h2(nxt, o):
    seen = set(); u = nxt[o]
    while u not in seen:
        if u == o: return False
        seen.add(u); u = nxt[u]
    return True

def run(g, acc, name):
    rows, o = rows_w(g); E = Engine(g); ev = [E.evaluate(tuple(r["s"])) for r in rows]; n = g.n
    H2 = [h2(r["nxt"], o) for r in rows]
    hh = [r["h1"] and H2[i] and r["Xi"][o][0] == r["W"][o][0] for i, r in enumerate(rows)]
    insc = [rows[j]["ph"] == rows[j + 1]["ph"] and hh[j] and H2[j + 1] and rows[j]["w"] == rows[j + 1]["w"] for j in range(len(rows) - 1)]
    for k in range(len(rows) - 1):
        a, b = rows[k], rows[k + 1]
        if a["ph"] != b["ph"]: continue
        X0, X1 = ev[k][0], ev[k + 1][0]
        Ev = max([lev(X0[a["s"][y]], X0[b["s"][y]]) for y in range(n) if g.owner[y] == 0 and a["s"][y] != b["s"][y] and X0[y][0] != y] + [-2])
        sb0, sb1 = ev[k][1], ev[k + 1][1]
        Od = lev(X0[sb0[o]], X0[sb1[o]]) if sb0[o] != sb1[o] and X0[o][0] != o else -2
        if X0[o] != X1[o]:
            tl = lev(X0[o], X1[o]); acc["theta_changes"] = acc.get("theta_changes", 0) + 1
            if not (tl <= Ev or (Od > Ev and tl == Od)): acc["TCSPLIT_FAIL"] = acc.get("TCSPLIT_FAIL", 0) + 1; acc.setdefault("ex_TCSPLIT", (name, k, tl, Ev, Od))
            acc["theta_" + ("eps" if Od > Ev else "even")] = acc.get("theta_" + ("eps" if Od > Ev else "even"), 0) + 1
        if not (Od > Ev): continue
        if not insc[k]: cat = "not_in_scope_run"
        else:
            j = k
            while j - 1 >= 0 and insc[j - 1]: j -= 1
            fbs = [i for i in range(j, k) if rows[i]["fb"]]
            if not fbs: cat = "scope_no_prior_fb"
            else:
                k0 = fbs[-1]; L = rows[k0]["M"]
                cat = "scope_case2_NL" if all(lev(rows[i]["Xi"][o], rows[i]["W"][o]) > L for i in range(k0 + 1, k + 1)) else "scope_r<=L"
        sn = b["cw"] == X0[o][0]
        acc[f"eps_{'SN' if sn else 'notSN'}_{cat}"] = acc.get(f"eps_{'SN' if sn else 'notSN'}_{cat}", 0) + 1

if __name__ == "__main__":
    acc = {}
    for f in sys.argv[1:]:
        g = load(f)
        if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) != 1: continue
        run(g, acc, os.path.basename(f))
    for k in sorted(acc): print(k, acc[k])
