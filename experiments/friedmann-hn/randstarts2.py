#!/usr/bin/env python3
"""Box 16 §4 (Lead 2026-10-28 21:05Z): N5 (n5b SPEC) on H_n (hn.py, mode fig, or a variant via --var) from R seeded random start pairs
plus G<k> starts (the I^glo strategy after k steps from ι, every GSTEP-th step, with τ = σ̄(σ_k)).
Per run: iterations, fallbacks, phases (R38 (a) key (λ_Ξ, τ)), longest phase (in-phase transitions), and per phase
  XR    = max over vertices v of #{in-phase transitions t -> t+1 with Ξ_t(v) != Ξ_{t+1}(v)} (Lead's "max Ξ-changes of one vertex per
          phase"); XRQ the same over Q (Odd vertices of out-degree >= 2);
  ALT   = max over S, c of ALT_c(S), N5-EXIT-box22 §9, same counter as box16.alt_phase (S split at fallbacks and λ_W changes).
The rows ALT needs (vs, sb, s, t, wn) are built from n5b's states with L-SI's Engine (experiments/si/si.py, via L-SI common.py; read-only);
its σ̄ is asserted equal to SPEC σ̄ (n5b SpecSI.evaluate_choice) at every state (an engine cross-check on every state).
Regions vs Oink zlk (one call per game; regions do not depend on the start) and verify.py on n5b's strategies, every run.
TF  = max over u in Q of the number of τ changes at u in the run; TFG = max over the gate vertices e_i of the number of changes of
      their owner's strategy (τ(e_i) in H_n / ex, σ(e_i) in dual): the "τ flips repeat at a gate" probe of §5.
Usage: randstarts2.py N R SEED GSTEP [--var NAME]   (NAME in hn_var.VARS; GSTEP 0 = no G starts)"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
for p in ("n5-epoch", "n5-exhaustive", "n5-second", "harness", "hard-families"):
    sys.path.insert(0, os.path.join(ROOT, "experiments", p))
sys.path.insert(0, HERE)
import hn  # noqa: E402
import census as CE  # noqa: E402
import check_instance as CI  # noqa: E402
from check_instance import n5b, verify, pg  # noqa: E402
from pgsolver_si import SI  # noqa: E402
sys.modules.pop("common", None)
sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "root"))
import common as LC  # noqa: E402  (L-SI, read-only)
import box16  # noqa: E402
assert hasattr(LC, "rows")

a = sys.argv[1:]
n, R, seed, gstep = int(a[0]), int(a[1]), int(a[2]), int(a[3])
var = a[a.index("--var") + 1] if "--var" in a else None
if var:
    import hn_var  # noqa: E402
    g, ix = hn_var.build(n, var); tag = f"H{n}{var}"
else:
    g, ix = hn.build(n); tag = f"H{n}"
os.makedirs(os.path.join(HERE, "instances"), exist_ok=True)
gp = os.path.join(HERE, "instances", f"{tag}.pg")
pg.write(g, gp)
ref, rtag = CI.zlk(gp, g.n)
SG = n5b.SpecSI(g); E = LC.Engine(g); box16.ENG[0] = E
rng = random.Random(seed)
starts = [("S3", None, None)]
io = hn.iota(n, ix) if not var else hn_var.iota(n, ix, var)
sig0 = [io.get(v, -1) if g.owner[v] == 0 else -1 for v in range(g.n)]
if var == "dual":   # ι is the counting player's start, here Odd's: F = (S3's σ, ι as τ)
    starts.append(("F", None, [io[v] if g.owner[v] == 1 else -1 for v in range(g.n)]))
else:
    _, sb0 = SG.evaluate_choice(list(sig0)); starts.append(("F", sig0, [sb0[v] if g.owner[v] == 1 else -1 for v in range(g.n)]))
for r in range(R):
    s, t = CE.rand_start(g, rng); starts.append((f"rand{r}", s, t))
if gstep:
    si = SI(g); strat = list(sig0); valu = si.evaluate(strat); k = 0
    while True:
        if k % gstep == 0 and k:
            _, sb = SG.evaluate_choice(list(strat)); starts.append((f"G{k}", list(strat), [sb[v] if g.owner[v] == 1 else -1 for v in range(g.n)]))
        if not any(g.owner[i] == 0 and si.nvo(valu[strat[i]], valu[si.best(valu, i)]) < 0 for i in range(g.n)):
            break
        strat = si.policy_switchbest(strat, valu); valu = si.evaluate(strat); k += 1
    print(f"# I^glo from ι: {k} steps", flush=True)
Q = [v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2]
worst = {}; bad = 0
for lab, s, t in starts:
    L, FB = [], []
    win, ws, it, fb = n5b.N5(g, mode="spec").run(list(s) if s else None, list(t) if t else None, trace=L, fbtrace=FB, max_iter=10 ** 6)
    ok = win == ref and not verify.check(g, win, ws)
    A = [CE.state_info(g, SG, x[0], x[1]) for x in L]
    rows = []
    for k, (sg, tg) in enumerate(L):
        vs, sb = E.evaluate(tuple(sg))
        if any(sb[v] != A[k]["sbar"][v] for v in Q):
            ok = False
        W, wn = LC.wplay(E, g, sg, tg)
        rows.append(dict(vs=vs, sb=list(sb), s=list(sg), t=list(tg), wn=wn, fb=FB[k] if k < len(FB) else 0))
    bad += not ok
    lamW_ch = [A[k]["lamW"] != A[k + 1]["lamW"] for k in range(len(A) - 1)] + [False]
    key = [(A[k]["lam"], L[k][1]) for k in range(len(L))]
    ph, i = [], 0
    while i < len(key):
        j = i
        while j + 1 < len(key) and key[j + 1] == key[i]:
            j += 1
        ph.append((i, j)); i = j + 1
    XR = XRQ = ALT = 0
    for x, y in ph:
        cnt = [0] * g.n
        for k in range(x, y):
            for v in range(g.n):
                if A[k]["Xi"][v] != A[k + 1]["Xi"][v]:
                    cnt[v] += 1
        XR = max(XR, max(cnt)); XRQ = max(XRQ, max([cnt[q] for q in Q] or [0]))
        ALT = max(ALT, box16.alt_phase(g, rows, x, y, lamW_ch)[0])
    tf = [0] * g.n
    for k in range(len(L) - 1):
        for v in Q:
            if L[k][1][v] != L[k + 1][1][v]:
                tf[v] += 1
    TF = max(tf + [0])
    gates = [v for v in range(g.n) if g.labels and g.labels[v] and g.labels[v][0] == "e"]
    TFG = max([sum(1 for k in range(len(L) - 1) if L[k][g.owner[v]][v] != L[k + 1][g.owner[v]][v]) for v in gates] + [0])
    longest = max(y - x for x, y in ph)
    rec = dict(it=it, fb=fb, phases=len(ph), longest=longest, XR=XR, XRQ=XRQ, ALT=ALT, TF=TF, TFG=TFG)
    print(f"{tag} {lab} " + " ".join(f"{k} {v}" for k, v in rec.items()) + f" {'OK' if ok else 'FAIL'}", flush=True)
    fam = "rand" if lab.startswith("rand") else "G" if lab.startswith("G") else lab
    for kk, v in rec.items():
        if fam not in worst:
            worst[fam] = {}
        if kk not in worst[fam] or v > worst[fam][kk][0]:
            worst[fam][kk] = (v, lab)
sha = __import__("hashlib").sha1(open(gp, "rb").read()).hexdigest()
for fam, d in worst.items():
    print(f"END {tag} sha1 {sha[:12]} V {g.n} fam {fam} " + " ".join(f"max_{k} {v[0]}({v[1]})" for k, v in d.items()))
print(f"END {tag} runs {len(starts)} bad {bad} oink {rtag}")
