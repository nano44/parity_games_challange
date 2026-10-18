"""L-RED successor 9 (box 14 item 2, produced on Opus 5.5): graded climb against (TREE-PIECE⁺) (L-ALG GAP-A-M §36a, l-alg 5eb1b4bd)
in TWO-PLAYER games. Uses L-ALG's b12_ident.run / treepieces UNMODIFIED; PLUS semantics exactly as b12_ident.tp_score (transitions
whose call sequence (depth, R, rank, V) is identical are skipped).
Per counted transition s -> s+1: K = treepieces(s+1), new = K - seen (keys held at searches <= s of the phase).
  nv   = #vertices with a new key (L-ALG's margin; 0 = VIOLATION)
  nk   = |new|
  dist = Σ over new keys of the min, over seen keys of the same vertex, of the number of differing key components (6 if none)
  fall = 1 if the transition's first differing call has the same (depth, R) and a LOWER rank (outcome falls at a fixed input, §36b S4)
Score: (violations, -min nv, -min nk at a min-nv transition, -min dist there, #fall transitions, transitions).
Usage: [LALG_DIR=..] DTL_ORDER=.. tpclimb.py G.pg ...  |  tpclimb.py climb START.pg STEPS SEED OUTDIR [GROW=p]"""
import sys, os, random
os.environ["ONEP_ANY"] = "1"                       # two-player moves in fixd_oneplayer.mutate (no class restriction)
LALG = os.environ.get("LALG_DIR", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
A = os.path.join(LALG, "experiments", "alg"); sys.path.insert(0, A); sys.path.insert(0, os.path.join(A, "..", "harness"))
import pg, b12_ident as I
from fixd_oneplayer import mutate


def rank(res, e, n): return n + 2 if res == 1 else (e if res == -1 else 0)


def analyse(g, order):
    d = I.run(g, order); log = getattr(d, "log", []); allc = getattr(d, "allc", {}); seen = set(); prev = None; pcalls = None
    out = []
    for ph, calls in log:
        Ac = allc.get(id(calls), []); k = I.treepieces(Ac, g.n)
        if prev == ph and Ac != pcalls:
            new = k - seen; nv = len({x[0] for x in new}); byv = {}
            for x in seen: byv.setdefault(x[0], []).append(x)
            dist = sum(min([sum(a != b for a, b in zip(x[1:], y[1:])) for y in byv.get(x[0], [])] or [6]) for x in new)
            i = next((j for j in range(min(len(Ac), len(pcalls))) if Ac[j] != pcalls[j]), None)
            fall = int(i is not None and Ac[i][:2] == pcalls[i][:2] and rank(*Ac[i][2:4], g.n) < rank(*pcalls[i][2:4], g.n))
            out.append(dict(ph=ph, nv=nv, nk=len(new), dist=dist, fall=fall))
        elif prev != ph:
            seen = set()
        seen |= k; prev = ph; pcalls = Ac
    return out, d


def score(g, order):
    T = analyse(g, order)[0]
    if not T: return (0, -99, -99, -99, 0, 0)
    m = min(t["nv"] for t in T); M = [t for t in T if t["nv"] == m]; mk = min(t["nk"] for t in M)
    return (sum(t["nv"] == 0 for t in T), -m, -mk, -min(t["dist"] for t in M if t["nk"] == mk), sum(t["fall"] for t in T), len(T))


def grow(g, rnd):
    n = g.n; prio = list(g.prio) + [rnd.randrange(max(g.prio) + 2)]; owner = list(g.owner) + [rnd.randint(0, 1)]
    succ = [list(x) for x in g.succ] + [sorted(set(rnd.sample(range(n + 1), min(n + 1, rnd.randint(1, 3)))))]
    v = rnd.randrange(n); succ[v] = sorted(set(succ[v] + [n]))
    return pg.Game(prio, owner, succ)


def climb(start, steps, seed, out, order):
    rnd = random.Random(seed); g = pg.read(start); os.makedirs(out, exist_ok=True); sg = score(g, order); print("start", sg, flush=True)
    GROW = float(os.environ.get("GROW", "0")); NMAX = int(os.environ.get("NMAX", "80"))
    for it in range(steps):
        h = grow(g, rnd) if GROW and g.n < NMAX and rnd.random() < GROW else mutate(g, 0, max(g.prio) + 2, rnd)
        if h is None: continue
        try:
            sh = score(h, order)
        except RecursionError:
            continue
        if sh >= sg:
            if sh > sg:
                print(it, sh, flush=True); pg.write(h, os.path.join(out, f"best_s{seed}.pg"))
                if sh[0] > 0: pg.write(h, os.path.join(out, f"TPP_VIOL_n{h.n}_s{seed}_{it}.pg")); print("VIOLATION", it, flush=True)
            g, sg = h, sh
    print("final", sg)


if __name__ == "__main__":
    sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable")
    if sys.argv[1] == "climb":
        climb(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5], order); sys.exit(0)
    for f in sys.argv[1:]:
        g = pg.read(f); print(os.path.basename(f), "n", g.n, order, "score", score(g, order))
