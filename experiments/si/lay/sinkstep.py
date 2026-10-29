#!/usr/bin/env python3
"""L-SI box 27: per-step sink anatomy (lay/wsink.py's sets): W-sinks (v, sigma_t, target, jH, ready), H-sinks (v, sigma_t, target, jW,
sigma_(t+1)), switchers (v, sigma_t, sigma_(t+1), last switch?). Usage: sinkstep.py GAME [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "lwp"))
src = open(os.path.join(HERE, "wsink.py")).read().replace('''            both = [v for v in WS if v in HS]''', '''            both = [v for v in WS if v in HS]
            lastsw = lambda v: all(R[s]["s"][v] == nxt[v] for s in range(t + 1, b + 1))
            print(f"[{a},{b}] t={t} WS", sorted((v, sig[v], B["s"][v], JH[v], ready(v)) for v in WS), "HS", sorted((v, sig[v], B["s"][v], JW[v], nxt[v]) for v in HS),
                  "switch", sorted((v, sig[v], nxt[v], "L" if lastsw(v) else "") for v in Ev if sig[v] != nxt[v]))''')
ns = {"__name__": "sinkstep", "__file__": os.path.join(HERE, "wsink.py")}; exec(compile(src, "wsink.py", "exec"), ns)
from common import rows, load, readstart
g = load(sys.argv[1]); E, R = rows(g, readstart(sys.argv[2]) if len(sys.argv) > 2 else None); ns["_run"](g, R, sys.argv[1])
