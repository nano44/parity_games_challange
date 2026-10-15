#!/usr/bin/env python3
"""Which bits of a chain program's gate outputs determine W on Q_n? Minimal determining subsets, and the induced function."""
import sys, os, json, itertools
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from quotient import build
from slp import eval_struct

f = sys.argv[1]; n = int(sys.argv[2])
d = json.load(open(f)); prog = [tuple(g) for g in d["program"]]
q = build(n)
vals = eval_struct(prog, q.S, keep=True)
cp = [i for i, g in enumerate(prog) if g[0] == "cpre"]
bits = [q.S.prio == 2] + [vals[i] for i in cp]
names = ["P2"] + [f"s{j+1}" for j in range(len(cp))]
M = np.stack(bits, 1).astype(np.int64)
W = q.W
def determines(idx):
    key = M[:, idx] @ (2 ** np.arange(len(idx)))
    tab = {}
    for k_, w in zip(key, W):
        if tab.setdefault(k_, w) != w: return False
    return True
print("all bits determine W:", determines(list(range(M.shape[1]))))
for r in range(1, M.shape[1] + 1):
    found = [c for c in itertools.combinations(range(M.shape[1]), r) if determines(list(c))]
    if found:
        print(f"minimal determining subsets of size {r}: {[[names[i] for i in c] for c in found][:8]}")
        c = found[0]
        key = M[:, list(c)] @ (2 ** np.arange(len(c)))
        tab = {}
        for k_, w in zip(key, W): tab[k_] = w
        rows = sorted(tab.items())
        print("   function:", {format(k_, f'0{len(c)}b')[::-1]: int(w) for k_, w in rows})
        print("   (bit order in key:", [names[i] for i in c], ")")
        break
