#!/usr/bin/env python3
"""L-COMP box 18 (a): MATCHED P-changes and carries (L-LIT T32 §E6, Lemma MATCH-Φ; docs/lit/T32-n5-frontier-crossfield.md @ l-lit a06dc24a).
For a vertex v and a phase P (key (λ_Ξ, τ), RESULTS R38 (a); or --key r104: (τ, λ_Ξ, λ of the dual Ξτ) as L-RED's gatep.py), P_t := the
path set of Ξ_t(v) (n5b valuation: the vertices before the cycle node with rank above it). A P-change A := P_t → B := P_{t+1} (t, t+1 ∈ P)
is MATCHED iff there is a matching M of some outgoing ranks (A ∖ B) to some incoming ranks (B ∖ A), each pair with w(i) > w(o), every
unmatched incoming rank even and every unmatched outgoing rank odd (w(r) = +pos(r) if Ω even, −pos(r) if odd; pos = order of the rank);
otherwise a CARRY. NM_P(v) = carries of v in P; PCH_P(v) = P-changes. Also the same restricted to P-changes with an unchanged top
(max rank of A = max rank of B, both nonempty; "fixed top"), and RESETs (L-RED R104: a fixed-top change that removes an element).
The matching is decided by augmenting paths (Kuhn) on the bipartite graph {(o, i) : w(i) > w(o)} with the constraint that the matching
covers every even o and every odd i (checked as: a maximum matching restricted to the forced vertices, see matched()).
Usage: nm.py [--key r38|r104] [--list FILE (paths rel. to experiments/, optional .start)] | GAME [START]"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__)); EXP = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(EXP, "n5-box17"))
import box17 as B  # noqa: E402
import pg  # noqa: E402


def matched(A, Bs, w):
    """True iff A -> Bs is MATCHED. w: rank -> signed position. Forced: even outs, odd ins. A matching covering all forced vertices of
    both sides exists iff (Mendelsohn-Dulmage) one covering the forced outs and one covering the forced ins exist; but here an edge never
    joins an even out to an odd in (w(even out) > 0 > w(odd in)), so we test directly: search a matching covering all forced vertices by
    augmenting from each forced vertex, allowing free vertices to be used, by brute-force-free Kuhn on the union."""
    outs = sorted(A - Bs); ins = sorted(Bs - A)
    adj = {o: [i for i in ins if w[i] > w[o]] for o in outs}
    fo = [o for o in outs if w[o] > 0]; fi = [i for i in ins if w[i] < 0]
    # forced outs need even ins above them (only even ins i have w(i) > w(o) > 0); forced ins need odd outs below them in w
    # (w(o) < w(i) < 0). The two sub-problems use disjoint vertex sets (even outs / even ins vs odd outs / odd ins), so solve each.
    def cover(left, right_of):
        mt = {}
        def aug(x, seen):
            for y in right_of(x):
                if y not in seen:
                    seen.add(y)
                    if y not in mt or aug(mt[y], seen):
                        mt[y] = x; return True
            return False
        return all(aug(x, set()) for x in left)
    ev_in = [i for i in ins if w[i] > 0]; od_out = [o for o in outs if w[o] < 0]
    ok1 = cover(fo, lambda o: [i for i in ev_in if w[i] > w[o]])
    ok2 = cover(fi, lambda i: [o for o in od_out if w[i] > w[o]])
    return ok1 and ok2


def wmap(g):
    order = sorted(range(g.n), key=lambda v: (g.prio[v], v)); w = {}
    for k, v in enumerate(order):
        w[v] = (k + 1) if g.prio[v] % 2 == 0 else -(k + 1)
    return w


def measure(g, st=None, key="r38"):
    e = B.Eng(g); R = B.trajectory(e, st or e.start()); w = wmap(g); rk = {v: abs(w[v]) for v in w}
    if key == "r104":
        for r in R:
            vt = e.N.SD.evaluate(list(r["t"])); r["key"] = (r["t"], r["key"][0], tuple(x[0] for x in vt))
    gates = {v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2}
    rows = []
    for i, j in B.phases(R):
        for v in range(g.n):
            c = dict(pch=0, nm=0, ft=0, ftnm=0, reset=0, resetnm=0, reset_stall=0, stallnm=0)
            for t in range(i, j):
                A, Bs = R[t]["xi"][v][1], R[t + 1]["xi"][v][1]
                if A == Bs:
                    continue
                m = matched(A, Bs, w); c["pch"] += 1; c["nm"] += not m
                if A and Bs and max(A, key=rk.get) == max(Bs, key=rk.get):
                    c["ft"] += 1; c["ftnm"] += not m
                    if A - Bs:
                        c["reset"] += 1; c["resetnm"] += not m
                        if t + 1 < j and R[t + 1]["fb"]:
                            c["reset_stall"] += 1; c["stallnm"] += not m
            if c["pch"]:
                rows.append(dict(phase=(i, j), v=v, gate=v in gates, **c))
    return R, rows


def summary(g, rows):
    out = {}
    for k in ("pch", "nm", "ft", "ftnm", "reset", "resetnm"):
        out[k + "_max"] = max([r[k] for r in rows], default=0)
    out["nm_over_n_max"] = round(out["nm_max"] / g.n, 3)
    gr = [r for r in rows if r["gate"]]; out["gate_nm_max"] = max([r["nm"] for r in gr], default=0)
    out["gate_ftnm_max"] = max([r["ftnm"] for r in gr], default=0)
    return out


def load(path):
    return pg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%")))


def startof(g, e, path):
    s, t = map(list, e.start())
    for line in open(path):
        p = line.split()
        if p and p[0] in ("SIGMA0", "TAU0"):
            tgt = s if p[0] == "SIGMA0" else t
            for x in p[1:]:
                a, b = map(int, x.split(":")); tgt[a] = b
    return tuple(s), tuple(t)


def main():
    a = sys.argv[1:]; key = "r38"
    if "--key" in a:
        k = a.index("--key"); key = a[k + 1]; del a[k:k + 2]
    items = []
    if a[0] == "--list":
        for line in open(a[1]):
            p = line.split()
            if p and not p[0].startswith("#"):
                items.append((os.path.join(EXP, p[0]), os.path.join(EXP, p[1]) if len(p) > 1 and os.environ.get("START") == "1" else None))
    else:
        items.append((a[0], a[1] if len(a) > 1 else None))
    for gp, sp in items:
        g = load(gp); e = B.Eng(g); st = startof(g, e, sp) if sp else None
        try:
            R, rows = measure(g, st, key)
        except Exception as ex:  # noqa: BLE001
            print("ERROR", gp, repr(ex)[:200], flush=True); continue
        print("NM", os.path.relpath(gp, EXP), "start" if sp else "S3", "n", g.n, "states", len(R), json.dumps(summary(g, rows)), flush=True)


if __name__ == "__main__":
    main()
