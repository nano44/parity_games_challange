"""REFEREE successor 25: P-N5-REACH REACH3 replay with an engine that is not L-NEW's.
N5 = L-COMP's n5b.py (--mode spec, default start = S3 by best reward), with its trace/fbtrace hooks; L(G) and the IDEAL states from
t3r_sim.py (successor 24's own simulator). Usage: reach_replay.py N5SECOND_DIR GENOME.json GAME_g3.pg"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import t3r_sim as ts
D = sys.argv[1]; sys.path.insert(0, D); sys.path.insert(0, os.path.join(D, "..", "hard-families")); sys.path.insert(0, os.path.join(D, "..", "harness"))
import n5b, pg
n5b.MODE = "spec"
G = json.load(open(sys.argv[2])); g = pg.read(sys.argv[3])
N = G["N"]; O = [(x, k) for x in range(N) for k in range(len(G["opts"][x]))]; M = len(O)
print("n", g.n, "N + 7M + 10 =", N + 7 * M + 10, g.n == N + 7 * M + 10)
gorder = sorted(O, key=lambda o: G["gate"][o[0]][o[1]]); gate_v = {o: N + i for i, o in enumerate(gorder)}; v_gate = {v: o for o, v in gate_v.items()}
succ = [list(g.succ[v]) if hasattr(g, "succ") else None for v in range(g.n)]
def choice(sig, x):              # mover x -> pad -> gate -> option k
    p = sig[x]; assert len(g.succ[p]) == 1, "mover successor is not a pad"
    o = v_gate[g.succ[p][0]]; assert o[0] == x; return o[1]
for x in range(N):                # structure: every mover edge goes through a pad to one of x's gates
    assert sorted(v_gate[g.succ[p][0]][1] for p in g.succ[x]) == list(range(len(G["opts"][x])))
IS = ts.run(G); L = len(IS) - 1
s = n5b.N5(g); tr = []; fbt = []; win, strat, it, fb = s.run(trace=tr, fbtrace=fbt)
rank = sorted(range(g.n), key=lambda v: (g.prio[v], v)); rk = {v: i for i, v in enumerate(rank)}
def val(sig, tau):
    f = [sig[v] if sig[v] != -1 else tau[v] for v in range(g.n)]; out = []
    for v in range(g.n):
        path = [v]; pos = {v: 0}
        while f[path[-1]] not in pos: pos[f[path[-1]]] = len(path); path.append(f[path[-1]])
        cyc = path[pos[f[path[-1]]]:]; c = max(cyc, key=lambda u: rk[u]); pre = path[:pos[f[path[-1]]]]
        out.append((c, frozenset(u for u in pre if rk[u] > rk[c]), len(pre)))
    return out
fl = 0
for t in range(1, len(tr)):
    (s0, t0), (s1, t1) = tr[t - 1], tr[t]
    if fbt[t - 1] or t0 != t1 or s0 == s1 or val(s0, t0) != val(s1, t1): break
    fl += 1
match = all(tuple(choice(tr[j][0], x) for x in range(N)) == tuple(IS[j]) for j in range(min(L, len(tr) - 1) + 1))
print(os.path.basename(sys.argv[3]), "L(G) own sim", L, "| n5b iterations", it, "fallbacks", fb, "| FL run from state 0:", fl,
      "| transition L+1 fallback:", bool(fbt[L]) if L < len(fbt) else None, "| mover choices = IDEAL states 0..L:", match)
