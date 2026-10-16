#!/usr/bin/env python3
"""L-RED successor 3 (Opus 5.5), 2026-10-16: nested deficit blocks on A_DTL (queue item 2: K_parent x K_child, third level).
Per phase (same player, no dominion between), the sequence of changes between consecutive searches at their first-difference
depth-0 index j, tagged DEF (same context and same ideal C6 result at j, actual differs; L-ALG dtl_deficit.py, read-only
via LALG_DIR) or not. A level-i BLOCK = a DEF at index i plus the following changes at indices > i up to the next change
at an index <= i. Inside a level-i block, level-(i+1) blocks are formed the same way.
  T2(i) = sum over level-i blocks of the DEF changes at indices > i inside them (the h4prod block score);
  K2(i) = number of level-i blocks containing >= 1 such DEF; minK(i) = the least child DEF count over those blocks;
  T3(i) = sum over level-i blocks, over level-(i+1) blocks inside, of the DEF changes at indices > i+1 inside them;
  K3(i) = number of level-(i+1) blocks (inside level-i blocks) containing >= 1 such DEF.
Also: for each block, the child context(s) at index i+1 (fresh = not seen in an earlier block of the same phase).
Order from DTL_ORDER (stable | oink). Usage: DTL_ORDER=oink LALG_DIR=.. nest.py G.pg ..."""
import sys, os

def _dd():
    ld = os.environ["LALG_DIR"]
    for q in (os.path.join(ld, "experiments", "alg"), os.path.join(ld, "experiments", "harness")):
        if q not in sys.path: sys.path.insert(0, q)
    import dtl_deficit as DD
    return DD

def phases(path):
    DD = _dd(); g = DD.pg.read(path); d = DD.build(g); d.run()
    out, seq = [], []
    for k, (a, b) in enumerate(zip(d.trace, d.trace[1:])):
        if a["p"] != b["p"] or b["dom"] != a["dom"]:
            if seq: out.append(seq)
            seq = []; continue
        pa, pb = a["pieces"], b["pieces"]; j = 0
        while j < min(len(pa), len(pb)) and pa[j][:3] == pb[j][:3]: j += 1
        if j >= min(len(pa), len(pb)): continue
        de = pa[j][0] == pb[j][0] and pa[j][3:] == pb[j][3:]
        seq.append(dict(s=k + 1, j=j, de=de, ctx=pa[j][0], p=a["p"]))
    if seq: out.append(seq)
    return out, d

def blocks(seq, i):
    """level-i blocks: list of sub-sequences following each DEF at index i"""
    res, k = [], 0
    while k < len(seq):
        if seq[k]["j"] == i and seq[k]["de"]:
            k += 1; sub = []
            while k < len(seq) and seq[k]["j"] > i:
                sub.append(seq[k]); k += 1
            res.append(sub)
        else: k += 1
    return res

def measure(path):
    ph, d = phases(path); best = dict(T2=0, K2=0, minK=0, T3=0, K3=0, i2=None, i3=None, maxdef=0, fresh=0)
    for seq in ph:
        best["maxdef"] = max(best["maxdef"], sum(c["de"] for c in seq))
        for i in sorted({c["j"] for c in seq if c["de"]}):
            bl = blocks(seq, i)
            ch = [sum(c["de"] for c in b) for b in bl]
            nz = [c for c in ch if c]
            if len(nz) >= 2 and sum(nz) > best["T2"]:
                best.update(T2=sum(nz), K2=len(nz), minK=min(nz), i2=i)
                seen, fr = set(), 0
                for b in bl:
                    cs = {c["ctx"] for c in b if c["j"] == i + 1}
                    fr += bool(cs - seen); seen |= cs
                best["fresh"] = fr
            t3 = k3 = 0
            for b in bl:
                for sb in blocks(b, i + 1):
                    gd = sum(c["de"] for c in sb if c["j"] > i + 1)
                    t3 += gd; k3 += bool(gd)
            if k3 >= 2 and t3 > best["T3"]: best.update(T3=t3, K3=k3, i3=i)
    return best, d, ph

def score(path):
    b, d, _ = measure(path)
    return 10000 * b["T3"] + 1000 * b["K3"] + 100 * b["T2"] + 10 * b["minK"] + b["maxdef"] + len(d.trace) / 1000.0

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    for f in sys.argv[1:]:
        b, d, ph = measure(f)
        print(f"== {os.path.basename(f)} order={os.environ.get('DTL_ORDER', 'stable')} n={d.n} searches={len(d.trace)} {b}")
        if "-v" in os.environ.get("NEST_V", ""):
            for seq in ph: print("   phase:", " ".join(f"s{c['s']}:{c['j']}{'D' if c['de'] else 'x'}|{len(c['ctx'])}" for c in seq))
