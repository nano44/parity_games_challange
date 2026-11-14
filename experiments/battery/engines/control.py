#!/usr/bin/env python3
"""Control engines for the self-test: each one is WRONG on purpose and the battery must say so.
Usage: control.py --flip-winner | --drop-strategy | --odd-cycle | --sleep | --garbage  GAME.pg
 --flip-winner: Zielonka's answer with the winner of vertex 0 flipped            -> WRONG-WINNER, exit 1
 --drop-strategy: Zielonka's answer with one strategy entry removed              -> BAD-STRATEGY, exit 1
 --odd-cycle: right winners; every winner-owned vertex with a self-loop plays it (on sets/x_control/loop2.pg that closes
   an odd cycle inside Even's region)                                            -> BAD-STRATEGY, exit 1
 --sleep: never answers                                                          -> TIMEOUT, exit 0
 --garbage: prints no JSON                                                       -> ERROR, exit 2"""
import sys, os, json, subprocess, time
mode, game = sys.argv[1], sys.argv[-1]
if mode == "--sleep": time.sleep(10 ** 6)
if mode == "--garbage": print("no json here"); sys.exit(0)
o = json.loads(subprocess.run([sys.executable, "-B", os.path.join(os.path.dirname(os.path.abspath(__file__)), "zielonka.py"), game], capture_output=True, text=True, check=True).stdout)
if mode == "--flip-winner": o["winner"][0] ^= 1
elif mode == "--drop-strategy": del o["strategy"][sorted(o["strategy"], key=int)[0]]
elif mode == "--odd-cycle":
    for line in open(game):
        p = line.strip().rstrip(";").split()
        if len(p) >= 4 and p[0].isdigit() and p[0] in o["strategy"] and p[0] in p[3].split(","): o["strategy"][p[0]] = int(p[0])
print(json.dumps(o))
