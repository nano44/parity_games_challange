#!/usr/bin/env python3
"""Box 210 Addendum A (L-NEW successor 72): a BRUTE-FORCE check of Lemma G-CLASS / GEN-LEVEL / GEN-PLATEAU on tiny split-form games,
written from the note alone by a fresh-context reviewer agent that this session started (read-only on the repository; NOT a fleet
referee; it changes no label). Own valuation (by the definition); Odd's reply by BRUTE FORCE over all positional Odd strategies (a
pointwise minimum; NO_POINTWISE_MIN is reported if none exists), so it does not assume «locally optimal => optimal» as gen210.py's
engine does; own Howard run; own checks of F1, [OPT], G-K1..G-K5, GL1, GL3, GL4, GL5, GP1..GP4 and the «switch in Y» step of Theorem
OF, for EVERY even up-set H and EVERY reference state b (BSEL=T: b = T only). Nothing of the repository is imported.
Output: one line per run set: «MUST0: all 0» or the counters that fired (with the first offending games), then descriptive counts.
Controls: CTRL=H (H not an up-set), CTRL=Hodd (H = the top k P-vertices whatever their parity), CTRL=nosplit (the game is not split).
Usage: brute210.py exh3 (all splits of 3-vertex games, all start strategies) | brute210.py exhgen NC NP (all general split-form games
       with NC choice and NP priority vertices) | brute210.py rsplit SEED COUNT N0 D DEG | brute210.py rgen SEED COUNT NC NP D"""
import sys, os, random, itertools, collections
CTRL = os.environ.get("CTRL", "")
BSEL = os.environ.get("BSEL", "all")

class SG:
    def __init__(self, prio, own, succ, isP):
        self.n = n = len(prio); self.prio = list(prio); self.own = list(own); self.succ = [list(s) for s in succ]; self.isP = list(isP)
        order = sorted(range(n), key=lambda v: (prio[v], v)); self.rank = [0] * n
        for r, v in enumerate(order): self.rank[v] = r
        self.byrank = order
        self.even = [prio[v] % 2 == 0 for v in range(n)]
        self.rew = [(self.rank[v] + 1) if self.even[v] else -(self.rank[v] + 1) for v in range(n)]
        self.w3 = [(3 ** self.rank[v]) * (1 if self.even[v] else -1) for v in range(n)]
        self.evc = [v for v in range(n) if not isP[v] and own[v] == 0]
        self.oddc = [v for v in range(n) if not isP[v] and own[v] == 1]
        self.evch = [v for v in self.evc if len(succ[v]) > 1]
        self.oddch = [v for v in self.oddc if len(succ[v]) > 1]
        self.P = [v for v in range(n) if isP[v]]
        # split form
        assert all(len(succ[v]) >= 1 for v in range(n))
        if CTRL != "nosplit":
            assert all(len(succ[v]) == 1 for v in self.P)
            assert all(isP[y] for v in range(n) if not isP[v] for y in succ[v])
            cr = [self.rank[v] for v in range(n) if not isP[v]]; pr = [self.rank[v] for v in self.P]
            assert (not cr) or (not pr) or max(cr) < min(pr)
    def dump(self):
        return "prio=%r own=%r succ=%r isP=%r" % (self.prio, self.own, self.succ, [int(b) for b in self.isP])
    def playvals(self, nxt):
        n, rank, w3, even, rew = self.n, self.rank, self.w3, self.even, self.rew
        val = [None] * n; key = [None] * n
        for v0 in range(n):
            pos = {}; path = []; v = v0
            while v not in pos: pos[v] = len(path); path.append(v); v = nxt[v]
            cyc = path[pos[v]:]; lam = cyc[0]
            for u in cyc:
                if rank[u] > rank[lam]: lam = u
            rl = rank[lam]; pi = 0; k2 = 0; k = 0; u = v0
            while u != lam:
                if rank[u] > rl: pi |= 1 << rank[u]; k2 += w3[u]
                u = nxt[u]; k += 1
            val[v0] = (lam, pi, k); key[v0] = (rew[lam], k2, -k if even[lam] else k)
        return val, key
    def reply(self, sigma, c=None):
        """brute force: all positional Odd strategies. returns (val, key, list of optimal nxt) or None if no pointwise minimum"""
        n = self.n
        base = [sigma[v] if (not self.isP[v] and self.own[v] == 0) else self.succ[v][0] for v in range(n)]
        res = []
        for combo in itertools.product(*[self.succ[g] for g in self.oddch]):
            nxt = base[:]
            for g, y in zip(self.oddch, combo): nxt[g] = y
            val, key = self.playvals(nxt); res.append((nxt, val, key))
        minkey = [min(r[2][v] for r in res) for v in range(n)]
        opt = [r for r in res if r[2] == minkey]
        if c is not None:
            c["replies"] += 1; c["odd_strategies"] += len(res)
            for nxt, val, key in res:
                if all(key[y] >= key[nxt[g]] for g in self.oddch for y in self.succ[g]):
                    c["locopt_strategies"] += 1
                    if key != minkey: c["LOCOPT_NOT_OPT"] += 1
        if not opt: return None
        return opt[0][1], minkey, [r[0] for r in opt]

def howard(G, sigma0, rng, tie="rand", c=None, cap=400):
    sigma = list(sigma0); hist = []
    while True:
        r = G.reply(sigma, c)
        if r is None: return None, sigma
        val, key, opts = r; hist.append((list(sigma), val, key, opts)); ns = list(sigma)
        for x in G.evch:
            cur = sigma[x]; bk = max(key[y] for y in G.succ[x])
            if key[cur] == bk: continue
            cands = [y for y in G.succ[x] if key[y] == bk]
            ns[x] = max(cands) if tie == "max" else (min(cands) if tie == "min" else rng.choice(cands))
        if ns == sigma or len(hist) > cap: break
        sigma = ns
    return hist, None

def upsets(G):
    """all even up-sets H (subsets of P): top-k vertices of the relevance order while they are even P-vertices"""
    out = [(0, frozenset())]; H = set(); m = 0
    for v in reversed(G.byrank):
        if not (G.even[v] and G.isP[v]): break
        H.add(v); m |= 1 << G.rank[v]; out.append((m, frozenset(H)))
    return out

MAXOPT = 12
def check(G, hist, c, bad, hsel="all"):
    n, rank, rew, succ, isP = G.n, G.rank, G.rew, G.succ, G.isP
    T = len(hist) - 1; sig = [h[0] for h in hist]; val = [h[1] for h in hist]; key = [h[2] for h in hist]
    opts = [h[3] if len(h[3]) <= MAXOPT else h[3][:MAXOPT // 2] + h[3][-MAXOPT // 2:] for h in hist]
    c["runs"] += 1; c["Tsum"] += T; c["Tmax"] = max(c["Tmax"], T)
    for t in range(T):
        for v in range(n):
            if key[t + 1][v] < key[t][v]: bad("F1", (t, v))
    ups = upsets(G)
    if CTRL == "H":      # control: H is NOT an up-set (top element removed) or contains an odd vertex
        ups2 = []
        for hm, H in ups:
            if len(H) >= 2:
                top = max(H, key=lambda v: rank[v]); ups2.append((hm & ~(1 << rank[top]), H - {top}))
        ups = ups2
    if CTRL == "Hodd":   # control: H = top-k vertices of P regardless of parity, k = 1..3
        ups = []; H = set(); hm = 0
        for v in list(reversed(G.byrank))[:3]:
            if not isP[v]: break
            H.add(v); hm |= 1 << rank[v]
            if not all(G.even[u] for u in H): ups.append((hm, frozenset(H)))
    if hsel == "top": ups = [ups[-1]]
    elif hsel == "none": ups = [ups[0]]
    evset = set(G.evc); oddset = set(G.oddc)
    for hmask, H in ups:
        c["H_runs"] += 1; c["H_nonempty"] += 1 if H else 0; c["H_proper"] += 1 if (H and hmask != ups[-1][0]) else 0
        cls = [[(rew[val[t][v][0]], val[t][v][1] & hmask) for v in range(n)] for t in range(T + 1)]
        # K2 on all values seen in this run: sorting by key must sort the classes
        allv = sorted(set((key[t][v], cls[t][v]) for t in range(T + 1) for v in range(n)))
        for i in range(len(allv) - 1):
            if allv[i + 1][1] < allv[i][1]: bad("K2", (allv[i], allv[i + 1]))
        for t in range(T + 1):
            for nxt in opts[t]:
                for v in range(n):
                    s = nxt[v]; lam = val[t][v][0]
                    if val[t][s][0] != lam: bad("K3lam", (t, v))
                    if v not in H or rank[v] <= rank[lam]:
                        if cls[t][v] != cls[t][s]: bad("K3eq", (t, v))
                    else:
                        if cls[t][v] != (rew[lam], (val[t][s][1] & hmask) | (1 << rank[v])) or not cls[t][v] > cls[t][s] or (val[t][s][1] >> rank[v]) & 1: bad("K3H", (t, v))
                for g in G.oddc:
                    if cls[t][g] != cls[t][nxt[g]]: bad("K4eq", (t, g))
            for g in G.oddc:
                for y in succ[g]:
                    if cls[t][g] > cls[t][y]: bad("K4", (t, g, y))
            if t < T:
                for v in range(n):
                    if cls[t + 1][v] < cls[t][v]: bad("K1", (t, v))
                for x in G.evc:
                    for y in succ[x]:
                        if cls[t + 1][x] < cls[t][y]: bad("K5", (t, x, y))
        for b in ([T] if BSEL == "T" and T >= 1 else range(1, T + 1)):
            fr = []
            for t in range(b + 1):
                lag = set(v for v in range(n) if cls[t][v] != cls[b][v])
                if not lag: fr.append(None); continue
                m = min(cls[t][v] for v in lag); fr.append((lag, m, frozenset(v for v in lag if cls[t][v] == m)))
            phis = set()
            allowed = set(cls[b][w] for x in G.evc for w in succ[x]) | set((rew[p], 0) for p in G.P)
            for t in range(b):
                if fr[t] is None:
                    if fr[t + 1] is not None: bad("L1sub", (b, t))
                    continue
                c["lagstates"] += 1
                lag, m, F = fr[t]; phis.add((m, len(F))); stall = all(cls[t + 1][v] == cls[t][v] for v in F)
                if fr[t + 1] is not None:
                    if not fr[t + 1][0] <= lag: bad("L1sub", (b, t))
                    p1, p2 = (m, -len(F)), (fr[t + 1][1], -len(fr[t + 1][2]))
                    if p2 < p1: bad("L1fall", (b, t))
                    if stall and (p2 != p1 or fr[t + 1][2] != F): bad("L1stall", (b, t))
                    if (not stall) and p2 == p1: bad("L1rise", (b, t))
                elif stall: bad("L1stallempty", (b, t))
                if m not in allowed: bad("L5set", (b, t))
                for nxt in opts[t]:
                    alpha = [z for z in F if z in evset and nxt[z] not in lag]
                    for z in alpha:
                        if m != cls[b][nxt[z]]: bad("L3m", (b, t, z))
                    beta = False
                    for v0 in F:
                        seen = set(); v = v0
                        while v in F and v not in seen: seen.add(v); v = nxt[v]
                        if v in F:
                            beta = True
                            if m != (rew[val[t][v][0]], 0): bad("L3beta_m", (b, t, v))
                            break
                    if not alpha and not beta: bad("L3", (b, t))
                    # proof steps of GL3/GL4 that do not need a stall
                    for z in F:
                        if isP[z] and nxt[z] not in F: bad("L4P", (b, t, z))
                        if z in oddset and nxt[z] not in F: bad("L4odd", (b, t, z))
                    if stall:
                        for z in F:
                            if z in evset and sig[b][z] not in F: bad("L4even", (b, t, z))
                if stall: c["stalls"] += 1
                else: c["nonstalls"] += 1
            if len(phis) > 2 * len(G.P) * n: bad("L5", b)
            # plateaus
            t = 0
            while t < b:
                if fr[t] is None: t += 1; continue
                u = t
                while t + 1 < b and fr[t + 1] is not None and (fr[t + 1][1], fr[t + 1][2]) == (fr[u][1], fr[u][2]): t += 1
                v = t; t += 1
                if v == u: continue
                c["plateaus"] += 1; c["platmax"] = max(c["platmax"], v - u); m = fr[u][1]; Y = set(x for x in range(n) if cls[u][x] <= m)
                for s in range(u, v + 1):
                    for x in range(n):
                        if (x in Y) != (cls[s][x] <= m) or (x in Y and cls[s][x] != cls[u][x]): bad("P1", (b, u, v, s, x))
                    for nxt in opts[s]:
                        for x in Y:
                            if nxt[x] not in Y: bad("P2", (b, s, x))
                        for g in G.oddc:
                            if g in Y and cls[s][nxt[g]] != cls[s][g]: bad("P4", (b, s, g))
                    for x in G.evc:
                        if x in Y:
                            for y in succ[x]:
                                if y not in Y or cls[s][y] > cls[s][x]: bad("P3", (b, s, x, y))
                    if s + 1 <= T and not any(sig[s + 1][x] != sig[s][x] for x in G.evc if x in Y): bad("OFswitchY", (b, u, v, s))
                # (OF1) satisfiable on this plateau? then v - u <= n_E(Y)
                oy = [g for g in G.oddch if g in Y]
                common = None
                for s in range(u, v + 1):
                    S = set(tuple(nxt[g] for g in oy) for nxt in hist[s][3])
                    common = S if common is None else (common & S)
                if common:
                    c["plateaus_OF1"] += 1
                    nE = sum(1 for x in Y if G.own[x] == 0)
                    if v - u > nE: bad("OFbound", (b, u, v, nE))
                    if v - u > len([x for x in G.evch if x in Y]): c["plat_gt_evchoiceY"] += 1

def split_of(prio0, own0, succ0, cpri=0):
    n0 = len(prio0)
    prio = [cpri] * n0 + [p + 2 for p in prio0]; own = list(own0) + [0] * n0
    succ = [[n0 + j for j in succ0[i]] for i in range(n0)] + [[i] for i in range(n0)]
    return SG(prio, own, succ, [False] * n0 + [True] * n0)

def nosplit(prio0, own0, succ0):
    return SG(list(prio0), list(own0), succ0, [len(s) == 1 for s in succ0])

def gen_split(rng, n0, d, deg, loops=True):
    prio0 = [rng.randint(0, d) for _ in range(n0)]; own0 = [rng.randrange(2) for _ in range(n0)]
    succ0 = [sorted(rng.sample(range(n0), rng.randint(1, min(deg, n0)))) for _ in range(n0)]
    if rng.random() < 0.3:   # a sink (self-loop only)
        i = rng.randrange(n0); succ0[i] = [i]
    if CTRL == "nosplit": return nosplit(prio0, own0, succ0)
    return split_of(prio0, own0, succ0)

def gen_general(rng, nC, nP, d):
    """general split form: C (priorities 0/1, any owner, successors a non-empty subset of P), P (priority 2..d+2, one successor: ANY vertex)"""
    n = nC + nP
    cmode = rng.randrange(3)
    prio = [(0 if cmode == 0 else 1 if cmode == 1 else rng.randrange(2)) for _ in range(nC)] + [rng.randint(2, d + 2) for _ in range(nP)]
    own = [rng.randrange(2) for _ in range(n)]
    succ = [sorted(rng.sample(range(nC, n), rng.randint(1, min(3, nP)))) for _ in range(nC)] + [[rng.randrange(n)] for _ in range(nP)]
    return SG(prio, own, succ, [False] * nC + [True] * nP)

class Bad:
    def __init__(self, c): self.c = c; self.ex = {}; self.ctx = None
    def __call__(self, name, info=None):
        self.c[name] += 1
        if name not in self.ex: self.ex[name] = (self.ctx, info)

MUST0 = ("NO_POINTWISE_MIN", "LOCOPT_NOT_OPT", "F1", "K1", "K2", "K3lam", "K3eq", "K3H", "K4", "K4eq", "K5", "L1sub", "L1fall", "L1stall", "L1rise",
         "L1stallempty", "L3", "L3m", "L3beta_m", "L4P", "L4odd", "L4even", "L5", "L5set", "P1", "P2", "P3", "P4", "OFswitchY", "OFbound")
def report(tag, c, bad):
    print(tag, "| MUST0:", " ".join("%s=%d" % (k, c[k]) for k in MUST0 if c[k]) or "all 0",
          "| " + " ".join("%s=%d" % (k, c[k]) for k in sorted(c) if k not in MUST0), flush=True)
    for name, (ctx, info) in bad.ex.items(): print("  FIRST", name, info, "GAME", ctx, flush=True)

def run_game(G, sigma0, rng, c, bad, tie="rand", hsel="all"):
    bad.ctx = G.dump() + " sigma0=%r" % (sigma0,)
    hist, s = howard(G, sigma0, rng, tie, c)
    c["games"] += 1
    if hist is None:
        bad("NO_POINTWISE_MIN", s); return None
    if len(hist) > 400: c["capped"] += 1; return None
    check(G, hist, c, bad, hsel); return hist

if __name__ == "__main__":
    a = sys.argv[1:]; mode = a[0]; c = collections.Counter(); bad = Bad(c)
    if mode == "exh3":
        # exhaustive: 3 original vertices, relevance = index order, all parity patterns, owners, successor sets, ALL start strategies
        rng = random.Random(1); n0 = 3; subs = [[j for j in range(n0) if (m >> j) & 1] for m in range(1, 1 << n0)]
        part = int(a[1]) if len(a) > 1 else None
        for pm in range(1 << n0):
            if part is not None and pm != part: continue
            prio0 = [2 * i + ((pm >> i) & 1) for i in range(n0)]
            for om in range(1 << n0):
                own0 = [(om >> i) & 1 for i in range(n0)]
                for ss in itertools.product(subs, repeat=n0):
                    G = split_of(prio0, own0, ss)
                    for st in itertools.product(*[G.succ[x] for x in G.evch]):
                        sigma0 = [G.succ[v][0] for v in range(G.n)]
                        for x, y in zip(G.evch, st): sigma0[x] = y
                        run_game(G, sigma0, rng, c, bad)
        report("exh3 part %r" % part, c, bad)
    elif mode == "exh4d2":
        # exhaustive: 4 original vertices, out-degree <= 2, relevance = index order, all parities / owners / successor sets / start strategies
        rng = random.Random(1); n0 = 4; subs = [[i] for i in range(n0)] + [[i, j] for i in range(n0) for j in range(i + 1, n0)]
        part = int(a[1]) if len(a) > 1 else None
        for pm in range(1 << n0):
            if part is not None and pm != part: continue
            prio0 = [2 * i + ((pm >> i) & 1) for i in range(n0)]
            for om in range(1 << n0):
                own0 = [(om >> i) & 1 for i in range(n0)]
                for ss in itertools.product(subs, repeat=n0):
                    G = split_of(prio0, own0, ss)
                    for st in itertools.product(*[G.succ[x] for x in G.evch]):
                        sigma0 = [G.succ[v][0] for v in range(G.n)]
                        for x, y in zip(G.evch, st): sigma0[x] = y
                        run_game(G, sigma0, rng, c, bad)
        report("exh4d2 part %r" % part, c, bad)
    elif mode == "exhgen":
        # exhaustive GENERAL split form: nC C-vertices (priority 0), nP P-vertices (relevance = index order, all parities), every P successor in V,
        # every C owner / successor set, ALL start strategies
        nC, nP = int(a[1]), int(a[2]); rng = random.Random(1); n = nC + nP
        subs = [[nC + j for j in range(nP) if (m >> j) & 1] for m in range(1, 1 << nP)]
        for pm in range(1 << nP):
            prio = [0] * nC + [2 + 2 * i + ((pm >> i) & 1) for i in range(nP)]
            for om in range(1 << nC):
                own = [(om >> i) & 1 for i in range(nC)] + [0] * nP
                for ps in itertools.product(range(n), repeat=nP):
                    for ss in itertools.product(subs, repeat=nC):
                        G = SG(prio, own, [list(x) for x in ss] + [[p] for p in ps], [False] * nC + [True] * nP)
                        for st in itertools.product(*[G.succ[x] for x in G.evch]):
                            sigma0 = [G.succ[v][0] for v in range(n)]
                            for x, y in zip(G.evch, st): sigma0[x] = y
                            run_game(G, sigma0, rng, c, bad)
        report("exhgen nC %d nP %d" % (nC, nP), c, bad)
    elif mode == "rsplit":
        seed, cnt, n0, d, deg = (int(x) for x in a[1:6]); rng = random.Random(seed)
        for i in range(cnt):
            G = gen_split(rng, n0, d, deg)
            sigma0 = [rng.choice(G.succ[v]) for v in range(G.n)]
            run_game(G, sigma0, rng, c, bad)
        report("rsplit seed %d cnt %d n0 %d d %d deg %d" % (seed, cnt, n0, d, deg), c, bad)
    elif mode == "rgen":
        seed, cnt, nC, nP, d = (int(x) for x in a[1:6]); rng = random.Random(seed)
        for i in range(cnt):
            G = gen_general(rng, nC, nP, d)
            sigma0 = [rng.choice(G.succ[v]) for v in range(G.n)]
            run_game(G, sigma0, rng, c, bad)
        report("rgen seed %d cnt %d nC %d nP %d d %d" % (seed, cnt, nC, nP, d), c, bad)
