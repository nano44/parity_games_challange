#!/usr/bin/env python3
"""L-RED R150: hill-climb from a SEED game (+ start) toward a CASC-EDGE kill ((returns of X per root)/deg X > 1) and a LEVEL-ONCE kill
(returns of one edge per (root, depth) >= 2), scored by L-NEW's retcause.py PERROOT line (l-new 457e41fe, path in env RETCAUSE) in a
subprocess. Score = (ratio, level, returns). Mutations: redirect / add / drop an edge, swap two priorities, flip an owner, change a start
choice; n fixed. Writes the best to OUT.pg / OUT.start.  Env SCORE=ret scores (max returns of one Even X per root, ratio, returns) instead; env PAD=k appends k spare vertices (Even, self-loop,
priority 0) that mutations can wire in.
Usage: RETCAUSE=... ovclimb.py SEED.pg SEED.start RNG STEPS OUT"""
import sys, os, random, subprocess, re, tempfile
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "xcn"))
import xcn
pg = xcn.pg; n5b = xcn.n5b
g0 = pg.read(sys.argv[1]); s0, t0 = n5b.read_start(sys.argv[2], g0); rng = random.Random(int(sys.argv[3])); steps = int(sys.argv[4]); out = sys.argv[5]
PAD = int(os.environ.get('PAD', '0')); n = g0.n + PAD; tmp = tempfile.mkdtemp(); RC = os.environ["RETCAUSE"]
def write(st, p):
    pr, ow, succ, st0 = st
    with open(p + ".pg", "w") as f:
        f.write(f"parity {n - 1};\n")
        for v in range(n): f.write(f"{v} {pr[v]} {ow[v]} {','.join(map(str, succ[v]))};\n")
    with open(p + ".start", "w") as f:
        f.write("SIGMA0 " + " ".join(f"{v}:{st0[v]}" for v in range(n) if ow[v] == 0) + "\nTAU0 " + " ".join(f"{v}:{st0[v]}" for v in range(n) if ow[v] == 1) + "\n")
def score(st):
    p = os.path.join(tmp, "c"); write(st, p)
    try: o = subprocess.run([sys.executable, "-I", RC, p + ".pg", p + ".start"], capture_output=True, text=True, timeout=120, env=dict(os.environ, TOP="1")).stdout
    except Exception: return (0.0, 0, 0)
    best = (0.0, 0, 0)
    for m in re.finditer(r"returns (\d+) edges.*?\n(?:.*\n)*?\s*PERROOT .*?\(returns of X per root\)/deg X ([\d.]+).*?per \(root, depth\) (\d+)", o):
        best = max(best, (float(m.group(2)), int(m.group(3)), int(m.group(1))))
    if os.environ.get("SCORE") == "ret":
        r = [int(x) for x in re.findall(r"PERROOT max returns of one Even X per root (\d+)", o)]
        return (max(r) if r else 0, best[0], best[2])
    return best
def mut(st):
    pr, ow, succ, st0 = list(st[0]), list(st[1]), [list(s) for s in st[2]], list(st[3])
    for _ in range(rng.randint(1, 2)):
        c = rng.randrange(6); v = rng.randrange(n)
        if c == 0: succ[v][rng.randrange(len(succ[v]))] = rng.randrange(n)
        elif c == 1 and len(succ[v]) < 4: succ[v].append(rng.randrange(n))
        elif c == 2 and len(succ[v]) > 1: succ[v].pop(rng.randrange(len(succ[v])))
        elif c == 3: w = rng.randrange(n); pr[v], pr[w] = pr[w], pr[v]
        elif c == 4: ow[v] ^= 1
        else: st0[v] = rng.choice(succ[v])
        succ[v] = sorted(set(succ[v]))
    for v in range(n):
        if st0[v] not in succ[v]: st0[v] = rng.choice(succ[v])
    return [pr, ow, succ, st0]
cur = [list(g0.prio) + [0] * PAD, list(g0.owner) + [0] * PAD, [sorted(set(s)) for s in g0.succ] + [[g0.n + i] for i in range(PAD)], [s0[v] if g0.owner[v] == 0 else t0[v] for v in range(g0.n)] + [g0.n + i for i in range(PAD)]]
cs = score(cur); print("seed", cs, flush=True); bs = cs
for it in range(steps):
    nx = mut(cur); ns = score(nx)
    if ns >= cs:
        cur, cs = nx, ns
        if cs > bs: bs = cs; write(cur, out); print(f"step {it} best {bs}", flush=True)
