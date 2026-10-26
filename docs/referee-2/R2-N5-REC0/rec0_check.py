#!/usr/bin/env python3
r"""REFEREE-2 successor 15 (Opus 5.5, D15): mechanical check of packet P-N5-REC0 (docs/new/P-N5-REC0-box45.md sha1 343239b5 @ 64506ecf).
N5 runs: succ. 13's own SPEC loop R2-N5-DUAL/dual_check.Runner (SPEC S1-S5 + FIX 1-4 on si.py, read-only). Everything else is written here
from the packet's §0 definitions. The lane's experiments/new/box45/rec0.py, recclimb.py are NOT run or imported.
Per phase P ((lambda_Xi, tau) constant; lambda = Xi's cycle-node map), epochs (sigma-bar|Q constant), D = {} states, W := sigma's valuation in
G_tau, all-unsplit (lambda_W = lambda), runs (maximal runs of in-phase non-fallback transitions):
  BOUND  N_0 <= (f + 1)(n + 1) + 4n(n - 1) + 1                                  (Lemma REC-0)
  EP0    len(E) <= n + m for every D = {} epoch (R64 (c)); COR: transitions with source in a D = {} epoch <= bound * (n + m)
  PREFIX the all-unsplit states of every run form a prefix of the run           (SN-PREFIX_D (a))
  KIND   per run, kind-(iii) epoch-last transitions with source < t  <= n - 1; kinds (i) <= f, (ii) <= 1 per run (proof step 5)
  SAT    every D = {} state t' >= t (t = first saturated D = {} state) has Xi = B; t* - t <= 4n(n - 1)  (proof step 4)
 with n <= LEVELMAX (simple paths of G_tau enumerated exactly; value(r) = (u, P(r), |r|), u a cycle node of lambda):
  BASE   all-unsplit => level >= 0;  UB  all-unsplit => W <= B pointwise        (steps 2, 4)
  STEP1  in-phase S4a k -> k+1, k D = {}, k+1 all-unsplit => level(k+1) >= min(level(k) + 1, n - 1)   (step 1, Q-R17)
  STEP2  in-phase S4a k -> k+1, both all-unsplit => level(k+1) >= level(k)       (step 2)
Mutation RC_MUT: step2 (STEP1 asks level + 2; bites only on exact +1 rises), full (STEP1 asks level n - 1 at once: must fail), nosat (bound without the 4n(n - 1) term: may never fail; recorded).
Usage: rec0_check.py random N nmin nmax seed kind [k] | files list.txt [runs]   (kind: kO | 1O)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-DUAL"))
import dual_check as DC
pg, Engine, Stats = DC.pg, DC.Engine, DC.Stats
MUT = os.environ.get("RC_MUT", "")
LEVELMAX = int(os.environ.get("LEVELMAX", "11"))

def Gtau(g, tu):
    return pg.Game(list(g.prio), list(g.owner), [[tu[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(g.n)])

def path_max(g, Et, tu, cyc):
    """best[x][L] = max key of value(r) over simple paths r of G_tau with exactly L edges from x to a cycle node u in cyc."""
    n = g.n; succ = [[tu[v]] if g.owner[v] == 1 else sorted(set(g.succ[v])) for v in range(n)]
    best = [[None] * n for _ in range(n)]
    def dfs(x, path, onp):
        v = path[-1]
        if v in cyc:
            u = v; L = len(path) - 1; mask = 0
            for y in path[:-1]:
                if Et.rank[y] > Et.rank[u]: mask |= Et.bit[y]
            k = Et.key((u, mask, L))
            if best[x][L] is None or k > best[x][L]: best[x][L] = k
        if len(path) >= n: return
        for w in succ[v]:
            if w not in onp:
                onp.add(w); path.append(w); dfs(x, path, onp); path.pop(); onp.discard(w)
    for x in range(n): dfs(x, [x], {x})
    return best

def level(Et, W, best, n):
    """max j <= n - 1 with W(x) >= value(r) for all r with <= j edges (n - 1 = full); -1 if even j = 0 fails"""
    j = -1
    for L in range(n):
        if all(best[x][L] is None or Et.key(W[x]) >= best[x][L] for x in range(n)): j = L
        else: break
    return j

def analyse(g, states, fbs, st, name):
    n = g.n; m = sum(len(set(s)) for s in g.succ)
    Q = [v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2]
    E = Engine(g)
    info = []
    for sg, tu in states:
        vs, tf = E.evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
        Gt = Gtau(g, tu); Et = Engine(Gt)
        W, _ = Et.evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
        lam = tuple(vs[v][0] for v in range(n)); lamW = tuple(W[v][0] for v in range(n))
        d0 = all(tf[q] == tu[q] for q in Q)
        info.append(dict(vs=vs, tf=tf, W=W, Et=Et, lam=lam, unsplit=(lamW == lam), d0=d0, tq=tuple(tf[q] for q in Q),
                         tk=tuple(tu[v] for v in range(n) if g.owner[v] == 1)))
        if d0 and any(vs[v] != W[v] for v in range(n)): st.bad("D0", f"{name}: D = {{}} state with Xi != W")
    k0 = 0
    while k0 < len(states):
        k1 = k0
        while k1 + 1 < len(states) and (info[k1 + 1]["lam"], info[k1 + 1]["tk"]) == (info[k0]["lam"], info[k0]["tk"]): k1 += 1
        phase(g, n, m, states, fbs, info, k0, k1, st, name)
        k0 = k1 + 1

def phase(g, n, m, states, fbs, info, a, b, st, name):
    st.inc("phases")
    f = sum(1 for k in range(a, b) if fbs[k])
    # epochs
    eps = []; x = a
    while x <= b:
        y = x
        while y + 1 <= b and info[y + 1]["tq"] == info[x]["tq"]: y += 1
        eps.append((x, y)); x = y + 1
    d0eps = [(x, y) for x, y in eps if info[x]["d0"]]
    N0 = len(d0eps)
    bound = (f + 1) * (n + 1) + (0 if MUT == "nosat" else 4 * n * (n - 1)) + 1
    st.inc("BOUND_checks")
    if N0 > bound: st.bad("BOUND", f"{name}: phase {a}..{b} N_0 {N0} > {bound} (f {f})")
    if N0 > st.c.get("max_N0", 0): st.c["max_N0"] = N0
    if N0 and N0 / (f + 1) > st.c.get("max_N0_per_f1", 0): st.c["max_N0_per_f1"] = round(N0 / (f + 1), 2)
    tr0 = 0
    for x, y in d0eps:
        L = (y - x) + (1 if y < b else 0); tr0 += L
        st.inc("EP0_checks")
        if L > n + m: st.bad("EP0", f"{name}: epoch {x}..{y} len {L} > n + m")
    if tr0 > bound * (n + m): st.bad("COR", f"{name}: phase {a}..{b}")
    # runs and prefix
    runs = []; s = a
    for k in range(a, b):
        if fbs[k]:
            runs.append((s, k)); s = k + 1
    runs.append((s, b))
    for (p, q) in runs:   # states p..q, transitions p..q-1 all non-fallback in-phase
        us = [info[k]["unsplit"] for k in range(p, q + 1)]
        st.inc("PREFIX_checks")
        if any(us[i + 1] and not us[i] for i in range(len(us) - 1)): st.bad("PREFIX", f"{name}: run {p}..{q}")
    # levels (small n)
    lev = {}
    if n <= LEVELMAX:
        Et = info[a]["Et"]; cyc = {u for u in range(n) if info[a]["lam"][u] == u}
        best = path_max(g, Et, states[a][1], cyc)
        B = [max((bb for bb in best[x] if bb is not None), default=None) for x in range(n)]
        for k in range(a, b + 1):
            if not info[k]["unsplit"]: continue
            W = info[k]["W"]; lv = level(Et, W, best, n); lev[k] = lv
            st.inc("BASE_checks")
            if lv < 0: st.bad("BASE", f"{name}@{k}")
            st.inc("UB_checks")
            if any(B[x] is not None and Et.key(W[x]) > B[x] for x in range(n)): st.bad("UB", f"{name}@{k}: W > B")
            if lv == n - 1 and any(B[x] is not None and Et.key(W[x]) != B[x] for x in range(n)): st.bad("SATB", f"{name}@{k}")
        for k in range(a, b):
            if fbs[k] or k not in lev or k + 1 not in lev: continue
            st.inc("STEP2_checks")
            if lev[k + 1] < lev[k]: st.bad("STEP2", f"{name}@{k}: {lev[k]} -> {lev[k + 1]}")
            if info[k]["d0"]:
                need = n - 1 if MUT == "full" else min(lev[k] + (2 if MUT == "step2" else 1), n - 1)
                st.inc("STEP1_checks")
                if lev[k] < n - 1: st.inc("STEP1_strict")
                if lev[k + 1] < n - 1: st.inc("STEP1_nonsat")
                if lev[k + 1] < need: st.bad("STEP1", f"{name}@{k}: {lev[k]} -> {lev[k + 1]}")
        # saturation
        sat = [k for k in range(a, b + 1) if info[k]["d0"] and k in lev and lev[k] == n - 1]
        if sat:
            t = sat[0]; ts = max(k for k in range(a, b + 1) if info[k]["d0"])
            st.inc("SAT_phases")
            for k in range(t, b + 1):
                if info[k]["d0"] and any(info[k]["Et"].key(info[k]["vs"][x]) != B[x] for x in range(n)): st.bad("SAT", f"{name}@{k}: Xi != B")
            if ts - t > 4 * n * (n - 1): st.bad("SAT", f"{name}: t* - t {ts - t}")
        else:
            t = b + 1
        # kinds of epoch-last transitions with source < t
        kinds = {"i": 0, "ii": {}, "iii": {}}
        for x, y in d0eps:
            if y >= t or y == b: continue
            if fbs[y]: kinds["i"] += 1; continue
            run = next(r for r in runs if r[0] <= y < r[1])
            if info[y + 1]["unsplit"]: kinds["iii"][run] = kinds["iii"].get(run, 0) + 1
            else: kinds["ii"][run] = kinds["ii"].get(run, 0) + 1
        st.inc("KIND_phases")
        if kinds["i"] > f or any(v > 1 for v in kinds["ii"].values()) or any(v > n - 1 for v in kinds["iii"].values()):
            st.bad("KIND", f"{name}: phase {a}..{b} {kinds}")
        mx = max(kinds["iii"].values(), default=0)
        if mx > st.c.get("max_kind_iii_per_run", 0): st.c["max_kind_iii_per_run"] = mx

def starts(g, r, rng):
    if r == 0: return list(Engine(g).initial("best")), list(Engine(DC.dual(g)).initial("best"))
    return [rng.choice(g.succ[v]) for v in range(g.n)], [rng.choice(g.succ[v]) for v in range(g.n)]

def run_game(g, s, t, st, name):
    states, fbs = DC.Runner(g).run(s, t)
    st.inc("runs")
    analyse(g, states, [bool(x) for x in fbs], st, name)

def main():
    st = Stats(); a = sys.argv[1:]
    if a[0] == "files":
        runs = int(a[2]) if len(a) > 2 else 3; rng = random.Random(7); cap = int(os.environ.get("MAXN", "64"))
        for path in [l.strip() for l in open(a[1]) if l.strip()]:
            g = pg.read(os.path.join(DC.ROOT, path))
            if g.n > cap: st.inc("skipped_n_gt_cap"); continue
            for r in range(runs):
                s, t = starts(g, r, rng); run_game(g, s, t, st, f"{path}#{r}")
    elif a[0] == "random":
        N, nmin, nmax, seed = map(int, a[1:5]); kind = a[5]; k = int(a[6]) if len(a) > 6 else 2; rng = random.Random(seed)
        for i in range(N):
            g = DC.rand_game(rng, rng.randint(nmin, nmax), kind)
            for r in range(k + 1):
                s, t = starts(g, r, rng); run_game(g, s, t, st, f"random{seed}:{i}#{r}")
    print("MODE", " ".join(a), "MUT", MUT or "-", "LEVELMAX", LEVELMAX)
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for v in st.viol[:30]: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c.get("VIOLATIONS") else "OK", f"violations={st.c.get('VIOLATIONS', 0)}")

if __name__ == "__main__":
    main()
