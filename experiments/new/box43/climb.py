#!/usr/bin/env python3
"""Box 43 climber: mutate a C^kO game (k fixed Odd choice vertices) to maximise an N5 measure from multi.py (DATA).
Objective (lexicographic): --obj T (tau-changing transitions), it, TJ, maxP, ret (max per-vertex tau(o_i) value returns).
Start pair: best-reward (SPEC S3), or with --starts also a start pair in the genome.
Usage: climb.py K NMAX STEPS SEED OBJ OUTDIR [--starts] [--deg2 (every Odd choice vertex has out-degree exactly 2)] [--frontier (with objective Dch/RDch: Even has >= 2 choice vertices)]
       [--seed FILE (start from this game; K is then its number of Odd choice vertices)]"""
import sys, os, random, json, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from multi import run, measure, rand_ckO, odd_choices, pg

def returns(g, states):
    best = 0
    for o in odd_choices(g):
        seq = [s[1][o] for s in states]; seen = {seq[0]}; r = 0
        for a, b in zip(seq, seq[1:]):
            if b != a:
                if b in seen: r += 1
                seen.add(b)
        best = max(best, r)
    return best

def returns_n(g, states, lamU):
    """returns at o_i by a switch made while o_i is NOT its own lambda^U cycle node (before and after): excludes the
    own-cycle-node length switches (the R38 CN-LAST kind)."""
    best = 0
    for o in odd_choices(g):
        seq = [s[1][o] for s in states]; seen = {seq[0]}; r = 0
        for i, (a, b) in enumerate(zip(seq, seq[1:])):
            if b != a:
                if b in seen and lamU[i][o] != o and lamU[i + 1][o] != o: r += 1
                seen.add(b)
        best = max(best, r)
    return best

def score(g, st, obj):
    if st is not None:
        st = ({v: st[v] for v in range(g.n) if g.owner[v] == 0}, {v: st[v] for v in range(g.n) if g.owner[v] == 1})
    try: states, lam, lamU, fbs = run(g, st, cap=5000)
    except RecursionError: return None, None
    m = measure(g, states, lam, lamU, fbs); m["ret"] = returns(g, states); m["retn"] = returns_n(g, states, lamU)
    m["tx"] = m["T"] - sum(len(g.succ[o]) - 1 for o in odd_choices(g))
    if "Dch" in obj or "RDch" in obj:
        from dset import prof, cls
        if FRONT and min(cls(g)) < 2: return None, None
        m.update({k: v for k, v in prof(g, st).items() if k in ("Dch", "RDch", "maxD")})
    return tuple(m[o] for o in obj.split(",")), m

def mutate(rng, g, O, nmax, st):
    n = g.n; prio, owner, succ = list(g.prio), list(g.owner), [list(s) for s in g.succ]; st = list(st) if st else None
    r = rng.random()
    if r < 0.35:                                   # rewire one edge
        v = rng.randrange(n); s = set(succ[v])
        if len(s) > (2 if v in O else 1) and rng.random() < 0.5: s.discard(rng.choice(sorted(s)))
        elif owner[v] == 0 or v in O: s.add(rng.randrange(n))
        else: s = {rng.randrange(n)}
        succ[v] = sorted(s)
    elif r < 0.6: prio[rng.randrange(n)] = rng.randrange(n + 4)
    elif r < 0.7:                                  # flip a non-choice vertex Even <-> forced Odd
        v = rng.randrange(n)
        if v not in O:
            owner[v] = 1 - owner[v]
            if owner[v] == 1: succ[v] = succ[v][:1]
    elif r < 0.8 and n < nmax:                     # add a vertex
        prio.append(rng.randrange(n + 4)); owner.append(0); succ.append([rng.randrange(n + 1)])
        u = rng.randrange(n); succ[u] = sorted(set(succ[u]) | {n}) if (owner[u] == 0 or u in O) else [n]
        if st: st.append(succ[n][0])
        n += 1
    elif r < 0.85 and n > len(O) + 2:              # delete a non-choice vertex
        v = rng.choice([x for x in range(n) if x not in O]); keep = [x for x in range(n) if x != v]; idx = {x: i for i, x in enumerate(keep)}
        ns = []
        for x in keep:
            s = sorted({idx[w] for w in succ[x] if w != v}) or [idx[x]]
            ns.append(s)
        prio = [prio[x] for x in keep]; owner = [owner[x] for x in keep]; succ = ns
        O = [idx[x] for x in O]
        if st: st = [idx[st[x]] if st[x] != v else ns[i][0] for i, x in enumerate(keep)]
        n -= 1
    else:
        if st: v = rng.randrange(n); st[v] = rng.choice(succ[v])
        else: prio[rng.randrange(n)] = rng.randrange(n + 4)
    for v in O:
        if len(succ[v]) < 2: return None
        if DEG2 and len(succ[v]) != 2: return None
    h = pg.Game(prio, owner, succ)
    if len(odd_choices(h)) != len(O): return None
    if st:
        st = [x if x in succ[v] else succ[v][0] for v, x in enumerate(st)]
    return h, O, st

def save(path, g, st, m):
    with open(path, "w") as f:
        f.write(f"parity {g.n - 1};\n")
        for v in range(g.n): f.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")
    if st is not None:
        with open(path[:-3] + ".start", "w") as f:
            f.write("SIGMA0 " + " ".join(f"{v}:{st[v]}" for v in range(g.n) if g.owner[v] == 0) + "\n")
            f.write("TAU0 " + " ".join(f"{v}:{st[v]}" for v in range(g.n) if g.owner[v] == 1) + "\n")

if __name__ == "__main__":
    K, NMAX, STEPS, SEED = map(int, sys.argv[1:5]); OBJ, OUT = sys.argv[5], sys.argv[6]; starts = "--starts" in sys.argv
    DEG2 = "--deg2" in sys.argv; FRONT = "--frontier" in sys.argv
    os.makedirs(OUT, exist_ok=True); rng = random.Random(SEED)
    g = None
    if "--seed" in sys.argv:
        from n5x import load
        g = load(sys.argv[sys.argv.index("--seed") + 1]); NMAX = max(NMAX, g.n)
    while g is None or (DEG2 and any(len(g.succ[o]) != 2 for o in odd_choices(g))): g = rand_ckO(rng, K + 2, max(K + 3, NMAX // 2), K)
    O = odd_choices(g); st = [s[0] for s in g.succ] if starts else None
    best, bm = score(g, st, OBJ)
    while best is None:
        g = rand_ckO(rng, K + 2, max(K + 3, NMAX // 2), K)
        if g is None or (DEG2 and any(len(g.succ[o]) != 2 for o in odd_choices(g))): continue
        O = odd_choices(g); st = [s[0] for s in g.succ] if starts else None; best, bm = score(g, st, OBJ)
    for t in range(STEPS):
        r = mutate(rng, g, O, NMAX, st)
        if r is None: continue
        h, O2, st2 = r; sc, m = score(h, st2, OBJ)
        if sc is None: continue
        if sc >= best:
            if sc > best:
                print(t, sc, " ".join(f"{a}={m[a]}" for a in ("n", "k", "it", "fb", "J", "T", "Tv", "TJ", "TS", "SS", "P", "maxP", "maxF", "ret", "retn", "tx", "prodeg")), flush=True)
                save(os.path.join(OUT, f"best_k{K}_s{SEED}{'_d2' if DEG2 else ''}.pg"), h, st2, m)
            g, O, st, best, bm = h, O2, st2, sc, m
