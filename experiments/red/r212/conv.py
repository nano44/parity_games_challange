#!/usr/bin/env python3
"""L-RED R212: convert fk.c text genomes <-> box 150 / flipdp JSON (R197 2-wide ladder convention of L-SI realise.py:
option k of a level-l mover has W-target 2(l-1)+k and rank id 2x+k). Usage: conv.py tojson in.txt out.json | totxt in.json out.txt"""
import sys, json
def read_txt(p):
    L = {}
    for line in open(p):
        w = line.split()
        if w: L[w[0]] = [int(x) for x in w[1:]]
    m = L["m"][0]; N = 2 * (m + 1); xt = L["xt"]
    lev = [v // 2 for v in range(N)]; opts = []
    for x in range(N):
        opts.append([[2 * (lev[x] - 1) + k if lev[x] > 0 else -1, xt[2 * x + k], 2 * x + k] for k in range(2)])
    gate = [[L["gate"][2 * x], L["gate"][2 * x + 1]] for x in range(N)]
    order, seen = [], set()
    def dfs(z):
        if z in seen: return
        seen.add(z)
        for o in opts[z]:
            if o[1] >= 0: dfs(o[1])
        order.append(z)
    for z in range(N): dfs(z)
    return {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": L["br"], "bp": L["bp"], "start": [0] * N, "xorder": order[::-1]}
def write_txt(G, p):
    N = G["N"]; m = max(G["lev"])
    for x in range(N):
        for k in range(2):
            o = G["opts"][x][k]
            assert o[2] == 2 * x + k and o[0] == (2 * (G["lev"][x] - 1) + k if G["lev"][x] > 0 else -1), "not in the ladder convention"
    with open(p, "w") as f:
        f.write("m %d\nxt %s\nbr %s\nbp %s\ngate %s\n" % (m, " ".join(str(G["opts"][x][k][1]) for x in range(N) for k in range(2)),
                " ".join(map(str, G["br"])), " ".join(map(str, G["bp"])), " ".join(str(G["gate"][x][k]) for x in range(N) for k in range(2))))
if __name__ == "__main__":
    if sys.argv[1] == "tojson": json.dump(read_txt(sys.argv[2]), open(sys.argv[3], "w"))
    else: write_txt(json.load(open(sys.argv[2])), sys.argv[3])
