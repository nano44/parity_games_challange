#!/usr/bin/env python3
"""REFEREE succ. 16: own simulator of P-N5-GCX-box21 §4 model ABS (sha1 5a91bebb), written from the packet text only. No lane code.
Non-terminals 0..n-1, terminals n..n+k-1 with constants h <= T. Integer weights w(v). Strategy s valid iff its functional graph on V is
acyclic. M_s(v) = sum of w on v's play + h(end), N_s the same with T. Step: arena Al(v) = {s(v)} u {y : M_s(y) > M_s(s(v))};
N* = pointwise greatest N over valid arena strategies (brute force over arena strategies; the run stops, NOGREATEST, if none exists);
C(v) = {y in Al(v) : w(v) + N*(y) = N*(v)}; the tie rule R picks s'(v) in C(v) from (Al(v), values, s(v)); if the picked strategy is
invalid (zero-weight tight cycle) the run stops (RULEINVALID).
Checks: HEIGHT (acyclic; rules basic, basicM): fixed after <= height steps.   TIE (acyclic; every rule): fixed after <= D = max path sum deg,
and each v constant from t_v = deg(v) + max_y t_y.   LOC (every model, every rule): s_{t+2}(v) != s_{t+1}(v) => some successor y with
M_t(y) != M_{t+1}(y) or N_{t+1}(y) != N_{t+2}(y) or viability for v changed (s_{t+1} vs s_{t+2}).   MONO, MONOSUCC, NORETURN (§4 remarks).
Usage: abs_model.py N nmin nmax seed [cyclic 0/1]"""
import sys, random, itertools, zlib
from collections import Counter

EX = []


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 30: EX.append((key,) + info)


class Abs:
    def __init__(self, n, succ, w, h, T):
        self.n, self.succ, self.w, self.h, self.T = n, succ, w, h, T

    def term(self, y): return y >= self.n

    def play(self, s, v):
        seq = []; x = v; seen = set()
        while not self.term(x):
            if x in seen: return None
            seen.add(x); seq.append(x); x = s[x]
        return seq, x

    def vals(self, s):
        M, N = {}, {}
        for v in range(self.n):
            p = self.play(s, v)
            if p is None: return None
            seq, e = p
            M[v] = sum(self.w[u] for u in seq) + self.h[e - self.n]; N[v] = sum(self.w[u] for u in seq) + self.T[e - self.n]
        for e in range(self.n, self.n + len(self.h)): M[e] = self.h[e - self.n]; N[e] = self.T[e - self.n]
        return M, N

    def viable(self, s, v, y):
        if self.term(y): return True
        p = self.play(s, y)
        return p is not None and v not in p[0]


def rule_pick(name, v, C, Al, cur, M, N):
    C = sorted(C)
    if name == "basic": return cur if cur in C else C[0]
    if name == "basicM": return cur if cur in C else max(C, key=lambda y: (M[y], -y))
    if name == "lowidx": return C[0]
    if name == "anti":
        o = [y for y in C if y != cur]
        return o[0] if o else cur
    if name == "sizedep":
        return min(C, key=lambda y: (M[y], y)) if len(Al) >= 3 else max(C, key=lambda y: (M[y], -y))
    if name == "hash":
        key = repr((sorted(Al), cur, sorted((y, M[y], N[y]) for y in Al))).encode()
        return C[zlib.crc32(key) % len(C)]
    raise ValueError(name)


RULES = ["basic", "basicM", "lowidx", "anti", "sizedep", "hash"]


def step(g, s, rule, cnt):
    MN = g.vals(s); M, N = MN
    Al = {v: sorted({s[v]} | {y for y in g.succ[v] if M[y] > M[s[v]]}) for v in range(g.n)}
    best = None; Nstar = None
    for choice in itertools.product(*[Al[v] for v in range(g.n)]):
        vv = g.vals(list(choice))
        if vv is None: continue
        Nc = vv[1]
        if Nstar is None: Nstar = dict(Nc)
        else:
            for x in range(g.n): Nstar[x] = max(Nstar[x], Nc[x])
    # greatest exists?
    ok = False
    for choice in itertools.product(*[Al[v] for v in range(g.n)]):
        vv = g.vals(list(choice))
        if vv is not None and all(vv[1][x] == Nstar[x] for x in range(g.n)): ok = True; break
    if not ok: return None, "NOGREATEST", Al
    for e in range(g.n, g.n + len(g.h)): Nstar[e] = g.T[e - g.n]
    C = {v: [y for y in Al[v] if g.w[v] + Nstar[y] == Nstar[v]] for v in range(g.n)}
    s2 = [rule_pick(rule, v, C[v], Al[v], s[v], M, N) for v in range(g.n)]
    vv = g.vals(s2)
    if vv is None or any(vv[1][x] != Nstar[x] for x in range(g.n)): return None, "RULEINVALID", Al
    return s2, "OK", Al


def gen(r, n, cyclic):
    k = r.randint(1, 4)
    succ = []
    for v in range(n):
        cands = list(range(v + 1, n)) if not cyclic else [x for x in range(n) if x != v]
        cands += list(range(n, n + k))
        d = r.randint(1, min(4, len(cands)))
        succ.append(r.sample(cands, d))
    w = [r.randint(-3, 3) for _ in range(n)]
    h = [r.randint(-4, 4) for _ in range(k)]
    T = [x + r.randint(0, 4) for x in h]
    return Abs(n, succ, w, h, T)


def start(g, r, cyclic):
    for _ in range(200):
        s = [r.choice(g.succ[v]) for v in range(g.n)]
        if g.vals(s) is not None: return s
    return None


def analyse(g, s0, rule, cyclic, cnt, name):
    seq = [s0]; status = "OK"
    for _ in range(4 * (g.n + sum(len(x) for x in g.succ)) + 10):
        s2, status, _ = step(g, seq[-1], rule, cnt)
        if s2 is None: cnt[status] += 1; break
        seq.append(s2)
        if s2 == seq[-2]: break
    else:
        cnt["NOFIX_" + ("cyc" if cyclic else "acyc")] += 1
        if not cyclic: fail(cnt, "ACYC_NOFIX", name, rule)
    vals = [g.vals(s) for s in seq]
    T = len(seq) - 1
    fixed = next((t for t in range(T) if seq[t + 1] == seq[t]), None)
    if not cyclic and status == "OK" and fixed is not None:
        memo = {}
        def ht(v):
            if v not in memo: memo[v] = 1 + max([ht(y) for y in g.succ[v] if not g.term(y)] + [0])
            return memo[v]
        tv = {}
        def tc(v):
            if v not in tv: tv[v] = len(g.succ[v]) + max([tc(y) for y in g.succ[v] if not g.term(y)] + [0])
            return tv[v]
        H = max(ht(v) for v in range(g.n)); Dd = max(tc(v) for v in range(g.n))
        cnt["FIX_runs"] += 1; cnt["MAX_fix_minus_H_" + rule] = max(cnt["MAX_fix_minus_H_" + rule], fixed - H + 100)
        if rule in ("basic", "basicM"):
            cnt["HEIGHT_chk"] += 1
            if fixed > H: fail(cnt, "HEIGHT", name, rule, fixed, H)
        cnt["TIE_chk"] += 1
        if fixed > Dd: fail(cnt, "TIE", name, rule, fixed, Dd)
        if fixed > H: cnt["TIE_beyond_height_" + rule] += 1
        for v in range(g.n):
            for t in range(tc(v), T):
                if seq[t + 1][v] != seq[t][v]: fail(cnt, "TIE_v", name, rule, v, t, tc(v)); break
    # LOC
    for t in range(T - 1):
        M0, N0 = vals[t]; M1, N1 = vals[t + 1]; M2, N2 = vals[t + 2]
        for v in range(g.n):
            if seq[t + 2][v] == seq[t + 1][v]: continue
            cnt["LOC_chk_" + rule] += 1
            ok = any(M0[y] != M1[y] or N1[y] != N2[y] or g.viable(seq[t + 1], v, y) != g.viable(seq[t + 2], v, y) for y in g.succ[v])
            if not ok: fail(cnt, "LOC_" + rule, name, t, v)
    # remarks
    for t in range(T):
        M0, N0 = vals[t]; M1, N1 = vals[t + 1]
        for v in range(g.n):
            cnt["MONO_chk"] += 1
            if M1[v] < M0[v] or N1[v] < N0[v]: fail(cnt, "MONO", name, rule, t, v)
            if M1[seq[t + 1][v]] < M0[seq[t][v]]: fail(cnt, "MONOSUCC", name, rule, t, v)
    for v in range(g.n):
        for t1 in range(T):
            if seq[t1 + 1][v] == seq[t1][v]: continue
            y = seq[t1][v]
            for t2 in range(t1 + 2, T + 1):
                if seq[t2][v] == y:
                    cnt["NORET_chk"] += 1
                    if not vals[t2][0][y] > vals[t1][0][y]: fail(cnt, "NORETURN", name, rule, v, t1, t2)
                    break


def main(a):
    N, lo, hi, seed = map(int, a[:4]); cyclic = int(a[4]) if len(a) > 4 else 0
    r = random.Random(seed); cnt = Counter()
    for i in range(N):
        g = gen(r, r.randint(lo, hi), cyclic)
        s0 = start(g, r, cyclic)
        if s0 is None: cnt["nostart"] += 1; continue
        for rule in RULES:
            cnt["RUNS"] += 1; analyse(g, s0, rule, cyclic, cnt, "g%d" % i)
    for k in sorted(cnt):
        v = cnt[k] - 100 if k.startswith("MAX_fix_minus_H") else cnt[k]
        print(k, v)
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
