#!/usr/bin/env python3
r"""REFEREE-2 successor 13 (Opus 5.5, D15): mechanical check of packet P-N5-DUAL (docs/new/P-N5-DUAL-box43.md sha1 a51f7c30 @ df073cb5).
Own N5 loop written from SPEC S1-S5 + FIX 1-4 on L-SI's engine experiments/si/si.py (SPEC's own S1 implementation, read-only), with a
flag for the Odd-first fallback N5^OF (packet §0). Dual game: owners swapped, priorities + 1 (= n5.py's dual; SPEC S1 "Odd's side").
The lane's mirror.py / dblfb.py / dualsym.py are NOT run or imported.
Checks:
  DUAL1   N5 on G from (s, t) = mirror of N5^OF on G^d from (t, s), statewise, same length.
  DUAL2   plain N5 on G^d from (t, s) equals the mirror on states 0..j, j := source of G's first two-sided fallback (all states if none);
          record whether it differs at j + 1.
  ENDG    I_sigma = {} at k => sigma constant after k; I_tau = {} at k => tau constant after k.
  PHIK    distinct tau along a run <= prod deg(o_i) and no tau repeats; phases ((lambda, tau)) <= n(n-1) + prod; mirror: distinct sigma
          <= prod over Even choice vertices, no sigma repeats, dual phases ((lambda^U, sigma)) <= n(n-1) + prod.
  MIRA    on C^1E: sigma changes <= d_e - 1, dual phases <= n(n-1) + d_e.
  MIRC    on C^1O, from a random state x: the first phase of N5^OF from x is a prefix of the first phase of N5 from x (same states).
Mutations DU_MUT: plain (DUAL1 with plain N5 on G^d instead of N5^OF), phi (PHIK with prod - 1), endg (ENDG asks sigma to CHANGE).
Usage: dual_check.py random N nmin nmax seed kind (kind: kO | 1E | 1O) | files list.txt [runs]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
for p in ("experiments/si", "experiments/harness"): sys.path.insert(0, os.path.join(ROOT, p))
import pg
from si import Engine
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-1O"))
from onecheck import Stats
MUT = os.environ.get("DU_MUT", "")

def dual(h): return pg.Game([p + 1 for p in h.prio], [1 - o for o in h.owner], [list(s) for s in h.succ])

class Runner:
    def __init__(s, g):
        s.g = g; s.n = g.n; s.E = Engine(g); s.Ed = Engine(dual(g))
    def info(s, sg, tu):
        g, n = s.g, s.n
        vs, _ = s.E.evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
        Is = s.E.improving(tuple(sg), vs)
        vt, _ = s.Ed.evaluate(tuple(tu[v] if g.owner[v] == 1 else -1 for v in range(n)))
        It = s.Ed.improving(tuple(tu), vt)
        return vs, Is, vt, It
    def run(s, sg, tu, odd_first=False, cap=100000):
        g, n = s.g, s.n
        sg, tu = list(sg), list(tu)
        states, fbs = [(tuple(sg), tuple(tu))], []
        while len(fbs) < cap:
            vs, Is, vt, It = s.info(sg, tu)
            if not Is and not It: break
            ns, nt = list(sg), list(tu)
            if Is:   # S4a: Odd's optimal counterstrategy in the dual of H to the dual-Even strategy tau
                opt = {v: {sg[v]} for v in range(n) if g.owner[v] == 0}
                for v, w in Is: opt[v].add(w)
                succ = [sorted(opt[v]) if g.owner[v] == 0 else [tu[v]] for v in range(n)]
                _, best = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ))).evaluate(
                    tuple(tu[v] if g.owner[v] == 1 else -1 for v in range(n)))
                for v in range(n):
                    if g.owner[v] == 0: ns[v] = best[v]
            if It:   # S4b: Odd's optimal counterstrategy on H' to sigma
                opt = {v: {tu[v]} for v in range(n) if g.owner[v] == 1}
                for v, w in It: opt[v].add(w)
                succ = [sorted(opt[v]) if g.owner[v] == 1 else [sg[v]] for v in range(n)]
                _, best = Engine(pg.Game(list(g.prio), list(g.owner), succ)).evaluate(
                    tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
                for v in range(n):
                    if g.owner[v] == 1: nt[v] = best[v]
            fb = 0
            if ns == sg and nt == tu:   # S4c (N5: Even first; N5^OF: Odd first)
                fb = 1 if not (Is and It) else 2
                even_side = bool(Is) and not (odd_first and It)
                if even_side:
                    for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (s.E.key(vs[w]), w))
                else:
                    for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (s.Ed.key(vt[w]), w))
            sg, tu = ns, nt
            states.append((tuple(sg), tuple(tu))); fbs.append(fb)
        return states, fbs

def restrict(g, st):
    sg, tu = st
    return (tuple(sg[v] for v in range(g.n) if g.owner[v] == 0), tuple(tu[v] for v in range(g.n) if g.owner[v] == 1))

def mirror_eq(g, a, b):
    """a: state of G, b: state of G^d; mirror iff b's Even strategy = a's tau and b's Odd strategy = a's sigma"""
    sa, ta = restrict(g, a); gd = dual(g)
    sb, tb = restrict(gd, b)
    return sb == ta and tb == sa

def lam(engine, strat, owner_mask):
    vs, _ = engine.evaluate(tuple(strat[v] if owner_mask[v] else -1 for v in range(len(strat))))
    return tuple(vs[v][0] for v in range(len(strat)))

def prod(xs):
    p = 1
    for x in xs: p *= x
    return p

def check(g, s, t, st, name, rng):
    n = g.n; gd = dual(g)
    RG, RD = Runner(g), Runner(gd)
    A, fa = RG.run(s, t)
    B, fb_ = RD.run(t, s, odd_first=(MUT != "plain"))
    st.inc("runs"); st.inc("iterations", len(fa))
    if len(A) != len(B) or any(not mirror_eq(g, A[k], B[k]) for k in range(len(A))):
        st.bad("DUAL1", f"{name}: N5 on G is not the mirror of N5^OF on G^d (lengths {len(A)}, {len(B)})")
    else: st.inc("DUAL1_ok")
    C, _ = RD.run(t, s)
    j = next((k for k, f in enumerate(fa) if f == 2), None)
    if j is not None: st.inc("runs_with_two_sided_fb"); st.inc("two_sided_fbs", sum(1 for f in fa if f == 2))
    upto = len(A) if j is None else j + 1
    if len(C) < upto or any(not mirror_eq(g, A[k], C[k]) for k in range(upto)): st.bad("DUAL2", f"{name}: plain mirror differs before j+1")
    elif j is None:
        if len(C) != len(A) or any(not mirror_eq(g, A[k], C[k]) for k in range(len(A))): st.bad("DUAL2", f"{name}: no two-sided fb but differs")
    else:
        if j + 1 < len(C) and j + 1 < len(A) and not mirror_eq(g, A[j + 1], C[j + 1]): st.inc("REC_plain_differs_at_j+1")
        else: st.inc("REC_plain_same_at_j+1")
    # ENDG
    for k in range(len(A)):
        _, Is, _, It = RG.info(list(A[k][0]), list(A[k][1]))
        if not Is:
            same = all(restrict(g, A[q])[0] == restrict(g, A[k])[0] for q in range(k, len(A)))
            if same == (MUT == "endg") and (MUT != "endg" or k < len(A) - 1): st.bad("ENDG", f"{name}: sigma changes after I_sigma empty at {k}")
        if not It:
            if any(restrict(g, A[q])[1] != restrict(g, A[k])[1] for q in range(k, len(A))): st.bad("ENDG", f"{name}: tau changes after I_tau empty at {k}")
    # PHIK, MIRA
    oc = [v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) > 1]
    ec = [v for v in range(n) if g.owner[v] == 0 and len(g.succ[v]) > 1]
    taus = [restrict(g, x)[1] for x in A]; sigs = [restrict(g, x)[0] for x in A]
    def changes_and_repeat(seq):
        seen, ch, rep = {seq[0]}, 0, False
        for a_, b_ in zip(seq, seq[1:]):
            if a_ != b_:
                ch += 1
                if b_ in seen: rep = True
                seen.add(b_)
        return len(seen), ch, rep
    dt, ct, rt = changes_and_repeat(taus); ds, cs, rs = changes_and_repeat(sigs)
    po, pe = prod(len(g.succ[v]) for v in oc), prod(len(g.succ[v]) for v in ec)
    if MUT == "phi": po -= 1
    if rt or dt > po: st.bad("PHIK", f"{name}: tau repeat {rt} or distinct {dt} > {po}")
    if rs or ds > pe: st.bad("PHIK", f"{name}: sigma repeat {rs} or distinct {ds} > {pe}")
    lamX = [lam(RG.E, x[0], [o == 0 for o in g.owner]) for x in A]
    lamU = [lam(RG.Ed, x[1], [o == 1 for o in g.owner]) for x in A]
    ph = 1 + sum(1 for k in range(len(A) - 1) if (lamX[k], taus[k]) != (lamX[k + 1], taus[k + 1]))
    dph = 1 + sum(1 for k in range(len(A) - 1) if (lamU[k], sigs[k]) != (lamU[k + 1], sigs[k + 1]))
    if ph > n * (n - 1) + po: st.bad("PHIK", f"{name}: phases {ph} > n(n-1)+prod")
    if dph > n * (n - 1) + pe: st.bad("PHIK", f"{name}: dual phases {dph} > n(n-1)+prod_E")
    st.mxr("max_phases", (ph, name)); st.mxr("max_dual_phases", (dph, name)); st.mxr("max_distinct_tau", (dt, name))
    st.inc("k_" + str(len(oc)))
    if len(ec) == 1:
        st.inc("C1E_runs")
        de = len(g.succ[ec[0]])
        if cs > de - 1 or dph > n * (n - 1) + de: st.bad("MIRA", f"{name}: C1E sigma changes {cs} / dual phases {dph}")
        st.mxr("C1E_max_sigma_changes_over_bound", (cs / max(de - 1, 1), name))
    # MIRC on C^1O from a random state
    if len(oc) == 1:
        x = ([rng.choice(g.succ[v]) for v in range(n)], [rng.choice(g.succ[v]) for v in range(n)])
        P, _ = RG.run(*x); Q, _ = RG.run(*x, odd_first=True)
        def first_phase(S):
            k0 = (lam(RG.E, S[0][0], [o == 0 for o in g.owner]), restrict(g, S[0])[1]); m = 1
            while m < len(S) and (lam(RG.E, S[m][0], [o == 0 for o in g.owner]), restrict(g, S[m])[1]) == k0: m += 1
            return [restrict(g, y) for y in S[:m]]
        fP, fQ = first_phase(P), first_phase(Q)
        if len(fQ) > len(fP) or fQ != fP[:len(fQ)]: st.bad("MIRC", f"{name}: N5^OF first phase not a prefix of N5's")
        else: st.inc("MIRC_ok")
        if len(fQ) < len(fP): st.inc("MIRC_strict_prefix")

def rand_game(rng, n, kind):
    while True:
        if kind == "1E":
            owner = [1] * n; e = rng.randrange(n); owner[e] = 0
            for v in range(n):
                if v != e and rng.random() < 0.35: owner[v] = 0
        else:
            owner = [rng.randrange(2) for _ in range(n)]
        prio = [rng.randrange(0, n + 1) for _ in range(n)]
        succ = []
        for v in range(n):
            k = rng.randint(1, min(3, n))
            succ.append(sorted(set(rng.sample(range(n), k))))
        if kind == "1E":
            for v in range(n):
                if owner[v] == 0 and v != e: succ[v] = succ[v][:1]
            if len(succ[e]) < 2: continue
        if kind == "1O":
            odd = [v for v in range(n) if owner[v] == 1]
            if not odd: continue
            o = rng.choice(odd)
            for v in odd:
                if v != o: succ[v] = succ[v][:1]
            if len(succ[o]) < 2: continue
        return pg.Game(prio, owner, succ)

def main():
    st = Stats(); a = sys.argv[1:]; rng = random.Random(4343)
    if a[0] == "random":
        N, nmin, nmax, seed, kind = int(a[1]), int(a[2]), int(a[3]), int(a[4]), a[5]; rng = random.Random(seed)
        for i in range(N):
            g = rand_game(rng, rng.randint(nmin, nmax), kind)
            s = [rng.choice(g.succ[v]) for v in range(g.n)]; t = [rng.choice(g.succ[v]) for v in range(g.n)]
            check(g, s, t, st, f"{kind}{seed}:{i}", rng)
    else:
        runs = int(a[2]) if len(a) > 2 else 2
        for path in [l.strip() for l in open(a[1]) if l.strip()]:
            g = pg.read(os.path.join(ROOT, path)) if hasattr(pg, "read") else None
            if g is None: raise SystemExit("pg.read missing")
            for r in range(runs):
                if r == 0:
                    E, Ed = Engine(g), Engine(dual(g)); s, t = list(E.initial("best")), list(Ed.initial("best"))
                else:
                    s = [rng.choice(g.succ[v]) for v in range(g.n)]; t = [rng.choice(g.succ[v]) for v in range(g.n)]
                check(g, s, t, st, f"{path}#{r}", rng)
    print("MODE", " ".join(a), "MUT", MUT or "-")
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for v in st.viol: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c.get("VIOLATIONS") else "OK", f"violations={st.c.get('VIOLATIONS', 0)}")

if __name__ == "__main__":
    main()
