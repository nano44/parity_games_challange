#!/usr/bin/env python3
"""Box 192 (L-NEW successor 60): potentials for R on IDEAL-CYC (Howard at the movers of Gamma(G); box191 idealcyc.py, unmodified).
Per step t -> t+1 (label C / R / p as box191 subrun191): records
  EQ     every sigma-bar change at an R-step is at a gate whose faces e_g, beta_g have the same cycle node (Lemma EQ-FLIP);
  HEAD   head(v) := most relevant e-vertex in Pi(v) (or none); whether some vertex's head changes at the step (HEAD-STEP test);
  HEADF  whether a face of a flipping gate changes head (FLIP-H test, per flip);
  XSZ    max over vertices of |(Pi_t(v) xor Pi_t+1(v)) & E-set| at Lambda-constant vertices (exchange size);
  MON    TOP-MON check: at Lambda-constant vertices head never decreases in relevance.
Usage: rpot192.py FILES.json | rpot192.py rand COUNT SEED"""
import sys, os, json, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [os.path.join(ROOT, "experiments/new/box191"), os.path.join(ROOT, "experiments/new/box189")]
import idealcyc, gamma3, rand191

def states(G):
    h, s0, movers, inv = idealcyc.build(G); E = idealcyc.Engine(h); st = idealcyc.run(G)
    _, _, _, V = gamma3.build(G, set()); name = {v: k for k, v in V.items()}
    gi = {}
    for x in range(G["N"]):
        for v in h.succ[movers[x]]: gi[(x, inv[v])] = v
    out = []
    for s in st:
        cur = list(s0)
        for x in range(G["N"]): cur[movers[x]] = gi[(x, s[x])]
        out.append(E.evaluate(tuple(cur)))
    return h, E, V, name, movers, out

def analyse(G):
    h, E, V, name, movers, ev = states(G)
    ES = 0
    for v in range(h.n):
        if name[v][0] == "e": ES |= 1 << E.rank[v]
    gates = [v for v in range(h.n) if h.owner[v] == 1 and name[v][0] == "g"]
    head = lambda val: (val[1] & ES).bit_length()      # 0 = none, else rank + 1
    r = dict(T=len(ev) - 1, C=0, R=0, p=0, flips=0, eqfail=0, Rnohead=0, flipnoh=0, xsz=0, monfail=0, Rnohead_t=[])
    for t in range(1, len(ev)):
        (pv, ps), (vs, sb) = ev[t - 1], ev[t]
        C = any(pv[v][0] != vs[v][0] for v in range(h.n)); fl = [g for g in gates if ps[g] != sb[g]]
        if h.owner and ps[[v for v in range(h.n) if name[v] == ("K", 2)][0]] != sb[[v for v in range(h.n) if name[v] == ("K", 2)][0]]: fl.append("K2")
        lab = "C" if C else ("R" if fl else "p"); r[lab] += 1
        for v in range(h.n):
            if pv[v][0] == vs[v][0]:
                if head(vs[v]) < head(pv[v]): r["monfail"] += 1
                r["xsz"] = max(r["xsz"], bin((pv[v][1] ^ vs[v][1]) & ES).count("1"))
        if lab != "R": continue
        r["flips"] += len(fl)
        hch = any(head(pv[v]) != head(vs[v]) for v in range(h.n))
        if not hch: r["Rnohead"] += 1; r["Rnohead_t"].append(t)
        for g in fl:
            q = name[g][1]; e, b = V[("e", q)], V[("b", q)]
            if vs[e][0] != vs[b][0] or pv[e][0] != pv[b][0]: r["eqfail"] += 1
            if head(vs[e]) == head(pv[e]) and head(vs[b]) == head(pv[b]): r["flipnoh"] += 1
    return r

if __name__ == "__main__":
    if sys.argv[1] == "rand":
        cnt, seed = int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed); tot = {}
        for i in range(cnt):
            G = rand191.rgen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.randint(2, 3)); a = analyse(G)
            for k in ("T", "C", "R", "p", "flips", "eqfail", "Rnohead", "flipnoh", "monfail"): tot[k] = tot.get(k, 0) + a[k]
            tot["xsz"] = max(tot.get("xsz", 0), a["xsz"])
        print(f"rand count {cnt} seed {seed}:", " ".join(f"{k} {v}" for k, v in tot.items()))
    else:
        for f in sys.argv[1:]:
            G = json.load(open(f)); a = analyse(G)
            print(os.path.basename(f), "N", G["N"], " ".join(f"{k} {v}" for k, v in a.items()))
