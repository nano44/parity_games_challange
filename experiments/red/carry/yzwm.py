#!/usr/bin/env python3
"""L-RED box 6 (produced on Opus 5.5): graded fitness for the two DATA hypotheses of L-ALG's conditional (P-KT) proof
(GAP-C.md §18h, l-alg b50e0c2; Lead 06:49Z): (YZ) Dom(prevV) removal Y_0 = Z_f (union of the final round's regions);
(WM_c1) the rescue-attractor inclusion. Runs L-ALG's dtl_pnl.py UNMODIFIED in a subprocess (LALG8_DIR >= b50e0c2) and
parses its table:
  bad  = "YZ ..." lines other than "Y_0 = Z_f" + lines containing "WM FAILS" / "WM-global FAILS" + "P-KT VIOLATION"
  monoP = "MONO at P pieces ... VIOLATION";  mono = "MONO all pairs VIOLATION";  P = "P pieces (depth 0)"
Score: 1e11 bad + 1e8 min(monoP, 9) + 1e6 min(mono, 9) + min(P, 999). Order from DTL_ORDER. Usage: yzwm.py G.pg ..."""
import sys, os, re, subprocess

def measure(path):
    ld = os.path.join(os.environ["LALG8_DIR"], "experiments", "alg")
    r = subprocess.run([sys.executable, os.path.join(ld, "dtl_pnl.py"), os.path.abspath(path)], capture_output=True, text=True,
                       timeout=300, cwd=ld)
    if r.returncode != 0: raise RuntimeError(r.stderr[-300:])
    m = dict(bad=0, monoP=0, mono=0, P=0)
    for line in r.stdout.splitlines():
        mt = re.match(r"^\s+(.*): (\d+)$", line)
        if not mt: continue
        k, v = mt.group(1), int(mt.group(2))
        if k.startswith("YZ ") and "Y_0 = Z_f" not in k: m["bad"] += v
        if "WM FAILS" in k or "WM-global FAILS" in k or k.startswith("P-KT VIOLATION"): m["bad"] += v
        if k.startswith("MONO at P pieces") and "VIOLATION" in k: m["monoP"] += v
        if k.startswith("MONO all pairs VIOLATION"): m["mono"] += v
        if k.startswith("P pieces (depth 0)"): m["P"] += v
    return m

def score(path):
    m = measure(path)
    return 10 ** 11 * m["bad"] + 10 ** 8 * min(m["monoP"], 9) + 10 ** 6 * min(m["mono"], 9) + min(m["P"], 999)

if __name__ == "__main__":
    for f in sys.argv[1:]:
        print(os.path.basename(f), os.environ.get("DTL_ORDER", "stable"), measure(f))
