"""L-RED box 22 (produced on Opus 5.5): trace of N8d-R2 (kl_single.py's own rule_r2 / strategy loop pieces, unmodified, KL_DIR): per
iteration the candidate Odd nodes (those with an admissible arc), the node R2 picked, and the labels raised; asserts the iteration count
equals kl_single.strategy_iteration's. Usage: KL_DIR=.. ktrace_r2.py G.pg SEED [dual]"""
import sys, os, random, importlib.util
KL = os.environ["KL_DIR"]; sys.path.insert(0, KL); sys.path.insert(0, os.path.join(KL, "..", "..", "harness")); sys.setrecursionlimit(100000)
spec = importlib.util.spec_from_file_location("kl_single", os.path.join(KL, "kl_single.py")); ks = importlib.util.module_from_spec(spec); spec.loader.exec_module(ks)
import pg
kl = ks.kl
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); seed = int(sys.argv[2]); dual = len(sys.argv) > 3
G = kl.Game(g, dual=dual); rng = random.Random(seed)
lab = lambda x: "T" if x is kl.TOP else ".".join(map(str, x))
tau = [G.succ[v][0] if G.owner[v] == 1 else None for v in range(G.n)]
mu = kl.label_setting(G, kl.edges_tau(G, tau), [tuple([0] * G.h) for _ in range(G.n)]); it = 0
while ks.candidates(G, mu):
    it += 1; c = ks.candidates(G, mu); new = ks.rule_r2(G, mu, tau, rng); v = next(u for u in range(G.n) if new[u] != tau[u])
    mu2 = kl.label_setting(G, kl.edges_tau(G, new), mu)
    print(f"it {it}: cand {c} pick {v}:{tau[v]}->{new[v]} | raised " + " ".join(f"{u}:{lab(mu[u])}->{lab(mu2[u])}" for u in range(G.n) if mu2[u] != mu[u]))
    tau, mu = new, mu2
ref = ks.strategy_iteration(G, ks.rule_r2, seed)[2]; assert it == ref, (it, ref); print(f"# iterations {it} == kl_single {ref}")
