#!/usr/bin/env python3
"""L-COMP 12 box 31: rclimb31 LJNOREAD term vs guard_l6.upstream: nr = |{0..3} ∩ upstream(D, [12])| and score = LJ score - nr*1e18.
Genomes: the given files + K re-target-only mutants of the first (movers 0-3 and 12 options, so nr varies). Usage: check_nr.py RCLIMB K SEED FILES..."""
import sys, os, random, subprocess, re
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(H, "l-lower")); sys.path.insert(0, H)
from sim6 import rd, wr, topo
from guard_l6 import upstream
import ref_lj
X, K, R = sys.argv[1], int(sys.argv[2]), random.Random(int(sys.argv[3])); files = sys.argv[4:]; od = os.path.join(H, "mut_check_nr"); os.makedirs(od, exist_ok=True)
D0 = rd(files[0]); N = 2 * D0['d']
for i in range(K):
    while True:
        E = {k: (list(v) if isinstance(v, list) else v) for k, v in D0.items()}
        for _ in range(R.randint(1, 3)):
            m = R.choice([0, 1, 2, 3, 4, 5, 6, 7, 24, 25]); y = R.randrange(-1, N); E['xt'][m] = -1 if y == m // 2 else y
        if topo(E) is not None: break
    p = os.path.join(od, f"nr{i:02d}.txt"); wr(E, p); files.append(p)
bad = 0; env = dict(os.environ, LJ="7", LJGATE="190", LJGUARD="20:17,34:22", LJNOREAD="12:0,1,2,3")
for p in files:
    o = os.path.join(od, "c_" + os.path.basename(p)); subprocess.run([X, p, "1", "0"], env=dict(env, OUT=o), capture_output=True, check=True)
    t = open(o).read().splitlines()[-1]; sc = int(re.search(r"# score (-?\d+)", t).group(1)); nr = int(re.search(r"lj_nr (\d+)", t).group(1))
    D = rd(p); rnr = len({0, 1, 2, 3} & upstream(D, [12])); r = ref_lj.ref(D, 7, 190, [(20, 17), (34, 22)])
    if r is None: ok = nr == rnr; enc = None
    else:
        tup = r[0]; enc = tup[0] * 10**17 + tup[1] * 10**16 + max(tup[2], -999) * 10**13 + max(tup[3], -999) * 10**10 + min(tup[4], 99999) * 10**4 + min(tup[5], 9999) - rnr * 10**18
        ok = nr == rnr and sc == enc
    bad += not ok; print(f"{os.path.basename(p)} C nr {nr} score {sc} | ref nr {rnr} score {enc} | {'OK' if ok else 'MISMATCH'}")
print(f"files {len(files)} mismatches {bad}")
