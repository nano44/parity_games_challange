"""L-ALG (produced on Opus 5.5, 2026-10-16 box 4). Synthetic test of candidate (LEX) (GAP-A-M §18): the actual A_DTL pruning
rounds at a FIXED context (p, R), as a function of the tangle set, computed at set level (dtl_ideal.actual_union /
survivors, the PROVED set semantics of §1). Tangles: every tangle a full DTL run stores (genuine tangles of the game), added
in RANDOM orders, not DTL's. For each prefix chain T_0 ⊂ T_1 ⊂ ... it checks: at every change of the death vector d
(stable survivors: INF), the max-index vertex whose death differs has a LARGER death in the later set (LEX), and the first
differing round set grows (LEX-R). Also every pair (T_i, T_j), i < j. Contexts: R = all vertices, p = 0, 1.
Usage: dtl_lexsynth.py [G.pg ...]  (LEXS_RANDOM random games n <= LEXS_NMAX; LEXS_ORDERS orders per context)."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_pyref as D, dtl_ideal as I, pg, gen

INF = 10 ** 6

def rounds(d, p, R, tl):
    cur = frozenset(v for v in R if d.pr[v] % 2 == p); rs = [cur]
    while cur:
        U, _ = I.actual_union(d, p, cur, R, tl)
        nx = frozenset(I.survivors(d, p, cur, R, U, tl))
        if nx == cur: break
        cur = nx; rs.append(cur)
    return rs

def deaths(rs):
    return {v: next((i for i in range(len(rs)) if v not in rs[i]), INF) for v in rs[0]}

def lexcmp(Da, Db):
    ch = [v for v in sorted(Da, reverse=True) if Da[v] != Db[v]]
    if not ch: return "EQ", None
    return ("UP" if Db[ch[0]] > Da[ch[0]] else "DOWN"), ch[0]

def roundcmp(ra, rb):
    L = max(len(ra), len(rb)); pick = lambda r, i: r[min(i, len(r) - 1)]
    r0 = next((i for i in range(L) if pick(ra, i) != pick(rb, i)), None)
    if r0 is None: return "EQ"
    a, b = pick(ra, r0), pick(rb, r0)
    return "UP" if a < b else "DOWN" if b < a else "X"

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    games = [(os.path.basename(f), pg.read(f)) for f in sys.argv[1:]]
    rnd = gen.Rng("lexsynth"); NMAX = int(os.environ.get("LEXS_NMAX", "16"))
    for i in range(int(os.environ.get("LEXS_RANDOM", "200"))):
        n = rnd.randint(5, NMAX); games.append((f"r{i}", gen.random_game(n, rnd.randint(2, n + 1), 1, rnd.randint(1, 3), rnd.next64())))
    K = int(os.environ.get("LEXS_ORDERS", "20")); prng = random.Random(1016)
    tot = {}; ex = []
    def inc(k): tot[k] = tot.get(k, 0) + 1
    for name, g in games:
        idx = sorted(range(g.n), key=lambda v: (g.prio[v], v)); new = {v: i for i, v in enumerate(idx)}
        d = D.DTL([g.prio[v] for v in idx], [g.owner[v] for v in idx], [[new[w] for w in g.succ[v]] for v in idx]); d.run()
        R = set(range(d.n))
        for p in (0, 1):
            # parity of a tangle = parity of its top priority (tpr may have been set to -1 when the tangle died)
            tl_all = [t for t in range(len(d.tv)) if max(d.pr[w] for w, _ in d.tv[t]) % 2 == p]
            # genuine tangles OF THE FULL GAME only: stored escapes = all opponent edges leaving the tangle in G
            def esc_full(t):
                C = {w for w, _ in d.tv[t]}; q = max(d.pr[w] for w in C) % 2
                return sorted({w for v in C if d.ow[v] != q for w in d.outs[v] if w not in C})
            tl_all = [t for t in tl_all if sorted(d.tout[t]) == esc_full(t)]
            if len(tl_all) < 2: continue
            for k in range(K):
                order = tl_all[:]; prng.shuffle(order)
                seq = [rounds(d, p, R, order[:j]) for j in range(len(order) + 1)]
                Ds = [deaths(r) for r in seq]
                for j in range(len(seq) - 1):
                    c, top = lexcmp(Ds[j], Ds[j + 1])
                    if c == "EQ": continue
                    inc("consec_" + c); inc("consec_round_" + roundcmp(seq[j], seq[j + 1]))
                    if c == "DOWN" and len(ex) < 5: ex.append((name, p, k, j, idx[top], Ds[j][top], Ds[j + 1][top]))
                for i in range(len(seq)):
                    for j in range(i + 1, len(seq)):
                        c, _ = lexcmp(Ds[i], Ds[j])
                        if c != "EQ": inc("pair_" + c)
    print(tot); print("examples (game, p, order#, prefix j, orig id of top changed vertex, death before, after):", ex)
