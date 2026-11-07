#!/usr/bin/env python3
"""L-NEW box 147: COARSE Xi-statistics on IDEAL-ACYC genomes (R178 §1 rule, box139/paths.py run()), deg 2.
Steps t >= 2 are CHAINED / UNCHAINED as in box 144 chain.py ALL form (= box146 energy.py): h_t = least-level mover of step t
(smallest index on a tie); t is chained iff h_(t-1) lies on the Xi-play, under state t-2, of the option h_t takes at t.
Per state s (all from s only): face values fv(x,k) (fastcyc values), B(x) = Xi-better option, UNST(x) = [B(x) != s(x)],
KP(x) = key-preferred option under the keys of s, AGR(x) = [B(x) == KP(x)], MRG(x) = pi-position of the merge vertex of x's two
Xi-plays (n if they only meet at T), PL(x) = length of the Xi-play of x's current option.
(A) Statistics PHI(s) (poly levels), each tested DOWN (strict fall at unchained, no rise at chained) and UP (mirror).
(B) Step quantities Q_t (functions of (s_(t-1), s_t)), same test on the sequence Q_t.
(C) Quotient test for a feature map F (any range): build the digraph on F-values with an edge F(s_(t-1)) -> F(s_t) per step t >= 2;
    SOME function g(F) works DOWN iff no unchained edge lies in a strongly connected component (cycle or self-loop). Reports the
    number of such bad edges and, if none, the minimum number of levels needed (longest unchained-weighted path in the condensation).
Usage: stat.py genome.json ...   (VERB=1 prints first violation per statistic)"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(HERE, "..", "box139", "paths.py")
src = open(P).read().split("def vx(G):")[0]; ns = {"__file__": P}; exec(src, ns); run = ns["run"]; fc = ns["fc"]
VERB = os.environ.get("VERB")
def topo(G):
    if "xorder" in G: return list(G["xorder"])
    N, opts = G["N"], G["opts"]; indeg = [0] * N
    for v in range(N):
        for o in opts[v]:
            if o[1] >= 0: indeg[o[1]] += 1
    order = []; avail = sorted(v for v in range(N) if indeg[v] == 0)
    while avail:
        v = avail.pop(0); order.append(v)
        for o in opts[v]:
            if o[1] >= 0:
                indeg[o[1]] -= 1
                if indeg[o[1]] == 0: avail.append(o[1]); avail.sort()
    return order
def feats(G, s, pos):
    N, opts, lev, gate = G["N"], G["opts"], G["lev"], G["gate"]
    val, idx, _, M = fc.values(G, s)
    fv = [[val(N + idx[(v, k)]) for k in range(len(opts[v]))] for v in range(N)]
    B = [max(range(len(opts[v])), key=lambda k: (fv[v][k], k == s[v])) for v in range(N)]
    order = sorted(range(N), key=lambda v: lev[v]); key = [None] * N
    for v in order:
        wt = opts[v][s[v]][0]; key[v] = (gate[v][s[v]],) if wt < 0 else key[wt] + (gate[v][s[v]],)
    KP = [min(range(len(opts[v])), key=lambda k: ((gate[v][k],) if opts[v][k][0] < 0 else key[opts[v][k][0]] + (gate[v][k],))) for v in range(N)]
    def play(x, k):
        out = []; y = opts[x][k][1]
        while y >= 0: out.append(y); y = opts[y][s[y]][1]
        return out
    MRG = []; PL = []; PLAY = []
    for x in range(N):
        p0, p1 = play(x, 0), play(x, 1); st = set(p1); m = next((y for y in p0 if y in st), -1)
        MRG.append(pos[m] if m >= 0 else N); PL.append(len(play(x, s[x]))); PLAY.append(tuple(play(x, s[x])))
    UNST = [int(B[v] != s[v]) for v in range(N)]; AGR = [int(B[v] == KP[v]) for v in range(N)]
    return dict(B=B, UNST=UNST, KP=KP, AGR=AGR, MRG=MRG, PL=PL, PLAY=PLAY, fv=fv, key=key)
def label(G, S):
    N, opts, lev = G["N"], G["opts"], G["lev"]; T = len(S) - 1
    mv = lambda t, x: S[t][x] != S[t - 1][x]
    def play(t, x, k):
        out = []; y = opts[x][k][1]
        while y >= 0: out.append(y); y = opts[y][S[t][y]][1]
        return out
    least = {}
    for t in range(1, T + 1):
        ms = [x for x in range(N) if mv(t, x)]
        if ms: least[t] = min(ms, key=lambda x: (lev[x], x))
    lab = {}
    for t in range(2, T + 1):
        if t not in least or t - 1 not in least: continue
        x = least[t]; Z = [y for y in play(t - 2, x, S[t][x]) if mv(t - 1, y)]; lab[t] = least[t - 1] in Z
    return lab, least
def stats(G, F, pos, n, lev, d):
    U = [x for x in range(n) if F["UNST"][x]]
    pi1 = lambda x: pos[x] + 1
    out = {
      "NUNST": len(U), "SUMPI_U": sum(pi1(x) for x in U), "SUMRPI_U": sum(n - pos[x] for x in U),
      "MAXPI_U": max((pos[x] for x in U), default=-1), "MINPI_U": min((pos[x] for x in U), default=n),
      "SUMLEV_U": sum(lev[x] + 1 for x in U), "NAGR": sum(F["AGR"]), "SUMPI_AGR": sum(F["AGR"][x] * pi1(x) for x in range(n)),
      "LVL_AGR": sum(1 for l in range(d) if all(F["AGR"][x] for x in range(n) if lev[x] == l)),
      "NB1": sum(F["B"]), "SUMPI_B": sum(F["B"][x] * pi1(x) for x in range(n)),
      "SUMMRG": sum(F["MRG"]), "SUMMRG_U": sum(F["MRG"][x] for x in U), "SUMPL": sum(F["PL"]),
      "NWANT": sum(1 for x in U if F["KP"][x] == F["B"][x]), "SUMPI_WANT": sum(pi1(x) for x in U if F["KP"][x] == F["B"][x]),
      "NWAIT": sum(1 for x in U if F["KP"][x] != F["B"][x]), "SUMPI_WAIT": sum(pi1(x) for x in U if F["KP"][x] != F["B"][x]),
      "MAXPI_WANT": max((pos[x] for x in U if F["KP"][x] == F["B"][x]), default=-1),
      "MINPI_WAIT": min((pos[x] for x in U if F["KP"][x] != F["B"][x]), default=n),
      "NPLAYU": sum(1 for x in range(n) if any(F["UNST"][y] for y in F["PLAY"][x])),
    }
    out["LEX_NU_MAXPI"] = (out["NUNST"], out["MAXPI_U"]); out["LEX_MAXPI_NU"] = (out["MAXPI_U"], out["NUNST"])
    out["LEX_NWAIT_NWANT"] = (out["NWAIT"], out["NWANT"])
    return out
QF = {  # quotient features (any range)
  "B": lambda F: tuple(F["B"]), "UNST": lambda F: tuple(F["UNST"]), "AGR": lambda F: tuple(F["AGR"]), "KP": lambda F: tuple(F["KP"]),
  "MRG": lambda F: tuple(F["MRG"]), "B+KP": lambda F: (tuple(F["B"]), tuple(F["KP"])), "UNST+KP": lambda F: (tuple(F["UNST"]), tuple(F["KP"])),
  "B+UNST": lambda F: (tuple(F["B"]), tuple(F["UNST"])),
}
def scc_test(nodes, edges):
    # edges: list of (a, b, unch). Tarjan SCC, then bad = unchained edges inside an SCC; levels = longest unchained-weighted path.
    adj = {}
    for a, b, u in edges: adj.setdefault(a, []).append(b); adj.setdefault(b, [])
    index = {}; low = {}; st = []; on = set(); comp = {}; c = [0]; i = [0]
    sys.setrecursionlimit(100000)
    def sc(v):
        index[v] = low[v] = i[0]; i[0] += 1; st.append(v); on.add(v)
        for w in adj[v]:
            if w not in index: sc(w); low[v] = min(low[v], low[w])
            elif w in on: low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            while True:
                w = st.pop(); on.discard(w); comp[w] = c[0]
                if w == v: break
            c[0] += 1
    for v in adj:
        if v not in index: sc(v)
    bad = sum(1 for a, b, u in edges if u and comp[a] == comp[b])
    if bad: return bad, None
    cadj = {}
    for a, b, u in edges:
        if comp[a] != comp[b] or u: cadj.setdefault(comp[a], []).append((comp[b], u))
    memo = {}
    def lp(x):
        if x not in memo: memo[x] = max((u + lp(y) for y, u in cadj.get(x, [])), default=0)
        return memo[x]
    return 0, max((lp(x) for x in set(comp.values())), default=0)
def analyse(G):
    S, CUR, KEY, why = run(G, cap=5000); n, lev = G["N"], G["lev"]; d = max(lev) + 1; T = len(S) - 1
    order = topo(G); pos = {v: i for i, v in enumerate(order)}
    FS = [feats(G, s, pos) for s in S]; ST = [stats(G, F, pos, n, lev, d) for F in FS]
    lab, least = label(G, S)
    # step quantities
    def stepq(t):
        a, b = FS[t - 1], FS[t]; ch = [x for x in range(n) if a["PLAY"][x] != b["PLAY"][x]]; mvs = [x for x in range(n) if S[t][x] != S[t - 1][x]]
        return {"Q_MAXPI_PLAYCH": max((pos[x] for x in ch), default=-1), "Q_MINPI_PLAYCH": min((pos[x] for x in ch), default=n),
                "Q_MAXPI_MV": max((pos[x] for x in mvs), default=-1), "Q_MINPI_MV": min((pos[x] for x in mvs), default=n),
                "Q_PIH": pos[least[t]] if t in least else -1, "Q_NMV": len(mvs), "Q_NPLAYCH": len(ch)}
    Q = {t: stepq(t) for t in range(1, T + 1)}
    viol = {}; first = {}
    def test(name, a, b, ch, t):
        for o in ("D", "U"):
            lo, hi = (b, a) if o == "D" else (a, b)
            bad = (not lo < hi) if not ch else (lo > hi)
            viol.setdefault((name, o), 0)
            if bad: viol[(name, o)] += 1; first.setdefault((name, o), (t, "ch" if ch else "UNCH", a, b))
    for t, ch in lab.items():
        for k in ST[0]: test(k, ST[t - 1][k], ST[t][k], ch, t)
        if t - 1 in Q:
            for k in Q[t]: test(k, Q[t - 1][k], Q[t][k], ch, t)
    qres = {}
    for k, f in QF.items():
        edges = [(f(FS[t - 1]), f(FS[t]), not ch) for t, ch in lab.items()]
        qres[k] = scc_test(None, edges) if edges else (0, 0)
    return dict(T=T, U=sum(1 for c in lab.values() if not c), CH=sum(lab.values()), viol=viol, first=first, q=qres, why=why, FS=FS, ST=ST, lab=lab, S=S, pos=pos)
if __name__ == "__main__":
    tot = {}; qtot = {}
    for p in sys.argv[1:]:
        G = json.load(open(p)); R = analyse(G)
        bad = [f"{k}{o}" for (k, o), c in R["viol"].items() if c == 0]
        print(f"STAT {os.path.basename(p)} N {G['N']} STEPS {R['T']} U {R['U']} CH {R['CH']} STOP {R['why']} SURVIVE {' '.join(bad) or '-'} "
              f"QUOT " + " ".join(f"{k}:{'BAD'+str(b) if b else 'lv'+str(l)}" for k, (b, l) in R["q"].items()))
        for k, c in R["viol"].items():
            tot[k] = tot.get(k, 0) + c
            if c and VERB: print("   first", k, R["first"][k])
        for k, (b, l) in R["q"].items(): qtot[k] = qtot.get(k, 0) + (b > 0)
    print("TOTAL VIOL (genomes x steps): " + " ".join(f"{k}{o} {c}" for (k, o), c in sorted(tot.items(), key=lambda z: z[1])))
    print("QUOT genomes with a bad (unchained-in-cycle) edge: " + " ".join(f"{k} {c}" for k, c in qtot.items()))
