#!/usr/bin/env python3
"""REFEREE succ. 16 probe for packet P-N5-RESTRICT (docs/new/P-N5-RESTRICT-box48.md, sha1 48c63a8e, freeze l-new 7e56744a). Own engine:
rl_engine.run (N5 = SPEC) and epr_probe's N5^tau step (written by REFEREE succ. 12 from SPEC with S4b^tau). No lane code.
Per phase P = (x..y) of N5 on G ((lambda_Xi, tau) constant), the cuts H and runs J tested:
 GP    G^P (Odd v keeps tau(v) and every sigma-bar_k(v), k in P), J = P
 GUJ   G^{u|J} for every u in Q and every maximal frozen-side u-stretch J of P (sigma-bar constant on Q - {u})
 GU    G^u for every u in Q and every maximal u-run J of P (D_k <= {u})
 GE    G'_E for every epoch E of P (sigma-bar constant on Q)           (R64's own case)
 RH    RANDH random H-admissible cuts: G^P plus each other Odd edge kept with probability 1/2, J = P
For each (H, J): R1-R4 = RESTRICT_H (i)-(iv) at every k in J; REP = REPRO_H (N5^tau on H from (sigma_x, tau) gives sigma_{x+1..y'}, tau,
and the fallback flags, len(J) transitions); ONEPH = lambda' at x..y equals lambda; UNLESS = when y -> y' is in-phase and sigma-bar_{y'} is
an Odd strategy of H, lambda' at y' = lambda (REPRO_H's "unless" clause); EXITLAM (count) = y' in-phase but lambda' at y' differs.
EXT (count, G^P only): the N5^tau run on G^P takes one more step from y and stays in the phase (lambda', tau): the N5^tau phase on G^P is
then strictly longer than P (the equality reading of "EVERY PHASE ... IS ONE N5^tau PHASE ON G^P" would fail; containment holds).
QP, XDEG of G^P; NQ = |Q| of G (the brief's point on §4's first READING).
Mutation MUT=1: G^P without (v, sigma-bar_x(v)) for the first v with sigma-bar_x(v) != tau(v) (P2 fails at x; must bite).
Usage: restrict_probe.py rand N nmin nmax kmax seed | files[:start]...  (env RANDSTARTS 2, MAXN 40, NOS3, FAMS=GP,GUJ,GU,GE,RH)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, dual_probe as D
from epr_probe import wval, s4a, s4b_arena, gates, n5tau_step
from gcx_probe import load_start
EX = []
MUT = int(os.environ.get("MUT", "0"))
FAMS = set(os.environ.get("FAMS", "GP,GUJ,GU,GE,RH").split(","))


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def check(g, st, info, H, x, y, p1, fam, cnt, name):
    n = g.n; t = list(st[x]["t"]); lam = info[x]["lam"]
    inph = y < p1
    L = (y - x) + (1 if inph else 0)
    cnt[fam + "_runs"] += 1
    Eg = {(v, w) for v in range(n) for w in H.succ[v]}
    for k in range(x, y + 1):
        s = st[k]["s"]
        Xi, sb, Is, It, _ = gates(g, s, t)
        Xp, sbp, Isp, Itp, _ = gates(H, s, t)
        cnt[fam + "_Rchk"] += 1
        if Xp != Xi or wval(H, s, t) != wval(g, s, t): fail(cnt, fam + "_R1", name, k)
        if sorted(Isp) != sorted(Is): fail(cnt, fam + "_R2", name, k)
        elif Is and s4a(H, s, t, Isp) != s4a(g, s, t, Is): fail(cnt, fam + "_R2out", name, k)
        if sorted(Itp) != sorted(e for e in It if e in Eg): fail(cnt, fam + "_R3", name, k)
        if k < p1 and Itp:
            Ha, val, _ = s4b_arena(H, s, t, Itp)
            cnt[fam + "_R4chk"] += 1
            if wval(Ha, s, t) != val: fail(cnt, fam + "_R4", name, k)
    s, tt = list(st[x]["s"]), list(t); ok = True
    for kk in range(x, x + L):
        r = n5tau_step(H, s, tt)
        if r is None: ok = False; break
        sn, tn, fb, dv = r
        if sn != list(st[kk + 1]["s"]) or tn != t or fb != bool(st[kk]["fb"]): ok = False; break
        if kk + 1 <= y:
            Xk, _ = RE.evaluate(H, sn)
            if tuple(v[0] for v in Xk) != lam: fail(cnt, fam + "_ONEPH", name, kk + 1)
        s, tt = sn, tn
    cnt[fam + "_REPchk"] += 1; cnt[fam + "_REPtrans"] += L
    if not ok: fail(cnt, fam + "_REP", name, x, y); return
    if inph:
        yp = y + 1
        Xy, _ = RE.evaluate(H, st[yp]["s"])
        lam_y = tuple(v[0] for v in Xy)
        adm = all(info[yp]["sb"][v] in H.succ[v] for v in range(n) if g.owner[v] == 1)
        if adm:
            cnt[fam + "_UNLESSchk"] += 1
            if lam_y != lam: fail(cnt, fam + "_UNLESS", name, x, y)
        elif lam_y != lam: cnt[fam + "_EXITLAM"] += 1
    if fam == "GP" and ok:
        r = n5tau_step(H, s, tt)
        cnt["GP_EXTchk"] += 1
        if r is not None:
            Xn, _ = RE.evaluate(H, r[0])
            if tuple(v[0] for v in Xn) == lam and r[1] == t:
                cnt["GP_EXT"] += 1
                if cnt["GP_EXT_ex"] < 3: cnt["GP_EXT_ex"] += 1; EX.append(("GP_EXT", name, x, y))


def analyse(g, start, cnt, name, rng):
    st = RE.run(g, start); n = g.n
    Q = [v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) > 1]
    info = []
    for a in st:
        Xi, sb = RE.evaluate(g, a["s"]); info.append(dict(Xi=Xi, sb=sb, lam=tuple(x[0] for x in Xi)))
    T_ = len(st) - 1
    key = [(info[k]["lam"], tuple(st[k]["t"])) for k in range(T_ + 1)]
    k = 0
    while k <= T_:
        j = k
        while j < T_ and key[j] == key[j + 1]: j += 1
        p0, p1 = k, j; k = j + 1
        if p1 == p0: continue
        cnt["phases"] += 1; cnt["inphase_trans"] += p1 - p0
        t = list(st[p0]["t"])
        def cut(keep):  # keep[v] = set of Odd successors
            return RE.Game(list(g.prio), list(g.owner), [list(g.succ[v]) if g.owner[v] == 0 else sorted(keep[v]) for v in range(n)])
        used = {v: {t[v]} | {info[q]["sb"][v] for q in range(p0, p1 + 1)} for v in range(n) if g.owner[v] == 1}
        QP = sum(1 for v in used if len(used[v]) >= 2); XD = sum(len(used[v]) - 1 for v in used)
        cnt["MAX_QP"] = max(cnt["MAX_QP"], QP); cnt["MAX_XDEG"] = max(cnt["MAX_XDEG"], XD); cnt["MAX_NQ"] = max(cnt["MAX_NQ"], len(Q))
        if QP >= 2: cnt["phases_QP2"] += 1
        if QP < len(Q): cnt["phases_QP_lt_NQ"] += 1
        if p1 - p0 >= 60 and cnt["longph_ex"] < 6:
            cnt["longph_ex"] += 1; EX.append(("LONGPHASE", name, p0, p1, "QP", QP, "NQ", len(Q), "XDEG", XD))
        if "GP" in FAMS:
            kp = {v: set(used[v]) for v in used}
            if MUT == 1:
                bad = next((v for v in range(n) if g.owner[v] == 1 and info[p0]["sb"][v] != t[v]), None)
                if bad is None: cnt["MUT_novictim"] += 1
                else: kp[bad].discard(info[p0]["sb"][bad]); cnt["MUT_applied"] += 1
            check(g, st, info, cut(kp), p0, p1, p1, "GP", cnt, name)
        if "RH" in FAMS:
            kp = {v: set(used[v]) | {w for w in g.succ[v] if rng.random() < 0.5} for v in used}
            check(g, st, info, cut(kp), p0, p1, p1, "RH", cnt, name)
        if "GE" in FAMS:
            s_ = p0
            while s_ <= p1:
                e_ = s_
                while e_ < p1 and all(info[e_ + 1]["sb"][q] == info[s_]["sb"][q] for q in Q): e_ += 1
                kp = {v: ({t[v], info[s_]["sb"][v]}) for v in used}
                check(g, st, info, cut(kp), s_, e_, p1, "GE", cnt, name); s_ = e_ + 1
        for u in Q:
            if "GUJ" in FAMS:
                s_ = p0
                while s_ <= p1:
                    e_ = s_
                    while e_ < p1 and all(info[e_ + 1]["sb"][q] == info[s_]["sb"][q] for q in Q if q != u): e_ += 1
                    kp = {v: (set(g.succ[v]) if v == u else {t[v], info[s_]["sb"][v]}) for v in used}
                    check(g, st, info, cut(kp), s_, e_, p1, "GUJ", cnt, name); s_ = e_ + 1
            if "GU" in FAMS:
                s_ = p0
                while s_ <= p1:
                    if any(info[s_]["sb"][q] != t[q] for q in Q if q != u): s_ += 1; continue
                    e_ = s_
                    while e_ < p1 and all(info[e_ + 1]["sb"][q] == t[q] for q in Q if q != u): e_ += 1
                    kp = {v: (set(g.succ[v]) if v == u else {t[v]}) for v in used}
                    check(g, st, info, cut(kp), s_, e_, p1, "GU", cnt, name); s_ = e_ + 1


def main(a):
    cnt = Counter(); rng = random.Random(4848); nst = int(os.environ.get("RANDSTARTS", "2"))
    def do(g, name, r, extra=None):
        starts = ([extra] if extra else []) + ([] if (extra and os.environ.get("NOS3")) else [RE.best_reward_start(g)]) + \
                 [D.rand_start(g, r) for _ in range(nst)]
        for j, s0 in enumerate(starts):
            cnt["RUNS"] += 1; analyse(g, s0, cnt, "%s/%d" % (name, j), rng)
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
            ex = load_start(g, sp) if sp else None
            do(g, os.path.relpath(path), random.Random(os.path.relpath(path)), ex)
    for k in sorted(cnt): print(k, cnt[k])
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
