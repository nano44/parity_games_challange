#!/usr/bin/env python3
"""L-RED 64 R230 (adversary vs L-SI 50 Lemma B-ONLY3 on Gamma3): census of B-ONLY3 violations on Gamma3(G) (all pads, L-NEW box189
gamma3.build at l-new fcba92fc; values by L-SI si.Engine; N5'-xi by L-NEW box190 n5v.run mode xi).
Violation at (state sigma, vertex v): v not an exception and rank(Lambda_sigma(v)) >= min rank of the e-vertices (Lambda at or above an
e-vertex; this includes «v's optimal cycle carries an e-vertex», since only e, c_W, K0, K3 outrank an e-vertex).
Exceptions EXC = {c_W} + {e_q, pe_q : q's W-target is c_W} (R123's list plus the pe pads of the e's with successor c_W).
Also counts gate ties Omega(pe_g) == Omega(pbeta_g) (NO-TIE3 shape) and Lambda in {K0, K3, c_W} at a non-exception.
State sets (each counted separately):
  FRAME-X  every mover state (sigma = transported start off the movers), exhaustive if the product of degrees <= XCAP, else XCAP random
  HOWARD   the Howard run at the movers on Gamma3 from the transported start (ties: keep current, then larger index); TIE states =
           states where some mover has >= 2 options of equal best Howard key (exact VJ tie)
  XI-STD   N5'-xi states from S3 that are standard (sigma = transported start off the movers)        -> inside B-ONLY3's frame
  XI-NSTD  N5'-xi states that are not standard (post-fallback etc.)                                 -> OUTSIDE the frame (reported apart)
BRUTE=1: second engine: Lambda by brute force over all positional Odd strategies (pointwise minimum, own VJ order), states with M <= 8.
Env: LNEW = git archive of l-new fcba92fc (experiments/new/box189, box190, box21, experiments/new/*.py, experiments/si, harness).
Usage: bonly3_230.py G.json ...  |  bonly3_230.py rand SEED COUNT   (prints one line per genome, a TOTAL line; VIOLATION lines)"""
import sys, os, json, random, itertools
L = os.environ["LNEW"]
sys.path[:0] = [os.path.join(L, "experiments/new/box189"), os.path.join(L, "experiments/new/box190"), os.path.join(L, "experiments/new/box21"),
                os.path.join(L, "experiments/new"), os.path.join(L, "experiments/si"), os.path.join(L, "experiments/harness")]
import gamma3, n5v, pg
from si import Engine
XCAP = int(os.environ.get("XCAP", "2048")); BRUTE = os.environ.get("BRUTE") == "1"; XI = os.environ.get("XI", "1") == "1"
PADS = {"K", "pe", "pb", "m"}

def topg(g): return f"parity {g.n - 1};\n" + "".join(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n" for v in range(g.n))

def brute_lambda(g, rank, sigma):
    """Lambda of the pointwise-optimal Odd reply, by enumerating Odd's positional strategies (independent of si.Engine)."""
    n = g.n; odd = [v for v in range(n) if g.owner[v] == 1]
    par = [g.prio[v] % 2 for v in range(n)]
    def rew(v): return 2 * rank[v] + 1 if par[v] == 0 else -(2 * rank[v] + 1)
    def keyv(val):
        w, P, ln = val; sw = sorted(P, key=lambda u: -rank[u])
        return (rew(w), tuple(rew(u) for u in sw), -ln if par[w] == 0 else ln)   # path set compared lexicographically by relevance
    def pkey(val):                                                            # Friedmann set order via signed weights
        w, P, ln = val; s = sum((1 << rank[u]) if par[u] == 0 else -(1 << rank[u]) for u in P)
        return (rew(w), s, -ln if par[w] == 0 else ln)
    best = [None] * n
    for ch in itertools.product(*[g.succ[v] for v in odd]):
        nx = list(sigma)
        for v, w in zip(odd, ch): nx[v] = w
        for v in range(n):
            seen = {}; p = []; u = v
            while u not in seen: seen[u] = len(p); p.append(u); u = nx[u]
            cyc = p[seen[u]:]; w = max(cyc, key=lambda z: rank[z]); pre = p[:p.index(w)]
            val = (w, frozenset(z for z in pre if rank[z] > rank[w]), len(pre))
            if best[v] is None or pkey(val) < pkey(best[v]): best[v] = val
    return [b[0] for b in best]

def census(G, tag):
    gm, sig0, tau0, V = gamma3.build(G, PADS); n = gm.n; E = Engine(gm); rank = E.rank
    N = G["N"]; opts = G["opts"]; O = [(x, k) for x in range(N) for k in range(len(opts[x]))]
    evs = [V[("e", q)] for q in O]; emin = min(rank[e] for e in evs)
    cW, K0, K3 = V["cW"], V[("K", 0)], V[("K", 3)]
    exc = {cW} | {V[("e", q)] for q in O if opts[q[0]][q[1]][0] < 0} | {V[("pe", q)] for q in O if opts[q[0]][q[1]][0] < 0}
    base = [sig0.get(v, -1) if gm.owner[v] == 0 else -1 for v in range(n)]
    def strat(ms):
        s = list(base)
        for x in range(N): s[x] = V[("m", (x, ms[x]))]
        return s
    R = dict(states=0, pairs=0, viol=0, top=0, ties=0)
    res = {k: dict(R) for k in ("FRAME-X", "HOWARD", "HOWARD-TIE", "XI-STD", "XI-NSTD")}; res["brute"] = dict(states=0, diff=0)
    first = []
    def score(s, key, label):
        vs, _ = E.evaluate(tuple(s)); r = res[key]; r["states"] += 1; bad = []
        for v in range(n):
            if v in exc: continue
            r["pairs"] += 1; lam = vs[v][0]
            if rank[lam] >= emin: r["viol"] += 1; bad.append((v, lam))
            if lam in (K0, K3, cW): r["top"] += 1
        r["ties"] += sum(1 for q in O if vs[V[("pe", q)]] == vs[V[("pbeta", q)]])
        if bad and len(first) < 3: first.append((label, key, bad[:4]))
        if BRUTE and len(O) <= 8 and key != "XI-NSTD":
            bl = brute_lambda(gm, rank, s); res["brute"]["states"] += 1
            res["brute"]["diff"] += sum(1 for v in range(n) if bl[v] != vs[v][0])
        return vs
    degs = [len(o) for o in opts]; tot = 1
    for d in degs: tot *= d
    if tot <= XCAP: it = itertools.product(*[range(d) for d in degs])
    else:
        rng = random.Random(230); it = (tuple(rng.randrange(d) for d in degs) for _ in range(XCAP))
    for ms in it: score(strat(ms), "FRAME-X", ms)
    ms = list(G["start"]); seen = set()
    while tuple(ms) not in seen:                                      # Howard at the movers on Gamma3, transported start off them
        seen.add(tuple(ms)); s = strat(ms); vs = score(s, "HOWARD", tuple(ms)); nm = list(ms); tie = False
        for x in range(N):
            ks = [E.key(E.extend(x, vs[V[("m", (x, k))]])) for k in range(degs[x])]; b = max(ks)
            if ks.count(b) >= 2: tie = True
            if ks[ms[x]] < b: nm[x] = max(k for k in range(degs[x]) if ks[k] == b)
        if tie: score(s, "HOWARD-TIE", tuple(ms))
        if nm == ms: break
        ms = nm
    res["T_how"] = len(seen) - 1
    if XI:
        gp = pg.parse(topg(gm)); E1, Ed1 = n5v.Engine(gp), n5v.Engine(n5v.dual(gp))
        s, t = n5v.n5x.start_pair(gp, E1, Ed1, None); st = [(tuple(s), tuple(t))]; fbs = []
        while len(st) <= 20000:
            r = n5v.step(gp, E1, Ed1, s, t, "xi")
            if r is None: break
            s, t, _, _, fb = r; st.append((tuple(s), tuple(t))); fbs.append(fb)
        ffb = next((i + 1 for i, f in enumerate(fbs) if f), len(st))   # index of the state reached by the first fallback
        res["xi_iter"] = len(st) - 1; res["xi_fb"] = sum(fbs); res["xi_ffb"] = ffb
        movers = set(range(N)); mpad = {V[("m", q)] for q in O}; early = 0
        for i, (s, t) in enumerate(st):
            std = all(s[v] == base[v] for v in range(n) if gm.owner[v] == 0 and v not in movers) and all(s[x] in mpad for x in range(N))
            if not std and i < ffb: early += 1                         # [STD3] failure before the first fallback
            score(list(s), "XI-STD" if std else "XI-NSTD", ("xi", i))
        res["early_nstd"] = dict(states=early)
    print(tag, "N", N, "M", len(O), json.dumps(res, separators=(",", ":")), flush=True)
    for f in first: print("VIOLATION", tag, f, flush=True)
    return res

def rgen(rng, d, w, D):                                       # = L-RED r221q brute221.rgen (Xi-cyclic allowed)
    N = d * w; lev = [x // w for x in range(N)]; opts = []
    for x in range(N):
        opts.append([[(rng.choice([y for y in range(N) if lev[y] == lev[x] - 1]) if lev[x] else -1), rng.choice(list(range(N)) + [-1]), 0] for _ in range(D)])
    M = N * D; perm = list(range(M)); rng.shuffle(perm); gate = []; i = 0
    for x in range(N):
        gate.append([])
        for o in opts[x]: o[2] = i; gate[x].append(perm[i]); i += 1
    br = list(range(M)); rng.shuffle(br)
    return {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": [rng.randrange(2) for _ in range(M)], "start": [rng.randrange(D) for _ in range(N)]}

if __name__ == "__main__":
    tot = {}; outdir = os.environ.get("OUT", "out")
    def add(r):
        for k, v in r.items():
            if isinstance(v, dict):
                d = tot.setdefault(k, {})
                for a, b in v.items(): d[a] = d.get(a, 0) + b
    if sys.argv[1] == "rand":
        rng = random.Random(int(sys.argv[2]))
        for i in range(int(sys.argv[3])):
            d = rng.randint(1, 4); w = rng.randint(1, 3); G = rgen(rng, d, w, rng.choice([2, 3]))
            r = census(G, f"rand{sys.argv[2]}_{i}"); add(r)
            if r["FRAME-X"]["viol"] + r["HOWARD"]["viol"] + r["XI-STD"]["viol"] + r["brute"]["diff"] + r.get("early_nstd", {}).get("states", 0):
                os.makedirs(outdir, exist_ok=True); json.dump(G, open(os.path.join(outdir, f"b3_{sys.argv[2]}_{i}.json"), "w"))
    else:
        for f in sys.argv[1:]:
            G = json.load(open(f))
            if not (isinstance(G, dict) and "opts" in G): continue
            add(census(G, os.path.basename(f)))
    print("TOTAL", json.dumps(tot, separators=(",", ":")), flush=True)
