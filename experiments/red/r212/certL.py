#!/usr/bin/env python3
"""L-RED R212 CERTL: certify a ladder witness of L^R_d (fk/fl text or JSON) for T: R197 convention, ISO flag, r187/ideal.py max over all
starts (= T), the argmax start stored; L-NEW box 150 checker (VIOL 0, XSIM 0) and r189/lemck.py (0 violations) at that start.
Writes the certified JSON (gates / betas renumbered 0..M-1). Usage: certL.py in out.json T"""
import sys, os, json, itertools, subprocess
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r187")]
import conv, ideal
p, out, T = sys.argv[1], sys.argv[2], int(sys.argv[3])
G = conv.read_txt(p) if p.endswith(".txt") else json.load(open(p)); N = G["N"]
assert all(G["lev"][v] == v // 2 for v in range(N)) and all(G["opts"][v][k][0] == (2 * (G["lev"][v] - 1) + k if G["lev"][v] else -1) for v in range(N) for k in range(2)), "not R197"
ids = sorted({o[2] for v in range(N) for o in G["opts"][v]}); rid = {i: r for r, i in enumerate(ids)}
br = [0] * len(ids); bp = [0] * len(ids)
for r, i in enumerate(sorted(ids, key=lambda i: G["br"][i])): br[rid[i]] = r; bp[rid[i]] = G["bp"][i]
G["opts"] = [[[o[0], o[1], rid[o[2]]] for o in G["opts"][v]] for v in range(N)]; G["br"], G["bp"] = br, bp
gs = sorted(x for g in G["gate"] for x in g); gid = {x: r for r, x in enumerate(gs)}; G["gate"] = [[gid[x] for x in g] for g in G["gate"]]
G.pop("xorder", None)
best, arg = -1, None
for u in itertools.product(range(2), repeat=N):
    G["start"] = list(u); S, _ = ideal.traj(G)
    if len(S) - 1 > best: best, arg = len(S) - 1, list(u)
G["start"] = arg; json.dump(G, open(out, "w"))
iso = all(o[1] not in (0, 1) for v in range(N) for o in G["opts"][v])
b = subprocess.run(["python3", os.path.join(H, "ref", "box150", "check.py"), out], capture_output=True, text=True).stdout.strip().splitlines()[-1]
l = subprocess.run(["python3", "r189/lemck.py", os.path.abspath(out)], capture_output=True, text=True, cwd=os.path.join(H, "..")).stdout.strip()
ok = best == T and " VIOL 0 " in b and "SBAR 0 TAU 0 ESC 0 W 0 AV 0 KEY 0 FB 0" in l and f"L {T} " in l
print(("CERTL OK" if ok else "CERTL FAIL"), os.path.basename(out), "d", max(G["lev"]) + 1, "T", best, "ISO", int(iso), "start", "".join(map(str, arg)), "|", b[:60], "|", l)
sys.exit(0 if ok else 1)
