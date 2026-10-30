#!/usr/bin/env python3
"""L-COMP box 23 (Lead 2026-10-30): R*_F and FL_F per W-run of N5, my own implementation on L-COMP's engine n5b (SPEC mode).

Written from the TEXT of RESULTS R88 / R89 and docs/new/N5-FREE-box85.md §3 (l-new 893b9346); L-NEW's xirise.py / freeclass.py and
the n5x engine are NOT imported here (they are run only by xcheck.py, in a separate process).
- state t = (σ_t, τ_t); transitions t -> t+1 are n5b.N5.run's loop body (box17.Eng.step, unchanged); fb_t = S4c fallback flag.
- Ξ_t := Ξσ_t (n5b's VJ valuation of σ_t, Odd best reply); Iσ_t := {(y, z): y Even, Ξ_t(z) strictly better than Ξ_t(σ_t y)} (SPEC S2).
- W_t := the [S1-val] valuation of the (σ_t, τ_t)-plays = VJ valuation of σ_t in the game with Odd restricted to τ_t; λ_W its cycle-node map.
- τ-stretch: maximal run of consecutive states with τ constant. W-run (R89): a maximal run of consecutive states of one τ-stretch none of
  whose transitions is an S4c fallback or changes λ_W. Only W-runs with >= 1 transition are reported.
- BLOCKED at state q (R88): Even y, z in succ(y), z != σ_q(y), W_q(z) strictly better (Even) than W_q(σ_q y), and (y, z) not in Iσ_q.
- R*_F (R88 R*_T read on F, R89 GP*-RUN): the transitions t -> t+1 of F at which some Even y adopts an edge (y, z) (σ_{t+1}(y) = z !=
  σ_t(y)) that was BLOCKED at an earlier state q of F. Reading "earlier": q < t ("strict"; xirise.py's reading) and q <= t ("incl");
  both are computed. (incl = strict always: S4a moves y only inside Iσ_t, and S4c only to a best, hence improving, successor, so an
  edge blocked at t itself is never adopted at t -> t+1; the code checks this.)
- FL_F (R89 FL_S read on F): transitions of F with σ_{t+1} != σ_t and W_{t+1} = W_t (whole valuation; W_t evaluated with τ of F).
- FREE-RED (box 85 §3): |F| <= (n - 1)(R*_F + 1) + FL_F, checked.
Also per F: LA_F(y, z) = late adoptions of one edge (max over edges), SIG0 = transitions of F at which σ does not move (box 84 §4 says 0).
Usage: rstar.py GAME.pg [START] [-v]   (START: lines 'SIGMA0 v:w ...' / 'TAU0 v:w ...'; unlisted vertices keep S3)"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(ROOT, "n5-box17")); sys.path.insert(0, os.path.join(ROOT, "n5-second"))
import box17 as B  # noqa: E402
import n5b  # noqa: E402
from n5b import SpecSI, restrict, EVEN, ODD  # noqa: E402
import pg  # noqa: E402


class Eng(B.Eng):
    def __init__(self, g):
        super().__init__(g)
        self.ev_ = [v for v in range(g.n) if g.owner[v] == EVEN]
        self.wsi = {}

    def wval(self, sigma, tau):
        if tau not in self.wsi:
            self.wsi[tau] = SpecSI(restrict(self.g, [[tau[v]] if self.g.owner[v] == ODD else None for v in range(self.g.n)]))
        return self.wsi[tau].evaluate(list(sigma))

    def sdata(self, sigma, tau):
        """per state: W valuation, its cycle-node map, and the BLOCKED edges at this state."""
        g, SG = self.g, self.N.SG
        xi = SG.evaluate(list(sigma)); W = self.wval(sigma, tau)
        blk = []
        for y in self.ev_:
            for z in set(g.succ[y]):
                if z == sigma[y]:
                    continue
                if SG.nvo(W[sigma[y]], W[z]) < 0 and not SG.nvo(xi[sigma[y]], xi[z]) < 0:
                    blk.append((y, z))
        return dict(W=tuple(W), lw=tuple(x[0] for x in W), blk=frozenset(blk))


def wruns(eng, states, fbs, data):
    """states: list of (σ, τ); fbs[t]: fallback flag of t -> t+1; data[t] = eng.sdata(states[t]). Yields W-runs [a, b], b > a."""
    a = None
    for t in range(len(states) - 1):
        ok = states[t + 1][1] == states[t][1] and not fbs[t] and data[t + 1]["lw"] == data[t]["lw"]
        if ok:
            if a is None:
                a = t
        elif a is not None:
            yield a, t; a = None
    if a is not None:
        yield a, len(states) - 1


def measure(eng, states, data, a, b):
    """R*_F (strict, incl), FL_F, |F|, max late adoptions of one edge, σ-still transitions, for the W-run [a, b]."""
    ev = eng.ev_; first = {}  # edge -> first state of F at which it is BLOCKED
    rs = ri = fl = sig0 = 0; la = {}
    for t in range(a, b + 1):
        for e in data[t]["blk"]:
            first.setdefault(e, t)
        if t == b:
            break
        s0, s1 = states[t][0], states[t + 1][0]
        moved = [(y, s1[y]) for y in ev if s1[y] != s0[y]]
        sig0 += not moved
        strict = [e for e in moved if e in first and first[e] < t]
        rs += bool(strict); ri += any(e in first and first[e] <= t for e in moved)
        for e in strict:
            la[e] = la.get(e, 0) + 1
        fl += bool(moved) and data[t + 1]["W"] == data[t]["W"]
    return dict(a=a, b=b, F=b - a, rs=rs, ri=ri, fl=fl, la=max(la.values(), default=0), sig0=sig0)


def run_game(g, start=None, eng=None, cache=None):
    """the whole N5 run from start (default S3); returns (states, list of measure() dicts)."""
    eng = eng or Eng(g); x = start or eng.start(); states, fbs, data = [], [], []
    seen = set()
    while True:
        if x in seen:
            raise n5b.RepeatedState(str(x))
        seen.add(x)
        if cache is not None and x in cache:
            d, nxt = cache[x]
        else:
            d = eng.sdata(*x); nxt = eng.step(*x)
            if cache is not None:
                cache[x] = (d, nxt)
        states.append(x); data.append(d)
        if nxt is None:
            break
        fbs.append(nxt[2]); x = (nxt[0], nxt[1])
    return states, [measure(eng, states, data, a, b) for a, b in wruns(eng, states, fbs, data)]


def summary(g, runs):
    n = g.n
    mx = dict(rs=0, ri=0, fl=0, F=0, la=0, sig0=0)
    viol = 0
    for r in runs:
        for k in mx:
            mx[k] = max(mx[k], r[k])
        viol += r["F"] > (n - 1) * (r["rs"] + 1) + r["fl"]
    return dict(n=n, runs=len(runs), viol_freered=viol, incl_ne_strict=sum(r["ri"] != r["rs"] for r in runs), **mx)


def overlay(g, s3, part):
    """S3 start overridden by every VALID entry of a start file (owner matches the line, edge exists), as L-RED R99's fullstart2.py.
    A start file may be partial (red/n3/instances/n3cov_phi.start) or carry wrong-owner entries (n3cov_lean.start, R99 erratum)."""
    return tuple(tuple(w if w != -1 and g.owner[v] == i and w in g.succ[v] else d for v, (d, w) in enumerate(zip(s3[i], part[i])))
                 for i in (0, 1))


def main():
    g = pg.read(sys.argv[1])
    st = None
    if len(sys.argv) > 2:
        st = overlay(g, Eng(g).start(), n5b.read_start(sys.argv[2], g))
    states, runs = run_game(g, st)
    print(f"RSTAR it {len(states) - 1} {summary(g, runs)}")
    if "-v" in sys.argv:
        for r in runs:
            print(" ", r)


if __name__ == "__main__":
    main()
