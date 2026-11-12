#!/usr/bin/env python3
"""L-RED 64 R230 item 5 (counter side of HYPOTHESIS [E-LEV] in R125 CHAIN3 / R123 UP-T): N5'-xi from S3 on Gamma3(G) with the
e-priorities PERMUTED (G["ekey"][x][k]: a sort key per option; the e-vertices get the same SET of priorities as gamma3.build gives, in
ekey order instead of (lev, gate) order), U(G) held small.
  U(G)   = #options (x, k) whose Xi-target xt has a higher level than x (R123 UP-T's U)
  inv    = #pairs of options (q, q') with lev(q) < lev(q') and pr(e_q) > pr(e_q')   ([E-LEV] holds iff inv = 0)
  T3     = index of the first fallback - 1 (N5'-xi's mover phase), total = N5'-xi iterations to the end (cap CAP), fb = #fallbacks
  nstd   = non-standard states before the first fallback (as std230)
Usage: elev230.py G.json ... (prints U, inv, T3, total per genome) | elev230.py repair IN.json OUT.json UMAX SEED (U <= UMAX, random ekey)"""
import sys, os, json, random
from bonly3_230 import gamma3, n5v, pg, topg, PADS
CAP = int(os.environ.get("CAP", "20000"))
def U(G):
    lev = G["lev"]; return sum(1 for x in range(G["N"]) for o in G["opts"][x] if o[1] >= 0 and lev[o[1]] > lev[x])
def fix_ekey(G, rng):
    ek = G.get("ekey") or []
    G["ekey"] = [[(ek[x][k] if x < len(ek) and k < len(ek[x]) else rng.random()) for k in range(len(G["opts"][x]))] for x in range(G["N"])]
    return G
def build(G):
    gm, sig, tau, V = gamma3.build(G, PADS); N = G["N"]
    O = [(x, k) for x in range(N) for k in range(len(G["opts"][x]))]
    if "ekey" in G:
        ps = sorted(gm.prio[V[("e", q)]] for q in O)
        for p, q in zip(ps, sorted(O, key=lambda q: (G["ekey"][q[0]][q[1]], q))): gm.prio[V[("e", q)]] = p
    return gm, sig, tau, V, O
def inv(G, gm, V, O):
    lev = G["lev"]; pr = {q: gm.prio[V[("e", q)]] for q in O}
    return sum(1 for a in O for b in O if lev[a[0]] < lev[b[0]] and pr[a] > pr[b])
def measure(G):
    gm, sig0, tau0, V, O = build(G); N = G["N"]
    gp = pg.parse(topg(gm)); E, Ed = n5v.Engine(gp), n5v.Engine(n5v.dual(gp))
    s, t = n5v.n5x.start_pair(gp, E, Ed, None); st = [(list(s), list(t))]; fbs = []
    while len(st) <= CAP:
        r = n5v.step(gp, E, Ed, s, t, "xi")
        if r is None: break
        s, t, _, _, fb = r; st.append((list(s), list(t))); fbs.append(fb)
    ffb = next((i + 1 for i, f in enumerate(fbs) if f), len(st))
    mpad = {V[("m", q)] for q in O}; nstd = 0
    for j in range(min(ffb, len(st))):
        s, t = st[j]
        if not (all(t[v] == tau0[v] for v in tau0) and all(s[v] == sig0[v] for v in sig0 if v >= N) and all(s[x] in mpad for x in range(N))): nstd += 1
    return dict(N=N, M=len(O), U=U(G), inv=inv(G, gm, V, O), T3=ffb - 1, total=len(st) - 1, fb=sum(fbs), nstd=nstd, capped=len(st) > CAP)
def repair(G, umax, rng):
    lev = G["lev"]; ups = [(x, k) for x in range(G["N"]) for k, o in enumerate(G["opts"][x]) if o[1] >= 0 and lev[o[1]] > lev[x]]
    rng.shuffle(ups)
    for x, k in ups[umax:]:
        low = [y for y in range(G["N"]) if lev[y] <= lev[x]]; G["opts"][x][k][1] = rng.choice(low + [-1])
    return G
if __name__ == "__main__":
    if sys.argv[1] == "repair":
        rng = random.Random(int(sys.argv[5])); G = json.load(open(sys.argv[2])); G.pop("_evals", None)
        G = fix_ekey(repair(G, int(sys.argv[4]), rng), rng); json.dump(G, open(sys.argv[3], "w")); print(sys.argv[3], measure(G)); sys.exit(0)
    for f in sys.argv[1:]:
        G = json.load(open(f)); print(os.path.basename(f), measure(G), flush=True)
