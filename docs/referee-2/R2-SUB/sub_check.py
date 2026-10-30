#!/usr/bin/env python3
r"""REFEREE-2 successor 22 (Opus 5.5, D15): check of premise [SUB] (L-NEW box 89): R88's FW-R* on every sub-interval F' = [a', b'] of a
W-run F, with BLOCKED and late adoptions read at states of F' (late: adoption at tau in [a', b') of an edge blocked at some t in [a', tau)).
Reuses my R2-N5-LATEP/latep_check.py state construction (my N5 loop; no lane code). For every W-run F of length <= SUBMAX all sub-intervals,
else SUBS random ones per W-run. Checks: SUB  WCH_{F'} <= (n - 1)(R*_T(F') + 1).  Control X_SUB0: WCH_{F'} > n - 1 (the bound is not
trivially n - 1 there). Also GPB: GP*'s base reading on F' (every u with lambda_W(u) = u has W_{a'}(u) = (u, empty, 0)).
Usage: sub_check.py files list.txt [runs [prefix]] | random N nmin nmax seed [starts]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-LATEP"))
import latep_check as L
SUBMAX = int(os.environ.get("SUBMAX", "40")); SUBS = int(os.environ.get("SUBS", "400"))
_rng = random.Random(4646)


def wrun_sub(g, E, info, a, b, st, name, Even, nE, mE, dE):
    n = g.n; K = E.key
    def blocked(t, y, z):
        I = info[t]; r = I["sg"][y]
        return z != r and (y, z) not in I["Is"] and K(I["W"][z]) > K(I["W"][r])
    if b - a <= SUBMAX: pairs = [(x, y) for x in range(a, b + 1) for y in range(x + 1, b + 1)]
    else: pairs = [tuple(sorted(_rng.sample(range(a, b + 1), 2))) for _ in range(SUBS)]
    for (a2, b2) in pairs:
        st.inc("SUB_checks")
        for u in range(n):
            if info[a2]["lamW"][u] == u and info[a2]["W"][u] != (u, 0, 0): st.bad("GPB", f"{name} [{a2},{b2}] u={u}")
        WCH = sum(info[t + 1]["W"] != info[t]["W"] for t in range(a2, b2))
        RT = 0
        for tau in range(a2, b2):
            ad = [(y, info[tau + 1]["sg"][y]) for y in Even if info[tau + 1]["sg"][y] != info[tau]["sg"][y]]
            if any(any(blocked(t, y, z) for t in range(a2, tau)) for (y, z) in ad): RT += 1
        if WCH > (n - 1) * (RT + 1): st.bad("SUB", f"{name} F[{a},{b}] sub [{a2},{b2}] WCH {WCH} RT {RT}")
        if WCH > n - 1: st.inc("X_SUB0")
        st.mxu("max_sub_WCH", WCH); st.mxu("max_sub_RT", RT)


L.wrun = wrun_sub
_keys = ("SUB", "GPB")
if __name__ == "__main__":
    import io, contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf): L.main()
    out = buf.getvalue().splitlines()
    for l in out:
        if not l.startswith("RESULT"): print(l)
    import re
    bad = 0
    for l in out:
        m = re.match(r"(\S+): (\d+)$", l)
        if m and m[1] in _keys: bad += int(m[2])
    print("RESULT", "PASS" if bad == 0 else "FAIL", "violations", bad)
