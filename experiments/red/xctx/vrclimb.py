"""L-RED successor 9 (box 14, produced on Opus 5.5): graded class climb against (VR-NEW_all) on 𝒞^1P (L-ALG GAP-A-M §32-§33a:
every chain-changing transition of a q-phase gives some vertex a new full key (v, rank_j, j, |R_j|, |V_j|) = b12_pot K-v-all).
Uses b12_pot.run / chain / keys / sig UNMODIFIED, with b12_pot.vr_score's semantics (a transition is tested iff sig changes),
restricted to q-phases (q = 1 - C). Per tested transition: nv = #vertices with a new key, nk = #new keys, dist = Σ over new keys of
the min number of differing components to a held key of the same vertex (5 if none).
Score: (violations, -min nv, -min nk at min nv, -min dist there, tested transitions).
Usage: DTL_ORDER=.. vrclimb.py G.pg ... | [GROW=p] vrclimb.py climb C START.pg STEPS SEED OUTDIR"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xscore as X
B = X.B


def analyse(g, order, C):
    d = B.run(g, order); q = 1 - C; seen = set(); prev = None; out = []
    for ph, calls in getattr(d, "log", []):
        ch = B.chain(calls, g.n); k = B.keys(ch)["K-v-all"]
        if prev is not None and prev[0] == ph and B.sig(ch) != prev[1] and ph[0] == q:
            new = k - seen; byv = {}
            for x in seen: byv.setdefault(x[0], []).append(x)
            dist = sum(min([sum(a != b for a, b in zip(x[1:], y[1:])) for y in byv.get(x[0], [])] or [5]) for x in new)
            out.append(dict(ph=ph, nv=len({x[0] for x in new}), nk=len(new), dist=dist))
        if prev is None or prev[0] != ph: seen = set()
        seen |= k; prev = (ph, B.sig(ch))
    return out, d


def score(g, order, C):
    T = analyse(g, order, C)[0]
    if not T: return (0, -99, -99, -99, 0)
    m = min(t["nv"] for t in T); M = [t for t in T if t["nv"] == m]; mk = min(t["nk"] for t in M)
    return (sum(t["nv"] == 0 for t in T), -m, -mk, -min(t["dist"] for t in M if t["nk"] == mk), len(T))


def climb(C, start, steps, seed, out, order):
    rnd = random.Random(seed); g = X.distinct(X.pg.read(start)); os.makedirs(out, exist_ok=True)
    sg = score(g, order, C); print("start", sg, flush=True); GROW = float(os.environ.get("GROW", "0")); NMAX = int(os.environ.get("NMAX", "60"))
    for it in range(steps):
        h = X.grow(g, C, rnd) if GROW and g.n < NMAX and rnd.random() < GROW else X.mutate(g, C, g.n + 2, rnd)
        if h is None: continue
        h = X.distinct(h)
        try:
            sh = score(h, order, C)
        except RecursionError:
            continue
        if sh >= sg:
            if sh > sg:
                print(it, sh, flush=True); X.pg.write(h, os.path.join(out, f"best_C{C}_s{seed}.pg"))
                if sh[0] > 0: X.pg.write(h, os.path.join(out, f"VRALL_VIOL_C{C}_n{h.n}_s{seed}_{it}.pg")); print("VIOLATION", it, flush=True)
            g, sg = h, sh
    print("final", sg)


if __name__ == "__main__":
    sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable")
    if sys.argv[1] == "climb":
        climb(int(sys.argv[2]), sys.argv[3], int(sys.argv[4]), int(sys.argv[5]), sys.argv[6], order); sys.exit(0)
    for f in sys.argv[1:]:
        g = X.distinct(X.pg.read(f)); C = X.controller(g)
        print(os.path.basename(f), "n", g.n, "C", C, order, "score", score(g, order, C) if C is not None else "NOT IN CLASS")
