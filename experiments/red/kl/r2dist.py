"""L-RED box 22 (produced on Opus 5.5): distribution of N8d-R2 dual pivots over seeds 1..S (kl_single.py unmodified, KL_DIR).
Usage: KL_DIR=.. r2dist.py G.pg S"""
import sys, os, importlib.util, statistics, collections
KL = os.environ["KL_DIR"]; sys.path.insert(0, KL); sys.path.insert(0, os.path.join(KL, "..", "..", "harness")); sys.setrecursionlimit(100000)
spec = importlib.util.spec_from_file_location("kl_single", os.path.join(KL, "kl_single.py")); ks = importlib.util.module_from_spec(spec); spec.loader.exec_module(ks)
import pg
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); S = int(sys.argv[2]); D = ks.kl.Game(g, dual=True)
x = [ks.strategy_iteration(D, ks.rule_r2, s)[2] for s in range(1, S + 1)]
print(f"{os.path.basename(sys.argv[1])} n {g.n} seeds 1..{S}: mean {statistics.mean(x):.2f} sd {statistics.pstdev(x):.2f} min {min(x)} max {max(x)} median {statistics.median(x)}")
print("  histogram (pivots: count):", " ".join(f"{k}:{v}" for k, v in sorted(collections.Counter(x).items())))
