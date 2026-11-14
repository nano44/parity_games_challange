#!/usr/bin/env python3
"""L-SI box 109: L-RED's gate transform (experiments/red/gate.py, read-only) applied D times to a sink game, labels = reverse
lexicographic edge index at each round (as experiments/si/gated.py); then a rule of n6.py on the result.
Usage: gate109.py FAMILY N DEPTH MODE.. [--cap K] [--order fwd|rev|wup|wdown|pup|pdown|dup|ddown|vdown_wup|vdown_wdown|vup_wdown]
       FAMILY in switchallexp, switchbestexp (pgsolver_port), zadehexp;  order rev = experiments/si/gated.py's labels (default)
       gate109.py bland N..    L-RED's gated Bland counter under RF from its designed starts"""
import sys, os, subprocess, time
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.environ.get("ROOT109") or os.path.abspath(os.path.join(HERE, "..", "..", ".."))
av = sys.argv[1:]; sys.argv = [sys.argv[0]]
sys.path[:0] = [HERE, os.path.join(ROOT, "experiments/red")] + [os.path.join(ROOT, p) for p in ("experiments/new/box190", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
import pg, gate, n6
if av[0] == "bland":     # gate109.py bland N..: L-RED's gated Bland counter gate(G_N) (gate.py's demo) under RF from its designed starts
    import rf109
    for N in map(int, av[1:]):
        prio, owner, succ, bland = gate.dlmm_G(N); out = []
        for name, lab in (("revBland", {k: 2 * N + 1 - b for k, b in bland.items()}), ("Bland", dict(bland))):
            P, O, S, names = gate.gate(prio, owner, succ, lab); g = pg.Game(P, O, S); E = n6.Engine(g)
            for sname in ("a->a", "a->b"):
                start = list(E.initial("first"))
                for v in range(len(prio)):
                    if owner[v] == 0 and len(succ[v]) >= 2:
                        d = S[v][0]; tgt = succ[v][0] if sname == "a->a" else succ[v][1]; start[d] = next(x for x in S[d] if S[x][1] == tgt)
                out.append(f"labels {name} start {sname}: RF {rf109.run(g, start=start)['its']}")
        print(f"GB109 gate(G_{N}) n {g.n} (MSF: 2^N - 1 = {2 ** N - 1} switches, experiments/si/instances/pinned.txt): " + " | ".join(out), flush=True)
    sys.exit(0)
cap = int(av[av.index("--cap") + 1]) if "--cap" in av else 10 ** 6
order = av[av.index("--order") + 1] if "--order" in av else "rev"
fam, N, depth = av[0], int(av[1]), int(av[2]); modes = [x for x in av[3:] if not x.startswith("--") and not x.isdigit() and x != order]
if fam == "zadehexp": txt = subprocess.run([sys.executable, os.path.join(ROOT, "experiments/si/gens.py"), fam, str(N)], capture_output=True, text=True).stdout
else: txt = subprocess.run([sys.executable, os.path.join(ROOT, "experiments/hard-families/pgsolver_port.py"), fam, str(N)], capture_output=True, text=True).stdout
g = pg.parse(txt)
cands = [v for v in range(g.n) if g.owner[v] == 1 and g.succ[v] == [v] and g.prio[v] == min(g.prio) and g.prio.count(g.prio[v]) == 1]
s = cands[0]; perm = [s] + [v for v in range(g.n) if v != s]; inv = {v: i for i, v in enumerate(perm)}
prio = [g.prio[v] for v in perm]; owner = [g.owner[v] for v in perm]; succ = [[inv[w] for w in g.succ[v]] for v in perm]
if prio[0] != 1:
    d = prio[0] - 1; prio = [p - d if p - d >= 1 else p - d + 2 * ((1 - (p - d) + 1) // 2) for p in prio]; prio[0] = 1
for _ in range(depth):
    labels = {}; k = 1
    for v in range(len(prio)):
        if owner[v] == 0 and len(succ[v]) >= 2:
            for w in succ[v]: labels[(v, w)] = k; k += 1
    if order == "rev": labels = {e: k - l for e, l in labels.items()}
    elif order != "fwd":       # systematic label rules: sort the Even edges by a key; the label is the rank (1 = lowest label)
        key = {"wup": lambda e: (e[1], e[0]), "wdown": lambda e: (-e[1], e[0]), "pup": lambda e: (prio[e[1]], e[0]), "pdown": lambda e: (-prio[e[1]], e[0]),
               "dup": lambda e: (e[1] - e[0], e[0]), "ddown": lambda e: (e[0] - e[1], e[0]), "vdown_wup": lambda e: (-e[0], e[1]), "vdown_wdown": lambda e: (-e[0], -e[1]),
               "vup_wdown": lambda e: (e[0], -e[1])}[order]
        labels = {e: i + 1 for i, e in enumerate(sorted(labels, key=key))}
    prio, owner, succ, _ = gate.gate(prio, owner, succ, labels)
G = pg.Game(prio, owner, succ)
for mode in modes:
    t0 = time.time(); r = n6.run(G, mode, cap=cap)
    print(f"G109 {fam} {N} depth {depth} order {order} mode {mode} n {G.n} iterations {r['its']} switches {r['sw']} capped {r['capped']} secs {time.time() - t0:.1f}", flush=True)
