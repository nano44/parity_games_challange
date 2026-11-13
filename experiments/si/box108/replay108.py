#!/usr/bin/env python3
"""Box 108 (L-SI 56): second engine.  Compare the state sequence of the own simulator (ideal108) on G_k with L-NEW's one217.OneP
(rule "key"); argv: DIR_OF_one217 KLO KHI.  Prints one line per k with a sha1 of the state sequence, and the run lengths of one217's
two other rules ("howard": every mover to its Xi-best option; "seq": the key step applied at one mover at a time) as DATA."""
import sys, os, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, sys.argv[1])
import gk108, ideal108, one217
bad = 0
for k in range(int(sys.argv[2]), int(sys.argv[3]) + 1):
    G, names = gk108.build(k); S = ideal108.Ideal(G).run(); P = one217.OneP(G); S2 = [tuple(s) for s in P.run("key")]
    same = int(S == S2); bad += 1 - same
    print(f"G_{k} N {G['N']} L_ideal108 {len(S) - 1} L_one217 {len(S2) - 1} same_states {same} states_sha1 {hashlib.sha1(repr(S).encode()).hexdigest()}"
          f" | other rules of one217 on the same genome (DATA, not the IDEAL step): howard {len(P.run('howard')) - 1} seq {len(P.run('seq')) - 1}", flush=True)
print("REPLAY108", "PASS" if bad == 0 else "FAIL"); sys.exit(1 if bad else 0)
