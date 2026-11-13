import sys, sim244 as sim70
G = sim70.load(sys.argv[1]); T, sw, S = sim70.run(G, trace=True); N = G["N"]; lev = G["lev"]
lo = int(sys.argv[2]) if len(sys.argv) > 2 else 0; hi = int(sys.argv[3]) if len(sys.argv) > 3 else 99
print("T", T, "N", N, "M", len(G["br"]))
for x in range(N):
    if not lo <= lev[x] <= hi: continue
    o = G["opts"][x]
    print(f"x{x:2d} L{lev[x]:2d} sw{sw[x]:4d} st{G['start'][x]} | " + " | ".join(f"k{k}: W{oo[0]:3d} X{oo[1]:3d}(L{lev[oo[1]] if oo[1]>=0 else -1:2d}) r{G['br'][oo[2]]:3d}{'+' if G['bp'][oo[2]]==0 else '-'} g{G['gate'][x][k]:3d}" for k, oo in enumerate(o)))
