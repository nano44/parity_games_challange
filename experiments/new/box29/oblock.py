#!/usr/bin/env python3
"""Box 29: inside crossing-free intervals of a phase (R constant), the maximal OTHER blocks (runs of consecutive OTHER states):
value-changing transitions per block minus (n − 1) (CONJECTURE OB: ≤ 0), and the number of state-type changes (EQ/THR/OTHER) per
crossing-free interval together with the number of F-value changes there (Lemma F1 bounds the latter by |F| − 1).
Usage: oblock.py game.pg [start] | oblock.py --rand N lo hi seed [--randstart]"""
import sys, random
from otherx import *

def typ(r):
    if r["other"]: return "O"
    return "E" if r["Xk"] == r["Wk"] else "T"

def analyse(g, start, acc):
    rows, _ = profile(g, start); o = odd_choice(g)
    for r in rows: r["R"] = reach_o(g, r["s"], r["t"], o); r["other"] = (not all(r["h"])) and r["Xk"] != r["Wk"]
    _, ph = profile(g, start)
    for (x, y) in ph:
        k = x
        while k <= y:
            j = k
            while j + 1 <= y and rows[j + 1]["R"] == rows[j]["R"]: j += 1
            F = [v for v in range(g.n) if v not in rows[k]["R"] and v != o]
            fch = sum(any(rows[i]["Xk"][v] != rows[i + 1]["Xk"][v] for v in F) for i in range(k, j))
            tch = sum(typ(rows[i]) != typ(rows[i + 1]) for i in range(k, j))
            acc["intervals"] += 1; acc["max_typech"] = max(acc["max_typech"], tch)
            acc["max_typech_minus_Fch"] = max(acc["max_typech_minus_Fch"], tch - 2 * fch)
            i = k
            while i <= j:
                if not rows[i]["other"]: i += 1; continue
                b = i
                while b + 1 <= j and rows[b + 1]["other"]: b += 1
                vc = sum(rows[q]["Xk"] != rows[q + 1]["Xk"] or rows[q]["Wk"] != rows[q + 1]["Wk"] for q in range(i, b))
                acc["blocks"] += 1; acc["OB_max_excess"] = max(acc["OB_max_excess"], vc - (g.n - 1))
                if vc > g.n - 1: acc["OB_fail"] += 1
                i = b + 1
            k = j + 1

if __name__ == "__main__":
    a = sys.argv[1:]; acc = dict(runs=0, intervals=0, blocks=0, OB_fail=0, OB_max_excess=-10**9, max_typech=0, max_typech_minus_Fch=-10**9)
    if a[0] != "--rand":
        g = load(a[0]); analyse(g, readstart(a[1]) if len(a) > 1 else None, acc); acc["runs"] = 1
    else:
        RS = "--randstart" in a; N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        for i in range(N):
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            start = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                     {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
            analyse(g, start, acc); acc["runs"] += 1
    print(acc)
