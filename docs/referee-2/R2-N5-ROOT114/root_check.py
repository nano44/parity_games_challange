#!/usr/bin/env python3
r"""REFEREE-2 successor 25 (Opus 5.5, D15): own check of P-N5-ROOT (docs/new/P-N5-ROOT-box114.md @ l-new ed2fdaf2, sha1 f06f493e).
State construction: my R2-N5-LATEP/latep_check.py (my N5 loop; W-runs as in R89); start files as in R2-N5-WRUN/wrun_check.py
(validated; non-edges rejected). The lane's experiments/new/box113/*.py are NOT imported. beta = P-N5-STAIR §5 (3n + 1 bits), as in my
R2-N5-STAIR/stair_check.py. Checks per W-run F = [a, b] (each must be 0):
  DROOT   Lemma DESC-ROOT: for every descent (v, k) (prev change k'), the walk x_(i+1) = s_(k+1)(x_i) stops at x_j not in C with a descent
          at k whose previous change is k', of type R/T/S; j = 0 when (v, k) is not COPIED
  DCNT    DESC_F <= n (R + T + S), T <= TS (injective tie-switch map)
  RSTAIR  Theorem ROOT-STAIR: |F| <= T1 + n(3n + 1) + (3n + 1) n (R + S + TS); R + S <= n WCT; TS <= n |F|
  RCC     root change (y, k) has y not in C
  ONEW    Lemma ORIGIN-NEW: origin root change with k - 1 >= a has (y, z) not in H_(k-1) and (y, z) in Is_k \ Is_(k-1)
  OPTOFF  [1E-N3] read through R91 OPT-OFF: sigma_k is optimal in H_(k-1): W_k(c) <= W_k(sigma_k y) for (y, c) in H_(k-1), y not own W-cycle node
  NFUEL   Lemma NEW-FUEL: Even y switched at k to z, k - 1 >= a, (y, z) not in H_(k-1) => Xi_(k-1)(z) != Xi_k(z)
  RSPLIT  every R-descent has k - 1 >= a; each R-descent through an H_(k-1) edge is a relay
  FRS     Corollary FUEL-ROOT-STAIR: R^fuel <= sum N <= sum n(n + 2)(HC + n), and the |F| bound
Boundary probes (NOT violations; the binder question «k a transition of F»): the transition k = b leaving F (if any), with b - 1 >= a:
  BND_*   kind (fb / tau / lamW), and whether ORIGIN-NEW / NEW-FUEL statements hold there.
Usage: root_check.py files list.txt [runs [prefix]] | random N nmin nmax seed [starts]   (DUMP=1: one line per W-run)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-LATEP")); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-WRUN"))
import latep_check as L
import wrun_check as WR
DUMP = os.environ.get("DUMP")
SHOW = int(os.environ.get("SHOW", "3"))
shown = {}


def note(st, key, msg):
    st.inc(key)
    if shown.get(key, 0) < SHOW: shown[key] = shown.get(key, 0) + 1; print("EX", key, msg, flush=True)


def fkey(x0, x1):
    if x0[0] != x1[0]: return (2, 0)
    d = x0[1] ^ x1[1]
    if d: return (1, d.bit_length() - 1)
    return (0, 0)


def wrun(g, E, info, a, b, st, name, *rest):
    n = g.n; K = E.key; T = b - a
    if T == 0: return
    st.inc("WRUNS"); st.inc("WRUN_transitions", T)
    C = {v for v in range(n) if info[a]["lamW"][v] == v}; tau = info[a]["tu"]; Ev = lambda v: g.owner[v] == 0
    def beta(x):
        c, m, l = x
        rb = tuple(((m >> q & 1) if E.rankpar[q] == 0 else 1 - (m >> q & 1)) for q in range(n - 1, -1, -1))
        sl = l if E.par[c] == 1 else -l
        return rb + tuple(1 if sl >= j else 0 for j in range(-n, n + 1))
    def s(k, v): return info[k]["sg"][v] if Ev(v) else tau[v]
    def sw(t, y): return Ev(y) and info[t]["sg"][y] != info[t + 1]["sg"][y]
    def wch(t, v): return info[t]["W"][v] != info[t + 1]["W"][v]
    def inH(t, y, z): return z == info[t]["sg"][y] or (y, z) in info[t]["Is"]
    nb = 3 * n + 1
    pos = {v: [] for v in range(n)}; when = {v: [] for v in range(n)}
    WCT = T1 = TS = 0
    for k in range(a, b):
        if info[k]["W"] == info[k + 1]["W"]: T1 += 1
        else: WCT += 1
        for v in range(n):
            if wch(k, v):
                b0, b1 = beta(info[k]["W"][v]), beta(info[k + 1]["W"][v])
                pos[v].append(next(i for i in range(nb) if b0[i] != b1[i])); when[v].append(k)
            elif sw(k, v): TS += 1
    # descents: dict (v, k) -> k'
    desc = {}
    for v in range(n):
        for j in range(1, len(pos[v])):
            if pos[v][j] > pos[v][j - 1]: desc[(v, when[v][j])] = when[v][j - 1]
    def typ(x, k, kp):
        if sw(k, x): return "R"
        if any(sw(t, x) for t in range(kp + 1, k)): return "T"
        if sw(kp, x): return "S"
        return "COPIED"
    cnt = {"R": 0, "T": 0, "S": 0, "COPIED": 0}
    for (v, k), kp in desc.items():
        tv = typ(v, k, kp); cnt[tv] += 1; st.inc("DROOT_checks")
        x = v; j = 0
        while not (x in C or any(sw(t, x) for t in range(kp, k + 1))):
            x = s(k + 1, x); j += 1
            if j > n: break
        if j > n or x in C: note(st, "DROOT", f"{name} v={v} k={k} walk ends in C/loops"); continue
        if desc.get((x, k)) != kp: note(st, "DROOT", f"{name} v={v} k={k} x_j={x} no descent with prev {kp}"); continue
        if typ(x, k, kp) == "COPIED": note(st, "DROOT", f"{name} v={v} x={x} COPIED")
        if tv != "COPIED" and j != 0: note(st, "DROOT", f"{name} v={v} j={j}")
        if j > 0: st.inc("DROOT_j_pos")
    D = len(desc)
    for t_ in cnt: st.inc("DESC_" + t_, cnt[t_])
    st.inc("DESC", D); st.inc("TS", TS)
    # T <= TS: injective map T-descent -> tie switch inside (k', k)
    used = set()
    for (x, k), kp in desc.items():
        if typ(x, k, kp) != "T": continue
        ts = [t for t in range(kp + 1, k) if sw(t, x) and not wch(t, x) and (x, t) not in used]
        if not ts: note(st, "DCNT", f"{name} T-descent {(x, k)} no tie switch"); continue
        used.add((x, ts[0]))
    R, Tn, S = cnt["R"], cnt["T"], cnt["S"]
    if D > n * (R + Tn + S) or Tn > TS: note(st, "DCNT", f"{name} D {D} R {R} T {Tn} S {S} TS {TS}")
    if T > T1 + n * nb + nb * n * (R + S + TS): note(st, "RSTAIR", f"{name} |F| {T}")
    if R + S > n * WCT or TS > n * T: note(st, "RSTAIR", f"{name} converse")
    # root changes, ORIGIN-NEW, OPT-OFF, NEW-FUEL
    for k in range(a, b):
        A, B = info[k], info[k + 1]
        if k - 1 >= a:
            P = info[k - 1]
            for y in range(n):
                if not Ev(y) or A["lamW"][y] == y: continue
                st.inc("OPTOFF_checks")
                for c in set(g.succ[y]):
                    if inH(k - 1, y, c) and K(A["W"][c]) > K(A["W"][A["sg"][y]]): note(st, "OPTOFF", f"{name}@{k} y={y} c={c}")
        for y in range(n):
            if not sw(k, y): continue
            z = B["sg"][y]
            if k - 1 >= a and not inH(k - 1, y, z):
                st.inc("NEWEDGE")
                if info[k - 1]["xi"][z] == A["xi"][z]: note(st, "NFUEL", f"{name}@{k} y={y} z={z}")
            if not wch(k, y): continue
            st.inc("ROOTCH")
            if y in C: note(st, "RCC", f"{name}@{k} y={y}")
            if wch(k, z): st.inc("RELAY"); continue
            st.inc("ORIGIN")
            if k - 1 < a: st.inc("ORIGIN_first"); continue
            if inH(k - 1, y, z) or (y, z) not in A["Is"] or (y, z) in info[k - 1]["Is"]: note(st, "ONEW", f"{name}@{k} y={y} z={z}")
    # boundary probe: transition b leaving F
    if b + 1 < len(info) and b - 1 >= a:
        A, B, P = info[b], info[b + 1], info[b - 1]
        kd = "tau" if B["tu"] != A["tu"] else ("lamW" if B["lamW"] != A["lamW"] else "fb")
        st.inc("BND_" + kd)
        for y in range(n):
            if not sw(b, y): continue
            z = B["sg"][y]
            if not inH(b - 1, y, z):
                st.inc("BND_newedge_" + kd)
                if P["xi"][z] == A["xi"][z]: note(st, "BND_NFUEL_FAILS_" + kd, f"{name}@{b} y={y} z={z}")
            if A["W"][y] != B["W"][y] and A["W"][z] == B["W"][z]:
                st.inc("BND_origin_" + kd)
                if inH(b - 1, y, z): note(st, "BND_ONEW_FAILS_" + kd, f"{name}@{b} y={y} z={z} yinC={y in C}")
    # ROOT-SPLIT and FUEL-ROOT-STAIR
    Rold = Rfuel = 0
    for (y, k), kp in desc.items():
        if not sw(k, y): continue
        if k - 1 < a: note(st, "RSPLIT", f"{name} R-descent at first transition"); continue
        z = info[k + 1]["sg"][y]
        if inH(k - 1, y, z):
            Rold += 1
            if not wch(k, z): note(st, "RSPLIT", f"{name}@{k} y={y} old-edge R-descent not a relay")
        else: Rfuel += 1
    fr = {}
    for k in range(a + 1, b):
        for y in range(n):
            if not sw(k, y): continue
            z = info[k + 1]["sg"][y]
            if inH(k - 1, y, z) or info[k - 1]["xi"][z] == info[k]["xi"][z]: continue
            fr.setdefault((y, z), []).append((k, fkey(info[k - 1]["xi"][z], info[k]["xi"][z])))
    SN = SB = 0
    for (y, z), lst in fr.items():
        HC = 0
        for u in range(a, b):
            if info[u]["xi"][z] == info[u + 1]["xi"][z]: continue
            last = [kx for (kr, kx) in lst if kr <= u]
            if last and fkey(info[u]["xi"][z], info[u + 1]["xi"][z]) > last[-1]: HC += 1
        SN += len(lst); SB += n * (n + 2) * (HC + n)
    if not (Rfuel <= SN <= SB): note(st, "FRS", f"{name} Rfuel {Rfuel} SN {SN} SB {SB}")
    if T > T1 + n * nb + nb * n * (SB + Rold + S + TS): note(st, "FRS", f"{name} |F|")
    st.inc("R_old", Rold); st.inc("R_fuel", Rfuel); st.inc("FUEL_reroutes", SN)
    if DUMP: print("WRUN", name, a, b, "n", n, "T", T, "WCT", WCT, "DESC", D, cnt, "TS", TS, "Rold", Rold, "Rfuel", Rfuel, flush=True)


_orig = WR._orig_run_game
def run_game(g, s, t, st, name):
    o = L.wrun; L.wrun = wrun
    try: _orig(g, s, t, st, name)
    finally: L.wrun = o
L.run_game = run_game; L.read_start = WR.read_start
KEYS = ("DROOT", "DCNT", "RSTAIR", "RCC", "ONEW", "OPTOFF", "NFUEL", "RSPLIT", "FRS", "XIPLAY", "XW", "XIMON")
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
