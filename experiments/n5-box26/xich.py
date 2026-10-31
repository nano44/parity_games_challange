#!/usr/bin/env python3
"""L-COMP box 26 (Lead 04:38Z): XICH_F(v) := the transitions of a W-run F at which Ξ(v) changes (RESULTS R95: WRUN-POLY ⟺ XI-CH-POLY),
my own count on n5b (SPEC). W-runs as n5-box23/rstar.wruns (R89). Ξ_t := n5b's VJ valuation of σ_t (SpecSI.evaluate, as n5b's step uses).
Per W-run: |F|, max_v XICH_F(v) (and the vertex), Σ_v XICH_F(v), the longest W-constant interval |I| inside F (W_t = W_{t+1}), and the
number of vertices whose Ξ changes at least once. Per game: the W-run with the largest max XICH (ties: larger |F|, then larger |I|).
Usage: xich.py GAME.pg [START] [-v]"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(ROOT, "n5-box23"))
import rstar  # noqa: E402
import n5b  # noqa: E402
import pg  # noqa: E402


def analyse(g, start=None, cap=None):
    eng = rstar.Eng(g); x = start or eng.start(); states, fbs, data = [], [], []
    while True:
        states.append(x); data.append(eng.sdata(*x)); nx = eng.step(*x)
        if nx is None:
            break
        if cap and len(states) > cap:
            raise n5b.RepeatedState("cap")
        fbs.append(nx[2]); x = (nx[0], nx[1])
    XI = [eng.N.SG.evaluate(list(s)) for s, _ in states]
    runs = []
    for a, b in rstar.wruns(eng, states, fbs, data):
        ch = [sum(1 for t in range(a, b) if XI[t + 1][v] != XI[t][v]) for v in range(g.n)]
        m = max(ch); W = [data[t]["W"] for t in range(a, b + 1)]
        longest = cur = 0
        for t in range(b - a):
            cur = cur + 1 if W[t + 1] == W[t] else 0; longest = max(longest, cur)
        runs.append(dict(a=a, b=b, F=b - a, max=m, arg=ch.index(m), sum=sum(ch), nz=sum(1 for c in ch if c), I=longest))
    return states, runs


def best(runs):
    return max(runs, key=lambda r: (r["max"], r["F"], r["I"]), default=None)


def main():
    g = pg.read(sys.argv[1]); args = [x for x in sys.argv[2:] if x != "-v"]
    st = rstar.overlay(g, rstar.Eng(g).start(), n5b.read_start(args[0], g)) if args else None
    states, runs = analyse(g, st)
    r = best(runs)
    tot = max((x["sum"] for x in runs), default=0)
    print(f"XICH n {g.n} it {len(states) - 1} runs {len(runs)} maxXICH {r['max'] if r else 0} (v {r['arg'] if r else -1}) "
          f"F {r['F'] if r else 0} sum {r['sum'] if r else 0} I {r['I'] if r else 0} | max|F| {max((x['F'] for x in runs), default=0)} "
          f"maxsum {tot}")
    if "-v" in sys.argv:
        for x in runs:
            print(" ", x)


if __name__ == "__main__":
    main()
