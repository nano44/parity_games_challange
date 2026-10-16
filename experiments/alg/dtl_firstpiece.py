#!/usr/bin/env python3
"""L-ALG (2026-10-15, DTL step 4, Lemma D): how many tangles are learned in the FIRST piece of a search (between the first
and the second "best vertices" line of the search in the release trace, when the first is stable) vs later pieces and
the recursion. Usage: dtl_firstpiece.py OINK game.pg [game.pg ...]  or  dtl_firstpiece.py OINK --random RNGAME N SEED."""
import sys, re, subprocess, random, os, tempfile
oink = sys.argv[1]
def count(path):
    r = subprocess.run([oink, "--dtl", "-t", "--no-single", "--no-wcwc", "--no-loops", path], capture_output=True, text=True, timeout=600)
    out = re.sub(r"\x1b\[[0-9;]*m", "", r.stdout + r.stderr)
    first = later = 0; state = None   # state: None (before 1st best-vertices), "first" (first piece, stable), "later"
    for line in out.splitlines():
        if "iteration" in line and ("-even" in line or "-odd" in line): state = None; continue
        if "best vertices:" in line:
            state = "first" if (state is None and "(stable)" in line) else "later"; continue
        if "new tangle" in line:
            if state == "first": first += 1
            else: later += 1
    return first, later
if sys.argv[2] == "--random":
    rngame, N, seed = sys.argv[3], int(sys.argv[4]), int(sys.argv[5]); rng = random.Random(seed); F = L = 0; d = tempfile.mkdtemp()
    for i in range(N):
        n = rng.randint(6, 16); g = subprocess.run([rngame, str(n), str(rng.randint(2, n)), "1", str(rng.randint(1, 3))], capture_output=True, text=True).stdout
        p = os.path.join(d, "g.pg"); open(p, "w").write(g); f, l = count(p); F += f; L += l
    print(f"random {N} games: first-piece tangles {F}, later/recursion tangles {L}")
else:
    for p in sys.argv[2:]: f, l = count(p); print(f"{os.path.basename(p)}: first-piece {f}, later {l}")
