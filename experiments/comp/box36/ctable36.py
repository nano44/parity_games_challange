#!/usr/bin/env python3
"""L-COMP box 36 item 3: exact C census over ALL genomes of (N, M) from an ALLK=1 sweep checkpoint (every block, k = 0 included).
C = own34's counter (max over (v, interval of constant Lambda_t(v), y) of #changes of E_t(v) with top y), engine fast36 (bin/next,
validated vs own34 on 1,075 genomes, cval36.log). Prints: genomes (must equal the full space), blocks done / all, maxC, #genomes with
C >= 2, C histogram, argmax genome (frozen to out/argmax/ARG_C_N<N>M<M>.json, re-run in own34). Usage: ctable36.py CKFILE [...]"""
import sys, os, json, hashlib
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "box34")]
import gen36, own34
for ck in sys.argv[1:]:
    base = os.path.basename(ck).split(".")[0]; N, M = int(base[1:base.index("M")]), int(base[base.index("M") + 1:])
    tot = 0; nC2 = 0; maxC = -1; arg = None; hist = {}; nb = 0
    for line in open(ck):
        d = json.loads(line); s = d["st"]; nb += 1; tot += s["genomes"]; nC2 += s["nC2"]
        for c, v in s["Chist"].items(): hist[c] = hist.get(c, 0) + v
        if s["maxC"] > maxC: maxC = s["maxC"]; arg = (d["lev"], d["D"], d["xts"], s["C_arg"]["inner"])
    full = sum(gen36.blocksize(D, M) for _, D, _ in gen36.blocks(N, M)); allb = sum(1 for _ in gen36.blocks(N, M))
    lev, D, xts, (gate, br, bp, st) = arg; G = gen36.make(N, lev, D, xts, gate, br, bp, st)
    f = os.path.join(H, "out", "argmax", f"ARG_C_N{N}M{M}.json"); json.dump(G, open(f, "w")); m = own34.measure(G, True, True)
    print(json.dumps(dict(N=N, M=M, NM=N + M, genomes=tot, full_space=full, blocks=f"{nb}/{allb}", complete=(nb == allb and tot == full),
                          maxC=maxC, nC2=nC2, Chist=dict(sorted(hist.items(), key=lambda kv: int(kv[0]))), argmax=os.path.basename(f),
                          sha1=hashlib.sha1(open(f, "rb").read()).hexdigest()[:8], own34_C=m["C"], own34_T3=m["T3"])), flush=True)
