#!/usr/bin/env python3
"""Fast self-check (run by check.sh / scripts/verify.sh):
 1. graphs.family sizes for (4,6): 27 even / 64 odd (L-STRUCT's independent enumeration gives the same counts);
 2. w(2,6) = 3: k=2 UNSAT with a CaDiCaL LRAT proof verified by lrat_check.py (if the cadical binary is present,
    else by two solvers: cadical153 + glucose4 via python-sat), k=3 SAT re-verified by check.py;
 3. w(3,5) >= 7: k=6 UNSAT (same proof route);
 4. lrat_check.py rejects a proof with a dropped hint."""
import sys, os, subprocess, shutil, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import graphs, search, check
ok = True
def fail(m):
    global ok; ok = False; print("FAIL:", m)
HERE = os.path.dirname(os.path.abspath(__file__))
e, o = graphs.family(4, 6, 0), graphs.family(4, 6, 1)
if (len(e), len(o)) != (27, 64): fail(f"family sizes {len(e)}/{len(o)}")
else: print("1. (4,6) family: 27 even / 64 odd")
quiet = lambda s: None
with tempfile.TemporaryDirectory() as td:
    def unsat_proved(n, d, k):
        cnf = os.path.join(td, f"{n}{d}{k}.cnf")
        aut, used = search.run(n, d, k, cnf_out=cnf, log=quiet)
        if aut is not None: return False, "SAT"
        if shutil.which("cadical"):
            pr = cnf + ".lrat"
            r = subprocess.run(["cadical", "-q", "--lrat=true", "--binary=false", cnf, pr], capture_output=True, text=True)
            c = subprocess.run([sys.executable, os.path.join(HERE, "lrat_check.py"), cnf, pr], capture_output=True, text=True)
            return r.returncode == 20 and c.returncode == 0, "LRAT " + c.stdout.strip()
        a2, _ = search.run(n, d, k, solver="glucose4", log=quiet)
        return a2 is None, "two solvers (no cadical binary)"
    good, how = unsat_proved(2, 6, 2)
    aut, _ = search.run(2, 6, 3, log=quiet)
    if not good or aut is None or check.violations(aut, graphs.family(2, 6, 0), graphs.family(2, 6, 1)):
        fail(f"w(2,6)=3 not reproduced ({how})")
    else:
        print(f"2. w(2,6) = 3: k=2 UNSAT ({how}); k=3 SAT, checker ok")
    good, how = unsat_proved(3, 5, 6)
    if not good: fail(f"w(3,5) >= 7 not reproduced ({how})")
    else: print(f"3. w(3,5) >= 7: k=6 UNSAT ({how})")
    if shutil.which("cadical"):
        cnf = os.path.join(td, "262.cnf"); pr = cnf + ".lrat"
        lines = open(pr).read().splitlines()
        for i, l in enumerate(lines):
            t = l.split()
            if t[1] != "d":
                z = t.index("0", 1)
                if len(t) - z - 2 >= 2:
                    lines[i] = " ".join(t[:z + 1] + t[z + 2:]); break
        open(pr, "w").write("\n".join(lines) + "\n")
        c = subprocess.run([sys.executable, os.path.join(HERE, "lrat_check.py"), cnf, pr], capture_output=True, text=True)
        if c.returncode == 0: fail("lrat_check accepted a corrupted proof")
        else: print("4. lrat_check rejects a corrupted proof:", c.stdout.strip())
    else:
        print("4. NOT RUN: no cadical binary")
print("SELFCHECK", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
