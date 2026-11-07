#!/usr/bin/env python3
"""L-RED 55 R218 (copied from r217): cross-checks of a genome G.
(1) own.py trajectory == box191 idealcyc.run trajectory, state by state (mover option tuples);
(2) box191 subrun191.labels counts (C / R / p);
(3) Gamma3(G) = box189 gamma3.build(G, all pads) written as .pg: Oink 8fbf0a7 --zlk regions vs N5'-xi impl 1 (box190 n5v.py mode xi,
    env WT) and impl 2 (n5bxi.py, env WT2), iteration counts of n5v xi / spec and n5bxi; harness verify.check on both strategies.
Usage: xcheck.py G.json ..."""
import sys, os, json, subprocess, importlib.util
WT, WT2, WT3 = os.environ["WT"], os.environ["WT2"], os.environ["WT3"]
sys.path[:0] = [os.path.join(WT3, "experiments/new/box191"), os.path.join(WT, "experiments/new/box190"), os.path.join(WT, "experiments/harness")]
import idealcyc, subrun191, gamma3, n5v, pg, verify
import own
sys.path.insert(0, os.path.join(WT2, "experiments/n5-second")); sys.path.insert(0, os.path.join(WT2, "experiments/new/box190"))
sp = importlib.util.spec_from_file_location("n5bxi", os.path.join(WT2, "experiments/new/box190/n5bxi.py")); n5bxi = importlib.util.module_from_spec(sp); sp.loader.exec_module(n5bxi)
OINK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../tools/oink/build/oink")
def topg(g):
    return f"parity {g.n - 1};\n" + "".join(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n" for v in range(g.n))
for f in sys.argv[1:]:
    G = json.load(open(f)); a = idealcyc.run(G); o, V, O, _ = own.run(G)
    inv = {V[("g", (x, k))]: k for x in range(G["N"]) for k in range(len(G["opts"][x]))}
    ob = [tuple(inv[v] for v in s) for s, _, _ in o]
    lab = subrun191.labels(G)
    g, sig, tau, _ = gamma3.build(G, {"K", "pe", "pb", "m"}); p = f[:-5] + "_g3.pg"; open(p, "w").write(topg(g))
    subprocess.run([OINK, "--zlk", p, p + ".sol"], capture_output=True, check=True)
    ref = {}
    for line in open(p + ".sol"):
        w = line.replace(";", "").split()
        if len(w) >= 2 and w[0] != "paritysol": ref[int(w[0])] = int(w[1])
    gp = pg.parse(open(p).read())
    st, fb, E = n5v.run(gp, "xi", cap=100000); w1, s1 = n5v.solution(gp, st, E)
    ss, _, _ = n5v.run(gp, "spec", cap=100000)
    w2, s2, it2, fb2 = n5bxi.N5xi(gp, mode="spec").run()
    s1w = [s1[v] if w1[v] == gp.owner[v] else None for v in range(gp.n)]
    okr = all(w1[v] == ref[v] == w2[v] for v in range(gp.n)); e1, e2 = verify.check(gp, w1, s1w), verify.check(gp, w2, s2)
    print(f"{os.path.basename(f)} N {G['N']} traj own==idealcyc {ob == a} (T {len(a) - 1}) | subrun191 C {lab.count('C')} R {lab.count('R')} "
          f"p {lab.count('p')} | Gamma3 n {gp.n}: n5v xi {len(st) - 1} (fb {fb}) spec {len(ss) - 1} n5bxi {it2} (fb {fb2}) | regions=Oink {okr} "
          f"verify {len(e1)}/{len(e2)}", flush=True)
