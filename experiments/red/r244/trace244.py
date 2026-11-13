import sys, sim244 as sim70
G = sim70.load(sys.argv[1]); T, sw, S = sim70.run(G, trace=True); N = G["N"]; lev = G["lev"]
xs = [int(a) for a in sys.argv[2].split(",")]; t0 = int(sys.argv[3]) if len(sys.argv) > 3 else 0; t1 = int(sys.argv[4]) if len(sys.argv) > 4 else T
print("t   " + " ".join(f"x{x:<2d}" for x in xs) + "  | switching movers (level)")
for t in range(t0, min(t1, T) + 1):
    mv = [x for x in range(N) if t > 0 and S[t][x] != S[t - 1][x]]
    print(f"{t:3d} " + " ".join(f" {S[t][x]}{'*' if x in mv else ' '}" for x in xs) + "  | " + " ".join(f"{x}(L{lev[x]})" for x in mv))
