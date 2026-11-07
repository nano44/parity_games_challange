#!/usr/bin/env python3
"""L-SI box 76: HIT structure. For mover y and step t, the old chain of y is (y, s_(t-1)(y)), (y1, s_(t-1)(y1)), ... ; the first hit
mover h_t(y) is the first mover of that chain (y included) that moves at t. Checks: HIT: R(y) == #{t : the old chain of y meets Mv_t}
(violations counted). DATA: max over (y, z) of H(y, z) := #{t : h_t(y) = z}; max of R(y) - |D*(y)| (D* = y and its strict
Xi-descendants); max of R(y) - N; per d max R; per d max over y of #{distinct first-hit movers}."""
import sys, os, itertools, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tw import load_corpus, is_lr, Sim, analyse
from tw2 import desc
C = collections.Counter(HIT_VIOL=0); R = collections.defaultdict(lambda: [-99, None])
def upd(k, v, w):
    if v > R[k][0]: R[k] = [v, w]
for path, G in load_corpus():
    if not is_lr(G): continue
    sim = Sim(G); N = G["N"]; d = N // 2; D, H = desc(G)
    for s0 in (itertools.product((0, 1), repeat=N) if N <= 10 else [tuple(G["start"])]):
        S = sim.run(s0); a = analyse(sim, S); T = a["T"]
        for y in range(N):
            Hc = collections.Counter(); Rc = 0; hits = 0
            for t in range(1, T + 1):
                if sim.val(S[t], y, S[t][y]) > sim.val(S[t - 1], y, S[t - 1][y]): Rc += 1
                x, k = y, S[t - 1][y]; h = None
                while True:
                    if x in a["Mv"][t]: h = x; break
                    nx = G["opts"][x][k][1]
                    if nx < 0: break
                    x, k = nx, S[t - 1][nx]
                if h is not None: hits += 1; Hc[h] += 1
            if hits != Rc: C["HIT_VIOL"] += 1
            w = (path, "".join(map(str, s0)), y, "R", Rc, "H", dict(Hc), "T", T)
            upd((d, "R"), Rc, w); upd((d, "maxH"), max(Hc.values() or [0]), w)
            upd((d, "R-|D*|"), Rc - 1 - len(D[y]), w); upd((d, "R-N"), Rc - N, w); upd((d, "#hitters"), len(Hc), w)
            C["pairs"] += 1
print("INFO", " ".join("%s %d" % kv for kv in sorted(C.items())))
for k in sorted(R): print(k, R[k][0], R[k][1])
