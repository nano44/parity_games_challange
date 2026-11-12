#!/usr/bin/env python3
"""L-COMP box 38: CHAIN3's bound (P-N5-CHAIN line L3 / box 196 §5, quoted): «T3 + 3 ≤ (1 + n3·((2M + 3)·F′_(U(G))(M) − 1))·(L3 + 1) + 3»,
n3 = N + 7M + 10, L3 = (M + 1)(2M + 1)(N + 1) + N(n3 − 1); F′_0 = 1 + M(M + 1)/2, F′_B = (M² + 3M + 1)(1 + M·F′_(B−1)²) (P-N5-ASC §5,
RESULTS R121 (f)). Prints log10 of the bound (exact integer arithmetic; F′ grows doubly exponentially in U). Usage: chainb38.py G.json ..."""
import sys, json, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import u38
def bound(N, M, U):
    F = 1 + M * (M + 1) // 2
    for _ in range(U): F = (M * M + 3 * M + 1) * (1 + M * F * F)
    n3 = N + 7 * M + 10; L3 = (M + 1) * (2 * M + 1) * (N + 1) + N * (n3 - 1)
    return (1 + n3 * ((2 * M + 3) * F - 1)) * (L3 + 1) + 3
def lbound(N, M, U):
    """log10 of the bound, in log space for large U (relative error < 1e-9 once F' > 10^15)."""
    if U <= 6: x = bound(N, M, U); return math.log10(x) if x < 10 ** 300 else len(str(x)) - 1 + math.log10(int(str(x)[:15]) / 10 ** 14)
    lf = math.log10(1 + M * (M + 1) // 2)
    for _ in range(U): lf = math.log10(M * M + 3 * M + 1) + math.log10(M) + 2 * lf
    n3 = N + 7 * M + 10; L3 = (M + 1) * (2 * M + 1) * (N + 1) + N * (n3 - 1)
    return math.log10(n3 * (2 * M + 3)) + lf + math.log10(L3 + 1)
if __name__ == "__main__":
    for f in sys.argv[1:]:
        G = json.load(open(f)); M = u38.NM(G) - G["N"]; U = u38.U(G)
        print(f"{os.path.basename(f)} N {G['N']} M {M} U {U} log10(CHAIN3 bound on T3 + 3) {lbound(G['N'], M, U):.4g}")
