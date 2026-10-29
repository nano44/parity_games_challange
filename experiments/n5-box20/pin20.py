#!/usr/bin/env python3
"""Box 20: pin the max-SBC (and max SF-iteration) game of each table: writes instances/<TABLE>_<key>.pg + .start, reruns N5-SF (n5sf.py)
from the stored start, recomputes SBC_σ, SBC_τ, iterations, and checks the regions against Oink zlk @ 8fbf0a7. Usage: pin20.py TABLE.json ..."""
import hashlib, json, os, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); EXP = os.path.abspath(os.path.join(HERE, ".."))
for p in ("lnew_box54",): sys.path.insert(0, os.path.join(HERE, p))
sys.path.insert(0, os.path.join(EXP, "harness"))
import n5sf, pg
from n5x import Engine, dual
OINK = os.path.join(EXP, "..", "tools", "oink", "build", "oink"); os.makedirs(os.path.join(HERE, "instances"), exist_ok=True)
for f in sys.argv[1:]:
    d = json.load(open(f)); tab = os.path.basename(f)[:-5]
    for key in ("sbc", "sf_it"):
        val, inst = d["best"][key]; g = pg.Game(inst["prio"], inst["owner"], inst["succ"]); base = os.path.join(HERE, "instances", f"{tab}_{key}")
        pg.write(g, base + ".pg"); s, t = inst["start"]
        with open(base + ".start", "w") as fh:
            fh.write("SIGMA0 " + " ".join(f"{v}:{s[v]}" for v in range(g.n) if g.owner[v] == 0) + "\nTAU0 " + " ".join(f"{v}:{t[v]}" for v in range(g.n) if g.owner[v] == 1) + "\n")
        sd = ({v: s[v] for v in range(g.n) if g.owner[v] == 0}, {v: t[v] for v in range(g.n) if g.owner[v] == 1})
        E, T = n5sf.trace(g, sd); T2 = [x for x in T if "lam" in x]; Ed = Engine(dual(g)); tb = [tuple(Ed.evaluate(tuple(x["t"]))[1]) for x in T2]
        sbs = sum(T2[i]["sb"] != T2[i + 1]["sb"] for i in range(len(T2) - 1)); sbt = sum(tb[i] != tb[i + 1] for i in range(len(T2) - 1))
        with tempfile.TemporaryDirectory() as td:
            subprocess.run([OINK, "--zlk", "-w", "1", base + ".pg", td + "/s"], capture_output=True, check=True); ref = pg.read_sol(open(td + "/s").read(), g.n)
        vs, _ = E.evaluate(tuple(T2[-1]["s"])); ok = [E.par[x[0]] for x in vs] == list(ref) and not T[-1].get("cycle", False)
        print(f"{tab}_{key} table {key} {val} | sha1 {hashlib.sha1(open(base + '.pg', 'rb').read()).hexdigest()} n {g.n} | rerun: SF it {len(T2) - 1} SBC {sbs}+{sbt} | regions = oink zlk: {ok}")
