#!/usr/bin/env python3
"""Box 190 DE-TOWER (L-NEW successor 58): N5' variants = SPEC S1-S5 with ONE rule changed in S4a (Even's step). Every variant keeps
sigma_new(v) in A(v) = {sigma(v)} + Iσ(v) (so each non-fallback iteration applies a subset of improving switches: R15 (d)'s
termination and SPEC S5's stop-correctness argument are untouched), S4b, S4c, S5 unchanged.
  mode "spec": N5 (box21 n5x.step).
  mode "xi"  : S4a's TIE (options w in A(v) with W*(v) = v + W*(w) in the arena H, v not its own H-cycle node) broken by the BEST
               Xi_sigma value (ties: SPEC's choice, then larger index) instead of SPEC's (root-first key) choice.
  mode "idx" : the same TIE broken by the LARGEST vertex index (a different key order).
  mode "seq" : SPEC's sigma_new applied at ONE Even vertex only (the least index where it differs), others keep sigma.
run(g, mode, start=None, cap) -> (states, fallbacks). Usage: n5v.py GAME.pg MODE [STARTFILE]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [os.path.join(ROOT, "experiments/new/box21"), os.path.join(ROOT, "experiments/new"), os.path.join(ROOT, "experiments/si"), os.path.join(ROOT, "experiments/harness")]
import pg, n5, n5x
from si import Engine
dual = n5.dual

def step(g, E, Ed, sigma, tau, mode):
    n = g.n
    vs, _ = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
    vt, _ = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
    if not Is and not It: return None
    ns, nt = list(sigma), list(tau)
    if Is:
        opt = {v: {sigma[v]} for v in range(n) if g.owner[v] == 0}
        for v, w in Is: opt[v].add(w)
        succ = [sorted(opt[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)]
        Er = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ)))
        vh, best = Er.evaluate(tuple(tau[v] if g.owner[v] == 1 else -1 for v in range(n)))
        for v in range(n):
            if g.owner[v] == 0: ns[v] = best[v]
        if mode in ("xi", "idx"):
            for v in range(n):
                if g.owner[v] != 0 or len(opt[v]) < 2 or vh[v][0] == v: continue
                tie = [w for w in opt[v] if Er.extend(v, vh[w]) == vh[v]]
                if not tie: continue
                if mode == "xi": ns[v] = max(tie, key=lambda w: (E.key(vs[w]), w == best[v], w))
                else: ns[v] = max(tie)
        if mode == "seq":
            ch = [v for v in range(n) if g.owner[v] == 0 and ns[v] != sigma[v]]
            ns = list(sigma)
            if ch: ns[ch[0]] = best[ch[0]]
    if It:
        opt = {v: {tau[v]} for v in range(n) if g.owner[v] == 1}
        for v, w in It: opt[v].add(w)
        succ = [sorted(opt[v]) if g.owner[v] == 1 else [sigma[v]] for v in range(n)]
        Er = Engine(pg.Game(list(g.prio), list(g.owner), succ))
        _, best = Er.evaluate(tuple(sigma[v] if g.owner[v] == 0 else -1 for v in range(n)))
        for v in range(n):
            if g.owner[v] == 1: nt[v] = best[v]
    fb = 0
    if ns == list(sigma) and nt == list(tau):
        fb = 1
        if Is:
            for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
        else:
            for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
    return ns, nt, Is, It, fb

def run(g, mode, start=None, cap=10 ** 6):
    E, Ed = Engine(g), Engine(dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, start)
    states = [(tuple(sigma), tuple(tau))]; fbs = 0
    while len(states) - 1 < cap:
        r = step(g, E, Ed, sigma, tau, mode)
        if r is None: break
        sigma, tau, _, _, fb = r; fbs += fb; states.append((tuple(sigma), tuple(tau)))
    return states, fbs, E

def solution(g, states, E):
    """SPEC S5 output: regions + strategies (sigma on Even's region, sigma-bar on Odd's)."""
    s = states[-1][0]; vs, sbar = E.evaluate(tuple(s))
    win = [0 if g.prio[vs[v][0]] % 2 == 0 else 1 for v in range(g.n)]
    strat = [s[v] if g.owner[v] == 0 else sbar[v] for v in range(g.n)]
    return win, strat

if __name__ == "__main__":
    g = n5x.load(sys.argv[1]); st = n5x.readstart(sys.argv[3]) if len(sys.argv) > 3 else None
    states, fb, E = run(g, sys.argv[2], st); print(f"n5v mode {sys.argv[2]} iterations {len(states) - 1} fallbacks {fb}")
