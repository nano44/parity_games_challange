#!/usr/bin/env python3
"""Box 29 checks for Lemma TC (L-NEW): inside a crossing-free interval of a phase (R constant): (i) H1 constant; (ii) H2 constant;
(iii) under H2, H3 constant; (iv) H1 ⟺ λ_Ξ(o) ∉ R ∪ {o}; H2 ⟺ τ(o) ∉ R ∪ {o}; (v) under ¬H1 ∧ ¬H2: EQ ⟺ θ = w;
(vi) under ¬H1 ∧ ¬H2, every EQ → OTHER transition changes w; (vii) under H2, no transition between OTHER and non-OTHER;
under H1 ∧ ¬H2, every state is OTHER. Usage: tccheck.py game.pg [start] | tccheck.py --rand N lo hi seed [--randstart]"""
import sys, random
from otherx import *

def analyse(g, start, acc):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, start); rows = []
    while True:
        Xi, sb = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t)); _, W = wvals(g, s, t)
        Xk = [E.key(Xi[v]) for v in range(g.n)]; Wk = [E.key(W[v]) for v in range(g.n)]
        h = (not oncycle(g, s, sb, o), not oncycle(g, s, t, o), Xi[o][0] == W[o][0]); R = reach_o(g, s, t, o) | {o}
        other = (not all(h)) and Xk != Wk
        rows.append(dict(ph=(tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), h=h, R=R, other=other, eq=Xk == Wk,
                         th=Xk[o], w=Wk[o], lx=Xi[o][0], a=t[o]))
        r = step(g, E, Ed, s, t)
        if r is None: break
        s, t = r[0], r[1]
    for r in rows:
        acc["states"] += 1
        acc["iv_fail"] += (r["h"][0] != (r["lx"] not in r["R"])) + (r["h"][1] != (r["a"] not in r["R"]))
        if not r["h"][0] and not r["h"][1]: acc["v_checks"] += 1; acc["v_fail"] += r["eq"] != (r["th"] == r["w"])
        if r["h"][0] and not r["h"][1]: acc["vii_b_checks"] += 1; acc["vii_b_fail"] += not r["other"]
    for k in range(len(rows) - 1):
        a, b = rows[k], rows[k + 1]
        if a["ph"] != b["ph"] or a["R"] != b["R"]: continue
        acc["transitions"] += 1
        acc["i_fail"] += a["h"][0] != b["h"][0]; acc["ii_fail"] += a["h"][1] != b["h"][1]
        if a["h"][1]: acc["iii_fail"] += a["h"][2] != b["h"][2]; acc["vii_a_fail"] += a["other"] != b["other"]
        if not a["h"][0] and not a["h"][1] and a["eq"] and b["other"]: acc["vi_checks"] += 1; acc["vi_fail"] += a["w"] == b["w"]

if __name__ == "__main__":
    a = sys.argv[1:]
    acc = {k: 0 for k in "states transitions i_fail ii_fail iii_fail iv_fail v_checks v_fail vi_checks vi_fail vii_a_fail vii_b_checks vii_b_fail".split()}
    if a[0] != "--rand":
        g = load(a[0]); analyse(g, readstart(a[1]) if len(a) > 1 else None, acc)
    else:
        RS = "--randstart" in a; N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        for i in range(N):
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            start = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                     {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
            analyse(g, start, acc)
    print(acc)
