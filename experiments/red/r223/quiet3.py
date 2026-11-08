#!/usr/bin/env python3
"""L-RED 58 R223 item 7 pre-check: P-N5-QUIET's Theorem QUIET / Corollary T-QUIET measured DIRECTLY on the Gamma3 Howard run of N5'-xi
(frozen box190 n5v.step mode xi from S3 on own3.build3's Gamma3(G); env WT = WT3 = worktree of l-new 131b4c1c), up to its first
fallback (T3 = number of pre-fallback iterations). Values by L-RED's own.py on Gamma3. class_t(v) := (Lambda_t(v), E_t(v)) over ALL
vertices of Gamma3 (E = e-vertices of Pi); a step is LOUD if some vertex changes class; Q3 := loud steps among the T3 steps.
L3 := (M+1)(2M+1)(N+1) + N(n3 - 1), n3 = N + 7M + 10. Counters (unit: genome): wov = some quiet window longer than L3;
tq = T3 > Q3 + (Q3 + 1)·L3. Recorded: max quiet window W3, max T3, max Q3.
Usage: quiet3.py files OUT G.json ... | quiet3.py exh OUT | quiet3.py rand SEED COUNT NMIN NMAX OUT | quiet3.py elev SEED COUNT NMIN NMAX UMAX OUT"""
import sys, os, json, random
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
import reach223
from reach223 import own, own3, n5v, n5x, pg
def check(G, cap=5000):
    prio, owner, succ, sig0, tau0, V = own3.build3(G); n = len(prio); N = G["N"]; M = sum(len(o) for o in G["opts"])
    gp = pg.parse(f"parity {n - 1};\n" + "".join(f"{v} {prio[v]} {owner[v]} {','.join(map(str, succ[v]))};\n" for v in range(n)))
    E, Ed = n5v.Engine(gp), n5v.Engine(n5v.dual(gp)); sigma, tau = n5x.start_pair(gp, E, Ed, None)
    vj = own.VJ(prio); evs = {V[("e", (x, k))] for x in range(N) for k in range(len(G["opts"][x]))}
    cls = lambda val: (val[0], frozenset(u for u in val[1] if u in evs))
    prev = None; T3 = 0; Q3 = 0; w = 0; W3 = 0
    while T3 < cap:
        sg = [sigma[v] if owner[v] == 0 else None for v in range(n)]; t0 = {v: tau[v] for v in range(n) if owner[v] == 1}
        vals, _ = own.evaluate(n, owner, succ, vj, sg, t0); cur = [cls(vals[v]) for v in range(n)]
        if prev is not None:
            if cur != prev: Q3 += 1; w = 0
            else: w += 1; W3 = max(W3, w)
        prev = cur
        rr = n5v.step(gp, E, Ed, sigma, tau, "xi")
        if rr is None or rr[4]: break
        sigma, tau = list(rr[0]), list(rr[1]); T3 += 1
    L3 = (M + 1) * (2 * M + 1) * (N + 1) + N * (N + 7 * M + 10 - 1)
    return dict(T3=T3, Q3=Q3, W3=W3, L3=L3, wov=int(W3 > L3), tq=int(T3 > Q3 + (Q3 + 1) * L3))
def uplinks(G): return sum(1 for x in range(G["N"]) for o in G["opts"][x] if o[1] >= 0 and G["lev"][o[1]] > G["lev"][x])
def elev(rng, N, umax):
    while True:
        G = reach223.rgen_cyc(rng, N)
        for x in range(N):
            for o in G["opts"][x]:
                if o[1] >= 0 and G["lev"][o[1]] > G["lev"][x] and rng.random() < 0.8: o[1] = rng.choice([y for y in range(N) if G["lev"][y] <= G["lev"][x]])
        if uplinks(G) <= umax and reach223.cyclic(G): return G
def summarize(tag, it, out):
    agg = dict(n=0, wov=0, tq=0, W3=0, T3=0, Q3=0, U=0); fo = open(out, "a")
    for name, G in it:
        r = check(G); agg["n"] += 1; agg["wov"] += r["wov"]; agg["tq"] += r["tq"]; agg["U"] = max(agg["U"], uplinks(G))
        for k in ("W3", "T3", "Q3"): agg[k] = max(agg[k], r[k])
        if r["wov"] or r["tq"]: fo.write(f"BAD {name} {r} {json.dumps(G)}\n"); fo.flush()
    line = f"QUIET3 {tag} genomes {agg['n']} wov {agg['wov']} tq {agg['tq']} maxW3 {agg['W3']} maxT3 {agg['T3']} maxQ3 {agg['Q3']} maxU {agg['U']}"
    fo.write(line + "\n"); print(line, flush=True)
if __name__ == "__main__":
    a = sys.argv[1]
    if a == "exh":
        import exh223
        summarize("exhaustive-N<=2-cyclic", ((f"exh{i}", G) for i, G in enumerate(exh223.mk(*t) for t in exh223.genomes()) if reach223.cyclic(G)), sys.argv[2])
    elif a == "rand":
        s, c, n0, n1, out = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]; rng = random.Random(s)
        summarize(f"rand-cyclic-N{n0}-{n1}-seed{s}", ((f"r{s}_{i}", reach223.rgen_cyc(rng, rng.randint(n0, n1))) for i in range(c)), out)
    elif a == "files":
        summarize("files:" + ",".join(os.path.basename(f) for f in sys.argv[3:])[:60], ((os.path.basename(f), json.load(open(f))) for f in sys.argv[3:]), sys.argv[2])
    elif a == "elev":
        s, c, n0, n1, um, out = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), sys.argv[7]; rng = random.Random(s)
        summarize(f"elev-U<={um}-N{n0}-{n1}-seed{s}", ((f"e{s}_{i}", elev(rng, rng.randint(n0, n1), um)) for i in range(c)), out)
