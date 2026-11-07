#!/bin/bash
# REC-K screen: mu_k <= 1 + ceil(k/2) on every ISO R197 genome file given, k = 0..8. Prints one line per (file, k) and a summary.
H=$(dirname "$0")
python3 - "$@" <<'PY'
import os, sys, json
H = os.path.dirname(os.path.abspath(sys.argv[0])) if False else os.environ.get("BOX", ".")
exec(open(os.path.join(H, "fk.py")).read().split("\nif __name__")[0])
sys.setrecursionlimit(100000); kills = 0; n = 0
for f in sys.argv[1:]:
    G = json.load(open(f))
    if not (fns["is_lr"](G) and fns["is_iso"](G)) or G["N"] > 10: continue
    row = []
    for k in range(9):
        T, mu, arg = muk(G, k); b = 1 + (k + 1) // 2; n += 1
        if mu > b: kills += 1; print("KILL", os.path.basename(f), k, mu, arg)
        row.append("%d/%d" % (T, mu))
    print("%-28s T_k/mu_k k=0..8: %s" % (os.path.basename(f), " ".join(row)), flush=True)
print("RECK checked %d (file,k) pairs, kills %d" % (n, kills))
PY
