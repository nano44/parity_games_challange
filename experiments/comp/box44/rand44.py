#!/usr/bin/env python3
"""L-COMP box 44 item 2: box 209's counters (lev44.measure, my builder + my engine) on genomes L-NEW's data did not draw:
  rand SEED COUNT NMMAX PX : random genomes by this lane's law (box43/rand43.rgen: N + M <= NMMAX, Ξ-target X with probability PX,
                             else a uniform mover; every Ξ-feedback number);
  mut SEED COUNT BASE.json : mutants of a frozen genome (1 to 6 moves of box39/mut39.mutate).
One line per genome is appended to OUT (resumable: the generator is replayed and finished indices are skipped).
Usage: rand44.py rand SEED COUNT NMMAX PX OUT | rand44.py mut SEED COUNT BASE.json OUT   (env BREF, LV44_CTRL as lev44)"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "box43"), os.path.join(H, "..", "box39")]
import lev44

if __name__ == "__main__":
    a = sys.argv[1:]; r = random.Random(int(a[1])); cnt = int(a[2]); out = a[-1]
    have = {l.split(" N ")[0] for l in open(out)} if os.path.exists(out) else set()
    if a[0] == "rand":
        import rand43
        gen = lambda: rand43.rgen(r, int(a[3]), float(a[4])); pre = "rand_s%s_nm%s_px%s" % (a[1], a[3], a[4])
    else:
        import mut39
        G0 = json.load(open(a[3])); G0 = mut39.canon(G0.get("genome", G0)); pre = "mut_s%s_%s" % (a[1], os.path.basename(a[3]).replace(".json", ""))
        def gen():
            G = G0
            for _ in range(r.randint(1, 6)):
                G2 = mut39.mutate(G, r)
                if G2 is not None: G = G2
            return G
    for i in range(cnt):
        G = gen(); tag = "%s_%d" % (pre, i)
        if tag in have: continue
        c, d, first, B = lev44.measure(G)
        with open(out, "a") as f:
            f.write(lev44.line(tag, c, d, B) + "".join(" | FIRST %s %s" % (k, first[k]) for k in lev44.KEYS if k in first) + ((" | GENOME " + json.dumps(G, sort_keys=True)) if first else "") + "\n")
