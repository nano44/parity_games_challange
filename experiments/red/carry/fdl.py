#!/usr/bin/env python3
"""L-RED box 6 (produced on Opus 5.5): (R1) target (Lead 10:14Z; REFEREE docs/referee/R-PROVED2.md (h), gap G-h1): consecutive
searches where s+1 re-finds a tangle of s as a duplicate with nothing earlier differing, so the tattr logs misalign.
Runs L-ALG's dtl_fdlcheck.py UNMODIFIED in a subprocess (LALG12_DIR) and counts its violations; gradient = duplicate-check
hits (k4b/pieces.py tracer, LALG5_DIR). Score: 1e11 violations + 1e6 min(dups, 999). Order from DTL_ORDER. Usage: fdl.py G.pg"""
import sys, os, re, subprocess
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "k4b"))

def measure(path):
    ld = os.path.join(os.environ["LALG12_DIR"], "experiments", "alg")
    r = subprocess.run([sys.executable, os.path.join(ld, "dtl_fdlcheck.py"), os.path.abspath(path)], capture_output=True, text=True, timeout=300, cwd=ld)
    mt = re.search(r"violations (\d+)", r.stdout)
    if not mt: raise RuntimeError(r.stdout[-300:] + r.stderr[-300:])
    import pieces as PC, pg
    d0 = PC.K.P.build(pg.read(path)); d = PC.PT(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.run()
    return dict(viol=int(mt.group(1)), dups=sum(len(tr["dups"]) for tr in d.trace))

def score(path):
    m = measure(path); return 10 ** 11 * m["viol"] + 10 ** 6 * min(m["dups"], 999)

if __name__ == "__main__":
    for f in sys.argv[1:]: print(os.path.basename(f), os.environ.get("DTL_ORDER", "stable"), measure(f))
