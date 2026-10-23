"""L-RED box 21 (produced on Opus 5.5): trace of N8a Algorithm 1 built ONLY from kl.py's own functions (label_setting, rule_all,
rule_global, violated, edges_tau; kl.py unmodified, from KL_DIR). Per iteration: the Odd nodes that switch (v: old -> new) and the
labels of the switching nodes before / after; at the end it asserts the iteration count equals kl.solve's.
Usage: KL_DIR=.. ktrace.py G.pg RULE [primal|dual]"""
import sys, os, importlib.util
KL = os.environ["KL_DIR"]; sys.path.insert(0, os.path.join(KL, "..", "..", "harness")); sys.setrecursionlimit(100000)
spec = importlib.util.spec_from_file_location("kl", os.path.join(KL, "kl.py")); kl = importlib.util.module_from_spec(spec); spec.loader.exec_module(kl)
import pg
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); rule = sys.argv[2]
side = sys.argv[3] if len(sys.argv) > 3 else "primal"
G = kl.Game(g, dual=(side == "dual"))
lab = lambda x: "T" if x is kl.TOP else "".join(map(str, x)) if G.base <= 10 else ".".join(map(str, x))
tau = [G.succ[v][0] if G.owner[v] == 1 else None for v in range(G.n)]
mu = [tuple([0] * G.h) for _ in range(G.n)]
mu = kl.label_setting(G, kl.edges_tau(G, tau), mu); it = 0
print(f"# {os.path.basename(sys.argv[1])} {side} rule {rule} n {G.n} d {G.d} h {G.h} base {G.base}")
print("pi    ", " ".join(f"{v}:{G.pi[v]}{'o' if G.owner[v] else 'e'}" for v in range(G.n)))
print("mu0   ", " ".join(f"{v}:{lab(mu[v])}" for v in range(G.n)))
while any(G.owner[v] == 1 and any(kl.violated(G, mu, v, w) for w in G.succ[v]) for v in range(G.n)):
    it += 1
    new, ch = (kl.rule_global if rule == "global" else kl.rule_all)(G, mu, tau)
    sw = [v for v in range(G.n) if new[v] != tau[v]]
    mu2 = kl.label_setting(G, kl.edges_tau(G, new), mu)
    up = [v for v in range(G.n) if mu2[v] != mu[v]]
    print(f"it {it}: switch " + " ".join(f"{v}:{tau[v]}->{new[v]}" for v in sw) + " | raised " + " ".join(f"{v}:{lab(mu[v])}->{lab(mu2[v])}" for v in up))
    tau, mu = new, mu2
r = kl.solve(g, rule); exp = r["it"] if side == "primal" else r["it_dual"]
assert it == exp, (it, exp); print(f"# iterations {it} == kl.solve {exp}")
