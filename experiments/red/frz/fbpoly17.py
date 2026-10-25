#!/usr/bin/env python3
"""Box 41 (L-RED successor 17): exact checker of docs/new/N5-FBPOLY-box41.md (sha1 7a7087f7; L-NEW succ. 20), written from its §§2-6:
  CNONLY   (§4) at an in-phase Even fallback with S_U = ∅ (S_U = switched Even vertices in U ∖ T, T = {o, c_θ}): every gate (y, z) has
           λ_k(y) = y and lev(Ξ_k σ_k y, Ξ_k z) = −1, and k + 1 is the last state of the phase; ≤ 1 such fallback per phase.
  EXITSW   (§2) at an in-phase Even fallback with S_U ≠ ∅: some u ∈ S_U whose x*_u = σ_{k+1}(u) has an honest k-play visiting T before u.
           Kinds of switched U ∖ T vertices: ct / o (first terminal) / loop (u before T).
  FREEZEX  (§3) o ≠ c_θ: a fallback g_j with j ≥ |U| − 1 that is the i-th fallback of its θ-run with i ≥ |U| − 1 has S_U = ∅.
  THAFTER  (§5) o ≠ c_θ, |U| ≥ 2, phase with ≥ |U| − 2 fallbacks: #θ-changes at transitions t → t+1 with t > g_{|U|−2} (both ends in
           the phase) ≤ deg_U(o) + |U| − 2, deg_U(o) = |succ(o) ∩ U|.
  FBPOLY   (§6) f ≤ 1 + (|U| − 2)(deg_U(o) + |U|) if o ≠ c_θ, |U| ≥ 2; f ≤ 1 if |U| = 2; f ≤ |U| if o = c_θ.
  FBCAP    (L-RED CONJECTURE) f ≤ max(1, |U| − 2).
Regime counters: THAFTER_phases (phases where §5's hypothesis holds), FREEZEX_hyp (fallbacks meeting §3's hypothesis).
Uses pfz17.states (rows: σ, τ, Ξ, σ̄, λ, fallback flag). Usage: fbpoly17.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "so"))
import sox, pfz17
from sox import lev

def analyse(g, acc, name, st=None):
    import ex16
    tr = ex16.trace(g, st) if st is not None else None
    rows, o, E = pfz17.states(g, tr=tr); N = len(rows); n = g.n
    def bump(k, v=1): acc[k] = acc.get(k, 0) + v
    def fail(k, *a): bump(k); print(k, name, st, *a, flush=True)
    a = 0
    while a < N:
        b = a
        while b + 1 < N and rows[b + 1]["lam"] == rows[a]["lam"] and rows[b + 1]["t"] == rows[a]["t"]: b += 1
        ct = rows[a]["Xi"][o][0]; U = {z for z in range(n) if rows[a]["Xi"][z][0] == ct}; u = len(U); T = {o, ct}
        degU = len(set(g.succ[o]) & U)
        efb = [k for k in range(a, b) if rows[k]["fb"] and rows[k]["s"] != rows[k + 1]["s"]]
        f = len(efb); bump("phases")
        # θ-run index of each fallback
        run_start = {}; s0 = a
        while s0 <= b:
            e0 = s0
            while e0 + 1 <= b and rows[e0 + 1]["Xi"][o] == rows[s0]["Xi"][o]: e0 += 1
            for k in range(s0, e0 + 1): run_start[k] = s0
            s0 = e0 + 1
        cn = 0
        for j, k in enumerate(efb, 1):
            r0, r1 = rows[k], rows[k + 1]
            S = [v for v in range(n) if g.owner[v] == 0 and r0["s"][v] != r1["s"][v]]; SU = [v for v in S if v in U - T]
            i = sum(1 for kk in efb if run_start[kk] == run_start[k] and kk <= k)
            if o != ct and j >= u - 1 and i >= u - 1:
                bump("FREEZEX_hyp")
                if SU: fail("FAIL_FREEZEX", k, j, i, u, SU)
            if not SU:
                cn += 1; bump("CNONLY_fallbacks")
                gates = E.improving(tuple(r0["s"]), r0["Xi"])
                for y, z in gates:
                    if r0["Xi"][y][0] != y or lev(r0["Xi"][r0["s"][y]], r0["Xi"][z]) != -1: fail("FAIL_CNONLY_gate", k, y, z); break
                if k + 1 != b: fail("FAIL_CNONLY_last", k, b)
            else:
                ok = False
                for v in SU:
                    x = r1["s"][v]; seen = set(); kind = None
                    while True:
                        if x in T: kind = "ct" if x == ct else "o"; break
                        if x == v: kind = "loop"; break
                        if x in seen: kind = "cyc?"; break
                        seen.add(x); x = r0["s"][x] if g.owner[x] == 0 else r0["sb"][x]
                    bump("EXITSW_kind_" + kind); ok = ok or kind in ("ct", "o")
                if not ok: fail("FAIL_EXITSW", k, SU)
        if cn > 1: fail("FAIL_CNONLY_count", a, cn)
        if o != ct and u >= 2 and f >= max(u - 2, 0):
            st0 = a if u == 2 else efb[u - 3] + 1
            ch = sum(1 for t in range(st0, b) if rows[t]["Xi"][o] != rows[t + 1]["Xi"][o]); bump("THAFTER_phases")
            if u >= 3: bump("THAFTER_phases_U3+")
            acc["max_THAFTER_slack"] = max(acc.get("max_THAFTER_slack", -99), ch - (degU + u - 2))
            if ch > degU + u - 2: fail("FAIL_THAFTER", a, ch, degU, u)
        bound = (1 + (u - 2) * (degU + u)) if (o != ct and u >= 2) else (u if o == ct else 10 ** 9)
        if u == 2 and o != ct: bound = 1
        if f > bound: fail("FAIL_FBPOLY", a, f, u, degU)
        if f > max(1, u - 2): fail("FAIL_FBCAP", a, f, u)
        # FB-PHASE (docs/si/N5-FBPHASE-box14.md §4, sha1 f7aaa624) and Corollary FX (§5)
        sizes = {}
        for z in rows[a]["lam"]: sizes[z] = sizes.get(z, 0) + 1
        do = len(set(g.succ[o])); N0 = max([0, u - 2] + [sz - 1 for cc, sz in sizes.items() if cc != ct])
        fbp = N0 + (do + n - 2) + (do + n - 1) * (u - 1) + 1
        acc["max_FBPHASE_slack"] = max(acc.get("max_FBPHASE_slack", -10 ** 9), f - fbp)
        if f > fbp: fail("FAIL_FBPHASE", a, f, fbp)
        rank = {v: i for i, v in enumerate(sorted(range(n), key=lambda v: (g.prio[v], v)))}
        def cw(k):
            x, path = o, []
            while x not in path: path.append(x); x = rows[k]["s"][x] if g.owner[x] == 0 else rows[k]["t"][x]
            return max(path[path.index(x):], key=lambda v: rank[v])
        X = sum(1 for k in range(a, b) if rows[k]["R"] != rows[k + 1]["R"])
        XSN = sum(1 for k in range(a, b) if not rows[k]["fb"] and rows[k]["R"] != rows[k + 1]["R"] and cw(k) == ct)
        acc["max_X"] = max(acc.get("max_X", 0), X); acc["max_FX_slack"] = max(acc.get("max_FX_slack", -10 ** 9), X - (n * (f + XSN) + n - 1))
        if X > n * (f + XSN) + n - 1: fail("FAIL_FX", a, X, f, XSN)
        acc["max_FBCAP_slack"] = max(acc.get("max_FBCAP_slack", -99), f - max(1, u - 2))
        a = b + 1
    return acc

if __name__ == "__main__":
    acc = {}
    for f in sys.argv[1:]:
        try: g = sox.load(f)
        except Exception: continue
        if len(sox.oddchoice(g)) != 1: continue
        analyse(g, acc, f)
    print(acc)
