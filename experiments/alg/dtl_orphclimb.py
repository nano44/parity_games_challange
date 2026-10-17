"""L-ALG succ. 6 (produced on Opus 5.5, 2026-10-17 box 6), GAP-C §18l/§18n (β'): hill-climb on real A_DTL runs (dtl_pyref,
order datum DTL_ORDER) for a violation of (NO-ORPHAN-pre): an alive stored p-tangle t ⊆ R with no escape in R at a
best_vertices call made before the search's first newly learned tangle. Fitness: the largest share of t's in-G' escapes
that lie outside R, over such calls and tangles (1.0 = a violation; ties broken by the number of such tangles at that
share). Mutations as dtl_fmclimb.py. Usage: dtl_orphclimb.py START.pg SEED STEPS OUTDIR"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_step5 as S5, dtl_pyref as D, dtl_fmclimb as FC


class OC(S5.S5):
    def search(s, p):
        s.T0 = len(s.tv); return S5.S5.search(s, p)

    def best_vertices(s, V, R, p):
        if len(s.tv) == s.T0:
            for i in range(len(s.tv)):
                if s.tpr[i] == -1 or s.tpr[i] % 2 != p: continue
                C = [v for v, _ in s.tv[i]]
                if not all(v in R for v in C): continue
                esc = [e for e in s.tout[i] if e in s.G]
                if not esc: continue
                sh = sum(e not in R for e in esc) / len(esc)
                if sh > s.best[0]: s.best = [sh, 1]
                elif sh == s.best[0]: s.best[1] += 1
        return D.DTL.best_vertices(s, V, R, p)


def fitness(g):
    d0 = S5.build(g); d = OC(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx
    d.trace = []; d.T0 = 0; d.best = [0.0, 0]
    try:
        d.run()
    except Exception:
        return (-1.0, 0)
    if not all(w is not None for w in d.win): return (2.0, 0)
    return tuple(d.best)


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    start, seed, steps, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    rnd = random.Random(seed); g = pg.read(start); fg = fitness(g); os.makedirs(out, exist_ok=True)
    print("start", fg, flush=True)
    for it in range(steps):
        h = FC.mutate(g, rnd); fh = fitness(h)
        if fh[0] >= 2.0:
            pg.write(h, os.path.join(out, f"incomplete_{seed}_{it}.pg")); print("INCOMPLETE RUN", it, flush=True); continue
        if fh >= fg:
            if fh > fg: print("step", it, "fitness", fh, flush=True)
            g, fg = h, fh
            if fg[0] >= 1.0:
                pg.write(g, os.path.join(out, f"orphpre_viol_{seed}_{it}.pg")); print("NO-ORPHAN-pre FAILS", it, fg, flush=True); break
    pg.write(g, os.path.join(out, f"orphpre_last_{seed}.pg")); print("end", fg, flush=True)
