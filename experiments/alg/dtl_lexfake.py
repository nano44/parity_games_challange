"""L-ALG (produced on Opus 5.5, 2026-10-16 box 4). Does candidate (LEX) (GAP-A-M §18) depend on tangle properties? Same set-
level check as dtl_lexsynth.py, but the 'tangles' are RANDOM vertex sets C (2..LEXF_MAXT vertices; parity = parity of max
priority in C; escapes = all opponent out-edges leaving C, as DTL stores them), with no strong-connectivity or dominance
requirement. Context R = all vertices. Usage: dtl_lexfake.py (LEXF_RANDOM games, n <= LEXF_NMAX, LEXF_T fake tangles each)."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_pyref as D, pg, gen
from dtl_lexsynth import rounds, deaths, lexcmp, roundcmp
from dtl_gentangle import genuine
GENUINE = os.environ.get("LEXF_GENUINE") == "1"   # 1: only genuine p-tangles (dtl_gentangle), sizes 1..LEXF_MAXT

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    TAG = os.environ.get("LEXF_SEED", ""); rnd = gen.Rng("lexfake" + TAG); prng = random.Random("7" + TAG)
    NG, NMAX, NT, MAXT = (int(os.environ.get(k, v)) for k, v in (("LEXF_RANDOM", "300"), ("LEXF_NMAX", "12"), ("LEXF_T", "12"), ("LEXF_MAXT", "5")))
    tot = {}; ex = []
    def inc(k): tot[k] = tot.get(k, 0) + 1
    for gi in range(NG):
        n = rnd.randint(5, NMAX); g = gen.random_game(n, rnd.randint(2, n + 1), 1, rnd.randint(1, 3), rnd.next64())
        idx = sorted(range(g.n), key=lambda v: (g.prio[v], v)); new = {v: i for i, v in enumerate(idx)}
        d = D.DTL([g.prio[v] for v in idx], [g.owner[v] for v in idx], [[new[w] for w in g.succ[v]] for v in idx])
        R = set(range(d.n))
        for p in (0, 1):
            d.tv, d.tout, d.tpr = [], [], []
            for _ in range(NT * (40 if GENUINE else 1)):
                if GENUINE and len(d.tv) >= NT: break
                C = prng.sample(range(d.n), prng.randint(1 if GENUINE else 2, min(MAXT, d.n)))
                if max(d.pr[w] for w in C) % 2 != p: continue
                if GENUINE:
                    gt = genuine(d, p, C, prng)
                    if gt is None or sorted(w for w, _ in gt[0]) in [sorted(w for w, _ in x) for x in d.tv]: continue
                    d.tv.append(gt[0]); d.tout.append(gt[1]); d.tpr.append(max(d.pr[w] for w in C)); continue
                esc = sorted({w for v in C if d.ow[v] != p for w in d.outs[v] if w not in C})
                d.tv.append([(w, -1) for w in C]); d.tout.append(esc); d.tpr.append(max(d.pr[w] for w in C))
            tl = list(range(len(d.tv)))
            if len(tl) < 2: continue
            for k in range(4):
                prng.shuffle(tl)
                seq = [rounds(d, p, R, tl[:j]) for j in range(len(tl) + 1)]; Ds = [deaths(r) for r in seq]
                for j in range(len(seq) - 1):
                    c, top = lexcmp(Ds[j], Ds[j + 1])
                    if c == "EQ": continue
                    inc("consec_" + c); inc("consec_round_" + roundcmp(seq[j], seq[j + 1]))
                    if c == "DOWN" and len(ex) < 3:
                        ex.append((gi, p, k, j, top, Ds[j][top], Ds[j + 1][top], g, [sorted(w for w, _ in d.tv[t]) for t in tl[:j + 1]], d.tv[tl[j]], d.tout[tl[j]]))
    print(tot)
    for e in ex: print("DOWN example: game", e[0], "p", e[1], "prefix", e[3], "top changed (internal idx)", e[4], e[5], "->", e[6])
    if ex:
        gi, p, k, j, top, a, b, g, sets, tv, tout = ex[0]
        print("game prio", g.prio, "owner", g.owner, "succ", g.succ); print("tangle sets (internal ids)", sets)
