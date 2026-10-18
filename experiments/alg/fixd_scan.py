"""L-ALG succ. 9 (box 11, produced on Opus 5.5), (FIX-d) scoping: max searches of A_DTL against n at a FIXED number of
priorities d, on random games (gen.random_game: priorities uniform in 0..d-1, owner Even w.p. 1/2).
A "search" = one Oink iteration (one search() call; run() dtl.cpp 1106-1121); a phase = the searches of one player.
Engines (both order data, L22/L26):
  oink  : pinned Oink `oink --dtl --no-single --no-wcwc --no-loops -v` @ 8fbf0a7 (Oink's own order), verified by Oink;
  pyref : experiments/alg/dtl_pyref.py, --order stable, winners checked against harness Zielonka.
Usage: fixd_scan.py ENGINE D N1,N2,... COUNT SEED [DEG]   (DEG = "lo-hi" out-degree range; default mixes 1-2, 1-3, 2-5)
Prints one row per n: n, games, max searches, max Even phase, max Odd phase, mean searches, max tangles, failures.
FIXD_KEEP=dir writes the argmax game of each n there."""
import sys, os, subprocess, tempfile, statistics
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, gen, zielonka
OINK = os.path.join(HERE, "..", "..", "tools", "oink", "build", "oink")


def run_oink(g):
    with tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False) as f:
        f.write(pg.dumps(g)); path = f.name
    try:
        out = subprocess.run([OINK, "--dtl", "--no-single", "--no-wcwc", "--no-loops", "-v", path],
                             capture_output=True, text=True, timeout=600).stdout
    finally:
        os.unlink(path)
    it = ev = od = tg = None
    for line in out.splitlines():
        if "solved in" in line: it = int(line.split("solved in")[1].split()[0])
        if "even iterations:" in line: ev = int(line.split(":")[-1])
        if "odd iterations:" in line: od = int(line.split(":")[-1])
        if "tangles." in line:
            tg = int(line.split("and")[-1].split()[0]); run_oink.dominions = int(line.split("found")[1].split()[0])
    ok = "solution verified" in out
    return it, ev or 0, od or 0, tg or 0, ok


def run_pyref(g):
    import dtl_pyref as P
    sys.setrecursionlimit(100000)
    W, S, d = P.solve_game(g, False, "stable")
    ref = zielonka.solve(g)
    refW = ref[0] if isinstance(ref, tuple) else ref
    ok = list(W) == list(refW)
    # Even searches = iterations until the first False of search(0); run() increments before each search
    return d.iterations, None, None, d.tangles, ok


def main():
    eng, D, Ns, count, seed = sys.argv[1], int(sys.argv[2]), [int(x) for x in sys.argv[3].split(",")], int(sys.argv[4]), int(sys.argv[5])
    degs = [tuple(map(int, sys.argv[6].split("-")))] if len(sys.argv) > 6 else [(1, 2), (1, 3), (2, 5)]
    keep = os.environ.get("FIXD_KEEP")
    print(f"# engine={eng} d={D} count={count} seed={seed} degs={degs}")
    print("n games maxS maxEven maxOdd meanS maxTangles fails")
    for n in Ns:
        rows = []; fails = 0; best = (-1, None)
        for i in range(count):
            lo, hi = degs[i % len(degs)]
            g = gen.random_game(n, D, lo, hi, seed * 100003 + i)
            if len(set(g.prio)) < D: continue
            it, ev, od, tg, ok = (run_oink if eng == "oink" else run_pyref)(g)
            if not ok or it is None: fails += 1; print("FAIL", n, i, flush=True); continue
            rows.append((it, ev, od, tg))
            if it > best[0]: best = (it, g)
        if not rows: continue
        mx = max(r[0] for r in rows)
        me = max((r[1] for r in rows if r[1] is not None), default="-")
        mo = max((r[2] for r in rows if r[2] is not None), default="-")
        print(n, len(rows), mx, me, mo, round(statistics.mean(r[0] for r in rows), 2), max(r[3] for r in rows), fails, flush=True)
        if keep and best[1] is not None:
            os.makedirs(keep, exist_ok=True); pg.write(best[1], os.path.join(keep, f"fixd_d{D}_n{n}_S{best[0]}.pg"))


if __name__ == "__main__":
    main()
