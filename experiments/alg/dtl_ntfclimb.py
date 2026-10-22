"""L-ALG succ. 6 (produced on Opus 5.5, 2026-10-17 box 6), GAP-C §18h (NT-f): hill-climb on real A_DTL runs for a −1 call
whose FINAL round's region loop accepts a stored tangle (refuting (NT-f), hence (FM)). Fitness: over the −1 calls, the
largest r/f such that round r's region loop accepts a tangle none of whose p-priority vertices is in V_r (such
acceptances happen at intermediate rounds, dtl_ntf.py "INV-T"); 1.0 = an NT-f violation. Mutations as dtl_fmclimb.py.
DTL_ORDER = oink | stable. Usage: dtl_ntfclimb.py START.pg SEED STEPS OUTDIR"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_step5 as S5, dtl_pyref as D, dtl_fmclimb as FC


class C(S5.S5):
    def attractTangle(s, t, p, R, Z, Gx, maxpr):
        r = D.DTL.attractTangle(s, t, p, R, Z, Gx, maxpr)
        if r and s.in_reg:
            if not any(w in s.cur_V for w, _ in s.tv[t] if s.pr[w] % 2 == p): s.late.append(s.rno)
        return r

    def best_vertices(s, V, R, p):
        V.clear(); V.update(v for v in R if s.pr[v] % 2 == p)
        if not V: return 0
        s.late = []; s.rno = 0
        while True:
            prevV = set(V); Z = set(); CurR = set(R); s.rno += 1; s.cur_V = set(V); s.in_reg = True
            for top in range(s.n - 1, -1, -1):
                if top not in V or top in Z: continue
                CurZ = {top}; s.Q = [top]; s.tattr(p, CurZ, CurR, CurR, s.pr[top], CurR); Z |= CurZ
            s.in_reg = False
            cand = [v for v in sorted(V, reverse=True) if not s.attracts(p, v, Z, R)]
            if not cand: return 1
            for t in [0] + [q for q in s.prios if 0 < q <= s.maxpr]:
                s.Q = sorted(Z); s.tattr(p, Z, R, R, t, None); keep = []
                for i, u in enumerate(cand):
                    if s.pr[u] <= t: keep += cand[i:]; break
                    if not s.attracts(p, u, Z, R): keep.append(u)
                cand = keep
            V -= set(cand)
            if not cand: return 1
            if not V:
                V.clear(); V.update(prevV)
                if s.late: s.best = max(s.best, max(s.late) / s.rno)
                return -1


def fitness(g):
    d0 = S5.build(g); d = C(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx
    d.trace = []; d.best = 0.0; d.in_reg = False; d.late = []; d.rno = 0; d.cur_V = set()
    sys.setrecursionlimit(100000)
    try:
        d.run()
    except Exception:
        return -1.0
    return d.best if all(w is not None for w in d.win) else 2.0


if __name__ == "__main__":
    start, seed, steps, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    rnd = random.Random(seed); g = pg.read(start); fg = fitness(g); os.makedirs(out, exist_ok=True); print("start", fg, flush=True)
    for it in range(steps):
        h = FC.mutate(g, rnd); fh = fitness(h)
        if fh >= 2.0: pg.write(h, os.path.join(out, f"incomplete_ntf_{seed}_{it}.pg")); print("INCOMPLETE RUN", it, flush=True); continue
        if fh >= fg:
            if fh > fg: print("step", it, "fitness", fh, flush=True)
            g, fg = h, fh
            if fg >= 1.0: pg.write(g, os.path.join(out, f"ntf_viol_{seed}_{it}.pg")); print("NT-f FAILS", it, flush=True); break
    pg.write(g, os.path.join(out, f"ntf_last_{seed}.pg")); print("end", fg, flush=True)
