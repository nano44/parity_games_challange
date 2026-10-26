#!/usr/bin/env python3
"""Box 12 pin gate (every game class, not only C^1O; check_instance.py's analyse assumes one Odd choice vertex).
For FILE.pg [+ FILE.start]: (1) exh.trace(check=True): n5.py's state sequence, counts asserted equal to n5.run; (2) n5b SPEC
(L-COMP's implementation) state sequence equal to it; (3) n5.py's regions = Oink zlk @ 8fbf0a7 (--tl where zlk aborts) and its
strategies pass experiments/harness/verify.py; (4) copy to instances/NAME.pg (+ .start) and print sha1 and the census line.
Usage: pin.py FILE.pg [FILE.start] NAME"""
import hashlib
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "n5-exhaustive"))
import check_instance as CI  # noqa: E402
from check_instance import exh, n5, n5b, verify, pg  # noqa: E402


def main():
    a = sys.argv[1:]
    src, name = a[0], a[-1]; stf = a[1] if len(a) > 2 else None
    g = pg.read(src); start = exh.readstart(stf) if stf else None
    st, fb = exh.trace(g, start, check=True)
    sig = tau = None
    if start:
        sig = [start[0].get(v, -1) for v in range(g.n)]; tau = [start[1].get(v, -1) for v in range(g.n)]
    L = []; _, _, itb, fbb = n5b.N5(g, mode="spec").run(sig, tau, trace=L)
    ev = lambda s, own: tuple(s[v] for v in range(g.n) if g.owner[v] == own)
    same = len(L) == len(st) and all(ev(x[0], 0) == ev(y[0], 0) and ev(x[1], 1) == ev(y[1], 1) for x, y in zip(L, st))
    it, fb5, win, ws, _ = n5.run(g, "n5", start)
    os.makedirs(os.path.join(HERE, "instances"), exist_ok=True)
    dst = os.path.join(HERE, "instances", name + ".pg"); shutil.copy(src, dst)
    if stf:
        shutil.copy(stf, os.path.join(HERE, "instances", name + ".start"))
    ref, rtag = CI.zlk(dst, g.n)
    errs = verify.check(g, win, ws)
    ok = same and (itb, fbb) == (it, fb5) and win == ref and not errs
    sha = hashlib.sha1(open(dst, "rb").read()).hexdigest()
    cmd = [sys.executable, os.path.join(HERE, "census.py"), "0", "0", dst + (":" + os.path.join(HERE, "instances", name + ".start") if stf else "")]
    out = subprocess.run(cmd, capture_output=True, text=True).stdout
    keep = [ln for ln in out.splitlines() if ln.startswith(("max_N_ep", "max_len_D", "max_absD", "top N_ep:", "top len_D2:", "RESULT"))]
    print(f"{name} sha1 {sha} n {g.n} m {g.m() if callable(getattr(g, 'm', None)) else ''} it {it} fb {fb5} | n5b states equal {same} "
          f"({itb},{fbb}) | regions = oink {rtag}: {win == ref} | verify: {'OK' if not errs else errs[:2]} | {'OK' if ok else 'FAIL'}")
    for ln in keep:
        print("   ", ln)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
