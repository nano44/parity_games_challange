"""L-ALG succ. 9 (box 11, produced on Opus 5.5), class (b1) ONE-PLAYER games (GAP-A-M §27): hill-climb inside the class
"player C owns every vertex with >= 2 successors" (the other player's vertices have out-degree exactly 1), for the longest
phase of the NON-controller q = 1 - C (Lemma CTRL, §27a: the controller's own searches are <= n + 1). Score = (searches of q
under pinned Oink `--dtl --no-single --no-wcwc --no-loops` minus q's dominions, total searches, tangles). Moves keep the class:
retarget an edge, add / delete an edge of a C-vertex, swap an owner when degrees allow, change a priority (0..P-1).
Usage: fixd_oneplayer.py C N P STEPS SEED OUTDIR   (C = 0 Even controls, 1 Odd controls). Writes the best game to OUTDIR.\nONEP_ANY=1 lifts the class restriction (calibration on two-player games)."""
import sys, os, random, subprocess, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg
OINK = os.path.join(HERE, "..", "..", "tools", "oink", "build", "oink")


def run(g):
    with tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False) as f:
        f.write(pg.dumps(g)); path = f.name
    try:
        out = subprocess.run([OINK, "--dtl", "--no-single", "--no-wcwc", "--no-loops", "-v", path], capture_output=True, text=True, timeout=600).stdout
    finally:
        os.unlink(path)
    r = {"ok": "solution verified" in out}
    for line in out.splitlines():
        if "solved in" in line: r["it"] = int(line.split("solved in")[1].split()[0])
        if "even iterations:" in line: r["ev"] = int(line.split(":")[-1])
        if "odd iterations:" in line: r["od"] = int(line.split(":")[-1])
        if "tangles." in line: r["tg"] = int(line.split("and")[-1].split()[0]); r["dom"] = int(line.split("found")[1].split()[0])
    return r


def inclass(g, C):
    if os.environ.get("ONEP_ANY") == "1": return True        # calibration: no class restriction (two-player games)
    return all(len(set(g.succ[v])) == 1 for v in range(g.n) if g.owner[v] != C)


def score(g, C):
    r = run(g); q = 1 - C
    ph = r.get("od" if q == 1 else "ev", 0)
    return (ph, r.get("it", 0), r.get("tg", 0)), r["ok"]


def mutate(g, C, P, rnd):
    prio, owner, succ = list(g.prio), list(g.owner), [list(s) for s in g.succ]
    n = len(prio); v = rnd.randrange(n); k = rnd.randrange(5)
    if k == 0:
        succ[v][rnd.randrange(len(succ[v]))] = rnd.randrange(n)
    elif k == 1 and (owner[v] == C or os.environ.get("ONEP_ANY") == "1"):
        succ[v].append(rnd.randrange(n))
    elif k == 2 and len(succ[v]) > 1:
        succ[v].pop(rnd.randrange(len(succ[v])))
    elif k == 3:
        if os.environ.get("ONEP_ANY") == "1": owner[v] ^= 1
        elif owner[v] == C and len(set(succ[v])) == 1: owner[v] = 1 - C
        elif owner[v] != C: owner[v] = C
    else:
        prio[v] = rnd.randrange(P)
    succ = [sorted(set(s)) for s in succ]
    h = pg.Game(prio, owner, succ)
    return h if inclass(h, C) else None


def start(C, N, P, rnd):
    prio = [rnd.randrange(P) for _ in range(N)]; owner = [C if rnd.random() < 0.5 else 1 - C for _ in range(N)]
    succ = [sorted(set(rnd.sample(range(N), rnd.randint(1, 3)))) if owner[v] == C else [rnd.randrange(N)] for v in range(N)]
    return pg.Game(prio, owner, succ)


def main():
    C, N, P, steps, seed = (int(x) for x in sys.argv[1:6]); out = sys.argv[6]
    rnd = random.Random(seed); g = start(C, N, P, rnd); best, ok = score(g, C)
    print(f"# C={C} n={N} P={P} steps={steps} seed={seed} start={best}", flush=True)
    for s in range(steps):
        h = mutate(g, C, P, rnd)
        if h is None: continue
        sc, ok = score(h, C)
        if not ok:
            print("FAIL (not verified)", s, flush=True); os.makedirs(out, exist_ok=True)
            pg.write(h, os.path.join(out, f"onep_FAIL_C{C}_n{N}_s{seed}_{s}.pg")); continue
        if sc >= best:
            if sc > best: print(s, sc, flush=True)
            best, g = sc, h
    os.makedirs(out, exist_ok=True); pg.write(g, os.path.join(out, f"onep_C{C}_n{N}_P{P}_s{seed}.pg")); print("best", best)


if __name__ == "__main__":
    main()
