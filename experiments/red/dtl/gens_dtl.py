#!/usr/bin/env python3
"""Families for the DTL box (L-RED). `chain n`: one-player (all Odd-owned) game with even priorities 2..2n, vertex i has
edges to every j <= i+1 (dense downward, one step up): DTL's sptl loop learns a chain of tangles, one more top per pass.
Usage: gens_dtl.py chain|counter_dftl|counter_odftl|ladder n"""
import sys


def chain(n):
    out = [f"parity {n - 1};"]
    for i in range(n):
        succ = sorted(set(range(0, min(n, i + 2))))
        out.append(f"{i} {2 * i + 2} 1 {','.join(map(str, succ))};")
    return "\n".join(out) + "\n"




def counter_dftl(n, two=False):
    """Transcription of van Dijk's src/tools/counter_dftl.cpp (oink branch dftl @ a028e62, 8 + 4N vertices) and, with
    two=True, counter_odftl.cpp (@ d54dfad, 8 + 6N vertices: a 2-cycle of priority 1 in front of each dominant)."""
    piv = 2 + 2 * n; k = 6 if two else 4; V = 8 + k * n
    pr = [0] * V; ow = [0] * V; E = []
    def init(v, p, o): pr[v] = p; ow[v] = o
    init(0, piv + 6, 1); init(1, 0, 1); init(2, piv + 5, 1); init(3, 2, 1); init(4, 2, 1)
    E += [(0, 3), (1, 0), (2, 1), (3, 2), (3, 4), (4, 3)]
    init(5, piv + 2, 0); init(6, piv + 4, 0); init(7, piv + 5, 0)
    E += [(1, 5), (5, 1), (5, 6), (6, 7), (7, 5)]
    for i in range(n):
        c = 8 + k * i; d = piv + 8 + 2 * i; e = piv - 2 * i
        init(c, e, 0); init(c + 1, e, 0); init(c + 2, d, 0); init(c + 3, d + 1, 0)
        E += [(1, c), (c, 1), (3, c + 1), (c + 1, 3), (c, c + 2), (c + 1, c + 2), (c + 3, c + 1)]
        if two:
            init(c + 4, 1, 0); init(c + 5, 1, 0); E += [(c + 2, c + 4), (c + 4, c + 5), (c + 5, c + 4), (c + 4, c + 3)]
        else:
            E += [(c + 2, c + 3)]
    succ = [[] for _ in range(V)]
    for a, b in E: succ[a].append(b)
    return f"parity {V - 1};\n" + "".join(f"{v} {pr[v]} {ow[v]} {','.join(map(str, succ[v]))};\n" for v in range(V))


def counter_odftl(n): return counter_dftl(n, True)


def ladder(m):
    """Absorption ladder against R8 (E)/(P). Higher open tops K_1 < ... < K_{m+2} (each K_i -> w_i -> K_i, w_i escapes to
    K_{i+1}; the top one is a dominion solved first, then one K per search dissolves top-down). Head J (Even, priority
    200) with base cycle {J, b0} (b0 Odd, escape K_1). Rungs: u_s Even -> a_s (Odd: returns to J, escapes to K_1 and to
    x_s); X_s = {x_s, x_s'} is a 2-cycle (escapes K_1 and a_{s-1}) learned at head x_s; the chain J -> u_1 -> u_2 ... is
    Even-owned (u_s -> u_{s+1}, u_s -> a_s), so the SCC at J grows by one rung whenever X_s fires. What Oink does (R8
    section 10): the top of the tower is a dominion in pass 1 and the dominion attractor (with tangles) solves the whole
    tower and the ladder in one search: 2m + 2 tangles, 1 iteration, J learns {J, b0} once."""
    V = []; E = []
    def add(lab, pr, ow): V.append((lab, pr, ow)); return len(V) - 1
    L = m + 2; K = []; W = []
    for i in range(1, L + 1):
        K.append(add(f"K{i}", 300 + 2 * i, 0)); W.append(add(f"w{i}", 299 + 2 * i, 1))
    for i in range(L):
        E += [(K[i], W[i]), (W[i], K[i])]
        if i + 1 < L: E.append((W[i], K[i + 1]))
    J = add("J", 200, 0); b0 = add("b0", 1, 1); E += [(J, b0), (b0, J), (b0, K[0])]
    a_prev = b0; u_prev = J
    for s in range(1, m + 1):
        us = add(f"u{s}", 2 * s, 0); as_ = add(f"a{s}", 2 * s + 1, 1); xs = add(f"x{s}", 100 + 2 * s, 1); xps = add(f"x{s}p", 99 + 2 * s, 1)
        E += [(u_prev, us), (us, as_), (as_, J), (as_, K[0]), (as_, xs), (xs, xps), (xs, K[0]), (xps, xs), (xps, a_prev)]
        a_prev = as_; u_prev = us
    succ = [[] for _ in V]
    for p_, q_ in E: succ[p_].append(q_)
    return f"parity {len(V)};\n" + "".join(f'{i} {pr} {ow} {",".join(map(str, succ[i]))} "{lab}";\n' for i, (lab, pr, ow) in enumerate(V))


def n5(_=0):
    """The proof lane's NOTE N5 straddle shape (DTL-proof.md 1.6) as a game, for a trace: t' = {a, c, d} with a -> c -> d,
    d (Odd) -> c, a, e; a -> tnew (a top only later); tau's region holds e. Dominion-free closure is not attempted: the
    purpose is to watch whether the pruning is non-monotone across searches (section 12)."""
    V = [("tnew", 14, 0), ("tau", 12, 0), ("a", 10, 0), ("c", 6, 0), ("d", 5, 1), ("e", 3, 1), ("g", 1, 1), ("h", 8, 0), ("q", 15, 1)]
    ix = {lab: i for i, (lab, _, _) in enumerate(V)}
    E = [("a", "c"), ("c", "d"), ("d", "c"), ("d", "a"), ("d", "e"), ("a", "tnew"), ("e", "tau"), ("tau", "e"), ("tau", "g"), ("g", "tau"), ("g", "q"),
         ("tnew", "h"), ("h", "tnew"), ("h", "d"), ("q", "q"), ("q", "h")]
    succ = [[] for _ in V]
    for x, y in E: succ[ix[x]].append(ix[y])
    return f"parity {len(V)};\n" + "".join(f'{i} {pr} {ow} {",".join(map(str, succ[i]))} "{lab}";\n' for i, (lab, pr, ow) in enumerate(V))


if __name__ == "__main__":
    sys.stdout.write({"chain": chain, "counter_dftl": counter_dftl, "counter_odftl": counter_odftl, "ladder": ladder, "n5": n5}[sys.argv[1]](int(sys.argv[2])))
