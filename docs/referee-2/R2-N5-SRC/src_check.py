#!/usr/bin/env python3
r"""REFEREE-2 successor 24 (Opus 5.5, D15): own check of P-N5-SRC (docs/red/P-N5-SRC.md @ l-red 0521fb82, sha1 3caae56e).
State construction: my R2-N5-LATEP/latep_check.py (my N5 loop; W-runs as in R89); start files as in R2-N5-WRUN/wrun_check.py. The lane's
experiments/red/xcn/*.py are NOT imported. Definitions are written from the packet text (§1): S_k := D_k u D_(k+1) u C, source event, source
block, C-only transition, m_C.
Checks per W-run F (each must be 0):
  PCS    PLAY-CAUSE^S: at a source-free transition, every x with a Xi-change has a switched Even y not in C on x's W_(k+1)-path before c
  S / X  (S_j) for switched Even y not in C, (X_j) for every x, in every source block
  ORD    once a block transition is C-only, every later one of the block is C-only (TAIL (T1) along the block)
  T0     at a source-free C-only transition: Xi_(k+1) = Xi_k, W_(k+1) = W_k, H_(k+1)(v) subset H_k(v) for every Even v
  T1     after a source-free C-only transition k, if k + 1 -> k + 2 is in F: sigma_(k+2) = sigma_(k+1) off C, W_(k+2) = W_(k+1)
  NRM / TL / BLK  normal part <= n - 1, tail <= m_C, block <= n - 1 + m_C;  SC  SRC-COUNT |F| <= E^S + (E^S + 1)(n - 1 + m_C)
  HXS    E^S_F <= sum_v HXS_F(v)
  OS     Lemma ONE-STEP (my repair of [SET] §5 Case 2 / 2b, see the report): at every transition t -> t + 1 of F, Even y not in C, z in H_t(y)
         with lambda_W(z) = lambda_W(y) and z's (sigma_(t+1), tau)-path to c avoiding y: y (+) W_(t+1)(z) <= W_(t+1)(y)
Counters: OS_cyc = OS instances with y on c's (sigma_(t+1), tau)-cycle; OS_newtop = those whose rho-play cycle top is not c (the step
«its play from y is y, then z's path» is then false); OS_newtop_even (must be 0 by ARENA-MAX); OS_newtop_case2 = those where y
switches to z at the next transition (the shape of [SET] §5 Case 2, b := z); one NEWTOP line per instance; case split as in R2-N5-SETTLE.
Usage: src_check.py files list.txt [runs [prefix]] | random N nmin nmax seed [starts]"""
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


def cycle_of(nx, c):
    cyc = [c]; v = nx[c]
    while v != c:
        cyc.append(v); v = nx[v]
        if len(cyc) > len(nx): return None
    return cyc


def wrun(g, E, info, a, b, st, name, Even, nE, mE, dE):
    n = g.n; K = E.key; T = b - a; pval = L.pval
    st.inc("WRUNS"); st.inc("WRUN_transitions", T)
    C = {v for v in range(n) if info[a]["lamW"][v] == v}
    tau = info[a]["tu"]
    mC = sum(len(set(g.succ[c])) - 1 for c in C if g.owner[c] == 0)
    nxW = [[info[t]["sg"][v] if g.owner[v] == 0 else tau[v] for v in range(n)] for t in range(a, b + 1)]
    def ell(t, x): return info[t]["W"][x][2]
    def H(t, y): return {info[t]["sg"][y]} | {z for (yy, z) in info[t]["Is"] if yy == y}
    src = []; HXS = {}; conly = []
    for k in range(a, b):
        A, B = info[k], info[k + 1]
        S = A["D"] | B["D"] | C
        ch = [v for v in S if A["xi"][v] != B["xi"][v]]
        for v in ch: HXS[v] = HXS.get(v, 0) + 1
        src.append(bool(ch))
        sw = [y for y in range(n) if g.owner[y] == 0 and A["sg"][y] != B["sg"][y]]
        conly.append(all(y in C for y in sw))
        # Lemma ONE-STEP at every transition of F
        for y in range(n):
            if g.owner[y] != 0 or y in C: continue
            c = B["lamW"][y]; nx = nxW[k + 1 - a]
            cyc = cycle_of(nx, c); oncyc = cyc is not None and y in cyc
            for z in H(k, y):
                if B["lamW"][z] != c: continue
                p = wpath(nx, z, C)
                if p is None or y in p: continue
                st.inc("OS_checks")
                lhs = E.extend(y, B["W"][z])
                if K(lhs) > K(B["W"][y]): st.bad("OS", f"{name}@{k} y={y} z={z}")
                if oncyc:
                    st.inc("OS_cyc")
                    rho = list(nx); rho[y] = z; v = pval(E, rho, y)
                    if v[0] != c:
                        st.inc("OS_newtop")
                        if g.prio[v[0]] % 2 == 0: st.bad("OS_newtop_even", f"{name}@{k} y={y} z={z}")
                        elif z != B["sg"][y]: st.inc("OS_newtop_nonchoice")
                        nxt = info[k + 2]["sg"][y] if k + 2 <= b else None
                        if nxt == z: st.inc("OS_newtop_case2")   # y switches to z at k+1 -> k+2: the [SET] §5 Case 2 shape
                        print("NEWTOP", name, "t", k, "y", y, "z", z, "c", c, "top", v[0], "sigma_(t+1)(y)", B["sg"][y], "sigma_(t+2)(y)", nxt,
                              "rho", v, "y+W(z)", lhs, "W(y)", B["W"][y], flush=True)
    ES = sum(src)
    if ES > sum(HXS.values()): st.bad("HXS", name)
    if T > ES + (ES + 1) * (n - 1 + mC): st.bad("SC", f"{name} |F| {T} ES {ES} mC {mC}")
    mxt(st, "max_ES", (ES, name))
    k = a
    while k < b:
        if src[k - a]: k += 1; continue
        k0 = k
        while k < b and not src[k - a]: k += 1
        k1 = k; st.inc("BLOCKS"); mxt(st, "max_block", (k1 - k0, name))
        if k1 - k0 > n - 1 + mC: st.bad("BLK", f"{name} [{k0},{k1}]")
        seen_c = False; nrm = 0; tl = 0
        for kk in range(k0, k1):
            j = kk - k0; A, B = info[kk], info[kk + 1]
            if conly[kk - a]:
                seen_c = True; tl += 1
                if A["xi"] != B["xi"] or A["W"] != B["W"]: st.bad("T0", f"{name}@{kk} Xi/W")
                for v in range(n):
                    if g.owner[v] == 0 and not H(kk + 1, v) <= H(kk, v): st.bad("T0", f"{name}@{kk} H v={v}")
                if kk + 1 < b:
                    C2 = info[kk + 2]
                    if any(C2["sg"][v] != B["sg"][v] for v in range(n) if g.owner[v] == 0 and v not in C): st.bad("T1", f"{name}@{kk}")
                    if C2["W"] != B["W"]: st.bad("T1", f"{name}@{kk} W")
            else:
                nrm += 1
                if seen_c: st.bad("ORD", f"{name}@{kk}")
            sw = [y for y in range(n) if g.owner[y] == 0 and A["sg"][y] != B["sg"][y]]
            for y in sw:
                if y not in C and ell(kk + 1, y) < j + 1: st.bad("S", f"{name}@{kk} j={j} y={y}")
            for x in range(n):
                if A["xi"][x] == B["xi"][x]: continue
                if ell(kk + 1, x) < j + 1: st.bad("X", f"{name}@{kk} j={j} x={x}")
                p = wpath(nxW[kk + 1 - a], x, C)
                if not p or not any(v in sw and v not in C for v in p[:-1]): st.bad("PCS", f"{name}@{kk} x={x}")
            if j >= 1:
                for y in sw:
                    if y in C: st.inc("CN_in_block"); continue
                    a_, b_ = A["sg"][y], B["sg"][y]
                    if b_ not in H(kk - 1, y): st.inc("CASE1"); continue
                    if A["W"][b_] != B["W"][b_]: st.inc("CASE_WR"); continue
                    if E.extend(y, B["W"][a_]) == B["W"][y]: st.inc("CASE2a"); continue
                    p = wpath(nxW[kk + 1 - a], a_, C)
                    st.inc("CASE2c" if p and y in p else "CASE2b")
        if nrm > n - 1: st.bad("NRM", f"{name} [{k0},{k1}]")
        if tl > mC: st.bad("TL", f"{name} [{k0},{k1}]")
        mxt(st, "max_tail", (tl, name))


_orig = WR._orig_run_game
def run_game(g, s, t, st, name):
    orig = L.wrun
    L.wrun = wrun
    try: _orig(g, s, t, st, name)
    finally: L.wrun = orig
L.run_game = run_game
L.read_start = WR.read_start
KEYS = ("PCS", "S", "X", "ORD", "T0", "T1", "NRM", "TL", "BLK", "SC", "HXS", "OS", "OS_newtop_even", "XIPLAY", "XW", "XIMON")
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
