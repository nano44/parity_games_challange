"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5), queue item (2): potentials of the tangle set alone, monotone in T
(attractors are monotone in T for fixed inputs, DTL-proof §3(a2)) with polynomial range. For the tangle set T_s stored before
search s of a phase (player p, unsolved set G'):
  PSI1 = sum over v in G', thresholds t in priorities: |p-tangle-attractor of {v} in G' at threshold t|  (range <= n^2 (d+1))
  PSI2 = sum over v in G': |p-tangle-attractor of {v} in G' at threshold pr(v)|                       (the "region of v as a top")
  PSI3 = sum over t: |p-tangle-attractor of G'_{>t} ... restricted to p-parity tops above t| (attractor of the p-vertices of
         priority > t, threshold t)
Each must STRICTLY grow from T_s to T_{s+1} for every non-last search s (the phase continues only if new tangles change some
attractor of the next search). Reports failures. DTL_ORDER=oink | stable. Usage: dtl_psi.py G.pg ... (PSI_V=1 verbose)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_spp as P

def attr(d, p, Z, G, maxpr):
    Z = set(Z); d.Q = sorted(Z); R = set(G) - Z
    d.tattr(p, Z, R, set(G), maxpr, R)
    return len(Z)

def psis(d, p, G, prios):
    s1 = s2 = s3 = 0
    for v in G:
        for t in prios:
            if t >= d.pr[v] or True:
                s1 += attr(d, p, {v}, G, t)
        s2 += attr(d, p, {v}, G, d.pr[v])
    for t in prios:
        H = {v for v in G if d.pr[v] > t and d.pr[v] % 2 == p}
        if H: s3 += attr(d, p, H, G, t)
    return s1, s2, s3

if __name__ == "__main__":
    sys.setrecursionlimit(100000); tot = [0, 0, 0, 0]
    for f in sys.argv[1:]:
        g = pg.read(f); d = P.build(g)
        orig = d.extractTangles; born = {}
        def ext(top, R, d=d, orig=orig, born=born):
            k = len(d.tv); r = orig(top, R)
            for i in range(k, len(d.tv)): born[i] = d.tpr[i]
            return r
        d.extractTangles = ext; d.run()
        ntv = len(d.tv); tpr_final = list(d.tpr); tpr_born = [born[i] for i in range(ntv)]
        rows, cur = [], []
        for t in d.trace:
            if cur and (t["p"] != cur[-1]["p"] or t["dom"] != cur[-1]["dom"]): rows.append(cur); cur = []
            cur.append(t)
        if cur: rows.append(cur)
        G_final = set(d.G); saveG = d.G
        for ph in rows:
            if len(ph) < 2: continue
            p, G = ph[0]["p"], set(ph[0]["G"]); prios = sorted({d.pr[v] for v in G}); vals = []
            for tr in ph:
                k = tr["t0"]
                # tangles of the phase player alive at the phase start and created before search: indices < k; disable the rest
                # alive during the phase: created before this search and not containing a vertex solved before the phase
                d.tpr = [tpr_born[i] if i < k and all(v in G for v, _ in d.tv[i]) else -1 for i in range(ntv)]
                d.G = G
                vals.append(psis(d, p, G, prios))
            d.tpr = tpr_final; d.G = saveG
            fails = [[s for s in range(len(ph) - 1) if not vals[s + 1][j] > vals[s][j]] for j in range(3)]
            tot[0] += len(ph) - 1; tot[1] += len(fails[0]); tot[2] += len(fails[1]); tot[3] += len(fails[2])
            if os.environ.get("PSI_V"): print(os.path.relpath(f), f"p={p} S={len(ph)}", "PSI1", [v[0] for v in vals], "fails", fails[0], "| PSI2 fails", fails[1], "| PSI3 fails", fails[2])
    print("transitions", tot[0], "PSI1 non-growth", tot[1], "PSI2", tot[2], "PSI3", tot[3])
