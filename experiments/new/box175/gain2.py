#!/usr/bin/env python3
"""L-NEW box 175: gain''(G) := T(G) - max over acyclic re-routings of the couplings AND over all starts of the lower genome of
T(G - top) (the start-free reading; the start-free reading is weaker as a conjecture, so a kill of it kills both). Lower genomes with
more than 2^14 starts are skipped. Usage: gain2.py files..."""
import os, sys, json, itertools
H = os.path.dirname(os.path.abspath(__file__))
g = {"__file__": os.path.join(H, "gain.py"), "__name__": "lib"}; exec(open(g["__file__"]).read().split("\nif __name__")[0], g)
def gain2(G, maxC=1):
    tau, top, cp = g["couplings"](G)
    if len(cp) > maxC: return None
    low = [x for x in range(G["N"]) if x not in top]; best = -1
    if len(low) > 14: return None
    for choice in itertools.product(*[[-1] + low for _ in cp]):
        H_ = g["lower"](G, top, dict(zip(cp, choice)))
        if not g["acyc"](H_["N"], H_["opts"]): continue
        gn = g["Gen"](H_)
        for st in itertools.product(*[range(len(o)) for o in H_["opts"]]):
            S, _ = gn.run(st); best = max(best, len(S) - 1)
    return len(cp), g["T"](G), best, g["T"](G) - best
if __name__ == "__main__":
    for f in sys.argv[1:]:
        try: G = json.load(open(f)); assert "opts" in G and "start" in G and max(len(o) for o in G["opts"]) <= 2
        except Exception: continue
        try: r = gain2(G)
        except Exception: continue
        if r: print("%-34s C %d T %3d bestlow(all starts) %3d gain'' %d" % (os.path.basename(f)[:34], *r), flush=True)
