#!/usr/bin/env python3
"""REFEREE successor 20: own control for packet P-N5-FIXD (L-NEW box 91; sources box 77 FIX-DEPTH / PHASE-RED, box 79 FLAT-SW / PHASE-RED').
Own engine rl_engine (SPEC S1-S5 from the text; no lane code). N5-LZC via wch_probe's one-line patch of rl_engine.run (--lzc).
Phase = maximal run of states with (lambda_Xi, tau) constant (RESULTS R38 (a)); PH=tau: tau only. fin := Xi_b (last state of the phase).
DEPTH_t(v) := leading coordinates of Xi_t(v) equal to fin(v) in the sequence (cycle node reward; rank n-1 .. 0 path bit; signed length);
n + 2 if Xi_t(v) = fin(v). K_t := sum_v DEPTH_t(v).
  XM    Xi_t(v) <= Xi_t'(v) <= fin(v) (key order) for consecutive t < t' in P   (R15 (a) input to FIXD-MON)
  KM    FIXD-MON: DEPTH_t(v) never decreases inside a phase (per vertex), K never decreases
  ST    longest run of consecutive in-phase transitions with Xi unchanged <= 4n(n-1)   (R15 (d))
  PR    PHASE-RED: |P| <= (4n(n-1)+1)(CH_P+1), CH_P <= n(n+2) + FLATTR_P, FLATTR_P <= sum_v FLAT_P(v)
  FLSWall  per (x, phase): switches of Even x in flat transitions keeping DEPTH(x) (box 79's FLATSW_P(x); FLSW = one charged x per transition)
  SW    FLAT-SW: every FLATTR transition has a switched Even x with Xi(x) changed;  PR'  PHASE-RED' bound
|P| := in-phase transitions = b - a.
MUT: 1 reference Xi_a instead of fin (KM should fail); 2 stall bound n instead of 4n(n-1); 3 CH <= FLATTR (drop n(n+2));
     4 FLAT-SW only through switched x whose old successor is Even (should fail).   Usage: fixd_probe.py [--lzc] FILES... | rand N lo hi seed"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE
import wch_probe as WP
MUT = int(os.environ.get("MUT", "0"))
PHT = os.environ.get("PH") == "tau"
LZ = "--lzc" in sys.argv
EX = []
STAT = Counter()


def fail(cnt, tag, *a):
    cnt[tag + "_V"] += 1
    if len(EX) < 30: EX.append((tag,) + a)


def depth(g, x, f):
    if x == f: return g.n + 2
    if x[0] != f[0]: return 0
    for r in range(g.n - 1, -1, -1):
        if ((x[1] >> r) & 1) != ((f[1] >> r) & 1): return 1 + (g.n - 1 - r)
    return g.n + 1          # same cycle node and path set, different length


def phases(st):
    key = lambda s: (tuple(s["t"]), None if PHT else tuple(x[0] for x in s["Xi"]))
    out, a = [], 0
    for k in range(1, len(st) + 1):
        if k == len(st) or key(st[k]) != key(st[a]): out.append((a, k - 1)); a = k
    return out


def analyse(cnt, g, start, name):
    st = (WP.run_lzc if LZ else RE.run)(g, start)
    n = g.n; stallmax = n if MUT == 2 else 4 * n * (n - 1)
    for (a, b) in phases(st):
        L = b - a; cnt["phases"] += 1; cnt["trans"] += L
        if L == 0: continue
        fin = st[b]["Xi"]; ref = st[a]["Xi"] if MUT == 1 else fin
        D = [[depth(g, st[k]["Xi"][v], ref[v]) for v in range(n)] for k in range(a, b + 1)]
        K = [sum(r) for r in D]
        CH = FLATTR = FSW = 0; stall = run = 0; FLAT = Counter(); FLSW = Counter(); FLSWA = Counter()
        for k in range(a, b):
            X0, X1 = st[k]["Xi"], st[k + 1]["Xi"]
            for v in range(n):
                k0, k1, kf = g.key(X0[v]), g.key(X1[v]), g.key(fin[v])
                if not (k0 <= k1 <= kf): fail(cnt, "XM", name, k, v)
                if D[k + 1 - a][v] < D[k - a][v]: fail(cnt, "KM", name, k, v)
            ch = [v for v in range(n) if X0[v] != X1[v]]
            if not ch:
                run += 1; stall = max(stall, run); continue
            run = 0; CH += 1
            for v in ch:
                if D[k + 1 - a][v] == D[k - a][v]: FLAT[v] += 1
            if K[k + 1 - a] > K[k - a]: cnt["krise"] += 1; continue
            FLATTR += 1
            sw = [x for x in ch if g.owner[x] == 0 and st[k]["s"][x] != st[k + 1]["s"][x] and (MUT != 4 or g.owner[st[k]["s"][x]] == 0)]
            for x in ch:
                if g.owner[x] == 0 and st[k]["s"][x] != st[k + 1]["s"][x] and D[k + 1 - a][x] == D[k - a][x]: FLSWA[x] += 1
            if sw: FSW += 1; FLSW[min(sw)] += 1
            else: fail(cnt, "SW", name, k, ch[:6])
        cnt["CH"] += CH; cnt["FLATTR"] += FLATTR; cnt["FSW"] += FSW
        if stall > stallmax: fail(cnt, "ST", name, a, b, stall)
        if L > (4 * n * (n - 1) + 1) * (CH + 1): fail(cnt, "PR1", name, a, b)
        if CH > (0 if MUT == 3 else n * (n + 2)) + FLATTR: fail(cnt, "PR2", name, a, b, CH, FLATTR)
        if FLATTR > sum(FLAT.values()): fail(cnt, "PR3", name, a, b)
        if L > (4 * n * (n - 1) + 1) * (n * (n + 2) + sum(FLSW.values()) + 1): fail(cnt, "PRp", name, a, b)
        STAT["maxstall"] = max(STAT["maxstall"], stall); STAT["maxFLATTR"] = max(STAT["maxFLATTR"], FLATTR)
        if FLAT:
            v, c = FLAT.most_common(1)[0]
            if c > STAT["maxFLAT"]: STAT["maxFLAT"] = c; STAT["maxFLAT_at"] = "%s n%d v%d ph[%d,%d] len%d" % (name, n, v, a, b, L)
        if FLSWA:
            x, c = FLSWA.most_common(1)[0]
            if c > STAT["maxFLSWall"]: STAT["maxFLSWall"] = c; STAT["maxFLSWall_at"] = "%s n%d x%d ph[%d,%d]" % (name, n, x, a, b)
        if FLSW: STAT["maxFLSW"] = max(STAT["maxFLSW"], FLSW.most_common(1)[0][1])


def main(a):
    import core_probe as CP
    a = [x for x in a if x != "--lzc"]
    cnt = Counter()
    def do(g, name, extra=None):
        if os.environ.get("STARTF"): extra = CP.parse_start(g, os.environ["STARTF"])
        starts = ([extra] if extra and not os.environ.get("NOSTART") else []) + ([] if os.environ.get("ONLYSTART") and extra else [RE.best_reward_start(g)])
        for s0 in starts:
            try: analyse(cnt, g, s0, name)
            except RuntimeError: cnt["maxit"] += 1
    if a[0] == "rand":
        import dual_probe as D
        N, lo, hi, seed = map(int, a[1:5]); r2 = random.Random(seed)
        for i in range(N):
            nn = r2.randint(lo, hi)
            do(D.rand_ck(r2, nn, r2.randint(0, min(5, nn - 1))), "rand%d" % i)
    else:
        for path in a:
            if path.endswith(".start"): continue
            try: g = RE.parse(path)
            except Exception: cnt["parse_err"] += 1; continue
            if g.n > int(os.environ.get("MAXN", "200")): cnt["skip_big"] += 1; continue
            sp = path[:-3] + ".start"; ex = None
            if os.path.exists(sp):
                try: ex = CP.parse_start(g, sp)
                except Exception: cnt["start_err"] += 1
            cnt["GAMES"] += 1; do(g, os.path.relpath(path), ex)
    for k in sorted(cnt): print(k, cnt[k])
    for k in sorted(STAT): print("STAT", k, STAT[k])
    print("VIOLATIONS", sum(v for k, v in cnt.items() if k.endswith("_V")))
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
