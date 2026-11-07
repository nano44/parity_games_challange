#!/usr/bin/env python3
"""L-RED 54 R217: climb IDEAL-CYC genomes (box191 idealcyc, mutation = box191 climb191.mut imported unmodified) scoring
S = max number of RE-ADOPTIONS of one mover (switches to an option it held before; a re-firing fuse needs them), ties by R (subrun191
labels), then T. Time-bounded (SECS) and resumable from OUT.json. Usage: swclimb.py seed OUT [seedjson]"""
import sys, os, json, time
WT3 = os.environ["WT3"]; B = os.path.join(WT3, "experiments/new/box191"); sys.path[:0] = [B]
seed, out = int(sys.argv[1]), sys.argv[2]; seedf = sys.argv[3] if len(sys.argv) > 3 else None
sys.argv = ["climb191.py", "R", "2", "4", "2", str(seed), "0", "/nonexistent/x"]
import idealcyc, subrun191
src = open(os.path.join(B, "climb191.py")).read(); ns = {"__file__": os.path.join(B, "climb191.py"), "__name__": "lib"}
exec(compile(src.split("cur = json.load")[0], "climb191", "exec"), ns); mut = ns["mut"]; rng = ns["rng"]; rng.seed(seed)
SECS = int(os.environ.get("SECS", "1200")); t0 = time.time()
def score(G):
    st = idealcyc.run(G, cap=3000); N = G["N"]
    sw = 0
    for x in range(N):
        seen = {st[0][x]}; r = 0
        for t in range(1, len(st)):
            if st[t][x] != st[t - 1][x]:
                r += st[t][x] in seen; seen.add(st[t][x])
        sw = max(sw, r)
    lab = subrun191.labels(G); return (sw, lab.count("R"), len(st) - 1)
cur = json.load(open(out + ".json")) if os.path.exists(out + ".json") else json.load(open(seedf))
cs = score(cur); print(f"start S/R/T {cs} N {cur['N']}", flush=True); it = 0
while time.time() - t0 < SECS:
    it += 1; c = mut(cur)
    try: s = score(c)
    except Exception: continue
    if s >= cs:
        if s > cs: json.dump(c, open(out + ".json", "w")); print(f"it {it} S/R/T {s} N {c['N']}", flush=True)
        cur, cs = c, s
print(f"SLICE end it {it} best {cs}", flush=True)
