"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5): harvest MIXED test games for GAP-C: random games (gen.random_game,
n in [nmin, nmax], dmax = 2..4) in which some search of p has W_p(G') != {}, |W_{1-p}(G')| >= 3 and finds no dominion.
Writes them to OUTDIR and runs (K-first) / (K4-B) on them. DTL_ORDER = oink | stable. Usage: dtl_mixedgen.py OUTDIR count seed nmin nmax"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, gen, dtl_k4b as KB
if __name__ == "__main__":
    sys.setrecursionlimit(100000); out, cnt, seed, nmin, nmax = sys.argv[1], *map(int, sys.argv[2:6]); os.makedirs(out, exist_ok=True)
    rnd = random.Random(seed); kept = 0; tab = {}
    for k in range(cnt):
        n = rnd.randint(nmin, nmax); g = gen.random_game(n, rnd.randint(3, n), 1, rnd.randint(2, 4), rnd.randrange(10 ** 9))
        d0 = KB.K.P.build(g); d = KB.K4B(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.run()
        hit = False
        for tr in d.trace:
            W = tr["Wp"]; G = set(tr["G"])
            if not W or len(G - W) < 3 or tr["d1"] > tr["dom"] or "first" not in tr: continue
            hit = True; V, Z, R = tr["first"]
            key = ("regions inside W_p" if Z <= W else "REGIONS MEET W_{1-p}", "learned inside W_p" if any(C <= W for C in tr["newt"]) else "K-in VIOLATION")
            tab[key] = tab.get(key, 0) + 1
            if not Z <= W: print("K4-B VIOLATION game", k, flush=True)
        if hit: kept += 1; pg.write(g, os.path.join(out, f"mixed_{seed}_{k}.pg"))
    print(f"games {cnt}, kept {kept} mixed games;", tab)
