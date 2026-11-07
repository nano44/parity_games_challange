import sys, os, json
sys.path[:0] = [os.path.dirname(os.path.abspath(__file__)), "../r170", "../../new/box21"]
sys.path.insert(0, "../r178")
import ideal, rel, stab
for f in sys.argv[1:]:
    G = json.load(open(f)); S, why = ideal.traj(G); st = rel.stats(G, S); pv = rel.pervertex(G, S)
    g = stab.build(G, 0, kgad=True, esc=True)[0]
    av = rel.avail(G, S)
    print(f"{os.path.basename(f)} | n {g.n} | movers {G['N']} | d {max(G['lev']) + 1} | deg {G['deg']} | L_FL {st['T']} | M {st['M']} | DREL {st['DREL']} | D2 {st['D2']} | (mu,KCH,per-stretch,twice) {pv} | (AVNmax,AVNsum,movesmax,movessum) {av}")
