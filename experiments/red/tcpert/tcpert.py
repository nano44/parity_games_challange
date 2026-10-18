#!/usr/bin/env python3
"""L-RED box 11 (produced on Opus 5.5): side check for the Lead (L-ALG target TC-6): uniform label-based perturbations of
Oink's Two Counters generator tc(N) (tools/oink/build/tc, pinned 8fbf0a7), solved by pinned Oink
`--dtl --no-single --no-wcwc --no-loops -v`; reports iterations per N and whether the solution verified.
A perturbation is a rule on labels "<Player>-<i>-<Role>[-<j>]": flip owners of a class, add edges between classes with an
index relation (i same / i+1), or shift a class's priority. Usage: tcpert.py RNGSEED TRIES OUTDIR | tcpert.py tcL N OUT.pg"""
import sys, os, random, re, subprocess, itertools
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."); T = os.path.join(ROOT, "tools", "oink", "build")
def gen(N):
    txt = subprocess.run([os.path.join(T, "tc"), str(N)], capture_output=True, text=True).stdout
    V = []
    for line in txt.splitlines()[1:]:
        m = re.match(r'(\d+) (\d+) ([01]) ([\d,]+) "([^"]*)"', line)
        if m: V.append([int(m[2]), int(m[3]), [int(x) for x in m[4].split(",")], m[5]])
    return V
def lab(s):
    p = s.split("-"); return (p[0], int(p[1]), p[2], int(p[3]) if len(p) > 3 else None)
ROLES = ["Z", "B", "A", "S", "T", "L", "H"]; PL = ["Even", "Odd"]
def apply(V, rule):
    V = [[a, b, list(c), d] for a, b, c, d in V]; L = [lab(v[3]) for v in V]
    for r in rule:
        if r[0] == "flip":
            for k, l in enumerate(L):
                if l[0] == r[1] and l[2] == r[2]: V[k][1] ^= 1
        elif r[0] == "edge":
            _, p1, r1, p2, r2, di = r
            for k, l in enumerate(L):
                if l[0] != p1 or l[2] != r1: continue
                for k2, l2 in enumerate(L):
                    if l2[0] == p2 and l2[2] == r2 and l2[1] == l[1] + di and (l[3] is None or l2[3] is None or l2[3] == l[3]) and k2 not in V[k][2]:
                        V[k][2].append(k2)
        elif r[0] == "prio":
            for k, l in enumerate(L):
                if l[0] == r[1] and l[2] == r[2]: V[k][0] = max(0, V[k][0] + r[3])
    return V
def solve(V, path):
    with open(path, "w") as f:
        f.write(f"parity {len(V)-1};\n" + "".join(f'{k} {v[0]} {v[1]} {",".join(map(str, v[2]))} "{v[3]}";\n' for k, v in enumerate(V)))
    o = subprocess.run([os.path.join(T, "oink"), "--dtl", "--no-single", "--no-wcwc", "--no-loops", "-v", path, "/dev/null"], capture_output=True, text=True, timeout=120).stdout + ""
    o = o + subprocess.run(["true"], capture_output=True, text=True).stdout
    m = re.search(r"solved in (\d+) iterations", o); ok = "solution verified" in o
    return (int(m[1]) if m else -1), ok
def randrule(rng):
    k = rng.randint(1, 2); rule = []
    for _ in range(k):
        t = rng.choice(["flip", "edge", "edge", "prio"])
        if t == "flip": rule.append(("flip", rng.choice(PL), rng.choice(ROLES)))
        elif t == "edge": rule.append(("edge", rng.choice(PL), rng.choice(ROLES), rng.choice(PL), rng.choice(ROLES), rng.choice([0, 1, -1])))
        else: rule.append(("prio", rng.choice(PL), rng.choice(ROLES), rng.choice([-2, 2])))
    return tuple(rule)
TCL = (("edge", "Even", "L", "Even", "H", -1),)   # tcL(N): every Even-i-L gets an edge to Even-(i-1)-H (R40)
def write_tcl(N, path):
    V = apply(gen(N), TCL)
    with open(path, "w") as f:
        f.write(f"parity {len(V)-1};\n" + "".join(f'{k} {v[0]} {v[1]} {",".join(map(str, v[2]))} "{v[3]}";\n' for k, v in enumerate(V)))
if __name__ == "__main__" and sys.argv[1] == "tcL":   # tcpert.py tcL N OUT.pg
    write_tcl(int(sys.argv[2]), sys.argv[3]); sys.exit(0)
if __name__ == "__main__":
    seed, tries, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]; rng = random.Random(seed); os.makedirs(out, exist_ok=True)
    base = {N: gen(N) for N in (3, 4, 5, 6)}; seen = set(); best = 0
    for it in range(tries):
        rule = randrule(rng)
        if rule in seen: continue
        seen.add(rule); res = []
        for N in (3, 4, 5, 6):
            try: res.append(solve(apply(base[N], rule), os.path.join(out, f"cur{seed}.pg")))
            except subprocess.TimeoutExpired: res.append((-2, False))
        its = [r[0] for r in res]; bad = [r for r in res if not r[1]]
        if bad: print("NOT VERIFIED", rule, res, flush=True); continue
        grow = its[3] - its[0]
        if grow > best or (its[3] > 8 and grow > 0):
            best = max(best, grow); print(it, rule, its, flush=True)
    print("done best growth", best)
