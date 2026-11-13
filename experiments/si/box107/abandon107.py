#!/usr/bin/env python3
"""Box 107 (L-SI successor 55): check of Lemma ABANDON, ENUM-ABANDON and ONE-AHEAD (docs/si/box107-timing.md §2) on key runs of
L-NEW's one-player model (their one217.OneP, read-only; its directory is argv[1]).
Per genome file: T; the full movers (sw = |K| - 1) and the enumerating movers (mu takes every value of K) among the movers of
level <= LMAX (key sets are built explicitly, 2^(level+1) tuples on a ladder, so higher levels are skipped and counted as «skipped»);
 (i)   for every full mover: mu changes exactly at its switches and runs through K in decreasing order            -> bad_i (must be 0)
 (ii)  ABANDON: a W-target of a full mover x changes its key at step t while s_t(x) is an option into it          -> viol_ii (must be 0)
       census of the key changes of W-targets of full movers: reader away / arrives in the same step / (leaves: impossible)
 (iii) ENUM-ABANDON: target of an enumerating mover x changes key while x points at it: x must keep its option and
       the new key of x must be the predecessor of the old one in K(x)                                            -> viol_iii (must be 0)
 (iv)  ONE-AHEAD: mu_t(w) ++ eps(x,k) >= max{lam in K_k(x): lam <= mu_t(x)} for every enumerating x, option k, time t -> viol_iv (must be 0)
 control: test (ii) applied to the NON-full movers of level 1..LMAX must fire somewhere (ctrl > 0) or the line says CONTROL-SILENT.
Usage: abandon107.py ONE217_DIR [--lmax L] G.json ..."""
import sys, json
a = sys.argv[1:]; sys.path.insert(0, a[0]); a = a[1:]
import one217
LMAX = 9
if a and a[0] == "--lmax": LMAX = int(a[1]); a = a[2:]
tot = {"bad_i": 0, "viol_ii": 0, "viol_iii": 0, "viol_iv": 0}
for fn in a:
    G = json.load(open(fn)); G = G.get("genome", G)
    P = one217.OneP(G); S = P.run("key"); N = G["N"]; lev = G["lev"]; opts = G["opts"]; gate = P.gate; T = len(S) - 1
    MU = []
    for s in S:
        key = {}
        for x in P.bylev:
            wt = opts[x][s[x]][0]; key[x] = (key[wt] if lev[x] > 0 else ()) + (gate[x][s[x]],)
        MU.append(key)
    low = [x for x in P.bylev if lev[x] <= LMAX]; skipped = N - len(low)
    K = {}
    for x in low:
        K[x] = set()
        for k, (wt, _, _) in enumerate(opts[x]):
            K[x] |= {(gate[x][k],)} if lev[x] == 0 else {q + (gate[x][k],) for q in K[wt]}
    sw = {x: sum(S[t][x] != S[t + 1][x] for t in range(T)) for x in low}
    full = [x for x in low if sw[x] == len(K[x]) - 1]
    enum = [x for x in low if len({MU[t][x] for t in range(T + 1)}) == len(K[x])]
    bad_i = viol_ii = viol_iii = viol_iv = chk_iv = ctrl = 0; census = {"away": 0, "arrive": 0, "leave": 0}
    for x in full:
        seq = [MU[0][x]]
        for t in range(T):
            if MU[t + 1][x] != MU[t][x]:
                bad_i += S[t][x] == S[t + 1][x]; seq.append(MU[t + 1][x])
        bad_i += seq != sorted(K[x], reverse=True)
    for x in low:
        if lev[x] == 0: continue
        Ks = sorted(K[x], reverse=True); idx = {q: i for i, q in enumerate(Ks)}
        for t in range(T):
            for k, (w, _, _) in enumerate(opts[x]):
                if MU[t + 1][w] == MU[t][w]: continue
                at, at1 = S[t][x] == k, S[t + 1][x] == k
                if x in full:
                    if at: viol_ii += 1; census["leave"] += (not at1)
                    elif at1: census["arrive"] += 1
                    else: census["away"] += 1
                else: ctrl += at
                if x in enum and at:
                    if not at1 or idx[MU[t + 1][x]] != idx[MU[t][x]] + 1: viol_iii += 1
        if x in enum:
            for t in range(T + 1):
                for k, (w, _, _) in enumerate(opts[x]):
                    cand = [q + (gate[x][k],) for q in K[w] if q + (gate[x][k],) <= MU[t][x]]
                    if cand:
                        chk_iv += 1; viol_iv += MU[t][w] + (gate[x][k],) < max(cand)
    nm = lambda x: f"{lev[x]}.{x}"
    print(f"{fn.split('/')[-1]} N {N} T {T} lmax {LMAX} skipped {skipped} full {len(full)} [{' '.join(map(nm, full))}] enum {len(enum)} "
          f"bad_i {bad_i} viol_ii {viol_ii} census away {census['away']} arrive {census['arrive']} leave {census['leave']} "
          f"viol_iii {viol_iii} viol_iv {viol_iv} checks_iv {chk_iv} ctrl {ctrl}{'' if ctrl else ' CONTROL-SILENT'}", flush=True)
    for k_, v_ in (("bad_i", bad_i), ("viol_ii", viol_ii), ("viol_iii", viol_iii), ("viol_iv", viol_iv)): tot[k_] += v_
print("TOTAL", " ".join(f"{k} {v}" for k, v in tot.items()))
sys.exit(1 if any(tot.values()) else 0)
