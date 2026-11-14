# Box 197 (L-NEW successor 65): height family on L-SI box 85's two85.build (read-only copy). Three lane formulas per height h = 2..8.
import sys, json, random; sys.path.insert(0, sys.argv[1]); import two85
from gen83 import save
out = sys.argv[2]
tri = [2, 5, 9, 14, 20, 27, 35, 44]
for h in range(2, 9):
    for fam in ("A", "B", "C"):
        if fam == "A": L, LM, LL = tri[:h], [6 * (l + 1) for l in range(h - 1)], tri[:h]
        if fam == "B": L, LM, LL = [3 * l + 1 for l in range(h)], [5 + 4 * l for l in range(h - 1)], tri[:h]
        if fam == "C": r = random.Random(1970 + h); L = sorted(r.sample(range(1, 6 * h), h)); LM = sorted(r.sample(range(4, 9 * h), h - 1)); LL = tri[:h]
        c = {"h": h, "L": L, "LM": LM, "LL": LL, "w": ["L"], "lw": ["M+"], "lup": "M+", "lexit": "M+"}
        G, names = two85.build(c); save(G, names, f"{out}/H{h}{fam}.json")
