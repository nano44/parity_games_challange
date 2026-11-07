#!/usr/bin/env python3
"""L-RED 53, R215 (2) (Lead 05:51Z / 06:22Z): climb IDEAL-CYC(G) (box191 idealcyc.py = Howard at the movers of Gamma(G); Xi-cycles
allowed; claude/l-new f09f67ec, env WT3) scoring R = number of steps labelled R by box191 subrun191.labels (no VJ cycle node changes,
Odd's optimal counterstrategy changes), ties by T. Mutation = box191 climb191.mut (imported unmodified). Time-bounded (SECS, default
1200) and resumable: restarts from OUT.json if present. Every new best is printed with T, R, C, p and the label string length.
SCORE=F scores the max number of face flips at one gate instead (ties by R, then T; the printed «R» column is then F).
Usage: rclimb.py d w D seed OUT [seedjson]"""
import sys, os, json, random, time
WT3 = os.environ["WT3"]; B = os.path.join(WT3, "experiments/new/box191"); sys.path[:0] = [B]
d, w, D, seed, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
seedf = sys.argv[6] if len(sys.argv) > 6 else None
sys.argv = ["climb191.py", "R", str(d), str(w), str(D), str(seed), "0", "/nonexistent/x"]
import idealcyc, rand191, subrun191
src = open(os.path.join(B, "climb191.py")).read(); ns = {"__file__": os.path.join(B, "climb191.py"), "__name__": "lib"}
exec(compile(src.split("cur = json.load")[0], "climb191", "exec"), ns); mut = ns["mut"]; rng = ns["rng"]; rng.seed(seed)
SECS = int(os.environ.get("SECS", "1200")); t0 = time.time()
SCORE = os.environ.get("SCORE", "R")
import gamma3
def maxflip(G):   # max number of gate-face changes of Odd's optimal counterstrategy (si.Engine) at one gate over the run
    h, s0, movers, inv = idealcyc.build(G); E = idealcyc.Engine(h); st = idealcyc.run(G); _, _, _, V = gamma3.build(G, set())
    Q = [(x, k) for x in range(G["N"]) for k in range(len(G["opts"][x]))]; fl = {q: 0 for q in Q}; prev = None
    for s in st:
        cur = list(s0)
        for x in range(G["N"]): cur[movers[x]] = V[("g", (x, s[x]))]
        _, sb = E.evaluate(tuple(cur)); face = {q: sb[V[("g", q)]] == V[("e", q)] for q in Q}
        if prev:
            for q in Q: fl[q] += face[q] != prev[q]
        prev = face
    return max(fl.values())
def score(G):
    lab = subrun191.labels(G); R, C = lab.count("R"), lab.count("C")
    if SCORE == "F": F = maxflip(G); return (F, R, len(lab)), F, len(lab), C
    return (R, len(lab)), R, len(lab), C
if os.path.exists(out + ".json"): cur = json.load(open(out + ".json"))
elif seedf and os.path.exists(seedf): cur = json.load(open(seedf))
else: cur = rand191.rgen(rng, d, w, D)
cs = score(cur); best = cs[0]; json.dump(cur, open(out + ".json", "w"))
print(f"start N {cur['N']} R {cs[1]} T {cs[2]} C {cs[3]}", flush=True); it = 0
while time.time() - t0 < SECS:
    it += 1; c = mut(cur)
    try: s = score(c)
    except Exception: continue
    if s[0] >= cs[0]:
        cur, cs = c, s
        if s[0] > best:
            best = s[0]; json.dump(cur, open(out + ".json", "w"))
            print(f"it {it} N {cur['N']} R {s[1]} T {s[2]} C {s[3]}", flush=True)
print(f"SLICE end it {it} best R {best[0]} T {best[1]}", flush=True)
