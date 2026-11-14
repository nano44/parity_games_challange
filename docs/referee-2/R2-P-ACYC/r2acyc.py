#!/usr/bin/env python3
"""REFEREE-2 successor 32: own simulator for packet P-ACYC (L-SI 43, claude/l-si e3ac4b06). Shares no code with L-SI, L-NEW or REFEREE
(no si.py, no pg.py, no n5v/n5x, no gamma3/idealcyc); written from the R104 / R117 / R118 TEXTS quoted in P-ACYC §0.

Builds Γ(G) (R104) and Γ3(G) (R117) from a genome JSON (keys N, lev, opts[x] = [[wtarget, xitarget, oid], ...], gate[x][k], br, bp,
start), freezes every non-mover Even vertex at the stated start (transported through the pads on Γ3), and computes:
  - VJ values (Λ, Π, k) of a positional profile (own code), the order ⊴ of VJ00 §4.2 / Friedmann §3;
  - Odd's optimal counterstrategy σ̄ to σ by Odd policy iteration from the WORST start (every gate on its e-face, K2 on its loop),
    switch-all, strict improvements only; and, for M <= BRUTE, by brute force over ALL Odd strategies (pointwise minimum; checks that
    the pointwise optimum exists and counts the optimal strategies with an e-face anywhere);
  - Howard (R118 (a)) at the movers: switch to a ⊴-largest successor, keep σ(x) if it is one; labels C / R / p; T.
Counters (per (state, gate) pair unless stated): notbeta (σ̄ off the β-face), nonstrict (β-face not strictly ⊴-better for Odd than the
e-face under σ̄'s values), lamfail (Λ(v) differs from LAMBDA-CONST's map with w* = K1), wstar (states with σ̄(K2) not toward K1),
C, R, T > N, brute failures. Modes:
  run FILE.json|SET.jsonl ...      Howard on Γ and on Γ3 from the stored start, every state checked, plus RAND random mover states/genome
  Usage: r2acyc.py [--rand K] [--brute M] [--seed S] FILES...
"""
import sys, json, random, itertools
EORDER = "gate"
from functools import cmp_to_key


# ---------------------------------------------------------------- game construction (R104 / R117 texts)
def build(G, pads):
    N = G["N"]; opts = G["opts"]
    O = [(x, k) for x in range(N) for k in range(len(opts[x]))]; M = len(O)
    gi = {(x, k): G["gate"][x][k] for (x, k) in O}
    assert len(set(gi.values())) == M, "gate indices must be distinct"
    # e-priority order: R104's landed text says only «e of even priority above every β»; default = gate-index order;
    # EORDER == "lev": (lev of the option's mover, gate index), the order of L-NEW's gamma3.py (used only to compare the controls)
    kf = (lambda o: (G["lev"][o[0]], gi[o])) if EORDER == "lev" else (lambda o: gi[o])
    gr = {o: r for r, o in enumerate(sorted(O, key=kf))}
    oid = {(x, k): opts[x][k][2] for (x, k) in O}
    V = {}; prio = []; owner = []; succ = []

    def add(name, p, o):
        V[name] = len(prio); prio.append(p); owner.append(o); succ.append([])
    for x in range(N): add(("x", x), 0, 0)
    byg = sorted(O, key=lambda o: gi[o])
    for o in byg: add(("g", o), 1, 1)
    bprio = {o: 6 + 2 * G["br"][oid[o]] + G["bp"][oid[o]] for o in O}
    for o in byg: add(("b", o), bprio[o], 0)
    eb = max(bprio.values()); eb += 1 + (eb % 2 == 0)  # least even > every β... then shifted by 2*gate index
    eb = eb if eb % 2 == 0 else eb + 1
    for o in byg: add(("e", o), eb + 2 * gr[o], 0)
    add("unused", 2, 0)
    top = max(prio) + 2; top += top % 2
    add("cW", top, 0); add("K0", top + 2, 0); add("K1", 5, 0); add("K2", 3, 1); add("K3", top + 3, 0)
    # the pads (Γ3): single-successor Even pads, priority <= 2 (m-pad of the genome start option: 2; all others 0)
    def pad(name, p):
        add(name, p, 0)
        return V[name]

    def edge(a, b, padname=None, p=0):
        if pads and padname is not None:
            q = pad(padname, p); succ[V[a]].append(q); succ[q].append(V[b])
        else:
            succ[V[a]].append(V[b])
    for (x, k) in O:
        edge(("x", x), ("g", (x, k)), ("m", (x, k)), 2 if G["start"][x] == k else 0)
    for o in O:
        edge(("g", o), ("e", o), ("pe", o)); edge(("g", o), ("b", o), ("pbeta", o))
        x, k = o; wt, xt = opts[x][k][0], opts[x][k][1]
        if xt >= 0: edge(("b", o), ("x", xt))
        edge(("b", o), "K0", ("pb", o))
        if wt >= 0: edge(("e", o), ("x", wt))
        else: edge(("e", o), "cW")
    edge("unused", "unused"); edge("cW", "cW")
    edge("K0", "K1"); edge("K0", "K3", "pA")
    edge("K1", "K0", "q"); edge("K1", "K1", "s")
    edge("K2", "K1", "r"); edge("K2", "K2")
    edge("K3", "K1"); edge("K3", "K2")
    n = len(prio)
    if pads: assert n == N + 7 * M + 10, (n, N, M)
    else: assert n == N + 3 * M + 6, (n, N, M)
    # frozen start at non-mover Even vertices (R104's stated start, transported)
    fz = {}
    def first_to(a, target):  # successor of a leading (through a pad if any) to target
        for w in succ[V[a]]:
            if w == V[target] or (len(succ[w]) == 1 and succ[w][0] == V[target] and prio[w] <= 2 and w >= V["K3"] + 1):
                return w
        raise KeyError((a, target))
    for o in O:
        x, k = o; xt = opts[x][k][1]
        fz[V[("b", o)]] = first_to(("b", o), ("x", xt) if xt >= 0 else "K0")
    fz[V["K0"]] = first_to("K0", "K3"); fz[V["K1"]] = first_to("K1", "K1"); fz[V["K3"]] = V["K2"]
    for v in range(n):
        if owner[v] == 0 and len(succ[v]) == 1: fz[v] = succ[v][0]
    return dict(n=n, prio=prio, owner=owner, succ=succ, V=V, O=O, N=N, M=M, fz=fz, pads=pads)


# ---------------------------------------------------------------- VJ values
class VJ:
    def __init__(self, g):
        self.g = g; n = g["n"]
        order = sorted(range(n), key=lambda v: (g["prio"][v], v)); self.rel = [0] * n
        for i, v in enumerate(order): self.rel[v] = i + 1
        self.rew = [self.rel[v] if g["prio"][v] % 2 == 0 else -self.rel[v] for v in range(n)]

    def values(self, f):
        """f: successor of every vertex. Returns val[v] = (Λ, frozenset Π, k)."""
        g = self.g; n = g["n"]; rel = self.rel
        val = [None] * n; state = [0] * n
        pred = [[] for _ in range(n)]
        for v in range(n): pred[f[v]].append(v)
        for s in range(n):
            if state[s]: continue
            path = []; v = s
            while state[v] == 0: state[v] = 1; path.append(v); v = f[v]
            if state[v] == 1:  # new cycle
                cyc = path[path.index(v):]; L = max(cyc, key=lambda u: rel[u])
                val[L] = (L, frozenset(), 0)
                # BFS backwards from L
                stack = [L]
                while stack:
                    u = stack.pop()
                    for p in pred[u]:
                        if p == L or val[p] is not None: continue
                        Lam, P, k = val[u]
                        val[p] = (Lam, P | {p} if rel[p] > rel[Lam] else P, k + 1); stack.append(p)
            for u in path: state[u] = 2
        assert all(x is not None for x in val)
        return val

    def cmp(self, a, b):
        """-1 if a ◁ b (worse for Even), 0 equal, 1 if a ▷ b."""
        if a == b: return 0
        rel, rew, pr = self.rel, self.rew, self.g["prio"]
        if a[0] != b[0]: return 1 if rew[a[0]] > rew[b[0]] else -1
        if a[1] != b[1]:
            m = max(a[1] ^ b[1], key=lambda u: rel[u])
            good = pr[m] % 2 == 0
            return (1 if good else -1) if m in a[1] else (-1 if good else 1)
        if pr[a[0]] % 2 == 1: return 1 if a[2] > b[2] else -1
        return 1 if a[2] < b[2] else -1


def odd_opt(g, vj, sig, start=None):
    """Odd's optimal counterstrategy to sig by switch-all strict policy iteration (one-player game)."""
    n = g["n"]; tau = dict(start or {}); succ = g["succ"]
    for v in range(n):
        if g["owner"][v] == 1 and v not in tau: tau[v] = succ[v][-1]
    for _ in range(10 ** 5):
        f = [sig[v] if g["owner"][v] == 0 else tau[v] for v in range(n)]
        val = vj.values(f); ch = False
        for v in tau:
            best = tau[v]
            for w in succ[v]:
                if vj.cmp(val[w], val[best]) < 0: best = w
            if best != tau[v]: tau[v] = best; ch = True
        if not ch: return tau, val
    raise RuntimeError("odd PI did not converge")


def worst_start(g):
    V = g["V"]; st = {}
    for o in g["O"]:
        gv = V[("g", o)]; st[gv] = g["succ"][gv][0]  # e-face (first edge built)
    st[V["K2"]] = V["K2"]
    return st


def brute(g, vj, sig):
    """All Odd strategies: pointwise minimum exists? number of pointwise-optimal strategies, and how many use an e-face."""
    n = g["n"]; odd = [v for v in range(n) if g["owner"][v] == 1]
    allv = []
    for choice in itertools.product(*[g["succ"][v] for v in odd]):
        tau = dict(zip(odd, choice)); f = [sig[v] if g["owner"][v] == 0 else tau[v] for v in range(n)]
        allv.append((tau, vj.values(f)))
    mins = [min((val[v] for _, val in allv), key=cmp_to_key(vj.cmp)) for v in range(n)]
    opt = [tau for tau, val in allv if all(val[v] == mins[v] for v in range(n))]
    return len(opt), mins, opt


# ---------------------------------------------------------------- the checks
def check_state(g, vj, sig, tau, val, G, res):
    V = g["V"]; succ = g["succ"]; K1 = V["K1"]
    for o in g["O"]:
        gv = V[("g", o)]; ef, bf = succ[gv][0], succ[gv][1]
        if tau[gv] != bf: res["notbeta"] += 1
        if not vj.cmp(val[bf], val[ef]) < 0: res["nonstrict"] += 1
        res["pairs"] += 1
    if tau[V["K2"]] == V["K2"]: res["wstar_not_K1"] += 1
    # LAMBDA-CONST map
    lev0e = set()
    for o in g["O"]:
        x, k = o
        if G["opts"][x][k][0] < 0:
            lev0e.add(V[("e", o)])
            if ("pe", o) in V: lev0e.add(V[("pe", o)])
    for v in range(g["n"]):
        if v == V["cW"] or v in lev0e: exp = V["cW"]
        elif v == V["unused"]: exp = v
        else: exp = K1
        if val[v][0] != exp: res["lamfail"] += 1


def mover_sig(g, ms):
    """full σ: frozen part + mover choices ms[x] = option index (through the m-pad on Γ3)."""
    sig = dict(g["fz"]); V = g["V"]
    for x in range(g["N"]): sig[V[("x", x)]] = g["succ"][V[("x", x)]][ms[x]]
    return [sig.get(v, -1) for v in range(g["n"])]


def howard(g, vj, G, ms0, res, brute_m):
    V = g["V"]; N = g["N"]; ms = list(ms0); prev = None; T = 0; stt = []
    while True:
        sig = mover_sig(g, ms)
        tau, val = odd_opt(g, vj, sig, worst_start(g))
        tau2, _ = odd_opt(g, vj, sig, None)          # a second start (beta-face, K2 loop) must give the same σ̄
        if tau2 != tau: res["pi_startdep"] += 1
        check_state(g, vj, sig, tau, val, G, res); res["states"] += 1
        if g["M"] <= brute_m:
            cnt, mins, opt = brute(g, vj, sig); res["brute_states"] += 1
            if cnt == 0: res["brute_noopt"] += 1
            if any(any(t[V[("g", o)]] != g["succ"][V[("g", o)]][1] for o in g["O"]) for t in opt): res["brute_eface"] += 1
            if any(mins[v] != val[v] for v in range(g["n"])): res["brute_valdiff"] += 1
        lam = [val[v][0] for v in range(g["n"])]; sb = tuple(sorted(tau.items()))
        if prev is not None:
            if lam != prev[0]: res["C"] += 1
            elif sb != prev[1]: res["R"] += 1
        prev = (lam, sb); stt.append(tuple(ms))
        new = list(ms); ch = False
        for x in range(N):
            xv = V[("x", x)]; cur = g["succ"][xv][ms[x]]; best = cur; ties = 0
            for k, w in enumerate(g["succ"][xv]):
                c = vj.cmp(val[w], val[best])
                if c > 0: best = w
            bl = [w for w in g["succ"][xv] if vj.cmp(val[w], val[best]) == 0]
            if len(bl) > 1: res["howard_ties"] += 1
            if vj.cmp(val[best], val[cur]) > 0:
                new[x] = g["succ"][xv].index(max(bl)); ch = True
        if not ch: break
        ms = new; T += 1
        if T > 50 * N + 50: raise RuntimeError("Howard too long")
    return T, stt


def main(argv):
    K = 0; BR = 0; seed = 1; files = []
    i = 0
    while i < len(argv):
        if argv[i] == "--rand": K = int(argv[i + 1]); i += 2
        elif argv[i] == "--brute": BR = int(argv[i + 1]); i += 2
        elif argv[i] == "--seed": seed = int(argv[i + 1]); i += 2
        elif argv[i] == "--eorder":
            global EORDER
            EORDER = argv[i + 1]; i += 2
        else: files.append(argv[i]); i += 1
    rng = random.Random(seed)
    genomes = []
    for f in files:
        if f.endswith(".jsonl"):
            for j, line in enumerate(open(f)): genomes.append((f"{f.split('/')[-1]}#{j}", json.loads(line)))
        else: genomes.append((f.split("/")[-1], json.load(open(f))))
    keys = ["genomes", "acyclic", "states", "pairs", "notbeta", "nonstrict", "lamfail", "wstar_not_K1", "C", "R", "T_gt_N", "howard_ties",
            "pi_startdep", "brute_states", "brute_noopt", "brute_eface", "brute_valdiff", "T3_ne_T", "mover_seq_ne"]
    tot = {m: {k: 0 for k in keys} for m in ("G", "G3", "Grand", "G3rand")}
    maxTN = 0.0
    for name, G in genomes:
        N = G["N"]
        # Ξ-acyclicity (own test)
        adj = {x: {o[1] for o in G["opts"][x] if o[1] >= 0} for x in range(N)}
        col = {}; acyc = True
        def dfs(u):
            nonlocal acyc
            col[u] = 1
            for w in adj[u]:
                if col.get(w) == 1: acyc = False
                elif w not in col: dfs(w)
            col[u] = 2
        sys.setrecursionlimit(10000)
        for x in range(N):
            if x not in col: dfs(x)
        line = [name, f"N {N}", f"acyclic {int(acyc)}"]
        Ts = {}
        for mode, pads in (("G", False), ("G3", True)):
            g = build(G, pads); vj = VJ(g); r = tot[mode]; r["genomes"] += 1; r["acyclic"] += acyc
            before = dict(r)
            T, seq = howard(g, vj, G, G["start"], r, BR); Ts[mode] = (T, seq)
            r["T_gt_N"] += T > N
            if mode == "G": maxTN = max(maxTN, T / N)
            line.append(f"{mode}: T {T} " + " ".join(f"{k} {r[k] - before[k]}" for k in ("notbeta", "nonstrict", "lamfail", "wstar_not_K1", "C", "R")))
            # random frozen-frame states (BETA-ACYC / LAMBDA-CONST hold for EVERY σ in the frozen frame)
            rr = tot[mode + "rand"]; rr["genomes"] += 1
            for _ in range(K):
                ms = [rng.randrange(len(G["opts"][x])) for x in range(N)]
                sig = mover_sig(g, ms); tau, val = odd_opt(g, vj, sig, worst_start(g))
                check_state(g, vj, sig, tau, val, G, rr); rr["states"] += 1
                if g["M"] <= BR:
                    cnt, mins, opt = brute(g, vj, sig); rr["brute_states"] += 1
                    if cnt == 0: rr["brute_noopt"] += 1
                    if any(any(t[g["V"][("g", o)]] != g["succ"][g["V"][("g", o)]][1] for o in g["O"]) for t in opt): rr["brute_eface"] += 1
                    if any(mins[v] != val[v] for v in range(g["n"])): rr["brute_valdiff"] += 1
        if Ts["G"][0] != Ts["G3"][0]: tot["G3"]["T3_ne_T"] += 1
        if Ts["G"][1] != Ts["G3"][1]: tot["G3"]["mover_seq_ne"] += 1
        print(" | ".join(line))
    for m in tot:
        print(f"TOTAL {m}: " + " ".join(f"{k} {v}" for k, v in tot[m].items()))
    print(f"max T/N on Γ: {maxTN:.3f}")


if __name__ == "__main__":
    main(sys.argv[1:])
