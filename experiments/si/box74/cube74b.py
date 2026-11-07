#!/usr/bin/env python3
"""L-SI box 74: restart-safe adaptive cube driver, version b (cube74.py + cheaper split order + continuous worker pool).
Split order: the key bits c(l, k) (levels 1..m-1), then the start state s_0(z) of run "a" (z = 0..2m-1), three binary variables per
split (8 children = all sign patterns), then the Xi-targets of the upper options (top movers first), one option per split (all 2m values).
Every split takes ALL values of the variables it fixes, so the leaves partition the search space: the answer is UNCONDITIONAL (no
symmetry breaking). frame.py env XCUBE carries the cube ("c<l>.<k>:b", "S<z>:b", "o:t"). State per cube in cubes/<TAG>/<id>.res or
<id>.split; a relaunch skips finished / split cubes; a killed cube restarts from scratch (loses <= TLIM).
Answer: UNSAT iff every leaf is UNSAT; SAT as soon as one leaf is SAT (model in <id>.log; the driver stops).
Usage: cube74b.py TAG m MODE T [T2]    (frame env: K, PRE, ...; driver env PAR (default 3), TLIM (default 1500 s))
       cube74b.py TAG summary"""
import os, sys, time, subprocess, itertools
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED
HERE = os.path.dirname(os.path.abspath(__file__)); FRAME = os.path.join(HERE, "..", "box70", "frame.py")
TAG = sys.argv[1]; DIR = os.path.join(HERE, "cubes", TAG); os.makedirs(DIR, exist_ok=True)
def kids_of(c):
    f = os.path.join(DIR, c + ".split"); return open(f).read().split() if os.path.exists(f) else None
def leaves():
    out, st = [], ["r"]
    while st:
        c = st.pop(); k = kids_of(c)
        if k: st += k
        else: out.append(c)
    return out
def res(c):
    f = os.path.join(DIR, c + ".res"); return open(f).read().strip() if os.path.exists(f) else None
if sys.argv[2] == "summary":
    L = leaves(); r = [res(c) for c in L]
    print(TAG, "leaves", len(L), "UNSAT", r.count("UNSAT"), "SAT", r.count("SAT"), "open", r.count(None)); sys.exit(0)
m, ARGS = int(sys.argv[2]), sys.argv[2:]
U = 2 * m
BIN = ["c%d.%d" % (l, k) for l in range(1, m) for k in (0, 1)] + ["S%d" % z for z in range(U)]
XO = [o for z in reversed(range(U)) for o in (2 * z, 2 * z + 1)]
DOM = {o: [-1] + [y for y in range(U) if y != o // 2] for o in range(2 * U)}
TLIM = float(os.environ.get("TLIM", "1500")); PAR = int(os.environ.get("PAR", "3"))
def parts(c): return [] if c == "r" else c.split("+")[1:]
def split(c):
    p = parts(c); nb = sum(1 for x in p if x[0] in "cS")
    if nb < len(BIN):
        vs = BIN[nb:nb + 3]; return ["%s+%s" % (c, "+".join("%s:%d" % (v, b) for v, b in zip(vs, bits))) for bits in itertools.product((0, 1), repeat=len(vs))]
    o = XO[len(p) - nb]; return ["%s+%d:%d" % (c, o, t) for t in DOM[o]]
def solve(c):
    xc = ",".join(parts(c)); logf = os.path.join(DIR, c + ".log"); t0 = time.time()
    try:
        with open(logf, "w") as lf:
            subprocess.run([sys.executable, FRAME] + ARGS, env=dict(os.environ, XCUBE=xc), stdout=lf, stderr=subprocess.STDOUT, timeout=TLIM)
    except subprocess.TimeoutExpired:
        open(os.path.join(DIR, c + ".split"), "w").write(" ".join(split(c)) + "\n"); return c, "SPLIT", time.time() - t0
    txt = open(logf).read(); r = "SAT" if "-> SAT" in txt else ("UNSAT" if "-> UNSAT" in txt else "ERROR")
    if r != "ERROR": open(os.path.join(DIR, c + ".res"), "w").write(r + "\n")
    return c, r, time.time() - t0
running = {}
with ThreadPoolExecutor(PAR) as ex:
    while True:
        L = leaves()
        if any(res(c) == "SAT" for c in L): print("ANSWER SAT", flush=True); break
        todo = [c for c in L if res(c) is None and c not in running.values()]
        if not todo and not running: print("ANSWER UNSAT (all %d leaves UNSAT)" % len(L), flush=True); break
        while todo and len(running) < PAR:
            c = todo.pop(0); running[ex.submit(solve, c)] = c          # breadth-first: shallow cubes first
        done, _ = wait(list(running), return_when=FIRST_COMPLETED)
        for f in done:
            c, r, dt = f.result(); del running[f]
            print(time.strftime("%H:%M:%S"), c, r, "%.0fs" % dt, flush=True)
            if r == "ERROR": raise SystemExit("cube %s ERROR (see log)" % c)
