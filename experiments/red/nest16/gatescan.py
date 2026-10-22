"""L-RED box 19 (produced on Fable 5.1): evaluate hand-built GATE + RETURN configurations on a union BASE ⊎ E (E placed above, as
pairunion 'above'). A config line is ';'-separated ops: 'move:v:prio' (set v's priority; parity kept by the caller),
'edge:u:v' (add the edge u -> v; u must be a C-vertex). Per config (one order): S, |P|, I, NEST*, P, the indices of transitions whose
first changed piece lies in E (part letter = last), the innermost witness window [a, b] of P, and how many E-transitions fall
strictly inside it. Chains from L-ALG's unmodified b12_pot / b12_core (via ../xctx/xscore.py). Solver sets are mapped back to
file ids as in piecemap.py. Usage: DTL_ORDER=.. gatescan.py BASE.pg E.pg OUTDIR CONFIGS.txt [cut1 cut2 ...]
(cuts label BASE's parts; E is the last part). Writes OUTDIR/<i>.pg for every config and prints one line per config."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "xctx")); sys.setrecursionlimit(100000)
import xscore as X
from comb.neststar import nest_star
B = X.B; pg = X.pg; order = os.environ.get("DTL_ORDER", "stable")


def above(b, a):
    mb = max(b.prio); sh = mb + 2 + (mb % 2)
    return pg.Game(list(b.prio) + [p + sh for p in a.prio], list(b.owner) + list(a.owner),
                   [list(s) for s in b.succ] + [[w + b.n for w in s] for s in a.succ])


def wit(Q):
    best = None
    for p in sorted({x for x, _ in Q}):
        idx = [i for x, i in Q if x == p]
        if len(idx) < 2: continue
        gap = [(x, i) for x, i in Q if idx[0] < i < idx[-1] and x > p]
        d = 1 + (nest_star(tuple(x for x, _ in gap)) if gap else 0)
        if best is None or d > best[0]: best = (d, p, idx[0], idx[-1], gap)
    if best is None: return []
    return [(best[1], best[2], best[3])] + wit(best[4])


def evaluate(g, C, cuts):
    g = X.distinct(g); d = B.run(g, order)
    idx = __import__("stdsort").oink_order(g.prio) if order == "oink" else sorted(range(g.n), key=lambda v: (g.prio[v], v))
    part = lambda v: chr(65 + next(k for k, c in enumerate(cuts) if v < c))
    L = [X.states(B.chain(calls, g.n)) for ph, calls in d.log if ph[0] == 1 - C]
    P = []; Epos = []; labs = []
    for i, (x, y) in enumerate(zip(L, L[1:])):
        p0 = next((p for p in range(max(len(x), len(y))) if p >= len(x) or p >= len(y) or x[p] != y[p]), None)
        if p0 is None: continue
        pc = set(y[p0][3] if p0 < len(y) else ()) | set(x[p0][3] if p0 < len(x) else ())
        lab = "".join(sorted({part(idx[v]) for v in pc})) or "-"
        P.append(p0); labs.append(lab)
        if lab == chr(64 + len(cuts)): Epos.append(len(P) - 1)
    W = wit(list(zip(P, range(len(P))))); a, b = (W[-1][1], W[-1][2]) if W else (-1, -1)
    inside = sum(1 for i in Epos if a < i < b)
    return dict(S=len(L), P=P, I=len(L) - 1 - len(P), nest=nest_star(tuple(P)), E=Epos, win=(a, b), inside=inside, labs=labs, wit=W)


if __name__ == "__main__":
    base = pg.read(sys.argv[1]); E = pg.read(sys.argv[2]); out = sys.argv[3]; cfgs = [l.strip() for l in open(sys.argv[4]) if l.strip()]
    cuts = [int(x) for x in sys.argv[5:]] + [base.n, base.n + E.n]
    g0 = above(base, E); C = X.controller(g0); os.makedirs(out, exist_ok=True)
    print(f"# base {os.path.basename(sys.argv[1])} E {os.path.basename(sys.argv[2])} n {g0.n} C {C} order {order} cuts {cuts}", flush=True)
    for i, cfg in enumerate(cfgs):
        prio = list(g0.prio); succ = [list(s) for s in g0.succ]
        for op in cfg.split(";"):
            f = op.split(":")
            if f[0] == "move": prio[int(f[1])] = int(f[2])
            elif f[0] == "edge":
                u, v = int(f[1]), int(f[2])
                if g0.owner[u] != C: print(f"{i} {cfg} SKIP: {u} not a C-vertex", flush=True); break
                if v not in succ[u]: succ[u] = sorted(succ[u] + [v])
        else:
            h = pg.Game(prio, list(g0.owner), succ)
            if not X.inclass(h, C): print(f"{i} {cfg} NOT IN CLASS", flush=True); continue
            try:
                r = evaluate(h, C, cuts)
            except RecursionError:
                print(f"{i} {cfg} RECURSION", flush=True); continue
            pg.write(h, os.path.join(out, f"{i}.pg"))
            print(f"{i} {cfg} S {r['S']} |P| {len(r['P'])} I {r['I']} NEST* {r['nest']} win {r['win']} Etrans {r['E']} inside {r['inside']} P {','.join(map(str, r['P']))} labs {'.'.join(r['labs'])}", flush=True)
