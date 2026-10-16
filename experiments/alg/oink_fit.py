"""Fitness via Oink: run tools/oink/build/oink --SOLVER -v on a game (temp file) and return the work counter Oink prints
(iterations / tangles / lifts / promotions / major iterations), or -1 on failure. ~3-5 ms per call."""
import os, re, subprocess, tempfile, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg
OINK = os.path.join(HERE, "..", "..", "tools", "oink", "build", "oink")
_pat = re.compile(r"solved with (\d+) (iterations|tangles|lifts|promotions|major)|(\d+) (iterations|tangles|lifts|promotions)")


def work(g, solver, raw=True, timeout=60):
    with tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False) as f:
        f.write(pg.dumps(g)); path = f.name
    try:
        cmd = [OINK, f"--{solver}", "-v"] + (["--no-single", "--no-wcwc"] if raw else []) + [path]
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout).stdout + ""
    except subprocess.TimeoutExpired:
        return 10**9
    finally:
        os.unlink(path)
    m = _pat.search(out)
    if not m:
        return -1
    return int(m.group(1) or m.group(3))
