#!/usr/bin/env python3
"""L-SI box 68: Lemma COMPOSE check (docs/si/N5-REFUTE-box68.md §1).
Stack an ISO ladder K (levels 0..m') under an ISO ladder G (levels 0..m): the composite C has levels 0..m'+m; K's movers keep their
indices; G's level-l mover (l >= 1) becomes C's level-(m'+l) mover (R197 wiring: option k of a C level-(m'+1) mover W-points to K's
top mover 2m'+k, i.e. G's external bit is K's top bit b_(m')); G's Xi-targets stay inside G (shifted), K's inside K; G's
level-0 movers are dropped (C's level 0 is K's). Claim: for every start (k_s, g_s) and bit b_0 of C's frozen level 0:
  (i) C's run restricted to K's movers is K's flip-free run from k_s under b_0;
  (ii) C's run restricted to G's movers is G's E_m run from g_s under the external schedule beta(t) = b_(m')(K-part of s_t), the bit
       of the NEW state at each step (BIT-CHAIN), including the steps where only K moves.
Checks (all must be 0): KPART, GPART on random composites (all starts, both b_0) and on named pairs.  Usage: compose.py count seed"""
import sys, os, json, random, itertools, copy
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box64"))
from flipdp import Ext
from climb import rand_iso

def compose(K, G):
    mK, mG = max(K["lev"]), max(G["lev"]); NK = K["N"]; NG = G["N"]
    up = [v for v in range(NG) if G["lev"][v] > 0]              # G's upper movers 2..NG-1
    idx = {v: NK + i for i, v in enumerate(up)}                   # new indices
    N = NK + len(up); lev = list(K["lev"]) + [mK + G["lev"][v] for v in up]
    opts = [copy.deepcopy(o) for o in K["opts"]]; MK = len(K["br"]); br = list(K["br"]); bp = list(K["bp"]); gate = [list(g) for g in K["gate"]]
    M = MK; gb = len(br)
    for v in up:
        o2 = []
        for k, (wt, xt, mm) in enumerate(G["opts"][v]):
            l = lev[idx[v]]; nwt = 2 * (l - 1) + k               # R197 wiring
            nxt = idx[xt] if xt >= 0 else -1
            o2.append([nwt, nxt, M]); br.append(gb + G["br"][mm]); bp.append(G["bp"][mm]); M += 1
        opts.append(o2); gate.append([10000 + g for g in G["gate"][v]])
    order = list(K.get("xorder", range(NK))) + [idx[v] for v in G.get("xorder", range(NG)) if v in idx]
    # ranks: G's ranks are shifted above K's; rank ORDER inside each part is preserved, and no chain mixes the parts
    rk = sorted(range(M), key=lambda i: br[i]); br2 = [0] * M
    for r, i in enumerate(rk): br2[i] = r
    return {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br2, "bp": bp, "start": [0] * N, "xorder": order}, idx

def bits_top(E, G, st, mtop):
    b = int(E.gate[0][st[0]] < E.gate[1][st[1]])
    for l in range(1, mtop + 1):
        a, c = st[2 * l], st[2 * l + 1]
        b = b if (a, c) == (0, 1) else (1 - b) if (a, c) == (1, 0) else int(G["gate"][2 * l][a] < G["gate"][2 * l + 1][a])
    return b

def check(K, G):
    C, idx = compose(K, G); EC, EK, EG = Ext(C), Ext(K), Ext(G); mK = max(K["lev"]); bad = [0, 0]; global INK, ING, ENDK, ENDG
    upK = EK.UP; upG = EG.UP
    for ks in itertools.product(*[range(2) for _ in upK]):
        for gs in itertools.product(*[range(2) for _ in upG]):
            for b in (0, 1):
                u = tuple(ks) + tuple(gs); kc, gc = tuple(ks), tuple(gs)
                while True:
                    w = EC.step(u, b)
                    if w == u: break
                    nk = EK.step(kc, b)
                    if tuple(w[:len(upK)]) != nk: bad[0] += 1; INK[0] += 1; break
                    stC = EC.full(w, b); beta = bits_top(EC, C, stC, mK)
                    if os.environ.get("NEG"): beta = 1 - beta  # negative control: wrong schedule
                    ng = EG.step(gc, beta)
                    if tuple(w[len(upK):]) != ng: bad[1] += 1; ING[0] += 1; break
                    u, kc, gc = w, nk, ng
                else: pass
                # after C stops, K and G must both be stuck under the final schedule
                stC = EC.full(u, b); beta = bits_top(EC, C, stC, mK)
                if EK.step(kc, b) != kc: bad[0] += 1; ENDK[0] += 1
                if EG.step(gc, beta) != gc: bad[1] += 1; ENDG[0] += 1
    return bad

INK=[0]; ING=[0]; ENDK=[0]; ENDG=[0]
if __name__ == "__main__":
    cnt, seed = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed); tot = [0, 0]; done = 0
    while done < cnt:
        mK, mG = rng.choice([(1, 1), (1, 2), (2, 1), (2, 2)])
        try:
            K, G = rand_iso(mK + 1, rng), rand_iso(mG + 1, rng); Ext(K); Ext(G); b = check(K, G)
        except AssertionError: continue
        done += 1; tot[0] += b[0]; tot[1] += b[1]
    print("R2CHECK inK", INK[0], "inG", ING[0], "endK", ENDK[0], "endG", ENDG[0]); print("COMPOSE random pairs", cnt, "KPART", tot[0], "GPART", tot[1]); sys.exit(1 if sum(tot) else 0)
