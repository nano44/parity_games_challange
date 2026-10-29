#!/usr/bin/env python3
"""L-NEW box 56 (successor 33): Theorem EXIT (docs/new/N5-SBC2-box56.md §2). For a game, computes
  FIX   = vertices from which no Even vertex with >= 2 distinct successors is reachable (their Xi is sigma-independent);
  CH    = Odd vertices with >= 2 distinct successors; H-EXIT(u): at most one successor of u outside FIX;
  H-TOP(u): u is the most relevant vertex of no cycle (no path from a successor back to u through vertices of rank < rank(u));
and along N5-SF's distinct-sigma sequence: flips(u) (sigma-bar changes at u), TIE(u) (some sigma with the minimum of Xi over succ(u)
attained twice), LOC_V (sigma-bar(u) is not a minimiser of Xi over succ(u) at a state where u is not its own cycle node; Lemma LOC-OPT).
EXIT_V: a u with H-EXIT, H-TOP and no tie that flips more than once (Theorem EXIT says never).
Usage: exit.py GAME [START] | --rand K SEED (K random games of the class, see gen())."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box54")); sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
import n5sf, pg
from n5x import load, readstart, Engine

def classes(g):
    n = g.n; succ = [sorted(set(s)) for s in g.succ]
    pred = [[] for _ in range(n)]
    for v in range(n):
        for w in succ[v]: pred[w].append(v)
    bad = [g.owner[v] == 0 and len(succ[v]) >= 2 for v in range(n)]
    reach = set(v for v in range(n) if bad[v]); st = list(reach)          # vertices that can reach an Even choice
    while st:
        w = st.pop()
        for v in pred[w]:
            if v not in reach: reach.add(v); st.append(v)
    FIX = set(range(n)) - reach
    rank = sorted(range(n), key=lambda v: (g.prio[v], v)); rk = {v: i for i, v in enumerate(rank)}
    CH = [u for u in range(n) if g.owner[u] == 1 and len(succ[u]) >= 2]
    hexit = {u: sum(w not in FIX for w in succ[u]) <= 1 for u in CH}
    def top(u):
        seen = set(); st = [w for w in succ[u]]
        while st:
            w = st.pop()
            if w == u: return True
            if w in seen or rk[w] > rk[u]: continue
            seen.add(w); st.extend(succ[w])
        return False
    htop = {u: not top(u) for u in CH}
    return FIX, CH, hexit, htop, succ

def run(g, st=None):
    FIX, CH, hexit, htop, succ = classes(g)
    E, T = n5sf.trace(g, st); T = [x for x in T if "lam" in x]; n = g.n
    seq = []
    for x in T:
        s = [x["s"][v] if g.owner[v] == 0 else -1 for v in range(n)]
        if not seq or seq[-1] != s: seq.append(s)
    VS = [E.evaluate(tuple(s)) for s in seq]
    flips = {u: 0 for u in CH}; tie = {u: False for u in CH}; loc = 0
    for j, (vs, sb) in enumerate(VS):
        for u in CH:
            ks = [E.key(vs[w]) for w in succ[u]]; mn = min(ks)
            if ks.count(mn) > 1: tie[u] = True
            if vs[u][0] != u and E.key(vs[sb[u]]) != mn: loc += 1
            if j and VS[j - 1][1][u] != sb[u]: flips[u] += 1
    good = [u for u in CH if hexit[u] and htop[u] and not tie[u]]
    exv = [u for u in good if flips[u] > 1]
    return dict(n=n, CH=len(CH), EXIT=sum(hexit.values()), TOP=sum(htop.values()), GOOD=len(good), TIES=sum(tie.values()),
                FLIPMAX_GOOD=max((flips[u] for u in good), default=0), FLIPMAX=max(flips.values(), default=0), LOC_V=loc, EXIT_V=len(exv),
                values=len(seq), SBC=sum(VS[j][1] != VS[j + 1][1] for j in range(len(VS) - 1)))

def gen(rng, n, viol=0.0):
    """random game of the class: a FIX part (Odd vertices any degree, Even degree 1; edges inside FIX), a general part (anything), Odd choice
    vertices of the general part get exactly one successor in the general part and the rest in FIX. Priorities random in 0..n."""
    f = max(2, n // 3); F = list(range(f)); Gp = list(range(f, n))
    owner = [rng.randrange(2) for _ in range(n)]; prio = [rng.randrange(n + 1) for _ in range(n)]; succ = []
    for v in range(n):
        if v < f:
            k = 1 if owner[v] == 0 else rng.choice([1, 2])
            succ.append(sorted(set(rng.choice(F) for _ in range(k))))
        elif owner[v] == 0:
            succ.append(sorted(set(rng.choice(Gp) for _ in range(rng.choice([1, 2, 3, 4])))))
        else:
            k = rng.choice([0, 1, 2]); extra = [rng.choice(Gp)] if rng.random() < viol else []   # viol: a second general successor (breaks H-EXIT)
            succ.append(sorted(set([rng.choice(Gp)] + extra + [rng.choice(F) for _ in range(k)])))
    return pg.Game(prio, owner, succ)

def rstart(rng, g):
    """a random Even start sigma_0 (Odd's tau_0 = S3); readstart format."""
    return ({v: rng.choice(sorted(set(g.succ[v]))) for v in range(g.n) if g.owner[v] == 0}, {})

if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "--rand":
        K, seed = int(a[1]), int(a[2]); viol = float(a[3]) if len(a) > 3 else 0.0; rng = random.Random(seed); agg = {}; vals = []
        for i in range(K):
            g = gen(rng, rng.randrange(12, 61), viol); r = run(g, rstart(rng, g)); vals.append(r["values"])
            for k in ("GOOD", "TIES", "LOC_V", "EXIT_V"): agg[k] = agg.get(k, 0) + r[k]
            agg["FLIPMAX_GOOD"] = max(agg.get("FLIPMAX_GOOD", 0), r["FLIPMAX_GOOD"]); agg["FLIPMAX"] = max(agg.get("FLIPMAX", 0), r["FLIPMAX"])
        print("games", K, "values mean %.1f max %d" % (sum(vals) / K, max(vals)), " ".join(f"{k}={v}" for k, v in sorted(agg.items())))
        print("EXIT PASS" if agg["EXIT_V"] == 0 and agg["LOC_V"] == 0 else "EXIT FAIL")
    else:
        r = run(load(a[0]), readstart(a[1]) if len(a) > 1 else None); print(" ".join(f"{k}={v}" for k, v in r.items()))
