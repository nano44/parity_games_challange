#!/usr/bin/env python3
"""L-RED 58 R223 item 5: adversary vs «ESC3 / W3 hold for EVERY genome» (L-NEW 64 box 196 reading) and RESULTS R118 (k) REACH3-CYC
(«N5'-xi from S3 on Gamma3(G) visits only standard states and makes Howard steps at the movers until its first fallback, at iteration
T3 + 1») on Xi-CYCLIC genomes. Game = own3.build3 (my builder; must equal frozen box189 gamma3.build). Algorithm = frozen box190
n5v.step (mode xi or spec) from S3 (box21 n5x.start_pair; must equal the standard state for the genome start). Every CHECK by own.py.
Per state j BEFORE the first fallback (state F-1 included), counters (unit: states):
  nstd : sigma off the movers != the standard sigma, or tau != tau0 (standard state);
  esc  : (K0, K1) not in I_sigma (ESC3, first half);
  w3   : some vertex's (sigma, tau)-play value differs from W3 (i): mover (cW, {}, 5l+5), its pads (cW, {}, 5l+4) for all options;
  how  : some mover's sigma_(j+1)(x) is not a Xi_sigma-best element of {sigma_j(x)} u I_sigma_j(x) (Howard step), or a non-mover moves;
  fbx  : transition j is a fallback while some mover has an improving edge, or not a fallback while none has (F = T3 + 1).
Per genome: start (S3 != standard), build (own3 != gamma3), nofb, and ties (Howard ties among best options, recorded only).
Usage: reach223.py exh OUT | reach223.py rand SEED COUNT NMIN NMAX OUT | reach223.py G.json ...   (env WT = WT3; MODE=xi default)"""
import sys, os, json, random, functools
here = os.path.dirname(os.path.abspath(__file__)); WT = os.environ["WT"]
sys.path[:0] = [here, os.path.join(here, "../r222"), os.path.join(WT, "experiments/new/box189"), os.path.join(WT, "experiments/new/box190"),
                os.path.join(WT, "experiments/new/box21"), os.path.join(WT, "experiments/harness")]
import own, own3, gamma3, n5v, n5x, pg
MODE = os.environ.get("MODE", "xi")
def cyclic(G):
    N = G["N"]; ed = {x: {o[1] for o in G["opts"][x] if o[1] >= 0} for x in range(N)}; col = [0] * N
    def dfs(x):
        col[x] = 1
        for y in ed[x]:
            if col[y] == 1 or (col[y] == 0 and dfs(y)): return True
        col[x] = 2; return False
    return any(col[x] == 0 and dfs(x) for x in range(N))
def check(G, cap=5000):
    prio, owner, succ, sig0, tau0, V = own3.build3(G); n = len(prio); N = G["N"]
    g, s2, t2, _ = gamma3.build(G, {"K", "pe", "pb", "m"})
    c = dict(build=int(prio != list(g.prio) or succ != [sorted(s) for s in g.succ] or s2 != sig0 or t2 != tau0), start=0, nstd=0, esc=0, w3=0, how=0, fbx=0, nofb=0, ties=0)
    gp = pg.parse(f"parity {n - 1};\n" + "".join(f"{v} {prio[v]} {owner[v]} {','.join(map(str, succ[v]))};\n" for v in range(n)))
    E, Ed = n5v.Engine(gp), n5v.Engine(n5v.dual(gp)); sigma, tau = n5x.start_pair(gp, E, Ed, None)
    if any(sigma[v] != sig0[v] for v in sig0) or any(tau[v] != tau0[v] for v in tau0): c["start"] = 1
    vj = own.VJ(prio); K0, K1 = V[("K", 0)], V[("K", 1)]; cW = V["cW"]
    O = [(x, k) for x in range(N) for k in range(len(G["opts"][x]))]
    T = 0; F = None
    while T < cap:
        sg = [sigma[v] if owner[v] == 0 else None for v in range(n)]; t0 = {v: tau[v] for v in range(n) if owner[v] == 1}
        vals, _ = own.evaluate(n, owner, succ, vj, sg, t0)
        imp = {v: [w for w in succ[v] if w != sigma[v] and vj.cmp(vals[w], vals[sigma[v]]) > 0] for v in range(n) if owner[v] == 0}
        if any(sigma[v] != sig0[v] for v in sig0 if v >= N) or any(tau[v] != tau0[v] for v in tau0): c["nstd"] += 1
        if K1 not in imp[K0]: c["esc"] += 1
        nx = [sigma[v] if owner[v] == 0 else tau[v] for v in range(n)]
        for x in range(N):
            lv = G["lev"][x]
            if own.VJ.val(vj, x, nx) != (cW, frozenset(), 5 * lv + 5) or any(own.VJ.val(vj, m, nx) != (cW, frozenset(), 5 * lv + 4) for m in succ[x]): c["w3"] += 1; break
        rr = n5v.step(gp, E, Ed, sigma, tau, MODE)
        if rr is None: break
        ns, nt, Is, It, fb = rr; T += 1
        moverimp = any(imp[x] for x in range(N))
        if bool(fb) == moverimp: c["fbx"] += 1
        if fb: F = T; break
        for x in range(N):
            R = [sigma[x]] + imp[x]
            best = max(R, key=functools.cmp_to_key(lambda u, w: vj.cmp(vals[u], vals[w])))
            tops = [w for w in R if vj.cmp(vals[w], vals[best]) == 0]
            c["ties"] += len(tops) > 1
            if ns[x] not in tops: c["how"] += 1
        if any(ns[v] != sigma[v] for v in range(N, n) if owner[v] == 0): c["how"] += 1
        sigma, tau = list(ns), list(nt)
    if F is None: c["nofb"] = 1
    return c, F
def summarize(tag, it, out):
    tot = {}; ng = 0; fo = open(out, "a")
    for name, G in it:
        c, F = check(G); ng += 1
        for k, v in c.items(): tot[k] = tot.get(k, 0) + (v > 0)
        bad = {k: v for k, v in c.items() if v and k != "ties"}
        if bad: fo.write(f"BAD {name} F {F} {bad} {json.dumps(G)}\n"); fo.flush()
    line = f"REACH223 {tag} mode {MODE} genomes {ng} " + " ".join(f"{k} {v}" for k, v in sorted(tot.items()))
    fo.write(line + "\n"); print(line, flush=True)
def rgen_cyc(rng, N):
    lev = sorted(rng.choice(range(max(1, N // 2))) for _ in range(N)); lev = [l - lev[0] for l in lev]
    for i in range(1, N): lev[i] = min(lev[i], lev[i - 1] + 1)
    opts = []; M = 0
    for x in range(N):
        oo = []
        for _ in range(rng.randint(1, 3)):
            w = rng.choice([y for y in range(N) if lev[y] == lev[x] - 1]) if lev[x] else -1
            r = rng.random(); xt = x if r < 0.2 else (rng.randrange(N) if r < 0.85 else -1)
            oo.append([w, xt, 0])
        opts.append(oo)
    while True:
        G = {"N": N, "lev": lev, "opts": opts}
        if cyclic(G): break
        x = rng.randrange(N); opts[x][rng.randrange(len(opts[x]))][1] = rng.randrange(N)
    M = sum(len(o) for o in opts); perm = list(range(M)); rng.shuffle(perm); gate = []; i = 0
    for x in range(N):
        gate.append([])
        for o in opts[x]: o[2] = i; gate[x].append(perm[i]); i += 1
    br = list(range(M)); rng.shuffle(br)
    return {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": [rng.randrange(2) for _ in range(M)], "start": [rng.randrange(len(o)) for o in opts]}
if __name__ == "__main__":
    a = sys.argv[1]
    if a == "exh":
        import exh223
        summarize("exhaustive-N<=2-cyclic", ((f"exh{i}", G) for i, G in enumerate(exh223.mk(*t) for t in exh223.genomes()) if cyclic(G)), sys.argv[2])
    elif a == "rand":
        seed, cnt, n0, n1, out = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]; rng = random.Random(seed)
        summarize(f"rand-N{n0}-{n1}-seed{seed}", ((f"r{seed}_{i}", rgen_cyc(rng, rng.randint(n0, n1))) for i in range(cnt)), out)
    else:
        for f in sys.argv[1:]: print(os.path.basename(f), check(json.load(open(f))))
