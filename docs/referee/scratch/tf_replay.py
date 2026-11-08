#!/usr/bin/env python3
"""REFEREE successor 27: P-TOWER-FUEL replays on the referee's own IDEAL simulator t3r_sim.py (written by successor 24 from R104's
text; no L-LOWER code imported). Values for D / theta via ENC integers; preferences pi via t3r_sim.better (the set rule of R104),
so Lemma 4 (a) and Lemma 5 (i) test ENC against R104's comparison, not against themselves.
Usage: tf_replay.py corpus FILE...   (lemma counters)     tf_replay.py inst G7.txt SL41.txt   (the §4 instance counts)"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import t3r_sim as S

def load(f):
    if f.endswith(".json"):
        return json.load(open(f))
    B = {}
    for ln in open(f):
        w = ln.split()
        if w and w[0] == "d": B["d"] = int(w[1])
        elif w and w[0] in ("xt", "br", "bp", "gate", "start"): B[w[0]] = list(map(int, w[1:]))
    d = B["d"]; N = 2 * d
    opts = [[[2 * (x // 2 - 1) + k if x >= 2 else -1, B["xt"][2 * x + k], 2 * x + k] for k in (0, 1)] for x in range(N)]
    return dict(N=N, lev=[x // 2 for x in range(N)], opts=opts, gate=[[B["gate"][2 * x], B["gate"][2 * x + 1]] for x in range(N)],
                br=B["br"], bp=B["bp"], start=B["start"])

class R:
    def __init__(s, G):
        s.G = G; s.N = G["N"]; s.d = s.N // 2; s.S = S.run(G); s.T = len(s.S) - 1
        s.K = [[S.key(G, st, x, st[x], {}) for x in range(s.N)] for st in s.S]
        s.O = [[0 if K[2 * l] < K[2 * l + 1] else 1 for l in range(s.d)] for K in s.K]
        s.F = [sum(s.O[t][l] != s.O[t - 1][l] for t in range(1, s.T + 1)) for l in range(s.d)]
        s.dbl = [l >= 1 and s.F[l] == 2 * s.F[l - 1] + 2 for l in range(s.d)]
        s.mv = lambda t, x: s.S[t][x] != s.S[t - 1][x]
    def c(s, t, l): return s.O[t][l - 1]
    def wins(s, j):
        b = [t for t in range(2, s.T + 1) if s.O[t][j - 1] != s.O[t - 1][j - 1]]; cuts = [1] + b + [s.T + 1]
        return [(a, e - 1, [(t, x) for t in range(a, e) for x in (2 * j, 2 * j + 1) if s.mv(t, x)]) for a, e in zip(cuts, cuts[1:])]
    def chain(s, st, x, k):
        out = []
        while True:
            w, xt, m = s.G["opts"][x][k]; out.append(m)
            if xt < 0: return out
            x, k = xt, st[xt]
    def eps(s, m): return (1 if s.G["bp"][m] == 0 else -1) << s.G["br"][m]
    def cv(s, st, z): return sum(s.eps(m) for m in s.chain(st, z, st[z]))
    def dec(s, st, x):
        a, b = set(s.chain(st, x, 0)), set(s.chain(st, x, 1)); m = max(a ^ b, key=lambda m: s.G["br"][m]); return m, (0 if m in a else 1)
    def pi(s, st, x):  # option of larger value by R104's set rule (t3r_sim.better)
        return 0 if S.better(s.G, S.value(s.G, st, x, 0), S.value(s.G, st, x, 1)) else 1
    def strictly_better_other(s, st, x):
        return S.better(s.G, S.value(s.G, st, x, 1 - st[x]), S.value(s.G, st, x, st[x]))

def kabove(r, j):
    k = 0
    while j + k + 1 < r.d and r.dbl[j + k + 1]: k += 1
    return k

def corpus(files):
    C = {}
    inc = lambda key, v=1: C.__setitem__(key, C.get(key, 0) + int(v))
    for f in files:
        G = load(f); r = R(G); assert S.in_LR(G), f
        inc("runs"); N, d, T = r.N, r.d, r.T
        for t in range(1, T + 1):  # MOVE (both directions) at every level >= 1; DF (a) as a function of dec at every state
            for x in range(2, N):
                l = x // 2; pred = r.strictly_better_other(r.S[t - 1], x) and r.c(t, l) != r.S[t - 1][x]
                inc("MOVE_units"); inc("MOVE_viol", pred != r.mv(t, x) or (r.mv(t, x) and r.S[t][x] != r.c(t, l)))
        for t in range(T + 1):
            for x in range(N):
                m, k = r.dec(r.S[t], x); want = k if G["bp"][m] == 0 else 1 - k
                inc("DFa_units"); inc("DFa_viol", want != r.pi(r.S[t], x))
        for j in range(1, d):
            # PAIR-DOUBLE sanity and doubling
            inc("PD_viol", r.F[j] > 2 * r.F[j - 1] + 2)
            if not r.dbl[j]: continue
            inc("levels"); p, q = 2 * j, 2 * j + 1; W = r.wins(j)
            Phi = lambda t: sum(r.S[t][x] != r.c(t, j) for x in (p, q)) if t >= 1 else sum(r.S[0][x] != r.O[0][j - 1] for x in (p, q))
            inc("E1_viol", not (Phi(0) == 2 and Phi(T) == 0))
            inc("E2_viol", any(Phi(t - 1) != 0 for t in range(1, T + 1) if r.O[t][j - 1] != r.O[t - 1][j - 1]))
            for t in range(1, T + 1):
                mp, mq = r.mv(t, p), r.mv(t, q); inc("E3_viol", (mp and mq) or ((mp or mq) != (r.O[t][j] != r.O[t - 1][j])))
            firsts = set()
            for a, e, mv in W:
                inc("windows"); inc("E4_viol", sorted(x for _, x in mv) != [p, q] or len({t for t, _ in mv}) != 2)
                if mv: firsts.add(min(mv)[1])
            g = [G["gate"][p][jj] < G["gate"][q][jj] for jj in (0, 1)]
            inc("E5_viol", len(firsts) > 1); inc("E5gamma_viol", g[0] != g[1])
            inc("E5_Fprev0_levels", r.F[j - 1] == 0)
            k = kabove(r, j)
            for i, (a, e, mv) in enumerate(W):
                pu = mv[1][0] - mv[0][0]; inc("PN_units"); inc("PN_viol", pu < k + 1); inc("PN_tight", pu == k + 1)
                if k >= 1 and i + 1 < len(W):
                    gp = W[i + 1][2][0][0] - mv[1][0]; inc("GN_units"); inc("GN_viol", gp < k + 1); inc("GN_tight", gp == k + 1)
            for x in (p, q):
                ts = [t for t in range(1, T + 1) if r.mv(t, x)]
                for t, t2 in zip(ts, ts[1:]):
                    inc("DFb_units"); inc("DFb_viol", len({r.dec(r.S[v], x) for v in range(t - 1, t2)}) == 1)
                    inc("DFb_endpoints_equal", r.dec(r.S[t - 1], x) == r.dec(r.S[t2 - 1], x))
            xp, xq = [o[1] for o in G["opts"][p]], [o[1] for o in G["opts"][q]]
            if xp[0] == xq[1] and xp[1] == xq[0] and xp[0] != xp[1] and min(xp) >= 0:
                inc("CE_pairs"); A0, A1 = xp
                th = {p: r.eps(G["opts"][p][1][2]) - r.eps(G["opts"][p][0][2]), q: r.eps(G["opts"][q][0][2]) - r.eps(G["opts"][q][1][2])}
                own = max(G["br"][G["opts"][x][kk][2]] for x in (p, q) for kk in (0, 1))
                D = lambda st: r.cv(st, A0) - r.cv(st, A1)
                for st in r.S:   # (i) at every state
                    inc("CEi_units"); inc("CEi_viol", (r.pi(st, p) == 0) != (D(st) > th[p]) or (r.pi(st, q) == 1) != (D(st) > th[q]))
                for a, e, mv in W:
                    (u1, f1), (u2, x2) = mv; inc("CE_windows")
                    inc("CEii_viol", (D(r.S[u1 - 1]) > th[f1]) == (D(r.S[u2 - 1]) > th[x2]))
                    hyp = []
                    for st in (r.S[u1 - 1], r.S[u2 - 1]):
                        sd = set(r.chain(st, A0, st[A0])) ^ set(r.chain(st, A1, st[A1]))
                        Rk = max((G["br"][m] for m in sd), default=-1); hyp.append((Rk > own, Rk, st))
                    if hyp[0][0] and hyp[1][0]:
                        inc("CEiii_units"); inc("CEiii_viol", (D(r.S[u1 - 1]) > 0) == (D(r.S[u2 - 1]) > 0))
                        for ok, Rk, st in hyp:   # the proof's intermediate inequality |D| >= 2^R > 2 max|theta|
                            inc("CEiii_states"); inc("proofstep_absD_lt_2^R", abs(D(st)) < (1 << Rk))
                            inc("proofstep_absD_le_2maxtheta", abs(D(st)) <= 2 * max(abs(th[p]), abs(th[q])))
        print(os.path.basename(f), "T", T, "F", r.F[:min(d, 9)], "doubling", [l for l in range(d) if r.dbl[l]], flush=True)
    print("COUNTERS", C)

def inst(f7, fs):
    for f, name in ((f7, "I-ROOM"), (fs, "I-FUEL")):
        G = load(f); r = R(G)
        print(name, os.path.basename(f), "inLR", S.in_LR(G, 28), "T", r.T, "F[:8]", r.F[:8], "doubling", [l for l in range(8) if r.dbl[l]],
              "start", "".join(map(str, r.S[0])))
        for j in range(1, 6):
            W = r.wins(j); pv = []; gv = []
            for i, (a, e, mv) in enumerate(W):
                assert len(mv) == 2
                if mv[1][0] - mv[0][0] < 7 - j: pv.append(i)
                if i + 1 < len(W) and W[i + 1][2][0][0] - mv[1][0] < 7 - j: gv.append(i)
            typ = lambda i: tuple((x, r.S[W[i][0]][x]) for x in (2 * j - 2, 2 * j - 1) if W[i][0] > 1 and r.mv(W[i][0], x))
            from collections import Counter
            print(f"  level {j}: windows {len(W)} pulse-viol {len(pv)} gap-viol {len(gv)} distinct windows {len(set(pv) | set(gv))}",
                  "pulse types", dict(Counter(typ(i) for i in pv)), "gap types", dict(Counter(typ(i) for i in gv)),
                  "pulse lengths", sorted({W[i][2][1][0] - W[i][2][0][0] for i in pv}),
                  "gap lengths", sorted({W[i + 1][2][0][0] - W[i][2][1][0] for i in gv}), "first window in pulse-viol", 0 in pv)
        W = r.wins(6); bad = [w for w in W if not (sorted(x for _, x in w[2]) == [12, 13])]
        print("  level 6: windows", len(W), "without one move of each of 12, 13:", len(bad), "| move-count profile of those:",
              sorted({len(w[2]) for w in bad}))
        if name == "I-FUEL":
            print("  CROSS: xt(12,.)", [o[1] for o in G["opts"][12]], "xt(13,.)", [o[1] for o in G["opts"][13]], "option 19 rank", G["br"][19],
                  "parity", G["bp"][19], "xt(11,.)", [o[1] for o in G["opts"][11]])
            badset = {w[0] for w in bad}
            for scope in ("any state s_(a-1)..s_(e-1)", "s_(a-1) only", "every state s_(a-1)..s_(e-1)", "any state s_a..s_e"):
                cnt = {True: 0, False: 0}
                for a, e, mv in W:
                    rng = {"any state s_(a-1)..s_(e-1)": range(a - 1, e), "s_(a-1) only": [a - 1],
                           "every state s_(a-1)..s_(e-1)": range(a - 1, e), "any state s_a..s_e": range(a, e + 1)}[scope]
                    hits = [any(r.dec(r.S[t], x)[0] == 19 for x in (12, 13)) for t in rng]
                    ok = all(hits) if scope.startswith("every") else any(hits)
                    cnt[a in badset] += ok
                print(f"  decider (9,1) of 12 or 13, scope [{scope}]: failing {cnt[True]}/48, others {cnt[False]}/{len(W) - 48}")
            # is (9,1) on 11's chain and is 11 -> 9?
            print("  option 19 on chain of 11's current option at s_0:", 19 in r.chain(r.S[0], 11, r.S[0][11]),
                  "| chain-membership over all states:", sum(19 in r.chain(st, 11, st[11]) for st in r.S), "/", r.T + 1)

if __name__ == "__main__":
    if sys.argv[1] == "corpus": corpus(sys.argv[2:])
    else: inst(sys.argv[2], sys.argv[3])
