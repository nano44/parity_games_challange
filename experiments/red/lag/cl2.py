"""L-RED box 10 (produced on Opus 5.5): the REGION CLOCK alone: L-ALG dtl_chainfam UP chain (k) + root top S (pr 2k+4,
Odd-owned, edge to the Odd sink W) + edge a -> S. S's round-1 root region gains x_m from visit m (clockcheck.py).
Usage: cl2.py k out.pg"""
import sys; from gb import GB
def build(k):
    g = GB()
    g.v("a", 2*k+1, 0); g.v("b", 2*k, 1); g.v("z", 2*k, 1)
    for j in range(1, k+1): g.v(f"x{j}", 2*(j-1), 1)
    g.e("a", "b", "a"); g.e("b", "z", "b"); g.e("z", "z", f"x{k}")
    for j in range(1, k+1): g.e(f"x{j}", f"x{j}", "a" if j == 1 else f"x{j-1}")
    g.v("S", 2*k+4, 1); g.v("W", 2*k+5, 1); g.e("W", "W"); g.e("S", "W"); g.e("a", "S")
    return g
if __name__ == "__main__": build(int(sys.argv[1])).write(sys.argv[2])
