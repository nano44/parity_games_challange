#!/usr/bin/env python3
"""L-RED R212 Lemma FROZEN-EMBED, machine check. For an ISO genome G of L^R_(m+1) (fk text or JSON) and a level-0 bit b:
 Lad(G, b) := drop movers 0, 1; shift every level down by one; the four options of the old level-1 movers keep their Xi-target and
 beta, lose their W-target, and get the gates of old level 1 re-assigned in the order of (kappa, gate), kappa = 0 for the option
 W-pointing to the level-0 mover with the smaller key under q_b. Claim: Lad(G, b) is in L^R_m and its run from every state equals the
 b-step sequence of G (flipdp Ext.step, levels >= 1). Check: every state, both b, full runs compared state by state with r187/ideal.py.
 Usage: embed.py genome ... [--rand cnt m seed]   |   embed.py --out genome.txt b out.json  (writes Lad(G, b))
 NEG=1: negative control, the gates of old level 1 are kept unchanged (mismatches expected)."""
import sys, os, json, itertools, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r187")]
import conv, ideal, flipdp_lsi as fd
def lad(G, b):
    E = fd.Ext(G); q = E.q[b]; small = 0 if G["gate"][0][q[0]] < G["gate"][1][q[1]] else 1
    N = G["N"]; n = N - 2; lev = [G["lev"][v + 2] - 1 for v in range(n)]
    opts = []
    for v in range(n):
        o = []
        for k, (wt, xt, bi) in enumerate(G["opts"][v + 2]):
            o.append([wt - 2 if lev[v] > 0 else -1, xt - 2 if xt >= 0 else -1, bi])
        opts.append(o)
    gate = [list(G["gate"][v + 2]) for v in range(n)]
    four = [(0 if G["opts"][x][k][0] == small else 1, G["gate"][x][k], x - 2, k) for x in (2, 3) for k in (0, 1)]
    vals = sorted(G["gate"][x][k] for x in (2, 3) for k in (0, 1))
    if os.environ.get("NEG") != "1":
        for r, (_, _, v, k) in enumerate(sorted(four)): gate[v][k] = vals[r]
    # renumber (order-preserving) the betas used and the gates to 0..2n-1 (lemck needs gates 0..M-1)
    used = sorted({o[2] for v in range(n) for o in opts[v]}, key=lambda i: G["br"][i]); rid = {i: r for r, i in enumerate(sorted({o[2] for v in range(n) for o in opts[v]}))}
    br = [0] * len(rid); bp = [0] * len(rid)
    for r, i in enumerate(used): br[rid[i]] = r; bp[rid[i]] = G["bp"][i]
    opts = [[[o[0], o[1], rid[o[2]]] for o in opts[v]] for v in range(n)]
    gs = sorted(gate[v][k] for v in range(n) for k in range(2)); gid = {x: r for r, x in enumerate(gs)}
    gate = [[gid[gate[v][k]] for k in range(2)] for v in range(n)]
    return {"N": n, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": bp, "start": [0] * n}
def check(G):
    E = fd.Ext(G); bad = 0; tot = 0
    for b in (0, 1):
        L = lad(G, b)
        assert all(L["lev"][v] == v // 2 for v in range(L["N"])) and all(L["opts"][v][k][0] == (2 * (L["lev"][v] - 1) + k if L["lev"][v] else -1) for v in range(L["N"]) for k in range(2)), "not R197"
        for u in itertools.product(range(2), repeat=L["N"]):
            L["start"] = list(u); S, why = ideal.traj(L)
            seq = [u]; cur = u
            while True:
                w = E.step(cur, b)
                if w == cur: break
                seq.append(w); cur = w
            tot += 1
            if [tuple(s) for s in S] != seq: bad += 1
    return bad, tot
if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--out":
        G = conv.read_txt(a[1]) if a[1].endswith(".txt") else json.load(open(a[1])); json.dump(lad(G, int(a[2])), open(a[3], "w")); sys.exit(0)
    gens = []
    if a and a[0] == "--rand":
        cnt, m, seed = map(int, a[1:4]); rng = random.Random(seed); N = 2 * (m + 1); M = 2 * N
        for _ in range(cnt):
            order = list(range(2, N)); rng.shuffle(order); pos = {v: i for i, v in enumerate(order)}
            opts = []
            for x in range(N):
                o = []
                for k in range(2):
                    later = [w for w in order if x >= 2 and pos[w] > pos[x]]
                    xt = rng.choice(later + [-1, -1]) if later else -1
                    o.append([2 * (x // 2 - 1) + k if x >= 2 else -1, xt, 2 * x + k])
                opts.append(o)
            while True:
                g = list(range(M)); rng.shuffle(g)
                if len({int(g[i] < g[2 + j]) for i in range(2) for j in range(2)}) == 2: break
            br = list(range(M)); rng.shuffle(br)
            gens.append(("rand", {"N": N, "lev": [v // 2 for v in range(N)], "opts": opts, "gate": [[g[2 * x], g[2 * x + 1]] for x in range(N)],
                                   "br": br, "bp": [rng.randint(0, 1) for _ in range(M)], "start": [0] * N}))
    else:
        for p in a: gens.append((p, conv.read_txt(p) if p.endswith(".txt") else json.load(open(p))))
    B = T = 0
    for name, G in gens:
        b, t = check(G); B += b; T += t
        if a and a[0] != "--rand": print(os.path.basename(name), "runs", t, "mismatches", b)
    print("FROZEN-EMBED genomes", len(gens), "runs compared", T, "mismatches", B); sys.exit(1 if B else 0)
