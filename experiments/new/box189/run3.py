#!/usr/bin/env python3
"""Box 189: N5 from S3 on Gamma3(G) (gamma3.py) for a pad set; reports (1) whether S3's start pair EQUALS R104's stated start
transported through the pads, (2) iterations, FL runs, (3) whether the mover projections of the S3 run equal the IDEAL trajectory
state for state. IDEAL trajectory: own implementation of R104's step (ideal_traj, from the R104 / packet §2 text).
Usage: run3.py GENOME PADS   (PADS e.g. K,pe,pb,m or none)"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [HERE, os.path.join(ROOT, "experiments/new/box21"), os.path.join(ROOT, "experiments/new"), os.path.join(ROOT, "experiments/si"), os.path.join(ROOT, "experiments/harness")]
import gamma3, n5x, n5, pg
from si import Engine

def chainB(G, s, x, k):
    B = []
    while True:
        B.append(G["opts"][x][k][2]); xt = G["opts"][x][k][1]
        if xt < 0: return B
        x, k = xt, s[xt]
def better(G, s, x, k, k2):   # (x,k) strictly Xi-better than (x,k2): Fact X rule (largest-rank beta of the symmetric difference)
    A, B = set(chainB(G, s, x, k)), set(chainB(G, s, x, k2)); D = A ^ B
    if not D: return False
    t = max(D, key=lambda b: G["br"][b]); return (G["bp"][t] == 0) == (t in A)
def ideal_traj(G, cap=10 ** 6):
    N, lev, opts, gate = G["N"], G["lev"], G["opts"], G["gate"]; s = list(G["start"]); S = [tuple(s)]
    order = sorted(range(N), key=lambda x: lev[x])
    while len(S) - 1 < cap:
        A = [[k for k in range(len(opts[x])) if k == s[x] or better(G, s, x, k, s[x])] for x in range(N)]
        if all(len(a) == 1 for a in A): return S, "opt"
        key = [None] * N; ns = list(s)
        for x in order:
            best = min(((gate[x][k],) if opts[x][k][0] < 0 else key[opts[x][k][0]] + (gate[x][k],), k) for k in A[x])
            key[x], ns[x] = best
        if ns == s: return S, "stuck"
        s = ns; S.append(tuple(s))
    return S, "cap"

def playval(g, sigma, tau):
    succ = [[sigma[v]] if g.owner[v] == 0 else [tau[v]] for v in range(g.n)]
    return tuple(Engine(pg.Game(list(g.prio), list(g.owner), succ)).evaluate(tuple(sigma))[0])

def fl_runs(g, states):
    E, Ed = Engine(g), Engine(n5.dual(g)); W = [playval(g, s, t) for s, t in states]; fl = []
    for j in range(1, len(states)):
        (s0, t0), (s1, t1) = states[j - 1], states[j]; fb = n5x.step(g, E, Ed, list(s0), list(t0))[4]
        fl.append((not fb) and t0 == t1 and s0 != s1 and W[j] == W[j - 1])
    runs, a = [], None
    for j, f in enumerate(fl + [False], 1):
        if f and a is None: a = j - 1
        if not f and a is not None: runs.append((a, j - 1)); a = None
    return runs

def main(path, pads):
    G = json.load(open(path)); S, why = ideal_traj(G); L = len(S) - 1
    g, sig, tau, V = gamma3.build(G, pads)
    E, Ed = Engine(g), Engine(n5.dual(g)); s3, t3 = n5x.start_pair(g, E, Ed, None)
    stated = list(s3), list(t3)
    for v, w in sig.items(): stated[0][v] = w
    for v, w in tau.items(): stated[1][v] = w
    diff = [v for v in range(g.n) if (s3[v] != stated[0][v] if g.owner[v] == 0 else t3[v] != stated[1][v])]
    states, fbs = n5x.trace(g, None, check=False)
    proj = [gamma3.mover_state(G, V, s, pads) for s, t in states]
    match = 0
    while match < len(proj) and match <= L and proj[match] == S[match]: match += 1
    runs = fl_runs(g, states)
    print(f"{os.path.basename(path)} pads={','.join(sorted(pads)) or 'none'} n {g.n} L(G) {L} | S3 == stated start: {not diff} "
          f"(differs at {len(diff)} vertices) | N5 from S3: {len(states) - 1} iterations, {fbs} fallbacks, FL runs "
          f"{[(a, b, b - a) for a, b in runs]} | movers follow IDEAL for states 0..{match - 1}")
    return not diff, len(states) - 1, runs, match - 1, L

if __name__ == "__main__":
    pads = set() if sys.argv[2] == "none" else set(sys.argv[2].split(","))
    main(sys.argv[1], pads)
