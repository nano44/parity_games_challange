#!/usr/bin/env python3
"""L-NEW box 159: REVERSED LIFT. Like box158/lift.py, but each old level-0 mover x points its G-key-preferred option (smaller own
gate) to new level-0 mover A and its other option to B. A starts at its Xi-WORSE option, which carries the LARGER gate; its better
option has the smallest gate overall. B never moves. So under A's start option the level-1 key order is reversed against G; A moves at
step 1 (unstable, key-preferred), and from the new state on the order is G's. Usage: liftrev.py in.json out.json"""
import sys, os, json
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box150", "check.py")
ns = {"__file__": P}; exec(open(P).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
G = json.load(open(sys.argv[1])); N = G["N"]; M = sum(len(o) for o in G["opts"]); A, B = N, N + 1
gate = [[gg + 10 for gg in x] for x in G["gate"]]          # shift old gates up; new small gates below
opts = []
for x in range(N):
    o = [list(v) for v in G["opts"][x]]
    if G["lev"][x] == 0:
        pref = min(range(len(o)), key=lambda k: G["gate"][x][k])
        for k in range(len(o)): o[k][0] = A if k == pref else B
    opts.append(o)
br = list(G["br"]); bp = list(G["bp"]); mr = max(br) + 1
# A: option 0 = Xi-better (rank mr+1 even), gate 0 (smallest); option 1 = worse (rank mr, even), gate 3. Start A at 1.
# B: option 0 better (rank mr+3 even), gate 1; option 1 worse (rank mr+2), gate 2; start B at 0 (never moves).
opts.append([[-1, -1, M], [-1, -1, M + 1]]); gate.append([0, 3]); br += [mr + 1, mr]; bp += [0, 0]
opts.append([[-1, -1, M + 2], [-1, -1, M + 3]]); gate.append([1, 2]); br += [mr + 3, mr + 2]; bp += [0, 0]
Gh = {"N": N + 2, "lev": [l + 1 for l in G["lev"]] + [0, 0], "opts": opts, "gate": gate, "br": br, "bp": bp,
      "start": list(G["start"]) + [1, 0], "xorder": list(G.get("xorder", range(N))) + [A, B]}
json.dump(Gh, open(sys.argv[2], "w"))
S, _ = Gen(G).run(G["start"]); Sh, _ = Gen(Gh).run(Gh["start"])
print(f"LIFTREV {os.path.basename(sys.argv[1])} T {len(S)-1} -> T^ {len(Sh)-1}; old-mover states equal: {[tuple(s[:N]) for s in Sh] == [tuple(s) for s in S]}")
