#!/usr/bin/env python3
"""L-RED R215: CANDIDATE N5'-xi (box190/n5v.py @ acdbd28b, unmodified, read-only worktree) vs Oink 8fbf0a7 --zlk on Oink rngame games.
Regions vs Oink's solution file; S5 strategies by harness verify.check. Also any *.pg given on the command line (e.g. climb bests).
Usage: oinkck.py COUNT NMAX SEED  |  oinkck.py --files a.pg b.pg ..."""
import sys, os, subprocess, random, tempfile
WT = os.environ.get("WT", "/tmp/claude-0/-home-user-parity-games-challange/ba7ebe66-d4de-5a49-84c3-f59b4e658f4a/scratchpad/wt190")
sys.path[:0] = [os.path.join(WT, "experiments/new/box190"), os.path.join(WT, "experiments/harness")]
import n5v, pg, verify
OINK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "tools", "oink", "build")
def oink(path):
    sol = path + ".sol"; subprocess.run([os.path.join(OINK, "oink"), "--zlk", path, sol], capture_output=True, check=True)
    win = {}
    for line in open(sol):
        w = line.replace(";", "").split()
        if len(w) >= 2 and w[0] != "paritysol": win[int(w[0])] = int(w[1])
    return win
def one(path, tag):
    g = pg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%"))); ref = oink(path)
    out = []
    for m in ("xi", "spec"):
        st, fb, E = n5v.run(g, m); win, strat = n5v.solution(g, st, E); e = verify.check(g, win, strat)
        ok = all(win[v] == ref[v] for v in range(g.n)) and not e
        out.append((m, len(st) - 1, ok))
    bad = [m for m, _, ok in out if not ok]
    print(f"{tag} n {g.n} | " + " | ".join(f"{m} {it} {'OK' if ok else 'WRONG'}" for m, it, ok in out), flush=True)
    return bad
if sys.argv[1] == "--files":
    nb = sum(1 for p in sys.argv[2:] if one(p, os.path.basename(p))); print(f"FILES {len(sys.argv) - 2} wrong {nb}")
else:
    cnt, nmax, seed = map(int, sys.argv[1:4]); rng = random.Random(seed); nb = 0; mx = 0
    d = tempfile.mkdtemp()
    for i in range(cnt):
        n = rng.randint(2, nmax); p = os.path.join(d, "g.pg")
        txt = subprocess.run([os.path.join(OINK, "rngame"), str(n), str(rng.randint(1, n)), "1", str(rng.randint(1, min(4, n - 1)))], capture_output=True, text=True).stdout
        open(p, "w").write(txt); g = pg.parse("".join(l for l in txt.splitlines(True) if not l.lstrip().startswith("%")))
        ref = oink(p); st, fb, E = n5v.run(g, "xi"); win, strat = n5v.solution(g, st, E); e = verify.check(g, win, strat)
        mx = max(mx, len(st) - 1)
        if not (all(win[v] == ref[v] for v in range(g.n)) and not e): nb += 1; os.replace(p, f"wrong_{seed}_{i}.pg"); print("WRONG", i, n, flush=True)
    print(f"OINK-RANDOM games {cnt} n 2..{nmax} seed {seed}: xi wrong {nb}, max iterations {mx}")
