#!/usr/bin/env python3
"""L-NEW box 150: machine check of packet P-IDEAL-RED (docs/new/P-IDEAL-RED.md) on IDEAL-ACYC genomes.
Own simulator of the IDEAL model as stated in RESULTS R104 (R178 §1): Xi-value of option (x,k) under state s = set of beta's on the
chain (x,k), (xt, s(xt)), ... up to X, encoded as the integer sum (+/-) 2^rank (+ for even parity), which orders sets exactly as
«largest-rank beta of the symmetric difference decides» (packet §1, Lemma ENC); key = gate indices of the W-target chain under the
NEW state, lowest level first; a step moves every mover to the key-least option among its current one and the strictly Xi-better
ones; stop when nothing is available or nothing changes. Cross-checked state for state against box139/paths.py run() (XSIM).
Checks (violation counters, all must be 0):
 XSIM     state sequence differs from box139/paths.py run()
 TOPO     pi is not a topological order of the Xi-graph (genome not acyclic)
 MONO     (Lemma MONO) the current face value of some mover falls at some step
 XINEW    (Lemma XI-NEW) a least-level mover h of step t >= 2 takes w with w in A_(t-2)(h)
 RISE     (Cor. RISE) face(h_t, w) does not rise strictly at t-1, or no mover on its play (state t-2) moved at t-1, or such a mover
          has pi <= pi(h_t)
 CHAIN    (Thm CHAIN-BACK) a chained step with pi(h_t) >= pi(h_(t-1)), or T > N (1 + U)
 KEYFLIP  (Lemma KEYFLIP, deg 2) moves(x) > 1 + KF_x, or T > sum_x (1 + KF_x), or sum KF > N T
 DECR     (Lemma DECREMENT, any degree) y_t has c = 0 at s_(t-1), or c(y_t) does not fall, or c(x) changes for some pi(x) > pi(y_t),
          or E = sum_x c(x) D^pi(x) does not fall strictly
 TOPMONO  (Cor. TOP-MONO, deg 2) for some k: TOP_k rises, or falls with RANK_t > k, or does not fall with RANK_t <= k
 RBOUND   (Cor. RANK-BOUND, deg 2) #{t : RANK_t <= k} > sum_(j<=k) C(N, j) - 1, or U > sum_(j <= R) C(N, j) - 1
 RESTR    (Lemma INTERVAL-RESTRICT, deg 2) for some k and maximal TOP_k-constant interval [a, b): a mover with pi >= p_k moves inside,
          or the restricted genome H's run from s_a does not begin with s_a .. s_(b-1), or a chained/unchained label at t >= a + 2
          differs from H's label at t - a
 ICHARGE  (Cor. INTERVAL-CHARGE, deg 2) #{RANK = r} > (N - r + 1)(1 + #{RANK <= r - 1}) for some r >= 2
 REC      (Cor. RECURSION, deg 2) U > (#TOP_1 intervals - 1) + sum_i (U(H_i) + 1)
Info only: REC148 = number of runs with U > sum_i (U(H_i) + 1) (the box 148 form, which omits the boundary steps).
NEG=1 / 2 / 3: broken step rules (3 = keys under the OLD state) (negative controls; violations expected).
ALL=1: also every start (2^N) for genomes with N <= ALLN (default 10).
Usage: check.py genome.json ...   Prints one line per genome and a TOTAL line."""
import sys, os, json, itertools
NEG = os.environ.get("NEG")  # negative controls: 1 = key-GREATEST available option, 2 = key-least option ignoring availability, 3 = keys of the old state
from math import comb
HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(HERE, "..", "box139", "paths.py")
_ns = {"__file__": os.path.abspath(P)}; exec(open(P).read().split("def vx(G):")[0], _ns); ref_run = _ns["run"]

def topo(G):
    if "xorder" in G: return list(G["xorder"])
    N, opts = G["N"], G["opts"]; indeg = [0] * N
    for v in range(N):
        for o in opts[v]:
            if o[1] >= 0: indeg[o[1]] += 1
    order, av = [], sorted(v for v in range(N) if indeg[v] == 0)
    while av:
        v = av.pop(0); order.append(v)
        for o in opts[v]:
            if o[1] >= 0:
                indeg[o[1]] -= 1
                if indeg[o[1]] == 0: av.append(o[1])
    return order

class Gen:
    def __init__(s, G):
        s.G = G; s.N = G["N"]; s.lev = G["lev"]; s.opts = G["opts"]; s.gate = G["gate"]; s.br = G["br"]; s.bp = G["bp"]
        s.byl = sorted(range(s.N), key=lambda v: s.lev[v])
    def eps(s, v, k):
        m = s.opts[v][k][2]; return (1 if s.bp[m] == 0 else -1) * (1 << s.br[m])
    def face(s, st, v, k, memo=None):
        """integer encoding of the beta-set of the chain from option (v,k) under state st (acyclic: terminates)"""
        tot, seen = 0, set()
        while True:
            if (v, k) in seen: raise RuntimeError("Xi-cycle")
            seen.add((v, k)); tot += s.eps(v, k); xt = s.opts[v][k][1]
            if xt < 0: return tot
            v, k = xt, st[xt]
    def play(s, st, v, k):
        """movers on the Xi-play of option (v,k) after v, under st"""
        out = []; xt = s.opts[v][k][1]
        while xt >= 0: out.append(xt); xt = s.opts[xt][st[xt]][1]
        return out
    def avail(s, st, v):
        c = s.face(st, v, st[v]); return [k for k in range(len(s.opts[v])) if k == st[v] or s.face(st, v, k) > c]
    def cnt(s, st, v):
        c = s.face(st, v, st[v]); return sum(1 for k in range(len(s.opts[v])) if s.face(st, v, k) > c)
    def keys(s, st):
        key = [None] * s.N
        for v in s.byl:
            wt = s.opts[v][st[v]][0]; key[v] = (s.gate[v][st[v]],) if wt < 0 else key[wt] + (s.gate[v][st[v]],)
        return key
    def optkey(s, key, v, k):
        wt = s.opts[v][k][0]; return (s.gate[v][k],) if wt < 0 else key[wt] + (s.gate[v][k],)
    def step(s, st):
        A = [s.avail(st, v) for v in range(s.N)]
        if all(len(a) == 1 for a in A): return None, A
        key = [None] * s.N; ns = list(st); oldkey = s.keys(st)
        for v in s.byl:
            if NEG == "1": k = max(A[v], key=lambda k: s.optkey(key, v, k))
            elif NEG == "3": k = min(A[v], key=lambda k: s.optkey(oldkey, v, k))
            elif NEG == "2": k = min(range(len(s.opts[v])), key=lambda k: s.optkey(key, v, k))
            else: k = min(A[v], key=lambda k: s.optkey(key, v, k))
            ns[v] = k; key[v] = s.optkey(key, v, k)
        if ns == list(st): return None, A
        return tuple(ns), A
    def run(s, start, cap=200000):
        S = [tuple(start)]; AS = []
        while len(S) - 1 < cap:
            ns, A = s.step(S[-1]); AS.append(A)
            if ns is None: return S, AS
            S.append(ns)
        raise RuntimeError("cap")

def restrict(G, keep, sa):
    """genome H: movers in keep get the single option sa(x) (same option record, gate, beta); start sa"""
    H = json.loads(json.dumps(G)); H["start"] = list(sa); H.pop("deg", None)
    for x in keep:
        H["opts"][x] = [G["opts"][x][sa[x]]]; H["gate"][x] = [G["gate"][x][sa[x]]]; H["start"][x] = 0
    return H

def labels(g, S):
    """h_t (least level, smallest index), chained flags for t >= 2, U"""
    T = len(S) - 1; h = [None] * (T + 1); ch = [None] * (T + 1)
    for t in range(1, T + 1):
        mv = [v for v in range(g.N) if S[t][v] != S[t - 1][v]]; h[t] = min(mv, key=lambda v: (g.lev[v], v))
    for t in range(2, T + 1):
        ch[t] = h[t - 1] in g.play(S[t - 2], h[t], S[t][h[t]])
    U = sum(1 for t in range(2, T + 1) if not ch[t])
    return h, ch, U

def Uof(G, start=None):
    g = Gen(G); S, _ = g.run(G["start"] if start is None else start); return labels(g, S)[2], S

def check(G, start, V, xsim=True):
    g = Gen(G); N = g.N; pi = topo(G); pos = {v: i for i, v in enumerate(pi)}
    if len(pi) != N or any(o[1] >= 0 and pos[o[1]] <= pos[v] for v in range(N) for o in g.opts[v]): V["TOPO"] += 1; return None
    S, AS = g.run(start); T = len(S) - 1; D = max(len(o) for o in g.opts); deg2 = D <= 2
    if xsim:
        G2 = dict(G); G2["start"] = list(start); R = ref_run(G2)[0]
        if [tuple(x) for x in R] != S: V["XSIM"] += 1
    F = [[g.face(S[t], v, S[t][v]) for v in range(N)] for t in range(T + 1)]
    for t in range(1, T + 1):
        if any(F[t][v] < F[t - 1][v] for v in range(N)): V["MONO"] += 1
    h, ch, U = labels(g, S)
    for t in range(2, T + 1):
        mv = [v for v in range(N) if S[t][v] != S[t - 1][v]]; lmin = min(g.lev[v] for v in mv)
        for x in [v for v in mv if g.lev[v] == lmin]:
            w = S[t][x]
            if w in AS[t - 2][x]: V["XINEW"] += 1
            pl = g.play(S[t - 2], x, w); Z = [z for z in pl if S[t - 1][z] != S[t - 2][z]]
            if not (g.face(S[t - 1], x, w) > g.face(S[t - 2], x, w)) or not Z or any(pos[z] <= pos[x] for z in Z): V["RISE"] += 1
        if ch[t] and not pos[h[t]] < pos[h[t - 1]]: V["CHAIN"] += 1
    if T > N * (1 + U): V["CHAIN"] += 1
    C = [[g.cnt(S[t], v) for v in range(N)] for t in range(T + 1)]
    E = [sum(C[t][v] * D ** pos[v] for v in range(N)) for t in range(T + 1)]
    RANK = [None] * (T + 1)
    for t in range(1, T + 1):
        mv = [v for v in range(N) if S[t][v] != S[t - 1][v]]; y = max(mv, key=lambda v: pos[v])
        if C[t - 1][y] == 0 or not C[t][y] < C[t - 1][y] or any(C[t][v] != C[t - 1][v] for v in range(N) if pos[v] > pos[y]) \
           or not E[t] < E[t - 1]: V["DECR"] += 1
        RANK[t] = 1 + sum(1 for v in range(N) if C[t - 1][v] > 0 and pos[v] > pos[y])
    res = {"N": N, "T": T, "U": U, "D": D}
    if not deg2: return res
    KF = [0] * N; mvs = [0] * N
    for t in range(1, T + 1):
        k0, k1 = g.keys(S[t - 1]), g.keys(S[t])
        for x in range(N):
            if len(g.opts[x]) < 2: continue
            kp0 = min(range(2), key=lambda k: g.optkey(k0, x, k)); kp1 = min(range(2), key=lambda k: g.optkey(k1, x, k))
            KF[x] += kp0 != kp1; mvs[x] += S[t][x] != S[t - 1][x]
    if any(mvs[x] > 1 + KF[x] for x in range(N)) or T > sum(1 + k for k in KF) or sum(KF) > N * T: V["KEYFLIP"] += 1
    def TOP(t, k):
        L = sorted((pos[v] for v in range(N) if C[t][v] > 0), reverse=True)[:k]; return tuple(L) + (-1,) * (k - len(L))
    for k in range(1, N + 1):
        for t in range(1, T + 1):
            a, b = TOP(t - 1, k), TOP(t, k)
            if b > a or (b < a) != (RANK[t] <= k): V["TOPMONO"] += 1
        if sum(1 for t in range(1, T + 1) if RANK[t] <= k) > sum(comb(N, j) for j in range(k + 1)) - 1: V["RBOUND"] += 1
    R = max([RANK[t] for t in range(2, T + 1) if not ch[t]], default=0)
    if U > sum(comb(N, j) for j in range(R + 1)) - 1: V["RBOUND"] += 1
    for r in range(2, N + 1):
        if sum(1 for t in range(1, T + 1) if RANK[t] == r) > (N - r + 1) * (1 + sum(1 for t in range(1, T + 1) if RANK[t] <= r - 1)):
            V["ICHARGE"] += 1
    for k in range(1, N + 1):
        a = 0; ivs = []
        for t in range(1, T + 2):
            if t == T + 1 or TOP(t, k) != TOP(a, k): ivs.append((a, t)); a = t
        for (a, b) in ivs:
            pk = TOP(a, k)[k - 1]; keep = [v for v in range(N) if pos[v] >= pk] if pk >= 0 else list(range(N))
            if any(S[t][v] != S[t - 1][v] for t in range(a + 1, b) for v in keep): V["RESTR"] += 1; continue
            H = restrict(G, keep, S[a]); gh = Gen(H); SH, _ = gh.run(H["start"])
            pref = [tuple(S[a][v] if v in keep else s[v] for v in range(N)) for s in SH[: b - a]]
            # H's states record option index 0 at kept movers; map back for comparison
            if len(SH) < b - a or pref != [tuple(x) for x in S[a:b]]: V["RESTR"] += 1; continue
            hh, chh, _ = labels(gh, SH)
            if any(chh[t - a] != ch[t] for t in range(a + 2, b)): V["RESTR"] += 1
        if k == 1:
            tot = 0
            for (a, b) in ivs:
                p1 = TOP(a, 1)[0]
                if p1 < 0: continue
                H = restrict(G, [v for v in range(N) if pos[v] >= p1], S[a]); tot += Uof(H)[0] + 1
            if U > (len(ivs) - 1) + tot: V["REC"] += 1
            if U > tot: V["REC148"] += 1
    res["KF"] = sum(KF); res["R"] = R
    return res

if __name__ == "__main__":
    ALL = os.environ.get("ALL"); ALLN = int(os.environ.get("ALLN", "10"))
    keysV = ["XSIM", "TOPO", "MONO", "XINEW", "RISE", "CHAIN", "KEYFLIP", "DECR", "TOPMONO", "RBOUND", "RESTR", "ICHARGE", "REC"]
    TOT = {k: 0 for k in keysV + ["REC148"]}; runs = 0; steps = 0
    for p in sys.argv[1:]:
        G = json.load(open(p)); V = {k: 0 for k in TOT}
        starts = [G["start"]]
        if ALL and G["N"] <= ALLN: starts = [list(s) for s in itertools.product(*[range(len(o)) for o in G["opts"]])]
        mx = None
        for st in starts:
            r = check(G, st, V, xsim=(st == G["start"] or len(starts) <= 64))
            runs += 1
            if r: steps += r["T"]
            if st == G["start"]: mx = r
        for k in V: TOT[k] += V[k]
        print(f"P-IDEAL-RED {os.path.basename(p)} N {mx['N']} D {mx['D']} T {mx['T']} U {mx['U']} KF {mx.get('KF','-')} R {mx.get('R','-')} "
              f"runs {len(starts)} " + " ".join(f"{k} {V[k]}" for k in keysV) + f" (REC148 {V['REC148']})")
    print(f"TOTAL genomes {len(sys.argv) - 1} runs {runs} steps {steps} " + " ".join(f"{k} {TOT[k]}" for k in keysV)
          + f" VIOL {sum(TOT[k] for k in keysV)} (info REC148 {TOT['REC148']})")
