#!/usr/bin/env python3
"""Family L_k of docs/new/N8a-kohloho.md §6: the 15-node crawl core (instances/n8a/nest_core.pg) plus k isolated Even self-loops with new
even priorities above every existing one (levels start adding at k = 2). Usage: gen_lk.py k > out.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness")); import pg
k = int(sys.argv[1]); g = pg.parse(open(os.path.join(HERE, "..", "instances", "n8a", "nest_core.pg")).read()); top = max(g.prio)
pr = list(g.prio) + [top + 2 * (i + 1) + ((top + 2 * (i + 1)) % 2) for i in range(k)]
sys.stdout.write(pg.dumps(pg.Game(pr, list(g.owner) + [0] * k, [list(s) for s in g.succ] + [[g.n + i] for i in range(k)])))
