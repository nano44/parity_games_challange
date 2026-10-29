#!/usr/bin/env python3
"""REFEREE successor 18: own control for packet P-N5-SF (L-NEW box 55, l-new 95a7a581, sha1 dbc2345f).
Own N5-SF on rl_engine (written from the packet's §0 definition of S4a'/S4b' and SPEC S1-S5; no lane code).
Checks per run (Even side on G; Odd side mirrored on G^d):
  TERM   the run stops with Is = It = 0; I <= (#s - 1) + (#t - 1); no strategy repeats (SF-TERM)
  CONF   S1 conformance: Xi_s(v) = play value of (s, sbar(s)) at every vertex (the standing premise behind ONE-PLAYER (a))
  ORB    distinct-s sequence = orbit of F from s_0 computed without tau; and a second run from the same s_0 with another t_0 gives the
         same distinct-s sequence (DECOUPLE); mirror for tau
  ONEP   at every s^(j): S1 on G_sbar gives Xi_s and the same I_s (ONE-PLAYER (a)); F(s) = rl_engine's N5 step on G_sbar from (s, sbar) (b)
  SEG    every stretch: b - a <= n + m, <= n - 1 Xi-changing transitions, an S4c transition inside a stretch is its last one and is Xi-flat
  TOT    #s - 1 < (n + m + 1)(1 + LAM + SBC), LAM <= n(n - 1); I < (n + m + 1)(2(n^2 - n + 1) + SBC); SBC <= 2I
MUT=1: S4a' uses tau (N5's own S4a) instead of sbar(s): ORB must fire. MUT=2: SEG with n - 1 in place of n + m (sharpness probe).
Usage: sf_probe.py rand N lo hi seed | FILES...   (env MAXN, RANDSTARTS)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE
MUT = int(os.environ.get("MUT", "0"))
EX = []


def fail(cnt, tag, *a):
    cnt[tag + "_V"] += 1
    if len(EX) < 30: EX.append((tag,) + a)


def cut(g, sb):
    """G_sbar: every owner-1 vertex keeps only (v, sb[v])"""
    return g.restrict([[sb[v]] if g.owner[v] == 1 else g.succ[v] for v in range(g.n)])


def side_info(g, s):
    """(Xi, sbar, I) for the owner-0 strategy s of g"""
    Xi, sb = RE.evaluate(g, s)
    return Xi, sb, RE.improving(g, Xi, s, 0)


def A_map(g, s, opp):
    """S4a': arena optimum of owner 0 against the owner-1 strategy opp (SPEC S4a with tau := opp)"""
    Xi, sb, I = side_info(g, s)
    A = {v: {s[v]} for v in range(g.n) if g.owner[v] == 0}
    for v, w in I: A[v].add(w)
    keep = [sorted(A[v]) if g.owner[v] == 0 else [opp[v]] for v in range(g.n)]
    _, ch = RE.evaluate(g.restrict(keep).dual(), [opp[v] if g.owner[v] == 1 else None for v in range(g.n)])
    return [ch[v] if g.owner[v] == 0 else None for v in range(g.n)]


def F_map(g, s):
    Xi, sb, I = side_info(g, s)
    assert I
    a = A_map(g, s, sb)
    if a != s: return a, False
    out = list(s)
    for v in range(g.n):
        cand = [w for (x, w) in I if x == v]
        if cand: out[v] = max(cand, key=lambda w: (g.key(Xi[w]), w))
    return out, True


def run_sf(g, s, t, maxit=20000):
    """N5-SF; returns states [(s, t, fb_even, fb_odd)]. Odd's side: owner-0 view on G^d (t is an owner-0 strategy of gd)."""
    gd = g.dual(); out = []
    for _ in range(maxit):
        Xi, sb, Is = side_info(g, s); Ut, tb, It = side_info(gd, t)
        out.append((list(s), list(t)))
        if not Is and not It: return out
        sn = A_map(g, s, (t if MUT == 1 else sb)) if Is else list(s)
        tn = A_map(gd, t, tb) if It else list(t)
        if sn == s and tn == t:
            if Is:
                for v in range(g.n):
                    c = [w for (x, w) in Is if x == v]
                    if c: sn[v] = max(c, key=lambda w: (g.key(Xi[w]), w))
            else:
                for v in range(g.n):
                    c = [w for (x, w) in It if x == v]
                    if c: tn[v] = max(c, key=lambda w: (gd.key(Ut[w]), w))
        s, t = sn, tn
    raise RuntimeError("maxit")


def distinct(seq):
    out = [seq[0]]
    for x in seq[1:]:
        if x != out[-1]: out.append(x)
    return out


def own_eq(g, a, b, own):
    return all(a[v] == b[v] for v in range(g.n) if g.owner[v] == own)


def check_side(cnt, g, seq, name, tag, rng, other_seq):
    """g: the game whose owner-0 player is this side (G for Even, G^d for Odd); seq: its distinct strategy sequence"""
    n, m = g.n, sum(len(x) for x in g.succ)
    infos = [side_info(g, s) for s in seq]
    p = len(seq) - 1
    # CONF
    for s, (Xi, sb, I) in zip(seq, infos):
        nx = [s[v] if g.owner[v] == 0 else sb[v] for v in range(n)]
        for v in range(n):
            cnt["CONF_chk"] += 1
            if RE.play_value(g, nx, v) != Xi[v]: fail(cnt, "CONF", name, tag, v)
    if infos[-1][2]: fail(cnt, "ORB_end", name, tag)
    # ORB (tau-free orbit)
    x = seq[0]; orb = [x]
    while side_info(g, x)[2]:
        x, _ = F_map(g, x); orb.append(x)
        if len(orb) > len(seq) + 5: break
    cnt["ORB_chk"] += 1
    if len(orb) != len(seq) or not all(own_eq(g, a, b, 0) for a, b in zip(orb, seq)): fail(cnt, "ORB", name, tag, len(orb), len(seq))
    # ONEP, SEG, TOT
    fbflag = []
    for j in range(p):
        Xi, sb, I = infos[j]; h = cut(g, sb)
        Xh, _ = RE.evaluate(h, seq[j]); Ih = RE.improving(h, Xh, seq[j], 0)
        cnt["ONEP_chk"] += 1
        if Xh != Xi or sorted(Ih) != sorted(I): fail(cnt, "ONEPa", name, tag, j)
        Fs, fb = F_map(g, seq[j]); fbflag.append(fb)
        # N5's step on G_sbar (rl_engine.run, first transition)
        nxt = n5_step(h, seq[j], sb)
        if not own_eq(g, nxt, Fs, 0) or not own_eq(g, Fs, seq[j + 1], 0): fail(cnt, "ONEPb", name, tag, j)
    lam = [tuple(x[0] for x in inf[0]) for inf in infos]; sbs = [tuple(inf[1][v] for v in range(n) if g.owner[v] == 1) for inf in infos]
    LAM = sum(1 for j in range(p) if lam[j + 1] != lam[j]); SBC = sum(1 for j in range(p) if sbs[j + 1] != sbs[j])
    a = 0; nseg = 0; segmax = 0
    while a <= p:
        b = a
        while b < p and lam[b + 1] == lam[a] and sbs[b + 1] == sbs[a]: b += 1
        nseg += 1; segmax = max(segmax, b - a); cnt["SEG_chk"] += 1
        lim = (n - 1) if MUT == 2 else (n + m)
        if b - a > lim: fail(cnt, "SEG" + ("_MUT2" if MUT == 2 else ""), name, tag, a, b, n, m)
        vc = sum(1 for j in range(a, b) if infos[j][0] != infos[j + 1][0])
        if vc > n - 1: fail(cnt, "SEGvc", name, tag, a, b, vc)
        for j in range(a, b):
            if fbflag[j]:
                cnt["SEG_fb_in"] += 1
                if j != b - 1: fail(cnt, "SEGfb_last", name, tag, j, b)
                if infos[j][0] != infos[j + 1][0]: fail(cnt, "SEGfb_flat", name, tag, j)
        a = b + 1
    cnt["TOT_chk"] += 1
    if not (p < (n + m + 1) * (1 + LAM + SBC) and LAM <= n * (n - 1)): fail(cnt, "TOT", name, tag, p, LAM, SBC)
    cnt["SBC_max"] = max(cnt["SBC_max"], SBC); cnt["segmax"] = max(cnt["segmax"], segmax)
    return p, SBC


def n5_step(h, s, sb):
    """N5's iteration (S4a with tau := sb, S4c Even branch; I_tau = 0 on h) on the one-player game h, from h's own S1 values"""
    Xi, _ = RE.evaluate(h, s); I = RE.improving(h, Xi, s, 0)
    A = {v: {s[v]} for v in range(h.n) if h.owner[v] == 0}
    for v, w in I: A[v].add(w)
    keep = [sorted(A[v]) if h.owner[v] == 0 else [sb[v]] for v in range(h.n)]
    _, ch = RE.evaluate(h.restrict(keep).dual(), [sb[v] if h.owner[v] == 1 else None for v in range(h.n)])
    sn = [ch[v] if h.owner[v] == 0 else None for v in range(h.n)]
    if sn == [x if h.owner[v] == 0 else None for v, x in enumerate(s)]:
        for v in range(h.n):
            c = [w for (x, w) in I if x == v]
            if c: sn[v] = max(c, key=lambda w: (h.key(Xi[w]), w))
    return sn


def analyse(cnt, g, s0, t0, name, rng):
    gd = g.dual(); n, m = g.n, sum(len(x) for x in g.succ)
    st = run_sf(g, s0, t0); I = len(st) - 1
    cnt["RUNS"] += 1; cnt["ITER"] += I
    S = distinct([x[0] for x in st]); T = distinct([x[1] for x in st])
    if len(set(map(tuple, S))) != len(S) or len(set(map(tuple, T))) != len(T): fail(cnt, "REP", name)
    if not I <= (len(S) - 1) + (len(T) - 1): fail(cnt, "TERM", name, I)
    pS, sbcS = check_side(cnt, g, S, name, "E", rng, None)
    pT, sbcT = check_side(cnt, gd, T, name, "O", rng, None)
    SBC = sbcS + sbcT
    if not (I < (n + m + 1) * (2 * (n * n - n + 1) + SBC) and SBC <= 2 * I): fail(cnt, "TOTI", name, I, SBC)
    # DECOUPLE across starts: same s0, another t0 (each Odd vertex's last successor), and same t0, another s0
    t1 = [g.succ[v][-1] if g.owner[v] == 1 else None for v in range(n)]
    s1 = [g.succ[v][-1] if g.owner[v] == 0 else None for v in range(n)]
    S2 = distinct([x[0] for x in run_sf(g, s0, t1)]); T2 = distinct([x[1] for x in run_sf(g, s1, t0)])
    cnt["TAU_chk"] += 1
    if len(S2) != len(S) or not all(own_eq(g, a, b, 0) for a, b in zip(S, S2)): fail(cnt, "TAU_E", name)
    if len(T2) != len(T) or not all(own_eq(g, a, b, 1) for a, b in zip(T, T2)): fail(cnt, "TAU_O", name)


def main(a):
    import core_probe as CP, dual_probe as D
    cnt = Counter(); rng = random.Random(55); nst = int(os.environ.get("RANDSTARTS", "1"))
    def do(g, name, extra=None):
        r = random.Random(name)
        starts = ([extra] if extra else []) + [RE.best_reward_start(g)] + [D.rand_start(g, r) for _ in range(nst)]
        for s0, t0 in starts:
            try: analyse(cnt, g, list(s0), list(t0), name, rng)
            except RuntimeError: cnt["maxit"] += 1
            except AssertionError as e: fail(cnt, "ASSERT", name, str(e))
    if a[0] == "rand":
        N, lo, hi, seed = map(int, a[1:5]); r2 = random.Random(seed)
        for i in range(N):
            nn = r2.randint(lo, hi)
            do(D.rand_ck(r2, nn, r2.randint(0, min(5, nn - 1))), "rand%d" % i)
    else:
        for path in a:
            if path.endswith(".start"): continue
            try: g = RE.parse(path)
            except Exception: cnt["parse_err"] += 1; continue
            if g.n > int(os.environ.get("MAXN", "64")): cnt["skip_big"] += 1; continue
            sp = path[:-3] + ".start"; ex = None
            if os.path.exists(sp):
                try: ex = CP.parse_start(g, sp)
                except Exception: cnt["start_err"] += 1
            if ex is not None and (None in [ex[0][v] for v in range(g.n) if g.owner[v] == 0] or None in [ex[1][v] for v in range(g.n) if g.owner[v] == 1]):
                cnt["start_incomplete"] += 1; ex = None
            cnt["GAMES"] += 1; do(g, os.path.relpath(path), ex)
    for k in sorted(cnt): print(k, cnt[k])
    print("VIOLATIONS", sum(v for k, v in cnt.items() if k.endswith("_V")))
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
