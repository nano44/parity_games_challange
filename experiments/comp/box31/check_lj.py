#!/usr/bin/env python3
"""L-COMP 12 box 31: rclimb31 LJ score vs ref_lj.py on a seed and K random mutants (python random.Random(SEED); 1-4 edits each; even-numbered mutants over ALL movers, odd-numbered over movers >= 12 only;: re-target, rank swap, parity flip, gate swap within a pair, start flip; cyclic mutants redrawn). Compares the encoded score and
every component (caps, q (C's -1 = none -> 2J-2 as the score uses), npaths, n1, T, F(J)). Env XTONLY=1: re-target edits only. Usage: check_lj.py RCLIMB31 J GATE GUARD seed.txt K SEED OUTDIR"""
import sys, os, random, subprocess, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "l-lower"))
from sim6 import rd, wr, topo
import ref_lj
X, J, gate, gs, seedf, K, sd, od = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], sys.argv[5], int(sys.argv[6]), int(sys.argv[7]), sys.argv[8]
guard = [tuple(map(int, t.split(':'))) for t in gs.split(',') if t]; os.makedirs(od, exist_ok=True); R = random.Random(sd)
def mutate(D, lo=0):
    while True:
        E = {k: (list(v) if isinstance(v, list) else v) for k, v in D.items()}; N = 2 * E['d']
        for _ in range(R.randint(1, 4)):
            r = R.randrange(5) if not os.environ.get('XTONLY') else 0; m = R.randrange(2 * lo, 2 * N)
            if r == 0: y = R.randrange(-1, N); E['xt'][m] = -1 if y == m // 2 else y
            elif r == 1: m2 = R.randrange(2 * N); E['br'][m], E['br'][m2] = E['br'][m2], E['br'][m]
            elif r == 2: E['bp'][m] ^= 1
            elif r == 3:
                l, k = m // 4, m % 2
                if l > 0: a, b = 4 * l + k, 4 * l + 2 + k; E['gate'][a], E['gate'][b] = E['gate'][b], E['gate'][a]
            else: E['start'][m // 2] ^= 1
        if topo(E) is not None: return E
D0 = rd(seedf); files = [seedf] + []
for i in range(K):
    p = os.path.join(od, f"mut{i:02d}.txt"); wr(mutate(D0, 12 if i % 2 else 0), p); files.append(p)
bad = 0
for p in files:
    o = os.path.join(od, "c_" + os.path.basename(p))
    env = dict(os.environ, LJ=str(J), LJGATE=str(gate), LJGUARD=gs, OUT=o); subprocess.run([X, p, "1", "0"], env=env, capture_output=True, check=True)
    t = open(o).read().splitlines()[-1]; sc = int(re.search(r"# score (-?\d+)", t).group(1)); T = int(re.search(r" T (\d+)", t).group(1))
    F = list(map(int, re.search(r" F ([-\d ]+) moves", t).group(1).split()))
    lj = re.search(r"lj_caps (\d+) lj_q (-?\d+) lj_npaths (\d+) lj_n1 (\d+)", t)
    r = ref_lj.ref(rd(p), J, gate, guard)
    if r is None: ok = sc == -10**18; rs = "guard/cyclic"
    else:
        tup, cp, q = r; enc = tup[0] * 10**17 + tup[1] * 10**16 + max(tup[2], -999) * 10**13 + max(tup[3], -999) * 10**10 + min(tup[4], 99999) * 10**4 + min(tup[5], 9999)
        ok = (lj is not None and sc == enc and T == tup[4] and F[J] == tup[5] and int(lj.group(1)) == cp and (int(lj.group(2)) if int(lj.group(2)) >= 0 else 2 * J - 2) == q
              and -int(lj.group(3)) == tup[2] and -int(lj.group(4)) == tup[3]); rs = f"{tup} caps {cp} q {q}"
    bad += not ok; print(f"{os.path.basename(p)} C score {sc} T {T} lj {lj.groups() if lj else None} | ref {rs} | {'OK' if ok else 'MISMATCH'}")
print(f"files {len(files)} mismatches {bad}")
