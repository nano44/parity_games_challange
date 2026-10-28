#!/usr/bin/env python3
"""REFEREE succ. 16 probe for P-N5-DEPTH-add-box22 (sha1 4d51aa5e, l-si aa6061d1). Own engine (rl_engine: SPEC; offmono_probe's kap/par;
root_probe's firstD). No lane code. Per phase ((lambda_Xi, tau) constant), maximal fallback-free run S, class c:
PER-CLASS C-intervals of c (transition-local reading, as R-N5-GCX's GCX-N1): t -> t+1 is good iff A^c_{t+1} <= A^c_t, D n U_c constant, and
Delta(u) constant for u in DD^c_t n DD^c_{t+1}; maximal good runs [a, b]. PURE iff D n U_c = DD^c at every state. L := max(|A_a| - 1, 0).
 GP     GATE-PUSH: t in [a + L, b), sigmabar changes at a gate u in D n U_c from y1 to y2 with y1 in A_{t+1}: M_{t+1}(y1) = M_t(y1) and
        (kappa_{t+1}(y1) > kappa_t(y1) or kappa_{t+1}(y1) = kappa_{t+1}(y2))
 GPC    its count: N_sb <= sum_{u in D n U_c} deg(u)(|U_c| - 2) + |A_a| + TIES_c
 PL     PURE-LEN as stated: b - a <= L + (1 + N_sb + N_cyc)(|U_c| - 1) + N_sb + N_cyc   (N_cyc = transitions changing c's honest cycle)
 PLSW   the same bound for the LAST transition of [a, b] with an Even switch in U_c (minus a)  (a class-local form)
 PLX    (count) PL failures where class c makes NO Even switch and no sigmabar change on [a + L, b] (frozen class, other classes moving)
 MR     MONO-REF: every in-phase t, z in U - {c}, m in T = (Q n U) u {c} on z's honest (t+1)-play, m != z, with the Q-vertices from z (incl.)
        to m (excl.) on no honest cycle at t: off_{t+1}(z; m) >= off_t(z; m). MR_pre: m at or before the play's first c; MR_post: m after c
 EO     E-ONEWAY: Even w in U - {c} switches a -> b at t; e1 := exit of a at t (first T-vertex of a's honest t-play), pi_a its class exit
        path; for t' = t+1, t+2, ... while pi_a and e1 are unchanged on [t, t'], e1 lies on w's honest play at every state of [t+1, t'] and
        MONO-REF's hypothesis holds for w -> e1: w does not switch back to a at t' -> t'+1
Usage: dadd_probe.py rand N nmin nmax kmax seed | files[:start]...  (RANDSTARTS, MAXN, NOS3)"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rl_engine as RE, dual_probe as D
import offmono_probe as OM
from zch_probe import Zc
from flip_probe import nxt
from root_probe import firstD
from gcx_probe import load_start
OM.MUT = 0
EX = []


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def hplay(nx, z):
    seq = []; x = z; seen = set()
    while x not in seen: seen.add(x); seq.append(x); x = nx[x]
    return seq


def analyse(g, start, cnt, name):
    st = RE.run(g, start); n = g.n
    Q = {v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) > 1}
    Qall = {v for v in range(n) if g.owner[v] == 1}
    for x in st:
        x["nx"] = nxt(g, x["s"], x["sb"])
        x["D"] = frozenset(u for u in Qall if x["sb"][u] != x["t"][u])
        x["fu"] = [firstD(g, x["s"], x["t"], x["D"], v) for v in range(n)]
    K = len(st); k = 0
    while k < K:
        j = k; lam = tuple(v[0] for v in st[k]["Xi"])
        while j + 1 < K and tuple(v[0] for v in st[j + 1]["Xi"]) == lam and st[j + 1]["t"] == st[k]["t"]: j += 1
        if j > k: phase(g, st, k, j, lam, Q, cnt, name)
        r = k
        while r <= j:
            e = r
            while e < j and not st[e]["fb"]: e += 1
            if e > r: runS(g, st, r, e, lam, Q, cnt, name)
            r = e + 1
        k = j + 1


def phase(g, st, a, b, lam, Q, cnt, name):
    n = g.n
    for c in sorted(set(lam)):
        U = {v for v in range(n) if lam[v] == c}
        T = (Q & U) | {c}
        Kp = lambda t, z: OM.kap(g, c, st[t]["Xi"][z])
        for t in range(a, b):
            nx0, nx1 = st[t]["nx"], st[t + 1]["nx"]
            oncyc = set(Zc(nx0, c))
            for z in U - {c}:
                pl = hplay(nx1, z)
                ic = pl.index(c) if c in pl else len(pl)
                ok = True
                for i in range(1, len(pl)):
                    if pl[i - 1] in Q and pl[i - 1] in oncyc: ok = False
                    if not ok: break
                    m = pl[i]
                    if m not in T: continue
                    tag = "MR_pre" if i <= ic else "MR_post"
                    cnt[tag + "_chk"] += 1
                    if OM.sub(Kp(t + 1, z), Kp(t + 1, m)) < OM.sub(Kp(t, z), Kp(t, m)): fail(cnt, tag, name, t, c, z, m)
            # E-ONEWAY windows
            for w in U - {c}:
                if g.owner[w] != 0 or st[t]["s"][w] == st[t + 1]["s"][w]: continue
                aa = st[t]["s"][w]
                pa = hplay(nx0, aa); idx = next((i for i, x in enumerate(pa) if x in T), None)
                if idx is None: continue
                e1 = pa[idx]; path = pa[:idx]
                cnt["EO_windows"] += 1
                for tp in range(t + 1, b):
                    nxp = st[tp]["nx"]
                    if any(nxp[x] != nx0[x] for x in path) or hplay(nxp, aa)[:idx + 1] != pa[:idx + 1]: break
                    plw = hplay(nxp, w)
                    if e1 not in plw: break
                    cyc_prev = set(Zc(st[tp - 1]["nx"], c))
                    if any(x in Q and x in cyc_prev for x in plw[:plw.index(e1)]): break
                    cnt["EO_chk"] += 1
                    if c in plw and plw.index(c) < plw.index(e1): cnt["EO_e1_after_c"] += 1
                    if st[tp + 1]["s"][w] == aa: fail(cnt, "EO", name, t, tp, c, w)


def runS(g, st, r, e, lam, Q, cnt, name):
    n = g.n; tau = st[r]["t"]
    for c in sorted(set(lam)):
        U = {v for v in range(n) if lam[v] == c}
        A = {t: {v for v in U if st[t]["fu"][v] is None} for t in range(r, e + 1)}
        M = lambda t, z: g.weight(st[t]["Xi"][z][1])
        Kp = lambda t, z: OM.kap(g, c, st[t]["Xi"][z])
        DU = {t: st[t]["D"] & U for t in range(r, e + 1)}
        DD = {t: {u for u in DU[t] if st[t]["sb"][u] in A[t] and tau[u] in A[t]} for t in range(r, e + 1)}
        Dl = lambda t, u: M(t, tau[u]) - M(t, st[t]["sb"][u])
        good = lambda t: A[t + 1] <= A[t] and DU[t] == DU[t + 1] and all(Dl(t, u) == Dl(t + 1, u) for u in DD[t] & DD[t + 1])
        t = r
        while t < e:
            if not good(t): t += 1; continue
            a = t
            while t < e and good(t): t += 1
            b = t
            if not all(DU[k] == DD[k] for k in range(a, b + 1)): continue
            cnt["PURE_ints"] += 1
            if DU[a]: cnt["PURE_withgate"] += 1
            L = max(len(A[a]) - 1, 0)
            Nsb = 0; ties = 0
            for k in range(a + L, b):
                ch = [u for u in DU[k] if st[k]["sb"][u] != st[k + 1]["sb"][u]]
                if ch: Nsb += 1
                for u in ch:
                    y1, y2 = st[k]["sb"][u], st[k + 1]["sb"][u]
                    if y1 not in A[k + 1]: continue
                    cnt["GP_chk"] += 1
                    tie = Kp(k + 1, y1) == Kp(k + 1, y2)
                    if tie: ties += 1
                    if M(k + 1, y1) != M(k, y1) or not (Kp(k + 1, y1) > Kp(k, y1) or tie): fail(cnt, "GP", name, k, c, u)
            if Nsb > sum(len(g.succ[u]) * max(len(U) - 2, 0) for u in DU[a]) + len(A[a]) + ties: fail(cnt, "GPC", name, a, c)
            Ncyc = sum(1 for k in range(a, b) if Zc(st[k]["nx"], c) != Zc(st[k + 1]["nx"], c))
            bound = L + (1 + Nsb + Ncyc) * (len(U) - 1) + Nsb + Ncyc
            cnt["PL_chk"] += 1
            if b - a > bound:
                frozen = not any(st[k]["s"][v] != st[k + 1]["s"][v] for k in range(a, b) for v in U if g.owner[v] == 0)
                cnt["PL_FAIL"] += 1; cnt["PLX_frozen" if frozen else "PLX_moving"] += 1
                if len(EX) < 40: EX.append(("PL", name, a, b, c, len(U), L, Nsb, Ncyc, bound, "frozen" if frozen else "moving"))
            sw = [k for k in range(a, b) for v in U if g.owner[v] == 0 and st[k]["s"][v] != st[k + 1]["s"][v]]
            cnt["PLSW_chk"] += 1
            if sw and max(sw) + 1 - a > bound: fail(cnt, "PLSW", name, a, b, c, max(sw))


def main(a):
    cnt = Counter(); rng = random.Random(2323); nst = int(os.environ.get("RANDSTARTS", "2"))
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
