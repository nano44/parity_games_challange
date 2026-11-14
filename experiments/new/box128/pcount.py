#!/usr/bin/env python3
"""L-NEW box 128 PORTAL-COUNT: which Even moves inside a TWO-FIX window are W-strict, and what pays for each.
Windows, G_F, classes, prefixes, ZC and NR exactly as L-RED R173 portalck.py (claude/l-red 02119133, read-only; windows / frozen from
experiments/red/r170/freeze.py). A STRETCH := a maximal run of window states with no S4c fallback on its transitions.
For an Even move of h at transition j (state j-1 -> j) from o to w: W-strict iff key(W_j(w)) > key(W_j(o)) (W_j := val(sigma_j, tau));
FLAT iff equal; WORSE iff smaller (S4a picks the arena optimum, so WORSE must be 0). Kinds, relative to h's previous move in the stretch:
  FIRST  : h's first move in the stretch;
  SAME   : cls(o) = cls(w) = X != None (a PORTAL pair); split by premises ZC / NR (premised SAME strict moves contradict PORTAL: PVIOL);
  DIFF   : cls(o) != cls(w) (or one is None); RET := DIFF into a class h already occupied earlier in the same stretch (class return).
Per stretch and h: STRICT_h and B_h := 1 + DIFF_h + (SAME_h without ZC and NR); PORTAL gives STRICT_h <= B_h (BVIOL counts failures).
Also: LAMXI := changes of the cycle node of Xi_t(X) at branching X inside windows (ZC stretches at X = 1 + changes), NB := branching
vertices of G_F; MAXSTRICT_h, MAXDIFF_h, MAXRET_h per (stretch, h).
CORNER: moves where the old or new option's W_j-play runs through h (the VJ comparison corner: WORSE can only occur there,
WORSE_NOCORNER must be 0). STATIC-TIE (lane lemma): a non-first strict move whose two options keep their Xi values on [j1-1, j2-1] and W
values on [j1, j2] contradicts the lemma unless an option's W-play at j1 or j2 runs through h (STATVIOL must be 0; STATCORNER counted).
PAID_XI: non-first strict moves where Xi of an option changes inside [j1-1, j2-1]; PAID_WONLY: only W of an option changes.
LEADVIOL: (stretch, h) with STRICT_h > LC_h := sum over the classes X of h's successors of (1 + changes of the Xi-cycle node of X in the
stretch) (+1 if some successor has no class): the Lead's proposed (#X) x (#ZC stretches) count, per h; MAXEXCESS := max STRICT_h - LC_h.
ENT: per (stretch, h), entries into each class; MULTI := classes entered >= 2 times (MAXMULTI max, MULTI2 = (stretch, h) with >= 2 such
classes); DEGVIOL: STRICT_h > 2 deg(h) - 1; MAXRATIO := max STRICT_h / deg(h).
Usage: pcount.py G.pg [START|-]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "red", "r170")); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, start_pair, readstart, Engine, dual
import pg
from freeze import run, windows, frozen

def play(succ1, x, cap):
    s = set(); v = x
    while v not in s and len(s) <= cap:
        s.add(v); v = succ1[v]
    return s

g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
E0, Ed0 = Engine(g), Engine(dual(g)); s, t = start_pair(g, E0, Ed0, st)
S, T, F, E = run(g, s, t); W, SB = windows(g, S, T, E)
n, own, pr = g.n, g.owner, g.prio
tot = dict(win=0, stretches=0, moves=0, strict=0, flat=0, worse=0, first=0, same=0, samezcnr=0, pviol=0, diff=0, ret=0, strictdiff=0,
           strictret=0, strictsame_nozc=0, strictsame_nonr=0, bviol=0, maxstrict=0, maxdiff=0, maxret=0, lamxi=0, nbsum=0, maxwinstrict=0, corner=0, worse_nocorner=0, statviol=0, statcorner=0, paid_xi=0, paid_wonly=0, leadviol=0, maxexcess=-10**9, maxmulti=0, multi2=0, degviol=0, maxratio=0)
for a, b in W:
    if b - a < 1: continue
    tot["win"] += 1
    gf = frozen(g, SB[a], T[a]); tau = T[a]; sb = SB[a]
    gw = pg.Game(list(pr), list(own), [list(g.succ[v]) if own[v] == 0 else [tau[v]] for v in range(n)])
    gx = pg.Game(list(pr), list(own), [list(g.succ[v]) if own[v] == 0 else [sb[v]] for v in range(n)])
    EW, EX = Engine(gw), Engine(gx)
    WV = {j: EW.evaluate(tuple(S[j][v] if own[v] == 0 else -1 for v in range(n)))[0] for j in range(a, b + 1)}
    XV = {j: EX.evaluate(tuple(S[j][v] if own[v] == 0 else -1 for v in range(n)))[0] for j in range(a, b + 1)}
    br = [v for v in range(n) if len(gf.succ[v]) > 1]; tot["nbsum"] += len(br)
    tot["lamxi"] += sum(XV[j][X][0] != XV[j + 1][X][0] for X in br for j in range(a, b))
    def cls(h, x):
        v, seen = x, {h}
        while len(gf.succ[v]) == 1:
            if v in seen: return None
            seen.add(v); v = gf.succ[v][0]
        return None if v in seen else v
    def prefix(h, x):
        v, seen = x, set()
        while len(gf.succ[v]) == 1 and v not in seen and v != h:
            seen.add(v); v = gf.succ[v][0]
        return seen
    def s1(j, world):
        return [S[j][v] if own[v] == 0 else (tau[v] if world == "W" else sb[v]) for v in range(n)]
    # stretches: maximal [p, q] in [a, b] with F[j] = 0 for j in p+1..q
    st_ = []; p = a
    for j in range(a + 1, b + 1):
        if F[j]: st_.append((p, j - 1)); p = j
    st_.append((p, b))
    winstrict = 0
    for p, q in st_:
        if q - p < 1: continue
        tot["stretches"] += 1
        mv = {}
        for j in range(p + 1, q + 1):
            for h in range(n):
                if own[h] == 0 and S[j][h] != S[j - 1][h]: mv.setdefault(h, []).append((j, S[j - 1][h], S[j][h]))
        for h, L in mv.items():
            strict = diff = ret = bad = 0; occ = [cls(h, L[0][1])]
            for r, (j, o, w) in enumerate(L):
                tot["moves"] += 1
                ko, kw = EW.key(WV[j][o]), EW.key(WV[j][w])
                corner = h in play(s1(j, "W"), o, n) or h in play(s1(j, "W"), w, n)
                tot["corner"] += corner; tot["worse_nocorner"] += kw < ko and not corner
                isst = kw > ko; tot["strict"] += isst; tot["flat"] += kw == ko; tot["worse"] += kw < ko; strict += isst
                if r > 0 and isst:
                    j1 = L[r - 1][0]
                    stat = all(XV[k][o] == XV[j1 - 1][o] and XV[k][w] == XV[j1 - 1][w] for k in range(j1 - 1, j)) and \
                           all(WV[k][o] == WV[j1][o] and WV[k][w] == WV[j1][w] for k in range(j1, j + 1))
                    c1 = any(h in play(s1(k, "W"), x, n) for k in (j1, j) for x in (o, w))
                    tot["statviol"] += stat and not c1; tot["statcorner"] += stat and c1
                    xch = any(XV[k][x] != XV[k + 1][x] for k in range(j1 - 1, j - 1) for x in (o, w))
                    tot["paid_xi"] += xch; tot["paid_wonly"] += (not xch) and not stat
                co, cw = cls(h, o), cls(h, w)
                if r == 0:
                    tot["first"] += 1
                elif co is not None and co == cw:
                    j1 = L[r - 1][0]; X = co; tot["same"] += 1
                    zc = len({XV[k][X][0] for k in range(j1 - 1, j)}) == 1
                    pre = {h} | prefix(h, o) | prefix(h, w)
                    nr = all(not (pre & play(s1(k, "X"), X, n)) for k in range(j1 - 1, j)) and \
                         all(not (pre & play(s1(k, "W"), X, n)) for k in range(j1, j + 1))
                    if zc and nr:
                        tot["samezcnr"] += 1; tot["pviol"] += isst
                    else:
                        bad += 1; tot["strictsame_nozc"] += isst and not zc; tot["strictsame_nonr"] += isst and zc and not nr
                else:
                    diff += 1; tot["diff"] += 1; tot["strictdiff"] += isst
                    if cw is not None and cw in occ[:-1]: ret += 1; tot["ret"] += 1; tot["strictret"] += isst
                occ.append(cw)
            tot["bviol"] += strict > 1 + diff + bad
            cl = {cls(h, x) for x in g.succ[h]} - {None}
            lc = sum(1 + sum(XV[k][X][0] != XV[k + 1][X][0] for k in range(p, q)) for X in cl) + (None in {cls(h, x) for x in g.succ[h]})
            ent = {}
            for (_, _, w) in L: ent[cls(h, w)] = ent.get(cls(h, w), 0) + 1
            multi = sum(c >= 2 for c in ent.values()); tot["maxmulti"] = max(tot["maxmulti"], multi); tot["multi2"] += multi >= 2
            tot["degviol"] += strict > 2 * len(g.succ[h]) - 1; tot["maxratio"] = max(tot["maxratio"], round(strict / len(g.succ[h]), 2))
            tot["leadviol"] += strict > lc; tot["maxexcess"] = max(tot["maxexcess"], strict - lc)
            tot["maxstrict"] = max(tot["maxstrict"], strict); tot["maxdiff"] = max(tot["maxdiff"], diff); tot["maxret"] = max(tot["maxret"], ret)
            winstrict += strict
    tot["maxwinstrict"] = max(tot["maxwinstrict"], winstrict)
print(f"PCOUNT {os.path.basename(sys.argv[1])} n {n} K {len(S) - 1} " + " ".join(f"{k.upper()} {v}" for k, v in tot.items()))
