#!/usr/bin/env python3
"""L-RED 63 R229 item 1 (K6, lagging merged copy at h >= 4): box 86's LAG TOWER builder (L-SI lag86.py / gen83.py at claude/l-si
d962efdb, imported READ-ONLY from $SI86 = an extracted `git archive d962efdb experiments/si/box86`) at h = 2..HMAX, all 16 configs
(cpos +-1, wreal 0/1, merge 0/1, cexit C/B), lane lengths L_l = l(l+1)/2 (box 86's 1, 3, 6 continued), a = b = 2, c = 1 (box 86's LT cfg).
Run: R221 own.py (IDEAL-CYC Howard from the genome's start, cap 3000). Own counters (no box 85 / 86 analysis code):
  bit_l(t) = 1 iff mover B_l plays its SET option at t; tog = #changes per bit (B_1 first); CNT = largest k with 0, 1, ..., k-1 a
  subsequence of the bit words read as binary (B_h most significant; box 85's definition; a full counter has CNT = 2^h);
  REARM = #times bit 1 goes 1 -> 0 at a step where a higher bit changes at that step or the one before, then back to 1 (box 85's definition);
  T, C (own census as gate229), gate classes from gate229 (gln must be 0).
Usage: lag229.py HMIN HMAX [OUTDIR]  (writes each genome to OUTDIR if given)"""
import sys, os, json, itertools
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r221"), os.environ["SI86"]]
import own, gate229, lag86
def bits_run(G, names):
    out, V, O, _ = own.run(G, 3000); mv = names["movers"]; labs = names["opts"]
    h = max(int(m[1:]) for m in mv if m[0] == "B" and m[1:].isdigit())
    setk = {}
    for l in range(1, h + 1):
        x = mv.index(f"B{l}"); setk[l] = (x, labs[x].index("SET"))
    words = []
    for (s, vals, tau) in out:
        words.append("".join("1" if s[setk[l][0]] == V[("g", setk[l])] else "0" for l in range(h, 0, -1)))
    tog = [sum(words[t][h - l] != words[t - 1][h - l] for t in range(1, len(words))) for l in range(1, h + 1)]
    k = 0
    for w in words:
        if int(w, 2) == k: k += 1
    rearm = 0; st = 0
    for t in range(1, len(words)):
        p, c = words[t - 1], words[t]
        if st == 0 and p[-1] == "1" and c[-1] == "0" and (p[:-1] != c[:-1] or (t >= 2 and words[t - 2][:-1] != p[:-1])): st = 1
        elif st == 1 and c[-1] == "1": rearm += 1; st = 0
        elif c[-1] == "1": st = 0
    return h, tog, k, rearm, words
if __name__ == "__main__":
    h0, h1 = int(sys.argv[1]), int(sys.argv[2]); od = sys.argv[3] if len(sys.argv) > 3 else None
    print("h cpos wreal merge cexit N+M T C CNT REARM tog np up lam gln mfl", flush=True)
    for h in range(h0, h1 + 1):
        for cpos, wreal, merge, cexit in itertools.product((1, -1), (0, 1), (0, 1), ("C", "B")):
            cfg = dict(h=h, L=[l * (l + 1) // 2 for l in range(1, h + 1)], a=2, b=2, c=1, cpos=cpos, wreal=wreal, merge=merge, cexit=cexit)
            G, nm = lag86.build(cfg)
            hh, tog, cnt, rearm, words = bits_run(G, nm); c = gate229.census(G)
            tag = f"LT{h}_{'p' if cpos > 0 else 'm'}{wreal}{merge}{cexit}"
            if od: json.dump(G, open(os.path.join(od, tag + ".json"), "w")); json.dump(nm, open(os.path.join(od, tag + ".names.json"), "w"))
            print(h, cpos, wreal, merge, cexit, G["N"] + sum(len(o) for o in G["opts"]), c["T"], c["C"], cnt, rearm, ",".join(map(str, tog)),
                  c["np"], c["up"], c["lam"], c["gln"], c["mfl"], flush=True)
