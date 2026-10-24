#!/usr/bin/env python3
"""Box 31 climb against L-NEW box 27 (docs/new/N5-xing-box27.md @ l-new 1322d958) on o-cyclic C^1O, canonical start.
L-NEW's checkers are imported UNMODIFIED from $LNEW_BOX25 (a checkout of experiments/new/box25 at l-new 1322d958):
  coarsecheck.run (Lemma C / CR / XA: C1, C2, C3; run twice: stretches cut at fallbacks, and --withfb),
  fbfcheck.run (Lemma FBF: ENTRY_AFTER_FB, ROUTE_CHANGE_AFTER_FB), fbedges.run (Lemma FBL: OTHER edges at throttled (h)-fallbacks).
Fitness (lexicographic): (violations, exercise) where exercise depends on --target:
  lemmas : throttled (h)-fallbacks + fbf checked transitions + re-entries     (default)
  nh     : max over joint λ-phases of non-(h) transitions                     ((NH), L-NEW §8)
  cyc    : max over joint λ-phases of (θ, w)-stretches                        ((CYC'))
Usage: xclimb.py n seed secs out [--from g.pg] [--target lemmas|nh|cyc]"""
import sys, os, random, time
B = os.environ.get("LNEW_BOX25") or sys.exit("set LNEW_BOX25")
sys.path.insert(0, B)
from collections import Counter
from common import *
from climb_fix import mutate
from wdrop_h import oncycle
import coarsecheck, fbfcheck, fbedges
VIOL = ("C1_fail", "C2_fail", "C3_fail", "C3_fail_after_fb", "ENTRY_AFTER_FB", "ROUTE_CHANGE_AFTER_FB", "OTHER", "fb_without_leave")

def profile(g):
    """per joint λ-phase (key as phaseprofile.py): non-(h) transitions and (θ, w)-stretches; returns (max nh, max stretches)."""
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, None); prev = None; k = 0
    nh = st = bnh = bst = 0
    while k < 400:
        Xi, sb = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t)); _, W = wvals(g, s, t)
        h = not oncycle(g, s, sb, o) and not oncycle(g, s, t, o) and Xi[o][0] == W[o][0]
        key = ((tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), E.key(Xi[o]), E.key(W[o]))
        if prev is None or key[0] != prev[0]: nh = 0; st = 1
        elif key[1:] != prev[1:]: st += 1
        nh += 0 if h else 1
        bnh, bst = max(bnh, nh), max(bst, st); prev = key
        r = step(g, E, Ed, s, t)
        if r is None: break
        s, t = list(r[0]), list(r[1]); k += 1
    return bnh, bst

def measure(g):
    c = Counter()
    coarsecheck.WITHFB = False; coarsecheck.run(g, None, c)
    c2 = Counter(); coarsecheck.WITHFB = True; coarsecheck.run(g, None, c2)
    for k in ("C1_fail", "C2_fail", "C3_fail", "C3_fail_after_fb"): c[k + "_withfb"] = c2[k]
    c["reentries_withfb"] = c2["reentries"]
    fbfcheck.run(g, None, c); fbedges.run(g, None, c)
    nh, cyc = profile(g); c["max_nh_phase"] = nh; c["max_stretches_phase"] = cyc
    return c

def score(c, target):
    v = sum(c[k] + c[k + "_withfb"] for k in VIOL)
    ex = {"lemmas": c["throttled_fallbacks"] + c["checked_transitions"] + c["reentries_withfb"],
          "nh": c["max_nh_phase"], "cyc": c["max_stretches_phase"]}[target]
    return (v, ex)

def fit(G, target):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(G[2][v]) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return (-1, -1), None
    g = pg.Game(*G)
    if not any(w in split(g, odd[0]) for w in G[2][odd[0]]): return (-1, -1), None
    try: c = measure(g)
    except Exception: return (-1, -1), None
    return score(c, target), c

if __name__ == "__main__":
    n, seed, secs, out = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
    target = sys.argv[sys.argv.index("--target") + 1] if "--target" in sys.argv else "lemmas"
    if "--from" in sys.argv:
        g = load(sys.argv[sys.argv.index("--from") + 1]); n = g.n; G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]
        f, c = fit(G, target)
    else:
        while True:
            g = rand_c1o(rng, n, n, forced=0.0)
            if g is None: continue
            G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f, c = fit(G, target)
            if f[0] >= 0: break
    print("START", f, dict(c), flush=True)
    t0 = time.time(); it = 0
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh, ch = fit(H, target)
        if fh >= f:
            if fh > f:
                print(f"{time.time()-t0:7.0f}s it {it} fit {fh} {dict(ch)}", flush=True)
                open(out + ".pg", "w").write(f"parity {n-1};\n" + "".join(f"{v} {H[0][v]} {H[1][v]} {','.join(map(str, H[2][v]))};\n" for v in range(n)))
            G, f = H, fh
    print("FINAL", f, it)
