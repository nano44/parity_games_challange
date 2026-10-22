#!/usr/bin/env python3
"""A3: psolC on random games beyond the exhaustive range: fraction solved completely by psolB / psolQ / psolC, Thm 4 per
node, soundness, and the smallest psolC-partial games found (shrunk with a1lib.shrink while psolC stays partial and
soundness holds). Usage: a3_random.py nmin nmax K seed [--corpus] (--corpus: gen.py-style varied corpus instead of
canonical uniform games). Writes OUT/a3_random_{tag}.txt and the smallest partial instances to instances/psolc_partial_*.pg."""
import sys, os, random, json, itertools
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import a1lib, pg, zielonka, gen
from psolb import PsolB
from psolq import PsolQ
from psolc import PsolC


def st(win, ref, res):
    if any(win[v] is not None and win[v] != ref[v] for v in range(len(ref))):
        return "UNSOUND"
    return "solved" if not res else "undecided"


def psolc_partial(g):
    ref = zielonka.solve(g)
    w, _, res, _ = PsolC(g, strat=None).run()
    return bool(res) and st(w, ref, res) == "undecided"


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    nmin, nmax, K, seed = int(args[0]), int(args[1]), int(args[2]), int(args[3])
    corpus = "--corpus" in sys.argv
    rnd = random.Random(seed)
    cnt, partial = {}, []
    pats_cache = {}
    for i in range(K):
        n = rnd.randint(nmin, nmax)
        if corpus:
            g = gen.random_game(n, rnd.choice([2, 3, 4, n // 2 + 1, n + 1]), 1, rnd.choice([1, 2, 3, 5]), seed * 1000003 + i,
                                rnd.choice([0.0, 0.2, 0.5, 0.8, 1.0]), rnd.random() < 0.7)
        else:
            if n <= 6 and n not in pats_cache:
                pats_cache[n] = list(a1lib.priority_patterns(n))
            pats = pats_cache.get(n)
            prio = list(rnd.choice(pats)) if pats else [rnd.randint(0, n) for _ in range(n)]
            succ = [sorted(rnd.sample(range(n), rnd.randint(1, min(n, 3)))) for _ in range(n)]
            g = pg.Game(prio, [rnd.randint(0, 1) for _ in range(n)], succ)
        ref = zielonka.solve(g)
        wb, _, rb, _ = PsolB(g).run(); wq, _, rq, _ = PsolQ(g).run(); wc, _, rc, _ = PsolC(g, strat=None).run()
        sb, sq, sc = st(wb, ref, rb), st(wq, ref, rq), st(wc, ref, rc)
        thm4 = all(wc[v] is not None for v in range(n) if wb[v] is not None)
        qc = all(wc[v] is not None for v in range(n) if wq[v] is not None)   # psolQ-decided ⊆ psolC-decided ?
        k = (n, sb, sq, sc, thm4, qc)
        cnt[k] = cnt.get(k, 0) + 1
        if sc == "undecided":
            partial.append((g, n, g.m, sb, sq, len(rc)))
    tag = f"n{nmin}-{nmax}_K{K}_s{seed}" + ("_corpus" if corpus else "")
    lines = [f"random {tag}: {K} games"]
    agg = {}
    for (n, sb, sq, sc, thm4, qc), v in cnt.items():
        for name, val in (("psolB", sb), ("psolQ", sq), ("psolC", sc), ("thm4", thm4), ("Q⊆C", qc)):
            agg[(n, name, val)] = agg.get((n, name, val), 0) + v
    for k in sorted(agg, key=str):
        lines.append(f"{k} : {agg[k]}")
    partial.sort(key=lambda t: (t[1], t[2]))
    lines.append(f"psolC-partial games: {len(partial)}")
    os.makedirs(os.path.join(HERE, "instances"), exist_ok=True)
    for j, (g, n, m, sb, sq, u) in enumerate(partial[:5]):
        h = a1lib.shrink(g, psolc_partial)
        name = f"psolc_partial_{tag}_{j}_n{h.n}_m{h.m}"
        pg.write(h, os.path.join(HERE, "instances", name + ".pg"))
        ref = zielonka.solve(h); w, _, res, _ = PsolC(h, strat=None).run()
        lines.append(f"  found n={n} m={m} psolB={sb} psolQ={sq} undecided={u}; shrunk to n={h.n} m={h.m}: {pg.dumps(h).replace(chr(10), ' | ')} ref={ref} undecided={sorted(res)}")
    text = "\n".join(lines)
    open(os.path.join(HERE, "out", f"a3_random_{tag}.txt"), "w").write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
