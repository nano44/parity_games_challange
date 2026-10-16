"""L-ALG (produced on Opus 5.5, 2026-10-16), docs/alg/GAP-A-M.md §6. Per search: the depth-0 piece sequence (context R_j, result, V/argmax, profile). For consecutive same-player searches
without a dominion: first piece j where (R_j, result) differs; classify: RES (same context, result changed), NEST (context
shrank by Dom growth of piece j-1 with the same result), FRESH (context changed otherwise). For NEST: do distances on the
common vertices go down?"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_pyref as D, dtl_ideal as I, pg, gen
from dtl_c6proto import C6

def mk(base):
    class P(base):
        def __init__(s, *a, **k):
            super().__init__(*a, **k); s.trace = []; s.depth = 0; s.ns = 0; s.dom_seen = 0
        def search(s, p):
            s.ns += 1; s.trace.append({"p": p, "pieces": [], "dom": s.dominions})
            return super().search(p)
        def search_rec(s, R, p, depth):
            # 11:20Z fix: restore the depth on return (before, every depth-0 piece after the first cut was unrecorded);
            # record the cut attractor (R of the depth-1 child) on the cutting depth-0 piece
            if depth == 1 and s.trace[-1]["pieces"]:
                s.trace[-1].setdefault("att", {})[len(s.trace[-1]["pieces"]) - 1] = frozenset(R)
            od = s.depth; s.depth = depth
            r = super().search_rec(R, p, depth); s.depth = od; return r
        def best_vertices(s, V, R, p):
            Rin = frozenset(R)
            res = super().best_vertices(V, R, p)
            if s.depth == 0:
                # profile by replay (set level, the actual or ideal rule as the class uses)
                tl = [t for t in range(len(s.tv)) if I.alive(s, t, p)]
                cur = {v for v in R if s.pr[v] % 2 == p}; prof = {}; r = 0
                while cur:
                    r += 1
                    U = I.ideal_union(s, p, cur, R, tl) if base is C6 else I.actual_union(s, p, cur, R, tl)[0]
                    nx = I.survivors(s, p, cur, R, U, tl)
                    for v in cur - nx: prof[v] = r
                    if nx == cur: break
                    cur = nx
                for v in cur: prof.setdefault(v, 99)
                s.trace[-1]["pieces"].append((Rin, res, frozenset(V), prof))
            return res
    return P

def sig(tr, j):
    """Corrected depth-0 piece state (GAP-A-M §6 CORRECTION): at a cut piece V is never read; its state is the attractor."""
    P = tr["pieces"][j]
    if os.environ.get("STATE_V") != "1" and j in tr.get("att", {}): return (P[0], P[1], "cut", tr["att"][j])
    return P[:3]

def first_diff(a, b):
    pa, pb = a["pieces"], b["pieces"]; j = 0
    while j < min(len(pa), len(pb)) and sig(a, j) == sig(b, j): j += 1
    return j

def analyse(d):
    out = {"RES": 0, "NEST": 0, "FRESH": 0, "NESTdown": 0, "same": 0}
    for a, b in zip(d.trace, d.trace[1:]):
        if a["p"] != b["p"]: continue
        if b["dom"] != a["dom"]: continue   # a dominion was found in search a: G' changes
        pa, pb = a["pieces"], b["pieces"]
        j = 0
        while j < min(len(pa), len(pb)) and sig(a, j) == sig(b, j):
            j += 1
        if j >= min(len(pa), len(pb)): out["same"] += 1; continue
        Ra, Rb = pa[j][0], pb[j][0]
        if Ra == Rb: out["RES"] += 1
        elif j > 0 and Rb < Ra and pa[j-1][1] == pb[j-1][1] and pa[j-1][2] == pb[j-1][2]:
            out["NEST"] += 1
            common = [v for v in pa[j][3] if v in pb[j][3]]
            if any(pb[j][3][v] < pa[j][3][v] for v in common): out["NESTdown"] += 1
        else: out["FRESH"] += 1
    return out


def seq(d):
    out = []
    for a, b in zip(d.trace, d.trace[1:]):
        if a["p"] != b["p"] or b["dom"] != a["dom"]:
            out.append("|"); continue
        pa, pb = a["pieces"], b["pieces"]
        j = 0
        while j < min(len(pa), len(pb)) and sig(a, j) == sig(b, j):
            j += 1
        out.append(str(j) if j < min(len(pa), len(pb)) else "*")
    return " ".join(out)

def replays(d):
    """Replays: transitions whose first-difference piece j (depth 0) is deeper than an earlier transition's j in the same
    phase (no dominion between); also the longest chain i0 < i1 < ... of piece indices each occurring after a change at
    the previous index (nested replay depth)."""
    rep, best, cur_min, chain = 0, 0, None, []
    for a, b in zip(d.trace, d.trace[1:]):
        if a["p"] != b["p"] or b["dom"] != a["dom"]:
            cur_min, chain = None, []; continue
        pa, pb = a["pieces"], b["pieces"]
        j = 0
        while j < min(len(pa), len(pb)) and sig(a, j) == sig(b, j):
            j += 1
        if j >= min(len(pa), len(pb)):
            continue
        if cur_min is not None and j > cur_min:
            rep += 1
        cur_min = j if cur_min is None else min(cur_min, j)
        # nested depth: longest strictly increasing run of first-difference indices among consecutive changes
        chain = [x for x in chain if x < j] + [j]
        best = max(best, len(chain))
    return rep, best

def level_seqs(d):
    phases, cur = [], []
    for a, b in zip(d.trace, d.trace[1:]):
        if a["p"] != b["p"] or b["dom"] != a["dom"]:
            phases.append(cur); cur = []; continue
        pa, pb = a["pieces"], b["pieces"]
        j = 0
        while j < min(len(pa), len(pb)) and sig(a, j) == sig(b, j):
            j += 1
        if j < min(len(pa), len(pb)):
            cur.append(j)
    phases.append(cur)
    return phases

def r2(ph):
    depth = [0] * len(ph); rep = 0; best = 0
    for t, j in enumerate(ph):
        prev = [u for u in range(t) if ph[u] == j]
        if not prev: continue
        u = prev[-1]; between = [w for w in range(u + 1, t) if ph[w] < j]
        if not between: continue
        rep += 1; op = between[-1]; depth[t] = 1 + depth[op]; best = max(best, depth[t])
    return rep, best

def replays2(d):
    rep = best = 0
    for ph in level_seqs(d):
        a, b = r2(ph); rep += a; best = max(best, b)
    return rep, best


def fresh_contexts(d):
    """Per phase and level j >= 1: F_j = number of DISTINCT level-j contexts in which piece j changed at least once
    (GAP-A-M.md §6: N_j <= K * C_j, so a product needs F_j to grow with j). Returns (sum_j (F_j - 1)^+, max_j F_j)."""
    tot, mx = 0, 0
    phase, F = [], {}
    def flush():
        nonlocal tot, mx
        for j, cs in F.items():
            if j >= 1:
                tot += max(0, len(cs) - 1); mx = max(mx, len(cs))
    for a, b in zip(d.trace, d.trace[1:]):
        if a["p"] != b["p"] or b["dom"] != a["dom"]:
            flush(); F = {}; continue
        pa, pb = a["pieces"], b["pieces"]
        j = 0
        while j < min(len(pa), len(pb)) and sig(a, j) == sig(b, j):
            j += 1
        if j < min(len(pa), len(pb)) and pa[j][0] == pb[j][0]:
            F.setdefault(j, set()).add(pa[j][0])
    flush()
    return tot, mx


if __name__ == "__main__":
    # usage: dtl_pieces.py [G.pg ...]: transition-level classification (RES/NEST/FRESH) and replay histogram, DTL and C6
    sys.setrecursionlimit(100000)
    games = [(f.split("/")[-1], pg.read(f)) for f in sys.argv[1:]]
    rnd = gen.Rng("pieces")
    for i in range(600):
        n = rnd.randint(8, 24); games.append((f"r{i}", gen.random_game(n, rnd.randint(2, n + 1), 1, rnd.randint(1, 3), rnd.next64())))
    for base, nm in ((D.DTL, "DTL"), (C6, "C6")):
        hist = {}; mx = (0, 0, None); cls = {}
        for name, g in games:
            idx = sorted(range(g.n), key=lambda v: (g.prio[v], v)); new = {v: i for i, v in enumerate(idx)}
            d = mk(base)([g.prio[v] for v in idx], [g.owner[v] for v in idx], [[new[w] for w in g.succ[v]] for v in idx]); d.run()
            r, dep = replays2(d)
            for k, v in analyse(d).items(): cls[k] = cls.get(k, 0) + v
            hist[(min(r, 9), dep)] = hist.get((min(r, 9), dep), 0) + 1
            if (dep, r) > mx[:2]: mx = (dep, r, name)
        print(nm, "games", len(games), "histogram (replays capped 9, depth): count", sorted(hist.items()), "max", mx, "transition classes", cls)
