#!/usr/bin/env python3
"""L-NEW box 77: candidate (sigma, sbar) pair potential for phase length. For a phase P = [a, b] (lambda_Xi, tau constant), fin := Xi_b.
DEPTH_t(v) := number of leading coordinates of Xi_t(v) equal to fin(v) in the [S1-ord] coordinate sequence (cycle reward; P-bits from
rank n-1 down; signed length): n + 2 if equal. K3_t := sum_v DEPTH_t(v), range [0, n(n + 2)].
Checks: MONO (K3 never decreases inside a phase; LEVEL-MON with ceiling fin), and per phase: len, STRICT (transitions with K3 rising),
STALL (longest run of consecutive transitions with K3 flat). Also K3W: the same with W's end-of-phase value (fails MONO at fallbacks).
Usage: fixdepth.py GAME.pg [START] [--lzc]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
if "--lzc" in sys.argv:
    sys.path.insert(0, os.path.join(HERE, "..", "box72")); from n5lz import step
args = [a for a in sys.argv[1:] if not a.startswith("--")]
g = load(args[0]); n = g.n; start = readstart(args[1]) if len(args) > 1 else None
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start)
S = [tuple(s)]; TAU = [tuple(t)]
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1]))
T = len(S) - 1
XI = [E.evaluate(x)[0] for x in S]; LX = [tuple(v[0] for v in x) for x in XI]
ph = [0] * (T + 1)
for k in range(1, T + 1): ph[k] = ph[k - 1] + (LX[k] != LX[k - 1] or TAU[k] != TAU[k - 1])
def depth(a, b):
    if a == b: return n + 2
    if a[0] != b[0]: return 0
    x = a[1] ^ b[1]
    if x: return 1 + (n - 1 - (x.bit_length() - 1))
    return n + 1
flatv = (0, None, None, 0); mono = 0; worst = (0, 0, 0, 0); tot_len = tot_strict = 0; maxstall = 0; ratio = 0.0
for p in range(ph[-1] + 1):
    ks = [k for k in range(T + 1) if ph[k] == p]
    if len(ks) < 2: continue
    fin = XI[ks[-1]]
    K = [sum(depth(XI[k][v], fin[v]) for v in range(n)) for k in ks]
    strict = sum(1 for i in range(len(K) - 1) if K[i + 1] > K[i]); mono += sum(1 for i in range(len(K) - 1) if K[i + 1] < K[i])
    stall = run = 0
    for i in range(len(K) - 1):
        run = run + 1 if K[i + 1] == K[i] else 0; stall = max(stall, run)
    for v in range(n):
        fl = sum(1 for k0, k1 in zip(ks, ks[1:]) if XI[k0][v] != XI[k1][v] and depth(XI[k0][v], fin[v]) == depth(XI[k1][v], fin[v]))
        if fl > flatv[0]: flatv = (fl, v, p, L0 := len(ks) - 1)
    L = len(ks) - 1; tot_len += L; tot_strict += strict; maxstall = max(maxstall, stall)
    if L > worst[0]: worst = (L, strict, stall, K[-1] - K[0])
print(f"FIXD {os.path.basename(args[0])} n {n} iters {T} phases {ph[-1] + 1} mono-viol {mono} trans {tot_len} strict {tot_strict} "
      f"flat {tot_len - tot_strict} max-stall {maxstall} longest-phase (len, strict, stall, gain) {worst} max-flat-changes-per-(v,phase) {flatv}")
