#!/usr/bin/env python3
"""L-COMP box 38 item 2(a): EXHAUSTIVE T3 by U(G) over ALL genomes of (N, M) (box 33/36 space, box36/gen36.py; every k, no filter).
U(G) (u38.py, P-N5-ASC §6 l. 179 / R121 (g)) depends only on (lev, D, xts), so it is constant on a gen36 block. Per block: fast38 block
mode (= validated fast36 engine, + T3 argmax) with [E-LEV] and with FAST36_NOELEV=1. One JSON line per finished block in OUT (resume
skips finished blocks; shard k/K takes blocks i = k mod K). Unit: one genome. Counter: T3 = N5'-xi iterations from S3 on Gamma3 before
the first fallback (TOTAL over the run up to the first fallback, not per gate). Usage: sweep38.py N M k/K OUT"""
import sys, os, json, subprocess, time
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "box36")]
import gen36, u38
N, M = int(sys.argv[1]), int(sys.argv[2]); sk, sK = map(int, sys.argv[3].split("/")); OUT = sys.argv[4]
EXE = os.path.join(H, "bin", "fast38_w1")


def blk(lev, D, xts, noelev):
    env = dict(os.environ); env.pop("FAST36_NOELEV", None)
    if noelev: env["FAST36_NOELEV"] = "1"
    args = [EXE, "block", str(N), str(M)] + [str(a) for a in lev] + [str(a) for a in D] + [str(a) for a in xts]
    d = json.loads(subprocess.run(args, capture_output=True, text=True, check=True, env=env).stdout)
    assert d["capped"] == 0
    return d


done = set()
if os.path.exists(OUT):
    for line in open(OUT):
        try: done.add(json.loads(line)["i"])
        except Exception: pass
t0 = time.time()
for i, (lev, D, xts) in enumerate(gen36.blocks(N, M)):
    if i % sK != sk or i in done: continue
    G = gen36.make(N, lev, D, xts, list(range(M)), list(range(M)), [0] * M, [0] * N); U = u38.U(G)
    e, ne = blk(lev, D, xts, False), blk(lev, D, xts, True)
    rec = dict(i=i, lev=list(lev), D=list(D), xts=list(xts), U=U, genomes=e["genomes"], T3e=e["maxT3"], arge=e["T3_arg"]["inner"],
               T3n=ne["maxT3"], argn=ne["T3_arg"]["inner"])
    with open(OUT, "a") as f: f.write(json.dumps(rec) + "\n")
with open(OUT + ".log", "a") as f: f.write(f"DONE shard {sk}/{sK} N {N} M {M} {time.time() - t0:.0f}s\n")
