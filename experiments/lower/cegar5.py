#!/usr/bin/env python3
"""CEGAR search for a k-gate program solving all one-player Büchi games with <= 5 vertices.
Candidate programs come from SAT (satsearch.encode) on a small structure: the quotient Q_3 plus counterexample games;
each candidate is verified on Q_4 (all types with <= 4 vertices) and then on ALL 5-vertex games (vec5.sweep, W cached).
UNSAT at any round proves B_1(5) > k (the subset is successor-closed). A verified candidate proves B_1(5) <= k.
Usage: cegar5.py k [window]   (window = w restricts gate i to read P2 and s_{i-w}..s_{i-1}; omit for unrestricted)"""
import sys, os, time, json
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pysat.solvers import Cadical153
import satsearch, restricted, vec5
from quotient import build
from slp import Struct, eval_struct, cost, depth
from games import pack

CACHE = os.environ.get("W5_CACHE", "/tmp/claude-0/-home-user-parity-games-challange/51bc3662-6fb9-51cf-b982-34798b3d1e12/scratchpad/w5")


def cached_W(k=5):
    os.makedirs(CACHE, exist_ok=True)
    S = vec5.all_succ(k)
    Ws = {}
    for pm in range(2 ** k):
        f = os.path.join(CACHE, f"W_k{k}_p{pm}.npy")
        if not os.path.exists(f):
            np.save(f, vec5.ref_W(S, pm, k))
        Ws[pm] = f
    return S, Ws


def sweep5(prog, S, Ws, order, max_fail=48):
    fails, nfail = [], 0
    k = 5
    for pm in order:
        W = np.load(Ws[pm])
        out = vec5.eval_prog(prog, S, pm, k)
        bad = np.nonzero(out != W)[0]
        nfail += len(bad)
        if len(bad):
            pick = bad if len(bad) <= 12 else np.random.default_rng(len(fails)).choice(bad, 12, replace=False)
            for gi in pick:
                succ = [[w for w in range(k) if (S[gi, v] >> w) & 1] for v in range(k)]
                prio = tuple(2 if (pm >> v) & 1 else 1 for v in range(k))
                fails.append((prio, (0,) * k, tuple(tuple(s) for s in succ)))
            if len(fails) >= max_fail:
                break
    return fails, nfail


class Sub:  # the SAT subset: Q_3 classes + raw games
    def __init__(self, q3):
        self.q3 = q3; self.games = []

    def struct(self):
        owner = list(self.q3.S.owner); prio = list(self.q3.S.prio)
        succ = [list(self.q3.S.indices[self.q3.S.indptr[c]:self.q3.S.indptr[c + 1]]) for c in range(self.q3.N)]
        W = list(self.q3.W)
        import zielonka
        from games import to_game
        for raw in self.games:
            base = len(owner)
            pr, ow, sc = raw
            owner.extend(ow); prio.extend(pr)
            succ.extend([[base + w for w in s] for s in sc])
            z = zielonka.solve(to_game(raw))
            W.extend([z[v] == 0 for v in range(len(pr))])
        q = type("Q", (), {})()
        q.S = Struct(owner, prio, succ); q.W = np.array(W, dtype=bool); q.N = q.S.N; q.n = 5
        return q


def main():
    k = int(sys.argv[1]); window = int(sys.argv[2]) if len(sys.argv) > 2 else None
    tag = f"k{k}" + (f"_w{window}" if window else "")
    print(f"== CEGAR n=5, {tag}", flush=True)
    q3 = build(3); q4 = build(4, verbose=True)
    S5, Ws = cached_W(5)
    print("W cache ready", flush=True)
    sub = Sub(q3)
    # seed with the deepest fooling pairs: lassos with one P2 on a 5-cycle, and their losing twins
    for n5 in (5,):
        cyc = tuple((v + 1) % n5 for v in range(n5))
        for pos in range(n5):
            prio = tuple(2 if v == pos else 1 for v in range(n5))
            sub.games.append((prio, (0,) * n5, tuple((cyc[v],) for v in range(n5))))
            sub.games.append((prio, (0,) * n5, tuple(((cyc[v],) if v != pos else (pos,)) for v in range(n5))))
    rnd = 0
    while True:
        rnd += 1
        q = sub.struct()
        t0 = time.time()
        if window:
            solver, decode, ncl = restricted.encode_restricted(q, list(range(q.N)), k, window=window)
        else:
            solver, decode, ncl = satsearch.encode(q, list(range(q.N)), k)
        ok = solver.solve()
        print(f"round {rnd}: subset {q.N} nodes ({len(sub.games)} games), {ncl} clauses -> {'SAT' if ok else 'UNSAT'} [{time.time()-t0:.1f}s]", flush=True)
        if not ok:
            print(f"RESULT: no program with {k} Cpre gates ({tag}) solves all one-player Büchi games with <= 5 vertices (UNSAT on a successor-closed subset).")
            json.dump({"k": k, "window": window, "result": "UNSAT", "subset_games": sub.games}, open(f"cegar5_{tag}.json", "w"))
            return 1
        prog = satsearch.program_from_tables(decode(solver.get_model()), k)
        del solver
        # verify on Q_4
        out4 = eval_struct(prog, q4.S)
        bad4 = np.nonzero(out4 != q4.W)[0]
        if len(bad4):
            pick = bad4 if len(bad4) <= 48 else np.random.default_rng(rnd).choice(bad4, 48, replace=False)
            for c in pick:
                raw, v = q4.rep[c]
                sub.games.append((tuple(raw[0]), tuple(raw[1]), tuple(tuple(s) for s in raw[2])))
            print(f"   Q_4: {len(bad4)} failing classes; added {len(pick)} games", flush=True)
            continue
        t0 = time.time()
        order = list(np.random.default_rng(rnd).permutation(32))
        fails, nfail = sweep5(prog, S5, Ws, order)
        print(f"   5-vertex sweep: {nfail} failing games in the patterns checked; added {len(fails)} [{time.time()-t0:.1f}s]", flush=True)
        if not fails:
            # full confirmation over all 32 patterns in order
            fails2, nfail2 = sweep5(prog, S5, Ws, list(range(32)), max_fail=1)
            if nfail2 == 0:
                print(f"RESULT: program with {k} Cpre gates ({tag}) solves ALL one-player Büchi games with <= 5 vertices. cost={cost(prog)} depth={depth(prog)}")
                json.dump({"n": 5, "k": k, "window": window, "result": "SAT-verified", "program": prog}, open(f"cegar5_{tag}.json", "w"))
                return 0
            fails = fails2
        sub.games.extend(fails)


if __name__ == "__main__":
    sys.exit(main())
