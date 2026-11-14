#!/usr/bin/env python3
"""REFEREE-2 successor 39: own replay for packet P-N5-WRAP (L-SI 53, claude/l-si e01447e7). Shares no code with L-SI, L-COMP, L-RED or
REFEREE (no wrap104 / n5v / n5bxi / si.py / n5x236). Written from the packet's §2.1 text and SPEC's text; the SPEC primitives (rank,
order, S1 = Odd's optimum, the dual, ⊕, play values, one-player optimum) are REFEREE-2's own R2-P-N5-END/r2end.py.

  W(H, s0) built from §2.1 (vertex order of §2.1, or --perm: a random permutation of the new vertices' indices);
  S3 by FIX 1; the run of N5′-xi (mode xi) or N5 (mode spec): S1/S2 on W and on W^d, S4a (spec: S1 on the dual of the arena; xi: the
  Ξσ-best element of TIE(v), SPEC's choice, then the larger index), S4b, S4c (FIX 3), S5.
Counters (must be 0; unit in brackets):
  s3fail [game] S3 ≠ the standard state of s0 | nonstd [state before the first fallback] not standard (pads at V_E, y at valves, κ0, τ0)
  e0fail [state] τ ≠ τ0 or Iτ ≠ ∅ | nohoward [(step, v ∈ V_E)] H-part move not to a ⊴_H-best successor (my own S1 on H), or a ⊴_H-best
  current successor left; for spec: H-part move outside {s(v)} ∪ strictly better | fbwrong [game] xi: first fallback ≠ T + 1 (T = #H-moves)
  endwrong [game] fallbacks ≠ 1 or iterations ≠ F + 2 | kconf [game] K-configs ≠ κ0^F, κ1, κ2, κ3 | odd5 [game] the 5-step value relation of
  ODD-W (b), (c) fails at some state (Ξσ(v) = (c, P, 6ℓ), Ξσ(m) = (c, P, 6ℓ + 5) against my S1 on H) | rem3 [game, spec] F > m_E − |V_E| + 1
G_n (Table 4 graph, Figure-4 priorities = Table 4's d, e, g, k, f, h minus 2; --table4 keeps Table 4's): Howard / I^loc on G_n from ι
  with own S1: steps T_n; ntfail [state] two nodes with equal Ξσ values (Claim NT); tiefail [(state, v)] a player-0 node with ≥ 2
  ⪯σ-best successors; sinkfail [state] some cycle component ≠ x; injfail [game] priorities not injective or x not the unique minimum.
Controls: --ctrl start (τ(K2) := r at S3: e0fail, kconf, nonstd fire), --ctrl worst (my H-check uses the WORST successor: nohoward fires),
  --nt-rand (Claim NT's distinctness counted on random games that are NOT 1-sink games: ntfail fires).
Usage: r2wrap.py rand COUNT SEED NMAX [--mode xi|spec] [--perm] [--ctrl ...] | r2wrap.py gn NMAX [--table4] | r2wrap.py wgn NMAX [--mode ..]
       | r2wrap.py ntrand COUNT SEED
"""
import sys, os, random
from collections import defaultdict
H_ = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(H_, "..", "R2-P-N5-END"))
from r2end import Order, s1, dual, oplus, vals_of

CTRL = None


def build_W(H, s0, perm_rng=None):
    """H = dict(pr, ow, E) (vertices 0..n-1); returns W as dict(pr, ow, E, names, idx) with §2.1's vertex order."""
    n = len(H["pr"]); pr, ow, E = [], [], []; names = []
    def add(nm, p, o): names.append(nm); pr.append(p); ow.append(o); E.append([])
    for v in range(n): add(("v", v), H["pr"][v] + 6, H["ow"][v])
    top = max(H["pr"]) + 6 + 2; top += top % 2
    for nm, p, o in (("cW", top, 0), ("K0", top + 2, 0), ("K1", 5, 0), ("K2", 3, 1), ("K3", top + 3, 0), ("pA", 0, 0), ("s", 0, 0),
                     ("q", 1, 0), ("r", 0, 0)):
        add(nm, p, o)
    for v in range(n):
        for w in H["E"][v]:
            if H["ow"][v] == 0:
                for t, p in (("pb", 1), ("y", 2), ("b", 0), ("pB", 0), ("pe", 1), ("g", 1), ("m", 2 if w == s0[v] else 0)):
                    add((t, v, w), p, 1 if t == "g" else 0)
            else:
                for t, p in (("pb", 1), ("y", 2), ("b", 0), ("x3", 0), ("x2", 0), ("x1", 0)):
                    add((t, v, w), p, 0)
        if H["ow"][v] == 1: add(("peo", v), 1, 0)
    N = len(names)
    if perm_rng is not None:          # permute the indices of the new vertices (statements must not depend on it)
        new = list(range(n, N)); sh = new[:]; perm_rng.shuffle(sh); mp = dict(zip(new, sh)); mp.update({v: v for v in range(n)})
        inv = sorted(range(N), key=lambda i: mp[i])
        names = [names[i] for i in inv]; pr = [pr[i] for i in inv]; ow = [ow[i] for i in inv]
    idx = {nm: i for i, nm in enumerate(names)}
    E = [[] for _ in range(N)]
    def e(a, b): E[idx[a]].append(idx[b])
    e("cW", "cW"); e("K0", "K1"); e("K0", "pA"); e("pA", "K3"); e("K1", "q"); e("K1", "s"); e("s", "K1"); e("q", "K0")
    e("K2", "r"); e("K2", "K2"); e("r", "K1"); e("K3", "K1"); e("K3", "K2")
    for v in range(n):
        for w in H["E"][v]:
            if H["ow"][v] == 0:
                e(("v", v), ("m", v, w)); e(("m", v, w), ("g", v, w)); e(("g", v, w), ("pe", v, w)); e(("pe", v, w), "cW")
                e(("g", v, w), ("pB", v, w)); e(("pB", v, w), ("b", v, w))
            else:
                e(("v", v), ("x1", v, w)); e(("x1", v, w), ("x2", v, w)); e(("x2", v, w), ("x3", v, w)); e(("x3", v, w), ("b", v, w))
            e(("b", v, w), ("y", v, w)); e(("y", v, w), ("v", w)); e(("b", v, w), ("pb", v, w)); e(("pb", v, w), "K0")
        if H["ow"][v] == 1: e(("v", v), ("peo", v)); e(("peo", v), "cW")
    assert N == n + 7 * sum(len(H["E"][v]) for v in range(n) if H["ow"][v] == 0) + 6 * sum(len(H["E"][v]) for v in range(n) if H["ow"][v] == 1) \
        + sum(1 for v in range(n) if H["ow"][v] == 1) + 9
    assert all(E[i] for i in range(N))
    return dict(pr=pr, ow=ow, E=E, names=names, idx=idx, n=N, nH=n)


def fix1(pr, ow, E):
    st = [None] * len(pr)
    for v in range(len(pr)):
        if ow[v] == 0:
            def key(w): r = pr[w] if pr[w] % 2 == 0 else -pr[w]; return (r, w if r % 2 == 0 else -w)
        else:
            def key(w): p = pr[w] + 1; r = p if p % 2 == 0 else -p; return (r, w if r % 2 == 0 else -w)
        st[v] = max(E[v], key=key)
    return st


def standard(Wg, H, s):
    """the standard state (σ, τ0) of the H-strategy s (dicts over W's vertices)."""
    I = Wg["idx"]; sig = {}; tau = {}
    for v in range(Wg["nH"]):
        if H["ow"][v] == 0: sig[I[("v", v)]] = I[("m", v, s[v])]
        else: tau[I[("v", v)]] = I[("peo", v)]
        for w in H["E"][v]:
            sig[I[("b", v, w)]] = I[("y", v, w)]
            if H["ow"][v] == 0: tau[I[("g", v, w)]] = I[("pe", v, w)]
    sig[I["K0"]] = I["pA"]; sig[I["K1"]] = I["s"]; sig[I["K3"]] = I["K2"]; tau[I["K2"]] = I["K2"]
    return sig, tau


def kconf(Wg, sig):
    I, nm = Wg["idx"], Wg["names"]
    return (nm[sig[I["K0"]]], nm[sig[I["K1"]]], nm[sig[I["K3"]]])


def hvals(H, s):
    sig = [s[v] if H["ow"][v] == 0 else None for v in range(len(H["pr"]))]
    return s1(H["pr"], H["ow"], H["E"], sig, Order(H["pr"]))[0]


def run(H, s0, mode, C, perm_rng=None, cap=20000):
    Wg = build_W(H, s0, perm_rng); pr, ow, E, I, nm = Wg["pr"], Wg["ow"], Wg["E"], Wg["idx"], Wg["names"]; n = Wg["n"]
    od = Order(pr); dpr, dow = dual(pr, ow); dod = Order(dpr); odH = Order(H["pr"])
    st = fix1(pr, ow, E)
    sig = [st[v] if ow[v] == 0 else None for v in range(n)]; tau = [st[v] if ow[v] == 1 else None for v in range(n)]
    s_std, t_std = standard(Wg, H, s0)
    if any(sig[v] != w for v, w in s_std.items()) or any(tau[v] != w for v, w in t_std.items()): C["s3fail"] += 1
    if CTRL == "start": tau[I["K2"]] = I["r"]
    tau0 = list(tau) if CTRL != "start" else [t_std.get(v) for v in range(n)]
    VE = [v for v in range(Wg["nH"]) if H["ow"][v] == 0]
    padof = {I[("m", v, w)]: w for v in VE for w in H["E"][v]}
    it = 0; fb = []; confs = [kconf(Wg, sig)]; hmoves = 0
    s_cur = list(s0)
    while True:
        val, sbar = s1(pr, ow, E, sig, od)
        Is = {v: [w for w in E[v] if w != sig[v] and od.cmp(val[w], val[sig[v]]) > 0] for v in range(n) if ow[v] == 0}
        Is = {v: l for v, l in Is.items() if l}
        dval, tbar = s1(dpr, dow, E, tau, dod)
        It = {v: [w for w in E[v] if w != tau[v] and dod.cmp(dval[w], dval[tau[v]]) > 0] for v in range(n) if ow[v] == 1}
        It = {v: l for v, l in It.items() if l}
        C["states"] += 1
        if tau != tau0 or It: C["e0fail"] += 1
        before_fb = not any(fb)
        if before_fb:
            s_std, t_std = standard(Wg, H, s_cur)
            if any(sig[v] != w for v, w in s_std.items()) or any(tau[v] != w for v, w in t_std.items()): C["nonstd"] += 1
            # ODD-W (b), (c): stretched values
            hv = hvals(H, s_cur)
            for v in range(Wg["nH"]):
                c, P, l = hv[v]; x = val[I[("v", v)]]
                if x != (I[("v", c)], frozenset(I[("v", u)] for u in P), 6 * l): C["odd5"] += 1
                if H["ow"][v] == 0:
                    for w in H["E"][v]:
                        c2, P2, l2 = hv[w]
                        if val[I[("m", v, w)]] != (I[("v", c2)], frozenset(I[("v", u)] for u in P2), 6 * l2 + 5): C["odd5"] += 1
        if not Is and not It: break
        it += 1
        if it > cap: C["capped"] += 1; break
        snew = list(sig); tnew = list(tau)
        if Is:
            A = {v: sorted(set([sig[v]] + Is.get(v, []))) for v in range(n) if ow[v] == 0}
            HE = [A[v] if ow[v] == 0 else [tau[v]] for v in range(n)]
            _, hch = s1(dpr, dow, HE, tau, dod)
            for v in range(n):
                if ow[v] == 0: snew[v] = hch[v] if hch[v] is not None else HE[v][0]
            if mode == "xi":
                fH = [snew[v] if ow[v] == 0 else tau[v] for v in range(n)]; Wv = vals_of(od, fH)   # W* = S4a's arena optimum (P2)
                for v in range(n):
                    if ow[v] == 0 and len(A[v]) >= 2 and Wv[v][0] != v:
                        TIE = [w for w in A[v] if oplus(od, v, Wv[w]) == Wv[v]]
                        best = [w for w in TIE if all(od.cmp(val[w], val[u]) >= 0 for u in TIE)]
                        snew[v] = snew[v] if snew[v] in best else max(best)
        if It:
            HE2 = [[sig[v]] if ow[v] == 0 else sorted(set([tau[v]] + It.get(v, []))) for v in range(n)]
            _, hc2 = s1(pr, ow, HE2, sig, od)
            for v in range(n):
                if ow[v] == 1: tnew[v] = hc2[v]
        isfb = snew == sig and tnew == tau
        if isfb:
            if Is:
                for v, l in Is.items():
                    bw = l[0]
                    for w in l[1:]:
                        c = od.cmp(val[w], val[bw])
                        if c > 0 or (c == 0 and w > bw): bw = w
                    snew[v] = bw
            else:
                for v, l in It.items():
                    bw = l[0]
                    for w in l[1:]:
                        c = dod.cmp(dval[w], dval[bw])
                        if c > 0 or (c == 0 and w > bw): bw = w
                    tnew[v] = bw
        elif before_fb:
            # the H-part step
            hv = hvals(H, s_cur); moved = False
            for v in VE:
                new = padof.get(snew[I[("v", v)]])
                if new is None: C["nohoward"] += 1; continue
                ws = H["E"][v]
                best = max(ws, key=lambda w: (0,)) if False else None
                bestv = None
                for w in ws:
                    if bestv is None or (odH.cmp(hv[w], bestv) > 0 if CTRL != "worst" else odH.cmp(hv[w], bestv) < 0): bestv = hv[w]
                if mode == "xi":
                    curbest = odH.cmp(hv[s_cur[v]], bestv) == 0
                    if (curbest and new != s_cur[v]) or (odH.cmp(hv[new], bestv) != 0): C["nohoward"] += 1
                else:
                    if new != s_cur[v] and odH.cmp(hv[new], hv[s_cur[v]]) <= 0: C["nohoward"] += 1
                moved |= new != s_cur[v]; s_cur[v] = new
            hmoves += 1
        fb.append(isfb); sig, tau = snew, tnew; confs.append(kconf(Wg, sig))
    nf = sum(fb); C["runs"] += 1; C["iters"] += it
    if nf != 1: C["endwrong"] += 1; return it, None, hmoves
    F = fb.index(True) + 1
    if it != F + 2: C["endwrong"] += 1
    if mode == "xi" and F != hmoves + 1: C["fbwrong"] += 1
    if mode == "spec":    # Remark 3 (under [RULE]): F ≤ m_E − |V_E| + 1
        mE = sum(len(H["E"][v]) for v in VE)
        if F > mE - len(VE) + 1: C["rem3"] += 1
        C["rec_spec_Fmax"] = max(C["rec_spec_Fmax"], F)
    k0 = ("pA", "s", "K2"); exp = [k0] * F + [("K1", "s", "K2"), ("K1", "q", "K2"), ("K1", "q", "K1")]
    if confs != exp: C["kconf"] += 1
    return it, F, hmoves


def rand_game(rng, nmax):
    n = rng.randint(1, nmax); pr = [rng.randint(0, max(1, n)) for _ in range(n)]; ow = [rng.randint(0, 1) for _ in range(n)]
    E = [sorted(rng.sample(range(n), rng.randint(1, min(n, 3)))) for _ in range(n)]
    s0 = [rng.choice(E[v]) if ow[v] == 0 else None for v in range(n)]
    return dict(pr=pr, ow=ow, E=E), s0


def gn(n, table4=False):
    """Friedmann G_n: Table 4's graph; priorities Figure 4 (Table 4's d, e, g, k, f, h minus 2) unless table4. Returns H, ι, names."""
    names = ["x", "s", "c", "r"] + [f"t{i}" for i in range(1, 2 * n + 1)] + [f"a{i}" for i in range(1, 2 * n + 1)] + \
        [f"{l}{i}" for l in "degkfh" for i in range(1, n + 1)]
    I = {nm: i for i, nm in enumerate(names)}; N = len(names); pr = [0] * N; ow = [0] * N; E = [[] for _ in range(N)]
    d = 0 if table4 else 2
    def put(nm, o, p, succ): pr[I[nm]] = p; ow[I[nm]] = o; E[I[nm]] = sorted(I[s] for s in succ)
    put("t1", 0, 4 * n + 3, ["s", "r", "c"])
    for i in range(2, 2 * n + 1): put(f"t{i}", 0, 4 * n + 2 * i + 1, ["s", "r", f"t{i - 1}"])
    for i in range(1, 2 * n + 1): put(f"a{i}", 1, 4 * n + 2 * i + 2, [f"t{i}"])
    put("c", 0, 8 * n + 4, ["s", "r"])
    for i in range(1, n + 1):
        put(f"d{i}", 0, 4 * i + 1 - d, ["s", f"e{i}", "r"] + [f"a{j}" for j in range(1, 2 * i + 1)])
        put(f"e{i}", 1, 4 * i + 2 - d, [f"d{i}", f"h{i}"])
        put(f"g{i}", 0, 4 * i + 4 - d, [f"f{i}", f"k{i}"])
        put(f"k{i}", 0, 8 * n + 4 * i + 7 - d, ["x"] + [f"g{j}" for j in range(i + 1, n + 1)])
        put(f"f{i}", 1, 8 * n + 4 * i + 9 - d, [f"e{i}"])
        put(f"h{i}", 1, 8 * n + 4 * i + 10 - d, [f"k{i}"])
    put("s", 0, 8 * n + 6, [f"f{j}" for j in range(1, n + 1)] + ["x"])
    put("r", 0, 8 * n + 8, [f"g{j}" for j in range(1, n + 1)] + ["x"])
    put("x", 1, 1, ["x"])
    iota = [None] * N
    iota[I["t1"]] = I["c"]
    for i in range(1, n + 1): iota[I[f"g{i}"]] = I[f"k{i}"]; iota[I[f"d{i}"]] = I["r"]; iota[I[f"k{i}"]] = I["x"]
    for i in range(2, 2 * n + 1): iota[I[f"t{i}"]] = I["r"]
    iota[I["c"]] = I["r"]; iota[I["s"]] = I["x"]; iota[I["r"]] = I["x"]
    assert all((iota[v] is not None) == (ow[v] == 0) for v in range(N))
    return dict(pr=pr, ow=ow, E=E), iota, names


def howard_gn(H, s0, C, sink):
    """I^loc / Howard on H from s0 with own S1; Claim NT counters at every state."""
    od = Order(H["pr"]); n = len(H["pr"]); s = list(s0); T = 0
    while True:
        sig = [s[v] if H["ow"][v] == 0 else None for v in range(n)]
        val, _ = s1(H["pr"], H["ow"], H["E"], sig, od); C["gn_states"] += 1
        if len(set(val)) != n: C["ntfail"] += 1
        if sink is not None and any(val[v][0] != sink for v in range(n)): C["sinkfail"] += 1
        ch = False
        for v in range(n):
            if H["ow"][v] != 0: continue
            mx = max(od.cmp(val[w], val[H["E"][v][0]]) for w in H["E"][v])
            bests = [w for w in H["E"][v] if all(od.cmp(val[w], val[u]) >= 0 for u in H["E"][v])]
            if len(bests) != 1: C["tiefail"] += 1
            if od.cmp(val[bests[0]], val[s[v]]) > 0: s[v] = max(bests); ch = True
        if not ch: return T
        T += 1


def main(a):
    global CTRL
    mode = "xi"; perm = False
    if "--mode" in a: mode = a[a.index("--mode") + 1]
    if "--perm" in a: perm = True
    if "--ctrl" in a: CTRL = a[a.index("--ctrl") + 1]
    C = defaultdict(int)
    if a[0] == "rand":
        cnt, seed, nmax = int(a[1]), int(a[2]), int(a[3]); rng = random.Random(seed); prng = random.Random(seed + 7) if perm else None
        for _ in range(cnt):
            H, s0 = rand_game(rng, nmax); run(H, s0, mode, C, prng)
    elif a[0] in ("gn", "wgn"):
        for n in range(1, int(a[1]) + 1):
            H, iota, names = gn(n, "--table4" in a); pr = H["pr"]; x = names.index("x")
            inj = len(set(pr)) == len(pr) and min(pr) == pr[x] and sorted(pr)[1] > pr[x]
            C["injfail"] += not inj
            if a[0] == "gn":
                Cn = defaultdict(int); T = howard_gn(H, iota, Cn, x)
                print(f"G_{n}: nodes {len(pr)} injective {int(inj)} max priority {max(pr)} T {T} 9*2^n-10 {9 * 2 ** n - 10} "
                      + " ".join(f"{k} {v}" for k, v in sorted(Cn.items())), flush=True)
                for k, v in Cn.items(): C[k] += v
            else:
                Cn = defaultdict(int); it, F, hm = run(H, iota, mode, Cn)
                Wn = build_W(H, iota)["n"]
                print(f"W(G_{n}, iota): |W| {Wn} mode {mode} iterations {it} F {F} H-steps {hm} "
                      + " ".join(f"{k} {v}" for k, v in sorted(Cn.items())), flush=True)
                for k, v in Cn.items(): C[k] += v
    elif a[0] == "ntrand":
        cnt, seed = int(a[1]), int(a[2]); rng = random.Random(seed)
        for _ in range(cnt):
            H, s0 = rand_game(rng, 8); howard_gn(H, [s0[v] for v in range(len(H["pr"]))], C, None)
    fails = ["s3fail", "nonstd", "e0fail", "nohoward", "fbwrong", "endwrong", "kconf", "odd5", "ntfail", "tiefail", "sinkfail", "injfail", "rem3"]
    print("TOTAL", " ".join(a), "FAILS", sum(C[k] for k in fails), "|", " ".join(f"{k} {C[k]}" for k in fails), "|",
          " ".join(f"{k} {v}" for k, v in sorted(C.items()) if k not in fails), flush=True)


if __name__ == "__main__":
    main(sys.argv[1:])
