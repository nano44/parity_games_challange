"""L-ALG succ. 6 (produced on Opus 5.5, 2026-10-17 box 6), GAP-C §18h (FM): hill-climb on real A_DTL runs (dtl_pyref, order
datum DTL_ORDER) for a −1 call whose final region union is not inside an earlier round's union. Fitness of a run: the
largest r'/f over the −1 calls and the round pairs r < r' with Z^{r'} ⊄ Z^r (a deficit vertex that reappears at round r');
an FM failure is r' = f (fitness 1.0, then the size of Z_f \\ Z^r breaks ties). Mutations: an edge added or removed, a
priority moved by ±1, an owner flipped. Usage: dtl_fmclimb.py START.pg SEED STEPS OUTDIR"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_pnl as PN, dtl_step5 as S5


def fitness(g):
    d0 = S5.build(g); d = PN.PN(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx
    d.trace = []; d.tab = {}; d.shown = 99; d.fname = "climb"; d.last_rounds = []; d.cur_new = []; d.kd = 99; d.margins = []
    best = [0.0, 0]
    orig = d.note_rounds
    def note(res, d=d):
        rs = d.rounds
        if res == -1 and len(rs) > 1:
            f = len(rs)
            for r in range(f):
                for r2 in range(r + 1, f):
                    if not rs[r2] <= rs[r]:
                        sc = (r2 + 1) / f; extra = len(rs[-1] - rs[r]) if r2 == f - 1 else 0
                        if (sc, extra) > tuple(best): best[0], best[1] = sc, extra
        orig(res)
    d.note_rounds = note
    sys.setrecursionlimit(100000)
    try:
        d.run()
    except Exception:
        return (-1.0, 0), d
    complete = all(w is not None for w in d.win)
    return ((best[0], best[1]) if complete else (2.0, 0)), d


def mutate(g, rnd):
    pr, ow, su = list(g.prio), list(g.owner), [list(s) for s in g.succ]; n = g.n; k = rnd.randrange(4)
    v = rnd.randrange(n)
    if k == 0: su[v] = sorted(set(su[v]) | {rnd.randrange(n)})
    elif k == 1 and len(su[v]) > 1: su[v].remove(rnd.choice(su[v]))
    elif k == 2: pr[v] = max(0, pr[v] + rnd.choice([-1, 1]))
    else: ow[v] = 1 - ow[v]
    return pg.Game(pr, ow, su)


if __name__ == "__main__":
    start, seed, steps, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    rnd = random.Random(seed); g = pg.read(start); fg, _ = fitness(g); os.makedirs(out, exist_ok=True)
    print("start", fg, flush=True)
    for it in range(steps):
        h = mutate(g, rnd); fh, _ = fitness(h)
        if fh[0] >= 2.0:
            pg.write(h, os.path.join(out, f"incomplete_{seed}_{it}.pg")); print("INCOMPLETE RUN", it, flush=True); continue
        if fh >= fg:
            if fh > fg: print("step", it, "fitness", fh, flush=True)
            g, fg = h, fh
            if fg[0] >= 1.0:
                pg.write(g, os.path.join(out, f"fm_viol_{seed}_{it}.pg")); print("FM FAILS", it, fg, flush=True); break
    pg.write(g, os.path.join(out, f"fm_last_{seed}.pg")); print("end", fg, flush=True)
