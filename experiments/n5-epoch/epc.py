#!/usr/bin/env python3
"""Box 14 (Lead 15:04Z): EP-ASM terms per phase, own instrumentation (census / nconf / honff machinery; n5b SPEC engine).
Source of the statement: docs/new/P-N5-EPC-box48.md §4 (pinned 9f48ded7), read-only. Per phase P:
  N_0, N_1, N_{>=2}: epochs by |D_E|;  NCONF_{>=2}, R0_{>=2} (exact, LEV_C via honff.lev; UNK counted): nconf.phase_stats;  f: in-phase fallbacks;
  fallback-free runs S (maximal runs of P's states with no in-phase fallback between consecutive ones; f + 1 of them);
  root r := the vertex of Q whose sigma-bar changes most often in P (ties: least id), R := sigma-bar on Q - {r} (relay sub-configuration);
  RELCH(S): transitions inside S at which R changes;  RDLEAVE(S): transitions inside S at which some relay u != r leaves D (sigma-bar(u) -> tau(u));
  G_DLEAVE: transitions of P at which some u in D leaves D (the DLEAVE part of L-SI's G_c, P-N5-ROOT §7; SWITCH gains NOT measured).
Checks: EPASM  N_ep <= (4n^2 - 3n) + N_1 + NCONF_{>=2}(2n^2 - n) + R0_{>=2}  (the Lead's form with N_1 measured; only when no UNK);
        HON0   N_0 <= 4n^2 - 3n;   VIS2  N_{>=2} <= NCONF_{>=2}(2n^2 - n) + R0_{>=2}.   Slack = right side - left side (min reported).
DATA only (would-be bound from N5-NCONF §5, not a claim): NCONF_{>=2}(S) <= (RELCH(S) + 1) * deg(r) per run S; failures counted (WB_FAIL).
Usage: epc.py STARTS SEED (--list FILE | FILE.pg[:START] ...) [--nmax N] [--budget B] [--rows MIN_NEP]"""
import os
import random
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import census as C  # noqa: E402
import nconf as NC  # noqa: E402
from census import ODD  # noqa: E402

VIOL = []


def phase(g, name, states, fbs, SG, A, a, b, budget, T, rows, top):
    n = g.n; tau = states[a][1]
    r, Q = NC.phase_stats(g, states, fbs, SG, A, a, b, True, budget)
    conf = [tuple(A[k]["sbar"][q] for q in Q) for k in range(a, b + 1)]
    ep = [0] + [i for i in range(1, len(conf)) if conf[i] != conf[i - 1]]
    nd = [sum(1 for q, w in zip(Q, conf[i]) if w != tau[q]) for i in ep]
    N0, N1 = nd.count(0), nd.count(1); N2 = len(nd) - N0 - N1
    f = sum(fbs[t] for t in range(a, b))
    ch = Counter(q for t in range(a, b) for q in Q if A[t]["sbar"][q] != A[t + 1]["sbar"][q])
    root = min(ch, key=lambda q: (-ch[q], q)) if ch else (Q[0] if Q else None)
    rel = [q for q in Q if q != root]
    gdl = sum(1 for t in range(a, b) if any(A[t]["sbar"][u] != tau[u] and A[t + 1]["sbar"][u] == tau[u] for u in Q))
    runs = []; s0 = a
    for t in range(a, b):
        if fbs[t]:
            runs.append((s0, t)); s0 = t + 1
    runs.append((s0, b))
    wbf = 0; maxrelch = 0; maxrdl = 0
    for x, y in runs:
        relch = sum(1 for t in range(x, y) if any(A[t]["sbar"][u] != A[t + 1]["sbar"][u] for u in rel))
        rdl = sum(1 for t in range(x, y) if any(A[t]["sbar"][u] != tau[u] and A[t + 1]["sbar"][u] == tau[u] for u in rel))
        cs = {tuple(A[k]["sbar"][q] for q in Q) for k in range(x, y + 1)}
        nc2 = sum(1 for c in cs if sum(1 for q, w in zip(Q, c) if w != tau[q]) >= 2)
        deg = len(set(g.succ[root])) if root is not None else 1
        wbf += nc2 > (relch + 1) * deg
        maxrelch = max(maxrelch, relch); maxrdl = max(maxrdl, rdl)
    T["phases"] += 1
    for k, v in (("N_ep", r["N_ep"]), ("N_0", N0), ("N_1", N1), ("N_2", N2), ("NCONF2", r["NCONF2"]), ("R0_2", r["R0_2"]), ("f", f),
                 ("ff_runs", len(runs)), ("G_DLEAVE", gdl), ("UNK", r["UNK"]), ("WB_FAIL", wbf)):
        T[k] += v
    where = f"{name} phase[{a},{b}]"
    if not r["UNK"]:
        rhs = (4 * n * n - 3 * n) + N1 + r["NCONF2"] * (2 * n * n - n) + r["R0_2"]
        sl = rhs - r["N_ep"]; s0_ = (4 * n * n - 3 * n) - N0; s2 = r["NCONF2"] * (2 * n * n - n) + r["R0_2"] - N2
        for tag, s in (("EPASM", sl), ("HON0", s0_), ("VIS2", s2)):
            if s < 0:
                VIOL.append(f"{tag} {where} slack={s}"); print("VIOLATION", tag, where, f"slack={s}", flush=True)
            if s < top.get("minslack_" + tag, (10 ** 18,))[0]:
                top["minslack_" + tag] = (s, f"{where} n={n} N_ep={r['N_ep']}")
    else:
        T["phases_UNK"] += 1
    for k, v in (("N_ep", r["N_ep"]), ("NCONF2", r["NCONF2"]), ("R0_2", r["R0_2"]), ("f", f), ("G_DLEAVE", gdl), ("maxRELCH_run", maxrelch),
                 ("maxRDLEAVE_run", maxrdl)):
        if v > top.get("max_" + k, (-1,))[0]:
            top["max_" + k] = (v, f"{where} n={n} |Q|={len(Q)}")
    if rows is not None and r["N_ep"] >= rows:
        print(f"ROW {where} n={n} |Q|={len(Q)} N_ep={r['N_ep']} N_0={N0} N_1={N1} N_2={N2} NCONF2={r['NCONF2']} R0_2={r['R0_2']} f={f} "
              f"runs={len(runs)} root={root} RELCH/run={[sum(1 for t in range(x, y) if any(A[t]['sbar'][u] != A[t + 1]['sbar'][u] for u in rel)) for x, y in runs]} "
              f"G_DLEAVE={gdl} WB_FAIL={wbf} UNK={r['UNK']} EPASM_slack={'UNK' if r['UNK'] else rhs - r['N_ep']}", flush=True)


def main():
    argv = sys.argv[1:]; nmax = 10 ** 9; budget = None; rows = None
    for opt in ("--nmax", "--budget", "--rows"):
        if opt in argv:
            i = argv.index(opt); v = int(argv[i + 1]); del argv[i:i + 2]
            if opt == "--nmax": nmax = v
            elif opt == "--budget": budget = v
            else: rows = v
    starts, seed = int(argv[0]), int(argv[1]); rng = random.Random(seed); T = Counter(); top = {}
    for name, g, st in C.games_from_args(argv[2:]):
        if g.n > nmax:
            continue
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
            SG, A, ph = NC.phases(g, states, fbs); T["runs"] += 1
            for a, b in ph:
                phase(g, f"{name}[{tag}]", states, fbs, SG, A, a, b, budget, T, rows, top)
    for k in sorted(T):
        print(f"{k}: {T[k]}")
    for k in sorted(top):
        print(f"{k}: {top[k][0]} | {top[k][1]}")
    print("RESULT", "FAIL" if VIOL else "OK", f"violations={len(VIOL)}")


if __name__ == "__main__":
    main()
