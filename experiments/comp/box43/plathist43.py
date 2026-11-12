#!/usr/bin/env python3
"""L-COMP box 43 item 1 (a): L-NEW 72's PLATEAU counters (claude/l-new 8db300fe experiments/new/box208/plat208.py, function plateaus:
p1, pclos, p2, p3, p4, p5 of box 208 Addendum A (P1)-(P7)) run on a history file in level208.py's --hist format (plat208.py has no
--hist mode at 8db300fe; this wrapper calls its function on level208.load(HIST)). The counter code is L-NEW's, unchanged; the history
is whatever engine wrote the file (mine: hist43.py). env LNEW208 = a checkout / archive of claude/l-new 8db300fe.
Usage: plathist43.py HIST.json ..."""
import sys, os, collections
sys.path.insert(0, os.path.join(os.environ["LNEW208"], "experiments", "new", "box208"))
import level208, plat208
for fn in sys.argv[1:]:
    c = collections.Counter(); plat208.plateaus(level208.load(fn), c)
    print("plat", os.path.basename(fn), "ctrl", plat208.CTRL, " ".join("%s %d" % (k, c[k]) for k in plat208.KEYS), flush=True)
