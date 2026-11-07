#!/usr/bin/env python3
"""L-RED R200 AGREE: xcnf.py (E 0: every mover prescribed, pure Xi problem) vs r199/xisat.py (z3) on random small prescribed runs.
Instances: random degree-2 ladder genomes (levels 0..2, N 4-6), their own IDEAL run (SAT by construction) or that run with one random
state bit of one step flipped (then W-side checked by req.py; skipped if violated). Usage: agree.py count seed"""
import sys, os, json, random, time
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r199"), os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import req as RQ, xisat, xcnf, ideal
cnt, seed = int(sys.argv[1]), int(sys.argv[2]); R = random.Random(seed); done = 0; tab = []
while done < cnt:
    nl = R.choice([2, 3, 4]); lev = []; WT = []
    for l in range(nl):
        for i in range(2): lev.append(l); WT.append([-1, -1] if l == 0 else R.choice([[2 * l - 2, 2 * l - 1], [2 * l - 1, 2 * l - 2]]))
    N = len(lev); g = list(range(2 * N)); R.shuffle(g); gate = [[g[2 * v], g[2 * v + 1]] for v in range(N)]
    perm = list(range(N)); R.shuffle(perm); pos = {v: i for i, v in enumerate(perm)}
    xt = {}
    for v in range(N):
        for k in (0, 1):
            later = [u for u in range(N) if pos[u] > pos[v]]; xt[(v, k)] = R.choice([-1] + later + later)
    rk = list(range(2 * N)); R.shuffle(rk)
    G = dict(N=N, lev=lev, deg=2, opts=[[[WT[v][k], xt[(v, k)], 2 * v + k] for k in (0, 1)] for v in range(N)], gate=gate,
             br=[rk[2 * v + k] for v in range(N) for k in (0, 1)], bp=[R.randint(0, 1) for _ in range(2 * N)], start=[R.randint(0, 1) for _ in range(N)])
    S, why = ideal.traj(G)
    if len(S) < 4: continue
    S = [list(s) for s in S]
    kind = "own"
    if os.environ.get("RANDRUN") == "1":   # random W-valid run: each step a random nonempty subset of the movers whose KP differs moves to KP
        kind = "randrun"; S = [list(G["start"])]
        for t in range(R.randint(3, 8)):
            nxt = list(S[-1])
            for _ in range(20):
                cand = list(S[-1]); ch = [v for v in range(N) if R.random() < 0.5]
                for v in ch: cand[v] ^= 1
                key = RQ.keys(lev, WT, gate, cand)
                if any(cand[v] != S[-1][v] for v in range(N)) and all(RQ.kp(lev, WT, gate, key, v) == cand[v] for v in range(N) if cand[v] != S[-1][v]):
                    nxt = cand; break
            if nxt == S[-1]: break
            S.append(nxt)
        if len(S) < 3: continue
    if R.random() < 0.6:
        kind = "flip"
        for _ in range(R.randint(1, 3)):
            t = R.randrange(1, len(S)); v = R.randrange(N); S[t][v] ^= 1; kind += f" t{t}v{v}"
    T = dict(movers=[[lev[v], WT[v]] for v in range(N)], states=S, gate=gate)
    bad, req = RQ.requirements(lev, WT, gate, [tuple(s) for s in S])
    if bad or not req: continue
    if any(S[t] == S[t - 1] for t in range(1, len(S))): continue   # an empty step ends every IDEAL run: not a valid prescribed run
    os.makedirs("out/agree_inst", exist_ok=True); json.dump(T, open(f"out/agree_inst/s{seed}_{done + 1}.json", "w"))
    r1, dt1, _ = xisat.solve(lev, WT, [tuple(s) for s in S], req, tmo=int(os.environ.get("XTMO", "600")))
    t0 = time.time(); C, I = xcnf.build(T, 0); r2, model = xcnf.solve(C); dt2 = time.time() - t0
    ok2 = None
    if r2:
        G2 = xcnf.decode(model, I); S2, _ = ideal.traj(G2); ok2 = [list(s) for s in S2[:len(S)]] == S
    r2s = "sat" if r2 else "unsat"
    if r1 not in ("sat", "unsat"):   # z3 undecided: second opinion without the LEM clauses
        C0, I0 = xcnf.build(T, 0, lem=False); r3, _ = xcnf.solve(C0); r2s += f" (noLEM {'sat' if r3 else 'unsat'})"
    tab.append((done, N, len(S) - 1, len(req), kind, r1, r2s, ok2)); done += 1
    print(f"inst {done} N {N} L {len(S) - 1} req {len(req)} {kind}: xisat {r1} ({dt1:.1f} s) xcnf {r2s} ({dt2:.1f} s) replay-match {ok2} {'AGREE' if r1 == r2s else 'DISAGREE'}", flush=True)
print("SUMMARY", sum(1 for x in tab if x[5] == x[6]), "/", len(tab), "agree;", sum(1 for x in tab if x[6] == "sat"), "sat;", "all sat replays match:", all(x[7] for x in tab if x[6] == "sat"))
