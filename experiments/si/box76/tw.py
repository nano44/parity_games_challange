#!/usr/bin/env python3
"""L-SI box 76 (TROPICAL-WINDOW): window-type measurements on 2-wide degree-2 ladders L^R_d (RESULTS R110 wiring).
Own simulator of RESULTS R104's IDEAL model (independent of L-NEW box150 Gen; XCHK=<path to box150/check.py> cross-checks every run).
Corpus: every L^R_d genome JSON under experiments/new/box150..box187 at l-new commit 9995f5a2d (read with git show; FROZEN list in
corpus.txt with blob sha1s), every start for N <= 10, the stored start otherwise. Extra genomes: argv paths (JSON files).
Output (deterministic): per (d, level) maxima of F(j), moves; window-type tables; additive-increment tables. See docs/si/N5-TROPICAL-box76.md.
"""
import sys, os, json, itertools, collections
NEG = os.environ.get("NEG")  # negative controls: 1 = key-greatest available option, 2 = key-least option ignoring availability

def load_corpus():
    """the 208 L^R_d genomes of the frozen corpus (corpus_lr.json.gz: [git blob sha1, path at l-new 9995f5a2d, file text]);
    every text is re-hashed as a git blob and must equal its recorded sha1."""
    import gzip, hashlib
    H = os.path.dirname(os.path.abspath(__file__)); out = []
    for blob, path, txt in json.loads(gzip.open(os.path.join(H, "corpus_lr.json.gz")).read()):
        b = txt.encode(); h = hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest()
        if h != blob: raise SystemExit("corpus blob mismatch " + path)
        out.append((path, json.loads(txt)))
    return out

def is_lr(G):
    if not isinstance(G, dict) or "opts" not in G: return False
    N = G["N"]; lev = G["lev"]
    if N % 2 or lev != [v // 2 for v in range(N)]: return False
    return all(len(G["opts"][x]) == 2 and G["opts"][x][k][0] == (2 * (lev[x] - 1) + k if lev[x] else -1) for x in range(N) for k in range(2))

class Sim:
    def __init__(s, G):
        s.N = G["N"]; s.lev = G["lev"]; s.o = G["opts"]; s.g = G["gate"]
        s.e = [[(1 << G["br"][s.o[x][k][2]]) * (1 if G["bp"][s.o[x][k][2]] == 0 else -1) for k in range(2)] for x in range(s.N)]
        s.order = sorted(range(s.N), key=lambda v: s.lev[v])
    def val(s, st, x, k):
        t = 0; n = 0
        while True:
            t += s.e[x][k]; y = s.o[x][k][1]; n += 1
            if n > 4 * s.N + 4: raise RuntimeError("Xi-cycle")
            if y < 0: return t
            x, k = y, st[y]
    def keys(s, st):
        K = [None] * s.N
        for x in s.order:
            w = s.o[x][st[x]][0]; K[x] = (s.g[x][st[x]],) if w < 0 else K[w] + (s.g[x][st[x]],)
        return K
    def okey(s, K, x, k):
        w = s.o[x][k][0]; return (s.g[x][k],) if w < 0 else K[w] + (s.g[x][k],)
    def run(s, st, cap=100000):
        S = [tuple(st)]
        while len(S) <= cap:
            st = S[-1]
            A = []
            for x in range(s.N):
                c = s.val(st, x, st[x]); A.append([k for k in range(2) if k == st[x] or s.val(st, x, k) > c])
            if all(len(a) == 1 for a in A): return S
            ns = list(st); K = [None] * s.N
            for x in s.order:
                cand = A[x] if NEG != "2" else range(2)          # NEG=2: ignore availability (negative control)
                k = (max if NEG == "1" else min)(cand, key=lambda k: s.okey(K, x, k)); ns[x] = k; K[x] = s.okey(K, x, k)
            if tuple(ns) == st: return S
            S.append(tuple(ns))
        raise RuntimeError("cap")

def analyse(sim, S):
    """per-step data: Mv, flips per level, c_j, pi, alignment."""
    N = sim.N; d = N // 2; T = len(S) - 1
    K = [sim.keys(s) for s in S]
    ordr = [[K[t][2 * j] < K[t][2 * j + 1] for j in range(d)] for t in range(T + 1)]   # ord_s(2j, 2j+1)
    c = [[None] + [0 if ordr[t][j - 1] else 1 for j in range(1, d)] for t in range(T + 1)]  # c_j(s_t)
    pi = [[0 if sim.val(S[t], x, 0) > sim.val(S[t], x, 1) else 1 for x in range(N)] for t in range(T + 1)]
    Mv = [None] + [{x for x in range(N) if S[t][x] != S[t - 1][x]} for t in range(1, T + 1)]
    flip = [None] + [[ordr[t][j] != ordr[t - 1][j] for j in range(d)] for t in range(1, T + 1)]
    return dict(T=T, d=d, K=K, c=c, pi=pi, Mv=Mv, flip=flip)

def main():
    xchk = os.environ.get("XCHK")
    Gen = None
    if xchk:
        ns = {"__file__": xchk, "__name__": "lib"}; exec(open(xchk).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
    corpus = load_corpus() + [(p, json.load(open(p))) for p in sys.argv[1:]]
    st = collections.Counter()
    Fmax = collections.defaultdict(int); Mmax = collections.defaultdict(int); MZmax = collections.defaultdict(int)
    wit = {}
    # window types: level j >= 1, window = maximal interval of constant c_j; type at entry (state s_(t0-1) vs new c, pi at s_(t0-1))
    WT = collections.defaultdict(lambda: [0, 0, 0, 0])  # type -> [count, max moves in window, max flips of pair j in window, max length]
    INC = collections.defaultdict(lambda: -99)  # (d, j) -> max over runs of mz(j+1) - max_{i<=j} m(i)
    PROF = collections.Counter()
    TEMP = collections.defaultdict(lambda: -1)   # (type, next type) at one level -> max moves of p,q in the first window
    SPAWN = collections.defaultdict(int)         # (type at level j, type at level j+1) -> max number of level-(j+1) windows starting in it
    for path, G in corpus:
        if not is_lr(G): continue
        st["files"] += 1; sim = Sim(G); N = G["N"]; d = N // 2
        Z = {G["opts"][x][k][1] for x in range(N) for k in range(2)} - {-1}
        g2 = Gen(G) if Gen else None
        starts = list(itertools.product((0, 1), repeat=N)) if N <= 10 else [tuple(G["start"])]
        for s0 in starts:
            S = sim.run(s0); st["runs"] += 1; st["steps"] += len(S) - 1
            if g2 is not None:
                S2, _ = g2.run(s0)
                if [tuple(x) for x in S2] != S: st["XCHK_MISMATCH"] += 1
            a = analyse(sim, S); T = a["T"]
            mv = [sum(1 for t in range(1, T + 1) if x in a["Mv"][t]) for x in range(N)]
            F = [sum(1 for t in range(1, T + 1) if a["flip"][t][j]) for j in range(d)]
            for j in range(d):
                if F[j] > Fmax[(d, j)]: Fmax[(d, j)] = F[j]; wit[("F", d, j)] = (path, "".join(map(str, s0)), T)
                m = max(mv[2 * j], mv[2 * j + 1]); Mmax[(d, j)] = max(Mmax[(d, j)], m)
                mz = max([mv[x] for x in (2 * j, 2 * j + 1) if x in Z] or [0])
                if mz > MZmax[(d, j)]: MZmax[(d, j)] = mz; wit[("MZ", d, j)] = (path, "".join(map(str, s0)), T)
            # additive increments: Xi-target moves at level j+1 minus max moves (all movers) at levels <= j
            pre = 0
            for j in range(d - 1):
                pre = max(pre, mv[2 * j], mv[2 * j + 1])
                mz = max([mv[x] for x in (2 * j + 2, 2 * j + 3) if x in Z] or [-99])
                if mz > -99 and mz - pre > INC[(d, j + 1)]: INC[(d, j + 1)] = mz - pre; wit[("INC", d, j + 1)] = (path, "".join(map(str, s0)), T, tuple(mv))
            PROF[(d, tuple(max(mv[2 * j], mv[2 * j + 1]) for j in range(d)))] += 1
            # windows
            WL = {}
            for j in range(1, d):
                WL[j] = []
                p, q = 2 * j, 2 * j + 1; t = 1
                while t <= T:
                    e = t
                    while e + 1 <= T and not a["flip"][e + 1][j - 1]: e += 1
                    cc = a["c"][t][j]; s_ = S[t - 1]; pi_ = a["pi"][t - 1]
                    ty = (int(s_[p] != cc) + int(s_[q] != cc), int(s_[p] == s_[q]),
                          int(s_[p] != cc and pi_[p] == cc) + int(s_[q] != cc and pi_[q] == cc))
                    w = WT[ty]; w[0] += 1
                    w[1] = max(w[1], sum(1 for u in range(t, e + 1) for x in (p, q) if x in a["Mv"][u]))
                    w[2] = max(w[2], sum(1 for u in range(t, e + 1) if a["flip"][u][j]))
                    w[3] = max(w[3], e - t + 1)
                    WL[j].append((t, e, ty, sum(1 for u in range(t, e + 1) for x in (p, q) if x in a["Mv"][u])))
                    t = e + 1
                for A_, B_ in zip(WL[j], WL[j][1:]):
                    TEMP[(A_[2], B_[2])] = max(TEMP[(A_[2], B_[2])], A_[3])
            for j in range(1, d - 1):
                for (t0, e0, ty0, _) in WL[j]:
                    cnt = collections.Counter(ty1 for (t1, e1, ty1, _) in WL[j + 1] if t0 <= t1 <= e0)
                    for ty1, n in cnt.items(): SPAWN[(ty0, ty1)] = max(SPAWN[(ty0, ty1)], n)
    print("INFO " + " ".join("%s %d" % kv for kv in sorted(st.items())))
    print("# per (d, level j): max F(j) | max moves (all movers of level j) | max moves (Xi-targets of level j)")
    for d in sorted({k[0] for k in Fmax}):
        print("d %d F %s | M %s | MZ %s" % (d, [Fmax[(d, j)] for j in range(d)], [Mmax[(d, j)] for j in range(d)], [MZmax[(d, j)] for j in range(d)]))
    print("# window types (Phi at entry, same option, ready = misaligned and pi = c): count, max moves of p,q, max flips of pair j, max length")
    for ty in sorted(WT): print("WT %s %s" % (ty, WT[ty]))
    types = sorted(WT)
    def mcm(Wd):
        best = None
        for L in range(1, len(types) + 1):
            for cyc in itertools.permutations(types, L):
                if cyc[0] != min(cyc): continue
                es = list(zip(cyc, cyc[1:] + cyc[:1]))
                if all(e in Wd for e in es):
                    m = sum(Wd[e] for e in es) / L
                    if best is None or m > best[0]: best = (m, cyc)
        return best
    print("# temporal max-plus graph (consecutive windows of one level; weight = max moves of p,q in the first window)")
    for k in sorted(TEMP): print("TEMP %s -> %s %d" % (k[0], k[1], TEMP[k]))
    print("MCM_TEMP %s" % (mcm(dict(TEMP)),))
    print("# spawn matrix B (level j type -> level j+1 type: max number of child windows starting inside); (+,x) recursion")
    for k in sorted(SPAWN): print("SPAWN %s -> %s %d" % (k[0], k[1], SPAWN[k]))
    print("SPAWN_MAX_TOTAL %d" % max(sum(SPAWN.get((a_, b_), 0) for b_ in types) for a_ in types))
    print("# additive increment: max over runs of [moves of a Xi-target of level j] - [max moves of any mover of level < j]")
    for k in sorted(INC): print("INC d %d j %d %d  witness %s" % (k[0], k[1], INC[k], wit[("INC",) + k]))
    for k in sorted(wit):
        if k[0] in ("F", "MZ") and k[2] == k[1] - 1: print("WIT %s %s" % (k, wit[k]))

if __name__ == "__main__":
    main()
