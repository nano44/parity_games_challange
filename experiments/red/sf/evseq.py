#!/usr/bin/env python3
"""L-RED: Even's DISTINCT-sigma sequence (DECOUPLE, N5-SF-box54 §2: it depends on sigma_0 only) under two rules, from the same sigma_0:
  sf   N5-SF S4a': optimum of the arena ({sigma(v)} + I_sigma) with Odd FIXED to sigma-bar(sigma)   (sf2.py's step)
  glo  I^glo / Schewe switch-best in the Xi frame: optimum of the arena game with Odd FREE (switch-all SI inside the arena from sigma)
Fallback (arena optimum = sigma): N5 S4c's Even switch. Engine: n5b (L-COMP PGSolver port), SPEC choice rule.
Prints per step the Even vertices that change, and the first step where the two sequences differ.
Usage: evseq.py GAME.pg [--rule sf|glo|both] [--cap K]"""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import sf2, pg, n5b
from n5b import SpecSI, dual, restrict, EVEN, ODD
from pgsolver_si import SI


def step(g, SG, sigma, rule):
    vs, sbar = SG.evaluate_choice(sigma)
    Is = n5b.N5.improving(SG, sigma, vs)
    if not Is:
        return None, sbar
    allow = [([sigma[v]] + Is.get(v, [])) if g.owner[v] == EVEN else None for v in range(g.n)]
    if rule == "sf":
        al = [a if a is not None else [sbar[v]] for v, a in enumerate(allow)]
        _, c2 = SpecSI(dual(restrict(g, al))).evaluate_choice([sbar[v] if g.owner[v] == ODD else -1 for v in range(g.n)])
        new = [c2[v] if g.owner[v] == EVEN else -1 for v in range(g.n)]
    else:
        H = SI(restrict(g, allow)); s = list(sigma)
        while True:
            val = H.evaluate(s); s2 = H.policy_switchall(s, val)
            if s2 == s: break
            s = s2
        new = s
    if new == list(sigma):
        new = list(sigma)
        for v in Is: new[v] = SG.best(vs, v)
    return new, sbar


def seq(g, rule, cap):
    SG = SpecSI(g); s = SG.initial_strategy_by_best_reward(); out = [(tuple(s), None)]
    while len(out) <= cap:
        new, sbar = step(g, SG, s, rule)
        out[-1] = (out[-1][0], tuple(sbar))
        if new is None: break
        s = new; out.append((tuple(s), None))
    return out


def labels(path):
    lab = {}
    for line in open(path):
        m = re.match(r'\s*(\d+)\s+\d+\s+\d+\s+[\d,]+\s*"([^"]*)"', line)
        if m: lab[int(m.group(1))] = m.group(2)
    return lab


def _main():
    a = sys.argv[1:]; g = pg.read(a[0]); L = labels(a[0]); cap = int(a[a.index("--cap") + 1]) if "--cap" in a else 10 ** 6
    rule = a[a.index("--rule") + 1] if "--rule" in a else "both"
    nm = lambda v: L.get(v, str(v))
    rules = ["sf", "glo"] if rule == "both" else [rule]
    S = {r: seq(g, r, cap) for r in rules}
    for r in rules:
        sb = sum(1 for x, y in zip(S[r], S[r][1:]) if y[1] is not None and x[1] != y[1])
        print(f"rule {r}: sigma-values {len(S[r])}, sigma-changes {len(S[r]) - 1}, sigma-bar changes along them {sb}")
    if rule == "both":
        A, B = S["sf"], S["glo"]
        for i in range(min(len(A), len(B))):
            if A[i][0] != B[i][0]:
                p = A[i - 1][0]
                print(f"first difference at step {i}")
                print(" sf :", " ".join(f"{nm(v)}:{nm(p[v])}>{nm(A[i][0][v])}" for v in range(g.n) if A[i][0][v] != p[v]))
                print(" glo:", " ".join(f"{nm(v)}:{nm(p[v])}>{nm(B[i][0][v])}" for v in range(g.n) if B[i][0][v] != p[v]))
                break
        else:
            print("no difference within", min(len(A), len(B)))


def shadow(path, cap=10 ** 6):
    """Along the SF sequence, compute the glo step from the same sigma and print the steps where they differ."""
    g = pg.read(path); L = labels(path); nm = lambda v: L.get(v, str(v)); SG = SpecSI(g)
    s = SG.initial_strategy_by_best_reward(); t = 0
    while t < cap:
        a, sbar = step(g, SG, s, "sf")
        if a is None: break
        b, _ = step(g, SG, s, "glo"); t += 1
        if a != b:
            da = " ".join(f"{nm(v)}>{nm(a[v])}" for v in range(g.n) if a[v] != b[v])
            db = " ".join(f"{nm(v)}>{nm(b[v])}" for v in range(g.n) if a[v] != b[v])
            print(f"{t}: sf [{da}]  glo [{db}]")
        s = a


if __name__ == "__main__":
    if sys.argv[1] == "--shadow":
        shadow(sys.argv[2])
    else:
        _main()
