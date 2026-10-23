"""L-RED box 21 (produced on Opus 5.5): generators for the N8a pivot families of docs/red/R53-n8a-counter.md.
F_k = klcount_n16 + 2k isolated self-loops (owner Even) with new top priorities max+1 .. max+2k   (switch-all: 4·n^{3+k} + 3 dual pivots)
G_k = klglobal_n16 + 2k isolated self-loops with new top priorities                                (global: 8·n^{1+k} + 6; switch-all: 5·n^{1+k} + 1)
H_k = klmin_n13 (greedy shrink of klglobal_n16) + 2k isolated self-loops with new top priorities  (BOTH rules: 4·n^{1+k} dual pivots)
n = 16 + 2k (F, G), 13 + 2k (H). Usage: famgen.py F|G|H k > out.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
base = {"F": "klcount_n16.pg", "G": "klglobal_n16.pg", "H": "klmin_n13.pg"}[sys.argv[1]]; k = int(sys.argv[2])
lines = [l for l in open(os.path.join(HERE, "instances", base)) if l.strip() and not l.startswith("parity")]
n0 = len(lines); mx = max(int(l.split()[1]) for l in lines); n = n0 + 2 * k
out = [f"parity {n - 1};\n"] + lines + [f"{n0 + i} {mx + 1 + i} 0 {n0 + i};\n" for i in range(2 * k)]
sys.stdout.write("".join(out))
