#!/usr/bin/env python3
"""gate.py-relabelled versions of the bench families (L-RED's generic gate transform, experiments/red/gate.py, used
read-only): every Even choice of a sink game is routed through a Friedmann simple cycle whose gate priority encodes a
designer label; labels here = reverse lexicographic edge index (so a first-difference rule processes edges in index
order).  Requires the family to be a 1-sink game with the sink at vertex 0 (priority 1, Odd, self-loop); families whose
vertex 0 is not such a sink are renumbered so that the FinalCycle vertex becomes 0, when one exists.
Usage: gated.py FAMILY N   (FAMILY in zadehexp, switchallexp, switchbestexp, randomfacetsubexp)"""
import sys, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "red")); sys.path.insert(0, os.path.join(ROOT, "experiments", "harness"))
import gate, pg

fam, N = sys.argv[1], int(sys.argv[2])
if fam in ("zadehexp", "randomfacetsubexp"):
    txt = subprocess.run(["python3", os.path.join(HERE, "gens.py"), fam, str(N)], capture_output=True, text=True).stdout
else:
    txt = subprocess.run(["python3", os.path.join(ROOT, "experiments", "hard-families", "pgsolver_port.py"), fam, str(N)], capture_output=True, text=True).stdout
g = pg.parse(txt)
# find the sink: an Odd vertex with a self-loop as its only edge and the unique minimum priority
cands = [v for v in range(g.n) if g.owner[v] == 1 and g.succ[v] == [v] and g.prio[v] == min(g.prio) and g.prio.count(g.prio[v]) == 1]
assert cands, "no unique sink"
s = cands[0]; perm = [s] + [v for v in range(g.n) if v != s]; inv = {v: i for i, v in enumerate(perm)}
prio = [g.prio[v] for v in perm]; owner = [g.owner[v] for v in perm]; succ = [[inv[w] for w in g.succ[v]] for v in perm]
if prio[0] != 1:                       # shift so that the sink has priority 1 and all others > 1 (parities kept)
    d = prio[0] - 1; prio = [p - d if p - d >= 1 else p - d + 2 * ((1 - (p - d) + 1) // 2) for p in prio]; prio[0] = 1
    assert all(p > 1 for p in prio[1:]) and all((prio[i] - g.prio[perm[i]]) % 2 == 0 for i in range(g.n))
labels = {}
k = 1
for v in range(g.n):
    if owner[v] == 0 and len(succ[v]) >= 2:
        for w in succ[v]:
            labels[(v, w)] = k; k += 1
labels = {e: k - l for e, l in labels.items()}        # reverse: lowest index = highest label
P, O, S, names = gate.gate(prio, owner, succ, labels)
sys.stdout.write(gate.dumps(P, O, S, names))
