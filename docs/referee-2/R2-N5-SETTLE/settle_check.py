#!/usr/bin/env python3
r"""REFEREE-2 successor 23 (Opus 5.5, D15): own check of P-N5-SETTLE (docs/si/P-N5-SETTLE-box52.md @ l-si 6a70a520, sha1 aef403c3).
State construction: my R2-N5-LATEP/latep_check.py (my N5 loop; W-runs as in R89); start files as in R2-N5-WRUN/wrun_check.py (forced
vertices repaired). The lane's experiments/si/heads52/*.py are NOT imported. Definitions from the packet text (U_k, EVENT from R143).
Checks per W-run F (each must be 0):
  S / X    RUN-SETTLE (S_j), (X_j) in every event-free block; BLK block length <= n - 1;  RC  RUN-COUNT |F| <= n(E_F + 1) - 1
  PC       PLAY-CAUSE: every x with a Xi-change at an event-free transition has a switched Even y not in C on x's (sigma_{k+1}, tau)-path
  HR       HEAD-RED: E_F <= sum SB_F(o) + sum CN_F(c) + sum HXU_F(u)
  WM       W-MON at every transition of F
  IDX/LEX  at every transition of F and every Even y with lambda_W(y) != y: sigma_{k+1}(y) is the smallest-index (Omega(c) odd) or the
           lexicographically least key (Omega(c) even) W_{k+1}-tight edge of H_k(y) (IDX-MONO / LEX-BFS with Claim RG', as RUN-SETTLE reads them)
  TX       T-XCH on the whole run: T <= m_E(1 + XE) + m_O(1 + XO)
Counters: case split of switches at j >= 1 (C1, WR, C2a, C2b, C2c), events by kind, longest event-free block.
Usage: settle_check.py files list.txt [runs [prefix]] | random N nmin nmax seed [starts]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-LATEP"))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-WRUN"))
import latep_check as L
import wrun_check as WR
RUN = {}


def mxt(st, k, v):
    if k not in st.mx or v > st.mx[k]: st.mx[k] = v


def wpath(nx, x, C):
    p = [x]
    while p[-1] not in C:
        p.append(nx[p[-1]])
        if len(p) > len(nx) + 1: return None
    return p


def wrun(g, E, info, a, b, st, name, Even, nE, mE, dE):
    n = g.n; K = E.key; T = b - a
    st.inc("WRUNS"); st.inc("WRUN_transitions", T)
    C = {v for v in range(n) if info[a]["lamW"][v] == v}
    tau = info[a]["tu"]
    nxW = [[info[t]["sg"][v] if g.owner[v] == 0 else tau[v] for v in range(n)] for t in range(a, b + 1)]
    def ell(t, x): return info[t]["W"][x][2]
    def U(t):
        I = info[t]; u = {I["sbar"][o] for o in range(n) if g.owner[o] == 1 and I["sbar"][o] != tau[o]}
        for c in C: u.add(I["sg"][c] if g.owner[c] == 0 else I["sbar"][c])
        return u
    Us = [U(t) for t in range(a, b + 1)]
    ev = []; SB = {}; CN = {}; HX = {}
    for k in range(a, b):
        A, B = info[k], info[k + 1]
        e1 = [o for o in range(n) if g.owner[o] == 1 and A["sbar"][o] != B["sbar"][o]]
        e2 = [c for c in C if g.owner[c] == 0 and A["sg"][c] != B["sg"][c]]
        e3 = [u for u in Us[k - a] | Us[k + 1 - a] if A["xi"][u] != B["xi"][u]]
        for o in e1: SB[o] = SB.get(o, 0) + 1
        for c in e2: CN[c] = CN.get(c, 0) + 1
        for u in e3: HX[u] = HX.get(u, 0) + 1
        st.inc("EV_i", bool(e1)); st.inc("EV_ii", bool(e2)); st.inc("EV_iii", bool(e3))
        ev.append(bool(e1 or e2 or e3))
        if any(K(B["W"][v]) < K(A["W"][v]) for v in range(n)): st.bad("WM", f"{name}@{k}")
        # IDX-MONO / LEX-BFS
        for y in range(n):
            if g.owner[y] != 0 or y in C: continue
            c = info[k]["lamW"][y]
            H = {A["sg"][y]} | {z for (yy, z) in A["Is"] if yy == y}
            Wn = B["W"]
            tight = [z for z in H if E.extend(y, Wn[z]) == Wn[y]]
            ch = B["sg"][y]
            if ch not in tight: st.bad("IDX", f"{name}@{k} y={y} choice not tight"); continue
            if g.prio[c] % 2 == 1:
                st.inc("IDX_checks")
                if ch != min(tight): st.bad("IDX", f"{name}@{k} y={y} {ch} vs {min(tight)}")
            else:
                st.inc("LEX_checks")
                def key(z):
                    p = wpath(nxW[k + 1 - a], z, C); return tuple(reversed(p[:-1])) if p else None
                best = min(tight, key=lambda z: key(z))
                if ch != best: st.bad("LEX", f"{name}@{k} y={y} {ch} vs {best}")
    E_F = sum(ev)
    if T > n * (E_F + 1) - 1: st.bad("RC", f"{name} F[{a},{b}] |F| {T} E {E_F}")
    if E_F > sum(SB.values()) + sum(CN.values()) + sum(HX.values()): st.bad("HR", f"{name}")
    mxt(st, "max_E_F", (E_F, name))
    k = a
    while k < b:
        if ev[k - a]: k += 1; continue
        k0 = k
        while k < b and not ev[k - a]: k += 1
        k1 = k; mxt(st, "max_block", (k1 - k0, name))
        if k1 - k0 > n - 1: st.bad("BLK", f"{name} block [{k0},{k1}]")
        for kk in range(k0, k1):
            j = kk - k0; A, B = info[kk], info[kk + 1]
            sw = [y for y in range(n) if g.owner[y] == 0 and A["sg"][y] != B["sg"][y]]
            for y in sw:
                if ell(kk + 1, y) < j + 1: st.bad("S", f"{name}@{kk} j={j} y={y}")
            for x in range(n):
                if A["xi"][x] == B["xi"][x]: continue
                if ell(kk + 1, x) < j + 1: st.bad("X", f"{name}@{kk} j={j} x={x}")
                p = wpath(nxW[kk + 1 - a], x, C)
                if not p or not any(v in sw and v not in C for v in p[:-1]): st.bad("PC", f"{name}@{kk} x={x}")
            if j >= 1:   # case split (statistics)
                for y in sw:
                    a_, b_ = A["sg"][y], B["sg"][y]
                    Hprev = {info[kk - 1]["sg"][y]} | {z for (yy, z) in info[kk - 1]["Is"] if yy == y}
                    if b_ not in Hprev: st.inc("CASE1"); continue
                    if A["W"][b_] != B["W"][b_]: st.inc("CASE_WR"); continue
                    if E.extend(y, B["W"][a_]) == B["W"][y]: st.inc("CASE2a"); continue
                    p = wpath(nxW[kk + 1 - a], a_, C)
                    st.inc("CASE2c" if p and y in p else "CASE2b")
        st.inc("BLOCKS")


_orig = WR._orig_run_game
def run_game(g, s, t, st, name):
    orig = L.wrun
    def cap(g_, E, info, a, b, st_, name_, Even, nE, mE, dE):
        RUN["info"] = info; wrun(g_, E, info, a, b, st_, name_, Even, nE, mE, dE)
    L.wrun = cap
    try: _orig(g, s, t, st, name)
    finally: L.wrun = orig
    info = RUN.get("info")
    if not info: return
    n = g.n; Ed = L.Engine(L.dual(g)); Tn = len(info) - 1
    Us = [Ed.evaluate(tuple(I["tu"][v] if g.owner[v] == 1 else -1 for v in range(n)))[0] for I in info]
    XE = max((sum(info[k + 1]["xi"][c] != info[k]["xi"][c] for k in range(Tn)) for c in range(n)), default=0)
    XO = max((sum(Us[k + 1][c] != Us[k][c] for k in range(Tn)) for c in range(n)), default=0)
    mE = sum(len(set(g.succ[v])) for v in range(n) if g.owner[v] == 0); mO = sum(len(set(g.succ[v])) for v in range(n) if g.owner[v] == 1)
    if Tn > mE * (1 + XE) + mO * (1 + XO): st.bad("TX", f"{name} T {Tn}")
    RUN.clear()
L.run_game = run_game
L.read_start = WR.read_start
KEYS = ("S", "X", "BLK", "RC", "PC", "HR", "WM", "IDX", "LEX", "TX", "XIPLAY", "XW", "XIMON")
if __name__ == "__main__":
    import io, contextlib, re
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf): L.main()
    out = buf.getvalue().splitlines(); bad = 0
    for l in out:
        if not l.startswith("RESULT"): print(l)
        m = re.match(r"(\S+): (\d+)$", l)
        if m and m[1] in KEYS: bad += int(m[2])
    print("RESULT", "PASS" if bad == 0 else "FAIL", "violations", bad)
