#!/usr/bin/env python3
"""L-RED (Opus 5.5): Phi_idx test restricted to its claim. For every depth-0 piece index j and consecutive same-player
searches (no dominion) where piece j has the SAME context, returned -1 in the earlier search, and its pruning rounds differ:
drivers = tangles born in the earlier search whose disabling undoes the first differing round r0 (as phi_drivers.py);
the change is CAP-ONLY if it has >= 1 driver and every driver is dead before r0 (in the earlier search) and rescues only
vertices of priority above its top. A CAP-ONLY change that raises no death-round record at index j (records from -1
results of that phase; a new stable result counts as infinity) is a Phi_idx COUNTEREXAMPLE.
Usage: phi_full.py GAME.pg ... | --random N NMAX SEED"""
import sys, os, importlib.util, random, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("rd", os.path.join(HERE, "redundancy.py"))
rd = importlib.util.module_from_spec(spec); spec.loader.exec_module(rd)
INF = 10 ** 9


class P(rd.RD):
    def __init__(self, *a, **k):
        super().__init__(*a, **k); self.calls = {}; self.d0 = 0; self.born = []; self.events = []; self.rec = {}; self._depth = 0
        self.alive = []
        self.lastp = None

    def search(self, p):
        if self.searches and (self.searches[-1]["player"] != p or self.searches[-1]["dominions"]): self.rec = {}
        self.d0 = 0
        return super().search(p)

    def search_rec(self, R, p, depth):
        od = self._depth; self._depth = depth
        r = super().search_rec(R, p, depth); self._depth = od; return r

    def extractTangles(self, top, R):
        b = len(self.tv); r = super().extractTangles(top, R)
        self.born += [len(self.searches) - 1] * (len(self.tv) - b)
        return r

    def rounds(self, R, p, disabled):
        cur = {v for v in R if self.pr[v] % 2 == p}; out = [frozenset(cur)]
        while cur:
            nx, _ = self.one_round(cur, R, p, disabled)
            if nx == cur: break
            cur = nx; out.append(frozenset(cur))
        return out

    def best_vertices(self, V, R, p):
        if self._depth != 0:
            return super().best_vertices(V, R, p)
        si = len(self.searches) - 1; j = self.d0; self.d0 += 1
        rb = self.rounds(R, p, set())
        res = super().best_vertices(V, R, p)
        prevc = self.calls.get((si - 1, j))
        if prevc and prevc[0] == frozenset(R) and prevc[3] == -1 and self.searches[si - 1]["player"] == p and not self.searches[si - 1]["dominions"] and prevc[2] != rb:
            ra = prevc[2]
            pick = lambda L, r: L[r] if r < len(L) else frozenset()
            r0 = next(r for r in range(1, max(len(ra), len(rb)) + 1) if pick(ra, r) != pick(rb, r))
            prev = rb[r0 - 1]; target = pick(rb, r0)
            drivers = []
            for C in range(len(self.tv)):
                if self.born[C] != si - 1 or self.tpr[C] == -1 or self.tpr[C] % 2 != p: continue
                without, _ = self.one_round(set(prev), R, p, {C})
                if without == target: continue
                vs = [w for w, _ in self.tv[C]]; h = max(vs, key=lambda v: (self.pr[v], v))
                death = next((r for r in range(1, len(ra)) if h not in ra[r]), None)
                resc = set(target) - set(without)
                drivers.append((death is not None and death < r0) and bool(resc) and all(self.pr[u] > self.pr[h] for u in resc))
                if not (death is not None and death < r0):
                    # alive-top driver: record where its top ends up in the EARLIER search (MIRROR (M1): in the return set?)
                    M = ra[-2] if len(ra) > 1 and not ra[-1] else ra[-1]          # the -1 return set of the earlier call
                    d0p = [pc for pc in self.searches[si - 1]["pieces"] if pc["depth"] == 0]
                    kind = d0p[j]["kind"] if j < len(d0p) else "?"
                    self.alive.append(dict(s=si, j=j, C=C, h=self.idx[h], kind=kind, h_in_prev_return=(h in M),
                                           h_death_prev=death, rounds_prev=len(ra) - 1, resc=sorted(self.idx[u] for u in resc)))
            capo = bool(drivers) and all(drivers)
            dn = {}
            for r in range(1, len(rb)):
                for v in rb[r - 1] - rb[r]: dn[v] = r
            if res == 1:
                for v in rb[-1]: dn[v] = INF
            elif rb and rb[-1]:
                for v in rb[-1]: dn[v] = len(rb)
            rec = self.rec.get(j, {})
            raised = any(x > rec.get(u, 0) for u, x in dn.items())
            d0p = [pc for pc in self.searches[si - 1]["pieces"] if pc["depth"] == 0]
            self.events.append(dict(s=si, j=j, cap_only=capo, raised=raised, nd=len(drivers),
                                    kind=d0p[j]["kind"] if j < len(d0p) else "?", file=None))
        self.calls[(si, j)] = (frozenset(R), None, rb, res)
        if res == -1:
            r = self.rec.setdefault(j, {})
            for k in range(1, len(rb)):
                for v in rb[k - 1] - rb[k]: r[v] = max(r.get(v, 0), k)
            for v in (rb[-1] if rb and rb[-1] else []): r[v] = max(r.get(v, 0), len(rb))
        return res


def run(path):
    g = rd.ff.pg.read(path)
    from stdsort import oink_order
    idx = oink_order(g.prio); newi = {v: i for i, v in enumerate(idx)}
    d = P([g.prio[v] for v in idx], [g.owner[v] for v in idx], [[newi[w] for w in g.succ[v]] for v in idx], False, ins_desc=True)
    rd.dtl_py.TV_SORTED = True; rd.dtl_py.PEARCE = True
    sys.setrecursionlimit(100000); d.idx = idx; d.run()
    return d


if __name__ == "__main__":
    if sys.argv[1] == "--random":
        N, nmax, seed = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]); rng = random.Random(seed); files = []
        for i in range(N):
            p = tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False).name; rd.write_random(p, rng.randint(4, nmax), rng); files.append(p)
    else:
        files = sys.argv[1:]
    tot = {"changes": 0, "cap_only": 0, "cap_only_raised": 0, "COUNTEREXAMPLE": 0, "other_flat": 0}
    for f in files:
        d = run(f)
        for e in d.events:
            tot["changes"] += 1
            if e["cap_only"]:
                tot["cap_only"] += 1
                if e["raised"]: tot["cap_only_raised"] += 1
                else:
                    tot["COUNTEREXAMPLE"] += 1; print(f"COUNTEREXAMPLE {os.path.basename(f)}: search {e['s']-1}->{e['s']} piece index {e['j']}")
            elif not e["raised"]:
                tot["other_flat"] += 1; k = "other_flat_" + e["kind"]; tot[k] = tot.get(k, 0) + 1
                if e["kind"] == "domfirst": print(f"FLAT DOMFIRST (not cap-only) {os.path.basename(f)}: search {e['s']-1}->{e['s']} index {e['j']} drivers {e['nd']}")
        for a in d.alive:
            tot.setdefault("alive_" + a["kind"], 0); tot["alive_" + a["kind"]] += 1
            if a["kind"] == "domfirst":
                tot.setdefault("alive_domfirst_top_in_prev_return", 0); tot["alive_domfirst_top_in_prev_return"] += a["h_in_prev_return"]
                print(f"ALIVE-TOP at DOMFIRST {os.path.basename(f)}: search {a['s']-1}->{a['s']} index {a['j']} driver t{a['C']} top {a['h']} "
                      f"(death in earlier search {a['h_death_prev']} of {a['rounds_prev']} rounds; in its return set: {a['h_in_prev_return']}) rescues {a['resc']}")
        if sys.argv[1] == "--random": os.unlink(f)
    print(f"games {len(files)}; {tot}")
