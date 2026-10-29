#!/usr/bin/env python3
"""L-COMP box 17 (Lead 2026-10-29 09:59Z): per N5 run, the four L-SI quantities, on L-COMP's own engine n5b (SPEC mode).

Written from the TEXT of L-SI's definitions (docs/si/N5-GRUN-box25.md §4-§5, docs/si/N5-LAY-box27.md §6, docs/si/N5-ALT-box23.md §13);
the plays, cycles, segments and counts below are computed here, not imported from experiments/si/.
- state t: (σ_t, τ_t); Ξ_t = Ξσ_t (n5b's VJ valuation (cycle node, path set, length)); σ̄_t = Odd's best reply to σ_t (SPEC S1 choice);
  honest successor map: σ on Even, σ̄ on Odd; W successor map: σ on Even, τ on Odd. fb_t = 1 if the transition t → t + 1 is a fallback.
- phase: a maximal block [i, j], j > i, of consecutive states with the same key (cycle node of Ξ_t at every vertex, τ_t) (RESULTS R38 KEY).
  f(P) := the fallbacks t → t + 1 with t, t + 1 ∈ P (in-phase fallbacks). CONJECTURE FB-LIN: f ≤ n.
- run: a maximal stretch [s, e] of states of one phase with no fallback between them.
- Q := Even vertices of out-degree ≥ 2. At a state b of a run: X_b := least set containing Q and every Even vertex on the W-play or
  honest play at b of a member; RO_b := Odd vertices on the honest b-play of a member of X_b; CW_b / CH_b := the cycles reached by the
  W- / honest b-plays of members of X_b. [a, b] is REL-admissible if it lies in one run, σ̄_t = σ̄_b on RO_b and every cycle of CW_b
  (CH_b) is a cycle of the W- (honest) successor map at every t ∈ [a, b]. A run [s, e] is cut from its end into maximal REL segments
  (b_1 = e, a_i least, b_{i+1} = a_i − 1, down to s); SEG(S) := the number of segments. CONJECTURE SEG-RUN: SEG = O(n).
- SEG-COUNT excess of a segment [a, b] (b > a): (b − a) − #{Even v : σ_t(v) ≠ σ_{t+1}(v) for some t ∈ [a, b)}. CONJECTURE SEG-COUNT: ≤ 0.
- L-WAVE′ events of a run [s, e]: (i) a cut a_i − 1 → a_i (a_i > s) that is not an L-cut, recorded at a_i; an L-cut is one where the set
  ch of Odd vertices u ∈ RO_{b_i} with σ̄_{a_i − 1}(u) ≠ σ̄_{a_i}(u) is nonempty and at each u ∈ ch Ξ(u) changes in its length only (same
  path set, Ξ different); (ii) every t ∈ [max(a_i, s + 1), b_i] such that the path set of Ξ changes from t − 1 to t at some Odd vertex of
  RO_{b_i} of out-degree ≥ 2. Gaps: consecutive points of {s} ∪ events ∪ {e}; gap length y − x. CONJECTURE L-WAVE′: every gap ≤ n − 1.
  (Reading where the text is silent, taken from L-SI's grun/lwave.py docstring and logic: events (ii) at t = a_i count, i.e. "inside
  [a, b] (or into it)"; a cut with ch = ∅ (a cycle appearance) is non-L.)
- DEADLOCK step of a segment [a, b] (b > a) (docs/si/N5-CHG-box28.md §0): t ∈ [a, b) at which no Even vertex makes its last switch in
  [a, b]. dl := max over segments of #{deadlock t > r0}, r0 the first state of the run (L-SI's DLRUN_V counts segments with dl > 0)."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(ROOT, "n5-second"))
import n5b  # noqa: E402
from n5b import N5, SpecSI, dual, restrict, EVEN, ODD  # noqa: E402,F401


class Eng:
    """n5b SPEC mode, one transition at a time (the body of n5b.N5.run's loop, unchanged), plus the per-state data."""

    def __init__(self, g):
        self.g = g; self.N = N5(g, mode="spec"); self.n = g.n
        self.Q = [v for v in range(g.n) if g.owner[v] == EVEN and len(set(g.succ[v])) >= 2]
        self.oddch = {v for v in range(g.n) if g.owner[v] == ODD and len(set(g.succ[v])) >= 2}

    def start(self):
        return (tuple(self.N.SG.initial_strategy_by_best_reward()), tuple(self.N.SD.initial_strategy_by_best_reward()))

    def step(self, sigma, tau):
        """None at termination, else (sigma2, tau2, isfb): exactly n5b.N5.run's iteration body."""
        N, g = self.N, self.g; sigma, tau = list(sigma), list(tau)
        vs = N.ev(N.SG, sigma); vt = N.ev(N.SD, tau)
        Is, It = N.improving(N.SG, sigma, vs), N.improving(N.SD, tau, vt)
        if not Is and not It:
            return None
        allow = [None] * g.n
        for v in range(g.n):
            allow[v] = [sigma[v]] + Is.get(v, []) if g.owner[v] == EVEN else [tau[v]]
        s2 = SpecSI(dual(restrict(g, allow)))
        _, c2 = N.opt(s2, [tau[v] if g.owner[v] == ODD else -1 for v in range(g.n)])
        sigma2 = [c2[v] if g.owner[v] == EVEN else -1 for v in range(g.n)]
        allow = [None] * g.n
        for v in range(g.n):
            if g.owner[v] == ODD:
                allow[v] = [tau[v]] + It.get(v, [])
        s3 = SpecSI(restrict(g, allow))
        _, c3 = N.opt(s3, sigma)
        tau2 = [c3[v] if g.owner[v] == ODD else -1 for v in range(g.n)]
        isfb = sigma2 == sigma and tau2 == tau
        if isfb:
            if Is:
                sigma2 = list(sigma)
                for v in Is:
                    sigma2[v] = N.SG.best(vs, v)
            else:
                tau2 = list(tau)
                for v in It:
                    tau2[v] = N.SD.best(vt, v)
        return tuple(sigma2), tuple(tau2), int(isfb)

    def info(self, sigma, tau):
        g = self.g; xi, sb = self.N.SG.evaluate_choice(list(sigma))
        hn = tuple(sigma[v] if g.owner[v] == EVEN else sb[v] for v in range(g.n))
        wn = tuple(sigma[v] if g.owner[v] == EVEN else tau[v] for v in range(g.n))
        return dict(s=sigma, t=tau, sb=tuple(sb), xi=xi, hn=hn, wn=wn, key=(tuple(x[0] for x in xi), tau),
                    cw=cycles(wn), ch=cycles(hn))


def play(nx, v):
    """v's play under nx: (vertices before the cycle, the cycle normalized to start at its least vertex)."""
    path, pos, x = [], {}, v
    while x not in pos:
        pos[x] = len(path); path.append(x); x = nx[x]
    c = path[pos[x]:]; k = c.index(min(c))
    return tuple(path[:pos[x]]), tuple(c[k:] + c[:k])


def cycles(nx):
    return frozenset(play(nx, v)[1] for v in range(len(nx)))


def trajectory(eng, st, cache=None):
    """states from st to termination: list of info dicts, each with fb (of the transition leaving it; 0 at the end)."""
    R = []; seen = set(); x = st
    while True:
        if x in seen:
            raise n5b.RepeatedState(str(x))
        seen.add(x)
        if cache is not None and x in cache:
            I, nxt = cache[x]
        else:
            I = eng.info(*x); r = eng.step(*x); nxt = r
            if cache is not None:
                cache[x] = (I, nxt)
        I = dict(I); I["fb"] = nxt[2] if nxt else 0; R.append(I)
        if nxt is None:
            return R
        x = (nxt[0], nxt[1])


def phases(R):
    i = 0
    while i < len(R):
        j = i
        while j + 1 < len(R) and R[j + 1]["key"] == R[i]["key"]:
            j += 1
        if j > i:
            yield i, j
        i = j + 1


def runs_of(R, i, j):
    s = i
    for k in range(i, j + 1):
        if k == j or R[k]["fb"]:
            yield s, k
            s = k + 1


def segments(eng, R, s, e):
    """maximal REL segments of run [s, e], from the end; each (a, b, RO_b)."""
    g = eng.g; out = []; b = e
    while b >= s:
        B = R[b]; X = set(); st = list(eng.Q); CW = set(); CH = set(); RO = set()
        while st:
            x = st.pop()
            if x in X:
                continue
            X.add(x)
            pw, cw = play(B["wn"], x); ph, chh = play(B["hn"], x)
            CW.add(cw); CH.add(chh)
            for y in pw + cw + ph + chh:
                if g.owner[y] == EVEN and y not in X:
                    st.append(y)
            RO.update(y for y in ph + chh if g.owner[y] == ODD)
        a = b
        while a > s and all(R[a - 1]["sb"][u] == B["sb"][u] for u in RO) and CW <= R[a - 1]["cw"] and CH <= R[a - 1]["ch"]:
            a -= 1
        out.append((a, b, RO)); b = a - 1
    return out


def analyse(eng, R):
    """per trajectory: dict with max values and the argmax places."""
    g, n = eng.g, eng.n; res = dict(f=-1, f_at=None, seg=0, seg_at=None, exc=None, exc_at=None, gap=-1, gap_at=None, dl=0, dl_at=None, dead=0, runs=0,
                                    phases=0, segs=0, gaps=0, it=len(R) - 1)
    for i, j in phases(R):
        res["phases"] += 1
        f = sum(R[k]["fb"] for k in range(i, j))
        if f > res["f"]:
            res["f"], res["f_at"] = f, (i, j)
        for s, e in runs_of(R, i, j):
            if e <= s:
                continue
            res["runs"] += 1; SG = segments(eng, R, s, e)
            if len(SG) > res["seg"]:
                res["seg"], res["seg_at"] = len(SG), (s, e)
            ev = []
            for a, b, RO in SG:
                if b > a:
                    res["segs"] += 1
                    sw = {v for t in range(a, b) for v in eng.Q if R[t]["s"][v] != R[t + 1]["s"][v]}
                    exc = (b - a) - len(sw)
                    if res["exc"] is None or exc > res["exc"]:
                        res["exc"], res["exc_at"] = exc, (a, b)
                    last = {v: max(t for t in range(a, b) if R[t]["s"][v] != R[t + 1]["s"][v]) for v in sw}
                    D = [t for t in range(a, b) if t not in set(last.values())]      # DEADLOCK steps (N5-CHG-box28 §0)
                    res["dead"] += len(D); dr = sum(1 for t in D if t > s)             # DL-RUN: deadlock steps t > r0 = s
                    if dr > res["dl"]:
                        res["dl"], res["dl_at"] = dr, (a, b, s, D)
                for t in range(max(a, s + 1), b + 1):
                    if any(R[t - 1]["xi"][u][1] != R[t]["xi"][u][1] for u in RO if u in eng.oddch):
                        ev.append(t)
                if a > s:
                    ch = [u for u in RO if R[a - 1]["sb"][u] != R[b]["sb"][u]]
                    isL = bool(ch) and all(R[a - 1]["xi"][u][1] == R[a]["xi"][u][1] and R[a - 1]["xi"][u] != R[a]["xi"][u] for u in ch)
                    if not isL:
                        ev.append(a)
            pts = sorted(set([s] + ev + [e]))
            for x, y in zip(pts, pts[1:]):
                res["gaps"] += 1
                if y - x > res["gap"]:
                    res["gap"], res["gap_at"] = y - x, (x, y)
    return res
