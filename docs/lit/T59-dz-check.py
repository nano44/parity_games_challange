#!/usr/bin/env python3
"""L-LIT T59 (docs/lit/T59-elimination-windows.md §4): the Zhong-Ye / Post-Ye undiscounted Dantzig contraction (arXiv 2609.40147
Thm 7.1, eq. (7.2)-(7.6)) read inside one W-run of N5. W-runs as in docs/lit/T58-elim-check.py (tau fixed, no fallback, W's cycle
nodes fixed). Numeric embedding of W (si.py Engine.key): for a vertex with W-value (c, P, l),
    V := weight(P) * BIG + (l if c is odd else -l),   BIG := 2n + 2,
so V is additive along a path to the fixed cycle node c and orders values with the same c exactly as Engine.key does.
At each state t of a W-run F = p..q (q its last state), over Even vertices v (succ = target of the edge):
    gap_t := sum_v' (V_q(v') - V_t(v'))        (all vertices; >= 0 by W-monotonicity on F)
    A_t   := max over (v, w) in I_sigma_t with lam_t(w) = lam_t(v) and v not on w's (sigma_t, tau)-play (no new cycle) of
             V_t(w) - V_t(sigma_t(v))                                                              (best ALLOWED residual)
    B_t   := max over Even v of V_t(sigma_q(v)) - V_t(sigma_t(v))                                  (best REFERENCE residual)
    BL_t  := the same max over v with (v, sigma_q(v)) neither sigma_t's edge nor in I_sigma_t   (BLOCKED reference residual)
Checks (must be 0 if the T59 §4 proof is right): STEPV  gap_{t+1} > gap_t - A_t;  GAPV  gap_t > n^2 * B_t;  MONV  V_{t+1} < V_t somewhere.
Reports per file: maxima over W-runs of LEN, KMAX = max_t B_t / A_t (A_t > 0), KBL = max_t BL_t / A_t, and HB = max_t (bit length of B_t
minus bit length of A_t) (the ordinal form of BLOCK-RATIO: the top rank where the reference gains vs where the arena can gain); ZERO_A =
states with gap_t > 0 and A_t <= 0 (W-flat transitions; FW-R*'s FL); CMIN = min_t (gap_t - gap_{t+1}) / gap_t over
states with A_t > 0 (the per-step contraction N5 actually achieved; Zhong-Ye's rule guarantees >= 1/n^2); WINC = max_t of the
first k with gap_{t+k} < gap_t / n^2 (or t + k = q): the windowed contraction that Zhong-Ye's elimination step (7.5) needs. Usage (repo root): python3 -I docs/lit/T59-dz-check.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
import importlib.util
_spec = importlib.util.spec_from_file_location("t58", os.path.join(HERE, "T58-elim-check.py")); t58 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(t58)
from n5x import load, readstart, Engine, dual
import pg

def run(g, start=None):
    n = g.n; own = g.owner; E = Engine(g); BIG = 2 * n + 2
    c = dict(WINC=0, CMIN=1.0, RUNS=0, LEN=0, STEPV=0, GAPV=0, MONV=0, ZERO_A=0, KMAX=0.0, KBL=0.0, HB=-10 ** 9, BLSTATES=0, STATES=0)
    for F, taus in wruns_t(g, start):
        if len(F) < 2: continue
        c['RUNS'] += 1; c['LEN'] = max(c['LEN'], len(F) - 1)
        tau = taus
        Ew = Engine(pg.Game(list(g.prio), list(g.owner), [[tau[v]] if own[v] == 1 else list(g.succ[v]) for v in range(n)]))
        def V(s):
            val = Ew.evaluate(s)[0]
            return [E.weight(p) * BIG + (l if E.par[w] == 1 else -l) for (w, p, l) in val], [w for (w, _, _) in val]
        Vs = [V(s) for s in F]; Vq, lq = Vs[-1]; last = F[-1]
        gaps = [sum(Vq[x] - Vt[x] for x in range(n)) for Vt, _ in Vs]
        for i in range(len(F)):
            if gaps[i] > 0:
                c['WINC'] = max(c['WINC'], next(k for k in range(1, len(F) - i + 1) if i + k == len(F) - 1 or gaps[i + k] * n * n < gaps[i]))
            Vt, lt = Vs[i]; s = F[i]
            if i + 1 < len(F) and any(Vs[i + 1][0][x] < Vt[x] for x in range(n)): c['MONV'] += 1
            if gaps[i] <= 0: continue
            c['STATES'] += 1
            Xi = E.evaluate(s)[0]; Is = E.improving(s, Xi)
            def through(w, v):
                x = w
                for _ in range(n + 1):
                    if x == v: return True
                    x = s[x] if own[x] == 0 else tau[x]
                return False
            A = max([Vt[w] - Vt[s[v]] for v, w in Is if lt[w] == lt[v] and not through(w, v)], default=None)
            ref = [(v, Vt[last[v]] - Vt[s[v]]) for v in range(n) if own[v] == 0]
            B = max(r for _, r in ref)
            Iset = set(Is)
            bl = [r for v, r in ref if last[v] != s[v] and (v, last[v]) not in Iset]
            BL = max(bl, default=0)
            if BL > 0: c['BLSTATES'] += 1
            if gaps[i] > n * n * B: c['GAPV'] += 1
            if A is None or A <= 0:
                c['ZERO_A'] += 1; continue
            if i + 1 < len(F) and gaps[i + 1] > gaps[i] - A: c['STEPV'] += 1
            if i + 1 < len(F): c['CMIN'] = min(c['CMIN'], (gaps[i] - gaps[i + 1]) / gaps[i])
            c['KMAX'] = max(c['KMAX'], B / A); c['KBL'] = max(c['KBL'], BL / A)
            c['HB'] = max(c['HB'], B.bit_length() - A.bit_length())
    return c

def wruns_t(g, start=None):
    """T58's W-run splitter, also returning the run's (fixed) tau."""
    n = g.n; own = g.owner; E, Ed = Engine(g), Engine(dual(g)); WE = {}
    s, t = t58.start_pair(g, E, Ed, start); s, t = tuple(s), tuple(t)
    def W(s, t):
        if t not in WE:
            WE[t] = Engine(pg.Game(list(g.prio), list(g.owner), [[t[v]] if own[v] == 1 else list(g.succ[v]) for v in range(n)]))
        return WE[t].evaluate(s)[0]
    run = [s]; w = W(s, t); rt = t
    while True:
        r = t58.step(g, E, Ed, list(s), list(t))
        if r is None: break
        ns, nt, _, _, fb, _, _ = r; ns, nt = tuple(ns), tuple(nt)
        w1 = W(ns, nt) if nt == t else None
        if nt != t or fb or any(w1[x][0] != w[x][0] for x in range(n)):
            yield run, rt; run = [ns]; rt = nt
        else:
            run.append(ns)
        s, t, w = ns, nt, W(ns, nt)
    yield run, rt

if __name__ == '__main__':
    a = sys.argv[1:]; g = load(a[0]); c = run(g, readstart(a[1]) if len(a) > 1 else None)
    print(f"T59 {os.path.basename(a[0])} n {g.n} " + " ".join(f"{k} {v:.3g}" if isinstance(v, float) else f"{k} {v}" for k, v in c.items()))
