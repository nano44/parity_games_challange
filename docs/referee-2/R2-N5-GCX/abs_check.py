#!/usr/bin/env python3
r"""REFEREE-2 successor 18 (Opus 5.5, D15): the abstract model ABS of P-N5-GCX-box21 §4 (sha1 5a91bebb), written from the packet's
definitions (lane code experiments/si/*gcx*, abscyc.py NOT run or imported).
Model: non-terminals 0..n-1, terminals T0..; weights w(v) and terminal constants h <= T in Z x Z (lexicographic tuples); a strategy s picks
s(v) in succ(v); VALID iff every play reaches a terminal; M_s, N_s = path weight + h / T of the end terminal.
Step from valid s: arena Al_s(v) = {s(v)} u {y : M_s(y) > M_s(s(v))}; s' = a valid arena strategy whose N is pointwise maximal (brute force over
all arena strategies; a run stops, counted NOPT, if no pointwise maximum exists); among the optimal strategies the tie rule picks per vertex:
  basic : keep s(v) if it is an N-maximiser over the viable arena successors, else the smallest-index one
  rule R: any deterministic function of (arena, values, current choice): here ten random tables keyed by those inputs, and the packet-breaking
          rule "smallest-index maximiser, but the LARGEST-index one when the current choice is a maximiser" (rule 'flip')
(the per-vertex choice must give an optimal valid strategy; if not, counted NOTJOINT and the run stops).
Checks: HEIGHT (acyclic, basic: fixed after <= height steps), TIE (acyclic, any rule: fixed after <= max path sum of degrees), LOC (cyclic and
acyclic, basic; and for 'flip' / random rules COUNTED as LOCFAIL, expected to fail), LOCP (repaired LOC' for every rule: a
change at t+1 -> t+2 with no successor change needs s_{t+1}(v) != s_t(v)), MONO, MONOSUCC, NORET.
Usage: abs_check.py random N nmin nmax seed [cyclic 0|1]  |  example   (the explicit LOC counterexample)"""
import sys, random, itertools

def addv(a, b): return (a[0] + b[0], a[1] + b[1])


class Model:
    def __init__(s, n, succ, w, h, T):
        s.n, s.succ, s.w, s.h, s.T = n, succ, w, h, T   # succ[v]: list of ints (< n non-terminal, >= n terminal n+i)

    def isterm(s, y): return y >= s.n

    def values(s, st):
        """(M, N) of every non-terminal, or None if st is not valid."""
        M, N = {}, {}
        for v in range(s.n):
            seen, x, mw = set(), v, (0, 0)
            while not s.isterm(x):
                if x in seen: return None
                seen.add(x); mw = addv(mw, s.w[x]); x = st[x]
            M[v] = addv(mw, s.h[x - s.n]); N[v] = addv(mw, s.T[x - s.n])
        return M, N

    def val(s, V, y, which):
        if s.isterm(y): return s.h[y - s.n] if which == 0 else s.T[y - s.n]
        return V[which][y]

    def viable(s, st, v, y):
        x, seen = y, set()
        while not s.isterm(x):
            if x == v or x in seen: return False
            seen.add(x); x = st[x]
        return True


def step(m, st, rule, table):
    V = m.values(st)
    Al = []
    for v in range(m.n):
        cur = st[v]; mc = m.val(V, cur, 0)
        Al.append([cur] + [y for y in m.succ[v] if y != cur and m.val(V, y, 0) > mc])
    best, cands = None, []
    for choice in itertools.product(*Al):
        W = m.values(choice)
        if W is None: continue
        cands.append((choice, W))
    # pointwise maximum of N
    top = None
    for choice, W in cands:
        if all(all(W[1][v] >= W2[1][v] for v in range(m.n)) for _, W2 in cands):
            top = W; break
    if top is None: return None, "NOPT", Al, V
    opt = [c for c, W in cands if W[1] == top[1]]
    new = []
    for v in range(m.n):
        maxs = sorted(set(c[v] for c in opt))   # the N-maximisers at v realisable in an optimal strategy
        cur = st[v]
        if rule == "basic":
            y = cur if cur in maxs else maxs[0]
        elif rule == "flip":
            y = maxs[-1] if cur in maxs else maxs[0]
        else:
            key = (tuple(Al[v]), tuple(m.val(V, z, 1) for z in Al[v]), cur)
            y = maxs[table(v, key) % len(maxs)]
        new.append(y)
    new = tuple(new)
    if new not in opt: return None, "NOTJOINT", Al, V
    return new, None, Al, V


def height(m, v, memo):
    if m.isterm(v): return 0
    if v in memo: return memo[v]
    memo[v] = 1 + max(height(m, y, memo) for y in m.succ[v]); return memo[v]


def degsum(m, v, memo):
    if m.isterm(v): return 0
    if v in memo: return memo[v]
    memo[v] = len(m.succ[v]) + max(degsum(m, y, memo) for y in m.succ[v]); return memo[v]


def rand_model(rng, n, cyclic):
    nt = rng.randint(1, 3)
    succ = []
    for v in range(n):
        cand = list(range(v + 1, n)) + [n + i for i in range(nt)] if not cyclic else [x for x in range(n) if x != v] + [n + i for i in range(nt)]
        k = rng.randint(1, min(3, len(cand)))
        succ.append(sorted(rng.sample(cand, k)))
    w = [(rng.randint(-2, 2), rng.randint(-1, 1)) for _ in range(n)]
    h, T = [], []
    for _ in range(nt):
        a = (rng.randint(-3, 3), rng.randint(-1, 1)); b = (rng.randint(0, 2), rng.randint(-1, 1))
        T.append(addv(a, b) if addv(a, b) >= a else a); h.append(a)
    return Model(n, succ, w, h, T)


def run(m, st0, rule, table, cnt, acyclic, name):
    seq = [tuple(st0)]
    Vs = []
    for it in range(4 * m.n * 4 + 10):
        new, err, Al, V = step(m, seq[-1], rule, table)
        Vs.append(V)
        if err: cnt[err] = cnt.get(err, 0) + 1; return
        seq.append(new)
        if new == seq[-2]: break
    else:
        cnt["NOFIX"] = cnt.get("NOFIX", 0) + 1; return
    Vs.append(m.values(seq[-1]))
    cnt["runs"] = cnt.get("runs", 0) + 1
    fix = len(seq) - 2       # first index t with s_{t+1} = s_t
    tag = rule if rule in ("basic", "flip") else "rand"
    if acyclic:
        H = max(height(m, v, {}) for v in range(m.n)); Dm = max(degsum(m, v, {}) for v in range(m.n))
        if rule == "basic" and fix > H: bad(cnt, "HEIGHT", name)
        if fix > Dm: bad(cnt, "TIE_" + tag, name)
        cnt["max_fix_over_height_" + tag] = max(cnt.get("max_fix_over_height_" + tag, -99), fix - H)
    for t in range(len(seq)):
        for v in range(m.n):
            if t >= 1:
                if Vs[t][0][v] < Vs[t - 1][0][v] or Vs[t][1][v] < Vs[t - 1][1][v]: bad(cnt, "MONO", name)
                if m.val(Vs[t], seq[t][v], 0) < m.val(Vs[t - 1], seq[t - 1][v], 0): bad(cnt, "MONOSUCC", name)
            if t + 2 < len(seq) and seq[t + 2][v] != seq[t + 1][v]:
                cnt["LOC_events_" + tag] = cnt.get("LOC_events_" + tag, 0) + 1
                ok = False
                for y in m.succ[v]:
                    if m.val(Vs[t], y, 0) != m.val(Vs[t + 1], y, 0) or m.val(Vs[t + 1], y, 1) != m.val(Vs[t + 2], y, 1): ok = True
                    if not m.isterm(y) and m.viable(seq[t + 1], v, y) != m.viable(seq[t + 2], v, y): ok = True
                if not ok:
                    if rule == "basic": bad(cnt, "LOC", name + f" t={t} v={v}")
                    else: cnt["LOCFAIL_" + tag] = cnt.get("LOCFAIL_" + tag, 0) + 1
                    # repaired LOC' (any deterministic rule): ... or s_{t+1}(v) != s_t(v)
                    if seq[t + 1][v] == seq[t][v]: bad(cnt, "LOCP", name + f" t={t} v={v} rule={rule}")
    # NO-RETURN: v leaves y at t1, holds y again at t2 > t1 => M_t2(y) > M_t1(y)
    for v in range(m.n):
        for t1 in range(len(seq) - 1):
            y = seq[t1][v]
            if seq[t1 + 1][v] == y: continue
            for t2 in range(t1 + 1, len(seq)):
                if seq[t2][v] == y:
                    if not m.val(Vs[t2], y, 0) > m.val(Vs[t1], y, 0): bad(cnt, "NORET", name)
                    cnt["NORET_checks"] = cnt.get("NORET_checks", 0) + 1
                    break


def bad(cnt, k, msg):
    cnt["VIOLATIONS"] = cnt.get("VIOLATIONS", 0) + 1; cnt["V_" + k] = cnt.get("V_" + k, 0) + 1
    if cnt.setdefault("_ex", []) and len(cnt["_ex"]) > 20: return
    cnt["_ex"].append(f"{k}: {msg}")


def main():
    a = sys.argv[1:]; cnt = {"_ex": []}
    if a[0] == "example":
        # v = 0 with three terminal successors y0 = T0 (h 0, T 0), y1 = T1 (h 1, T 5), y3 = T2 (h 2, T 5); start s(0) = T0
        m = Model(1, [[1, 2, 3]], [(0, 0)], [(0, 0), (1, 0), (2, 0)], [(0, 0), (5, 0), (5, 0)])
        for rule in ("basic", "flip"):
            seq = [(1,)]
            for _ in range(4):
                new, err, Al, V = step(m, seq[-1], rule, None)
                print(rule, "state", len(seq) - 1, "s(v) =", seq[-1][0], "arena", Al[0], "-> s'(v) =", new[0])
                seq.append(new)
            print(rule, "choices:", [x[0] for x in seq])
        return
    N, nmin, nmax, seed = map(int, a[1:5]); cyclic = len(a) > 5 and a[5] == "1"
    rng = random.Random(seed)
    for i in range(N):
        n = rng.randint(nmin, nmax)
        m = rand_model(rng, n, cyclic)
        st0 = [rng.choice(m.succ[v]) for v in range(n)]
        if m.values(st0) is None:
            # make a valid start: point every vertex to a terminal successor if it has one, else skip
            if cyclic: cnt["invalid_start"] = cnt.get("invalid_start", 0) + 1; continue
        rules = ["basic", "flip"] + [f"r{j}" for j in range(3)]
        for rule in rules:
            sd = rng.randrange(1 << 30)
            table = (lambda v, key, sd=sd: hash((sd, v, key)) & 0xffffff)
            run(m, st0, rule, table, cnt, not cyclic, f"{seed}:{i}:{rule}")
    ex = cnt.pop("_ex")
    print("MODE", " ".join(a))
    for k in sorted(cnt): print(f"{k}: {cnt[k]}")
    for e in ex: print("VIOLATION", e)
    print("RESULT", "FAIL" if cnt.get("VIOLATIONS") else "OK", f"violations={cnt.get('VIOLATIONS', 0)}")


if __name__ == "__main__":
    main()
