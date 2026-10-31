#!/usr/bin/env python3
r"""REFEREE-2 successor 24 (Opus 5.5, D15): own check of P-N5-ODD (docs/si/P-N5-ODD-box57.md @ l-si 0afc0d70a, sha1 03eec41d).
State construction: my R2-N5-LATEP/latep_check.py (my N5 loop); start files as in R2-N5-WRUN/wrun_check.py. The lane's src54/fseg55/
grow56 tools are NOT imported. Checks (each must be 0):
  whole run, every transition k:
    OLD    OLD-PLAY: a Xi-change at x has an Even switch on x's (sigma_k, sbar_k)-play
    STEP   ODD-STEP: Odd o, x = sbar_k(o), Xi(x) unchanged => Xi(o) unchanged       (STEP_case2 = configurations with o on x's new play)
    RELAY  ODD-RELAY: Odd o with a Xi-change; every u on x's old play whose prefix pi has no Even switch / Odd sbar change: Xi(u) changes
  per W-run F:
    ROOT   SRC-ROOT: the u_k chain from every Odd o_0 with a Xi-change ends at (a) an Odd prefix event or (b) an Even C-node, all with Xi-changes
    FLEX   FUEL-LEX on consecutive fuel re-routes of each pair (ASC / EQHI / REP);  FCNT  N <= n(n + 2)(HC + n)
  Counters: ROOT_a, ROOT_b, FUEL, ASC, EQHI, REP20, REP00, REP00_with_higher (a (0,0)=(0,0) boundary with a higher-key change inside:
  the FUEL-COUNT classification point), MID_EQKEY (a key-(1,r) change strictly between two (1,r) re-routes: the FUEL-LEX proof point).
Usage: odd_check.py files list.txt [runs [prefix]] | random N nmin nmax seed [starts]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-LATEP")); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-WRUN"))
import latep_check as L
import wrun_check as WR
CAP = {}


def play(nx, v):
    seen = {}; p = []; x = v
    while x not in seen: seen[x] = len(p); p.append(x); x = nx[x]
    return p


def key(x0, x1):
    if x0[0] != x1[0]: return (2, 0)
    d = x0[1] ^ x1[1]
    if d: return (1, d.bit_length() - 1)
    return (0, 0)


def whole(g, info, st, name):
    n = g.n
    for k in range(len(info) - 1):
        A, B = info[k], info[k + 1]
        sw = {y for y in range(n) if g.owner[y] == 0 and A["sg"][y] != B["sg"][y]}
        ch = {x for x in range(n) if A["xi"][x] != B["xi"][x]}
        oc = {z for z in range(n) if g.owner[z] == 1 and A["sbar"][z] != B["sbar"][z]}
        for x in ch:
            st.inc("OLD_checks")
            if not any(y in sw for y in play(A["nxX"], x)): st.bad("OLD", f"{name}@{k} x={x}")
        for o in range(n):
            if g.owner[o] != 1: continue
            x = A["sbar"][o]
            if o in play(B["nxX"], x): st.inc("STEP_case2")
            st.inc("STEP_checks")
            if x not in ch and o in ch: st.bad("STEP", f"{name}@{k} o={o}")
            if o in ch:
                p = play(A["nxX"], x)
                for i, u in enumerate(p):
                    if i > 0 and (p[i - 1] in sw or p[i - 1] in oc): break
                    st.inc("RELAY_checks")
                    if u not in ch: st.bad("RELAY", f"{name}@{k} o={o} u={u}"); break


def wrun(g, E, info, a, b, st, name, *rest):
    CAP["info"] = info
    n = g.n
    if b == a: return
    C = {v for v in range(n) if info[a]["lamW"][v] == v}
    for k in range(a, b):
        A, B = info[k], info[k + 1]
        sw = {y for y in range(n) if g.owner[y] == 0 and A["sg"][y] != B["sg"][y]}
        oc = {z for z in range(n) if g.owner[z] == 1 and A["sbar"][z] != B["sbar"][z]}
        ch = {x for x in range(n) if A["xi"][x] != B["xi"][x]}
        DC_ = A["D"] | C
        for o0 in ch:
            if g.owner[o0] != 1: continue
            o = o0; seen = set(); st.inc("ROOT_checks")
            while True:
                if o not in ch: st.bad("ROOT", f"{name}@{k} o0={o0} o={o} no change"); break
                if g.owner[o] == 0:
                    if o in C: st.inc("ROOT_b")
                    else: st.bad("ROOT", f"{name}@{k} o0={o0} ends at Even {o} not in C")
                    break
                if o in seen: st.bad("ROOT", f"{name}@{k} o0={o0} loop"); break
                seen.add(o)
                p = play(A["nxX"], A["sbar"][o]); fs = []
                for u in p:
                    if u in DC_: break
                    fs.append(u)
                else: st.bad("ROOT", f"{name}@{k} no u_k"); break
                u = p[len(fs)]
                if any(z in sw or z in oc for z in fs): st.inc("ROOT_a"); break
                o = u
    # fuel re-routes
    fr = {}
    for k in range(a + 1, b):
        P0, A, B = info[k - 1], info[k], info[k + 1]
        for y in range(n):
            if g.owner[y] != 0 or A["sg"][y] == B["sg"][y]: continue
            z = B["sg"][y]
            if z == P0["sg"][y] or (y, z) in P0["Is"]: continue
            if P0["xi"][z] == A["xi"][z]: continue
            fr.setdefault((y, z), []).append((k, key(P0["xi"][z], A["xi"][z])))
    for (y, z), lst in fr.items():
        st.inc("FUEL", len(lst))
        chz = [(u, key(info[u]["xi"][z], info[u + 1]["xi"][z])) for u in range(a, b) if info[u]["xi"][z] != info[u + 1]["xi"][z]]
        runs = 1
        for (k1, ka), (k2, kb) in zip(lst, lst[1:]):
            t1, t2 = k1 - 1, k2 - 1
            if kb < ka: continue
            runs += 1
            mid = [kk for (u, kk) in chz if t1 < u < t2]
            if kb > ka: st.inc("ASC")
            elif any(kk > ka for kk in mid):
                st.inc("EQHI")
                if ka == (0, 0): st.inc("REP00_with_higher")
            elif ka in ((2, 0), (0, 0)): st.inc("REP20" if ka == (2, 0) else "REP00")
            else: st.bad("FLEX", f"{name} pair {(y, z)} k {k1},{k2} key {ka}")
            if ka[0] == 1 and kb == ka and any(kk == ka for kk in mid): st.inc("MID_EQKEY")
        HC = 0
        for (u, kk) in chz:
            last = [kx for (kr, kx) in lst if kr <= u]
            if last and kk > last[-1]: HC += 1
        N = len(lst)
        if N > n * (n + 2) * (HC + n): st.bad("FCNT", f"{name} pair {(y, z)} N {N} HC {HC}")


_orig = WR._orig_run_game
def run_game(g, s, t, st, name):
    o = L.wrun; L.wrun = wrun; CAP.clear()
    try: _orig(g, s, t, st, name)
    finally: L.wrun = o
    if CAP.get("info"): whole(g, CAP["info"], st, name)
L.run_game = run_game; L.read_start = WR.read_start
KEYS = ("OLD", "STEP", "RELAY", "ROOT", "FLEX", "FCNT", "XIPLAY", "XW", "XIMON")
if __name__ == "__main__":
    import io, contextlib, re
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf): L.main()
    bad = 0
    for l in buf.getvalue().splitlines():
        if not l.startswith("RESULT"): print(l)
        m = re.match(r"(\S+): (\d+)$", l)
        if m and m[1] in KEYS: bad += int(m[2])
    print("RESULT", "PASS" if bad == 0 else "FAIL", "violations", bad)
