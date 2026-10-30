import sys, random, os, subprocess, copy
sys.path.insert(0, "/home/user/parity_games_challange/experiments/red/tree")
import gb, tiedlib
seed = int(sys.argv[1]); T = float(sys.argv[2]); rnd = random.Random(seed)
K, m = int(sys.argv[3]), int(sys.argv[4])
d = f"/tmp/claude-0/r131/base_{K}_{m}"
if not os.path.exists(d + ".pg"):
    subprocess.run(["python3", "/home/user/parity_games_challange/experiments/red/span/mkrw.py", str(K), str(m), d + ".pg", d + ".start"], env=dict(os.environ, LATE="1"), capture_output=True)
B = gb.from_pg(d + ".pg", d + ".start")
anchors = [x for x in B.names if x in ("h", "hp", "z", "M", "EQ", "EQp") or x[0] in "rcvdabCuw" ]
prios = sorted(set(B.pr.values())); top = max(prios)
import time; t0 = time.time(); cnt = 0; bestrb = 0
while time.time() - t0 < T:
    G = copy.deepcopy(B)
    ng = rnd.randint(2, 5); new = [f"g{i}" for i in range(ng)]
    for i, x in enumerate(new):
        own = rnd.randint(0, 1); p = rnd.choice(prios) + rnd.choice([-1, 0, 1]) if rnd.random() < 0.8 else rnd.randint(1, top + 3)
        pool = anchors + new[:i] + new[i + 1:]
        G.v(x, own, max(0, p), rnd.sample(pool, rnd.randint(1, 3)))
        if rnd.random() < 0.7: G.start(x, rnd.choice(G.sc[x]))
    # wire one existing Even vertex? keep base intact; y = g0 must be Even with >=2 succs
    G.own["g0"] = 0
    if len(G.sc["g0"]) < 2: G.sc["g0"].append(rnd.choice(new[1:]))
    g, st = G.game()
    try: c, reps = tiedlib.stats(g, st, cap=400)
    except Exception as e: continue
    cnt += 1
    mid = [r for r in reps if r["reblk"] and not r["tied"] and r["u"] < c["it"] - 3]
    if len(mid) > 0 or c["untied_reblk"] > 1:
        bestrb = max(bestrb, c['reblk'])
        print(seed, cnt, c, [(x, G.own[x], G.pr[x], G.sc[x], G.st.get(x)) for x in new], [(G.names[r['y']], G.names[r['z']], r['u'], r['k'], r['reblk'], r['tied']) for r in reps if r['y'] >= len(B.names) or r['z'] >= len(B.names)][:6], flush=True)
        if True:
            import pickle; pickle.dump(G, open(f"/tmp/claude-0/r131/hit_{seed}_{cnt}.pkl", "wb"))
print("done", seed, cnt, flush=True)
