import sys, json
from dsl import build
import topo2
sys.path.insert(0, "../sel"); import trace as T
from fbphase import fstats
G = json.load(open(sys.argv[1])) if sys.argv[1] != "seed" else topo2.rnd(None)
m = int(sys.argv[2])
g, st, nm = build(topo2.spec(G, m))
st = topo2.taustar(g, st); T.run(g, st, nm=dict(enumerate(nm)))
print(fstats(g, st))
