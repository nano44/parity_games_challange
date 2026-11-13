#!/usr/bin/env python3
"""L-RED 70 R244: CORE of a tower. Greedy deletion of movers from a Xi-acyclic genome while the enumeration depth k (box 217 A6: full
levels, sw = |K| - 1 from some base level; sim244.kdepth) stays >= K0. A removal of x: every W-pointer to x is re-pointed to another
mover of x's level (tried in turn; no such mover -> x stays), every Xi-pointer to x goes to the exit or to x's start-option Xi-target
('splice'); ranks and gates keep their relative order. After the deletion pass, Xi-pointers are cut to the exit where k survives, and
deletion is retried. Engine: sim244 (own). Output: the core genome (general R104 genome: movers per level may differ from 2).
Usage: prune244.py G.json OUT.json [SEED]"""
import sys, json, random, copy, hashlib, sim244
def remove(G, x, wrepl, mode):
    N = G["N"]; H = copy.deepcopy(G)
    sx = H["opts"][x][H["start"][x]][1]
    for y in range(N):
        if y == x: continue
        for o in H["opts"][y]:
            if o[0] == x:
                if wrepl is None: return None
                o[0] = wrepl
            if o[1] == x: o[1] = -1 if mode == "exit" else (sx if sx != y else -1)
    keep = [y for y in range(N) if y != x]; ren = {y: i for i, y in enumerate(keep)}; ren[-1] = -1
    bs = [o[2] for y in keep for o in H["opts"][y]]; rb = {b: i for i, b in enumerate(bs)}
    order = sorted(bs, key=lambda b: H["br"][b]); newbr = [0] * len(bs)
    for r, b in enumerate(order): newbr[rb[b]] = r
    gs = sorted(g for y in keep for g in H["gate"][y]); rg = {g: i for i, g in enumerate(gs)}
    return dict(N=len(keep), lev=[H["lev"][y] for y in keep],
                opts=[[[ren[o[0]], ren[o[1]], rb[o[2]]] for o in H["opts"][y]] for y in keep],
                gate=[[rg[g] for g in H["gate"][y]] for y in keep], br=newbr, bp=[H["bp"][b] for b in bs], start=[H["start"][y] for y in keep])
def kof(G):
    try: T, sw, _ = sim244.run(G, cap=100000)
    except ValueError: return -1, 0
    return sim244.kdepth(G, sw)[0][0], T
def prune(G, K0, rng):
    changed = True
    while changed:
        changed = False
        xs = list(range(G["N"])); rng.shuffle(xs); xs.sort(key=lambda x: -G["lev"][x])
        for x in xs:
            same = [y for y in range(G["N"]) if y != x and G["lev"][y] == G["lev"][x]]
            needw = any(o[0] == x for y in range(G["N"]) for o in G["opts"][y])
            done = False
            for wrepl in (same if needw else [None]):
                for mode in ("exit", "splice"):
                    H = remove(G, x, wrepl, mode)
                    if H is not None and kof(H)[0] >= K0: G = H; done = True; break
                if done: break
            if done: changed = True; break
        if not changed:                      # cut Xi-pointers to the exit where k survives, then retry deletions once more
            cut = 0
            for y in range(G["N"]):
                for o in G["opts"][y]:
                    if o[1] >= 0:
                        old = o[1]; o[1] = -1
                        if kof(G)[0] >= K0: cut += 1
                        else: o[1] = old
            if cut: changed = True
    return G
if __name__ == "__main__":
    G = sim244.load(sys.argv[1]); rng = random.Random(int(sys.argv[3]) if len(sys.argv) > 3 else 1)
    K0, T0 = kof(G); C = prune(G, K0, rng); k, T = kof(C)
    per = {}
    for x in range(C["N"]): per[C["lev"][x]] = per.get(C["lev"][x], 0) + 1
    h = hashlib.sha1(json.dumps(C, sort_keys=True).encode()).hexdigest()
    json.dump(C, open(sys.argv[2], "w"))
    print(f"PRUNE244 {sys.argv[1].split('/')[-1]}: start N {G['N']} k {K0} T {T0} -> core N {C['N']} k {k} T {T} d {max(C['lev']) + 1} movers/level {[per.get(l, 0) for l in range(max(C['lev']) + 1)]} sha1(json sort_keys) {h}", flush=True)
