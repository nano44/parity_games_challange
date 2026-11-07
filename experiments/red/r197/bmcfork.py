#!/usr/bin/env python3
"""BLOCK=file: JSON list of (xt, gate, start) structures to exclude (REL -> FIX lift loop, r197/liftloop.py). KF=1: add KEYFLIP clauses (redundant). FREE=k: levels < k are free drivers (each move still goes to a strictly Xi-better option, but at ANY time, ignoring keys: a relaxation used to test
composition; run with LEM=0, the lemma clauses assume the rule everywhere). FMIN="l:k,...": additionally require >= k flips of the level-l key ranking R_l among states 1..L (carries; XI=free leaves Xi
unconstrained as in bmc4). L-RED R197 BMCFORK = r193/bmc4.py + XI=fork|down|up: the Xi-targets of each mover's two options are the two movers of ONE level
(fork: any level, or both exit; down: level l-1, level 0 -> exit; up: level l+1, top -> exit). Everything else as bmc4. Original: L-RED R193 BMC4 = r188/bmc3.py + REDUNDANT constraints from proved lane lemmas (LEM=1, default): Xi-reachability reach[x][y]
(acyclic, so the closure equation has one solution); R189 Corollary RE-REVERSAL (deg 2: between two consecutive moves of x some Xi-descendant
of x moves at a step in [t1, t2-1]); R178 XI-NEW / box 144 (a least-level mover of step t >= 2 has a Xi-descendant that moved at t-1).
Both hold on every IDEAL-ACYC run, so adding them changes no answer. LAG=1 (needs LEM): R189 Corollary LAG as well. Original: L-RED R188 BMC3 = R180 bmc.py + symmetry breaking (valid symmetries of the 2-wide ladder): (i) at level 0 the two options of a vertex
are interchangeable (both W-faces go to c_W): gate(v,0) < gate(v,1); (ii) swapping the two vertices of level l together with options 0/1 of
every level-(l+1) vertex is a symmetry: pos(2l) <= pos(2l+1) (pos = acyclic Xi-order). Original R180 text: L-RED R180 BMC: z3 bounded model check of the IDEAL model (fastabs semantics) on a W-ladder of depth d, width 2, deg 2.
Everything free: Xi-targets (acyclic via positions), beta ranks / parities (one per option), gate indices, start. The run is N5's
deterministic S4a dynamics; asks for L consecutive sigma-changing steps (no fallback). SAT => writes a fastabs genome and replays
it. Usage: bmc.py d L out.json"""
import sys, os, json
import z3
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r177"))
SYM = os.environ.get("SYM", "1") == "1"
import fastabs as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'r193'))
d, L, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]; N = 2 * d; lev = [v // 2 for v in range(N)]
faces = [(v, k) for v in range(N) for k in (0, 1)]; M = len(faces)
S = z3.Solver()
rank = {f: z3.Int(f"r{f}") for f in faces}; par = {f: z3.Bool(f"p{f}") for f in faces}
xt = {f: z3.Int(f"x{f}") for f in faces}; pos = [z3.Int(f"pos{v}") for v in range(N)]; gate = {f: z3.Int(f"g{f}") for f in faces}
S.add(z3.Distinct(*rank.values()), z3.Distinct(*gate.values()))
for f in faces:
    S.add(rank[f] >= 0, rank[f] < M, gate[f] >= 0, gate[f] < M, xt[f] >= -1, xt[f] < N, xt[f] != f[0])
    for u in range(N): S.add(z3.Implies(xt[f] == u, pos[u] > pos[f[0]]))
if SYM:
    for v in range(N):
        if lev[v] == 0: S.add(gate[(v, 0)] < gate[(v, 1)])
    for l in range(d): S.add(pos[2 * l] <= pos[2 * l + 1])
XI = os.environ.get("XI", "fork")
for v in range(N):
    a, b = xt[(v, 0)], xt[(v, 1)]; l = lev[v]
    if XI == "down": tl = l - 1
    elif XI == "up": tl = l + 1 if l + 1 < d else -1
    if XI in ("down", "up"):
        if tl < 0: S.add(a == -1, b == -1)
        else: S.add(z3.Or(z3.And(a == 2 * tl, b == 2 * tl + 1), z3.And(a == 2 * tl + 1, b == 2 * tl)))
    elif XI == "fork":
        S.add(z3.Or(z3.And(a == -1, b == -1), *[z3.Or(z3.And(a == 2 * m, b == 2 * m + 1), z3.And(a == 2 * m + 1, b == 2 * m)) for m in range(d)]))
FIX = os.environ.get("FIX")
if FIX:
    R = json.load(open(FIX))
    for v, k in faces:
        S.add(xt[(v, k)] == R["xt"][f"{v},{k}"], gate[(v, k)] == R["gate"][f"{v},{k}"])
if os.environ.get("REL") == "1":   # relaxation (as r188/bmcrel.py): free distinct nonzero integer weights; its UNSAT is an upper bound
    Wt = {f: z3.Int(f"w{f}") for f in faces}; S.add(z3.Distinct(*Wt.values())); S.add(*[Wt[f] != 0 for f in faces])
else:
    Wt = {f: z3.If(par[f], -1, 1) * z3.Sum([z3.If(rank[f] == r, 2 ** r, 0) for r in range(M)]) for f in faces}
KL = []; LS = []; FREE = int(os.environ.get('FREE', '0'))   # FREE=k: movers of levels < k move arbitrarily (a driver; RELAXATION)   # KL[t][v]: option 0 of v is key-smaller under the keys of state t+1
sig = [[z3.Bool(f"s{t}_{v}") for v in range(N)] for t in range(L + 1)]     # True = option 1
def opt(t, v): return z3.If(sig[t][v], 1, 0)
for t in range(L + 1):
    X = [z3.Int(f"X{t}_{u}") for u in range(N)]
    def Fv(v, k): return Wt[(v, k)] + z3.Sum([z3.If(xt[(v, k)] == u, X[u], 0) for u in range(N)])
    for u in range(N): S.add(X[u] == z3.If(sig[t][u], Fv(u, 1), Fv(u, 0)))
    if FIX and t == 0:
        for u in range(N): S.add(sig[0][u] == bool(R['start'][u]))
    if t == L: break
    # availability at state t
    av = {}
    for v in range(N):
        av[(v, 0)] = z3.Or(z3.Not(sig[t][v]), Fv(v, 0) > Fv(v, 1)); av[(v, 1)] = z3.Or(sig[t][v], Fv(v, 1) > Fv(v, 0))
    # keys in the NEW tree (state t+1): lessv[x][y] for x, y on the same level: key_{t+1}(x) < key_{t+1}(y)
    less = {}
    def g_of(v, b): return z3.If(b, gate[(v, 1)], gate[(v, 0)])
    for l in range(d):
        vs = [v for v in range(N) if lev[v] == l]
        for x in vs:
            for y in vs:
                if x == y: continue
                gx, gy = g_of(x, sig[t + 1][x]), g_of(y, sig[t + 1][y])
                if l == 0: less[(x, y)] = gx < gy
                else:
                    a, b = 2 * (l - 1), 2 * (l - 1) + 1
                    same = sig[t + 1][x] == sig[t + 1][y]
                    tx = sig[t + 1][x]; ty = sig[t + 1][y]
                    lowless = z3.If(tx, less[(b, a)], less[(a, b)])  # targets differ: tx -> b, ty -> a (or reverse)
                    less[(x, y)] = z3.If(same, gx < gy, lowless)
    # option keys of v in the new tree: compare option 0 vs option 1 of v
    LS.append([less[(2 * l, 2 * l + 1)] for l in range(d)])
    KL.append({})
    for v in range(N):
        if lev[v] == 0: k0less = gate[(v, 0)] < gate[(v, 1)]
        else: k0less = less[(2 * (lev[v] - 1), 2 * (lev[v] - 1) + 1)]
        KL[-1][v] = k0less
        # chosen = key-least among available
        both = z3.And(av[(v, 0)], av[(v, 1)])
        if lev[v] >= FREE: S.add(sig[t + 1][v] == z3.If(both, z3.Not(k0less), sig[t][v]))
        else: S.add(z3.Implies(sig[t + 1][v] != sig[t][v], both))   # free driver: moves only to a strictly Xi-better option, at any time
    S.add(z3.Or([sig[t + 1][v] != sig[t][v] for v in range(N)]))
FMIN = os.environ.get("FMIN")
if FMIN:
    for item in FMIN.split(","):
        l, k = map(int, item.split(":"))
        S.add(z3.Sum([z3.If(LS[t][l] != LS[t + 1][l], 1, 0) for t in range(len(LS) - 1)]) >= k)
FRATIO = os.environ.get("FRATIO")   # "l1,l2,...": F_l >= 2 F_(l-1) >= 2 at each listed level (flips over transitions 2..L)
if FRATIO:
    fl = lambda l: z3.Sum([z3.If(LS[t][l] != LS[t + 1][l], 1, 0) for t in range(len(LS) - 1)])
    for l in map(int, FRATIO.split(",")): S.add(fl(l) >= 2 * fl(l - 1), fl(l - 1) >= 1)
if os.environ.get("LEM", "1") == "1":
    reach = [[z3.Bool(f"re{x}_{y}") for y in range(N)] for x in range(N)]
    for x in range(N):
        for y in range(N):
            S.add(reach[x][y] == z3.Or([z3.Or(xt[(x, k)] == y, z3.Or([z3.And(xt[(x, k)] == z, reach[z][y]) for z in range(N) if z != x])) for k in (0, 1)]))
        S.add(z3.Not(reach[x][x]))
    mvd = [[sig[t + 1][v] != sig[t][v] for v in range(N)] for t in range(L)]   # mvd[t][v]: v moves at step t+1
    for x in range(N):
        for a in range(L):
            for b in range(a + 1, L):
                gap = z3.And(mvd[a][x], mvd[b][x], *[z3.Not(mvd[c][x]) for c in range(a + 1, b)])
                S.add(z3.Implies(gap, z3.Or([z3.And(reach[x][y], z3.Or([mvd[c][y] for c in range(a, b)])) for y in range(N) if y != x])))
    for t in range(1, L):
        for x in range(N):
            lower = [z3.Not(mvd[t][u]) for u in range(N) if lev[u] < lev[x]]
            S.add(z3.Implies(z3.And(mvd[t][x], *lower), z3.Or([z3.And(reach[x][y], mvd[t - 1][y]) for y in range(N) if y != x])))
if os.environ.get("KF") == "1":
    # L-NEW box 149 Lemma KEYFLIP (deg 2, any IDEAL-ACYC run): consecutive moves of x at steps a+1 < b+1 need a different
    # key-preferred option at states a+1 and b+1 (KL[a][x] != KL[b][x]); redundant for rule-bound movers (levels >= FREE)
    mvk = [[sig[t + 1][v] != sig[t][v] for v in range(N)] for t in range(L)]
    for x in range(N):
        if lev[x] < FREE: continue
        for a in range(L):
            for b in range(a + 1, L):
                gap = z3.And(mvk[a][x], mvk[b][x], *[z3.Not(mvk[c][x]) for c in range(a + 1, b)])
                S.add(z3.Implies(gap, KL[a][x] != KL[b][x]))
if os.environ.get("LAG") == "1":
    # R189 Corollary LAG (deg 2): x stays at step t, moves at step t+1, and its option key order is the same at states t and t+1
    # => some Xi-descendant of x moved at step t
    for t in range(1, L):
        for x in range(N):
            if lev[x] == 0: continue
            S.add(z3.Implies(z3.And(mvd[t][x], z3.Not(mvd[t - 1][x]), KL[t][x] == KL[t - 1][x]), z3.Or([z3.And(reach[x][y], mvd[t - 1][y]) for y in range(N) if y != x])))
BLOCK = os.environ.get("BLOCK")
if BLOCK and os.path.exists(BLOCK):   # list of FIX structures (xt, gate, start) already refuted by the exact lift: exclude them
    for B in json.load(open(BLOCK)):
        S.add(z3.Not(z3.And(*[xt[(v, k)] == B["xt"][f"{v},{k}"] for v, k in faces], *[gate[(v, k)] == B["gate"][f"{v},{k}"] for v, k in faces],
                            *[sig[0][v] == bool(B["start"][v]) for v in range(N)])))
r = S.check(); print("BMCFORK XI", XI, "FREE", FREE, "FMIN", FMIN, "FRATIO", FRATIO, "d", d, "L", L, "LEM", os.environ.get("LEM", "1"), "LAG", os.environ.get("LAG", "0"), "REL", os.environ.get("REL", "0"), "->", r, flush=True)
if r == z3.sat and os.environ.get("REL") == "1":   # write the structure as a FIX file (xt, gate, start) for the exact model
    m = S.model(); ev = lambda e: m.eval(e, model_completion=True)
    json.dump(dict(xt={f"{v},{k}": ev(xt[(v, k)]).as_long() for v, k in faces}, gate={f"{v},{k}": ev(gate[(v, k)]).as_long() for v, k in faces},
                   start=[1 if z3.is_true(ev(sig[0][v])) else 0 for v in range(N)]), open(out, "w")); print("REL model written", out)
if r == z3.sat and os.environ.get("REL") != "1":
    m = S.model(); ev = lambda e: m.eval(e, model_completion=True)
    order = sorted(range(N), key=lambda v: ev(pos[v]).as_long())
    G = dict(N=N, lev=lev, deg=2, opts=[[[-1 if lev[v] == 0 else 2 * (lev[v] - 1) + k, ev(xt[(v, k)]).as_long(), 2 * v + k] for k in (0, 1)] for v in range(N)],
             gate=[[ev(gate[(v, k)]).as_long() for k in (0, 1)] for v in range(N)], br=[ev(rank[f]).as_long() for f in faces],
             bp=[1 if z3.is_true(ev(par[f])) else 0 for f in faces], start=[1 if z3.is_true(ev(sig[0][v])) else 0 for v in range(N)], xorder=order)
    json.dump(G, open(out, "w")); print("replay", F.simulate(G))
