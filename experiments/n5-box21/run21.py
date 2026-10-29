#!/usr/bin/env python3
"""L-COMP box 21: N5, N5-SF and Oink on PGSolver's friedmannsubexp / fearnleysubexp (ports in hard-families/pgsolver_port.py), start = SPEC S3
(best-reward; PGSolver's generators define no start). Per instance:
- N5 by n5b SPEC (L-COMP engine): iterations, fallbacks, λ-phases (key (λ_Ξ, τ), R38 (a)) and the longest phase (box17.phases);
- the same run by n5x (L-NEW / L-SI engine, via n5-exhaustive check_instance's trace): the state sequences must be equal;
- N5's output: regions = Oink zlk @ 8fbf0a7 (tl if zlk aborts), strategies pass harness/verify.py;
- N5-SF by L-NEW's n5sf.py (verbatim copy, n5-box20/lnew_box54, l-new 56a42d4f): iterations, fallbacks, cycle, SBC_σ (σ̄ changes), SBC_τ
  (τ̄ changes, the mirror), LAM, SEG ((σ̄, λ_Ξ)-stretches), regions vs Oink, final improving edge.
Usage: run21.py GAME.pg ...   (prints one ROW per game)"""
import hashlib, json, os, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); EXP = os.path.abspath(os.path.join(HERE, ".."))
for p in ("n5-box20/lnew_box54", "n5-box17", "n5-exhaustive", "harness", "n5-second"):
    sys.path.insert(0, os.path.join(EXP, p))
import n5sf  # noqa: E402
from n5x import Engine, dual  # noqa: E402
import box17 as B, pg, verify  # noqa: E402
from exh import trace as n5x_trace  # noqa: E402
import n5  # noqa: E402
OINK = os.path.join(EXP, "..", "tools", "oink", "build", "oink")


def oink(path, n):
    with tempfile.TemporaryDirectory() as td:
        out = os.path.join(td, "s"); r = subprocess.run([OINK, "--zlk", "-w", "1", path, out], capture_output=True); tag = "zlk"
        if r.returncode != 0:
            subprocess.run([OINK, "--tl", "-w", "1", path, out], capture_output=True, check=True); tag = "tl"
        return pg.read_sol(open(out).read(), n), tag


def main():
    for path in sys.argv[1:]:
        g = pg.read(path); n = g.n; sha = hashlib.sha1(open(path, "rb").read()).hexdigest(); ref, tag = oink(path, n)
        e = B.Eng(g); R = B.trajectory(e, e.start()); an = B.analyse(e, R); ph = list(B.phases(R))
        n5b_states = [(r["s"], r["t"]) for r in R]
        st, fb = n5x_trace(g, None, check=True)
        ev = lambda s, own: tuple(s[v] for v in range(n) if g.owner[v] == own)
        same = len(st) == len(n5b_states) and all(ev(a[0], 0) == ev(b[0], 0) and ev(a[1], 1) == ev(b[1], 1) for a, b in zip(st, n5b_states))
        it, fb5, win, ws, _ = n5.run(g, "n5", None); errs = verify.check(g, win, ws)
        E, T = n5sf.trace(g, None); cyc = T[-1].get("cycle", False); T2 = [x for x in T if "lam" in x]; Ed = Engine(dual(g))
        tb = [tuple(Ed.evaluate(tuple(x["t"]))[1]) for x in T2]
        sbs = sum(T2[i]["sb"] != T2[i + 1]["sb"] for i in range(len(T2) - 1)); sbt = sum(tb[i] != tb[i + 1] for i in range(len(T2) - 1))
        lam = sum(T2[i]["lam"] != T2[i + 1]["lam"] for i in range(len(T2) - 1))
        seg = 1 + sum((T2[i]["sb"], T2[i]["lam"]) != (T2[i + 1]["sb"], T2[i + 1]["lam"]) for i in range(len(T2) - 1))
        vs, _ = E.evaluate(tuple(T2[-1]["s"])); sfwin = [E.par[x[0]] for x in vs]; sfopt = bool(E.improving(tuple(T2[-1]["s"]), vs))
        row = dict(game=os.path.basename(path), sha1=sha, n=n, m=g.m, start="S3",
                   n5_it=len(R) - 1, n5_fb=sum(r["fb"] for r in R), n5_phases=len(ph), n5_longest_phase=max([j - i for i, j in ph], default=0),
                   n5b_eq_n5x=same, n5_regions_eq_oink=(win == ref), oink=tag, verify="OK" if not errs else str(errs[:2]),
                   sf_it=len(T2) - 1, sf_fb=sum(x.get("fb", 0) for x in T2), sf_cycle=cyc, sbc_sigma=sbs, sbc_tau=sbt, sbc=sbs + sbt,
                   sf_lam=lam, sf_seg=seg, sf_regions_eq_oink=(sfwin == list(ref)), sf_final_improving=sfopt,
                   seg_max=an["seg"], exc_max=an["exc"], lwgap_max=an["gap"], f_max=an["f"])
        print("ROW", json.dumps(row), flush=True)


if __name__ == "__main__":
    main()
