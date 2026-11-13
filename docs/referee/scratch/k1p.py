#!/usr/bin/env python3
"""REFEREE successor 36: own tests for the first review of P-N5-KEY1P (l-new 44775605, sha1 f7191623...).

Written from the packet's sections 1-9 and from P-N5-REALIZE.md section 2 (through gkx.py's step(), the definition-based IDEAL
step); the lane's key1p.py / one217.py are not imported. One line of named must-0 counters per genome or set:
  ideq    Lemma IDEAL-1P (c), (d): the key run of 1P (integer values, own code below) differs from the IDEAL run of gkx.step()
  ordv    Lemma IDEAL-1P (a): at some state, for two options of one mover, [v_s larger] differs from the beta-set order
  l0a     Lemma 0 (a): a current key not in K(x); two options of a mover with one key; |K(x)| recursion against the enumeration
          of W-paths (small K only); the two bounds
  l0b     Lemma 0 (b): two distinct Xi-paths from x with one value (enumeration, small PXi only); the recursion; the bound
  l0c     Lemma 0 (c): two options of one mover with equal v_s at a run state
  a1v, a1mu   A1 (V), (mu) with their strict clauses
  a2      A2: sw(x) > min(|K|, |PXi|) - 1; max sw > T; T > sum sw
  a2p     A2-POLY: T > D * N^(1 + c log2 D) with c := max_x min(lev, hXi) / log2 N
  a3      A3 (i), (ii) on the key run;  a3r: A3 (ii) on runs of a RANDOM rule (each mover takes a random element of A_t(x))
  a4h     A4 (i), (ii);  a4x: A4 (iii) (both clauses)
  enum    ENUM-NEC (mindeg >= 2 only): k_c > (1/c) log2(T + 1) for c in {1, 3/4, 1/2}
Usage: k1p.py file G.json ... | k1p.py gk k ... | k1p.py rand SEED COUNT | k1p.py mut SEED COUNT G.json ... (COUNT mutants per
       file, 1 to 4 own random mutations each) | k1p.py lift D G.json ...   [--ctrl NAME]
Controls (--ctrl): howard (Howard's rule for KEY: a1mu), down (movers leave A: a1v), a2half, a3all, a4any, w0 (all weights 0: l0c,
ordv), perm (keys by a permuted gate order: ideq).
"""
import sys, os, json, random, math, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))     # python3 -I drops the script directory
import gkx

CTRL = ""

def weights(G):
    w = {}
    for x in range(G["N"]):
        for k, (wt, xt, b) in enumerate(G["opts"][x]):
            w[(x, k)] = 0 if CTRL == "w0" else (1 << G["br"][b]) * (1 if G["bp"][b] == 0 else -1)
    return w

def topo_xi(G):
    """movers ordered targets first (acyclic Xi-graph)."""
    N = G["N"]
    seen, out = set(), []
    def visit(x):
        if x in seen:
            return
        seen.add(x)
        for (_, xt, _) in G["opts"][x]:
            if xt >= 0:
                visit(xt)
        out.append(x)
    sys.setrecursionlimit(100000)
    for x in range(N):
        visit(x)
    return out

class OneP:
    def __init__(self, G):
        self.G = G
        self.N = G["N"]
        self.w = weights(G)
        self.order = topo_xi(G)
        self.bylev = sorted(range(self.N), key=lambda x: G["lev"][x])
        self.gperm = None
        if CTRL == "perm":
            M = sum(len(o) for o in G["opts"])
            p = list(range(M))
            random.Random(5).shuffle(p)
            self.gperm = p
    def gate(self, x, k):
        g = self.G["gate"][x][k]
        return self.gperm[g] if self.gperm else g
    def values(self, s):
        V = {}
        v = {}
        for x in self.order:
            for k, (wt, xt, b) in enumerate(self.G["opts"][x]):
                v[(x, k)] = self.w[(x, k)] + (V[xt] if xt >= 0 else 0)
            V[x] = v[(x, s[x])]
        return V, v
    def avail(self, s, V, v):
        return [[k for k in range(len(self.G["opts"][x])) if k == s[x] or v[(x, k)] > V[x]] for x in range(self.N)]
    def keys(self, s):
        key = {}
        for x in self.bylev:
            wt = self.G["opts"][x][s[x]][0]
            key[x] = (key[wt] if wt >= 0 else ()) + (self.gate(x, s[x]),)
        return key
    def step(self, s, rule="key", rnd=None):
        V, v = self.values(s)
        A = self.avail(s, V, v)
        s2 = list(s)
        key = {}
        for x in self.bylev:
            def okey(k):
                wt = self.G["opts"][x][k][0]
                return (key[wt] if wt >= 0 else ()) + (self.gate(x, k),)
            if rule == "key":
                kk = min(A[x], key=okey)
            elif rule == "howard":
                kk = max(A[x], key=lambda k: v[(x, k)])
            elif rule == "random":
                kk = rnd.choice(A[x])
            elif rule == "down":
                out = [k for k in range(len(self.G["opts"][x])) if k not in A[x]]
                kk = out[0] if out else s[x]
            s2[x] = kk
            key[x] = okey(kk)
        return s2
    def run(self, rule="key", rnd=None, cap=200000):
        S = [list(self.G["start"])]
        while True:
            s2 = self.step(S[-1], rule, rnd)
            if s2 == S[-1] or len(S) > cap:
                return S
            S.append(s2)

def count_K(G):
    """|K(x)| by the recursion of Lemma 0 (a)."""
    K = {}
    for x in sorted(range(G["N"]), key=lambda x: G["lev"][x]):
        K[x] = len(G["opts"][x]) if G["lev"][x] == 0 else sum(K[wt] for (wt, _, _) in G["opts"][x])
    return K

def enum_K(G, x, limit=3000):
    """the set of keys of the W-paths from x (None if more than limit)."""
    def rec(x):
        out = []
        for k, (wt, _, _) in enumerate(G["opts"][x]):
            if wt < 0:
                out.append((G["gate"][x][k],))
            else:
                sub = rec(wt)
                if sub is None:
                    return None
                out += [kappa + (G["gate"][x][k],) for kappa in sub]
            if len(out) > limit:
                return None
        return out
    return rec(x)

def count_P(G, order):
    P, h = {}, {}
    for x in order:
        P[x] = sum((P[xt] if xt >= 0 else 1) for (_, xt, _) in G["opts"][x])
        h[x] = max((h[xt] + 1 if xt >= 0 else 0) for (_, xt, _) in G["opts"][x])
    return P, h

def enum_P(G, w, x, limit=3000):
    """values of all Xi-paths from x (None if more than limit)."""
    def rec(x):
        out = []
        for k, (_, xt, _) in enumerate(G["opts"][x]):
            if xt < 0:
                out.append(w[(x, k)])
            else:
                sub = rec(xt)
                if sub is None:
                    return None
                out += [w[(x, k)] + v for v in sub]
            if len(out) > limit:
                return None
        return out
    return rec(x)

def check(G, name, n5=False):
    P1 = OneP(G)
    N = G["N"]
    degs = [len(o) for o in G["opts"]]
    D, mindeg = max(degs), min(degs)
    M = sum(degs)
    c = dict(ideq=0, ordv=0, l0a=0, l0b=0, l0c=0, a1v=0, a1mu=0, a2=0, a2p=0, a3=0, a3r=0, a4h=0, a4x=0, enum=0)
    rule = {"howard": "howard", "down": "down"}.get(CTRL, "key")
    S = P1.run(rule, cap=20000)
    T = len(S) - 1
    # IDEAL-1P: against the definition-based IDEAL run
    S0, word = gkx.run(G, cap=10 ** 6)
    if CTRL in ("", "perm", "w0", "a2half", "a3all", "a4any"):
        c["ideq"] = int(S != S0)
    Kc = count_K(G)
    Pc, hX = count_P(G, P1.order)
    # Lemma 0 (a), (b) by enumeration where small
    for x in range(N):
        lev = G["lev"][x]
        c["l0a"] += int(Kc[x] > D ** (lev + 1)) + int(mindeg >= 2 and Kc[x] < 2 ** (lev + 1))
        if Kc[x] <= 3000:
            ks = enum_K(G, x)
            c["l0a"] += int(ks is None or len(ks) != Kc[x] or len(set(ks)) != len(ks))
        c["l0b"] += int(Pc[x] > D ** (hX[x] + 1))
        if Pc[x] <= 3000:
            vs = enum_P(G, P1.w, x)
            c["l0b"] += int(vs is None or len(vs) != Pc[x] or len(set(vs)) != len(vs))
    sw = [0] * N
    Vs, vs_, mus = [], [], []
    for s in S:
        V, v = P1.values(s)
        Vs.append(V)
        vs_.append(v)
        mus.append(P1.keys(s))
    for t, s in enumerate(S):
        v = vs_[t]
        for x in range(N):
            vals = [v[(x, k)] for k in range(degs[x])]
            c["l0c"] += int(len(set(vals)) != len(vals))
            # IDEAL-1P (a): integer order against the beta-set order, every pair of options
            Bs = [gkx.Bset(G, s, x, k) for k in range(degs[x])]
            for k1 in range(degs[x]):
                for k2 in range(degs[x]):
                    if k1 != k2:
                        c["ordv"] += int((v[(x, k1)] > v[(x, k2)]) != gkx.ahead_sets(G, Bs[k1], Bs[k2]))
            # Lemma 0 (a): the current key is a key of a W-path whose last entry is the gate of the current option
            c["l0a"] += int(mus[t][x][-1] != P1.gate(x, s[x]) or len(mus[t][x]) != G["lev"][x] + 1)
    for t in range(T):
        for x in range(N):
            moved = S[t + 1][x] != S[t][x]
            sw[x] += moved
            c["a1v"] += int(Vs[t + 1][x] < Vs[t][x] or (moved and not Vs[t + 1][x] > Vs[t][x]))
            c["a1mu"] += int(mus[t + 1][x] > mus[t][x] or (moved and not mus[t + 1][x] < mus[t][x]))
    for x in range(N):
        kb = Kc[x] // 2 if CTRL == "a2half" else Kc[x]
        c["a2"] += int(sw[x] > min(kb, Pc[x]) - 1)
    c["a2"] += int(T > sum(sw)) + int(max(sw) > T)
    c["a2"] += int(sum(sw) > sum(min(Kc[x], Pc[x]) - 1 for x in range(N)))
    if N >= 2:
        cc = max(min(G["lev"][x], hX[x]) for x in range(N)) / math.log2(N)
        c["a2p"] = int(T > D * N ** (1 + cc * math.log2(D)) + 1e-9) if D >= 1 else 0
    # A3
    for x in range(N):
        if degs[x] == 2:
            (w0, x0, _), (w1, x1, _) = G["opts"][x]
            hyp1 = G["lev"][x] == 0 or w0 == w1
            hyp2 = x0 == x1
            if CTRL == "a3all":
                hyp1 = True
            if hyp1 or hyp2:
                c["a3"] += int(sw[x] > 1)
    # A3 (ii) under a random rule
    rnd = random.Random(1234)
    for rep in range(3):
        SR = P1.run("random", rnd, cap=5000)
        for x in range(N):
            if degs[x] == 2 and G["opts"][x][0][1] == G["opts"][x][1][1]:
                c["a3r"] += int(sum(1 for a, b in zip(SR, SR[1:]) if a[x] != b[x]) > 1)
    # A4
    for x in range(N):
        full = sw[x] == Kc[x] - 1
        if CTRL == "a4any":
            full = sw[x] >= 1
        if full:
            seq = [mus[t][x] for t in range(T + 1)]
            c["a4h"] += int(len(set(seq)) != Kc[x])
            c["a4h"] += sum(1 for t in range(T) if seq[t + 1] != seq[t] and S[t + 1][x] == S[t][x])
            if G["lev"][x] >= 1:
                for k, (wt, _, _) in enumerate(G["opts"][x]):
                    c["a4h"] += int(len(set(mus[t][wt] for t in range(T + 1))) != Kc[wt])
        if degs[x] == 2:
            sg = [vs_[t][(x, 0)] > vs_[t][(x, 1)] for t in range(T + 1)]
            XF = sum(1 for t in range(1, T + 1) if sg[t] != sg[t - 1])
            c["a4x"] += int(sw[x] > 1 + XF)
            if full:
                c["a4x"] += int(XF < Kc[x] - 2)
    # ENUM-NEC
    kinfo = ""
    if mindeg >= 2:
        for cexp in (1.0, 0.75, 0.5):
            lv = [G["lev"][x] for x in range(N) if sw[x] + 1 >= Kc[x] ** cexp - 1e-9]
            kc = 1 + max(lv) if lv else 0
            c["enum"] += int(kc > (1 / cexp) * math.log2(T + 1) + 1e-9)
            kinfo += f" k_{cexp:g} {kc}"
    line = (f"{name} ctrl {CTRL or 0} N {N} M {M} D {D} mindeg {mindeg} T {T} L {len(S0) - 1} stop {word} maxsw {max(sw)} "
            + " ".join(f"{a} {b}" for a, b in c.items()) + kinfo)
    return line, c, S

def rand_genome(rnd):
    d = rnd.randrange(1, 6)
    width = [rnd.randrange(1, 4) for _ in range(d)]
    lev = [l for l in range(d) for _ in range(width[l])]
    N = len(lev)
    bylev = {l: [x for x in range(N) if lev[x] == l] for l in range(d)}
    perm = list(range(N))
    rnd.shuffle(perm)                      # Xi-edges go from later to earlier in perm: acyclic
    pos = {x: i for i, x in enumerate(perm)}
    opts = []
    b = 0
    for x in range(N):
        row = []
        for k in range(rnd.randrange(1, 4)):
            wt = rnd.choice(bylev[lev[x] - 1]) if lev[x] >= 1 else -1
            cand = [y for y in range(N) if pos[y] < pos[x]]
            xt = rnd.choice(cand) if cand and rnd.random() < 0.8 else -1
            row.append([wt, xt, b])
            b += 1
        opts.append(row)
    M = b
    g = list(range(M))
    rnd.shuffle(g)
    r = list(range(M))
    rnd.shuffle(r)
    gate, i = [], 0
    for x in range(N):
        gate.append(g[i:i + len(opts[x])])
        i += len(opts[x])
    return {"N": N, "lev": lev, "deg": [len(o) for o in opts], "opts": opts, "gate": gate, "br": r,
            "bp": [rnd.randrange(2) for _ in range(M)], "start": [rnd.randrange(len(o)) for o in opts]}

def lift(G, Dn):
    """LIFT(G, D) from the packet's section 11: a chain of D degree-1 movers under G."""
    if Dn == 0:
        return G
    N = G["N"]
    M = sum(len(o) for o in G["opts"])
    H = json.loads(json.dumps(G))
    opts = []
    for i in range(Dn):
        opts.append([[i - 1 if i >= 1 else -1, -1, M + i]])
    for x in range(N):
        opts.append([[(wt + Dn) if wt >= 0 else Dn - 1, (xt + Dn) if xt >= 0 else -1, b] for (wt, xt, b) in G["opts"][x]])
    H["N"] = N + Dn
    H["lev"] = list(range(Dn)) + [l + Dn for l in G["lev"]]
    H["opts"] = opts
    H["gate"] = [[M + i] for i in range(Dn)] + [list(r) for r in G["gate"]]
    H["br"] = list(G["br"]) + [M + i for i in range(Dn)]
    H["bp"] = list(G["bp"]) + [0] * Dn
    H["start"] = [0] * Dn + list(G["start"])
    H["deg"] = [len(o) for o in opts]
    return H

def mutate(G, rnd):
    """One random mutation that keeps G a genome with an acyclic Xi-graph (own mutator; not the lane's climb217.mutate)."""
    H = json.loads(json.dumps(G))
    N = H["N"]
    M = sum(len(o) for o in H["opts"])
    for _ in range(50):
        kind = rnd.randrange(6)
        x = rnd.randrange(N)
        k = rnd.randrange(len(H["opts"][x]))
        if kind == 0 and H["lev"][x] >= 1:
            cand = [y for y in range(N) if H["lev"][y] == H["lev"][x] - 1]
            H["opts"][x][k][0] = rnd.choice(cand)
            return H
        if kind == 1:
            old = H["opts"][x][k][1]
            H["opts"][x][k][1] = rnd.choice(list(range(N)) + [-1])
            if gkx.member(H)[7] == 0 and H["opts"][x][k][1] != x:
                return H
            H["opts"][x][k][1] = old
        if kind == 2:
            a, b = rnd.sample(range(M), 2)
            H["br"][a], H["br"][b] = H["br"][b], H["br"][a]
            return H
        if kind == 3:
            b = rnd.randrange(M)
            H["bp"][b] ^= 1
            return H
        if kind == 4:
            y = rnd.randrange(N)
            j = rnd.randrange(len(H["opts"][y]))
            if (x, k) != (y, j):
                H["gate"][x][k], H["gate"][y][j] = H["gate"][y][j], H["gate"][x][k]
                return H
        if kind == 5 and len(H["opts"][x]) >= 2:
            H["start"][x] = (H["start"][x] + 1) % len(H["opts"][x])
            return H
    return H

def main():
    global CTRL
    a = sys.argv[1:]
    if "--ctrl" in a:
        i = a.index("--ctrl")
        CTRL = a[i + 1]
        del a[i:i + 2]
    cmd = a[0]
    tot = None
    def acc(c):
        nonlocal tot
        tot = c if tot is None else {k: tot[k] + c[k] for k in c}
    if cmd == "file":
        for f in a[1:]:
            G = json.load(open(f))
            rec = ""
            if "genome" in G:                      # a climb record of box 217: {"genome": ..., "T_key": ...}
                want = G.get("T_key")
                G = G["genome"]
                rec = f" recT {want}"
            line, c, S = check(G, f.split("/")[-1])
            if rec:
                rec += f" recdiff {int(len(S) - 1 != want)}"
            print(line + rec, flush=True)
    elif cmd == "gk":
        for k in map(int, a[1:]):
            G, _ = gkx.rule(k)
            line, c, _ = check(G, f"G_{k}")
            print(line, flush=True)
    elif cmd == "rand":
        seed, cnt = int(a[1]), int(a[2])
        rnd = random.Random(seed)
        maxT = steps = 0
        mem = 0
        for i in range(cnt):
            G = rand_genome(rnd)
            mem += int(sum(gkx.member(G)) != 0)
            line, c, S = check(G, f"rand{i}")
            acc(c)
            maxT = max(maxT, len(S) - 1)
            steps += len(S) - 1
        print(f"rand seed {seed} genomes {cnt} ctrl {CTRL or 0} notmember {mem} steps {steps} maxT {maxT} " +
              " ".join(f"{k} {v}" for k, v in tot.items()), flush=True)
    elif cmd == "mut":
        seed, cnt = int(a[1]), int(a[2])
        rnd = random.Random(seed)
        n = maxT = steps = mem = 0
        for f in a[3:]:
            G0 = json.load(open(f))
            for i in range(cnt):
                G = G0
                for _ in range(rnd.randrange(1, 5)):
                    G = mutate(G, rnd)
                mem += int(sum(gkx.member(G)) != 0)
                line, c, S = check(G, "mut")
                acc(c)
                n += 1
                maxT = max(maxT, len(S) - 1)
                steps += len(S) - 1
        print(f"mut seed {seed} genomes {n} ctrl {CTRL or 0} notmember {mem} steps {steps} maxT {maxT} " +
              " ".join(f"{k} {v}" for k, v in tot.items()), flush=True)
    elif cmd == "lift":
        Dn = int(a[1])
        for f in a[2:]:
            G = json.load(open(f))
            H = lift(G, Dn)
            line, c, S = check(H, f"LIFT({f.split('/')[-1]},{Dn})")
            _, _, S0 = check(G, "base")
            same = int([s[Dn:] for s in S] != S0)
            print(line + f" notmember {int(sum(gkx.member(H)) != 0)} liftdiff {same}", flush=True)

if __name__ == "__main__":
    main()
