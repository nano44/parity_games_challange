#!/usr/bin/env python3
"""Box 22: sfb.py (N5-SF on n5b) vs L-NEW's n5sf.py (verbatim copy, n5x engine): full state sequences (σ on Even, τ on Odd), SBC_σ, SBC_τ.
Usage: sfxcheck.py GAME.pg ... | --random SEED COUNT NMAX"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); EXP = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(EXP, "n5-box20", "lnew_box54"))
import sfb, n5sf, pg
from n5x import Engine, dual


def cmp(g, sd):
    e = sfb.B.Eng(g); st = e.start()
    if sd:
        s, t = map(list, st)
        for v, w in sd[0].items(): s[v] = w
        for v, w in sd[1].items(): t[v] = w
        st = (tuple(s), tuple(t))
    A = sfb.run(g, st); E, T = n5sf.trace(g, ({v: st[0][v] for v in range(g.n) if g.owner[v] == 0}, {v: st[1][v] for v in range(g.n) if g.owner[v] == 1}))
    T2 = [x for x in T if "lam" in x]; Ed = Engine(dual(g)); tb = [tuple(Ed.evaluate(tuple(x["t"]))[1]) for x in T2]
    ev = lambda s, own: tuple(s[v] for v in range(g.n) if g.owner[v] == own)
    same = len(A["states"]) == len(T2) and all(ev(a[0], 0) == ev(b["s"], 0) and ev(a[1], 1) == ev(b["t"], 1) for a, b in zip(A["states"], T2))
    sbs = sum(T2[i]["sb"] != T2[i + 1]["sb"] for i in range(len(T2) - 1)); sbt = sum(tb[i] != tb[i + 1] for i in range(len(T2) - 1))
    return same and (sbs, sbt) == (A["sbc_sigma"], A["sbc_tau"]), A


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "--random":
        rnd = random.Random(int(a[1])); bad = 0; cnt = int(a[2]); nmax = int(a[3])
        for k in range(cnt):
            n = rnd.randint(2, nmax); own = [rnd.randint(0, 1) for _ in range(n)]; p = -1; pr = []
            for v in range(n): p += 1 if rnd.random() < 0.5 else 2; pr.append(p)
            succ = [sorted(rnd.sample(range(n), rnd.randint(1, min(n, 3)))) for _ in range(n)]; g = pg.Game(pr, own, succ)
            sd = ({v: rnd.choice(succ[v]) for v in range(n) if own[v] == 0}, {v: rnd.choice(succ[v]) for v in range(n) if own[v] == 1})
            ok, _ = cmp(g, sd if k % 2 else None); bad += not ok
            if not ok: print("MISMATCH", pr, own, succ, sd if k % 2 else "S3")
        print(f"SFXCHECK random games {cnt} mismatches {bad}")
    else:
        for path in a:
            ok, A = cmp(pg.read(path), None); print("SFXCHECK", os.path.basename(path), "OK" if ok else "MISMATCH", "it", A["it"], "sbc", A["sbc_sigma"], A["sbc_tau"])
