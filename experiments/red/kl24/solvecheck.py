"""L-RED box 24 (produced on Opus 5.5): bench.py's run_one in-process, with a larger pivot cap (kl2.main has no cap option; its
default cap 10^7 stops HL88_3). kl2.solve (kl2fast's C least fixed point; experiments/n8d-second, read-only) primal + dual R2,
regions vs Oink zlk @ 8fbf0a7 (-w 1), strategies by experiments/harness/verify.py. Prints one CSV row like bench.py.
Usage: solvecheck.py G.pg SEED [CAP]"""
import os, subprocess, sys, tempfile, time
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
for d in ("n8d-second", "harness"):
    sys.path.insert(0, os.path.join(R, "experiments", d))
import kl2fast  # noqa: E402,F401
import kl2  # noqa: E402
import pg  # noqa: E402
import verify  # noqa: E402

path, seed = sys.argv[1], int(sys.argv[2]); cap = int(sys.argv[3]) if len(sys.argv) > 3 else 10 ** 10
g = pg.read(path)
with tempfile.TemporaryDirectory() as td:
    out = os.path.join(td, "sol")
    r = subprocess.run([os.path.join(R, "tools", "oink", "build", "oink"), "--zlk", "-w", "1", path, out], capture_output=True)
    assert r.returncode == 0, "oink zlk failed"
    ref = pg.read_sol(open(out).read(), g.n)
t0 = time.time()
win, strat, pp, pd = kl2.solve(g, "r2", seed, "first", False, cap)
dt = time.time() - t0
status = "MISMATCH" if win != ref else ("BADSTRAT" if verify.check(g, win, strat) else "OK")
print(f"{os.path.basename(path)},{g.n},r2,{seed},{pp},{pd},{dt:.1f},zlk,{status},kl2fast(solve cap {cap})")
