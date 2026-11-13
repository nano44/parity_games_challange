import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gk108, ideal108
k = int(sys.argv[1]); G, names = gk108.build(k); S = ideal108.Ideal(G).run(); ix = {n: i for i, n in enumerate(names)}
def col(s, j):
    g = lambda n: str(s[ix[n]]) if n in ix else "-"
    return f"{g(f'u{j}')}{g(f'v{j}')} {g(f'y{j}')}{g(f'yb{j}')} {g(f'yp{j}')}{g(f'ypb{j}')}{g(f'e{j}')}"
print("  t | " + " | ".join(f"uv yY pPe [{j}]" for j in range(k)))
for t, s in enumerate(S):
    print(f"{t:3d} | " + " | ".join(col(s, j).ljust(13) for j in range(k)))
