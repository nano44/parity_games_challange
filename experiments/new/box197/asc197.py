#!/usr/bin/env python3
"""Box 197 (L-NEW successor 65): Lemma ASC-WIT on the Gamma3 Howard run (box 196's setting, qt3_196's engine).
For every state t <= T3, vertex v, ascent (c_i, c_{i+1}) of seq_t(v): g1 := the first gate on the play after c_i.
  awA   : sigma-bar(g1) = pe_g1 (Odd takes the W-face at g1)                         [should be 0 under E-LEV]
  awB   : Lambda(pe_g1) = Lambda(v) and E(pe_g1) has no e-vertex at least as relevant as c_{i+1}   [should be 0]
  caseL : Lambda(pe_g1) != Lambda(v) (record)        caseE: Lambda equal (record)
Also per (v, maximal Lambda-interval I): D := distinct e-sets, Mact := distinct e-vertices seen, tops := the most relevant e of each change
(E_{t-1} xor E_t), Rtop := changes whose top was in an earlier set of I (a top re-entry), Rcarry := other re-entries;
  dfail : D > 1 + Mact + Rtop   [should be 0: Lemma RE-COUNT]     lexdec: a change whose top is not in the new set [should be 0: E-MON3]
  rootfail: Lemma ASC-ROOT fails (witness recursion from the first ascent does not end in a gate whose W-face has a better cycle node)
  record: maxR (re-entries in one (v, I)), maxalt (longest alternation x y x y ... of two symbols in one tops sequence), maxtops.
Controls (A197_CTRL): 1 awA faces swapped; 2 rootfail reward test reversed; 3 awB target above all of E(v); 4 dfail with Rtop := 0.
Usage: asc197.py FAMILY SEED COUNT | --files G.json ...   (ROOT defaults to the repo root from this file's place)"""
import sys, os, json, random, collections
ROOT = os.environ.get("ROOT") or os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")); os.environ.setdefault("Q196_ROOT", ROOT); os.environ.setdefault("EG195_ROOT", ROOT)
sys.path[:0] = [os.path.join(ROOT, p) for p in ("experiments/new/box196", "experiments/new/box195", "experiments/new/box191", "experiments/new/box189",
                "experiments/new/box190", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
import eg195, gamma3, n5v, n5x
CTRL = os.environ.get("A197_CTRL", "0")   # 1: awA with the faces swapped; 2: rootfail with the reward test reversed; 3: awB against a target above all of E(v) (each must fire)

def run(G, cap=20000):
    g0, _, _, V = gamma3.build(G, eg195.PADS); g = eg195.topg(g0); n = g.n; name = {v: k for k, v in V.items()}
    kind = {v: (name[v][0] if isinstance(name[v], tuple) else name[v]) for v in range(n)}
    N = G["N"]; O = [(x, k) for x in range(N) for k in range(len(G["opts"][x]))]
    E, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None)
    gate_of = {V[("g", o)]: (V[("pe", o)], V[("pbeta", o)]) for o in O}
    evs = [v for v in range(n) if kind[v] == "e"]; ES = sum(E.bit[v] for v in evs)
    c = collections.Counter(); hist = []; it = 0
    lev = lambda u: G["lev"][name[u][1][0]]
    def root(u, vs, sb, sigma, depth):          # Lemma ASC-ROOT: follow witnesses from u's FIRST ascent until case L
        path = []; seen = set(); z = u
        while z not in seen:
            seen.add(z); path.append(z); z = sigma[z] if g.owner[z] == 0 else sb[z]
        pos = [i for i, z in enumerate(path) if kind[z] == "e" and vs[u][1] & E.bit[z]]
        asc = [(a, b) for a, b in zip(pos, pos[1:]) if E.rank[path[b]] > E.rank[path[a]]]
        if not asc: c["rootfail"] += 1; return
        a, b = asc[0]; ci = path[a]
        g1 = next(z for z in path[a + 1:b + 1] if z in gate_of); pe, pb = gate_of[g1]
        if lev(g1) >= lev(ci) or sb[g1] == pe or E.key(vs[pe]) <= E.key(vs[pb]): c["rootfail"] += 1; return
        if vs[pe][0] != vs[u][0]:
            if (E.rew[vs[pe][0]] <= E.rew[vs[u][0]]) != (CTRL == "2"): c["rootfail"] += 1
            c["rootok"] += 1; c["rootdepth"] = max(c["rootdepth"], depth + 1); return
        if depth > G["N"]: c["rootfail"] += 1; return
        root(pe, vs, sb, sigma, depth + 1)
    while it < cap:
        vs, sb = E.evaluate(tuple(sigma)); hist.append(vs)
        for v in range(n):
            path = []; seen = set(); u = v
            while u not in seen:
                seen.add(u); path.append(u); u = sigma[u] if g.owner[u] == 0 else sb[u]
            pos = [i for i, u in enumerate(path) if kind[u] == "e" and vs[v][1] & E.bit[u]]
            for a, b in zip(pos, pos[1:]):
                if E.rank[path[b]] <= E.rank[path[a]]: continue
                g1 = next(u for u in path[a + 1:b + 1] if u in gate_of); pe, pb = gate_of[g1]
                if CTRL == "1": pe, pb = pb, pe
                if sb[g1] == pe: c["awA"] += 1; continue
                if vs[pe][0] != vs[v][0]: c["caseL"] += 1; continue
                c["caseE"] += 1
                tgt = max(E.rank[f] for f in evs if vs[v][1] & E.bit[f]) + 1 if CTRL == "3" else E.rank[path[b]]
                if not any(vs[pe][1] & E.bit[f] and E.rank[f] >= tgt for f in evs): c["awB"] += 1
            if len(pos) > 1 and any(E.rank[path[b]] > E.rank[path[a]] for a, b in zip(pos, pos[1:])):
                root(v, vs, sb, sigma, 0)
        res = n5v.step(g, E, Ed, sigma, tau, "xi")
        if res is None or res[4]: break
        sigma, tau = res[0], res[1]; it += 1
    T3 = len(hist) - 1; mxD = mxgap = 0; worst = None
    for v in range(n):
        t = 0
        while t <= T3:
            s = t
            while t + 1 <= T3 and hist[t + 1][v][0] == hist[s][v][0]: t += 1
            sets = {hist[u][v][1] & ES for u in range(s, t + 1)}; act = 0
            for x in sets: act |= x
            D, Ma = len(sets), bin(act).count("1")
            seen = hist[s][v][1] & ES; R = 0; Rt = 0; tops = []
            for u in range(s + 1, t + 1):
                a, b = hist[u - 1][v][1] & ES, hist[u][v][1] & ES
                if a == b: continue
                d = a ^ b; top = max((f for f in evs if d & E.bit[f]), key=lambda f: E.rank[f]); tops.append(top)
                if seen & E.bit[top]: Rt += 1
                for f in evs:
                    if (b & ~a) & E.bit[f] and seen & E.bit[f]:
                        R += 1; c["Rtop" if f == top else "Rcarry"] += 1
                if not (b & E.bit[top]): c["lexdec"] += 1
                seen |= b
            if D > 1 + Ma + (0 if CTRL == "4" else Rt): c["dfail"] += 1
            al = 0
            for x in set(tops):
                for y in set(tops):
                    if x == y: continue
                    L = 0; want = x
                    for z in tops:
                        if z == want: L += 1; want = y if want == x else x
                    al = max(al, L)
            c["maxalt"] = max(c["maxalt"], al); c["dslen"] = max(c["dslen"], len(tops))
            c["maxR"] = max(c["maxR"], R)
            mxD = max(mxD, D); mxgap = max(mxgap, D - Ma)
            if worst is None or D - Ma > worst[0]: worst = (D - Ma, D, Ma)
            t += 1
    return dict(T3=T3, mxD=mxD, mxgap=mxgap, worst=worst, **c)

def summ(name, rows):
    tot = collections.Counter()
    for r in rows:
        for k in ("awA", "awB", "caseL", "caseE", "Rtop", "Rcarry", "lexdec", "dfail", "rootfail", "rootok"): tot[k] += r.get(k, 0)
    w = max(r["worst"] for r in rows)
    print(f"{name} runs {len(rows)} " + " ".join(f"{k} {tot[k]}" for k in ("awA", "awB", "caseL", "caseE", "Rtop", "Rcarry", "lexdec", "dfail", "rootfail", "rootok")) + f" maxR {max(r.get('maxR',0) for r in rows)} maxalt {max(r.get('maxalt',0) for r in rows)} maxtops {max(r.get('dslen',0) for r in rows)} rootdepth {max(r.get('rootdepth',0) for r in rows)}" +
          f" max T3 {max(r['T3'] for r in rows)} max D {max(r['mxD'] for r in rows)} max D-Mact {w[0]} (D {w[1]}, Mact {w[2]})", flush=True)

if __name__ == "__main__":
    if sys.argv[1] == "--files":
        for fn in sys.argv[2:]:
            G = json.load(open(fn)); G = G.get("genome", G) if isinstance(G, dict) else G
            if isinstance(G, dict) and "opts" in G and "start" in G: summ(os.path.basename(fn), [run(G)])
            else: print(os.path.basename(fn), "skipped (not a genome with a start)")
    else:
        fam, seed, cnt = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed)
        summ(f"{fam} seed {seed}", [run(eg195.gen(rng, fam)) for _ in range(cnt)])
