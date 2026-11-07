#!/usr/bin/env python3
"""L-RED R178 FASTCYC: fastabs (r177) without the Xi-acyclicity restriction. Xi-plays may close cycles: with sigma fixed G_X is a
functional graph, so each value is (cycle node c, path set P above c, length to c) read off the lasso, compared as si.py Engine.key:
(reward(c), signed weight of P, -len if c even else +len). Priorities: x 0, gate 1, T 2 (even self-loop), beta 4 + 2 rank + parity;
ranks by (priority, index) follow these numbers. Checked against abs177 (engine) by fastver2.py. Usage like fastabs.py."""
import sys, random, json, os
FB = os.environ.get("FB") == "1"

def build_succ(G, s):
    """functional G_X under s: nodes ('x',v), ('g',v,k), ('b',v,k), 'T'."""
    pass

def values(G, s):
    N, opts, br, bp = G["N"], G["opts"], G["br"], G["bp"]
    # node encoding: x v -> v ; gate (v,k) -> N + idx ; beta (v,k) -> N + M + idx ; T -> N + 2M
    idx = {}; M = 0
    for v in range(N):
        for k in range(len(opts[v])): idx[(v, k)] = M; M += 1
    T = N + 2 * M; nxt = [0] * (T + 1); pr = [0] * (T + 1)
    for v in range(N):
        nxt[v] = N + idx[(v, s[v])]; pr[v] = (0, 0)
        for k, (wt, xt, b) in enumerate(opts[v]):
            gi = N + idx[(v, k)]; bi = N + M + idx[(v, k)]
            nxt[gi] = bi; pr[gi] = (1, 0)
            nxt[bi] = T if xt < 0 else xt; pr[bi] = (4 + 2 * br[b] + bp[b], 1)
    nxt[T] = T; pr[T] = (2, 0)
    def val(x):
        seq = []; pos = {}; y = x
        while y not in pos: pos[y] = len(seq); seq.append(y); y = nxt[y]
        cyc = seq[pos[y]:]; c = max(cyc, key=lambda z: (pr[z][0], z))
        # path from x to c (first occurrence of c on the lasso)
        pre = seq[:seq.index(c)]
        P = [z for z in pre if (pr[z][0], z) > (pr[c][0], c)]
        w = sum((1 << (pr[z][0])) * (1 if pr[z][0] % 2 == 0 else -1) for z in P)
        rew = pr[c][0] if pr[c][0] % 2 == 0 else -pr[c][0]
        ln = len(pre)
        return (rew, w, -ln if pr[c][0] % 2 == 0 else ln)
    return val, idx, N, M

def simulate(G, cap=100000):
    N, lev, opts, gate = G["N"], G["lev"], G["opts"], G["gate"]
    order = sorted(range(N), key=lambda v: lev[v]); s = list(G["start"]); steps = 0
    while steps < cap:
        val, idx, _, M = values(G, s)
        def face(v, k): return val(N + idx[(v, k)])
        cur = [face(v, s[v]) for v in range(N)]
        avail = [[k for k in range(len(opts[v])) if k == s[v] or face(v, k) > cur[v]] for v in range(N)]
        if all(len(a) == 1 for a in avail): return steps, "opt"
        key = [None] * N; ns = list(s)
        for v in order:
            best = None
            for k in avail[v]:
                wt = opts[v][k][0]
                kk = ((gate[v][k],) if wt < 0 else key[wt] + (gate[v][k],))
                if best is None or kk < best[0]: best = (kk, k)
            key[v] = best[0]; ns[v] = best[1]
        if ns == s:
            if not FB: return steps, "stuck"
            ns = [max(avail[v], key=lambda k: (face(v, k), N + idx[(v, k)])) for v in range(N)]
        s = ns; steps += 1
    return steps, "cap"

def randG(d, deg, rng, W=2):
    N = W * d; lev = [i // W for i in range(N)]; opts = []; b = 0
    for v in range(N):
        o = []
        for k in range(deg):
            wt = -1 if lev[v] == 0 else rng.choice([u for u in range(N) if lev[u] == lev[v] - 1])
            o.append([wt, rng.choice(list(range(N)) + [-1]), b]); b += 1
        opts.append(o)
    M = b; br = list(range(M)); rng.shuffle(br); gates = list(range(N * deg)); rng.shuffle(gates)
    return dict(N=N, lev=lev, opts=opts, gate=[gates[v * deg:(v + 1) * deg] for v in range(N)], br=br,
                bp=[rng.randint(0, 1) for _ in range(M)], start=[rng.randrange(deg) for _ in range(N)], deg=deg, cyc=True)

def mutate(G, rng):
    H = json.loads(json.dumps(G)); N = H["N"]; deg = H["deg"]; r = rng.random()
    if r < 0.3:
        v = rng.randrange(N); k = rng.randrange(deg); H["opts"][v][k][1] = rng.choice(list(range(N)) + [-1])
    elif r < 0.45:
        v = rng.randrange(N); k = rng.randrange(deg)
        if H["lev"][v] > 0: H["opts"][v][k][0] = rng.choice([u for u in range(N) if H["lev"][u] == H["lev"][v] - 1])
    elif r < 0.6:
        M = len(H["br"]); a, b = rng.randrange(M), rng.randrange(M); H["br"][a], H["br"][b] = H["br"][b], H["br"][a]
    elif r < 0.7:
        H["bp"][rng.randrange(len(H["bp"]))] ^= 1
    elif r < 0.88:
        a, b = rng.randrange(N), rng.randrange(N); ka, kb = rng.randrange(deg), rng.randrange(deg)
        H["gate"][a][ka], H["gate"][b][kb] = H["gate"][b][kb], H["gate"][a][ka]
    else:
        H["start"][rng.randrange(N)] = rng.randrange(deg)
    return H

if __name__ == "__main__":
    d, deg, iters, rs, seed = (int(a) for a in sys.argv[1:6]); W = int(sys.argv[6]) if len(sys.argv) > 6 else 2
    rng = random.Random(seed); gb, gbs = None, -1
    for r in range(rs):
        G = randG(d, deg, rng, W); bs = simulate(G)[0]
        for it in range(iters):
            H = mutate(G, rng); hs = simulate(H)[0]
            if hs >= bs: G, bs = H, hs
        if bs > gbs: gb, gbs = G, bs; json.dump(gb, open(os.environ.get("OUT", "/dev/null"), "w"))
        print("RESTART", r, bs, "BEST", gbs, flush=True)
    print("FASTCYC d", d, "deg", deg, "W", W, "best", gbs)
