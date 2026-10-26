#!/usr/bin/env python3
"""L-SI box 22 (successor 18): DATA for docs/si/N5-EXIT-box22.md. EXIT_x per phase (P-N5-OFFMONO-box49 §2, CHAIN-COUNT): for a phase, its
class c and x in Q_c := (Q cap U_c) - {c}, par_t(x) := the first vertex of Q - {x} on x's honest play at t strictly before c (c if none);
an EXIT change at t -> t+1 is par_t(x) != par_t+1(x). Every exit change is classified:
  CYC    x on its honest cycle at t or t + 1 (R72's CYC);
  RT     sigma-bar(x) unchanged (an Even switch on the chosen option's class exit path re-routes it; the switching Even vertices are
         recorded: on the old class exit path, ALWAYS expected (rt_onpath) -- RT_V counts the others);
  CH     sigma-bar(x) changes, y1 -> y2. CHV: the class exit paths AND exits (relay.py exits()) of y1 and y2 are the same at t and t + 1
         (pure value; the relay ping-pong); CHR: otherwise. For CHV the cause is recorded: P1UP (kappa(p1) rises strictly, p1 := par_t(x)),
         VIAB (y1's honest play at t + 1 passes x), TIE (neither: equal kappa options); CHV_V counts CHV with none of the three.
Per x the exit sequence is recorded: RET = an exit change back to an exit used earlier in the phase (ping-pong), NEX = distinct exits.
Root cause of a CHV exit change (the chain of R72's CHOSEN read on exits): follow p1 := par_t(x); if p1 has an exit change at the same
transition, continue at p1 (its own class), else stop: the end is OFF (p1's offset to its fixed parent rises: same-exit rise), RT/CHR/CYC
at p1, or VAL (p1 = c ... impossible in a phase, counted as ROOTC_V). DEPTH = the chain length.
Totals and per-(phase, class) lines (-v): game, phase [i, j], len, c, |U_c|, k = |Q_c|, sum EXIT, max EXIT_x, RT, CHV, CHR, CYC.
MUT=1: the exit is taken at t + 1 from the state t (a shifted classification): CHV_V must bite.
Usage: exitx.py --one GAME [START] [-v] | --list FILE [KMIN] (env RS, NMAX) | --rand COUNT NLO NHI SEED (env K)"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "rund"))
from common import rows, phases, M, load, readstart
from relay import exits
C = Counter(); VERB = "-v" in sys.argv; MUT = os.environ.get("MUT") == "1"; LINES = []; VIOL = []

def hplay(A, z, c):
    nx = A["nxt"]; out, x, seen = [], z, set()
    while x not in seen and x != c: seen.add(x); out.append(x); x = nx[x]
    return out

def oncyc(A, q):
    nx = A["nxt"]; x, seen = nx[q], set()
    while x not in seen and x != q: seen.add(x); x = nx[x]
    return x == q

def par(A, x, c, Qs):
    for z in hplay(A, x, c)[1:]:
        if z in Qs: return z
    return c

def chain(A, x, c, Qs):
    out = [x]
    while out[-1] != c and len(out) <= len(Qs) + 1: out.append(par(A, out[-1], c, Qs))
    return out

def kap(E, A, z, sc):
    return (M(E, A["vs"][z]), sc * A["vs"][z][2])

def run(g, name, start=None):
    E, R = rows(g, start)
    Qs = {v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2}
    for i, j in phases(R):
        C["phases"] += 1
        cls = {}
        for v in range(g.n): cls.setdefault(R[i]["vs"][v][0], []).append(v)
        for c, Ul in cls.items():
            U = set(Ul); Qc = sorted((Qs & U) - {c})
            if not Qc: continue
            C["classes"] += 1; sc = 1 if E.par[c] == 1 else -1
            P = [{x: par(R[t], x, c, Qs) for x in Qc} for t in range(i, j + 1)]
            ex = Counter(); seq = {x: [P[0][x]] for x in Qc}; kinds = Counter(); evs = {}
            for t in range(i, j):
                A, B = R[t], R[t + 1]; pa, pb = P[t - i], P[t + 1 - i]
                if MUT and t + 2 - i < len(P): pb = P[t + 2 - i]
                for x in Qc:
                    if pa[x] == pb[x]: continue
                    ex[x] += 1; seq[x].append(pb[x])
                    if oncyc(A, x) or oncyc(B, x): kd = "CYC"
                    elif A["sb"][x] == B["sb"][x]:
                        kd = "RT"; old = set(hplay(A, A["sb"][x], c)); old = {z for z in old if g.owner[z] == 0}
                        sw = [z for z in range(g.n) if g.owner[z] == 0 and A["s"][z] != B["s"][z]]
                        if any(z in old for z in sw): C["rt_onpath"] += 1
                        else: C["RT_V"] += 1; VIOL.append(("RT", name, t, x))
                    else:
                        y1, y2 = A["sb"][x], B["sb"][x]
                        ea = {y: (p, e) for y, p, e in exits(A["nxt"], x, c, Qs, g.succ)}
                        eb = {y: (p, e) for y, p, e in exits(B["nxt"], x, c, Qs, g.succ)}
                        p1_, p2_ = pa[x], pb[x]; pl2 = hplay(B, y2, c) + [c]
                        if ea[y1] == eb[y1] and p1_ in pl2 and not oncyc(A, x) and not oncyc(B, x):      # Lemma NO-UP's hypotheses
                            lv = [w for w in pl2[:pl2.index(p1_)] if w in Qs and w != c]
                            if not any(oncyc(A, w) for w in lv):
                                tie = kap(E, A, y1, sc) == kap(E, A, y2, sc) and kap(E, B, y1, sc) == kap(E, B, y2, sc)
                                C["noup_checks"] += 1
                                if not tie: C["NOUP_V"] += 1; VIOL.append(("NOUP", name, t, x))
                        if ea[y1] == eb[y1] and not oncyc(A, x) and not oncyc(B, x):                     # Lemma PUSH
                            pl1 = hplay(B, p1_, c) + [c] if p1_ != c else [c]
                            tie1 = kap(E, B, y1, sc) == kap(E, B, y2, sc)
                            for m in [w for w in pl2 if (w in Qs or w == c)]:
                                lv = [w for w in pl2[:pl2.index(m)] if w in Qs and w != c]
                                if any(oncyc(A, w) for w in lv): continue
                                rr = p2_ if os.environ.get("PUSHMUT") == "1" else p1_
                                d = tuple(a - b - e + f for a, b, e, f in zip(kap(E, B, rr, sc), kap(E, B, m, sc), kap(E, A, rr, sc), kap(E, A, m, sc)))
                                C["push_checks"] += 1; C["push_m_is_c"] += (m == c); C["push_m_is_p1"] += (m == p1_)
                                if not (d > (0, 0) or tie1): C["PUSH_V"] += 1; VIOL.append(("PUSH", name, t, x, m))
                        if ea[y1] == eb[y1] and ea[y2] == eb[y2]:
                            kd = "CHV"; p1 = pa[x]; p2 = pb[x]
                            ch2 = chain(B, p2, c, Qs); ch1 = chain(A, p1, c, Qs)
                            rel = "UP" if p1 in ch2 else ("DOWN" if p2 in ch1 else "DISJ"); C["chv_" + rel] += 1
                            if rel == "UP" and chain(A, p2, c, Qs)[:ch2.index(p1) + 1] == ch2[:ch2.index(p1) + 1]: C["chv_UP_fixedchain"] += 1
                            if kap(E, B, p1, sc) > kap(E, A, p1, sc): C["chv_P1UP"] += 1
                            elif x in hplay(B, y1, c): C["chv_VIAB"] += 1
                            elif kap(E, A, y1, sc) == kap(E, A, y2, sc): C["chv_TIE"] += 1
                            else: C["CHV_V"] += 1; VIOL.append(("CHV", name, t, x))
                        else: kd = "CHR"
                    if kd != "CYC" and kap(E, A, x, sc) == kap(E, B, x, sc):                         # Lemma EXIT-RHO
                        if kap(E, A, A["sb"][x], sc) == kap(E, A, B["sb"][x], sc) and A["sb"][x] != B["sb"][x]: C["rho_tie"] += 1
                        else: C["RHO_V"] += 1; VIOL.append(("RHO", name, t, x))
                    kinds[kd] += 1; C[kd] += 1; evs[(t, x)] = kd
                    if kd in ("RT", "CHR"):
                        p1, p2 = pa[x], pb[x]; ch2 = chain(B, p2, c, Qs); ch1 = chain(A, p1, c, Qs)
                        C[kd.lower() + "_" + ("UP" if p1 in ch2 else ("DOWN" if p2 in ch1 else "DISJ"))] += 1
                    if os.environ.get("TRACE") == str(x): print("TR", t, x, pa[x], "->", pb[x], kd, "sb", A["sb"][x], B["sb"][x])
                    if pb[x] in seq[x][:-1]: C["RET"] += 1
            # root causes of CHV exit changes: follow old exits down while they also change exit at the same transition
            for (t, x), kd in evs.items():
                if kd != "CHV": continue
                y, d = x, 0
                while True:
                    p1 = P[t - i][y]
                    if p1 == c: C["ROOTC_V"] += 1; break
                    d += 1
                    if (t, p1) in evs:
                        if evs[(t, p1)] != "CHV": C["root_" + evs[(t, p1)]] += 1; break
                        y = p1; continue
                    pp = P[t - i][p1]
                    if pp == P[t + 1 - i][p1]: C["root_OFF"] += 1
                    else: C["root_OTHER"] += 1
                    break
                C["depth_max"] = max(C["depth_max"], d); C["depth_sum"] += d
            for x in Qc:
                last = {}; prev = None
                for t in range(i, j + 1):
                    p = P[t - i][x]
                    if oncyc(R[t], x): prev = None; continue
                    o = tuple(a - b for a, b in zip(kap(E, R[t], x, sc), kap(E, R[t], p, sc)))
                    if p in last and o < last[p]:
                        C["PEM_drop_in" if prev == p else "PEM_drop_ret"] += 1
                        if prev != p: VIOL.append(("PEM", name, t, x, p)) if os.environ.get("PEMV") else None
                    if p in last and o > last[p]: C["PEM_rise_in" if prev == p else "PEM_rise_ret"] += 1
                    if p in last and o == last[p] and prev != p: C["PEM_eq_ret"] += 1
                    last[p] = o; prev = p
            if os.environ.get("MR") == "1":            # Lemma MONO-REF: off(z; m) never falls when m is on z's honest (t+1)-play
                for t in range(i, j):
                    A, B = R[t], R[t + 1]
                    for z in U:
                        if z == c: continue
                        pl = hplay(B, z, c) + [c]; qs = [w for w in pl if w in Qs and w != c]
                        refs = [w for w in pl[1:] if w in Qs or w == c]
                        if os.environ.get("MRMUT") == "1": refs = [w for w in Qc if w not in pl][:1]
                        for m in refs:
                            lv = [w for w in qs if pl.index(w) < (pl.index(m) if m in pl else len(pl))]
                            if any(oncyc(A, w) for w in lv): C["mr_skip_cyc"] += 1; continue
                            d = tuple(a - b - e + f for a, b, e, f in zip(kap(E, B, z, sc), kap(E, B, m, sc), kap(E, A, z, sc), kap(E, A, m, sc)))
                            C["mr_checks"] += 1
                            if d < (0, 0): C["MR_V"] += 1; VIOL.append(("MR", name, t, z, m))
                            elif d > (0, 0): C["mr_rise"] += 1
            phi = [sum(len(chain(R[t], x, c, Qs)) - 1 for x in Qc) for t in range(i, j + 1)]; nd = no = 0   # Lemma DEPTH
            for t in range(i, j):
                ch = [x for x in Qc if P[t - i][x] != P[t + 1 - i][x]]
                if not ch: continue
                if all(P[t + 1 - i][x] in chain(R[t], P[t - i][x], c, Qs) for x in ch):
                    nd += 1
                    if phi[t + 1 - i] >= phi[t - i]: C["DEPTH_V"] += 1; VIOL.append(("DEPTH", name, t))
                else: no += 1
            rr = dj = cy = 0                                  # the reduction's terms: RR (chosen-route re-routing), DJ (DISJ exit change), CYC'
            for t in range(i, j):
                A, B = R[t], R[t + 1]
                sw = {w for w in U if g.owner[w] == 0 and A["s"][w] != B["s"][w]}
                rr += any(any(z in sw for z in hplay(A, A["sb"][x], c)[:hplay(A, A["sb"][x], c).index(P[t - i][x]) if P[t - i][x] in hplay(A, A["sb"][x], c) else None]) for x in Qc)
                dj += any(P[t - i][x] != P[t + 1 - i][x] and P[t - i][x] not in chain(B, P[t + 1 - i][x], c, Qs) and P[t + 1 - i][x] not in chain(A, P[t - i][x], c, Qs) for x in Qc)
                cy += any(oncyc(A, x) or oncyc(B, x) for x in Qc)
            C["RR_c"] += rr; C["DJ_c"] += dj; C["CYCp_c"] += cy; C["N_ex"] += nd + no
            if nd + no > (len(Qc) ** 2 - len(Qc) + 1) * (1 + rr + dj + cy): C["RED_V"] += 1; VIOL.append(("RED", name, i))
            C["n_alldown"] += nd; C["n_other"] += no; k_ = len(Qc)
            if nd > (k_ * k_ - k_) * (1 + no): C["DEPTHB_V"] += 1
            if no: C["down_per_other_x100_max"] = max(C["down_per_other_x100_max"], 100 * nd // no)
            T = set(Qc) | {c}
            def exT(S, w):
                for z in hplay(S, w, c)[1:] + [c]:
                    if z in T: return z
            for t in range(i, j):                       # Even own moves: w switches and its exit changes; UP/DOWN/DISJ as for Odd
                A, B = R[t], R[t + 1]
                for w in U:
                    if g.owner[w] != 0 or w == c or A["s"][w] == B["s"][w]: continue
                    e1, e2 = exT(A, w), exT(B, w)
                    if e1 == e2: C["ev_same"] += 1; continue
                    ch2 = chain(B, e2, c, Qs) if e2 != c else [c]; ch1 = chain(A, e1, c, Qs) if e1 != c else [c]
                    rel = "UP" if e1 in ch2 else ("DOWN" if e2 in ch1 else "DISJ"); C["ev_" + rel] += 1
                    a, b = A["s"][w], B["s"][w]                # Even-NO-RETURN check: a DOWN move back to a successor left by an UP move
                    pa_ = hplay(A, a, c) + [c]; pb_ = hplay(B, a, c) + [c]
                    if rel == "DOWN" and pa_[:pa_.index(e2) + 1 if e2 in pa_ else 0] == pb_[:pb_.index(e2) + 1 if e2 in pb_ else 0]: C["ev_DOWN_newpathfixed"] += 1
            sw = Counter(); swt = 0
            for t in range(i, j):
                ws = [w for w in U if g.owner[w] == 0 and R[t]["s"][w] != R[t + 1]["s"][w]]
                for w in ws: sw[w] += 1
                swt += bool(ws)
            C["ESW_sum"] += sum(sw.values()); C["ESW_trans"] += swt
            if sw: C["ESW_max_per_vertex"] = max(C["ESW_max_per_vertex"], max(sw.values()))
            tot = sum(ex.values()); C["EXIT_sum"] += tot
            mx = max(ex.values()) if ex else 0; C["EXIT_max"] = max(C["EXIT_max"], mx)
            nex = max(len(set(s)) for s in seq.values()); C["NEX_max"] = max(C["NEX_max"], nex)
            ln = j - i; C["len_max"] = max(C["len_max"], ln)
            if mx: C["ratio_x100_max"] = max(C["ratio_x100_max"], 100 * mx // ln)
            LINES.append((name, i, j, ln, c, len(U), len(Qc), tot, mx, kinds["RT"], kinds["CHV"], kinds["CHR"], kinds["CYC"], nex,
                          sum(sw.values()), max(sw.values()) if sw else 0))

def main():
    a = [x for x in sys.argv[1:] if x != "-v"]
    if a[0] == "--one":
        run(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    elif a[0] == "--rand":                                 # random C^kO games as gcx.py --rand
        ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box43")); from multi import rand_ckO
        cnt, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); q = 0; K = int(os.environ.get("K", "0"))
        while q < cnt:
            g = rand_ckO(rng, lo, hi, K or rng.choice((2, 2, 3, 4)))
            if g is None: continue
            q += 1
            st = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1})
            run(g, f"rand seed {seed} #{q}", None if q % 2 else st)
    elif a[0] == "--list":
        kmin = int(a[2]) if len(a) > 2 else 1; ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        for line in open(a[1]):
            f = line.split()[0] if line.strip() and not line.startswith("#") else None
            if not f: continue
            g = load(os.path.join(ROOT, f))
            if g.n > int(os.environ.get("NMAX", "48")) or sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2) < kmin:
                continue
            run(g, f); rng = random.Random(f)
            for _ in range(int(os.environ.get("RS", "0"))):
                run(g, f + " rs", ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                   {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}))
    if VERB:
        for L in LINES:
            if L[7]: print("PC", *L)
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for v in VIOL[:8]: print("VIOLATION", v)
    print("EXITX PASS" if not VIOL else "EXITX FAIL")

if __name__ == "__main__":
    main()
