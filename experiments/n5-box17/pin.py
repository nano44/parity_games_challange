#!/usr/bin/env python3
"""Box 17: pin the extremal games of a results JSON (exh17 / randtab / merge output). For each quantity k in best: writes
instances/<PREFIX>_<k>.pg (+ .start) and runs (1) n5-exhaustive/check_instance.check (n5.py via n5x = n5b SPEC full state sequence,
regions = Oink zlk @ 8fbf0a7 (tl if zlk aborts), verify.py strategies, sha1), (2) xcheck.py (box17 on n5b vs L-SI's tools on L-SI's
engine: the quantity values). Usage: pin.py RESULTS.json PREFIX"""
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "n5-exhaustive"))
import hashlib
import check_instance as CI
from check_instance import pg, trace, n5, n5b, verify
CI.INST = os.path.join(HERE, "instances")


def check(g, start, name):
    """check_instance.check without its C^1O-only measures."""
    os.makedirs(CI.INST, exist_ok=True); path = os.path.join(CI.INST, name + ".pg"); pg.write(g, path)
    if start:
        with open(os.path.join(CI.INST, name + ".start"), "w") as f:
            f.write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in sorted(start[0].items())) + "\n")
            f.write("TAU0 " + " ".join(f"{v}:{w}" for v, w in sorted(start[1].items())) + "\n")
    sha = hashlib.sha1(open(path, "rb").read()).hexdigest()
    st, fb = trace(g, start, check=True)
    sig = tau = None
    if start:
        sig = [start[0].get(v, -1) for v in range(g.n)]; tau = [start[1].get(v, -1) for v in range(g.n)]
    L = []; _, _, itb, fbb = n5b.N5(g, mode="spec").run(sig, tau, trace=L)
    ev = lambda s, own: tuple(s[v] for v in range(g.n) if g.owner[v] == own)
    same = len(L) == len(st) and all(ev(a[0], 0) == ev(b[0], 0) and ev(a[1], 1) == ev(b[1], 1) for a, b in zip(L, st))
    it, fb5, win, ws, _ = n5.run(g, "n5", start); ref, rtag = CI.zlk(path, g.n); errs = verify.check(g, win, ws)
    ok = same and (itb, fbb) == (it, fb5) and win == ref and not errs
    print(f"{name} sha1 {sha} n {g.n} it {it} fb {fb5} | n5b states equal {same} ({itb},{fbb}) | regions = oink {rtag}: {win == ref} | "
          f"verify: {'OK' if not errs else errs[:2]} | {'OK' if ok else 'FAIL'}")
    return ok, sha
d = json.load(open(sys.argv[1])); pre = sys.argv[2]; allok = True
for k, rec in d["best"].items():
    if not rec: continue
    val, inst, place = rec; g = pg.Game(inst["prio"], inst["owner"], inst["succ"]); name = f"{pre}_{k}"
    st = None
    if inst["start"]:
        s, t = inst["start"]; st = ({v: s[v] for v in range(g.n) if g.owner[v] == 0}, {v: t[v] for v in range(g.n) if g.owner[v] == 1})
    print(f"[{k} = {val} at {place}]", end=" "); sys.stdout.flush()
    ok, sha = check(g, st, name)
    p = os.path.join(CI.INST, name + ".pg"); args = [p] + ([os.path.join(CI.INST, name + ".start")] if st else [])
    x = subprocess.run([sys.executable, os.path.join(HERE, "xcheck.py")] + args, capture_output=True, text=True).stdout.strip()
    print("   ", x); allok &= ok and " OK " in x
print("PIN", "ALL OK" if allok else "FAIL")
