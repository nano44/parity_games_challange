# L-SI box 73: an m = 2 frame system whose maximal flip-free beta-run (a steps) is followed after the flip by a maximal (not beta)-run
# (b steps): no junction loss. Usage: fullfull2.py a b
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import dyn2
a, b = map(int, sys.argv[1:3])
def st(s): return "".join(str((s >> z) & 1) for z in range(4))
for l in open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "tables.txt")):
    tab = tuple(int(w, 16) for w in l.split())
    for cc in range(4):
        c = {(1, 0): cc & 1, (1, 1): cc >> 1}; T0, T1, pq = dyn2.analyse(tab, c)
        for be in (0, 1):
            if (T0[be], T0[1 - be]) != (a, b): continue
            for s in range(16):
                r = dyn2.run(tab, c, s, be)
                if len(r) - 1 == a and len(dyn2.run(tab, c, r[-1], 1 - be)) - 1 == b:
                    print("table", l.strip(), "c_1(0), c_1(1) =", cc & 1, cc >> 1, "beta", be, "pre", [st(x) for x in r], "post", [st(x) for x in dyn2.run(tab, c, r[-1], 1 - be)])
                    sys.exit(0)
