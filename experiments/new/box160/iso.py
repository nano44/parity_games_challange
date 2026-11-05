#!/usr/bin/env python3
"""L-NEW box 160, EXACT (CaDiCaL via pysat): maximum run length on R197-convention 2-wide degree-2 ladders (d levels) under extra
side conditions. Engine: L-RED's xcnf.py (claude/l-red experiments/red/r200/xcnf.py @ 5f3e89e1, used read-only from an extracted copy;
path in env LRED = the directory that holds experiments/red/). This driver only ADDS clauses to xcnf.build(movers = [], E = d), as
L-RED's r200/xmax.py does, and replays every SAT model under L-RED's r187/ideal.py AND under the box 150 simulator (box150/check.py).
Side conditions (env):
  ISO=1     no option has a level-0 mover as its Xi-target (level 0 acts on the rest only through the W-keys).
  NOW=1     the level-0 key order b_0 (which level-0 mover has the smaller key) is the same at every state of the run.
  FREE0=1 KF=k  level-0 states are FREE (external agent); b_0 changes <= k times; every step moves a mover of level >= 1;
            T counts those steps (the run above level 0 under an externally flipped level-0 key bit). Use with ISO=1.
  FRZ=v,..  the listed movers never move.
  NOL0=1    no level-0 step at all (the run is a LIFT-type run; sanity: max = T*(d-1)).
  SEG=...   passed through to xcnf (seg1 / mid / tail cardinalities).
Usage: iso.py d t out.json   -> SAT/UNSAT for «some genome + start has T >= t»."""
import sys, os, json, time
LR = os.path.join(os.environ["LRED"], "experiments", "red")
sys.path[:0] = [os.path.join(LR, "r200"), os.path.join(LR, "r187"), os.path.join(LR, "r178"), os.path.join(LR, "r199")]
os.environ.setdefault("TMIN", "1")
if os.environ.get("FREE0") == "1":   # external control of level 0: box160/xcnf_free0.py (one-line change of L-RED's xcnf.py)
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import xcnf_free0 as xcnf; os.environ["LEM"] = "0"
else: import xcnf
import ideal
d, t, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
T = dict(movers=[], gate=[], states=[[] for _ in range(t + 1)])
t0 = time.time(); C, I = xcnf.build(T, d, lem=os.environ.get("LEM", "1") == "1")
N = I["N"]; L0 = [v for v in range(N) if I["lev"][v] == 0]
if os.environ.get("ISO") == "1":
    for f in I["faces"]:
        for u in L0:
            if u != f[0]: C.add([-I["b"][(f, u)]])
if os.environ.get("NOW") == "1":   # level-0 steps never change the level-0 key order b_0 (they act only through the Xi-side)
    g0 = I["g0"]; glt0 = lambda a, b: g0[(a, b)] if (a, b) in g0 else -g0[(b, a)]
    def b0(tt):
        a, c = I["st"][(tt, 0)], I["st"][(tt, 1)]
        return C.OR([C.AND([a if ka else xcnf.neg(a), c if kc else xcnf.neg(c), glt0((0, ka), (1, kc))]) for ka in (0, 1) for kc in (0, 1)])
    B0 = b0(0)
    for tt in range(1, t + 1): C.add([C.EQ(b0(tt), B0)])
if os.environ.get("FREE0") == "1":   # KF=k: b_0 changes at most k times over s_0..s_t; every step moves a mover of level >= 1
    from pysat.card import CardEnc, EncType
    g0 = I["g0"]; glt0 = lambda a, b: g0[(a, b)] if (a, b) in g0 else -g0[(b, a)]
    def b0f(tt):
        a, c = I["st"][(tt, 0)], I["st"][(tt, 1)]
        return C.OR([C.AND([a if ka else xcnf.neg(a), c if kc else xcnf.neg(c), glt0((0, ka), (1, kc))]) for ka in (0, 1) for kc in (0, 1)])
    BB = [b0f(tt) for tt in range(t + 1)]
    fl = [xcnf.neg(C.EQ(BB[tt], BB[tt - 1])) for tt in range(1, t + 1)]
    fl = [x for x in fl if x is not False]
    k = int(os.environ.get("KF", "2"))
    if any(x is True for x in fl): k -= sum(1 for x in fl if x is True); fl = [x for x in fl if x is not True]
    if k < 0: C.add([])
    elif fl and k < len(fl):
        enc = CardEnc.atmost(lits=fl, bound=k, top_id=C.n, encoding=EncType.seqcounter); C.n = max(C.n, enc.nv); [C.add(list(c)) for c in enc.clauses]
    for tt in range(1, t + 1): C.add([I["mv"][(tt, v)] for v in range(N) if I["lev"][v] >= 1])
for u in [int(x) for x in os.environ.get("FRZ", "").split(",") if x]:   # FRZ=v,...: these movers never move
    for tt in range(1, t + 1): C.add([xcnf.neg(I["mv"][(tt, u)])])
if os.environ.get("NOL0") == "1":
    for tt in range(1, t + 1):
        for u in L0: C.add([xcnf.neg(I["mv"][(tt, u)])])
print(f"ISO d {d} t {t} N {N} ISO={os.environ.get('ISO')} NOL0={os.environ.get('NOL0')} NOW={os.environ.get('NOW')} SEG={os.environ.get('SEG')} vars {C.n} clauses {len(C.cl)} build {time.time() - t0:.1f} s", flush=True)
t1 = time.time(); r, model = xcnf.solve(C)
print(f"RESULT d {d} T >= {t}: {'SAT' if r else 'UNSAT'} {time.time() - t1:.1f} s", flush=True)
if r and os.environ.get("FREE0") == "1":   # replay with the level-0 schedule forced (own step function, box 150 Gen for values / keys)
    G = xcnf.decode(model, I); json.dump(G, open(out, "w")); ms = set(l for l in model if l > 0)
    tv = lambda l: l if isinstance(l, bool) else ((l in ms) if l > 0 else (-l not in ms))
    sched = [[int(tv(I["st"][(tt, u)])) for u in L0] for tt in range(t + 1)]
    P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box150", "check.py")
    ns = {"__file__": P}; exec(open(P).read().split("\nif __name__")[0], ns); g = ns["Gen"](G)
    cur = list(G["start"]); cur[0], cur[1] = sched[0]; nst = 0; flips = 0
    def b0(st): k = g.keys(st); return k[0] < k[1]
    for tt in range(1, t + 1):
        A = [g.avail(tuple(cur), v) for v in range(N)]; key = [None] * N; nw = list(cur)
        for v in g.byl:
            if g.lev[v] == 0: k = sched[tt][L0.index(v)]
            else: k = min(A[v], key=lambda k: g.optkey(key, v, k))
            nw[v] = k; key[v] = g.optkey(key, v, k)
        if any(nw[v] != cur[v] for v in range(N) if g.lev[v] >= 1): nst += 1
        flips += b0(tuple(nw)) != b0(tuple(cur)); cur = nw
    print(f"replay (forced level-0 schedule {sched}): steps moving level >= 1: {nst} of {t}; b_0 flips {flips}", flush=True)
elif r:
    G = xcnf.decode(model, I); json.dump(G, open(out, "w")); S, why = ideal.traj(G)
    P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box150", "check.py")
    ns = {"__file__": P}; exec(open(P).read().split("\nif __name__")[0], ns); S2, _ = ns["Gen"](G).run(G["start"])
    lev = G["lev"]; z = [u for u in range(1, len(S)) if any(S[u][v] != S[u - 1][v] for v in range(N) if lev[v] == 0)]
    cuts = [0] + z + [len(S)]; segs = [cuts[i + 1] - cuts[i] - 1 for i in range(len(cuts) - 1)]
    isoOK = all(o[1] not in L0 for o2 in G["opts"] for o in o2)
    print(f"replay ideal.py L {len(S) - 1} ({why}); box150 L {len(S2) - 1}; same {[tuple(x) for x in S] == [tuple(x) for x in S2]}; "
          f"level-0 steps {z}; segs {segs}; iso {isoOK} -> {out}", flush=True)
