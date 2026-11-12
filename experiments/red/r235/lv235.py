#!/usr/bin/env python3
"""L-RED 66 R235: FRESH counter for L-NEW 72 box 208 (claude/l-new 8db300fe, docs/new/N5-LEVEL-box208.md): Lemma LEVEL (§3), Lemma
PLATEAU (Addendum A) and Theorem ALL-TCYC, on L-RED's own IDEAL-CYC engine (experiments/red/r221q/own.py; no code from level208 /
plat208 / gfc203 / si.py). Classes: class_t(v) = (Lambda_t(v), E_t(v)), E = the e-vertices of Pi; order: reward(Lambda), then the most
relevant element of E ^ E' (an e-vertex, even) lies in the larger. Reference b = T (the last state).
Per genome (must-0 counters):
  phifail    a step with LAG_t != {} at which Phi falls, or stays at a non-stall, or changes at a stall (L1)
  nocyc      a stall at which iterating s (mover -> sigma_b gate, gate -> current face, beta -> its successor) from a FRONT vertex leaves
             FRONT or meets a non-(mover, gate, beta) vertex before closing a cycle (L4)
  qfail      #non-stall steps with LAG != {} above P = 2M(N + 2M) (C1);  tfail: T above P(N + 2M + 6) + N (ALL-TCYC)
  platfail   a plateau (maximal constant-Phi interval [u, v], u < v) with v - u > N + 2M + 5 (PLATEAU)
  sharpfail  v - u > #movers of Y (Y = {x : class_u(x) <= m}); L-RED's route: LAM-GAP / SHARP on the one-player sub-game H (R234)
  oddquiet   an Odd flip at a gate whose two face classes are both unchanged at that step (L-LIT T69 (a); landed R126 GATE-CLASS
             excludes it); k2flips: flips of K2 (LOC-K2 excludes them)
Descriptive: oddflips, T, q, plateaus, maxplat, max (v - u)/(movers of Y), stalls. CTRL=1: the e-set order REVERSED (most relevant differing element in the SMALLER class) -> must fire.
Usage: lv235.py G.json ...  (prints one line per genome and a TOTAL)"""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r221q"))
import own as OWN
CTRL = os.environ.get("CTRL") == "1"
def analyse(G):
    n, prio, ow, succ, V, O = OWN.build(G); out, V2, O2, _ = OWN.run(G); vj = OWN.VJ(prio); rk = vj.rk
    N = G["N"]; M = len(O); T = len(out) - 1
    E = {V[("e", q)] for q in O}; gates = {V[("g", q)]: q for q in O}; betas = {V[("b", q)]: q for q in O}
    def cls(val):
        lam, Pi = val[0], val[1]
        return (vj.rew(lam), tuple(sorted((rk[u] for u in Pi if u in E), reverse=True)))
    def lt(a, b):          # class a < class b
        if a[0] != b[0]: return a[0] < b[0]
        x, y = set(a[1]), set(b[1]); d = x ^ y
        return bool(d) and ((max(d) in y) != CTRL)
    C = [[cls(vals[v]) for v in range(n)] for (_, vals, _) in out]
    fin = C[T]
    def phi(t):
        lag = [v for v in range(n) if C[t][v] != fin[v]]
        if not lag: return None, None
        m = lag[0]
        for v in lag:
            if lt(C[t][v], C[t][m]): m = v
        mc = C[t][m]; front = [v for v in lag if C[t][v] == mc]
        return mc, front
    r = dict(N=N, M=M, T=T, phifail=0, nocyc=0, qfail=0, tfail=0, platfail=0, sharpfail=0, q=0, stalls=0, plateaus=0, maxplat=0, maxratio=0.0, oddflips=0, oddquiet=0, k2flips=0)
    P = 2 * M * (N + 2 * M); seq = []
    for t in range(T + 1):
        mc, fr = phi(t); seq.append((mc, None if fr is None else len(fr), fr))
    sigb = out[T][0]
    for t in range(T):
        mc, k, fr = seq[t]
        if mc is None: continue
        stall = all(C[t + 1][v] == C[t][v] for v in fr)
        mc2, k2, _ = seq[t + 1]
        if stall:
            r["stalls"] += 1
            if (mc2, k2) != (mc, k): r["phifail"] += 1
            # (L4): iterate s inside FRONT
            F = set(fr); tau = out[t][2]; sig = out[t][0]; v = fr[0]; seen = set(); ok = True
            for _ in range(len(F) + 2):
                if v in seen: break
                seen.add(v)
                if v < N: w = sigb[v]
                elif v in gates: w = tau[v]
                elif v in betas: w = succ[v][0]
                else: ok = False; break
                if w not in F: ok = False; break
                v = w
            if not ok: r["nocyc"] += 1
        else:
            r["q"] += 1
            if mc2 is not None and not (lt(mc, mc2) or (mc2 == mc and k2 < k)): r["phifail"] += 1
    for t in range(T):          # (a) of L-LIT T69: an Odd flip at a gate with BOTH face classes constant (R126 GATE-CLASS says never)
        for g, q in gates.items():
            if out[t][2][g] != out[t + 1][2][g]:
                r["oddflips"] += 1; fe, fb = V[("e", q)], V[("b", q)]
                if C[t][fe] == C[t + 1][fe] and C[t][fb] == C[t + 1][fb]: r["oddquiet"] += 1
        if out[t][2][V["K2"]] != out[t + 1][2][V["K2"]]: r["k2flips"] += 1
    r["qfail"] = int(r["q"] > P); r["tfail"] = int(T > P * (N + 2 * M + 6) + N)
    t = 0
    while t <= T:
        if seq[t][0] is None: t += 1; continue
        u = t
        while t + 1 <= T and seq[t + 1][0] == seq[u][0] and seq[t + 1][1] == seq[u][1]: t += 1
        v = t
        if v > u:
            r["plateaus"] += 1; L = v - u; r["maxplat"] = max(r["maxplat"], L); m = seq[u][0]
            Ymov = sum(1 for x in range(N) if not lt(m, C[u][x]))
            r["platfail"] += L > N + 2 * M + 5; r["sharpfail"] += L > Ymov
            r["maxratio"] = max(r["maxratio"], round(L / max(1, Ymov), 3))
        t += 1
    return r
if __name__ == "__main__":
    tot = {}
    for fn in sys.argv[1:]:
        G = json.load(open(fn)); G = G.get("genome", G); G.pop("_evals", None)
        if not (isinstance(G, dict) and "opts" in G): continue
        r = analyse(G); print(os.path.basename(fn), r, flush=True)
        for k, v in r.items():
            if k in ("N", "M"): continue
            tot[k] = max(tot.get(k, 0), v) if k in ("T", "maxplat", "maxratio") else tot.get(k, 0) + v
        tot["genomes"] = tot.get("genomes", 0) + 1
    print("TOTAL", tot, flush=True)
