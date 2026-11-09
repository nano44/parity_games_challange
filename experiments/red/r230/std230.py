#!/usr/bin/env python3
"""L-RED 64 R230 (adversary vs R118 (k) REACH3-CYC / R125 REACH3-ALL): N5'-xi from S3 on Gamma3(G) (all pads), Xi-cyclic genomes allowed.
Hard counters (each a REACH3-CYC failure; must be 0):
  nstd   states j < ffb (ffb = index of the state reached by the first fallback) that are not standard: tau != start, or sigma != start
         off the movers, or a mover not on a mover pad   [unit: states]
  nonhow transitions j -> j+1 < ffb at which some mover's new successor is not a <=-best (Howard key) successor, or some mover with a
         strictly better successor keeps its edge                                                        [unit: transitions]
  t3     1 if ffb != T3 + 1, T3 = the first state where no mover has a strictly better successor          [unit: genomes]
Near-miss scores (climb gradient only, not failures):
  offimp (state, edge) pairs before ffb in I_sigma at a non-mover Even vertex other than (K0, K1)
  mtie   (state, mover) pairs before ffb with >= 2 equal best Howard keys (exact VJ ties)
  taui   states before ffb with I_tau != empty
score(G) = (nstd + nonhow + t3, taui, mtie, states) (SCORE=off: (.., offimp, taui, mtie)). Env LNEW as bonly3_230.py.
Usage: std230.py G.json ... | std230.py rand SEED COUNT"""
import sys, os, json, random
from bonly3_230 import gamma3, n5v, pg, topg, rgen, PADS
def measure(G, cap=4000):
    gm, sig0, tau0, V = gamma3.build(G, PADS); n = gm.n; N = G["N"]; opts = G["opts"]
    O = [(x, k) for x in range(N) for k in range(len(opts[x]))]; degs = [len(o) for o in opts]
    gp = pg.parse(topg(gm)); E, Ed = n5v.Engine(gp), n5v.Engine(n5v.dual(gp))
    s, t = n5v.n5x.start_pair(gp, E, Ed, None); st = [(list(s), list(t))]; fbs = []
    while len(st) <= cap:
        r = n5v.step(gp, E, Ed, s, t, "xi")
        if r is None: break
        s, t, _, _, fb = r; st.append((list(s), list(t))); fbs.append(fb)
        if fb: break                                             # nothing after the first fallback is scored
    ffb = len(st) - 1 if fbs and fbs[-1] else len(st)
    K0, K1 = V[("K", 0)], V[("K", 1)]; mpad = {V[("m", q)]: q[1] for q in O}
    c = dict(nstd=0, nonhow=0, t3=0, offimp=0, mtie=0, taui=0, states=ffb, n=n, N=N, M=len(O)); T3 = None
    for j in range(min(ffb, len(st))):
        s, t = st[j]
        std = all(t[v] == tau0[v] for v in tau0) and all(s[v] == sig0[v] for v in sig0 if v >= N) and all(s[x] in mpad for x in range(N))
        if not std: c["nstd"] += 1; continue
        vs, _ = E.evaluate(tuple(s if True else s)); Is = E.improving(tuple(s), vs)
        vt, _ = Ed.evaluate(tuple(t)); It = Ed.improving(tuple(t), vt)
        c["taui"] += bool(It); c["offimp"] += sum(1 for v, w in Is if v >= N and (v, w) != (K0, K1))
        better = False; best = {}
        for x in range(N):
            ks = {V[("m", (x, k))]: E.key(E.extend(x, vs[V[("m", (x, k))]])) for k in range(degs[x])}
            b = max(ks.values()); best[x] = {w for w, kk in ks.items() if kk == b}; c["mtie"] += len(best[x]) >= 2
            if ks[s[x]] < b: better = True
        if not better and T3 is None: T3 = j
        if j + 1 < ffb:
            s2 = st[j + 1][0]
            for x in range(N):
                if s2[x] not in best[x] or (s[x] not in best[x] and s2[x] == s[x]): c["nonhow"] += 1; break
    c["t3"] = int(T3 is None or ffb != T3 + 1) if ffb < len(st) or (fbs and fbs[-1]) else 1
    c["T3"] = T3; c["ffb"] = ffb
    return c
def score(c):
    h = c["nstd"] + c["nonhow"] + c["t3"]
    if os.environ.get("SCORE", "tie") == "off": return (h, c["offimp"], c["taui"], c["mtie"])
    return (h, c["taui"], c["mtie"], c["states"])          # default: ties and run length (where N5'-xi and Howard can part)
if __name__ == "__main__":
    tot = {}
    if sys.argv[1] == "rand":
        rng = random.Random(int(sys.argv[2])); Gs = ((f"r{i}", rgen(rng, rng.randint(1, 4), rng.randint(1, 3), rng.choice([2, 3]))) for i in range(int(sys.argv[3])))
    else: Gs = ((os.path.basename(f), json.load(open(f))) for f in sys.argv[1:])
    for tag, G in Gs:
        if not (isinstance(G, dict) and "opts" in G): continue
        c = measure(G)
        for k in ("nstd", "nonhow", "t3", "offimp", "mtie", "taui", "states"): tot[k] = tot.get(k, 0) + c[k]
        tot["genomes"] = tot.get("genomes", 0) + 1
        if score(c)[0]: print("FAIL", tag, c, flush=True)
    print("TOTAL", tot, flush=True)
