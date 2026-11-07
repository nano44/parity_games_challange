#!/usr/bin/env python3
"""L-RED R215 (adversary vs CANDIDATE N5'-xi, L-NEW box 190 @ acdbd28b): hill-climb on N5'-xi iterations.
Object under test: box190/n5v.py run(g, "xi") imported UNMODIFIED from a read-only worktree of acdbd28b (env WT, default scratch wt190).
Modes:  game  : random parity games, n vertices, out-degree 1..3, priorities 0..n; mutation = rewire an edge / change a priority / owner.
        cyc   : R104 Gamma3(G) (box189/gamma3.py, pads K,pe,pb,m) of 2-wide degree-2 ladder genomes WITH Xi-cycles allowed (outside REALIZE).
Score = xi iterations (ties: + spec iterations / 1000). Every new best is checked: regions vs harness zielonka + harness verify.check of
S5's strategies (both modes); a wrong answer is printed as WRONG with the instance file. Usage: xiclimb.py mode n_or_d seed iters outprefix"""
import sys, os, json, random, copy
WT = os.environ.get("WT", "/tmp/claude-0/-home-user-parity-games-challange/ba7ebe66-d4de-5a49-84c3-f59b4e658f4a/scratchpad/wt190")
sys.path[:0] = [os.path.join(WT, "experiments/new/box190"), os.path.join(WT, "experiments/new/box189"), os.path.join(WT, "experiments/harness")]
import n5v, pg, zielonka, verify
mode, P, seed, iters, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
rng = random.Random(seed)
def run(g, m):
    st, fb, E = n5v.run(g, m, cap=5000); return len(st) - 1, st, E
def check(g, st, E):
    win, strat = n5v.solution(g, st, E); ref = zielonka.solve(g); e = verify.check(g, win, strat)
    return win == ref and not e
# ---- game mode
def rgame():
    n = P; prio = [rng.randrange(n + 1) for _ in range(n)]; own = [rng.randrange(2) for _ in range(n)]
    succ = [sorted(rng.sample(range(n), rng.randint(1, min(3, n)))) for _ in range(n)]
    return dict(prio=prio, own=own, succ=succ)
def mg(s):
    s = copy.deepcopy(s); n = P; r = rng.random(); v = rng.randrange(n)
    if r < 0.5:
        k = rng.randint(1, min(3, n)); s["succ"][v] = sorted(rng.sample(range(n), k))
    elif r < 0.85: s["prio"][v] = rng.randrange(n + 1)
    else: s["own"][v] ^= 1
    return s
def tog(s): return pg.Game(list(s["prio"]), list(s["own"]), [list(x) for x in s["succ"]])
# ---- cyc mode (genome in box150 JSON form; Xi-targets any mover != self or -1, cycles allowed)
def rgen():
    d = P; N = 2 * d; M = 2 * N; lev = [v // 2 for v in range(N)]
    opts = [[[2 * (lev[v] - 1) + k if lev[v] else -1, rng.choice([w for w in range(-1, N) if w != v]), 2 * v + k] for k in range(2)] for v in range(N)]
    br = list(range(M)); rng.shuffle(br); bp = [rng.randrange(2) for _ in range(M)]
    gt = list(range(M)); rng.shuffle(gt); gate = [[gt[2 * v], gt[2 * v + 1]] for v in range(N)]
    return dict(N=N, lev=lev, opts=opts, gate=gate, br=br, bp=bp, start=[rng.randrange(2) for _ in range(N)])
def mgen(G):
    G = copy.deepcopy(G); N = G["N"]; M = 2 * N; r = rng.random(); v = rng.randrange(N); k = rng.randrange(2)
    if r < 0.35: G["opts"][v][k][1] = rng.choice([w for w in range(-1, N) if w != v])
    elif r < 0.6: i, j = rng.randrange(M), rng.randrange(M); G["br"][i], G["br"][j] = G["br"][j], G["br"][i]
    elif r < 0.7: G["bp"][rng.randrange(M)] ^= 1
    elif r < 0.9: a, c, ka, kc = rng.randrange(N), rng.randrange(N), rng.randrange(2), rng.randrange(2); G["gate"][a][ka], G["gate"][c][kc] = G["gate"][c][kc], G["gate"][a][ka]
    else: G["start"][v] ^= 1
    return G
if mode == "cyc":
    import gamma3
    def toG(G): return gamma3.build(G, {"K", "pe", "pb", "m"})[0]
    new, mut = rgen, mgen
else:
    toG, new, mut = tog, rgame, mg
def score(s):
    g = toG(s); a, st, E = run(g, "xi"); b, _, _ = run(g, "spec"); return a + b / 1000.0, a, b, g, st, E
cur = new(); cs = score(cur); best = cs[0]
for it in range(iters):
    c = mut(cur)
    try: sc = score(c)
    except Exception as ex: continue
    if sc[0] >= cs[0]:
        cur, cs = c, sc
        if sc[0] > best:
            best = sc[0]; ok = check(sc[3], sc[4], sc[5]); json.dump(cur, open(out + ".json", "w")); pg.write(sc[3], out + ".pg")
            print(f"it {it} n {sc[3].n} xi {sc[1]} spec {sc[2]} {'OK' if ok else 'WRONG'}", flush=True)
            if not ok: json.dump(cur, open(out + f"_WRONG_{it}.json", "w")); pg.write(sc[3], out + f"_WRONG_{it}.pg")
print(f"FINAL best xi {int(best)}", flush=True)
