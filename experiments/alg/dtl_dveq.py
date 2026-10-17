"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5): is the author's DV (dtl_distval.distval, Oink's re-check order)
equal to the clean DV* (dtl_dvstar.dvstar, true least fixed points)? If always, Lemma DV-MONO follows from DV*-MONO.
Part 1: every tangle set T_s of every phase of the C5 corpus (DTL-learned). Part 2: random games with random genuine tangle
sets (re-indexed by priority). Usage: dtl_dveq.py games seed [G.pg ...]  (prints the first differences)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, gen, dtl_spp as P
from dtl_distval import distval
from dtl_dvstar import dvstar
from dtl_dvsynth import mkdtl, setT
from dtl_gentangle import genuine

def cmp_synth(games, seed):
    rnd = random.Random(seed); tried = diff = 0
    for k in range(games):
        n = rnd.randint(4, 11); g = gen.random_game(n, rnd.randint(2, n + 2), 1, 3, rnd.randrange(10 ** 9)); d, _ = mkdtl(g); p = rnd.randrange(2)
        tl = []
        for _ in range(40):
            t = genuine(d, p, set(rnd.sample(range(n), rnd.randint(1, min(n, 5)))), rnd)
            if t and t[1] and sorted(v for v, _ in t[0]) not in [sorted(v for v, _ in c[0]) for c in tl]: tl.append(t)
        T = [c for c in tl if rnd.random() < 0.6]; setT(d, T); G = set(range(n)); tried += 1
        a = distval(d, G, p); b = dvstar(d, G, p, [(frozenset(v for v, _ in c[0]), tuple(c[1])) for c in T])
        if a != b:
            diff += 1
            if diff <= 2: print("DIFF synthetic: internal game", [(d.pr[v], d.ow[v], d.outs[v]) for v in range(n)], "p", p, "T", [[v for v, _ in c[0]] for c in T], "DV", a, "DV*", b, flush=True)
    print(f"synthetic: {tried} (game, T) pairs, DV != DV* in {diff}")

if __name__ == "__main__":
    sys.setrecursionlimit(100000); games, seed = int(sys.argv[1]), int(sys.argv[2]); tot = dif = 0
    for f in sys.argv[3:]:
        g = pg.read(f); d = P.build(g); born = {}; orig = d.extractTangles
        def ext(top, R, d=d, orig=orig, born=born):
            k = len(d.tv); r = orig(top, R)
            for i in range(k, len(d.tv)): born[i] = d.tpr[i]
            return r
        d.extractTangles = ext; d.run(); ntv = len(d.tv); tf = list(d.tpr); sG = d.G
        rows, cur = [], []
        for t in d.trace:
            if cur and (t["p"] != cur[-1]["p"] or t["dom"] != cur[-1]["dom"]): rows.append(cur); cur = []
            cur.append(t)
        if cur: rows.append(cur)
        for ph in rows:
            p, G = ph[0]["p"], set(ph[0]["G"])
            for tr in ph:
                k = tr["t0"]; d.tpr = [born[i] if i < k and all(v in G for v, _ in d.tv[i]) else -1 for i in range(ntv)]; d.G = G
                tl = [(frozenset(v for v, _ in d.tv[i]), tuple(d.tout[i])) for i in range(ntv) if d.tpr[i] != -1 and d.tpr[i] % 2 == p]
                a = distval(d, G, p); b = dvstar(d, G, p, tl); tot += 1
                if a != b:
                    dif += 1
                    if dif <= 2: print("DIFF on DTL run", os.path.relpath(f), "p", p, "search t0", k, {d.idx[v]: (a.get(v), b.get(v)) for v in set(a) | set(b) if a.get(v) != b.get(v)}, flush=True)
            d.tpr = tf; d.G = sG
    if sys.argv[3:]: print(f"DTL runs: {tot} tangle sets, DV != DV* in {dif}")
    if games: cmp_synth(games, seed)
