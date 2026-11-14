import sys, os, json, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, "../r178")
import downgen, stabrun, fastcyc
rng = random.Random(int(sys.argv[1])); res = []
for t in range(int(sys.argv[2])):
    G = downgen.randdown(int(sys.argv[3]), 2, rng)
    ideal = fastcyc.simulate(G); R = stabrun.analyse(G, 0)
    bad = [r for r in R["rows"] if not (r[2] and r[3] and r[4]) or r[1]]
    print(t, "IDEAL", ideal, "K", R["K"], "FAITHFUL", R["faithful"], "first bad", bad[:1])
