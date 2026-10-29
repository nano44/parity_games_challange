#!/usr/bin/env python3
"""REFEREE succ. 17 probe for packet P-N5-TOPSHAPE (docs/new/P-N5-TOPSHAPE-box49.md, sha1 c5b0e8d8..., freeze l-new 4c2ea43e). Own engine
only (rl_engine). No lane code. Per phase ((lambda_Xi, tau) constant), every vertex v, every transition with P_t != P_{t+1}:
 DELTA  weight(P_{t+1}) > weight(P_t) iff the top d of P_t ^ P_{t+1} is even and in P_{t+1}, or odd and in P_t  (and the rise is strict: MON + INJ)
 A      top rises only to an even rank;   B  an even top never falls;   C  once even, stays even
 COR    top changes per (v, phase) <= n - 1;  also the shape: distinct tops = decreasing odd run, optional bottom, increasing even run
 stats  max P-changes per (v, phase); max top changes; Delta-top rises (TOP-MONO in the Delta form, DEAD in the packet)
Ranks are positions in V sorted by (priority, index) (SPEC S1); a rank is even/odd as the priority of its vertex; bottom = -1.
Mutations: MUT=1 (a) demanded with ODD;  MUT=2 COR bound n - 2;  MUT=3 TOP-MONO in the Delta form demanded (non-increasing Delta-tops).
Usage: topshape_probe.py rand N nmin nmax kmax seed | files...  (RANDSTARTS 2, MAXN 200; TRACE=v:phase_start prints the Delta-tops)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, dual_probe as D, core_probe as CP
EX = []
MUT = int(os.environ.get("MUT", "0"))


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 30: EX.append((key,) + info)


def top(mask): return mask.bit_length() - 1   # -1 = bottom


def analyse(g, start, cnt, name):
    st = RE.run(g, start); n = g.n
    even = lambda r: g.prio[g.byrank[r]] % 2 == 0
    T = len(st); k = 0
    while k < T:
        j = k; lam = tuple(v[0] for v in st[k]["Xi"])
        while j + 1 < T and tuple(v[0] for v in st[j + 1]["Xi"]) == lam and st[j + 1]["t"] == st[k]["t"]: j += 1
        if j > k: phase(g, st, k, j, cnt, name, even)
        k = j + 1


def phase(g, st, a, b, cnt, name, even):
    n = g.n; cnt["PHASES"] += 1
    tr = os.environ.get("TRACE")
    for v in range(n):
        tops = [top(st[t]["Xi"][v][1]) for t in range(a, b + 1)]
        pch = 0; tch = 0; dtops = []; seen_even = False; distinct = [tops[0]]
        for i, t in enumerate(range(a, b)):
            A, B = st[t]["Xi"][v][1], st[t + 1]["Xi"][v][1]
            if st[t]["Xi"][v][0] != st[t + 1]["Xi"][v][0]: fail(cnt, "CNODE", name, t, v)
            if A == B: continue
            pch += 1; cnt["PCH"] += 1
            d = top(A ^ B); dtops.append(d)
            wA, wB = g.weight(A), g.weight(B)
            pred = (even(d) and (B >> d) & 1) or (not even(d) and (A >> d) & 1)
            cnt["DELTA_chk"] += 1
            if (wB > wA) != bool(pred): fail(cnt, "DELTA", name, t, v)
            if not wB > wA: fail(cnt, "STRICT", name, t, v)
            t0, t1 = tops[i], tops[i + 1]
            if t1 > t0:
                cnt["A_chk"] += 1
                if (even(t1) if MUT == 1 else not even(t1)): fail(cnt, "A" + ("_MUT1" if MUT == 1 else ""), name, t, v, t0, t1)
            if t0 >= 0 and even(t0):
                cnt["B_chk"] += 1
                if t1 < t0: fail(cnt, "B", name, t, v, t0, t1)
            if t0 >= 0 and even(t0): seen_even = True
            if seen_even and not (t1 >= 0 and even(t1)): fail(cnt, "C", name, t, v)
            if t1 != t0: tch += 1; distinct.append(t1)
        if pch:
            cnt["VP_chk"] += 1
            cnt["MAX_PCH"] = max(cnt["MAX_PCH"], pch); cnt["MAX_TCH"] = max(cnt["MAX_TCH"], tch)
            bound = n - 2 if MUT == 2 else n - 1
            if tch > bound: fail(cnt, "COR" + ("_MUT2" if MUT == 2 else ""), name, a, v, tch)
            # shape: odd strictly decreasing, then optional bottom, then even strictly increasing
            i = 0
            while i < len(distinct) and distinct[i] >= 0 and not even(distinct[i]): i += 1
            odd_run = distinct[:i]; rest = distinct[i:]
            if rest and rest[0] == -1: rest = rest[1:]
            ok = all(odd_run[x] > odd_run[x + 1] for x in range(len(odd_run) - 1)) and \
                 all(r >= 0 and even(r) for r in rest) and all(rest[x] < rest[x + 1] for x in range(len(rest) - 1))
            if not ok: fail(cnt, "SHAPE", name, a, v, distinct)
            rises = sum(1 for x in range(len(dtops) - 1) if dtops[x + 1] > dtops[x])
            cnt["MAX_DTOP_RISES"] = max(cnt["MAX_DTOP_RISES"], rises)
            if MUT == 3 and rises: fail(cnt, "TOPMONO_MUT3", name, a, v, rises)
            if tch == n - 1: cnt["COR_sharp"] += 1
            cnt["MAX_TCH_x100_over_n"] = max(cnt["MAX_TCH_x100_over_n"], 100 * tch // n)
            if tr and tr == "%d:%d" % (v, a):
                print("TRACE", name, "v", v, "phase", (a, b), "P-changes", pch, "top changes", tch, "rises of Delta-top", rises)
                print("TRACE Delta-tops", dtops[:20]); print("TRACE distinct tops", distinct)


def main(a):
    cnt = Counter(); rng = random.Random(4949); nst = int(os.environ.get("RANDSTARTS", "2"))
    def do(g, name, r, extra=None):
        starts = ([extra] if extra else []) + ([RE.best_reward_start(g)] if (not extra or nst > 0) else []) + \
                 [D.rand_start(g, r) for _ in range(nst)]
        for j, s0 in enumerate(starts):
            cnt["RUNS"] += 1; analyse(g, s0, cnt, "%s/%d" % (name, j))
    if a[0] == "rand":
        N, lo, hi, km, seed = map(int, a[1:6]); r2 = random.Random(seed)
        for i in range(N):
            nn = r2.randint(lo, hi)
            do(D.rand_ck(r2, nn, r2.randint(0, min(km, nn - 1))), "rand%d" % i, rng)
    else:
        for path in a:
            if path.endswith(".start"): continue
            try: g = RE.parse(path)
            except Exception: cnt["parse_err"] += 1; continue
            if g.n > int(os.environ.get("MAXN", "200")): cnt["skip_big"] += 1; continue
            sp = path[:-3] + ".start"
            ex = CP.parse_start(g, sp) if os.path.exists(sp) else None
            cnt["GAMES"] += 1; do(g, os.path.relpath(path), random.Random(os.path.relpath(path)), ex)
    for k in sorted(cnt): print(k, cnt[k])
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
