"""REFEREE successor 25: membership (i)-(vii) for P-M2D-DEAD from RESULTS R104 (l. 9864) and R110 (l. 11323) text; own code."""
import json, sys
for f in sys.argv[1:]:
    G = json.load(open(f)); N = G["N"]; d = N // 2; O = [(x, k) for x in range(N) for k in range(len(G["opts"][x]))]; M = len(O)
    ok = {}
    ok["(i) W-targets one level down, none at level 0"] = all((G["opts"][x][k][0] == -1) == (G["lev"][x] == 0) and (G["opts"][x][k][0] < 0 or G["lev"][G["opts"][x][k][0]] == G["lev"][x] - 1) for x, k in O)
    ok["(i) Xi-targets a mover or X(-1)"] = all(-1 <= G["opts"][x][k][1] < N for x, k in O)
    ok["(ii) N = 2d even, lev = x//2, levels 0..d-1"] = N % 2 == 0 and G["lev"] == [x // 2 for x in range(N)]
    ok["(ii) W_d: level-0 movers exactly {0,1}"] = [x for x in range(N) if G["lev"][x] == 0] == [0, 1]
    ok["(ii) all degree 2"] = all(len(G["opts"][x]) == 2 for x in range(N))
    ok["(ii) option k of level l>=1 W-points to 2(l-1)+k"] = all(G["opts"][x][k][0] == 2 * (G["lev"][x] - 1) + k for x, k in O if G["lev"][x] >= 1)
    B = [G["opts"][x][k][2] for x, k in O]
    ok["(v) one beta per option, ids 0..M-1"] = sorted(B) == list(range(M)) and len(G["br"]) == M and len(G["bp"]) == M
    ok["(v) ranks distinct"] = len(set(G["br"])) == M
    ok["(v) parities in {0,1}"] = set(G["bp"]) <= {0, 1}
    g = [G["gate"][x][k] for x, k in O]; ok["(v) gates distinct"] = len(set(g)) == M
    ok["(vi) start one option per mover"] = len(G["start"]) == N and all(G["start"][x] in range(len(G["opts"][x])) for x in range(N))
    adj = {x: [G["opts"][x][k][1] for k in range(2) if G["opts"][x][k][1] >= 0] for x in range(N)}
    col = [0] * N
    def dfs(u):
        col[u] = 1
        for v in adj[u]:
            if col[v] == 1 or (col[v] == 0 and not dfs(v)): return False
        col[u] = 2; return True
    ok["(iv) Xi-graph acyclic"] = all(col[x] == 2 or dfs(x) for x in range(N))
    ok["(iii) ISO (not required)"] = all(G["opts"][x][k][1] not in (0, 1) for x, k in O)
    print(f.split("/")[-1], "d", d, "M", M); [print("  ", k, v) for k, v in ok.items()]
