import sys, os, json, random
sys.path[:0] = [os.path.dirname(os.path.abspath(__file__)), "../r178", "../r170", "../../new/box21"]
from n5x import Engine
import downgen, stabrun, ideal, fastcyc
def cmp(G):
    S, why = ideal.traj(G); R = stabrun.analyse(G, 0); gv = R["gv"]
    real = [tuple(next(k for k in range(G["deg"]) if R["S"][j][v] == gv[(v, k)]) for v in range(G["N"])) for j in range(len(R["S"]))]
    m = len(S); same = real[:m] == S
    return len(S) - 1, why, R["faithful"], same
if __name__ == "__main__":
    rng = random.Random(int(sys.argv[1])); tot = [0, 0]
    for t in range(int(sys.argv[2])):
        G = downgen.randdown(int(sys.argv[3]), 2, rng) if os.environ.get('CLASS', 'down') == 'down' else downgen.randacyc(int(sys.argv[3]), 2, rng) if os.environ.get('CLASS') == 'acyc' else fastcyc.randG(int(sys.argv[3]), 2, rng); r = cmp(G); tot[0] += 1; tot[1] += r[3] and r[0] == r[2]
        if not (r[3] and r[0] == r[2]): print("MISMATCH", t, r)
    print("games", tot[0], "equal (states and FAITHFUL = IDEAL steps)", tot[1])
