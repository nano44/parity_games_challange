#!/usr/bin/env python3
"""L-NEW box 70: L-SI's re-entry classes (P-N5-CUT-box43.md §3-§4, l-si 2678f6c6) re-implemented from the packet text, with the
anatomy of the S (W-silent) and C (own-cycle) re-entries. Plain N5 (box21/n5x.step), S3 start or START file.
Re-entry j-1 -> j of v into c inside a lambda-run R (lambda = Xi's cycle-node map), after the leave s -> s+1 of c (sigma_s(v) = c !=
sigma_{s+1}(v)). F: the re-entry is an Even S4c fallback. Else tau* := tau_{j-1}, [a, b] the tau*-piece containing j-1 (maximal run of
states with tau = tau* joined by S4a steps), W* := val(sigma, tau*) on G_tau*. Anchor q: max(s, a) <= q-1 <= j-2, (v, c) in H_{q-1} =
sigma_{q-1} u I_sigma_{q-1}. FR: no anchor. C: anchor (smallest q) and v its own W*-cycle node at some state of [q, j]. P: W*(c) changes on
[q, j]. S: the rest. Per S re-entry also records: LEAVE-TIE (W*_{s'+1}(sigma_{s'+1} v) = W*_{s'+1}(c) at the leave, if s' := s lies in
the piece), OUT-SUCC (v's successors on the window [q, j]), and whether the transition j-1 -> j changes W* anywhere (WFLAT).
Output: class totals, max per (lambda-run, edge) of S and of C, max over lambda-runs of sum over edges of S + C (= SC* of the run).
Usage: silent.py GAME.pg [START] [--verbose]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
from collections import Counter
args = [a for a in sys.argv[1:] if not a.startswith("--")]; VERB = "--verbose" in sys.argv
g = load(args[0]); n = g.n
start = readstart(args[1]) if len(args) > 1 else None
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start)
S = [tuple(s)]; TAU = [tuple(t)]; FB = []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    ns, nt, _, _, fb, _, _ = r; S.append(tuple(ns)); TAU.append(tuple(nt)); FB.append(fb)
T = len(S) - 1
XI = [E.evaluate(x)[0] for x in S]; LX = [tuple(v[0] for v in x) for x in XI]
IMP = [set(E.improving(S[k], XI[k])) for k in range(T + 1)]
Wc = {}
def Wv(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(g.owner), [[tau[v]] if g.owner[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
s4a = [S[k + 1] != S[k] and not FB[k] for k in range(T)]
lam = [0] * (T + 1)
for k in range(1, T + 1): lam[k] = lam[k - 1] + (LX[k] != LX[k - 1])
def piece_start(j1, tau):
    a = j1
    while a > 0 and TAU[a - 1] == tau and s4a[a - 1]: a -= 1
    return a
C = Counter(); per = Counter(); runsum = Counter(); info = []; perpiece = Counter(); flatS = 0; Sn = 0
ev = [v for v in range(n) if g.owner[v] == 0]
for v in ev:
    leaves = {}                                   # c -> state s of v's latest leave of c (s -> s+1)
    for k in range(T):
        if S[k][v] == S[k + 1][v]: continue
        c, j = S[k + 1][v], k + 1
        if c in leaves and lam[leaves[c]] == lam[j]:
            s_ = leaves[c]
            if FB[k]: cls = "F"
            else:
                tau = TAU[j - 1]; a = piece_start(j - 1, tau)
                q = next((q for q in range(max(s_, a) + 1, j) if S[q - 1][v] == c or (v, c) in IMP[q - 1]), None)
                if q is None: cls = "FR"
                else:
                    W = {x: Wv(x, tau) for x in range(q, j + 1)}
                    if any(W[x][v][0] == v for x in range(q, j + 1)): cls = "C"
                    elif len({W[x][c] for x in range(q, j + 1)}) > 1: cls = "P"
                    else:
                        cls = "S"; perpiece[(a, v, c)] += 1
                        succs = sorted({S[x][v] for x in range(q, j)})
                        wflat = Wv(j - 1, tau) == Wv(j, tau); flatS += wflat; Sn += 1
                        info.append((v, c, s_, q, j, succs, wflat, [XI[x][v] != Wv(x, tau)[v] for x in (j - 1, j)]))
            C[cls] += 1
            if cls in ("S", "C"): per[(lam[j], v, c, cls)] += 1; runsum[lam[j]] += 1
        leaves[S[k][v]] = k

# GXC events (box 70 Lemma SIL-Z / Corollary GXC): (v, t) with v Even, sigma_{t+1}(v) != sigma_t(v), tau_{t+1} = tau_t, v in Z_t and Z_{t+1},
# Xi_{t+1}(v) > Xi_t(v) strictly and W_{t+1}(v) <= W_t(v) (W read with tau_t). Per lambda-run maximum; every S re-entry must be one.
GX = set(); gxrun = Counter()
for k in range(T):
    if TAU[k + 1] != TAU[k] or lam[k + 1] != lam[k]: continue
    w0, w1 = Wv(k, TAU[k]), Wv(k + 1, TAU[k]); Ek = Wc[TAU[k]]
    for v in ev:
        if S[k][v] == S[k + 1][v]: continue
        if XI[k][v] != w0[v] and E.key(XI[k + 1][v]) > E.key(XI[k][v]) and not Ek.key(w1[v]) > Ek.key(w0[v]):
            GX.add((v, k)); gxrun[lam[k]] += 1
SnotG = sum(1 for x in info if (x[0], x[4] - 1) not in GX)
mx = lambda cl: max([x for (l, v, c, k), x in per.items() if k == cl] or [0])
print(f"SILENT {os.path.basename(args[0])} n {n} iters {T} classes {dict(C)} max-S-per-edge {mx('S')} max-C-per-edge {mx('C')} "
      f"SCrun {max(runsum.values()) if runsum else 0} max-S-per-piece-edge {max(perpiece.values()) if perpiece else 0} S-at-Wflat {flatS}/{Sn} GXCrun {max(gxrun.values()) if gxrun else 0} S-not-GXC {SnotG}")
if VERB:
    for x in info: print("  S v %d c %d leave %d anchor %d reentry %d succ %s Wflat %s inZ(j-1,j) %s" % x)
