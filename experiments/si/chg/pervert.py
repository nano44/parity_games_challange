#!/usr/bin/env python3
"""L-SI box 28 (docs/si/N5-CHG-box28.md §8): per-vertex switch counts per FALLBACK-FREE RUN (CONJECTURE SW-PER-VERTEX, Lead 10:48Z).
For each run [s, e] (runlin/trace.py runs: (lambda_Xi, tau) constant, no fallback inside) and each Even v: SW(v) = switches of v in the
run, RISE(v) = transitions t with Xi_(t+1)(v) != Xi_t(v) (strict rises, R15 (a)), DIST(v) = distinct values Xi_t(sigma_t v) over the run.
Counters:  SWRISE_V  a switch of v at t with Xi_(t+1)(v) = Xi_t(v) (Lemma SW-RISE's exception: R15 (b) length-only switches at cycle
           nodes; FLATCN counts those where v is its own cycle node, which R15 (b) allows)
           PERV_V    a run in which some Even vertex switches more than n times (CONJECTURE SW-PER-VERTEX in its O(n) form, constant 1)
           RISEN_V   a run in which some vertex's Xi rises more than n times
Prints the top runs by max SW(v) / n. Usage: pervert.py --list FILE | --one GAME [START]   (START=1 reads list column 2)"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "lwp"))
from suffix import rows, load, readstart
from trace import runs
C = Counter(); EX = []; TOP = []

def _run(g, R, name):
    n = g.n; Ev = [v for v in range(n) if g.owner[v] == 0]
    for s, e, i, j in runs(R):
        if e <= s: continue
        C["runs"] += 1; sw = Counter(); ri = Counter(); dv = {v: set() for v in Ev}
        for t in range(s, e):
            A, B = R[t], R[t + 1]
            for v in range(n):
                if A["vs"][v] != B["vs"][v]: ri[v] += 1
            for v in Ev:
                dv[v].add(A["vs"][A["s"][v]])
                if A["s"][v] != B["s"][v]:
                    sw[v] += 1
                    if A["vs"][v] == B["vs"][v]:
                        cn = A["vs"][v][0] == v
                        C["FLATCN" if cn else "SWRISE_V"] += 1
                        if not cn: EX.append(("SWRISE", name, s, e, t, v))
        if not sw: continue
        m = max(sw.values()); r = max(ri.values()) if ri else 0; dmax = max(len(x) for x in dv.values())
        if m > n: C["PERV_V"] += 1; EX.append(("PERV", name, s, e, m, n))
        if r > n: C["RISEN_V"] += 1; EX.append(("RISEN", name, s, e, r, n))
        TOP.append((round(m / n, 3), name, s, e, e - s, m, r, dmax, n))

def run(g, name, start=None):
    E, R = rows(g, start, cap=20000); _run(g, R, name)

def main():
    a = sys.argv[1:]
    if a[0] == "--one": run(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        for line in open(a[1]):
            p = line.split() if line.strip() and not line.startswith("#") else None
            if p:
                f = os.path.join(ROOT, p[0]) if os.path.exists(os.path.join(ROOT, p[0])) else os.path.join(ROOT, "experiments", p[0])
                s = None
                if len(p) > 1 and os.environ.get("START") == "1":
                    s = os.path.join(ROOT, p[1]) if os.path.exists(os.path.join(ROOT, p[1])) else os.path.join(ROOT, "experiments", p[1])
                try: run(load(f), p[0], readstart(s) if s else None)
                except Exception: C["SKIPPED_input"] += 1
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    print("columns: maxSW/n, game, s, e, run length, max SW(v), max RISE(v), max DIST(v), n")
    for z in sorted(TOP, reverse=True)[:8]: print("TOP", z)
    for z in EX[:8]: print("EXAMPLE", z)
    for k in ("SWRISE", "PERV", "RISEN"): print(k, "PASS" if k + "_V" not in C else "FAIL")

if __name__ == "__main__":
    main()
