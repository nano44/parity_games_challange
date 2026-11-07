#!/usr/bin/env python3
"""L-COMP box 28 (copy of box27/acube.py; changes: ROOTS env = list of root cube ids (default: the 8 PAIR-SWAP roots of d 4),
state in box28/cubes/TAG, cnf.py from box27, SAT stop does not pkill). Box 27 text follows: adaptive, restart-safe cube driver for cnf.py ("T >= L" queries).
Roots: SYM=1 (s_0(u_0) = s_0(v_0) = 0, sound relabelling, ENCODING.md §1) x every assignment of s_0 of movers 2..2d-1.
Each cube is solved under a wall-clock limit TLIM (s, default 1200); on timeout it is SPLIT into children by the Xi-target of the
next option in a fixed order (options (x, k) in mover order, all values of its Xi-target domain: exit or each allowed mover), so
children partition the parent. State per cube in cubes2/TAG/: <id>.res (RESULT line, final) or <id>.split (children made).
A relaunch skips finished / split cubes (idempotent); a killed cube restarts from scratch (loses <= TLIM).
Answer: UNSAT iff every leaf is UNSAT; SAT as soon as one leaf is SAT (model -> cubes2/TAG/<id>.json, then STOP on SAT).
Usage: acube.py TAG d L            env W, P (as cnf.py), PAR (workers, default 4), TLIM
       acube.py TAG d L summary"""
import os, sys, json, time, subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
HERE = os.path.dirname(os.path.abspath(__file__))
B27 = os.path.join(HERE, "..", "box27"); sys.path.insert(0, B27)
TAG, d, L = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cubes", TAG); os.makedirs(DIR, exist_ok=True)
TLIM = float(os.environ.get("TLIM", "1200")); PAR = int(os.environ.get("PAR", "4"))
P = [int(v) for v in os.environ["P"].split(",")] if os.environ.get("P") else None
W = os.environ.get("W", "R")
ROOTS = [int(v) for v in os.environ.get("ROOTS", "0,2,8,10,32,34,40,42").split(",")]
os.environ["SYM"] = "1"; os.environ.pop("CUBE", None)
import cnf
_C, _I = cnf.build(d, 1, P, W)          # only for the Xi-target domain sizes (option order = cnf.py opts order)
def ndom(j): return len(_I["Xv"][_I["opts"][j]])

def parse(cid):
    """cid = 'r' or 'r.c1.c2...' -> (root int, child indices)."""
    parts = cid.split("."); return int(parts[0]), [int(c) for c in parts[1:]]

def solve(cid):
    """one cube = one cnf.py subprocess (killed at TLIM); fresh CNF + the cube's start bits and Xi-target choices as unit clauses."""
    r, ch = parse(cid)
    env = dict(os.environ, SYM="1", CUBE=",".join(f"{x}:{(r >> i) & 1}" for i, x in enumerate(range(2, 2 * d))),
               XCUBE=",".join(f"{j}:{c}" for j, c in enumerate(ch)), W=W)
    if P: env["P"] = ",".join(map(str, P))
    logf = os.path.join(DIR, cid + ".log"); t0 = time.time()
    try:
        with open(logf, "w") as lf:
            subprocess.run([sys.executable, os.path.join(B27, "cnf.py"), str(d), str(L), os.path.join(DIR, cid + ".json")],
                           env=env, stdout=lf, stderr=subprocess.STDOUT, timeout=TLIM)
    except subprocess.TimeoutExpired:
        dt = time.time() - t0; n = ndom(len(ch))
        kids = [f"{cid}.{c}" for c in range(n)]
        open(os.path.join(DIR, cid + ".split.tmp"), "w").write(f"timeout {dt:.0f} s; children {' '.join(kids)}\n")
        os.replace(os.path.join(DIR, cid + ".split.tmp"), os.path.join(DIR, cid + ".split")); return cid, "SPLIT", dt
    dt = time.time() - t0; res = [l for l in open(logf) if l.startswith("RESULT")]
    if not res: return cid, "ERROR", dt
    open(os.path.join(DIR, cid + ".res.tmp"), "w").write(res[0]); os.replace(os.path.join(DIR, cid + ".res.tmp"), os.path.join(DIR, cid + ".res"))
    return cid, "SAT" if ": SAT" in res[0] else "UNSAT", dt

def leaves():
    out = []; stack = [str(r) for r in ROOTS]
    while stack:
        c = stack.pop()
        if os.path.exists(os.path.join(DIR, c + ".split")):
            kids = open(os.path.join(DIR, c + ".split")).read().split("children ")[1].split(); stack.extend(kids)
        else: out.append(c)
    return out

def summary():
    lv = leaves(); st = {"SAT": 0, "UNSAT": 0, "open": 0}
    for c in lv:
        f = os.path.join(DIR, c + ".res")
        if os.path.exists(f): st["SAT" if ": SAT" in open(f).read() else "UNSAT"] += 1
        else: st["open"] += 1
    nsplit = sum(1 for f in os.listdir(DIR) if f.endswith(".split"))
    ans = "SAT" if st["SAT"] else ("UNSAT" if st["open"] == 0 else "OPEN")
    print(f"TAG {TAG} d {d} L {L} P {P} W {W}: leaves {len(lv)} SAT {st['SAT']} UNSAT {st['UNSAT']} open {st['open']} splits {nsplit} -> {ans}", flush=True)
    return ans

if __name__ == "__main__":
    if len(sys.argv) > 4 and sys.argv[4] == "summary": summary(); sys.exit(0)
    while summary() == "OPEN":
        todo = [c for c in leaves() if not os.path.exists(os.path.join(DIR, c + ".res"))]
        sat = False
        with ThreadPoolExecutor(PAR) as ex:
            futs = [ex.submit(solve, c) for c in todo]
            for f in as_completed(futs):
                cid, res, dt = f.result(); print(f"{time.strftime('%H:%M:%S', time.gmtime())} {cid} {res} {dt:.0f} s", flush=True)
                if res == "ERROR": print("ERROR in cube", cid, "(see its .log); stopping", flush=True); os._exit(2)
                if res == "SAT": sat = True; [g.cancel() for g in futs]; break
        if sat:
            summary(); break
