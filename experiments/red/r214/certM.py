#!/usr/bin/env python3
"""L-RED R214 CERTM: certify a MOVES witness: R197 ladder genome (JSON/text), mover z, claimed moves r. Renumbers gates / betas (as
r212/certL.py), finds a start whose IDEAL run (r187/ideal.py) moves z >= r times, stores it, then runs L-NEW box 150 check.py
(VIOL 0, XSIM 0) and r189/lemck.py (0 violations) on the run from that start, and r214/mvck.py over all starts.
Usage: certM.py in out.json z r"""
import sys, os, json, itertools, subprocess
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(H, "..", "r212"); sys.path[:0] = [R, os.path.join(H, "..", "r187")]
import conv, ideal
p, out, z, r = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
G = conv.read_txt(p) if p.endswith(".txt") else json.load(open(p)); N = G["N"]
assert all(G["lev"][v] == v // 2 for v in range(N)) and all(G["opts"][v][k][0] == (2 * (G["lev"][v] - 1) + k if G["lev"][v] else -1) for v in range(N) for k in range(2)), "not R197"
ids = sorted({o[2] for v in range(N) for o in G["opts"][v]}); rid = {i: q for q, i in enumerate(ids)}
br = [0] * len(ids); bp = [0] * len(ids)
for q, i in enumerate(sorted(ids, key=lambda i: G["br"][i])): br[rid[i]] = q; bp[rid[i]] = G["bp"][i]
G["opts"] = [[[o[0], o[1], rid[o[2]]] for o in G["opts"][v]] for v in range(N)]; G["br"], G["bp"] = br, bp
gs = sorted(x for g in G["gate"] for x in g); gid = {x: q for q, x in enumerate(gs)}; G["gate"] = [[gid[x] for x in g] for g in G["gate"]]
G.pop("xorder", None)
best, arg = -1, None
for u in itertools.product(range(2), repeat=N):
    G["start"] = list(u); S, _ = ideal.traj(G); mz = sum(1 for t in range(1, len(S)) if S[t][z] != S[t - 1][z])
    if mz > best: best, arg = mz, list(u)
G["start"] = arg; json.dump(G, open(out, "w")); S, _ = ideal.traj(G)
tg = any(o[1] == z for v in range(N) for o in G["opts"][v])
b = subprocess.run(["python3", os.path.join(R, "ref", "box150", "check.py"), out], capture_output=True, text=True).stdout.strip().splitlines()[-1]
l = subprocess.run(["python3", "r189/lemck.py", os.path.abspath(out)], capture_output=True, text=True, cwd=os.path.join(H, "..")).stdout.strip()
m = subprocess.run(["python3", os.path.join(H, "mvck.py"), out], capture_output=True, text=True).stdout.strip()
ok = best >= r and " VIOL 0 " in b and " XSIM 0 " in b and "SBAR 0 TAU 0 ESC 0 W 0 AV 0 KEY 0 FB 0" in l and f"L {len(S) - 1} " in l
print(("CERTM OK" if ok else "CERTM FAIL"), os.path.basename(out), "d", max(G["lev"]) + 1, "z", z, "level", G["lev"][z], "Xi-target", int(tg),
      "moves", best, "run T", len(S) - 1, "start", "".join(map(str, arg)), "|", b[:70], "|", l, "|", m.split(": ", 1)[1][:60])
sys.exit(0 if ok else 1)
