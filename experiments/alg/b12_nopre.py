"""L-ALG succ. 10 (box 12, produced on Opus 5.5), GAP-A-M §31: (NO-PRE-a) "a vertex y of a tangle t that fired at top τ in round r
of visit i (context R, phase fixed) is never a round-r top above τ at visit i+1". Such a y has pr(y) = pr(τ), index above τ, and was
pruned at visit i in a round r′ < r (else it would lie in an earlier round-r region and t could not fire at τ).
Graded counts per run (model fixd_stealentry.SE, with V recorded at the start of every round):
  pre    the precondition itself (y is a round-r top at visit i+1)
  near   y ∈ V_r(i+1): y survives to round r at the next visit (a top, or attracted into an earlier region)
  surv   y survives at visit i+1 to the round r′ in which it was pruned at visit i (it is NOT pruned there again)
  gap    max over these y of (first round without y at visit i+1) − (first round without y at visit i); surv ⇔ gap ≥ 1
  above  tie-above events: a fired t holds a same-priority y above τ
Modes: scan G.pg ...  |  climb N P STEPS SEED OUTDIR [START.pg]  (two-player games, class-free moves of fixd_oneplayer.mutate
with ONEP_ANY=1; score (pre, near, surv, gap, above); a run with pre ≥ 1 is written to OUTDIR)."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, fixd_stealentry as SE
from fixd_oneplayer import start, mutate


class NP(SE.SE):
    def best_vertices(self, V, R, p):
        self._vr = []
        V.clear(); V.update(v for v in R if self.pr[v] % 2 == p)
        if not V:
            return 0
        rounds = []
        if not hasattr(self, "visits"): self.visits = []; self.vrs = []
        self.visits.append((self.phase, frozenset(R), p, rounds)); self.vrs.append(self._vr)
        while True:
            prevV = set(V); self._vr.append(frozenset(V))
            Z = set(); CurR = set(R); steps = []
            for top in range(self.n - 1, -1, -1):
                if top not in V or top in Z:
                    continue
                CurZ = {top}; self.Q = [top]; self._rec = {top: ("top",)}; self._fired = set(); pref = frozenset(Z)
                self.tattr(p, CurZ, CurR, CurR, self.pr[top], CurR)
                steps.append((top, pref, dict(self._rec), set(self._fired)))
                self._rec = None
                Z |= CurZ
            rounds.append(steps)
            cand = [v for v in sorted(V, reverse=True) if not self.attracts(p, v, Z, R)]
            if not cand:
                return 1
            for t in [0] + [q for q in self.prios if q > 0 and q <= self.maxpr]:
                self.Q = sorted(Z)
                self.tattr(p, Z, R, R, t, None)
                keep = []
                for i, u in enumerate(cand):
                    if self.pr[u] <= t:
                        keep += cand[i:]; break
                    if not self.attracts(p, u, Z, R):
                        keep.append(u)
                cand = keep
            V -= set(cand)
            if not cand:
                return 1
            if not V:
                V.clear(); V.update(prevV)
                return -1


def run(g, order):
    saved = SE.SE
    SE.SE = NP
    try:
        return SE.run(g, order)
    finally:
        SE.SE = saved


def counts(d):
    by = {}
    for k, (ph, R, p, rounds) in enumerate(d.visits): by.setdefault((ph, R), []).append(k)
    pre = near = surv = above = 0; gap = -99; ex = None
    for key, ks in by.items():
        for a, b in zip(ks, ks[1:]):
            ra, rb, va, vb = d.visits[a][3], d.visits[b][3], d.vrs[a], d.vrs[b]
            for r, steps in enumerate(ra):
                tops_b = {s[0] for s in rb[r]} if r < len(rb) else set()
                for top, _, _, fz in steps:
                    for t in fz:
                        for y, _ in d.tv[t]:
                            if not (y > top and d.pr[y] == d.pr[top]): continue
                            above += 1
                            rp = next((k for k in range(len(va)) if y not in va[k]), None)    # first round without y at visit i
                            if rp is not None and rp < len(vb) and y in vb[rp]: surv += 1
                            if rp is not None:
                                rq = next((k for k in range(len(vb)) if y not in vb[k]), len(vb) + 1)   # first round without y at i+1
                                gap = max(gap, rq - rp)
                            if r < len(vb) and y in vb[r]: near += 1
                            if y in tops_b:
                                pre += 1
                                if ex is None: ex = (key[0], len(key[1]), a, b, r, top, y, sorted(v for v, _ in d.tv[t]))
    return (pre, near, surv, gap, above), ex


if __name__ == "__main__":
    sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable")
    if sys.argv[1] == "scan":
        tot = [0, 0, 0, -99, 0]
        for f in sys.argv[2:]:
            try:
                g = pg.read(f)
            except ValueError:
                continue
            c, ex = counts(run(g, order)); tot = [max(x, y) if k == 3 else x + y for k, (x, y) in enumerate(zip(tot, c))]
            if c[0]: print("PRECONDITION", f, c, ex, flush=True)
        print("order", order, "files", len(sys.argv) - 2, "(pre, near, surv, max gap, above)", tot)
    else:
        os.environ["ONEP_ANY"] = "1"                      # class-free moves (two-player games); set here only, not at import
        N, P, steps, seed = (int(a) for a in sys.argv[2:6]); out = sys.argv[6]; rnd = random.Random(seed); os.makedirs(out, exist_ok=True)
        g = pg.read(sys.argv[7]) if len(sys.argv) > 7 else start(0, N, P, rnd); P = max(P, max(g.prio) + 1)
        sg, _ = counts(run(g, order))
        for it in range(steps):
            h = mutate(g, 0, P, rnd)
            if h is None: continue
            try:
                sh, ex = counts(run(h, order))
            except RecursionError:
                continue
            if sh >= sg:
                if sh > sg: print(it, sh, flush=True)
                g, sg = h, sh
                if sg[0] >= 1:
                    fn = os.path.join(out, f"nopre_viol_n{g.n}_s{seed}.pg"); pg.write(g, fn); print("PRECONDITION", sg, ex, fn, flush=True); break
        fn = os.path.join(out, f"nopre_final_n{g.n}_s{seed}.pg"); pg.write(g, fn); print("final", sg, fn)
