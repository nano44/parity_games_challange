# L-LIT T34 (docs/lit/T34-friedmann-vs-n5.md). Reads other lanes' code read-only (hn.py, census.py: L-COMP; n5b.py: L-COMP).
# Usage: python3 -I docs/lit/T34-gateshut-check.py N R SEED   (R = number of random starts, L-COMP's CE.rand_start with that seed; R = 0: S3 and F only)
# T34: check Lemma GATE-SHUT on Friedmann's H_n under N5 (n5b SPEC). At every visited state, for every gate i with tau(e_i) = h_i:
# if (H1) the cycle node of Xi_tau(h_i) has rank below rank(d1_i), and (H2) the (taubar, tau)-play from h_i avoids d1_i, d2_i, d3_i, e_i,
# then d1_i must NOT be in I_tau(e_i). Also counts how often the hypotheses hold and how often h->d flips happen.
import os, random, sys
ROOT = "/home/user/parity_games_challange"; H = os.path.join(ROOT, "experiments", "friedmann-hn")
for p in ("n5-epoch", "n5-exhaustive", "n5-second", "harness", "hard-families"):
    sys.path.insert(0, os.path.join(ROOT, "experiments", p))
sys.path.insert(0, H)
import hn, census as CE, n5b
n, R, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
g, ix = hn.build(n); rng = random.Random(seed)
rank = {v: r for r, v in enumerate(sorted(range(g.n), key=lambda v: (g.prio[v], v)))}
SG = n5b.SpecSI(g)
starts = [("S3", None, None)]
io = hn.iota(n, ix); sig0 = [io.get(v, -1) if g.owner[v] == 0 else -1 for v in range(g.n)]
_, sb0 = SG.evaluate_choice(list(sig0)); starts.append(("F", sig0, [sb0[v] if g.owner[v] == 1 else -1 for v in range(g.n)]))
for r in range(R):
    s, t = CE.rand_start(g, rng); starts.append((f"rand{r}", s, t))
held = viol = flips = flips_h = tot = 0
for lab, s, t in starts:
    N = n5b.N5(g); N.mode = "spec"; tr = []
    N.run(list(s) if s else None, list(t) if t else None, trace=tr)
    for k, (sig, tau) in enumerate(tr):
        tau = list(tau); vt, tbar = N.SD.evaluate_choice(tau); It = N.improving(N.SD, tau, vt)
        for i in range(1, n + 1):
            e, h, d1, d2, d3 = (ix[f"e{i}"], ix[f"h{i}"], ix[f"d1_{i}"], ix[f"d2_{i}"], ix[f"d3_{i}"])
            if tau[e] != h:
                continue
            tot += 1
            c = vt[h][0]; v = h; seen = []
            while v not in seen:
                seen.append(v); v = tau[v] if g.owner[v] == 1 else tbar[v]
            hyp = rank[c] < rank[d1] and not ({d1, d2, d3, e} & set(seen))
            imp = d1 in It.get(e, [])
            nxt = tr[k + 1][1][e] if k + 1 < len(tr) else h
            if nxt == d1:
                flips += 1; flips_h += hyp
            if hyp:
                held += 1
                if imp:
                    viol += 1; print("VIOLATION", lab, k, i)
print(f"n={n} starts={len(starts)} gate-states with tau(e)=h: {tot}; with (H1),(H2): {held}; violations (d1 in I_tau): {viol}; "
      f"h->d1 flips: {flips}, of which with (H1),(H2): {flips_h}")
