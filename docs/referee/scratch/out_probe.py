#!/usr/bin/env python3
"""REFEREE succ. 8 probe for packet P-N5-OUT (docs/new/P-N5-OUT-box37.md, pin 719ce66, sha1 9f032e61...). Own engine (rl_engine,
rl_probe states; no lane code). C^1O asserted. Phase = (lambda_Xi, tau); HN = H1 and not H2; HN stretch = maximal run of HN states
of one phase; crossing = in-phase transition with R changing.
 SPLIT   (a) HN at k, in-phase S4a: R_k <= R_{k+1}; (b) in-phase Even fallback: Rbar_{k+1} <= Rbar_k
 EPOCH   per stretch: X_S <= 2(n-1)(B+1), f_S <= K(X_S+1)+X_S
 FFLAT   in-phase Even fallback with HN at k: Xi_{k+1} = Xi_k on F_k, theta unchanged
 FREEZE  FREEZE-STEP (i)-(iii) at every in-phase transition meeting its hypotheses
 NOENT   tau(o) = o, case A: from every fallback state a in a stretch, on the theta-constant run [a, b] in S: INV (i), (ii), no entry,
         Rbar shrinks, Xi(z) == Xi_a(z) (agree at ranks >= rank o)
 NEC     tau(o) = o, case A: every break theta-separated (a); N_HN <= floor(T/2) + 1; f_HN bound (c)
 CASEB   tau(o) = o, case B: at HN fallback states every R -> Rbar gate has level -1 and z's route longer
Usage: out_probe.py files... | lib37"""
import sys, os
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P
EX = []


def K_(g, x): return g.key(x)


def equiv(g, o, x, y):
    l = P.lev(x, y)
    return l < g.rank[o]


def run(g, cnt, name):
    o, st = P.states(g); n = g.n; T = len(st) - 1; nE = sum(1 for v in range(n) if g.owner[v] == 0); KK = nE * (2 * n - 1)
    inph = [st[k]["key"] == st[k + 1]["key"] for k in range(T)]
    HN = [a["H1"] and not a["H2"] for a in st]
    R = [a["Rb"] - {o} for a in st]
    cross = [inph[k] and R[k] != R[k + 1] for k in range(T)]
    for k in range(T):
        if not (inph[k] and HN[k]): continue
        a, b = st[k], st[k + 1]
        if not a["fb"]:
            cnt["SPLIT_a_chk"] += 1
            if not R[k] <= R[k + 1]: cnt["SPLIT_a_FAIL"] += 1; EX.append((name, "SPLITa", k))
        elif a["Is"]:
            cnt["SPLIT_b_chk"] += 1
            if not b["Rb"] <= a["Rb"]: cnt["SPLIT_b_FAIL"] += 1; EX.append((name, "SPLITb", k))
            cnt["FFLAT_chk"] += 1
            if any(b["Xi"][v] != a["Xi"][v] for v in a["F"]) or b["Xi"][o] != a["Xi"][o]: cnt["FFLAT_FAIL"] += 1; EX.append((name, "FFLAT", k))
        # FREEZE-STEP
        if b["H1"] and b["Xi"][o] == a["Xi"][o] and not any(z in a["Rb"] for y, z in a["Is"]):
            cnt["FREEZE_chk"] += 1
            okr = b["Rb"] <= a["Rb"] and all(P.route(b["nx"], z, o) == P.route(a["nx"], z, o) for z in b["Rb"] if z != o)
            okv = all(b["Xi"][z] == a["Xi"][z] for z in b["Rb"])
            ok3 = not any(z in b["Rb"] for y, z in b["Is"])
            if not (okr and okv and ok3): cnt["FREEZE_FAIL"] += 1; EX.append((name, "FREEZE", k, okr, okv, ok3))
    # stretches
    stretches, k = [], 0
    while k <= T:
        if HN[k]:
            j = k
            while j < T and HN[j + 1] and inph[j]: j += 1
            stretches.append((k, j)); k = j + 1
        else: k += 1
    for (s0, s1) in stretches:
        cnt["stretches"] += 1
        trs = list(range(s0, s1))
        X = sum(cross[t] for t in trs); f = sum(st[t]["fb"] for t in trs)
        ent = [t for t in trs if cross[t] and R[t] < R[t + 1]]; ev = [t for t in trs if cross[t] and st[t + 1]["Rb"] < st[t]["Rb"]]
        if X != len(ent) + len(ev): cnt["SPLIT_mixed_FAIL"] += 1
        breaks = []
        for e in ent:
            prev_e = max([x for x in ent if x < e], default=-1)
            evs = [x for x in ev if prev_e < x < e]
            if evs: breaks.append((evs[0], e))
        B = len(breaks); cnt["breaks"] += B
        if X > 2 * (n - 1) * (B + 1) or f > KK * (X + 1) + X: cnt["EPOCH_FAIL"] += 1; EX.append((name, "EPOCH", s0))
        cnt["fb_in_stretch"] += f; cnt["fb_in_stretch_crossing"] += sum(1 for t in trs if st[t]["fb"] and cross[t])
        a0 = st[s0]; to = a0["t"][o]
        if to != o: continue
        c = a0["Xi"][o][0]; caseA = g.rank[o] > g.rank[c]
        cnt["tauoo_stretch_A" if caseA else "tauoo_stretch_B"] += 1
        if caseA:
            for (ea, e) in breaks:
                cnt["NEC_a_chk"] += 1
                if not any(st[j]["Xi"][o] != st[j + 1]["Xi"][o] and not st[j]["fb"] for j in range(ea + 1, e + 1)):
                    cnt["NEC_a_FAIL"] += 1; EX.append((name, "NECa", ea, e))
            for a in range(s0, s1 + 1):
                if not (st[a]["fb"] and st[a]["Is"]): continue
                b = a
                while b + 1 <= s1 and st[b + 1]["Xi"][o] == st[a]["Xi"][o]: b += 1
                cnt["NOENT_runs"] += 1
                for t in range(a, b + 1):
                    x = st[t]; cnt["NOENT_states"] += 1
                    i1 = not any(y in x["F"] and z in x["Rb"] for y, z in x["Is"])
                    i2 = all(P.lev(x["Xi"][x["s"][v]], x["Xi"][z]) < g.rank[o] for v, z in x["Is"] if v in x["Rb"] and v != o and z in x["Rb"])
                    fr = all(equiv(g, o, x["Xi"][z], st[a]["Xi"][z]) for z in x["Rb"])
                    ne = t == b or not (R[t] < R[t + 1] or (R[t] != R[t + 1] and not st[t + 1]["Rb"] <= x["Rb"]))
                    if not (i1 and i2 and fr and ne): cnt["NOENT_FAIL"] += 1; EX.append((name, "NOENT", a, t, i1, i2, fr, ne))
        else:
            for a in range(s0, s1 + 1):
                x = st[a]
                if not (x["fb"] and x["Is"]): continue
                for v, z in x["Is"]:
                    if v in x["Rb"] and v != o and z in x["Rb"]:
                        cnt["CASEB_chk"] += 1
                        lz = len(P.route(x["nx"], z, o)) if z != o else 0
                        ls = len(P.route(x["nx"], x["s"][v], o)) if x["s"][v] != o else 0
                        if P.lev(x["Xi"][x["s"][v]], x["Xi"][z]) != -1 or not lz > ls: cnt["CASEB_FAIL"] += 1; EX.append((name, "CASEB", a, v, z))


def main(a):
    files = [os.path.join(P.ROOT, l.split()[0]) for l in open(os.path.join(P.ROOT, "experiments/new/box37/lib37.txt")) if l.strip()] \
        if a == ["lib37"] else a
    cnt = Counter()
    for f in files:
        g = RE.parse(f)
        try: P.assert_c1o(g)
        except AssertionError: cnt["skip_not_c1o"] += 1; continue
        if g.n > 64: cnt["skip_big"] += 1; continue
        cnt["games"] += 1; run(g, cnt, os.path.relpath(f, P.ROOT))
    for k in sorted(cnt): print("%-24s %d" % (k, cnt[k]))
    print("FAILS", sum(v for k, v in cnt.items() if k.endswith("_FAIL")))
    for e in EX[:12]: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
