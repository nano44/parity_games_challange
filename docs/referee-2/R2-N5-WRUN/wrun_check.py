#!/usr/bin/env python3
r"""REFEREE-2 successor 23 (Opus 5.5, D15): own check of P-N5-WRUN (docs/new/P-N5-WRUN-box92.md @ l-new 7668bc9b, sha1 fae68aa0).
State construction: my R2-N5-LATEP/latep_check.py (my N5 loop R2-N5-DUAL Runner; W-runs cut at S4c fallbacks, tau-changes, lambda_W-changes;
info[t] = sg, tu, xi, Is, sbar, nxX, W, lam, lamW). The lane's experiments/new/box84-box92 scripts are NOT imported. Definitions from the
packet text. Start files: unlisted vertices take the best-reward start; a forced vertex takes its only edge (comp54_n80 repair).
Checks per W-run F (each must be 0):
  STEP   every transition of F switches an Even vertex (Fact STEP-SW)
  SWR    ENT_F(v, c) <= 1 + RISE_F(c) per Even edge ([R86] SW-RETURN, read on F)
  XIR    |F| <= m_E + sum_c d_E(c) XiCH_F(c) (Theorem XI-RUN) and the same on every W-constant interval (INT-XCH0)
  RETX   RET_F(X, g) <= XiCH_F(g), and Xi_k(g) |> Xi_s(g) for every return k -> k+1 with last leave s (RET-XiRISE)
  E0B    E0_F(X, g) <= n (E0-BOUND);  TRI  |F| <= m_E + sum RET <= m_E(n+1) + sum REG + sum FREE (TRIPLE-RED)
  WAIT   WAIT-CYCLE': after a REG self-routed block at t1 (route pi, pattern), no later state of the RUN has sigma(X) = g and the pattern
         (sampled: up to WAITS blocks per run)
  GDEV   GAP-DEV at every blocked (y, z, q): Xi_q(z) <| W_q(z) and an Odd o on z's (sigma_q, sigmabar_q)-play with sigmabar_q(o) != tau(o)
  PCH    XiCH_F(z) <= (n-1) + PCH + (n + PCH)(n-1);  RST  R*_F <= sum_{Even edges (y,z)} XiCH_F(z) (RSTAR-PCH)
  PRE    PREFIX-MON k = 1, 2, 3 (non-decreasing while lambda(Xi(v)) fixed; strict at changes of depth < k); LEV  LEVEL-RED bound
  NODEV  if Xi = W on all of F: R*_F = 0, WCH_F <= n - 1, |F| <= (n-1) + 4n^2(n-1)
  BIPR   |F| <= SB_F + (SB_F + 1)(n - 1)(R° + 1) + FL_F (BIP-RED; [SUB] on frozen stretches checked as SUBF)
  EXT    Fact EXT on the values it is applied to in REL2-WRISE (computed on states where (A1), (A2) hold): reflection holds
Controls: X_EXT_GLOBAL counts value pairs met (x, x') with y in P(x) xor P(x') where ext(y, .) is NOT injective (Fact EXT as stated
globally fails there); X_REG_blocks, X_E0, X_FREE; X_DEEP (changes of depth >= k).
Usage: wrun_check.py files list.txt [runs [prefix]] | random N nmin nmax seed [starts]   (PINS=1 prints per-W-run |F|, max XiCH, bound)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-LATEP"))
import latep_check as L
WAITS = int(os.environ.get("WAITS", "300")); PINS = os.environ.get("PINS") == "1"
_rng = random.Random(9292)
RUNSTATE = {}


def read_start(g, path):
    E, Ed = L.Engine(g), L.Engine(L.dual(g))
    s, t = list(E.initial("best")), list(Ed.initial("best"))
    for l2 in open(path):
        ps = l2.split()
        if ps and ps[0] in ("SIGMA0", "TAU0"):
            for kv in ps[1:]:
                v, w = map(int, kv.split(":")); (s if ps[0] == "SIGMA0" else t)[v] = w
    for v in range(g.n):
        if len(set(g.succ[v])) == 1: (s if g.owner[v] == 0 else t)[v] = g.succ[v][0]
    return s, t, all((s if g.owner[v] == 0 else t)[v] in g.succ[v] for v in range(g.n))


def play_until(nx, start, X):
    """route from start to X under nx: list of vertices before X, or None if X is not reached before a repeat"""
    seen, path, x = set(), [], start
    while x != X:
        if x in seen: return None
        seen.add(x); path.append(x); x = nx[x]
    return path


def cycle_of(nx, v):
    seen, path, x = {}, [], v
    while x not in seen: seen[x] = len(path); path.append(x); x = nx[x]
    return set(path[seen[x]:])


def mxt(st, k, v):
    if k not in st.mx or v > st.mx[k]: st.mx[k] = v


def wrun(g, E, info, a, b, st, name, Even, nE, mE, dE):
    n = g.n; K = E.key; rank = E.rank; T = b - a
    st.inc("WRUNS"); st.inc("WRUN_transitions", T)
    edges = [(v, c) for v in Even for c in sorted(set(g.succ[v]))]
    XiCH = [sum(info[t + 1]["xi"][c] != info[t]["xi"][c] for t in range(a, b)) for c in range(n)]
    bound = mE + sum(dE[c] * XiCH[c] for c in range(n))
    if PINS and T: print("PIN", name, f"F[{a},{b}]", "|F|", T, "maxXiCH", max(XiCH), "bound", bound, flush=True)
    mxt(st, "max_F", (T, name)); mxt(st, "max_XiCH", (max(XiCH) if n else 0, name))
    if T > bound: st.bad("XIR", f"{name} F[{a},{b}] {T} > {bound}")
    if T: mxt(st, "max_ratio_F_bound_x1000", (int(1000 * T / bound), name))
    sw = {t: [v for v in Even if info[t + 1]["sg"][v] != info[t]["sg"][v]] for t in range(a, b)}
    for t in range(a, b):
        if not sw[t]: st.bad("STEP", f"{name}@{t}")
    def blocked(t, y, z):
        I = info[t]; r = I["sg"][y]
        return z != r and (y, z) not in I["Is"] and K(I["W"][z]) > K(I["W"][r])
    # SW-RETURN, returns, RET-XiRISE
    RET = {}; ENT = {}
    lastleave = {}; held = {e: (info[a]["sg"][e[0]] == e[1]) for e in edges}
    retlist = []
    for t in range(a, b):
        for v in sw[t]:
            old, new = info[t]["sg"][v], info[t + 1]["sg"][v]
            lastleave[(v, old)] = t; held[(v, old)] = True if held.get((v, old)) else held.get((v, old), False)
            ENT[(v, new)] = ENT.get((v, new), 0) + 1
            if held.get((v, new)):
                RET[(v, new)] = RET.get((v, new), 0) + 1; s = lastleave[(v, new)]; retlist.append((v, new, s, t))
                if not K(info[t]["xi"][new]) > K(info[s]["xi"][new]): st.bad("RETX", f"{name} ({v},{new}) s={s} k={t}")
            held[(v, new)] = True
    for (v, c), k in ENT.items():
        if k > 1 + XiCH[c]: st.bad("SWR", f"{name} ({v},{c})")
    for (v, c), r in RET.items():
        if r > XiCH[c]: st.bad("RETX", f"{name} ({v},{c}) RET {r} > XiCH {XiCH[c]}")
    if T > mE + sum(RET.values()): st.bad("TRI", f"{name} F[{a},{b}] |F| > m_E + sum RET")
    # self-routed blocks per state (only for edges that have a return window covering the state, plus a sample for WAIT)
    blocks = {}
    def block(t, X, g_):
        key = (t, X, g_)
        if key in blocks: return blocks[key]
        I = info[t]; res = None
        if g_ != I["sg"][X] and (X, g_) not in I["Is"]:
            pi = play_until(I["nxX"], g_, X)
            if pi is not None:
                Zs = cycle_of(I["nxX"], X)
                if not (X in Zs and any(u in Zs for u in pi)):
                    e0 = I["lam"][X] == X and all(rank[u] < rank[X] for u in pi)
                    res = ("E0" if e0 else "REG", tuple(pi))
        blocks[key] = res; return res
    REG = {}; E0 = {}; FREE = {}
    for (X, g_, s, k) in retlist:
        cls = [block(t, X, g_) for t in range(s + 1, k + 1)]
        kinds = {c[0] for c in cls if c}
        e = (X, g_)
        if "REG" in kinds: REG[e] = REG.get(e, 0) + 1
        elif "E0" in kinds: E0[e] = E0.get(e, 0) + 1
        else: FREE[e] = FREE.get(e, 0) + 1
    st.inc("X_REG", sum(REG.values())); st.inc("X_E0", sum(E0.values())); st.inc("X_FREE", sum(FREE.values()))
    if any(c > n for c in E0.values()): st.bad("E0B", f"{name}")
    if T > mE * (n + 1) + sum(REG.values()) + sum(FREE.values()): st.bad("TRI", f"{name} F[{a},{b}]")
    # WAIT-CYCLE' on sampled REG blocks (all states of F, all Even edges), checked against later states of the whole run
    cand = [(t, X, g_) for t in range(a, b + 1) for (X, g_) in edges]
    _rng.shuffle(cand); nW = 0
    allst = RUNSTATE["info"]
    for (t1, X, g_) in cand:
        if nW >= WAITS: break
        bl = block(t1, X, g_)
        if not bl or bl[0] != "REG": continue
        nW += 1; st.inc("X_REG_blocks_checked")
        pat = [(u, info[t1]["sg"][u]) for u in bl[1] if g.owner[u] == 0]
        for t in range(t1 + 1, len(allst)):
            sg = allst[t]["sg"]
            if sg[X] == g_ and all(sg[u] == w for u, w in pat): st.bad("WAIT", f"{name} block ({X},{g_})@{t1} pattern back at {t}"); break
    # GAP-DEV and R*_F
    Rstar = 0; LATE = {}
    for q in range(a, b + 1):
        I = info[q]
        for (y, z) in edges:
            if blocked(q, y, z):
                st.inc("X_blocked_records")
                if not K(I["xi"][z]) < K(I["W"][z]): st.bad("GDEV", f"{name}@{q} ({y},{z}) Xi not < W")
                x, seen, dev = z, set(), False
                while x not in seen:
                    seen.add(x)
                    if g.owner[x] == 1 and I["sbar"][x] != I["tu"][x]: dev = True
                    x = I["nxX"][x]
                if not dev: st.bad("GDEV", f"{name}@{q} ({y},{z}) no deviation")
    for u in range(a, b):
        late = False
        for y in sw[u]:
            z = info[u + 1]["sg"][y]
            if any(blocked(t, y, z) for t in range(a, u)): late = True; LATE[(y, z)] = LATE.get((y, z), 0) + 1
        Rstar += late
    if Rstar > sum(XiCH[z] for (y, z) in edges): st.bad("RST", f"{name} R* {Rstar}")
    for (y, z), c in LATE.items():
        if c > XiCH[z]: st.bad("RST", f"{name} LATE ({y},{z}) {c} > XiCH {XiCH[z]}")
    mxt(st, "max_Rstar", (Rstar, name))
    # PCH, PREFIX-MON, LEVEL-RED
    def terms(m):
        out = []
        for r in range(n - 1, -1, -1):
            if m >> r & 1: out.append((2, r) if E.rankpar[r] == 0 else (0, -r))
        return out
    def pre(m, k): tl = terms(m)[:k]; return tuple(tl + [(1, 0)] * (k - len(tl)))
    for v in range(n):
        PCH = sum(1 for t in range(a, b) if info[t + 1]["xi"][v][0] == info[t]["xi"][v][0] and info[t + 1]["xi"][v][1] != info[t]["xi"][v][1])
        if XiCH[v] > (n - 1) + PCH + (n + PCH) * (n - 1): st.bad("PCH", f"{name} v={v}")
        for k in (1, 2, 3):
            deep = 0
            for t in range(a, b):
                x, y = info[t]["xi"][v], info[t + 1]["xi"][v]
                if x[0] != y[0] or x[1] == y[1]: continue
                r = (x[1] ^ y[1]).bit_length() - 1; d = bin(x[1] >> (r + 1)).count("1")
                p0, p1 = pre(x[1], k), pre(y[1], k)
                if p1 < p0 or (d < k and not p1 > p0): st.bad("PRE", f"{name}@{t} v={v} k={k}")
                if d >= k: deep += 1
            st.inc(f"X_DEEP{k}", deep)
            if PCH > n * (2 * n + 1) ** k + deep: st.bad("LEV", f"{name} v={v} k={k}")
    # NO-DEV
    WCH = sum(info[t + 1]["W"] != info[t]["W"] for t in range(a, b)); FL = T - WCH
    if all(info[t]["xi"] == info[t]["W"] for t in range(a, b + 1)):
        st.inc("X_NODEV_runs")
        if Rstar or WCH > n - 1 or T > (n - 1) + 4 * n * n * (n - 1): st.bad("NODEV", f"{name} F[{a},{b}]")
        mxt(st, "max_NODEV_F", (T, name))
    # BIP-RED and [SUB] on frozen stretches
    cuts = [t for t in range(a, b) if info[t + 1]["sbar"] != info[t]["sbar"]]; SB = len(cuts)
    mxt(st, "max_SB", (SB, name))
    Rdeg = 0; p = a
    for c in cuts + [b]:
        q = c if c in cuts else b
        Rp = 0
        relc = {}
        for u in range(p, q):
            rel = [y for y in sw[u] if any(blocked(t, y, info[u + 1]["sg"][y]) for t in range(p, u))]
            if rel: Rp += 1
            for y in rel: relc[(y, info[u + 1]["sg"][y])] = relc.get((y, info[u + 1]["sg"][y]), 0) + 1
        if relc: mxt(st, "max_strict_releases_per_edge_per_Phi", (max(relc.values()), name))
        Wp = sum(info[t + 1]["W"] != info[t]["W"] for t in range(p, q))
        if Wp > (n - 1) * (Rp + 1): st.bad("SUBF", f"{name} Phi[{p},{q}]")
        Rdeg = max(Rdeg, Rp); p = q + 1
    if T > SB + (SB + 1) * (n - 1) * (Rdeg + 1) + FL: st.bad("BIPR", f"{name} F[{a},{b}]")
    # INT-XCH0 on W-constant intervals
    p = a
    for t in list(range(a, b)) + [b]:
        if t == b or info[t + 1]["W"] != info[t]["W"]:
            q = t
            if q > p:
                xc = [sum(info[u + 1]["xi"][d] != info[u]["xi"][d] for u in range(p, q)) for d in range(n)]
                if q - p > mE + sum(dE[d] * xc[d] for d in range(n)): st.bad("XIR", f"{name} I[{p},{q}]")
                mxt(st, "max_Wconst_interval", (q - p, name))
            p = t + 1
    # Fact EXT: global-statement control
    for t in range(a, min(b + 1, a + 3)):
        for y in range(n):
            xs = [info[t]["xi"][c] for c in range(n)]
            for i in range(min(len(xs), 6)):
                for j in range(i + 1, min(len(xs), 6)):
                    x1, x2 = xs[i], xs[j]
                    if x1 != x2 and E.extend(y, x1) == E.extend(y, x2): st.inc("X_EXT_GLOBAL")


_orig_run_game = L.run_game
def run_game(g, s, t, st, name):
    RUNSTATE.clear()
    orig_wrun = L.wrun
    collected = {}
    def cap(g_, E, info, a, b, st_, name_, Even, nE, mE, dE):
        RUNSTATE["info"] = info; wrun(g_, E, info, a, b, st_, name_, Even, nE, mE, dE)
    L.wrun = cap
    try: _orig_run_game(g, s, t, st, name)
    finally: L.wrun = orig_wrun
L.run_game = run_game
L.read_start = read_start
KEYS = ("STEP", "SWR", "XIR", "RETX", "E0B", "TRI", "WAIT", "GDEV", "PCH", "RST", "PRE", "LEV", "NODEV", "BIPR", "SUBF")
if __name__ == "__main__":
    import io, contextlib, re
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf): L.main()
    out = buf.getvalue().splitlines(); bad = 0
    for l in out:
        if not l.startswith("RESULT"): print(l)
        m = re.match(r"(\S+): (\d+)$", l)
        if m and m[1] in KEYS + ("XIPLAY", "XW", "XIMON", "WMON"): bad += int(m[2])
    print("RESULT", "PASS" if bad == 0 else "FAIL", "violations", bad)
