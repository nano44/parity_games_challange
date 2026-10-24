#!/usr/bin/env python3
"""REFEREE probe for packet P-N5-U1 (docs/new/P-N5-U1-box31.md, pin eee0d8a, sha1 eb90788d...). Own N5 trace (the n5.py loop, recorded;
asserted equal to n5.run's iteration/fallback counts); W from the play of (sigma, tau) by Engine on the game with Odd fixed to tau.
Phase = (lambda_Xi, lambda_U, tau) constant; crossing-free interval = maximal run of a phase with R constant.
Checks (all from the packet's definitions, written independently of experiments/new/box31/):
 TBc   every S4a transition (any game), every Even v not its own W'-cycle node: sigma'(v) is the key-min over the TIED arena
       successors (ext(v, W'(z)) == W'(v)); key = index if c = lambda_W'(v) odd, else root-first sequence of z's sigma'-play to c
 TB    the packet's statements: v switches, W'(v) = W(v), not own cycle node: c odd => sigma'(v) < sigma(v);
       c even and W' = W on v's sigma-play before c => pk'(v) <lex pk(v)
 R1    on route-form pieces: Xi(v) = pi_v (+) theta, W(v) = pi_v (+) w for v in R
 CASC  W-flat runs of route-form pieces: a switching R-vertex of level l switches only at run steps <= l - 2
 C1    W-flat transitions of a piece: W unchanged also on o's W-continuation into F (TB's hypothesis on the whole play)
 U1    U1 pieces (rank c_w > rank c_theta): kappa_w freeze index <= |R|; #transitions changing Xi, W or sigma on R <= bound(|R|, f);
       W non-decreasing on R at non-fallback transitions
 WC    intervals with not H2: w = (c_w, {}, d), d <= |R| - 1; #w-changes <= (f + 1)(|R|^2 - 1) + f
Every game is asserted to be in C^1O (exactly one Odd vertex with out-degree > 1) before use.
Usage: u1_probe.py game.pg [game.pg ...] | u1_probe.py rand N nmin nmax seed"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
for p in ("experiments/new", "experiments/si", "experiments/harness"): sys.path.insert(0, os.path.join(ROOT, p))
import pg, n5
from si import Engine

def dual(h): return pg.Game([p + 1 for p in h.prio], [1 - o for o in h.owner], [list(s) for s in h.succ])

def load(path): return pg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%")))

def assert_c1o(g):
    ch = [v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1]
    assert len(ch) == 1, "not in C^1O: exactly one Odd choice vertex required (found %d)" % len(ch)
    return ch[0]

def trace(g):
    """The n5.py mode-n5 loop, recorded. Returns list of (sigma, tau, fb_flag_of_transition_out, Is)."""
    n = g.n; E, Ed = Engine(g), Engine(dual(g))
    sigma, tau = list(E.initial("best")), list(Ed.initial("best")); out = []; it = fb = 0
    while True:
        vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
        vt, tbar = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
        out.append([tuple(sigma), tuple(tau), 0, Is, bool(Is)])
        if not Is and not It: break
        it += 1; ns, nt = list(sigma), list(tau)
        if Is:
            opt = {v: {sigma[v]} for v in range(n) if g.owner[v] == 0}
            for v, w in Is: opt[v].add(w)
            succ = [sorted(opt[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)]
            Er = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ)))
            _, best = Er.evaluate(tuple(tau[v] if g.owner[v] == 1 else -1 for v in range(n)))
            for v in range(n):
                if g.owner[v] == 0: ns[v] = best[v]
        if It:
            opt = {v: {tau[v]} for v in range(n) if g.owner[v] == 1}
            for v, w in It: opt[v].add(w)
            succ = [sorted(opt[v]) if g.owner[v] == 1 else [sigma[v]] for v in range(n)]
            Er = Engine(pg.Game(list(g.prio), list(g.owner), succ))
            _, best = Er.evaluate(tuple(sigma[v] if g.owner[v] == 0 else -1 for v in range(n)))
            for v in range(n):
                if g.owner[v] == 1: nt[v] = best[v]
        if ns == sigma and nt == tau:
            fb += 1; out[-1][2] = 1
            if Is:
                for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
            else:
                for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
        sigma, tau = ns, nt
    r = n5.run(g, "n5")
    assert (r[0], r[1]) == (it, fb), ("trace differs from n5.run", r[:2], (it, fb))
    return E, Ed, out, it, fb

def wval(g, E, s, t):
    """valuation of the play of (s, t) in g (Engine on g with Odd fixed to t)."""
    h = pg.Game(list(g.prio), list(g.owner), [list(g.succ[v]) if g.owner[v] == 0 else [t[v]] for v in range(g.n)])
    Eh = Engine(h); val, _ = Eh.evaluate(tuple(s[v] if g.owner[v] == 0 else -1 for v in range(g.n)))
    return val

def nxt_of(g, s, t): return [s[v] if g.owner[v] == 0 else t[v] for v in range(g.n)]

def play_to(nx, v, c):
    """vertices of the play from v up to (excluding) the first visit of c; None if c is never reached"""
    p, seen = [], set()
    while v != c:
        if v in seen: return None
        seen.add(v); p.append(v); v = nx[v]
    return p

def reaches(nx, v, o):
    seen = set()
    while v not in seen:
        if v == o: return True
        seen.add(v); v = nx[v]
    return False

def returns(nx, o):
    x, seen = nx[o], set()
    while x not in seen:
        if x == o: return True
        seen.add(x); x = nx[x]
    return False

def lam_key(E, val): return E.key(val)

def check_tb(g, E, s, s1, t, Is, cnt):
    """TB and TBc at an S4a transition s -> s1 (tau = t)."""
    n = g.n; W = wval(g, E, s, t); W1 = wval(g, E, s1, t); nx, nx1 = nxt_of(g, s, t), nxt_of(g, s1, t)
    arena = {v: {s[v]} for v in range(n) if g.owner[v] == 0}
    for v, w in Is: arena[v].add(w)
    for v in range(n):
        if g.owner[v] != 0: continue
        c = W1[v][0]
        if c == v: continue
        tied = [z for z in arena[v] if E.extend(v, W1[z]) == W1[v]]
        cnt["TBc_cases"] += 1
        if s1[v] not in tied: cnt["TBc_choice_not_tied_FAIL"] += 1; continue
        if E.par[c] == 1: best = min(tied)
        else:
            def key(z):
                p = play_to(nx1, z, c); return tuple(reversed(p))
            best = min(tied, key=key)
        if best != s1[v]: cnt["TBc_FAIL"] += 1
        # the packet's TB statements
        if s1[v] != s[v] and W1[v] == W[v] and W[v][0] != v:
            c = W[v][0]
            if E.par[c] == 1:
                cnt["TB_odd"] += 1
                if not s1[v] < s[v]: cnt["TB_odd_FAIL"] += 1
            else:
                p0 = play_to(nx, v, c)
                if all(W1[x] == W[x] for x in p0):
                    cnt["TB_even"] += 1
                    p1 = play_to(nx1, v, c)
                    if not (len(p1) == len(p0) and tuple(reversed(p1)) < tuple(reversed(p0))): cnt["TB_even_FAIL"] += 1

def states(g, E, Ed, out, o):
    rows = []
    for (s, t, fb, Is, s4a) in out:
        Xi, sb = E.evaluate(s); U, _ = Ed.evaluate(t); W = wval(g, E, s, t)
        nx = nxt_of(g, s, t); hn = [s[v] if g.owner[v] == 0 else sb[v] for v in range(g.n)]
        R = frozenset(v for v in range(g.n) if reaches(nx, v, o))
        H1, H2 = not returns(hn, o), not returns(nx, o)
        rows.append(dict(s=s, t=t, fb=fb, Is=Is, Xi=Xi, W=W, nx=nx, R=R, H1=H1, H2=H2,
                         Xk=tuple(E.key(x) for x in Xi), Wk=tuple(E.key(x) for x in W),
                         ph=(tuple(x[0] for x in Xi), tuple(x[0] for x in U), t)))
    return rows

def u1bound(r, f):
    K = (f + 1) * (r - 1) * (r - 2)
    return r + f + K + (K + f + 1) * (r - 2)

def run(g, cnt, name=None):
    o = assert_c1o(g); E, Ed, out, it, fb = trace(g); n = g.n
    cnt["runs"] += 1; cnt["iterations"] += it; cnt["fallbacks"] += fb
    for k in range(len(out) - 1):
        if out[k][4] and not out[k][2]:
            check_tb(g, E, out[k][0], out[k + 1][0], out[k][1], out[k][3], cnt)
    rows = states(g, E, Ed, out, o)
    a = 0
    for i in range(1, len(rows) + 1):
        if i == len(rows) or rows[i]["ph"] != rows[a]["ph"] or rows[i]["R"] != rows[a]["R"]:
            interval(g, E, o, rows[a:i], cnt, name); a = i

def interval(g, E, o, I, cnt, name):
    R = I[0]["R"]; L = len(I) - 1
    cnt["intervals"] += 1
    if not I[0]["H2"]:
        cnt["WC_intervals"] += 1
        f = sum(I[k]["fb"] for k in range(L)); wc = sum(I[k]["Wk"][o] != I[k + 1]["Wk"][o] for k in range(L))
        for r in I:
            cw, P, d = r["W"][o]
            if P != 0 or d > len(R) - 1 or cw not in R: cnt["WC_shape_FAIL"] += 1
        cnt["WC_max"] = max(cnt["WC_max"], wc)
        if wc > (f + 1) * (len(R) ** 2 - 1) + f: cnt["WC_FAIL"] += 1
    rform = lambda r: (r["H1"] or r["Xi"][o][0] == o) and (r["H2"] or r["W"][o][0] == o)
    k = 0
    while k <= L:
        if not rform(I[k]): k += 1; continue
        j = k
        while j < L and rform(I[j + 1]) and I[j + 1]["Xk"][o] == I[k]["Xk"][o] and I[j + 1]["Wk"][o] == I[k]["Wk"][o]: j += 1
        piece(g, E, o, I[k:j + 1], R, cnt, name)
        k = j + 1

def piece(g, E, o, J, R, cnt, name):
    n = g.n; ct, cw = J[0]["Xi"][o][0], J[0]["W"][o][0]; th, w = J[0]["Xi"][o], J[0]["W"][o]
    u1 = E.rank[cw] > E.rank[ct]
    cnt["pieces"] += 1; cnt["U1_pieces"] += u1
    Rl = [v for v in R if v != o]
    rt = [{v: play_to(r["nx"], v, o) for v in Rl} for r in J]
    def ext(route, val):
        for x in reversed(route): val = E.extend(x, val)
        return val
    for i, r in enumerate(J):
        for v in Rl:
            if ext(rt[i][v], th) != r["Xi"][v] or ext(rt[i][v], w) != r["W"][v]: cnt["R1_FAIL"] += 1
    T = len(J) - 1                                     # transitions of J: i -> i+1, both in J
    # W-flat runs and CASC
    flat = [not J[i]["fb"] and all(J[i]["W"][v] == J[i + 1]["W"][v] for v in R) for i in range(T)]
    i = 0
    while i < T:
        if not flat[i]: i += 1; continue
        j = i
        while j < T and flat[j]: j += 1
        cnt["Wflat_runs"] += 1; cnt["Wflat_maxlen"] = max(cnt["Wflat_maxlen"], j - i)
        per = Counter()
        for st in range(i, j):
            a, b = J[st], J[st + 1]
            # C1: o's W-continuation (F part) unchanged
            if J[st]["H2"]:
                p = play_to(a["nx"], a["nx"][o], cw)
                if p is not None and any(a["W"][x] != b["W"][x] for x in p): cnt["C1_FAIL"] += 1
            for v in Rl:
                if a["s"][v] != b["s"][v] if g.owner[v] == 0 else False:
                    lv = len(rt[st][v]); per[v] += 1; cnt["CASC_switches"] += 1
                    if st - i > lv - 2: cnt["CASC_FAIL"] += 1; cnt["CASC_FAIL_" + str(name)] += 1
        if per: cnt["CASC_max_per_vertex"] = max(cnt["CASC_max_per_vertex"], max(per.values()))
        i = j
    if not u1: return
    # U1: freeze, count, W monotone
    top = E.rank[cw]
    kap = [{v: frozenset(u for u in rt[i][v] if E.rank[u] > top) for v in Rl} for i in range(len(J))]
    last = max([i for i in range(1, len(J)) if kap[i] != kap[i - 1]], default=0)
    cnt["U1_max_freeze"] = max(cnt["U1_max_freeze"], last)
    if last > len(R): cnt["U1_freeze_FAIL"] += 1
    f = sum(J[i]["fb"] for i in range(T))
    ch = sum(any(J[i]["Xk"][v] != J[i + 1]["Xk"][v] or J[i]["Wk"][v] != J[i + 1]["Wk"][v] or J[i]["s"][v] != J[i + 1]["s"][v]
                 for v in R) for i in range(T))
    cnt["U1_max_changes"] = max(cnt["U1_max_changes"], ch); cnt["U1_max_len"] = max(cnt["U1_max_len"], T)
    if ch > u1bound(len(R), f): cnt["U1_FAIL"] += 1
    for i in range(T):
        if not J[i]["fb"] and any(J[i + 1]["Wk"][v] < J[i]["Wk"][v] for v in R): cnt["U1_Wdecrease_FAIL"] += 1
    if name: print("  U1 piece", name, "len", T, "|R|", len(R), "c_theta", ct, "c_w", cw, "f", f, "R-changing", ch,
                   "bound", u1bound(len(R), f), "freeze", last, "H2", J[0]["H2"])

def rand_c1o(rng, lo, hi):
    n = rng.randint(lo, hi); owner = [0] * n; o = rng.randrange(n); owner[o] = 1
    for v in range(n):
        if v != o and rng.random() < 0.1: owner[v] = 1
    succ = [sorted(set(rng.sample(range(n), min(n, rng.choice((1, 2, 2, 3)))))) for _ in range(n)]
    for v in range(n):
        if owner[v] == 1 and v != o: succ[v] = succ[v][:1]
    succ[o] = sorted(set(rng.sample(range(n), min(n, rng.choice((2, 3, 4))))))
    if len(succ[o]) < 2: return None
    return pg.Game([rng.randrange(n + 3) for _ in range(n)], owner, succ)

if __name__ == "__main__":
    a = sys.argv[1:]; cnt = Counter()
    if a[0] == "rand":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        for _ in range(N):
            g = rand_c1o(rng, lo, hi)
            if g is None: continue
            run(g, cnt)
        print(dict(sorted(cnt.items()))); sys.exit()
    for p in a:
        c1 = Counter(); g = load(p); print(p, "n", g.n); run(g, c1, os.path.basename(p))
        print("  ", dict(sorted(c1.items()))); cnt.update(c1)
    print("TOTAL", dict(sorted((k, v) for k, v in cnt.items() if not k.endswith("_max") and "max" not in k)))

def arena_test(N, lo, hi, seed):
    """TB / TBc on single S4a steps over random arenas: random game, random sigma, tau, random arena A(v) containing sigma(v)
    (TB's proof uses only that H_k contains sigma_k; the gate is not used)."""
    rng = random.Random(seed); cnt = Counter()
    for _ in range(N):
        n = rng.randint(lo, hi); owner = [rng.randrange(2) for _ in range(n)]
        succ = [sorted(set(rng.sample(range(n), min(n, rng.choice((1, 2, 3, 4)))))) for _ in range(n)]
        g = pg.Game([rng.randrange(n + 2) for _ in range(n)], owner, succ); E = Engine(g)
        s = tuple(rng.choice(succ[v]) if owner[v] == 0 else -1 for v in range(n))
        t = tuple(rng.choice(succ[v]) if owner[v] == 1 else -1 for v in range(n))
        Is = [(v, w) for v in range(n) if owner[v] == 0 for w in succ[v] if w != s[v] and rng.random() < 0.7]
        opt = {v: {s[v]} for v in range(n) if owner[v] == 0}
        for v, w in Is: opt[v].add(w)
        h = [sorted(opt[v]) if owner[v] == 0 else [t[v]] for v in range(n)]
        Er = Engine(dual(pg.Game(list(g.prio), list(g.owner), h)))
        _, best = Er.evaluate(tuple(t[v] if owner[v] == 1 else -1 for v in range(n)))
        s1 = tuple(best[v] if owner[v] == 0 else -1 for v in range(n))
        cnt["arenas"] += 1; check_tb(g, E, s, s1, t, Is, cnt)
    return cnt
