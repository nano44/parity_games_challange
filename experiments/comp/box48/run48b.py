#!/usr/bin/env python3
"""L-COMP BOX 48 (3)+(4) (Lead 12:28Z): N5 on the GAME Γ3(G_k), two independent implementations.
 - MY Γ3: experiments/comp/box34/own34.build(G_k, elev=True) (my builder from R104 + P-N5-REACH §3 text), S3 = own34.standard; written as
   inst/G_<k>_g3.pg (pgsolver format, sha1 logged) with the start in inst/G_<k>_g3.start.
 - n5b (experiments/n5-second/n5b.py, L-COMP's second N5 implementation) --mode spec from that start, to the end: iterations, fallbacks,
   winners + strategies (its .sol); run with python3 -I.
 - wrong: n5b's winners against Zielonka (experiments/harness/zielonka.py) on the same game, unit vertex, must 0; verr: the harness strategy
   verifier (experiments/harness/verify.py check) on n5b's (win, strat), must 0.
 - engdiff: (iterations, fallbacks) of n5b vs L-NEW's n5v spec on L-NEW's own Γ3 (box 189 gamma3.build with all pads; box47/replay47.run,
   env LNEW = archive of claude/l-new), must 0; the first-fallback step T of n5v is printed too (= T_key + 1 + ... as L-RED-B reports).
 - controls (each must fire): ctrl_mode: n5b --mode xi on my Γ3: its (iterations, fallbacks) differ from n5v spec (engdiff_ctrl 1);
   ctrl_win: Zielonka's winners with vertex 0's winner flipped vs Zielonka (wrong_ctrl ≥ 1).
One line per k appended to out/run48b.out (a k already there is skipped). Usage: run48b.py KLO KHI [--non5v]"""
import sys, os, json, subprocess, hashlib, time
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(H, "..", "..", ".."))
sys.path[:0] = [H, os.path.join(H, "..", "box34"), os.path.join(H, "..", "box47"), os.path.join(R, "experiments", "harness")]
import gk48, own34, pg, zielonka, verify
a = sys.argv[1:]; non5v = "--non5v" in a; a = [x for x in a if x != "--non5v"]; klo, khi = int(a[0]), int(a[1])
OUT = os.path.join(H, "out", "run48b.out"); done = set()
if os.path.exists(OUT): done = {l.split()[0] for l in open(OUT) if l.strip()}
def n5b(p, st, mode, sol=None):
    cmd = [sys.executable, "-I", os.path.join(R, "experiments", "n5-second", "n5b.py"), p, "--start", st, "--mode", mode] + ([sol] if sol else [])
    o = subprocess.run(cmd, capture_output=True, text=True).stdout.split(); i = o.index("iterations"); return int(o[i + 1]), int(o[i + 3])
for k in range(klo, khi + 1):
    if "G_%d" % k in done: continue
    G, names = gk48.gen(k); g, V = own34.build(G, True); s, t = own34.standard(G, V, g)
    p = os.path.join(H, "inst", "G_%d_g3.pg" % k); st = p[:-3] + ".start"; sol = p[:-3] + ".n5b.sol"
    pg.write(g, p); open(st, "w").write("SIGMA0 " + " ".join("%d:%d" % (v, w) for v, w in enumerate(s) if w >= 0) + "\nTAU0 " + " ".join("%d:%d" % (v, w) for v, w in enumerate(t) if w >= 0) + "\n")
    hp = hashlib.sha1(open(p, "rb").read()).hexdigest()[:12]
    t0 = time.time(); it, fb = n5b(p, st, "spec", sol); dt = time.time() - t0
    win = pg.read_sol(open(sol).read(), g.n); strat = [None] * g.n
    for l in open(sol):
        w_ = l.strip().rstrip(";").split()
        if len(w_) >= 3 and w_[0].isdigit(): strat[int(w_[0])] = int(w_[2])
    zw, _ = zielonka.solve_with_strategy(g); wrong = sum(1 for v in range(g.n) if win[v] != zw[v]); verr = len(verify.check(g, win, strat))
    fl = list(zw); fl[0] ^= 1; wctrl = sum(1 for v in range(g.n) if fl[v] != zw[v])
    itx, fbx = n5b(p, st, "xi")
    if non5v: nv = None
    else:
        import replay47; r = replay47.run(G, "spec"); nv = (r["Ttot"], r["F"], r["T"], r["n"])
    eng = "n/a" if nv is None else int((it, fb) != (nv[0], nv[1])); engc = "n/a" if nv is None else int((itx, fbx) != (nv[0], nv[1]))
    W0 = sum(1 for v in range(g.n) if win[v] == 0)
    line = "G_%d N %d n %d pg_sha1 %s | n5b spec iterations %d fallbacks %d sec %.0f | wrong %d verr %d (Even wins %d of %d) | n5v spec %s | engdiff %s | ctrl: n5b xi iterations %d fallbacks %d engdiff_ctrl %s, wrong_ctrl %d" % (
        k, G["N"], g.n, hp, it, fb, dt, wrong, verr, W0, g.n, "iterations %d fallbacks %d T_first_fallback %d n %d" % nv if nv else "not run", eng, itx, fbx, engc, wctrl)
    with open(OUT, "a") as f: f.write(line + "\n")
    print(line, flush=True)
