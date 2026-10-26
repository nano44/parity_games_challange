#!/usr/bin/env python3
"""L-SI box 17 (successor 13): DATA for Lemma P^c_sch and Corollary CHARGE (docs/si/N5-RUND-box17.md §14).
Setting: S = a maximal run of states inside one phase (key (lambda_Xi, tau) constant), no fallback, lambda_W map constant (CR-D's (ii)).
Level L (env L, default -1). Even edge (x, z) FORBIDDEN AT k: z != sigma_k(x), COARSE_L W_k(z) > COARSE_L W_k(sigma_k x), not Xi_k(z) > Xi_k(sigma_k x).
Path r = (r_0..r_m) to a W-cycle node; its SCHEDULE at state k is clean if every Even edge (r_i, r_i+1) is not forbidden at state k-1-i, and k-m >= k_0.
  P^c_sch: clean schedule at k  =>  COARSE_L W_k(r_0) >= COARSE_L value(r).
  GEN check: for all s <= t in S and every x, with r = x's W-play prefix at t: clean at s => COARSE W_s(x) == COARSE W_t(x) (with MON).
  CHARGE: every change of COARSE W(x) at s-1 -> s has r = x's play at s with dirty schedule at s-1 (a WINDOW change if s-1-m < k_0,
  else CHARGED to a forbidden (i, edge, state s-2-i)).
Also per forbidden edge: #states forbidden, first / last forbidden state (relative to k_0), PERSISTENT if forbidden at the last state j-1.
FS_SPAN_V: an edge forbidden at k and again at some k' >= k + n (CONJECTURE FS); FS_DUR_V: forbidden at > n - 1 states. NOGEN=1 skips GEN.
UNF_V: a charged change with no switch event into a charged edge after its forbidden state (PROVED impossible, note §16);
  UF_ONCE_V: an Even vertex with two U events in one run (CONJECTURE UF-ONCE); U_GT_NE: |U| > #Even (count only).
  U: switch events into an edge forbidden within the previous n - 1 states; SWITCH_INTO_FORB_V: a switch into an edge forbidden at that state (impossible).
OFFUP_V: a forbidden (x, z) with equal cycle nodes in both frames at z and sigma(x) but offset(z) <= offset(sigma x) (PROVED impossible, §17).
FZ_EQ_V: a forbidden (x, z) with Xi(z) = W(z) (PROVED impossible, note §16); forb_gate_*: gate classes of z and a = sigma(x) (first D-vertex on the W-play).
MUT=1: schedule shifted by one (edge i at k-i); MUT=2: forbidden-ness ignored (CR-D without (i)). Usage: sched.py --one GAME [START] [-v] | --list FILE [KMIN] | --rand COUNT NLO NHI SEED (env K) (env RS random start pairs, NMAX)"""
import sys, os, random
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "fb2o"))
from n5x import step, start_pair, Engine, dual, load, readstart
from tcdir import lasso, wval
L = int(os.environ.get("L", "-1")); MUT = os.environ.get("MUT", "0"); VERB = "-v" in sys.argv
C = Counter(); VIOL = []

def ck(E, x):
    m = (x[1] >> (L + 1)) << (L + 1) if L >= 0 else x[1]
    return (E.rew[x[0]], E.weight(m))

def check(g, name, start=None):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []
    while len(rows) <= 3000:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        wn = (lambda s, t: (lambda v: s[v] if g.owner[v] == 0 else t[v]))(list(s), tuple(t))
        W = [wval(E, wn, v) for v in range(g.n)]
        D = {u for u in range(g.n) if g.owner[u] == 1 and sb[u] != t[u]}
        rows.append(dict(key=(tuple(x[0] for x in vs), tuple(t)), lw=tuple(w[0] for w in W), s=list(s), wn=wn, vs=vs, W=W, D=D,
                         fb=r[4] if r else 0))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while (j + 1 < len(rows) and not rows[j]["fb"] and rows[j + 1]["key"] == rows[i]["key"]
               and rows[j + 1]["lw"] == rows[i]["lw"]): j += 1
        if j > i: run(g, E, name, rows, i, j)
        i = j + 1

def forb(g, E, R):
    out = set()
    for x in range(g.n):
        if g.owner[x] != 0: continue
        a = R["s"][x]
        for z in set(g.succ[x]):
            if z != a and ck(E, R["W"][z]) > ck(E, R["W"][a]) and not E.key(R["vs"][z]) > E.key(R["vs"][a]):
                out.add((x, z))
                if tuple(R["vs"][z]) == tuple(R["W"][z]): C["FZ_EQ_V"] += 1; VIOL.append(("FZ_EQ", x, z))
                if R["vs"][z][0] == R["W"][z][0] and R["vs"][a][0] == R["W"][a][0]:
                    if not off(E, R, z) > off(E, R, a): C["OFFUP_V"] += 1; VIOL.append(("OFFUP", x, z))
                    else: C["offup_checked"] += 1
                else: C["offup_cn_split"] += 1
                gz, ga = gate(R, z), gate(R, a)
                C["forb_gate_" + ("z_in_F" if gz is None else "a_in_F" if ga is None else "same" if gz == ga else "diff")] += 1
    return out

def off(E, R, v):
    return E.weight(R["W"][v][1]) - E.weight(R["vs"][v][1])

def gate(R, v):
    return next((y for y in lasso(R["wn"], v)[0] if y in R["D"]), None)

def play(R, x):
    pl, ci = lasso(R["wn"], x); return pl[:pl.index(R["W"][x][0]) + 1]

def dirty(g, F, R, r, k, i0):
    """None if the schedule of r at state k is clean, 'window' if k - m < k_0, else the list of forbidden (i, edge, state)."""
    m = len(r) - 1
    if k - m < i0: return "window"
    bad = []
    for q in range(m):
        if g.owner[r[q]] != 0: continue
        st = k - q if MUT == "1" else k - 1 - q
        if MUT != "2" and st in F and (r[q], r[q + 1]) in F[st]: bad.append((q, (r[q], r[q + 1]), st))
    return bad or None

def ustruct(g, E, name, rows, F, i, j, k, e):
    """Structure of one unforbid-switch (k, e = (y, z)); f = the last state < k at which e is forbidden."""
    y, z = e; f = max(ff for ff in range(max(i, k - g.n + 1), k) if e in F[ff]); a_f, a_k = rows[f]["s"][y], rows[k]["s"][y]
    G = lambda kk, v: "F" if gate(rows[kk], v) is None else "g%d" % gate(rows[kk], v)
    later = [kk for kk in range(k + 1, j) if any(x == y for x, _ in F[kk])]
    C["U_y_forbidden_later"] += bool(later); C["U_y_gated_after"] += gate(rows[k + 1], y) is not None
    C["U_from_F"] += gate(rows[k], a_k) is None
    C["U_xi_z_rose"] += E.key(rows[k]["vs"][z]) > E.key(rows[f]["vs"][z]); C["U_a_changed"] += a_f != a_k
    C["U_xi_a_rose"] += E.key(rows[k]["vs"][a_k]) > E.key(rows[f]["vs"][a_f])
    C["U_D_changed"] += rows[k]["D"] != rows[f]["D"]
    d0, d1 = off(E, rows[k], y), off(E, rows[k + 1], y)
    C["U_offset_up"] += d1 > d0; C["U_offset_same"] += d1 == d0; C["U_offset_down"] += d1 < d0
    upk = off(E, rows[k], z) > off(E, rows[k], a_k)
    C["U_offset_up_at_k"] += upk
    skey = lambda kk: (frozenset(rows[kk]["D"]), tuple((u, tuple(rows[kk]["vs"][u]), tuple(rows[kk]["W"][u])) for u in sorted(rows[kk]["D"])))
    bd = any(skey(kk) != skey(f) for kk in range(f, k + 2))
    up = d1 > d0
    C["U_cls_" + ("up" if up else "boundary" if bd else "OTHER")] += 1
    if not up and not bd: VIOL.append(("U_OTHER", name, i, k, e))
    C["U_upk_noboundary"] += upk and not any(skey(kk) != skey(f) for kk in range(f, k + 1))
    C["U_x_up%d_bd%d_upk%d" % (up, bd, upk)] += 1
    if not bd:
        C["U_nb_offz_f>offz_k1"] += off(E, rows[f], z) > off(E, rows[k + 1], z)
        C["U_nb_offa_k>offa_f"] += off(E, rows[k], a_k) > off(E, rows[f], a_f)
        print(f"  NB k={k - i} f={f - i} y={y} z={z} a_f={a_f} a_k={a_k} off_y {d0}->{d1} off_z f/k/k+1 {off(E, rows[f], z)}/{off(E, rows[k], z)}/{off(E, rows[k + 1], z)}"
              f" off_a f/k {off(E, rows[f], a_f)}/{off(E, rows[k], a_k)} lam_y={rows[k]['W'][y][0]}")
    print(f"  USTRUCT {name} k0={i} k={k - i} f={f - i} y={y} z={z} a_f={a_f}({G(f, a_f)}) a_k={a_k}({G(k, a_k)}) z@f={G(f, z)} z@k={G(k, z)}"
          f" y@k+1={G(k + 1, y)} D_f={sorted(rows[f]['D'])} D_k={sorted(rows[k]['D'])} y_forbidden_later={later[:3]}")

def run(g, E, name, rows, i, j):
    C["runs"] += 1; C["states"] += j - i + 1
    F = {k: forb(g, E, rows[k]) for k in range(i, j)}
    first, last, cnt = {}, {}, Counter()
    for k in range(i, j):
        for e in F[k]: first.setdefault(e, k - i); last[e] = k - i; cnt[e] += 1
    pers = {e for e in last if last[e] == j - 1 - i}
    C["forbidden_edges"] += len(last); C["persistent_edges"] += len(pers); C["forbidden_pairs"] += sum(cnt.values())
    if cnt:
        mc = max(cnt.values()); C["max_forb_states_per_edge"] = max(C["max_forb_states_per_edge"], mc)
        if mc > g.n - 1: C["FORB_GT_N1"] += 1; print("FORB_GT_N1", name, i, j - i, g.n, cnt.most_common(1))
        C["max_last_forb_rel"] = max(C["max_last_forb_rel"], max(last.values()))
        for e in last:
            sp = last[e] - first[e]; C["max_span"] = max(C["max_span"], sp); C["max_span_minus_n"] = max(C["max_span_minus_n"], sp - g.n)
            if sp >= g.n: C["FS_SPAN_V"] += 1; VIOL.append(("FS_SPAN", name, i, e, first[e], last[e], g.n))
            if cnt[e] > g.n - 1: C["FS_DUR_V"] += 1; VIOL.append(("FS_DUR", name, i, e, cnt[e], g.n))
            if e in pers: C["max_pers_count"] = max(C["max_pers_count"], cnt[e])
        C["max_KF"] = max(C["max_KF"], len({k for k in F if F[k]})); C["max_runlen"] = max(C["max_runlen"], j - i)
        if max(last.values()) > g.n - 1: C["LASTFORB_GT_N1"] += 1
    if VERB:
        print(f"RUN {name} k0={i} len={j - i} edges_forbidden={len(last)} persistent={len(pers)}")
        for e in sorted(last, key=lambda e: last[e]):
            print(f"  EDGE {e} first={first[e]} last={last[e]} count={cnt[e]} {'PERSISTENT' if e in pers else ''}")
    cv = [[ck(E, rows[k]["W"][x]) for x in range(g.n)] for k in range(i, j + 1)]
    # GEN: every pair s <= t
    for tt in (range(i, j + 1) if os.environ.get("NOGEN") != "1" else ()):
        for x in range(g.n):
            r = play(rows[tt], x)
            for ss in range(i, tt):
                if dirty(g, F, rows[tt], r, ss, i) is None:
                    C["gen_clean"] += 1
                    if cv[ss - i][x] != cv[tt - i][x]:
                        C["GEN_V"] += 1; VIOL.append(("GEN", name, i, ss, tt, x))
                    elif len(r) > 1: C["gen_clean_content"] += 1
    # UNF: switch events (k', e) at k' -> k'+1 into an edge e forbidden at some state in [k'-n+1, k'-1]
    U = set(); sw = 0
    for k in range(i, j):
        for x in range(g.n):
            if g.owner[x] != 0 or rows[k]["s"][x] == rows[k + 1]["s"][x]: continue
            sw += 1; e = (x, rows[k + 1]["s"][x])
            if e in F[k]: C["SWITCH_INTO_FORB_V"] += 1; VIOL.append(("SWITCH_INTO_FORB", name, k, e))
            if any(e in F[f] for f in range(max(i, k - g.n + 1), k)):
                U.add((k, e))
                if os.environ.get("USTRUCT") == "1": ustruct(g, E, name, rows, F, i, j, k, e)
    C["switches"] += sw; C["U"] += len(U); C["max_U_run"] = max(C["max_U_run"], len(U))
    Ux = Counter(e[0] for _, e in U)
    if Ux:
        C["max_U_per_vertex"] = max(C["max_U_per_vertex"], max(Ux.values()))
        if max(Ux.values()) > 1: C["UF_ONCE_V"] += 1; VIOL.append(("UF_ONCE", name, i, sorted(U)))
    if len(U) > sum(1 for v in range(g.n) if g.owner[v] == 0): C["U_GT_NE"] += 1
    if VERB: print("  U", sorted(U))
    # CHARGE: every change at s-1 -> s
    pervx = defaultdict(lambda: Counter()); charged_edges = defaultdict(set)
    for ss in range(i + 1, j + 1):
        for x in range(g.n):
            if cv[ss - i][x] == cv[ss - 1 - i][x]: continue
            C["changes"] += 1; pervx[x]["changes"] += 1
            r = play(rows[ss], x); d = dirty(g, F, rows[ss], r, ss - 1, i)
            if d is None: C["CHARGE_V"] += 1; VIOL.append(("CHARGE", name, i, ss, x)); continue
            if d == "window": C["window"] += 1; pervx[x]["window"] += 1; continue
            C["charged"] += 1; pervx[x]["charged"] += 1
            if not any((kk, e) in U for _, e, f in d for kk in range(f + 1, ss)): C["UNF_V"] += 1; VIOL.append(("UNF", name, i, ss, x, d))
            es = {e for _, e, _ in d}; charged_edges[x] |= es
            if es & pers: C["charged_persistent"] += 1
            if VERB: print(f"  CHANGE x={x} s={ss - i} m={len(r) - 1} charged={d}")
    for x, c in pervx.items():
        C["max_changes_per_vertex"] = max(C["max_changes_per_vertex"], c["changes"])
        C["max_charged_per_vertex"] = max(C["max_charged_per_vertex"], c["charged"])
        C["max_charged_edges_per_vertex"] = max(C["max_charged_edges_per_vertex"], len(charged_edges[x]))
    if VERB:
        for x in sorted(pervx): print(f"  VERTEX {x} {dict(pervx[x])} charged_edges={sorted(charged_edges[x])}")

def main():
    a = [x for x in sys.argv[1:] if x != "-v"]
    if a[0] == "--one":
        g = load(a[1]); check(g, a[1], readstart(a[2]) if len(a) > 2 else None)
    elif a[0] == "--rand":
        sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box43")); from multi import rand_ckO
        cnt, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); q = 0; K = int(os.environ.get("K", "0"))
        while q < cnt:
            g = rand_ckO(rng, lo, hi, K or rng.choice((2, 2, 3, 4)))
            if g is None: continue
            q += 1
            st = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1})
            check(g, f"rand seed {seed} #{q}", None if q % 2 else st)
    else:
        kmin = int(a[2]) if len(a) > 2 else 2
        for line in open(a[1]):
            f = line.strip()
            if not f: continue
            g = load(os.path.join(ROOT, f))
            if g.n > int(os.environ.get("NMAX", "48")) or sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2) < kmin:
                continue
            check(g, f); rng = random.Random(f)
            for _ in range(int(os.environ.get("RS", "0"))):
                check(g, f + " rs", ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                     {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}))
    print(f"L={L} MUT={MUT}", " ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for v in VIOL[:8]: print("VIOLATION", v)
    print("SCHED PASS" if not VIOL else "SCHED FAIL")

if __name__ == "__main__":
    main()
