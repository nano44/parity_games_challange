#!/usr/bin/env python3
"""L-RED 68 R240: adversary against FLAT-IDX (L-RED-B 3, B3 §3, «L-RED-B reading, NOT PROVED»; as stated in the Lead's brief 2026-11-13
02:19Z; the file claude/l-red-b 9bce72fa docs/red-b/B3-guide.md was NOT on origin when this was written): «on W(H, s0) (wrap104), before
N5's first fallback and while τ is standard at the gates, σ_(j+1)(v) is the least-position option of {σ_j(v)} ∪ Iσ_j(v) for every Even
vertex v of H; so positions never increase, and at most |E(H)| iterations move H.»
POSITION of the pad m_(v,w) := the index of w in H.succ[v] (wrap104 creates the pads, gates and pe's of v in that order).
W(H, s0) is box 104's wrap104.wrap (objects only, via w237 / wr237). W's DEFINITION (box 104 §3) fixes only «the new vertices are
indexed after V»; their order among themselves is a choice of wrap104. PERM (env) renumbers the new vertices and nothing else (owners,
priorities and edges kept, so the game is W(H, s0) as defined): none (wrap104's numbering), all (a random permutation of all new
vertices), pe / g / m (a random permutation of the Even-edge pe's / gates / pads among their own index slots), rev (all new vertices in
reverse order).
N5: n5s237 mode spec (SPEC-exact, L-RED 67) from S3; second engine box 190 n5v spec (state by state up to the first fallback F).
Counters (unit (transition before F, Even vertex v of H) unless said):
 notmin   σ_(j+1)(v) is not the least-position element of A_j(v) = {σ_j(v)} ∪ {pads strictly Ξσ-better}        [FLAT-IDX]
 idxinc   the position of σ_(j+1)(v) is larger than that of σ_j(v)                                          [«positions never increase»]
 hbound   (unit games) the number of transitions before F that move some vertex of H exceeds |E(H)|          [the bound]
 taunstd  (unit states 0..F-1) τ differs from the standard τ0 at some gate or o ∈ V_O                         [the proviso]
 keymin   σ_(j+1)(v) is not the element of A_j(v) whose pad has the least ROOT-FIRST KEY (index of its pe, then gate, then pad)
          (WRAP Remark (3) / R104 [RULE]: the numbering-independent form)
 notA     σ_(j+1)(v) ∉ A_j(v) (WRAP (v))
CTRL=1: N5′-xi (mode xi) instead of N5: notmin must fire. Usage: flat240.py FAMILY ARGS...   (aim237 families, plus «par K SEED NMAX»:
H with groups of Even vertices sharing ONE successor set and one priority; env PERM, XEVERY (default 10))"""
import sys, os, random, hashlib, json, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [os.path.join(HERE, "..", "r237"), os.path.join(HERE, "..", "r236")]
import aim237, n5s237 as S, pg
R = aim237.R
PERM = os.environ.get("PERM", "none"); CTRL = os.environ.get("CTRL") == "1"; XEVERY = int(os.environ.get("XEVERY", "10"))
KEYS = ("notmin", "idxinc", "hbound", "taunstd", "keymin", "notA")

def par(K, seed, nmax):
    rng = random.Random(seed)
    for i in range(K):
        n = rng.randint(3, nmax); prio = [rng.randint(0, n) for _ in range(n)]; owner = [rng.randint(0, 1) for _ in range(n)]; succ = [None] * n
        for grp in range(rng.randint(1, 3)):
            S_ = sorted(rng.sample(range(n), rng.randint(2, min(n, 4)))); p = rng.randint(0, n)
            for v in rng.sample(range(n), rng.randint(2, n)):
                if succ[v] is None: succ[v] = list(S_); owner[v] = 0; prio[v] = p
        for v in range(n):
            if succ[v] is None: succ[v] = sorted(rng.sample(range(n), rng.randint(1, min(n, 3))))
        H = pg.Game(prio, owner, succ); yield H, [rng.choice(H.succ[v]) if owner[v] == 0 else -1 for v in range(n)]

def relabel(H, g, std_t, mp, rng):
    n, N = H.n, g.n; new = list(range(n, N)); pi = list(range(N))
    gates = {}; pes = {}
    for (v, w), m in mp.items(): gt = g.succ[m][0]; gates[(v, w)] = gt; pes[(v, w)] = std_t[gt]
    def perm_slots(vs):
        sl = sorted(vs); sh = list(sl); rng.shuffle(sh)
        for a, b in zip(sl, sh): pi[a] = b
    if PERM == "all": sh = list(new); rng.shuffle(sh); [pi.__setitem__(a, b) for a, b in zip(new, sh)]
    elif PERM == "rev": [pi.__setitem__(a, b) for a, b in zip(new, reversed(new))]
    elif PERM == "pe": perm_slots(pes.values())
    elif PERM == "g": perm_slots(gates.values())
    elif PERM == "m": perm_slots(mp.values())
    prio = [0] * N; owner = [0] * N; succ = [None] * N
    for v in range(N): prio[pi[v]] = g.prio[v]; owner[pi[v]] = g.owner[v]; succ[pi[v]] = sorted(pi[w] for w in g.succ[v])
    return pi, prio, owner, succ, {k: pi[x] for k, x in mp.items()}, {k: pi[x] for k, x in gates.items()}, {k: pi[x] for k, x in pes.items()}, {pi[a]: pi[b] for a, b in std_t.items()}

def one(H, s0, rng, second=False):
    g, std_s, std_t, mp, inv = R.WR.wrap(H, s0); pi, prio, owner, succ, mp2, gt2, pe2, st2 = relabel(H, g, std_t, mp, rng)
    N = len(prio); order = sorted(range(N), key=lambda v: (prio[v], v)); rk = [0] * N
    for r, v in enumerate(order): rk[v] = r
    ev = [p % 2 == 0 for p in prio]; O = S.Ord(rk, ev); isE = [o == 0 for o in owner]; isO = [o == 1 for o in owner]
    tr = []; fbt = []; its, fbs, _, _, _ = S.run(prio, owner, succ, "xi" if CTRL else "spec", trace=tr, fbtrace=fbt); F = fbt[0] if fbt else len(tr)
    pos = {m: H.succ[v].index(w) for (v, w), m in mp2.items()}; key = {m: (pe2[k], gt2[k], m) for k, m in mp2.items()}
    vE = [v for v in range(H.n) if H.owner[v] == 0]; c = {k: 0 for k in KEYS}; moves = 0; Eh = sum(len(s) for s in H.succ)
    for t in range(min(F, len(tr))):
        sg, tu = tr[t]; c["taunstd"] += int(any(tu[a] != b for a, b in st2.items()))
        if t + 1 < min(F, len(tr)):
            sg2 = tr[t + 1][0]; vs, _ = S.vjproc(N, rk, ev, [[sg[v]] if isE[v] else succ[v] for v in range(N)], isO); mv = False
            for v in vE:
                A = [m for m in succ[v] if m == sg[v] or O.better(vs[m], vs[sg[v]])]; nw = sg2[v]; mv |= nw != sg[v]
                c["notA"] += int(nw not in A); c["notmin"] += int(nw != min(A, key=lambda m: pos[m])); c["idxinc"] += int(pos[nw] > pos[sg[v]])
                c["keymin"] += int(nw != min(A, key=lambda m: key[m]))
            moves += mv
    c["hbound"] = int(moves > Eh)
    xd = xcheck(prio, owner, succ, tr, F) if second else None
    return c, F, moves, Eh, N, xd, (prio, owner, succ, tr)

def xcheck(prio, owner, succ, tr, F):
    N = len(prio)
    if True:
        LNEW = os.environ["LNEW"]
        sys.path[:0] = [os.path.join(LNEW, p) for p in ("experiments/new/box190", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
        import n5v, n5x, n5
        from si import Engine
        g2 = pg.parse(f"parity {N - 1};\n" + "".join(f"{v} {prio[v]} {owner[v]} {','.join(map(str, succ[v]))};\n" for v in range(N)))
        E, Ed = Engine(g2), Engine(n5.dual(g2)); sigma, tau = n5x.start_pair(g2, E, Ed, None); xd = 0
        for t in range(min(F, len(tr))):
            xd |= int(any(sigma[v] != w for v, w in tr[t][0].items()))
            r = n5v.step(g2, E, Ed, sigma, tau, "xi" if CTRL else "spec")
            if r is None: break
            sigma, tau = r[0], r[1]
    return xd

if __name__ == "__main__":
    t0 = time.time(); fam = sys.argv[1:]; rng = random.Random(240 + sum(map(ord, PERM)))
    gen = par(*map(int, fam[1:4])) if fam[0] == "par" else aim237.family(fam)
    tot = {k: 0 for k in KEYS}; games = 0; maxF = 0; maxmv = 0; x = xd = 0; ex = []; os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
    for i, (H, s0) in enumerate(gen):
        c, F, mv, Eh, N, d, game = one(H, s0, rng, second=(XEVERY and i % XEVERY == 0))
        games += 1; maxF = max(maxF, F); maxmv = max(maxmv, mv)
        for k in KEYS: tot[k] += c[k]
        if d is not None: x += 1; xd += d
        if (c["notmin"] or c["idxinc"]) and len(ex) < 2 and not CTRL:
            prio, owner, succ, tr = game; txt = f"parity {N - 1};\n" + "".join(f"{v} {prio[v]} {owner[v]} {','.join(map(str, succ[v]))};\n" for v in range(N))
            fn = os.path.join(HERE, "out", f"inst_{PERM}_{fam[0]}_{i}.pg"); open(fn, "w").write(txt)
            ex.append((i, {k: v for k, v in c.items() if v}, f"F {F}", os.path.basename(fn), hashlib.sha1(txt.encode()).hexdigest(), "n5v xdiff", xcheck(prio, owner, succ, tr, F)))
    print(f"FLAT240 {' '.join(fam)} PERM {PERM}" + (" CTRL 1 (N5'-xi)" if CTRL else "") + f": games {games} | " + " ".join(f"{k} {tot[k]}" for k in KEYS)
          + f" | max F {maxF} max H-moving transitions {maxmv} | second engine (n5v) sampled {x} xdiff {xd} | {time.time() - t0:.0f} s" + (f" | first: {ex}" if ex else ""), flush=True)
