"""L-RED successor 9 (box 14, produced on Opus 5.5): climb for a (CHAIN-CHANGE) violation at the transition into the FINAL
search of the last q-phase (a search that learns nothing; R42 §3 route (γ)). Score: (identical-chain q-transitions anywhere,
-dist of the last transition of the last q-phase, length of that phase). dist as in chainchg.py.
Usage: DTL_ORDER=.. chainfin.py G.pg ... | chainfin.py climb C START.pg STEPS SEED OUTDIR"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xscore as X, chainchg as CC


def score(g, order, C):
    d = X.B.run(g, order); q = 1 - C; phases = {}
    for ph, calls in getattr(d, "log", []): phases.setdefault(ph, []).append(X.states(X.B.chain(calls, g.n)))
    Q = [ph for ph in phases if ph[0] == q]
    ident = sum(1 for ph in Q for s in range(len(phases[ph]) - 1) if CC.dist(phases[ph][s], phases[ph][s + 1], g.n) == 0)
    if not Q: return (ident, -99, 0)
    L = phases[max(Q, key=lambda ph: ph[1])]
    return (ident, -round(CC.dist(L[-2], L[-1], g.n), 3) if len(L) > 1 else -99, len(L))


def climb(C, start, steps, seed, out, order):
    rnd = random.Random(seed); g = X.distinct(X.pg.read(start)); os.makedirs(out, exist_ok=True)
    sg = score(g, order, C); print("start", sg, flush=True); GROW = float(os.environ.get("GROW", "0"))
    for it in range(steps):
        h = X.grow(g, C, rnd) if GROW and g.n < 60 and rnd.random() < GROW else X.mutate(g, C, g.n + 2, rnd)
        if h is None: continue
        h = X.distinct(h)
        try:
            sh = score(h, order, C)
        except RecursionError:
            continue
        if sh >= sg:
            if sh > sg:
                print(it, sh, flush=True); X.pg.write(h, os.path.join(out, f"best_C{C}_s{seed}.pg"))
                if sh[0] > 0: X.pg.write(h, os.path.join(out, f"CHG_VIOL_C{C}_n{h.n}_s{seed}_{it}.pg")); print("VIOLATION", it, flush=True)
            g, sg = h, sh
    print("final", sg)


if __name__ == "__main__":
    sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable")
    if sys.argv[1] == "climb":
        climb(int(sys.argv[2]), sys.argv[3], int(sys.argv[4]), int(sys.argv[5]), sys.argv[6], order); sys.exit(0)
    for f in sys.argv[1:]:
        g = X.distinct(X.pg.read(f)); C = X.controller(g)
        print(os.path.basename(f), "score", score(g, order, C) if C is not None else "NOT IN CLASS")
