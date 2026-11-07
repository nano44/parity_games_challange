#!/usr/bin/env python3
"""L-SI box 74: restart-safe adaptive cube driver for a box 70 frame query (pattern of L-COMP box 27 acube.py; own code).
A cube fixes the Xi-targets of some upper options (frame.py env XCUBE "o:t,..."). A cube is solved by one frame.py subprocess under a
wall-clock limit TLIM (s, default 1500); on timeout it is SPLIT by the Xi-target of the next option in ORDER (all 2m values: X or any
other upper mover; frame.py's exactly-one clause makes the children a partition of the parent). No symmetry breaking: the answer is
UNCONDITIONAL. State per cube in cubes/<TAG>/<id>.res (final RESULT line) or <id>.split; a relaunch skips finished/split cubes; a
killed cube restarts from scratch (loses <= TLIM). Answer: UNSAT iff every leaf is UNSAT; SAT as soon as one leaf is SAT (model in
<id>.log; the driver then stops).
Usage: cube74.py TAG m MODE T [T2]      (env as frame.py: K, PRE, ...; driver env PAR (default 3), TLIM)
       cube74.py TAG summary"""
import os, sys, time, subprocess
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__)); FRAME = os.path.join(HERE, "..", "box70", "frame.py")
TAG = sys.argv[1]; DIR = os.path.join(HERE, "cubes", TAG); os.makedirs(DIR, exist_ok=True)
def leaves():
    out, st = [], ["r"]
    while st:
        c = st.pop()
        if os.path.exists(os.path.join(DIR, c + ".split")): st += open(os.path.join(DIR, c + ".split")).read().split()
        else: out.append(c)
    return out
def res(c):
    f = os.path.join(DIR, c + ".res"); return open(f).read().strip() if os.path.exists(f) else None
if sys.argv[2] == "summary":
    L = leaves(); r = [res(c) for c in L]
    print(TAG, "leaves", len(L), "UNSAT", r.count("UNSAT"), "SAT", r.count("SAT"), "open", r.count(None)); sys.exit(0)
m, ARGS = int(sys.argv[2]), sys.argv[2:]
U = 2 * m; ORDER = [o for z in reversed(range(U)) for o in (2 * z, 2 * z + 1)]   # top movers' options first
DOM = {o: [-1] + [y for y in range(U) if y != o // 2] for o in range(2 * U)}
TLIM = float(os.environ.get("TLIM", "1500")); PAR = int(os.environ.get("PAR", "3"))
def fixes(c): return [] if c == "r" else [tuple(map(int, p.split(":"))) for p in c.split(".")[1:]]
def solve(c):
    xc = ",".join("%d:%d" % ot for ot in fixes(c)); logf = os.path.join(DIR, c + ".log"); t0 = time.time()
    try:
        with open(logf, "w") as lf:
            subprocess.run([sys.executable, FRAME] + ARGS, env=dict(os.environ, XCUBE=xc), stdout=lf, stderr=subprocess.STDOUT, timeout=TLIM)
    except subprocess.TimeoutExpired:
        d = len(fixes(c)); o = ORDER[d]
        kids = ["%s.%d:%d" % (c, o, t) for t in DOM[o]]
        open(os.path.join(DIR, c + ".split"), "w").write(" ".join(kids) + "\n"); return c, "SPLIT", time.time() - t0
    txt = open(logf).read(); r = "SAT" if "-> SAT" in txt else ("UNSAT" if "-> UNSAT" in txt else "ERROR")
    if r != "ERROR": open(os.path.join(DIR, c + ".res"), "w").write(r + "\n")
    return c, r, time.time() - t0
while True:
    todo = [c for c in leaves() if res(c) is None]
    if any(res(c) == "SAT" for c in leaves()): print("ANSWER SAT"); break
    if not todo: print("ANSWER UNSAT (all %d leaves UNSAT)" % len(leaves())); break
    with ThreadPoolExecutor(PAR) as ex:
        for c, r, dt in ex.map(solve, todo[:PAR]):
            print(time.strftime("%H:%M:%S"), c, r, "%.0fs" % dt, flush=True)
            if r == "ERROR": raise SystemExit("cube %s ERROR (see log)" % c)
