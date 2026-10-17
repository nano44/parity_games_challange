"""L-ALG (produced on Opus 5.5, 2026-10-16), docs/alg/GAP-A-M.md §14: c_i = number of distinct Dom(prevV) (-1, not cut)
contexts at depth-0 piece index i in a phase (GAP-A-M §11e: carries at index i <= n(n+2) c_i). Per phase and index: c_i,
recurrences (a context seen before, left, and visited again), and the kind of the level-j transition (j < i) that moved
index i to a NEW context: 'dom' (piece j Dom(prevV), V changed), 'cut' (piece j cut, removed set changed), 'flip' (piece j's
result type changed). Usage: dtl_ctx.py [G.pg ...] (plus CTX_RANDOM random games, n <= CTX_NMAX); CTX_C6=1 for C6."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_pyref as D, dtl_pieces as P, pg, gen

def kind(a, b, j):
    ca, cb = j in a.get("att", {}), j in b.get("att", {})
    pa, pb = a["pieces"][j], b["pieces"][j]
    if ca != cb or pa[1] != pb[1]: return "flip"
    return "cut" if ca else ("dom" if pa[1] == -1 else "stable")

def analyse(d, st, name):
    phase = []
    def flush():
        if not phase: return
        L = max(len(tr["pieces"]) for tr in phase)
        for i in range(L):
            seq = [tr["pieces"][i][0] if i < len(tr["pieces"]) and tr["pieces"][i][1] == -1 and i not in tr.get("att", {}) else None for tr in phase]
            ctx = [c for c in seq if c is not None]
            ci = len(set(ctx))
            if ci > st["max_ci"][0]: st["max_ci"] = (ci, name, i, d.n)
            st["sum_ci"] += ci; st["n_idx"] += int(ci > 0)
            seen, last = set(), None
            for c in ctx:
                if c != last and c in seen: st["recur"] += 1; st["ex_rec"].append((name, i)) if len(st["ex_rec"]) < 3 else None
                seen.add(c); last = c
        for a, b in zip(phase, phase[1:]):
            j = P.first_diff(a, b)
            if j >= min(len(a["pieces"]), len(b["pieces"])): continue
            for i in range(j + 1, min(len(a["pieces"]), len(b["pieces"]))):
                pi = b["pieces"][i]
                if pi[1] == -1 and i not in b.get("att", {}) and pi[0] != a["pieces"][i][0]:
                    k = kind(a, b, j); st["new_ctx_by"][k] = st["new_ctx_by"].get(k, 0) + 1
    for k, tr in enumerate(d.trace):
        if phase and (tr["p"] != phase[-1]["p"] or tr["dom"] != phase[-1]["dom"]): flush(); phase = []
        phase.append(tr)
    flush()

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    games = [(f.split("/")[-1], pg.read(f)) for f in sys.argv[1:]]
    rnd = gen.Rng("ctx")
    for i in range(int(os.environ.get("CTX_RANDOM", "600"))):
        n = rnd.randint(8, int(os.environ.get("CTX_NMAX", "26"))); games.append((f"r{i}", gen.random_game(n, rnd.randint(2, n + 1), 1, rnd.randint(1, 3), rnd.next64())))
    base = P.C6 if os.environ.get("CTX_C6") == "1" else D.DTL
    st = dict(max_ci=(0, None, None, None), sum_ci=0, n_idx=0, recur=0, ex_rec=[], new_ctx_by={})
    for name, g in games:
        idx = sorted(range(g.n), key=lambda v: (g.prio[v], v)); new = {v: i for i, v in enumerate(idx)}
        d = P.mk(base)([g.prio[v] for v in idx], [g.owner[v] for v in idx], [[new[w] for w in g.succ[v]] for v in idx]); d.run()
        analyse(d, st, name)
    print("games", len(games), "base", base.__name__); print(st)
