#!/usr/bin/env python3
"""L-RED 65 R231 item 1: INDEPENDENT counters for L-NEW 70 BOX 206 (l-new 9d360059 + Add. A 8e6a4641) on L-RED's own engine
(r221q/own.py). No L-NEW code. Scope: every vertex of Gamma(G) (n = N + 3M + 6).
Definitions (box 206 §0): class_t(v) = (Lambda_t(v), E_t(v)); change depth at a fixed-Lambda E change = #elements of E_(t-1) ∪ E_t more
relevant than z (z = most relevant element of the symmetric difference); loud depth of a loud step = -1 if some Lambda changes, else the
least change depth.  Must-0 counters:
  elfall  (vertex, step) with Lambda fixed and E falling (R121 E-MON)
  pfail   (change, c), c = 0..CMAX: P^(c) (c+1 most relevant of E) does not strictly rise at a change of depth <= c, or moves at depth > c
  cfail   (vertex, Lambda-interval, c): more than S_c(M) - 1 changes of depth <= c (DEPTH-COUNT)
  qfail   (genome, c): Q > n(2M+2) + n(2M+3)(S_c(M)-1) + Q_(>c) (LOUD-SPLIT), or with (N+M) for n in the middle term (DIV-LOUD)
  tfail   genome with T > Q + (Q+1) L (LOUD-SPLIT (i), QUIET's L)
  dnop / dlam / dsym / ddep / dkind  (v, t) DIV failures: no divergence vertex p before the first w; Lambda(p) != w at t-1 or t;
          E(p)'s symmetric difference != E(v)'s; depth(p) > depth(v); p neither a switching mover nor a flipping gate
  dlfail  loud step (no Lambda change) whose loud depth is not attained at a switching mover or flipping gate (DIV-LOUD)
Descriptive: T, Q, loud-depth histogram, maxdepth, Q_(>1).
Usage: dep231.py G.json ... | dep231.py rand SEED COUNT [k1]"""
import sys, os, json, random
from math import comb
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r221q"))
import own
CMAX = 3
def S(c, m): return sum(comb(m, j) for j in range(c + 2))
def measure(G, cap=20000, ctrl=0):
    out, V, O, ow = own.run(G, cap); n, prio, _, succ, _, _ = own.build(G); N = G["N"]; M = len(O); rk = own.VJ(prio).rk
    if ctrl == 1: rk = {v: -r for v, r in rk.items()}                      # control: relevance reversed for the depth bookkeeping
    evs = {V[("e", q)] for q in O}; name = {v: k for k, v in V.items()}
    movers = set(range(N)); gates = {V[("g", q)] for q in O}
    cls = []; nxts = []
    for s, vals, tau in out:
        cls.append([(vals[v][0], frozenset(u for u in vals[v][1] if u in evs)) for v in range(n)])
        nxts.append([(s[v] if v < N else succ[v][0]) if ow[v] == 0 else tau[v] for v in range(n)])
    T = len(out) - 1
    c = dict(T=T, N=N, M=M, n=n, elfall=0, pfail=0, cfail=0, qfail=0, tfail=0, dnop=0, dlam=0, dsym=0, ddep=0, dkind=0, dlfail=0,
             divcases=0, maxdepth=-1, Q=0)
    hist = {}
    def top(E, k): return sorted(E, key=lambda u: -rk[u])[:k]
    def lt(A, B):   # A < B in lex order (most relevant element of A Δ B lies in B)
        d = set(A) ^ set(B); return bool(d) and max(d, key=lambda u: rk[u]) in B
    cnt = {}   # (v, lam, c) -> changes of depth <= c
    for t in range(1, T + 1):
        A, B = cls[t - 1], cls[t]
        lamch = any(A[v][0] != B[v][0] for v in range(n)); loud = any(A[v] != B[v] for v in range(n))
        depths = {}
        for v in range(n):
            (la, Ea), (lb, Eb) = A[v], B[v]
            if la != lb or Ea == Eb: continue
            d = Ea ^ Eb; z = max(d, key=lambda u: rk[u]); dep = sum(1 for u in Ea | Eb if rk[u] > rk[z]); depths[v] = dep
            c["maxdepth"] = max(c["maxdepth"], dep)
            if z not in Eb: c["elfall"] += 1
            for cc in range(CMAX + 1):
                Pa, Pb = top(Ea, cc + 1), top(Eb, cc + 1)
                if dep <= cc:
                    if not lt(Pa, Pb): c["pfail"] += 1
                    cnt[(v, la, cc)] = cnt.get((v, la, cc), 0) + 1
                elif set(Pa) != set(Pb): c["pfail"] += 1
            # DIV
            c["divcases"] += 1; w = la; na, nb = nxts[t - 1], nxts[t]; u = v; p = None; seen = set()
            while u != w and u not in seen:
                seen.add(u)
                if na[u] != nb[u]: p = u; break
                u = na[u]
            if p is None: c["dnop"] += 1; continue
            if ctrl == 2: p = na[p]                                       # control: p replaced by its old successor
            (pa, Fa), (pb, Fb) = A[p], B[p]
            if pa != w or pb != w: c["dlam"] += 1; continue
            if (Fa ^ Fb) != d: c["dsym"] += 1
            zp = max(Fa ^ Fb, key=lambda u: rk[u]) if Fa ^ Fb else None
            if zp is not None and sum(1 for u in Fa | Fb if rk[u] > rk[zp]) > dep: c["ddep"] += 1
            if not ((p in movers and out[t][0][p] != out[t - 1][0][p]) or (p in gates and na[p] != nb[p])): c["dkind"] += 1
        if loud:
            c["Q"] += 1
            ld = -1 if lamch else min(depths.values())
            hist[ld] = hist.get(ld, 0) + 1
            if not lamch:
                att = [v for v in depths if depths[v] == ld]
                if not any((v in movers and out[t][0][v] != out[t - 1][0][v]) or (v in gates and nxts[t - 1][v] != nxts[t][v]) for v in att):
                    c["dlfail"] += 1
    for (v, la, cc), k in cnt.items():
        if k > S(cc, M) - 1: c["cfail"] += 1
    L = (M + 1) * (2 * M + 1) * (N + 1) + N * (n - 1)
    for cc in range(CMAX + 1):
        Qc = sum(h for d, h in hist.items() if d > cc)
        if c["Q"] > n * (2 * M + 2) + n * (2 * M + 3) * (S(cc, M) - 1) + Qc: c["qfail"] += 1
        if c["Q"] > n * (2 * M + 2) + (N + M) * (2 * M + 3) * (S(cc, M) - 1) + Qc: c["qfail"] += 1
    if T > c["Q"] + (c["Q"] + 1) * L: c["tfail"] += 1
    c["hist"] = dict(sorted(hist.items())); c["Q>1"] = sum(h for d, h in hist.items() if d > 1)
    return c
def rgen(rng, d, w, D):          # = L-RED r221q brute221.rgen (Xi-cyclic allowed), copied from r230/bonly3_230.py
    N = d * w; lev = [x // w for x in range(N)]; opts = []
    for x in range(N):
        opts.append([[(rng.choice([y for y in range(N) if lev[y] == lev[x] - 1]) if lev[x] else -1), rng.choice(list(range(N)) + [-1]), 0] for _ in range(D)])
    M = N * D; perm = list(range(M)); rng.shuffle(perm); gate = []; i = 0
    for x in range(N):
        gate.append([])
        for o in opts[x]: o[2] = i; gate[x].append(perm[i]); i += 1
    br = list(range(M)); rng.shuffle(br)
    return {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": [rng.randrange(2) for _ in range(M)], "start": [rng.randrange(D) for _ in range(N)]}
MUST0 = ("elfall", "pfail", "cfail", "qfail", "tfail", "dnop", "dlam", "dsym", "ddep", "dkind", "dlfail")
if __name__ == "__main__":
    ctrl = int(os.environ.get("DEP_CTRL", "0"))
    if sys.argv[1] == "rand":
        from blk231 import xi_k
        rng = random.Random(int(sys.argv[2])); k1 = len(sys.argv) > 4
        def gen():
            i = 0
            while i < int(sys.argv[3]):
                G = rgen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.choice([2, 3]))
                if k1 and xi_k(G) != 1: continue
                yield f"r{i}", G; i += 1
        Gs = gen()
    else: Gs = ((os.path.basename(f), json.load(open(f))) for f in sys.argv[1:])
    tot = {k: 0 for k in MUST0}; tot.update(genomes=0, divcases=0, Q=0); H = {}
    for tag, G in Gs:
        if not (isinstance(G, dict) and "opts" in G): continue
        c = measure(G, ctrl=ctrl); tot["genomes"] += 1
        for k in MUST0 + ("divcases", "Q"): tot[k] += c[k]
        for d, h in c["hist"].items(): H[d] = H.get(d, 0) + h
        if sys.argv[1] != "rand" or any(c[k] for k in MUST0): print(tag, {k: c[k] for k in ("N", "M", "T", "Q", "maxdepth", "Q>1", "hist") + MUST0 + ("divcases",)}, flush=True)
    print("TOTAL", tot, "hist", dict(sorted(H.items())), flush=True)
