#!/usr/bin/env python3
r"""REFEREE-2 successor 24 (Opus 5.5, D15): own check of P-N5-STAIR (docs/new/P-N5-STAIR-box112.md @ l-new 9a58765f, sha1 31771241).
State construction: my R2-N5-LATEP/latep_check.py (my N5 loop; W-runs as in R89); start files as in R2-N5-WRUN/wrun_check.py. The lane's
new/box107-111/*.py are NOT imported. CS = RESULTS R93's coordinate sequence; beta = the packet's §5 encoding (3n + 1 bits), both from
the packet text. Checks per W-run F = [a, b] (each must be 0):
  LEXK   CS order = engine order (E.key) on every compared pair;  BITK  beta order = engine order on W(v) pairs of one vertex in F
  FROZ   BW_k, AF_k non-decreasing on F; LS_k non-decreasing on F (end = b)
  NF1    every W-constant transition is in N_F;  BWACC  |F| <= (M + 1) n(n + 2) + M N_F
  FG     FIRST-GOOD;  BALT  GOOD(v, b) <= 1 + BAD(v, b);  RR  RESET-RED both directions
  COPY   beta(W_j(v)) = pi_v(beta(W_j(z))) for j = k, k + 1, every v not in C with the same W-successor z at k and k + 1, when W(v) or W(z) moves
  ROOT   RESET-ROOT: every reset (v, bit) at k has a first switched Even y before c on v's W_(k+1)-path, with a reset at k; TD <= n * sum
  DCOPY  DESC-COPY;  ASC  q_(j+1) != q_j and WCH(v) <= (3n + 1)(1 + DESC(v));  STAIR  WCT <= n(3n + 1) + (3n + 1) DESC_F
Counters: BWRISE, RESET_T (transitions with a reset), WCT, SWCH (sum WCH), DESC, T4, longest consecutive T4 run.
Usage: stair_check.py files list.txt [runs [prefix]] | random N nmin nmax seed [starts]   (DUMP=1: one line per W-run)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-LATEP")); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-WRUN"))
import latep_check as L
import wrun_check as WR
DUMP = os.environ.get("DUMP")


def mxt(st, k, v):
    if k not in st.mx or v > st.mx[k]: st.mx[k] = v


def lcp(x, y):
    i = 0
    while i < len(x) and x[i] == y[i]: i += 1
    return i


def wrun(g, E, info, a, b, st, name, *rest):
    n = g.n; K = E.key; T = b - a; st.inc("WRUNS"); st.inc("WRUN_transitions", T)
    if T == 0: return
    C = {v for v in range(n) if info[a]["lamW"][v] == v}; tau = info[a]["tu"]
    csc = {}
    def CS(x):
        r = csc.get(x)
        if r is None:
            c, m, l = x
            r = (E.rew[c],) + tuple((1 if E.rankpar[q] == 0 else -1) if m >> q & 1 else 0 for q in range(n - 1, -1, -1)) + \
                (l if E.par[c] == 1 else -l,)
            csc[x] = r
        return r
    def beta(x):
        c, m, l = x
        rb = tuple(((m >> q & 1) if E.rankpar[q] == 0 else 1 - (m >> q & 1)) for q in range(n - 1, -1, -1))
        sl = l if E.par[c] == 1 else -l
        return rb + tuple(1 if sl >= j else 0 for j in range(-n, n + 1))
    def lexchk(x, y):
        st.inc("LEXK_checks")
        if (CS(x) < CS(y)) != (K(x) < K(y)) or (CS(x) == CS(y)) != (x == y): st.bad("LEXK", f"{name} {x} {y}")
    Wq = info[b]["W"]; Xe = info[b]["xi"]
    BW = []; AF = []; LS = []; A = []
    for k in range(a, b + 1):
        I = info[k]
        for v in range(n): lexchk(I["W"][v], Wq[v]); lexchk(I["xi"][v], Wq[v])
        BW.append(sum(lcp(CS(I["W"][v]), CS(Wq[v])) for v in range(n)))
        AF.append(sum(lcp(CS(I["xi"][v]), CS(Wq[v])) for v in range(n)))
        LS.append(sum(lcp(CS(I["xi"][v]), CS(Xe[v])) for v in range(n)))
        A.append(sum(lcp(CS(I["xi"][v]), CS(I["W"][v])) for v in range(n)))
    for i in range(T):
        if BW[i + 1] < BW[i] or AF[i + 1] < AF[i] or LS[i + 1] < LS[i]: st.bad("FROZ", f"{name}@{a + i}")
    M = n * (n + 2) + 1; NF = 0; t4run = 0
    for i in range(T):
        wc = info[a + i]["W"] == info[a + i + 1]["W"]
        inN = BW[i + 1] == BW[i] and A[i + 1] >= A[i]
        if wc and not inN: st.bad("NF1", f"{name}@{a + i}")
        NF += inN
        if BW[i + 1] > BW[i]: st.inc("BWRISE")
        if inN and not wc: st.inc("T4"); t4run += 1; mxt(st, "max_T4_run", (t4run, name))
        else: t4run = 0
    if T > (M + 1) * n * (n + 2) + M * NF: st.bad("BWACC", name)
    # bits and changes
    nb = 3 * n + 1; good = {}; bad = {}; pos = {v: [] for v in range(n)}; when = {v: [] for v in range(n)}
    WCT = 0; TD = 0; TDroot = 0
    for k in range(a, b):
        A0, B0 = info[k], info[k + 1]
        ch = [v for v in range(n) if A0["W"][v] != B0["W"][v]]
        if ch: WCT += 1
        sw = {y for y in range(n) if g.owner[y] == 0 and A0["sg"][y] != B0["sg"][y]}
        bx = {}
        def bb(v, j):
            if (v, j) not in bx: bx[(v, j)] = beta(info[j]["W"][v])
            return bx[(v, j)]
        resets_at = {}
        for v in ch:
            x0, x1 = A0["W"][v], B0["W"][v]
            st.inc("BITK_checks")
            if x0[0] != x1[0] or not ((bb(v, k) < bb(v, k + 1)) == (K(x0) < K(x1))): st.bad("BITK", f"{name}@{k} v={v}")
            f = [i for i in range(nb) if bb(v, k)[i] != bb(v, k + 1)[i]]
            if not f or bb(v, k)[f[0]] != 0: st.bad("FG", f"{name}@{k} v={v}")
            for i in f:
                if bb(v, k + 1)[i] == 1: good[(v, i)] = good.get((v, i), 0) + 1
                else: bad[(v, i)] = bad.get((v, i), 0) + 1; resets_at.setdefault(v, []).append(i)
            pos[v].append(f[0] if f else -1); when[v].append(k)
        if resets_at: st.inc("RESET_T")
        # RESET-ROOT
        nxt = [B0["sg"][u] if g.owner[u] == 0 else tau[u] for u in range(n)]
        for v, rl in resets_at.items():
            TD += len(rl); u = v; y = None; seen = 0
            while u not in C and seen <= n:
                if g.owner[u] == 0 and u in sw: y = u; break
                u = nxt[u]; seen += 1
            st.inc("ROOT_checks")
            if y is None: st.bad("ROOT", f"{name}@{k} v={v} no switched y"); continue
            yb0, yb1 = beta(A0["W"][y]), beta(B0["W"][y])
            if not any(yb0[i] == 1 and yb1[i] == 0 for i in range(nb)): st.bad("ROOT", f"{name}@{k} v={v} y={y} no reset")
        TDroot += sum(sum(1 for i in range(nb) if beta(A0["W"][y])[i] == 1 and beta(B0["W"][y])[i] == 0) for y in sw if A0["W"][y] != B0["W"][y])
        # COPY
        nk = [A0["sg"][u] if g.owner[u] == 0 else tau[u] for u in range(n)]
        for v in range(n):
            if v in C or nk[v] != nxt[v]: continue
            z = nk[v]
            if A0["W"][v] == B0["W"][v] and A0["W"][z] == B0["W"][z]: continue
            st.inc("COPY_checks"); c = A0["lamW"][v]; rv = n - 1 - E.rank[v]; sh = 1 if E.par[c] == 1 else -1
            for j in (k, k + 1):
                bv, bz = bb(v, j), bb(z, j)
                ok = all(bv[i] == bz[i] for i in range(n) if i != rv)
                ok = ok and bv[rv] == ((1 if E.rank[v] > E.rank[c] else 0) if E.rankpar[E.rank[v]] == 0 else (0 if E.rank[v] > E.rank[c] else 1))
                for t in range(2 * n + 1):          # v's threshold bit t (j = t - n): [sl_z >= j - sh]
                    s = t - sh
                    exp = bz[n + s] if 0 <= s <= 2 * n else (1 if s < 0 else 0)
                    if bv[n + t] != exp: ok = False; break
                if not ok: st.bad("COPY", f"{name}@{j} v={v} z={z}"); break
    if TD > n * TDroot: st.bad("ROOT", f"{name} TD {TD} > n*{TDroot}")
    # BIT-ALT, RESET-RED
    for key, gd in good.items():
        if gd > 1 + bad.get(key, 0): st.bad("BALT", f"{name} {key}")
    SW = sum(len(pos[v]) for v in range(n))
    if not (WCT <= SW <= n * nb + TD): st.bad("RR", f"{name} WCT {WCT} SW {SW} TD {TD}")
    if TD > nb * n * WCT: st.bad("RR", f"{name} conv")
    # ASC-RUN, DESC-COPY, STAIR
    D = {}
    for v in range(n):
        q = pos[v]; d = 0
        for j in range(1, len(q)):
            if q[j] == q[j - 1]: st.bad("ASC", f"{name} v={v} same position")
            if q[j] > q[j - 1]:
                d += 1
                k1, k0 = when[v][j], when[v][j - 1]
                if v not in C and not any(g.owner[v] == 0 and info[t]["sg"][v] != info[t + 1]["sg"][v] for t in range(k0, k1 + 1)):
                    st.inc("DCOPY_checks"); z = info[k1]["sg"][v] if g.owner[v] == 0 else tau[v]
                    zw = when[z]
                    if k1 not in zw or zw.index(k1) == 0 or pos[z][zw.index(k1)] <= pos[z][zw.index(k1) - 1]: st.bad("DCOPY", f"{name} v={v} z={z} k={k1}")
        D[v] = d
        if len(q) > nb * (1 + d): st.bad("ASC", f"{name} v={v} WCH {len(q)} DESC {d}")
    DF = sum(D.values())
    if WCT > n * nb + nb * DF: st.bad("STAIR", f"{name} WCT {WCT} DESC {DF}")
    st.inc("WCT", WCT); st.inc("SWCH", SW); st.inc("DESC", DF); st.inc("TD", TD)
    if DUMP: print("WRUN", name, a, b, "n", n, "WT", T, "WCT", WCT, "WCH", SW, "DESC", DF, "TD", TD, "NF", NF, flush=True)


_orig = WR._orig_run_game
def run_game(g, s, t, st, name):
    o = L.wrun; L.wrun = wrun
    try: _orig(g, s, t, st, name)
    finally: L.wrun = o
L.run_game = run_game; L.read_start = WR.read_start
KEYS = ("LEXK", "BITK", "FROZ", "NF1", "BWACC", "FG", "BALT", "RR", "COPY", "ROOT", "DCOPY", "ASC", "STAIR", "XIPLAY", "XW", "XIMON")
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
