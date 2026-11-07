import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# L-SI box 73: m = 2 exact: in one-flip runs, how many level-1 movers move in BOTH segments (re-armed), by run length
import dyn2
tabs = [tuple(int(w, 16) for w in l.split()) for l in open("tables.txt")]
agg = {}
for tab in tabs:
    for cc in range(4):
        c = {(1, 0): cc & 1, (1, 1): cc >> 1}
        for b in (0, 1):
            for s in range(16):
                seq = dyn2.run(tab, c, s, b)
                for p in range(1, len(seq)):
                    post = dyn2.run(tab, c, seq[p], 1 - b)
                    if len(post) == 1: continue
                    m1 = seq[0] ^ seq[p]; m2 = post[0] ^ post[-1]   # level-1 movers move at most once per segment
                    re = bin(m1 & m2 & 3).count("1"); T = p + len(post) - 1
                    agg[(T, re)] = agg.get((T, re), 0) + 1
for k in sorted(agg): print("T %d rearmed-level1 %d : %d runs" % (k + (agg[k],)))
