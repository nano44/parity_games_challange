#!/usr/bin/env python3
"""Box 31 climb against L-NEW box 27 (docs/new/N5-xing-box27.md @ l-new 1322d958) on o-cyclic C^1O, canonical start.
L-NEW's checkers are imported UNMODIFIED from $LNEW_BOX25 (a checkout of experiments/new/box25 at l-new 1322d958):
  coarsecheck.run (Lemma C / CR / XA: C1, C2, C3; run twice: stretches cut at fallbacks, and --withfb),
  fbfcheck.run (Lemma FBF: ENTRY_AFTER_FB, ROUTE_CHANGE_AFTER_FB), fbedges.run (Lemma FBL: OTHER edges at throttled (h)-fallbacks).
Fitness (lexicographic): (violations, exercise) where exercise depends on --target:
  lemmas : throttled (h)-fallbacks + fbf checked transitions + re-entries     (default)
  nh     : max over joint λ-phases of non-(h) transitions                     ((NH), L-NEW §8)
  cyc    : max over joint λ-phases of (θ, w)-stretches                        ((CYC'))
  reent  : throttled re-entries into R inside one stretch (coarsecheck's count, cut at fallbacks + --withfb), then leaves; Theorem XA
           data (referees on P-N5-XA: none observed)
  reentu : as reent, but only re-entries with u* ≠ none count first (Theorem XA's main case)
  cycu   : (max θ-changes inside one (w, u*)-run, max θ-changes per phase)    ((CYC-u*), L-NEW §8b; lemma checks skipped in
           the fitness, run them on the bests)
  A (w, u*)-run: consecutive states of one joint λ-phase (phaseprofile.py's key) with (h), θ ◁ w, w fixed and u* (the most
  relevant vertex of P(θ) Δ P(w), coarsecheck.py's computation) fixed.
Usage: xclimb.py n seed secs out [--from g.pg] [--pad N] [--target lemmas|nh|cyc|cycu]
  --pad N: append inert Even vertices (priority 0, self-loop) up to N vertices, as thetaclimb.py does."""
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

def cycu(g):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, None); prev = None; k = 0
    run = ph = brun = bph = 0
    while k < 400:
        Xi, sb = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t)); _, W = wvals(g, s, t)
        h = not oncycle(g, s, sb, o) and not oncycle(g, s, t, o) and Xi[o][0] == W[o][0]
        pk = (tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]); th, w = E.key(Xi[o]), E.key(W[o])
        d = Xi[o][1] ^ W[o][1]; us = (d.bit_length() - 1) if d else None
        rk = (pk, w, us) if h and th < w else None
        if prev is None or pk != prev[0]: ph = 0
        elif th != prev[1]: ph += 1
        if rk is None or prev is None or rk != prev[2]: run = 0
        elif th != prev[1]: run += 1
        brun, bph = max(brun, run), max(bph, ph); prev = (pk, th, rk)
        r = step(g, E, Ed, s, t)
        if r is None: break
        s, t = list(r[0]), list(r[1]); k += 1
    return brun, bph

def measure(g):
    c = Counter()
    coarsecheck.WITHFB = False; coarsecheck.run(g, None, c)
    c2 = Counter(); coarsecheck.WITHFB = True; coarsecheck.run(g, None, c2)
    c["leaves_fb"] = c2["leaves_fb"]
    for k in ("C1_fail", "C2_fail", "C3_fail", "C3_fail_after_fb"): c[k + "_withfb"] = c2[k]
    c["reentries_withfb"] = c2["reentries"]; c["reentries_no_ustar_withfb"] = c2["reentries_no_ustar"]
    fbfcheck.run(g, None, c); fbedges.run(g, None, c)
    nh, cyc = profile(g); c["max_nh_phase"] = nh; c["max_stretches_phase"] = cyc
    return c

def score(c, target):
    v = sum(c[k] + c[k + "_withfb"] for k in VIOL)
    ex = {"lemmas": c["throttled_fallbacks"] + c["checked_transitions"] + c["reentries_withfb"],
          "nh": c["max_nh_phase"], "cyc": c["max_stretches_phase"],
          "reent": (c["reentries"] + c["reentries_withfb"]) * 1000 + c["leaves_arena"] + c["leaves_fb"],
          "reentu": (c["reentries"] - c["reentries_no_ustar"] + c["reentries_withfb"] - c["reentries_no_ustar_withfb"]) * 1000
                    + c["reentries"] + c["leaves_arena"]}[target]
    return (v, ex)

def fit(G, target):
    if target == "cycu":
        n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(G[2][v]) > 1]
        if len(odd) != 1 or any(not x for x in G[2]): return (-1, -1), None
        g = pg.Game(*G)
        if not any(w in split(g, odd[0]) for w in G[2][odd[0]]): return (-1, -1), None
        try: a, b = cycu(g)
        except Exception: return (-1, -1), None
        return (a, b), {"cycu_run": a, "theta_changes_phase": b}
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
        g = load(sys.argv[sys.argv.index("--from") + 1]); G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]
        if "--pad" in sys.argv:
            for v in range(g.n, int(sys.argv[sys.argv.index("--pad") + 1])): G[0].append(0); G[1].append(0); G[2].append([v])
        n = len(G[0])
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
