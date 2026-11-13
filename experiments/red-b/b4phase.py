#!/usr/bin/env python3
"""B4 (L-RED-B successor 3; docs/red-b/B4-postfb.md §2): phases of N5 (SPEC) runs on guided wrappers. For each wrapper: run n5v
(mode spec, or xi for the engdiff CONTROL) step by step from S3, record the fallback iterations f_1 < ... < f_k, print PRE, BETWEEN,
POST, k, I, P1 = I - f_1; run n5b --mode spec on the same .pg; must-0 counters wrong (regions vs harness Zielonka), engdiff
((I, k) of engine 1 vs engine 2), phasesum. Inputs: state files of gfam.py / gclimb.py (as gverify.py), or «fam FAMILY n...» (the
family member with its own start, rho0 = Odd's optimal counterstrategy to it in H, gamma empty).
Usage: b4phase.py B3ROOT OUTDIR ALG (STATEFILE... | fam FAMILY n...)"""
import sys, os, json, hashlib, subprocess, re
root = os.path.abspath(sys.argv[1]); out = sys.argv[2]; ALG = sys.argv[3]; os.makedirs(out, exist_ok=True)
os.environ["LNEW"] = os.path.join(root, "lnew"); os.environ["LRED"] = os.path.join(root, "lred")
os.environ["LLIT"] = os.path.join(root, "llit"); os.environ["HN"] = os.path.join(root, "lcomp/experiments/friedmann-hn")
sys.path.insert(0, os.path.join(root, "lsi/experiments/si/box104"))
import gscan104 as GS
import wrap104 as W
from wrap104 import pg, n5v, n5, n5x, zielonka
from si import Engine
N5B = os.path.join(root, "trunk/experiments/n5-second/n5b.py")

def fam(name, n):
    if name == "fried": r = W.fried_game(n); return r[0], list(r[1])
    if name == "lmcs": H, s0 = W.lmcs_game(n, "fig4"); return H, list(s0)
    if name == "hn": H, s0 = GS.fam("hn", n); return H, list(s0)

def phases(g, cap=10 ** 6):
    E, Ed = Engine(g), Engine(n5.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None); its = 0; fl = []
    while its < cap:
        r = n5v.step(g, E, Ed, sigma, tau, ALG)
        if r is None: break
        sigma, tau, _, _, fb = r; its += 1
        if fb: fl.append(its)
    vs, _ = E.evaluate(tuple(sigma)); win = [0 if g.prio[vs[v][0]] % 2 == 0 else 1 for v in range(g.n)]
    return its, fl, int(win != zielonka.solve(g))

def one(tag, H, s0, rho0, gamma, copy):
    g = GS.wrapg(H, s0, rho0, gamma, copy)[0]
    path = os.path.join(out, tag + ".pg"); pg.write(g, path); sha = hashlib.sha1(open(path, "rb").read()).hexdigest()
    I, fl, wrong = phases(g); k = len(fl)
    if k:
        pre = fl[0] - 1; post = I - fl[-1]; between = sum(fl[i + 1] - fl[i] - 1 for i in range(k - 1)); p1 = I - fl[0]
    else:
        pre, post, between, p1 = I, 0, 0, 0
    phasesum = int(I != pre + between + post + k)
    r = subprocess.run([sys.executable, N5B, path, "--mode", "spec"], capture_output=True, text=True)
    m = re.search(r"iterations (\d+) fallbacks (\d+)", r.stdout)
    engdiff = int(not m or (int(m.group(1)), int(m.group(2))) != (I, k))
    print("B4PHASE alg %s %s |H| %d |Wg| %d sha1 %s | I %d k %d PRE %d BETWEEN %d POST %d P1 %d fallbacks at %s | n5b %s | wrong %d engdiff %d phasesum %d" % (
        ALG, tag, H.n, g.n, sha, I, k, pre, between, post, p1, fl[:12], ("I %s k %s" % m.groups()) if m else "FAILED",
        wrong, engdiff, phasesum), flush=True)
    os.remove(path)
    return wrong, engdiff, phasesum

tot = [0, 0, 0]; cnt = 0
if sys.argv[4] == "fam":
    name = sys.argv[5]
    for n in map(int, sys.argv[6:]):
        H, s0 = fam(name, n); EH = Engine(H)
        _, cs = EH.evaluate(tuple(s0[v] if H.owner[v] == 0 else -1 for v in range(H.n)))
        rho0 = {v: cs[v] for v in range(H.n) if H.owner[v] == 1}
        r = one("%s_n%d_own" % (name, n), H, s0, rho0, {}, True); cnt += 1
        for i in range(3): tot[i] += r[i]
else:
    for sf in sys.argv[4:]:
        S = json.load(open(sf)); base = os.path.basename(sf)[:-5]
        if base.startswith("gfam_") or base.startswith("b4c_b4_"):
            m = re.match(r"(?:gfam|b4c_b4)_([a-z]+)_n(\d+)_s\d+_c(\d)", base); H = fam(m.group(1), int(m.group(2)))[0]; copy = m.group(3) == "1"
            G = S["G"]; s0 = [G["s0"].get(str(v), -1) if H.owner[v] == 0 else -1 for v in range(H.n)]
            rho0 = {v: G["rho"][str(v)] for v in range(H.n) if H.owner[v] == 1}
            gamma = {tuple(map(int, k.split(","))): t for k, t in G["gam"].items()}
        else:
            D = S["D"]; copy = base.endswith("_c1"); H = pg.Game(D["prio"], D["own"], D["succ"])
            s0 = [D["s0"][str(v)] if D["own"][v] == 0 else -1 for v in range(H.n)]
            rho0 = {v: D["rho"][str(v)] for v in range(H.n) if D["own"][v] == 1}
            gamma = {tuple(map(int, k.split(","))): t for k, t in D["gam"].items()}
        r = one(base, H, s0, rho0, gamma, copy); cnt += 1
        for i in range(3): tot[i] += r[i]
print("B4PHASE SUMMARY alg %s wrappers %d wrong %d engdiff %d phasesum %d" % (ALG, cnt, tot[0], tot[1], tot[2]), flush=True)
