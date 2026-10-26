#!/usr/bin/env python3
"""Box 48 DATA (N5-KPOLY §2): offset resets along routing chains (the odometer of RESULTS R61 FB-kT). Per phase, class c, Odd choice q in
U_c with lambda(q) != q: par_t(q) := the first vertex of Q - {q} on q's honest play at t before c (None = q DIRECT); offset s_t(q) := M_t(q) -
M_t(par_t(q)) (M = path weight of Xi, as L-SI common.M). At an in-phase transition t -> t+1 with par_t(q) = par_{t+1}(q) = p != None:
RESET if s_{t+1}(q) < s_t(q), RISE if >. Also PARCHG (par changes), and for each q the longest run of resets with p fixed.
A RESET with M(q) unchanged or rising means p rose by more than q: the odometer move. Counts per phase: max resets of one q.
ENTRY: see entry(); RESET_NOT_ENTRY_V and CHAIN_V must be 0 (CHAIN_V: an M(q) change with no event on q's chain).\nUsage: reset.py STARTS SEED (--list FILE | files) [--nmax N] [--start F]   (imports experiments/si/root/common.py read-only)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "root"))
from common import rows, phases, M, load, readstart
C = {}; TOP = []
MUT = os.environ.get("MUT", "0")   # controls: 1 = chain check ignores parent changes (CHAIN_V must bite); 2 = ENTRY tested against a wrong
                                    # parent (another Odd choice vertex of the class, if any; ENTRY must bite)
def inc(k, v=1): C[k] = C.get(k, 0) + v
def mx(k, v): C[k] = max(C.get(k, v), v)
def par(A, q, Q):
    nx, vs = A["nxt"], A["vs"]; c = vs[q][0]; x, seen = nx[q], {q}
    while x not in seen:
        if x == c: return None
        if x in Q: return x
        seen.add(x); x = nx[x]
    return None
def via(A, z, p, avoid=None):
    """z's honest play at state A meets p before its cycle node (and avoids `avoid`)."""
    nx, c = A["nxt"], A["vs"][z][0]; x, seen = z, set()
    while x not in seen:
        if x == avoid: return False
        if x == p: return True
        if x == c: return False
        seen.add(x); x = nx[x]
    return False
def entry(A, B, q, p):
    """ENTRY at t -> t+1 for (q, p): q's (t+1)-segment (successor of q up to p, exclusive) has a vertex whose t-play misses p, or
    sigma-bar_{t+1}(q)'s t-play meets q."""
    y2 = B["nxt"][q]
    if not via(A, y2, p, avoid=q) and y2 != p: return True
    x = y2
    while x != p:
        if not via(A, x, p): return True
        x = B["nxt"][x]
    return False
def run(g, start, nm):
    E, R = rows(g, start)
    Q = {v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2}
    for i, j in phases(R):
        inc("phases"); per = {}
        for t in range(i, j):
            A, B = R[t], R[t + 1]
            for q in Q:
                if A["vs"][q][0] == q or B["vs"][q][0] == q: continue
                pa, pb = par(A, q, Q), par(B, q, Q)
                if pa != pb: inc("PARCHG"); continue
                if pa is None: continue
                inc("checks"); sa = M(E, A["vs"][q]) - M(E, A["vs"][pa]); sb = M(E, B["vs"][q]) - M(E, B["vs"][pa])
                if MUT == "2":
                    alt = [x for x in Q if x not in (q, pa) and A["vs"][x][0] == A["vs"][q][0]]
                    en = entry(A, B, q, alt[0]) if alt else entry(A, B, q, pa)
                else: en = entry(A, B, q, pa)
                if en: inc("ENTRY")
                if sb < sa:
                    inc("RESET"); per[q] = per.get(q, 0) + 1
                    if not en: inc("RESET_NOT_ENTRY_V")
                    if M(E, B["vs"][pa]) > M(E, A["vs"][pa]): inc("RESET_par_rose")
                elif sb > sa: inc("RISE")
        for t in range(i, j):
            A, B = R[t], R[t + 1]
            for q in Q:
                if A["vs"][q][0] == q or B["vs"][q][0] == q or M(E, A["vs"][q]) == M(E, B["vs"][q]): continue
                inc("MQ_changes"); x, ok, seen = q, False, set()
                while x is not None and x not in seen:
                    seen.add(x); pa, pb = par(A, x, Q), par(B, x, Q)
                    if pa != pb:
                        if MUT == "1": break
                        ok = True; break
                    if pa is None:
                        ok = M(E, A["vs"][x]) != M(E, B["vs"][x]); break
                    if (M(E, B["vs"][x]) - M(E, B["vs"][pa])) != (M(E, A["vs"][x]) - M(E, A["vs"][pa])) or entry(A, B, x, pa): ok = True; break
                    x = pa
                if not ok: inc("CHAIN_V")
        if per:
            m = max(per.values()); mx("max_resets_one_q_phase", m); inc("phases_with_reset")
            TOP.append((m, len(per), j - i, g.n, nm))
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
    print(" ".join(f"{k} {v}" for k, v in sorted(C.items())))
    for w in sorted(TOP, reverse=True)[:10]: print("  top (max resets of one q, q's with resets, len, n, name):", *w)
