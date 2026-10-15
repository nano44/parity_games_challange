#!/usr/bin/env python3
"""Faster variant of cegar5.py: the SAT model's truth tables are evaluated directly on all 5-vertex games (one lookup per
gate per vertex instead of thousands of Boolean gates), every sweep covers all 32 priority patterns, and up to `per_pat`
counterexamples per pattern are added each round. Same soundness: UNSAT on the successor-closed subset => B_1(5) > k;
a candidate is accepted only after it agrees with the reference on all 916·10^6 five-vertex games and on all of Q_4.
Usage: cegar5b.py k [window] [per_pat]"""
import sys, os, time, json
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import satsearch, restricted, vec5, cegar5
from quotient import build
from slp import eval_struct, cost, depth


def eval_tables(tables, k, S, pm, kv=5):
    """Return the output mask per game for the program given by truth tables (tables[i-1] for gate i, tables[k] = output)."""
    full = (1 << kv) - 1
    s_masks = []
    for i in range(1, k + 2):
        tab = np.array(tables[i - 1], dtype=np.uint8)
        y = np.zeros(len(S), dtype=np.uint8)
        for v in range(kv):
            idx = np.full(len(S), (pm >> v) & 1, dtype=np.int64)
            for j in range(1, i):
                idx |= ((s_masks[j - 1] >> v) & 1).astype(np.int64) << j
            y |= (tab[idx] << v).astype(np.uint8)
        if i <= k:
            s_masks.append(vec5.cpre(y, S, kv))
        else:
            return y


def sweep_tables(tables, k, S, Ws, per_pat):
    fails, nfail = [], 0
    kv = 5
    for pm in range(32):
        W = np.load(Ws[pm])
        out = eval_tables(tables, k, S, pm, kv)
        bad = np.nonzero(out != W)[0]
        nfail += len(bad)
        if len(bad):
            pick = bad if len(bad) <= per_pat else np.random.default_rng(pm + 7 * len(fails)).choice(bad, per_pat, replace=False)
            for gi in pick:
                succ = [[w for w in range(kv) if (S[gi, v] >> w) & 1] for v in range(kv)]
                prio = tuple(2 if (pm >> v) & 1 else 1 for v in range(kv))
                fails.append((prio, (0,) * kv, tuple(tuple(s) for s in succ)))
    return fails, nfail


def main():
    k = int(sys.argv[1]); window = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "0" else None
    per_pat = int(sys.argv[3]) if len(sys.argv) > 3 else 12
    tag = f"k{k}" + (f"_w{window}" if window else "") + "_b"
    print(f"== CEGAR-b n=5, {tag}, per_pat={per_pat}", flush=True)
    q3 = build(3); q4 = build(4, verbose=True)
    S5, Ws = cegar5.cached_W(5)
    sub = cegar5.Sub(q3)
    n5 = 5; cyc = tuple((v + 1) % n5 for v in range(n5))
    for pos in range(n5):
        prio = tuple(2 if v == pos else 1 for v in range(n5))
        sub.games.append((prio, (0,) * n5, tuple((cyc[v],) for v in range(n5))))
        sub.games.append((prio, (0,) * n5, tuple(((cyc[v],) if v != pos else (pos,)) for v in range(n5))))
    rnd = 0
    while True:
        rnd += 1
        q = sub.struct(); t0 = time.time()
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
        tables = decode(solver.get_model()); del solver
        prog = satsearch.program_from_tables(tables, k)
        out4 = eval_struct(prog, q4.S)
        bad4 = np.nonzero(out4 != q4.W)[0]
        if len(bad4):
            pick = bad4 if len(bad4) <= 96 else np.random.default_rng(rnd).choice(bad4, 96, replace=False)
            for c in pick:
                raw, v = q4.rep[c]
                sub.games.append((tuple(raw[0]), tuple(raw[1]), tuple(tuple(s) for s in raw[2])))
            print(f"   Q_4: {len(bad4)} failing classes; added {len(pick)} games", flush=True)
            continue
        t0 = time.time()
        fails, nfail = sweep_tables(tables, k, S5, Ws, per_pat)
        print(f"   5-vertex sweep (all 32 patterns): {nfail} failing games; added {len(fails)} [{time.time()-t0:.1f}s]", flush=True)
        if not fails:
            # confirm with the gate-level evaluator on all patterns (independent code path)
            fails2, nfail2 = cegar5.sweep5(prog, S5, Ws, list(range(32)), max_fail=1)
            if nfail2 == 0:
                print(f"RESULT: program with {k} Cpre gates ({tag}) solves ALL one-player Büchi games with <= 5 vertices. cost={cost(prog)} depth={depth(prog)}")
                json.dump({"n": 5, "k": k, "window": window, "result": "SAT-verified", "program": prog, "tables": tables}, open(f"cegar5_{tag}.json", "w"))
                return 0
            fails = fails2
        sub.games.extend(fails)


if __name__ == "__main__":
    sys.exit(main())
