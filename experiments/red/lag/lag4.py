#!/usr/bin/env python3
"""L-RED box 10 (produced on Opus 5.5): inversion relay + chainfam region clock (design: docs/red/R39).
Clock: dtl_chainfam UP (a, b, z, x_1..x_k) + root top S (Odd-owned, S -> W, W Odd sink) + edge a -> S, so S's round-1 region
gains x_m from visit m. Levels j = -1..D: tangle t_j on tau_j (Odd-owned top, edges w_j, v_j), w_j (Even -> y_j), y_j (Odd -> v_j, escape T_j),
v_j (Even -> tau_j): pulling w_j alone into an earlier region pulls nothing else, and y_j is then not re-attracted at T_j;
T_j Odd-owned with the single edge T_j -> b (so T_j survives round 1 and is parked in X with b, which lets tau_j close in the
next context and learn t_j). Hold: w_j -> y_{j-1}. Freeze: w_j -> f_j, f_j Odd with edges x_{j+OFF}, S.
Tops: S > T_{-1} > ... > T_D > tau_D > ... > tau_{-1} > clock. Usage: lag4.py D out.pg [OFF] [EXTRA]"""
import sys, os; from gb import GB
def build(D, OFF=3, extra=2, tedge="b"):
    k = D + OFF + extra; g = GB(); base = 2 * k + 2
    g.v("a", 2*k+1, 0); g.v("b", 2*k, 1); g.v("z", 2*k, 1)
    for j in range(1, k+1): g.v(f"x{j}", 2*(j-1), 1)
    g.e("a", "b", "a"); g.e("b", "z", "b"); g.e("z", "z", f"x{k}")
    for j in range(1, k+1): g.e(f"x{j}", f"x{j}", "a" if j == 1 else f"x{j-1}")
    L = list(range(-1, D + 1)); top = base + 4 * len(L) + 4
    g.v("W", top + 3, 1); g.e("W", "W"); g.v("S", top + 2, 1); g.e("S", "W"); g.e("a", "S")
    for i, j in enumerate(L):
        g.v(f"T{j}", top - 2 * i, 1)
        if tedge: g.e(f"T{j}", tedge)
    for i, j in enumerate(reversed(L)): g.v(f"tau{j}", top - 2 * len(L) - 2 * i, 1)
    for j in L:
        g.v(f"w{j}", 1, 0); g.v(f"y{j}", 1, 1); g.v(f"v{j}", 1, 0); g.v(f"f{j}", 1, 1)
        g.e(f"tau{j}", f"w{j}", f"v{j}"); g.e(f"w{j}", f"y{j}", f"f{j}"); g.e(f"y{j}", f"v{j}", f"T{j}"); g.e(f"v{j}", f"tau{j}")
        g.e(f"f{j}", f"x{j + OFF}", "S")
        if j > -1: g.e(f"w{j}", f"y{j - 1}")
    return g
if __name__ == "__main__":
    a = sys.argv; build(int(a[1]), *(int(x) for x in a[3:])).write(a[2])
