#!/usr/bin/env python3
"""P-IDEAL-IM line L-3 = line L-2 with exactly the five replacements R1-R5 of CHECKER C128 (fixes entry 2); each old string must
occur exactly once in L-2. Usage: mkL3.py L2 OUT"""
import sys
R = [
 ("LOCAL (IM (a)) 0 on 250,248;",
  "LOCAL 0 on 250,248 (y on neither chain, unhappy or not), among them IM (a) on the 125,124 with y unhappy;"),
 ("BIT-CHAIN (i) 0 on 66,520,",
  "BIT-CHAIN (i) at the c-step image of the state 0 on 66,520 (5,670 distinct (genome, c, image) triples),"),
 ("own c-step = the box 64 simulator 0 on 18,944;",
  "own c-step = the box 64 simulator 0 on 18,944, on the 301 genomes the box 64 simulator accepts;"),
 ("the negated schedule disagreeing 21,234 times on K's part and 54,433 times on G's;",
  "the negated schedule failing 54,433 times on G's part (30,113 steps and 24,320 end-of-run checks) and 21,234 times on K's (end-of-run checks after a failure on G's part only; K's steps do not use the schedule);"),
 ("COMPOSE-LB and the T_∞ bound: no separate DATA;",
  "BIT-CHAIN (ii), COMPOSE-LB and the T_∞ bound: no separate DATA;"),
]
s = open(sys.argv[1], encoding="utf-8").read()
for i, (o, n) in enumerate(R, 1):
    c = s.count(o)
    if c != 1: raise SystemExit("R%d: old string occurs %d times" % (i, c))
    s = s.replace(o, n)
open(sys.argv[2], "w", encoding="utf-8").write(s)
print("L-3 written; %d bytes" % len(s.encode()))
