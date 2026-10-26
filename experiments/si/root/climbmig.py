#!/usr/bin/env python3
"""L-SI box 21 (successor 17): hill-climb against CONJECTURE C-ONCE / C-FREEZE (docs/si/N5-GCX-box21.md). Score (lexicographic):
(MIG2X_cint + MIG_LATE, most X-type migrations of one vertex in one C-interval, most migration transitions inside one C-interval, all migration transitions in C-intervals), from gcx.py's counters.
Mutations as fb2o/climb2o.py (one priority, redirect / add / drop one edge), any number of Odd choice vertices >= KMIN. DATA tool.
Usage: climbmig.py SEED STEPS START.pg [START.start] (env KMIN, default 2; OBJ mig | ue | ul: a U event late in its C-interval, CONJECTURE UL_C). Writes the best game to root/instances/."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import gcx
from common import load, readstart
import pg

OBJ = os.environ.get("OBJ", "mig")      # mig: C-ONCE_X / MIG_LATE; ue: UE-ONCE_C (an edge unforbid-switched twice inside one C-interval)
gcx.UEV = OBJ in ("ue", "ul")

def score(g, start=None):
    gcx.C.clear(); gcx.MX.clear(); gcx.EX.clear()
    try: gcx.run(g, "climb", start)
    except Exception: return None
    C = gcx.C + gcx.MX
    if OBJ == "ue": return (C["UE2_Cr"], C["UR_in"], C["cint_len_max"])
    if OBJ == "ul": return (C["UL_C"], C["UR_in_index_max_minus_U"], C["cint_len_max"])
    return (C["MIG2X_cint"] + C["MIG_LATE"], C["migx_per_vertex_max"], C["cint_migt_one_max"], C["cint_migt"])

def kq(g): return sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2)

def mutate(rng, g, kmin):
    prio, owner, succ = list(g.prio), list(g.owner), [list(s) for s in g.succ]
    n = g.n; v = rng.randrange(n); r = rng.random()
    if r < 0.25: prio[v] = rng.randrange(2 * n + 3)
    elif r < 0.6: succ[v][rng.randrange(len(succ[v]))] = rng.randrange(n)
    elif r < 0.8: succ[v].append(rng.randrange(n))
    elif len(succ[v]) > 1: succ[v].pop(rng.randrange(len(succ[v])))
    if len(set(prio)) < n: return None                     # SPEC S1: rewards injective
    h = pg.Game(prio, owner, [sorted(set(s)) for s in succ])
    return h if kq(h) >= kmin else None

def main():
    seed, steps = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed); kmin = int(os.environ.get("KMIN", "2"))
    g = load(sys.argv[3]); st = readstart(sys.argv[4]) if len(sys.argv) > 4 else None
    sc = score(g, st); first = sc
    for _ in range(steps):
        h = mutate(rng, g, kmin)
        if h is None: continue
        s2 = score(h)                                      # mutated games start from N5's default start pair
        if s2 is not None and s2 >= sc: g, sc, st = h, s2, None
    os.makedirs(os.path.join(HERE, "instances"), exist_ok=True)
    out = os.path.join(HERE, "instances", f"{OBJ}_s{seed}_n{g.n}_{sc[0]}_{sc[1]}.pg")
    with open(out, "w") as f:
        f.write(f"parity {g.n - 1};\n")
        for v in range(g.n): f.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")
    print(f"seed {seed} n {g.n}: start score {first} -> best {sc} -> {out}")

if __name__ == "__main__":
    main()
