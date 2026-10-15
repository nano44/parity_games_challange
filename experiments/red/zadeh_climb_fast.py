#!/usr/bin/env python3
"""Hill-climb over vertex numberings for S5 (Zadeh + index tie-break) with the exp-game start, scored by L-SI's vjfast
(L-RED, R7). Same search as zadeh_order_climb.py, ~100x faster: each candidate numbering is written as a renumbered .pg and
vjfast zadeh --start spec:<the exp-game start, renumbered> is run on it. Mutations: swap two vertex ids. Usage:
  zadeh_climb_fast.py VJFAST game.pg [--steps 3000] [--restarts 3] [--seed 0] [--identity | --init FILE] [--out best.pg]"""
import sys, os, random, time, re, subprocess, tempfile
vjf, path = sys.argv[1], sys.argv[2]; arg = lambda k, d: type(d)(sys.argv[sys.argv.index(k) + 1]) if k in sys.argv else d
steps, restarts, seed = arg("--steps", 3000), arg("--restarts", 3), arg("--seed", 0); rng = random.Random(seed)
rows = {}; lab = {}
for line in open(path):
    m = re.match(r'^(\d+)\s+(\d+)\s+([01])\s+([\d,]+)\s*(?:"([^"]*)")?', line.strip())
    if m: v = int(m.group(1)); rows[v] = (int(m.group(2)), int(m.group(3)), [int(x) for x in m.group(4).split(",")]); lab[v] = m.group(5) or str(v)
n_v = len(rows); byname = {l: v for v, l in lab.items()}; find = byname.get
parse = lambda v: (lab[v][0], int(lab[v][1:])) if len(lab[v]) > 1 and lab[v][1:].isdigit() else (lab[v][0], 0)
n = 0
while find(f"E{n}") is not None: n += 1
start = {}
for v in rows:
    p, o, s = rows[v]
    if o == 0 and len(s) >= 2:
        c, j = parse(v)
        t = {"a": f"o{j}", "b": f"p{j}", "v": f"r{j}", "w": f"q{j}", "o": "m1", "p": "m1", "q": "m1", "r": "m1", "d": f"E{j}", "g": f"c{j}",
             "s": "m0", "m": (f"m{j + 1}" if j < n - 1 else "Y")}.get(c)
        if t and find(t) is not None and find(t) in s: start[v] = find(t)


def renumber(pos):
    out = [f"parity {n_v - 1};"]
    for old in sorted(rows, key=lambda v: pos[v]):
        p, o, s = rows[old]; out.append(f'{pos[old]} {p} {o} {",".join(str(pos[x]) for x in sorted(s, key=lambda x: pos[x]))} "{lab[old]}";')
    return "\n".join(out) + "\n"


tmp = tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False).name


def score(pos):
    open(tmp, "w").write(renumber(pos)); spec = " ".join(f"{pos[v]}:{pos[w]}" for v, w in start.items())
    r = subprocess.run([vjf, "zadeh", tmp, "--start", "spec:" + spec], capture_output=True, text=True, timeout=600)
    return int([l for l in r.stderr.splitlines() if l.startswith("solved with")][0].split()[2])


init = None
if "--init" in sys.argv:          # start restart 0 from the numbering of FILE, matched by label; labels FILE lacks go last
    got = {}
    for line in open(sys.argv[sys.argv.index("--init") + 1]):
        m = re.match(r'^(\d+)\s+\d+\s+[01]\s+[\d,]+\s*"([^"]*)"', line.strip())
        if m: got[m.group(2)] = int(m.group(1))
    order = sorted(rows, key=lambda v: (lab[v] not in got, got.get(lab[v], 0), v)); init = [0] * n_v
    for i, v in enumerate(order): init[v] = i
t0 = time.time(); overall = (0, None); ident = score(list(range(n_v)))
for r in range(restarts):
    pos = init if (init and r == 0) else list(range(n_v)) if ("--identity" in sys.argv and r == 0) else rng.sample(range(n_v), n_v); cur = score(pos)
    for _ in range(steps):
        q = list(pos); a, b = rng.sample(range(n_v), 2); q[a], q[b] = q[b], q[a]; sc = score(q)
        if sc >= cur: pos, cur = q, sc
    print(f"restart {r}: {cur}", flush=True)
    if cur > overall[0]: overall = (cur, pos)
if "--out" in sys.argv: open(sys.argv[sys.argv.index("--out") + 1], "w").write(renumber(overall[1]))
os.unlink(tmp)
print(f"{os.path.basename(path)} N={n} |V|={n_v}: identity numbering {ident}, best numbering found {overall[0]} ({restarts} restarts x {steps} steps, {time.time() - t0:.0f}s)")
