"""L-ALG (produced on Opus 5.5, 2026-10-16), GAP-A-M.md §16. Staircase at a fixed Dom(prevV) context (C6): for consecutive
searches of a phase whose depth-0 piece j has the same context and result -1, with M = max death (the round of the
return set): check Lemma S (M never drops; at equal M the return set only grows), classify each change of the next
index's context: 'M_up' (M rose, return set reset to the new leaders), 'same_M_grow' (return set grew at equal M),
'dom_only' (equal return set, Dom grown); and FRESH (context never seen before at j+1 in the phase) vs RECUR.
Usage: dtl_stair.py [G.pg ...] (plus STAIR_RANDOM random games)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_mirror as M, pg, gen

def run(d, st, name):
    phase = []
    def flush():
        L = max((len(tr["pieces"]) for tr in phase), default=0)
        for j in range(L - 1):
            seen = set()
            for a, b in zip(phase, phase[1:]):
                if j + 1 >= min(len(a["pieces"]), len(b["pieces"])): continue
                seen.add(a["pieces"][j + 1][0])
                pa, pb = a["pieces"][j], b["pieces"][j]
                if pa[0] != pb[0] or pa[1] != -1 or pb[1] != -1 or j in a.get("cuts", set()) or j in b.get("cuts", set()): continue
                def Mof(tr, P):
                    rr = M.rounds(d, tr["p"], P[0], M.tl_at(d, tr["p"], P[3], tr["G"])); return len(rr) - 1
                Ma, Mb = Mof(a, pa), Mof(b, pb)
                if Mb < Ma: st["S_M_drop"] += 1; st["ex"].append((name, j)) if len(st["ex"]) < 3 else None
                if Mb == Ma and not pa[2] <= pb[2]: st["S_sameM_not_grow"] += 1; st["ex"].append((name, j, "nogrow")) if len(st["ex"]) < 3 else None
                Ca, Cb = a["pieces"][j + 1][0], b["pieces"][j + 1][0]
                if Ca == Cb: continue
                kind = "M_up" if Mb > Ma else ("same_M_grow" if pa[2] != pb[2] else "dom_only")
                fr = "FRESH" if Cb not in seen else "RECUR"
                st[kind + "_" + fr] = st.get(kind + "_" + fr, 0) + 1
                # reset at j+1: some vertex common to both child contexts dies earlier in b than in a
                qa, qb = a["pieces"][j + 1], b["pieces"][j + 1]
                ra_ = M.rounds(d, a["p"], qa[0], M.tl_at(d, a["p"], qa[3], a["G"])); rb_ = M.rounds(d, b["p"], qb[0], M.tl_at(d, b["p"], qb[3], b["G"]))
                def dd(rr, v):
                    for r in range(1, len(rr)):
                        if v in rr[r - 1] and v not in rr[r]: return r
                    return 10 ** 6
                common = rb_[0] & ra_[0]
                reset = any(dd(rb_, v) < dd(ra_, v) for v in common)
                st[kind + "_" + fr + ("_RESET" if reset else "_noreset")] = st.get(kind + "_" + fr + ("_RESET" if reset else "_noreset"), 0) + 1
            seen.clear()
    for tr in d.trace:
        if phase and (tr["p"] != phase[-1]["p"] or tr["dom"] != phase[-1]["dom"]): flush(); phase = []
        phase.append(tr)
    if phase: flush()

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    games = [(f.split("/")[-1], pg.read(f)) for f in sys.argv[1:]]
    rnd = gen.Rng("stair")
    for i in range(int(os.environ.get("STAIR_RANDOM", "400"))):
        n = rnd.randint(8, 26); games.append((f"r{i}", gen.random_game(n, rnd.randint(2, n + 1), 1, rnd.randint(1, 3), rnd.next64())))
    st = dict(S_M_drop=0, S_sameM_not_grow=0, ex=[])
    for name, g in games:
        idx = sorted(range(g.n), key=lambda v: (g.prio[v], v)); new = {v: i for i, v in enumerate(idx)}
        d = M.Tr([g.prio[v] for v in idx], [g.owner[v] for v in idx], [[new[w] for w in g.succ[v]] for v in idx]); d.run()
        run(d, st, name)
    print("games", len(games)); print(st)
