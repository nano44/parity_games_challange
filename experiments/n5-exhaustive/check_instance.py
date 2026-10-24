#!/usr/bin/env python3
"""Check and save reported instances (box 3 item 3). For each record of an exh.py JSON list (or a .pg [+ .start]):
  - n5x.trace(check=True): states of n5.py's loop, counts asserted equal to n5.run;
  - n5b.py SPEC mode (L-COMP's independent implementation): the full (sigma, tau) state sequence must equal n5x's;
  - n5.py's solution: regions == Oink zlk @ 8fbf0a7 and strategies pass experiments/harness/verify.py;
  - saves instances/<name>.pg (+ .start) and prints sha1, iterations, longest phase, trust, re-entries.
Usage: check_instance.py JSON KEY NAMEPREFIX [MAX]   |   check_instance.py --pg FILE.pg [FILE.start]"""
import hashlib
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(ROOT, "experiments", "n5-second"))
sys.path.insert(0, os.path.join(ROOT, "experiments", "harness"))
import exh  # noqa: E402
from exh import pg, trace  # noqa: E402
import n5  # noqa: E402
import n5b  # noqa: E402
import verify  # noqa: E402

OINK = os.path.join(ROOT, "tools", "oink", "build", "oink")
INST = os.path.join(HERE, "instances")


def zlk(path, n):
    with tempfile.TemporaryDirectory() as td:
        out = os.path.join(td, "s")
        r = subprocess.run([OINK, "--zlk", "-w", "1", path, out], capture_output=True)
        if r.returncode != 0:
            r = subprocess.run([OINK, "--tl", "-w", "1", path, out], capture_output=True)
            tag = "tl (zlk aborted)"
        else:
            tag = "zlk"
        return pg.read_sol(open(out).read(), n), tag


def check(g, start, name):
    os.makedirs(INST, exist_ok=True)
    path = os.path.join(INST, name + ".pg")
    pg.write(g, path)
    if start:
        with open(os.path.join(INST, name + ".start"), "w") as f:
            f.write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in sorted(start[0].items())) + "\n")
            f.write("TAU0 " + " ".join(f"{v}:{w}" for v, w in sorted(start[1].items())) + "\n")
    sha = hashlib.sha1(open(path, "rb").read()).hexdigest()
    st, fb = trace(g, start, check=True)                         # asserts n5.run (iterations, fallback)
    sig = tau = None
    if start:
        sig = [start[0].get(v, -1) for v in range(g.n)]; tau = [start[1].get(v, -1) for v in range(g.n)]
    L = []
    nb = n5b.N5(g, mode="spec")
    _, _, itb, fbb = nb.run(sig, tau, trace=L)
    ev = lambda s, own: tuple(s[v] for v in range(g.n) if g.owner[v] == own)
    same = len(L) == len(st) and all(ev(a[0], 0) == ev(b[0], 0) and ev(a[1], 1) == ev(b[1], 1) for a, b in zip(L, st))
    it, fb5, win, ws, _ = n5.run(g, "n5", start)
    ref, rtag = zlk(path, g.n)
    errs = verify.check(g, win, ws)
    o = exh.odd_choice(g)
    maxph, trust, tlen, reA, reB = exh.analyse(g, st, o) if len(st) > 1 else (0, 0, 0, 0, 0)
    ok = same and (itb, fbb) == (it, fb5) and win == ref and not errs
    print(f"{name} sha1 {sha[:12]} n {g.n} it {it} fb {fb5} maxph {maxph} trust {trust} reA {reA} reB {reB} | "
          f"n5b states equal {same} ({itb},{fbb}) | regions = oink {rtag}: {win == ref} | verify: {'OK' if not errs else errs[:2]} "
          f"| {'OK' if ok else 'FAIL'}")
    return ok, sha


def main():
    a = sys.argv[1:]
    if a[0] == "--pg":
        g = pg.read(a[1]); st = exh.readstart(a[2]) if len(a) > 2 else None
        check(g, st, os.path.splitext(os.path.basename(a[1]))[0])
        return
    d = json.load(open(a[0])); recs = d[a[1]][:int(a[3])] if len(a) > 3 else d[a[1]]
    bad = 0
    for i, r in enumerate(recs):
        start = None
        if r.get("start"):
            s = r["start"]
            if isinstance(s, str):
                s = eval(s)                                      # json default=str for tuples of dicts
            start = ({int(k): v for k, v in s[0].items()}, {int(k): v for k, v in s[1].items()})
        g = pg.Game(r["prio"], r["owner"], r["succ"])
        ok, _ = check(g, start, f"{a[2]}_{i}")
        bad += not ok
    print(f"checked {len(recs)}, failures {bad}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
