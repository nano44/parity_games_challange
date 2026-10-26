#!/usr/bin/env python3
r"""REFEREE-2 successor 13 (Opus 5.5, D15): mechanical check of packet P-N5-FX (docs/si/P-N5-FX-box14.md sha1 aa227b0b).
State sequence: SPEC N5 via R2-N5-RE/re_check.n5_spec (S3 start + random start pairs). R, c_w from own play values (re_check.Game);
lambda_Xi from SPEC's S1 (si.py, read-only), as in R2-N5-1O/onecheck.py.
Per phase ((lambda_Xi, tau) constant), per in-phase transition k -> k+1 (S4a or Even S4c fallback):
  KIND    every crossing (R_{k+1} != R_k, R := vertices != o whose (sigma, tau)-play reaches o) is (i) a fallback, (ii) S4a with
          c_w(k) = c_theta, or (iii) S4a with c_w(k) != c_theta; (iii) has R_k strictly inside R_{k+1} (R-STICK).
  FXA     X <= n (f + X_SN) + n - 1 (Corollary FX (a)); X_SN := kind-(ii) crossings.
  FXB     X <= n (F* + 13(d_o+1)n^3(F*+1+T) + T) + n - 1, F* := 1 + (n-2)(2n-1), T := n^2 + 2n - 1; and f <= F* (via R48 (i)).
  Records: R30 (c)'s bound X <= (f+1)(n-1) + f + X_SN (checked too: it is landed and stronger); max X, max X / FX(a) bound.
Mutations FX_MUT: seg (n - 2 crossings per segment), noiii (FX(a) without the segment term: X <= f + X_SN), stick (kind (iii) asks R_{k+1} inside R_k), r30 (R30 (c) with n - 2)."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-1O"))
import onecheck as OC
RC, Engine, lpg = OC.RC, OC.Engine, OC.lpg
MUT = os.environ.get("FX_MUT", "")

def reach_o(g, f, o):
    R = set()
    for v in range(g.n):
        if v == o: continue
        x, seen = v, set()
        while x not in seen and x != o:
            seen.add(x); x = f[x]
        if x == o: R.add(v)
    return frozenset(R)

def check(g, o, states, fbs, st, name):
    E = Engine(lpg.Game(list(g.prio), list(g.owner), [list(s) for s in g.succ])); n = g.n; do = len(g.succ[o])
    lam, R, cw = [], [], []
    for sg, tu in states:
        vs, _ = E.evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
        lam.append(tuple(vs[v][0] for v in range(n)))
        f = [sg[v] if g.owner[v] == 0 else tu[v] for v in range(n)]
        R.append(reach_o(g, f, o)); cw.append(g.play(f, o)[0][0])
    key = [(lam[k], tuple(states[k][1])) for k in range(len(states))]
    phases, cur = [], [0]
    for k in range(1, len(states)):
        if key[k] == key[k - 1]: cur.append(k)
        else: phases.append(cur); cur = [k]
    phases.append(cur)
    Fs = 1 + (n - 2) * (2 * n - 1); T = n * n + 2 * n - 1
    for ph in phases:
        cth = lam[ph[0]][o]; f = X = xsn = 0
        for k in ph[:-1]:
            if fbs[k]: f += 1
            if R[k + 1] == R[k]: continue
            X += 1
            if fbs[k]: st.inc("kind_i")
            elif cw[k] == cth: xsn += 1; st.inc("kind_ii")
            else:
                st.inc("kind_iii")
                ok = (R[k + 1] < R[k]) if MUT == "stick" else (R[k] < R[k + 1])
                if not ok: st.bad("KIND", f"{name}: kind (iii) at {k} not a strict enlargement")
        st.inc("phases")
        if X: st.inc("phases_with_X")
        a = n * (f + xsn) + n - 1 if MUT != "seg" else (n - 1) * (f + xsn) + n - 2
        if MUT == "noiii": a = f + xsn
        if X > a: st.bad("FXA", f"{name}: X {X} > FX(a) {a} (f {f}, X_SN {xsn})")
        b = n * (Fs + 13 * (do + 1) * n ** 3 * (Fs + 1 + T) + T) + n - 1
        if X > b or (n >= 2 and f > max(Fs, 1)): st.bad("FXB", f"{name}: X {X} or f {f} over FX(b)")
        r30 = (f + 1) * (n - 1) + f + xsn if MUT != "r30" else (f + 1) * (n - 2) + f + xsn
        if X > r30: st.bad("R30C", f"{name}: X {X} > R30 (c) {r30}")
        if X: st.mxr("max_X", (X, name)); st.mxr("X_over_FXa", (X / max(a, 1), name)); st.mxr("X_over_R30c", (X / r30, name))
        st.mxr("max_XSN", (xsn, name)); st.mxr("max_f", (f, name))

def main():
    st = OC.Stats(); a = sys.argv[1:]
    def go(g, o, s, t, name):
        states, fbs = RC.n5_spec(g, o, s, t); st.inc("runs"); check(g, o, states, fbs, st, name)
    if a[0] == "random":
        N, nmin, nmax, seed = map(int, a[1:5]); rng = random.Random(seed)
        for i in range(N):
            g, o = RC.rand_game(rng, rng.randint(nmin, nmax), cyc=rng.random() < 0.7)
            s, t = RC.rand_start(rng, g) if i % 2 else OC.s3(g)
            go(g, o, s, t, f"random{seed}:{i}")
    else:
        runs = int(a[2]) if len(a) > 2 else 3; rng = random.Random(1014)
        for path in [l.strip() for l in open(a[1]) if l.strip()]:
            g = RC.parse(open(os.path.join(OC.ROOT, path)).read()); o = OC.one_choice(g)
            if o is None: st.inc("skipped_not_1O"); continue
            for r in range(runs):
                s, t = OC.s3(g) if r == 0 else RC.rand_start(rng, g)
                go(g, o, s, t, f"{path}#{r}")
    print("MODE", " ".join(a), "MUT", MUT or "-")
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for v in st.viol: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c.get("VIOLATIONS") else "OK", f"violations={st.c.get('VIOLATIONS', 0)}")

if __name__ == "__main__":
    main()
