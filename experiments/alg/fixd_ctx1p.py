"""L-ALG succ. 9 (box 11, produced on Opus 5.5), GAP-A-M §27c: (CTX⁺) inside the class 𝒞^1P (one-player games, controller C,
priorities made ALL-DISTINCT after every move; Lemma NOSTEAL-1P needs only the q-parity ones distinct). Hill-climb with
dtl_ctxclimb.fitness (#distinct first-difference best_vertices contexts in a phase, transitions, -|G'|) under DTL_ORDER, with the
class-preserving moves of fixd_oneplayer.mutate. Every improvement is also checked against Lemma NOSTEAL-1P (max k must be 0,
dtl_stealdepth model) and Zielonka; a violation is printed as NOSTEAL-VIOLATION and saved.
Usage: DTL_ORDER=oink|stable fixd_ctx1p.py C START.pg|random:N:P STEPS SEED OUTDIR"""
import sys, os, random
os.environ.setdefault("RM_DV", "0"); os.environ.setdefault("RM_LIGHT", "1")
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_ctxclimb as CC
from fixd_oneplayer import start, mutate, inclass


def distinct(g):
    seq = sorted(range(g.n), key=lambda v: (g.prio[v], v)); q = {}; last = None
    for v in seq:
        q[v] = g.prio[v] % 2 if last is None else q[last] + (2 if g.prio[v] % 2 == q[last] % 2 else 1); last = v
    return pg.Game([q[v] for v in range(g.n)], g.owner, g.succ)


def nosteal_ok(g, order):
    os.environ["RM_EXCL"] = "1"; os.environ["RM_PREF"] = "1"
    import fixd_steal1p as F
    (mk, md, it), ok = F.measure(g, order)
    return mk == 0, ok


def main():
    sys.setrecursionlimit(100000)
    C, src, steps, seed, out = int(sys.argv[1]), sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
    order = os.environ.get("DTL_ORDER", "stable"); rnd = random.Random(seed); os.makedirs(out, exist_ok=True)
    if src.startswith("random:"):
        _, N, P = src.split(":"); g = start(C, int(N), int(P), rnd)
    else:
        g = pg.read(src)
    assert inclass(g, C), "start game not in the class"
    g = distinct(g); fg = CC.fitness(g); print("start", fg, flush=True)
    for it in range(steps):
        h = mutate(g, C, max(g.prio) + 1, rnd)
        if h is None: continue
        h = distinct(h); fh = CC.fitness(h)
        if fh[0] >= 10 ** 6:
            pg.write(h, os.path.join(out, f"incomplete_C{C}_{seed}_{it}.pg")); print("INCOMPLETE RUN", it, flush=True); continue
        if fh >= fg:
            if fh > fg:
                ns, zok = nosteal_ok(h, order)
                print("step", it, "fitness", fh, "nosteal", ns, "zielonka", zok, flush=True)
                if not ns or not zok: pg.write(h, os.path.join(out, f"NOSTEAL_VIOLATION_C{C}_{seed}_{it}.pg"))
                pg.write(h, os.path.join(out, f"ctx1p_best_C{C}_{seed}.pg"))
            g, fg = h, fh
    print("end", fg, flush=True)


if __name__ == "__main__":
    main()
