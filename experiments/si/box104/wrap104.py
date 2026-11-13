#!/usr/bin/env python3
"""L-SI box 104: the W-FLAT WRAPPER W(H, s0) of an arbitrary parity game H and a positional Even strategy s0 (docs/si/box104-map.md §5).
W keeps H's vertices (same indices and owners, priorities + 6) and replaces every edge by a path of 6 edges:
  Even edge v -> w :  v -> m (pad, 2 if w = s0(v) else 0) -> g (ODD gate, 1) -> { pe (pad, 1) -> c_W ;  pbeta (pad, 0) -> b }
  Odd  edge o -> w :  o -> x1 -> x2 -> x3 (pads, 0) -> b
  valve b (Even, 0) -> { y (pad, 2) -> w ;  pb (pad, 1) -> K0 }
  every Odd vertex o of H gets one more edge  o -> pe_o (pad, 1) -> c_W
  c_W: even self-loop of priority top (above every vertex of H); the core K0 (top + 2), K1 (5), K2 (Odd, 3), K3 (top + 3) with the
  pads pA, s, q, r exactly as in R117's Gamma3.
All pads are single-successor Even vertices of priority <= 2. S3 (SPEC FIX 1) picks: s0 at H's Even vertices, pe at every gate and at
every Odd vertex of H (tau0), y at every valve, the core config (pA, s, K2), K2 -> K2: the STANDARD state of s0.
Claim tested (Lemma WRAP): N5'-xi from S3 on W(H, s0) is, at H's Even vertices, a Howard (VJ switch-best) run of H from s0 until its
first fallback at T + 1 (T = the first state at which no Even vertex of H has a strictly better successor in H), and stops after
exactly T + 3 iterations with one fallback.
Must-0 counters (per game): s3fail, nonstd (unit states before the first fallback), nohoward (unit (step, Even vertex of H): the new
successor is not a best successor BY H'S OWN VALUATION (si.Engine on H), or a best current one was left), fbwrong, endwrong, wrong
(regions of W against harness Zielonka on W). CTRL=1: best := worst (nohoward must fire). CTRL=2: T := T + 1.
Usage: wrap104.py rand SEED COUNT NMAX      random games (harness gen.random_game), s0 = a random Even strategy
       wrap104.py fried n...               H = PGSolver switchallexp_n, s0 = best-reward start; compares with fried.howard's T
       wrap104.py xck n... | xcklmcs VER n...  W(switchallexp_n) | W(G_n, iota): engine 1 (n5v.py xi) against engine 2 (n5bxi.py), Zielonka, verify
       wrap104.py ties n...                on Howard's run of switchallexp_n itself (fried.howard): tie events = (state, Even vertex)
                                           pairs at which the current successor is not best and two or more successors are best
       wrap104.py lmcs VER n...            H = G_n of Friedmann, arXiv 1106.0778v2 (LMCS 7(3:19)), s0 = iota_{G_n}. VER fig4: the INJECTIVE
                                           priorities of the paper's Figure 4 and Fact 6.1 (d_i 4i-1, e_i 4i, g_i 4i+2, k_i 8n+4i+5,
                                           f_i 8n+4i+7, h_i 8n+4i+8; L-LIT T66 Addendum D, claude/l-lit 9ae31ec3); VER table4: Table 4
                                           as printed (those six 2 higher; then pr(g_n) = pr(a_1)). Graph, owners, iota and the other
                                           priorities: L-LIT's transcription (env LLIT: claude/l-lit 5c53efbd docs/lit/T66-depth-check.py,
                                           function lmcs, read-only). Howard's T and its tie events by this file's own howard().
       wrap104.py pg n OUT.pg              write W(switchallexp_n);   wrap104.py pglmcs VER n OUT.pg   write W(G_n, iota)
       wrap104.py dumprand SEED COUNT NMAX OUT.json   freeze the random games of «rand» (H, s0, T, iterations, |W|) as JSON
       wrap104.py json FILE.json           re-run the six counters on a frozen list;   wrap104.py pgjson FILE.json I OUT.pg   write its I-th W
(env LNEW, LRED as free104.py; ALG=spec runs N5 instead: nohoward, fbwrong are then not tested and endwrong := not (1 fallback, F + 2))"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import free104 as F
import pg, n5v, n5, n5x, gen, zielonka
from si import Engine
CTRL = int(os.environ.get("CTRL", "0")); ALG = os.environ.get("ALG", "xi")

def wrap(H, s0):
    n = H.n; prio = [p + 6 for p in H.prio]; own = list(H.owner); succ = [None] * n; std_s = {}; std_t = {}; mp = {}
    def new(p, o, s=None): prio.append(p); own.append(o); succ.append(s); return len(prio) - 1
    cW = new(0, 0); succ[cW] = [cW]; K = [new(0, 0) for _ in range(4)]; own[K[2]] = 1
    pA = new(0, 0, [K[3]]); s_ = new(0, 0, [K[1]]); q = new(1, 0, [K[0]]); r = new(0, 0, [K[1]])
    succ[K[0]] = [K[1], pA]; succ[K[1]] = [q, s_]; succ[K[2]] = [r, K[2]]; succ[K[3]] = [K[1], K[2]]
    std_s[K[0]] = pA; std_s[K[1]] = s_; std_s[K[3]] = K[2]; std_t[K[2]] = K[2]
    def valve(w):
        pb = new(1, 0, [K[0]]); y = new(2, 0, [w]); b = new(0, 0, [y, pb]); std_s[b] = y; return b
    for v in range(n):
        out = []
        if H.owner[v] == 0:
            for w in H.succ[v]:
                b = valve(w); pbeta = new(0, 0, [b]); pe = new(1, 0, [cW]); g = new(1, 1, [pe, pbeta]); std_t[g] = pe
                m = new(2 if w == s0[v] else 0, 0, [g]); mp[(v, w)] = m; out.append(m)
        else:
            for w in H.succ[v]:
                b = valve(w); x3 = new(0, 0, [b]); x2 = new(0, 0, [x3]); x1 = new(0, 0, [x2]); out.append(x1)
            pe = new(1, 0, [cW]); out.append(pe); std_t[v] = pe
        succ[v] = out
    top = max(prio) + 2; top += top % 2
    prio[cW] = top; prio[K[0]], prio[K[1]], prio[K[2]], prio[K[3]] = top + 2, 5, 3, top + 3
    inv = {m: w for (v, w), m in mp.items()}
    return pg.Game(prio, own, [sorted(s) for s in succ]), std_s, std_t, mp, inv

def check(H, s0):
    """runs N5'-xi (or N5) from S3 on W(H, s0); returns (counters, T, iterations, |W|)"""
    g, std_s, std_t, mp, inv = wrap(H, s0); E, Ed = Engine(g), Engine(n5.dual(g)); EH = Engine(H); n = H.n
    ev = [v for v in range(n) if H.owner[v] == 0]
    sigma, tau = n5x.start_pair(g, E, Ed, None); c = dict(s3fail=0, nonstd=0, nohoward=0, fbwrong=0, endwrong=0, wrong=0)
    c["s3fail"] = int(any(sigma[v] != mp[(v, s0[v])] for v in ev) or any(sigma[v] != w for v, w in std_s.items()) or any(tau[v] != w for v, w in std_t.items()))
    its = 0; fbs = 0; F1 = None; T = None
    while its < 10 ** 6:
        if F1 is None:
            sH = tuple(inv[sigma[v]] if H.owner[v] == 0 else -1 for v in range(n)); vs, _ = EH.evaluate(sH); key = lambda w: EH.key(vs[w])
            c["nonstd"] += int(any(sigma[v] != w for v, w in std_s.items()) or any(tau[v] != w for v, w in std_t.items()))
            if T is None and not any(key(w) > key(sH[v]) for v in ev for w in H.succ[v]): T = its
        r = n5v.step(g, E, Ed, sigma, tau, ALG)
        if r is None: break
        ns, nt, _, _, fb = r; its += 1; fbs += fb
        if fb and F1 is None: F1 = its
        if F1 is None and ALG == "xi":
            for v in ev:
                ref = (min if CTRL == 1 else max)(key(w) for w in H.succ[v]); nw = inv[ns[v]]
                c["nohoward"] += int(key(nw) != ref or (key(sH[v]) == ref and nw != sH[v]))
        sigma, tau = ns, nt
    if T is None: T = -1
    if CTRL == 2: T += 1
    if ALG == "xi": c["fbwrong"] = int(F1 != T + 1); c["endwrong"] = int(fbs != 1 or its != T + 3)
    else: c["endwrong"] = int(fbs != 1 or F1 is None or its != F1 + 2); T = F1 if F1 is not None else -1
    vs, _ = E.evaluate(tuple(sigma)); win = [0 if g.prio[vs[v][0]] % 2 == 0 else 1 for v in range(g.n)]
    c["wrong"] = int(win != zielonka.solve(g))
    return c, T, its, g.n

def howard(H, s0):
    """Howard (VJ switch-best) on H from s0: every Even vertex to a best successor, keeping a best current one, else the larger index
    (fried.howard's rule). Returns (T, tie events)."""
    EH = Engine(H); s = tuple(s0[v] if H.owner[v] == 0 else -1 for v in range(H.n)); T = 0; ties = 0
    while True:
        vs, _ = EH.evaluate(s); key = lambda w: EH.key(vs[w])
        for v in range(H.n):
            if H.owner[v] == 0:
                ks = [key(w) for w in H.succ[v]]; ties += (key(s[v]) != max(ks) and ks.count(max(ks)) >= 2)
        ns = tuple(max(H.succ[v], key=lambda w: (key(w), w == s[v], w)) if H.owner[v] == 0 else -1 for v in range(H.n))
        if ns == s: return T, ties
        s = ns; T += 1

def lmcs_game(n, ver="fig4"):
    import importlib.util
    spec = importlib.util.spec_from_file_location("t66", os.path.join(os.environ["LLIT"], "docs/lit/T66-depth-check.py")); t66 = importlib.util.module_from_spec(spec)
    sys.argv, keep = [sys.argv[0]], sys.argv
    try: spec.loader.exec_module(t66)
    finally: sys.argv = keep
    g, start, names = t66.lmcs(n); prio = list(g.prio)
    if ver == "fig4":
        for v, nm in enumerate(names):
            if nm[0] in "degkfh": prio[v] -= 2
        assert len(set(prio)) == g.n and max(prio) == 12 * n + 8          # injective; Fact 6.1's highest priority
    else: assert ver == "table4" and len(set(prio)) == g.n - 1 and max(prio) == 12 * n + 10
    return pg.Game(prio, list(g.owner), [list(x) for x in g.succ]), list(start)

def rand_games(seed, cnt, nmax):
    rng = random.Random(seed)
    for i in range(cnt):
        n = rng.randint(2, nmax); H = gen.random_game(n, rng.randint(1, n + 1), 1, min(n, 4), rng.randrange(10 ** 9))
        yield H, [rng.choice(H.succ[v]) if H.owner[v] == 0 else -1 for v in range(n)]

def fried_game(n):
    V = F.fried.game(n); H = pg.Game([v[1] for v in V], [v[2] for v in V], [v[3] for v in V])
    s0 = [max(v[3], key=lambda w: (F.fried.rew(V[w][1]), w)) if v[2] == 0 else -1 for v in V]; T, _ = F.fried.howard(V)
    return H, s0, T

if __name__ == "__main__":
    lab = "T" if ALG == "xi" else "F"
    if sys.argv[1] == "rand":
        seed, cnt, nmax = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
        tot = dict(s3fail=0, nonstd=0, nohoward=0, fbwrong=0, endwrong=0, wrong=0); mT = 0; sT = 0; mn = 0
        for H, s0 in rand_games(seed, cnt, nmax):
            c, T, its, wn = check(H, s0)
            for k in tot: tot[k] += c[k]
            mT = max(mT, T); sT += T; mn = max(mn, wn)
        print(f"WRAP104 alg {ALG} rand seed {seed} games {cnt} n<={nmax}{' CTRL ' + str(CTRL) if CTRL else ''}: " + " ".join(f"{k} {v}" for k, v in tot.items())
              + f" | max {lab} {mT} sum {lab} {sT} max |W| {mn}", flush=True)
    elif sys.argv[1] == "fried":
        for n in map(int, sys.argv[2:]):
            H, s0, TH = fried_game(n); c, T, its, wn = check(H, s0)
            print(f"WRAP104 alg {ALG} switchallexp n {n}: |H| {H.n} m {sum(len(s) for s in H.succ)} Howard T (fried.howard) {TH} | |W| {wn} | {lab} {T} iterations {its} | "
                  f"iterations - Howard T = {its - TH} | " + " ".join(f"{k} {v}" for k, v in c.items()), flush=True)
    elif sys.argv[1] in ("xck", "xcklmcs"):
        import n5bxi, verify
        for n in map(int, sys.argv[2 if sys.argv[1] == "xck" else 3:]):
            if sys.argv[1] == "xck": H, s0, TH = fried_game(n)
            else: H, s0 = lmcs_game(n, sys.argv[2]); TH = howard(H, s0)[0]
            g = wrap(H, s0)[0]
            st, fb1, E = n5v.run(g, "xi"); w1, s1 = n5v.solution(g, st, E); w2, s2, it2, fb2 = n5bxi.N5xi(g, mode="spec").run()
            ref = zielonka.solve(g); s1w = [s1[v] if w1[v] == g.owner[v] else None for v in range(g.n)]
            e1, e2 = verify.check(g, w1, s1w), verify.check(g, w2, s2)
            ok = (len(st) - 1, fb1, w1) == (it2, fb2, w2) and w1 == ref and not e1 and not e2
            print(f"WXCK104 {'switchallexp' if sys.argv[1] == 'xck' else 'lmcs ' + sys.argv[2]} n {n}: Howard T {TH}; |W| {g.n}; impl1 iterations {len(st) - 1} fallbacks {fb1}; impl2 iterations {it2} fallbacks {fb2}; regions equal "
                  f"{w1 == w2}; vs Zielonka {w1 == ref}/{w2 == ref}; verify errors {len(e1)}/{len(e2)}; {'AGREE+CORRECT' if ok else 'MISMATCH'}", flush=True)
    elif sys.argv[1] == "ties":
        for n in map(int, sys.argv[2:]):
            V = F.fried.game(n); H = pg.Game([v[1] for v in V], [v[2] for v in V], [v[3] for v in V]); EH = Engine(H); T, traj = F.fried.howard(V)
            ties = 0; sw = 0
            for s in traj[:-1]:
                vs, _ = EH.evaluate(s)
                for v in range(H.n):
                    if H.owner[v]: continue
                    ks = [EH.key(vs[w]) for w in H.succ[v]]; b = max(ks)
                    if EH.key(vs[s[v]]) != b: sw += 1; ties += ks.count(b) >= 2
            print(f"TIES104 switchallexp n {n}: Howard T {T}; switches {sw}; tie events {ties}", flush=True)
    elif sys.argv[1] in ("dumprand", "json", "pgjson"):
        import json
        if sys.argv[1] == "dumprand":
            L = []
            for H, s0 in rand_games(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])):
                c, T, its, wn = check(H, s0); assert not any(c.values())
                L.append(dict(prio=list(H.prio), owner=list(H.owner), succ=[list(x) for x in H.succ], s0=list(s0), T=T, iterations=its, W=wn))
            json.dump(dict(seed=int(sys.argv[2]), nmax=int(sys.argv[4]), alg=ALG, games=L), open(sys.argv[5], "w")); print(f"WRAP104 dumprand: {len(L)} games written")
        else:
            D = json.load(open(sys.argv[2])); L = D["games"]
            if sys.argv[1] == "pgjson":
                d = L[int(sys.argv[3])]; pg.write(wrap(pg.Game(d["prio"], d["owner"], d["succ"]), d["s0"])[0], sys.argv[4])
            else:
                tot = dict(s3fail=0, nonstd=0, nohoward=0, fbwrong=0, endwrong=0, wrong=0); diff = 0
                for d in L:
                    c, T, its, wn = check(pg.Game(d["prio"], d["owner"], d["succ"]), d["s0"]); diff += (T, its, wn) != (d["T"], d["iterations"], d["W"])
                    for k in tot: tot[k] += c[k]
                print(f"WRAP104 alg {ALG} json {os.path.basename(sys.argv[2])} games {len(L)}: " + " ".join(f"{k} {v}" for k, v in tot.items()) + f" | rows differing from the frozen (T, iterations, |W|) {diff}", flush=True)
    elif sys.argv[1] == "lmcs":
        ver = sys.argv[2]
        for n in map(int, sys.argv[3:]):
            H, s0 = lmcs_game(n, ver); TH, ties = howard(H, s0); c, T, its, wn = check(H, s0)
            m = sum(len(x) for x in H.succ); f61 = H.n == 10 * n + 4 and 2 * m == 3 * n * n + 41 * n + 10   # Fact 6.1's highest priority 12n + 8 is Figure 4's, not Table 4's
            print(f"WRAP104 alg {ALG} lmcs {ver} n {n}: |H| {H.n} m {m} Fact 6.1 (nodes, edges) {f61} maxprio {max(H.prio)} distinct priorities {len(set(H.prio))} | Howard T (own howard) {TH} tie events {ties} | |W| {wn} | "
                  f"{lab} {T} iterations {its} | iterations - Howard T = {its - TH} | 2^n = {2 ** n} | " + " ".join(f"{k} {v}" for k, v in c.items()), flush=True)
    elif sys.argv[1] == "pglmcs":
        H, s0 = lmcs_game(int(sys.argv[3]), sys.argv[2]); pg.write(wrap(H, s0)[0], sys.argv[4])
    elif sys.argv[1] == "pg":
        H, s0, TH = fried_game(int(sys.argv[2])); pg.write(wrap(H, s0)[0], sys.argv[3])
