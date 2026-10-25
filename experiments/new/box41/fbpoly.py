#!/usr/bin/env python3
"""Box 41: data for docs/new/N5-FBPOLY-box41.md (in-phase Even fallbacks per phase on 𝒞^1O). Per phase: U = λ^{-1}(c_θ), T = {o, c_θ},
κ_t(z) = (signed weight of P(Ξ_t z), s_θ·ℓ) (= E.key(Ξ_t z)[1:]), g_j = j-th in-phase Even fallback, θ-runs.
At every in-phase Even fallback k (S = switched Even vertices):
- CN: S ∩ (U ∖ T) = ∅. Check (CNa) every v ∈ S is a cycle node of Ξ_k, (CNb) every gate (y, z) has lev −1, (CNc) k + 1 is the last
  state of the phase. FAIL_CN*.
- UT: S ∩ (U ∖ T) ≠ ∅. For u ∈ S ∩ (U ∖ T), x* = σ_{k+1}(u): follow the honest play at k from x* to the first vertex in {u} ∪ T:
  'loop' (u first), 'ct' (c_θ first), 'o' (o first). (GS) some u is not 'loop'. FAIL_GS otherwise.
  (HF) 'ct' only at fallbacks g_j with j ≤ |U| − 2. (PF) 'o' only at the first |U| − 2 fallbacks of the θ-run. (UT-POS) a UT fallback
  after g_{|U|−2} is among the first |U| − 2 fallbacks of its θ-run.
- TH: θ-changes at transitions t → t+1, t > g_{|U|−2}: ≤ deg(o) + |U| − 2. BOUND: #fallbacks ≤ 1 + (|U| − 2)(deg(o) + |U|) (o ≠ c_θ),
  ≤ 1 + (|U| − 1) (o = c_θ).
DATA only. Usage: fbpoly.py game.pg ... | --rand N nlo nhi seed [starts]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "box39")); sys.path.insert(0, os.path.join(HERE, "..", "box38"))
from neb_run import *

KMAX = int(os.environ.get("KMAX", "12"))
def fail(acc, k, *info): bump(acc, k); print(k, *info, flush=True)

def analyse(g, acc, name, s0=None):
    rows, o, E = trace(g, s0); N = len(rows); n = g.n; bump(acc, "runs")
    sb = [E.evaluate(tuple(r["s"]))[1] for r in rows]
    a = 0
    while a < N:
        b = a
        while b + 1 < N and rows[b + 1]["ph"] == rows[a]["ph"]: b += 1
        Xi0 = rows[a]["Xi"]; ct = Xi0[o][0]; U = {z for z in range(n) if Xi0[z][0] == ct}; T = {o, ct}; u = len(U)
        dego = len(set(g.succ[o]) & U)
        kap = lambda t, z: E.key(rows[t]["Xi"][z])[1:]
        fbs = [k for k in range(a, b) if rows[k]["fb"] and rows[k]["t"] == rows[k + 1]["t"] and rows[k]["s"] != rows[k + 1]["s"]]
        bump(acc, "phases"); bump(acc, "fallbacks", len(fbs))
        # θ-run index of each fallback
        run_id, rid = {}, 0
        for t in range(a, b + 1):
            if t > a and rows[t]["th"] != rows[t - 1]["th"]: rid += 1
            run_id[t] = rid
        cnt_in_run = {}
        for j, k in enumerate(fbs, 1):
            r = run_id[k]; cnt_in_run[r] = cnt_in_run.get(r, 0) + 1; jt = cnt_in_run[r]
            s, s1 = rows[k]["s"], rows[k + 1]["s"]; S = [v for v in range(n) if g.owner[v] == 0 and s[v] != s1[v]]
            nxt = lambda z: s[z] if g.owner[z] == 0 else sb[k][z]
            SU = [v for v in S if v in U and v not in T]
            if not SU:
                bump(acc, "CN_fallbacks")
                if any(rows[k]["Xi"][v][0] != v for v in S): fail(acc, "FAIL_CNa", name, k)
                Xi = rows[k]["Xi"]
                for v in S:
                    for w in set(g.succ[v]):
                        if w != s[v] and E.key(Xi[w]) > E.key(Xi[s[v]]):
                            if not (Xi[w][0] == Xi[s[v]][0] and Xi[w][1] == Xi[s[v]][1]): fail(acc, "FAIL_CNb", name, k, v, w)
                if k + 1 != b: fail(acc, "FAIL_CNc", name, k, b)
                continue
            bump(acc, "UT_fallbacks"); kinds = []
            for v in SU:
                z, seen = s1[v], set()
                while z not in T and z != v:
                    assert z not in seen and z in U; seen.add(z); z = nxt(z)
                kd = "loop" if z == v and z not in T else ("ct" if z == ct else "o")
                kinds.append(kd); bump(acc, "UT_kind_" + kd)
                if kd == "ct" and j > u - 2: fail(acc, "FAIL_HF", name, k, v, j, u)
                if kd == "o" and jt > u - 2: fail(acc, "FAIL_PF", name, k, v, jt, u)
            if all(kd == "loop" for kd in kinds): fail(acc, "FAIL_GS", name, k)
            if j > u - 2:
                bump(acc, "UT_after_hatfreeze")
                if jt > u - 2: fail(acc, "FAIL_UTPOS", name, k)
        # κ lower bounds directly (|U| ≤ KMAX): (KH) t > g_j, z ∈ Û: κ_t(z) ≥ best κwt over simple paths of G_Û to c_θ with ≤ j edges;
        # (KP) t in a θ-run after its j-th fallback, z ∈ U ∖ {c_θ}: κ_t(z) ≥ best κwt over simple paths of G_{U∖{c_θ}} to o, ≤ j edges, + κ(θ).
        if 3 <= u <= KMAX and fbs and o != ct:
            sth = 1 if E.par[ct] == 1 else -1; hi = E.rank[ct]
            kw = lambda v: ((E.weight(E.bit[v]) if E.rank[v] > hi else 0), sth)
            add = lambda x, y: (x[0] + y[0], x[1] + y[1])
            def best(nodes, end, jmax):
                bst = [dict() for _ in range(jmax + 1)]
                def dfs(x, seen, w, d, z):
                    if x == end:
                        for jj in range(d, jmax + 1):
                            if bst[jj].get(z) is None or w > bst[jj][z]: bst[jj][z] = w
                        return
                    if d == jmax: return
                    for y in (set(g.succ[x]) if g.owner[x] == 0 else {g.succ[x][0]}):
                        if y in nodes and y not in seen: dfs(y, seen | {y}, add(w, kw(x)), d + 1, z)
                for z in nodes: dfs(z, {z}, (0, 0), 0, z)
                return bst
            jm = min(u - 2, len(fbs)); bh = best(U - {o}, ct, jm)
            for j in range(1, jm + 1):
                for t in range(fbs[j - 1] + 1, b + 1):
                    for z in U - {o}:
                        if bh[j].get(z) is not None:
                            bump(acc, "KH_checks")
                            if kap(t, z) < bh[j][z]: fail(acc, "FAIL_KH", name, t, z)
            bo = best(U - {ct}, o, u - 2); byrun = {}
            for k in fbs: byrun.setdefault(run_id[k], []).append(k)
            for r, ks in byrun.items():
                ts = [t for t in range(a, b + 1) if run_id[t] == r]
                for j in range(1, min(u - 2, len(ks)) + 1):
                    for t in ts:
                        if t <= ks[j - 1]: continue
                        for z in U - {ct}:
                            if bo[j].get(z) is not None:
                                bump(acc, "KP_checks")
                                if kap(t, z) < add(bo[j][z], kap(t, o)): fail(acc, "FAIL_KP", name, t, z)
        # θ-changes after g_{|U|-2}
        if o != ct and len(fbs) >= max(u - 2, 0):
            st = fbs[u - 3] + 1 if u >= 3 else a
            ch = sum(1 for t in range(st, b) if rows[t]["th"] != rows[t + 1]["th"])
            mx(acc, "max_TH_minus_bound", ch - (dego + u - 2), name)
            if ch > dego + u - 2: fail(acc, "FAIL_TH", name, ch, dego, u)
        bnd = 1 + ((u - 2) * (dego + u) if o != ct else u - 1)
        if len(fbs) > bnd: fail(acc, "FAIL_BOUND", name, len(fbs), bnd)
        mx(acc, "max_fallbacks_per_phase", len(fbs), u, name); mx(acc, "max_fb_minus_cap", len(fbs) - max(1, u - 2), u, name)
        a = b + 1

if __name__ == "__main__":
    acc = {}
    if sys.argv[1] == "--rand":
        from common import rand_c1o
        N, lo, hi, seed = map(int, sys.argv[2:6]); starts = int(sys.argv[6]) if len(sys.argv) > 6 else 0; rng = random.Random(seed)
        for i in range(N):
            g = rand_c1o(rng, lo, hi)
            if g is None: bump(acc, "rejected"); continue
            if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) != 1: bump(acc, "skipped_not_C1O"); continue
            analyse(g, acc, "rand%d_%d" % (seed, i))
            for _ in range(starts):
                s0 = [rng.choice(g.succ[v]) if g.owner[v] == 0 else -1 for v in range(g.n)]
                analyse(g, acc, "rand%d_%d_s" % (seed, i), s0)
    else:
        for f in sys.argv[1:]:
            try: g = load(f)
            except Exception: bump(acc, "load_fail"); continue
            if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) == 1: bump(acc, "files"); analyse(g, acc, f)
            else: bump(acc, "skipped_not_C1O")
    for key in sorted(acc): print(key, acc[key])
