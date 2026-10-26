#!/usr/bin/env python3
"""Box 45b (L-RED successor 19; Lead 03:07Z): exact checker of P-N5-FBRED (docs/new/P-N5-FBRED-box44.md, sha1 11b15455) on EVERY game,
written from the packet's §0 / §2 / §3 definitions (not from L-NEW's fbf.py). Trace = o1_19.trace (own copy of n5.py's loop).
Per phase (maximal run with (λ_Ξ, τ) constant): in-phase transitions k -> k+1 (both ends in the phase); g_1 < g_2 < ... the in-phase
fallbacks (all Even: an Odd S4c fallback changes τ; checked as ODDFB_INPHASE).
  Q := Odd vertices with out-degree >= 2; C := honest cycle nodes of the phase; T := C ∪ Q; U_c := λ^{-1}(c).
  ρ := #(transition t -> t+1 of the phase, q ∈ Q) with Ξ_{t+1}(q) != Ξ_t(q)   [transitions of the phase = in-phase transitions].
  Q-run: maximal run of consecutive states of the phase with Ξ(q) constant for all q ∈ Q.  N_late := #Q-runs holding (as source
  state) a fallback g_j with j >= n.
  S_k := switched Even vertices at a fallback; S := S_k ∖ T.
Checks: FBRED  f <= 1 + (n − 1)(2 + ρ);   FBRED_LATE  f <= 1 + (n − 1) + (n − 1)·N_late;   CNO  at most one in-phase fallback with S = ∅,
and it is the phase's last transition (CN-LAST: k+1 is the phase's last state);  OUT  regions = Oink zlk, strategies verified by
harness/verify.py (and Oink -v when --oink).
Reported per run: max f, f/n, ρ at the max-f phase, N_late, late fallbacks (j >= n), Q-runs.
Usage: fbr19.py file game.pg [start.json] [--oink]"""
import sys, os, json, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "o1"))
import o1_19 as O, pg, verify

def analyse(g, start=None, mode="n5", tmp=None, use_oink=False, cap=10 ** 6):
    n = g.n; Q = [v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1]
    S, FB, E = O.trace(g, start, mode, cap)
    ev = [E.evaluate(s) for s, _ in S]; Xi = [X for X, _ in ev]; lam = [tuple(x[0] for x in X) for X in Xi]
    SB = [B for _, B in ev]
    N = len(S); r = dict(Nep=0, epoch_n1=0, s4a_run=0, s4a_run_pre=0, sigbar_repeat=0, levels=0, sw_trans=0, sg_checks=0, acc_checks=0, n=n, Q=len(Q), ITER=len(FB), fmax=0, fn=0.0, rho_at=0, U_at=0, Nlate_at=0, rhomax=0, Nlate=0, late=0, phases=0, fails=[])
    a = 0
    while a < N:
        b = a
        while b + 1 < N and lam[b + 1] == lam[a] and S[b + 1][1] == S[a][1]: b += 1
        r["phases"] += 1
        C = set(lam[a]); T = C | set(Q)
        fbs = [k for k in range(a, b) if FB[k]]
        if any(FB[k] == 2 for k in fbs): r["fails"].append("ODDFB_INPHASE")
        f = len(fbs)
        rho = sum(1 for k in range(a, b) for q in Q if Xi[k + 1][q] != Xi[k][q])
        # Q-runs: maximal runs of states a..b with Ξ(Q) constant
        qrun = [0] * (b - a + 1)
        for k in range(a + 1, b + 1): qrun[k - a] = qrun[k - a - 1] + (1 if any(Xi[k][q] != Xi[k - 1][q] for q in Q) else 0)
        late_runs = {qrun[k - a] for j, k in enumerate(fbs, 1) if j >= n}
        nl = len(late_runs); late = sum(1 for j in range(1, f + 1) if j >= n)
        if f > 1 + (n - 1) * (2 + rho): r["fails"].append(f"FBRED f={f} rho={rho}")
        if f > 1 + (n - 1) + (n - 1) * nl: r["fails"].append(f"FBRED_LATE f={f} Nlate={nl}")
        cno = []
        for k in fbs:
            Sk = {v for v in range(n) if g.owner[v] == 0 and S[k][0][v] != S[k + 1][0][v]}
            if not (Sk - T): cno.append(k)
        if len(cno) > 1 or (cno and cno[0] + 1 != b): r["fails"].append(f"CNO {cno} b={b}")
        # ---- Lemma ACCEL (N5-FBF §8): (a) simple-path values; (SG) strict gain at switches of Even z with λ(z) != z
        lv = {}; swt = 0
        for k in range(a, b + 1):
            for z in range(n):
                lv.setdefault(z, set()).add(Xi[k][z])
                c = lam[k][z]
                if z == c: continue
                path, v, seen = [], z, set()
                while v != c and v not in seen and lam[k][v] == c:
                    seen.add(v); path.append(v); v = S[k][0][v] if g.owner[v] == 0 else SB[k][v]
                r["acc_checks"] += 1
                if v != c: r["fails"].append(f"ACCEL_a nonsimple/leaves U_c z={z} k={k}"); continue
                val = (c, 0, 0)
                for u in reversed(path): val = E.extend(u, val)
                if tuple(val) != tuple(Xi[k][z]): r["fails"].append(f"ACCEL_a value z={z} k={k} {val} {Xi[k][z]}")
        for k in range(a, b):
            swz = [z for z in range(n) if g.owner[z] == 0 and S[k][0][z] != S[k + 1][0][z] and lam[k][z] != z]
            if swz: swt += 1
            for z in swz:
                r["sg_checks"] += 1
                if not E.key(Xi[k + 1][z]) > E.key(Xi[k][z]): r["fails"].append(f"SG z={z} k={k} fb={FB[k]}")
        # ---- Lemma EPOCH (N5-FBF §9.1, l-new 916aa2b3): epochs = maximal runs of states of the phase with σ̄|Q constant
        ep = [0] * (b - a + 1); seenQ = [tuple(SB[a][q] for q in Q)]
        for k in range(a + 1, b + 1):
            cur = tuple(SB[k][q] for q in Q); ep[k - a] = ep[k - a - 1] + (cur != tuple(SB[k - 1][q] for q in Q))
            if cur != seenQ[-1]:
                if cur in seenQ: r["sigbar_repeat"] += 1
                seenQ.append(cur)
        Nep = ep[-1] + 1; r["Nep"] = max(r["Nep"], Nep)
        if f > 1 + n * Nep: r["fails"].append(f"EPOCH_c f={f} Nep={Nep}")
        for e in range(Nep):
            Ek = [k for k in range(a, b + 1) if ep[k - a] == e]; lo, hi = Ek[0], Ek[-1]
            efb = [k for k in range(lo, min(hi, b - 1) + 1) if k < b and FB[k]]          # fallbacks k -> k+1 with k ∈ E
            run = best = 0; pre = 0; frz = efb[n - 2] if len(efb) >= n - 1 else None
            for k in range(lo, hi):                                                       # transitions with both ends in E
                if FB[k]: run = 0
                else:
                    run += 1; best = max(best, run)
                    if frz is None or k <= frz: pre = max(pre, run)
            r["s4a_run"] = max(r["s4a_run"], best); r["s4a_run_pre"] = max(r["s4a_run_pre"], pre)
            if frz is not None:
                r["epoch_n1"] += 1
                for k in range(frz + 1, hi):
                    if Xi[k + 1] != Xi[k]: r["fails"].append(f"EPOCH_a_frozen k={k}"); break
                    if any(g.owner[z] == 0 and S[k][0][z] != S[k + 1][0][z] and lam[k][z] != z for z in range(n)): r["fails"].append(f"EPOCH_b_switch k={k}"); break
                if hi - frz > 4 * n * (n - 1) + 1: r["fails"].append(f"EPOCH_b_count {hi - frz}")
        r["levels"] = max(r["levels"], max(len(x) for x in lv.values())); r["sw_trans"] = max(r["sw_trans"], swt)
        if f > r["fmax"]: r.update(fmax=f, fn=f / n, rho_at=rho, Nlate_at=nl, U_at=max(sum(1 for z in lam[a] if z == c) for c in C))
        r["rhomax"] = max(r["rhomax"], rho); r["Nlate"] = max(r["Nlate"], nl); r["late"] = max(r["late"], late)
        a = b + 1
    win, ws = E.regions(S[-1][0])
    e = verify.check(g, win, ws)
    if e: r["fails"].append("OUT_STRAT " + e[0])
    if use_oink:
        oc = O.oink_check(g, win, ws, tmp or tempfile.mkdtemp())
        if oc != "OK": r["fails"].append("OUT_OINK " + oc)
    return r

if __name__ == "__main__":
    a = sys.argv
    g = pg.parse("".join(l for l in open(a[2]) if not l.lstrip().startswith("%")))
    st = json.load(open(a[3]))["start"] if len(a) > 3 and a[3].endswith(".json") else None
    print(json.dumps(analyse(g, st, "n5", None, "--oink" in a)))
