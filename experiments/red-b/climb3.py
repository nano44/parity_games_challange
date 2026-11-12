#!/usr/bin/env python3
"""Hill climbs on Gamma3 / HOW3 (L-RED-B, B2 / box 209). Every candidate is checked by all lev3 must-0 counters; a candidate with
a non-zero counter goes to work/viol3c_<tag>.jsonl. Objectives:
  T       1000 T3 / (N + M)           (growth of T3 per size)
  Tabs    T3 (sizes capped)
  plat    1000 (longest plateau) / (movers of Y + 1), ties by the plateau length
  phi     number of Phi values (reference T3)
  tail    T3 - b'
  stall   stall steps
Usage: climb3.py <obj> <seed> <iters> <Ncap> <Mcap> [tie] [start.json]
Resumable: work/climb3_<tag>.json every 100 iterations (best genome, score, iteration)."""
import sys, os, json, random, time
import eng, eng3, gen, lev3, mut

def score(G, obj, tie, rng):
    g = eng3.build3(G)
    h = eng3.how3_run(g, tie=tie, rng=rng, cap=50000)
    c, d = lev3.check3(g, h, refs="T")
    bad = {k: c[k] for k in lev3.CNT if c[k]}
    NM = g.N + g.M
    if obj == "T": s = (1000 * d["T"]) // NM
    elif obj == "Tabs": s = d["T"]
    elif obj == "plat": s = int(1000 * d["platratio"]) * 100 + d["platmax"]
    elif obj == "phi": s = d["phivals"]
    elif obj == "tail": s = d["tailmax"]
    elif obj == "stall": s = d["stalls"]
    else: raise ValueError(obj)
    return s, bad, d

def main():
    obj, seed, iters, Ncap, Mcap = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    tie = sys.argv[6] if len(sys.argv) > 6 else "keep-low"
    tag = "%s_s%d_N%d_M%d_%s" % (obj, seed, Ncap, Mcap, tie)
    os.makedirs("work", exist_ok=True); sf = "work/climb3_%s.json" % tag
    rng = random.Random(seed); vf = open("work/viol3c_%s.jsonl" % tag, "a")
    if os.path.exists(sf):
        S = json.load(open(sf)); G = S["G"]; it0 = S["it"]; rng.seed(seed * 1000003 + it0)
    else:
        if len(sys.argv) > 7: G = eng.load(sys.argv[7]); G.pop("name", None)
        else:
            while True:
                G = gen.shaped(rng, rng.randint(2, max(2, Ncap // 2)), "mix"); G.pop("eorder", None)
                if mut.M_of(G) <= Mcap: break
        it0 = 0
    best, bad, d = score(G, obj, tie, rng); nviol = 0; t0 = time.time()
    for it in range(it0, iters):
        H = G
        for _ in range(rng.randint(1, 3)):
            H2 = mut.mutate(H, rng, Ncap, Mcap)
            if H2 is not None: H = H2
        if H is G or H["N"] > Ncap or mut.M_of(H) > Mcap: continue
        H.pop("eorder", None)
        s, bad, d2 = score(H, obj, tie, rng)
        if bad:
            nviol += 1; vf.write(json.dumps({"G": H, "tie": tie, "c": bad}) + "\n"); vf.flush()
        if s >= best:
            if s > best:
                print("it %d score %d T3 %d N %d M %d platmax %d phivals %d" % (it, s, d2["T"], H["N"], mut.M_of(H), d2["platmax"],
                      d2["phivals"]), flush=True)
            G, best, d = H, s, d2
        if it % 100 == 0:
            json.dump({"G": G, "score": best, "it": it + 1}, open(sf, "w"))
    json.dump({"G": G, "score": best, "it": iters}, open(sf, "w"))
    print("CLIMB3 %s best %d T3 %d N %d M %d platmax %d phivals %d viol %d %.0fs" % (tag, best, d["T"], G["N"], mut.M_of(G),
          d["platmax"], d["phivals"], nviol, time.time() - t0), flush=True)

if __name__ == "__main__":
    main()
