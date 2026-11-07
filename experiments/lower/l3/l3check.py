#!/usr/bin/env python3
"""L-LOWER box L3 fast regression (run by experiments/lower/check.sh; < 1 min).
1. Family A (genA.py): T = 2d, moves(2l+1) = 2*floor(2l/3)+1 (l >= 1), every other mover 1, for d = 3..20 (CONJECTURE A-RUN data).
2. Own simulator sim.py == L-NEW box150 Gen (trunk experiments/new/box150/check.py) state for state: family A d 3..8 (every start
   for d <= 4) and inst/dense_d5_l3_H10.json (byte copy of L-RED claude/l-red experiments/red/r214/out/dense_d5_l3_H10.json, 36d340c7;
   every start).
3. tricheck (TRI, TRI-MU, FEEDBACK) on 60 random L^R_d genomes (seed 11, every start for N <= 8) and family A: 0 violations."""
import os, sys, json, itertools, subprocess
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
from sim import run, moves
from genA import genA
for d in range(3, 21):
    A = genA(d); S = run(A, A["start"]); m = moves(S, A["N"])
    assert len(S) - 1 == 2 * d and all(m[2 * l + 1] == 2 * ((2 * l) // 3) + 1 for l in range(1, d)) \
        and all(m[2 * l] == 1 for l in range(d)) and m[1] == 1, d
print("family A: T = 2d and moves(2l+1) = 2*floor(2l/3)+1 for d = 3..20")
P0 = os.path.join(H, "..", "..", "new", "box150", "check.py")
ns = {"__file__": os.path.abspath(P0), "__name__": "lib"}; exec(open(P0).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
runs = 0
gs = [genA(d) for d in range(3, 9)] + [json.load(open(os.path.join(H, "inst", "dense_d5_l3_H10.json")))]
for G in gs:
    N = G["N"]; sts = itertools.product([0, 1], repeat=N) if N <= 10 else [G["start"]]
    for st in sts:
        st = list(st); a = [tuple(s) for s in run(G, st)]; b = [tuple(s) for s in Gen(G).run(st)[0]]
        assert a == b, (N, st); runs += 1
print("sim.py == box150 Gen on", runs, "runs")
fa = []
for d in range(3, 9):
    p = os.path.join(H, "out", f"genA_d{d}.json")
    if not os.path.exists(p): json.dump(genA(d), open(p, "w"))
    fa.append(p)
out = subprocess.run([sys.executable, "-I", os.path.join(H, "tricheck.py"), "11", "60"] + fa, capture_output=True, text=True,
                     env=dict(os.environ, ALLN="8")).stdout
line = [l for l in out.splitlines() if l.startswith("TRICHECK")][-1]; print(line)
V = eval(line.split("violations ")[1].split(" info")[0]); assert all(v == 0 for v in V.values()), V
# DEAD MOVES-2D instances (docs/lower/L3-families.md §9): sha1 pins, moves of the named Xi-target mover, agreement with box150 Gen
import hashlib
KILLS = [("kill/KILL_M2D_d6_mu13.json", "5301c716f68f219bda2806f29b317c94e0ed5df0", 8, 13, 13),
         ("kill/KILL_M2D_d8_mu21.json", "d96c2b3657e79c410b180580d829366cbecc9ea4", 15, 21, 24),
         ("kill/REC_d7_mu17.json", "62917c189113bee004d02ada48803f235143a9eb", 8, 17, 17),
         ("kill/REC_d8_mu24.json", "18d26cec2651290dfd9d137712bdadbb36d6f3d8", 8, 24, 25),
         ("kill/REC_d9_mu29.json", "2d034e7fcc3a9261e2fbdcaf5eae9dd5f38a2313", 15, 29, 31),
         ("kill/REC_d10_mu32.json", "b114f4cdefaf1da6818e15512bc1fdb19c249e59", 15, 32, 33),
         ("kill/REC_d10_tower_mu30.json", "cc94dc9c46ef63f7a3a54b536d9d3b38fdee5255", 8, 30, 35),
         ("kill/REC_d11_mu40.json", "bbdb33d963d198c439aec63c8c75b0f080043510", 15, 40, 44),
         ("kill/REC_d12_mu42.json", "28e62d513b697ab3083da6310af631c14e1fc830", 15, 42, 48)]
for f, sh, z, mz, T in KILLS:
    p = os.path.join(H, f); assert hashlib.sha1(open(p, "rb").read()).hexdigest() == sh, f
    G = json.load(open(p)); S = run(G, G["start"]); m = moves(S, G["N"])
    Zs = {o[1] for x in range(G["N"]) for o in G["opts"][x]} - {-1}
    assert z in Zs and G["lev"][z] >= 1 and m[z] == mz and len(S) - 1 == T and m[z] > 2 * (G["N"] // 2), f
    assert [tuple(s) for s in S] == [tuple(s) for s in Gen(G).run(G["start"])[0]], f
    print(f"DEAD MOVES-2D: {f}: d {G['N'] // 2}, mover {z} (level {G['lev'][z]}, Xi-target) moves {mz} > 2d, T {T}; box150 Gen agrees")
# T record (not a mu kill): kill/RECT_d11_T59.json
p = os.path.join(H, "kill", "RECT_d11_T59.json"); assert hashlib.sha1(open(p, "rb").read()).hexdigest() == "57b6dc80810bd4b7e072186e4e97c23753f72afd"
G = json.load(open(p)); S = run(G, G["start"]); assert len(S) - 1 == 59 and [tuple(s) for s in S] == [tuple(s) for s in Gen(G).run(G["start"])[0]]
print("T record: kill/RECT_d11_T59.json: d 11, T 59; box150 Gen agrees")
p = os.path.join(H, "kill", "RECT_d13_T66.json"); assert hashlib.sha1(open(p, "rb").read()).hexdigest() == "4eb7e76d734503a0e7a5b70c1ac58cd0b610daa8"
G = json.load(open(p)); S = run(G, G["start"]); assert len(S) - 1 == 66 and [tuple(s) for s in S] == [tuple(s) for s in Gen(G).run(G["start"])[0]]
print("T record: kill/RECT_d13_T66.json: d 13, T 66; box150 Gen agrees")
for f, sh, TT in (("RECT_d13_T99.json", "8946c0ff80d45d766726c645f53f546e1420824d", 99), ("RECT_d14_F46.json", "d3c9b701c59f16f25e300f5b9d690a734527561c", 65),
                  ("RECT_d14_T107.json", "48bffdb3e54510762e1c376f1ef1ff2d25d4b19e", 107), ("RECT_d15_T114.json", "5b5d8bc6c687b55975cce097cc7833af7c4e2797", 114)):
    p = os.path.join(H, "kill", f); assert hashlib.sha1(open(p, "rb").read()).hexdigest() == sh, f
    G = json.load(open(p)); S = run(G, G["start"]); assert len(S) - 1 == TT and [tuple(s) for s in S] == [tuple(s) for s in Gen(G).run(G["start"])[0]], f
    print(f"T record: kill/{f}: d {G['N'] // 2}, T {TT}; box150 Gen agrees")
print("L3 CHECK PASS")
