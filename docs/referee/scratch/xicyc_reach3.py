"""REFEREE successor 26: REACH3-CYC replay. For each genome: (1) my Gamma3 builder (xicyc_replay.build, pad=True) equals the lane's
gamma3.build(G, PADS) (prio, owner, successor sets, start); (2) the lane's N5'-xi (box190 n5v.run(g, 'xi')) from S3: states up to the
first fallback; (3) my own Howard run on IDEAL-CYC(Gamma3) (own VJ engine): mover sequences compared state for state, standard states,
fallback index. Usage: xicyc_reach3.py LNEW_ROOT files.json... | LNEW_ROOT random COUNT SEED"""
import sys, os, json, random
R = sys.argv[1]; sys.path[:0] = [os.path.dirname(os.path.abspath(__file__)), os.path.join(R, "experiments/new/box190"),
    os.path.join(R, "experiments/new/box189"), os.path.join(R, "experiments/new/box191"), os.path.join(R, "experiments/harness")]
import n5v, gamma3, rand191
from xicyc_replay import build, howard
PADS = {"K", "pe", "pb", "m"}
def one(G, name):
    g, sig0, tau0, V = gamma3.build(G, PADS); prio, own, fs, sig, movers, idx, succ = build(G, True)
    same = (list(g.prio) == prio and list(g.owner) == own and all(sorted(g.succ[v]) == sorted(succ[v]) for v in range(g.n))
            and all(sig0[v] == sig[v] for v in sig0 if g.owner[v] == 0))
    E5, Ed5 = n5v.Engine(g), n5v.Engine(n5v.dual(g)); sg, ta5 = n5v.n5x.start_pair(g, E5, Ed5, None)
    states = [(tuple(sg), tuple(ta5))]; fbs = []
    while len(states) < 5000:
        r = n5v.step(g, E5, Ed5, sg, ta5, "xi")
        if r is None: break
        sg, ta5, _, _, fb = r; fbs.append(fb); states.append((tuple(sg), tuple(ta5)))
        if fb: break
    s0, t0 = states[0]; xi = []; std = True; fb_at = None
    for t, (s, ta) in enumerate(states):
        if t > 0 and fbs[t - 1]: fb_at = t; break
        std &= all(s[v] == s0[v] for v in range(g.n) if g.owner[v] == 0 and v not in movers) and list(ta) == list(t0)
        xi.append(tuple(s[x] for x in movers))
    E, lab, ties, hst, mv, _ = howard(G, True); mine = [tuple(st[0][x] for x in movers) for st in hst]
    # tie-free check: every N5'-xi mover step is a Howard step under MY values on IDEAL-CYC(Gamma3), and the stop is the first state
    # with no strictly better mover successor
    hw = True; base = [sig.get(v) for v in range(E.n)]
    for t in range(len(xi)):
        cur = list(base)
        for i, x in enumerate(movers): cur[x] = xi[t][i]
        _, val = E.best_reply(cur)
        imp = [x for x in movers if any(E.cmp(val[w], val[cur[x]]) > 0 for w in E.succ[x])]
        if t == len(xi) - 1: hw &= not imp; break
        hw &= bool(imp)
        for i, x in enumerate(movers):
            y = xi[t + 1][i]; isbest = all(E.cmp(val[y], val[w]) >= 0 for w in E.succ[x])
            hw &= isbest and (y == cur[x] or E.cmp(val[y], val[cur[x]]) > 0)
    ok = same and std and hw and fb_at == len(xi)
    pm = max((len(r) for r in lab.replace("R", "C").split("C")), default=0); ok = ok and pm <= G["N"]
    print(name, "N", G["N"], "max p-run", pm, "builder-equal", same, "N5'-xi standard", std, "T3(xi)", len(xi) - 1, "T3(own Howard)", len(mine) - 1, "first fallback at transition",
          fb_at, "Howard ties", ties, "labels", lab, "xi-steps-are-Howard", hw, "xi==own-tie-rule", xi == mine, "OK" if ok else "FAIL")
    return ok, len(mine) - 1
if sys.argv[2] == "random":
    cnt, seed = int(sys.argv[3]), int(sys.argv[4]); rng = random.Random(seed); good = trans = 0
    for i in range(cnt):
        G = rand191.rgen(rng, rng.randint(1, 5), rng.randint(1, 3), rng.randint(2, 3)); ok, T = one(G, f"rand{seed}#{i}"); good += ok; trans += T
    print(f"random {cnt} seed {seed}: MATCH {good}/{cnt}; mover-phase transitions {trans}")
else:
    for f in sys.argv[2:]: one(json.load(open(f)), os.path.basename(f))
