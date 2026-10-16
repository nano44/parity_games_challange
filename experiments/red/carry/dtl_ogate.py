#!/usr/bin/env python3
"""L-RED CARRY box (produced on Opus 5.5): census of ORDER-GATE events in actual A_DTL runs (R10 (O1)-(O3)).
An event is an sptl region computed twice with the SAME (player, top, region vertex set), where the SCC of the top under
the stored strategies differs between the two computations (that is an attraction-order or strategy switch). For each
event it reports the tangles that fired in the later computation and not in the earlier one (the "new firings") and
classifies the new SCC:
  O2 = it contains every vertex of some newly fired tangle;
  O3 = it has an escape (opponent edge leaving it) into a newly fired tangle;
  OTHER = neither. An OTHER would contradict reading (O1).
Run on L-COMP's dtl_py with Oink's order data (as dtl_flipflop.py --order oink), so it is exact against the pinned binary.
Usage: dtl_ogate.py GAME.pg ... | --random N NMAX SEED"""
import sys, os, importlib.util, random, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("ff", os.path.join(HERE, "..", "dtl", "dtl_flipflop.py"))
ff = importlib.util.module_from_spec(spec); spec.loader.exec_module(ff)
dtl_py = ff.dtl_py


class OG(ff.TraceDTL):
    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self.regs = {}; self.events = []; self._fired = None; self.nsr = 0

    def search(self, p):
        self.nsr += 1
        return super().search(p)

    def attractTangle(self, t, p, R, Z, Gx, maxpr):
        ok = dtl_py.DTL.attractTangle(self, t, p, R, Z, Gx, maxpr)
        if ok and self._fired is not None: self._fired.add(t)
        return ok

    def sptl(self, V, R, p):
        changes = False
        for top in range(self.n - 1, -1, -1):
            if top not in V or top not in R: continue
            Z = {top}; self.str[top] = -1; self.Q = [top]; self._fired = set()
            self.tattr(p, Z, R, R, self.pr[top], R)
            fired = self._fired; self._fired = None
            closed = (self.str[top] != -1) if self.ow[top] == p else not any(w in R for w in self.outs[top])
            if closed:
                st, ow = self.str, self.ow
                def succ(v):
                    if ow[v] == p:
                        s = st[v]; return [s] if s != -1 and s in Z else []
                    return [w for w in self.outs[v] if w in Z]
                scc = next(frozenset(C) for C in dtl_py.DTL.pearce(top, succ) if top in C)
                key = (p, top, frozenset(Z))
                if key in self.regs:
                    s0, f0, n0 = self.regs[key]
                    if scc != s0:
                        newf = fired - f0
                        tv = {t: {w for w, _ in self.tv[t]} for t in newf}
                        esc = {w for v in scc if ow[v] != p for w in self.outs[v] if w not in scc}
                        o2 = any(tv[t] <= scc for t in newf); o3 = any(esc & tv[t] for t in newf)
                        self.events.append(dict(key=key, s0=s0, s1=scc, newf=sorted(newf), cls="O2" if o2 else "O3" if o3 else "OTHER",
                                                searches=(n0, self.nsr)))
                self.regs[key] = (scc, fired, self.nsr)
            if closed and top not in self.W:
                self.W.add(top)
                if self.extractTangles(top, Z): changes = True
        return changes


def run(path):
    g = ff.pg.read(path)
    from stdsort import oink_order
    idx = oink_order(g.prio); new = {v: i for i, v in enumerate(idx)}
    d = OG([g.prio[v] for v in idx], [g.owner[v] for v in idx], [[new[w] for w in g.succ[v]] for v in idx], False, ins_desc=True)
    dtl_py.TV_SORTED = True; dtl_py.PEARCE = True
    sys.setrecursionlimit(100000); d.run(); d.idx = idx
    return d


def write_random(path, n, rng):
    with open(path, "w") as f:
        f.write(f"parity {n-1};\n")
        for v in range(n):
            succ = sorted({rng.randrange(n)} | {rng.randrange(n) for _ in range(rng.randrange(3))})
            f.write(f"{v} {rng.randrange(n+1)} {rng.randrange(2)} {','.join(map(str, succ))};\n")


if __name__ == "__main__":
    files = []
    if sys.argv[1] == "--random":
        N, nmax, seed = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]); rng = random.Random(seed)
        for i in range(N):
            p = tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False).name; write_random(p, rng.randint(4, nmax), rng); files.append(p)
    else:
        files = sys.argv[1:]
    tot = {"O2": 0, "O3": 0, "OTHER": 0}; recur = 0; shown = 0
    for f in files:
        d = run(f)
        recur += sum(1 for _ in d.regs)
        for e in d.events:
            tot[e["cls"]] += 1
            if (e["cls"] == "OTHER" or sys.argv[1] != "--random") and shown < 12:
                shown += 1
                L = lambda s: sorted(d.idx[v] for v in s)
                print(f"{os.path.basename(f)}: top {d.idx[e['key'][1]]} p {e['key'][0]} |region| {len(e['key'][2])} searches {e['searches']} "
                      f"SCC {L(e['s0'])} -> {L(e['s1'])} new firings {e['newf']} class {e['cls']}")
        if sys.argv[1] == "--random": os.unlink(f)
    print(f"games {len(files)}; distinct (player, top, region) keys {recur}; order-gate events {sum(tot.values())}: {tot}")
