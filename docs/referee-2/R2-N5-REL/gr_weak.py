#!/usr/bin/env python3
"""REFEREE-2 succ. 19 (§C of REL, REFEREE's REL-N1): GATE-RISE with (i) weakened. Kinds among sigmabar(u) changes at in-phase S4a transitions
with (ii), (iii) holding: W1 = u on its honest cycle at t+1 only, u != lambda(u); W0 = on its cycle at t only, u != lambda(u); WB = both, u != lambda.
Reports whether Xi(u) strictly rises. Usage: gr_weak.py pairs list prefix | files list runs"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import rel_check as RC
R = RC.R
st = R.Stats(); a = sys.argv[1:]; rng = random.Random(2626)
def run(gp, s, t, name):
    states, fbs = R.DC.Runner(gp).run(s, t); ctx = R.Ctx(gp); g, n = gp, gp.n; K = ctx.key
    I = [R.state_info(ctx, x, y, st, name) for x, y in states]
    for k in range(len(I) - 1):
        if fbs[k] or I[k]["lamX"] != I[k + 1]["lamX"] or I[k]["tu"] != I[k + 1]["tu"]: continue
        s0, s1 = I[k], I[k + 1]; lam = s0["lamX"]
        for u in range(n):
            if g.owner[u] != 1: continue
            y1, y2 = s0["hn"][u], s1["hn"][u]
            if y1 == y2: continue
            c0, c1 = RC.oncyc(s0["hn"], u), RC.oncyc(s1["hn"], u)
            if not (c0 or c1) or lam[u] == u: continue
            if u in R.lasso(s0["hn"], y2)[0] and not c0: continue   # (ii) fails (y2's t-play through u)
            if K(s0["xi"][y1]) == K(s0["xi"][y2]): continue          # (iii) fails
            kind = "WB" if (c0 and c1) else ("W1" if c1 else "W0")
            st.inc(kind)
            if not K(s1["xi"][u]) > K(s0["xi"][u]): st.inc(kind + "_norise"); print("NORISE", kind, name, k, u, flush=True)
if a[0] == "pairs":
    for line in [l.split() for l in open(a[1]) if l.strip()]:
        gp = R.pg.read(os.path.join(a[2], line[0]))
        if len(line) > 1:
            s, t = R.read_start(gp, os.path.join(a[2], line[1]))
            for v in range(gp.n):
                x = s if gp.owner[v] == 0 else t
                if x[v] not in gp.succ[v]: x[v] = gp.succ[v][0]
        else: s, t = R.starts(gp, 0, None)
        run(gp, s, t, line[0])
else:
    for path in [l.strip() for l in open(a[1]) if l.strip()]:
        gp = R.pg.read(os.path.join(R.DC.ROOT, path))
        for r in range(int(a[2])):
            s, t = R.starts(gp, r, rng); run(gp, s, t, f"{path}#{r}")
for k in sorted(st.c):
    if not k.startswith("ENGXI"): print(f"{k}: {st.c[k]}")
