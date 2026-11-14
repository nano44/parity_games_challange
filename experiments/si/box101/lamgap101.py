#!/usr/bin/env python3
"""L-SI box 101: Lemma LAM-GAP on random one-player games (all vertices Even; VJ order and valuation from L-RED 65's own.py at
claude/l-red 59daaef2, read-only, env RED). Howard: every vertex with a strictly better successor (by VJ value) moves to a best one,
keeping the current one if best; ties: random among the best (rule rnd) or larger index (rule idx). Ch = vertices with >= 2 successors.
A window = a maximal run of states with Lambda(v) constant for EVERY vertex v. Must-0 counters (unit run):
  gapfail  = runs with a window of more than |Ch| + 1 iterations (states a..b with b - a > |Ch| + 1)
  optfail  = runs with a state t = a + |Ch| inside a window (t <= b) at which some value differs from opt(v) := the best VJ value of a
             simple path from v to Lambda_t(v) (brute force; only for n <= NOPT)
  lfail    = runs longer than (#Lambda-change steps + 1) * (|Ch| + 2)
  pathfail = runs with a state t in a window [a, b] and a simple path P from a vertex v to a vertex l with Lambda_t(l) = l (any l),
             with at most t - a choice vertices before l, such that val_t(v) is below value(P) = (l, Pi(P), |P|) (the induction claim of the
             proof; n <= NOPT)
Control CTRL=1: the bound |Ch| + 1 replaced by floor(|Ch| / 2) (must fire on long fuses).
Usage: lamgap101.py SEED COUNT NMAX [NOPT]"""
import sys, os, random, functools
sys.path.insert(0, os.path.join(os.environ["RED"], "experiments/red/r221q"))
import own
CTRL = os.environ.get("CTRL") == "1"
PC = 1 if os.environ.get("PCTRL") == "1" else 0   # PCTRL=1: control for pathfail (paths with <= k + 1 choice vertices; must fire)
def game(rng, n):
    prio = rng.sample(range(2 * n + 2), n)
    succ = []
    for v in range(n):
        d = rng.choice([1, 1, 2, 2, 3]); succ.append(sorted(set(rng.sample(range(n), min(d, n)))))
    # half the time, add a fuse: a long path v_i -> v_(i+1) with a shortcut at the end
    return prio, succ
def run(prio, succ, rng, rule, cap=10000):
    n = len(prio); vj = own.VJ(prio); key = functools.cmp_to_key(vj.cmp)
    sig = [rng.choice(s) for s in succ]; out = []
    for _ in range(cap):
        vals = [vj.val(v, sig) for v in range(n)]; out.append((list(sig), vals))
        ns = list(sig); ch = False
        for v in range(n):
            best = max(key(vals[w]) for w in succ[v])
            if best > key(vals[sig[v]]):
                B = [w for w in succ[v] if not key(vals[w]) < best]
                ns[v] = max(B) if rule == "idx" else rng.choice(B); ch = True
        if not ch: return out, vj
        sig = ns
    return out, vj
def opt(v, lam, succ, vj):
    # best VJ value (lam, Pi, len) over simple paths v -> lam (lam's own value is (lam, {}, 0))
    key = functools.cmp_to_key(vj.cmp); best = [None]
    def dfs(u, seen, path):
        if u == lam:
            val = (lam, frozenset(x for x in path if vj.rk[x] > vj.rk[lam]), len(path))
            if best[0] is None or key(val) > key(best[0]): best[0] = val
            return
        for w in succ[u]:
            if w not in seen: dfs(w, seen | {w}, path + [u])
    dfs(v, {v}, []); return best[0]
def paths(v, tops, succ, vj):
    # all simple paths v -> l for l in tops: (l, Pi, len, #choice vertices before l)
    res = []
    def dfs(u, seen, path):
        if u in tops:
            res.append((u, frozenset(x for x in path if vj.rk[x] > vj.rk[u]), len(path), sum(1 for x in path if len(succ[x]) >= 2)))
            if u != v or path: return
        for w in succ[u]:
            if w not in seen or (w in tops and w != v): dfs(w, seen | {w}, path + [u])
    dfs(v, {v}, []); return res
def main():
    seed, cnt, nmax = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); nopt = int(sys.argv[4]) if len(sys.argv) > 4 else 7
    rng = random.Random(seed); tot = dict(pathfail=0, pathchecked=0, runs=0, gapfail=0, optfail=0, lfail=0, optchecked=0); mx = (0, 0); maxT = 0
    for i in range(cnt):
        n = rng.randint(2, nmax); prio, succ = game(rng, n)
        if rng.random() < 0.3:   # fuse: path 0 -> 1 -> ... -> n-1 plus random extra edges
            for v in range(n - 1):
                if v + 1 not in succ[v]: succ[v] = sorted(succ[v] + [v + 1])
        Ch = sum(1 for s in succ if len(s) >= 2); bound = Ch // 2 if CTRL else Ch + 1
        for rule in ("rnd", "idx"):
            out, vj = run(prio, succ, rng, rule); T = len(out) - 1; tot["runs"] += 1; maxT = max(maxT, T)
            lam = [tuple(v[0] for v in vals) for sig, vals in out]
            cuts = [0] + [t for t in range(1, len(out)) if lam[t] != lam[t - 1]] + [len(out)]
            lsteps = len(cuts) - 2; gf = of = pf = 0
            for a, b1 in zip(cuts, cuts[1:]):
                b = b1 - 1
                if b - a > bound: gf = 1
                if mx[0] < b - a: mx = (b - a, Ch)
                if n <= nopt and not CTRL:
                    for t in range(a, b + 1):
                        vals = out[t][1]; tops = {v for v in range(n) if vals[v][0] == v}; k = t - a
                        for v in range(n):
                            for (l, Pi, ln, c) in paths(v, tops, succ, vj):
                                if c <= k + PC and vj.cmp(vals[v], (l, Pi, ln)) < 0: pf = 1
                                tot["pathchecked"] += c <= k
                t = a + Ch
                if t <= b and n <= nopt and not CTRL:
                    tot["optchecked"] += 1
                    vals = out[t][1]
                    for v in range(n):
                        o = opt(v, vals[v][0], succ, vj)
                        if o is None or vj.cmp(o, vals[v]) != 0: of = 1; break
            tot["pathfail"] += pf; tot["gapfail"] += gf; tot["optfail"] += of; tot["lfail"] += int(T > (lsteps + 1) * (Ch + 2))
    print("TOTAL", " ".join("%s %d" % kv for kv in tot.items()), "max_window", mx[0], "at_Ch", mx[1], "maxT", maxT, flush=True)
main()
