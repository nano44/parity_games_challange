"""L-RED successor 32 (R134): random second observer obsB + reader R -> {obs, obsB}; REP of R (tiedlib). Usage: obsread.py SEED SECS WO.pg WO.start"""
import sys, random, time, copy
sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__import__("os").path.abspath(__file__)), "..", "tree")); import gb, tiedlib
seed, T = int(sys.argv[1]), float(sys.argv[2]); rnd = random.Random(seed)
B = gb.from_pg(sys.argv[3], sys.argv[4])   # WO = mix/obs2.py (OWNER=0 ABOVE=a) of span/mkrw.py 4 16; m = 16
best = (0, 0); t0 = time.time(); tr = 0
while time.time() - t0 < T:
    tr += 1; G = copy.deepcopy(B)
    mode = rnd.choice(["rev", "shift", "rand", "sub"])
    js = list(range(1, m + 1))
    if mode == "rev": qs = {j: 294 + 2 * (m - j) for j in js}
    elif mode == "shift": k = rnd.randint(1, m - 1); qs = {j: 294 + 2 * ((j + k) % m) for j in js}
    elif mode == "rand": perm = rnd.sample(range(m), m); qs = {j: 294 + 2 * perm[j - 1] for j in js}
    else: js = sorted(rnd.sample(js, rnd.randint(2, m))); qs = {j: 294 + 2 * j for j in js}
    par = rnd.choice([0, 1])
    for j in js: G.v(f"yB{j}", 1, qs[j] + par, [f"r{j}"])
    G.v("obsB", rnd.choice([0, 1]), rnd.randint(0, 3), [f"yB{j}" for j in js])
    G.v("R", 0, rnd.randint(0, 300), ["obs", "obsB"]); G.start("R", rnd.choice(["obs", "obsB"]))
    g, st = G.game()
    try: c, reps = tiedlib.stats(g, st, cap=2000)
    except Exception: continue
    rR = sum(1 for r in reps if G.names[r["y"]] == "R")
    if c["runs"] == 1 and (rR, c["it"]) > best:
        best = (rR, c["it"]); print(tr, mode, par, G.own["obsB"], G.pr["obsB"], G.pr["R"], G.st["R"], js if mode == "sub" else qs, "REP(R)", rR, c, flush=True)
print("done", tr)
