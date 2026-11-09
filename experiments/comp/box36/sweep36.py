#!/usr/bin/env python3
"""L-COMP box 36 item 2(c): EXHAUSTIVE per-gate flip census over ALL genomes of (N, M) (gen36 space = box 33's) with Xi-feedback
number k >= 1 (k = 0 blocks counted, not run). Engine: own36.census (own34 run, Python) or ENGINE=c (fast36 C engine, validated).
Per k (unit: genome; scope: N5'-xi from S3 on Gamma3 up to the first fallback, [E-LEV]):
  genomes, maxratio = max over genomes and gates of flips(g) / (lamch(g) + 1) (+ argmax genome, gate, flips, lamch),
  maxkfx = max of flips(g) - 2(lamch(g) + 1) (K1-FLIP(2) margin; > 0 = violation; + argmax), maxflip, maxT3, c2fail = #genomes with
  some gate violating K1-FLIP(2), hist of (flips, lamch) at the ratio-argmax gate of each genome.
Checkpoint: one JSON line per finished (lev, D, xts) block in OUT.ck; a restart skips finished blocks. SHARD k/K takes blocks i = k mod K.
Usage: [ENGINE=c] [ALLK=1 FAST36_BINDIR=bin/next] sweep36.py N M k/K OUT"""
import sys, os, json, time, collections
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
import gen36
N, M = int(sys.argv[1]), int(sys.argv[2]); sk, sK = map(int, sys.argv[3].split("/")); OUT = sys.argv[4]
ENGINE = os.environ.get("ENGINE", "py")
ALLK = os.environ.get("ALLK") == "1"     # item 3: run k = 0 blocks too (C counter needs every genome); needs ENGINE=c, FAST36_BINDIR=bin/next
if ENGINE == "py":
    import own36
    def run_block(lev, D, xts):
        res = []
        for gate, br, bp, st in gen36.inner(D, M):
            G = gen36.make(N, lev, D, xts, gate, br, bp, st); o, rows = own36.census(G, True, False)
            if rows:
                am = max(rows, key=lambda z: (z[1] / (z[2] + 1), z[1])); ak = max(rows, key=lambda z: z[1] - 2 * (z[2] + 1))
                res.append((o["T3"], am[1], am[2], list(am[0]), ak[1], ak[2], list(ak[0]), max(z[1] for z in rows), (gate, br, bp, st)))
        return res
else:
    import fast36
    def run_block(lev, D, xts):
        return fast36.run_block(N, lev, D, xts, M)


def new_stats():
    return dict(genomes=0, maxratio=-1, ratio_arg=None, maxkfx=None, kfx_arg=None, maxflip=0, maxT3=0, c2fail=0, hist={})


def merge(S, k, res, lev, D, xts):
    s = S.setdefault(str(k), new_stats())
    for T3, af, al, ag, kf, kl, kg, mf, inn in res:
        s["genomes"] += 1; r = af / (al + 1); kfx = kf - 2 * (kl + 1)
        if r > s["maxratio"]:
            s["maxratio"] = r; s["ratio_arg"] = dict(lev=lev, D=D, xts=xts, inner=inn, gate=ag, flips=af, lamch=al, T3=T3)
        if s["maxkfx"] is None or kfx > s["maxkfx"]:
            s["maxkfx"] = kfx; s["kfx_arg"] = dict(lev=lev, D=D, xts=xts, inner=inn, gate=kg, flips=kf, lamch=kl, T3=T3)
        s["maxflip"] = max(s["maxflip"], mf); s["maxT3"] = max(s["maxT3"], T3); s["c2fail"] += kfx > 0
        h = f"{af},{al}"; s["hist"][h] = s["hist"].get(h, 0) + 1


def combine(S, k, b):
    s = S.setdefault(str(k), new_stats())
    s["genomes"] += b["genomes"]; s["c2fail"] += b["c2fail"]; s["maxflip"] = max(s["maxflip"], b["maxflip"]); s["maxT3"] = max(s["maxT3"], b["maxT3"])
    if b["maxratio"] > s["maxratio"]: s["maxratio"], s["ratio_arg"] = b["maxratio"], b["ratio_arg"]
    if b["maxkfx"] is not None and (s["maxkfx"] is None or b["maxkfx"] > s["maxkfx"]): s["maxkfx"], s["kfx_arg"] = b["maxkfx"], b["kfx_arg"]
    for h, c in b["hist"].items(): s["hist"][h] = s["hist"].get(h, 0) + c


if __name__ == "__main__":
    ck = OUT + ".ck"; done = {}
    if os.path.exists(ck):
        for line in open(ck):
            d = json.loads(line); done[d["i"]] = d
    f = open(ck, "a"); t0 = time.time(); S = {}; k0 = 0
    for i, (lev, D, xts) in enumerate(gen36.blocks(N, M)):
        if i % sK != sk: continue
        if i in done: d = done[i]
        else:
            k = gen36.xi_k(N, D, xts)
            if k == 0 and not ALLK: d = dict(i=i, k=0, n=gen36.blocksize(D, M))
            else:
                if ENGINE == "py": B = {}; merge(B, k, run_block(lev, D, xts), list(lev), list(D), list(xts)); stt = B.get(str(k), new_stats())
                else: stt = run_block(lev, D, xts)
                d = dict(i=i, k=k, n=gen36.blocksize(D, M), st=stt)
            d.update(lev=list(lev), D=list(D), xts=list(xts)); f.write(json.dumps(d) + "\n"); f.flush()
            print(f"block {i} k {d['k']} n {d['n']} {time.time() - t0:.0f}s", flush=True)
        if d["k"] == 0 and "st" not in d: k0 += d["n"]; continue
        combine(S, d["k"], d["st"])
    summ = dict(N=N, M=M, shard=f"{sk}/{sK}", engine=ENGINE, k0_genomes_not_run=k0, per_k=S)
    json.dump(summ, open(OUT, "w"), indent=1)
    for k, s in sorted(S.items()):
        print("SUMMARY N", N, "M", M, "k", k, "genomes", s["genomes"], "maxratio", s["maxratio"], "maxkfx", s["maxkfx"], "maxflip",
              s["maxflip"], "maxT3", s["maxT3"], "c2fail", s["c2fail"], "ratio_arg", json.dumps(s["ratio_arg"]), flush=True)
