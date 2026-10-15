#!/usr/bin/env python3
"""L-RED adversarial families against L-SI's MSF (docs/red/R1-MSF.md).

gated_bland N   "Gate relabelling" of the Disser-Loho-Maat-Mosis Bland counter G_N (arXiv 2512.16684 v2, Fig. 4.1 / Lemma 4.4;
                L-SI's port experiments/si/gens.py dlmm_bland):
                  sink (Odd, 1, self-loop); a_i (Even, 2i+1), b_i (Odd, 2i+2), i = 1..N; a_i, b_i -> b_{i+1}, a_{i+1};
                  a_{N+1} = sink, b_{N+1} (Odd, 2N+4) -> sink.  Bland numbers: (a_i, b_{i+1}) = 2i, (a_i, a_{i+1}) = 2i - 1.
                Every choice of a_i is routed through a simple cycle in Friedmann's sense (arXiv 1106.0778 section 6.1,
                Lemma 6.1): a_i -> d_i (Even, priority 3) -> e_i^a, e_i^b (Odd, EVEN priorities); e_i^a -> {d_i, a_{i+1}},
                e_i^b -> {d_i, b_{i+1}}.  By Lemma 6.1 the switch d_i -> e is improving iff Odd currently loops e -> d_i,
                i.e. iff the exit of e beats d_i's current route; its MSF level is the priority of e (the only difference
                is {d_i, e}).  After the switch Odd escapes through the exit (even 2-cycle), so d_i's value becomes the
                exit's value: the gate relabels the LEVEL of an underlying switch without changing its EFFECT.
                Gate priorities decrease with the Bland number (e_i^a: 4N+6-4i, e_i^b: 4N+4-4i), so MSF's "highest level
                first" is Bland's "lowest number first".  The underlying priorities are shifted by C = 4N+4 so that every
                underlying comparison is decided above the gate junk.  PGSolver's best-reward start gives sigma_0 of
                Lemma 4.4 (d_i -> e_i^a, the higher even priority).
                Ids: sink 0; a_i = 5i-4, b_i = 5i-3, d_i = 5i-2, e_i^a = 5i-1, e_i^b = 5i (i = 1..N); b_{N+1} = 5N+1.
Usage: gens_red.py FAMILY N"""
import sys


def gated_bland(N):
    C = 4 * N + 4
    sink = 0
    A = lambda i: sink if i == N + 1 else 5 * i - 4
    B = lambda i: 5 * N + 1 if i == N + 1 else 5 * i - 3
    D = lambda i: 5 * i - 2
    EA = lambda i: 5 * i - 1
    EB = lambda i: 5 * i
    rows = [f"{sink} 1 1 {sink} \"sink\";"]
    for i in range(1, N + 1):
        rows.append(f"{A(i)} {2 * i + 1 + C} 0 {D(i)} \"a{i}\";")
        rows.append(f"{B(i)} {2 * i + 2 + C} 1 {A(i + 1)},{B(i + 1)} \"b{i}\";")
        rows.append(f"{D(i)} 3 0 {EA(i)},{EB(i)} \"d{i}\";")
        rows.append(f"{EA(i)} {4 * N + 6 - 4 * i} 1 {D(i)},{A(i + 1)} \"ea{i}\";")
        rows.append(f"{EB(i)} {4 * N + 4 - 4 * i} 1 {D(i)},{B(i + 1)} \"eb{i}\";")
    rows.append(f"{B(N + 1)} {2 * N + 4 + C} 1 {sink} \"b{N + 1}\";")
    return f"parity {5 * N + 1};\n" + "\n".join(rows) + "\n"


def friedmann_Gn(n, pads=None, padprio=0):
    """Friedmann's lower-bound game G_n for the locally optimizing policy (switch-all), arXiv 1106.0778 section 6.4, Table 4
    (10n+4 nodes), with the initial strategy iota_{G_n} (p.16) printed as a '% start v:w ...' line (the PGSolver best-reward
    start is not iota).  Optional pads: pads(i) dangling Even vertices of priority padprio with the single edge -> d_i, for
    i = 1..n (the vertices whose valuation changes exactly when d_i's does; they count for d_i's switches only).
    Ids: x 0, s 1, r 2, c 3; t_i = 3 + i, a_i = 3 + 2n + i (i = 1..2n); for i = 1..n: d_i, e_i, g_i, k_i, f_i, h_i =
    4n + 4 + 6(i-1) + 0..5; pads follow."""
    X, S, R, C = 0, 1, 2, 3
    T = lambda i: 3 + i; A = lambda i: 3 + 2 * n + i
    base = 4 * n + 4
    D = lambda i: base + 6 * (i - 1); E = lambda i: D(i) + 1; G = lambda i: D(i) + 2; K = lambda i: D(i) + 3; F = lambda i: D(i) + 4; H = lambda i: D(i) + 5
    rows = {}; start = {}
    rows[X] = (1, 1, [X], "x")
    rows[S] = (8 * n + 6, 0, [F(j) for j in range(1, n + 1)] + [X], "s"); start[S] = X
    rows[R] = (8 * n + 8, 0, [G(j) for j in range(1, n + 1)] + [X], "r"); start[R] = X
    rows[C] = (8 * n + 4, 0, [S, R], "c"); start[C] = R
    for i in range(1, 2 * n + 1):
        rows[T(i)] = (4 * n + 3 if i == 1 else 4 * n + 2 * i + 1, 0, [S, R, C] if i == 1 else [S, R, T(i - 1)], f"t{i}")
        start[T(i)] = C if i == 1 else R
        rows[A(i)] = (4 * n + 2 * i + 2, 1, [T(i)], f"a{i}")
    for i in range(1, n + 1):
        rows[D(i)] = (4 * i + 1, 0, [S, E(i), R] + [A(j) for j in range(1, 2 * i + 1)], f"d{i}"); start[D(i)] = R
        rows[E(i)] = (4 * i + 2, 1, [D(i), H(i)], f"e{i}")
        rows[G(i)] = (4 * i + 4, 0, [F(i), K(i)], f"g{i}"); start[G(i)] = K(i)
        rows[K(i)] = (8 * n + 4 * i + 7, 0, [X] + [G(j) for j in range(i + 1, n + 1)], f"k{i}"); start[K(i)] = X
        rows[F(i)] = (8 * n + 4 * i + 9, 1, [E(i)], f"f{i}")
        rows[H(i)] = (8 * n + 4 * i + 10, 1, [K(i)], f"h{i}")
    nxt = 10 * n + 4
    if pads:
        if callable(pads):                       # pads(i) dangling vertices on d_i
            plan = {D(i): pads(i) for i in range(1, n + 1)}
        else:                                    # dict label -> number of pads (labels as in rows)
            byl = {rows[v][3]: v for v in rows}; plan = {byl[l]: k for l, k in pads.items()}
        for v0, k in plan.items():
            for _ in range(k):
                rows[nxt] = (padprio, 0, [v0], f"p_{rows[v0][3]}"); start[nxt] = v0; nxt += 1
    out = [f"parity {nxt - 1};"]
    for v in range(nxt):
        pr, pl, su, lab = rows[v]
        out.append(f"{v} {pr} {pl} {','.join(map(str, sorted(set(su))))} \"{lab}\";")
    return "\n".join(out) + "\n% start " + " ".join(f"{v}:{w}" for v, w in sorted(start.items())) + "\n"


def padded_Gn(n, C=1):
    """friedmann_Gn with pads(i) = C (n + 1 - i): the lowest open gate has the most dangling traffic (S7 attack, R3)."""
    return friedmann_Gn(n, pads=lambda i: C * (n + 1 - i))


def padded2_Gn(n, C=1, P=None):
    """friedmann_Gn with pads(d_i) = C (n + 1 - i) and P pads on every correction vertex (s, r, c, t_i, g_i, k_i), P > C n,
    so that corrections always precede the next gate closing and lower gates precede higher ones (S7 attack, R3)."""
    if P is None: P = C * n + 1
    pads = {f"d{i}": C * (n + 1 - i) for i in range(1, n + 1)}
    for l in ["s", "r", "c"] + [f"t{i}" for i in range(1, 2 * n + 1)] + [f"g{i}" for i in range(1, n + 1)] + [f"k{i}" for i in range(1, n + 1)]:
        pads[l] = P
    return friedmann_Gn(n, pads=pads)


def padded3_Gn(n, C=None, P=None, lane=0):
    """friedmann_Gn with pads only on s, r (P) and on the gates d_i (C (n + 1 - i)); none on g, k (so that g_mu's access and
    the selector updates come after the lower gates reopen) and `lane` pads on each t_i (S7 attack, R3)."""
    if C is None: C = 4 * n + 3
    if P is None: P = 10 * C * n
    pads = {f"d{i}": C * (n + 1 - i) for i in range(1, n + 1)}; pads["s"] = P; pads["r"] = P
    if lane:
        for i in range(1, 2 * n + 1): pads[f"t{i}"] = lane
    return friedmann_Gn(n, pads=pads)


def padded4_Gn(n, C=None):
    """friedmann_Gn with pads encoding the single-switch order the counter needs under S7 (R3): s, r (10Cn) > selectors k_i
    (Cn + C) > gates d_i (C (n+1-i), lowest gate first) > access g_i (C (n+1-i) - 1, just below its own gate) > lane (0)."""
    if C is None: C = 4 * n + 3
    pads = {}
    for i in range(1, n + 1):
        pads[f"d{i}"] = C * (n + 1 - i); pads[f"g{i}"] = C * (n + 1 - i) - 1; pads[f"k{i}"] = C * n + C
    pads["s"] = pads["r"] = 10 * C * n
    return friedmann_Gn(n, pads=pads)


def padded5_Gn(n, C=None, rpads=0, gmode="below"):
    """padded4 with NO pads on r (r's pads were entering reopened gates through g_j -> f_j -> e_j -> d_j and inflating their
    closings above the selectors k_{j-1}; Lemma D then forces the gate to close before the selector updates)."""
    if C is None: C = 4 * n + 3
    pads = {}
    for i in range(1, n + 1):
        pads[f"d{i}"] = C * (n + 1 - i); pads[f"k{i}"] = C * n + C
        if gmode == "below": pads[f"g{i}"] = C * (n + 1 - i) - 1
    pads["s"] = 10 * C * n
    if rpads: pads["r"] = rpads
    return friedmann_Gn(n, pads=pads)


FAMILIES = {"gated_bland": gated_bland, "friedmann_Gn": friedmann_Gn, "padded_Gn": padded_Gn, "padded2_Gn": padded2_Gn,
            "padded3_Gn": padded3_Gn, "padded4_Gn": padded4_Gn, "padded5_Gn": padded5_Gn}
if __name__ == "__main__":
    sys.stdout.write(FAMILIES[sys.argv[1]](int(sys.argv[2])))
