#!/usr/bin/env python3
"""L-COMP box 35 (2) (Lead 02:14Z): EXACT checks for «a genome with C >= 2 below N + M 33», engine own34 ([E-LEV], N5'-xi from S3 on Gamma3
up to the first fallback; C = max over (v, I, y) of #changes of E_t(v) in I with top y).
Mode enum N M: ALL genomes of (N, M) in the eg195 schema (as box33/enum33.py: levels = every nondecreasing reachable level vector from 0,
every split with >= 1 option per mover, wt = the FIRST mover of level lev - 1 (enum33's convention; with one mover per level it is the
only choice), xt in {-1} + movers, gate and br permutations, bp bits, start): prints #genomes, max C, hist of C, argmax.
Mode nbr G.json K: every genome reachable from G by <= K DELETIONS (shrink34's moves: one option of a mover with >= 2 options; one mover y,
with W-targets pointing to y re-pointed to EACH other mover of y's level in turn (all choices enumerated), Xi-targets to y -> X), distinct
results by sha1; prints #distinct genomes per depth, how many have C >= 2 and the smallest N + M among them.
Usage: exact35.py enum N M OUT | exact35.py nbr G.json K OUT"""
import sys, os, json, itertools, hashlib, time
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
import own34, shrink34_moves as SM

def C_of(G):
    m = own34.measure(G, True, extra=True); return m["C"], m

def enum(N, M):
    def levvecs():
        out = []
        def rec(v):
            if len(v) == N: out.append(tuple(v)); return
            for l in (v[-1], v[-1] + 1): rec(v + [l])
        rec([0]); return out
    for lev in levvecs():
        for D in itertools.product(range(1, M + 1), repeat=N):
            if sum(D) != M: continue
            for xts in itertools.product(range(-1, N), repeat=M):
                for gate in itertools.permutations(range(M)):
                    for br in itertools.permutations(range(M)):
                        for bp in itertools.product((0, 1), repeat=M):
                            for st in itertools.product(*[range(d) for d in D]):
                                opts = []; g = []; b = 0
                                for x in range(N):
                                    oo = []; gg = []
                                    for _ in range(D[x]):
                                        wt = -1 if lev[x] == 0 else [y for y in range(N) if lev[y] == lev[x] - 1][0]
                                        oo.append([wt, xts[b], b]); gg.append(gate[b]); b += 1
                                    opts.append(oo); g.append(gg)
                                yield {"N": N, "lev": list(lev), "opts": opts, "gate": g, "br": list(br), "bp": list(bp), "start": list(st)}

def sha(G): return hashlib.sha1(json.dumps(G, sort_keys=True).encode()).hexdigest()
mode = sys.argv[1]
if mode == "enum":
    N, M, OUT = int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; t0 = time.time()
    n = 0; hist = {}; best = (-1, None); err = 0
    for G in enum(N, M):
        try: c, m = C_of(G)
        except Exception: err += 1; continue
        n += 1; hist[c] = hist.get(c, 0) + 1
        if c > best[0]: best = (c, G)
    open(OUT, "w").write(f"ENUM N {N} M {M} genomes {n} err {err} maxC {best[0]} hist {dict(sorted(hist.items()))} {time.time() - t0:.0f}s\nARGMAX {json.dumps(best[1], sort_keys=True)}\n")
else:
    G0 = json.load(open(sys.argv[2])); K = int(sys.argv[3]); OUT = sys.argv[4]; t0 = time.time()
    seen = {sha(G0)}; frontier = [G0]; f = open(OUT, "w")
    c0, m0 = C_of(G0); f.write(f"# nbr {sys.argv[2]} N+M {SM.size(G0)} C {c0} K {K}\n")
    hits_total = 0
    for depth in range(1, K + 1):
        nxt = []; hits = 0; minhit = None
        for G in frontier:
            for H2 in SM.all_deletions(G):
                h = sha(H2)
                if h in seen: continue
                seen.add(h); nxt.append(H2)
                c, m = C_of(H2)
                if c >= 2:
                    hits += 1; s = SM.size(H2)
                    if minhit is None or s < minhit[0]: minhit = (s, H2)
        hits_total += hits
        f.write(f"depth {depth} distinct {len(nxt)} with C>=2 {hits} smallest N+M with C>=2 {minhit[0] if minhit else None} {time.time() - t0:.0f}s\n"); f.flush()
        if minhit: f.write(f"HIT {json.dumps(minhit[1], sort_keys=True)}\n")
        frontier = nxt
    f.write(f"SUMMARY nbr K {K} total distinct {len(seen) - 1} with C>=2 {hits_total}\n")
