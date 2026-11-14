"""REFEREE successor 26: static parts of P-IDEAL-DBL §6 (own code): MAXPLUS (mover 6 a Xi-target; strict Xi-descendants of 6 and their
moves, from dbl_replay); RE-ENTRY (upward options of low movers whose Xi-target has an option pointing down). Usage: LSI_ROOT"""
import sys, os, json; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dbl_replay as D
R = sys.argv[1] + "/experiments/si/box76/inst/"
G = json.load(open(R + "dense_d5_l3_H10.json")); o, st = D.analyse(G, [int(c) for c in "1100110110"])
targets = {G["opts"][x][k][1] for x in range(G["N"]) for k in range(2)} - {-1}
desc = set(); stack = [6]
while stack:
    x = stack.pop()
    for k in range(2):
        y = G["opts"][x][k][1]
        if y >= 0 and y not in desc: desc.add(y); stack.append(y)
print("MAXPLUS: mover 6 level", G["lev"][6], "Xi-target", 6 in targets, "moves(6)", o["moves"][6], "max moves levels 0-2",
      max(o["moves"][x] for x in range(6)), "strict Xi-descendants of 6", sorted(desc), "their max moves", max((o["moves"][y] for y in desc), default=0))
for f, x, low in (("lower/REC_d10_tower_mu30.json", 11, 1), ("lower/KILL_M2D_d6_mu13.json", 5, 2)):
    G = json.load(open(R + f)); lev = G["lev"]
    up = [(z, k) for z in range(G["N"]) for k in range(2) if G["opts"][z][k][1] == x and lev[z] < lev[x]]
    down = [(k, G["opts"][x][k][1], lev[G["opts"][x][k][1]]) for k in range(2) if G["opts"][x][k][1] >= 0 and lev[G["opts"][x][k][1]] < lev[x]]
    print("RE-ENTRY", f, "mover", x, "level", lev[x], "upward options pointing to it from levels", sorted({lev[z] for z, k in up}), up,
          "its options with lower Xi-target (k, target, level)", down)
