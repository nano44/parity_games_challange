"""L-RED box 21 (produced on Opus 5.5): per iteration of N8a Algorithm 1 (kl.py's own functions, unmodified, KL_DIR), the admissible arcs of
every Odd node: reports the max number of admissible arcs at one node, and whether the set of Odd nodes with an admissible arc ever
differs from the set the rule switches. Usage: KL_DIR=.. kadmiss.py G.pg RULE [primal|dual]"""
import sys, os, importlib.util
KL = os.environ["KL_DIR"]; sys.path.insert(0, os.path.join(KL, "..", "..", "harness")); sys.setrecursionlimit(100000)
spec = importlib.util.spec_from_file_location("kl", os.path.join(KL, "kl.py")); kl = importlib.util.module_from_spec(spec); spec.loader.exec_module(kl)
import pg
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); rule = sys.argv[2]
G = kl.Game(g, dual=(len(sys.argv) > 3 and sys.argv[3] == "dual"))
tau = [G.succ[v][0] if G.owner[v] == 1 else None for v in range(G.n)]
mu = kl.label_setting(G, kl.edges_tau(G, tau), [tuple([0] * G.h) for _ in range(G.n)]); it = 0; mx = 0; subset = 0; nonadm = 0
while True:
    adm = {v: [w for w in G.succ[v] if kl.violated(G, mu, v, w)] for v in range(G.n) if G.owner[v] == 1}
    adm = {v: a for v, a in adm.items() if a}
    if not adm: break
    it += 1; mx = max(mx, max(len(a) for a in adm.values()))
    new, ch = (kl.rule_global if rule == "global" else kl.rule_all)(G, mu, tau)
    sw = {v for v in range(G.n) if new[v] != tau[v]}
    if sw != set(adm): subset += 1
    if any(new[v] not in adm.get(v, []) for v in sw): nonadm += 1
    tau = new; mu = kl.label_setting(G, kl.edges_tau(G, tau), mu)
print(f"{os.path.basename(sys.argv[1])} {rule}: iterations {it}, max admissible arcs at one Odd node {mx}, iterations where switched set != nodes-with-admissible-arc {subset}, iterations with a switch to a non-admissible arc {nonadm}")
