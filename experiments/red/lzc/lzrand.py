import sys, random, time
sys.argv.append("--lzc")
sys.path.insert(0, "/home/user/parity_games_challange/experiments/new/box21"); sys.path.insert(0, __import__("os").environ.get("LNEW", "/tmp/claude-0/lnew") + "/experiments/new/box72")
import n5x, n5lz, pg
seed = int(sys.argv[1]); T = float(sys.argv[2]); N = int(sys.argv[3]); rnd = random.Random(seed)
best = 0; bestN = 10**9; t0 = time.time(); cnt = 0; worse = 0; better = 0; err = 0
orig = n5x.step
while time.time() - t0 < T:
    n = rnd.randint(4, N)
    pr = rnd.sample(range(0, 3 * n), n); own = [rnd.randint(0, 1) for _ in range(n)]
    succ = [sorted(set(rnd.sample(range(n), rnd.randint(1, min(3, n))))) for _ in range(n)]
    g = pg.Game(pr, own, succ)
    st = ({v: rnd.choice(succ[v]) for v in range(n) if own[v] == 0}, {v: rnd.choice(succ[v]) for v in range(n) if own[v] == 1}) if rnd.random() < 0.5 else None
    try:
        n5x.step = orig; a, _ = n5x.trace(g, st, check=False)
        n5lz._wc.clear(); n5x.step = n5lz.step; b, _ = n5x.trace(g, st, check=False)
    except Exception as e: err += 1; continue
    cnt += 1; d = (len(b) - 1) - (len(a) - 1)
    worse += d > 0; better += d < 0
    if d > best or (d == best and d > 0 and len(a) - 1 < bestN): best = d; bestN = len(a) - 1; print(seed, cnt, "N5", len(a) - 1, "LZC", len(b) - 1, pr, own, succ, st, flush=True)
print("done", seed, cnt, "LZC slower", worse, "faster", better, "errors", err, flush=True)
