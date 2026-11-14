#!/usr/bin/env python3
"""Box 212 RF-D DATA (L-NEW successor 74): N5 ITSELF (SPEC's root-first key; box190 n5v.py mode "spec" = box21 n5x.step) from S3 on
Gamma3(G), up to its first fallback, through box 208's level208.prep(G, g3=True) (which runs n5v.step in mode "xi"; this tool switches the
mode at import, RFD_MODE = spec (default) | xi | idx | seq; no file of box 190 / 208 is edited). Reference state: the last state T only.
Must-0 counters (rule-free; RF-A / RF-B on Gamma3, box 209's (K0')-(K4'), (L1')-(L3'), (L5') and PLATEAU3 (P1), (P2), (P4)):
  imp3   (unit steps): a step that changes no mover, changes a non-mover Even vertex, or moves a mover to a gate whose Xi_sigma value
         (n5v Engine's key) is not strictly above its current gate's                                           [hypothesis IMP3]
  monofail, k3fail, k4fail, einF, l3fail, phifail (level208.census, units there); phivals3 (unit genomes): more than P3 = 2M(N + 4M)
         values of Phi; p1, pclos, p3 (plat208.plateaus: (P1), (P2), (P4))
Descriptive (Howard-only facts, expected to fire under the key rule): k5fail, stallnocyc, p2 ((P3)), p4 ((P6)), p5 ((P7)); and T, phivals,
  stalls, plat, platmax, maxlen, tail (T - b'), tail_gt_nE (tail longer than the number of Even vertices), steps, movesum (mover switches).
Controls: RFD_CTRL=1 inverts imp3's comparison (must fire on every run with a step); LV_CTRL=2 (level208's: FRONT := the highest
  lagging class; l3fail must fire).
Usage: rfd212.py G.json ... | rfd212.py --rand SEED COUNT MODE (eg195.gen modes, as level208 --rand)"""
import sys, os, json, random, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "box208"))
import level208, plat208
import n5v
MODE = os.environ.get("RFD_MODE", "spec"); CTRL = os.environ.get("RFD_CTRL") == "1"; _orig = n5v.step; LOG = []
def _step(g, E, Ed, sigma, tau, mode):
    res = _orig(g, E, Ed, sigma, tau, MODE)
    if res is not None and not res[4]:
        vs, _ = E.evaluate(tuple(sigma)); LOG.append((list(sigma), list(res[0]), [E.key(v) for v in vs]))
    return res
n5v.step = _step
RULEFREE = ("imp3", "monofail", "k3fail", "k4fail", "einF", "l3fail", "phifail", "phivals3", "p1", "pclos", "p3")
DESC = ("k5fail", "stallnocyc", "p2", "p4", "p5", "T", "phivals", "stalls", "plat", "platmax", "maxlen", "tail", "tail_gt_nE", "steps", "movesum")
MAXK = ("T", "phivals", "platmax", "maxlen", "tail")

def one(G):
    del LOG[:]
    P = level208.prep(G, True); c = level208.census(P); pc = collections.Counter(); plat208.plateaus(P, pc)
    for k in ("p1", "pclos", "p2", "p3", "p4", "p5", "maxlen"): c[k] = pc[k]
    n, T, cls, owner, mv = P["n"], P["T"], P["cls"], P["owner"], set(P["movers"])
    N = G["N"]; M = sum(len(o) for o in G["opts"]); nE = sum(1 for v in range(n) if owner[v] == 0)
    if c["phivals"] > 2 * M * (N + 4 * M): c["phivals3"] = 1
    if len(LOG) != T: c["imp3"] += 1                       # the history and the logged steps must agree
    for sg, ns, key in LOG:
        ch = [v for v in range(n) if owner[v] == 0 and ns[v] != sg[v]]
        worse = (lambda v: key[ns[v]] >= key[sg[v]]) if CTRL else (lambda v: key[ns[v]] <= key[sg[v]])
        if not ch or any(v not in mv for v in ch) or any(worse(v) for v in ch): c["imp3"] += 1
        c["steps"] += 1; c["movesum"] += len(ch)
    bp = next(t for t in range(T + 1) if all(cls[t][x] == cls[T][x] for x in range(n)))
    c["tail"] = T - bp; c["tail_gt_nE"] = int(T - bp > nE)
    return c

def fmt(c):
    return "RULEFREE " + " ".join("%s %d" % (k, c[k]) for k in RULEFREE) + " DESC " + " ".join("%s %d" % (k, c[k]) for k in DESC)

if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--rand":
        import eg195
        seed, cnt, mode = int(a[1]), int(a[2]), a[3]; rng = random.Random(seed); g = 0; tot = collections.Counter()
        while g < cnt:
            G = eg195.gen(rng, mode)
            if G is None or G["N"] < 2: continue
            g += 1; c = one(G)
            for k in RULEFREE + DESC: tot[k] = max(tot[k], c[k]) if k in MAXK else tot[k] + c[k]
        print("rand", mode, "seed", seed, "genomes", g, "RFD_MODE", MODE, fmt(tot), flush=True)
    else:
        for fn in a:
            G = json.load(open(fn)); G = G.get("genome", G)
            print(os.path.basename(fn), "RFD_MODE", MODE, fmt(one(G)), flush=True)
