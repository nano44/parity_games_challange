#!/usr/bin/env python3
"""Box 49 DATA (P-N5-OFFMONO-add-box49): Remark Z-CONST, Corollary CHAIN-COUNT', Lemma ZCH-COUNT, per phase P and class c (U := lambda^-1(c)).
Z_t(c) := c's honest cycle at t as a sequence from c; ZCH := in-phase transitions with Z_t(c) != Z_{t+1}(c); N := vertices v != c of Z_{t+1}(c)
with next_{t+1}(v) != next_t(v). Each ZCH transition is classed STRICT (some v in N with kappa_{t+1}(v) > kappa_t(v)), else TIE (N nonempty),
else CEVEN (N empty, c Even), else ODDC (N empty, c in Q); OTHER must be 0 (a TIE with an Even or kappa-changed vertex in N; or N empty
and c not able to move). Checks (each must be 0):
  ZC_V      Z unchanged but kappa or par changes at a vertex on it (Remark Z-CONST);
  PSI_V     c Even and psi := kappa(next(c)) falls at an in-phase transition (Lemma ZCH-COUNT's c-Even case);
  CEVEN_V   more than n - 1 CEVEN changes in a phase and class;
  STRICT_V  some v takes more than n - 1 STRICT charges in a phase (charge = the first strict v of N);
  ZB_V      ZCH > (n-1)|U| + TIE + ODDC (Lemma ZCH-COUNT, the (n - 1) form);
  ZC := ZCH n CYC, CYC := transitions at which some x in Q n U - {c} lies on Z_t(c) (P-N5-OFFMONO's CYC_c);
  PM_V      off(x; p) falls at a transition inside an x-piece (pieces cut at EXIT_x u ZC);
  CC_V      #kappa(q)-changes > |ZC| + sum_x (|EXIT_x| + sum over x-pieces of (values - 1))  (the count CHAIN-COUNT''s proof gives);
  CCD_V     #kappa(q)-changes > |ZC| + sum_x D (|EXIT_x| + |ZC| + 1), D := max values of off(x; p) on any x-piece (CHAIN-COUNT' as stated).
Controls: MUT=1 x-pieces not cut at ZC (ZC := the empty set); MUT=2 the OPPOSITE length
sign -s_c (must bite: PSI_V / PM_V); MUT=3 x-pieces not cut at EXIT_x (must bite: PM_V, offsets to a changed parent). Usage: zch.py STARTS SEED (--list FILE | files) [--nmax N] [--start F]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "root"))
from common import rows, phases, load, readstart, M
C = {}
def inc(k, v=1): C[k] = C.get(k, 0) + v
def mx(k, v): C[k] = max(C.get(k, v), v)
MUT = os.environ.get("MUT", "0")
def cyc_seq(A, c):
    nx = A["nxt"]; out, x = [c], nx[c]
    while x != c and len(out) <= len(nx): out.append(x); x = nx[x]
    return tuple(out)
def par(A, x, Q, c):
    nx, y, seen = A["nxt"], A["nxt"][x], {x}
    while y != c and y not in seen:
        if y in Q: return y
        seen.add(y); y = nx[y]
    return c
def run(g, start, nm):
    E, R = rows(g, start); n = g.n
    Q = {v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) >= 2}
    for i, j in phases(R):
        inc("phases"); inc("trans", j - i)
        for c in {R[i]["vs"][v][0] for v in range(n)}:
            U = [v for v in range(n) if R[i]["vs"][v][0] == c]
            sc = 1 if E.par[c] == 1 else -1
            if MUT == "2": sc = -sc
            kap = lambda S, v: (M(E, S["vs"][v]), sc * S["vs"][v][2])
            X = [x for x in U if x in Q and x != c]
            zch = set(); cycset = set(); cls = {"STRICT": 0, "TIE": 0, "CEVEN": 0, "ODDC": 0}; charges = {}
            for k in range(i, j):
                A, B = R[k], R[k + 1]
                za, zb = cyc_seq(A, c), cyc_seq(B, c)
                if any(x in za for x in X): cycset.add(k)
                if g.owner[c] == 0:
                    if kap(B, B["nxt"][c]) < kap(A, A["nxt"][c]): inc("PSI_V")
                if za == zb:
                    for v in za:
                        if kap(A, v) != kap(B, v) or (v in Q and v != c and par(A, v, Q, c) != par(B, v, Q, c)): inc("ZC_V")
                    continue
                zch.add(k); N = [v for v in zb if v != c and A["nxt"][v] != B["nxt"][v]]
                st = [v for v in N if kap(B, v) > kap(A, v)]
                if st: cls["STRICT"] += 1; charges[st[0]] = charges.get(st[0], 0) + 1
                elif N:
                    if all(g.owner[v] == 1 and kap(B, v) == kap(A, v) for v in N): cls["TIE"] += 1
                    else: inc("OTHER")
                elif g.owner[c] == 0: cls["CEVEN"] += 1
                elif c in Q: cls["ODDC"] += 1
                else: inc("OTHER")
            for kk, vv in cls.items(): inc("ZCH_" + kk, vv)
            inc("ZCH", len(zch)); mx("max_ZCH", len(zch)); mx("max_TIE", cls["TIE"]); mx("max_ODDC", cls["ODDC"])
            if charges and max(charges.values()) > n - 1: inc("STRICT_V")
            if len(zch) > (n - 1) * len(U) + cls["TIE"] + cls["ODDC"]: inc("ZB_V")
            if cls["CEVEN"] > n - 1: inc("CEVEN_V")
            cut = set() if MUT == "1" else (zch & cycset); inc("ZC", len(cut)); inc("CYC", len(cycset))
            tot, Dmax, ex = 0, 1, {}
            for x in X:
                pr = [par(R[k], x, Q, c) for k in range(i, j + 1)]
                exits = {k for k in range(i, j) if pr[k - i] != pr[k + 1 - i]}; ex[x] = len(exits)
                pieces, cur = [], [i]
                for k in range(i, j):
                    if (k in exits and MUT != "3") or k in cut: pieces.append(cur); cur = [k + 1]
                    else: cur.append(k + 1)
                pieces.append(cur); s = len(exits)
                for pc in pieces:
                    p = pr[pc[0] - i] if MUT != "3" else None
                    offs = [tuple(a - b for a, b in zip(kap(R[k], x), kap(R[k], p if p is not None else pr[k - i]))) for k in pc]
                    for a, b in zip(offs, offs[1:]):
                        if b < a: inc("PM_V")
                    vals = len(set(offs)); s += vals - 1; Dmax = max(Dmax, vals)
                tot += s
            for q in X:
                ch = sum(1 for k in range(i, j) if kap(R[k], q) != kap(R[k + 1], q))
                inc("kchanges", ch)
                if ch > len(cut) + tot: inc("CC_V")
                if ch > len(cut) + sum(Dmax * (ex[x] + len(cut) + 1) for x in X): inc("CCD_V")
                mx("max_kchanges", ch)
if __name__ == "__main__":
    a = sys.argv[1:]; nmax = 10 ** 9; fixed = None
    if "--nmax" in a: i = a.index("--nmax"); nmax = int(a[i + 1]); del a[i:i + 2]
    if "--start" in a: i = a.index("--start"); fixed = readstart(a[i + 1]); del a[i:i + 2]
    K = int(a[0]); RNG = random.Random(int(a[1])); a = a[2:]
    if a[0] == "--list":
        gs = [(l.split()[0], load(os.path.join(ROOT, l.split()[0]))) for l in open(a[1]) if l.strip() and not l.startswith("#")]
    else: gs = [(f, load(f)) for f in a]
    for nm, g in gs:
        if g.n > nmax: continue
        sts = [fixed] if fixed else [None] + [({v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                                {v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) for _ in range(K)]
        for st in sts:
            try: run(g, st, nm)
            except RecursionError: inc("RECERR")
    for k in ("ZC_V", "PSI_V", "CEVEN_V", "STRICT_V", "ZB_V", "PM_V", "CC_V", "CCD_V", "OTHER"): C.setdefault(k, 0)
    print(" ".join(f"{k} {v}" for k, v in sorted(C.items())))
