"""L-RED box 20 (produced on Opus 5.5): fast two-player climb for long DTL phases at fixed n (no class restriction).
Fitness (pinned Oink 8fbf0a7, `--dtl --no-single --no-wcwc --no-loops -v`, oink order): F = max(even iterations, odd iterations)
- dominions found, a lower-bound proxy for the longest phase S (a player's searches split into at most dominions+1 phases);
'verified' is required. Moves: add / remove an edge (out-degree stays >= 1), change a priority in 0..2n-1, flip an owner.
Accept >=. Writes OUT/best.pg on every strict gain and prints 'step F even odd dom'. The final S is measured separately with
smeasure.py (L-ALG's phase convention, both orders). Usage: oclimb.py START.pg STEPS SEED OUT [--n N (neutral pad)] [--secs T (wall-clock limit)]"""
import sys, os, random, subprocess, re, tempfile, time
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
OINK = os.path.join(R, "tools", "oink", "build", "oink")


def read(f):
    pr, ow, su = [], [], []
    for line in open(f):
        t = line.strip().rstrip(";").split()
        if not t or t[0] == "parity": continue
        pr.append(int(t[1])); ow.append(int(t[2])); su.append(sorted({int(x) for x in t[3].split(",")}))
    return pr, ow, su


def dumps(g):
    pr, ow, su = g
    return f"parity {len(pr) - 1};\n" + "".join(f"{v} {pr[v]} {ow[v]} {','.join(map(str, su[v]))};\n" for v in range(len(pr)))


def fit(g, tmp):
    open(tmp, "w").write(dumps(g))
    try:
        out = subprocess.run([OINK, "--dtl", "--no-single", "--no-wcwc", "--no-loops", "-v", tmp], capture_output=True, text=True, timeout=60).stdout
    except subprocess.TimeoutExpired:
        return None
    if "verified" not in out: return None
    ev = int(re.search(r"even iterations: (\d+)", out).group(1)); od = int(re.search(r"odd iterations: (\d+)", out).group(1))
    dm = int(re.search(r"found (\d+) dominions", out).group(1))
    return (max(ev, od) - dm, ev, od, dm)


def mutate(g, rnd):
    pr, ow, su = list(g[0]), list(g[1]), [list(s) for s in g[2]]; n = len(pr); k = rnd.random(); v = rnd.randrange(n)
    if k < 0.35:
        w = rnd.randrange(n)
        if w in su[v]: return None
        su[v] = sorted(su[v] + [w])
    elif k < 0.6:
        if len(su[v]) < 2: return None
        su[v].remove(rnd.choice(su[v]))
    elif k < 0.9: pr[v] = rnd.randrange(2 * n)
    else: ow[v] = 1 - ow[v]
    return pr, ow, su


if __name__ == "__main__":
    start, steps, seed, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    rnd = random.Random(seed); os.makedirs(out, exist_ok=True); tmp = os.path.join(out, "cur.pg")
    g = read(start); N = int(sys.argv[sys.argv.index("--n") + 1]) if "--n" in sys.argv else len(g[0])
    n0 = len(g[0])
    while len(g[0]) < N:          # NEUTRAL pad (from 08:12Z): priority 0, random owner, one successor into the original game, no edge
        # into it, so it is attracted with its successor and cannot form a tangle or dominion; the climb then uses it as material.
        # (Before 08:12Z the pad gave random priorities and an incoming edge; those padded seeds collapsed to F <= 8.)
        g[0].append(0); g[1].append(rnd.randint(0, 1)); g[2].append([rnd.randrange(n0)])
    best = fit(g, tmp); print("start", best, flush=True); open(os.path.join(out, "best.pg"), "w").write(dumps(g))
    secs = float(sys.argv[sys.argv.index("--secs") + 1]) if "--secs" in sys.argv else 1e18; t0 = time.time()
    for it in range(steps):
        if time.time() - t0 > secs: print("time limit at step", it, flush=True); break
        h = mutate(g, rnd)
        if h is None: continue
        f = fit(h, tmp)
        if f is None or f[0] < best[0]: continue
        if f[0] > best[0]:
            print(it, *f, flush=True); open(os.path.join(out, "best.pg"), "w").write(dumps(h))
        g, best = h, f
        if it % 2000 == 0: print("hb", it, best, flush=True)
    print("final", best, flush=True)
