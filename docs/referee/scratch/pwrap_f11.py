#!/usr/bin/env python3
"""REFEREE s34: [F11] G_n from Table 4 as I read it in the PDF (p. 15; sha256 46c96f44…), with Table 4's priorities and with Figure 4's
(the six formulas d, e, g, k, f, h minus 2). Prints: injectivity, highest priority vs Fact 6.1 (12n + 8), node / edge counts vs Fact 6.1,
n_O, m_O, m_E, |W(G_n, ι)| = n + 7 m_E + 6 m_O + n_O + 9 vs 10.5n² + 152.5n + 48, and whether G_n|τ (τ(e_i) = h_i) has a cycle other
than x's loop (Lemma 6.7 (1)'s graph claim). Mine; no lane code."""
def game(n, fig4):
    P, O, S = {}, {}, {}
    m = 2 if fig4 else 0
    P["t1"], O["t1"], S["t1"] = 4*n + 3, 0, ["s", "r", "c"]
    for i in range(2, 2*n + 1): P[f"t{i}"], O[f"t{i}"], S[f"t{i}"] = 4*n + 2*i + 1, 0, ["s", "r", f"t{i-1}"]
    for i in range(1, 2*n + 1): P[f"a{i}"], O[f"a{i}"], S[f"a{i}"] = 4*n + 2*i + 2, 1, [f"t{i}"]
    P["c"], O["c"], S["c"] = 8*n + 4, 0, ["s", "r"]
    for i in range(1, n + 1):
        P[f"d{i}"], O[f"d{i}"], S[f"d{i}"] = 4*i + 1 - m, 0, ["s", f"e{i}", "r"] + [f"a{j}" for j in range(1, 2*i + 1)]
        P[f"e{i}"], O[f"e{i}"], S[f"e{i}"] = 4*i + 2 - m, 1, [f"d{i}", f"h{i}"]
        P[f"g{i}"], O[f"g{i}"], S[f"g{i}"] = 4*i + 4 - m, 0, [f"f{i}", f"k{i}"]
        P[f"k{i}"], O[f"k{i}"], S[f"k{i}"] = 8*n + 4*i + 7 - m, 0, ["x"] + [f"g{j}" for j in range(i + 1, n + 1)]
        P[f"f{i}"], O[f"f{i}"], S[f"f{i}"] = 8*n + 4*i + 9 - m, 1, [f"e{i}"]
        P[f"h{i}"], O[f"h{i}"], S[f"h{i}"] = 8*n + 4*i + 10 - m, 1, [f"k{i}"]
    P["s"], O["s"], S["s"] = 8*n + 6, 0, [f"f{j}" for j in range(1, n + 1)] + ["x"]
    P["r"], O["r"], S["r"] = 8*n + 8, 0, [f"g{j}" for j in range(1, n + 1)] + ["x"]
    P["x"], O["x"], S["x"] = 1, 1, ["x"]
    return P, O, S
def cyc_other_than_x(n, S, O):
    # G_n|tau: Odd e_i keeps only h_i; Even keeps all edges. Any cycle not equal to x's loop?
    E = {v: ([f"h{v[1:]}"] if v.startswith("e") else S[v]) for v in S}
    col = {}; 
    def dfs(v, stack):
        col[v] = 1
        for w in E[v]:
            if w == "x" and v == "x": continue
            if col.get(w) == 1: return True
            if col.get(w) is None and dfs(w, stack): return True
        col[v] = 2; return False
    import sys; sys.setrecursionlimit(10000)
    return any(col.get(v) is None and dfs(v, []) for v in E)
for n in range(1, 11):
    for fig4 in (False, True):
        P, O, S = game(n, fig4)
        nv = len(P); me = sum(len(S[v]) for v in S if O[v] == 0); mo = sum(len(S[v]) for v in S if O[v] == 1); no = sum(O.values())
        W = nv + 7*me + 6*mo + no + 9
        print(f"n {n} {'fig4 ' if fig4 else 'table4'} injective {len(set(P.values())) == nv} max {max(P.values())} (12n+8 {12*n+8}) "
              f"nodes {nv} (10n+4 {10*n+4}) edges {me+mo} (1.5n²+20.5n+5 {1.5*n*n+20.5*n+5}) n_O {no} m_O {mo} m_E {me} "
              f"|W| {W} (10.5n²+152.5n+48 {10.5*n*n+152.5*n+48}) x-only-cycle {not cyc_other_than_x(n, S, O)} xmin {min(P, key=P.get) == 'x'}")
