#!/usr/bin/env python3
"""L-COMP box 18 (b): cheap invariant checks from L-LIT T32 (docs/lit/T32-n5-frontier-crossfield.md @ l-lit a06dc24a) on n5b runs.
- LIP (T32 §E1 (b), CONJECTURE LIP): in every maximal REL segment [a, b] (box17.segments), for v ∈ E_b := (Even ∩ X_b) ∖ T (T = vertices of
  the cycles CW_b ∪ CH_b) and every t ∈ [a, b]: SW_[a,t](v) ≤ SW_[a,t](w) + 1, where SW_[a,t](x) = #{s ∈ [a, t) : σ_s(x) ≠ σ_{s+1}(x)} and
  w = jW(v) (first Even vertex outside T after v on v's W-play at b; SW(⊥) := 0) or jH(v) (same on the honest play). Three readings
  are counted: LIP-W (w = jW), LIP-H (w = jH), LIP-OR (the inequality for at least one of the two).
- HAM-MONO (T32 §E7): per (vertex v, phase P = [i, j]), at every P-change t → t+1 of P_t := P(Ξ_t v): d_{t+1} > d_t with d_t := |P_t Δ P_i|
  (strict), and the weak forms: non-decreasing; strict / non-decreasing on even ranks only and on odd ranks only.
- NEST-FACE (ii) (T32 §E7): k_t := the largest rank in P_{t+1} Δ P_i at the P-change t → t+1; k does not decrease along the P-changes of
  (v, P). Part (i) ("Ξ-best among the path sets REALIZABLE at t+1 agreeing with P_i above k") is NOT tested: "realizable" is not
  defined in T32 (READING needed).
Usage: inv.py [--list FILE] | GAME [START]   (prints per instance the failure counts and the first failure of each)"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import nm  # noqa: E402
B = nm.B


def frames(e, R, b):
    """E_b, jW, jH at state b (definitions as N5-LAY-box27 §1)."""
    g = e.g; Bs = R[b]; X = set(); st = list(e.Q); CW = set(); CH = set()
    while st:
        x = st.pop()
        if x in X:
            continue
        X.add(x); pw, cw = B.play(Bs["wn"], x); ph, ch = B.play(Bs["hn"], x); CW.add(cw); CH.add(ch)
        st += [y for y in pw + cw + ph + ch if g.owner[y] == 0 and y not in X]
    T = {v for c in CW | CH for v in c}; E = {v for v in X if v not in T}

    def j(nx, v):
        x = nx[v]; seen = {v}
        while x not in seen:
            if g.owner[x] == 0 and x not in T:
                return x
            seen.add(x); x = nx[x]
        return None
    return E, {v: j(Bs["wn"], v) for v in E}, {v: j(Bs["hn"], v) for v in E}


def check(g, st=None):
    e = B.Eng(g); R = B.trajectory(e, st or e.start()); w = nm.wmap(g); C = {}; first = {}

    def bad(k, info):
        C[k] = C.get(k, 0) + 1; first.setdefault(k, info)
    for i, j in B.phases(R):
        for s, t_e in B.runs_of(R, i, j):
            if t_e <= s:
                continue
            for a, b, _ in B.segments(e, R, s, t_e):
                if b <= a:
                    continue
                E, jW, jH = frames(e, R, b); C["lip_checks"] = C.get("lip_checks", 0) + len(E) * (b - a)
                sw = {v: 0 for v in range(g.n)}
                for t in range(a, b + 1):
                    if t > a:
                        for v in e.Q:
                            if R[t - 1]["s"][v] != R[t]["s"][v]:
                                sw[v] += 1
                    for v in E:
                        cw = sw[v] <= (sw[jW[v]] if jW[v] is not None else 0) + 1
                        ch = sw[v] <= (sw[jH[v]] if jH[v] is not None else 0) + 1
                        if not cw: bad("LIP-W", (a, b, t, v, sw[v], jW[v]))
                        if not ch: bad("LIP-H", (a, b, t, v, sw[v], jH[v]))
                        if not (cw or ch): bad("LIP-OR", (a, b, t, v, sw[v], jW[v], jH[v]))
        for v in range(g.n):
            P0 = R[i]["xi"][v][1]; dprev = (0, 0, 0); kprev = None
            for t in range(i, j):
                A, Bn = R[t]["xi"][v][1], R[t + 1]["xi"][v][1]
                if A == Bn:
                    continue
                C["pchanges"] = C.get("pchanges", 0) + 1
                D = Bn ^ P0; d = (len(D), sum(1 for x in D if w[x] > 0), sum(1 for x in D if w[x] < 0))
                for k, name in enumerate(("", "-EVEN", "-ODD")):
                    if not d[k] > dprev[k]: bad("HAM-MONO" + name, ((i, j), v, t, dprev[k], d[k]))
                    if not d[k] >= dprev[k]: bad("HAM-WEAK" + name, ((i, j), v, t, dprev[k], d[k]))
                k_t = max((abs(w[x]) for x in D), default=0)
                if kprev is not None and k_t < kprev: bad("NEST-FACE(ii)", ((i, j), v, t, kprev, k_t))
                dprev, kprev = d, k_t
    return R, C, first


def main():
    a = sys.argv[1:]; items = []
    if a[0] == "--list":
        for line in open(a[1]):
            p = line.split()
            if p and not p[0].startswith("#"):
                items.append((os.path.join(nm.EXP, p[0]), os.path.join(nm.EXP, p[1]) if len(p) > 1 and os.environ.get("START") == "1" else None))
    else:
        items.append((a[0], a[1] if len(a) > 1 else None))
    for gp, sp in items:
        g = nm.load(gp); e = B.Eng(g); st = nm.startof(g, e, sp) if sp else None
        try:
            R, C, first = check(g, st)
        except Exception as ex:  # noqa: BLE001
            print("ERROR", gp, repr(ex)[:200], flush=True); continue
        print("INV", os.path.relpath(gp, nm.EXP), "start" if sp else "S3", "n", g.n, "states", len(R), json.dumps(C), json.dumps({k: str(v) for k, v in first.items()}), flush=True)


if __name__ == "__main__":
    main()
