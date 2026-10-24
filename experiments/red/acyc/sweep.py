"""L-RED box 30 (produced on Opus 5.5): large random sweep for (ACYC) / (YZ) failures (STEP5.md §6.1, GAPS G-S5-6), using L-ALG's
experiments/alg/dtl_yzclimb.fitness UNMODIFIED (Python reference of A_DTL; fitness = (max |Y_0 minus Z_f|, ACYC failures, largest
new part, straddling Dom acceptances)). Order from DTL_ORDER (stable | oink). Random games: n in [NMIN, NMAX], priorities in
0..PMAX(n) (duplicates allowed), owners uniform, out-degree 1-3. Every game with a straddle is counted; any ACYC or YZ failure is
written to OUTDIR. Usage: sweep.py COUNT NMIN NMAX SEED OUTDIR [PRIOFRAC]"""
import os, random, sys, time
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
sys.path.insert(0, os.path.join(R, "experiments", "alg")); sys.path.insert(0, os.path.join(R, "experiments", "harness"))
import pg  # noqa: E402
import dtl_yzclimb as YC  # noqa: E402
cnt, nmin, nmax, seed, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
pf = float(sys.argv[6]) if len(sys.argv) > 6 else 1.0
os.makedirs(out, exist_ok=True); rng = random.Random(seed); t0 = time.time()
stat = {"games": 0, "incomplete": 0, "error": 0, "straddle_games": 0, "straddles": 0, "maxnew": 0, "acyc": 0, "yz": 0}
for i in range(cnt):
    n = rng.randint(nmin, nmax); P = max(1, int(pf * n))
    prio = [rng.randrange(P) for _ in range(n)]; owner = [rng.randrange(2) for _ in range(n)]
    succ = [sorted(set(rng.sample(range(n), rng.choice((1, 2, 2, 3))))) for _ in range(n)]
    g = pg.Game(prio, owner, succ); f = YC.fitness(g); stat["games"] += 1
    if f[0] < 0: stat["error"] += 1; continue
    if f[0] >= 99: stat["incomplete"] += 1; pg.write(g, os.path.join(out, f"incomplete_{seed}_{i}.pg")); continue
    if f[3]: stat["straddle_games"] += 1; stat["straddles"] += f[3]; stat["maxnew"] = max(stat["maxnew"], f[2])
    if f[1]: stat["acyc"] += 1; pg.write(g, os.path.join(out, f"acyc_viol_{seed}_{i}.pg")); print("ACYC FAILS", i, f, flush=True)
    if f[0]: stat["yz"] += 1; pg.write(g, os.path.join(out, f"yz_viol_{seed}_{i}.pg")); print("YZ FAILS", i, f, flush=True)
print(os.environ.get("DTL_ORDER", "stable"), stat, f"{time.time() - t0:.0f}s", flush=True)
