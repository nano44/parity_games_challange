#!/usr/bin/env python3
"""REFEREE successor 24: own randomized check of P-IDEAL-KEYS (l-new b302bbf5) §2-§6 with my simulator t3r_sim.py (beta-SETS, no ENC;
no lane code). Random IDEAL-ACYC genomes: 2-5 levels, 1-3 movers per level, degree 1-3 (DEG2=1: every mover degree <= 2), W-targets any
mover one level down, Xi-targets acyclic (random topological order, exit allowed), distinct ranks / gates, random parities, random starts.
Checks per run (counts printed):
  LOCALKP  KF_x <= WE_x (every mover)                         PAIRKF  deg 2, lev >= 1: KF_x = 0 (a = b) / flips(a, b) (a != b)
  CASCADE  every flip of a same-level pair is own, or (l >= 1) below with w_p != w_q flipping at t
  FLET     flips(p, q) <= T                                    PMOVES  (DEG2 genomes) moves(x) <= 1 + flips(a,b) / <= 1
  RENEWA   top-only step t >= 2: previous step... (i) w not in A_(s_(t-2))(h), (ii) value of (h, w) strictly better at s_(t-1) than at
           s_(t-2) (set order), (iii) some z != h on chain of (h, w) under s_(t-2) in Mv_(t-1), all such z in D(h); first steps of
           maximal intervals: step a-1 is lower
  RENEWB   keys of top movers constant on [a-1, b]
  RETURN   deg-2 x, consecutive moves t1 < t2: other option's Xi-target z is a mover and cv(z) at s_(t2-1) strictly better than at s_(t1-1)
  RETCNT   moves(x) <= 1 + R(x,0) + R(x,1) (rises by set order)
  MERGEB   random s, s' agreeing on Pre_a u Pre_b: same Xi-order of (x, a), (x, b) (sign only; no ENC)
Controls (must fire): RETURN_OWN (z = Xi-target of the option x moved TO), CASCADE_PREV (below-flip looked for at t - 1).
Usage: python3 -I keys_check.py n seed   |   FILES='<glob>' python3 -I keys_check.py (every start if <= 64, else stored + 15 random)"""
import itertools, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import t3r_sim as R

DEG2 = os.environ.get("DEG2") == "1"

def rgen(rng):
    d = rng.randint(2, 5)
    lev = []
    for l in range(d):
        lev += [l] * rng.randint(1, 3)
    N = len(lev)
    order = list(range(N)); rng.shuffle(order); pos = {v: i for i, v in enumerate(order)}
    opts = []; b = 0
    for x in range(N):
        deg = rng.choice([1, 2, 2, 2] if DEG2 else [1, 2, 2, 3])
        o = []
        for k in range(deg):
            w = -1 if lev[x] == 0 else rng.choice([y for y in range(N) if lev[y] == lev[x] - 1])
            later = [y for y in range(N) if pos[y] > pos[x]]
            xt = rng.choice(later + [-1]) if later else -1
            o.append([w, xt, b]); b += 1
        opts.append(o)
    ranks = list(range(b)); rng.shuffle(ranks)
    gates = list(range(b)); rng.shuffle(gates)
    gate = []; i = 0
    for x in range(N):
        gate.append(gates[i:i + len(opts[x])]); i += len(opts[x])
    return {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": ranks, "bp": [rng.randrange(2) for _ in range(b)],
            "start": [rng.randrange(len(opts[x])) for x in range(N)]}

def W(G, x):
    out, st = set(), [x]
    while st:
        u = st.pop()
        for o in G["opts"][u]:
            if o[0] >= 0 and o[0] not in out:
                out.add(o[0]); st.append(o[0])
    return out

def D(G, x):
    out, st = set(), [x]
    while st:
        u = st.pop()
        for o in G["opts"][u]:
            if o[1] >= 0 and o[1] not in out:
                out.add(o[1]); st.append(o[1])
    return out

def ck(G, s, x):
    return R.key(G, s, x, s[x], {})

def kp(G, s, x):
    return min(range(len(G["opts"][x])), key=lambda k: R.key(G, s, x, k, {}))

def chain_movers(G, s, x, k):
    out = []
    y = G["opts"][x][k][1]
    while y >= 0:
        out.append(y); y = G["opts"][y][s[y]][1]
    return out

def avail(G, s, x):
    cur = R.value(G, s, x, s[x])
    return {k for k in range(len(G["opts"][x])) if k == s[x] or R.better(G, R.value(G, s, x, k), cur)}

C = {k: 0 for k in "LOCALKP PAIRKF CASCADE FLET PMOVES RENEWA RENEWB RETURN RETCNT MERGEB".split()}
V = {k: 0 for k in C}
import json, glob
CTL = {"RETURN_OWN": 0, "CASCADE_PREV": 0}
FILES = os.environ.get("FILES")
if FILES:
    lst = []
    for f in sorted(glob.glob(FILES, recursive=True)):
        try:
            G = json.load(open(f))
            if not (isinstance(G, dict) and "opts" in G and "start" in G and G["N"] <= 30):
                continue
            G["opts"] = [[list(o[:3]) for o in ox] for ox in G["opts"]]
            if any(G["lev"][o[0]] != G["lev"][x] - 1 for x in range(G["N"]) for o in G["opts"][x] if o[0] >= 0):
                continue
            R.run(G)
            lst.append(G)
        except Exception:
            continue
    n, seed = len(lst), 0
else:
    n, seed = int(sys.argv[1]), int(sys.argv[2])
rng = random.Random(seed); runs = steps = 0
for gi in range(n):
    G = lst[gi] if FILES else rgen(rng); N = G["N"]
    if FILES:
        nst = 1
        for x in range(N):
            nst *= len(G["opts"][x])
        starts = [list(c) for c in itertools.product(*[range(len(G["opts"][x])) for x in range(N)])] if nst <= 64 else \
                 [list(G["start"])] + [[rng.randrange(len(G["opts"][x])) for x in range(N)] for _ in range(15)]
    else:
        starts = [[rng.randrange(len(G["opts"][x])) for x in range(N)] for _ in range(3)]
    for st in starts:
        S = R.run(G, st); T = len(S) - 1; runs += 1; steps += T
        Mv = [None] + [{x for x in range(N) if S[t][x] != S[t - 1][x]} for t in range(1, T + 1)]
        moves = [sum(1 for t in range(1, T + 1) if x in Mv[t]) for x in range(N)]
        KF = [sum(1 for t in range(1, T + 1) if kp(G, S[t], x) != kp(G, S[t - 1], x)) for x in range(N)]
        def flipset(p, q, old=False):
            out = set()
            for t in range(1, T + 1):
                ref = S[t - 1] if old else S[t]
                if (ck(G, ref, p) < ck(G, ref, q)) != (ck(G, S[t - 1], p) < ck(G, S[t - 1], q)):
                    out.add(t)
            return out
        for x in range(N):
            Wx = W(G, x); WE = sum(1 for t in range(1, T + 1) if Mv[t] & Wx)
            C["LOCALKP"] += 1; V["LOCALKP"] += KF[x] > WE
        FL = {}
        for l in set(G["lev"]):
            L = [x for x in range(N) if G["lev"][x] == l]
            for p, q in itertools.permutations(L, 2):
                FL[(p, q)] = flipset(p, q)
        for (p, q), fs in FL.items():
            if p > q:
                continue
            C["FLET"] += 1; V["FLET"] += len(fs) > T
            for t in fs:
                C["CASCADE"] += 1
                if p in Mv[t] or q in Mv[t]:
                    continue
                l = G["lev"][p]
                wp, wq = G["opts"][p][S[t][p]][0], G["opts"][q][S[t][q]][0]
                if l == 0 or wp == wq or t not in FL.get((wp, wq), set()):
                    V["CASCADE"] += 1
                if not (l == 0 or wp == wq or (t - 1) in FL.get((wp, wq), set())):
                    CTL["CASCADE_PREV"] += 1
        for x in range(N):
            if len(G["opts"][x]) == 2 and G["lev"][x] >= 1:
                a, b = G["opts"][x][0][0], G["opts"][x][1][0]
                C["PAIRKF"] += 1
                exp = 0 if a == b else len(FL[(a, b)])
                V["PAIRKF"] += KF[x] != exp
                if all(len(o) <= 2 for o in G["opts"]):
                    C["PMOVES"] += 1; V["PMOVES"] += moves[x] > 1 + exp
            elif all(len(o) <= 2 for o in G["opts"]):
                C["PMOVES"] += 1; V["PMOVES"] += moves[x] > 1
        tau = max(G["lev"])
        top = [t >= 1 and all(G["lev"][x] == tau for x in Mv[t]) for t in range(T + 1)]
        t = 1
        while t <= T:
            if not top[t]:
                t += 1; continue
            a = t
            while t + 1 <= T and top[t + 1]:
                t += 1
            b = t; t += 1
            C["RENEWB"] += 1
            for h in [x for x in range(N) if G["lev"][x] == tau]:
                for k in range(len(G["opts"][h])):
                    ks = {R.key(G, S[u], h, k, {}) for u in range(a - 1, b + 1)}
                    V["RENEWB"] += len(ks) != 1
            for u in range(max(a, 2), b + 1):
                if u == a:
                    V["RENEWA"] += top[a - 1]
                for h in Mv[u]:
                    C["RENEWA"] += 1
                    w = S[u][h]
                    i_ = w not in avail(G, S[u - 2], h)
                    ii = R.better(G, R.value(G, S[u - 1], h, w), R.value(G, S[u - 2], h, w))
                    Z = [z for z in chain_movers(G, S[u - 2], h, w) if z != h and z in Mv[u - 1]]
                    iii = bool(Z) and all(z in D(G, h) for z in Z)
                    V["RENEWA"] += not (i_ and ii and iii)
        for x in range(N):
            if len(G["opts"][x]) != 2:
                continue
            ts = [t for t in range(1, T + 1) if x in Mv[t]]
            for t1, t2 in zip(ts, ts[1:]):
                C["RETURN"] += 1
                o2 = 1 - S[t1][x]; z = G["opts"][x][o2][1]
                V["RETURN"] += z < 0 or not R.better(G, R.value(G, S[t2 - 1], z, S[t2 - 1][z]), R.value(G, S[t1 - 1], z, S[t1 - 1][z]))
                zo = G["opts"][x][S[t1][x]][1]
                CTL["RETURN_OWN"] += zo < 0 or not R.better(G, R.value(G, S[t2 - 1], zo, S[t2 - 1][zo]), R.value(G, S[t1 - 1], zo, S[t1 - 1][zo]))
            Rk = 0
            for k in range(2):
                z = G["opts"][x][k][1]
                if z >= 0:
                    Rk += sum(1 for u in range(1, T + 1) if R.better(G, R.value(G, S[u], z, S[u][z]), R.value(G, S[u - 1], z, S[u - 1][z])))
            C["RETCNT"] += 1; V["RETCNT"] += moves[x] > 1 + Rk
    # MERGE (b), random states
    for _ in range(5):
        s = tuple(rng.randrange(len(G["opts"][y])) for y in range(N))
        x = rng.randrange(N)
        if len(G["opts"][x]) < 2:
            continue
        a, b = rng.sample(range(len(G["opts"][x])), 2)
        ya, zb = chain_movers(G, s, x, a), chain_movers(G, s, x, b)
        m = next((y for y in ya if y in zb), None)
        pre = set(ya[:ya.index(m)] if m is not None else ya) | set(zb[:zb.index(m)] if m is not None else zb)
        s2 = tuple(s[y] if y in pre else rng.randrange(len(G["opts"][y])) for y in range(N))
        C["MERGEB"] += 1
        o1 = R.better(G, R.value(G, s, x, a), R.value(G, s, x, b))
        o2 = R.better(G, R.value(G, s2, x, a), R.value(G, s2, x, b))
        V["MERGEB"] += o1 != o2
print("CONTROLS (must fire) " + " ".join(f"{k} {v}" for k, v in CTL.items()))
print(f"genomes {n} seed {seed} FILES {FILES} DEG2 {int(DEG2)} runs {runs} steps {steps}")
print("CHECKS " + " ".join(f"{k} {v}" for k, v in C.items()))
print("VIOL   " + " ".join(f"{k} {v}" for k, v in V.items()))
