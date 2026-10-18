#!/usr/bin/env python3
"""L-RED box 10 (produced on Opus 5.5): UNIFORM candidate family for R39: lag4 skeleton with a fixed control rule
T_j -> RULE (default "x1,tau": T_j -> {x_1, tau_j}); no helpers. Usage: lagfam.py D out.pg [RULE]"""
import sys; sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__))); import lag4
def build(D, rule="x1,tau"):
    g = lag4.build(D, tedge=None)
    for j in range(-1, D + 1):
        tg = [("tau" + str(j) if r == "tau" else "y" + str(j) if r == "y" else r) for r in rule.split(",")]
        g.out[g.ids[f"T{j}"]] = []; g.e(f"T{j}", *tg)
    return g
if __name__ == "__main__":
    a = sys.argv; build(int(a[1]), a[3] if len(a) > 3 else "x1,tau").write(a[2])
