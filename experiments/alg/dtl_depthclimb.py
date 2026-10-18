"""L-ALG succ. 7 (produced on Opus 5.5, 2026-10-17 box 8): self-attack on (STEAL-DEPTH_1) (GAP-A-M §23g). Hill climb by
edge mutation (add, delete or redirect one edge, never leaving a vertex without a successor) from a start game. Fitness
(dtl_stealdepth.analyze, both order data): 1e6 * incomplete + 1e4 * max depth + 1e2 * max k + (#re-steals). The climb
keeps ties, so it drifts. A new best is written to OUT_DIR/best_<tag>.pg with its scores. Every reported instance must be
re-run with pinned Oink and dtl_stealdepth.py.
Usage: RM_EXCL=1 RM_PREF=1 RM_LIGHT=1 RM_DV=0 dtl_depthclimb.py START.pg OUT_DIR TAG SEED STEPS"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_stealdepth as SD


def score(g):
    tot = 0; info = []
    for order in ("stable", "oink"):
        d = SD.run_game(g, order); inc = not all(w is not None for w in d.win)
        t = {}; mk, md, nc = SD.analyze(d, "", t)
        nre = sum(v for k, v in t.items() if k.startswith("RE-STEAL"))
        tot = max(tot, 1e6 * inc + 1e4 * md + 1e2 * mk + nre); info.append((order, int(inc), mk, md, nre, nc))
    return tot, info


def mutate(g, rnd):
    succ = [list(s) for s in g.succ]; n = len(succ); u = rnd.randrange(n); op = rnd.random()
    if op < 0.4:
        succ[u] = sorted(set(succ[u]) | {rnd.randrange(n)})
    elif op < 0.7 and len(succ[u]) > 1:
        succ[u].remove(rnd.choice(succ[u]))
    else:
        w = rnd.choice(succ[u]); succ[u].remove(w); succ[u] = sorted(set(succ[u]) | {rnd.randrange(n)})
    return pg.Game(list(g.prio), list(g.owner), succ)


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    start, outd, tag, seed, steps = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5])
    rnd = random.Random(seed); g = pg.read(start); best, info = score(g); cur = best
    print(f"start {best} {info}", flush=True)
    for it in range(steps):
        h = mutate(g, rnd)
        try: sc, inf = score(h)
        except RecursionError: continue
        except Exception as ex:
            print(f"it {it} EXCEPTION {type(ex).__name__}: {ex}", flush=True); pg.write(h, os.path.join(outd, f"exc_{tag}_{it}.pg")); continue
        if sc >= cur:
            g, cur = h, sc
            if sc > best:
                best = sc; pg.write(g, os.path.join(outd, f"best_{tag}.pg"))
                print(f"{time.strftime('%H:%MZ', time.gmtime())} it {it} NEW BEST {best} {inf}", flush=True)
                if inf[0][1] or inf[1][1]: print("INCOMPLETE RUN FOUND", flush=True)
