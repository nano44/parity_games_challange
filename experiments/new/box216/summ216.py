#!/usr/bin/env python3
"""Box 216 summary (L-NEW successor 76): one line per output file of out/: genomes, timeouts, the sum of every must-0 counter (must0_sum),
the per-counter sums of the must-0 counters, and the named descriptive maxima. Must-0 sets: xflip216 (xmove xflip xflipd jmove jfmin),
gate216 (the MUST0 block), split216 (playfail kindfail hwfail gtfail trfail dnfail rhfail rh2fail spfail rw1fail wlamfail), qt3_196
(cnlow locfail ties bonly k2fail upfail emon nonstd). HOW items (f5best, dom, nohoward, wfail, Tfail) are reported, never must-0."""
import os, re, collections
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, "out")
M0 = {"xflip": "xmove xflip xflipd jmove jfmin", "gate": "f1 strict imp grfail gr2fail efp npshape stepb par pexp ssimp loud",
      "split": "playfail kindfail hwfail gtfail trfail dnfail rhfail rh2fail spfail rw1fail wlamfail",
      "qt3": "cnlow locfail ties bonly k2fail upfail emon nonstd"}
DESC = {"xflip": "T Tk jfmax", "gate": "Tk Wq", "split": "T3", "qt3": "T3 W"}
SUMD = {"xflip": "moves xfsum kfsum xfmsum jfsum mvkey", "gate": "f5best dom Q sumD flips couples", "split": "", "qt3": "nohoward wfail Tfail"}
def kv(line): return {k: int(v) for k, v in re.findall(r"\b([A-Za-z_0-9]+) (-?\d+)\b", line)}
for fn in sorted(os.listdir(OUT)):
    if not fn.endswith(".out"): continue
    kind = next((k for k in M0 if fn.startswith(k)), None)
    if kind is None: continue
    L = open(os.path.join(OUT, fn)).read().splitlines(); g = to = 0; s = collections.Counter(); mx = collections.Counter(); done = "DONE" in L
    for line in L:
        if line.startswith("TIMEOUT"): to += 1; continue
        if line == "DONE" or not line.strip(): continue
        d = kv(line.replace("max T3", "T3")); g += 1
        for k in M0[kind].split() + SUMD[kind].split(): s[k] += d.get(k, 0)
        for k in DESC[kind].split(): mx[k] = max(mx[k], d.get(k, 0))
    print(fn, "done" if done else "PARTIAL", "genomes", g, "timeouts", to, "must0_sum", sum(s[k] for k in M0[kind].split()),
          " ".join("%s %d" % (k, s[k]) for k in M0[kind].split()), "|", " ".join("%s %d" % (k, s[k]) for k in SUMD[kind].split()),
          "|", " ".join("max_%s %d" % (k, mx[k]) for k in DESC[kind].split()))
