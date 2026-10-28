#!/usr/bin/env python3
"""L-SI box 23 (successor 19): DATA for docs/si/N5-ALT-box23.md (FRESH-EDGE). Per phase and fallback-free run S: a transition t -> t+1 is
FRESH (scope run / phase) if some Even w switches at it to an edge (w, y) that w held at NO earlier state of the scope. NOFRESH_run /
NOFRESH_ph count the other transitions (every in-phase transition has an Even switch or is a fallback/Odd step: R38). Each NOFRESH transition
is tagged GCH if a gate's sigma-bar changes at it. NOFRESH2_gci_gch: a sigma-bar-changing transition inside a global C-interval with neither a fresh Even edge nor a gate moving to an option it did not hold earlier in that C-interval (FRESH2; gate options held at the interval's first state count as held). NOFRESH3_gci(_gch): inside a global C-interval, neither a fresh Even edge, nor a fresh gate option, nor a strict shrink of A (A_t+1 < A_t; A is non-increasing on the interval, so each vertex leaves A once per interval) (FRESH3). gci_kind_<E><O><A>[_gch]: the in-interval transitions by which of the three fresh events they carry. NOFRESH_gci: the same with scope = the global C-interval (P-N5-GCX §1) containing the transition. RET_EVEN_run: Even switches back to an edge held earlier in the run.
FMUT=1 (control): A-shrinks are not credited; NOFRESH3 must then rise (post31_n48).
Usage: fresh.py --one GAME [START] | --list FILE [KMIN] (env RS, NMAX). VERB=1 prints the NOFRESH_run transitions."""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from common import rows, phases, load, readstart, Dset, avoid
C = Counter(); EX = []

def run(g, name, start=None):
    E, R = rows(g, start); n = g.n; Ev = [v for v in range(n) if g.owner[v] == 0]
    for i, j in phases(R):
        runs, s = [], i
        for k in range(i, j):
            if R[k]["fb"]: runs.append((s, k)); s = k + 1
        runs.append((s, j))
        hph = {w: {R[i]["s"][w]} for w in Ev}
        info = {}
        for k in range(i, j + 1):
            Dk = Dset(g, R[k]); Ak = avoid(R[k]["wn"], Dk, n)
            info[k] = (frozenset(Dk), frozenset(Ak), {u: (E.weight(R[k]["vs"][R[k]["t"][u]][1]) - E.weight(R[k]["vs"][R[k]["sb"][u]][1]))
                       for u in Dk if R[k]["sb"][u] in Ak and R[k]["t"][u] in Ak})
        incut = lambda k: info[k + 1][1] <= info[k][1] and info[k + 1][0] == info[k][0] and info[k + 1][2] == info[k][2]
        for s, e in runs:
            hr = {w: {R[s]["s"][w]} for w in Ev}; nf = 0; hg = {w: {R[s]["s"][w]} for w in Ev}; gl = 0; ho = {}
            for k in range(s, e):
                sw = [w for w in Ev if R[k]["s"][w] != R[k + 1]["s"][w]]
                fr = any(R[k + 1]["s"][w] not in hr[w] for w in sw); fp = any(R[k + 1]["s"][w] not in hph[w] for w in sw)
                C["RET_EVEN_run"] += sum(R[k + 1]["s"][w] in hr[w] for w in sw); C["trans"] += 1; C["noswitch"] += not sw
                gch = any(R[k]["sb"][u] != R[k + 1]["sb"][u] for u in Dset(g, R[k]) | Dset(g, R[k + 1]))
                if not fr:
                    C["NOFRESH_run"] += 1; C["NOFRESH_run_gch"] += gch; nf += 1
                    if os.environ.get("VERB") == "1": print("NOFRESH", name, i, s, k, [(w, R[k]["s"][w], R[k + 1]["s"][w]) for w in sw])
                if not fp: C["NOFRESH_ph"] += 1
                if incut(k):                                     # inside a global C-interval (GCI scope)
                    gl += 1; C["trans_gci"] += 1
                    if not any(R[k + 1]["s"][w] not in hg[w] for w in sw):
                        C["NOFRESH_gci"] += 1; C["NOFRESH_gci_gch"] += gch
                        if os.environ.get("VERB") == "1" and (gch or os.environ.get("ALL") == "1"): print("NOFRESH_GCI", name, i, s, k, "gch", gch, [(w, R[k]["s"][w], R[k + 1]["s"][w]) for w in sw])
                    gu = [u for u in Dset(g, R[k]) | Dset(g, R[k + 1]) if R[k]["sb"][u] != R[k + 1]["sb"][u]]
                    fe = any(R[k + 1]["s"][w] not in hg[w] for w in sw); fo = any(R[k + 1]["sb"][u] not in ho.setdefault(u, {R[k]["sb"][u]}) for u in gu)
                    ash = info[k + 1][1] < info[k][1] and os.environ.get("FMUT") != "1"      # FMUT=1: control, A-shrinks not credited
                    C["gci_kind_" + "".join(x for x, b in (("E", fe), ("O", fo), ("A", ash)) if b) + ("_gch" if gch else "")] += 1
                    if not (fe or fo or ash):
                        C["NOFRESH3_gci"] += 1; C["NOFRESH3_gci_gch"] += gch
                        if gch: EX.append(("NF3", name, i, s, k, gu, [(w, R[k]["s"][w], R[k + 1]["s"][w]) for w in sw]))
                    if gch:
                        C["gci_gch"] += 1
                        if not fe and not fo:
                            C["NOFRESH2_gci_gch"] += 1; EX.append(("NF2", name, i, s, k, gu, [(w, R[k]["s"][w], R[k + 1]["s"][w]) for w in sw]))
                        elif not fe: C["gci_gch_oddonly"] += 1
                    for u in gu: ho.setdefault(u, {R[k]["sb"][u]}).add(R[k + 1]["sb"][u])
                    for w in sw: hg[w].add(R[k + 1]["s"][w])
                else:
                    gl = 0; hg = {w: {R[k + 1]["s"][w]} for w in Ev}; ho = {}
                for w in sw: hr[w].add(R[k + 1]["s"][w]); hph[w].add(R[k + 1]["s"][w])
            if e > s:
                C["runs"] += 1; C["NOFRESH_run_max"] = max(C["NOFRESH_run_max"], nf)
                if nf: EX.append(("NF", name, i, s, e, nf, n))
            if e < j:
                for w in Ev: hph[w].add(R[e + 1]["s"][w])

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
    for x in sorted([e for e in EX if e[0] == "NF"], key=lambda e: -e[5])[:6] + [e for e in EX if e[0] == "NF2"][:6] + [e for e in EX if e[0] == "NF3"][:6]: print("EXAMPLE", x)

if __name__ == "__main__":
    main()
