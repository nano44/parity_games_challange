#!/usr/bin/env python3
"""L-RED 67 R237 (2), second part: instances AIMED at single sentences of Lemma WRAP's proof (L-SI 52 box 104 section 3, step (W4) first),
run through WRAP's six must-0 counters on both own engines (w237.check «x», «s»), the N5 counters of WRAP (v) / Remark (3)
(w237.check_spec) and box 104's own check (second engine: box 190 n5v xi on si.Engine).
Families (unit: one (H, s0)):
 perm VER n K SEED   Friedmann's G_n (arXiv 1106.0778v2, box 104's lmcs_game, VER fig4|table4) under K random renumberings of its
                     vertices. Aimed at «the ranks of H's vertices are ordered in W as in H» and at every index tie-break of the
                     engines (pads are numbered after V in the order of the renumbered edges): the run must stay Howard's, T + 3.
 fperm n K SEED      the same for PGSolver's switchallexp_n (box 104's fried_game).
 eqprio K SEED NMAX  random games whose priorities take ONE value (all 0, all 1) or two values: rank ties by index only. Aimed at
                     (W4) (b) «the pointwise minimum is unique as a value» and at the order isomorphism under equal priorities.
 oneowner K SEED NMAX  all-Even games (no Odd reply: (W4) (a) is empty) and all-Odd games (V_E empty: T = 0, the run is the endgame).
 loops K SEED NMAX   every vertex has a self-loop (cycle nodes everywhere; (W1), (c) with w = v).
 optstart K SEED NMAX  s0 := the last strategy of Howard's run on H (T = 0: the first fallback is iteration 1).
 big K SEED NMIN NMAX  larger random games (|W| in the thousands).
 plen K SEED NMAX    (L-RED 68) a DAG (successors of i among j < i) into ONE cycle node c with a self-loop and the TOP priority (n,
                     parity alternating over the K games), every other priority < n: every play's P is empty, so SPEC's LENGTH
                     component decides every comparison. Aimed at «(c, P, l) -> (c, P, 6 l) is strictly order-preserving» and (c)'s 6 l + 5.
 pset K SEED NMAX    (L-RED 68) the same DAG into ONE cycle node c with the LOWEST priority (0 or 1), the others distinct priorities
                     2..n+1 (TARGET.md section 1 allows priorities up to 2n+2 here: the order is what matters): P-sets decide. Aimed at
                     «through vertices that are in no P-set (W1) ... same P» and at Q1 (the top differing vertex decides).
Env: BOX104, LNEW, LRED, LLIT (as wr237.py); CTRL=1 (wr237's control). Output: one summary line per call."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import w237 as Wm
R = Wm.R
import pg, gen
KEYS = Wm.KEYS; SKEYS = Wm.SKEYS

def permute(H, s0, rng):
    n = H.n; p = list(range(n)); rng.shuffle(p)          # old vertex v becomes p[v]
    prio = [0] * n; owner = [0] * n; succ = [None] * n; t0 = [-1] * n
    for v in range(n):
        prio[p[v]] = H.prio[v]; owner[p[v]] = H.owner[v]; succ[p[v]] = sorted(p[w] for w in H.succ[v])
        t0[p[v]] = p[s0[v]] if H.owner[v] == 0 else -1
    return pg.Game(prio, owner, succ), t0

def howard_last(H, s0):
    """Howard's run on H by H's own valuation (wr237.hval); returns its last strategy"""
    s = list(s0)
    while True:
        V, vals = R.hval(H, [s[v] if H.owner[v] == 0 else None for v in range(H.n)]); ch = False
        for v in range(H.n):
            if H.owner[v] != 0: continue
            b = s[v]
            for w in H.succ[v]:
                if V.better(vals[w], vals[b]): b = w
            if b != s[v]: s[v] = b; ch = True
        if not ch: return s

def rnd(rng, n, prios, owners=None, loops=False):
    owner = [rng.randint(0, 1) if owners is None else owners for _ in range(n)]
    succ = [sorted(set(rng.sample(range(n), rng.randint(1, min(n, 4)))) | ({v} if loops else set())) for v in range(n)]
    H = pg.Game([rng.choice(prios) for _ in range(n)], owner, succ)
    return H, [rng.choice(H.succ[v]) if H.owner[v] == 0 else -1 for v in range(n)]

def family(args):
    m = args[0]
    if m == "perm":
        ver, n, K, seed = args[1], int(args[2]), int(args[3]), int(args[4]); rng = random.Random(seed); H, s0 = R.WR.lmcs_game(n, ver)
        yield H, s0
        for _ in range(K): yield permute(H, s0, rng)
    elif m == "fperm":
        n, K, seed = int(args[1]), int(args[2]), int(args[3]); rng = random.Random(seed); H, s0, _ = R.WR.fried_game(n)
        yield H, s0
        for _ in range(K): yield permute(H, s0, rng)
    elif m in ("eqprio", "oneowner", "loops", "optstart"):
        K, seed, nmax = int(args[1]), int(args[2]), int(args[3]); rng = random.Random(seed)
        for i in range(K):
            n = rng.randint(1, nmax)
            if m == "eqprio": yield rnd(rng, n, [[0], [1], [0, 1], [1, 2], [0, 2], [1, 3]][i % 6])
            elif m == "oneowner": yield rnd(rng, n, list(range(n + 1)), owners=i % 2)
            elif m == "loops": yield rnd(rng, n, list(range(n + 1)), loops=True)
            else:
                H, s0 = rnd(rng, n, list(range(n + 1))); yield H, howard_last(H, s0)
    elif m in ("plen", "pset"):
        K, seed, nmax = int(args[1]), int(args[2]), int(args[3]); rng = random.Random(seed)
        for i in range(K):
            n = rng.randint(2, nmax); c = 0; owner = [rng.randint(0, 1) for _ in range(n)]
            succ = [[0]] + [sorted(set(rng.sample(range(v), rng.randint(1, min(v, 3))))) for v in range(1, n)]
            if m == "plen": prio = [n - (i % 2)] + [rng.randint(0, n - 2) for _ in range(1, n)]
            else:
                hi = list(range(2, n + 1)); rng.shuffle(hi); prio = [i % 2] + hi
            H = pg.Game(prio, owner, succ); yield H, [rng.choice(H.succ[v]) if H.owner[v] == 0 else -1 for v in range(n)]
    elif m == "big":
        K, seed, nmin, nmax = int(args[1]), int(args[2]), int(args[3]), int(args[4]); rng = random.Random(seed)
        for _ in range(K):
            n = rng.randint(nmin, nmax); H = gen.random_game(n, rng.randint(2, n + 1), 1, 4, rng.randrange(10 ** 9))
            yield H, [rng.choice(H.succ[v]) if H.owner[v] == 0 else -1 for v in range(n)]
    else: raise SystemExit("unknown family")

if __name__ == "__main__":
    tot = {k: 0 for k in KEYS}; spec = {k: 0 for k in SKEYS}; sec = {k: 0 for k in KEYS}; games = 0; Ts = set(); tied = 0; xdiff = 0; maxW = 0; maxF = 0; sumT = 0; w4 = {k: 0 for k in Wm.WKEYS}; W1 = 0
    for H, s0 in family(sys.argv[1:]):
        c, T, its, wn = Wm.check(H, s0, "s"); c2, T2, its2, _ = Wm.check(H, s0, "x"); cv, F, itv, _ = Wm.check_spec(H, s0); c3, T3, its3, _ = Wm.second(H, s0); cw, w1, _ = Wm.check_w4(H, s0); W1 += w1
        for k in Wm.WKEYS: w4[k] += cw[k]
        games += 1; Ts.add(T); tied += int((T, its) != (T2, its2)); xdiff += int((T, its) != (T3, its3)); maxW = max(maxW, wn); maxF = max(maxF, F); sumT += T
        for k in KEYS: tot[k] += c[k] + c2[k]; sec[k] += c3[k]
        for k in SKEYS: spec[k] += cv[k]
        if sum(c.values()) + sum(c2.values()) + sum(cv.values()) + sum(c3.values()) + sum(cw.values()):
            print("AIM237 CANDIDATE", dict(prio=H.prio, owner=H.owner, succ=H.succ, s0=s0), c, c2, cv, c3, flush=True)
    print("AIM237 " + " ".join(sys.argv[1:]) + f": games {games} | own engines x + s: " + " ".join(f"{k} {tot[k]}" for k in KEYS)
          + f" | T values {sorted(Ts)[:6]}{'...' if len(Ts) > 6 else ''} ({len(Ts)} distinct) sumT {sumT} tiediff(x,s) {tied} max|W| {maxW}"
          + " | N5 (spec): " + " ".join(f"{k} {spec[k]}" for k in SKEYS) + f" maxF {maxF}"
          + " | (W4)-(W6): " + " ".join(f"{k} {w4[k]}" for k in Wm.WKEYS) + f" (W-1 starts {W1})"
          + " | second engine (n5v xi): " + " ".join(f"{k} {sec[k]}" for k in KEYS) + f" xdiff(s, n5v) {xdiff} | ctrl {R.CTRL}", flush=True)
