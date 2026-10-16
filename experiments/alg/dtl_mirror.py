#!/usr/bin/env python3
"""L-ALG (produced on Opus 5.5, 2026-10-16): test of L-RED's MIRROR reading (R10 "Outside 2CE", l-red f954923) and of its
"redundancy" step, on the ideal-pruning variant C6 (no deficits in the pruning, MIRROR's premise). For every change between
consecutive same-player searches s, s+1 (no dominion) whose first differing depth-0 piece i is a -1 piece at an equal
context: r0 = first round where the ideal rounds differ; drivers = tangles learned in s whose removal from the tangle set of
s+1 undoes the change of round r0; for each driver C with top h (maximum priority, then index): h's status at round r0 in s
(dead before r0 / alive and survives r0 / alive and PRUNED at r0). Redundancy predicts "alive => survives". Also: does C
contain a tangle learned in the same search s (an in-search sub-tangle)?
Usage: dtl_mirror.py [G.pg ...] [--random N]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_pyref as D, dtl_ideal as I, pg, gen
from dtl_c6proto import C6


class Tr(C6):
    def __init__(s, *a, **k):
        super().__init__(*a, **k); s.ns = 0; s.depth = 0; s.trace = []; s.born = {}; s.piece = -1

    def search(s, p):
        s.ns += 1; s.piece = -1
        s.trace.append({"p": p, "pieces": [], "dom": s.dominions, "G": frozenset(s.G)})
        return super().search(p)

    def search_rec(s, R, p, depth):
        if depth == 1:
            s.trace[-1].setdefault("cuts", set()).add(s.piece)    # a recursion follows only a cut (-1, Q nonempty)
        od = s.depth; s.depth = depth; r = super().search_rec(R, p, depth); s.depth = od; return r

    def best_vertices(s, V, R, p):
        if s.depth == 0:
            s.piece += 1
        Rin = frozenset(R); nt = len(s.tv)
        res = super().best_vertices(V, R, p)
        if s.depth == 0:
            s.trace[-1]["pieces"].append((Rin, res, frozenset(V), nt))
        return res

    def extractTangles(s, top, R):
        b = len(s.tv); r = super().extractTangles(top, R)
        for t in range(b, len(s.tv)):
            s.born[t] = (s.ns, s.piece, s.depth, s.tpr[t])   # tpr at birth: deletion later sets tpr = -1
        return r


def rounds(d, p, R, tl):
    """Ideal rounds V_0, V_1, ...; for a -1 result the list ends with the empty set (the return set is the last
    nonempty entry)."""
    cur = {v for v in R if d.pr[v] % 2 == p}; out = [frozenset(cur)]
    while cur:
        nx = I.survivors(d, p, cur, R, I.ideal_union(d, p, cur, R, tl), tl)
        if nx == cur: break
        cur = nx; out.append(frozenset(cur))
    return out


def tl_at(d, p, n, G):
    # parity from the priority at birth (a later deletion sets tpr = -1, and -1 % 2 == 1 in Python)
    return [t for t in range(n) if d.born[t][3] % 2 == p and all(w in G for w, _ in d.tv[t])]


def analyse(d, out, name):
    for k, (a, b) in enumerate(zip(d.trace, d.trace[1:])):
        if a["p"] != b["p"] or b["dom"] != a["dom"]: continue
        pa, pb = a["pieces"], b["pieces"]; i = 0
        while i < min(len(pa), len(pb)) and pa[i][:3] == pb[i][:3]: i += 1
        if i >= min(len(pa), len(pb)) or pa[i][0] != pb[i][0] or pa[i][1] != -1: continue
        p, R, G = a["p"], pa[i][0], a["G"]
        kind = "cut" if i in a.get("cuts", set()) else "dom"            # MIRROR concerns Dom(prevV) pieces only
        out.setdefault("by_kind", {}).setdefault(kind, {"changes": 0})
        out["by_kind"][kind]["changes"] += 1
        Ta, Tb = tl_at(d, p, pa[i][3], G), tl_at(d, p, pb[i][3], G)
        ra, rb = rounds(d, p, R, Ta), rounds(d, p, R, Tb)
        r0 = next((r for r in range(1, max(len(ra), len(rb))) if (ra[r] if r < len(ra) else ra[-1]) != (rb[r] if r < len(rb) else rb[-1])), None)
        if r0 is None: continue
        out["changes"] += 1
        prev = ra[r0 - 1]
        target = rb[r0] if r0 < len(rb) else rb[-1]
        new = [t for t in Tb if d.born.get(t, (0,))[0] == k + 1]
        for C in new:
            tl = [t for t in Tb if t != C]
            if I.survivors(d, p, set(prev), R, I.ideal_union(d, p, set(prev), R, tl), tl) == target: continue
            vs = [w for w, _ in d.tv[C]]
            h = max(vs, key=lambda v: (d.pr[v], v))
            death = next((r for r in range(1, len(ra)) if h not in ra[r]), None)
            if death is not None and death < r0: st = "dead_before_r0"
            elif death == r0: st = "alive_PRUNED_at_r0"
            else: st = "alive_survives_r0"
            out[st] = out.get(st, 0) + 1
            bk = out["by_kind"][kind]; bk[st] = bk.get(st, 0) + 1
            # rescued vertices: survive round r0 with C, not without C (from the same previous round)
            tl0 = [t for t in Tb if t != C]
            S1 = I.survivors(d, p, set(prev), R, I.ideal_union(d, p, set(prev), R, Tb), Tb)
            S0 = I.survivors(d, p, set(prev), R, I.ideal_union(d, p, set(prev), R, tl0), tl0)
            resc = S1 - S0
            rel = "all_higher" if resc and all(d.pr[u] > d.pr[h] for u in resc) else ("some_lower_or_equal" if resc else "none")
            key = st.split("_")[0] + "_rescued_" + rel
            out[key] = out.get(key, 0) + 1
            sub = any(t != C and d.born.get(t, (0,))[0] == k + 1 and {w for w, _ in d.tv[t]} <= set(vs) for t in Tb)
            # MIRROR (M1) proxy: is C's escape coverage at every round r >= r0 of s+1 already present in s at round r?
            # (coverage in s: escape outside R or inside the full threshold closure of s's round-r union, computed
            # without C). All rounds covered => NOT self-reinforcing => MIRROR predicts this cannot happen.
            if st == "alive_survives_r0":
                esc = d.tout[C]; nonself = True
                # coverage that helps h itself: every escape outside R or inside W_{pr(h)-1} of s's round r (computed
                # without C); rounds of s from r0 to h's death in s (after that h is gone and redundancy says nothing)
                last = death if death is not None else len(ra) - 1
                for r in range(r0, last + 1):
                    Vr = ra[r - 1]
                    U = I.ideal_union(d, p, set(Vr), R, Ta)
                    Wh = I.lfp(d, p, U, R, d.pr[h] - 1, Ta) if d.pr[h] >= 1 else U
                    if not all(e not in R or e in Wh for e in esc):
                        nonself = False; break
                out["alive_nonselfreinforcing"] = out.get("alive_nonselfreinforcing", 0) + nonself
                bk["nonself"] = bk.get("nonself", 0) + nonself
                if nonself and kind == "dom" and len(out.setdefault("ns_ex", [])) < 3:
                    # where does MIRROR's chain break? h's death in s, coverage at that round, M_s
                    dr = death
                    Vd = ra[dr - 1] if dr is not None else None
                    covd = None
                    if Vd is not None:
                        U = I.ideal_union(d, p, set(Vd), R, Ta); Wf = I.lfp(d, p, U, R, max(d.pr), Ta)
                        covd = all(e not in R or e in Wf for e in esc)
                    out["ns_ex"].append(dict(game=name, s=k + 1, piece=i, r0=r0, C=C, Cset=sorted(vs), h=h, pr_h=d.pr[h],
                        death_s_h=dr, rounds_s=len(ra), rounds_s1=len(rb), M_s=sorted(ra[-2] if len(ra) > 1 and not ra[-1] else ra[-1]), M_s1=sorted(rb[-2] if len(rb) > 1 and not rb[-1] else rb[-1]), born=d.born[C],
                        cov_at_death=covd, h_owner=d.ow[h], h_succ=d.outs[h]))
                out["alive_selfreinforcing"] = out.get("alive_selfreinforcing", 0) + (not nonself)
            out["with_insearch_subtangle"] += sub
            if st != "alive_survives_r0" and len(out["ex"]) < 4:
                out["ex"].append((name, k + 1, i, r0, C, sorted(vs), h, death, sub, st))


def main():
    args = sys.argv[1:]
    if "--random" in args:
        j = args.index("--random"); args = args[:j] + args[j + 2:]
    files = args
    nrand = int(sys.argv[sys.argv.index("--random") + 1]) if "--random" in sys.argv else 300
    out = {"changes": 0, "with_insearch_subtangle": 0, "ex": []}
    rnd = gen.Rng("mirror"); games = [(f.split("/")[-1], pg.read(f)) for f in files]
    for i in range(nrand):
        n = rnd.randint(8, 22); games.append((f"r{i}", gen.random_game(n, rnd.randint(2, n + 1), 1, rnd.randint(1, 3), rnd.next64())))
    sys.setrecursionlimit(100000)
    for name, g in games:
        idx = sorted(range(g.n), key=lambda v: (g.prio[v], v)); new = {v: i for i, v in enumerate(idx)}
        d = Tr([g.prio[v] for v in idx], [g.owner[v] for v in idx], [[new[w] for w in g.succ[v]] for v in idx]); d.run()
        analyse(d, out, name)
    print(out)


if __name__ == "__main__":
    main()
