#!/usr/bin/env python3
"""Box 5 (Lead 19:0xZ): split each phase's OTHER-touching transitions (O) as in L-NEW box 29 (docs/new/N5-NH2-box29.md §0, §4-§5,
l-new 670a63b): crossing-free interval I = maximal run of states of a phase with R constant (R = vertices whose (sigma, tau)-play
reaches o, plus o; F = V \\ R). Each OTHER-touching transition k -> k+1 of the phase is
  CROSS  if R_k != R_{k+1} (charged to X);
  else, inside I: FCH if Xi or W changes at some vertex of F (Lemma F1°: <= |F| - 1 Xi-changes on F per I; on F Xi = W, Lemma G),
                  RONLY if Xi or W changes only on R (o in R), FLAT if no value changes.
Per I also: WC = changes of w = W(o) in I when not H1 and not H2 hold on I (W-CYC), and RONLY per OTHER block (maximal run of
consecutive OTHER states of I; a transition belongs to the block of its OTHER endpoint(s)) for CONJECTURE (OB_R): <= |R|.
O = CROSS + sum_I (FCH + RONLY + FLAT). Usage: xo_split.py game.pg [...]   (prints per phase with O > 0 and per interval)"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
import box4  # noqa: E402,F401  (paths)
sys.path.insert(0, os.path.join(ROOT, "experiments/new/box28"))
from nhprof import profile, load  # noqa: E402
from exh import odd_choice, Rset  # noqa: E402


def split_phases(g, start=None):
    rows, ph = profile(g, start); o = odd_choice(g)
    for r in rows:
        r["R"] = frozenset(Rset(g, r["s"], r["t"], o))           # includes o
        r["other"] = (not all(r["h"])) and r["Xk"] != r["Wk"]
    out = []
    for x, y in ph:
        P = dict(phase=(x, y), it=y - x, O=0, CROSS=0, intervals=[])
        a = x
        for i in range(x + 1, y + 2):
            if i == y + 1 or rows[i]["R"] != rows[i - 1]["R"]:
                b = i - 1; R = rows[a]["R"]; F = set(range(g.n)) - R
                I = dict(states=(a, b), R=len(R), F=len(F), FCH=0, RONLY=0, FLAT=0, WC=0, blocks=[], h12=None)
                nh = all(not rows[k]["h"][0] and not rows[k]["h"][1] for k in range(a, b + 1))
                I["h12"] = "notH1&notH2" if nh else "".join("H%d" % (j + 1) for j in (0, 1) if rows[a]["h"][j]) or "mixed"
                blk, cur = [], None
                for k in range(a, b):
                    A, B = rows[k], rows[k + 1]
                    if nh and A["w"] != B["w"]:
                        I["WC"] += 1
                    if not (A["other"] or B["other"]):
                        cur = None; continue
                    ch = [v for v in range(g.n) if A["Xk"][v] != B["Xk"][v] or A["Wk"][v] != B["Wk"][v]]
                    kind = "FLAT" if not ch else ("FCH" if any(v in F for v in ch) else "RONLY")
                    I[kind] += 1
                    if cur is None or not A["other"]:
                        cur = [0]; blk.append(cur)
                    cur[0] += kind == "RONLY"
                    if not B["other"]:
                        cur = None
                I["blocks"] = [c[0] for c in blk]
                P["intervals"].append(I)
                if i <= y:
                    P["CROSS"] += rows[i - 1]["other"] or rows[i]["other"]
                a = i
        P["O"] = P["CROSS"] + sum(I["FCH"] + I["RONLY"] + I["FLAT"] for I in P["intervals"])
        out.append(P)
    return rows, out


if __name__ == "__main__":
    for f in sys.argv[1:]:
        g = load(f); _, out = split_phases(g)
        for P in out:
            if not P["O"]:
                continue
            Is = P["intervals"]
            print(f"{os.path.basename(f)} n {g.n} phase {P['phase']} ({P['it']} it): O {P['O']} = CROSS {P['CROSS']} + FCH "
                  f"{sum(I['FCH'] for I in Is)} + RONLY {sum(I['RONLY'] for I in Is)} + FLAT {sum(I['FLAT'] for I in Is)}; "
                  f"{len(Is)} crossing-free intervals")
            for I in Is:
                if I["FCH"] + I["RONLY"] + I["FLAT"] + I["WC"]:
                    print(f"   I {I['states']} |R| {I["R"]} (without o {I["R"] - 1}) |F| {I['F']} {I['h12']}: FCH {I['FCH']} (F1° bound {I['F'] - 1}) "
                          f"RONLY {I['RONLY']} (per OTHER block {I['blocks']}; OB_R bound |R| = {I['R']}) FLAT {I['FLAT']} WC {I['WC']}")
