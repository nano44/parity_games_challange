"""L-ALG (produced on Opus 5.5, 2026-10-16), docs/alg/GAP-A-M.md §13, (H4). A_DTL runs; at every depth-0 piece also the
ideal (C6 rule, same tangle set, same context) result. A change between consecutive searches of a phase (no dominion
between) at its first-difference piece j with the SAME context is DEF (deficit-triggered) when the ideal (result, V) at
that context is equal in both searches while the actual one differs, else LRN (the ideal result moved too).
Also checks: actual vs ideal at one call (weaker: actual -1 / V_actual subset of V_ideal), and lag (actual at b == ideal
at a). Usage: dtl_deficit.py [G.pg ...] (plus DEFICIT_RANDOM seeded random games, n <= DEFICIT_NMAX)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_pyref as D, dtl_ideal as I, pg, gen
from dtl_c6proto import C6

class T(D.DTL):
    def __init__(s, *a, **k):
        super().__init__(*a, **k); s.trace = []; s.depth = 0
    def search(s, p):
        s.trace.append({"p": p, "pieces": [], "dom": s.dominions})
        return super().search(p)
    def search_rec(s, R, p, depth):
        s.depth = depth
        return super().search_rec(R, p, depth)
    def best_vertices(s, V, R, p):
        Rin = frozenset(R)
        if s.depth == 0:
            Vh = set(); rh = C6.best_vertices(s, Vh, set(R), p)
        res = super().best_vertices(V, R, p)
        if s.depth == 0:
            s.trace[-1]["pieces"].append((Rin, res, frozenset(V), rh, frozenset(Vh)))
        return res

def build(g):
    """T on game g in the order given by DTL_ORDER: 'stable' (default; order datum omega = (priority, id)) or 'oink'
    (Oink's own order, exact against pinned Oink: stdsort.oink_order, ins_desc, TV_SORTED, PEARCE)."""
    if os.environ.get("DTL_ORDER") == "oink":
        sys.path.insert(0, os.path.join(HERE, "..", "dtl-bench")); from stdsort import oink_order
        idx = oink_order(g.prio); D.TV_SORTED = True; D.PEARCE = True; kw = {"ins_desc": True}
    else:
        idx = sorted(range(g.n), key=lambda v: (g.prio[v], v)); kw = {}
    new = {v: i for i, v in enumerate(idx)}
    d = T([g.prio[v] for v in idx], [g.owner[v] for v in idx], [[new[w] for w in g.succ[v]] for v in idx], **kw)
    d.idx = idx
    return d

def analyse(d, st, name):
    for tr in d.trace:
        for (R, ra, Va, rh, Vh) in tr["pieces"]:
            st["calls"] += 1
            if (ra, Va) != (rh, Vh):
                st["calls_def"] += 1
                weaker = (ra == -1 and rh == 1) or (ra == rh and Va <= Vh)
                st["weaker" if weaker else "NOT_weaker"] += 1
                if not weaker and len(st["ex_nw"]) < 3: st["ex_nw"].append((name, ra, sorted(Va), rh, sorted(Vh)))
    percx, phase_def, phase_all = {}, 0, 0
    def flush():
        nonlocal percx, phase_def, phase_all
        if percx: st["max_def_per_ctx"] = max(st["max_def_per_ctx"], max(percx.values()))
        # compounding check: deeper (index >= 1) contexts with >= 2 DEF changes in this phase
        st["deep_ctx_def2"] = st.get("deep_ctx_def2", 0) + sum(1 for (j, _), c in percx.items() if j >= 1 and c >= 2)
        # nested shape: in a phase with DEF at piece 0, the number of DISTINCT deeper contexts with >= 1 DEF change
        if any(j == 0 for (j, _) in percx):
            st["nested_ctx"] = max(st.get("nested_ctx", 0), sum(1 for (j, _) in percx if j >= 1))
        if phase_def > st["max_def_phase"][0]: st["max_def_phase"] = (phase_def, phase_all, name); st["n_max_def_phase"] = d.n
        percx, phase_def, phase_all = {}, 0, 0
    for a, b in zip(d.trace, d.trace[1:]):
        if a["p"] != b["p"] or b["dom"] != a["dom"]:
            flush(); continue
        pa, pb = a["pieces"], b["pieces"]
        j = 0
        while j < min(len(pa), len(pb)) and pa[j][:3] == pb[j][:3]:
            j += 1
        if j >= min(len(pa), len(pb)): continue
        phase_all += 1
        if pa[j][0] != pb[j][0]: st["ctx_changed"] += 1; continue
        ideal_same = pa[j][3:] == pb[j][3:]
        if ideal_same:
            st["DEF"] += 1; phase_def += 1
            percx[(j, pa[j][0])] = percx.get((j, pa[j][0]), 0) + 1
            if len(st["ex_def"]) < 4: st["ex_def"].append((name, j, pa[j][1], pb[j][1], pa[j][3]))
            (ra, Va), (rb, Vb) = pa[j][1:3], pb[j][1:3]
            if (ra, rb) == (-1, 1) or (ra == rb == 1 and Va < Vb): k = "DEF_up"
            elif (ra, rb) == (1, -1) or (ra == rb == 1 and Vb < Va): k = "DEF_down"
            else: k = "DEF_other"
            st[k] = st.get(k, 0) + 1
            if k != "DEF_up" and len(st["ex_" + k]) < 3: st["ex_" + k].append((name, d.trace.index(b), j, ra, sorted(Va), rb, sorted(Vb)))
            if ra == -1 and rb == -1 and Va != Vb: st["DEF_m1m1"] = st.get("DEF_m1m1", 0) + 1
        else:
            st["LRN"] += 1
            if pb[j][1:3] == pa[j][3:]: st["LRN_lag"] += 1
    flush()

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    games = [(f.split("/")[-1], pg.read(f)) for f in sys.argv[1:]]
    rnd = gen.Rng("deficit"); NMAX = int(os.environ.get("DEFICIT_NMAX", "24"))
    for i in range(int(os.environ.get("DEFICIT_RANDOM", "600"))):
        n = rnd.randint(6, NMAX); games.append((f"r{i}", gen.random_game(n, rnd.randint(2, n + 1), 1, rnd.randint(1, 3), rnd.next64())))
    st = dict(calls=0, calls_def=0, weaker=0, NOT_weaker=0, DEF=0, LRN=0, LRN_lag=0, ctx_changed=0, max_def_per_ctx=0,
              max_def_phase=(0, 0, None), n_max_def_phase=None, ex_def=[], ex_nw=[], ex_DEF_down=[], ex_DEF_other=[])
    for name, g in games:
        d = build(g); d.run()
        analyse(d, st, name)
    print("games", len(games)); print(st)
