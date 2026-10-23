#!/usr/bin/env python3
"""N7: entropic temperature homotopy on the parity-induced discounted game (docs/new/N7-entropic.md). Same pipeline as n6.py up to the
binary discounted game (compressed priorities, weights (-B)^p scaled to max 1, gamma = beta_G). For temperature tau the soft Bellman
operator  T_tau(v)_i = s_i * tau * log sum_a exp(s_i (c_i + gamma v_{succ_a(i)}) / tau)   (s_i = +1 Even/max, -1 Odd/min)
is a gamma-contraction in sup norm, so v_tau is unique. Path following: Newton on F(v) = v - T_tau(v), J = I - gamma P_pi (soft policy pi),
backtracking on |F|_inf; tau <- f tau with adaptive f (success f <- max(f^2, 1e-4), failure f <- sqrt f). Start tau0 = 4 ginv (scaled),
v from the uniform policy. After every tau-step the hard rounding (argmax/argmin of Q) is certified with harness/verify.py.
Count = Newton steps. Usage: n7.py game.pg [--maxit K] [--sol out.sol] -> n,N,d,bits,prec,it_cert,it_total,status,tau_final,secs"""
import sys, os, time, argparse
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import pg, verify
from n6 import binarize, compress, strategies_from, regions
from flint import arb_mat, arb, ctx


def setup(g):
    states = binarize(g); N = len(states)
    cp = compress(g.prio); d = max(cp); B = N + 1
    ginv = 4 * N ** 3 * B ** d
    if os.environ.get("N6GINV"): ginv = int(os.environ["N6GINV"])
    bits = ginv.bit_length()
    ctx.prec = int(os.environ.get("N6PRECF", "8")) * bits + 16 * N.bit_length() + 64
    gamma = arb(1) - arb(1) / arb(ginv)
    sgn = [1 if states[i][0] == 0 else -1 for i in range(N)]
    cost = [0 if states[i][1] is None else (-B) ** cp[states[i][1]] for i in range(N)]
    cmax = max(abs(x) for x in cost) or 1
    c = [arb(x) / cmax for x in cost]
    return states, N, d, bits, ctx.prec, gamma, sgn, c, ginv


def run(g, maxit=20000, sol=None):
    t0 = time.time()
    states, N, d, bits, prec, gamma, sgn, c, ginv = setup(g)
    succ = [states[i][2] for i in range(N)]
    it = 0; it_cert = None; status = "maxit"; ntau = 0

    def soft(v, tau):
        """T_tau(v), soft policies pi[i] = (p0, p1)"""
        Tv, pi = [], []
        for i in range(N):
            q0 = (c[i] + gamma * v[succ[i][0]]) * sgn[i]; q1 = (c[i] + gamma * v[succ[i][1]]) * sgn[i]
            m = q0 if q0 > q1 else q1
            e0 = ((q0 - m) / tau).exp(); e1 = ((q1 - m) / tau).exp(); Z = e0 + e1
            Tv.append(((m + tau * Z.log()) * sgn[i]).mid()); pi.append(((e0 / Z).mid(), (e1 / Z).mid()))
        return Tv, pi

    def resid(v, tau):
        Tv, pi = soft(v, tau)
        return [(v[i] - Tv[i]).mid() for i in range(N)], pi

    def newton(v, tau, tol, cap):
        nonlocal it
        for _ in range(cap):
            F, pi = resid(v, tau); fn = max(abs(x) for x in F)
            if fn <= tol: return v, True
            if it >= maxit: return v, False
            it += 1
            J = arb_mat(N, N)
            for i in range(N):
                J[i, i] += 1
                J[i, succ[i][0]] -= (gamma * pi[i][0]).mid(); J[i, succ[i][1]] -= (gamma * pi[i][1]).mid()
            dv = J.solve(arb_mat(N, 1, [-x for x in F]), algorithm="approx").mid()
            a = arb(1); ok = False
            while a > arb("1e-30"):
                vn = [(v[i] + a * dv[i, 0]).mid() for i in range(N)]
                Fn, _ = resid(vn, tau)
                if max(abs(x) for x in Fn) < fn * (1 - a / 10): ok = True; break
                a = (a * arb("0.5")).mid()
            if not ok: return v, False
            v = vn
        return v, False

    def certify(v):
        nonlocal it_cert
        choice = []
        for i in range(N):
            q0 = (c[i] + gamma * v[succ[i][0]]) * sgn[i]; q1 = (c[i] + gamma * v[succ[i][1]]) * sgn[i]
            choice.append(0 if q0 >= q1 else 1)
        strat = strategies_from(g, states, choice); win = regions(g, strat)
        if not verify.check(g, win, strat):
            if it_cert is None:
                it_cert = it
                if sol: pg.write_sol(win, sol, strat)
            return True
        return False

    tau = arb(4 * ginv)
    # start: uniform policy values (exact solve), then Newton at tau0
    J = arb_mat(N, N); rhs = arb_mat(N, 1)
    for i in range(N):
        J[i, i] += 1; J[i, succ[i][0]] -= gamma / 2; J[i, succ[i][1]] -= gamma / 2; rhs[i, 0] = c[i]
    v0 = J.solve(rhs, algorithm="approx").mid(); v = [v0[i, 0] for i in range(N)]
    tolrel = arb(os.environ.get("N7TOL", "1e-3"))   # path neighbourhood: |F|_inf <= tolrel * tau
    v, ok = newton(v, tau, (tolrel * tau).mid(), 200)
    if not ok: status = "start-fail"
    f = arb("0.5"); tiny = arb(2) ** (-(prec - 64))
    while ok and it < maxit:
        if certify(v) and os.environ.get("N6STOPCERT", "1") == "1": status = "cert"; break
        if tau < tiny: status = "converged"; break
        tn = (tau * f).mid()
        vn, good = newton(v, tn, (tolrel * tn).mid(), 40)
        if good:
            v, tau = vn, tn; ntau += 1; f = max((f * f).mid(), arb("1e-4"))
        else:
            f = f.sqrt().mid()
            if f > 1 - arb("1e-12"): status = "stalled"; break
    if it_cert is None: certify(v)
    return dict(n=g.n, N=N, d=d, bits=bits, prec=prec, it_cert=it_cert, it_total=it, status=status + f"/tau{ntau}",
                tau=float(tau), secs=round(time.time() - t0, 1))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("game"); ap.add_argument("--maxit", type=int, default=20000)
    ap.add_argument("--sol"); a = ap.parse_args()
    g = pg.parse("".join(l for l in open(a.game) if not l.lstrip().startswith("%")))
    r = run(g, a.maxit, sol=a.sol)
    print(",".join(str(r[k]) for k in ("n", "N", "d", "bits", "prec", "it_cert", "it_total", "status", "tau", "secs")))
