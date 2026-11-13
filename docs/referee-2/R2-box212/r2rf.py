#!/usr/bin/env python3
"""REFEREE-2 successor 40: own replay for the PRE-READ of box 212 RF-LEVEL (L-NEW 74, claude/l-new be167574). Shares no code with
L-NEW (rf212 / rfd212 / rv208 / level208), L-RED, L-COMP or REFEREE. Engine: REFEREE-2's own R2-P-ACYC/r2acyc.py through
R2-P-N5-LEVEL/r2lv.py (successor 39), whose counters are reused unchanged; only the step rule is replaced here.

An IMPROVING RUN (box 212 §3, written from its text): every step changes σ at a non-empty set of movers, each to a gate of strictly
⊴-larger Ω_t value. Rules (own definitions; RF-A / RF-B / RF-C claim the rule-free counters for EVERY such rule):
  howard   r2lv's own Howard step (tie --tie)
  allleast every improvable mover to its ⊴-least strictly better gate      allrand  every improvable mover to a random strictly better gate
  subrand  a random non-empty subset of improvable movers, random better    onebest  one random improvable mover, to a ⊴-best gate
  oneleast the least-index improvable mover, to its ⊴-least better gate      onerand  one random improvable mover, random better gate
  worsen   CONTROL: Howard, but at step 0 one mover moves to a strictly WORSE gate (impfail, k1fail, f1fail must fire)
Must-0 under every rule (RULEFREE): r2lv's cn2 bonly notie locgate lock2 f1 opt pistart k1 k2 k3a-e k4 l1 l2 l3 l3then l5 c2 p1 p2 p4,
and here: impfail [step] not an improving step | k5newfail [(t,x)] class_(t+1)(x) < class_t(σ_(t+1)(x)) (RF-A (iv)) |
nspfail [b] more than P non-stall steps with LAG ≠ ∅ before b | p5pvalfail [(b,plateau,s,x)] H_Y (movers keep their gates IN Y, every
other vertex s_u(x)) valued by r2lv.hvalues ≠ Ω_s on Y | p5pimpfail [(b,plateau,s,x)] a switch at a mover of Y that leaves Y or is not
strictly H_Y-improving | tailfail [run] on the tail [b′, T] (b = T) a class changes, a gate changes its face, or σ̄(K2) ≠ K1 |
rfcfail [run] T > P + (P + 1)·W, W = the longest plateau or the tail (b = T) | rfa1fail [run] T > (P + 1)(λ* + 1) + tail, λ* longest plateau.
Descriptive under a non-Howard rule (Howard-only facts, expected to fire): r2lv's dom k5 quietn l4map l4cyc c3 c4 win rh k1t fvst allt
p3 p5val p5step p6 p7 h0 p7run; records: rec_restrict_diff [(b,plateau,s)] a non-idle step of the run on the movers of Y ≠ the
SAME rule applied to H_Y at σ_s|Y (deterministic rules only: howard (max tie), allleast, oneleast); rec_restrict_idle: steps that move no
mover of Y; rec_restrict_steps: the non-idle steps compared; rec_platexit [(b,plateau,s,x)] a mover of Y with a strictly
better gate outside Y; rec_tail_gt_N [run]; rec_Wmax; rec_nsp_max.
Controls (--rctrl, each must FIRE; mechanics of the new counters): k5t (K5-NEW with class_t(x)), nsp0 (bound 0 for nspfail), tailshift
(the tail from b′ − 1), rfc (bound := W alone: fires on a run with a step outside its longest window), hval (H_Y valued with relevance by index: p5pvalfail). The rule control is --rule worsen.
Usage: r2rf.py --rule R [--rctrl C] [--tie max|min] [--seed S] [--gen COUNT SEED KIND] [--mut COUNT SEED FILE] FILES...
"""
import sys, os, random
from collections import defaultdict
H = os.path.dirname(os.path.abspath(__file__))
R2 = os.environ.get("R2DIR", os.path.join(H, ".."))
sys.path[:0] = [os.path.join(R2, "R2-P-N5-LEVEL"), os.path.join(R2, "R2-P-ACYC"), os.path.join(R2, "R2-P-N5-END"), os.path.join(R2, "R2-P-N5-SPLIT")]
import r2lv as L
A = L.A
RULE = "howard"; RR = random.Random(0); LAST = {}; RCTRL = None
RULEFREE = ["cn2fail", "bonlyfail", "notiefail", "locgatefail", "lock2fail", "f1fail", "optfail", "pistartfail", "k1fail", "k2fail",
            "k3afail", "k3bfail", "k3cfail", "k3dfail", "k3efail", "k4fail", "l1fail", "l2fail", "l3fail", "l3thenfail", "l5fail", "c2fail",
            "p1fail", "p2fail", "p4fail",
            "impfail", "k5newfail", "nspfail", "p5pvalfail", "p5pimpfail", "tailfail", "rfcfail", "rfa1fail"]
HOWONLY = [k for k in L.FAILS if k not in RULEFREE]


def step_choice(g, vj, sig, val, ms, rule, first):
    """returns the new mover state (list of option indices) or None if no mover is improvable."""
    V = g["V"]; succ = g["succ"]; N = g["N"]; cmp = vj.cmp
    imp = {}
    for x in range(N):
        xv = V[("x", x)]; cur = sig[xv]
        better = [w for w in succ[xv] if cmp(val[w], val[cur]) > 0]
        if better: imp[x] = (xv, cur, better)
    if not imp: return None
    new = list(ms)
    def best(xv, better):
        b = better[0]
        for w in better:
            if cmp(val[w], val[b]) > 0: b = w
        bl = [w for w in better if cmp(val[w], val[b]) == 0]
        return max(bl) if L.TIE == "max" else min(bl)
    def least(better):
        b = better[0]
        for w in better:
            if cmp(val[w], val[b]) < 0: b = w
        bl = [w for w in better if cmp(val[w], val[b]) == 0]
        return min(bl)
    if rule == "worsen" and first:
        for x in range(N):
            xv = V[("x", x)]; cur = sig[xv]
            worse = [w for w in succ[xv] if cmp(val[w], val[cur]) < 0]
            if worse: new[x] = succ[xv].index(worse[0]); return new
        rule = "howard"
    if rule in ("howard", "worsen"):
        for x, (xv, cur, better) in imp.items(): new[x] = succ[xv].index(best(xv, better))
    elif rule == "allleast":
        for x, (xv, cur, better) in imp.items(): new[x] = succ[xv].index(least(better))
    elif rule == "allrand":
        for x, (xv, cur, better) in imp.items(): new[x] = succ[xv].index(RR.choice(better))
    elif rule == "subrand":
        ks = sorted(imp); S = [x for x in ks if RR.random() < 0.5] or [RR.choice(ks)]
        for x in S: xv, cur, better = imp[x]; new[x] = succ[xv].index(RR.choice(better))
    elif rule == "onebest":
        x = RR.choice(sorted(imp)); xv, cur, better = imp[x]; new[x] = succ[xv].index(best(xv, better))
    elif rule == "oneleast":
        x = min(imp); xv, cur, better = imp[x]; new[x] = succ[xv].index(least(better))
    elif rule == "onerand":
        x = RR.choice(sorted(imp)); xv, cur, better = imp[x]; new[x] = succ[xv].index(RR.choice(better))
    else: raise SystemExit("unknown rule " + rule)
    return new


def run(G, cap=5000):
    g = A.build(G, False); vj = A.VJ(g); n = g["n"]
    ms = list(G["start"]); St = []
    while True:
        sig = A.mover_sig(g, ms); tau, val = A.odd_opt(g, vj, sig, A.worst_start(g))
        tau2, _ = A.odd_opt(g, vj, sig, None)
        f = [sig[v] if g["owner"][v] == 0 else tau[v] for v in range(n)]
        St.append(dict(f=f, val=val, ms=list(ms), pistart=(tau2 != tau)))
        new = step_choice(g, vj, sig, val, ms, RULE, len(St) == 1)
        if new is None or len(St) > cap: break
        ms = new
    St[0]["ties"] = 0
    LAST.update(g=g, vj=vj, St=St)
    return g, vj, St


def classes(g, vj, St, evs):
    rel = vj.rel
    return [[(vj.rew[s["val"][v][0]], sum(1 << rel[e] for e in s["val"][v][1] if e in evs)) for v in range(g["n"])] for s in St]


def rule_on_H(Y, Ym, fH, hv, succ, cmp, rule):
    """the SAME deterministic rule applied to H_Y (movers of Y keep their gates in Y) at fH: the new successor map on Ym."""
    out = dict((x, fH[x]) for x in Ym); imp = {}
    for x in sorted(Ym):
        better = [w for w in succ[x] if w in Y and cmp(hv[w], hv[fH[x]]) > 0]
        if better: imp[x] = better
    def pick(better, want):
        b = better[0]
        for w in better:
            if cmp(hv[w], hv[b]) * want > 0: b = w
        bl = [w for w in better if cmp(hv[w], hv[b]) == 0]
        return (max(bl) if L.TIE == "max" else min(bl)) if want > 0 else min(bl)
    if rule == "howard":
        for x, bt in imp.items(): out[x] = pick(bt, 1)
    elif rule == "allleast":
        for x, bt in imp.items(): out[x] = pick(bt, -1)
    elif rule == "oneleast" and imp:
        x = min(imp, key=lambda z: z); out[x] = pick(imp[x], -1)
    return out


def extras(C):
    g, vj, St = LAST["g"], LAST["vj"], LAST["St"]
    G = LAST["G"]; sd = L.structure(g, G); n = g["n"]; N = g["N"]; M = g["M"]; succ = g["succ"]; prio = g["prio"]; cmp = vj.cmp
    mset, gates = sd["mset"], sd["gates"]; K1v, K2v = g["V"]["K1"], g["V"]["K2"]
    T = len(St) - 1
    if T >= 5000: return
    P = 2 * M * (N + 2 * M); cls = classes(g, vj, St, sd["evs"])
    movers = sorted(mset)
    for t in range(T):
        f0, f1, val = St[t]["f"], St[t + 1]["f"], St[t]["val"]
        I = [x for x in movers if f1[x] != f0[x]]
        if not I or any(cmp(val[f1[x]], val[f0[x]]) <= 0 for x in I): C["impfail"] += 1
        for x in movers:
            cx = cls[t][x] if RCTRL == "k5t" else cls[t + 1][x]
            if cx < cls[t][f1[x]]: C["k5newfail"] += 1
    nb = n * T * T
    BSET = sorted(set([T] + (list(range(1, T + 1)) if nb <= 3 * 10 ** 7 else L.RNG.sample(range(1, T + 1), min(T, 6)))))
    for b in BSET:
        st = L.level(b, 0, cls, St, sd, g, vj, None, P, M, N, n, T)
        nsp = sum(1 for t in range(b) if st["lag"][t] and t not in st["stallset"])
        C["rec_nsp_max"] = max(C["rec_nsp_max"], nsp)
        if nsp > (0 if RCTRL == "nsp0" else P): C["nspfail"] += 1
        for (u, v) in st["plateaus"]:
            m = st["m"][u]; Y = {x for x in range(n) if cls[u][x] <= m}; Ym = [x for x in Y if x in mset]; fu = St[u]["f"]
            if any(St[s]["f"][x] not in Y for s in range(u, v + 1) for x in Y): continue      # p2fail is counted by r2lv
            for s in range(u, v + 1):
                f = St[s]["f"]; fH = {x: (f[x] if x in mset else fu[x]) for x in Y}
                hv = L.hvalues(Y, fH, prio); val = St[s]["val"]
                for x in Y:
                    if hv[x] != val[x]: C["p5pvalfail"] += 1
                for x in Ym:
                    if any(w not in Y and cmp(val[w], val[f[x]]) > 0 for w in succ[x]): C["rec_platexit"] += 1
                if s < v:
                    f1 = St[s + 1]["f"]
                    for x in Ym:
                        if f1[x] != f[x] and (f1[x] not in Y or cmp(hv[f1[x]], hv[f[x]]) <= 0): C["p5pimpfail"] += 1
                    if RULE in ("howard", "allleast", "oneleast"):
                        if all(f1[x] == f[x] for x in Ym): C["rec_restrict_idle"] += 1      # an idle step on Y (lane: «interleaved»)
                        else:
                            want = rule_on_H(Y, Ym, fH, hv, succ, cmp, RULE)
                            if any(want[x] != f1[x] for x in Ym): C["rec_restrict_diff"] += 1
                            C["rec_restrict_steps"] += 1
        if b == T:
            bp = st["bprime"]; tail = T - bp
            W = max([v - u for (u, v) in st["plateaus"]] + [tail]); lam = max([v - u for (u, v) in st["plateaus"]] + [0])
            C["rec_Wmax"] = max(C["rec_Wmax"], W); C["rec_tail_max"] = max(C["rec_tail_max"], tail)
            if tail > N: C["rec_tail_gt_N"] += 1
            if (T > W) if RCTRL == "rfc" else (T > P + (P + 1) * W): C["rfcfail"] += 1
            if T > (P + 1) * (lam + 1) + tail: C["rfa1fail"] += 1
            for t in range(max(bp - 1, 0) if RCTRL == "tailshift" else bp, T + 1):
                if cls[t] != cls[bp] or St[t]["f"][K2v] != K1v or any(St[t]["f"][gv] != St[bp]["f"][gv] for gv in gates): C["tailfail"] += 1; break


def main(argv):
    global RULE, RCTRL
    rest = []; i = 0
    while i < len(argv):
        if argv[i] == "--rule": RULE = argv[i + 1]; i += 2
        elif argv[i] == "--seed": RR.seed(int(argv[i + 1])); i += 2
        elif argv[i] == "--rctrl":
            RCTRL = argv[i + 1]; i += 2
            if RCTRL == "hval": L.CTRL = "hval"
        else: rest.append(argv[i]); i += 1
    L.run = run
    orig = L.analyse
    def analyse(G, C, nm):
        LAST["G"] = G
        for k in RULEFREE + ["rec_restrict_diff", "rec_platexit", "rec_tail_gt_N"]: C[k] += 0
        orig(G, C, nm)
        extras(C)
        for k in HOWONLY: C["rec_how_" + k] = C.pop(k, 0)
    L.analyse = analyse
    L.FAILS[:] = RULEFREE                       # r2lv prints and sums FAILS: here the rule-free list only
    sys.stdout.write(f"RULE {RULE}; descriptive (Howard-only) counters: {' '.join(HOWONLY)}\n")
    L.main(rest)


if __name__ == "__main__":
    main(sys.argv[1:])
