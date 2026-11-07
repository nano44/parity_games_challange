"""REFEREE s23: own check of P-IDEAL-FLIP on xinew_probe's beta-SET simulator. Step^c and forced runs written from packet §1 text.
Usage: python3 -I flip_probe.py <iso_d4_st9.json> <kf0.json> <kf1.json> [SEED COUNT]"""
import sys, os, json, random, functools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xinew_probe as X
def conv(G):
    return G["lev"], [[[o[0] if o[0] >= 0 else None, o[1] if o[1] >= 0 else 'X', G["br"][o[2]], G["bp"][o[2]], G["gate"][x][k]] for k, o in enumerate(G["opts"][x])] for x in range(G["N"])], list(G["start"])
def isLR(lev, opts):
    N = len(lev); return N % 2 == 0 and all(lev[x] == x // 2 and len(opts[x]) == 2 and all((o[0] is None) == (lev[x] == 0) and (o[0] is None or o[0] == 2 * (lev[x] - 1) + k) for k, o in enumerate(opts[x])) for x in range(N))
def isISO(opts): return all(o[1] not in (0, 1) for r in opts for o in r)
def stepc(lev, opts, s, c):
    """Step^c_G(s): movers 0,1 kept; U level by level with key^c (level 1: (kappa^c_w, g)); kappa^c_0 = 1-c, kappa^c_1 = c."""
    N = len(lev); A = [X.avail(opts, s, x, 0) for x in range(N)]; new = list(s); key = {}
    kap = {0: 1 - c, 1: c}
    for l in sorted(set(lev)):
        if l == 0: continue
        for x in [y for y in range(N) if lev[y] == l]:
            def kc(k):
                wt = opts[x][k][0]
                return ((kap[wt],) if l == 1 else key[(wt, new[wt])]) + (opts[x][k][4],)
            for k in range(len(opts[x])): pass
            new[x] = min(A[x], key=kc)
            for k in range(len(opts[x])): key[(x, k)] = kc(k)
    return new
def Vk(lev, opts, s0, kmax):
    """max moves over forced runs from s0 with flips <= kmax (frames changing nothing skipped)."""
    @functools.lru_cache(None)
    def f(u, c, left):
        best = 0; nu = tuple(stepc(lev, opts, list(u), c))
        if nu != u: best = max(best, 1 + f(nu, c, left))
        if left > 0:
            nu2 = tuple(stepc(lev, opts, list(u), 1 - c))
            if nu2 != u: best = max(best, 1 + f(nu2, 1 - c, left - 1))
        return best
    return max(f(tuple(s0), c, kmax) for c in (0, 1))
if __name__ == '__main__':
    # (1) DEAD instance
    lev, opts, st = conv(json.load(open(sys.argv[1])))
    s, _ = X.run(lev, opts, st, 0); T = len(s) - 1
    l0 = [t for t in range(1, T + 1) if s[t][0] != s[t-1][0] or s[t][1] != s[t-1][1]]
    seg1 = l0[0] - 1 if l0 else T; tail = T - l0[-1] if l0 else 0
    print("INST LR", isLR(lev, opts), "ISO", isISO(opts), "T", T, "level-0 steps", l0, "seg1", seg1, "tail", tail, "states", ["".join(map(str, x)) for x in s])
    # (2) FLIP-1 instances, forced runs as in §5
    for f, cs in ((sys.argv[2], (0, 0, 0)), (sys.argv[3], (0, 1, 1))):
        lev, opts, st = conv(json.load(open(f))); u = [list(st)]
        for c in cs: u.append(stepc(lev, opts, u[-1], c))
        mv = sum(u[t][2:] != u[t-1][2:] for t in range(1, len(u)))
        print(os.path.basename(f), "LR", isLR(lev, opts), "ISO", isISO(opts), "frames", [x[2:] for x in u], "moves", mv, "V_0", Vk(lev, opts, st, 0), "V_1", Vk(lev, opts, st, 1), "V_6", Vk(lev, opts, st, 6))
    # (3) random LR_2 ISO genomes: FLIP-1 bounds V_0 <= 2, V_k <= 3; and W-ONLY (a) on real runs of random LR_3
    seed = int(sys.argv[4]) if len(sys.argv) > 4 else 1; cnt = int(sys.argv[5]) if len(sys.argv) > 5 else 400
    rng = random.Random(seed); bad = dict(v0=0, vk=0, wonly=0); mx = [0, 0]; runs = 0; wst = 0
    def rgen(d):
        N = 2 * d; ranks = list(range(4 * d)); rng.shuffle(ranks); gates = list(range(4 * d)); rng.shuffle(gates); i = 0; opts = []
        order = list(range(2, N)); rng.shuffle(order); pos = {x: j for j, x in enumerate(order)}
        for x in range(N):
            row = []
            for k in range(2):
                later = [y for y in range(2, N) if x >= 2 and pos[y] > pos[x]] if x >= 2 else [y for y in range(2, N)]
                xt = rng.choice(later + ['X', 'X']) if later else 'X'
                row.append([None if x < 2 else 2 * (x // 2 - 1) + k, xt, ranks[i], rng.randint(0, 1), gates[i]]); i += 1
            opts.append(row)
        return [x // 2 for x in range(N)], opts
    for _ in range(cnt):
        lev, opts = rgen(2)
        for st in ([a, b, c, d] for a in (0, 1) for b in (0, 1) for c in (0, 1) for d in (0, 1)):
            runs += 1; v0 = Vk(lev, opts, st, 0); v6 = Vk(lev, opts, st, 6); mx[0] = max(mx[0], v0); mx[1] = max(mx[1], v6)
            if v0 > 2: bad['v0'] += 1
            if v6 > 3: bad['vk'] += 1
    for _ in range(cnt):
        lev, opts = rgen(3); st = [rng.randint(0, 1) for _ in range(6)]
        s, _ = X.run(lev, opts, st, 0)
        for t in range(1, len(s)):
            wst += 1; c = 1 if opts[0][s[t][0]][4] < opts[1][s[t][1]][4] else 0
            if stepc(lev, opts, s[t-1], c)[2:] != s[t][2:]: bad['wonly'] += 1
    print("RANDOM LR_2 ISO (genome,start) pairs", runs, "max V_0", mx[0], "max V_6", mx[1], "| W-ONLY(a) real steps LR_3 (ISO not required)", wst, "| violations", bad)
