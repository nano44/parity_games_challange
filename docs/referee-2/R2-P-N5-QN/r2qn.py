#!/usr/bin/env python3
"""REFEREE-2 successor 35: own replay of packet P-N5-QN (L-NEW 68, claude/l-new e252182d) on IDEAL-CYC(G). Builder, VJ values / order and
Odd's optimal counterstrategy are REFEREE-2's own R2-P-ACYC/r2acyc.py (successor 32); genome generator from R2-P-N5-QUIET/r2quiet.py
(levels, Ξ-targets anywhere incl. upward and self). Howard at the movers (keep σ(x) if best, else the largest best option). No lane code.
Counters (all must be 0 unless marked):
  gc     (step, gate) flips of σ̄(g) with neither e_g's nor β_g's class changing                            GATE-CLASS
  gf     gates with flips(g) > (D^tot(e_g) − 1) + (D^tot(β_g) − 1)                                         GATE-FLIP (a)
  cpay   (record) gates with flips(g) > 2·min(D^tot(e_g) − 1, D^tot(β_g) − 1) + 1  (L-RED's CLASS-PAYS, not signed here)
  qnotp  quiet steps that are not p-steps (some Λ or some Odd σ̄ changes)                                  QUIET-N
  qwin   quiet windows longer than N;  Tq  runs with T > Q + (Q + 1)·N;  qsum  runs with Q > Σ_v (D^tot(v) − 1)
  lam    states where Λ over v ∉ {c_W, c_X, e → c_W} takes more than k + 1 values (k = exact Ξ-feedback number)  (k+1)-Λ
  lamid  states where some such Λ is neither K1 nor the most relevant vertex of the Γ-cycle of a cycle of Ξ_σ    (k+1)-Λ, the values
  lamid_mover (record) states where some such Λ is a mover (the statement's literal reading «most relevant vertex of a cycle of Ξ_σ
         on the movers» would need this)
Per run (record): T, Q, longest quiet window W, max flips(g) with its lamch(g) (Λ changes at e_g or β_g) and face heights; max ascents
of e-sequences (seq_t(v) = e-vertices of Π_t(v) in play order).
Controls: --ctrl: GATE-CLASS looks at e_g's class only; GATE-FLIP's bound uses e_g only; window bound N := 0; (k+1)-Λ bound k;
  lamid allows K1 only; qnotp counts quiet steps that ARE p-steps; qsum bound 0.
Usage: r2qn.py [--ctrl] [--gen COUNT SEED] FILES.json ..."""
import sys, os, json, random, itertools
from functools import cmp_to_key
H = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [os.path.join(H, "..", "R2-P-ACYC"), os.path.join(H, "..", "R2-P-N5-QUIET")]
import r2acyc as A
import r2quiet as Q_

def kfb(G):
    N = G["N"]; adj = {x: {o[1] for o in G["opts"][x] if o[1] >= 0} for x in range(N)}
    def acyc(rem):
        col = {}
        def dfs(u):
            col[u] = 1
            for w in adj[u]:
                if w in rem: continue
                if col.get(w) == 1 or (col.get(w) is None and not dfs(w)): return False
            col[u] = 2; return True
        return all(x in rem or col.get(x) == 2 or dfs(x) for x in range(N))
    for k in range(N + 1):
        if k > 3 and N > 30: return None          # exact search too costly: (k+1)-Λ not counted on this genome (lamskip)
        for S in itertools.combinations(range(N), k):
            if acyc(set(S)): return k
    return N

def run(G, R, ctrl):
    g = A.build(G, False); vj = A.VJ(g); V = g["V"]; succ = g["succ"]; rel = vj.rel; n = g["n"]; N = g["N"]; cmp = vj.cmp
    O = g["O"]; ev = {V[("e", o)] for o in O}; K1, cW, cX = V["K1"], V["cW"], V.get("unused")   # r2acyc names c_X «unused»
    exc = {cW} | {V[("e", o)] for o in O if G["opts"][o[0]][o[1]][0] < 0}
    if cX is not None: exc.add(cX)
    movers = [V[("x", x)] for x in range(N)]; mset = set(movers)
    gates = [(V[("g", o)], V[("e", o)], V[("b", o)]) for o in O]
    odd = [v for v in range(n) if g["owner"][v] == 1 and len(succ[v]) > 1]
    k = kfb(G)
    if k is None: R["lamskip"] += 1; kb = 10 ** 9
    else: kb = k - 1 if ctrl else k
    ms = list(G["start"]); st = []
    while True:
        sig = A.mover_sig(g, ms); tau, val = A.odd_opt(g, vj, sig, A.worst_start(g)); st.append((sig, tau, val))
        # (k+1)-Λ at this state
        f = [sig[v] if g["owner"][v] == 0 else tau[v] for v in range(n)]
        lams = {val[v][0] for v in range(n) if v not in exc}
        if len(lams) > kb + 1: R["lam"] += 1
        # allowed values: K1 and, for each cycle of Ξ_σ, the most relevant vertex of the Γ-cycle through it
        allowed = {K1}; seen = set()
        for x0 in movers:
            path = []; x = x0; pos = {}
            while x not in pos and x not in seen:
                pos[x] = len(path); path.append(x); gv = f[x]; bv = [w for w in succ[gv] if w not in ev][0]; x = f[bv]
                if x not in mset: break
            if x in pos:
                cyc = []; y = x
                while True:
                    gv = f[y]; bv = [w for w in succ[gv] if w not in ev][0]; cyc += [y, gv, bv]; y = f[bv]
                    if y == x: break
                allowed.add(max(cyc, key=lambda u: rel[u]))
            seen |= set(path)
        if any(l not in (({K1}) if ctrl else allowed) for l in lams): R["lamid"] += 1
        if any(l in mset for l in lams): R["lamid_mover"] += 1
        new = list(ms); ch = False
        for x in range(N):
            xv = V[("x", x)]; cur = sig[xv]; best = max(succ[xv], key=cmp_to_key(lambda a, b: cmp(val[a], val[b])))
            if cmp(val[best], val[cur]) > 0:
                bl = [w for w in succ[xv] if cmp(val[w], val[best]) == 0]; new[x] = succ[xv].index(max(bl)); ch = True
        if not ch: break
        ms = new
        if len(st) > 50 * n: raise RuntimeError("Howard too long")
    T = len(st) - 1
    cls = [[(val[v][0], frozenset(u for u in val[v][1] if u in ev)) for v in range(n)] for _, _, val in st]
    D = [len({cls[t][v] for t in range(T + 1)}) for v in range(n)]
    flips = {gv: 0 for gv, _, _ in gates}; lamch = {gv: 0 for gv, _, _ in gates}
    Q = W = cur = 0
    for t in range(1, T + 1):
        loud = cls[t] != cls[t - 1]
        for gv, e, b in gates:
            if st[t][2][e][0] != st[t - 1][2][e][0] or st[t][2][b][0] != st[t - 1][2][b][0]: lamch[gv] += 1
            if st[t][1][gv] != st[t - 1][1][gv]:
                flips[gv] += 1
                ce = cls[t][e] != cls[t - 1][e]; cb = cls[t][b] != cls[t - 1][b]
                if not (ce or (cb and not ctrl)): R["gc"] += 1
        if loud: Q += 1; cur = 0; continue
        cur += 1; W = max(W, cur)
        if cur > (0 if ctrl else N): R["qwin"] += 1
        if any(st[t][2][v][0] != st[t - 1][2][v][0] for v in range(n)) or any(st[t][1][v] != st[t - 1][1][v] for v in odd) != ctrl: R["qnotp"] += 1
    for gv, e, b in gates:
        if flips[gv] > (D[e] - 1) + (0 if ctrl else D[b] - 1): R["gf"] += 1
        if flips[gv] > 2 * min(D[e] - 1, D[b] - 1) + 1: R["cpay"] += 1
    sumD = sum(d - 1 for d in D)
    if T > Q + (Q + 1) * (0 if ctrl else N): R["Tq"] += 1
    if Q > (0 if ctrl else sumD): R["qsum"] += 1
    gm = max(gates, key=lambda q: flips[q[0]])
    # max ascents of e-sequences over all states / vertices
    masc = 0
    for sig, tau, val in st:
        f = [sig[v] if g["owner"][v] == 0 else tau[v] for v in range(n)]
        for v in range(n):
            seq = []; u = v; seen = set()
            while u not in seen:
                seen.add(u)
                if u in ev and u in val[v][1]: seq.append(u)
                u = f[u]
            masc = max(masc, sum(1 for a, b in zip(seq, seq[1:]) if rel[b] > rel[a]))
    return dict(N=N, M=g["M"], k=k, T=T, Q=Q, W=W, maxflips=flips[gm[0]], lamch=lamch[gm[0]], faces=(D[gm[1]], D[gm[2]]), maxasc=masc,
                C=sum(1 for t in range(1, T + 1) if any(st[t][2][v][0] != st[t - 1][2][v][0] for v in range(n))))

KEYS = ["runs", "lamskip", "gc", "gf", "qnotp", "qwin", "Tq", "qsum", "lam", "lamid", "cpay", "lamid_mover"]
if __name__ == "__main__":
    a = sys.argv[1:]; ctrl = "--ctrl" in a; a = [x for x in a if x != "--ctrl"]; Gs = []
    while a:
        if a[0] == "--gen":
            cnt, seed = int(a[1]), int(a[2]); rng = random.Random(seed); Gs += [(f"gen{seed}#{j}", Q_.gen(rng)) for j in range(cnt)]; a = a[3:]
        else:
            G = json.load(open(a[0]))
            if isinstance(G, dict) and "genome" in G: G = G["genome"]
            if isinstance(G, dict) and "opts" in G and "start" in G: Gs.append((os.path.basename(a[0]), G))
            else: print(os.path.basename(a[0]), "skipped (not a genome)")
            a = a[1:]
    R = {kk: 0 for kk in KEYS}; mx = {}
    for name, G in Gs:
        r = run(G, R, ctrl); R["runs"] += 1
        for kk in ("T", "W", "maxflips", "maxasc", "k"): mx[kk] = max(mx.get(kk, 0), r[kk] if r[kk] is not None else -1)
        if not name.startswith("gen"): print(name, " ".join(f"{kk} {v}" for kk, v in r.items()), flush=True)
    print("TOTAL" + (" CTRL" if ctrl else "") + ": " + " ".join(f"{kk} {R[kk]}" for kk in KEYS) + " | max " + " ".join(f"{kk} {v}" for kk, v in mx.items()))
