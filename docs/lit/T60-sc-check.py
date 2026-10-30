#!/usr/bin/env python3
"""L-LIT T60 (docs/lit/T60-best-reply-flips.md §3): does Odd's best reply sigma-bar inside one W-run of N5 meet the single-crossing
hypothesis of monotone comparative statics (Milgrom-Shannon; as stated in Etessami et al. arXiv 1909.03210 §5.1)?
W-runs as in docs/lit/T59-dz-check.py / T58-elim-check.py (tau fixed, no fallback, W's cycle nodes fixed). For an Odd o and a W-run
F = p..q, Odd's objective at state t is f(w, t) := -Xi_t(w) over w in succ(o) (si.py Engine.key order; Odd minimizes Xi).
  SB      max over o of the number of transitions of F at which sigma-bar(o) changes (L-SI's SB_F(o));
  PF      max over o and pairs {w1, w2} of succ(o) of the number of STRICT order reversals of (Xi_t(w1), Xi_t(w2)) along F
          (a reversal: the last strict order seen and the current strict order differ; ties are skipped);
  SC1     the number of (run, o) with some pair reversing more than once (single crossing in t fails for every order of succ(o));
  CYC     the number of (run, o) where every pair reverses at most once but the reversal directions are cyclic (no linear order of
          succ(o) has single crossing);
  SCOK    the number of (run, o) with SB > 0 where a single-crossing order exists (then Topkis/Milgrom-Shannon bounds SB(o) by
          deg(o) - 1 under a monotone tie selection);
  OVER    the number of (run, o) with SB > deg(o) - 1 although a single-crossing order exists (tie selection not monotone);
  SBDEG   the (SB, deg) of the vertex attaining SB.
Usage (repo root): python3 -I docs/lit/T60-sc-check.py GAME.pg [START]"""
import sys, os, itertools
HERE = os.path.dirname(os.path.abspath(__file__))
import importlib.util
def _load(name, fn):
    sp = importlib.util.spec_from_file_location(name, os.path.join(HERE, fn)); m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m); return m
t59 = _load("t59", "T59-dz-check.py")
from n5x import load, readstart, Engine

def acyclic(nodes, arcs):
    indeg = {x: 0 for x in nodes}
    for a, b in arcs: indeg[b] += 1
    st = [x for x in nodes if indeg[x] == 0]; seen = 0
    while st:
        x = st.pop(); seen += 1
        for a, b in arcs:
            if a == x:
                indeg[b] -= 1
                if indeg[b] == 0: st.append(b)
    return seen == len(nodes)

def run(g, start=None):
    n = g.n; own = g.owner; E = Engine(g)
    c = dict(RUNS=0, LEN=0, SB=0, PF=0, SC1=0, CYC=0, SCOK=0, OVER=0, SBDEG=(0, 0), FLIPS=0)
    for F, _ in t59.wruns_t(g, start):
        if len(F) < 2: continue
        c['RUNS'] += 1; c['LEN'] = max(c['LEN'], len(F) - 1)
        ev = [E.evaluate(s) for s in F]; K = [[E.key(x) for x in val] for val, _ in ev]
        for o in range(n):
            if own[o] != 1 or len(E.succ[o]) < 2: continue
            br = [tb[o] for _, tb in ev]
            sb = sum(1 for i in range(len(F) - 1) if br[i + 1] != br[i]); c['FLIPS'] += sb
            if sb > c['SB']: c['SB'] = sb; c['SBDEG'] = (sb, len(E.succ[o]))
            succ = E.succ[o]; worst = 0; arcs = []
            for w1, w2 in itertools.combinations(succ, 2):
                last = 0; rev = 0; first = 0
                for k in K:
                    s = (k[w1] > k[w2]) - (k[w1] < k[w2])
                    if s == 0: continue
                    if last and s != last:
                        rev += 1
                        if rev == 1: arcs.append((w1, w2) if s > 0 else (w2, w1))   # w1 overtakes w2 upward: Odd's preference moves to w2
                    last = s
                worst = max(worst, rev)
            c['PF'] = max(c['PF'], worst)
            if sb == 0: continue
            if worst > 1: c['SC1'] += 1
            elif not acyclic(succ, arcs): c['CYC'] += 1
            else:
                c['SCOK'] += 1
                if sb > len(succ) - 1: c['OVER'] += 1
    return c

if __name__ == '__main__':
    a = sys.argv[1:]; g = load(a[0]); c = run(g, readstart(a[1]) if len(a) > 1 else None)
    print(f"T60 {os.path.basename(a[0])} n {g.n} " + " ".join(f"{k} {v[0]}/{v[1]}" if isinstance(v, tuple) else f"{k} {v}" for k, v in c.items()))
