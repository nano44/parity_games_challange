#!/usr/bin/env python3
"""L-SI box 16: DATA for the not-(h3_D) KIND-MONO port (docs/si/N5-2O-T-box16.md §8). Inside each phase, on every maximal run S of
consecutive S4a transitions with D_k constant and |D_k| = 2, with both gates in ONE honest class (same honest cycle node c) and (h3_D)
failing at some gate, it tests the set form of RESULTS R50's FRZ-U: with m* := the most relevant of c and the gates' W-cycle nodes and
kappa_W(v) := P(W(v)) n V_{>m*}, kappa_W is constant on R_D from state k0 + |R_D| - 1 of S on (R_D constant on the checked part).
It counts runs, checks, violations, and how often the two gates have DIFFERENT W-cycle nodes (Fact B fails across terminals by cycle
node). Saves the first violating game + start pair. Usage: km2.py --list FILE [KMIN] | --rand COUNT NLO NHI SEED (K env)"""
import sys, os, random, json
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, HERE)
from n5x import step, start_pair, Engine, dual, load
from tcdir import lasso, wval
C = dict(states=0, cfg=0, cfg_diffW=0, runs=0, checks=0, viol=0)
SAVED = []

def check(g, name, start=None):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []; k = 0; s0, t0 = list(s), list(t)
    while k <= 3000:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        D = frozenset(u for u in range(g.n) if g.owner[u] == 1 and sb[u] != t[u])
        wn = (lambda s, t: (lambda v: s[v] if g.owner[v] == 0 else t[v]))(list(s), tuple(t))
        W = {v: wval(E, wn, v) for v in range(g.n)}
        RD = frozenset(v for v in range(g.n) if any(x in D for x in lasso(wn, v)[0]))
        cfg = False
        if len(D) == 2:
            a, b = sorted(D)
            if vs[a][0] == vs[b][0] and any(vs[u][0] != W[u][0] for u in D):
                cfg = True; C["cfg"] += 1; C["cfg_diffW"] += W[a][0] != W[b][0]
        C["states"] += 1
        mstar = max([vs[u][0] for u in D] + [W[u][0] for u in D], key=lambda x: E.rank[x]) if D else None
        rows.append(dict(key=(tuple(x[0] for x in vs), tuple(t)), D=D, RD=RD, cfg=cfg, W=W, m=mstar, fb=r[4] if r else 0))
        if r is None: break
        s, t = r[0], r[1]; k += 1
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and not rows[j]["fb"] and rows[j + 1]["key"] == rows[i]["key"] and rows[j + 1]["D"] == rows[i]["D"] \
                and rows[j + 1]["RD"] == rows[i]["RD"] and rows[i]["cfg"] and rows[j + 1]["cfg"]:
            j += 1
        if rows[i]["cfg"] and j > i:
            C["runs"] += 1
            m = max((rows[x]["m"] for x in range(i, j + 1)), key=lambda y: E.rank[y])
            cut = lambda val: (val[1] >> (E.rank[m] + 1)) << (E.rank[m] + 1)
            base = i + len(rows[i]["RD"]) - 1
            for x in range(base + 1, j + 1):
                C["checks"] += 1
                if any(cut(rows[x]["W"][v]) != cut(rows[base]["W"][v]) for v in rows[i]["RD"]):
                    C["viol"] += 1
                    if not SAVED: SAVED.append((g, name, start, i, x))
        i = j + 1

def save(g, start, tag):
    out = os.path.join(HERE, "instances", tag)
    with open(out + ".pg", "w") as f:
        f.write(f"parity {g.n - 1};\n")
        for v in range(g.n): f.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")
    if start: json.dump({"sigma": start[0], "tau": start[1]}, open(out + ".start.json", "w"))
    return out

def main():
    a = sys.argv[1:]
    if a[0] == "--one":
        g = load(a[1]); st = json.load(open(a[2])) if len(a) > 2 else None
        check(g, a[1], ({int(x): y for x, y in st["sigma"].items()}, {int(x): y for x, y in st["tau"].items()}) if st else None)
    elif a[0] == "--rand":
        sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box43")); from multi import rand_ckO
        cnt, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); i = 0; K = int(os.environ.get("K", "0"))
        while i < cnt:
            g = rand_ckO(rng, lo, hi, K or rng.choice((2, 2, 3, 4)))
            if g is None: continue
            i += 1
            st = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1})
            check(g, f"rand seed {seed} #{i}", None if i % 2 else st)
    else:
        kmin = int(a[2]) if len(a) > 2 else 2
        for line in open(a[1]):
            f = line.strip()
            if not f: continue
            g = load(os.path.join(ROOT, f))
            if g.n > 48 or sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2) < kmin: continue
            check(g, f)
    print(" ".join(f"{k}={v}" for k, v in C.items()))
    if SAVED:
        g, name, st, i, x = SAVED[0]
        print("FIRST VIOLATION", name, "run start", i, "state", x, "->", save(g, st, f"km2_viol_n{g.n}"))

if __name__ == "__main__":
    main()
