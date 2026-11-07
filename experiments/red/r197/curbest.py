import sys, os, json, glob
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178"), os.path.join(H, "..", "r190")]
import anal, delclimb
for f in sorted(sys.argv[1:]):
    try: G = json.load(open(f))
    except Exception: continue
    L, why, F, M, Dl, lagn, off = anal.run(G, 2); os.environ["SCORE"] = "U"; _, U, perU = delclimb.stats(G, 2)
    print(os.path.basename(f), "L", L, "U", U, "F", F, "moves", M, "DELAY", Dl)
