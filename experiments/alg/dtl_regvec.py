"""L-ALG (produced on Opus 5.5, 2026-10-16), GAP-A-M §13e. For consecutive depth-0 calls at one (player, context) on A_DTL:
first round r0 where the ACTUAL round sets differ (equal V_{r0-1}); compare the actual region vectors computed on
V_{r0-1}: first differing top k (Lemma R check: Z_k grew), and whether t_k is (i) a vertex whose round-r0 survival
changed, (ii) a leader (return set) of the earlier or later call. Usage: DTL_ORDER=oink dtl_regvec.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_deficit as X, dtl_ideal as I, pg

class Rv(X.T):
    def __init__(s, *a, **k):
        super().__init__(*a, **k); s.ns = 0; s.calls = {}
    def search(s, p):
        s.ns += 1; return super().search(p)
    def best_vertices(s, V, R, p):
        if s.depth == 0:
            tl = [t for t in range(len(s.tv)) if I.alive(s, t, p)]
            cur = {v for v in R if s.pr[v] % 2 == p}; rounds, regv = [frozenset(cur)], []
            while cur:
                Ua, regs = I.actual_union(s, p, cur, R, tl); regv.append([(t, frozenset(z)) for t, z in regs])
                nx = I.survivors(s, p, cur, R, Ua, tl)
                if nx == cur: break
                cur = nx; rounds.append(frozenset(cur))
            Vh = set(); rh = X.C6.best_vertices(s, Vh, set(R), p)
            s.calls.setdefault((p, frozenset(R)), []).append((s.ns, rounds, regv, (rh, frozenset(Vh)), list(tl)))
        return super().best_vertices(V, R, p)

def build(g):
    d0 = X.build(g); idx = d0.idx; new = {v: i for i, v in enumerate(idx)}
    kw = {"ins_desc": True} if os.environ.get("DTL_ORDER") == "oink" else {}
    d = Rv([g.prio[v] for v in idx], [g.owner[v] for v in idx], [[new[w] for w in g.succ[v]] for v in idx], **kw); d.idx = idx
    return d

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    tot = {}
    for f in sys.argv[1:]:
        g = pg.read(f); d = build(g); d.run(); o = lambda S: sorted(d.idx[v] for v in S)
        print("==", f.split("/")[-1])
        for key, occ in d.calls.items():
            for (s1, r1, v1, h1, *_), (s2, r2, v2, h2, *_) in zip(occ, occ[1:]):
                if h1 != h2 or r1 == r2: continue                     # DEF pairs only: ideal unchanged, actual changed
                L = max(len(r1), len(r2))
                pick = lambda r, i: r[min(i, len(r) - 1)]   # fixed box 4 (L-RED caveat): a stable run stays at its fixpoint; a -1 run ends with the empty set
                r0 = next((i for i in range(1, L + 1) if pick(r1, i) != pick(r2, i)), None)
                if r0 is None or r0 - 1 >= len(v1) or r0 - 1 >= len(v2): continue
                A, B = v1[r0 - 1], v2[r0 - 1]
                k = next((i for i in range(min(len(A), len(B))) if A[i] != B[i]), None)
                if k is None: tot["no_region_diff"] = tot.get("no_region_diff", 0) + 1; continue
                (ta, za), (tb, zb) = A[k], B[k]
                grew = ta == tb and za < zb
                changed = pick(r1, r0) ^ pick(r2, r0)
                lead1 = r1[-2] if len(r1) > 1 and not r1[-1] else r1[-1]; lead2 = r2[-2] if len(r2) > 1 and not r2[-1] else r2[-1]
                cls = ("lexR_ok" if grew else "lexR_FAIL") + ("_top_changed" if ta in changed else "") + ("_top_leader" if (ta in lead1 or ta in lead2) else "")
                tot[cls] = tot.get(cls, 0) + 1
                print(f"  |R|={len(key[1])} s{s1}->s{s2} r0={r0} first differing region top {d.idx[ta]} (pr {d.pr[ta]}) {'grew' if grew else 'NOT grew'}; survival changed {o(changed)}; leaders {o(lead1)} -> {o(lead2)}")
    print(tot)
