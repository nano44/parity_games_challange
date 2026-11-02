#!/usr/bin/env python3
"""L-NEW box 137: adversarial climb against CONJECTURE RET-1 (each option re-entered at most once per FL run).
SCORE = 10^6 * RETMAX + 10^3 * MOVMAX + RET (rel.analyse, default S3 start, cap 600 iterations); a mutation is kept when SCORE does
not drop and every rel.py lemma check stays 0. Mutation: one edge / priority / owner change (same move set as L-RED r179 climb179.mut,
re-implemented here). Usage: climb137.py seed.pg iters seed out.pg"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import rel, pg
from n5x import load
CHK = ("ceilviol", "satdec", "frozviol", "syncviol", "cwviol", "chainviol", "defviol")
def score(g):
    try: R, ex, K = rel.analyse(g, None, cap=600)
    except Exception: return -1, None
    if any(R[k] for k in CHK): print("LEMMAVIOL", R, ex, flush=True); return 10 ** 9, R
    return 10 ** 6 * R["retmax"] + 10 ** 3 * R["movmax"] + R["ret"], R
def mut(g, rng):
    n = g.n; pr = list(g.prio); ow = list(g.owner); su = [list(x) for x in g.succ]; r = rng.random(); v = rng.randrange(n)
    if r < 0.35: su[v][rng.randrange(len(su[v]))] = rng.randrange(n)
    elif r < 0.55:
        if len(su[v]) < 5: su[v].append(rng.randrange(n))
    elif r < 0.7:
        if len(su[v]) > 1: su[v].pop(rng.randrange(len(su[v])))
    elif r < 0.92: pr[v] = rng.randrange(0, n + 2)
    else: ow[v] ^= 1
    return pg.Game(pr, ow, [sorted(set(x)) for x in su])
def write(g, p):
    with open(p, "w") as f:
        f.write(f"parity {g.n - 1};\n")
        for v in range(g.n): f.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")
if __name__ == "__main__":
    src, iters, seed, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
    g = load(src); bs, R = score(g); print("START", bs, R, flush=True)
    for it in range(iters):
        h = mut(g, rng); hs, HR = score(h)
        if hs >= 10 ** 9: write(h, out + ".viol"); break
        if hs >= bs:
            if hs > bs: print("IT", it, hs, HR, flush=True)
            g, bs, R = h, hs, HR; write(g, out)
    print("BEST", bs, R, flush=True)
