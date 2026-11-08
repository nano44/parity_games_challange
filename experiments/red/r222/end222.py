#!/usr/bin/env python3
"""L-RED 57 R222 item 3: adversary vs L-NEW 63 box 195 (Theorem ENDGAME-3 / ENDGAME-3-N5, Lemmas E0-E4) @ claude/l-new a42838357.
Runs the algorithm objects themselves (box 190 n5v.step modes spec = N5, xi = N5'-xi, idx = TIE broken by largest index) on
Gamma3(G) (box 189 gamma3.build, all pads), from S3 (box 191 n5x.start_pair). Every CHECK uses L-RED code: own.py's VJ order and its
Odd optimisation (own.evaluate), not n5v's Engine. Per run, counters (0 = the claim held):
  e0   : states with tau != tau at S3 (E0);
  pre  : iterations before the first fallback F whose result K-config != kappa0 (E1 (b));
  e1a  : at S3 and at F's input state: core improving edges (own valuation) != {(K0, K1)} (E1 (a));
  e2   : F's result K-config != kappa1;  e3: iteration F+1 is a fallback or its K-config != kappa2;
  e4   : iteration F+2 is a fallback, or K-config != kappa3, or some beta with a mover Xi-target not on its pb pad;
  len  : total iterations != F + 2;  nofb: no fallback;
  fin  : at the final state (own valuation): some Even vertex has a strictly better successor (I_sigma != {}), or two options of a mover
         differ in value, or a gate's Odd optimum is not strict (pe-face value not strictly below the pbeta-face value), or a gate's
         value != (c_W, {}, 5*lev + 3).
Families (generator copied from L-RED 56's spost221.gen, plus): rand, esc, noesc, deep, dense, lvl0, late (L-RED's own.py-based late),
  self (60 % of Xi-targets = the mover itself), wide (degree 4-6, d 1-3).
Control: CTRL=1 swaps kappa2 / kappa3 and evaluates «fin» at F's result state (e3, e4, fin must fire).
Usage: end222.py FAMILY SEED COUNT OUT.txt   (needs env WT, WT3 as experiments/red/r218/env.sh sets them; resumable by run id)"""
import sys, os, json, random, functools
WT, WT3 = os.environ["WT"], os.environ["WT3"]
sys.path[:0] = [os.path.join(WT3, "experiments/new/box191"), os.path.join(WT, "experiments/new/box190"), os.path.join(WT, "experiments/harness"), os.path.join(WT3, "experiments/new/box189")]
import gamma3, n5v, n5x, pg
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import own
def gen(mode, rng):
    d = rng.randint(6, 9) if mode == "deep" else (rng.randint(1, 3) if mode == "wide" else rng.randint(1, 5))
    w = rng.randint(1, 2) if mode == "deep" else rng.randint(1, 3)
    D = rng.randint(3, 4) if mode in ("dense", "lvl0") else (rng.randint(4, 6) if mode == "wide" else rng.choice([2, 3]))
    lev = [x // w for x in range(d * w)]
    if mode == "lvl0": lev = [0] * rng.randint(2, 4) + lev
    N = len(lev); opts = []
    for x in range(N):
        oo = []
        for _ in range(D):
            wt = rng.choice([y for y in range(N) if lev[y] == lev[x] - 1]) if lev[x] else -1
            if mode == "esc": xt = -1 if rng.random() < 0.7 else rng.randrange(N)
            elif mode == "noesc": xt = rng.randrange(N)
            elif mode == "self": xt = x if rng.random() < 0.6 else rng.choice(list(range(N)) + [-1])
            else: xt = rng.choice(list(range(N)) + [-1])
            oo.append([wt, xt, 0])
        opts.append(oo)
    M = sum(len(o) for o in opts); perm = list(range(M)); rng.shuffle(perm); gate = []; i = 0
    for x in range(N):
        gate.append([])
        for o in opts[x]: o[2] = i; gate[x].append(perm[i]); i += 1
    br = list(range(M)); rng.shuffle(br)
    G = {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": [rng.randrange(2) for _ in range(M)], "start": [rng.randrange(len(o)) for o in opts]}
    if mode == "late":
        out, V, O, _ = own.run(G); vals = out[-1][1]; vj = own.VJ(own.build(G)[1]); key = functools.cmp_to_key(vj.cmp)
        G["start"] = [min(range(len(opts[x])), key=lambda k: key(vals[V[("g", (x, k))]])) for x in range(N)]
    return G
def topg(g): return f"parity {g.n - 1};\n" + "".join(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n" for v in range(g.n))
def check(G, mode, cap=5000):
    pads = {"K", "pe", "pb", "m"}; g, _, _, VV = gamma3.build(G, pads); gp = pg.parse(topg(g)); n = gp.n
    E, Ed = n5v.Engine(gp), n5v.Engine(n5v.dual(gp)); sigma, tau = n5x.start_pair(gp, E, Ed, None)
    K0, K1, K2, K3 = (VV[("K", i)] for i in range(4)); pA, s, q, r = VV["pA"], VV["s"], VV["q"], VV["r"]
    kap = lambda sg: (sg[K0], sg[K1], sg[K3]); k0, k1, k2, k3 = (pA, s, K2), (K1, s, K2), (K1, q, K2), (K1, q, K1)
    if os.environ.get("CTRL") == "1": k2, k3 = k3, k2          # control: the counters must fire
    O = [(x, k) for x in range(G["N"]) for k in range(len(G["opts"][x]))]
    betas = [(VV[("b", qq)], G["opts"][qq[0]][qq[1]][1], VV[("pb", qq)]) for qq in O]
    vj = own.VJ(list(gp.prio)); succ = [list(gp.succ[v]) for v in range(n)]; owner = list(gp.owner)
    def vals_of(sg, tu):
        sig = [sg[v] if owner[v] == 0 else None for v in range(n)]; t0 = {v: tu[v] for v in range(n) if owner[v] == 1}
        return own.evaluate(n, owner, succ, vj, sig, t0)
    def core_improving(sg, tu):
        vals, _ = vals_of(sg, tu)
        return {(v, w) for v in (K0, K1, K3) for w in succ[v] if w != sg[v] and vj.cmp(vals[w], vals[sg[v]]) > 0}
    c = dict(e0=0, pre=0, e1a=0, e2=0, e3=0, e4=0, len=0, nofb=0, fin=0, capped=0)
    tau0 = list(tau); states = [(list(sigma), list(tau))]; fbs = []
    if core_improving(sigma, tau) != {(K0, K1)}: c["e1a"] += 1
    while len(fbs) < cap:
        rr = n5v.step(gp, E, Ed, sigma, tau, mode)
        if rr is None: break
        ns, nt, Is, It, fb = rr; fbs.append(bool(fb)); sigma, tau = list(ns), list(nt); states.append((sigma, tau))
    else: c["capped"] = 1
    c["e0"] = sum(1 for (_, tu) in states if list(tu) != tau0)
    if True not in fbs: c["nofb"] = 1; return c, len(fbs), None
    F = fbs.index(True) + 1                                   # iteration number; result state index F
    c["pre"] = sum(1 for i in range(1, F) if kap(states[i][0]) != k0)
    if core_improving(*states[F - 1]) != {(K0, K1)}: c["e1a"] += 1
    if kap(states[F][0]) != k1: c["e2"] = 1
    if len(fbs) < F + 1 or fbs[F] or kap(states[F + 1][0]) != k2: c["e3"] = 1
    if len(fbs) < F + 2 or fbs[F + 1] or kap(states[F + 2][0]) != k3 or any(xt >= 0 and states[F + 2][0][b] != pb for b, xt, pb in betas): c["e4"] = 1
    if len(fbs) != F + 2: c["len"] = 1
    sg, tu = states[F] if os.environ.get("CTRL") == "1" else states[-1]; vals, _ = vals_of(sg, tu); cW = max(range(n), key=lambda v: gp.prio[v] if gp.prio[v] % 2 == 0 and v not in (K0,) else -1)
    bad = 0
    for v in range(n):
        if owner[v] == 0 and any(vj.cmp(vals[w], vals[sg[v]]) > 0 for w in succ[v] if w != sg[v]): bad += 1
    for x in range(G["N"]):
        vv = [vals[w] for w in succ[x]]
        if any(vj.cmp(a, vv[0]) != 0 for a in vv): bad += 1
    for qq in O:
        gv = VV[("g", qq)]; pe, pbe = VV[("pe", qq)], VV[("pbeta", qq)]
        if not vj.cmp(vals[pe], vals[pbe]) < 0: bad += 1
        lam, P, k = vals[gv]
        if lam != VV["cW"] or P or k != 5 * G["lev"][qq[0]] + 3: bad += 1
    c["fin"] = bad
    return c, len(fbs), F
if __name__ == "__main__":
    fam, seed, cnt, outf = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    done = set()
    if os.path.exists(outf): done = {ln.split()[1] for ln in open(outf) if ln.startswith("RUN ")}
    rng = random.Random(seed); fo = open(outf, "a")
    for i in range(cnt):
        G = gen(fam, rng); rid = f"{fam}_{seed}_{i}"
        if rid in done: continue
        res = []
        for mode in ("spec", "xi", "idx"):
            c, T, F = check(G, mode); res.append((mode, T, F, c))
        bad = [(m, {k: v for k, v in c.items() if v}) for m, T, F, c in res if any(c.values())]
        fo.write(f"RUN {rid} N {G['N']} M {sum(len(o) for o in G['opts'])} " + " ".join(f"{m}:T{T}/F{F}" for m, T, F, c in res) + (f" BAD {bad}" if bad else " ok") + "\n"); fo.flush()
        if bad: json.dump(G, open(os.path.join(os.path.dirname(outf), f"end_bad_{rid}.json"), "w"))
