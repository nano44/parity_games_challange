import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dyn2
tabs = [tuple(int(w, 16) for w in l.split()) for l in open("tables.txt")]
def b1(c, s, bb):
    a, b = s & 1, (s >> 1) & 1
    return (1 - bb if a else bb) if a != b else c[(1, a)]
agg = {}
for tab in tabs:
    for cc in range(4):
        c = {(1, 0): cc & 1, (1, 1): cc >> 1}
        for b in (0, 1):
            for s in range(16):
                seq = dyn2.run(tab, c, s, b)
                for p in range(len(seq)):
                    post = dyn2.run(tab, c, seq[p], 1 - b)
                    full = seq[:p + 1] + post[1:]; bits = [b] * p + [1 - b] * (len(post) - 1)
                    L1 = sum(bin((full[i] ^ full[i + 1]) & 3).count("1") for i in range(len(full) - 1))
                    L2 = sum(bin((full[i] ^ full[i + 1]) & 12).count("1") for i in range(len(full) - 1))
                    only2 = sum(1 for i in range(len(full) - 1) if (full[i] ^ full[i + 1]) & 3 == 0)
                    keys = [b1(c, full[i + 1], bits[i]) for i in range(len(full) - 1)]
                    kch = sum(1 for i in range(len(keys) - 1) if keys[i] != keys[i + 1])
                    k = (p > 0 and len(post) > 1, L1, kch); T = len(full) - 1
                    agg[k] = max(agg.get(k, 0), T)
for k in sorted(agg): print("flip-used %d L1moves %d b1changes %d : max T %d" % (k + (agg[k],)))
