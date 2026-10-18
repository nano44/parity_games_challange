"""L-ALG succ. 10 (box 12, produced on Opus 5.5), GAP-A-M §32: candidate potentials for (CTX⁺) on 𝒞^1P (Lead 14:37Z). For every
search s of a phase of q, the depth-0 chain of best_vertices calls (j = 0, 1, ...): context R_j, result res_j (1 stable, −1, 0),
round count e_j (for −1: the emptying round), final V_j (V* or prevV), piece_j = R_j \\ R_{j+1}. rank_j := n + 2 if stable,
e_j if −1, 0 if the call returned 0. A candidate is a predicate on consecutive searches s, s+1 of one phase (a TRANSITION):
  MONO candidates (a poly-range Φ that never drops and rises at every transition):
    SUM-RANK     Φ = Σ_j rank_j
    VERT-RANK    Φ = Σ_v rank of the call whose piece holds v
    VERT-RANK-PW pointwise: every v's piece rank is ≥ before (transitions where some v drops are violations)
    STABLE-CNT   Φ = number of stable depth-0 calls
    LEN          Φ = −(number of depth-0 calls)
  NEW-KEY candidates (pigeonhole: search s+1 holds a key never seen in the phase's earlier searches; searches ≤ #keys):
    K-jr      (j, rank_j)              K-Rr   (|R_j|, rank_j)        K-jRr  (j, |R_j|, rank_j)
    K-jrV     (j, rank_j, |V_j|)       K-RrV  (|R_j|, rank_j, |V_j|) K-jRrV (j, |R_j|, rank_j, |V_j|)
    K-Rset    (R_j as a set, rank_j)   (counts distinct contexts; exponential range, recorded as the reference)
    vertex-indexed (v ranges over the piece of call j): K-v-r (v, rank_j), K-v-rj (v, rank_j, j), K-v-rs (v, rank_j, |R_j|),
    K-v-rV (v, rank_j, |V_j|), K-v-rjV (v, rank_j, j, |V_j|), K-v-all (v, rank_j, j, |R_j|, |V_j|)
A MONO candidate is violated at a transition where Φ(s+1) ≤ Φ(s) (it must rise strictly); a NEW-KEY candidate where search s+1
has no new key, tested only at transitions whose depth-0 chain (R_j, rank_j, V_j) changes (the others are counted separately). Printed: transitions, violations per candidate, first violating instance.
Corpus: b12_topchain.classgames (forced class set) with CLASS=1, else the files as they are.
Usage: DTL_ORDER=stable|oink [CLASS=1 TRIALS=k SEED=s NMAX=n] b12_pot.py G.pg ...
   or: [KEY=K-v-r] DTL_ORDER=... b12_pot.py climb C START.pg STEPS SEED OUTDIR   (class-preserving climb; score (violations of KEY,
       chain-changing transitions, searches); a violation is written to OUTDIR)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, fixd_stealentry as SE, b12_nopre as NPm
from b12_topchain import classgames


class CH(NPm.NP):
    def search(self, p):
        self.phase = (p, self.dominions); self.calls = []
        r = SE.P.DTL.search(self, p)
        if not hasattr(self, "log"): self.log = []
        self.log.append((self.phase, self.calls)); return r

    def search_rec(self, R, p, depth):
        old = getattr(self, "_dep", 0); self._dep = depth
        try:
            return SE.P.DTL.search_rec(self, R, p, depth)
        finally:
            self._dep = old

    def best_vertices(self, V, R, p):
        Rk = frozenset(R); res = NPm.NP.best_vertices(self, V, R, p)
        if getattr(self, "_dep", 0) == 0 and hasattr(self, "calls"):
            self.calls.append((Rk, res, len(self._vr) if res else 0, frozenset(V)))
        return res


def run(g, order):
    saved = SE.SE; SE.SE = CH
    try:
        return SE.run(g, order)
    finally:
        SE.SE = saved


def chain(calls, n):
    out = []
    for j, (R, res, e, V) in enumerate(calls):
        nxt = calls[j + 1][0] if j + 1 < len(calls) else frozenset()
        out.append((j, R, n + 2 if res == 1 else (e if res == -1 else 0), V, R - nxt, res))
    return out


def sig(ch):
    return tuple((R, r, V) for j, R, r, V, _, _ in ch)


def mono(ch, n):
    vr = {}
    for j, R, r, V, piece, res in ch:
        for v in piece: vr[v] = r
    return {"SUM-RANK": sum(c[2] for c in ch), "VERT-RANK": sum(vr.values()), "STABLE-CNT": sum(1 for c in ch if c[5] == 1),
            "LEN": -len(ch)}, vr


def keys(ch):
    return {"K-jr": {(j, r) for j, R, r, V, _, _ in ch}, "K-Rr": {(len(R), r) for j, R, r, V, _, _ in ch},
            "K-jRr": {(j, len(R), r) for j, R, r, V, _, _ in ch}, "K-jrV": {(j, r, len(V)) for j, R, r, V, _, _ in ch},
            "K-RrV": {(len(R), r, len(V)) for j, R, r, V, _, _ in ch}, "K-jRrV": {(j, len(R), r, len(V)) for j, R, r, V, _, _ in ch},
            "K-Rset": {(R, r) for j, R, r, V, _, _ in ch},
            "K-v-r": {(v, r) for j, R, r, V, piece, _ in ch for v in piece},
            "K-v-rj": {(v, r, j) for j, R, r, V, piece, _ in ch for v in piece},
            "K-v-rs": {(v, r, len(R)) for j, R, r, V, piece, _ in ch for v in piece},
            "K-v-rV": {(v, r, len(V)) for j, R, r, V, piece, _ in ch for v in piece},
            "K-v-rjV": {(v, r, j, len(V)) for j, R, r, V, piece, _ in ch for v in piece},
            "K-v-all": {(v, r, j, len(R), len(V)) for j, R, r, V, piece, _ in ch for v in piece}}


if __name__ == "__main__" and sys.argv[1] == "climb":
    sys.setrecursionlimit(100000)
    import importlib; M = importlib.import_module("b12_pot")
    M.vr_climb(int(sys.argv[2]), sys.argv[3], int(sys.argv[4]), int(sys.argv[5]), sys.argv[6], os.environ.get("DTL_ORDER", "stable"),
               os.environ.get("KEY", "K-v-r")); sys.exit(0)

if __name__ == "__main__":
    sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable")
    src = classgames(sys.argv[1:], int(os.environ.get("TRIALS", "2")), int(os.environ.get("SEED", "1")), int(os.environ.get("NMAX", "200"))) \
        if os.environ.get("CLASS") == "1" else ((os.path.basename(f), pg.read(f)) for f in sys.argv[1:])
    trans = same = 0; bad = {}; first = {}
    for name, g in src:
        try:
            d = run(g, order)
        except RecursionError:
            continue
        seen = {}; prev = None
        for ph, calls in getattr(d, "log", []):
            ch = chain(calls, g.n); m, vr = mono(ch, g.n); k = keys(ch)
            if prev is not None and prev[0] == ph:
                trans += 1; pm, pvr = prev[1], prev[2]
                viol = [c for c in m if m[c] <= pm[c]]
                if any(v in pvr and vr[v] < pvr[v] for v in vr): viol.append("VERT-RANK-PW")
                if sig(ch) == prev[3]: same += 1                     # identical depth-0 chain: keys are not tested
                else: viol += [c for c in k if not (k[c] - seen[c])]
                for c in viol:
                    bad[c] = bad.get(c, 0) + 1; first.setdefault(c, (name, g.n))
            if prev is None or prev[0] != ph: seen = {c: set() for c in k}
            for c in k: seen[c] |= k[c]
            prev = (ph, m, vr, sig(ch))
    allc = ["SUM-RANK", "VERT-RANK", "VERT-RANK-PW", "STABLE-CNT", "LEN", "K-jr", "K-Rr", "K-jRr", "K-jrV", "K-RrV", "K-jRrV", "K-Rset",
            "K-v-r", "K-v-rj", "K-v-rs", "K-v-rV", "K-v-rjV", "K-v-all"]
    print("order", order, "transitions", trans, "of which identical depth-0 chain (keys not tested)", same)
    for c in allc: print(f"  {c:13s} violations {bad.get(c, 0):6d}  first {first.get(c)}")


def vr_score(g, order, key="K-v-r"):
    """(transitions violating key, chain-changing transitions, searches) over g's phases; used by the climb. With MARGIN=1:
    (violations, −(fewest vertices supplying a new key at one chain-changing transition), chain-changing, searches)."""
    d = run(g, order); viol = changing = 0; seen = None; prev = None; marg = g.n + 1
    for ph, calls in getattr(d, "log", []):
        ch = chain(calls, g.n); k = keys(ch)[key]
        if prev is not None and prev[0] == ph and sig(ch) != prev[1]:
            changing += 1; marg = min(marg, len({x[0] for x in k - seen}))
            if not (k - seen): viol += 1
        if prev is None or prev[0] != ph: seen = set()
        seen |= k; prev = (ph, sig(ch))
    if os.environ.get("MARGIN") == "1": return (viol, -marg, changing, d.iterations)
    return (viol, changing, d.iterations)


def vr_climb(C, start_file, steps, seed, out, order, key):
    import random
    from fixd_oneplayer import mutate
    from fixd_ctx1p import distinct
    rnd = random.Random(seed); g = distinct(pg.read(start_file)); P = max(g.prio) + 1; sg = vr_score(g, order, key)
    os.makedirs(out, exist_ok=True); print("start", sg, flush=True)
    for it in range(steps):
        h = mutate(g, C, P, rnd)
        if h is None: continue
        h = distinct(h)
        try:
            sh = vr_score(h, order, key)
        except RecursionError:
            continue
        if sh >= sg:
            if sh > sg: print(it, sh, flush=True)
            g, sg = h, sh
            if sg[0] >= 1:
                fn = os.path.join(out, f"{key}_viol_C{C}_n{g.n}_s{seed}.pg"); pg.write(g, fn); print("VIOLATION", sg, fn, flush=True); return
    fn = os.path.join(out, f"{key}_final_C{C}_n{g.n}_s{seed}.pg"); pg.write(g, fn); print("final", sg, fn)
