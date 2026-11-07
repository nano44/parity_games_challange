#!/usr/bin/env python3
"""L-NEW box 171 (1): frozen-interval accounting on real IDEAL runs. Top level = max level. A step is LOWER if some mover below the
top level moves, else TOP-ONLY. Counts: T, L := #lower steps, TO := #top-only steps, I := #maximal runs of consecutive top-only steps
(«frozen intervals with top moves»), gaps := L + 1 (the number of places such a run can sit), and for the restriction H := the genome
without its top level (only meaningful when no lower option Xi-targets a top mover: flag 'autonomous'), T(H) from its own run.
Usage: frozen.py file.json ..."""
import os, sys, json
H_ = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(H_, "..", "box165", "permover.py")).read().split("\nif __name__")[0])
def restrict_top(G):
    top = max(G["lev"]); keep = [v for v in range(G["N"]) if G["lev"][v] < top]; idx = {v: i for i, v in enumerate(keep)}
    if any(o[1] >= 0 and G["lev"][o[1]] == top for v in keep for o in G["opts"][v]): return None
    opts = [[[o[0] if o[0] < 0 else idx[o[0]], o[1] if o[1] < 0 else idx[o[1]], o[2]] for o in G["opts"][v]] for v in keep]
    return {"N": len(keep), "lev": [G["lev"][v] for v in keep], "opts": opts, "gate": [G["gate"][v] for v in keep], "br": G["br"],
            "bp": G["bp"], "start": [G["start"][v] for v in keep]}
rows = []
for f in sys.argv[1:]:
    try: G = json.load(open(f)); assert "N" in G; S, _ = Gen(G).run(G["start"])
    except Exception: continue
    top = max(G["lev"]); low = [v for v in range(G["N"]) if G["lev"][v] < top]
    kinds = ["L" if any(S[t][v] != S[t - 1][v] for v in low) else "T" for t in range(1, len(S))]
    L = kinds.count("L"); TO = kinds.count("T"); I = sum(1 for i, k in enumerate(kinds) if k == "T" and (i == 0 or kinds[i - 1] == "L"))
    maxrun = max([len(r) for r in "".join(kinds).split("L")] + [0])
    Hg = restrict_top(G); TH = None
    if Hg is not None:
        try: TH = len(Gen(Hg).run(Hg["start"])[0]) - 1
        except Exception: TH = None
    rows.append((os.path.basename(f), G["N"], top + 1, len(S) - 1, L, TO, I, maxrun, TH, "".join(kinds)))
for r in sorted(rows, key=lambda r: -r[3])[:40]:
    print("%-30s N %2d d %d T %3d lower %3d top-only %2d intervals %2d maxrun %d T(H) %s  %s" % (r[0][:30], *r[1:9], r[9][:70]))
tot = [r for r in rows]; print("files", len(tot), "max intervals", max(r[6] for r in tot), "max top-only", max(r[5] for r in tot), "max maxrun", max(r[7] for r in tot))
