#!/usr/bin/env python3
"""L-NEW box 50 (successor 31): FB-LIN first question (Lead 11:19Z): does an in-phase fallback force a path-set change, or a CARRY (L-LIT's
P-N5-MPGS (A): a P-change A -> B that is not MATCHED), at a specific vertex? For every in-phase transition t -> t+1 (fallback or S4a) and every
vertex v, Xi(v)'s change is classified: none / LEN (length only) / MAT (matched P-change) / CAR (carry). SW := the Even vertices switched at t.
MATCHED test: a matching of outs A-B to ins B-A with w(in) > w(out) (w = +pos for even ranks, -pos for odd, pos = index in R_c) covering
every even out and every odd in; by Mendelsohn-Dulmage it exists iff one matching covers the even outs and one covers the odd ins (each by
augmenting paths). CHECK=1 compares against L-LIT's brute force (T33) on every P-change with |A delta B| <= 7.
Usage: fbcarry.py --list FILE | --one GAME [START]"""
import sys, os, itertools
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
for p in ("root", "runlin"): sys.path.insert(0, os.path.join(ROOT, "experiments", "si", p))
from common import rows, load, readstart, phases
C = Counter(); TOP = []; CHECK = os.environ.get("CHECK") == "1"

def bits(m):
    out, r = [], 0
    while m:
        if m & 1: out.append(r)
        m >>= 1; r += 1
    return out

def cover(req, other, adj):
    """is there a matching covering every vertex of req (adj(x) = admissible partners in other)?"""
    match = {}
    def aug(x, seen):
        for y in adj(x):
            if y in seen: continue
            seen.add(y)
            if y not in match or aug(match[y], seen): match[y] = x; return True
        return False
    return all(aug(x, set()) for x in req)

def matched(A, B, par, pos):
    w = lambda r: pos[r] if par[r] == 0 else -pos[r]
    outs, ins = A - B, B - A
    ev_out = [o for o in outs if par[o] == 0]; od_in = [i for i in ins if par[i] == 1]
    return cover(ev_out, ins, lambda o: [i for i in ins if w(i) > w(o)]) and cover(od_in, outs, lambda i: [o for o in outs if w(i) > w(o)])

def brute(A, B, par, pos):
    w = lambda r: pos[r] if par[r] == 0 else -pos[r]
    outs, ins = sorted(A - B), sorted(B - A); mo = {o for o in outs if par[o] == 0}; mi = {i for i in ins if par[i] == 1}
    for k in range(min(len(outs), len(ins)) + 1):
        for so in itertools.combinations(outs, k):
            if not mo <= set(so): continue
            for si in itertools.permutations(ins, k):
                if mi <= set(si) and all(w(i) > w(o) for o, i in zip(so, si)): return True
    return False

def kind(E, a, b):
    if a == b: return "NONE"
    if a[0] != b[0]: return "CYC"                      # cannot happen inside a phase (lambda constant)
    if a[1] == b[1]: return "LEN"
    rc = E.rank[a[0]]; R_c = sorted(r for r in range(len(E.rank)) if r > rc); pos = {r: k + 1 for k, r in enumerate(R_c)}
    A, B = set(bits(a[1])), set(bits(b[1])); par = E.rankpar
    m = matched(A, B, par, pos)
    if CHECK and len(A ^ B) <= 7:
        C["check"] += 1
        if m != brute(A, B, par, pos): C["CHECK_MISMATCH"] += 1
    return "MAT" if m else "CAR"

def one(g, name, start=None):
    E, R = rows(g, start); n = g.n; ev = [v for v in range(n) if g.owner[v] == 0]
    for i, j in phases(R):
        nfb = 0; carriers = []
        for t in range(i, j):
            fb = bool(R[t]["fb"]); tag = "FB" if fb else "SA"; nfb += fb
            K = {v: kind(E, R[t]["vs"][v], R[t + 1]["vs"][v]) for v in range(n)}
            SW = [v for v in ev if R[t]["s"][v] != R[t + 1]["s"][v]]
            C[tag] += 1
            if "CYC" in K.values(): C[tag + "_CYC_V"] += 1
            anyP = any(k in ("MAT", "CAR") for k in K.values()); anyC = "CAR" in K.values()
            swP = any(K[v] in ("MAT", "CAR") for v in SW); swC = any(K[v] == "CAR" for v in SW)
            allswP = all(K[v] in ("MAT", "CAR") for v in SW)
            C[tag + "_anyP"] += anyP; C[tag + "_anyCAR"] += anyC; C[tag + "_swP"] += swP; C[tag + "_swCAR"] += swC; C[tag + "_allswP"] += allswP
            for v in SW: C[tag + "_sw_" + K[v]] += 1
            if fb: carriers.append({v for v in range(n) if K[v] == "CAR"})
            if fb and not anyP: TOP.append(("noP", name, i, j, t, SW, [K[v] for v in SW]))
            if fb and not anyC: TOP.append(("noCAR", name, i, j, t, SW, [K[v] for v in SW]))
        C["fb_per_phase_max"] = max(C["fb_per_phase_max"], nfb)
        if nfb >= 2:                                   # one vertex carrying at EVERY fallback of the phase?
            C["ph_f2"] += 1; cov = Counter(v for S in carriers for v in S); best = max(cov.values(), default=0)
            if best == nfb: C["ph_common_carrier"] += 1
            else: TOP.append(("nocommon", name, i, j, nfb, best))
            C["cover_min_x100"] = min(C.get("cover_min_x100", 100), 100 * best // nfb)

def main():
    a = sys.argv[1:]
    if a[0] == "--one": one(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        for line in open(a[1]):
            p = line.split() if line.strip() and not line.startswith("#") else None
            if p:
                X = lambda q: os.path.join(ROOT, "experiments", q)
                try: one(load(X(p[0])), p[0], readstart(X(p[1])) if len(p) > 1 and os.environ.get("START") == "1" else None)
                except Exception as ex: C["ERR"] += 1; print("ERR", p[0], repr(ex)[:80])
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for kd in ("noP", "noCAR", "nocommon"):
        xs = [x for x in TOP if x[0] == kd]
        print(kd, len(xs)); [print("  ", x) for x in xs[:8]]

if __name__ == "__main__":
    main()
