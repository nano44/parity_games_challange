"""L-ALG succ. 8 (produced on Opus 5.5, 2026-10-18 box 10): self-attack on (EXIT_c) with c = 2 (GAP-A-M §23r, §23w). Hill climb by
edge mutation (dtl_depthclimb.mutate) from a start game. Fitness (both order data, max): 1e6 * incomplete + 1e4 * max exits
per (step, vertex) on the §23t grid (dtl_drthr conventions, virtual end-of-round step included) + 1e2 * max round-count falls
per context (dtl_roundfalls) + #(step, vertex) pairs with 2 exits. Ties kept (drift). A new best is written to
OUT_DIR/best_<tag>.pg. Any exits ≥ 3 or INCOMPLETE goes to the Lead at once, after a pinned-Oink re-run and dtl_drthr.py.
Usage: RM_LIGHT=1 RM_DV=0 dtl_exitclimb.py START.pg OUT_DIR TAG SEED STEPS"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_drthr as DT, dtl_depthclimb as DC
FD = DT.FD


def analyze(g, order):
    d0 = FD.P.X.build(g); d = DT.DR(d0.pr, d0.ow, d0.outs, ins_desc=(order == "oink")); d.idx = d0.idx; d.run()
    inc = int(not all(w is not None for w in d.win)); mx = 0; n2 = 0; rf = 0
    for ph in FD.phase_rows(d):
        visits = {}
        for r_ in ph:
            for rc in r_["recs"]: visits.setdefault(rc["key"], []).append(rc)
        for key_, vl in visits.items():
            if len(vl) < 2: continue
            R = key_[1]; p = vl[0]["p"]; grid = sorted(v for v in R if d.pr[v] % 2 == p)
            if not grid: continue
            nr = len(R) + 1; gs = [DT.grid_tops(rc, nr) for rc in vl]; ex = {}
            for i in range(len(gs) - 1):
                for r in range(nr):
                    for w in set(gs[i][r]) | set(gs[i + 1][r]):
                        tx, ty = gs[i][r].get(w, -1), gs[i + 1][r].get(w, -1)
                        if tx > ty:
                            for t in grid:
                                if ty <= t < tx: ex[(r, t, w)] = ex.get((r, t, w), 0) + 1
                            if ty == -1: ex[(r, "U", w)] = ex.get((r, "U", w), 0) + 1
            if ex: mx = max(mx, max(ex.values())); n2 += sum(1 for v in ex.values() if v >= 2)
            seq = [len(rc.get("rtop", [])) for rc in vl]; rf = max(rf, sum(1 for a, b in zip(seq, seq[1:]) if b < a))
    return inc, mx, rf, n2


def score(g):
    tot = 0; info = []
    for order in ("stable", "oink"):
        inc, mx, rf, n2 = analyze(g, order)
        tot = max(tot, 1e6 * inc + 1e4 * mx + 1e2 * rf + n2); info.append((order, inc, mx, rf, n2))
    return tot, info


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    start, outd, tag, seed, steps = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5])
    rnd = random.Random(seed); g = pg.read(start); best, info = score(g); cur = best
    print(f"start {best} {info}", flush=True)
    for it in range(steps):
        h = DC.mutate(g, rnd)
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
                if inf[0][2] >= 3 or inf[1][2] >= 3: print("EXITS >= 3 FOUND", flush=True)
    print(f"{time.strftime('%H:%MZ', time.gmtime())} done best {best}", flush=True)
