#!/usr/bin/env python3
"""L-RED (Opus 5.5): Phi_idx test restricted to its claim. For every depth-0 piece index j and consecutive same-player
searches (no dominion) where piece j has the SAME context, returned -1 in the earlier search, and its pruning rounds differ:
drivers = tangles born in the earlier search whose disabling undoes the first differing round r0, or which ALONE (every
other new tangle disabled) reproduce it (sufficient singletons, L-ALG 38f10e4) (as phi_drivers.py);
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
        self.alive = []; self.recx = {}           # recx[j][context R] = per-context record at index j (cross-context split)
        self.lastp = None

    def search(self, p):
        if self.searches and (self.searches[-1]["player"] != p or self.searches[-1]["dominions"]): self.rec = {}; self.recx = {}
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
            drivers = []; rescu = set()
            newT = {C for C in range(len(self.tv)) if self.born[C] == si - 1 and self.tpr[C] != -1 and self.tpr[C] % 2 == p}
            none, _ = self.one_round(set(prev), R, p, set(newT))
            self.nsuf = getattr(self, "nsuf", 0)
            for C in sorted(newT):
                without, _ = self.one_round(set(prev), R, p, {C})
                alone, _ = self.one_round(set(prev), R, p, newT - {C})
                nec, suf = without != target, alone == target and none != target
                if not (nec or suf): continue
                if not nec: without = none; self.nsuf += 1    # sufficient singleton only (L-ALG 38f10e4)
                vs = [w for w, _ in self.tv[C]]; h = max(vs, key=lambda v: (self.pr[v], v))
                death = next((r for r in range(1, len(ra)) if h not in ra[r]), None)
                resc = set(target) - set(without); rescu |= resc
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
            cross = {}
            for c, rc in self.recx.get(j, {}).items():
                if c == frozenset(R): continue
                for u, x in rc.items(): cross[u] = max(cross.get(u, 0), x)
            same = self.recx.get(j, {}).get(frozenset(R), {})
            raised_same = any(x > same.get(u, 0) for u, x in dn.items())
            raised_cross = any(x > cross.get(u, 0) for u, x in dn.items())
            rc_resc = any(dn.get(u, 0) > cross.get(u, 0) for u in rescu)      # Phi_idx proper: a RESCUED vertex beats the cross record
            rs_resc = any(dn.get(u, 0) > rec.get(u, 0) for u in rescu)
            d0p = [pc for pc in self.searches[si - 1]["pieces"] if pc["depth"] == 0]
            self.events.append(dict(s=si, j=j, cap_only=capo, raised=raised, nd=len(drivers), has_cross=bool(cross),
                                    raised_same=raised_same, raised_cross=raised_cross, rc_resc=rc_resc, rs_resc=rs_resc,
                                    kind=d0p[j]["kind"] if j < len(d0p) else "?", file=None))
        self.calls[(si, j)] = (frozenset(R), None, rb, res)
        if res == -1 and self._depth == 0:
            rx = self.recx.setdefault(j, {}).setdefault(frozenset(R), {})
            for k in range(1, len(rb)):
                for v in rb[k - 1] - rb[k]: rx[v] = max(rx.get(v, 0), k)
            for v in (rb[-1] if rb and rb[-1] else []): rx[v] = max(rx.get(v, 0), len(rb))
        if res == -1:
            r = self.rec.setdefault(j, {})
            for k in range(1, len(rb)):
                for v in rb[k - 1] - rb[k]: r[v] = max(r.get(v, 0), k)
            for v in (rb[-1] if rb and rb[-1] else []): r[v] = max(r.get(v, 0), len(rb))
        return res


def ctx_counts(d):
    """L-ALG GAP-A-M 11e reduction: per phase (consecutive same-player searches, no dominion in between) and depth-0 index
    i, c_i = number of DISTINCT contexts R of Dom(prevV) (domfirst) pieces at index i that returned -1. Returns a list of
    (first search of phase, i, c_i)."""
    out = []; phase = None; C = {}
    for si, sr in enumerate(d.searches):
        if phase is None or d.searches[si - 1]["player"] != sr["player"] or d.searches[si - 1]["dominions"]:
            out += [(phase, i, len(cs)) for i, cs in C.items()]; phase = si; C = {}
        d0 = [pc for pc in sr["pieces"] if pc["depth"] == 0]
        for j, pc in enumerate(d0):
            c = d.calls.get((si, j))
            if c and pc["kind"] == "domfirst" and c[3] == -1: C.setdefault(j, set()).add(c[0])
    out += [(phase, i, len(cs)) for i, cs in C.items()]
    return out


def replay_blocks(d):
    """Lead 12:04Z / L-ALG GAP-A-M 14-15 target: chained resets. Per phase, F = first-difference depth-0 index of each
    consecutive search pair (pieces compared by (context, kind, V); context = the call's R). A BLOCK at level i = a
    transition with first difference i followed by the transitions with first difference > i, up to the next one <= i.
    Returns (score, longest phase, detail): score = max over (phase, i) with >= 2 blocks at i of sum over blocks of
    (deeper changes in the block - 1)^+. A K x K two-level counter scores about K(K - 1)."""
    best, longest, det = 0, 0, None
    phases = []; cur = []
    for si, sr in enumerate(d.searches):
        if cur and (d.searches[si - 1]["player"] != sr["player"] or d.searches[si - 1]["dominions"]):
            phases.append(cur); cur = []
        cur.append(si)
    if cur: phases.append(cur)
    def sig(si):
        d0 = [pc for pc in d.searches[si]["pieces"] if pc["depth"] == 0]
        return [(d.calls.get((si, j), (None,))[0], pc["kind"], frozenset(pc.get("V") or ())) for j, pc in enumerate(d0)]
    for ph in phases:
        longest = max(longest, len(ph))
        F = []
        for a, b in zip(ph, ph[1:]):
            A, B = sig(a), sig(b); j = 0
            while j < min(len(A), len(B)) and A[j] == B[j]: j += 1
            F.append(j)
        for i in set(F):
            blocks = []; k = 0
            while k < len(F):
                if F[k] == i:
                    c = 0; k += 1
                    while k < len(F) and F[k] > i: c += 1; k += 1
                    blocks.append(c)
                else: k += 1
            if len(blocks) >= 2:
                sc = sum(max(0, c - 1) for c in blocks)
                if sc > best: best, det = sc, (ph[0], i, blocks, F)
    return best, longest, det


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
                if e["has_cross"]:
                    for k in ("rc_resc",): tot.setdefault("cap_only_has_cross_" + k, 0); tot["cap_only_has_cross_" + k] += e[k]
                for k in ("has_cross", "raised_same", "raised_cross", "rs_resc"):
                    tot.setdefault("cap_only_" + k, 0); tot["cap_only_" + k] += e[k]
                if e["has_cross"] and not e["raised_cross"]:
                    tot.setdefault("cap_only_cross_flat", 0); tot["cap_only_cross_flat"] += 1
                    print(f"CROSS-FLAT (raises only its same-context record) {os.path.basename(f)}: search {e['s']-1}->{e['s']} index {e['j']}")
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
        tot["sufficient_only_drivers"] = tot.get("sufficient_only_drivers", 0) + getattr(d, "nsuf", 0)
        if sys.argv[1] == "--random": os.unlink(f)
    print(f"games {len(files)}; {tot}")
