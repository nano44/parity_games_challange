#!/usr/bin/env python3
"""N6: path-following interior-point method on the Jurdzinski-Savani P-matrix LCP of the discounted game induced by a parity game
(docs/new/N6-ipm.md). Max-parity, owner 0 = Even (maximiser).

Pipeline: compress priorities (order and parity kept) -> binary arena (out-degree 1 doubled, out-degree k > 2 split into a chain of
k - 2 helper states of the same owner, helper actions cost 0) -> weights (-B)^p with B = n' + 1 (n' = binary size) -> discount
gamma = 1 - 1/(4 n'^3 B^d) (Friedmann 1106.0778 sec. 9, beta_G with max|r| <= B^d) -> LCP w = q + M z of HIJ 1304.1888 Def. 16 ->
infeasible primal-dual IPM (Mehrotra predictor-corrector inside the wide neighbourhood N_-inf(theta), residual kept proportional
to mu) in arb arithmetic at PREC bits, radii dropped (mid) after every operation.
After every iteration the iterate is rounded (state i keeps the action with the smaller slack) and the induced parity strategies of
both players are checked with experiments/harness/verify.py: the first iteration whose rounding verifies is 'cert'.
Usage: n6.py game.pg [--maxit K] [--sol out.sol]  -> one CSV-ish line: n n' d bits it_cert it_total mu_final status
"""
import sys, os, math, time, argparse
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import pg, verify
from flint import arb_mat, arb, ctx


def binarize(g):
    """-> list of states: (owner, cost_prio or None, [succ_state_a, succ_state_b]); state v < g.n is original vertex v."""
    n = g.n
    states = [None] * n
    extra = []
    for v in range(n):
        s = list(dict.fromkeys(g.succ[v]))
        if len(s) == 1:
            states[v] = [g.owner[v], v, [s[0], s[0]]]
        elif len(s) == 2:
            states[v] = [g.owner[v], v, s]
        else:
            # v -> s0 | h1 ; h1 -> s1 | h2 ; ... ; h_{k-2} -> s_{k-2} | s_{k-1}
            k = len(s); prev = v; first = True
            for j in range(k - 2):
                h = n + len(extra); extra.append(None)
                st = [g.owner[v], v if first else None, [s[j], h]]
                if first: states[v] = st
                else: extra[prev - n] = st
                prev = h; first = False
            extra[prev - n] = [g.owner[v], None, [s[k - 2], s[k - 1]]]
    return states + extra


def compress(prio):
    """order-preserving map keeping parity, minimal max."""
    vals = sorted(set(prio)); m = {}; cur = -1
    for p in vals:
        c = cur + 1 if cur >= 0 else 0
        if c % 2 != p % 2: c += 1
        m[p] = c; cur = c
    return [m[p] for p in prio]


def strategies_from(g, states, choice):
    """choice[i] in {0,1} per binary state -> parity successor per original vertex (follow helper chain)."""
    n = g.n; strat = [None] * n
    for v in range(n):
        x = states[v][2][choice[v]]
        while x >= n:
            x = states[x][2][choice[x]]
        strat[v] = x
    return strat


def regions(g, strat):
    """winner of each vertex's play under both positional strategies (lasso, max priority on the cycle)."""
    n = g.n; win = [None] * n
    for v in range(n):
        if win[v] is not None: continue
        path, pos, x = [], {}, v
        while x not in pos and win[x] is None:
            pos[x] = len(path); path.append(x); x = strat[x]
        if win[x] is not None: w = win[x]
        else:
            cyc = path[pos[x]:]; w = max(g.prio[c] for c in cyc) % 2
        for y in path: win[y] = w
    return win


def build(g, prec_extra=64):
    states = binarize(g)
    N = len(states)
    cp = compress(g.prio); d = max(cp)
    B = N + 1
    one_minus_gamma_inv = 4 * N ** 3 * B ** d          # 1/(1-gamma), exact integer
    if os.environ.get("N6GINV"): one_minus_gamma_inv = int(os.environ["N6GINV"])   # experiment only: other discounts
    bits = one_minus_gamma_inv.bit_length()
    prec = int(os.environ.get("N6PRECF", "8")) * bits + 16 * N.bit_length() + prec_extra
    ctx.prec = prec
    gamma = arb(1) - arb(1) / arb(one_minus_gamma_inv)
    sgn = [1 if states[i][0] == 0 else -1 for i in range(N)]   # Even = maximiser -> +1 (HIJ Player 2), Odd -> -1
    cost = [0 if states[i][1] is None else (-B) ** cp[states[i][1]] for i in range(N)]
    # actions: sigma = index 0, tau = index 1; cost of both actions of state i = cost[i]
    A = arb_mat(N, N); Bm = arb_mat(N, N)
    for i in range(N):
        A[i, i] += 1; Bm[i, i] += 1
        A[i, states[i][2][0]] -= gamma; Bm[i, states[i][2][1]] -= gamma
    Binv = Bm.inv().mid()
    AB = (A * Binv).mid()
    M = arb_mat(N, N); q = arb_mat(N, 1)
    cmax = max(abs(x) for x in cost) or 1
    c = arb_mat(N, 1, [arb(x) / cmax for x in cost])     # scaling the costs scales (w, z): same LCP solution support
    ABc = (AB * c).mid()
    for i in range(N):
        for j in range(N):
            M[i, j] = (AB[i, j] * sgn[i] * sgn[j]).mid()
        q[i, 0] = (sgn[i] * ABc[i, 0] - sgn[i] * c[i, 0]).mid()
    # natural strictly feasible start (no big-M): y = K s with K = 2/(1-gamma) gives, for every state and both actions,
    # s_i (y_i - c_a - gamma y_j) >= K(1-gamma) - 1 = 1 > 0, so w = s(A y - c), z = s(Bm y - c) are > 0 and w = q + M z.
    K = arb(2 * one_minus_gamma_inv)
    y = arb_mat(N, 1, [K * sgn[i] for i in range(N)])
    Ay = (A * y).mid(); By = (Bm * y).mid()
    w0 = arb_mat(N, 1, [(sgn[i] * (Ay[i, 0] - c[i, 0])).mid() for i in range(N)])
    z0 = arb_mat(N, 1, [(sgn[i] * (By[i, 0] - c[i, 0])).mid() for i in range(N)])
    build.start = (w0, z0)
    return states, N, d, bits, prec, M, q, one_minus_gamma_inv


def ipm(g, maxit=500, theta=float(os.environ.get("N6THETA", "1e-3")), sol=None):
    t0 = time.time()
    states, N, d, bits, prec, M, q, ginv = build(g)
    qmax = max(abs(float(q[i, 0])) for i in range(N)) if N else 1.0
    RHO = float(os.environ.get("N6RHO", "1"))
    # reduced costs are <= 2 max|c| / (1 - gamma) = 2 ginv (costs scaled to max|c| = 1): the solution lies in [0, 2 ginv]^N
    rho = arb(max(1.0, qmax, 2.0 * ginv)) * arb(RHO)
    # big-M embedding (Kojima-Megiddo-Noma-Yoshise, initial points): M' = [[M, e], [-e^T, 0]], q' = [q; lam], x'^T M' x' = x^T M x.
    # Start z = rho e, z_{N+1} = t with w = q + M z + t e >= rho, lam chosen so that w_{N+1} t = rho^2: FEASIBLE, residual 0.
    # At the solution z_{N+1} = 0 iff lam > e^T z* (checked: status 'bigM' otherwise).
    Nst = N
    mode = os.environ.get("N6START", "game")
    if mode == "game":
        w, z = build.start
    elif mode == "bigm":
        Nst = N; Na = N + 1
        z0 = arb_mat(N, 1, [rho] * N); Mz = (M * z0).mid()
        t = (rho - min((q[i, 0] + Mz[i, 0]).mid() for i in range(N))).mid()
        if t < rho: t = rho
        lam = (arb(N) * rho + rho * rho / t).mid()
        lam = max(lam, (arb(4) * arb(N) * arb(2 * ginv) + rho * rho / t).mid())
        Ma = arb_mat(Na, Na); qa = arb_mat(Na, 1)
        for i in range(N):
            for j in range(N): Ma[i, j] = M[i, j]
            Ma[i, N] = 1; Ma[N, i] = -1; qa[i, 0] = q[i, 0]
        qa[N, 0] = lam
        M, q, N = Ma, qa, Na
        z = arb_mat(N, 1, [rho] * Nst + [t])
        w = (q + M * z).mid()
        for _ in range(30):   # centre on the feasible set: z_i <- mu / w_i for i <= Nst (t fixed), w = q + M z
            mu_ = (sum((w[i, 0] * z[i, 0] for i in range(N)), arb(0)) / N).mid()
            zn = arb_mat(N, 1, [(mu_ / w[i, 0]).mid() if i < Nst else z[i, 0] for i in range(N)])
            wn = (q + M * zn).mid()
            if min(wn[i, 0] for i in range(N)) <= 0: break
            z, w = zn, wn
    else:
        # infeasible start (Kojima-Megiddo-Mizuno style): z = w = rho e with rho >= the solution bound 4 ginv + 2
        rho = arb(max(1.0, qmax, 4.0 * ginv + 2)) * arb(RHO)
        z = arb_mat(N, 1, [rho] * N); w = arb_mat(N, 1, [rho] * N)
    r0 = (w - M * z - q).mid()
    r0n = max(abs(r0[i, 0]) for i in range(N))
    feasible = bool(r0n < arb(2) ** (-(prec // 2)))   # residual at rounding level: feasible path following, no KMM test
    if r0n == 0: r0n = arb(1)
    mu0 = (sum((w[i, 0] * z[i, 0] for i in range(N)), arb(0)) / N).mid()
    it_cert = None; status = "maxit"; mu = mu0
    tiny = arb(2) ** (-(prec - 64))     # ABSOLUTE: slacks of optimal vs non-optimal actions can be ~2^-O(N d log N) (doc sec. 3)
    for it in range(1, maxit + 1):
        mu = (sum((w[i, 0] * z[i, 0] for i in range(N)), arb(0)) / N).mid()
        r = (w - M * z - q).mid()
        # rounding + certificate
        choice = [0 if w[i, 0] <= z[i, 0] else 1 for i in range(Nst)]
        strat = strategies_from(g, states, choice)
        win = regions(g, strat)
        errs = verify.check(g, win, strat)
        if os.environ.get("N6DBG2") and it % 20 == 0: print(it, float(mu), errs[:2], file=sys.stderr)
        if not errs:
            if it_cert is None:
                it_cert = it - 1
                if sol: pg.write_sol(win, sol, strat)
            status = "cert"
        if mu < tiny or (it_cert is not None and os.environ.get("N6STOPCERT")):
            status = "converged"; break
        # Newton matrix K = W + Z M ; dw = M dz - r
        K = arb_mat(N, N)
        for i in range(N):
            zi = z[i, 0]
            for j in range(N):
                K[i, j] = (zi * M[i, j]).mid()
            K[i, i] = (K[i, i] + w[i, 0]).mid()

        def solve(rhs_c):
            rhs = arb_mat(N, 1, [(rhs_c[i] + z[i, 0] * r[i, 0]).mid() for i in range(N)])
            dz = K.solve(rhs, algorithm="approx").mid()
            dw = (M * dz - r).mid()
            return dz, dw

        def maxstep(dz, dw):
            a = arb(1)
            for i in range(N):
                if dz[i, 0] < 0: a = min(a, (-z[i, 0] / dz[i, 0]).mid())
                if dw[i, 0] < 0: a = min(a, (-w[i, 0] / dw[i, 0]).mid())
            return a
        # predictor (affine)
        dz_a, dw_a = solve([-(w[i, 0] * z[i, 0]) for i in range(N)])
        a_a = maxstep(dz_a, dw_a)
        mu_aff = (sum(((w[i, 0] + a_a * dw_a[i, 0]) * (z[i, 0] + a_a * dz_a[i, 0]) for i in range(N)), arb(0)) / N).mid()
        sig = (mu_aff / mu) ** 3
        if sig > 1: sig = arb(1)
        ratio = (min((w[i, 0] * z[i, 0]).mid() for i in range(N)) / mu).mid()
        th = arb(theta) if ratio >= arb(theta) else ratio   # never let centrality fall below min(theta, current ratio)
        rnorm = max(abs(r[i, 0]) for i in range(N))

        def linesearch(dz, dw, centring=False):
            """largest a (from 0.99 * max step, factor 0.8) keeping the wide neighbourhood min w_i z_i >= theta mu and the KMM
            infeasibility condition mu_k/mu_0 >= |r_k|/|r_0|; None if no a >= 1e-12 works."""
            a = (maxstep(dz, dw) * arb("0.99")).mid()
            while a > arb("1e-12"):
                zn = (z + dz * a).mid(); wn = (w + dw * a).mid()
                prods = [(wn[i, 0] * zn[i, 0]).mid() for i in range(N)]
                mun = (sum(prods, arb(0)) / N).mid()
                rn = (rnorm * (1 - a)).mid()
                kmm = feasible or mun * r0n >= rn * mu0
                dec = mun <= (1 - a / 100) * mu or (centring and min(prods) / mun > ratio)
                if min(prods) > 0 and min(prods) >= th * mun and kmm and dec:
                    return a, zn, wn
                a = (a * arb("0.8")).mid()
            return None
        # corrector (Mehrotra); safeguard: if its step is short, try fixed centring sigma = 0.3, 0.7, 1 and keep the longest step
        best = None
        cands = [lambda: solve([(sig * mu - w[i, 0] * z[i, 0] - dw_a[i, 0] * dz_a[i, 0]).mid() for i in range(N)])]
        for s_ in ("0.3", "0.7", "1"):
            cands.append(lambda s_=s_: solve([(arb(s_) * mu - w[i, 0] * z[i, 0]).mid() for i in range(N)]))
        order = list(range(len(cands)))
        if ratio < arb(theta): order = [3, 2, 1, 0]
        for k in order:
            cand = cands[k]
            dz, dw = cand()
            res = linesearch(dz, dw, centring=(k == 3))
            if res and (best is None or res[0] > best[0]): best = res + (k,)
            if best and best[0] > arb("0.1"): break
        if best is None:
            status = "stalled"; break
        a, z, w = best[0], best[1], best[2]; sig = arb(best[3])
        if os.environ.get("N6DBG"): print(it, best[3], float(a), float(mu), float(rnorm), min(float(w[i, 0] * z[i, 0]) for i in range(N)) / max(float(mu), 1e-300), file=sys.stderr)
    if N > Nst and z[Nst, 0] > w[Nst, 0]: status += "-bigM"
    return dict(n=g.n, N=Nst, d=d, bits=bits, prec=prec, it_cert=it_cert, it_total=it, status=status,
                mu=float(mu / mu0) if mu0 > 0 else 0.0, secs=round(time.time() - t0, 1))


def track(g, maxit=5000, sol=None):
    """Adaptive long-step path following on the central path w o z = mu e, w = q + M z (feasible throughout, from the game's
    natural start, see build). At each target mu: damped Newton (Armijo on the proximity max_i |w_i z_i / mu - 1|, positivity
    kept with factor 0.99) until proximity <= 0.5; target factor f adapts (success: f <- max(f^2, 1e-4); failure after 40 Newton
    steps: restore, f <- sqrt(f)). Count = total Newton steps ('it'). Every 1 step the rounding is checked (verify.py)."""
    t0 = time.time()
    states, N, d, bits, prec, M, q, ginv = build(g)
    PROX = arb(os.environ.get("N6PROX", "0.5"))   # neighbourhood: max_i |w_i z_i / T_i - 1| <= PROX
    w, z = build.start
    tiny = arb(2) ** (-(prec - 64))
    it = 0; it_cert = None; status = "maxit"; nmu = 0

    def prods(w, z): return [(w[i, 0] * z[i, 0]).mid() for i in range(N)]

    def prox(w, z, T):
        """T: target vector (list) or scalar mu"""
        if not isinstance(T, list): T = [T] * N
        return max(abs((p_ / T[i] - 1)).mid() for i, p_ in enumerate(prods(w, z)))

    def certify():
        nonlocal it_cert, status
        choice = [0 if w[i, 0] <= z[i, 0] else 1 for i in range(N)]
        strat = strategies_from(g, states, choice); win = regions(g, strat)
        if not verify.check(g, win, strat):
            if it_cert is None:
                it_cert = it
                if sol: pg.write_sol(win, sol, strat)
            return True
        return False

    def newton(w, z, mu, cap):
        """Newton for w o z = T, w = q + M z: K dz = T - w o z with K = W + Z M, dw = M dz; fraction-to-boundary step (0.99),
        halved only if the proximity would blow up (> 10x and > 1). Success = proximity max|w_i z_i / T_i - 1| <= 0.5.
        (A log-coordinate variant and an Armijo rule on the max-norm proximity were tried and are worse; N6-ipm.md sec. 7.)"""
        nonlocal it
        T = mu if isinstance(mu, list) else [mu] * N
        for _ in range(cap):
            pr = prox(w, z, mu)
            if pr <= PROX: return w, z, True
            if it >= maxit: return w, z, False
            it += 1
            K = arb_mat(N, N)
            for i in range(N):
                zi = z[i, 0]
                for j in range(N): K[i, j] = (zi * M[i, j]).mid()
                K[i, i] = (K[i, i] + w[i, 0]).mid()
            rhs = arb_mat(N, 1, [(T[i] - w[i, 0] * z[i, 0]).mid() for i in range(N)])
            dz = K.solve(rhs, algorithm="approx").mid(); dw = (M * dz).mid()
            a = arb(1)
            for i in range(N):
                if dz[i, 0] < 0: a = min(a, (-z[i, 0] / dz[i, 0] * arb("0.99")).mid())
                if dw[i, 0] < 0: a = min(a, (-w[i, 0] / dw[i, 0] * arb("0.99")).mid())
            if os.environ.get("N6LIM") and a < arb("1e-6"):
                res = (K * dz - rhs).mid()
                print("RES", it, float(max(abs(res[i, 0]) for i in range(N))), float(max(abs(rhs[i, 0]) for i in range(N))), file=sys.stderr)
                dz2 = K.solve(rhs, nonstop=True)
                print("BALL", dz2[7, 0].str(5) if N > 7 else "", file=sys.stderr)
                L = sorted([(float(-z[i, 0] / dz[i, 0]), "z", i) for i in range(N) if dz[i, 0] < 0] + [(float(-w[i, 0] / dw[i, 0]), "w", i) for i in range(N) if dw[i, 0] < 0])[:2]
                print("LIM", it, L, [(i, states[i][0], states[i][2], float(z[i, 0]), float(w[i, 0]), float(dz[i, 0]), float(dw[i, 0])) for _, _, i in L], file=sys.stderr)
            ok = False
            while a > arb("1e-30"):
                zn = (z + dz * a).mid(); wn = (w + dw * a).mid()
                pn = prox(wn, zn, mu)
                if pn <= PROX or pn <= max(pr * 10, arb(1)):
                    ok = True; break
                a = (a * PROX).mid()
            if not ok: return w, z, False
            w, z = wn, zn
            if os.environ.get("N6DBG"): print(it, float(a), float(prox(w, z, mu)), file=sys.stderr)
        return w, z, prox(w, z, mu) <= PROX

    p0 = prods(w, z); mu = arb(1); ncs = 0; ok = True
    if os.environ.get("N6PATH", "central") == "central":
        # centring by target following: T_s = p0^(1-s) mu0^s, s: 0 -> 1 with an adaptive step (counted in 'it' like every Newton step)
        mu = (sum(p0, arb(0)) / N).mid()
        sc, ds = arb(0), PROX
        # each target may move by at most a factor 2 per centring step: ds <= ln 2 / ln(max spread) (O(bits) steps in all)
        spread = max(max((p0[i] / mu).mid(), (mu / p0[i]).mid()) for i in range(N))
        TF = arb(os.environ.get("N6TFAC", "2"))
        dsmax = (TF.log() / spread.log()).mid() if spread > TF else arb(1)
        ds = min(ds, dsmax)
        while sc < 1:
            s1 = min(arb(1), (sc + ds).mid())
            T = [((p0[i] ** (1 - s1)) * (mu ** s1)).mid() for i in range(N)]
            wn, zn, good = newton(w, z, T, 40)
            if good:
                w, z, sc = wn, zn, s1; ds = min((ds * 2).mid(), dsmax); ncs += 1
            else:
                ds = (ds / 4).mid()
                if ds < arb("1e-9") or it >= maxit: ok = False; status = "centre-fail"; break
        if ok:
            w, z, ok = newton(w, z, mu, 40)
            if not ok: status = "centre-fail"
        wts = [arb(1)] * N
    else:
        # weighted path (default): the natural start lies EXACTLY on the weighted path w o z = t p0 at t = 1; follow t -> 0
        wts = p0
    tgt = lambda t: [(t * wts[i]).mid() for i in range(N)]
    f = arb("0.1")
    while ok and it < maxit:
        if certify() and os.environ.get("N6STOPCERT", "1") == "1": status = "cert"; break
        if mu * max(wts) < tiny: status = "converged"; break
        wn, zn, good = newton(w, z, tgt((mu * f).mid()), 40)
        if good:
            w, z, mu = wn, zn, (mu * f).mid(); nmu += 1
            f = max((f * f).mid(), arb("1e-4"))
        else:
            f = (f.sqrt()).mid()
            if f > 1 - arb(os.environ.get("N6FGAP", "1e-6")): status = "stalled"; break
    if it_cert is None: certify()
    return dict(n=g.n, N=N, d=d, bits=bits, prec=prec, it_cert=it_cert, it_total=it, status=status + f"/c{ncs}/mu{nmu}",
                mu=float(mu), secs=round(time.time() - t0, 1))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("game"); ap.add_argument("--maxit", type=int, default=500)
    ap.add_argument("--sol"); a = ap.parse_args()
    g = pg.parse("".join(l for l in open(a.game) if not l.lstrip().startswith("%")))
    r = (ipm if os.environ.get("N6ALG") == "ipm" else track)(g, a.maxit, sol=a.sol)
    print(",".join(str(r[k]) for k in ("n", "N", "d", "bits", "prec", "it_cert", "it_total", "status", "mu", "secs")))
