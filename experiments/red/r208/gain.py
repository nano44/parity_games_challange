#!/usr/bin/env python3
"""L-RED R208 GAIN: for an extended genome E (top level = max level; lower movers = indices < N0 = number of non-top movers, which
coupext.py places first), C := #lower options with Xi-target in the top level; gain_x := T(E) - T(E^-) (coupled targets -> X);
gain' := T(E) - max over re-routings (X or any lower mover, acyclic; exhaustive for C <= 2, coordinate ascent else). Usage: gain.py E.json ..."""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
import coupext
for f in sys.argv[1:]:
    E = json.load(open(f)); top = max(E["lev"]); N0 = sum(1 for l in E["lev"] if l < top)
    assert all(E["lev"][v] < top for v in range(N0))
    P = {"coup": [(x, k, None) for x in range(N0) for k in range(len(E["opts"][x])) if E["opts"][x][k][1] >= N0]}
    t = coupext.T(E); tx = coupext.T(coupext.minus(E, N0)); tb = coupext.bestlow(E, {"N": N0}, P)
    print(f"{os.path.basename(f)}: d {top + 1} T {t} C {len(P['coup'])} T(E^-) {tx} gain_x {t - tx} best lower routing {tb} gain' {t - tb}")
