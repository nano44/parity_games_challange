#!/usr/bin/env python3
"""Class-structured adversarial numberings for index-tie-break rules (S5 zadeh, S6 cunningham; L-RED). Vertices of the
PGSolver-labelled families are grouped by the letter part of their label (e.g. 'e3' -> class 'e'); a scheme = a rank per
class and a direction per class; the numbering sorts vertices by (rank, +index or -index). A scheme applies to every N, so
growth can be measured.  Hill-climb at N = N0 (objective: vjfast iterations), then report iterations for N0..N0+3.
Usage: search_classnum.py VJFAST GENS_DIR FAMILY RULE [--n0 4] [--steps 300] [--restarts 3] [--seed 0]"""
import sys, os, re, random, subprocess, tempfile, argparse
ap = argparse.ArgumentParser(); ap.add_argument("vjfast"); ap.add_argument("gens"); ap.add_argument("family"); ap.add_argument("rule")
ap.add_argument("--n0", type=int, default=4); ap.add_argument("--steps", type=int, default=300); ap.add_argument("--restarts", type=int, default=3)
ap.add_argument("--seed", type=int, default=0); ap.add_argument("--timeout", type=float, default=300); a = ap.parse_args(); rng = random.Random(a.seed)


def load(N):
    txt = subprocess.run(["python3", os.path.join(a.gens, "gens.py"), a.family, str(N)], capture_output=True, text=True).stdout
    rows = {}
    for line in txt.splitlines():
        m = re.match(r'^(\d+)\s+(\d+)\s+([01])\s+([\d,]+)\s+"([^"]*)"', line.strip())
        if m:
            lab = m.group(5); cls = re.match(r"[A-Za-z]+", lab).group(0); idx = int(re.sub(r"[^0-9]", "", lab) or 0)
            rows[int(m.group(1))] = (int(m.group(2)), int(m.group(3)), [int(x) for x in m.group(4).split(",")], cls, idx)
    return rows


def numbering(rows, scheme):
    rank, direc = scheme
    order = sorted(rows, key=lambda v: (rank.get(rows[v][3], 99), direc.get(rows[v][3], 1) * rows[v][4], v))
    return {old: new for new, old in enumerate(order)}


def score(rows, scheme):
    perm = numbering(rows, scheme); n = len(rows)
    out = [f"parity {n - 1};"] + [f"{perm[v]} {rows[v][0]} {rows[v][1]} {','.join(map(str, sorted(perm[x] for x in rows[v][2])))};" for v in sorted(rows, key=lambda v: perm[v])]
    with tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False) as f: f.write("\n".join(out) + "\n"); p = f.name
    try:
        r = subprocess.run([a.vjfast, a.rule, p], capture_output=True, text=True, timeout=a.timeout)
        it = int([l for l in r.stderr.splitlines() if l.startswith("solved with")][0].split()[2])
    except Exception:
        it = -1
    os.unlink(p); return it


rows0 = load(a.n0); classes = sorted({r[3] for r in rows0.values()})
print(f"{a.family} N={a.n0}: n={len(rows0)} classes {classes}; identity numbering: {score(rows0, ({}, {}))}", flush=True)
best_all = (-1, None)
for rs in range(a.restarts):
    perm = list(classes); rng.shuffle(perm); rank = {c: i for i, c in enumerate(perm)}; direc = {c: rng.choice((1, -1)) for c in classes}
    cur = score(rows0, (rank, direc))
    for k in range(a.steps):
        r2 = dict(rank); d2 = dict(direc)
        if rng.random() < 0.6:
            c1, c2 = rng.sample(classes, 2); r2[c1], r2[c2] = r2[c2], r2[c1]
        else:
            c = rng.choice(classes); d2[c] = -d2[c]
        sc = score(rows0, (r2, d2))
        if sc >= cur: rank, direc, cur = r2, d2, sc
    print(f"restart {rs}: best {cur}; order {[c for c in sorted(classes, key=lambda c: rank[c])]} dirs {direc}", flush=True)
    if cur > best_all[0]: best_all = (cur, (rank, direc))
sch = best_all[1]
print("growth of the best scheme:", [(N, score(load(N), sch)) for N in range(a.n0 - 1, a.n0 + 4)], flush=True)
