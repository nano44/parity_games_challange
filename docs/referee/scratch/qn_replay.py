"""REFEREE successor 30: P-N5-QN replay on IDEAL-CYC(G) with own code (xicyc_replay.howard on own build; own generator end_replay.gen).
Counters (all must be 0 except controls):
  lfail   flips at a gate with neither face changing class (GATE-CLASS)          [flip steps]
  gfail   gates with flips(g) > (D(e_g) - 1) + (D(b_g) - 1) (GATE-FLIP (a))      [gates]
  qflip   quiet steps at which sigma-bar changes at some Odd vertex              [steps]
  qnotp   quiet steps not labelled p by R118's labels                            [steps]
  qfail   maximal quiet windows longer than N                                    [windows]
  Tfail   runs with T > Q + (Q + 1) N                                            [runs]
  Qfail   runs with Q > sum_v (D(v) - 1)                                         [runs]
  c1fail  vertices whose class sequence repeats a class after leaving it (C1)    [vertices]
  lamfail states with more than k + 1 distinct Lambda off cW, cX, e->cW          [states]
  gtie    (state, gate) with Omega(e_g) == Omega(b_g) (NO-TIE)                   [pairs]
Controls: ctrlE = flips with the e-face's class unchanged (must fire somewhere); ctrlK = states with more than k distinct Lambda (fires).
Usage: qn_replay.py FAM SEED COUNT | qn_replay.py --files F.json ..."""
import sys, os, json, random, itertools, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xicyc_replay import howard
from end_replay import gen

def fvs(G):
    N = G["N"]; E = {(x, o[1]) for x in range(N) for o in G["opts"][x] if o[1] >= 0}
    def acyc(rm):
        adj = collections.defaultdict(list)
        for a, b in E:
            if a not in rm and b not in rm: adj[a].append(b)
        col = {}
        def dfs(u):
            col[u] = 1
            for w in adj[u]:
                if col.get(w) == 1 or (w not in col and not dfs(w)): return False
            col[u] = 2; return True
        return all(col.get(u) == 2 or (u not in col and dfs(u)) for u in range(N) if u not in rm)
    for k in range(N + 1):
        for rm in itertools.combinations(range(N), k):
            if acyc(set(rm)): return k

def one(G, C):
    E, lab, ties, states, movers, idx = howard(G)
    n = E.n; N = G["N"]; O = [(x, k) for x in range(N) for k in range(len(G["opts"][x]))]
    evs = {idx[("e", q)] for q in O}; cW, cX = idx["cW"], idx["cX"]
    excl = {cW, cX} | {idx[("e", q)] for q in O if G["opts"][q[0]][q[1]][0] < 0}
    gates = [(idx[("g", q)], idx[("e", q)], idx[("b", q)]) for q in O]
    odd = [v for v in range(n) if E.owner[v] == 1]
    k = fvs(G); C["runs"] += 1; C["kmax"] = max(C["kmax"], k)
    cls = [[(val[v][0], frozenset(val[v][1] & evs)) for v in range(n)] for (_, _, val) in states]
    for (s, st, val) in states:
        nl = len({val[v][0] for v in range(n) if v not in excl})
        C["lamfail"] += nl > k + 1; C["ctrlK"] += nl > k
        for g, e, b in gates: C["gtie"] += E.cmp(val[e], val[b]) == 0
    T = len(states) - 1; Q = 0; cur = 0; flips = collections.Counter()
    for t in range(1, T + 1):
        a, b = states[t - 1], states[t]; loud = any(cls[t][v] != cls[t - 1][v] for v in range(n))
        for g, e, bb in gates:
            if a[1][g] != b[1][g]:
                flips[g] += 1
                C["lfail"] += cls[t][e] == cls[t - 1][e] and cls[t][bb] == cls[t - 1][bb]
                C["ctrlE"] += cls[t][e] == cls[t - 1][e]
        if loud: Q += 1; cur = 0
        else:
            cur += 1; C["qfail"] += cur == N + 1
            C["qflip"] += any(a[1][v] != b[1][v] for v in odd); C["qnotp"] += lab[t - 1] != "p"
    D = []
    for v in range(n):
        seq = [cls[t][v] for t in range(T + 1)]; seen = set(); last = None; rep = False
        for c in seq:
            if c != last:
                if c in seen: rep = True
                seen.add(c); last = c
        C["c1fail"] += rep; D.append(len(seen))
    for g, e, bb in gates: C["gfail"] += flips[g] > (D[e] - 1) + (D[bb] - 1)
    C["Qfail"] += Q > sum(d - 1 for d in D); C["Tfail"] += T > Q + (Q + 1) * N
    C["T"] = max(C["T"], T); C["flips"] += sum(flips.values()); C["maxflip"] = max(C["maxflip"], max(flips.values(), default=0))

KEYS = ("lfail", "gfail", "qflip", "qnotp", "qfail", "Tfail", "Qfail", "c1fail", "lamfail", "gtie", "ctrlE", "ctrlK", "runs", "kmax", "T", "flips", "maxflip")
def show(tag, C): print(tag, " ".join(f"{k} {C[k]}" for k in KEYS), flush=True)

if __name__ == "__main__":
    if sys.argv[1] == "--files":
        for f in sys.argv[2:]:
            C = collections.Counter(); one(json.load(open(f)), C); show(os.path.basename(f), C)
    else:
        fam, seed, cnt = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed); C = collections.Counter()
        for _ in range(cnt): one(gen(rng, fam), C)
        show(f"{fam} seed {seed} x{cnt}", C)
