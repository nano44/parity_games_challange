#!/usr/bin/env python3
"""Hill climbs (L-RED-B), second generation: objectives from press.stats and lev.check_run; every candidate is checked by
BOTH (27 + 5 must-0 counters); a candidate with a non-zero counter is written to work/viol2_<tag>.jsonl.
Usage: climb2.py <objective> <seed> <iters> <Ncap> <Mcap> [start.json]
Objectives: R (flip steps), maxgate (most flips of one gate), stallflips (flips at stall steps), minch (a flip step with
  the FEWEST class changes: maximises -minch among runs with a flip), betavals (distinct lowest-lagging classes in case
  (beta)), lamvals (distinct cycle nodes over the run), RoverQ (1000 R / (Q + 1)), plat, loud, mvals, phi, platrel, T, Tn
  (as in climb.py), score2 (T * 1000 / bound-free scale N + M, ties broken by stalls).
Resumable: work/climb2_<tag>.json every 200 iterations."""
import sys, os, json, random, time
import eng, gen, lev, mut, press

def score(G, obj, tie):
    g = eng.build(G)
    h = eng.howard_run(g, tie=tie, cap=20000)
    c, d = lev.check_run(g, h, refs="T")
    c2, d2 = press.stats(g, h)
    bad = {k: c[k] for k in lev.CNT if c[k]}; bad.update({k: c2[k] for k in press.PCNT if c2[k]})
    if obj == "R": s = d2["R"] * 1000 + d2["flips"]
    elif obj == "maxgate": s = d2["maxgate"] * 1000 + d2["R"]
    elif obj == "stallflips": s = d2["stallflips"] * 1000 + d["stallloud"]
    elif obj == "minch": s = (100000 - d2["minch"]) if d2["minch"] >= 0 else 0
    elif obj == "betavals": s = d2["betavals"] * 1000 + d["beta"]
    elif obj == "lamvals": s = d2["lamvals"] * 1000 + d2["C"]
    elif obj == "RoverQ": s = (1000 * d2["R"]) // (d2["Q"] + 1)
    elif obj == "plat": s = d["platmax"] * 1000 + d["T"]
    elif obj == "loud": s = d["stallloud"] * 1000 + d["stalls"]
    elif obj == "mvals": s = d["mvals"] * 1000 + d["T"]
    elif obj == "phi": s = d["phivals"]
    elif obj == "platrel": s = (1000 * d["platmax"]) // (d["platY"] + 1)
    elif obj == "T": s = d["T"]
    elif obj == "Tn": s = (1000 * d["T"]) // (g.N + g.M)
    else: raise ValueError(obj)
    info = dict(T=d["T"], platmax=d["platmax"], platY=d["platY"], stalls=d["stalls"], loud=d["stallloud"], mvals=d["mvals"],
                phivals=d["phivals"], R=d2["R"], flips=d2["flips"], maxgate=d2["maxgate"], stallflips=d2["stallflips"],
                minch=d2["minch"], betavals=d2["betavals"], lamvals=d2["lamvals"], Q=d2["Q"])
    return s, info, bad

def main():
    obj, seed, iters, Ncap, Mcap = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    startf = sys.argv[6] if len(sys.argv) > 6 else None
    tag = "%s_s%d_N%d_M%d%s" % (obj, seed, Ncap, Mcap, ("_" + os.path.basename(startf).replace(".json", "")) if startf else "")
    os.makedirs("work", exist_ok=True)
    ck = "work/climb2_%s.json" % tag; vf = open("work/viol2_%s.jsonl" % tag, "a")
    if os.path.exists(ck):
        S = json.load(open(ck)); cur, cs, best, bs, it, nviol = S["cur"], S["cs"], S["best"], S["bs"], S["it"], S.get("nviol", 0)
    else:
        rng0 = random.Random(seed)
        if startf: cur = mut.normalize(json.load(open(startf)))
        else: cur = gen.shaped(rng0, min(Ncap, 6), "mix")
        cs, _, _ = score(cur, obj, "keep-low"); best, bs, it, nviol = cur, cs, 0, 0
    t0 = time.time()
    def save():
        json.dump({"cur": cur, "cs": cs, "best": best, "bs": bs, "it": it, "nviol": nviol}, open(ck + ".tmp", "w")); os.replace(ck + ".tmp", ck)
    while it < iters:
        rng = random.Random(seed * 1000003 + it); it += 1
        cand = cur
        for _ in range(rng.choice([1, 1, 1, 2, 2, 3, 5])):
            c2 = mut.mutate(cand, rng, Ncap, Mcap)
            if c2 is not None: cand = c2
        if cand is cur: continue
        try: s, info, bad = score(cand, obj, rng.choice(["keep-low", "keep-low", "high"]))
        except RuntimeError: continue
        if bad:
            nviol += 1; vf.write(json.dumps({"G": cand, "bad": bad}) + "\n"); vf.flush()
        if s >= cs or rng.random() < 0.002:
            cur, cs = cand, s
            if s > bs:
                best, bs = cand, s
                print("it %d best %d N %d M %d %s  %.0fs" % (it, bs, cand["N"], mut.M_of(cand),
                      " ".join("%s %d" % (k, v) for k, v in info.items()), time.time() - t0), flush=True)
        if it % 200 == 0: save()
    save()
    print("CLIMB2 %s done it %d best %d viol %d" % (tag, it, bs, nviol), flush=True)

if __name__ == "__main__":
    main()
