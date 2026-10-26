#!/usr/bin/env python3
"""Box 46: pin a climb best (json with prio, owner, succ, start) as NAME.pg + NAME.start.json; re-run rec0_20 with Oink and print the result.
Usage: pin20.py best.json NAME"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import rec0_20 as R0, pg
j = json.load(open(sys.argv[1])); nm = os.path.join(HERE, "instances", sys.argv[2])
g = pg.Game(j["prio"], j["owner"], [sorted(set(s)) for s in j["succ"]]); pg.write(g, nm + ".pg")
g2 = pg.parse("".join(l for l in open(nm + ".pg") if not l.lstrip().startswith("%")))
json.dump(dict(start=j["start"]), open(nm + ".start.json", "w"))
r = R0.analyse(g2, j["start"], True, budget=400000); print(json.dumps(r))
