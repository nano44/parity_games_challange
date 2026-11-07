#!/usr/bin/env python3
"""Packet P-M2D-DEAD (docs/lower/P-M2D-DEAD.md) check: replays both instances from the pinned copies in kill/ with the own
simulator sim.py AND an inline second implementation written from R104's definition in this file (literal β-sets, compared by
the largest-rank element of the symmetric difference; literal lexicographic keys), checks sha1 pins, the membership conditions
(i)-(vii) via memcheck.py, and prints the per-step table (step, state, movers of the step) used in the packet.
Usage: p_m2d_check.py [--table]"""
import os, sys, json, hashlib, subprocess
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
from sim import run as run1
PINS = [("kill/KILL_M2D_d6_mu13.json", "5301c716f68f219bda2806f29b317c94e0ed5df0", 8, 13, 13),
        ("kill/KILL_M2D_d8_mu21.json", "d96c2b3657e79c410b180580d829366cbecc9ea4", 15, 21, 24)]
def run2(G, s0):
    """second implementation: β-sets as frozensets of β indices; better(P, Q) by the largest-rank β of P △ Q and its parity"""
    N = G["N"]; O = G["opts"]; br = G["br"]; bp = G["bp"]
    def bset(s, x, k):
        out = set()
        while True:
            out.add(O[x][k][2]); y = O[x][k][1]
            if y < 0: return frozenset(out)
            x, k = y, s[y]
    def better(P, Q):
        D = P ^ Q
        if not D: return False
        m = max(D, key=lambda b: br[b]); return (m in P) == (bp[m] == 0)
    def key(s, x, k):
        ks = []
        while True:
            ks.append(G["gate"][x][k]); w = O[x][k][0]
            if w < 0: return tuple(reversed(ks))
            x, k = w, s[w]
    S = [tuple(s0)]
    while True:
        s = S[-1]
        A = [[k for k in range(len(O[x])) if k == s[x] or better(bset(s, x, k), bset(s, x, s[x]))] for x in range(N)]
        if all(len(a) == 1 for a in A): return S
        ns = list(s)
        for lev in sorted(set(G["lev"])):
            for x in range(N):
                if G["lev"][x] == lev: ns[x] = min(A[x], key=lambda k: key(ns, x, k))
        if tuple(ns) == s: return S
        S.append(tuple(ns))
for f, sh, z, mz, T in PINS:
    p = os.path.join(H, f); assert hashlib.sha1(open(p, "rb").read()).hexdigest() == sh, f
    G = json.load(open(p)); S1 = [tuple(s) for s in run1(G, G["start"])]; S2 = run2(G, G["start"])
    assert S1 == S2, f
    mv = sum(1 for t in range(1, len(S1)) if S1[t][z] != S1[t - 1][z])
    assert len(S1) - 1 == T and mv == mz and mz > G["N"], f
    out = subprocess.run([sys.executable, "-I", os.path.join(H, "memcheck.py"), p, str(z)], capture_output=True, text=True).stdout
    assert "ALL PASS" in out, out
    print(f"P-M2D-DEAD {f}: sha1 ok, two implementations agree (T {T}), mover {z} moves {mv} > 2d = {G['N']}, membership ALL PASS")
    if "--table" in sys.argv:
        for t, s in enumerate(S1):
            print(f"  t {t:2d} state {''.join(map(str, s))} movers {[x for x in range(G['N']) if t and s[x] != S1[t-1][x]]}")
R = os.path.join(H, "..", "..", "..")
for fn, sh in (("docs/lower/P-M2D-DEAD-line-L1.txt", "1dec8b4da3be767d4cffeb2f37fdd2f017cb10e6"), ("docs/lower/P-M2D-DEAD-fixes.md", "966aee219a0c9e894e3959714a6c1bf764a3962a"), ("docs/lower/P-M2D-DEAD-line-L2.txt", "8ca7bcca624b6bc9ca6ee92eb46457608efbe051")):
    assert hashlib.sha1(open(os.path.join(R, fn), "rb").read()).hexdigest() == sh, fn
print("P-M2D-DEAD line files L-1, L-2 and fixes entry 1 pinned")
print("P-M2D-DEAD CHECK PASS")
