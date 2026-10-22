"""L-RED box 10: print the control vertices (T_j, helpers h*) of a schemaclimb game: priority, owner, successors by name.
Usage: SKEL=3|4 ctrlshow.py G.pg D [NH]"""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import lag3, lag4
D = int(sys.argv[2]); NH = int(sys.argv[3]) if len(sys.argv) > 3 else 3
ids = (lag4 if os.environ.get("SKEL") == "4" else lag3).build(D).ids; inv = {v: k for k, v in ids.items()}; inv.update({len(ids) + h: f"h{h}" for h in range(NH)})
base = {}
for part in open(sys.argv[1]).read().split(";")[1:]:
    p = part.split()
    if len(p) < 4: continue
    nm = inv[int(p[0])]; succ = [inv[int(x)] for x in p[3].split(",")]
    if (nm[0] == "T" or nm[0] == "h") or os.environ.get("ALL"): print(nm, "pr", p[1], "own", p[2], "->", succ)
