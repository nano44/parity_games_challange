#!/usr/bin/env python3
"""L-RED R199 XISEARCH: find Xi-targets, beta-ranks and parities realising the Xi-requirements of a prescribed run (r199/req.py).
Exact semantics (RESULTS R104): option values are the sets of betas on their chains, compared by the beta of largest rank in the
symmetric difference (better iff that beta is in the set and even, or in the other set and odd).
GREEDY (PROVED below, lane): with Xi-targets fixed, the requirements are pairs (A, B, «A better»); a rank order and parities exist
iff repeatedly picking a face f whose parity demands (over the not yet decided requirements whose A xor B contains f) agree, giving
f that parity and the next lower... no: the next HIGHEST free rank, and deleting the requirements it decides, empties the list.
(Proof: «if»: the order built decides every requirement correctly by its top face. «only if»: given a solution, at any stage its
highest-ranked face among the faces occurring in a remaining symmetric difference is consistent (it decides each of those
requirements, with its fixed parity); taking any consistent f instead keeps the rest solvable, since the remaining requirements
do not contain f in their symmetric differences, so the solution's order restricted to them still decides them.) Faces in no
symmetric difference take the lowest ranks.
Outer search: local search over acyclic Xi-targets (topological order + targets later in it) minimising the number of requirements
left when greedy stops. Usage: xisearch.py target.json out.json [iters] [seed]   (target as req.py)"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import req as RQ
SOFT = os.environ.get("SOFT", "1") == "1"; TEMP = float(os.environ.get("TEMP", "1.0")); RESET = int(os.environ.get("RESET", "5000"))
def chain(xt, s, x, k):
    out = [(x, k)]; u = xt[(x, k)]
    while u >= 0: out.append((u, s[u])); u = xt[(u, s[u])]
    return out
def reqsets(xt, S, req):
    R = []
    for (s, x), b in req.items():
        A = set(chain(xt, S[s], x, b)); B = set(chain(xt, S[s], x, 1 - b)); R.append((A - B, B - A))
    return R
def greedy(R, faces):
    """R: list of (A-only, B-only), A must be better. Returns (rank order top-first with parities, #left)"""
    left = list(range(len(R))); order = []; used = set(); viol = 0
    while left:
        dem = {}
        for i in left:
            a, b = R[i]
            for f in a: dem.setdefault(f, set()).add(0)    # f in A only: A better iff f even (parity 0)
            for f in b: dem.setdefault(f, set()).add(1)    # f in B only: A better iff f odd
        cand = [f for f, p in dem.items() if len(p) == 1 and f not in used]
        if not cand:
            if not SOFT: return order, len(left)
            # SOFT: take the face with the largest parity majority, count the minority requirements as violated
            cnt = {}
            for i in left:
                a, b = R[i]
                for f in a: cnt.setdefault(f, [0, 0])[0] += 1
                for f in b: cnt.setdefault(f, [0, 0])[1] += 1
            f = max(cnt, key=lambda f: (max(cnt[f]) - min(cnt[f]) * 3, max(cnt[f]))); p = 0 if cnt[f][0] >= cnt[f][1] else 1
            viol += min(cnt[f]); order.append((f, p)); used.add(f)
            left = [i for i in left if f not in R[i][0] and f not in R[i][1]]; continue
        f = cand[0]; p = next(iter(dem[f])); order.append((f, p)); used.add(f)
        left = [i for i in left if f not in R[i][0] and f not in R[i][1]]
    return order, viol
def realise(lev, WT, gate, start, xt, order, faces):
    M = len(faces); rank = {}; par = {}; r = M - 1
    for f, p in order: rank[f] = r; par[f] = p; r -= 1
    for f in faces:
        if f not in rank: rank[f] = r; par[f] = 0; r -= 1
    N = len(lev); pos = topo(N, xt)
    return RQ.genome(lev, WT, gate, start, dict(xt=xt, pos=pos, rank=rank, par=par))
def topo(N, xt):
    indeg = {v: 0 for v in range(N)}; succ = {v: set() for v in range(N)}
    for (v, k), u in xt.items():
        if u >= 0 and u not in succ[v]: succ[v].add(u); indeg[u] += 1
    q = [v for v in range(N) if indeg[v] == 0]; order = []
    while q:
        v = q.pop(); order.append(v)
        for u in succ[v]:
            indeg[u] -= 1
            if indeg[u] == 0: q.append(u)
    pos = [0] * N
    for i, v in enumerate(order): pos[v] = i
    return pos
def search(lev, WT, S, req, iters=20000, seed=0, init=None, allow=None, log=False):
    rng = random.Random(seed); N = len(lev); faces = [(v, k) for v in range(N) for k in (0, 1)]
    pi = list(range(N)); rng.shuffle(pi); P = {v: i for i, v in enumerate(pi)}
    if init:
        xt = dict(init); P = {v: i for i, v in enumerate(sorted(range(N), key=lambda v: topo(N, xt)[v]))}
    else: xt = {f: -1 for f in faces}
    def ok_t(f, u): return u < 0 or (P[u] > P[f[0]] and (allow is None or u in allow.get(f[0], range(-1, N))))
    def score(xt): return greedy(reqsets(xt, S, req), faces)[1]
    sc = score(xt); best = (sc, dict(xt))
    for it in range(iters):
        if sc == 0: break
        x2 = dict(xt); P2 = dict(P)
        if rng.random() < 0.2:   # swap two movers in the order, repair targets
            a, b = rng.sample(range(N), 2); P2[a], P2[b] = P2[b], P2[a]
            for f in faces:
                u = x2[f]
                if u >= 0 and P2[u] <= P2[f[0]]: x2[f] = -1
        else:
            f = rng.choice(faces); later = [u for u in range(N) if P2[u] > P2[f[0]] and (allow is None or u in allow.get(f[0], range(N)))]
            x2[f] = rng.choice(later + [-1])
        s2 = score(x2)
        temp = TEMP * (1 - it / iters) + 1e-9
        if s2 <= sc or rng.random() < pow(2.718, -(s2 - sc) / temp): xt, P, sc = x2, P2, s2
        if sc < best[0]:
            best = (sc, dict(xt))
            if log: print("  it", it, "left", sc, flush=True)
        if it % RESET == RESET - 1 and sc > best[0]: xt = dict(best[1]); sc = best[0]; P = {v: i for i, v in enumerate(sorted(range(N), key=lambda v: topo(N, xt)[v]))}
    return best
def violated(xt, S, req, faces):
    """requirements (keys) violated by the SOFT greedy order for these Xi-targets"""
    keys = list(req.items()); R = reqsets(xt, S, req); order, v = greedy(R, faces)
    rank = {f: len(order) - i for i, (f, p) in enumerate(order)}; par = dict(order); bad = []
    for (key, b), (a, bb) in zip(keys, R):
        top = max(a | bb, key=lambda f: rank.get(f, 0), default=None)
        okk = top is not None and top in par and ((top in a and par[top] == 0) or (top in bb and par[top] == 1))
        if not okk: bad.append(key[1])
    return bad
def lns(lev, WT, S, req, xt, rounds=40, K=8, seed=0, tmo=120, log=True):
    import xisat
    rng = random.Random(seed); N = len(lev); faces = [(v, k) for v in range(N) for k in (0, 1)]
    for r in range(rounds):
        badm = violated(xt, S, req, faces)
        hot = [f for f in faces if f[0] in badm]
        free = set(rng.sample(hot, min(len(hot), K // 2))) if hot else set()
        rest = [f for f in faces if f not in free]; free |= set(rng.sample(rest, min(len(rest), K - len(free))))
        fx = {f: u for f, u in xt.items() if f not in free}
        res, dt, sol = xisat.solve(lev, WT, S, req, tmo=tmo, fixxt=fx)
        if log: print(f"  LNS round {r}: free {len(free)} (hot movers {sorted(set(badm))[:8]}) -> {res} {dt:.1f} s", flush=True)
        if res == "sat": return sol
    return None
if __name__ == "__main__":
    import ideal
    T = json.load(open(sys.argv[1])); out = sys.argv[2]; it = int(sys.argv[3]) if len(sys.argv) > 3 else 20000; seed = int(sys.argv[4]) if len(sys.argv) > 4 else 0
    if "opts" in T:
        lev = T["lev"]; WT = [[o[0] for o in T["opts"][v]] for v in range(T["N"])]; gate = T["gate"]; S, why = ideal.traj(T)
    else:
        lev = [m[0] for m in T["movers"]]; WT = [m[1] for m in T["movers"]]; gate = T["gate"]; S = [tuple(s) for s in T["states"]]
    bad, req = RQ.requirements(lev, WT, gate, S)
    print("XISEARCH L", len(S) - 1, "N", len(lev), "W-side violations", bad, "requirements", len(req), flush=True)
    if bad: sys.exit(1)
    if os.environ.get("CHECKOWN") == "1" and "opts" in T:
        xt = {(v, k): T["opts"][v][k][1] for v in range(T["N"]) for k in (0, 1)}
        print("own Xi-targets: greedy left", greedy(reqsets(xt, S, req), [(v, k) for v in range(len(lev)) for k in (0, 1)])[1])
    sc, xt = search(lev, WT, S, req, it, seed, log=True)
    print("best left", sc, flush=True)
    if sc > 0 and os.environ.get("LNS", "1") == "1":
        sol = lns(lev, WT, S, req, xt, rounds=int(os.environ.get("ROUNDS", "40")), K=int(os.environ.get("K", "8")), seed=seed)
        if sol:
            G = RQ.genome(lev, WT, gate, S[0], dict(xt=sol["xt"], pos=topo(len(lev), sol["xt"]), rank=sol["rank"], par=sol["par"]))
            json.dump(G, open(out, "w")); S2, why = ideal.traj(G)
            print("LNS SAT replay L", len(S2) - 1, why, "prefix matches target:", list(S2[:len(S)]) == list(S), out); sys.exit(0)
    if sc == 0:
        faces = [(v, k) for v in range(len(lev)) for k in (0, 1)]; order, _ = greedy(reqsets(xt, S, req), faces)
        G = realise(lev, WT, gate, S[0], xt, order, faces); json.dump(G, open(out, "w")); S2, why = ideal.traj(G)
        print("replay L", len(S2) - 1, why, "prefix matches target:", list(S2[:len(S)]) == list(S), out)
