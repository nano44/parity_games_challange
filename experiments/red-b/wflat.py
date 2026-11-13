#!/usr/bin/env python3
"""B3 (L-RED-B successor 3): direct test of the claim FLAT-IDX (L-RED-B reading, not proved; docs/red-b/B3-guide.md §3) on the
FLAT wrapper W(H, s0) of L-SI's wrap104.py (claude/l-si 2051a0ee, git archive): before the first fallback of N5 (SPEC, L-NEW's
box190/n5v.py mode spec) from S3 on W, at every iteration j and every Even vertex v of H,
   sigma_(j+1)(v) = the option of least position in H.succ[v] among {sigma_j(v)} and the improving options Isigma_j(v),
so the position of sigma(v) never increases and the iterations that move some Even vertex of H number <= sum_v (deg(v) - 1).
Counters (must be 0 under ALG=spec while tau stays standard at the gates; unit (iteration, Even vertex of H) unless stated):
  idxinc   the position of sigma(v) increases;  notmin  sigma_(j+1)(v) is not the least-position option of {sigma_j(v)} + I_j(v);
  hbound   [game] iterations with an H-move > sum_v (deg(v) - 1);   taunstd [iteration] tau not standard at some gate (premise; DATA)
CONTROL: ALG=xi (N5'-xi: Howard's best-value choice) must fire idxinc / notmin on some games.
Usage: wflat.py B3ROOT ALG rand SEED COUNT NMAX | ALG fam FAMILY n...      (FAMILY fried | lmcs | hn)"""
import sys, os, random
root = os.path.abspath(sys.argv[1]); ALG = sys.argv[2]
os.environ["LNEW"] = os.path.join(root, "lnew"); os.environ["LRED"] = os.path.join(root, "lred")
os.environ["LLIT"] = os.path.join(root, "llit"); os.environ["HN"] = os.path.join(root, "lcomp/experiments/friedmann-hn")
os.environ["ALG"] = ALG
sys.path.insert(0, os.path.join(root, "lsi/experiments/si/box104"))
import wrap104 as W
from wrap104 import pg, n5v, n5, n5x, gen
from si import Engine

def one(H, s0, tag):
    g, std_s, std_t, mp, inv = W.wrap(H, s0); E, Ed = Engine(g), Engine(n5.dual(g))
    ev = [v for v in range(H.n) if H.owner[v] == 0]
    pos = {(v, w): H.succ[v].index(w) for v in ev for w in H.succ[v]}
    sigma, tau = n5x.start_pair(g, E, Ed, None)
    c = dict(idxinc=0, notmin=0, hbound=0, taunstd=0); its = 0; F1 = None; hit = 0
    gates = [x for x in std_t if g.owner[x] == 1 and x not in range(H.n)]
    while its < 10 ** 6:
        r = n5v.step(g, E, Ed, sigma, tau, ALG)
        if r is None: break
        ns, nt, Is, It, fb = r; its += 1
        if fb and F1 is None: F1 = its
        if F1 is None:
            if any(tau[x] != std_t[x] for x in gates): c["taunstd"] += 1
            moved = False
            for v in ev:
                a, b = inv[sigma[v]], inv[ns[v]]
                opts = [a] + [inv[w] for (x, w) in Is if x == v]
                want = min(opts, key=lambda w: pos[(v, w)])
                if pos[(v, b)] > pos[(v, a)]: c["idxinc"] += 1
                if b != want: c["notmin"] += 1
                moved |= (a != b)
            hit += moved
        sigma, tau = ns, nt
    bound = sum(len(H.succ[v]) - 1 for v in ev)
    if hit > bound: c["hbound"] += 1
    print("WFLAT alg %s %s |H| %d |W| %d iterations %d first fallback %s H-move iterations %d bound %d | %s" % (
        ALG, tag, H.n, g.n, its, F1, hit, bound, " ".join("%s %d" % kv for kv in c.items())), flush=True)
    return c

tot = dict(idxinc=0, notmin=0, hbound=0, taunstd=0); fired = dict(tot); cnt = 0
if sys.argv[3] == "rand":
    seed, count, nmax = int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]); rng = random.Random(seed)
    for i in range(count):
        n = rng.randint(2, nmax)
        H = gen.random_game(n, rng.randint(2, n + 1), 1, 3, seed * 100000 + i)
        s0 = [rng.choice(H.succ[v]) if H.owner[v] == 0 else -1 for v in range(H.n)]
        c = one(H, s0, "rand%d_%d" % (seed, i)); cnt += 1
        for k in tot: tot[k] += c[k]; fired[k] += int(c[k] > 0)
else:
    name = sys.argv[4]
    for n in map(int, sys.argv[5:]):
        if name == "fried": r = W.fried_game(n); H, s0 = r[0], list(r[1])
        elif name == "lmcs": H, s0 = W.lmcs_game(n, "fig4"); s0 = list(s0)
        else:
            sys.path.insert(0, os.environ["HN"]); import hn
            H, ix = hn.build(n, "fig"); io = hn.iota(n, ix); s0 = [io.get(v, H.succ[v][0]) if H.owner[v] == 0 else -1 for v in range(H.n)]
        c = one(H, s0, "%s_n%d" % (name, n)); cnt += 1
        for k in tot: tot[k] += c[k]; fired[k] += int(c[k] > 0)
print("WFLAT SUMMARY alg %s games %d | units: %s | games with the counter > 0: %s" % (ALG, cnt, " ".join("%s %d" % kv for kv in tot.items()),
      " ".join("%s %d" % kv for kv in fired.items())), flush=True)
