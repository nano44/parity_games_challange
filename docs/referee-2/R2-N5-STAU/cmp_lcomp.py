#!/usr/bin/env python3
"""REFEREE-2 succ. 15: run stau_check (all §1 checks) on L-COMP's pinned N5^tau instances (l-comp 16c960b5, copied to lcomp_pinned/);
count S4b^tau keeps ALONG THE N5^tau RUN (tau kept where SPEC's S4b moves it) and whether the N5^tau run differs from SPEC's."""
import sys, os
import stau_check as S
for base in sys.argv[1:]:
    g = S.pg.read(base + ".pg"); s, t = [x[0] for x in g.succ], [x[0] for x in g.succ]
    for line in open(base + ".start"):
        p = line.split()
        if not p or p[0].startswith("#"): continue
        tgt = s if p[0] == "SIGMA0" else t
        for kv in p[1:]:
            v, w = map(int, kv.split(":")); tgt[v] = w
    st = S.Stats()
    S.run_game(g, s, t, st, os.path.basename(base))
    states, fbs, infos = S.run(g, s, t, S.Stats(), "x", True)
    keeps = sum(1 for k, inf in enumerate(infos) if inf["It"] and list(states[k + 1][1]) == list(states[k][1]) and list(inf["s4b_spec"]) != list(states[k][1]))
    print(os.path.basename(base), "n", g.n, "N5tau_len", len(infos), "keeps_along_N5tau", keeps, "RUNS_differ", st.c.get("RUNS_differ", 0),
          "R48_max_f", st.c.get("R48_max_f"), "violations", st.c.get("VIOLATIONS", 0))
