#!/usr/bin/env python3
"""Box 23: pin witnesses. For each GAME.pg START (full start file) or a results JSON (exh23 best records, written to instances/):
 (1) n5-box17 pin.check: n5.py (L-NEW driver) = n5b SPEC state by state, (it, fb) equal, regions = Oink zlk @ 8fbf0a7 (tl if zlk
     aborts), verify.py strategies OK, sha1;
 (2) L-RED's experiments/red/seg/xeng.py (n5.py on L-SI's si.py valuations vs n5b): "state sequences identical: True";
 (3) the counts: rstar.py (mine, n5b) and L-NEW's xirise.py (n5x), max R*_F and max FL_F must agree.
Usage: pin23.py --json RESULTS.json PREFIX     |    pin23.py GAME.pg START [GAME.pg START ...]"""
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(ROOT, "n5-box17"))
import types  # noqa: E402
P = types.SimpleNamespace()   # n5-box17/pin.py's check(), loaded without running pin.py's script part (which starts at "d = json.load")
_src = open(os.path.join(ROOT, "n5-box17", "pin.py")).read().split("d = json.load")[0]
_ns = {"__file__": os.path.join(ROOT, "n5-box17", "pin.py")}; exec(compile(_src, "pin.py", "exec"), _ns); P.check = _ns["check"]
CI = _ns["CI"]; CI.INST = os.path.join(HERE, "instances")


def counts(pgf, stf):
    a = subprocess.run([sys.executable, "-I", os.path.join(HERE, "rstar.py"), pgf, stf], capture_output=True, text=True, cwd=ROOT).stdout
    b = subprocess.run(["timeout", "1800", sys.executable, "-I", "new/box85/xirise.py", pgf, stf], capture_output=True, text=True, cwd=ROOT).stdout
    m = re.search(r"'rs': (\d+).*'fl': (\d+)", a); x = re.search(r"'rstar': (\d+), 'fl': (\d+)", b)
    mine = (int(m.group(1)), int(m.group(2))) if m else None; theirs = (int(x.group(1)), int(x.group(2))) if x else None
    return mine, theirs


def one(pgf, stf):
    g = CI.pg.read(pgf); s, t = CI.n5b.read_start(stf, g)
    st = ({v: s[v] for v in range(g.n) if g.owner[v] == 0}, {v: t[v] for v in range(g.n) if g.owner[v] == 1})
    if any(w == -1 for w in list(st[0].values()) + list(st[1].values())) or len(st[0]) + len(st[1]) != g.n:
        print("PARTIAL START", stf); return False
    name = os.path.splitext(os.path.basename(pgf))[0]
    ok, sha = P.check(g, st, name)                      # writes instances/name.pg/.start (same content) and checks (1)
    x = subprocess.run([sys.executable, "-I", os.path.join(ROOT, "red", "seg", "xeng.py"), pgf, stf], capture_output=True, text=True).stdout
    xok = "state sequences identical: True" in x
    mine, theirs = counts(os.path.relpath(pgf, ROOT), os.path.relpath(stf, ROOT))
    cok = mine is not None and mine == theirs
    print(f"   xeng {'OK' if xok else 'FAIL ' + x.strip()[-200:]} | R*_F, FL_F mine {mine} xirise {theirs} {'OK' if cok else 'FAIL'}")
    return ok and xok and cok


def main():
    allok = True
    if sys.argv[1] == "--json":
        d = json.load(open(sys.argv[2])); pre = sys.argv[3]; os.makedirs(CI.INST, exist_ok=True)
        for k in ("rs", "fl"):
            rec = d["best"].get(k)
            if not rec or rec[0] == 0:
                continue
            val, inst = rec; g = CI.pg.Game(inst["prio"], inst["owner"], inst["succ"]); name = f"{pre}_{k}{val}"
            p = os.path.join(CI.INST, name + ".pg"); CI.pg.write(g, p); s, t = inst["start"]
            with open(os.path.join(CI.INST, name + ".start"), "w") as f:
                f.write("SIGMA0 " + " ".join(f"{v}:{s[v]}" for v in range(g.n) if g.owner[v] == 0) + "\n")
                f.write("TAU0 " + " ".join(f"{v}:{t[v]}" for v in range(g.n) if g.owner[v] == 1) + "\n")
            print(f"[{k} = {val}]", end=" ", flush=True)
            allok &= one(p, os.path.join(CI.INST, name + ".start"))
    else:
        a = sys.argv[1:]
        for pgf, stf in zip(a[::2], a[1::2]):
            allok &= one(os.path.abspath(pgf), os.path.abspath(stf))
    print("PIN", "ALL OK" if allok else "FAIL")


if __name__ == "__main__":
    main()
