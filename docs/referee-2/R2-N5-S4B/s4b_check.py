#!/usr/bin/env python3
r"""REFEREE-2 successor 25 (Opus 5.5, D15): own check of P-N5-S4B (docs/si/P-N5-S4B-box63.md @ l-si 68fa36619, sha1 f1b65da5).
Engine: my lane's DC.Runner / Engine / dual / pg (R2-N5-FRAME via R2-N5-LATEP); starts via R2-N5-WRUN read_start (validated). The lane's
experiments/si/anc58/s4bopt.py is NOT imported. At every state k with I_tau_k nonempty:
  H'_k built from the SPEC S4b text (Odd v: {tau_k(v)} u I_tau_k(v); Even v: sigma_k(v); G's priorities), tau_new := Engine(H'_k).evaluate(sigma_k)'s
  counterstrategy (S1's procedure on H', not dual).
  NEXT   tau_(k+1) = tau_new unless Odd fallback (fallback with I_sigma_k empty)      KEEP  tau-stretch transition => tau_k = tau_new
  OPTV   brute force over every positional Odd strategy of H'_k (if <= CAP): no (rho, x) with val(sigma_k, rho)(x) strictly below val(sigma_k, tau_new)(x)
  MUT=1  replaces tau_new by tau_k in OPTV (control: must bite somewhere).
Usage: s4b_check.py files list.txt [runs [prefix]]"""
import sys, os, itertools
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-LATEP")); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-WRUN"))
import latep_check as L
import wrun_check as WR
DC, pg, Engine, dual, pval = L.DC, L.pg, L.Engine, L.dual, L.pval
CAP = int(os.environ.get("CAP", "1024")); MUT = os.environ.get("MUT")


def run_game(g, s, t, st, name):
    n = g.n; E = Engine(g); Ed = Engine(dual(g)); K_ = E.key
    states, fbs = DC.Runner(g).run(list(s), list(t), cap=L.MAXT)
    K = len(states) - 1; st.inc("runs")
    for k in range(K + 1):
        sg, tu = states[k]
        xe, _ = E.evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n))); Is = set(E.improving(tuple(sg), xe))
        vt, _ = Ed.evaluate(tuple(tu[v] if g.owner[v] == 1 else -1 for v in range(n))); It = set(Ed.improving(tuple(tu), vt))
        if not It: continue
        st.inc("states_It")
        A = {v: sorted({tu[v]} | {w for (x, w) in It if x == v}) for v in range(n) if g.owner[v] == 1}
        succ = [A[v] if g.owner[v] == 1 else [sg[v]] for v in range(n)]
        Hp = pg.Game(list(g.prio), list(g.owner), succ)
        _, best = Engine(Hp).evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
        tnew = [best[v] if g.owner[v] == 1 else tu[v] for v in range(n)]
        if k < K:
            nt = states[k + 1][1]; oddfb = bool(fbs[k]) and not Is
            if oddfb: st.inc("odd_fallbacks")
            elif list(nt) != tnew: st.bad("NEXT", f"{name}@{k}")
            if list(nt) == list(tu):
                st.inc("KEEP_checks")
                if tnew != list(tu): st.bad("KEEP", f"{name}@{k}")
        ref = list(tu) if MUT else tnew
        Odd = [v for v in range(n) if g.owner[v] == 1]; prod = 1
        for v in Odd: prod *= len(A[v])
        if prod > CAP: st.inc("states_not_enumerated"); continue
        st.inc("states_enumerated")
        nx0 = [sg[v] if g.owner[v] == 0 else ref[v] for v in range(n)]; base = [K_(pval(E, nx0, x)) for x in range(n)]
        for ch in itertools.product(*[A[v] for v in Odd]):
            st.inc("rhos"); r = dict(zip(Odd, ch)); nx = [sg[v] if g.owner[v] == 0 else r[v] for v in range(n)]
            for x in range(n):
                if K_(pval(E, nx, x)) < base[x]: st.bad("OPTV", f"{name}@{k} x={x}"); break


L.run_game = run_game; L.read_start = WR.read_start
KEYS = ("NEXT", "KEEP", "OPTV")
if __name__ == "__main__":
    import io, contextlib, re
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf): L.main()
    bad = 0
    for l in buf.getvalue().splitlines():
        if not l.startswith("RESULT"): print(l)
        m = re.match(r"(\S+): (\d+)$", l)
        if m and m[1] in KEYS: bad += int(m[2])
    print("RESULT", "PASS" if bad == 0 else "FAIL", "violations", bad)
