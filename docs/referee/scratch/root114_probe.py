#!/usr/bin/env python3
"""REFEREE successor 21: own control for packet P-N5-ROOT (L-NEW box 114, l-new ed2fdaf2, sha1 f06f493e). Own engine rl_engine (beta and
descents as in stair_probe.py); no lane code. Per W-run F = [p, q]:
  DR    Lemma DESC-ROOT: from every descent (v, k) walk x_(i+1) := s_(k+1)(x_i) to the least j with x_j in C or switched in [k', k];
        x_j not in C, (x_j, k) is a descent with previous change k', of type R/T/S; j = 0 if (v, k) is R/T/S. Counts R, T, S, COPIED, TS.
  RS    ROOT-STAIR bound;  ON  Lemma ORIGIN-NEW (origin root change with k-1 in F enters by an edge outside H_(k-1));
  NF    Lemma NEW-FUEL (switch to z with k-1 in F and (y, z) not in H_(k-1) => Xi_(k-1)(z) != Xi_k(z)); ROLD counts R-descents by old edges.
MUT 1: NEW-FUEL for every switch (old set {sigma_k(y)} instead of H_(k-1)); must bite. MUT 2: DESC-ROOT walk stopping only at a vertex
switched at k (drops T/S); must bite where T- or S-descents occur. MUT 3: DEAD (a) «every R-descent enters by a new edge»; bites iff ROLD > 0.
Usage: root114_probe.py FILES... | rand N lo hi seed   (env MUT, MAXN)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE
import stair_probe as SP
MUT = int(os.environ.get("MUT", "0"))
EX = []


def fail(cnt, tag, *a):
    cnt[tag + "_V"] += 1
    if len(EX) < 30: EX.append((tag,) + a)


def analyse(cnt, g, start, name):
    st = RE.run(g, start); n = g.n; T = len(st) - 1
    Ev = [v for v in range(n) if g.owner[v] == 0]
    Xi = [s["Xi"] for s in st]
    W = [[RE.play_value(g, SP.nxs(g, s["s"], s["t"]), v) for v in range(n)] for s in st]
    runs, a = [], 0
    for k in range(T):
        if st[k]["t"] != st[k + 1]["t"] or st[k]["fb"] or [x[0] for x in W[k]] != [x[0] for x in W[k + 1]]: runs.append((a, k)); a = k + 1
    runs.append((a, T))
    for (p, q) in runs:
        if q == p: continue
        cnt["wruns"] += 1; F = q - p; cnt["trans"] += F
        tau = st[p]["t"]; C = {v for v in range(n) if W[p][v][0] == v}
        B = [[SP.beta(g, W[k][v]) for v in range(n)] for k in range(p, q + 1)]
        sw = [{y for y in Ev if st[k]["s"][y] != st[k + 1]["s"][y]} for k in range(p, q)]
        succ = lambda k, v: st[k]["s"][v] if g.owner[v] == 0 else tau[v]
        H = lambda k, y: {st[k]["s"][y]} | {w for (x, w) in st[k]["Is"] if x == y}
        last = {}; desc = {}; WCT = 0; TS = 0
        for i in range(F):
            k = p + i
            ch = [v for v in range(n) if W[k][v] != W[k + 1][v]]
            if ch: WCT += 1
            TS += sum(1 for y in sw[i] if W[k][y] == W[k + 1][y])
            for v in ch:
                j = SP.lcp(B[i][v], B[i + 1][v])
                if v in last and j > last[v][1]: desc[(v, k)] = last[v][0]
                last[v] = (k, j)
            # root changes
            for y in sw[i]:
                if W[k][y] == W[k + 1][y]: continue
                z = st[k + 1]["s"][y]
                if k - 1 >= p:
                    old = z in H(k - 1, y)
                    if W[k][z] == W[k + 1][z]:
                        cnt["ON_chk"] += 1
                        if old: fail(cnt, "ON", name, k, y, z)
            for y in sw[i]:
                z = st[k + 1]["s"][y]
                if k - 1 >= p and (z not in H(k - 1, y) if MUT != 1 else True):
                    cnt["NF_chk"] += 1
                    if Xi[k - 1][z] == Xi[k][z]: fail(cnt, "NF", name, k, y, z)
        typ = Counter()
        def ttype(x, k, k0):
            if x in sw[k - p]: return "R"
            if any(x in sw[t - p] for t in range(k0 + 1, k)): return "T"
            if x in sw[k0 - p]: return "S"
            return "COPIED"
        R_old = 0
        for (v, k), k0 in desc.items():
            tv = ttype(v, k, k0); typ[tv] += 1
            x, path = v, [v]
            while True:
                if x in C or (any(x in sw[t - p] for t in range(k0, k + 1)) if MUT != 2 else x in sw[k - p]): break
                x = succ(k + 1, x); path.append(x)
                if len(path) > n + 1: break
            cnt["DR_chk"] += 1
            if x in C or desc.get((x, k)) != k0 or ttype(x, k, k0) == "COPIED": fail(cnt, "DR", name, v, k, x)
            if tv != "COPIED" and x != v: fail(cnt, "DR0", name, v, k)
            if tv == "R" and st[k + 1]["s"][v] in H(k - 1, v):
                R_old += 1
                if MUT == 3: fail(cnt, "OLDEDGE", name, v, k)
        for t_ in ("R", "T", "S", "COPIED"): cnt["D" + t_] += typ[t_]
        cnt["TS"] += TS; cnt["ROLD"] += R_old
        if typ["T"] > TS: fail(cnt, "TTS", name, p)
        if sum(typ.values()) > n * (typ["R"] + typ["T"] + typ["S"]): fail(cnt, "DRN", name, p)
        if F > (F - WCT) + n * (3 * n + 1) + (3 * n + 1) * n * (typ["R"] + typ["S"] + TS): fail(cnt, "RS", name, p)


def main(a):
    import core_probe as CP
    cnt = Counter()
    def do(g, name, extra=None):
        try: analyse(cnt, g, extra, name)
        except RuntimeError: cnt["maxit"] += 1
    if a and a[0] == "rand":
        import dual_probe as D
        N, lo, hi, seed = map(int, a[1:5]); r2 = random.Random(seed)
        for i in range(N):
            nn = r2.randint(lo, hi)
            cnt["GAMES"] += 1; do(D.rand_ck(r2, nn, r2.randint(0, min(5, nn - 1))), "rand%d" % i)
    else:
        for p in a:
            if p.endswith(".start"): continue
            try: g = RE.parse(p)
            except Exception: cnt["parse_err"] += 1; continue
            if g.n > int(os.environ.get("MAXN", "100")): cnt["skip_big"] += 1; continue
            sp = p[:-3] + ".start"; ex = None
            if os.path.exists(sp):
                try: ex = CP.parse_start(g, sp)
                except Exception: cnt["start_err"] += 1
            cnt["GAMES"] += 1; do(g, os.path.basename(p), ex)
    for k in sorted(cnt): print(k, cnt[k])
    print("VIOLATIONS", sum(v for k, v in cnt.items() if k.endswith("_V")))
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
