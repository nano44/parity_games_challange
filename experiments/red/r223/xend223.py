#!/usr/bin/env python3
"""L-RED 58 R223 item 1: ENDGAME-3 / ENDGAME-3-N5 / EXACT-L (P-N5-END, claude/l-new 131b4c1c) on the SECOND implementations, which share
no valuation code with n5v: N5 = L-COMP's experiments/n5-second/n5b.py (mode spec, start S3 = its initial_strategy_by_best_reward,
fbtrace gives each fallback's position), N5'-xi = box190 n5bxi.py (fallback count only). Gamma3(G) = frozen box189 gamma3.build.
Regions checked against Oink 8fbf0a7 --zlk (tools/oink/build/oink, scripts/setup_oink.sh); strategies by harness verify.check.
Per genome: n5b: fallbacks == 1 and total == F + 2; n5bxi: fallbacks == 1 and total == (n5v xi total, via end222.check);
n5b total == n5v spec total. Counter: genomes with any failure (unit: genome). Usage: xend223.py OUTDIR G.json ... | --fam FAM SEED CNT
(env WT = WT3 = worktree of claude/l-new 131b4c1c)"""
import sys, os, json, random, subprocess, importlib.util
here = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(here, "../r222")]
import end222
WT = os.environ["WT"]
sys.path[:0] = [os.path.join(WT, "experiments/n5-second"), os.path.join(WT, "experiments/hard-families")]
import n5b, pg, verify, gamma3
sp = importlib.util.spec_from_file_location("n5bxi", os.path.join(WT, "experiments/new/box190/n5bxi.py")); n5bxi = importlib.util.module_from_spec(sp); sp.loader.exec_module(n5bxi)
OINK = os.path.join(here, "../../../tools/oink/build/oink")
def one(G, tag, outdir):
    g, _, _, _ = gamma3.build(G, {"K", "pe", "pb", "m"}); p = os.path.join(outdir, "_x223.pg"); open(p, "w").write(end222.topg(g))
    gp = pg.parse(open(p).read())
    subprocess.run([OINK, "--zlk", p, p + ".sol"], capture_output=True, check=True); ref = {}
    for line in open(p + ".sol"):
        w = line.replace(";", "").split()
        if len(w) >= 2 and w[0] != "paritysol": ref[int(w[0])] = int(w[1])
    fbt = []; w1, s1, it1, fb1 = n5b.N5(gp, mode="spec").run(fbtrace=fbt)
    w2, s2, it2, fb2 = n5bxi.N5xi(gp, mode="spec").run()
    cs, Ts, Fs = end222.check(G, "spec"); cx, Tx, Fx = end222.check(G, "xi")
    F1 = fbt.index(1) + 1 if 1 in fbt else None
    bad = []
    if fb1 != 1 or F1 is None or it1 != F1 + 2: bad.append(f"n5b fb {fb1} F {F1} T {it1}")
    if it1 != Ts or F1 != Fs: bad.append(f"n5b T/F {it1}/{F1} != n5v spec {Ts}/{Fs}")
    if fb2 != 1 or it2 != Tx: bad.append(f"n5bxi fb {fb2} T {it2} vs n5v xi {Tx}")
    if not all(w1[v] == ref[v] == w2[v] for v in range(gp.n)): bad.append("regions != Oink")
    if verify.check(gp, w1, s1) or verify.check(gp, w2, s2): bad.append("verify")
    print(f"X {tag} n {gp.n} n5b T{it1}/F{F1}/fb{fb1} n5bxi T{it2}/fb{fb2} n5v spec T{Ts}/F{Fs} xi T{Tx}/F{Fx} " + (f"BAD {bad}" if bad else "ok"), flush=True)
    return bool(bad)
if __name__ == "__main__":
    outdir = sys.argv[1]; nb = n = 0
    if sys.argv[2] == "--fam":
        fam, seed, cnt = sys.argv[3], int(sys.argv[4]), int(sys.argv[5]); rng = random.Random(seed)
        items = [(f"{fam}_{seed}_{i}", end222.gen(fam, rng)) for i in range(cnt)]
    else: items = [(os.path.basename(f), json.load(open(f))) for f in sys.argv[2:]]
    for tag, G in items: nb += one(G, tag, outdir); n += 1
    print(f"XEND223 genomes {n} bad {nb}", flush=True)
