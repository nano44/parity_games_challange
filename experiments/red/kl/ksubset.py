"""L-RED box 21 (produced on Opus 5.5): NOT a frozen N8a rule. Runs Algorithm 1 with kl.py's own functions (unmodified, KL_DIR) under
SUBSET rules, to test how far the H_k counter is rule-independent: 'first' = switch only the lowest-index Odd node with an admissible arc,
'last' = only the highest-index one, 'rand:S' = one uniformly random such node (seed S). Every Odd node in these games has at most one
admissible arc (kadmiss.py), so the arc choice is forced. Prints the iteration count and checks the final regions against kl.solve.
Usage: KL_DIR=.. ksubset.py G.pg first|last|rand:S [dual]"""
import sys, os, random, importlib.util
KL = os.environ["KL_DIR"]; sys.path.insert(0, os.path.join(KL, "..", "..", "harness")); sys.setrecursionlimit(100000)
spec = importlib.util.spec_from_file_location("kl", os.path.join(KL, "kl.py")); kl = importlib.util.module_from_spec(spec); spec.loader.exec_module(kl)
import pg
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); rule = sys.argv[2]; dual = len(sys.argv) > 3
G = kl.Game(g, dual=dual); rnd = random.Random(int(rule.split(":")[1]) if rule.startswith("rand") else 0)
tau = [G.succ[v][0] if G.owner[v] == 1 else None for v in range(G.n)]
mu = kl.label_setting(G, kl.edges_tau(G, tau), [tuple([0] * G.h) for _ in range(G.n)]); it = 0
while True:
    adm = sorted(v for v in range(G.n) if G.owner[v] == 1 and any(kl.violated(G, mu, v, w) for w in G.succ[v]))
    if not adm: break
    it += 1; v = adm[0] if rule == "first" else adm[-1] if rule == "last" else rnd.choice(adm)
    tau = list(tau); tau[v] = next(w for w in G.succ[v] if kl.violated(G, mu, v, w))
    new = kl.label_setting(G, kl.edges_tau(G, tau), mu); assert all(kl.lab_max(a, b) == b for a, b in zip(mu, new)); mu = new
ref = kl.strategy_iteration(G, "all")[0]
print(f"{os.path.basename(sys.argv[1])} {'dual' if dual else 'primal'} {rule}: iterations {it}, regions == kl {[x is kl.TOP for x in mu] == [x is kl.TOP for x in ref]}")
