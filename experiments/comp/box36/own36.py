#!/usr/bin/env python3
"""L-COMP box 36 (successor 15): per-gate flip census on own34's N5'-xi-on-Gamma3 run (third engine for K1-FLIP data).
Engine: own34.run (L-COMP's independent engine, box 34; Gamma3 from R104 + P-N5-REACH §3, n5b SPEC + [N5XI]), states 0..T3 up to the
first fallback. Definitions, written from L-NEW box 202 TEXT (docs/new/N5-XIFVS-box202.md §0-§2 at claude/l-new fa17fdf6):
  - k(G) = minimum feedback vertex set of the Xi-graph (vertices = movers; edge x -> xt for every option with xt >= 0; self-loops
    count). MY code: brute force over mover subsets by size 0..KCAP (default 3), «>KCAP» above.
  - sigma-bar_t = Odd's choice in the SPEC evaluation of sigma_t (n5b SpecSI.evaluate_choice: SPEC S1 (iv)/(v) rules).
  - flips(g) = #t in 1..T3 with sigma-bar_(t-1)(g) != sigma-bar_t(g), g a gate (Odd, successors pe_g, pB_g).
  - lamch(g) = #t in 1..T3 with Lambda_(t-1) != Lambda_t at pe_g or at pB_g (Lambda = first component of the sigma_t valuation).
  - ratio(g) = flips(g) / (lamch(g) + 1); kfx = max_g flips(g) - 2(lamch(g) + 1) (CONJECTURE K1-FLIP(2) margin; > 0 = violation).
  - F = #t with some gate flip; R = box 200's returns: max over (u, b, Lambda) of #t at which u (|succ| >= 2) changes its edge to b
    (sigma_t for Even u, sigma-bar_t for Odd u) while Lambda_t(u) = Lambda_(t-1)(u); C = own34 counter C (max c_y over (v, I)).
Usage: own36.py G.json [...] [--noelev] [--nocounters]   -> one line per genome."""
import sys, os, json, itertools, collections
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, "..", "box34"))
import own34
from n5b import SpecSI
KCAP = int(os.environ.get("KCAP", "3"))
FACE = {}   # gate -> (ch_pe, lam_pe, ch_pB, lam_pB) of the last census (L-SI box 93 (d) counters)


def xiadj(G):
    adj = [set() for _ in range(G["N"])]
    for x in range(G["N"]):
        for wt, xt, b in G["opts"][x]:
            if xt >= 0: adj[x].add(xt)
    return adj


def acyclic(adj, removed):
    N = len(adj); col = [0] * N
    for s in range(N):
        if s in removed or col[s]: continue
        st = [(s, iter(adj[s]))]; col[s] = 1
        while st:
            v, it = st[-1]; nxt = None
            for w in it:
                if w in removed: continue
                if col[w] == 1: return False
                if col[w] == 0: nxt = w; break
            if nxt is None: col[v] = 2; st.pop()
            else: col[nxt] = 1; st.append((nxt, iter(adj[nxt])))
    return True


def kfvs(G, cap=KCAP):
    adj = xiadj(G); N = G["N"]
    for k in range(cap + 1):
        for S in itertools.combinations(range(N), k):
            if acyclic(adj, set(S)): return k
    return f">{cap}"


def census(G, elev=True, counters=True, cap=20000):
    r = own34.run(G, elev, cap); g, V, vals, sigs = r["g"], r["V"], r["vals"], r["sigs"]; T = r["T3"]
    SG = SpecSI(g); n = g.n
    sbar = [SG.evaluate_choice(list(s))[1] for s in sigs]
    gates = [(q, V[("g", q)], V[("pe", q)], V[("pB", q)]) for q in sorted(k[1] for k in V if isinstance(k, tuple) and k[0] == "g")]
    rows = []
    for q, gv, pe, pb in gates:
        fl = sum(sbar[t - 1][gv] != sbar[t][gv] for t in range(1, T + 1))
        lc = sum(vals[t - 1][pe][0] != vals[t][pe][0] or vals[t - 1][pb][0] != vals[t][pb][0] for t in range(1, T + 1))
        rows.append((q, fl, lc))
        FACE[q] = tuple(sum(f(t) for t in range(1, T + 1)) for f in (lambda t: vals[t - 1][pe] != vals[t][pe], lambda t: vals[t - 1][pe][0] != vals[t][pe][0],
                                                                       lambda t: vals[t - 1][pb] != vals[t][pb], lambda t: vals[t - 1][pb][0] != vals[t][pb][0]))
    out = dict(T3=T, fallback=r["fallback"], n=n)
    if rows:
        am = max(rows, key=lambda z: (z[1] / (z[2] + 1), z[1]))
        out.update(maxflip=max(z[1] for z in rows), ratio=round(am[1] / (am[2] + 1), 4), ratio_gate=list(am[0]), ratio_flips=am[1],
                   ratio_lamch=am[2], kfx=max(z[1] - 2 * (z[2] + 1) for z in rows), k1fail=sum(z[1] > 2 * z[2] + 1 for z in rows),
                   k1c2fail=sum(z[1] > 2 * (z[2] + 1) for z in rows), totflips=sum(z[1] for z in rows))
    if counters:
        nx = lambda t, u: sigs[t][u] if g.owner[u] == 0 else sbar[t][u]
        Rc = collections.Counter(); F = 0
        multi = [u for u in range(n) if len(g.succ[u]) >= 2]
        for t in range(1, T + 1):
            F += any(sbar[t - 1][gv] != sbar[t][gv] for _, gv, _, _ in gates)
            for u in multi:
                if nx(t - 1, u) != nx(t, u) and vals[t - 1][u][0] == vals[t][u][0]: Rc[(u, nx(t, u), vals[t][u][0])] += 1
        out.update(F=F, R=max(Rc.values(), default=0), C=own34.counters(r, True)["C"])
    return out, rows


if __name__ == "__main__":
    elev = "--noelev" not in sys.argv; cnt = "--nocounters" not in sys.argv
    for f in [a for a in sys.argv[1:] if not a.startswith("--")]:
        G = json.load(open(f)); NM = G["N"] + sum(len(o) for o in G["opts"])
        out, _ = census(G, elev, cnt)
        print(os.path.basename(f), "N+M", NM, "k", kfvs(G), out, flush=True)
