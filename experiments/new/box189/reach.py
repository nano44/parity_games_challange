#!/usr/bin/env python3
"""Box 189 REACH (L-NEW successor 58): run N5 (SPEC S1-S5, box21 n5x engine) on R104's Gamma(G) (L-RED r187 stab.build(G, 0,
kgad=True, esc=True)) from the default start S3 AND from R104's stated start; per state report the mover projection, whether the state
is STANDARD (sigma = sigma^s off the movers, tau = tau_0; R104 packet §3.1), and the FL runs (maximal non-fallback transitions keeping
tau, changing sigma, keeping the (sigma, tau)-play value W). Compares with the IDEAL trajectory (r187 ideal.traj).
Usage: reach.py GENOME.json [LREDROOT]   (LREDROOT = a tree holding experiments/red/r187, r178 and experiments/new/box21)."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
LR = sys.argv[2] if len(sys.argv) > 2 else os.environ.get("LRED")
sys.path[:0] = [os.path.join(LR, "experiments/red/r187"), os.path.join(LR, "experiments/red/r178"),
                os.path.join(ROOT, "experiments/new/box21"), os.path.join(ROOT, "experiments/new"), os.path.join(ROOT, "experiments/si"), os.path.join(ROOT, "experiments/harness")]
import stab, ideal, n5x, pg, n5
from si import Engine

def acyclic(G):
    N = G["N"]; adj = [[o[1] for o in G["opts"][x] if o[1] >= 0] for x in range(N)]; col = [0] * N
    def dfs(x):
        col[x] = 1
        for y in adj[x]:
            if col[y] == 1 or (col[y] == 0 and not dfs(y)): return False
        col[x] = 2; return True
    return all(col[x] or dfs(x) for x in range(N))

def playval(g, sigma, tau):
    succ = [[sigma[v]] if g.owner[v] == 0 else [tau[v]] for v in range(g.n)]
    h = pg.Game(list(g.prio), list(g.owner), succ); E = Engine(h)
    vs, _ = E.evaluate(tuple(sigma)); return tuple(vs)

def analyse(G, start, cap=100000):
    g, sig0, tau0, gv, ev, bv = stab.build(G, 0, kgad=True, esc=True)
    N = G["N"]; inv = {gv[q]: q[1] for q in gv}
    states, fbs = n5x.trace(g, start, cap=cap, check=False)
    E, Ed = Engine(g), Engine(n5.dual(g))
    rows = []
    for j, (s, t) in enumerate(states):
        proj = tuple(inv.get(s[x], -1) for x in range(N))
        std = all(s[v] == sig0[v] for v in sig0 if v >= N) and all(t[v] == tau0[v] for v in tau0)
        rows.append((proj, std))
    W = [playval(g, s, t) for s, t in states]
    fl = []
    for j in range(1, len(states)):
        (s0, t0), (s1, t1) = states[j - 1], states[j]
        # fallback detection: recompute the step
        r = n5x.step(g, E, Ed, list(s0), list(t0))
        fb = r[4]
        fl.append((not fb) and t0 == t1 and s0 != s1 and W[j] == W[j - 1])
    runs, cur = [], 0
    for j, f in enumerate(fl, 1):
        if f: cur += 1
        else:
            if cur: runs.append((j - 1 - cur, j - 1)); cur = 0
    if cur: runs.append((len(fl) - cur, len(fl)))
    return g, states, rows, runs, fbs

if __name__ == "__main__":
    G = json.load(open(sys.argv[1])); assert acyclic(G), "Xi-cyclic genome: outside R104"
    S, why = ideal.traj(G); L = len(S) - 1
    print(f"genome {os.path.basename(sys.argv[1])} N {G['N']} M {sum(len(o) for o in G['opts'])} L(G) {L} ({why})")
    g, sig0, tau0, *_ = stab.build(G, 0, kgad=True, esc=True)
    for name, start in (("STATED", (sig0, tau0)), ("S3", None)):
        g, states, rows, runs, fbs = analyse(G, start)
        print(f"[{name}] n {g.n} iterations {len(states) - 1} fallbacks {fbs} FL runs (a,b,len) " +
              " ".join(f"({a},{b},{b - a})" for a, b in runs) + f" max {max([b - a for a, b in runs] or [0])}")
        stdidx = [j for j, (p, sd) in enumerate(rows) if sd]
        print(f"  standard states at {stdidx[:20]}{'...' if len(stdidx) > 20 else ''}")
        for j, (p, sd) in enumerate(rows[:60]):
            mark = ""
            if p in S: mark = f" =IDEAL[{S.index(p)}]"
            print(f"  {j:3d} std={int(sd)} movers {''.join(map(str, p)) if all(x >= 0 for x in p) else p}{mark}")
