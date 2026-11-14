#!/usr/bin/env python3
"""L-RED 71 R247: tables for docs/red/R247-rf.md from out/*.out and out/climbs/*.log (nothing typed by hand). Usage: summ247.py"""
import re, os, glob
H = os.path.dirname(os.path.abspath(__file__)); rd = lambda f: open(os.path.join(H, "out", f)).read().splitlines() if os.path.exists(os.path.join(H, "out", f)) else []
print("### Table 1: engine check and RF on the named families (out/engine.out; unit: iterations = applied switch sets)")
E = {}
for l in rd("engine.out"):
    t = l.split()
    if t and t[0] == "SI247": E[(t[1], t[5])] = int(t[9])
fam = lambda pre, rng, rule: ", ".join(str(E.get((pre.format(i), rule), "-")) for i in rng)
print(f"- Howard on Friedmann's G_n from iota, n = 1..6: {fam('friedmann_G{}', range(1, 7), 'howard')}; 9 * 2^n - 10 = {', '.join(str(9 * 2 ** n - 10) for n in range(1, 7))}")
print(f"- RF on Friedmann's G_n from iota, n = 1..7: {fam('friedmann_G{}', range(1, 8), 'rf')}")
print(f"- RF on Gamma3(G_k) from S3, k = 3..8: {fam('Gamma3_G{}', range(3, 9), 'rf')}")
print(f"- RF on Gamma3^top(G_k) from S3, k = 3..8: {fam('G_{}_top.pg', range(3, 9), 'rf')}; Howard there, k = 3..6: {fam('G_{}_top.pg', range(3, 7), 'howard')}")
print("\n### Table 2: where RF leaves Howard's run on Friedmann's G_n (out/viol.out)")
cur = None
for l in rd("viol.out"):
    if l.startswith("== friedmann"): cur = l[3:]
    if l.startswith("howard iterations") and cur: print(f"- {cur}: {l}")
    if l.startswith("  blocked") and cur == "friedmann_G3": print(f"  - G_3 pairs: {l.strip()}")
print("\n### Table 3: decoy k_i -> z_i -> d_i on Friedmann's G_n (out/decoy.out)")
for l in rd("decoy.out"):
    if l.startswith("DECOY247"): print("- " + l)
print("\n### Table 4: delay patches of G_n (out/patch.out; rf / howard iterations)")
P = {}
for l in rd("patch.out"):
    m = re.match(r"PATCH247 opts \[(.*?)\] n (\d+) iterations (\d+) rule iterations (\d+)", l)
    if m: P.setdefault(m.group(1), []).append((int(m.group(2)), int(m.group(3)), int(m.group(4))))
for k, v in P.items(): print(f"- [{k or 'none'}] n = {v[0][0]}..{v[-1][0]}: RF {', '.join(str(x[1]) for x in v)}; Howard {', '.join(str(x[2]) for x in v)}")
print("\n### Table 5: PGSolver families from S3 (out/pgs.out; generators = trunk experiments/hard-families/pgsolver_port.py)")
G = {}
for l in rd("pgs.out"):
    t = l.split()
    if t and t[0] == "SI247":
        m = re.match(r"(\w+)_N(\d+)", t[1]); G.setdefault((m.group(1), t[5]), []).append((int(m.group(2)), int(t[3]), int(t[9])))
for (f, rule), v in sorted(G.items()): print(f"- {f} {rule}: " + ", ".join(f"N {a} (n {b}): {c}" for a, b, c in v))
print("\n### Table 6: exhaustive maxima (out/exh_*.out)")
for f in sorted(glob.glob(os.path.join(H, "out", "exh_*.out"))):
    for l in open(f):
        if l.startswith("EXH247 n") or l.startswith("EXH247 witness") or l.startswith("EXH247 histogram"): print("- " + l.strip())
print("\n### Table 7: climbs (out/climbs/*.log; last BEST line and END line)")
for f in sorted(glob.glob(os.path.join(H, "out", "climbs", "climb_*.log")), key=lambda x: (len(x), x)):
    b = [l for l in open(f) if l.startswith("BEST")]; e = [l for l in open(f) if l.startswith("END")]
    if b: print(f"- {os.path.basename(f)}: {b[-1].strip()} | {e[-1].strip() if e else 'no END line'}")
