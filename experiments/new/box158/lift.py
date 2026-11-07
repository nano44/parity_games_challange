#!/usr/bin/env python3
"""L-NEW box 158: LIFT. From a genome G (levels 0..d-1) build G^ with levels 0..d: two new level-0 movers A, B of degree 2 that never
move (both options Xi-target X; the start option has the larger even-parity rank among the two), every old mover one level up, old
level-0 options get W-target A, gates and ranks of the new options above all old ones. Claim (Lemma LIFT): the run of G^ from
(start of G, A and B at their start) has the same states on the old movers, so T(G^) = T(G), and no level-0 mover of G^ moves.
Usage: lift.py in.json out.json  (prints T of both)"""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": os.path.abspath(P)}; exec(open(P).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
G = json.load(open(sys.argv[1])); N = G["N"]; M = sum(len(o) for o in G["opts"]); A, B = N, N + 1
opts = [[[A if G["lev"][x] == 0 else o[0], o[1], o[2]] for o in G["opts"][x]] for x in range(N)]
gate = [list(gg) for gg in G["gate"]]; br = list(G["br"]); bp = list(G["bp"]); mg = max(max(gg) for gg in gate) + 1; mr = max(br) + 1
for i, y in enumerate((A, B)):
    opts.append([[-1, -1, M + 2 * i], [-1, -1, M + 2 * i + 1]]); gate.append([mg + 2 * i, mg + 2 * i + 1])
    br += [mr + 2 * i + 1, mr + 2 * i]; bp += [0, 0]          # option 0: larger rank, even parity -> better; start at 0: stable
Gh = {"N": N + 2, "lev": [l + 1 for l in G["lev"]] + [0, 0], "opts": opts, "gate": gate, "br": br, "bp": bp,
      "start": list(G["start"]) + [0, 0], "xorder": list(G.get("xorder", range(N))) + [A, B]}
json.dump(Gh, open(sys.argv[2], "w"))
S, _ = Gen(G).run(G["start"]); Sh, _ = Gen(Gh).run(Gh["start"])
same = [tuple(s[:N]) for s in Sh] == [tuple(s) for s in S] and all(s[N:] == (0, 0) for s in Sh)
print(f"LIFT {os.path.basename(sys.argv[1])} T {len(S) - 1} -> T^ {len(Sh) - 1} levels {max(G['lev']) + 1} -> {max(Gh['lev']) + 1} SAME {same}")
