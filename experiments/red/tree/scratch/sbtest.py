import sys, subprocess
sys.path.insert(0, "/home/user/parity_games_challange/experiments/red/tree")
import gb, tiedlib, pg
OINK = "/home/user/parity_games_challange/tools/oink/build/oink"
f = sys.argv[1]
subprocess.run([OINK, "--zlk", f, f + ".sol"], capture_output=True)
G = gb.from_pg(f)
g, _ = G.game()
odd = {}
for l in open(f + ".sol"):
    a = l.strip().rstrip(";").split()
    if len(a) >= 3 and a[0].isdigit() and a[1] == "1": odd[int(a[0])] = int(a[2])
st = ({}, {v: w for v, w in odd.items() if g.owner[v] == 1})
c, reps = tiedlib.stats(g, st, cap=10 ** 5)
c0, _ = tiedlib.stats(g, None, cap=10 ** 5)
print(f, "n", g.n, "tau*-start", c, "default", c0)
