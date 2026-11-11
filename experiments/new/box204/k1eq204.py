#!/usr/bin/env python3
"""Box 204 (L-NEW successor 68): checks for Lemma E-FACE = W-TARGET and the k = 1 mechanism census, on IDEAL-CYC (box203 gfc203.hist_ideal).
Per genome:
  wfail  (must 0; unit (gate, state)): a gate g whose W-target wt(g) is a mover, with class_t(e_g) != (Lambda_t(wt), {e_g} u E_t(wt)), or
         with e_g in E_t(wt);
  dfail  (must 0; unit gate): D^tot(e_g) != D^tot(wt(g)) for such a gate;
  record gate (most flips): flips, D^tot of its faces, D^tot of its W-target, and how many of each face's class changes fall on steps
         where the set of cycles of the functional Xi-graph Xi_sigma changes (Ccyc);
  T, R (R118: steps with a sigma-bar change and no Lambda change), C, sum_g flips, max over gates of min(D^tot faces) and of max(D^tot faces).
  bfail  (must 0; unit (gate, state)): class_t(beta_g) != class_t(xt(g)) for a mover Xi-target, or != (K1, empty) on escape;
Controls: K1EQ_CTRL=1 compares class(e_g) with class(wt) WITHOUT adding e_g (wfail must fire); K1EQ_CTRL=2 adds e_g to class(xt)
in the beta check (bfail must fire).
Usage: k1eq204.py G.json ... | k1eq204.py --rand k1|rand SEED COUNT  (ROOT default from this file's place)."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box203"))
import gfc203, idealcyc
CTRL = os.environ.get("K1EQ_CTRL", "0")

def run(G):
    H, n, E, V, gates = gfc203.hist_ideal(G); st = idealcyc.run(G, cap=20000); N = G["N"]; T = len(H) - 1
    emask = 0
    for k, v in V.items():
        if isinstance(k, tuple) and k[0] == "e": emask |= E.bit[v]
    cl = lambda v, t: (H[t][0][v][0], H[t][0][v][1] & emask)
    def cycs(s):
        nxt = {x: G["opts"][x][s[x]][1] for x in range(N)}; seen = set(); out = set()
        for x0 in range(N):
            path = []; idx = {}; x = x0
            while x >= 0 and x not in idx and x not in seen: idx[x] = len(path); path.append(x); x = nxt[x]
            if x >= 0 and x in idx: out.add(frozenset(path[idx[x]:]))
            seen.update(path)
        return frozenset(out)
    cy = [cycs(s) for s in st]; cch = {t for t in range(1, T + 1) if cy[t] != cy[t - 1]}
    wfail = dfail = bfail = 0; sumfl = 0; best = None; mn = mx = 0
    Dt = lambda v: len({cl(v, t) for t in range(T + 1)})
    for gv, (q, a, b) in gates.items():
        wt = G["opts"][q[0]][q[1]][0]; ebit = E.bit[a]
        if wt >= 0:
            for t in range(T + 1):
                la, ea = cl(a, t); lw, ew = cl(wt, t)
                want = (lw, ew | (0 if CTRL == "1" else ebit))
                if (la, ea) != want or (ew & ebit): wfail += 1
            if Dt(a) != Dt(wt): dfail += 1
        xt = G["opts"][q[0]][q[1]][1]
        for t in range(T + 1):                      # FACE-TARGET (b): class(beta_g) = class(xt), or (K1, 0) on escape
            want = cl(xt, t) if xt >= 0 else (V[("K", 1)], 0)
            if CTRL == "2" and xt >= 0: want = (want[0], want[1] | ebit)
            if cl(b, t) != want: bfail += 1
        fl = sum(H[t - 1][1][gv] != H[t][1][gv] for t in range(1, T + 1)); sumfl += fl
        da, db = Dt(a), Dt(b); mn = max(mn, min(da, db)); mx = max(mx, da, db)
        if best is None or fl > best[0]: best = (fl, q, da, db, Dt(wt) if wt >= 0 else None, a, b)
    fl, q, da, db, dw, a, b = best
    chg = lambda v: [t for t in range(1, T + 1) if cl(v, t) != cl(v, t - 1)]
    ca, cb = chg(a), chg(b)
    C = sum(1 for t in range(1, T + 1) if any(H[t - 1][0][v][0] != H[t][0][v][0] for v in range(n)))
    R = sum(1 for t in range(1, T + 1) if not any(H[t - 1][0][v][0] != H[t][0][v][0] for v in range(n))
            and any(H[t - 1][1][v] != H[t][1][v] for v in range(n) if H[t][1][v] is not None))
    return dict(wfail=wfail, dfail=dfail, bfail=bfail, T=T, C=C, R=R, sumflips=sumfl, maxminface=mn, maxmaxface=mx, gate=q, flips=fl,
                Dface=(da, db), Dwt=dw, ech=len(ca), ech_at_Ccyc=len([t for t in ca if t in cch]), bch=len(cb),
                bch_at_Ccyc=len([t for t in cb if t in cch]), Ccyc_changes=len(cch))

if __name__ == "__main__":
    if sys.argv[1] == "--rand":                     # --rand k1|rand SEED COUNT: totals of wfail, dfail
        import random, collections
        sys.path.insert(0, os.path.join(gfc203.ROOT, "experiments/new/box191")); import rand191, k1srch202, fvs202
        mode, seed, cnt = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]); rng = random.Random(seed); c = collections.Counter()
        while c["genomes"] < cnt:
            if mode == "rand": G = rand191.rgen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.randint(2, 3))
            else:
                G = k1srch202.mk(rng)
                if G is None or fvs202.kfvs(G)[0] != 1: continue
            r = run(G); c["genomes"] += 1; c["wfail"] += r["wfail"]; c["dfail"] += r["dfail"]; c["bfail"] += r["bfail"]
        print(mode, "seed", seed, "ctrl", CTRL, dict(c), flush=True); sys.exit(0)
    for f in sys.argv[1:]:
        r = run(json.load(open(f)))
        print(os.path.basename(f), "ctrl", CTRL, " ".join(f"{k} {v}" for k, v in r.items()).replace(", ", ","), flush=True)
