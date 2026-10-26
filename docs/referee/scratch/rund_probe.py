#!/usr/bin/env python3
"""REFEREE succ. 13 probe for packet P-N5-RUND (docs/si/P-N5-RUND-box17.md, pin 94910ed3, sha1 71e198f3...). Own engine only (rl_engine:
SPEC from the text; epr_probe.wval). No lane code. For every maximal fallback-free run S inside a phase of an N5 run (phase: (lambda_Xi, tau)
constant), and for every level L in {-1, ..., n - 1}:
 CRREL   (ii) on S and (i_rel) at L at every state => COARSE_L(W) constant from k0 + n - 1
 OFFa    under (h3_D) on S: lambda_Xi = lambda_W; s^Xi, s^W non-decreasing        OFFb  Delta_k(v) = 0 / delta_k(u(v)) as stated
 OFFc    offsets multiples of 2^{l_S}                                              TGi   rise inequality at offset changes
 TGii    offset changes at sources >= k0 + n - 1 <= (2^{L*+2} - 2) / 2^{l_S}        TGiii N_v <= (n - 1) + 2^{B+1}
 PIECEb  maximal blocks with aligned sources and lambda_W constant have < n + m transitions; SPLIT  |S| <= N + (N + 1)(n + m - 1) under h3
 PSCH    (n <= PSCHMAX) clean schedule of r at k => COARSE W_k(r_0) >= COARSE value(r), every simple r to a W-cycle node; (ii) on S
 FRZSCH  clean schedule of x's W-play prefix r_t at s => COARSE W(x) constant on [s, t]   (ii) on S
 CHARGE  every change of COARSE W(x) at s-1 -> s is window or charged               (ii) on S
 FZ      forbidden (x, z) at k => Xi_k(z) < W_k(z) and z's W-play meets D_k
 UNF     each charged change has k' with f < k' <= s - 1 <= f + n - 1, sigma switches r_q into r_{q+1} at k', e not forbidden at k'
 CHU     changes of COARSE_L W(x) on S <= (n - 1)(1 + |U(S)|)                      (ii) on S
Runs with k0 = every state of the maximal run (suffix runs) for FRZSCH / CHARGE / UNF / CHU when SUFFIX=1.
Usage: rund_probe.py rand N nmin nmax kmax seed | files...   (env RANDSTARTS, PSCHMAX (default 7), MAXN, SUFFIX)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, dual_probe as D, epr_probe as E
EX = []
MUT = int(os.environ.get("MUT", "0"))  # controls: 1 = schedule shifted by one state, 2 = forbidden-ness ignored


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def lev(g, x, y):
    if x == y: return None            # bottom
    if x[0] != y[0]: return float("inf")
    d = x[1] ^ y[1]
    return d.bit_length() - 1 if d else -1


def coarse(L, x):
    return (x[0], x[1] & ~((1 << (L + 1)) - 1))


def ckey(g, cx):
    return (g.rew[cx[0]], g.weight(cx[1]))


def wsum(g, mask): return g.weight(mask)


def play(nx, v):
    seq, pos = [], {}
    x = v
    while x not in pos: pos[x] = len(seq); seq.append(x); x = nx[x]
    return seq, pos[x]


def analyse_run(g, st, info, a, b, cnt, name, n, m):
    """states a..b, transitions a..b-1 all in-phase S4a"""
    S = list(range(a, b + 1)); T = b - a
    Q = [v for v in range(n) if g.owner[v] == 1]
    lamW = {k: [x[0] for x in info[k]["W"]] for k in S}
    lamX = {k: [x[0] for x in info[k]["Xi"]] for k in S}
    ii = all(lamW[k] == lamW[a] for k in S)
    Dk = {k: [u for u in Q if info[k]["sb"][u] != st[k]["t"][u]] for k in S}
    h3 = all(lamX[k][u] == lamW[k][u] for k in S for u in Dk[k])
    nx = {k: [st[k]["s"][v] if g.owner[v] == 0 else st[k]["t"][v] for v in range(n)] for k in S}
    Xi = {k: info[k]["Xi"] for k in S}; W = {k: info[k]["W"] for k in S}
    Ev = [v for v in range(n) if g.owner[v] == 0]
    def forb(k, L, x, z):
        aa = st[k]["s"][x]
        return z != aa and ckey(g, coarse(L, W[k][z])) > ckey(g, coarse(L, W[k][aa])) and not g.key(Xi[k][z]) > g.key(Xi[k][aa])
    # FZ (level-independent strongest: any L)
    for k in S:
        Dset = set(Dk[k])
        for x in Ev:
            for z in g.succ[x]:
                if any(forb(k, L, x, z) for L in range(-1, n)):
                    cnt["FZ_chk"] += 1
                    seq, _ = play(nx[k], z)
                    if not (g.key(Xi[k][z]) < g.key(W[k][z]) and Dset.intersection(seq)): fail(cnt, "FZ", name, k, x, z)
    # PIECE_D (b) and SPLIT-RED
    def aligned(k):
        for x in Ev:
            aa = st[k]["s"][x]
            for z in g.succ[x]:
                if z != aa and (g.key(Xi[k][z]) > g.key(Xi[k][aa])) != (g.key(W[k][z]) > g.key(W[k][aa])): return False
        return True
    al = {k: aligned(k) for k in S[:-1]}
    blk = 0
    for k in S[:-1]:
        blk = blk + 1 if (al[k] and lamW[k + 1] == lamW[k]) else 0
        cnt["PIECEb_chk"] += 1
        if blk >= n + m: fail(cnt, "PIECEb", name, k, blk)
    Ns = sum(1 for k in S[:-1] if not al[k])
    if h3:
        cnt["SPLIT_chk"] += 1
        if T > Ns + (Ns + 1) * (n + m - 1): fail(cnt, "SPLIT", name, a, T, Ns)
    # OFFSET / TWIN-GAP under h3
    if h3 and T > 0:
        for k in S:
            if lamX[k] != lamW[k]: fail(cnt, "OFFa", name, k, "lam")
        for k in S[:-1]:
            for v in range(n):
                if wsum(g, Xi[k + 1][v][1]) < wsum(g, Xi[k][v][1]) or wsum(g, W[k + 1][v][1]) < wsum(g, W[k][v][1]): fail(cnt, "OFFa", name, k, v)
        cnt["OFFa_chk"] += 1
        Delta = {}; U = set(); Ls = []
        for k in S:
            Dset = set(Dk[k])
            for u in Dk[k]:
                U |= {r for r in range(n) if ((Xi[k][u][1] ^ W[k][u][1]) >> r) & 1}
                lv = lev(g, Xi[k][u], W[k][u]); Ls.append(-1 if lv is None else lv)
            for v in range(n):
                dl = wsum(g, W[k][v][1]) - wsum(g, Xi[k][v][1]); Delta[k, v] = dl
                seq, cs = play(nx[k], v)
                uv = next((x for x in seq if x in Dset), None)
                if uv is None: exp = 0
                else:
                    piv = seq[:seq.index(uv)]
                    c = lamX[k][v]
                    exp = 0 if c in piv else wsum(g, W[k][uv][1]) - wsum(g, Xi[k][uv][1])
                cnt["OFFb_chk"] += 1
                if dl != exp: fail(cnt, "OFFb", name, k, v, dl, exp)
        Lstar = max(Ls + [-1])
        if U:
            lS = min(U)
            if any(Delta[k, v] % (1 << lS) for k in S for v in range(n)): fail(cnt, "OFFc", name, a)
            if Lstar < max(U): fail(cnt, "OFFc", name, a, "rank above L*")
            B = Lstar - lS + 1
            for v in range(n):
                Nv = 0; late = 0
                for k in S[:-1]:
                    d = Delta[k + 1, v] - Delta[k, v]
                    if d:
                        Nv += 1
                        if k >= a + n - 1: late += 1
                        rW = wsum(g, W[k + 1][v][1]) - wsum(g, W[k][v][1]); rX = wsum(g, Xi[k + 1][v][1]) - wsum(g, Xi[k][v][1])
                        cnt["TGi_chk"] += 1
                        if (d > 0 and rW < d) or (d < 0 and rX < -d): fail(cnt, "TGi", name, k, v)
                cnt["TG_chk"] += 1; cnt["MAX_Nv"] = max(cnt["MAX_Nv"], Nv); cnt["MAX_B"] = max(cnt["MAX_B"], B)
                if late * (1 << lS) > (1 << (Lstar + 2)) - 2: fail(cnt, "TGii", name, a, v, late)
                if Nv > (n - 1) + (1 << (B + 1)): fail(cnt, "TGiii", name, a, v, Nv)
        else:
            if any(Delta[k, v] for k in S for v in range(n)): fail(cnt, "OFFc", name, a, "U empty but offset")
    # level-dependent checks
    for L in range(-1, n):
        # CR-REL
        irel = all(not forb(k, L, x, z) for k in S for x in Ev for z in g.succ[x])
        if ii and irel and T >= n:
            cnt["CRREL_chk"] += 1
            base = [coarse(L, W[a + n - 1][v]) for v in range(n)]
            if any([coarse(L, W[k][v]) for v in range(n)] != base for k in S if k >= a + n - 1): fail(cnt, "CRREL", name, a, L)
        if not ii: continue
        cyc = {u for u in range(n) if lamW[a][u] == u}
        forbset = {(k, x, z) for k in S for x in Ev for z in g.succ[x] if forb(k, L, x, z)}
        def clean(r, k):
            mm = len(r) - 1
            if k - mm < a0: return False
            for q in range(mm):
                if MUT == 2: continue
                if g.owner[r[q]] == 0 and (k - 1 - q + (1 if MUT == 1 else 0), r[q], r[q + 1]) in forbset: return False
            return True
        starts = S if os.environ.get("SUFFIX", "1") == "1" else [a]
        for a0 in starts:
            SS = [k for k in S if k >= a0]
            # P^c_sch (exhaustive paths, small n, k0 = a only)
            if a0 == a and n <= int(os.environ.get("PSCHMAX", "7")):
                succ = [[st[a]["t"][v]] if g.owner[v] == 1 else g.succ[v] for v in range(n)]
                for x in range(n):
                    stack = [[x]]
                    while stack:
                        p = stack.pop(); v = p[-1]
                        if v in cyc:
                            val = (v, 0, 0)
                            for w in reversed(p[:-1]): val = g.ext(w, val)
                            for k in SS:
                                if clean(p, k):
                                    cnt["PSCH_chk"] += 1
                                    if ckey(g, coarse(L, W[k][x])) < ckey(g, coarse(L, val)): fail(cnt, "PSCH", name, k, L, p)
                        if len(p) < n:
                            for w in succ[v]:
                                if w not in p: stack.append(p + [w])
            # FRZ-SCH, CHARGE, UNF, CHARGE-U
            Uev = set()
            for k in SS[:-1]:
                for y in Ev:
                    z = st[k + 1]["s"][y]
                    if z != st[k]["s"][y] and any((f, y, z) in forbset for f in range(max(a0, k - n + 1), k)): Uev.add((k, y, z))
            for x in range(n):
                prefix = {}
                for t in SS:
                    seq, cs = play(nx[t], x); prefix[t] = seq[:seq.index(lamW[a][x]) + 1] if lamW[a][x] in seq else None
                for t in SS:
                    r = prefix[t]
                    if r is None: fail(cnt, "PREFIX", name, t, x); continue
                    for s in SS:
                        if s > t: break
                        if clean(r, s):
                            cnt["FRZSCH_chk"] += 1
                            if any(coarse(L, W[q][x]) != coarse(L, W[t][x]) for q in range(s, t + 1)): fail(cnt, "FRZSCH", name, s, t, x, L)
                changes = 0
                for s in SS[1:]:
                    if coarse(L, W[s][x]) == coarse(L, W[s - 1][x]): continue
                    changes += 1
                    r = prefix[s]; mm = len(r) - 1
                    cnt["CHARGE_chk"] += 1
                    if s - 1 - mm < a0: cnt["WINDOW"] += 1; continue
                    ch = [(q, s - 2 - q) for q in range(mm) if g.owner[r[q]] == 0 and (s - 2 - q, r[q], r[q + 1]) in forbset]
                    if not ch: fail(cnt, "CHARGE", name, s, x, L); continue
                    cnt["CHARGED"] += 1
                    for (q, f) in ch:
                        y, z = r[q], r[q + 1]
                        kp = max(k for k in range(f, s) if st[k]["s"][y] != z)
                        cnt["UNF_chk"] += 1
                        if not (f < kp <= s - 1 <= f + n - 1 and st[kp + 1]["s"][y] == z and (kp, y, z) not in forbset): fail(cnt, "UNF", name, s, x, L)
                cnt["CHU_chk"] += 1; cnt["MAX_U"] = max(cnt["MAX_U"], len(Uev))
                if changes > (n - 1) * (1 + len(Uev)): fail(cnt, "CHU", name, a0, x, L, changes, len(Uev))


def analyse(g, start, cnt, name):
    st = RE.run(g, start)
    n, m = g.n, sum(len(s) for s in g.succ)
    info = [dict(Xi=x["Xi"], W=E.wval(g, x["s"], x["t"]), sb=x["sb"], fb=x["fb"]) for x in st]
    K = len(st); k = 0
    lam = [[v[0] for v in x["Xi"]] for x in st]
    while k < K:
        j = k
        while j + 1 < K and lam[j + 1] == lam[k] and st[j + 1]["t"] == st[k]["t"]: j += 1
        # runs inside phase [k, j]
        r = k
        while r <= j:
            e = r
            while e < j and not st[e]["fb"]: e += 1
            if e > r: cnt["RUNS_S"] += 1; analyse_run(g, st, info, r, e, cnt, name, n, m)
            r = e + 1
        k = j + 1


def main(a):
    cnt = Counter(); rng = random.Random(1717); nst = int(os.environ.get("RANDSTARTS", "3"))
    def do(g, name, r):
        for j, s in enumerate([RE.best_reward_start(g)] + [D.rand_start(g, r) for _ in range(nst)]):
            cnt["RUNS"] += 1; analyse(g, s, cnt, "%s/%d" % (name, j))
    if a[0] == "rand":
        N, lo, hi, km, seed = map(int, a[1:6]); r2 = random.Random(seed)
        for i in range(N):
            n = r2.randint(lo, hi)
            do(D.rand_ck(r2, n, r2.randint(0, min(km, n - 1))), "rand%d" % i, rng)
    else:
        for f in a:
            f, _, sf = f.partition(":")
            if f.endswith(".start"): continue
            sf = sf or (f[:-3] + ".start")
            g = RE.parse(f)
            if g.n > int(os.environ.get("MAXN", "40")): cnt["skip_big"] += 1; continue
            do(g, os.path.relpath(f), random.Random(os.path.relpath(f)))
            if os.path.exists(sf):  # given start pair (SIGMA0 / TAU0 lines, v:w); omitted vertices keep S3's choice
                b0 = RE.best_reward_start(g); s0, t0 = list(b0[0]), list(b0[1])
                for l in open(sf):
                    p_ = l.split()
                    if p_ and p_[0] in ("SIGMA0", "TAU0"):
                        for vw in p_[1:]:
                            v, w = map(int, vw.split(":")); (s0 if p_[0] == "SIGMA0" else t0)[v] = w
                cnt["RUNS"] += 1; cnt["given_starts"] += 1; analyse(g, (s0, t0), cnt, os.path.relpath(f) + "@start")
    for k in sorted(cnt): print(k, cnt[k])
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
