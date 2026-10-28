#!/usr/bin/env python3
"""L-SI box 23 (successor 19): DATA for docs/si/N5-ALT-box23.md (TOP-ONCE). Per phase, every rise of a vertex's Xi path set: z with
M_t(z) != M_t+1(z) at an in-phase transition (same cycle node by the phase). TOP h := the highest rank in P_t(z) xor P_t+1(z) (Q1 of SPEC:
the rank that decides the comparison); IN if h enters P(z), OUT if it leaves. Counts per phase: MR (M-rises), LR (length-only changes),
WRONG (a fall of Xi(z) in the Xi order: must be 0, R15 (a)), MULT_ph = the largest number of rises of one z with the same (h, direction) in one
phase, MULT_run = the same inside one fallback-free run; RISES_max = the most M-rises of one z in one phase, against n. XIRISES: changes of Xi(z) of any kind (M or length) per phase, max over z, also / n (x100); PHASELEN / n (x100). GATE: the rises of the
abandoned option y1 at gate changes (u in D_t cup D_t+1, sigma-bar changes y1 -> y2), whether such a rise's (y1, h, dir) recurs.
TRACE=z prints z's changes per phase (rank of the top changed path vertex, +/- enters/leaves, e/o its parity).
Usage: mrise.py --one GAME [START] | --list FILE [KMIN] (env RS, NMAX)"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from common import rows, phases, load, readstart, Dset
C = Counter(); EX = []

def run(g, name, start=None):
    E, R = rows(g, start); n = g.n
    for i, j in phases(R):
        runs, s = [], i
        for k in range(i, j):
            if R[k]["fb"]: runs.append((s, k)); s = k + 1
        runs.append((s, j))
        rid = {}
        for s, e in runs:
            for k in range(s, e): rid[k] = s
        mph, mrun, nr = Counter(), Counter(), Counter()
        if os.environ.get("TRACE"):                         # TRACE=z: z's Xi changes in every phase: t:rank(+|-)(e|o) (top of the path-set change) or t:L
            z = int(os.environ["TRACE"]); seq = []
            for k in range(i, j):
                a, b = R[k]["vs"][z], R[k + 1]["vs"][z]
                if a[1] != b[1]:
                    h = (a[1] ^ b[1]).bit_length() - 1; seq.append(f"{k}:{h}{'+' if b[1] >> h & 1 else '-'}{'e' if E.rankpar[h] == 0 else 'o'}")
                elif a != b: seq.append(f"{k}:L")
            print("TRACE", name, "phase", i, j, "fallbacks", [k for k in range(i, j) if R[k]["fb"]], "z", z, " ".join(seq))
        for k in range(i, j):
            a, b = R[k]["vs"], R[k + 1]["vs"]
            D = Dset(g, R[k]) | Dset(g, R[k + 1])
            gy = {R[k]["sb"][u] for u in D if R[k]["sb"][u] != R[k + 1]["sb"][u]}
            for z in range(n):
                if a[z] == b[z]: continue
                if E.key(b[z]) < E.key(a[z]): C["WRONG"] += 1
                if a[z][1] == b[z][1]: C["LR"] += 1; continue
                x = a[z][1] ^ b[z][1]; h = x.bit_length() - 1; d = "IN" if b[z][1] >> h & 1 else "OUT"
                C["MR"] += 1; C["MR_" + d + "_" + ("even" if E.rankpar[h] == 0 else "odd")] += 1
                nr[z] += 1; mph[(z, h, d)] += 1
                if k in rid: mrun[(rid[k], z, h, d)] += 1
                if z in gy:
                    C["GATE_rise"] += 1
                    if mph[(z, h, d)] > 1: C["GATE_rise_repeat_ph"] += 1
        if mph:
            m = max(mph.values()); C["MULT_ph"] = max(C["MULT_ph"], m)
            if m > 1:
                C["phases_mult"] += 1; z, h, d = max(mph, key=mph.get); EX.append(("MULT", name, i, z, h, d, m, n))
        if mrun: C["MULT_run"] = max(C["MULT_run"], max(mrun.values()))
        tr = Counter()
        for k in range(i, j):
            for z in range(n):
                if R[k]["vs"][z] != R[k + 1]["vs"][z]: tr[z] += 1
        if tr:
            C["XIRISES_max"] = max(C["XIRISES_max"], max(tr.values())); r = 100 * max(tr.values()) // n
            if r > C["XIRISES_x100_over_n_max"]: C["XIRISES_x100_over_n_max"] = r; C["XIRISES_argmax_" + name.replace(" ", "_")] = max(tr.values())
            C["PHASELEN_x100_over_n_max"] = max(C["PHASELEN_x100_over_n_max"], 100 * (j - i) // n)
        if nr: C["RISES_max"] = max(C["RISES_max"], max(nr.values())); C["RISES_minus_n_max_plus1000"] = max(C["RISES_minus_n_max_plus1000"], 1000 + max(nr.values()) - n)

def main():
    a = sys.argv[1:]
    if a[0] == "--one": run(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        kmin = int(a[2]) if len(a) > 2 else 1; ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        for line in open(a[1]):
            tk = line.split() if line.strip() and not line.startswith("#") else []
            if not tk: continue
            f = tk[0]; P = lambda x: os.path.join(ROOT, x) if os.path.exists(os.path.join(ROOT, x)) else os.path.join(ROOT, "experiments", x)
            g = load(P(f))
            if g.n > int(os.environ.get("NMAX", "48")) or sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2) < kmin: continue
            run(g, f, readstart(P(tk[1])) if len(tk) > 1 else None); rng = random.Random(f)
            for _ in range(int(os.environ.get("RS", "0"))):
                run(g, f + " rs", ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                   {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}))
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for x in sorted(EX, key=lambda e: -e[6])[:6]: print("EXAMPLE", x)

if __name__ == "__main__":
    main()
