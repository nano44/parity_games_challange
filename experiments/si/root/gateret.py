#!/usr/bin/env python3
"""L-SI box 23 (successor 19): DATA for ALTERNATION / (G1) (docs/si/N5-ALT-box23.md). Per phase and fallback-free run S (lambda_W constant
checked), every Odd GATE CHANGE: a transition t -> t+1 and an Odd u in D_t cup D_t+1 with sigma-bar_t(u) != sigma-bar_t+1(u). Each is tagged
by its transition's kind (global C-interval of staticdepth.py GCI=1 / P-N5-GCX §1: in = inside a global C-interval; else the first matching cut
kind AG / DCH / OSB / DDSET / OVAL, over all classes at once). RETURNS: u moves to an option y it held earlier and left, counted per scope:
RET_gci (same global C-interval), RET_run (same run S), RET_phase (same phase). MAXCH_run: the most changes of one gate in one run, against
its out-degree (EXC_run: changes of u in S minus (deg(u) - 1), max). For every change y1 -> y2 at u (both in U_lambda(u)): which component of
Xi(y1) rose from t to t+1 (CN cycle node / M path weight / L length / none = tie case) and whether Xi_t+1(y2) < Xi_t+1(y1) strictly.
Usage: gateret.py --one GAME [START] | --list FILE [KMIN] (env RS, NMAX). VERB=1 prints every change."""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from common import rows, phases, load, readstart, Dset, avoid
C = Counter(); EX = []

def run(g, name, start=None):
    E, R = rows(g, start); n = g.n; V = os.environ.get("VERB") == "1"
    deg = {u: len(set(g.succ[u])) for u in range(n)}
    for i, j in phases(R):
        info = {}
        for k in range(i, j + 1):
            Dk = Dset(g, R[k]); Ak = avoid(R[k]["wn"], Dk, n)
            DD = {u: (E.weight(R[k]["vs"][R[k]["t"][u]][1]) - E.weight(R[k]["vs"][R[k]["sb"][u]][1])) for u in Dk
                  if R[k]["sb"][u] in Ak and R[k]["t"][u] in Ak}
            info[k] = (frozenset(Dk), frozenset(Ak), DD)
        runs, s = [], i
        for k in range(i, j):
            if R[k]["fb"]: runs.append((s, k)); s = k + 1
        runs.append((s, j))
        held_ph = {}
        for s, e in runs:
            if e <= s: continue
            lw = {tuple(R[k]["W"][v][0] for v in range(n)) for k in range(s, e + 1)}
            if len(lw) > 1: C["lambdaW_moves"] += 1; continue
            C["runs"] += 1; held_run = {}; held_gci = {}; chg = Counter()
            for u in range(n):
                if g.owner[u] == 1: held_run[u] = {R[s]["sb"][u]}; held_gci[u] = {R[s]["sb"][u]}; held_ph.setdefault(u, set()).add(R[s]["sb"][u])
            for k in range(s, e):
                D0, A0, DD0 = info[k]; D1, A1, DD1 = info[k + 1]
                if not A1 <= A0: kind = "AG"
                elif D0 != D1: kind = "DCH"
                elif DD0 != DD1:
                    ch = {u for u in set(DD0) | set(DD1) if DD0.get(u) != DD1.get(u)}
                    if set(DD0) != set(DD1): kind = "DDSET"
                    elif any(R[k]["sb"][u] != R[k + 1]["sb"][u] for u in ch): kind = "OSB"
                    else: kind = "OVAL"
                else: kind = "in"
                C["trans_" + kind] += 1
                if kind != "in":
                    for u in held_gci: held_gci[u] = {R[k + 1]["sb"][u]}
                for u in sorted(D0 | D1):
                    y1, y2 = R[k]["sb"][u], R[k + 1]["sb"][u]
                    if y1 == y2: continue
                    C["gch_" + kind] += 1; chg[u] += 1
                    a0, a1, b1 = R[k]["vs"][y1], R[k + 1]["vs"][y1], R[k + 1]["vs"][y2]
                    if a0[0] != a1[0]: comp = "CN"
                    elif E.weight(a0[1]) != E.weight(a1[1]): comp = "M"
                    elif a0[2] != a1[2]: comp = "L"
                    else: comp = "none"
                    C["rise_" + comp] += 1; C["y2_strictly_below_y1"] += E.key(b1) < E.key(a1)
                    for sc, H in (("gci", held_gci), ("run", held_run), ("phase", held_ph)):
                        if kind == "in" or sc != "gci":
                            if y2 in H[u]: C["RET_" + sc] += 1; C["RET_" + sc + "_" + kind] += 1
                    if V: print("CHG", name, "ph", i, "run", s, "t", k, kind, "u", u, y1, "->", y2, "rise", comp, "dir", (y1 in A0, y2 in A0), "ret_run", y2 in held_run[u])
                    for H in (held_gci, held_run, held_ph): H[u].add(y2)
            for u, cnt in chg.items():
                C["MAXCH_run"] = max(C["MAXCH_run"], cnt); x = cnt - (deg[u] - 1)
                C["EXC_run_max_plus1000"] = max(C["EXC_run_max_plus1000"], 1000 + x)
                if x > 0: C["EXC_run_gates"] += 1; EX.append(("EXC", name, i, s, u, cnt, deg[u]))

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
    for x in sorted(EX, key=lambda e: -(e[5] - e[6]))[:6]: print("EXAMPLE", x)

if __name__ == "__main__":
    main()
