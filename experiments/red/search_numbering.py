#!/usr/bin/env python3
"""Adversarial vertex numbering for index-tie-break rules (S5 zadeh, S6 cunningham; L-RED). The input's numbering is the
adversary's: hill-climb over permutations of the vertex ids of a family instance, scoring the iteration count of L-SI's
vjfast under RULE (start best-reward, which also depends on indices).  Usage:
  search_numbering.py VJFAST game.pg RULE [--steps 400] [--restarts 4] [--seed 0] [--out best.pg]"""
import sys, os, random, subprocess, tempfile, argparse, re
ap = argparse.ArgumentParser(); ap.add_argument("vjfast"); ap.add_argument("game"); ap.add_argument("rule")
ap.add_argument("--steps", type=int, default=400); ap.add_argument("--restarts", type=int, default=4); ap.add_argument("--seed", type=int, default=0)
ap.add_argument("--out", default=""); ap.add_argument("--timeout", type=float, default=120); a = ap.parse_args(); rng = random.Random(a.seed)
rows = {}
for line in open(a.game):
    m = re.match(r'^(\d+)\s+(\d+)\s+([01])\s+([\d,]+)', line.strip())
    if m: rows[int(m.group(1))] = (int(m.group(2)), int(m.group(3)), [int(x) for x in m.group(4).split(",")])
n = len(rows)


def renumber(perm):          # perm[old] = new
    out = [f"parity {n - 1};"]
    for old in sorted(rows, key=lambda v: perm[v]):
        p, o, s = rows[old]; out.append(f"{perm[old]} {p} {o} {','.join(map(str, sorted(perm[x] for x in s)))};")
    return "\n".join(out) + "\n"


def score(perm):
    with tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False) as f: f.write(renumber(perm)); p = f.name
    try:
        r = subprocess.run([a.vjfast, a.rule, p], capture_output=True, text=True, timeout=a.timeout)
        it = int([l for l in r.stderr.splitlines() if l.startswith("solved with")][0].split()[2])
    except Exception:
        it = -1
    os.unlink(p); return it


best_all = (-1, None)
ident = list(range(n)); print(f"identity numbering: {score(ident)} iterations ({a.rule}, n={n})", flush=True)
for rs in range(a.restarts):
    perm = list(range(n)); rng.shuffle(perm); cur = score(perm)
    for k in range(a.steps):
        cand = list(perm); i, j = rng.randrange(n), rng.randrange(n); cand[i], cand[j] = cand[j], cand[i]
        if rng.random() < 0.3:
            i2, j2 = rng.randrange(n), rng.randrange(n); cand[i2], cand[j2] = cand[j2], cand[i2]
        sc = score(cand)
        if sc >= cur: perm, cur = cand, sc
    print(f"restart {rs}: best {cur}", flush=True)
    if cur > best_all[0]: best_all = (cur, perm)
print(f"best over restarts: {best_all[0]}")
if a.out: open(a.out, "w").write(renumber(best_all[1]))
