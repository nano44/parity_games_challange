"""REFEREE s23 §C: do KEYFLIP (KP = key-least option) and TOP-MONO fail at degree >= 3? Own R104-text simulator (xinew_probe)."""
import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xinew_probe as X
os.environ["BIG"] = "1"
rng = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 7)
kf_fail = top_fail = runs = 0
for _ in range(int(sys.argv[2]) if len(sys.argv) > 2 else 3000):
    lev, opts, start = X.genome(rng)
    if max(len(o) for o in opts) < 3: continue
    st, As = X.run(lev, opts, start, 0); runs += 1; N = len(lev); T = len(st) - 1
    def key(x, k, s):
        wt = opts[x][k][0]; return (key(wt, s[wt], s) if wt is not None else ()) + (opts[x][k][4],)
    KP = [[min(range(len(opts[x])), key=lambda k: key(x, k, s)) for x in range(N)] for s in st]
    for x in range(N):
        mv = sum(st[t][x] != st[t-1][x] for t in range(1, T+1)); kf = sum(KP[t][x] != KP[t-1][x] for t in range(1, T+1))
        if mv > 1 + kf: kf_fail += 1
    # pi = topological order used by genome(): recover from xt edges (any topo order works); use Kahn
    indeg = [0]*N
    for x in range(N):
        for o in opts[x]:
            if o[1] != 'X': indeg[o[1]] += 1
    order = [x for x in range(N) if indeg[x] == 0]; i = 0
    while i < len(order):
        x = order[i]; i += 1
        for o in opts[x]:
            if o[1] != 'X':
                indeg[o[1]] -= 1
                if indeg[o[1]] == 0: order.append(o[1])
    pos = {x: j for j, x in enumerate(order)}
    C = [[len(X.avail(opts, s, x, 0)) - 1 for x in range(N)] for s in st]
    for t in range(1, T+1):
        y = max((x for x in range(N) if st[t][x] != st[t-1][x]), key=lambda x: pos[x])
        rank = 1 + sum(1 for x in range(N) if C[t-1][x] > 0 and pos[x] > pos[y])
        for k in range(1, N+1):
            tp = lambda c: tuple(sorted((pos[x] for x in range(N) if c[x] > 0), reverse=True)[:k]) + (-1,)*0
            a = sorted((pos[x] for x in range(N) if C[t-1][x] > 0), reverse=True)[:k]; a += [-1]*(k-len(a))
            b = sorted((pos[x] for x in range(N) if C[t][x] > 0), reverse=True)[:k]; b += [-1]*(k-len(b))
            if b > a or (b < a) != (rank <= k): top_fail += 1
print("deg>=3 runs", runs, "KEYFLIP fails", kf_fail, "TOP-MONO fails", top_fail)
