#!/usr/bin/env python3
r"""REFEREE-2 successor 13 (Opus 5.5, D15): mechanical check of packet P-N5-1O (docs/si/P-N5-1O-box15.md sha1 2cf5e672 @ trunk 291c110d).
State sequence: SPEC N5 via my lane's R2-N5-RE/re_check.n5_spec (experiments/new/n5.py + experiments/si/si.py, read-only), from the S3 start
and from random start pairs. Everything checked against it is computed HERE from the definitions: play values (c, P, l) and SPEC S1's order
(re_check.Game), positional strategies enumerated by brute force, an own Zielonka (max-parity) and an own strategy verifier.
Checks (packet items):
  R15D   every iteration changes (sigma, tau) (Theorem step 1).
  PHI    #phases <= n(n-1) + d_o, phase = maximal run with (lambda_Xi, tau) constant (step 2; R47 (b)).
  FB     per phase: in-phase fallbacks are Even's (tau unchanged); f <= R48 (i) bound (o != c_theta: 1 + (|U|-2)(|succ(o) & U^| + |U|);
         o = c_theta: |U|); f <= F := 2n^2 (step 3).
  TSTAR  per phase: in-phase transitions <= T*(n, m, d_o, Delta) (step 3 with R50 (h)); ITER <= (n(n-1) + d_o)(T* + 1) (step 4).
  OUT    at the stop (Lemma OUT): (O1) I_sigma = I_tau = {} (si) and no improving Even edge by own values; (O2) the (sigma, sbar)-play
         value of every v equals si's Xi_sigma(v) (sbar = S1's counterstrategy, si tau_full); (O3) for EVERY positional Odd tau'
         (enumerated), V_{sigma,tau'} >= Xi_sigma pointwise (R18 (d) Lemma S (a) / R21 (a)); (O3b) for every positional Even sigma'
         (enumerated when the product of out-degrees <= CAP), V_{sigma',sbar} <= V_{sigma,sbar} (R36 (c) in H = G_sbar); (O4) W := {v :
         Omega(lambda(v)) even} = W_E by own Zielonka; (O5) sigma wins every play from W, sbar every play from V \ W (own verifier);
         (O6) sigma-closure of W and sbar-closure of V \ W.
  Records: REW0 = stops where some v in W has lambda(v) of reward 0 (the rank-0 vertex, even priority): the packet's "> 0" (Lemma OUT
         step 2) is false there and ">= 0" is what holds; max ratios phases / bound, f / R48 bound, ITER / bound.
Modes: random N nmin nmax seed (one Odd choice vertex) | general N nmin nmax seed (several Odd choice vertices: Lemma OUT READING data, no
       phase checks) | files list.txt [runs].   Mutations ONE_MUT: flip (W := odd cycle nodes), sbar (random Odd strategy for sbar),
       early (output read at the START state), phi (phases <= d_o), fb (f <= max(0, |U| - 3))."""
import sys, os, random, itertools
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-RE"))
import re_check as RC
MUT = os.environ.get("ONE_MUT", "")
CAP = 4096
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
for p in ("experiments/new", "experiments/si", "experiments/harness"): sys.path.insert(0, os.path.join(ROOT, p))
import pg as lpg, n5
from si import Engine

class Stats:
    def __init__(s): s.c = {}; s.mx = {}; s.viol = []
    def inc(s, k, d=1): s.c[k] = s.c.get(k, 0) + d
    def mxr(s, k, v):
        if k not in s.mx or v[0] > s.mx[k][0]: s.mx[k] = v
    def bad(s, k, msg):
        s.inc("VIOLATIONS"); s.inc("V_" + k)
        if len(s.viol) < 30: s.viol.append(f"{k}: {msg}")

def tstar(n, m, do, D):
    F = 2 * n * n; TH = n * n + 2 * n - 1
    XSN = 13 * (do + 1) * n ** 3 * (F + 1 + TH) + TH
    X = (F + 1) * (n - 1) + F + XSN
    Th = (n - 1) + n * (X + 1) + X
    So = do * (Th + 1)
    Wch = (F + X + 1) * n * n
    Nst = 1 + X + Th + Wch
    NXi = F + Nst + (X + 1) * (n - 1) + (Nst + F) * 3 * D * n ** 4
    return (m - n + 1) * (So + NXi + 1)

def to_val(g, v):  # si (c, mask over ranks, l) -> (c, frozenset, l)
    c, mask, l = v
    return (c, frozenset(u for u in range(g.n) if mask >> g.rank[u] & 1), l)

def zielonka(g, V):
    """own Zielonka on the subgame V (a set, closed for the moves used); returns (W_E, W_O)."""
    if not V: return set(), set()
    p = max(g.prio[v] for v in V); i = p % 2          # player i likes p
    A = attr(g, V, {v for v in V if g.prio[v] == p}, i)
    W = zielonka(g, V - A)
    if not W[1 - i]:
        res = [set(), set()]; res[i] = set(V); return res[0], res[1]
    B = attr(g, V, W[1 - i], 1 - i)
    W2 = zielonka(g, V - B)
    res = [set(W2[0]), set(W2[1])]; res[1 - i] |= B
    return res[0], res[1]

def attr(g, V, T, i):
    A = set(T); ch = True
    while ch:
        ch = False
        for v in V - A:
            sv = [w for w in g.succ[v] if w in V]
            if (g.owner[v] == i and any(w in A for w in sv)) or (g.owner[v] != i and all(w in A for w in sv)):
                A.add(v); ch = True
    return A

def wins_fixed(g, f_owner, fmap, region, player):
    """player's positional strategy fmap (on player's vertices) wins every play from region (opponent free)?
    Fails iff from region the graph reaches a vertex u with priority of the opponent's parity on a cycle of vertices of prio <= prio(u)."""
    succ = [[fmap[v]] if g.owner[v] == player else g.succ[v] for v in range(g.n)]
    reach, st = set(region), list(region)
    while st:
        x = st.pop()
        for y in succ[x]:
            if y not in reach: reach.add(y); st.append(y)
    for u in reach:
        if g.prio[u] % 2 == player: continue
        lim = g.prio[u]; seen, st = set(), [u]
        while st:
            x = st.pop()
            for y in succ[x]:
                if g.prio[y] > lim: continue
                if y == u: return False, u
                if y not in seen: seen.add(y); st.append(y)
    return True, None

def check_out(g, sg, tu, st, name):
    lg = lpg.Game(list(g.prio), list(g.owner), [list(s) for s in g.succ])
    E, Ed = Engine(lg), Engine(n5.dual(lg)); n = g.n
    sgt = tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n))
    vs, tf = E.evaluate(sgt)
    Is = E.improving(tuple(sg), vs); vt, _ = Ed.evaluate(tuple(tu)); It = Ed.improving(tuple(tu), vt)
    if MUT != "early" and (Is or It): st.bad("O1", f"{name}: stop with improving edges"); return
    Xi = [to_val(g, vs[v]) for v in range(n)]
    sbar = [tf[v] if g.owner[v] == 1 else None for v in range(n)]
    if MUT == "sbar":
        rng = random.Random(hash(name) & 0xffff); sbar = [rng.choice(g.succ[v]) if g.owner[v] == 1 else None for v in range(n)]
    st.inc("stops")
    f = [sg[v] if g.owner[v] == 0 else sbar[v] for v in range(n)]
    # O1 own: no improving Even edge
    if MUT != "early":
        for v in range(n):
            if g.owner[v] == 0:
                for z in g.succ[v]:
                    if g.cmp(Xi[z], Xi[sg[v]]) > 0: st.bad("O1", f"{name}: own improving edge {v}->{z}")
    # O2 realisation
    for v in range(n):
        pv = g.play(f, v)[0]
        if pv != Xi[v]: st.bad("O2", f"{name}: v={v} play {pv} != Xi {Xi[v]}"); break
    else: st.inc("O2_ok")
    # O3 every positional Odd tau'
    odd = [v for v in range(n) if g.owner[v] == 1]
    prod = 1
    for v in odd: prod *= len(g.succ[v])
    if prod <= CAP:
        st.inc("O3_runs")
        for ch in itertools.product(*[g.succ[v] for v in odd]):
            f2 = list(f)
            for v, w in zip(odd, ch): f2[v] = w
            for v in range(n):
                if g.cmp(g.play(f2, v)[0], Xi[v]) < 0: st.bad("O3", f"{name}: tau' {ch} beats Xi at {v}"); break
            st.inc("O3_strats")
    else: st.inc("O3_skipped")
    # O3b every positional Even sigma' against sbar
    ev = [v for v in range(n) if g.owner[v] == 0]
    prod = 1
    for v in ev: prod *= len(g.succ[v])
    if prod <= CAP:
        st.inc("O3b_runs")
        base = [g.play(f, v)[0] for v in range(n)]
        for ch in itertools.product(*[g.succ[v] for v in ev]):
            f2 = list(f)
            for v, w in zip(ev, ch): f2[v] = w
            for v in range(n):
                if g.cmp(g.play(f2, v)[0], base[v]) > 0: st.bad("O3b", f"{name}: sigma' {ch} beats sigma at {v}"); break
            st.inc("O3b_strats")
    else: st.inc("O3b_skipped")
    # O4 regions
    lam = [Xi[v][0] for v in range(n)]
    W = {v for v in range(n) if (g.prio[lam[v]] % 2 == 0) != (MUT == "flip")}
    WE, WO = zielonka(g, set(range(n)))
    if W != WE: st.bad("O4", f"{name}: W {sorted(W)} != W_E {sorted(WE)}")
    else: st.inc("O4_ok")
    # O5 strategies
    ok1, u1 = wins_fixed(g, 0, sg, W, 0)
    ok2, u2 = wins_fixed(g, 1, sbar, set(range(n)) - W, 1)
    if not ok1: st.bad("O5", f"{name}: sigma loses from W (odd cycle at {u1})")
    if not ok2: st.bad("O5", f"{name}: sbar loses from V\\W (even cycle at {u2})")
    if ok1 and ok2: st.inc("O5_ok")
    # O6 closure
    for v in range(n):
        nxt = [sg[v]] if g.owner[v] == 0 else g.succ[v]
        if v in W and any(w not in W for w in nxt): st.bad("O6", f"{name}: sigma-play leaves W at {v}"); break
        nxt = [sbar[v]] if g.owner[v] == 1 else g.succ[v]
        if v not in W and any(w in W for w in nxt): st.bad("O6", f"{name}: sbar-play enters W at {v}"); break
    # REW0 record
    r0 = min(range(n), key=lambda u: g.rank[u])
    if g.prio[r0] % 2 == 0 and any(lam[v] == r0 for v in W):
        st.inc("REW0_stops")

def check_phases(g, o, states, fbs, st, name):
    lg = lpg.Game(list(g.prio), list(g.owner), [list(s) for s in g.succ]); E = Engine(lg); n = g.n
    m = sum(len(s) for s in g.succ); do = len(g.succ[o]); D = max(len(s) for s in g.succ)
    lams = []
    for sg, tu in states:
        vs, _ = E.evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
        lams.append(tuple(vs[v][0] for v in range(n)))
    keys = [(lams[k], tuple(states[k][1])) for k in range(len(states))]
    for k in range(len(fbs)):
        if states[k] == states[k + 1]: st.bad("R15D", f"{name}: iteration {k} changes nothing")
    phases, cur = [], [0]
    for k in range(1, len(states)):
        if keys[k] == keys[k - 1]: cur.append(k)
        else: phases.append(cur); cur = [k]
    phases.append(cur)
    P = len(phases); bP = n * (n - 1) + do
    if MUT == "phi": bP = do
    st.inc("runs"); st.inc("phases", P); st.inc("iterations", len(fbs))
    st.mxr("phases_over_bound", (P / bP, name)); st.mxr("max_phases", (P, name))
    if P > bP: st.bad("PHI", f"{name}: {P} phases > {bP}")
    T = tstar(n, m, do, D)
    if len(fbs) > (n * (n - 1) + do) * (T + 1): st.bad("TSTAR", f"{name}: ITER {len(fbs)} > bound")
    st.mxr("iter_over_bound", (len(fbs) / ((n * (n - 1) + do) * (T + 1)), name))
    for ph in phases:
        lam = lams[ph[0]]; cth = lam[o]; U = {v for v in range(n) if lam[v] == cth}; Uh = U - {o}
        f = 0
        for k in ph[:-1]:
            if fbs[k]:
                f += 1
                if states[k][1] != states[k + 1][1]: st.bad("FB", f"{name}: in-phase fallback changes tau at {k}")
        tin = len(ph) - 1
        if o != cth: b = 1 + (len(U) - 2) * (len(set(g.succ[o]) & Uh) + len(U))
        else: b = len(U)
        if MUT == "fb": b = max(0, len(U) - 3)
        if f > b: st.bad("FB", f"{name}: f {f} > R48 bound {b} (|U| {len(U)}, o==c {o == cth})")
        if f > 2 * n * n: st.bad("FB", f"{name}: f {f} > 2n^2")
        if f: st.inc("phases_with_fb"); st.mxr("f_over_R48", (f / max(b, 1), name)); st.mxr("max_f", (f, name))
        if tin > T: st.bad("TSTAR", f"{name}: phase with {tin} transitions > T*")
        st.mxr("max_phase_len", (tin, name))

def one_choice(g):
    oc = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1]
    return oc[0] if len(oc) == 1 else None

def rand_general(rng, n):
    while True:
        owner = [rng.randrange(2) for _ in range(n)]
        prio = [rng.randrange(0, n + 1) for _ in range(n)]
        succ = [rng.sample(range(n), rng.randint(1, min(3, n))) for _ in range(n)]
        g = RC.Game(prio, owner, succ)
        if sum(1 for v in range(n) if owner[v] == 1 and len(g.succ[v]) > 1) >= 2: return g

def do_game(g, o, s, t, st, name, general=False):
    states, fbs = RC.n5_spec(g, o, s, t)
    if not general: check_phases(g, o, states, fbs, st, name)
    else: st.inc("runs"); st.inc("iterations", len(fbs))
    sg, tu = states[0] if MUT == "early" else states[-1]
    check_out(g, sg, tu, st, name)

def main():
    st = Stats(); a = sys.argv[1:]
    if a[0] in ("random", "general"):
        N, nmin, nmax, seed = map(int, a[1:5]); rng = random.Random(seed)
        for i in range(N):
            n = rng.randint(nmin, nmax)
            if a[0] == "random":
                g, o = RC.rand_game(rng, n, cyc=rng.random() < 0.7); assert one_choice(g) == o
            else:
                g = rand_general(rng, n); o = None
            s, t = RC.rand_start(rng, g) if i % 2 else s3(g)
            do_game(g, o, s, t, st, f"{a[0]}{seed}:{i}", general=(a[0] == "general"))
    elif a[0] == "files":
        runs = int(a[2]) if len(a) > 2 else 3; rng = random.Random(1013)
        for path in [l.strip() for l in open(a[1]) if l.strip()]:
            g = RC.parse(open(os.path.join(ROOT, path)).read()); o = one_choice(g)
            if o is None: st.inc("skipped_not_1O"); continue
            for r in range(runs):
                s, t = s3(g) if r == 0 else RC.rand_start(rng, g)
                do_game(g, o, s, t, st, f"{path}#{r}")
    print("MODE", " ".join(a), "MUT", MUT or "-")
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for v in st.viol: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c.get("VIOLATIONS") else "OK", f"violations={st.c.get('VIOLATIONS', 0)}")

def s3(g):
    def br(v, dual):
        def rr(w):
            p = g.prio[w] + (1 if dual else 0)
            r_ = p if p % 2 == 0 else -p
            return (r_, w if r_ % 2 == 0 else -w)
        return max(g.succ[v], key=rr)
    return [br(v, False) for v in range(g.n)], [br(v, True) for v in range(g.n)]

if __name__ == "__main__":
    main()
