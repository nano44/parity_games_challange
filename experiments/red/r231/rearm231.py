#!/usr/bin/env python3
"""L-RED 65 R231 item (a): sweep of the re-arm Xi-target t over every mover of MWR(n) (CW(n) + one option per c_k with Xi-target t, built by
carry231.py logic in-process), own engine. Prints t's name, k, N + M, D_mov, T; marks k != 1.  Usage: rearm231.py MWR.json NAMES.json [PAR]"""
import sys, os, json, subprocess, tempfile
from blk231 import analyse, xi_k
mw, nmf = sys.argv[1], sys.argv[2]; par = sys.argv[3] if len(sys.argv) > 3 else "0"; nm = json.load(open(nmf)); rn = {v: k for k, v in nm.items()}
N0 = json.load(open(mw))["N"]; here = os.path.dirname(os.path.abspath(__file__)); tmp = tempfile.mkdtemp()
def build(t):
    env = dict(os.environ); f = os.path.join(tmp, "g.json")
    if t is not None: env["CW_REARM"] = str(t)
    else: env.pop("CW_REARM", None)
    subprocess.run([sys.executable, os.path.join(here, "carry231.py"), mw, nmf, f, par], env=env, check=True); return json.load(open(f))
for t in [None] + list(range(N0)):
    G = build(t); k = xi_k(G); A = analyse(G)
    dm = max(len(set(A["cls"][x])) for x in range(G["N"]))
    print(f"t {rn.get(t, t)} k {k} N+M {G['N'] + A['M']} D_mov {dm} T {A['T']}" + ("" if k == 1 else "  (k != 1)"), flush=True)
