#!/usr/bin/env python3
"""L-SI box 66: one-flip (pre, post) pairs of the external-flip model E_m (box 64 flipdp.Ext), per genome:
for every start u, bit b and flip time t on the flip-free b-run from u: pre = t, post = L_(1-b)(s_t) (flip-free afterwards).
pairs(G) = set of attained (pre, post, stuck) with stuck = (t is the end of the b-run).
Usage: front.py genome.json ...                 print the Pareto frontier of each genome
       front.py --climb m p seed iters outdir   hill-climb max post subject to pre >= p (lower bounds on the m-level frontier;
                                                live outputs in outdir, NOT pinned)"""
import sys, os, json, itertools, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box64"))
from flipdp import Ext

def pairs(G):
    E = Ext(G); states = list(itertools.product(*[range(len(E.opts[v])) for v in E.UP]))
    nxt = {(u, b): E.step(u, b) for u in states for b in (0, 1)}; L = {}
    def run(u, b):
        if (u, b) not in L:
            seq = [u]
            while nxt[(seq[-1], b)] != seq[-1]: seq.append(nxt[(seq[-1], b)])
            L[(u, b)] = seq
        return L[(u, b)]
    P = set()
    for u in states:
        for b in (0, 1):
            seq = run(u, b)
            for t, st in enumerate(seq): P.add((t, len(run(st, 1 - b)) - 1, t == len(seq) - 1))
    return P

def frontier(P):
    pts = {(a, c) for a, c, _ in P}
    return sorted(p for p in pts if not any(q != p and q[0] >= p[0] and q[1] >= p[1] for q in pts))

if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "--climb":
        sys.path.insert(0, os.path.join(HERE, "..", "box64")); from climb import rand_iso, mutate
        m, p, seed, iters, out = int(a[1]), int(a[2]), int(a[3]), int(a[4]), a[5]; rng = random.Random(seed); os.makedirs(out, exist_ok=True)
        def sc(G):
            try: P = pairs(G)
            except AssertionError: return None
            v = [c for (t, c, _) in P if t >= p]; return (max(v) if v else -1, max(t for t, _, _ in P))
        cur = None
        while cur is None:
            G = rand_iso(m + 1, rng); s = sc(G)
            if s: cur, cs = G, s
        best = cs; stale = 0
        for it in range(iters):
            H = mutate(cur, rng); s = sc(H)
            if s is None: continue
            if s >= cs: stale = 0 if s > cs else stale; cur, cs = H, s
            else: stale += 1
            if cs > best:
                best = cs; json.dump(cur, open(os.path.join(out, "f_m%d_p%d_s%d.json" % (m, p, seed)), "w"))
                print("it", it, "pre>=%d max post" % p, best[0], "frontier", frontier(pairs(cur)), flush=True)
            if stale > 3000:
                G = rand_iso(m + 1, rng); s = sc(G)
                if s: cur, cs, stale = G, s, 0
        print("FINAL m", m, "p", p, "best", best)
    else:
        for f in a:
            P = pairs(json.load(open(f))); print(os.path.basename(f), "frontier", frontier(P),
                  "max pre+post", max(t + c for t, c, _ in P))
