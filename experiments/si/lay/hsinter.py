#!/usr/bin/env python3
"""L-SI box 27: per REL segment, the most INTERMEDIATE switches (to a non-target, sigma_(t+1)(v) != sigma_b(v)) made by one vertex at
steps where it is an H-sink (lay/wsink.py's sets); and how many of those steps are deadlock steps (no last switch). The SEG-COUNT charging
(note §6) fails only if one H-sink makes >= 2 intermediate switches at deadlock steps. Usage: hsinter.py --list FILE | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "lwp"))
src = open(os.path.join(HERE, "wsink.py")).read().replace('''            both = [v for v in WS if v in HS]''', '''            both = [v for v in WS if v in HS]
            dead = not any(R[t]["s"][v] != nxt[v] and all(R[s]["s"][v] == nxt[v] for s in range(t + 1, b + 1)) for v in Ev)
            for v in HS:
                if sig[v] != nxt[v] != B["s"][v]: HI[(name, a, b, v)] += 1; HD[(name, a, b, v)] += dead''')
ns = {"__name__": "hsinter", "__file__": os.path.join(HERE, "wsink.py")}; exec(compile(src, "wsink.py", "exec"), ns)
from common import rows, load, readstart
HI, HD = Counter(), Counter(); ns["HI"], ns["HD"] = HI, HD
def run(g, name, start=None): E, R = rows(g, start); ns["_run"](g, R, name)
a = sys.argv[1:]
if a[0] == "--one": run(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
else:
    ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
    for line in open(a[1]):
        p = line.split() if line.strip() and not line.startswith("#") else None
        if p: run(load(os.path.join(ROOT, p[0])), p[0], readstart(os.path.join(ROOT, p[1])) if len(p) > 1 and os.environ.get("START") == "1" else None)
print("H-sink intermediate switches per (segment, vertex): histogram", sorted(Counter(HI.values()).items()), "| at deadlock steps:", sorted(Counter(HD.values()).items()))
for k, c in HI.most_common(5): print("TOP", k, c, "deadlock", HD[k])
