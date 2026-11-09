"""L-COMP box 37: named genome representation. to_named(G, names) -> dict(movers=[(name, lev, [opt...], start)], gate=[(name,k)...] in gate
rank order, br=[(name,k)...] in br rank order); opt = dict(wt=name|None, xt=name|None, bp=0/1). from_named(Nd) -> genome (eg195 schema,
b = option order). Names of unnamed movers: str(index)."""
import json
def to_named(G, names):
    inv = {v: k for k, v in names.items()}; nm = lambda x: None if x < 0 else inv.get(x, str(x))
    mv = []; gl = []; bl = []
    for x in range(G["N"]):
        os_ = []
        for k, (wt, xt, b) in enumerate(G["opts"][x]):
            os_.append(dict(wt=nm(wt), xt=nm(xt), bp=G["bp"][b])); gl.append((G["gate"][x][k], (nm(x), k))); bl.append((G["br"][b], (nm(x), k)))
        mv.append([nm(x), G["lev"][x], os_, G["start"][x]])
    return dict(movers=mv, gate=[q for _, q in sorted(gl)], br=[q for _, q in sorted(bl)])
def from_named(Nd):
    mv = Nd["movers"]; idx = {m[0]: i for i, m in enumerate(mv)}; N = len(mv)
    ix = lambda n: -1 if n is None else idx.get(n, -1)
    G = dict(N=N, lev=[m[1] for m in mv], opts=[], gate=[], br=[], bp=[], start=[])
    exist = {(m[0], k) for m in mv for k in range(len(m[2]))}
    gr = {q: r for r, q in enumerate(q for q in Nd["gate"] if q in exist)}; br = {q: r for r, q in enumerate(q for q in Nd["br"] if q in exist)}
    assert len(gr) == len(exist) and len(br) == len(exist), "rank lists miss options"
    b = 0
    for m in mv:
        o = []; g = []
        for k, op in enumerate(m[2]):
            o.append([ix(op["wt"]), ix(op["xt"]), b]); g.append(gr[(m[0], k)]); G["br"].append(br[(m[0], k)]); G["bp"].append(op["bp"]); b += 1
        G["opts"].append(o); G["gate"].append(g); G["start"].append(m[3] if m[3] < len(m[2]) else 0)
    # re-rank gate/br to permutations 0..M-1 already
    return G
