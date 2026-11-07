#!/usr/bin/env python3
"""REFEREE successor 24: own check of P-IDEAL-ALIGN (l-new cb8e0dca) with my simulator t3r_sim.py (R104 text: beta-SETS, literal keys;
no lane code). On genomes of L^R_d (R110 wiring): ALIGN (a) KP(2l) = KP(2l+1) = c_l(s); (b) a moving pair mover lands on c_l(s_t);
(c) ord(2l, 2l+1) formula; F0; PAIR-DOUBLE F(l) <= 2F(l-1)+2 (+ equality count); MOVES KF_x = F(l-1) (level >= 1), moves bound;
T-BOUND (both forms); PATH-RISE (rises of the current Xi-SET of z, by the R104 set order, <= P(z) - 1, P(z) counted by my own DFS).
KP-MOVE (a), (b) on the non-L^R corpus genomes (FILES mode).
Controls (must fire): PAIRDOUBLE_TIGHTER (F(l) <= F(l-1) + 1, false in general), PATH_TIGHTER (rises <= P(z) - 2).
Usage: python3 -I align_probe.py n seed  |  FILES='<glob>' python3 -I align_probe.py"""
import glob, itertools, json, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import t3r_sim as R

def in_lr(G):
    N = G["N"]
    return N % 2 == 0 and N >= 2 and G["lev"] == [x // 2 for x in range(N)] and all(
        len(G["opts"][x]) == 2 and all(G["opts"][x][k][0] == (2 * (x // 2 - 1) + k if x >= 2 else -1) for k in (0, 1)) for x in range(N))

def rlr(rng, d):
    N = 2 * d; order = list(range(N)); rng.shuffle(order); pos = {v: i for i, v in enumerate(order)}
    opts = []
    for x in range(N):
        later = [y for y in range(N) if pos[y] > pos[x]]
        opts.append([[-1 if x < 2 else 2 * (x // 2 - 1) + k, rng.choice(later + [-1]) if later else -1, 2 * x + k] for k in range(2)])
    r = list(range(2 * N)); rng.shuffle(r); g = list(range(2 * N)); rng.shuffle(g)
    return {"N": N, "lev": [x // 2 for x in range(N)], "opts": opts, "gate": [[g[2 * x], g[2 * x + 1]] for x in range(N)], "br": r,
            "bp": [rng.randrange(2) for _ in range(2 * N)], "start": [0] * N}

def ck(G, s, x): return R.key(G, s, x, s[x], {})
def kp(G, s, x): return min(range(len(G["opts"][x])), key=lambda k: R.key(G, s, x, k, {}))

def npaths(G):
    memo = {}
    def p(z):
        if z < 0: return 1
        if z not in memo: memo[z] = sum(p(o[1]) for o in G["opts"][z])
        return memo[z]
    return p

C = {k: 0 for k in "ALIGNA ALIGNB ALIGNC F0 DBL MOVES_KF MOVES_MV TB PATH KPMOVEA KPMOVEB".split()}
V = {k: 0 for k in C}; CTL = {"PAIRDOUBLE_TIGHTER": 0, "PATH_TIGHTER": 0}; EQ = 0; runs = steps = 0

def check_lr(G, st):
    global EQ, runs, steps
    S = R.run(G, st); T = len(S) - 1; N = G["N"]; d = N // 2; runs += 1; steps += T
    for t in range(T + 1):
        s = S[t]
        for l in range(1, d):
            p, q = 2 * l, 2 * l + 1
            c = 0 if ck(G, s, 2 * l - 2) < ck(G, s, 2 * l - 1) else 1
            C["ALIGNA"] += 1; V["ALIGNA"] += not (kp(G, s, p) == kp(G, s, q) == c)
            if t >= 1:
                C["ALIGNB"] += 1; V["ALIGNB"] += any(s[x] != S[t - 1][x] and s[x] != c for x in (p, q))
            want = (s[p] == c) if s[p] != s[q] else (G["gate"][p][s[p]] < G["gate"][q][s[q]])
            C["ALIGNC"] += 1; V["ALIGNC"] += (ck(G, s, p) < ck(G, s, q)) != want
    F = [sum(1 for t in range(1, T + 1) if (ck(G, S[t], 2 * l) < ck(G, S[t], 2 * l + 1)) != (ck(G, S[t - 1], 2 * l) < ck(G, S[t - 1], 2 * l + 1)))
         for l in range(d)]
    C["F0"] += 1; V["F0"] += F[0] > 2 or any(sum(1 for t in range(1, T + 1) if S[t][y] != S[t - 1][y]) > 1 for y in (0, 1))
    for l in range(1, d):
        C["DBL"] += 1; V["DBL"] += F[l] > 2 * F[l - 1] + 2; EQ += F[l] == 2 * F[l - 1] + 2
        CTL["PAIRDOUBLE_TIGHTER"] += F[l] > F[l - 1] + 1
    P = npaths(G)
    for x in range(N):
        l = G["lev"][x]
        mv = sum(1 for t in range(1, T + 1) if S[t][x] != S[t - 1][x])
        if l >= 1:
            kf = sum(1 for t in range(1, T + 1) if kp(G, S[t], x) != kp(G, S[t - 1], x))
            C["MOVES_KF"] += 1; V["MOVES_KF"] += kf != F[l - 1]
        C["MOVES_MV"] += 1; V["MOVES_MV"] += mv > (1 + F[l - 1] if l >= 1 else 1)
        rises = sum(1 for t in range(1, T + 1) if R.better(G, R.value(G, S[t], x, S[t][x]), R.value(G, S[t - 1], x, S[t - 1][x])))
        C["PATH"] += 1; V["PATH"] += rises > P(x) - 1; CTL["PATH_TIGHTER"] += rises > P(x) - 2
    C["TB"] += 1; V["TB"] += T > 2 * d + 2 * sum(F[:d - 1]) or T > 2 ** (d + 2) - 2 * d - 4
    return T

def check_kpmove(G, st):
    S = R.run(G, st); T = len(S) - 1
    for x in range(G["N"]):
        if len(G["opts"][x]) != 2: continue
        ts = [t for t in range(1, T + 1) if S[t][x] != S[t - 1][x]]
        for t in ts:
            C["KPMOVEA"] += 1; V["KPMOVEA"] += S[t][x] != kp(G, S[t], x)
        kf = sum(1 for t in range(1, T + 1) if kp(G, S[t], x) != kp(G, S[t - 1], x))
        C["KPMOVEB"] += 1; V["KPMOVEB"] += len(ts) > 1 + kf

def tmax(G):
    return max(len(R.run(G, st)) - 1 for st in itertools.product((0, 1), repeat=G["N"])) if G["N"] <= 8 else len(R.run(G)) - 1

FILES = os.environ.get("FILES")
if FILES:
    nl = ng = 0
    for f in sorted(glob.glob(FILES, recursive=True)):
        try:
            G = json.load(open(f))
            if not (isinstance(G, dict) and "opts" in G and "start" in G and G["N"] <= 30): continue
            G["opts"] = [[list(o[:3]) for o in ox] for ox in G["opts"]]
            R.run(G)
        except Exception:
            continue
        nst = 1
        for x in range(G["N"]): nst *= len(G["opts"][x])
        sts = list(itertools.product(*[range(len(G["opts"][x])) for x in range(G["N"])])) if nst <= 64 else [tuple(G["start"])]
        if in_lr(G):
            nl += 1
            for st in sts: check_lr(G, st)
        elif all(G["lev"][o[0]] == G["lev"][x] - 1 for x in range(G["N"]) for o in G["opts"][x] if o[0] >= 0):
            ng += 1
            for st in sts: check_kpmove(G, st)
    print(f"FILES {FILES}: L^R genomes {nl}, other genomes (KP-MOVE only) {ng}")
else:
    n, seed = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed)
for_lr = []
if not FILES:
    for i in range(n):
        d = rng.randint(2, 6); G = rlr(rng, d)
        if i % 3 == 0 and d <= 4:   # hill-climb a third of the small ones for longer runs (mutate one field, keep if max T >= )
            best = tmax(G)
            for _ in range(150):
                H = json.loads(json.dumps(G)); kind = rng.randrange(4); N = H["N"]
                if kind == 0: a, b = rng.sample(range(2 * N), 2); H["br"][a], H["br"][b] = H["br"][b], H["br"][a]
                elif kind == 1: H["bp"][rng.randrange(2 * N)] ^= 1
                elif kind == 2:
                    x, y = rng.randrange(N), rng.randrange(N); k, j = rng.randrange(2), rng.randrange(2)
                    H["gate"][x][k], H["gate"][y][j] = H["gate"][y][j], H["gate"][x][k]
                else:
                    x, k = rng.randrange(N), rng.randrange(2); H["opts"][x][k][1] = rng.choice([y for y in range(N) if y != x] + [-1])
                if not R.in_LR(H): continue
                t = tmax(H)
                if t >= best: G, best = H, t
        sts = list(itertools.product((0, 1), repeat=G["N"])) if G["N"] <= 6 else [tuple(rng.randrange(2) for _ in range(G["N"])) for _ in range(16)]
        for st in sts: check_lr(G, st)
print(f"runs {runs} steps {steps} PAIR-DOUBLE equalities {EQ}")
print("CHECKS " + " ".join(f"{k} {v}" for k, v in C.items()))
print("VIOL   " + " ".join(f"{k} {v}" for k, v in V.items()))
print("CONTROLS (must fire) " + " ".join(f"{k} {v}" for k, v in CTL.items()))
