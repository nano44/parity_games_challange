#!/usr/bin/env python3
"""Box 34 climb on nested carries (Lead 21:1xZ): fitness = ((CL) violations, max (C) in one phase, Z of that phase).
(C) = '+−' reversals of R whose reversing transition is a fallback, a drain of consecutive evicting fallbacks counting once
(docs/si/P-N5-Z-fixes-box5.md §2); computed with L-SI's zcount.zsigns per phase, exactly as revpay.scan's loop but per phase.
(CL) violations exactly as L-SI's clclimb.fit (carries.scan; consecutive carries with w unchanged and a higher carry level).
L-SI's modules (experiments/si/xing/) are imported unmodified. Usage: ccclimb.py seed secs OUT seed.pg | ccclimb.py --eval g.pg ..."""
import sys, os, random, time
X = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "si", "xing"); sys.path.insert(0, X)
from revpay import *
import carries as C
ROOTP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")
sys.path.insert(0, os.path.join(ROOTP, "experiments/new/box21")); sys.path.insert(0, os.path.join(ROOTP, "experiments/new/box25"))
from climb_fix import mutate
from pureY import split

def cz(path):
    g = load(path); rows, ph = profile(g); assert_run(g, rows); annotate(g, rows); best = (0, 0, (0, 0))
    for (x, y) in ph:
        Z, sg = zsigns(rows, x, y); prev = None; c = 0
        for s, k in sg:
            if s != "±" and prev is not None and s != prev and prev + s == "+-" and rows[k]["fb"]: c += 1
            if s != "±": prev = s
        best = max(best, (c, Z, (x, y)))
    return best

def evaluate(path):
    out = C.scan(path, show=False)
    viol = sum(1 for a, b in zip(out, out[1:]) if b["wsame"] and b["carry_lev"] > a["carry_lev"] and a["carry_lev"] >= 0)
    c, Z, ph = cz(path)
    return (viol, c, Z), dict(CL_viol=viol, C=c, Z=Z, phase=ph, carries=len(out))

def fit(G, tmp):
    BAD = (-1, -1, -1)
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(G[2][v]) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return BAD, None
    g = pg.Game(*G)
    if not any(w in split(g, odd[0]) for w in G[2][odd[0]]): return BAD, None
    try:
        open(tmp, "w").write(f"parity {n-1};\n" + "".join(f"{v} {G[0][v]} {G[1][v]} {','.join(map(str, G[2][v]))};\n" for v in range(n)))
        return evaluate(tmp)
    except Exception: return BAD, None

if __name__ == "__main__":
    if sys.argv[1] == "--eval":
        for p in sys.argv[2:]: print(os.path.basename(p), evaluate(p)[1], flush=True)
        sys.exit()
    seed, secs, out = int(sys.argv[1]), float(sys.argv[2]), sys.argv[3]; rng = random.Random(seed); tmp = out + ".tmp.pg"
    g = load(sys.argv[4]); n = g.n; G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f, c = fit(G, tmp)
    t0 = time.time(); it = 0; print("start", f, c, flush=True)
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh, ch = fit(H, tmp)
        if fh >= f:
            if fh > f:
                print(f"{time.time()-t0:7.0f}s it {it} fit {fh} {ch}", flush=True)
                open(out + ".pg", "w").write(f"parity {n-1};\n" + "".join(f"{v} {H[0][v]} {H[1][v]} {','.join(map(str, H[2][v]))};\n" for v in range(n)))
            G, f = H, fh
    print("FINAL", f, it, flush=True)
