#!/usr/bin/env python3
"""Box 14 (Lead 14:08Z; L-NEW 27, docs/new/N5-NCONF-box48.md §0, §2 on claude/l-new 9ac695aa): own counter of NCONF, NCONF_{>=2} and the
fallback-free returns R0 per phase (L-NEW's experiments/new/box48/nconf.py is for cross-checking only; not imported).
Definitions (N5-NCONF §0, §2):
  configuration C = sigma-bar|Q at a state; D_C = {q in Q : C(q) != tau(q)} (tau fixed on the phase); C-epochs E_1 < ... < E_V with first
  states s_1 < ... < s_V; a RETURN is a pair (i, i+1); REV = N_ep - NCONF = sum_C (V_C - 1).
  NCONF(P) = distinct configurations of P's states; NCONF_{>=2}(P) = those with |D_C| >= 2.
  RET0 (Lead's 'fallback-free returns'): returns with no in-phase fallback SOURCE t in [s_i, s_{i+1}).
  R0 (Corollary VIS): RET0 returns with moreover LEV_C(s_i) <= n - 2, LEV_C = LEV in H_C (Odd fixed to C) via honff.lev with Odd map sigma-bar
       at s_i (budget-capped; UNK counted and NOT counted in R0, so R0 is reported with its UNK count).  R0 <= RET0.
  Index _{>=2}: restricted to configurations with |D_C| >= 2.
Checks (L-NEW-proved, unrefereed): VIS  V_C <= 2n^2 - n + R0_C;  EP-C  N_ep <= NCONF*(2n^2 - n) + R0 (both only when no UNK in the phase).
Usage: nconf.py STARTS SEED (--list FILE | --rand C NLO NHI KLO KHI GSEED | FILE.pg[:START] ...) [--lev] [--budget B] [--rows MIN_NEP]"""
import os
import random
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import census as C  # noqa: E402
import honff as H  # noqa: E402
from census import SpecSI, ODD  # noqa: E402

VIOL = []


def phases(g, states, fbs, A=None):
    SG = SpecSI(g)
    if A is None:
        A = [C.state_info(g, SG, s, t) for s, t in states]
    key = [(A[k]["lam"], states[k][1]) for k in range(len(A))]
    out = []; i = 0
    while i < len(A):
        j = i
        while j + 1 < len(A) and key[j + 1] == key[i]:
            j += 1
        out.append((i, j)); i = j + 1
    return SG, A, out


def phase_stats(g, states, fbs, SG, A, a, b, lev=False, budget=None):
    n = g.n; Q = [v for v in range(n) if g.owner[v] == ODD and len(set(g.succ[v])) >= 2]; tau = states[a][1]
    conf = [tuple(A[k]["sbar"][q] for q in Q) for k in range(a, b + 1)]
    starts = {}
    for idx, cf in enumerate(conf):
        if idx == 0 or conf[idx - 1] != cf:
            starts.setdefault(cf, []).append(a + idx)
    nd = {cf: sum(1 for q, w in zip(Q, cf) if w != tau[q]) for cf in starts}
    r = Counter(); r["N_ep"] = sum(len(v) for v in starts.values()); r["NCONF"] = len(starts)
    r["NCONF2"] = sum(1 for cf in starts if nd[cf] >= 2); r["maxV"] = max(len(v) for v in starts.values())
    unk = 0
    for cf, ss in starts.items():
        r0c = 0
        for s0, s1 in zip(ss, ss[1:]):
            if any(fbs[t] for t in range(s0, s1)):
                continue
            r["RET0"] += 1; r["RET0_2"] += nd[cf] >= 2
            if lev:
                lv = H.lev(g, SG, A[s0]["Xi"], A[a]["lam"], A[s0]["sbar"] if True else None, budget)
                if lv is None:
                    unk += 1; continue
                if lv <= n - 2:
                    r0c += 1; r["R0"] += 1; r["R0_2"] += nd[cf] >= 2
        if lev and not unk and len(ss) > 2 * n * n - n + r0c:
            VIOL.append(f"VIS conf={cf} V={len(ss)} R0_C={r0c}")
    r["UNK"] = unk
    if lev and not unk and r["N_ep"] > r["NCONF"] * (2 * n * n - n) + r["R0"]:
        VIOL.append(f"EP-C N_ep={r['N_ep']} NCONF={r['NCONF']} R0={r['R0']}")
    return r, Q


def main():
    argv = sys.argv[1:]; lev = "--lev" in argv; argv = [x for x in argv if x != "--lev"]; budget = None; rows = None
    for opt in ("--budget", "--rows"):
        if opt in argv:
            i = argv.index(opt); v = int(argv[i + 1]); del argv[i:i + 2]
            if opt == "--budget": budget = v
            else: rows = v
    starts, seed = int(argv[0]), int(argv[1]); rng = random.Random(seed)
    T = Counter(); top = {}
    for name, g, st in C.games_from_args(argv[2:]):
        pairs = [("S3", None, None)]
        if st:
            s, t = C.full_start(g, *C.read_start(st, g)); pairs = [("start", s, t)]
        for r_ in range(starts):
            s, t = C.rand_start(g, rng); pairs.append((f"R{r_}", s, t))
        for tag, s, t in pairs:
            try:
                states, fbs = C.run_states(g, s, t, cap=3000)
            except Exception as e:   # noqa: BLE001
                T["runs_failed"] += 1; print("RUNFAIL", name, tag, repr(e)[:150]); continue
            SG, A, ph = phases(g, states, fbs); T["runs"] += 1
            for a, b in ph:
                nv = len(VIOL)
                r, Q = phase_stats(g, states, fbs, SG, A, a, b, lev, budget)
                for v in VIOL[nv:]:
                    print("VIOLATION", name, tag, f"phase[{a},{b}]", v, flush=True)
                T["phases"] += 1
                for k in ("N_ep", "NCONF", "NCONF2", "RET0", "RET0_2", "R0", "R0_2", "UNK"):
                    T[k] += r[k]
                    if r[k] > top.get(k, (-1,))[0]:
                        top[k] = (r[k], f"{name}[{tag}] phase[{a},{b}] n={g.n} |Q|={len(Q)} N_ep={r['N_ep']} NCONF={r['NCONF']} "
                                        f"NCONF2={r['NCONF2']} RET0={r['RET0']} RET0_2={r['RET0_2']} R0={r['R0']} R0_2={r['R0_2']}")
                if r["NCONF"] > g.n:
                    T["phases_NCONF_gt_n"] += 1
                if rows is not None and r["N_ep"] >= rows:
                    print(f"ROW {name}[{tag}] phase[{a},{b}] n={g.n} |Q|={len(Q)} N_ep={r['N_ep']} NCONF={r['NCONF']} NCONF2={r['NCONF2']} "
                          f"maxV={r['maxV']} REV={r['N_ep'] - r['NCONF']} RET0={r['RET0']} RET0_2={r['RET0_2']}"
                          + (f" R0={r['R0']} R0_2={r['R0_2']} UNK={r['UNK']}" if lev else ""), flush=True)
    for k in sorted(T):
        print(f"{k}: {T[k]}")
    for k in sorted(top):
        print(f"max {k}: {top[k][0]} | {top[k][1]}")
    print("RESULT", "FAIL" if VIOL else "OK", f"violations={len(VIOL)}")


if __name__ == "__main__":
    main()
