#!/usr/bin/env python3
"""REFEREE succ. 16 probe for P-N5-OFFMONO-add3-box49 (sha1 b7cd0ff1, l-new 8b7e2e6e, trunk pin 77f2664e). Own engine (rl_engine;
offmono_probe's kap / kwt / par; zch_probe's Z_t(c)). No lane code. Per phase P, class c, in-phase transition t -> t+1, q in Q n U - {c},
p := par_{t+1}(q), y1 := sigmabar_t(q), y2 := sigmabar_{t+1}(q):
 OMP    OFFSET-MONO+ : off_{t+1}(q; p) >= off_t(q; p), at EVERY q (counted separately for q on an honest cycle at t, the new case)
 RED    on-cycle q: kappa_t(y2) >= kappa_t(y1) (the reduced claim of the proof), with the case: L1 (y2's t-play meets q before c), L2a (meets q
        after c, P(Xi_t y2) != {}: then kappa_t(y2) > kappa_t(y1) strictly is claimed), L2b (after c, P = {}); Y2Q counts y2 = q (excluded by
        the proof) and NOMEET counts plays that never meet q (excluded)
 ST1    Step 1 at y2: off_{t+1}(y2; p) >= off_t(y2; p)
 CC3    CHAIN-COUNT''' sum form and D form (D := max v_x over x-pieces''' = cut at EXIT_x only) on J := the phase
Mutations: MUT=1 p := a vertex off q's (t+1)-play (the lane's control; must bite at on-cycle checks); MUT=2 opposite length sign
(offmono_probe's own MUT=2, kappa flipped; must bite). Usage: add3_probe.py rand N nmin nmax kmax seed | files[:start]...  (RANDSTARTS, MAXN, NOS3)"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rl_engine as RE, dual_probe as D
import offmono_probe as OM
from zch_probe import Zc
from flip_probe import nxt
from gcx_probe import load_start
EX = []
MUT = int(os.environ.get("MUT", "0"))
OM.MUT = 2 if MUT == 2 else 0


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def analyse(g, start, cnt, name):
    st = RE.run(g, start); n = g.n
    Q = {v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) > 1}
    for x in st: x["nx"] = nxt(g, x["s"], x["sb"])
    K = len(st); k = 0
    while k < K:
        j = k; lam = tuple(v[0] for v in st[k]["Xi"])
        while j + 1 < K and tuple(v[0] for v in st[j + 1]["Xi"]) == lam and st[j + 1]["t"] == st[k]["t"]: j += 1
        if j > k: phase(g, st, k, j, lam, Q, cnt, name)
        k = j + 1


def tplay(nx, y, c):
    seq = []; x = y; seen = set()
    while x not in seen:
        seen.add(x); seq.append(x); x = nx[x]
    return seq


def phase(g, st, a, b, lam, Q, cnt, name):
    n = g.n
    for c in sorted(set(lam)):
        U = {v for v in range(n) if lam[v] == c}
        Qc = sorted((Q & U) - {c})
        if not Qc: continue
        Kp = lambda t, z: OM.kap(g, c, st[t]["Xi"][z])
        par = lambda t, x: OM.par(st[t]["nx"], Q, x, c)
        for t in range(a, b):
            Zs = set(Zc(st[t]["nx"], c))
            for q in Qc:
                p = par(t + 1, q)
                if MUT == 1:
                    onp = set(tplay(st[t + 1]["nx"], q, c))
                    off = [z for z in sorted(U) if z not in onp]
                    if not off: continue
                    p = off[0]
                o0, o1 = OM.sub(Kp(t, q), Kp(t, p)), OM.sub(Kp(t + 1, q), Kp(t + 1, p))
                oncyc = q in Zs
                tag = "cyc" if oncyc else "nocyc"
                cnt["OMP_chk_" + tag] += 1
                if o1 < o0: fail(cnt, "OMP_" + tag, name, t, c, q, p)
                if not oncyc or MUT: continue
                y1, y2 = st[t]["sb"][q], st[t + 1]["sb"][q]
                if y2 == q: cnt["Y2Q"] += 1; continue
                pl = tplay(st[t]["nx"], y2, c)
                if q not in pl: cnt["NOMEET"] += 1; fail(cnt, "RED_nomeet", name, t, c, q); continue
                iq = pl.index(q); ic = pl.index(c) if c in pl else None
                if ic is None or iq < ic: case = "L1"
                else: case = "L2a" if st[t]["Xi"][y2][1] != 0 else "L2b"
                cnt["RED_" + case] += 1
                if case in ("L1", "L2a") and len(EX) < 40: EX.append((case, name, t, c, q, y1, y2, p))
                if Kp(t, y2) < Kp(t, y1): fail(cnt, "RED_" + case, name, t, c, q)
                if case == "L2a" and not Kp(t, y2) > Kp(t, y1): fail(cnt, "RED_L2a_strict", name, t, c, q)
                s0, s1 = OM.sub(Kp(t, y2), Kp(t, p)), OM.sub(Kp(t + 1, y2), Kp(t + 1, p))
                cnt["ST1_chk"] += 1
                if s1 < s0: fail(cnt, "ST1", name, t, c, q)
        if MUT: continue
        EXIT = {x: {t for t in range(a, b) if par(t, x) != par(t + 1, x)} for x in Qc}
        sumv = {}; Dm = 1
        for x in Qc:
            tot = 0; t = a
            while t < b:
                if t in EXIT[x]: t += 1; continue
                s = t
                while t < b and t not in EXIT[x]: t += 1
                pp = par(s, x)
                seq = [OM.sub(Kp(k2, x), Kp(k2, pp)) for k2 in range(s, t + 1)]
                tot += len(set(seq)) - 1; Dm = max(Dm, len(set(seq)))
                if any(seq[i + 1] < seq[i] for i in range(len(seq) - 1)): fail(cnt, "CC3_mono", name, s, c, x)
            sumv[x] = tot
        cnt["MAX_D"] = max(cnt["MAX_D"], Dm)
        for q in Qc:
            chg = sum(1 for t in range(a, b) if Kp(t, q) != Kp(t + 1, q))
            sform = sum(len(EXIT[x]) + sumv[x] for x in Qc)
            dform = sum(Dm * (len(EXIT[x]) + 1) for x in Qc)
            cnt["CC3_chk"] += 1; cnt["SUM_kchg"] += chg
            if chg > sform or chg > dform: fail(cnt, "CC3", name, a, c, q, chg, sform, dform)


def main(a):
    cnt = Counter(); rng = random.Random(4950); nst = int(os.environ.get("RANDSTARTS", "2"))
    def do(g, name, r, extra=None):
        starts = ([extra] if extra else []) + ([] if (extra and os.environ.get("NOS3")) else [RE.best_reward_start(g)]) + \
                 [D.rand_start(g, r) for _ in range(nst)]
        for j, s0 in enumerate(starts):
            cnt["RUNS"] += 1; analyse(g, s0, cnt, "%s/%d" % (name, j))
    if a[0] == "rand":
        N, lo, hi, km, seed = map(int, a[1:6]); r2 = random.Random(seed)
        for i in range(N):
            nn = r2.randint(lo, hi)
            do(D.rand_ck(r2, nn, r2.randint(0, min(km, nn - 1))), "rand%d" % i, rng)
    else:
        for f in a:
            path, _, sp = f.partition(":")
            if path.endswith(".start"): continue
            try: g = RE.parse(path)
            except Exception: cnt["parse_err"] += 1; continue
            if g.n > int(os.environ.get("MAXN", "40")): cnt["skip_big"] += 1; continue
            if not sp and os.path.exists(path[:-3] + ".start"): sp = path[:-3] + ".start"
            ex = None
            if sp:
                try: ex = load_start(g, sp)
                except Exception: cnt["start_err"] += 1
            do(g, os.path.relpath(path), random.Random(os.path.relpath(path)), ex)
    for k in sorted(cnt): print(k, cnt[k])
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
