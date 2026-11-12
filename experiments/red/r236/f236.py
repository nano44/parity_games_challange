#!/usr/bin/env python3
"""L-RED 66 R236: faithfulness check of L-SI 52's F_n (claude/l-si 26704e01 experiments/si/box104/inst) with L-RED's own engine.
Per file: (1) parity-game validity in TARGET.md §1's sense as the .pg encodes it: header 'parity K' with K = max id, ids 0..K each once,
owners in {0, 1}, priorities >= 0 integers, every vertex >= 1 successor, every successor id in range (no dead ends = total edges);
(2) N5'-xi from SPEC S3 with n5x236 (iterations, fallbacks) and N5 spec-mode (n5x236 mode spec: SPEC with my tie readings);
(4) regions against the harness Zielonka (must-0 regfail). Usage: f236.py FILE.pg ..."""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [HERE, os.path.join(ROOT, "experiments/harness")]
import n5x236 as X, pg, zielonka
for fn in sys.argv[1:]:
    lines = [l.strip() for l in open(fn) if l.strip()]
    K = int(re.match(r"parity (\d+);", lines[0]).group(1)); ids = []; bad = []
    for l in lines[1:]:
        if l.startswith("start"): continue
        p = l.rstrip(";").split()
        v, pr, o = int(p[0]), int(p[1]), int(p[2]); ss = [int(x) for x in p[3].split(",") if x != ""]
        ids.append(v)
        if o not in (0, 1): bad.append(("owner", v))
        if pr < 0: bad.append(("prio", v))
        if not ss: bad.append(("deadend", v))
        if any(w < 0 or w > K for w in ss): bad.append(("range", v))
    if sorted(ids) != list(range(K + 1)): bad.append(("ids", len(ids), K + 1))
    prio, owner, succ = X.parse(fn)
    it, fb, win, s, sb = X.run(prio, owner, succ, "xi")
    its, fbs, wins, _, _ = X.run(prio, owner, succ, "spec")
    z = zielonka.solve(pg.Game(prio, owner, succ))
    rf = sum(1 for v in range(len(prio)) if (0 if win[v] else 1) != z[v]); rfs = sum(1 for v in range(len(prio)) if (0 if wins[v] else 1) != z[v])
    sl = sum(1 for v in range(len(prio)) if v in succ[v])
    print(os.path.basename(fn), "|V|", len(prio), "edges", sum(map(len, succ)), "maxprio", max(prio), "selfloops", sl, "valid", not bad, bad[:3],
          "| xi iterations", it, "fallbacks", fb, "| spec(my ties) iterations", its, "fallbacks", fbs,
          "| Even wins", sum(win), "zielonka Even", z.count(0), "regfail xi", rf, "spec", rfs, flush=True)
