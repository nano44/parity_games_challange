#!/usr/bin/env python3
"""REFEREE successor 33: pre-read of L-NEW 72's box 209 (claude/l-new 311bbf81, docs/new/N5-LEVEL3-box209.md): own replay on HOW3(G).
Own code only: Gamma3(G) builder and HOW3 Howard run xicyc_replay.howard(G, pad=True) (successor 26; non-mover Even vertices frozen at
the standard state; tie rule: keep if best, else the larger index), VJ engine xicyc_vj; generators of box208_replay.py (successor 32).
No lane code imported; every counter is written from box 209's STATEMENTS (sections 2-5).
class_t(v) := (Lambda_t(v), E_t(v)); order: reward(Lambda), then the most relevant differing e-vertex.
Must-be-0 counters (unit):
 k0   (state, vertex outside the core)  Lambda = K1 XOR (K0 and K3 in Pi); K0 or K3 in Pi without the other; cW in Pi       (K0')
 k1   (step, vertex) class falls, or F1 fails;   k2  (pair of values of non-core vertices; same state, t / t+1, two random states)
      Omega <| or = Omega' but class > class'                                                                              (K1'), (K2')
 k3a  (state, vertex) Lambda(v) != Lambda(s(v));  k3c  class(v) != class(s(v)), v not an e-vertex;  k3d (state, e with mover successor w)
      class(e) != (Lambda(w), {e} + E(w)) or e in E(w);  k3e (state, vertex) a class of the eight core vertices, cW, cX, an e -> cW,
      its pad pe, or a pad pb differs from its class at state 0                                                            (K3'), (K0')
 k4   (state, gate) class(g) != min(class(pe_g), class(pbeta_g));  k5 (step, mover, m-pad) class_(t+1)(x) < class_t(y)     (K4'), (K5')
 LEVEL3, reference b (T3 and two random states), t < b with LAG nonempty:
 l1   (step) LAG grows; Phi falls; Phi equal at a non-stall; Phi or FRONT changes at a stall; (reference T3) non-stall steps != #Phi values
 l2   (state, vertex) FRONT holds a vertex that is not a mover, an m-pad, a gate, a pad pbeta or a beta with a mover successor
 l3   (state) neither (alpha) nor (beta);  l3v (state) (alpha) with m != class_b(sigma_t(z)), or (beta) with m != (c, {}) or c not a beta
 l4   (stall, FRONT vertex) the map s leaves FRONT, or a gate's sbar_t is not pbeta_g;  l4c (stall) no cycle x_1 .. x_r as in (L4')
 l5   (reference) more than 2M(N + 4M) values of Phi; or m outside {class_b(m-pad)} + {(c, {})}
 c4   (reference) after LAG is empty a class changes
 PLATEAU3, every maximal interval [u, v], u < v, of constant Phi (three references):
 p1 (state, vertex) {class_s <= m} != Y or a vertex of Y changes class;  p2 (state, vertex of Y) its successor is outside Y
 p3 (state, mover of Y, m-pad) class_s(pad) > class_s(mover), or the pad or its gate is outside Y
 p4 (state, Odd vertex of Y) sbar_s != sbar_u or outside Y;  p4c (plateau, gate of Y with both faces in Y and equal classes) sbar != pe_g
 p5v (state, vertex of Y) its value in the one-player game H (own VJ on H) differs from Omega_s
 p5h (step, mover of Y) the step s -> s+1, u <= s <= v, is not a legal Howard step of H on H's values;  p6 (step) it switches no mover of Y
 p7 (plateau) v - u > the Even vertices of Y, or > N + 6M + 9
 TAIL (reference T3, b' the first state with LAG empty): t1 (Odd vertex, step of [b', T3]) sbar changes;  t2 (genome) T3 - b' > N + 6M + 9
 tb (genome) T3 > P3 (n_E3 + 1) + n_E3;  nE (genome) the number of Even vertices of Gamma3 != N + 6M + 9, or n != N + 7M + 10
Controls (must fire): c_k4 (max for min), c_k5 (no time shift), ch1..ch5 (FRONT := the highest lagging class), c_Y (Y := FRONT only),
 c_l3v ((alpha) against the class at b of the mover z itself instead of sigma_t(z)).
usage: box209_replay.py files G.json ... | gen FAMILY SEED COUNT | mut SEED COUNT MAXMUT G.json ..."""
import sys, os, json, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xicyc_replay import howard
from xicyc_vj import VJ
import end_replay
from box208_replay import Ctr, mutate, own_gen


def one(name, G, c, rng, verbose=True):
    E, lab, ties, states, movers, idx = howard(G, True, cap=20000); assert len(lab) < 20000
    T = len(states) - 1; n = E.n; N = G["N"]; M = sum(len(o) for o in G["opts"]); inv = {v: k for k, v in idx.items()}
    kind = [None] * n
    for k, v in idx.items(): kind[v] = k[0] if isinstance(k, tuple) else k
    isE = [kind[v] == "e" for v in range(n)]; evs = [v for v in range(n) if isE[v]]; gates = [v for v in range(n) if kind[v] == "g"]
    mset = set(movers); K = [idx[("K", i)] for i in range(4)]; core = set(K) | {idx[k] for k in ("pA", "s", "q", "r")}; cW, cX = idx["cW"], idx["cX"]
    face = {g: (idx[("pe", inv[g][1])], idx[("pbeta", inv[g][1])]) for g in gates}
    mpads = [v for v in range(n) if kind[v] == "m"]
    e_to_cW = [e for e in evs if E.succ[e] == [cW]]
    const = sorted(core) + [cW, cX] + e_to_cW + [idx[("pe", inv[e][1])] for e in e_to_cW] + [v for v in range(n) if kind[v] == "pb"]
    nE3 = N + 6 * M + 9; P3 = 2 * M * (N + 4 * M)
    if sum(1 for v in range(n) if E.owner[v] == 0) != nE3 or n != N + 7 * M + 10: c.inc("nE")
    def cls(val_v):
        return (E.reward(val_v[0]), tuple(sorted((E.rk[u] for u in val_v[1] if isE[u]), reverse=True)))
    CL = [[cls(val[v]) for v in range(n)] for (_, _, val) in states]
    ST = [st for (_, st, _) in states]; VAL = [val for (_, _, val) in states]
    c.inc("genomes"); c.inc("states", T + 1); c.mx("maxT", T)
    if T > P3 * (nE3 + 1) + nE3: c.inc("tb")
    nc = [v for v in range(n) if v not in core]
    for t in range(T + 1):
        st, val, cl = ST[t], VAL[t], CL[t]
        for v in nc:
            lamK1 = val[v][0] == K[1]; k0in, k3in = K[0] in val[v][1], K[3] in val[v][1]
            if k0in != k3in or lamK1 != k0in or cW in val[v][1]: c.inc("k0")
        for v in range(n):
            w = st[v]
            if val[v][0] != val[w][0]: c.inc("k3a")
            if not isE[v] and cl[v] != cl[w]: c.inc("k3c")
        for e in evs:
            w = E.succ[e][0]
            if w in mset:
                want = (cl[w][0], tuple(sorted(cl[w][1] + (E.rk[e],), reverse=True)))
                if cl[e] != want or E.rk[e] in cl[w][1]: c.inc("k3d")
        for v in const:
            if cl[v] != CL[0][v]: c.inc("k3e")
        for g in gates:
            a, b = face[g]
            if cl[g] != min(cl[a], cl[b]): c.inc("k4")
            if cl[g] != max(cl[a], cl[b]): c.inc("c_k4")
        pairs = [(v, w) for v in nc for w in nc] if len(nc) <= 50 else [(rng.choice(nc), rng.choice(nc)) for _ in range(1200)]
        for (v, w) in pairs:
            if E.cmp(val[v], val[w]) <= 0 and cl[v] > cl[w]: c.inc("k2")
        t2 = rng.randint(0, T)                                         # (K2') «at two states»
        for _ in range(200):
            v, w = rng.choice(nc), rng.choice(nc)
            if E.cmp(val[v], VAL[t2][w]) <= 0 and cl[v] > CL[t2][w]: c.inc("k2")
        if t < T:
            nval, ncl = VAL[t + 1], CL[t + 1]
            for v in range(n):
                if ncl[v] < cl[v]: c.inc("k1")
                if v not in core and E.cmp(val[v], nval[v]) <= 0 and cl[v] > ncl[v]: c.inc("k2")
                if E.cmp(val[v], nval[v]) > 0: c.inc("k1")
            for x in movers:
                for y in E.succ[x]:
                    if ncl[x] < cl[y]: c.inc("k5")
                    if cl[x] < cl[y]: c.inc("c_k5")
    def cycles(st):
        seen = [0] * n; out = []
        for v0 in range(n):
            if seen[v0]: continue
            path = []; v = v0
            while not seen[v]:
                seen[v] = 1; path.append(v); v = st[v]
            if v in path: out.append(path[path.index(v):])
        return out
    CYC = [cycles(ST[t]) for t in range(T + 1)]
    FK = ("x", "m", "g", "pbeta")
    def infront(v): return kind[v] in FK or (kind[v] == "b" and E.succ[v][0] in mset)
    def level(b, ctrl_hi=False):
        clb = CL[b]; mp_cls = {clb[y] for y in mpads}; phis = []; stalls = []; tag = "ch" if ctrl_hi else "l"
        prevLAG = prevPhi = prevFRONT = prevStall = None; bprime = None
        for t in range(0, b + 1):
            cl = CL[t]; LAG = [v for v in range(n) if cl[v] != clb[v]]
            if prevLAG is not None and not set(LAG) <= prevLAG: c.inc(tag + "1")
            if not LAG:
                if prevLAG and prevStall: c.inc(tag + "1")
                bprime = t; break
            m = (max if ctrl_hi else min)(cl[v] for v in LAG); FRONT = [v for v in LAG if cl[v] == m]; Fs = set(FRONT); Ls = set(LAG)
            Phi = (m, -len(FRONT))
            if prevPhi is not None:
                if prevStall and (Phi != prevPhi or Fs != prevFRONT): c.inc(tag + "1")
                if not prevStall and not Phi > prevPhi: c.inc(tag + "1")
            for v in FRONT:
                if not infront(v): c.inc(tag + "2")
            st = ST[t]; alpha = [z for z in FRONT if kind[z] == "x" and st[z] not in Ls]
            beta = [cy for cy in CYC[t] if all(v in Fs for v in cy)]
            if not alpha and not beta: c.inc(tag + "3")
            if not ctrl_hi:
                if alpha: c.inc("n_alpha")
                if beta: c.inc("n_beta")
            bad = any(m != clb[st[z]] for z in alpha)
            if not ctrl_hi and any(m != clb[z] for z in alpha): c.inc("c_l3v")   # control: the class at b of the mover itself
            for cy in beta:
                cnode = VAL[t][cy[0]][0]
                if m != (E.reward(cnode), ()) or kind[cnode] != "b": bad = True
            if bad: c.inc(tag + "3v")
            if m not in mp_cls and not (m[1] == () and beta): c.inc(tag + "5")
            phis.append(Phi)
            stall = None
            if t < b:
                ncl = CL[t + 1]; stall = all(ncl[v] == cl[v] for v in FRONT)
                if stall:
                    stb = ST[b]; smap = {}
                    for v in FRONT:
                        if kind[v] == "x": w = stb[v]; ok = w in Fs
                        elif kind[v] == "g": w = st[v]; ok = w in Fs and w == face[v][1]
                        elif kind[v] in ("m", "pbeta", "b"): w = E.succ[v][0]; ok = w in Fs
                        else: w = None; ok = False
                        smap[v] = w
                        if not ok: c.inc(tag + "4")
                    # (L4'): a cycle of s through a mover, of the shape mover -> m-pad -> gate -> pbeta -> beta -> mover
                    found = False
                    for x in [v for v in FRONT if kind[v] == "x"]:
                        v = x; seen = set(); okc = True
                        while v not in seen and v is not None and v in Fs: seen.add(v); v = smap.get(v)
                        if v == x:
                            cyc = []; v = x
                            while True:
                                cyc.append(kind[v]); v = smap[v]
                                if v == x: break
                            if len(cyc) % 5 == 0 and all(cyc[i:i + 5] == ["x", "m", "g", "pbeta", "b"] for i in range(0, len(cyc), 5)): found = True; break
                    if not found: c.inc(tag + "4c")
                stalls.append((t, stall, m, Fs))
            prevLAG, prevPhi, prevFRONT, prevStall = Ls, Phi, Fs, stall
        if bprime is None: bprime = b + 1
        if len(set(phis)) > P3: c.inc(tag + "5")
        plats = []; i = 0
        while i < len(stalls):
            if stalls[i][1]:
                j = i
                while j + 1 < len(stalls) and stalls[j + 1][1]: j += 1
                plats.append((stalls[i][0], stalls[j][0] + 1, stalls[i][2], stalls[i][3])); i = j + 1
            else: i += 1
        return bprime, stalls, plats, len(set(phis))
    def hgame(Y, u):
        loc = {x: i for i, x in enumerate(Y)}
        hsucc = [[loc[y] for y in E.succ[x]] if kind[x] == "x" else [loc[ST[u][x]]] for x in Y]
        return loc, hsucc, VJ([E.prio[x] for x in Y], [0 if kind[x] == "x" else E.owner[x] for x in Y], hsucc)
    def hsteps(Y, u, v, loc, hsucc, H, lastmustmove):
        hv = []
        for s in range(u, min(v + 1, T) + 1):
            hst = [loc.get(ST[s][x], None) if kind[x] == "x" else hsucc[i][0] for i, x in enumerate(Y)]
            if any(w is None for w in hst): c.inc("p5v"); return
            val = H.values(hst); hv.append((hst, val))
            if s <= v:
                for i, x in enumerate(Y):
                    g = VAL[s][x]
                    if g[0] not in loc or any(w not in loc for w in g[1]) or val[i] != (loc[g[0]], frozenset(loc[w] for w in g[1]), g[2]): c.inc("p5v")
        for j in range(len(hv) - 1):
            (stA, vA), (stB, vB) = hv[j], hv[j + 1]; moved = False
            for i, x in enumerate(Y):
                if kind[x] != "x": continue
                cur, new = stA[i], stB[i]; best = cur
                for w in hsucc[i]:
                    if H.cmp(vA[w], vA[best]) > 0: best = w
                B = [w for w in hsucc[i] if H.cmp(vA[w], vA[best]) == 0]
                if not ((new == cur) if cur in B else (new in B)): c.inc("p5h")
                moved |= new != cur
            if not moved: c.inc("p6")
    def plateau(u, v, m, J, ctrl=False):
        Y = [x for x in range(n) if CL[u][x] <= m] if not ctrl else sorted(J)
        Ys = set(Y)
        for s in range(u, v + 1):
            cl = CL[s]; st = ST[s]
            if not ctrl:
                for x in range(n):
                    if (cl[x] <= m) != (x in Ys) or (x in Ys and cl[x] != CL[u][x]): c.inc("p1")
            for x in Y:
                if st[x] not in Ys: c.inc("p2" if not ctrl else "c_Y")
            if ctrl: continue
            for x in Y:
                if kind[x] == "x":
                    for y in E.succ[x]:
                        if cl[y] > cl[x] or y not in Ys or E.succ[y][0] not in Ys: c.inc("p3")
                if E.owner[x] == 1 and (st[x] != ST[u][x] or st[x] not in Ys): c.inc("p4")
        if ctrl: return
        for g in gates:
            if g in Ys and face[g][0] in Ys and face[g][1] in Ys and CL[u][face[g][0]] == CL[u][face[g][1]]:
                c.inc("n_p4case3")
                if any(ST[s][g] != face[g][0] for s in range(u, v + 1)): c.inc("p4c")
        try: loc, hsucc, H = hgame(Y, u)
        except KeyError:
            c.inc("p5v"); return
        hsteps(Y, u, v, loc, hsucc, H, True)
        ne = sum(1 for x in Y if E.owner[x] == 0); nm = sum(1 for x in Y if kind[x] == "x")
        if v - u > ne or v - u > nE3: c.inc("p7")
        c.inc("plateaus"); c.mx("maxplat", v - u); c.mx("maxplat_pct_movers", (100 * (v - u)) // max(nm, 1))
    refs = [T] + ([rng.randint(1, T), rng.randint(1, T)] if T >= 2 else [])
    for ri, b in enumerate(refs):
        bp, stalls, plats, nphi = level(b)
        if not all(CL[t] == CL[b] for t in range(bp, b + 1)): c.inc("c4")
        if ri == 0:
            c.mx("maxPhi", nphi); c.inc("stalls", sum(1 for s in stalls if s[1]))
            if sum(1 for s in stalls if s[0] < bp and not s[1]) != nphi: c.inc("l1")
            c.mx("maxtail", T - bp)
            if T - bp > nE3: c.inc("t2")
            for s in range(bp, T):
                for x in range(n):
                    if E.owner[x] == 1 and ST[s + 1][x] != ST[s][x]: c.inc("t1")
            if bp < T:                                                   # PLATEAU3 (ii): the tail as a Howard run of H := all of Gamma3
                Yall = list(range(n)); loc, hsucc, H = hgame(Yall, bp); hsteps(Yall, bp, T - 1, loc, hsucc, H, True)
        for (u, v, m, J) in plats:
            plateau(u, v, m, J)
            if ri == 0: plateau(u, v, m, J, ctrl=True)
        if ri == 0 and T >= 1: level(b, ctrl_hi=True)
    if verbose: print("%-22s N %3d M %3d n %4d T3 %3d ties %d" % (name, N, M, n, T, ties))


MUST0 = ["k0", "k1", "k2", "k3a", "k3c", "k3d", "k3e", "k4", "k5", "l1", "l2", "l3", "l3v", "l4", "l4c", "l5", "c4", "p1", "p2", "p3", "p4", "p4c",
         "p5v", "p5h", "p6", "p7", "t1", "t2", "tb", "nE"]
REC = ["genomes", "states", "maxT", "maxPhi", "stalls", "plateaus", "maxplat", "maxplat_pct_movers", "maxtail", "n_alpha", "n_beta", "n_p4case3",
       "c_k4", "c_k5", "ch1", "ch2", "ch3", "ch3v", "ch4", "ch4c", "ch5", "c_Y", "c_l3v"]


def main():
    mode = sys.argv[1]; c = Ctr(); rng = random.Random(3209)
    if mode == "files":
        for fn in sys.argv[2:]: one(os.path.basename(fn)[:-5], json.load(open(fn)), c, rng)
    elif mode == "gen":
        fam, seed, count = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]); g = random.Random(seed)
        for i in range(count): one("%s_%d" % (fam, i), (own_gen(g, fam) if fam in ("tiny", "noX", "big") else end_replay.gen(g, fam)), c, rng, verbose=False)
        print("family %s seed %d count %d" % (fam, seed, count))
    else:
        seed, count, maxmut = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]); g = random.Random(seed)
        for fn in sys.argv[5:]:
            G0 = json.load(open(fn))
            for i in range(count): one("mut", mutate(G0, g, g.randint(1, maxmut)), c, rng, verbose=False)
        print("mutants: seed %d, %d per base, 1..%d mutations, bases %s" % (seed, count, maxmut, " ".join(os.path.basename(f)[:-5] for f in sys.argv[5:])))
    print("MUST-0:  " + "  ".join("%s %d" % (k, c.get(k, 0)) for k in MUST0))
    print("RECORDS: " + "  ".join("%s %d" % (k, c.get(k, 0)) for k in REC))


if __name__ == "__main__":
    main()
