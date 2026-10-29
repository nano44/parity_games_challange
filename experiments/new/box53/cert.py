#!/usr/bin/env python3
"""L-NEW box 53: EXACT re-check (pure Python, integers; no LP library) of an obstruction certificate written by mkcert.py.
A certificate {game, start, fam, y: [[t, y_t], ...]} says: with Delta_t := f(s_{t+1}) - f(s_t) (feat.py feature family fam, N5 run of
game from start), the y_t are positive integers and sum_t y_t Delta_t = 0. Then no c has c . Delta_t >= 1 at those t (sum y_t (c . Delta_t)
would be > 0 and = 0), i.e. the game has NO linear ranking function over that feature family (Farkas / Gordan).
Prints CERT OK / CERT FAIL per file. Usage: cert.py CERT.json..."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, HERE); import feat
ok_all = True
for f in sys.argv[1:]:
    C = json.load(open(f)); X = lambda q: q if os.path.isabs(q) else os.path.join(ROOT, q)
    S = feat.states(feat.load(X(C["game"])), feat.readstart(X(C["start"])) if C.get("start") else None)
    k = len(S[0][C["fam"]]); tot = [0] * k; ok = all(y > 0 for _, y in C["y"]) and len(C["y"]) > 0
    for t, y in C["y"]:
        for j in range(k): tot[j] += y * (S[t + 1][C["fam"]][j] - S[t][C["fam"]][j])
    ok = ok and all(v == 0 for v in tot)
    ok_all &= ok
    print("CERT", "OK" if ok else "FAIL", os.path.basename(f), C["game"], "fam", C["fam"], "transitions", len(S) - 1, "circuit", len(C["y"]))
sys.exit(0 if ok_all else 1)
