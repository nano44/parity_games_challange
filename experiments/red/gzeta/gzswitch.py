"""L-RED box 23 (produced on Opus 5.5): per-node switch statistics of the N8d-R2 DUAL run (kl_single.py functions, unmodified, KL_DIR)
on G_zeta: how often each improver node switches, how many switches go 1 -> 0 (a cycle node leaving its cycle = a cycle OPENING in
Friedmann's terms; the 0-edge is the FIRST successor by gzeta.py's convention), and the first such opening. Usage: KL_DIR=.. gzswitch.py G.pg SEED"""
import sys, os, re, random, collections, importlib.util
KL = os.environ["KL_DIR"]; sys.path.insert(0, KL); sys.path.insert(0, os.path.join(KL, "..", "..", "harness")); sys.setrecursionlimit(100000)
spec = importlib.util.spec_from_file_location("kl_single", os.path.join(KL, "kl_single.py")); ks = importlib.util.module_from_spec(spec); spec.loader.exec_module(ks)
import pg
kl = ks.kl
txt = open(sys.argv[1]).read(); names = dict((int(m.group(1)), m.group(2)) for m in re.finditer(r'^(\d+) .*"(.*)";', txt, re.M))
g = pg.parse(re.sub(r' "[^"]*"', "", txt)); G = kl.Game(g, dual=True); rng = random.Random(int(sys.argv[2]))
tau = [G.succ[v][0] if G.owner[v] == 1 else None for v in range(G.n)]
mu = kl.label_setting(G, kl.edges_tau(G, tau), [tuple([0] * G.h) for _ in range(G.n)]); it = 0; cnt = collections.Counter(); opens = []; first = None
while ks.candidates(G, mu):
    it += 1; new = ks.rule_r2(G, mu, tau, rng); v = next(u for u in range(G.n) if new[u] != tau[u]); cnt[v] += 1
    if new[v] == G.succ[v][0]:
        opens.append(v)
        if first is None: first = (it, names[v])
    tau = new; mu = kl.label_setting(G, kl.edges_tau(G, tau), mu)
print(f"{os.path.basename(sys.argv[1])} seed {sys.argv[2]}: dual pivots {it}, nodes that switched {len(cnt)}, max switches of one node {max(cnt.values())},"
      f" switches back to the 0-edge (openings) {len(opens)}, first opening {first}")
print("  switch count histogram:", dict(sorted(collections.Counter(cnt.values()).items())))
print("  by group:", dict(collections.Counter(re.sub(r'[\d,]+', '', names[v]) for v in cnt)))
