"""L-ALG (produced on Opus 5.5, 2026-10-16 box 4), GAP-A-M §18h: candidate (LEX) FAILS in an actual A_DTL run.
instances/lex_viol_oink_n20.pg (found by dtl_downclimb.py seed 201 from climbs_1016/b_best_s33.pg). Odd's phase, searches
3 -> 4 (no dominion between), alive tangles 2 -> 3 (a superset), context R = all 20 vertices, ideal (C6) result the same
stable set in both: the actual death of vertex 19 (priority 21) FALLS 12 -> 11 while the only riser above it in priority
order is vertex 17, also priority 21 but LOWER in index (death 2 -> 4). So the highest changed vertex falls, and a fall
happens at the top changed priority level. Checked in both order data (DTL_ORDER=oink and stable). Exit 0 iff reproduced.
Usage: dtl_lexviol_check.py"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, importlib
INF = 10 ** 6
deaths = lambda r: {v: next((i for i in range(len(r)) if v not in r[i]), INF) for v in r[0]}
ok = True
for order in ("oink", "stable"):
    os.environ["DTL_ORDER"] = order
    import dtl_pyref, dtl_deficit, dtl_regvec
    for m in (dtl_pyref, dtl_deficit, dtl_regvec): importlib.reload(m)
    g = pg.read(os.path.join(HERE, "instances", "lex_viol_oink_n20.pg")); d = dtl_regvec.build(g); d.run()
    occ = d.calls[(1, frozenset(range(20)))]
    (s1, r1, v1, h1, t1), (s2, r2, v2, h2, t2) = [o for o in occ if o[0] in (3, 4)]
    D1, D2 = deaths(r1), deaths(r2); ch = [v for v in sorted(D1, reverse=True) if D1[v] != D2[v]]
    top = ch[0]; i19, i17 = d.idx.index(19), d.idx.index(17)
    good = (set(t1) <= set(t2) and h1 == h2 and h1[0] == 1 and d.idx[top] == 19 and (D1[i19], D2[i19]) == (12, 11)
            and (D1[i17], D2[i17]) == (2, 4) and d.pr[i19] == d.pr[i17] == 21)
    print(f"order {order}: searches {s1}->{s2}, |T| {len(t1)}->{len(t2)}, ideal same stable {h1 == h2 and h1[0] == 1}, "
          f"top changed vertex {d.idx[top]} death {D1[top]}->{D2[top]}; vertex 17 {D1[i17]}->{D2[i17]}: {'LEX-VIOLATION REPRODUCED' if good else 'NOT reproduced'}")
    ok &= good
sys.exit(0 if ok else 1)
