#!/usr/bin/env python3
"""L-RED-B B6 attempt 2: the key run of a genome on THREE simulators of the same model, state by state.
  A  onep.py            (this lane; written from box 217 par. 6.1's text)
  B  one217.OneP        (L-NEW box 217, claude/l-new a143d406; LNEW tree)
  C  r187/ideal.traj    (L-RED R187, the IDEAL model's simulator named in RESULTS R104's packet; LRED tree)
Per genome one line: N, M, levels, T (steps of A), TB, TC, ideq (must be 0: 1 if the three state sequences are not identical),
maxsw (largest number of switches of one mover), sumsw, howard (Howard steps on A), stop (C's stop word: stuck / opt),
k (box 217's enumeration depth on A), mindeg.
Control B6SIM_CTRL=1: simulator A runs with the gate numbers of the first level-0 mover's options swapped (ideq must fire on G_k).
Usage: b6sim.py LNEW LRED G.json ..."""
import sys, os, json, copy
LNEW, LRED = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
sys.path[:0] = [os.path.join(LNEW, "experiments/new/box217"), os.path.join(LRED, "experiments/red/r187")]
import onep
import one217
import ideal
CTRL = os.environ.get("B6SIM_CTRL", "0")

for fn in sys.argv[3:]:
    G = onep.load(fn)
    GA = G
    if CTRL == "1":
        GA = copy.deepcopy(G)
        x = next(x for x in range(G["N"]) if G["lev"][x] == 0 and G["start"][x] == 0 and len(G["opts"][x]) == 2 and x > 0)
        GA["gate"][x] = GA["gate"][x][::-1]
    SA = onep.OneP(GA).run("key")
    SB = one217.OneP(G).run("key")
    SC, stop = ideal.traj(G, cap=10 ** 7)
    ideq = int(not ([tuple(s) for s in SA] == [tuple(s) for s in SB] == [tuple(s) for s in SC]))
    st = onep.stats(GA, SA)
    H = onep.OneP(G).run("howard")
    M = sum(len(o) for o in G["opts"])
    print(f"{os.path.basename(fn)} ctrl {CTRL} N {G['N']} M {M} levels {max(G['lev']) + 1} T {len(SA) - 1} TB {len(SB) - 1} TC {len(SC) - 1} ideq {ideq} "
          f"maxsw {max(st['sw'])} sumsw {sum(st['sw'])} howard {len(H) - 1} stop {stop} k {st['k']} mindeg {min(len(o) for o in G['opts'])}", flush=True)
