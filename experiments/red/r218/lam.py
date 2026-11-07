"""L-RED 55 R218: per state, the cycle node and pre-cycle e-count of named vertices (own.py). Usage: lam.py G.json name ..."""
import sys, json, own
f = sys.argv[1]; G = json.load(open(f)); nm = json.load(open(f[:-5] + ".names.json")); inv = {v: k for k, v in nm.items()}
out, V, O, ow = own.run(G); rv = {v: k for k, v in V.items()}
def vn(v):
    k = rv[v]
    if isinstance(k, str): return k
    if k[0] == "x": return inv[k[1]]
    return f"{k[0]}:{inv[k[1][0]]}.{k[1][1]}"
for t, (s, vals, tau) in enumerate(out):
    print(t, " ".join(f"{m}:{vn(vals[nm[m]][0])}/{len(vals[nm[m]][1])}" for m in sys.argv[2:]))
