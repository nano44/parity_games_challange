#!/usr/bin/env python3
"""L-RED R200 BF: brute-force exact Xi check of a prescribed run for N = 4 movers (independent of xcnf/xisat encodings): every
acyclic Xi-target assignment (5^8 candidates), then r199/xisearch.greedy (Lemma GREEDY, R199 §1: ranks/parities exist for fixed
targets iff greedy empties the list). Compared with xcnf.py (LEM on and off) on random W-valid runs (agree.py RANDRUN generator).
Usage: bf.py count seed"""
import sys, os, json, random, itertools, time
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r199"), os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
os.environ["SOFT"] = "0"   # exact greedy (must be set before xisearch is imported)
import req as RQ, xisearch as XS, xcnf, ideal
def acyclic(N, xt):
    succ = {v: {u for (w, k), u in xt.items() if w == v and u >= 0} for v in range(N)}; col = {}
    def dfs(v):
        col[v] = 1
        for u in succ[v]:
            if col.get(u) == 1 or (u not in col and not dfs(u)): return False
        col[v] = 2; return True
    return all(v in col or dfs(v) for v in range(N))
def brute(N, S, req):
    faces = [(v, k) for v in range(N) for k in (0, 1)]
    doms = [[u for u in range(-1, N) if u != f[0]] for f in faces]
    for combo in itertools.product(*doms):
        xt = dict(zip(faces, combo))
        if not acyclic(N, xt): continue
        order, left = XS.greedy(XS.reqsets(xt, S, req), faces)
        if left == 0: return "sat", xt
    return "unsat", None
if __name__ == "__main__":
    cnt, seed = int(sys.argv[1]), int(sys.argv[2]); R = random.Random(seed); done = 0; agree = 0; nun = 0
    while done < cnt:
        N = 4; lev = [0, 0, 1, 1]; WT = [[-1, -1], [-1, -1], R.choice([[0, 1], [1, 0]]), R.choice([[0, 1], [1, 0]])]
        g = list(range(8)); R.shuffle(g); gate = [[g[2 * v], g[2 * v + 1]] for v in range(N)]
        S = [[R.randint(0, 1) for _ in range(N)]]
        for t in range(R.randint(3, 7)):
            nxt = None
            for _ in range(30):
                cand = [b ^ (R.random() < 0.5) for b in S[-1]]; key = RQ.keys(lev, WT, gate, cand)
                if cand != S[-1] and all(RQ.kp(lev, WT, gate, key, v) == cand[v] for v in range(N) if cand[v] != S[-1][v]): nxt = cand; break
            if nxt is None: break
            S.append(nxt)
        if len(S) < 3: continue
        St = [tuple(s) for s in S]; bad, req = RQ.requirements(lev, WT, gate, St)
        if bad or not req: continue
        t0 = time.time(); r0, xt = brute(N, St, req); d0 = time.time() - t0
        T = dict(movers=[[lev[v], WT[v]] for v in range(N)], states=S, gate=gate); res = []
        for lem in (True, False):
            C, I = xcnf.build(T, 0, lem=lem); r, model = xcnf.solve(C); rs = "sat" if r else "unsat"
            if r:
                G = xcnf.decode(model, I); S2, _ = ideal.traj(G); rs += "/replay-ok" if [tuple(s) for s in S2[:len(S)]] == St else "/REPLAY-MISMATCH"
            res.append(rs)
        ok = all(x.split("/")[0] == r0 for x in res) and all("MISMATCH" not in x for x in res); agree += ok; nun += r0 == "unsat"; done += 1
        print(f"inst {done} L {len(S) - 1} req {len(req)}: brute {r0} ({d0:.1f} s) xcnf LEM {res[0]} noLEM {res[1]} {'AGREE' if ok else 'DISAGREE'}", flush=True)
    print("SUMMARY", agree, "/", done, "agree;", nun, "brute-unsat")
