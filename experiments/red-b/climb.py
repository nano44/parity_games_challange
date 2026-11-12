#!/usr/bin/env python3
"""Hill climbs on genomes (L-RED-B). Every candidate is run on eng.py and checked by lev.check_run (reference b = T);
a candidate with a non-zero must-0 counter is written to work/viol_<tag>.jsonl and the climb continues.
Usage: climb.py <objective> <seed> <iters> <Ncap> <Mcap> [start.json]
Objectives: T (run length), plat (longest plateau), loud (loud stalls), mvals (values of m), phi (values of Phi),
  platrel (1000 * longest plateau / (movers in Y + 1)), stalls, bothYeq, Tn (1000 * T / (N + M)).
State is checkpointed to work/climb_<tag>.json every 200 iterations and the climb resumes from it."""
import sys, os, json, random, time
import eng, gen, lev, mut

def score(G, obj, tie="keep-low"):
    g = eng.build(G)
    h = eng.howard_run(g, tie=tie, cap=20000)
    c, d = lev.check_run(g, h, refs="T")
    bad = {k: c[k] for k in lev.CNT if c[k]}
    if obj == "T": s = d["T"]
    elif obj == "plat": s = d["platmax"] * 1000 + d["T"]
    elif obj == "loud": s = d["stallloud"] * 1000 + d["stalls"]
    elif obj == "mvals": s = d["mvals"] * 1000 + d["T"]
    elif obj == "phi": s = d["phivals"]
    elif obj == "platrel": s = (1000 * d["platmax"]) // (d["platY"] + 1)
    elif obj == "stalls": s = d["stalls"] * 1000 + d["T"]
    elif obj == "bothYeq": s = d["cov_bothYeq"] * 1000 + d["cov_bothY"]
    elif obj == "Tn": s = (1000 * d["T"]) // (g.N + g.M)
    else: raise ValueError(obj)
    return s, d, bad

def main():
    obj, seed, iters, Ncap, Mcap = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    startf = sys.argv[6] if len(sys.argv) > 6 else None
    tag = "%s_s%d_N%d_M%d%s" % (obj, seed, Ncap, Mcap, ("_" + os.path.basename(startf).replace(".json", "")) if startf else "")
    os.makedirs("work", exist_ok=True)
    ck = "work/climb_%s.json" % tag; vf = open("work/viol_%s.jsonl" % tag, "a")
    if os.path.exists(ck):
        S = json.load(open(ck)); cur, cs, best, bs, it = S["cur"], S["cs"], S["best"], S["bs"], S["it"]
    else:
        rng0 = random.Random(seed)
        if startf: cur = mut.normalize(json.load(open(startf)))
        else: cur = gen.shaped(rng0, min(Ncap, 6), "mix")
        cs, _, _ = score(cur, obj); best, bs, it = cur, cs, 0
    t0 = time.time(); nviol = 0
    while it < iters:
        rng = random.Random(seed * 1000003 + it); it += 1
        cand = cur
        for _ in range(rng.choice([1, 1, 1, 2, 2, 3, 5])):
            c2 = mut.mutate(cand, rng, Ncap, Mcap)
            if c2 is not None: cand = c2
        if cand is cur: continue
        try: s, d, bad = score(cand, obj, tie=rng.choice(["keep-low", "keep-low", "high"]))
        except RuntimeError: continue
        if bad:
            nviol += 1; vf.write(json.dumps({"G": cand, "bad": bad}) + "\n"); vf.flush()
        if s >= cs or rng.random() < 0.002:
            cur, cs = cand, s
            if s > bs:
                best, bs = cand, s
                print("it %d best %d N %d M %d T %d platmax %d platY %d stalls %d loud %d mvals %d phivals %d  %.0fs" % (
                    it, bs, cand["N"], mut.M_of(cand), d["T"], d["platmax"], d["platY"], d["stalls"], d["stallloud"], d["mvals"],
                    d["phivals"], time.time() - t0), flush=True)
        if it % 200 == 0:
            json.dump({"cur": cur, "cs": cs, "best": best, "bs": bs, "it": it}, open(ck + ".tmp", "w")); os.replace(ck + ".tmp", ck)
    json.dump({"cur": cur, "cs": cs, "best": best, "bs": bs, "it": it}, open(ck + ".tmp", "w")); os.replace(ck + ".tmp", ck)
    print("CLIMB %s done it %d best %d viol %d" % (tag, it, bs, nviol), flush=True)

if __name__ == "__main__":
    main()
