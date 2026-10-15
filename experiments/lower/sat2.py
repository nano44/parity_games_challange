#!/usr/bin/env python3
"""Two-player Büchi: exact B_2(n) by SAT on the quotient Q_n (n <= 3) and CEGAR against all 4-vertex games (n = 4).
Encoding: gate i has a truth table over (P_2, V_E, s_1..s_{i-1}); s_i(c) = OR (Even owner) / AND (Odd owner) over successors
of y_i; output table over (P_2, V_E, s_1..s_k) must equal W.  Usage: sat2.py exact n kmax | sat2.py cegar4 k [per_round]"""
import sys, os, time, json
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pysat.solvers import Cadical153
from quotient import build
from slp import Struct, eval_struct, cost, depth
import vec2, zielonka
from games import to_game


def encode2(S, W, nodes, k):
    lab2 = S.prio == 2; labE = S.owner == 0
    nv = [0]
    def new():
        nv[0] += 1; return nv[0]
    t, s, y = {}, {}, {}
    for i in range(1, k + 2):
        for e in range(2 ** (i + 1)):
            t[(i, e)] = new()
    for i in range(1, k + 1):
        for c in nodes:
            s[(i, c)] = new(); y[(i, c)] = new()
    cl = []
    for c in nodes:
        base = (1 if lab2[c] else 0) | (2 if labE[c] else 0)
        for i in range(1, k + 2):
            for e in range(2 ** (i + 1)):
                if (e & 3) != base:
                    continue
                neg = []
                for j in range(1, i):
                    bit = (e >> (j + 1)) & 1
                    neg.append(-s[(j, c)] if bit else s[(j, c)])
                tv = t[(i, e)]
                if i <= k:
                    cl.append(neg + [-y[(i, c)], tv]); cl.append(neg + [y[(i, c)], -tv])
                else:
                    cl.append(neg + ([tv] if W[c] else [-tv]))
    for i in range(1, k + 1):
        for c in nodes:
            succ = [int(r) for r in S.indices[S.indptr[c]:S.indptr[c + 1]]]
            ys = [y[(i, r)] for r in succ]
            if labE[c]:
                cl.append([-s[(i, c)]] + ys)
                for yr in ys: cl.append([s[(i, c)], -yr])
            else:
                cl.append([s[(i, c)]] + [-yr for yr in ys])
                for yr in ys: cl.append([-s[(i, c)], yr])
    solver = Cadical153(bootstrap_with=cl)
    def decode(model):
        m = set(v for v in model if v > 0)
        return [[int(t[(i, e)] in m) for e in range(2 ** (i + 1))] for i in range(1, k + 2)]
    return solver, decode, len(cl)


def program_from_tables2(tables, k):
    prog = [("P", 2), ("VE",), ("EMPTY",)]
    s_gate = {}
    def lit(j, bit):
        base = 0 if j == 0 else (1 if j == 1 else s_gate[j - 1])
        if bit: return base
        prog.append(("not", base)); return len(prog) - 1
    def table_gate(i, tab):
        acc = 2
        for e in range(len(tab)):
            if not tab[e]: continue
            term = None
            for j in range(i + 1):
                g = lit(j, (e >> j) & 1)
                if term is None: term = g
                else: prog.append(("and", term, g)); term = len(prog) - 1
            prog.append(("or", acc, term)); acc = len(prog) - 1
        return acc
    for i in range(1, k + 1):
        a = table_gate(i, tables[i - 1]); prog.append(("cpre", a)); s_gate[i] = len(prog) - 1
    out = table_gate(k + 1, tables[k]); prog.append(("or", out, out))
    return prog


def exact(n, kmax):
    q = build(n, owners_set=(0, 1), verbose=True)
    for k in range(0, kmax + 1):
        t0 = time.time()
        solver, decode, ncl = encode2(q.S, q.W, list(range(q.N)), k)
        ok = solver.solve()
        print(f"  n={n} k={k}: {ncl} clauses -> {'SAT' if ok else 'UNSAT'} [{time.time()-t0:.1f}s]", flush=True)
        if ok:
            prog = program_from_tables2(decode(solver.get_model()), k)
            assert (eval_struct(prog, q.S) == q.W).all()
            json.dump({"n": n, "B2": k, "program": prog}, open(f"min_b2_n{n}.json", "w"))
            print(f"B_2({n}) = {k} (witness verified on Q_{n}, cost {cost(prog)} depth {depth(prog)})")
            return k
    print(f"B_2({n}) > {kmax}")


class Sub:
    def __init__(self, q3):
        self.q3 = q3; self.games = []
    def struct(self):
        owner = list(self.q3.S.owner); prio = list(self.q3.S.prio)
        succ = [list(self.q3.S.indices[self.q3.S.indptr[c]:self.q3.S.indptr[c + 1]]) for c in range(self.q3.N)]
        W = list(self.q3.W)
        for raw in self.games:
            base = len(owner); pr, ow, sc = raw
            owner.extend(ow); prio.extend(pr); succ.extend([[base + w for w in s] for s in sc])
            z = zielonka.solve(to_game(raw)); W.extend([z[v] == 0 for v in range(len(pr))])
        return Struct(owner, prio, succ), np.array(W, dtype=bool)


def cegar4(k, per_round=400):
    tag = f"b2_n4_k{k}"
    q3 = build(3, owners_set=(0, 1), verbose=True)
    S4, ve4, p24 = vec2.all_games(4); W4 = vec2.ref_W(S4, ve4, p24, 4)
    print(f"all 4-vertex two-player games: {len(S4)}", flush=True)
    sub = Sub(q3)
    ckpt = f"{tag}.subset.json"
    if os.path.exists(ckpt):
        sub.games = [tuple((tuple(g[0]), tuple(g[1]), tuple(tuple(x) for x in g[2]))) for g in json.load(open(ckpt))]
        print(f"resumed {len(sub.games)} games", flush=True)
    rnd = 0
    while True:
        rnd += 1
        json.dump(sub.games, open(ckpt, "w"))
        S, W = sub.struct(); t0 = time.time()
        solver, decode, ncl = encode2(S, W, list(range(S.N)), k)
        ok = solver.solve()
        print(f"round {rnd}: subset {S.N} nodes ({len(sub.games)} games), {ncl} clauses -> {'SAT' if ok else 'UNSAT'} [{time.time()-t0:.1f}s]", flush=True)
        if not ok:
            print(f"RESULT: no program with {k} Cpre gates solves all two-player Büchi games with <= 4 vertices (UNSAT on a successor-closed subset).")
            json.dump({"k": k, "result": "UNSAT", "subset_games": sub.games}, open(f"{tag}.json", "w")); return 1
        tables = decode(solver.get_model()); del solver
        t0 = time.time()
        out = vec2.eval_tables(tables, k, S4, ve4, p24, 4)
        bad = np.nonzero(out != W4)[0]
        print(f"   sweep over all 4-vertex games: {len(bad)} failing [{time.time()-t0:.1f}s]", flush=True)
        if len(bad) == 0:
            prog = program_from_tables2(tables, k)
            # independent confirmation with the gate-level evaluator on the quotient Q_4? (not built); on random games vs Zielonka
            rng = np.random.default_rng(1); bad2 = 0
            for gi in rng.choice(len(S4), 100000, replace=False):
                raw = vec2.game_at(S4, ve4, p24, gi, 4); z = zielonka.solve(to_game(raw))
                from slp import eval_game
                m = eval_game(prog, to_game(raw))
                bad2 += any(((m >> v) & 1) != (z[v] == 0) for v in range(4))
            print(f"RESULT: program with {k} Cpre gates solves ALL two-player Büchi games with <= 4 vertices ({len(S4)} games; gate-level re-check vs Zielonka on 100000 random games: {bad2} mismatches). cost={cost(prog)} depth={depth(prog)}")
            json.dump({"n": 4, "k": k, "result": "SAT-verified", "program": prog, "tables": tables}, open(f"{tag}.json", "w")); return 0
        pick = bad if len(bad) <= per_round else rng_pick(bad, per_round, rnd)
        sub.games.extend(vec2.game_at(S4, ve4, p24, int(gi), 4) for gi in pick)


def rng_pick(bad, m, seed):
    return np.random.default_rng(seed).choice(bad, m, replace=False)


if __name__ == "__main__":
    if sys.argv[1] == "exact":
        exact(int(sys.argv[2]), int(sys.argv[3]))
    else:
        sys.exit(cegar4(int(sys.argv[2]), int(sys.argv[3]) if len(sys.argv) > 3 else 400))
