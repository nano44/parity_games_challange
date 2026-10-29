#!/usr/bin/env python3
"""L-SI box 32 (docs/si/N5-RTC-box32.md): CONJECTURE R*-TC (R*_T <= TC) by an injection. For every frozen W-phase (all D != {}; the
same-pair core is reported separately): the late-adoption* transitions s (some Even y switches at s -> s+1 to w with (y, w) BLOCKED at an
earlier state t of the phase: W_t(w) > W_t(rho_t y), (y, w) not in I_sigma_t) and the basin-changing transitions (TC). Candidates of s:
{s} if s changes a basin; else the basin-changing transitions s' in [t, s) at which y or w changes basin, t := the LAST state < s at which
(y, w) was blocked (union over the late* adoptions of s). Checks:
  LEMMA  (Lemma LATE-BASIN): a non-basin-changing s whose w had, at t, a same-pair gate with G3* at t has a non-empty candidate set;
  MATCH  a maximum matching of late* transitions into candidates has size R*_T (an injection exists; implies R*_T <= TC);
  NAIVE  the multiplicity of the map s -> latest candidate (collisions of the naive injection).
MUT=lastonly: candidates = {s} only (the per-transition form, known false: 8 transitions); the MATCH control must fail there.
Usage: inj.py --list FILE | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "frz")); sys.path.insert(0, os.path.join(HERE, "..", "root"))
sys.path.insert(0, os.path.join(HERE, "..", "tord"))
from common import rows, load, readstart, phases
from fwphase import fwphases
from gates import basins
C = Counter(); MX = {}; EX = []
MUT = os.environ.get("MUT", "")

def matching(cand):
    own = {}
    def aug(s, seen):
        for c in cand[s]:
            if c in seen: continue
            seen.add(c)
            if c not in own or aug(own[c], seen): own[c] = s; return True
        return False
    return sum(1 for s in cand if aug(s, set()))

def _run(E, g, R, name):
    n = g.n
    for i, j in phases(R):
        for a, b in fwphases(R, i, j):
            D = {u for u in range(n) if g.owner[u] == 1 and R[a]["sb"][u] != R[a]["t"][u]}
            if not D: continue
            sp = all(R[a]["vs"][d][0] == R[a]["W"][d][0] for d in D)
            tag = "SP" if sp else "NSP"
            F = [basins(R[t]["wn"], D, n) for t in range(a, b + 1)]
            bc = [F[q] != F[q + 1] for q in range(b - a)]
            tc = sum(bc)
            lastbl = {}; cand = {}
            for k in range(a, b):
                Fk = F[k - a]; G3k = {d for d in D if Fk[R[k]["t"][d]] != d and Fk[R[k]["sb"][d]] != d}
                Is = {}
                for x, z in E.improving(tuple(R[k]["s"]), R[k]["vs"]): Is.setdefault(x, set()).add(z)
                late = []
                for y in range(n):
                    if g.owner[y] != 0: continue
                    w = R[k + 1]["s"][y]
                    if w != R[k]["s"][y] and (y, w) in lastbl: late.append((y, w, lastbl[(y, w)]))
                kr = None
                for y in range(n):
                    if g.owner[y] != 0: continue
                    kr = E.key(R[k]["W"][R[k]["s"][y]])
                    for w in g.succ[y]:
                        if w != R[k]["s"][y] and w not in Is.get(y, set()) and E.key(R[k]["W"][w]) > kr:
                            lastbl[(y, w)] = (k, Fk[w], Fk[w] != -1 and Fk[w] in G3k and R[k]["vs"][Fk[w]][0] == R[k]["W"][Fk[w]][0])
                if not late: continue
                cs = set()
                if bc[k - a]: cs.add(k)
                elif MUT != "lastonly":
                    for y, w, (t, _, _) in late:
                        for q in range(t, k):
                            if bc[q - a] and (F[q - a][y] != F[q + 1 - a][y] or F[q - a][w] != F[q + 1 - a][w]): cs.add(q)
                    if not cs:
                        C[tag + "_noBC_empty"] += 1
                        if all(gd for _, _, (_, _, gd) in late):
                            C["LEMMA_VIOL"] += 1
                            if len(EX) < 6: EX.append(("LEMMA_VIOL", name, a, b, k, late))
                        elif len(EX) < 6: EX.append(("empty(not same-pair G3* at t)", name, a, b, k, late))
                if not bc[k - a]:
                    C[tag + "_late_noBC"] += 1
                    if os.environ.get("SHOW") == "1" and sp: print("NOBC", name, a, b, "s", k, "late", [(y, w, t) for y, w, (t, _, _) in late], "cand", sorted(cs), "gap", k - max(cs) if cs else None, flush=True)
                cand[k] = sorted(cs)
            if not cand: continue
            rT = len(cand); m = matching(cand)
            naive = Counter(c[-1] for c in cand.values() if c)
            mult = max(naive.values()) if naive else 0
            C[tag + "_phases"] += 1; C[tag + "_RT"] += rT; C[tag + "_TC"] += tc
            if rT > tc: C[tag + "_RT>TC"] += 1
            if m < rT:
                C[tag + "_MATCH_FAIL"] += 1
                if len(EX) < 6: EX.append(("MATCH_FAIL", name, a, b, rT, m, tc))
            if mult > 1: C[tag + "_naive_collision"] += 1
            for key, v in ((tag + " RT", rT), (tag + " RT/(TC+1)", rT / (tc + 1)), (tag + " naive_mult", mult)):
                if v > MX.get(key, (-99,))[0]: MX[key] = (v, rT, tc, m, n, len(D), name, a, b)

def run(g, name, start=None):
    E, R = rows(g, start, cap=20000); _run(E, g, R, name)

def main():
    a = sys.argv[1:]
    if a[0] == "--one": run(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        for line in open(a[1]):
            p = line.split() if line.strip() and not line.startswith("#") else None
            if p:
                f = os.path.join(ROOT, p[0]) if os.path.exists(os.path.join(ROOT, p[0])) else os.path.join(ROOT, "experiments", p[0])
                s = None
                if len(p) > 1 and os.environ.get("START") == "1":
                    s = os.path.join(ROOT, p[1]) if os.path.exists(os.path.join(ROOT, p[1])) else os.path.join(ROOT, "experiments", p[1])
                try: run(load(f), p[0], readstart(s) if s else None)
                except Exception as e: C["SKIPPED_input"] += 1
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    print("columns: value, R*_T, TC, matching, n, |D|, game, a, b")
    for k in sorted(MX): print("MAX", k, MX[k])
    for z in EX: print("EXAMPLE", z)

if __name__ == "__main__": main()
