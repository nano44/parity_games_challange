#!/usr/bin/env python3
"""Box 40: survey of Q states (H1 ∧ H2 ∧ ¬H3: c_w ≠ c_θ) per phase. Classifies every state of every phase as HN, Q, H ((h) = H1 ∧ H2 ∧ H3)
or N1 (¬H1); checks Remark H3-IN-HN (no Q state in a phase with an HN state and τ(o) ≠ o: FAIL_Q_IN_HN) and that a phase with a Q state
has λ(τ(o)) ≠ c_θ (FAIL_QLAM). Counts per phase: Q states, fallbacks at Q states, crossings at Q states (entries / evictions), longest
run of consecutive Q states. DATA only. Usage: qsurvey.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "box39")); sys.path.insert(0, os.path.join(HERE, "..", "box38"))
from neb_run import *

def fail(acc, k, *info): bump(acc, k); print(k, *info, flush=True)

def wcyc_node(g, E, s, t, o):
    v, seen = o, []
    while v not in seen: seen.append(v); v = s[v] if g.owner[v] == 0 else t[v]
    cyc = seen[seen.index(v):]; return max(cyc, key=lambda x: E.rank[x])

def analyse(g, acc, name):
    rows, o, E = trace(g, None); N = len(rows); a = 0
    for r in rows:
        r["cls"] = "N1" if not r["h1"] else ("HN" if not r["h2"] else ("H" if wcyc_node(g, E, r["s"], r["t"], o) == r["Xi"][o][0] else "Q"))
    while a < N:
        b = a
        while b + 1 < N and rows[b + 1]["ph"] == rows[a]["ph"]: b += 1
        cl = [rows[t]["cls"] for t in range(a, b + 1)]; t0 = rows[a]["t"][o]; ct = rows[a]["Xi"][o][0]
        if "Q" in cl:
            bump(acc, "phases_with_Q")
            if "HN" in cl and t0 != o: fail(acc, "FAIL_Q_IN_HN", name, a)
            if rows[a]["Xi"][t0][0] == ct: fail(acc, "FAIL_QLAM", name, a)
            if "H" in cl: bump(acc, "phases_with_Q_and_H")
            if "HN" in cl: bump(acc, "phases_with_Q_and_HN")
            q = cl.count("Q"); bump(acc, "Q_states", q)
            fq = sum(1 for k in range(a, b) if rows[k]["fb"] and rows[k]["cls"] == "Q"); bump(acc, "Q_fallbacks", fq)
            ent = sum(1 for k in range(a, b) if rows[k]["cls"] == "Q" and set(rows[k]["R"]) < set(rows[k + 1]["R"]))
            ev = sum(1 for k in range(a, b) if rows[k]["cls"] == "Q" and set(rows[k + 1]["R"]) < set(rows[k]["R"]))
            oth = sum(1 for k in range(a, b) if rows[k]["cls"] == "Q" and set(rows[k + 1]["R"]) != set(rows[k]["R"])) - ent - ev
            bump(acc, "Q_entries", ent); bump(acc, "Q_evictions", ev); bump(acc, "Q_mixed_crossings", oth)
            fbev = sum(1 for k in range(a, b) if rows[k]["cls"] == "Q" and rows[k]["fb"] and set(rows[k + 1]["R"]) != set(rows[k]["R"]))
            bump(acc, "Q_fallback_crossings", fbev)
            s4ent = sum(1 for k in range(a, b) if rows[k]["cls"] == "Q" and not rows[k]["fb"] and set(rows[k]["R"]) - set(rows[k + 1]["R"]))
            bump(acc, "Q_S4a_with_a_leave", s4ent)
            run = best = 0
            for c in cl:
                run = run + 1 if c == "Q" else 0; best = max(best, run)
            mx(acc, "max_Q_fallbacks_phase", fq, g.n, name, a, q)
            mx(acc, "max_Q_run", best, g.n, name, a)
        a = b + 1

if __name__ == "__main__":
    acc = {}
    for f in sys.argv[1:]:
        try: g = load(f)
        except Exception: bump(acc, "load_fail"); continue
        if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) == 1: bump(acc, "files"); analyse(g, acc, f)
        else: bump(acc, "skipped_not_C1O")
    for key in sorted(acc): print(key, acc[key])
