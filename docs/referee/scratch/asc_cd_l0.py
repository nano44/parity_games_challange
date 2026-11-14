"""REFEREE 28: CHAIN-DECOMP line wording check. For v = e_g of a level-0 gate g, the first e-vertex on v's play is v itself and its
successor is c_W (not a mover), and v is not in Pi(v) (its cycle node is c_W). Own builder / engine; prints one witness per genome.
Usage: asc_cd_l0.py GENOME.json ..."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xicyc_vj import VJ
from xicyc_replay import build
for f in sys.argv[1:]:
    G = json.load(open(f)); prio, own, fs, sig, movers, idx, succ = build(G, False); E = VJ(prio, own, fs)
    st, val = E.best_reply([sig.get(v) for v in range(E.n)])
    q = next((x, k) for x in range(G["N"]) for k in range(len(G["opts"][x])) if G["opts"][x][k][0] < 0)
    e = idx[("e", q)]
    print(os.path.basename(f), "level-0 option", q, "e-vertex", e, "successor", fs[e], "== cW", fs[e] == [idx["cW"]],
          "successor is a mover", fs[e][0] in movers, "| Lambda(e) == cW", val[e][0] == idx["cW"], "| e in Pi(e)", e in val[e][1])
