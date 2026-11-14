import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dyn2, sys
tabs = [tuple(int(w, 16) for w in l.split()) for l in open("tables.txt")]
want = tuple(map(int, sys.argv[1:3])); shown = 0
def st(s): return "".join(str((s >> z) & 1) for z in range(4))
for tab in tabs:
    for cc in range(4):
        c = {(1, 0): cc & 1, (1, 1): cc >> 1}
        T0, T1, pq = dyn2.analyse(tab, c)
        for b in (0, 1):
            if (T0[b], T0[1 - b]) == want and shown < 2:
                shown += 1
                print("tab", " ".join("%04x" % w for w in tab), "c", cc, "pre bit", b, "T0", T0, "T1", T1)
                for s in range(16):
                    r = dyn2.run(tab, c, s, b)
                    if len(r) - 1 == T0[b]:
                        print(" max b-run", [st(x) for x in r], "then other-bit runs from each:", [len(dyn2.run(tab, c, x, 1 - b)) - 1 for x in r])
                for s in range(16):
                    r = dyn2.run(tab, c, s, 1 - b)
                    if len(r) - 1 == T0[1 - b]: print(" max other-run", [st(x) for x in r])
                # C table per state
                print(" C(z,s) rows z=A1,B1,A2,B2 over s=0..15 (s bit z):")
                for z in range(4): print("  ", "".join(str((tab[z] >> s) & 1) for s in range(16)))
