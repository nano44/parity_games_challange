#!/usr/bin/env python3
"""Box 44 DATA for Lemma ALT (docs/new/N5-FBF-box44.md §10). At every in-phase transition t -> t+1 and every Odd choice vertex q with
sigma-bar_{t+1}(q) != sigma-bar_t(q) and lambda(q) != q, classify: CLEAN (q on no honest cycle at t and t+1, and y2 := sigma-bar_{t+1}(q)
has an honest play at t avoiding q) vs NONCLEAN; for CLEAN ones: STRICT (Xi(q) rises) or TIE (Xi(q) unchanged; then
kappa_t(y2) = kappa_t(y1) and kappa(y2) unchanged, which is checked: TIE_V counts failures of that). ALT_V counts CLEAN changes with
Xi(q) DEcreasing or (no rise and no tie). Usage: altcheck.py --list FILE | --rand C LO HI SEED | files"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box43")); sys.path.insert(0, HERE)
from multi import rand_ckO
from n5x import load, step, start_pair, Engine, dual
C = dict(changes=0, CLEAN=0, STRICT=0, TIE=0, TIE_V=0, ALT_V=0, NONCLEAN=0, NC_noH1=0, NC_y2thru=0, CYC=0)
def oncycle(nxt, q):
    x, seen = nxt[q], set()
    while x not in seen and x != q: seen.add(x); x = nxt[x]
    return x == q
def avoids(nxt, y, q):
    x, seen = y, set()
    while x not in seen:
        if x == q: return False
        seen.add(x); x = nxt[x]
    return True
def check(g, cap=4000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, None)
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2]; prev = None
    while True:
        vs, sb = E.evaluate(tuple(s)); lam = tuple(x[0] for x in vs); nxt = [s[v] if g.owner[v] == 0 else sb[v] for v in range(g.n)]
        cur = (lam, tuple(t), sb, vs, nxt)
        if prev and (prev[0], prev[1]) == (lam, tuple(t)):
            psb, pvs, pnxt = prev[2], prev[3], prev[4]
            for q in Q:
                if sb[q] == psb[q]: continue
                C["changes"] += 1
                if lam[q] == q: C["CYC"] += 1; continue
                y1, y2 = psb[q], sb[q]
                h1 = not oncycle(pnxt, q) and not oncycle(nxt, q)
                if not h1: C["NONCLEAN"] += 1; C["NC_noH1"] += 1; continue
                if not avoids(pnxt, y2, q): C["NONCLEAN"] += 1; C["NC_y2thru"] += 1; continue
                C["CLEAN"] += 1; a, b = E.key(pvs[q]), E.key(vs[q])
                if b > a: C["STRICT"] += 1
                elif b == a:
                    C["TIE"] += 1
                    if not (pvs[y2] == pvs[y1] or E.key(pvs[y2]) == E.key(pvs[y1])) or pvs[y2] != vs[y2]: C["TIE_V"] += 1
                else: C["ALT_V"] += 1
        r = step(g, E, Ed, s, t)
        if r is None: break
        prev = cur; s, t = r[0], r[1]
if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "--list":
        R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        gs = [load(os.path.join(R0, l.split()[0])) for l in open(a[1]) if l.strip() and not l.startswith("#")]
    elif a[0] == "--rand":
        cnt, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        gs = [g for g in (rand_ckO(rng, lo, hi, rng.randint(2, 4)) for _ in range(cnt)) if g is not None]
    else: gs = [load(f) for f in a]
    for g in gs: check(g)
    print(f"runs {len(gs)}: " + ", ".join(f"{k} {v}" for k, v in C.items()))
