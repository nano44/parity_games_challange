#!/usr/bin/env python3
"""L-ALG (produced on Opus 5.5, 2026-10-16): actual vs IDEAL pruning in DTL's best_vertices (GAP-A, Lemma (M)).

For every best_vertices call of a DTL run (library: dtl_pyref.py, L-COMP's independent implementation of C5-DTL.md) and
every pruning round with input V, this recomputes at SET level (order-free least fixed points):
  U      = union of the top-down consumed regions (what the code calls Z after the region loop),
  U_hat  = the IDEAL layered union: for q descending over the priorities of V, U_hat := Attr_{<=q}(U_hat u V_q) in R
           (plain tangle attractor in R, nothing consumed, threshold q),
  surv   = {v in V : attracts(v, U) or exists t < pr(v): attracts(v, Attr_{<=t}(U))}      (the code's survivors),
  surv^  = the same with U_hat.
Checks: (I1) U == the code's region union; (I2) U subset of U_hat; (I3) surv subset of surv^; and reports every round
where surv != surv^ (a straddle that changes the pruning) and where U != U_hat.
Usage: dtl_ideal.py N_GAMES SEED [--nmin A --nmax B] [--order stable|reverse] [--file G.pg ...]
"""
import sys, os, argparse
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, gen
import dtl_pyref as D


def alive(d, t, p):
    return d.tpr[t] != -1 and d.tpr[t] % 2 == p and all(w in d.G for w, _ in d.tv[t])


def lfp(d, p, base, Rs, h, tl):
    """Tangle attractor LFP: start base (subset of Rs), add u in Rs with pr <= h by the vertex rules (escapes = edges into
    Rs minus Z) and tangles t in tl (vertices in Z or Rs, new ones pr <= h, >= 1 new, escapes in Z or outside Rs, >= 1 in Z)."""
    Z = set(base)
    pr, ow, outs = d.pr, d.ow, d.outs
    changed = True
    while changed:
        changed = False
        for u in list(Rs - Z):
            if pr[u] > h:
                continue
            if ow[u] == p:
                ok = any(w in Z for w in outs[u])
            else:
                ok = any(w in Z for w in outs[u]) and not any(w in Rs and w not in Z for w in outs[u])
            if ok:
                Z.add(u); changed = True
        for t in tl:
            vs = [w for w, _ in d.tv[t]]
            new = [w for w in vs if w not in Z]
            if not new or any(w not in Rs for w in new) or any(pr[w] > h for w in new):
                continue
            esc = d.tout[t]
            if any(e not in Z and e in Rs for e in esc) or not any(e in Z for e in esc):
                continue
            Z.update(new); changed = True
    return Z


def attracts(d, p, v, Z, R):
    return d.attracts(p, v, Z, R)


def actual_union(d, p, V, R, tl):
    Z, CurR, regs = set(), set(R), []
    for top in range(d.n - 1, -1, -1):
        if top not in V or top in Z:
            continue
        Zt = lfp(d, p, {top}, CurR, d.pr[top], tl)
        regs.append((top, Zt)); Z |= Zt; CurR -= Zt
    return Z, regs


def ideal_union(d, p, V, R, tl):
    U = set()
    for q in sorted({d.pr[v] for v in V}, reverse=True):
        U = lfp(d, p, U | {v for v in V if d.pr[v] == q}, R, q, tl)
    return U


def survivors(d, p, V, R, U, tl):
    prios = sorted({d.pr[v] for v in R})
    W, out = {}, set()
    for v in V:
        if attracts(d, p, v, U, R):
            out.add(v); continue
        for t in prios:
            if t >= d.pr[v]:
                break
            if t not in W:
                W[t] = lfp(d, p, U, R, t, tl)
            if attracts(d, p, v, W[t], R):
                out.add(v); break
    return out


class Inst(D.DTL):
    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self.log = {"rounds": 0, "I1": 0, "I2": 0, "I3": 0, "surv_diff": 0, "U_diff": 0, "examples": []}

    def best_vertices(self, V, R, p):
        V.clear(); V.update(v for v in R if self.pr[v] % 2 == p)
        if not V:
            return 0
        while True:
            prevV = set(V)
            tl = [t for t in range(len(self.tv)) if alive(self, t, p)]
            Ua, regs = actual_union(self, p, V, R, tl)
            Uh = ideal_union(self, p, V, R, tl)
            sa = survivors(self, p, V, R, Ua, tl)
            sh = survivors(self, p, V, R, Uh, tl)
            # --- the code's own round (copied from dtl_pyref.best_vertices)
            Z = set(); CurR = set(R)
            for top in range(self.n - 1, -1, -1):
                if top not in V or top in Z:
                    continue
                CurZ = {top}; self.Q = [top]
                self.tattr(p, CurZ, CurR, CurR, self.pr[top], CurR)
                Z |= CurZ
            L = self.log; L["rounds"] += 1
            if Z != Ua: L["I1"] += 1
            if not Ua <= Uh: L["I2"] += 1
            if Ua != Uh: L["U_diff"] += 1
            if not sa <= sh: L["I3"] += 1
            if sa != sh:
                L["surv_diff"] += 1
                if len(L["examples"]) < 5:
                    L["examples"].append((p, sorted(R), sorted(V), sorted(sa), sorted(sh), sorted(Uh - Ua)))
            cand = [v for v in sorted(V, reverse=True) if not self.attracts(p, v, Z, R)]
            if not cand:
                assert sa == V, "survivor formula mismatch (stable)"
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
            assert V == sa, ("survivor formula mismatch", sorted(V), sorted(sa))
            if not cand:
                return 1
            if not V:
                V.clear(); V.update(prevV)
                return -1


def run_game(g, order):
    idx = sorted(range(g.n), key=lambda v: (g.prio[v], v if order == "stable" else -v))
    new = {v: i for i, v in enumerate(idx)}
    d = Inst([g.prio[v] for v in idx], [g.owner[v] for v in idx], [[new[w] for w in g.succ[v]] for v in idx])
    d.run()
    return d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("count", type=int); ap.add_argument("seed", type=int)
    ap.add_argument("--nmin", type=int, default=4); ap.add_argument("--nmax", type=int, default=16)
    ap.add_argument("--order", default="stable"); ap.add_argument("--file", nargs="*", default=[])
    a = ap.parse_args()
    sys.setrecursionlimit(100000)
    tot = {"rounds": 0, "I1": 0, "I2": 0, "I3": 0, "surv_diff": 0, "U_diff": 0}
    ex = []
    games = [(f, pg.read(f)) for f in a.file]
    rnd = gen.Rng(f"dtl_ideal|{a.seed}")
    for i in range(a.count):
        n = rnd.randint(a.nmin, a.nmax)
        games.append((f"rand{i}", gen.random_game(n, rnd.randint(2, n + 1), 1, rnd.randint(1, 3), rnd.next64())))
    for name, g in games:
        d = run_game(g, a.order)
        for k in tot:
            tot[k] += d.log[k]
        for e in d.log["examples"]:
            if len(ex) < 8:
                ex.append((name, e))
    print("totals", tot)
    for name, e in ex:
        print("SURV-DIFF", name, "p", e[0], "R", e[1], "V", e[2], "actual", e[3], "ideal", e[4], "Uh-U", e[5])


if __name__ == "__main__":
    main()


# ---------------------------------------------------------------------------------------------------------------------
# Context monotonicity (Claims P/Q = (M)) on a full run, plus the U != U_hat precursor, for climbs (dtl_mclimb.py).
class Ctx(Inst):
    """Records, for every best_vertices call, (player, R) -> [(search#, ntangles, rounds V_0..V_end, result)]."""
    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self.calls, self.nsearch = {}, 0

    def search(self, p):
        self.nsearch += 1
        return super().search(p)

    def best_vertices(self, V, R, p):
        rounds = []
        orig = self.log["rounds"]
        res = None
        V.clear(); V.update(v for v in R if self.pr[v] % 2 == p)
        if not V:
            return 0
        Vin = set(V)
        res = Inst.best_vertices(self, V, R, p)
        # replay the rounds at set level to record them (cheap, same functions as the checks)
        tl = [t for t in range(len(self.tv)) if alive(self, t, p)]
        cur = set(Vin)
        while True:
            rounds.append(frozenset(cur))
            Ua, _ = actual_union(self, p, cur, R, tl)
            nxt = survivors(self, p, cur, R, Ua, tl)
            if nxt == cur or not nxt:
                break
            cur = nxt
        key = (p, frozenset(R))
        self.calls.setdefault(key, []).append((self.nsearch, len(self.tv), rounds, res))
        return res


def pq_violations(d):
    """For recurring (p, R): consecutive occurrences o1 (earlier) and o2; a vertex pruned at a round index < its round
    index in o1 (or pruned in o2 but surviving to the end in o1) is a Claim-P violation."""
    viol = []
    for key, occ in d.calls.items():
        for (s1, n1, r1, res1), (s2, n2, r2, res2) in zip(occ, occ[1:]):
            if s1 == s2:
                continue
            def death(rounds, res, v):
                for i in range(1, len(rounds)):
                    if v in rounds[i - 1] and v not in rounds[i]:
                        return i
                # a -1 result prunes the whole last set in one more round
                return len(rounds) if res == -1 else float("inf")
            for v in r1[0]:
                a, b = death(r1, res1, v), death(r2, res2, v)
                if b < a:
                    viol.append((key[0], s1, s2, v, a, b))
    return viol
