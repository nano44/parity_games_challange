#!/usr/bin/env python3
"""L-COMP box 19: CONJECTURE CUT-Φ (L-LIT T35 §4, docs/lit/T35-howard-quadratic-vs-runquad.md @ l-lit 5bdebc10): at every REL cut
a_i − 1 → a_i (a_i > s) of a fallback-free run [s, e] (cut by box17.segments, = L-SI's seglast.segs), Σ_v Φ_v(P(Ξ v)) rises by ≥ 1 unless
some vertex makes a CARRY at that transition. Φ, carry as P-N5-MPGS (A) (l-lit a23179b0) §A: for vertex v with cycle node c = λ(v)
(constant in the run), R_c = ranks above rank(c), pos(r_k) = k in R_c, w = ±pos (sign by the parity of Ω), Φ_v(A) = Σ_{r ∈ A} w(r);
carry = a P-change that is not MATCHED (n5-box18/nm.matched, = T33's rule). Also counted: cuts with no P-change at all, and the
kind of the cut (σ̄-change on RO_b / cycle appearance only). Usage: cutphi.py [--list FILE] | GAME [START]   (START=1 reads column 2)"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); EXP = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(EXP, "n5-box18"))
import nm  # noqa: E402
B = nm.B


def phi_w(g, R, t, v):
    """w restricted to R_c for vertex v at state t (c = cycle node of Ξ_t(v))."""
    order = sorted(range(g.n), key=lambda u: (g.prio[u], u)); c = R[t]["xi"][v][0]; rc = order.index(c)
    return {u: (k + 1 if g.prio[u] % 2 == 0 else -(k + 1)) for k, u in enumerate(order[rc + 1:])}


def check(g, st=None):
    e = B.Eng(g); R = B.trajectory(e, st or e.start()); C = dict(cuts=0, fail=0, carry_cuts=0, nopch_cuts=0, sb_cuts=0, cyc_only_cuts=0)
    first = []
    for i, j in B.phases(R):
        for s, f in B.runs_of(R, i, j):
            if f <= s:
                continue
            for a, b, RO in B.segments(e, R, s, f):
                if a <= s:
                    continue
                t = a - 1; C["cuts"] += 1; dphi = 0; carry = False; pch = 0
                sbch = any(R[t]["sb"][u] != R[b]["sb"][u] for u in RO)
                C["sb_cuts" if sbch else "cyc_only_cuts"] += 1
                for v in range(g.n):
                    A, Bs = R[t]["xi"][v][1], R[t + 1]["xi"][v][1]
                    if A == Bs:
                        continue
                    assert R[t]["xi"][v][0] == R[t + 1]["xi"][v][0]
                    w = phi_w(g, R, t, v); pch += 1
                    dphi += sum(w[r] for r in Bs) - sum(w[r] for r in A)
                    if not nm.matched(A, Bs, w):
                        carry = True
                if carry:
                    C["carry_cuts"] += 1
                if not pch:
                    C["nopch_cuts"] += 1
                if dphi < 1 and not carry:
                    C["fail"] += 1
                    if len(first) < 3:
                        first.append(dict(run=(s, f), cut=(t, a), seg=(a, b), dphi=dphi, pchanges=pch, kind="sigmabar" if sbch else "cycle"))
    return R, C, first


def main():
    a = sys.argv[1:]; items = []
    if a[0] == "--list":
        for line in open(a[1]):
            p = line.split()
            if p and not p[0].startswith("#"):
                items.append((os.path.join(EXP, p[0]), os.path.join(EXP, p[1]) if len(p) > 1 and os.environ.get("START") == "1" else None))
    else:
        items.append((a[0], a[1] if len(a) > 1 else None))
    for gp, sp in items:
        g = nm.load(gp); e = B.Eng(g); st = nm.startof(g, e, sp) if sp else None
        try:
            R, C, first = check(g, st)
        except Exception as ex:  # noqa: BLE001
            print("ERROR", gp, repr(ex)[:200], flush=True); continue
        print("CUTPHI", os.path.relpath(gp, EXP), "start" if sp else "S3", "n", g.n, "states", len(R), json.dumps(C), json.dumps(first), flush=True)


if __name__ == "__main__":
    main()
