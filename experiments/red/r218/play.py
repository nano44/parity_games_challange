import sys, json, own
"""L-RED 55 R218: print the play of named vertices at state t of an own.py run. Usage: play.py G.json t name ..."""
f = sys.argv[1]; t = int(sys.argv[2]); G = json.load(open(f)); nm = json.load(open(f[:-5] + ".names.json")); inv = {v: k for k, v in nm.items()}
out, V, O, ow = own.run(G); rv = {v: k for k, v in V.items()}; n, prio, own_, succ, _, _ = own.build(G)
def vn(v):
    k = rv[v]
    if isinstance(k, str): return k
    if k[0] == "x": return inv[k[1]]
    return f"{k[0]}:{inv[k[1][0]]}.{k[1][1]}"
s, vals, tau = out[t]; N = G["N"]
nxt = lambda v: (s[v] if v < N else (tau[v] if own_[v] == 1 else succ[v][0]))
for m in sys.argv[3:]:
    v = nm[m]; seen = []; 
    while v not in seen: seen.append(v); v = nxt(v)
    print(m, "->", " ".join(vn(u) + (f"[{prio[u]}]" if vn(u)[0] == "e" else "") for u in seen if vn(u)[0] != "b" or True), "|| loops to", vn(v))
