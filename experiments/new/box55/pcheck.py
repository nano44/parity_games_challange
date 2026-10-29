#!/usr/bin/env python3
"""L-NEW box 55 (successor 33): pinned check of packet docs/new/P-N5-SF-box55.md on one game (+ optional start).
Runs N5-SF (experiments/new/box54/n5sf.py, read-only) and checks, per side (Even on G, Odd on G^d):
  ORB_V   DECOUPLE: the distinct-sigma sequence of the run differs from the orbit sigma_0, F(sigma_0), ... of the one-sided map F
          (F(s) = the S4a' arena optimum against sbar(s) if != s, else the S4c switch; computed here without tau);
  TAU_V   DECOUPLE: a second run from the same sigma_0 and a different tau_0 gives a different distinct-sigma sequence;
  IMP_V   SF-RED identity: I_sigma on G differs from the improving set of sigma on G_sbar (Odd cut to sbar(sigma)), or Xi differs;
  RED_V   SF-RED: F(s) differs from N5's S4a/S4c step (experiments/new/box21/n5x.step) on G_sbar(s) with tau := sbar(s);
  MON_V   R15 (a): some Xi value goes down along the distinct-sigma sequence;
  SEG_V   SF-RED: a (sbar, lambda)-stretch has >= n + m transitions or > n - 1 value-changing ones;
  LAM_V   LAM > n(n - 1);  TOT_V  #values - 1 >= (n + m)(1 + LAM + SBC);  REP_V  a state repeats (SF-TERM).
MUT=1: F and the run use tau's CURRENT value in place of sbar (i.e. N5's opponent) for the orbit only; ORB must then FAIL on the pins.
Prints one ROW per side and CHECK PASS / CHECK FAIL. Usage: pcheck.py GAME [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box54")); sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
import n5sf, n5x, pg
from n5x import Engine, dual, load, readstart, start_pair
MUT = os.environ.get("MUT") == "1"

def arena_opt(g, s, opp, Is):
    """S4a' / N5 S4a: Even's optimum of H (Even v: {s(v)} + Is(v); Odd v: opp(v)), S1 procedure on the dual of H (as n5x.step)."""
    n = g.n; opt = {v: {s[v]} for v in range(n) if g.owner[v] == 0}
    for v, w in Is: opt[v].add(w)
    succ = [sorted(opt[v]) if g.owner[v] == 0 else [opp[v]] for v in range(n)]
    _, best = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ))).evaluate(tuple(opp[v] if g.owner[v] == 1 else -1 for v in range(n)))
    return [best[v] if g.owner[v] == 0 else s[v] for v in range(n)]

def F(g, E, s, tau=None):
    vs, sb = E.evaluate(tuple(s)); Is = E.improving(tuple(s), vs)
    if not Is: return None
    ns = arena_opt(g, s, tau if (MUT and tau is not None) else sb, Is)
    if ns == list(s):
        for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
    return ns

def distinct(seq, g=None, who=0):
    """consecutive-distinct sequence of a player's strategies, projected to that player's vertices (a start file may set an
    entry of the other player's vertex, e.g. red/n3/instances/n3cov_lean.start SIGMA0 47:18 with 47 Odd; S1 ignores it)."""
    out = []
    for x in seq:
        if g is not None: x = [x[v] if g.owner[v] == who else -1 for v in range(g.n)]
        if not out or out[-1] != x: out.append(x)
    return out

def side(g, E, seq, seq2, taus, C, lab):
    n, m = g.n, sum(len(set(g.succ[v])) for v in range(g.n))
    orb = [list(seq[0])]
    while True:
        k = len(orb) - 1
        nx = F(g, E, orb[-1], taus[k] if k < len(taus) else None)
        if nx is None or len(orb) > len(seq) + 2: break
        orb.append(nx)
    if orb != seq: C[lab + "ORB_V"] = 1
    if seq2 != seq: C[lab + "TAU_V"] = 1
    VS = [E.evaluate(tuple(s)) for s in seq]
    sbc = lam = 0; seg_t = seg_vc = 0; segs = 1; mx = 0
    for i, s in enumerate(seq):
        vs, sb = VS[i]; Is = sorted(E.improving(tuple(s), vs))
        gi = pg.Game(list(g.prio), list(g.owner), [list(g.succ[v]) if g.owner[v] == 0 else [sb[v]] for v in range(n)])
        Ei, Edi = Engine(gi), Engine(dual(gi)); vi, _ = Ei.evaluate(tuple(s))
        if sorted(Ei.improving(tuple(s), vi)) != Is or list(vi) != list(vs): C[lab + "IMP_V"] = 1
        if i + 1 < len(seq):
            t = [sb[v] if g.owner[v] == 1 else -1 for v in range(n)]
            r = n5x.step(gi, Ei, Edi, list(s), t)
            if r is None or list(r[0]) != list(seq[i + 1]): C[lab + "RED_V"] = 1
            vn, sbn = VS[i + 1]
            if any(E.key(vn[v]) < E.key(vs[v]) for v in range(n)): C[lab + "MON_V"] = 1
            lamc = tuple(x[0] for x in vn) != tuple(x[0] for x in vs); sbcc = list(sbn) != list(sb)
            lam += lamc; sbc += sbcc
            if lamc or sbcc:
                segs += 1; seg_t = seg_vc = 0
            else:
                seg_t += 1; seg_vc += list(vn) != list(vs); mx = max(mx, seg_t)
                if seg_t >= n + m or seg_vc > n - 1: C[lab + "SEG_V"] = 1
    if lam > n * (n - 1): C[lab + "LAM_V"] = 1
    if len(seq) - 1 >= (n + m) * (1 + lam + sbc): C[lab + "TOT_V"] = 1
    print("ROW", lab, "n", n, "m", m, "values", len(seq), "orbit", len(orb), "SBC", sbc, "LAM", lam, "SEG", segs, "SEGMAX", mx)

def main():
    g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 else None
    E, T = n5sf.trace(g, st); C = {}
    if T[-1].get("cycle"): C["REP_V"] = 1
    T = [x for x in T if "lam" in x]
    E0, Ed0 = Engine(g), Engine(dual(g)); s0, t0 = start_pair(g, E0, Ed0, st)
    # second run: same sigma_0, a different tau_0 (each Odd vertex takes its LAST successor), and the mirror
    t1 = [g.succ[v][-1] if g.owner[v] == 1 else -1 for v in range(g.n)]
    s1 = [g.succ[v][-1] if g.owner[v] == 0 else -1 for v in range(g.n)]
    def fromdict(s, t): return ({v: s[v] for v in range(g.n) if g.owner[v] == 0}, {v: t[v] for v in range(g.n) if g.owner[v] == 1})
    _, Ta = n5sf.trace(g, fromdict(s0, t1)); _, Tb = n5sf.trace(g, fromdict(s1, t0))
    Ta = [x for x in Ta if "lam" in x]; Tb = [x for x in Tb if "lam" in x]
    side(g, E, distinct([x["s"] for x in T], g, 0), distinct([x["s"] for x in Ta], g, 0), [x["t"] for x in T], C, "E_")
    gd = dual(g); Ed = Engine(gd)
    side(gd, Ed, distinct([x["t"] for x in T], g, 1), distinct([x["t"] for x in Tb], g, 1), [x["s"] for x in T], C, "O_")
    print("iterations", len(T) - 1, "fallbacks", sum(x.get("fb", 0) for x in T))
    print(" ".join(sorted(C)) if C else "violations none")
    print("CHECK PASS" if not C else "CHECK FAIL")
    sys.exit(0 if not C else 1)

if __name__ == "__main__":
    main()
