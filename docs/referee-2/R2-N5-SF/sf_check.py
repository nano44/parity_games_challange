#!/usr/bin/env python3
r"""REFEREE-2 successor 20 (Opus 5.5, D15): own check of P-N5-SF (docs/new/P-N5-SF-box55.md, sha1 dbc2345f @ l-new 95a7a581).
N5-SF written here from the packet's §0 (S4a' / S4b': opponent = sigmabar(sigma) / taubar(tau); S4c with FIX 3 unchanged) on si.py (SPEC S1's
own implementation, read-only), mirroring my lane's R2-N5-DUAL/dual_check.Runner (N5), which is used for N5 itself (one-player steps,
WIN). The lane's n5sf.py / n5x.py / pcheck.py are NOT imported.
Checks (each must be 0):
  TERM   the run stops at I_sigma = I_tau = {}; every iteration changes sigma or tau; no sigma and no tau value recurs; I <= (#s-1) + (#t-1)
  ORB    distinct-sigma sequence == the orbit sigma_0, F(sigma_0), ... computed WITHOUT tau, ending at the first sigma with I_sigma = {};
         ORB2: a second run from (sigma_0, random tau_0') has the same distinct-sigma sequence. Mirror (F^d, tau_0, random sigma_0').
  OPa    at every sigma^(j), j < p: S1 on G_sbar (Odd cut to sbar(sigma)) gives Xi_sigma and I_sigma (mirror on G^d_tbar)
  OPb    F(sigma^(j)) == one N5 iteration (dual_check.Runner, cap 1) on G_sbar from (sigma^(j), sbar), restricted to sigma (mirror on G^d_tbar)
  SEG    every stretch [a, b] (sbar and lambda constant): b - a <= n + m, Xi-changing transitions <= n - 1; a fallback transition inside a
         stretch is its last and ends at p (FBLAST)
  BND    #s - 1 < (n+m+1)(1 + LAM + SBC) per side; LAM <= n(n-1); I < (n+m+1)(2(n^2-n+1) + SBC); SBC_side <= #side - 1; SBC <= 2 I
Data (counted, not violations): SEGsharp (stretches with b - a = n + m, i.e. Remark 1's sharper "< n + m" fails), WIN (N5-SF's final
lambda-parity regions == N5's from the same start), X_ORBN5 (runs where N5's own distinct-sigma sequence differs from N5-SF's: the variant
is a different algorithm), max SBC, LAM, stretch length.
Usage: sf_check.py random N nmin nmax seed [starts] | files list.txt [runs [prefix]]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-DUAL"))
import dual_check as DC
pg, Engine, dual = DC.pg, DC.Engine, DC.dual


class St:
    def __init__(s): s.c, s.mx = {}, {}
    def inc(s, k, d=1): s.c[k] = s.c.get(k, 0) + d
    def mxu(s, k, v):
        if v > s.mx.get(k, -1): s.mx[k] = v
    def bad(s, k, msg):
        s.inc(k)
        if s.c[k] <= 5: print("VIOLATION", k, msg, flush=True)


class Side:
    """one player's side: game X (G for Even, G^d for Odd), own owner 0 in X. Strategies are full-length lists."""
    def __init__(s, X):
        s.X, s.n, s.E = X, X.n, Engine(X); s.cache = {}
    def info(s, st):
        key = tuple(st[v] if s.X.owner[v] == 0 else -1 for v in range(s.n))
        if key not in s.cache:
            val, ch = s.E.evaluate(key)
            I = set(s.E.improving(tuple(st), val))
            opp = tuple(ch[v] if s.X.owner[v] == 1 else -1 for v in range(s.n))
            s.cache[key] = ([tuple(x) for x in val], I, opp)
        return s.cache[key]
    def arena_opt(s, st, I, opp):
        """S4a' on X: own v keeps {st(v)} + I-targets, opponent v keeps opp(v); own optimum = Odd's optimal counterstrategy in the dual."""
        X, n = s.X, s.n
        A = {v: {st[v]} for v in range(n) if X.owner[v] == 0}
        for v, w in I: A[v].add(w)
        succ = [sorted(A[v]) if X.owner[v] == 0 else [opp[v]] for v in range(n)]
        _, best = Engine(dual(pg.Game(list(X.prio), list(X.owner), succ))).evaluate(tuple(opp[v] if X.owner[v] == 1 else -1 for v in range(n)))
        return [best[v] if X.owner[v] == 0 else st[v] for v in range(n)]
    def fallback(s, st, val, I):
        new = list(st)
        for v in {v for v, _ in I}: new[v] = max((w for x, w in I if x == v), key=lambda w: (s.E.key(val[w]), w))
        return new
    def F(s, st):
        val, I, opp = s.info(st)
        if not I: return None
        a = s.arena_opt(st, I, opp)
        return a if own(s.X, a) != own(s.X, st) else s.fallback(st, val, I)


def own(X, st): return tuple(st[v] for v in range(X.n) if X.owner[v] == 0)


def run_sf(g, SE, SO, s, t, cap=200000):
    """N5-SF on G. SE on G (sigma), SO on G^d (tau). Returns states [(sigma, tau)] and fallback flags."""
    s, t = list(s), list(t); states, fbs = [(tuple(s), tuple(t))], []
    while len(fbs) < cap:
        vs, Is, sbar = SE.info(s); vt, It, tbar = SO.info(t)
        if not Is and not It: break
        ns = SE.arena_opt(s, Is, sbar) if Is else list(s)
        nt = SO.arena_opt(t, It, tbar) if It else list(t)
        fb = 0
        if own(SE.X, ns) == own(SE.X, s) and own(SO.X, nt) == own(SO.X, t):
            if Is: ns = SE.fallback(s, vs, Is); fb = 1
            else: nt = SO.fallback(t, vt, It); fb = 2
        s, t = ns, nt; states.append((tuple(s), tuple(t))); fbs.append(fb)
    return states, fbs


def dedup(seq):
    out = []
    for x in seq:
        if not out or out[-1] != x: out.append(x)
    return out


def side_checks(g, S, seq_full, fbflags, name, tag, st, n, m):
    """seq_full: the side's strategy at every state (full lists); fbflags[k]: this side fell back at transition k."""
    X = S.X; ownseq = [own(X, x) for x in seq_full]
    d = dedup(ownseq); p = len(d) - 1
    if len(set(d)) != len(d): st.bad("TERM", f"{name} {tag}: a strategy value recurs")
    # representatives (full lists) of each distinct value, and which transition produced it (fallback or not)
    reps, fbj = [seq_full[0]], []
    for k in range(1, len(seq_full)):
        if ownseq[k] != ownseq[k - 1]: reps.append(seq_full[k]); fbj.append(fbflags[k - 1])
    # ORB: tau-free orbit
    orb, x = [own(X, reps[0])], list(reps[0])
    while True:
        y = S.F(x)
        if y is None: break
        orb.append(own(X, y)); x = y
        if len(orb) > len(d) + 5: break
    st.inc(f"ORB_{tag}_checks")
    if orb != d: st.bad("ORB", f"{name} {tag}: orbit {len(orb)} vs run {len(d)}")
    if S.info(reps[-1])[1]: st.bad("TERM", f"{name} {tag}: last strategy still has improving edges")
    # OP, SEG, BND
    infos = [S.info(r) for r in reps]
    lam = [tuple(v[0] for v in inf[0]) for inf in infos]; sb = [inf[2] for inf in infos]
    for j in range(p):
        val, I, opp = infos[j]
        Gc = pg.Game(list(X.prio), list(X.owner), [list(X.succ[v]) if X.owner[v] == 0 else [opp[v]] for v in range(n)])
        Ec = Engine(Gc); vc, _ = Ec.evaluate(tuple(reps[j][v] if X.owner[v] == 0 else -1 for v in range(n)))
        st.inc(f"OP_{tag}_checks")
        if [tuple(z) for z in vc] != val or set(Ec.improving(tuple(reps[j]), vc)) != I: st.bad("OPa", f"{name} {tag} j={j}")
        states, _ = DC.Runner(Gc).run(list(reps[j]), list(opp), cap=1)
        if len(states) < 2 or own(X, states[1][0]) != d[j + 1]: st.bad("OPb", f"{name} {tag} j={j}")
    a = 0; S_ = 0
    for b in range(p + 1):
        if b == p or sb[b + 1] != sb[b] or lam[b + 1] != lam[b]:
            S_ += 1; L = b - a; st.mxu(f"maxstretch_{tag}", L); st.inc(f"stretches_{tag}")
            if L > n + m: st.bad("SEG", f"{name} {tag} stretch {a}-{b} len {L} > n+m")
            if L == n + m: st.inc("SEGsharp")
            if L > n - 1: st.inc("X_SEGn1")   # control: a stretch longer than n - 1 (the m term is used)
            vch = sum(infos[j + 1][0] != infos[j][0] for j in range(a, b))
            if vch > n - 1: st.bad("SEG", f"{name} {tag} stretch {a}-{b}: {vch} value changes")
            for j in range(a, b):
                if fbj[j] and (j + 1 != b or b != p): st.bad("FBLAST", f"{name} {tag} fallback at {j} in stretch {a}-{b}, p={p}")
            a = b + 1
    SBC = sum(sb[j + 1] != sb[j] for j in range(p)); LAM = sum(lam[j + 1] != lam[j] for j in range(p))
    st.mxu(f"maxSBC_{tag}", SBC); st.mxu(f"maxLAM_{tag}", LAM)
    if not (p < (n + m + 1) * (1 + LAM + SBC)) or LAM > n * (n - 1) or SBC > p: st.bad("BND", f"{name} {tag} p={p} LAM={LAM} SBC={SBC}")
    return p, SBC, d


def run_game(g, s, t, st, name, rng):
    n = g.n; m = sum(len(x) for x in g.succ)
    SE, SO = Side(g), Side(dual(g))
    states, fbs = run_sf(g, SE, SO, s, t)
    I = len(states) - 1; st.inc("runs"); st.inc("iterations", I); st.mxu("maxI", I)
    if SE.info(list(states[-1][0]))[1] or SO.info(list(states[-1][1]))[1]: st.bad("TERM", f"{name}: stopped with improving edges")
    for k in range(I):
        if own(g, states[k][0]) == own(g, states[k + 1][0]) and own(SO.X, states[k][1]) == own(SO.X, states[k + 1][1]): st.bad("TERM", f"{name}@{k}: no change")
    st.inc("fallbacks_E", sum(f == 1 for f in fbs)); st.inc("fallbacks_O", sum(f == 2 for f in fbs))
    pE, sE, dE = side_checks(g, SE, [x for x, _ in states], [f == 1 for f in fbs], name, "E", st, n, m)
    pO, sO, dO = side_checks(g, SO, [y for _, y in states], [f == 2 for f in fbs], name, "O", st, n, m)
    if I > pE + pO: st.bad("TERM", f"{name}: I {I} > {pE} + {pO}")
    SBC = sE + sO
    if not (I < (n + m + 1) * (2 * (n * n - n + 1) + SBC)) or SBC > 2 * I: st.bad("BND", f"{name}: I {I} SBC {SBC}")
    # ORB2: other tau_0 (resp. sigma_0)
    t2 = [rng.choice(g.succ[v]) for v in range(n)]; s2 = [rng.choice(g.succ[v]) for v in range(n)]
    st2, _ = run_sf(g, SE, SO, s, t2); st3, _ = run_sf(g, SE, SO, s2, t)
    st.inc("ORB2_checks")
    if dedup([own(g, x) for x, _ in st2]) != dE: st.bad("ORB2", f"{name}: sigma sequence depends on tau_0")
    if dedup([own(SO.X, y) for _, y in st3]) != dO: st.bad("ORB2", f"{name}: tau sequence depends on sigma_0")
    # data: N5 vs N5-SF
    n5s, _ = DC.Runner(g).run(list(s), list(t))
    if dedup([own(g, x) for x, _ in n5s]) != dE: st.inc("X_ORBN5")
    lamSF = tuple(v[0] for v in SE.info(list(states[-1][0]))[0]); lamN5 = tuple(v[0] for v in SE.info(list(n5s[-1][0]))[0])
    st.inc("WIN_checks")
    if [g.prio[c] % 2 for c in lamSF] != [g.prio[c] % 2 for c in lamN5]: st.bad("WIN", f"{name}: regions differ from N5")


def main():
    st = St(); a = sys.argv[1:]; rng = random.Random(5555)
    if a[0] == "random":
        N, nmin, nmax, seed = map(int, a[1:5]); ns = int(a[5]) if len(a) > 5 else 2; rng = random.Random(seed)
        for i in range(N):
            g = DC.rand_game(rng, rng.randint(nmin, nmax), "kO")
            for r in range(ns + 1):
                if r == 0: s, t = Engine(g).initial("best"), Engine(dual(g)).initial("best")
                else: s, t = [rng.choice(g.succ[v]) for v in range(g.n)], [rng.choice(g.succ[v]) for v in range(g.n)]
                run_game(g, list(s), list(t), st, f"rand{seed}:{i}#{r}", rng)
    elif a[0] == "files":
        runs = int(a[2]) if len(a) > 2 else 2; pre = a[3] if len(a) > 3 else ""
        for line in [l.split() for l in open(a[1]) if l.strip()]:
            g = pg.read(os.path.join(DC.ROOT, pre + line[0]))
            if len(line) > 1:
                # partial start files: unlisted vertices take the S3 best-reward start (the convention of the packet's pinned check)
                s, t = list(Engine(g).initial("best")), list(Engine(dual(g)).initial("best"))
                for l2 in open(os.path.join(DC.ROOT, pre + line[1])):
                    ps = l2.split()
                    if ps and ps[0] in ("SIGMA0", "TAU0"):
                        for kv in ps[1:]:
                            v, w = map(int, kv.split(":")); (s if ps[0] == "SIGMA0" else t)[v] = w
                if all((s if g.owner[v] == 0 else t)[v] in g.succ[v] for v in range(g.n)):
                    st.inc("starts_valid"); run_game(g, list(s), list(t), st, f"{line[0]}#start", rng)
                else: st.inc("starts_INVALID_skipped")
            for r in range(runs):
                if r == 0: s, t = Engine(g).initial("best"), Engine(dual(g)).initial("best")
                else: s, t = [rng.choice(g.succ[v]) for v in range(g.n)], [rng.choice(g.succ[v]) for v in range(g.n)]
                run_game(g, list(s), list(t), st, f"{line[0]}#{r}", rng)
    print("MODE", " ".join(a))
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"max {k}: {st.mx[k]}")
    bad = sum(st.c.get(k, 0) for k in ("TERM", "ORB", "ORB2", "OPa", "OPb", "SEG", "FBLAST", "BND", "WIN"))
    print("RESULT", "PASS" if bad == 0 else "FAIL", "violations", bad)


if __name__ == "__main__":
    main()
