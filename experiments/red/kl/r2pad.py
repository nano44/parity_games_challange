"""L-RED box 22 (produced on Opus 5.5): N8d-R2 pivots over seeds 1..S (kl_single.py unmodified, KL_DIR) for a game padded with 2k isolated
self-loops (owner Even) with new top priorities max+1..max+2k (the R53 level trick). Prints per k: n, primal and dual pivots per seed,
min / mean, and writes OUT_k.pg. Usage: KL_DIR=.. r2pad.py G.pg KMAX S OUTPREFIX"""
import sys, os, importlib.util, statistics
KL = os.environ["KL_DIR"]; sys.path.insert(0, KL); sys.path.insert(0, os.path.join(KL, "..", "..", "harness")); sys.setrecursionlimit(100000)
spec = importlib.util.spec_from_file_location("kl_single", os.path.join(KL, "kl_single.py")); ks = importlib.util.module_from_spec(spec); spec.loader.exec_module(ks)
import pg
kl = ks.kl
f, KMAX, S, pre = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
lines = [l for l in open(f) if l.strip() and not l.startswith("parity")]; n0 = len(lines); mx = max(int(l.split()[1]) for l in lines)
for k in range(KMAX + 1):
    n = n0 + 2 * k; txt = "".join([f"parity {n - 1};\n"] + lines + [f"{n0 + i} {mx + 1 + i} 0 {n0 + i};\n" for i in range(2 * k)])
    open(f"{pre}_{k}.pg", "w").write(txt); g = pg.parse(txt)
    P = kl.Game(g); D = kl.Game(g, dual=True)
    p = [ks.strategy_iteration(P, ks.rule_r2, s)[2] for s in range(1, S + 1)]; d = [ks.strategy_iteration(D, ks.rule_r2, s)[2] for s in range(1, S + 1)]
    print(f"k {k} n {n}: primal {p} min {min(p)} mean {statistics.mean(p):.1f} | dual {d} min {min(d)} mean {statistics.mean(d):.1f}", flush=True)
