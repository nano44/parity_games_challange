"""kl2fast.py reproduces kl2.py: compare two bench CSVs row by row on (family, N, file, rule, seed) -> (pivots_primal,
pivots_dual); both must be status OK. Usage: repro.py A.csv B.csv [A2.csv B2.csv ...]. Exit 1 on any difference."""
import csv
import sys


def load(p):
    with open(p) as f:
        return {(r["family"], r["N"], r["file"], r["rule"], r["seed"]): r for r in csv.DictReader(f)}


bad = tot = 0
args = sys.argv[1:]
for a, b in zip(args[::2], args[1::2]):
    A, B = load(a), load(b)
    for k in sorted(set(A) | set(B)):
        if k not in A or k not in B:
            print("MISSING", k, a if k not in A else b); bad += 1; continue
        x, y = A[k], B[k]
        tot += 1
        if x["status"] != "OK" or y["status"] != "OK" or \
                (x["pivots_primal"], x["pivots_dual"]) != (y["pivots_primal"], y["pivots_dual"]):
            print("DIFF", k, x["status"], x["pivots_primal"], x["pivots_dual"], "|", y["status"], y["pivots_primal"],
                  y["pivots_dual"]); bad += 1
print(f"repro: {tot} rows compared, {bad} differences: {'PASS' if bad == 0 else 'FAILED'}")
sys.exit(1 if bad else 0)
