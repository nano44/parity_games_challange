#!/usr/bin/env python3
"""L-SI box 75 (packet P-IDEAL-IM): DATA checks, each with a negative control, on random ISO genomes of L^R_(m+1) (R110's definition)
and on the lane's real m 3 pins. Own implementation of R110's c-step from its text (A-sets under the old state; keys under the new state,
lowest level first; a level-1 option W-pointing to mover w keyed (kappa^c_w, its gate), kappa^c_0 = 1 - c, kappa^c_1 = c; levels >= 2:
key of the W-target's new option, then the own gate), cross-checked against box 64 flipdp.Ext.step (XSIM-checked against L-NEW's Gen).
Items: IM (§1), BIT-CHAIN and KEY-DIR (§2), VALUE-MONO (§3), FRAME-MAP (§5: the extracted frame system satisfies the frame's clause
groups and its BIT-CHAIN step equals the c-step on every state). Usage: imcheck.py [NG] [seed]   (exit 1 on any violation)"""
import sys, os, random, itertools, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box64")); from flipdp import Ext
NG = int(sys.argv[1]) if len(sys.argv) > 1 else 200; rng = random.Random(int(sys.argv[2]) if len(sys.argv) > 2 else 75)
def gen(m):
    N = 2 * (m + 1); lev = [v // 2 for v in range(N)]; up = list(range(2, N)); order = up[:]; rng.shuffle(order); pos = {z: i for i, z in enumerate(order)}
    opts = []
    for x in range(N):
        o = []
        for k in range(2):
            wt = 2 * (lev[x] - 1) + k if lev[x] > 0 else -1
            later = [y for y in up if pos.get(x, -1) < pos[y]] if x >= 2 else []
            xt = rng.choice([-1] + later) if later and rng.random() < 0.75 else -1
            o.append([wt, xt, 2 * x + k])
        opts.append(o)
    br = list(range(2 * N)); rng.shuffle(br); g = list(range(2 * N)); rng.shuffle(g)
    return {"N": N, "lev": lev, "opts": opts, "gate": [[g[2 * x], g[2 * x + 1]] for x in range(N)], "br": br, "bp": [rng.randint(0, 1) for _ in range(2 * N)], "start": [0] * N}
class Cs:
    def __init__(s, G):
        s.G = G; s.N = G["N"]; s.lev = G["lev"]; s.m = max(s.lev); s.UP = list(range(2, s.N))
    def eps(s, x, k): o = 2 * x + k; return (1 if s.G["bp"][o] == 0 else -1) << s.G["br"][o]
    def val(s, st, x, k):                       # R105 ENC: integer value of option (x, k) under st
        t = s.G["opts"][x][k][1]; return s.eps(x, k) + (0 if t < 0 else s.val(st, t, st[t]))
    def chain(s, st, x, k):
        out, t = [], s.G["opts"][x][k][1]
        while t >= 0: out.append(t); t = s.G["opts"][t][st[t]][1]
        return out
    def C(s, st, x): return int(s.val(st, x, 1) > s.val(st, x, 0))   # the strictly better option (values of the two options differ)
    def cstep(s, st, c):
        ns = list(st); key = {}
        for l in range(1, s.m + 1):
            for x in (2 * l, 2 * l + 1):
                A = [st[x]] + [1 - st[x]] * (s.val(st, x, 1 - st[x]) > s.val(st, x, st[x]))
                def kf(k):
                    w = s.G["opts"][x][k][0]; g = s.G["gate"][x][k]
                    return ((1 - c if w == 0 else c), g) if l == 1 else key[w] + (g,)
                k = min(A, key=kf); ns[x] = k; key[x] = kf(k)
        return ns
    def bits(s, st, c):                         # BIT-CHAIN bits b_0 := c, b_l from the level-l states of st (l = 1..m)
        b = [c]
        for l in range(1, s.m + 1):
            a, bb = st[2 * l], st[2 * l + 1]
            b.append(b[-1] if (a, bb) == (0, 1) else (1 - b[-1] if (a, bb) == (1, 0) else int(s.G["gate"][2 * l][a] < s.G["gate"][2 * l + 1][a])))
        return b
    def keytuple(s, st, x, c):                  # R110 c-step key of x's current option under st
        l = s.lev[x]; w = s.G["opts"][x][st[x]][0]; g = s.G["gate"][x][st[x]]
        return ((1 - c if w == 0 else c), g) if l == 1 else s.keytuple(st, w, c) + (g,)
bad = {k: 0 for k in ["IM", "BITCHAIN", "KEYDIR", "MONO", "FRAME_LOCAL", "FRAME_OWN", "FRAME_STEP", "XSTEP"]}
neg = {k: 0 for k in ["IM", "BITCHAIN", "KEYDIR", "MONO", "FRAME_STEP"]}
cnt = {k: 0 for k in bad}
gens = [gen(rng.choice([1, 2, 3])) for _ in range(NG)]
for p in ["../box74/out/fl7_m3_s2.json", "../box74/out/fl10_K2_m3_s1.json", "../box73/out/pq_4_6_m3_s1.json", "../box72/out/sum2_18_m3_s1.json"]:
    gens.append(json.load(open(os.path.join(HERE, p))))
for G in gens:
    S = Cs(G); m = S.m; U = S.UP
    try: E = Ext(G)
    except AssertionError: E = None
    for up in itertools.product((0, 1), repeat=len(U)):
        st = [0, 0] + list(up)
        for c in (0, 1):
            ns = S.cstep(st, c)
            if E is not None:                    # cross-check with flipdp (level 0 forced to a configuration q with b_0(q) = c)
                cnt["XSTEP"] += 1; bad["XSTEP"] += tuple(ns[2:]) != E.step(tuple(up), c)
            # VALUE-MONO: no value falls, a moved mover's value rises; negative control: the step reversed
            for x in U:
                cnt["MONO"] += 1; d = S.val(ns, x, ns[x]) - S.val(st, x, st[x])
                bad["MONO"] += d < 0 or (ns[x] != st[x] and d <= 0)
                neg["MONO"] += (ns[x] != st[x]) and not (d < 0)          # reversed claim «a moved mover's value falls» fails
            # BIT-CHAIN: b_l = [key(A_l) < key(B_l)] under ns; KEY-DIR: a level-l mover moves iff st(x) = b_(l-1)(ns) and C_x(st) != b_(l-1)
            b = S.bits(ns, c)
            for l in range(1, m + 1):
                cnt["BITCHAIN"] += 1; kb = int(S.keytuple(ns, 2 * l, c) < S.keytuple(ns, 2 * l + 1, c))
                bad["BITCHAIN"] += b[l] != kb; neg["BITCHAIN"] += (1 - b[l]) != kb
                for x in (2 * l, 2 * l + 1):
                    cnt["KEYDIR"] += 1; mv = ns[x] != st[x]; pred = st[x] == b[l - 1] and S.C(st, x) != b[l - 1]
                    bad["KEYDIR"] += mv != pred; neg["KEYDIR"] += mv != (st[x] != b[l - 1] and S.C(st, x) != b[l - 1])
            if c == 1: continue
            for z in U:
                # FRAME: C_z independent of s_z (FRAME_OWN); LOCAL; IM (Lemma IM); negative control for IM: the direction reversed
                cnt["FRAME_OWN"] += 1; s2 = list(st); s2[z] ^= 1; bad["FRAME_OWN"] += S.C(st, z) != S.C(s2, z)
                ch = [set(S.chain(st, z, k)) for k in (0, 1)]
                for y in U:
                    if y == z: continue
                    s2 = list(st); s2[y] ^= 1; a, b2 = S.C(st, z), S.C(s2, z)
                    if y not in ch[0] and y not in ch[1]: cnt["FRAME_LOCAL"] += 1; bad["FRAME_LOCAL"] += a != b2; continue
                    if S.C(st, y) == st[y]: continue     # y happy: IM says nothing
                    cnt["IM"] += 1
                    if y in ch[0] and y in ch[1]: bad["IM"] += a != b2
                    else:
                        k = 0 if y in ch[0] else 1; bad["IM"] += b2 not in (a, k); neg["IM"] += b2 not in (a, 1 - k)
            # FRAME_STEP: frame.py's step (C from st; key-preferred index 0 iff bit = 1; bits from the NEW level-l states) = c-step
            for c2 in (0, 1):
                fs = list(st); bit = c2
                for l in range(1, m + 1):
                    for x in (2 * l, 2 * l + 1):
                        cz = S.C(st, x)
                        if cz != st[x] and cz == 1 - bit: fs[x] ^= 1
                    if l < m:
                        a, b3 = fs[2 * l], fs[2 * l + 1]
                        bit = (1 - bit if a else bit) if a != b3 else int(G["gate"][2 * l][a] < G["gate"][2 * l + 1][a])
                cnt["FRAME_STEP"] += 1; real = S.cstep(st, c2); bad["FRAME_STEP"] += fs != real
                neg["FRAME_STEP"] += fs != S.cstep(st, 1 - c2)        # the bit matters
print("genomes", len(gens), "checks", cnt); print("violations", bad); print("negative controls fired", neg)
ok = all(v == 0 for v in bad.values()) and all(neg[k] > 0 for k in neg)
print("PASS" if ok else "FAIL"); sys.exit(0 if ok else 1)
