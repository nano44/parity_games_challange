#!/usr/bin/env python3
"""Per phase, the quantities of P-N5-EPC (l-new, sha1 9f48ded7) §0/§2/§4, from its definitions: configuration C = sigma-bar|Q; epochs =
maximal runs with C constant; N_ep, NCONF, NCONF_{>=2} (|D_C| >= 2, D_C = {q : C(q) != tau(q)}), N_ep^{>=2}; returns (i, i+1) of a
configuration; FFRET = returns with no in-phase fallback source in [s_i, s_{i+1}) -- an UPPER bound for R0 (R0 also needs
LEV_C(s_i) <= n - 2; R0_2_certain counts the |D_C| >= 2 fallback-free returns with Xi_{s_i} != Xi_{s_{i+1}}, which are in R0 by SAT_C (2)); FFRET_{>=2} likewise for |D_C| >= 2; REV = sum over fallback-free runs of (epoch starts - distinct
configurations); max epochs of one configuration. Usage: epc.py GAME [START]"""
import sys, os
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import n3x
g = n3x.load(sys.argv[1]); st = n3x.readstart(sys.argv[2]) if len(sys.argv) > 2 else None
E, rows = n3x.trace(g, st); n = g.n
Q = [v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2]
keys = [(r["lam"], r["tau"]) for r in rows]; i = 0
while i < len(rows):
    j = i
    while j + 1 < len(rows) and keys[j + 1] == keys[i]: j += 1
    if j - i >= 5:
        tau = rows[i]["tau"]; cf = [tuple(rows[k]["nxt"][q] for q in Q) for k in range(i, j + 1)]
        starts = [i] + [k for k in range(i + 1, j + 1) if cf[k - i] != cf[k - i - 1]]
        byC = defaultdict(list)
        for s in starts: byC[cf[s - i]].append(s)
        Dsz = lambda C: sum(1 for q, c in zip(Q, C) if c != tau[q])
        fbs = [k for k in range(i, j) if rows[k]["fb"]]
        ff = ff2 = r0 = 0
        for C, ss in byC.items():
            for a, b in zip(ss, ss[1:]):
                if not any(a <= t < b for t in fbs):
                    ff += 1; ff2 += Dsz(C) >= 2
                    # exact R0 membership when Xi changes from s_i to s_{i+1}: by SAT_C (2), LEV_C(s_i) = n - 1 would keep Xi constant
                    if Dsz(C) >= 2 and any(E.key(rows[a]["vs"][v]) != E.key(rows[b]["vs"][v]) for v in range(n)): r0 += 1
        rev, last = 0, i
        for t in fbs + [j]:
            st_ = [s for s in starts if last <= s <= t]; rev += len(st_) - len({cf[s - i] for s in st_}); last = t + 1
        print(f"phase@{i} T={j-i} f={len(fbs)} N_ep={len(starts)} NCONF={len(byC)} NCONF2={sum(1 for C in byC if Dsz(C) >= 2)} "
              f"N_ep2={sum(len(v) for C, v in byC.items() if Dsz(C) >= 2)} FFRET={ff} FFRET2={ff2} R0_2_certain={r0} REV={rev} max_epochs_one_C={max(len(v) for v in byC.values())} |Q|={len(Q)}")
    i = j + 1
