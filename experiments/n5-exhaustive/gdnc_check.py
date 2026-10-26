#!/usr/bin/env python3
"""Box 9b (Lead 2026-10-26 05:05Z): independent check of L-SI's Lemma G_D-NC and Corollary FRZ-U_D (docs/si/N5-2O-T-box16.md §6, l-si
b92f84d4), written from the packet text and RESULTS R55's setting only (L-SI's experiments/si/fb2o/gdnc.py NOT opened).
Run and values: REFEREE-2's fb_check.run_n5 (SPEC run; asserted here = n5.run counts) and Engine valuations; the plays, D_k, u(v), pi_v,
(NC), (h3_D), M_D and every check below are my own code from the definitions:
  D_k = {Odd u : sigmabar_k(u) != tau_k(u)};  W-play = (sigma_k, tau_k);  honest play = (sigma_k, sigmabar_k);  u(v) = first vertex of D_k
  on v's W-play (v included);  R_D = {v : u(v) exists};  pi_v = W-path from v to u(v), u(v) excluded;  W_k(v) = value of v's W-play.
  (NC) at k: no u in D_k lies on its own honest cycle, none on its own W-cycle.  (h3_D): lambda_Xi(u) = lambda_W(u) for u in D_k.
  M_D = max_{u in D_k} lev(Xi_k(u), W_k(u)), BOT if D_k empty.
Checks (every state of every run):
  b'   under (NC), every v in R_D, u = u(v): (HP) v's honest play follows pi_v to u; the honest and the W-play from u avoid pi_v;
       Xi_k(v) = pi_v (+) Xi_k(u); W_k(v) = pi_v (+) W_k(u).
  c1'  under (NC) and (h3_D): y, z in R_D with u(y) = u(z) = u: pi_y(+)Xi(u) <= pi_z(+)Xi(u) iff pi_y(+)W(u) <= pi_z(+)W(u).
  c2'  under (NC) and (h3_D): COARSE_L(Xi_k(v)) = COARSE_L(W_k(v)) for every v and EVERY L with M_D <= L <= n - 1 (L = BOT when M_D = BOT).
  FRZ  Corollary FRZ-U_D: every maximal fallback-free run S of transitions inside one phase (key (lambda_Xi, tau)) with (NC) and (h3_D)
       at every state of S: for every L with max(max_S M_D, -1) <= L <= n - 1 (and L = BOT if max_S M_D = BOT), COARSE_L(W) is constant
       on S from its (n-1)-th state on, read 1-based: the 0-based states S[n-2], S[n-1], ... all have equal COARSE_L(W); a check
       needs S to have at least n states (n - 1 transitions), else it is vacuous (counted).
  MUT  mutation control (MUT=1): b' checked at every state WITHOUT (NC); failures counted, not violations.
Usage: gdnc_check.py rand N NMIN NMAX KMIN KMAX SEED | inst FILE.pg [STARTS] | files LIST.txt [STARTS]   (each game: canonical start + one random start pair)"""
import os
import random
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
for p in ("docs/referee-2/R2-N5-FB", "docs/referee-2/R2-N5-CLS"):
    sys.path.insert(0, os.path.join(ROOT, p))
import fb_check as F  # noqa: E402
import cls_check as CC  # noqa: E402

BOT, INF, lev, coarse = F.BOT, F.INF, F.lev, F.coarse
MUT = os.environ.get("MUT") == "1"


def lasso(f, v):
    """positional play from v on successor map f: (path before the cycle, cycle)."""
    seen, path, x = {}, [], v
    while x not in seen:
        seen[x] = len(path); path.append(x); x = f[x]
    return path[:seen[x]], path[seen[x]:]


def on_own_cycle(f, u):
    return u in lasso(f, u)[1]


def state_info(g, E, s, t):
    n = g.n
    Xi, sbar = E.evaluate(tuple(s)); Xi = list(Xi); sbar = list(sbar)
    Wf = [s[v] if g.owner[v] == 0 else t[v] for v in range(n)]
    Hf = [s[v] if g.owner[v] == 0 else sbar[v] for v in range(n)]
    W = [F.play_val(E, Wf, v)[0] for v in range(n)]
    D = {u for u in range(n) if g.owner[u] == 1 and sbar[u] != t[u]}
    uv, pi = {}, {}
    for v in range(n):
        x, path, seen = v, [], set()
        while x not in seen:
            if x in D:
                uv[v] = x; pi[v] = path; break
            seen.add(x); path.append(x); x = Wf[x]
    NC = all(not on_own_cycle(Hf, u) and not on_own_cycle(Wf, u) for u in D)
    h3 = all(Xi[u][0] == W[u][0] for u in D)
    MD = max([lev(Xi[u], W[u]) for u in D], default=BOT)
    return dict(Xi=Xi, W=W, Wf=Wf, Hf=Hf, D=D, uv=uv, pi=pi, NC=NC, h3=h3, MD=MD, lam=tuple(x[0] for x in Xi))


def levels(MD, n):
    return ([BOT] if MD == BOT else []) + list(range(max(MD, -1), n))


def check_bprime(g, E, S, c, bad, name, tag="b'"):
    for v, u in S["uv"].items():
        p = S["pi"][v]; ok = True
        hp = lasso(S["Hf"], v)[0] + lasso(S["Hf"], v)[1]
        if hp[:len(p) + 1] != p + [u]: ok = False
        ps = set(p)
        hu = lasso(S["Hf"], u); wu = lasso(S["Wf"], u)
        if ps & set(hu[0] + hu[1]) or ps & set(wu[0] + wu[1]): ok = False
        if S["Xi"][v] != CC.prefix(E, p, S["Xi"][u]) or S["W"][v] != CC.prefix(E, p, S["W"][u]): ok = False
        c[tag + "_checks"] += 1
        if not ok:
            bad(f"{name} {tag} v={v} u={u}") if tag == "b'" else c.update({"MUT_b'_failures": 1})


def check_state(g, E, S, c, bad, name):
    n = g.n
    c["states"] += 1; c["states_NC"] += S["NC"]; c["states_NC_h3"] += S["NC"] and S["h3"]
    c["states_D_ge2"] += len(S["D"]) >= 2
    hD = all(not ((set(lasso(f, u)[0][1:] + lasso(f, u)[1]) - {u}) & S["D"]) and not on_own_cycle(f, u)
             for u in S["D"] for f in (S["Hf"], S["Wf"]))     # (h_D): no revisit of D after leaving u
    c["states_NC_not_hD"] += S["NC"] and not hD; S["hD"] = hD
    if MUT:
        check_bprime(g, E, S, c, bad, name, tag="MUT")
    if not S["NC"]:
        return
    check_bprime(g, E, S, c, bad, name)
    if not S["h3"]:
        return
    by_u = {}
    for v, u in S["uv"].items():
        by_u.setdefault(u, []).append(v)
    for u, vs in by_u.items():
        for y in vs:
            for z in vs:
                a = E.key(CC.prefix(E, S["pi"][y], S["Xi"][u])) <= E.key(CC.prefix(E, S["pi"][z], S["Xi"][u]))
                b = E.key(CC.prefix(E, S["pi"][y], S["W"][u])) <= E.key(CC.prefix(E, S["pi"][z], S["W"][u]))
                c["c1'_checks"] += 1
                if a != b:
                    bad(f"{name} c1' y={y} z={z} u={u}")
    for L in levels(S["MD"], n):
        c["c2'_checks"] += 1
        if any(coarse(S["Xi"][v], L) != coarse(S["W"][v], L) for v in range(n)):
            bad(f"{name} c2' L={L} MD={S['MD']}")


def check_run(g, s, t, c, mx, bad, name):
    states, fbs, E, Ed = F.run_n5(g, s, t)
    r = F.n5.run(g, "n5", ({v: s[v] for v in range(g.n) if g.owner[v] == 0}, {v: t[v] for v in range(g.n) if g.owner[v] == 1}))
    if (len(fbs), sum(fbs)) != tuple(r[:2]):
        bad(f"{name} run differs from n5.run")
    A = [state_info(g, E, a, b) for a, b in states]
    for k, S in enumerate(A):
        check_state(g, E, S, c, bad, f"{name}@{k}")
    c["runs"] += 1; c["transitions"] += len(fbs)
    # FRZ-U_D: maximal runs of consecutive non-fallback in-phase transitions with (NC) and (h3_D) at every state
    n = g.n; T = len(fbs); k = 0; best = 0
    good = [A[j]["NC"] and A[j]["h3"] for j in range(len(A))]
    ok_tr = [not fbs[j] and A[j]["lam"] == A[j + 1]["lam"] and states[j][1] == states[j + 1][1] and good[j] and good[j + 1]
             for j in range(T)]
    while k < T:
        if not ok_tr[k]:
            k += 1; continue
        j = k
        while j < T and ok_tr[j]:
            j += 1
        Sx = list(range(k, j + 1)); c["FRZ_runs"] += 1; best = max(best, len(Sx))
        if len(Sx) > n - 1:
            mD = max(A[x]["MD"] for x in Sx)
            tail = Sx[n - 2:]
            nh = sum(1 for x in Sx if not A[x]["hD"]); c["FRZ_checked_runs"] += 1; c["FRZ_checked_states_not_hD"] += nh
            c["FRZ_checked_runs_with_not_hD"] += nh > 0; c["FRZ_checked_states_D_ge2"] += sum(1 for x in Sx if len(A[x]["D"]) >= 2)
            for L in levels(mD, n):
                c["FRZ_checks"] += 1
                ref = [coarse(A[tail[0]]["W"][v], L) for v in range(n)]
                if any([coarse(A[x]["W"][v], L) for v in range(n)] != ref for x in tail):
                    bad(f"{name} FRZ-U_D run [{k},{j}] L={L}")
        else:
            c["FRZ_runs_too_short(vacuous)"] += 1
        k = j
    mx["max_FRZ_run_states"] = max(mx["max_FRZ_run_states"], best)
    mx["max_FRZ_run_minus_(n-1)"] = max(mx["max_FRZ_run_minus_(n-1)"], best - (n - 1))
    return best


def rand_ckO(rng, n, k):
    """random game with exactly k Odd vertices of out-degree >= 2 (k <= n - 1), every vertex at least one successor."""
    owner = [rng.randrange(2) for _ in range(n)]
    odd_choice = set(rng.sample(range(n), k))
    for v in odd_choice:
        owner[v] = 1
    succ = []
    for v in range(n):
        if v in odd_choice:
            d = rng.randint(2, min(3, n)); succ.append(sorted(rng.sample(range(n), d)))
        elif owner[v] == 1:
            succ.append([rng.randrange(n)])
        else:
            d = rng.randint(1, min(3, n)); succ.append(sorted(rng.sample(range(n), d)))
    prio = [rng.randrange(n + 1) for _ in range(n)]
    return F.lpg.Game(prio, owner, succ)


def rand_start(g, rng):
    E, Ed = F.Engine(g), F.Engine(F.n5.dual(g))
    s, t = list(E.initial("best")), list(Ed.initial("best"))
    s = [rng.choice(g.succ[v]) if g.owner[v] == 0 else s[v] for v in range(g.n)]
    t = [rng.choice(g.succ[v]) if g.owner[v] == 1 else t[v] for v in range(g.n)]
    return s, t


def report(c, mx, viol):
    for k in sorted(c):
        print(f"{k}: {c[k]}")
    for k in sorted(mx):
        print(f"{k}: {mx[k]}")
    for v in viol[:20]:
        print("VIOLATION", v)
    print("RESULT", "FAIL" if viol else "OK", f"violations={len(viol)}")


def main():
    c, mx, viol = Counter(), Counter(), []
    bad = lambda m: viol.append(m)  # noqa: E731
    if sys.argv[1] == "rand":
        N, lo, hi, klo, khi, seed = map(int, sys.argv[2:8]); rng = random.Random(seed)
        for i in range(N):
            n = rng.randint(lo, hi); g = rand_ckO(rng, n, rng.randint(klo, min(khi, n - 1)))
            E, Ed = F.Engine(g), F.Engine(F.n5.dual(g))
            check_run(g, list(E.initial("best")), list(Ed.initial("best")), c, mx, bad, f"r{seed}#{i}c")
            s, t = rand_start(g, rng); check_run(g, s, t, c, mx, bad, f"r{seed}#{i}r")
    else:
        files = [sys.argv[2]] if sys.argv[1] == "inst" else [l.strip() for l in open(sys.argv[2]) if l.strip()]
        for path in files:
            g = F.lpg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%")))
            rng = random.Random(7); E, Ed = F.Engine(g), F.Engine(F.n5.dual(g)); nm = os.path.basename(path)
            check_run(g, list(E.initial("best")), list(Ed.initial("best")), c, mx, bad, nm + ":canon")
            for r in range(int(sys.argv[3]) if len(sys.argv) > 3 else 0):
                s, t = rand_start(g, rng); check_run(g, s, t, c, mx, bad, f"{nm}:rand{r}")
            c["files"] += 1
    report(c, mx, viol)


if __name__ == "__main__":
    main()
