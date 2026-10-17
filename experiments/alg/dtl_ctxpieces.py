"""L-ALG succ. 7 (produced on Opus 5.5, 2026-10-17 box 8), GAP-A-M §23j: structure of depth-0 contexts toward (CTX⁺).
Same model as dtl_rootmono.RM (RM_DV=0 RM_LIGHT=1). Per search, ctx0 = the depth-0 best_vertices contexts in call
order (a decreasing chain from G′). Pieces = successive differences ctx0[i] \\ ctx0[i+1]. Per phase: S, distinct depth-0
contexts over all searches, distinct pieces, max chain length, and the distinct "piece sets" (a context R = G′ minus the
union of the pieces before it; if R is determined by WHICH pieces were removed, not their order, the count of contexts is
the count of distinct piece sets). Also: (PIECE-REUSE) fraction of pieces already seen earlier in the phase.
Usage: RM_DV=0 RM_LIGHT=1 DTL_ORDER=oink|stable dtl_ctxpieces.py G.pg ... (games/unions as dtl_step5stats)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_rootmono as RMM, dtl_step5stats as ST
FD = RMM.FD

if __name__ == "__main__":
    sys.setrecursionlimit(100000); rows = []; tot = {}
    for f, g in ST.games(sys.argv[1:]):
        d0 = FD.P.X.build(g); d = RMM.RM(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.run()
        nm = f if f.startswith(("union", "random")) else os.path.relpath(f)
        if not all(w is not None for w in d.win): print("INCOMPLETE", nm, flush=True)
        for ph in FD.phase_rows(d):
            if len(ph) < 2: continue
            ctxs = set(); pieces = []; seen = set(); reuse = 0; mchain = 0; nonchain = 0
            for r in ph:
                c0 = r["ctx0"]; ctxs.update(c0); mchain = max(mchain, len(c0))
                for a, b in zip(c0, c0[1:]):
                    if not b <= a: nonchain += 1
                    pc = a - b; pieces.append(pc)
                    if pc in seen: reuse += 1
                    seen.add(pc)
            npc = len(pieces)
            kc = "depth-0 contexts of a search form a decreasing chain: " + ("yes" if nonchain == 0 else "NO"); tot[kc] = tot.get(kc, 0) + 1
            rows.append((len(ctxs), len(seen), npc, reuse, mchain, len(ph), len(ph[0]["G"]), nm))
    rows.sort(reverse=True)
    print("distinct depth-0 contexts | distinct pieces | pieces (with repeats) | reused | max chain | S | |G'| | game")
    for r in rows[:20]: print(*r)
    if rows:
        print(f"phases {len(rows)}; max distinct contexts {max(r[0] for r in rows)}; max contexts/|G'| {max(r[0] / r[6] for r in rows):.3f}; max distinct pieces {max(r[1] for r in rows)}; max pieces/|G'| {max(r[1] / r[6] for r in rows):.3f}")
        print(f"reused pieces overall: {sum(r[3] for r in rows)} of {sum(r[2] for r in rows)}")
    for k in sorted(tot): print(f"{tot[k]:7d}  {k}")
