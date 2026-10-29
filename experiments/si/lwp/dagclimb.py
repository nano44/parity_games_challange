#!/usr/bin/env python3
"""L-SI box 26 (successor 22): climb inside the pure-length regime for CONJECTURE L-WAVE' (docs/si/N5-LWP-box26.md). Games: a DAG on
0..n-2 (edges to larger indices only) plus the unique top even sink g = n-1 (self-loop); all other priorities 0, so c = g and P = {} at every
vertex and state: no L-WAVE' event except ties / cycle appearances, and a run is one gap up to those. Mutations: add / drop a forward edge,
flip an owner, change a start choice, add a vertex (n <= NMAX). Score = grun/lwave.py maxgap (PMODE=1; > 0 is a kill); also prints the
longest fallback-free run. Usage: dagclimb.py STEPS RNGSEED N0 NMAX OUTPREFIX"""
import sys, os, random
os.environ["PMODE"] = "1"
HERE = os.path.dirname(os.path.abspath(__file__))
for p in (os.path.join(HERE, "..", "grun"), os.path.join(HERE, "..", "root"), os.path.join(HERE, "..", "runlin")): sys.path.insert(0, p)
from common import rows
from lwave import maxgap
from trace import runs
from growclimb import save
import pg

def build(own, succ):
    n = len(own) + 1; L = ["parity %d;" % (n - 1)]
    for v in range(n - 1): L.append("%d 0 %d %s;" % (v, own[v], ",".join(map(str, sorted(succ[v])))))
    L.append("%d %d 0 %d;" % (n - 1, n + (n % 2), n - 1))
    return pg.parse("\n".join(L) + "\n")

def opt_tau(own, succ):
    """Odd's optimal strategy of the min-max distance game to g (DP backwards: Even 1 + min, Odd 1 + max, ties to the smaller index).
    With TAUOPT=1 tau0 := this, so I_tau stays empty (it depends on tau alone) and the whole run is one phase."""
    m = len(own); d = [0] * (m + 1); t = {}
    for v in reversed(range(m)):
        ws = sorted(succ[v]); best = (max if own[v] else min)(d[w] for w in ws); d[v] = 1 + best
        if own[v]: t[v] = min(w for w in ws if d[w] == best)
    return t

def score(own, succ, st):
    if os.environ.get("TAUOPT") == "1":
        st = list(st)
        for v, w in opt_tau(own, succ).items(): st[v] = w
    g = build(own, succ); n = g.n
    sp = ({v: st[v] for v in range(n - 1) if own[v] == 0}, {v: st[v] for v in range(n - 1) if own[v] == 1})
    try: E, R = rows(g, sp, cap=1500)
    except (RecursionError, RuntimeError): return None
    return maxgap(g, R), max((b - a for a, b, i, j in runs(R)), default=0), g

def mutate(rng, own, succ, st, nmax):
    own, succ, st = list(own), [set(s) for s in succ], list(st); m = len(own); k = rng.random()
    if k < 0.3:
        v = rng.randrange(m); w = rng.randrange(v + 1, m + 1); succ[v].add(w)
    elif k < 0.5:
        v = rng.randrange(m)
        if len(succ[v]) > 1: x = rng.choice(sorted(succ[v])); succ[v].discard(x); st[v] = st[v] if st[v] != x else min(succ[v])
    elif k < 0.6: v = rng.randrange(m); own[v] ^= 1
    elif k < 0.9 - (0.1 if os.environ.get('NOGROW') == '1' else 0) + (0.1 if os.environ.get('NOGROW') == '1' else 0): v = rng.randrange(m); st[v] = rng.choice(sorted(succ[v]))
    else:
        if m + 1 >= nmax or os.environ.get('NOGROW') == '1': return None
        p = rng.randrange(m + 1)                  # insert a new vertex at position p; shift indices >= p (g shifts too)
        f = lambda x: x + 1 if x >= p else x
        succ = [set(map(f, s)) for s in succ]; st = [f(x) for x in st]
        nw = {rng.randrange(p + 1, m + 2) for _ in range(rng.randint(1, 3))}
        succ.insert(p, nw); own.insert(p, rng.randint(0, 1)); st.insert(p, rng.choice(sorted(nw)))
        for u in range(p):
            if rng.random() < 0.15: succ[u].add(p)
    return own, succ, st

def main():
    steps, seed, n0, nmax, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]; rng = random.Random(seed)
    m = n0 - 1; own = [rng.randint(0, 1) for _ in range(m)]
    succ = [{rng.randrange(v + 1, m + 1) for _ in range(rng.randint(1, 3))} for v in range(m)]; st = [rng.choice(sorted(s)) for s in succ]
    cur = score(own, succ, st); print("seed", cur[:2], "n", n0, flush=True)
    for it in range(steps):
        res = mutate(rng, own, succ, st, nmax)
        if res is None: continue
        sc = score(*res)
        if sc is None or sc[0] < cur[0]: continue
        if sc[0] > cur[0]:
            print("step", it, "score", sc[0], "run", sc[1], "n", sc[2].n, flush=True); save(out, sc[2], res[2] + [sc[2].n - 1])
        own, succ, st = res; cur = sc
    print("final score", cur[0], "run", cur[1], "n", cur[2].n)

if __name__ == "__main__":
    main()
