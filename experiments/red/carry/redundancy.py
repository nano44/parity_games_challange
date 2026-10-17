#!/usr/bin/env python3
"""L-RED (produced on Opus 5.5): empirical test of the REDUNDANCY reading used by R10 (MIRROR) and R12 section 6:
"in one best_vertices call, a stored tangle whose top is still in V changes a pruning round only by being lifted into
the region of a different (higher) top" (or by a straddle, i.e. a region-partition effect).
For every pruning round of every best_vertices call of a run, the round is replayed twice from the same V: with all
tangles (FULL) and with every tangle whose top is in V disabled (RED). Rounds whose survivor sets differ are counted and
classified: LIFT if some disabled tangle fired, in FULL, inside the region of a top other than its own; OTHER otherwise.
An OTHER contradicts the reading. The replay saves and restores the strategy array, so the run itself is unchanged
(checked: the FULL replay equals the actual round). Usage: redundancy.py GAME.pg ... | --random N NMAX SEED"""
import sys, os, importlib.util, random, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("ff", os.path.join(HERE, "..", "dtl", "dtl_flipflop.py"))
ff = importlib.util.module_from_spec(spec); spec.loader.exec_module(ff)
dtl_py = ff.dtl_py


class RD(ff.TraceDTL):
    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self.ttop = []; self.stat = {"rounds": 0, "diff": 0, "LIFT": 0, "OTHER": 0, "mismatch": 0}; self.other = []
        self._reg = None; self._fired_in = None

    def extractTangles(self, top, R):
        before = len(self.tv)
        r = super().extractTangles(top, R)
        self.ttop += [top] * (len(self.tv) - before)
        return r

    def attractTangle(self, t, p, R, Z, Gx, maxpr):
        ok = super().attractTangle(t, p, R, Z, Gx, maxpr)
        if ok and self._fired_in is not None: self._fired_in.append((t, self._reg))
        return ok

    def one_round(self, V, R, p, disabled):
        saved = list(self.str) if isinstance(self.str, list) else dict(self.str)
        savedpr = {t: self.tpr[t] for t in disabled}
        for t in disabled: self.tpr[t] = -1
        fired = []; self._fired_in = fired
        Z = set(); CurR = set(R)
        for top in range(self.n - 1, -1, -1):
            if top not in V or top in Z: continue
            self._reg = top
            CurZ = {top}; self.Q = [top]
            dtl_py.DTL.tattr(self, p, CurZ, CurR, CurR, self.pr[top], CurR)
            Z |= CurZ
        cand = [v for v in sorted(V, reverse=True) if not self.attracts(p, v, Z, R)]
        self._reg = "thr"
        for t in [0] + [q for q in self.prios if q > 0 and q <= self.maxpr]:
            if not cand: break
            self.Q = sorted(Z)
            dtl_py.DTL.tattr(self, p, Z, R, R, t, None)
            keep = []
            for i, u in enumerate(cand):
                if self.pr[u] <= t: keep += cand[i:]; break
                if not self.attracts(p, u, Z, R): keep.append(u)
            cand = keep
        self._fired_in = None
        for t, v in savedpr.items(): self.tpr[t] = v
        if isinstance(self.str, list): self.str[:] = saved
        else: self.str.clear(); self.str.update(saved)
        return set(V) - set(cand), fired

    def best_vertices(self, V, R, p):
        cur = {v for v in R if self.pr[v] % 2 == p}
        while cur:
            alive = [t for t in range(len(self.tv)) if self.tpr[t] != -1 and self.tpr[t] % 2 == p]
            dis = {t for t in alive if t < len(self.ttop) and self.ttop[t] in cur}
            full, fired = self.one_round(cur, R, p, set())
            red, _ = self.one_round(cur, R, p, dis)
            self.stat["rounds"] += 1
            if full != red:
                self.stat["diff"] += 1
                lift = any(t in dis and reg != self.ttop[t] for t, reg in fired)
                self.stat["LIFT" if lift else "OTHER"] += 1
                if not lift and len(self.other) < 5: self.other.append((len(self.searches), sorted(full ^ red)))
            if full == cur or not full: break
            cur = full
        last = cur
        res = super().best_vertices(V, R, p)
        # sanity: the FULL replay must reproduce the actual call (stable: V* = last; -1: V = the last nonempty round set)
        if res in (1, -1) and set(V) != set(last): self.stat["mismatch"] += 1
        return res


def write_random(path, n, rng):
    with open(path, "w") as f:
        f.write(f"parity {n-1};\n")
        for v in range(n):
            succ = sorted({rng.randrange(n)} | {rng.randrange(n) for _ in range(rng.randrange(3))})
            f.write(f"{v} {rng.randrange(n+1)} {rng.randrange(2)} {','.join(map(str, succ))};\n")


def run(path):
    g = ff.pg.read(path)
    from stdsort import oink_order
    idx = oink_order(g.prio); new = {v: i for i, v in enumerate(idx)}
    d = RD([g.prio[v] for v in idx], [g.owner[v] for v in idx], [[new[w] for w in g.succ[v]] for v in idx], False, ins_desc=True)
    dtl_py.TV_SORTED = True; dtl_py.PEARCE = True
    sys.setrecursionlimit(100000); d.run(); d.idx = idx
    return d


if __name__ == "__main__":
    if sys.argv[1] == "--random":
        N, nmax, seed = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]); rng = random.Random(seed); files = []
        for i in range(N):
            p = tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False).name; write_random(p, rng.randint(4, nmax), rng); files.append(p)
    else:
        files = sys.argv[1:]
    tot = {}
    for f in files:
        d = run(f)
        for k, v in d.stat.items(): tot[k] = tot.get(k, 0) + v
        for s, diff in d.other: print(f"OTHER {os.path.basename(f)} search {s}: survivors differ on {[d.idx[v] for v in diff]}")
        if sys.argv[1] == "--random": os.unlink(f)
    print(f"games {len(files)}; {tot}")
