#!/usr/bin/env python3
"""REFEREE successor 24: own check of P-IDEAL-RISE §1-§4 (l-new 2f4d96de) with my simulator t3r_sim.py (R104 text, set order, no ENC).
- PHIK: Phi_K(s) - Phi_K(step(s)) >= 1 from EVERY state of random L^R_d genomes (d 1-5) and of the L^R corpus genomes (d <= 5);
  T <= Phi_K(s_0) on every such run; Phi_K range = 2^(d+2) - 2d - 4 (all-1 and all-0 states built level by level).
- OPTK: my own forcing genomes tau(l, p) built from §3's text (every Xi-target X, all parities even, ranks: the option the state should
  keep gets the larger rank, at p the other one; gates as §3), for d 1-7: Mv_1 = {p}, k(p) 1 -> 0, level l+1 both 0 -> 1, rest unchanged.
- RISE: every option's Xi-set never gets worse along a run; R(x, k) = rises of the current set of xt(x, k) (0 if X); R <= T;
  T <= 1 + #{t <= T-1 with some option rising} <= 1 + sum R; MOVE-RISE (a move raises the mover's current set); R(x,k) >= moves(z).
Controls: PHIK with weights 2^(d-l) - 2 (must fail somewhere); RISE_C with "T <= #{rise steps}" (no +1; must fail somewhere).
Usage: python3 -I rise_probe.py n seed [FILES glob]"""
import glob, itertools, json, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import t3r_sim as R

def kp(G, s, x): return min(range(2), key=lambda k: R.key(G, s, x, k, {}))
def kbits(G, s): return [int(s[x] != kp(G, s, x)) for x in range(G["N"])]
def phik(G, s, wfun=lambda d, l: 2 ** (d - l) - 1):
    d = G["N"] // 2; return sum(wfun(d, x // 2) * b for x, b in enumerate(kbits(G, s)))

def rlr(rng, d):
    N = 2 * d; order = list(range(N)); rng.shuffle(order); pos = {v: i for i, v in enumerate(order)}
    opts = []
    for x in range(N):
        later = [y for y in range(N) if pos[y] > pos[x]]
        opts.append([[-1 if x < 2 else 2 * (x // 2 - 1) + k, rng.choice(later + [-1]) if later else -1, 2 * x + k] for k in range(2)])
    r = list(range(2 * N)); rng.shuffle(r); g = list(range(2 * N)); rng.shuffle(g)
    return {"N": N, "lev": [x // 2 for x in range(N)], "opts": opts, "gate": [[g[2 * x], g[2 * x + 1]] for x in range(N)], "br": r,
            "bp": [rng.randrange(2) for _ in range(2 * N)], "start": [0] * N}

C = {k: 0 for k in "PHIK PHIK_T RANGE OPTK RISE_A RISE_B RISE_C MOVERISE MOVERISE_R".split()}
V = {k: 0 for k in C}; CTL = {"PHIK_WEAKER": 0, "RISE_C_NO_PLUS1": 0}

def extreme(G, want):
    s = [0] * G["N"]
    for x in range(G["N"]):          # movers are numbered level by level
        k = kp(G, tuple(s), x); s[x] = k if want == 0 else 1 - k
    return tuple(s)

def check_phik(G):
    d = G["N"] // 2
    for st in itertools.product((0, 1), repeat=G["N"]):
        n = R.step(G, st)
        if n is None: continue
        C["PHIK"] += 1; V["PHIK"] += phik(G, st) - phik(G, n) < 1
        CTL["PHIK_WEAKER"] += phik(G, st, lambda d, l: max(0, 2 ** (d - l) - 2)) - phik(G, n, lambda d, l: max(0, 2 ** (d - l) - 2)) < 1
        S = R.run(G, st); C["PHIK_T"] += 1; V["PHIK_T"] += len(S) - 1 > phik(G, st)
    hi, lo = extreme(G, 1), extreme(G, 0)
    C["RANGE"] += 1; V["RANGE"] += not (set(kbits(G, hi)) == {1} and set(kbits(G, lo)) == {0} and phik(G, hi) - phik(G, lo) == 2 ** (d + 2) - 2 * d - 4)

def tau(d, l, p):
    N = 2 * d; q = p ^ 1; s = [0] * N
    G = {"N": N, "lev": [x // 2 for x in range(N)], "opts": [[[-1 if x < 2 else 2 * (x // 2 - 1) + k, -1, 2 * x + k] for k in range(2)] for x in range(N)],
         "gate": [[0, 0] for _ in range(N)], "br": [0] * (2 * N), "bp": [0] * (2 * N), "start": None}
    nxt = iter(range(1000, 100000, 7))
    for x in range(N): G["gate"][x] = [next(nxt), next(nxt)]          # distinct; level l / 0 overwritten below
    if l == 0:
        sp, sq = 0, 1                                                 # any options for p, q
        a, b, c, e = 1, 2, 3, 4                                       # g(p, 1-s(p)) < g(q, s(q)) < g(p, s(p)); g(q, 1-s(q)) > g(q, s(q))
        G["gate"][p][1 - sp] = a; G["gate"][q][sq] = b; G["gate"][p][sp] = c; G["gate"][q][1 - sq] = e
        s[p], s[q] = sp, sq
    else:
        c_l = 0 if R.key(G, tuple(s), 2 * l - 2, s[2 * l - 2], {}) < R.key(G, tuple(s), 2 * l - 1, s[2 * l - 1], {}) else 1
        s[q] = c_l; s[p] = 1 - c_l
        ordl = int(s[2 * l] == c_l)                                   # order of the pair at s (different options)
        want = 1 - ordl                                               # gamma_l(c_l) != ord_l(s)
        lo_, hi_ = 5, 6
        G["gate"][2 * l][c_l], G["gate"][2 * l + 1][c_l] = (lo_, hi_) if want == 1 else (hi_, lo_)
        G["gate"][2 * l][1 - c_l], G["gate"][2 * l + 1][1 - c_l] = 7, 8
    if l + 1 < d:
        c1 = 0 if R.key(G, tuple(s), 2 * l, s[2 * l], {}) < R.key(G, tuple(s), 2 * l + 1, s[2 * l + 1], {}) else 1
        s[2 * l + 2] = s[2 * l + 3] = c1
    for x in range(N):
        keep = (1 - s[x]) if x == p else s[x]
        for k in range(2): G["br"][2 * x + k] = 2 * x + (1 if k == keep else 0)
    G["start"] = list(s); return G

def check_tau(d, l, p):
    G = tau(d, l, p); s = tuple(G["start"]); n = R.step(G, s); ok = n is not None and R.in_LR(G, d)
    if ok:
        k0, k1 = kbits(G, s), kbits(G, n); ok = [x for x in range(G["N"]) if n[x] != s[x]] == [p]
        for x in range(G["N"]):
            if x == p: ok &= (k0[x], k1[x]) == (1, 0)
            elif l + 1 < d and x // 2 == l + 1: ok &= (k0[x], k1[x]) == (0, 1)
            else: ok &= k0[x] == k1[x]
    C["OPTK"] += 1; V["OPTK"] += not ok

def check_rise(G, st):
    S = R.run(G, st); T = len(S) - 1; N = G["N"]
    opts = [(x, k) for x in range(N) for k in range(len(G["opts"][x]))]
    Rk = {o: 0 for o in opts}; risesteps = 0
    for t in range(1, T + 1):
        anyr = False
        for (x, k) in opts:
            a, b = R.value(G, S[t - 1], x, k), R.value(G, S[t], x, k)
            C["RISE_A"] += 1
            if R.better(G, b, a): Rk[(x, k)] += 1; anyr = True
            elif R.better(G, a, b): V["RISE_A"] += 1
        risesteps += anyr and t <= T - 1
        for z in range(N):
            if S[t][z] != S[t - 1][z]:
                C["MOVERISE"] += 1; V["MOVERISE"] += not R.better(G, R.value(G, S[t], z, S[t][z]), R.value(G, S[t - 1], z, S[t - 1][z]))
    C["RISE_B"] += 1; V["RISE_B"] += max(Rk.values()) > T
    if T >= 1:
        C["RISE_C"] += 1; V["RISE_C"] += not (T <= 1 + risesteps <= 1 + sum(Rk.values())); CTL["RISE_C_NO_PLUS1"] += T > risesteps
    for (x, k) in opts:
        z = G["opts"][x][k][1]
        if z >= 0:
            mz = sum(1 for t in range(1, T + 1) if S[t][z] != S[t - 1][z]); C["MOVERISE_R"] += 1; V["MOVERISE_R"] += Rk[(x, k)] < mz

n, seed = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed); ng = 0
for i in range(n):
    d = rng.randint(1, 5); G = rlr(rng, d); ng += 1
    check_phik(G); check_rise(G, tuple(rng.randrange(2) for _ in range(G["N"])))
nc = 0
if len(sys.argv) > 3:
    for f in sorted(glob.glob(sys.argv[3], recursive=True)):
        try:
            G = json.load(open(f))
            if not (isinstance(G, dict) and "opts" in G and "start" in G): continue
            G["opts"] = [[list(o[:3]) for o in ox] for ox in G["opts"]]
            R.run(G)
        except Exception:
            continue
        if G["N"] % 2 == 0 and R.in_LR(G) and G["N"] <= 10: check_phik(G); nc += 1   # in_LR without d does not reject odd N
        if G["N"] <= 30 and all(G["lev"][o[0]] == G["lev"][x] - 1 for x in range(G["N"]) for o in G["opts"][x] if o[0] >= 0):
            check_rise(G, tuple(G["start"]))
for d in range(1, 8):
    for l in range(d):
        for p in (2 * l, 2 * l + 1): check_tau(d, l, p)
print(f"random L^R genomes {ng}, corpus L^R genomes (all states) {nc}")
print("CHECKS " + " ".join(f"{k} {v}" for k, v in C.items()))
print("VIOL   " + " ".join(f"{k} {v}" for k, v in V.items()))
print("CONTROLS (must fire) " + " ".join(f"{k} {v}" for k, v in CTL.items()))
