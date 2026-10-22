#!/usr/bin/env python3
"""REFEREE (successor 3, Fable 5.1) probe for packet P-N5-1P (docs/new/N5-phase-bound-box10.md @ 26905f0).
Everything below is computed FROM THE DEFINITIONS (VJ00 BRICS RS-00-48 §4.2-4.3): plays are simulated, the order is the MaxDiff
order of §4.2, no si.py, no n5.py (except in mode 'n5', where n5.py's unmodified loop is run and its trajectory is compared with
a brute-force switch-best step computed here).

One-player game: Odd vertices have out-degree 1 (a forced edge). A strategy rho fixes every play.
Switch-best step: rho_{k+1} = a strategy of the arena H_k (x may use {rho_k(x)} u I_k(x)) whose valuation is the POINTWISE MAX over
all arena strategies (enumerated exhaustively when the arena has <= EXH strategies, else by switch-all SI inside the arena, which is
checked against the exhaustive optimum whenever both are computed). Tie-break among optimal strategies: rand | keep | far.

Checks per run (every one prints its own counter, violations are printed in full):
  F1  the chosen optimum dominates EVERY arena strategy pointwise (exhaustive)   F1X  a pointwise maximum exists (exhaustive)
  F2  Omega_{k+1} >= Omega_k pointwise
  LP  Lemma P: in a lambda-phase, after k steps, Omega_k(x) >= value(r) for every simple path r of <= k edges from x to a cycle node u of rho_0
  PH  Theorem PH: in a phase, every step with in-phase index >= n-1 is value-flat; value-changing steps <= n-1; flat steps <= m-n; steps < n+m
  PC  phases <= n(n-1)+1; total steps < (n^2-n+1)(n+m); value-changing steps <= n^3-n^2+n
  NC  a no-change optimum (rho itself optimal with I != {}) happens only when every improving edge is a flat cycle-closer at its own cycle node;
      the N5 fallback (each such x to its best improving successor) leaves I = {} and the valuation unchanged
  L58 VJ00 Lemma 5.8 (1=>2) on one-player games: a strategy with no improving edge dominates every strategy pointwise (exhaustive over ALL strategies, n <= nall)
Usage: n5_1p_probe.py games seed nmax tiebreak [n5]      (tiebreak in rand|keep|far; 'n5' runs n5.py's loop and compares)"""
import sys, os, random, itertools, functools
sys.setrecursionlimit(10000)
EXH = 20000

def reward(prio, v): return prio[v] if prio[v] % 2 == 0 else -prio[v]

def cmp_sets(prio, B, C):
    """VJ00 §4.2: B < C iff MaxDiff in (B\\C) odd or in (C\\B) even. Returns -1/0/1."""
    if B == C: return 0
    d = max(B ^ C, key=lambda v: prio[v])
    if d in C: return -1 if prio[d] % 2 == 0 else 1     # d in C\B: even => B < C (Even prefers C)
    return 1 if prio[d] % 2 == 0 else -1                 # d in B\C: odd  => B < C

def cmp_val(prio, a, b):
    """Order on play values (c, P, l): reward of c; then P by MaxDiff; then l (longer better iff c odd)."""
    ra, rb = reward(prio, a[0]), reward(prio, b[0])
    if ra != rb: return -1 if ra < rb else 1
    s = cmp_sets(prio, a[1], b[1])
    if s: return s
    if a[2] == b[2]: return 0
    if prio[a[0]] % 2 == 1: return -1 if a[2] < b[2] else 1
    return -1 if a[2] > b[2] else 1

def play_value(prio, rho, x):
    seen = {}; path = []; v = x
    while v not in seen:
        seen[v] = len(path); path.append(v); v = rho[v]
    cyc = path[seen[v]:]
    c = max(cyc, key=lambda u: prio[u])
    pre = path[:path.index(c)]
    return (c, frozenset(u for u in pre if prio[u] > prio[c]), len(pre))

def valuation(prio, rho, n): return tuple(play_value(prio, rho, x) for x in range(n))

def improving(prio, succ, owner, rho, Om):
    return [(x, z) for x in range(len(rho)) if owner[x] == 0 for z in succ[x] if z != rho[x] and cmp_val(prio, Om[z], Om[rho[x]]) > 0]

def dominates(prio, A, B): return all(cmp_val(prio, a, b) >= 0 for a, b in zip(A, B))

def arena_optimum(prio, succ, owner, rho, I, n, tb, rng, stats):
    """Returns (list of optimal strategies or None, optimum valuation, exhaustive?)."""
    opts = [[rho[x]] + sorted({z for y, z in I if y == x}) for x in range(n)]
    size = 1
    for o in opts: size *= len(o)
    # switch-all SI inside the arena (used when the arena is too large; checked against the exhaustive optimum otherwise)
    cur = list(rho)
    while True:
        Om = valuation(prio, cur, n)
        ch = False
        for x in range(n):
            best = max(opts[x], key=functools.cmp_to_key(lambda a, b: cmp_val(prio, Om[a], Om[b])))
            if cmp_val(prio, Om[best], Om[cur[x]]) > 0: cur[x] = best; ch = True
        if not ch: break
    si_val = valuation(prio, cur, n)
    if size > EXH:
        stats['si_only'] += 1
        return [cur], si_val, False
    vals = {}
    for s in itertools.product(*opts):
        vals[s] = valuation(prio, s, n)
    key = functools.cmp_to_key(lambda a, b: cmp_val(prio, a, b))
    top = tuple(max((vals[s][x] for s in vals), key=key) for x in range(n))
    optimal = [s for s in vals if vals[s] == top]
    stats['exh'] += 1
    if not optimal:
        stats['F1X_viol'] += 1; print("F1X VIOLATION (no pointwise maximum in the arena)", prio, succ, owner, rho, I); return None, top, True
    if si_val != top: stats['SIvsEXH_viol'] += 1; print("SI-in-arena != exhaustive optimum", prio, succ, owner, rho)
    for s in vals:
        if not dominates(prio, top, vals[s]): stats['F1_viol'] += 1; print("F1 VIOLATION", prio, succ, owner, rho, s)
    stats['F1_checks'] += len(vals)
    if tb == 'rand': ch = rng.choice(optimal)
    elif tb == 'keep': ch = max(optimal, key=lambda s: sum(1 for x in range(n) if s[x] == rho[x]))
    else: ch = min(optimal, key=lambda s: sum(1 for x in range(n) if s[x] == rho[x]))
    return [list(ch)], top, True

def simple_path_table(prio, succ, n, U):
    """best[(u, x, L)] = best value (u, P, L) over simple paths x -> u with exactly L edges (x != u)."""
    best = {}
    key = functools.cmp_to_key(lambda a, b: cmp_val(prio, a, b))
    def rec(u, x0, v, path, seen):
        for w in succ[v]:
            if w == u:
                P = frozenset(q for q in path if prio[q] > prio[u]); val = (u, P, len(path)); k = (u, x0, len(path))
                if k not in best or cmp_val(prio, val, best[k]) > 0: best[k] = val
            elif w not in seen:
                rec(u, x0, w, path + [w], seen | {w})
    for u in U:
        for x in range(n):
            if x != u: rec(u, x, x, [x], {x})
    return best

def n5_trajectory(prio, succ, owner, s0):
    """Run experiments/new/n5.py's loop UNMODIFIED and record the sigma it evaluates on the main engine (first Engine built)."""
    HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "..", "..", "..")
    for p in ("experiments/new", "experiments/si", "experiments/harness"):
        if os.path.join(ROOT, p) not in sys.path: sys.path.insert(0, os.path.join(ROOT, p))
    import pg, si, n5
    traj = []; main = []
    orig_init, orig_eval = si.Engine.__init__, si.Engine.evaluate
    def init(self, *a, **k):
        orig_init(self, *a, **k)
        if not main: main.append(self)
    def ev(self, strat):
        r = orig_eval(self, strat)
        if main and self is main[0]: traj.append((tuple(strat), r[0]))
        return r
    si.Engine.__init__, si.Engine.evaluate = init, ev
    try:
        g = pg.Game(list(prio), list(owner), [list(s) for s in succ])
        start = ({v: s0[v] for v in range(len(s0)) if owner[v] == 0}, {v: succ[v][0] for v in range(len(s0)) if owner[v] == 1})
        it, fb, win, ws, ev_count = n5.run(g, "n5", start)
    finally:
        si.Engine.__init__, si.Engine.evaluate = orig_init, orig_eval
    # the loop evaluates sigma once per iteration; regions() re-evaluates the final sigma: drop consecutive repeats
    out = []
    for s, v in traj:
        if not out or out[-1][0] != s: out.append((s, v))
    return it, fb, out, main[0]

def main():
    INST = sys.argv[1] == 'inst'
    if INST:
        tb = sys.argv[2]; files = sys.argv[3:]; games, seed, nmax = len(files), 0, 0; N5 = True
        HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "experiments", "harness")); import pg
    else:
        games, seed, nmax, tb = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
        N5 = len(sys.argv) > 5 and sys.argv[5] == 'n5'
    nall = 6
    rng = random.Random(seed)
    st = dict(exh=0, si_only=0, F1_checks=0, F1_viol=0, F1X_viol=0, SIvsEXH_viol=0, F2_checks=0, F2_viol=0, LP_checks=0, LP_viol=0,
              PH_viol=0, PC_viol=0, NC_events=0, NC_viol=0, runs=0, steps=0, flat=0, nochange=0, maxphase_vc=(0, 0), maxphase_len=(0, 0),
              L58_games=0, L58_strats=0, L58_viol=0, N5_runs=0, N5_iter=0, N5_fb=0, N5_viol=0, N5_valmismatch=0, N5_notopt=0, N5_bound_viol=0,
              phases_max=(0, 0))
    for gi in range(games):
        if INST:
            g = pg.read(files[gi]); n, owner, succ = g.n, list(g.owner), [sorted(set(s)) for s in g.succ]
            assert len(set(g.prio)) == n, "priorities must be injective"
            assert all(len(succ[v]) == 1 for v in range(n) if owner[v] == 1), "Odd must have out-degree 1"
            prio = list(g.prio)
            inst_s0 = [succ[v][0] for v in range(n)]
            if os.path.exists(files[gi] + ".start"):
                for tok in open(files[gi] + ".start").readline().split()[1:]: a, b = map(int, tok.split(":")); inst_s0[a] = b
            print("instance", os.path.basename(files[gi]), "n", n, "m", sum(len(s) for s in succ), flush=True)
        else:
            n = rng.randint(3, nmax)
            owner = [0 if rng.random() < 0.75 else 1 for _ in range(n)]
            prio = rng.sample(range(2 * n), n)
            succ = [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, 4)))) if owner[v] == 0 else [rng.randrange(n)] for v in range(n)]
        m = sum(len(s) for s in succ)
        LPOK = n <= 24   # the simple-path table is exponential; skipped (and said so) above n = 24
        # L58: exhaustive over ALL strategies of the game
        allsize = 1
        for s in succ: allsize *= len(s)
        if n <= nall and allsize <= EXH:
            st['L58_games'] += 1
            vals = {s: valuation(prio, s, n) for s in itertools.product(*succ)}
            keyf = functools.cmp_to_key(lambda a, b: cmp_val(prio, a, b))
            topall = tuple(max((vals[s][x] for s in vals), key=keyf) for x in range(n))
            for s, Om in vals.items():
                if not improving(prio, succ, owner, s, Om):
                    st['L58_strats'] += 1
                    if Om != topall: st['L58_viol'] += 1; print("L58 VIOLATION", prio, succ, owner, s, Om, topall)
        for rep in range(1 if INST else 2):
            s0 = list(inst_s0) if INST else [rng.choice(succ[v]) for v in range(n)]
            rho = list(s0); st['runs'] += 1
            Om = valuation(prio, rho, n); lam = tuple(v[0] for v in Om)
            phase_start = 0; k = 0; phases = 1; best = simple_path_table(prio, succ, n, set(lam)) if LPOK else {}; vc_in_phase = 0; flat_in_phase = 0; total_vc = 0
            bigphase_vc = 0
            def check_LP(Om, kk):
                for (u, x, L), val in best.items():
                    if L <= kk:
                        st['LP_checks'] += 1
                        if cmp_val(prio, Om[x], val) < 0:
                            st['LP_viol'] += 1; print("LEMMA P VIOLATION", dict(n=n, k=kk, x=x, u=u, L=L, Om=Om[x], path=val, prio=prio, owner=owner, succ=succ, start=s0, rho=rho))
            check_LP(Om, 0)
            while True:
                I = improving(prio, succ, owner, rho, Om)
                if not I: break
                optimal, top, exh = arena_optimum(prio, succ, owner, rho, I, n, tb, rng, st)
                if optimal is None: break
                new = optimal[0]
                st['F2_checks'] += 1
                if not dominates(prio, top, Om): st['F2_viol'] += 1; print("F2 VIOLATION", prio, succ, owner, rho)
                if new == rho:
                    # no-change optimum: NC check, then the N5 fallback
                    st['nochange'] += 1; st['NC_events'] += 1
                    for (x, z) in I:
                        h = list(rho); h[x] = z; vh = valuation(prio, h, n)
                        if not (Om[x][0] == x and vh == Om):
                            st['NC_viol'] += 1; print("NC VIOLATION (non-flat improving edge at a no-change step)", prio, succ, owner, rho, (x, z), Om[x], vh[x])
                    fb = list(rho)
                    for x in {x for x, _ in I}:
                        fb[x] = max((z for y, z in I if y == x), key=lambda z: (functools.cmp_to_key(lambda a, b: cmp_val(prio, a, b))(Om[z]), z))
                    vfb = valuation(prio, fb, n)
                    if vfb != Om or improving(prio, succ, owner, fb, vfb):
                        st['NC_viol'] += 1; print("NC VIOLATION (fallback not flat or leaves improving edges)", prio, succ, owner, rho, fb)
                    new = fb; top = vfb
                k += 1; st['steps'] += 1
                newOm = valuation(prio, new, n)
                assert newOm == top
                newlam = tuple(v[0] for v in newOm)
                flat = (newOm == Om)
                if flat: st['flat'] += 1
                if newlam == lam:
                    idx = k - 1 - phase_start   # in-phase index of this step
                    if flat: flat_in_phase += 1
                    else:
                        vc_in_phase += 1; total_vc += 1
                        if idx >= n - 1: st['PH_viol'] += 1; print("PH VIOLATION (value-changing step at in-phase index >= n-1)", dict(n=n, idx=idx, prio=prio, owner=owner, succ=succ, start=s0))
                    if vc_in_phase > n - 1 or flat_in_phase > m - n or (k - phase_start) >= n + m:
                        st['PH_viol'] += 1; print("PH VIOLATION (counts)", dict(n=n, m=m, vc=vc_in_phase, flat=flat_in_phase, steps=k - phase_start, prio=prio, owner=owner, succ=succ, start=s0))
                    if vc_in_phase > st['maxphase_vc'][0]: st['maxphase_vc'] = (vc_in_phase, n)
                    if k - phase_start > st['maxphase_len'][0]: st['maxphase_len'] = (k - phase_start, n)
                    check_LP(newOm, k - phase_start)
                else:
                    total_vc += 1   # a lambda change is value-changing
                    phases += 1; phase_start = k; vc_in_phase = flat_in_phase = 0
                    lam = newlam; best = simple_path_table(prio, succ, n, set(lam)) if LPOK else {}
                    check_LP(newOm, 0)
                rho, Om = new, newOm
            if phases > n * (n - 1) + 1 or k >= (n * n - n + 1) * (n + m) or total_vc > n ** 3 - n ** 2 + n:
                st['PC_viol'] += 1; print("PC VIOLATION", dict(n=n, m=m, phases=phases, steps=k, vc=total_vc))
            if phases > st['phases_max'][0]: st['phases_max'] = (phases, n)
            if INST: print("  switch-best steps", k, "phases", phases, "value-changing", total_vc, "max vc in a phase", st['maxphase_vc'], "LP checked" if LPOK else "LP SKIPPED (n > 24)", flush=True)
            if N5:
                st['N5_runs'] += 1
                it, fb, traj, E = n5_trajectory(prio, succ, owner, s0)
                st['N5_iter'] += it; st['N5_fb'] += fb
                if INST: print("  n5.py iterations", it, "fallbacks", fb, "my switch-best steps", k, flush=True)
                if it >= (n * n - n + 1) * (n + m): st['N5_bound_viol'] += 1; print("N5 BOUND VIOLATION", n, m, it)
                # (a) engine valuation = my valuation (G-N1 on these games); (b) each N5 step is an arena optimum of the previous sigma
                for j, (s, vs) in enumerate(traj):
                    s = [s[v] if owner[v] == 0 else succ[v][0] for v in range(n)]   # si.py stores -1 at Odd vertices
                    mine = valuation(prio, s, n)
                    eng = tuple((vs[x][0], frozenset(v for v in range(n) if (vs[x][1] >> E.rank[v]) & 1), vs[x][2]) for x in range(n))
                    if eng != mine: st['N5_valmismatch'] += 1; print("N5 ENGINE VALUATION MISMATCH", prio, owner, succ, s, eng, mine)
                    if j + 1 < len(traj):
                        I = improving(prio, succ, owner, s, mine)
                        nxt = [traj[j + 1][0][v] if owner[v] == 0 else succ[v][0] for v in range(n)]
                        if not I: st['N5_viol'] += 1; print("N5 moved with I = {}", prio, owner, succ, s); continue
                        opts = [{s[x]} | {z for y, z in I if y == x} for x in range(n)]
                        if any(nxt[x] not in opts[x] for x in range(n) if owner[x] == 0):
                            st['N5_viol'] += 1; print("N5 step outside the arena", prio, owner, succ, s, nxt); continue
                        optimal, top, exh = arena_optimum(prio, succ, owner, s, I, n, 'rand', rng, st)
                        vn = valuation(prio, nxt, n)
                        if vn != top:
                            # allowed only as the fallback (S4c): N5's arena optimum returned sigma, then switch-all-best; that is flat
                            if vn == mine and all(nxt[x] == s[x] or (x, nxt[x]) in I for x in range(n)): pass
                            else: st['N5_notopt'] += 1; print("N5 step is not an arena optimum", prio, owner, succ, s, nxt, vn, top)
    print("RESULT", " ".join(f"{k}={v}" for k, v in st.items()), f"games={games} seed={seed} nmax={nmax} tb={tb} n5={N5}")

if __name__ == "__main__": main()
