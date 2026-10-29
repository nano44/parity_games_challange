#!/usr/bin/env python3
"""REFEREE-2 succ. 19 (§C of FBCK): REFEREE's FBCK-N1 extension of READER-INV Lemma (a) to a SET H (no old -> H edges): for random games G,
random dressings G' = G + H (any owners/out-degrees in H, edges into V or earlier H; here Even H vertices may have out-degree >= 2 too, which
the claim does not exclude) and random sigma on G' Even vertices, compare S1's sigmabar and Xi (cycle node, P as a VERTEX set, length) on V.
Control MUT=backedge adds one old -> H edge (must produce DIFFs).
Usage: sbar_ext.py N seed h"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-RUND"))
import rund_check as R
DC, pg = R.DC, R.pg
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-H3")); import h3_check as H
N, seed, h = map(int, sys.argv[1:4]); rng = random.Random(seed)
def vset(E, m): return frozenset(v for v in range(len(E.rank)) if m & E.bit[v])
diff = checks = 0
for i in range(N):
    nn = rng.randint(4, 14)
    g0 = DC.rand_game(rng, nn, "kO") if i % 2 else H.rand_kO(rng, nn, rng.randint(1, 4))
    prio, owner, succ = list(g0.prio), list(g0.owner), [list(x) for x in g0.succ]
    for j in range(h):
        v = nn + j; d = rng.randint(1, 3)
        succ.append(sorted(set(rng.randrange(0, v + 1) for _ in range(d)))); owner.append(rng.randint(0, 1)); prio.append(rng.randint(0, max(prio) + 1))
    if os.environ.get("MUT") == "backedge":   # control: violates "no old vertex has an edge into H"
        odds = [v for v in range(nn) if owner[v] == 1]   # at an Odd old vertex, so sigma on V stays a strategy of G
        if odds: x = rng.choice(odds); succ[x] = sorted(set(succ[x] + [nn + rng.randrange(0, h)]))
    g1 = pg.Game(prio, owner, succ)
    E0, E1 = DC.Engine(g0), DC.Engine(g1)
    for r in range(4):
        sg = [rng.choice(g1.succ[v]) if g1.owner[v] == 0 else -1 for v in range(g1.n)]
        v0, b0 = E0.evaluate(tuple(sg[:nn])); v1, b1 = E1.evaluate(tuple(sg))
        checks += 1
        bad = [v for v in range(nn) if (g0.owner[v] == 1 and b0[v] != b1[v]) or v0[v][0] != v1[v][0] or v0[v][2] != v1[v][2]
               or vset(E0, v0[v][1]) != vset(E1, v1[v][1])]
        if bad: diff += 1; print("DIFF", i, r, bad[:5], flush=True)
print(f"checks {checks} diffs {diff} (h {h}, seed {seed})")
