#!/usr/bin/env python3
"""L-COMP box 36: table of the exhaustive sweeps (out/sweep/N<N>M<M>.json, all shards merged from the .ck files) and freezing of the
argmax genomes (ratio argmax and kfx argmax per (N, M, k)) to out/argmax/ with SHA1SUMS. Every argmax genome is re-run with own36
(Python, own34 engine) and the C engine; the table line carries both results (they must agree).
Usage: table36.py out/sweep/N1M4.json.ck [...]"""
import sys, os, json, hashlib, collections
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
import gen36, own36, fast36


def combine(S, k, b):   # = sweep36.combine (sweep36 parses argv at import)
    s = S.setdefault(str(k), dict(genomes=0, maxratio=-1, ratio_arg=None, maxkfx=None, kfx_arg=None, maxflip=0, maxT3=0, c2fail=0, hist={}))
    s["genomes"] += b["genomes"]; s["c2fail"] += b["c2fail"]; s["maxflip"] = max(s["maxflip"], b["maxflip"]); s["maxT3"] = max(s["maxT3"], b["maxT3"])
    if b["maxratio"] > s["maxratio"]: s["maxratio"], s["ratio_arg"] = b["maxratio"], b["ratio_arg"]
    if b["maxkfx"] is not None and (s["maxkfx"] is None or b["maxkfx"] > s["maxkfx"]): s["maxkfx"], s["kfx_arg"] = b["maxkfx"], b["kfx_arg"]
    for h, c in b["hist"].items(): s["hist"][h] = s["hist"].get(h, 0) + c

os.makedirs(os.path.join(H, "out", "argmax"), exist_ok=True)
rows = []
for ck in sys.argv[1:]:
    base = os.path.basename(ck).split(".")[0].rstrip("c"); N, M = int(base[1:base.index("M")]), int(base[base.index("M") + 1:])
    S = {}; k0 = 0; blocks = 0
    for line in open(ck):
        d = json.loads(line); blocks += 1
        if d["k"] == 0: k0 += d["n"]; continue
        combine(S, d["k"], d["st"])
    total = sum(gen36.blocksize(D, M) for _, D, _ in gen36.blocks(N, M)); nbl = sum(1 for _ in gen36.blocks(N, M))
    for k, s in sorted(S.items()):
        out = dict(N=N, M=M, NM=N + M, k=int(k), genomes=s["genomes"], complete=blocks == nbl, k0=k0, total=total,
                   maxratio=s["maxratio"], maxkfx=s["maxkfx"], maxflip=s["maxflip"], maxT3=s["maxT3"], c2fail=s["c2fail"])
        for tag, a in (("ratio", s["ratio_arg"]), ("kfx", s["kfx_arg"])):
            gate, br, bp, st = a["inner"]; G = gen36.make(N, a["lev"], a["D"], a["xts"], gate, br, bp, st)
            f = os.path.join(H, "out", "argmax", f"ARG_{tag}_N{N}M{M}_k{k}.json"); json.dump(G, open(f, "w"))
            o, r2 = own36.census(G, True, False); T, fb, rc = fast36.one(G)
            gq = tuple(a["gate"]); py = [z for z in r2 if tuple(z[0]) == gq][0]; cc = [z for z in rc if z[0] == gq][0]
            out[tag] = dict(file=os.path.basename(f), sha1=hashlib.sha1(open(f, "rb").read()).hexdigest()[:8], gate=a["gate"],
                            flips=a["flips"], lamch=a["lamch"], T3=a["T3"], own36=[o["T3"], py[1], py[2]], c=[T, cc[1], cc[2]],
                            agree=(o["T3"], py[1], py[2]) == (T, cc[1], cc[2]) == (a["T3"], a["flips"], a["lamch"]))
        out["hist"] = dict(sorted(s["hist"].items(), key=lambda kv: tuple(map(int, kv[0].split(",")))))
        rows.append(out); print(json.dumps(out), flush=True)
with open(os.path.join(H, "out", "argmax", "SHA1SUMS"), "w") as f:
    for fn in sorted(os.listdir(os.path.join(H, "out", "argmax"))):
        if fn.endswith(".json"): f.write(hashlib.sha1(open(os.path.join(H, "out", "argmax", fn), "rb").read()).hexdigest() + "  " + fn + "\n")
