#!/usr/bin/env python3
"""Box 207 Addendum A (L-NEW successor 71): Lemma PAID at Xi-feedback number k = 1 on IDEAL-CYC. For a feedback vertex R (fvs202; the
first in sorted order) at every state and every gate g at its e-face: g is DIRECT if R lies on the play of beta_g or of e_g; otherwise
next(g) := the gate of the first e-vertex on beta_g's play. Must-0 counters (unit (state, gate at its e-face)): nonext (not DIRECT and
beta_g's play has no e-vertex: PAID-1 fails), notK1 (not DIRECT and the cycle node of e_g's or beta_g's play is not K1), notE (next(g) not
at its e-face), lexfail (not DIRECT and E(e_g) >= E(e_next(g)) in the lex order of R121), nochain (the chain g, next(g), ... does not end
at a DIRECT gate). Descriptive: egates, direct, maxchain (longest chain). Control PAID_CTRL=1: R := the mover AFTER R in index order that
is not a feedback vertex (chains must fail on some genome).
Usage: paid207.py G.json ... | paid207.py --rand SEED COUNT"""
import sys, os, json, random, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE] + [os.path.join(HERE, "..", d) for d in ("box203", "box202", "box191")]
import gfc203, idealcyc, fvs202, rlocal207
CTRL = os.environ.get("PAID_CTRL") == "1"
def census(G, c):
    Rs = rlocal207.fvsets(G)
    if not Rs: c["nofvs"] += 1; return
    R = Rs[0]
    if CTRL: R = next((x for x in list(range(R + 1, G["N"])) + list(range(R)) if x not in Rs), R)
    H, n, E, V, gates = gfc203.hist_ideal(G); ST = idealcyc.run(G); h, s0, movers, inv = idealcyc.build(G)
    ebits = sorted(E.rank[v] for k, v in V.items() if isinstance(k, tuple) and k[0] == "e"); pos = {r: i for i, r in enumerate(ebits)}
    def es(mask):
        x = 0
        for r_ in ebits:
            if (mask >> r_) & 1: x |= 1 << pos[r_]
        return x
    e2g = {V[("e", k[1])]: V[("g", k[1])] for k in V if isinstance(k, tuple) and k[0] == "e"}
    r = V[("x", R)]; K1 = V[("K", 1)]
    for t in range(len(H)):
        s = list(s0)
        for x in range(G["N"]): s[movers[x]] = V[("g", (x, ST[t][x]))]
        f = lambda v: s[v] if h.owner[v] == 0 else H[t][1][v]
        def play(v):
            seen = []
            while v not in seen: seen.append(v); v = f(v)
            return seen
        ate = {g for g, (q, a, b) in gates.items() if H[t][1][g] == a}; nxt = {}; direct = set()
        for g in ate:
            q, a, b = gates[g]; pa, pb = play(a), play(b); c["egates"] += 1
            if r in pa or r in pb: direct.add(g); c["direct"] += 1; continue
            if H[t][0][a][0] != K1 or H[t][0][b][0] != K1: c["notK1"] += 1
            fe = next((w for w in pb if w in e2g), None)
            if fe is None: c["nonext"] += 1; continue
            hg = e2g[fe]; nxt[g] = hg
            if hg not in ate: c["notE"] += 1
            if es(H[t][0][a][1]) >= es(H[t][0][fe][1]): c["lexfail"] += 1
        for g in ate:
            k, cur, seen = 0, g, set()
            while cur not in direct and cur in nxt and cur not in seen: seen.add(cur); cur = nxt[cur]; k += 1
            if cur not in direct: c["nochain"] += 1
            c["maxchain"] = max(c["maxchain"], k)
KEYS = ("egates", "direct", "maxchain", "nonext", "notK1", "notE", "lexfail", "nochain")
if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--rand":
        os.environ["K1_MODE"] = "1"; import k1srch202
        rng = random.Random(int(a[1])); g = 0; c = collections.Counter()
        while g < int(a[2]):
            G = k1srch202.mk(rng)
            if G is None or fvs202.kfvs(G)[0] != 1: continue
            g += 1; census(G, c)
        print("rand k1 seed", a[1], "genomes", g, " ".join("%s %d" % (k, c[k]) for k in KEYS), flush=True)
    else:
        for f in a:
            c = collections.Counter(); census(json.load(open(f)), c); print(os.path.basename(f), " ".join("%s %d" % (k, c[k]) for k in KEYS), flush=True)
