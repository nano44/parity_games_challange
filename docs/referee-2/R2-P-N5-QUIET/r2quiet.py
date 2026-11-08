#!/usr/bin/env python3
"""REFEREE-2 successor 33: own replay of packet P-N5-QUIET (L-NEW 62/63, claude/l-new 9329859d / d9c49489 / df0d2a25) on IDEAL-CYC(G).
Shares no code with L-NEW, L-RED, L-SI or REFEREE: builder, VJ values / order, Odd's optimal counterstrategy (switch-all strict Odd PI
from two starts) and the brute force over all Odd strategies are REFEREE-2's own R2-P-ACYC/r2acyc.py (successor 32); Howard at the
movers and every counter below are written here from the packet's / R118's TEXT.
Howard (R118 (a)): every mover goes to a ⊴-largest successor and keeps σ(x) if σ(x) is one (ties among new ones: largest vertex id).
Per state t (unit (state, vertex) or (state, gate) or state):
  cn2      Λ_t(v) of priority < 2                               (CN2, on the run's pairs; cn2rand: random positional pairs)
  loc      σ̄_t(g) is not the face of strictly ⊴-smaller value (LOC-GATE), ties counted separately (NO-TIE: ties must be 0)
  k2a/k2b  σ̄_t(K2) ≠ K1 / not Ω_t(K1) ◁ Ω_t(K2)                 (LOC-K2, both conjuncts)
  bonly    v ∉ {c_W} ∪ {e with successor c_W} and Λ_t(v) not less relevant than every e-vertex (B-ONLY)
  pidep    the two Odd-PI starts give different σ̄ (σ̄ is then not unique; values compared too: pival)
  brute    (M ≤ BR) values differ from the pointwise minimum over ALL Odd positional strategies, or no pointwise optimum ([OPT])
Per run (classes (Λ, E), E = e-vertices of Π):
  Q (loud steps), W (longest quiet window, steps), L = (M+1)(2M+1)(N+1) + N(n-1) EXACT, wfail (windows with > L steps),
  Tfail (T > Q + (Q+1)L), TQfail (T > (1 + Σ_v (D^tot_E(v) - 1))(L + 1)), Qsum (Q > Σ_v (D^tot_E(v) - 1)),
  crossflip (σ̄ flips on a quiet step at a gate whose faces are in different classes), q2a (quiet step: chosen gate's class ≠ class(x)),
  q2b (quiet step t → t+1: some gate of mover x in a class strictly above class(x) at t), backflip (quiet step: gate with both faces
  in one class flips e → β), multiflip ((window, gate) pairs with both faces in one class and ≥ 2 flips), Lnew = (M+1)(N+1) for info.
--gamma3: the same replay on Γ3(G) (R117 pads; Howard at the movers of Γ3, NOT N5′-xi's S4a tie rule; DATA for the
  Γ3 scope question only). Usage: r2quiet.py [--gamma3] [--eorder gate|lev] [--brute M] [--rand K --seed S] FILES.json|SET.jsonl ...
       r2quiet.py gen COUNT SEED OUT.jsonl  (own random genomes: levels, Ξ-targets anywhere incl. upward and self, W-targets one level down)"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(H, "..", "R2-P-ACYC"))
import r2acyc as A
from functools import cmp_to_key


def gen(rng):
    d = rng.randint(1, 5); w = [rng.randint(1, 3) for _ in range(d)]
    lev = [l for l in range(d) for _ in range(w[l])]; N = len(lev); byl = [[x for x in range(N) if lev[x] == l] for l in range(d)]
    opts = []; b = 0
    for x in range(N):
        ox = []
        for _ in range(rng.randint(1, 3)):
            wt = rng.choice(byl[lev[x] - 1]) if lev[x] else -1
            xt = rng.choice([-1] + list(range(N)))
            ox.append([wt, xt, b]); b += 1
        opts.append(ox)
    M = b; gp = rng.sample(range(M), M); gate = []; i = 0
    for x in range(N): gate.append(gp[i:i + len(opts[x])]); i += len(opts[x])
    return dict(N=N, lev=lev, opts=opts, gate=gate, br=rng.sample(range(M), M), bp=[rng.randint(0, 1) for _ in range(M)],
                start=[rng.randrange(len(opts[x])) for x in range(N)])


PADS = False
def replay(G, R, BR, rng, K):
    g = A.build(G, PADS); vj = A.VJ(g); V = g["V"]; succ = g["succ"]; prio = g["prio"]; rel = vj.rel; n = g["n"]; N = g["N"]; M = g["M"]
    cmp = vj.cmp; K1, K2, cW = V["K1"], V["K2"], V["cW"]
    K2to = V["r"] if PADS else K1     # Γ3: K2 → r → K1
    ev = {V[("e", o)] for o in g["O"]}; emin = min(rel[e] for e in ev)
    excl = {cW}          # c_W and every single-successor vertex leading into it (level-0 e's; on Γ3 also their pe-pads)
    while True:
        add = {v for v in range(n) if v not in excl and len(succ[v]) == 1 and succ[v][0] in excl}
        if not add: break
        excl |= add
    gates = [(V[("g", o)], succ[V[("g", o)]][0], succ[V[("g", o)]][1]) for o in g["O"]]   # the gate's two successors (Γ: e, β; Γ3: pads)
    L = (M + 1) * (2 * M + 1) * (N + 1) + N * (n - 1)   # on Γ3 (PADS) n = n3 = N + 7M + 10: the bound QUIET would give if it transferred
    def cls(val, v): return (val[v][0], frozenset(u for u in val[v][1] if u in ev))
    def ccmp(a, b):          # class order: reward of Λ, then E lex (e-vertices are even: more is better)
        if a == b: return 0
        if a[0] != b[0]: return 1 if vj.rew[a[0]] > vj.rew[b[0]] else -1
        m = max(a[1] ^ b[1], key=lambda u: rel[u]); return 1 if m in a[1] else -1
    ms = list(G["start"]); states = []
    while True:
        sig = A.mover_sig(g, ms)
        tau, val = A.odd_opt(g, vj, sig, A.worst_start(g)); tau2, val2 = A.odd_opt(g, vj, sig, None)
        R["pidep"] += tau2 != tau; R["pival"] += val2 != val
        if M <= BR:
            cnt, mins, _ = A.brute(g, vj, sig); R["brute_states"] += 1
            R["brute"] += cnt == 0 or any(mins[v] != val[v] for v in range(n))
        R["states"] += 1
        for v in range(n):
            R["pairs"] += 1; R["cn2"] += prio[val[v][0]] < 2
            if v not in excl:
                R["bonly_units"] += 1; R["bonly"] += rel[val[v][0]] >= emin
        for gv, ef, bf in gates:
            R["gatestates"] += 1; c = cmp(val[ef], val[bf])
            if c == 0: R["ties"] += 1
            elif tau[gv] != (ef if c < 0 else bf): R["loc"] += 1
        R["k2a"] += tau[K2] != K2to; R["k2b"] += not cmp(val[K1], val[K2]) < 0
        states.append((tuple(ms), tau, val))
        new = list(ms); ch = False
        for x in range(N):
            xv = V[("x", x)]; cur = sig[xv]; best = max(succ[xv], key=cmp_to_key(lambda a, b: cmp(val[a], val[b])))
            if cmp(val[best], val[cur]) > 0:
                bl = [w for w in succ[xv] if cmp(val[w], val[best]) == 0]; new[x] = succ[xv].index(max(bl)); ch = True
        if not ch: break
        ms = new
        if len(states) > 50 * n: raise RuntimeError("Howard too long")
    T = len(states) - 1; C = [[cls(val, v) for v in range(n)] for _, _, val in states]
    Q = W = cur = 0; wins = []; ws = 0
    for t in range(1, T + 1):
        if C[t] != C[t - 1]:
            Q += 1
            if cur: wins.append((ws, t - 1))
            cur = 0; ws = t; continue
        cur += 1; W = max(W, cur)
        (ms0, ta, va), (ms1, tb, vb) = states[t - 1], states[t]
        for gv, ef, bf in gates:
            if ta[gv] != tb[gv]:
                if C[t][ef] != C[t][bf]: R["crossflip"] += 1
                elif tb[gv] == bf: R["backflip"] += 1
        sg0 = A.mover_sig(g, ms0)
        for x in range(N):
            xv = V[("x", x)]; sg = sg0[xv]
            R["q2a"] += C[t - 1][sg] != C[t - 1][xv]
            R["q2b"] += any(ccmp(C[t - 1][w], C[t - 1][xv]) > 0 for w in succ[xv])
    if cur: wins.append((ws, T))
    for a, b in wins:
        R["windows"] += 1; R["wfail"] += (b - a) > L
        for gv, ef, bf in gates:
            if C[a][ef] == C[a][bf] and sum(states[t][1][gv] != states[t - 1][1][gv] for t in range(a + 1, b + 1)) >= 2: R["multiflip"] += 1
    sumD = sum(len({C[t][v] for t in range(T + 1)}) - 1 for v in range(n))
    R["Tfail"] += T > Q + (Q + 1) * L; R["TQfail"] += T > (1 + sumD) * (L + 1); R["Qsum"] += Q > sumD
    # CN2 on random positional pairs (every positional pair: random σ at movers, random τ)
    for _ in range(K):
        s2 = A.mover_sig(g, [rng.randrange(len(G["opts"][x])) for x in range(N)])
        f = [s2[v] if g["owner"][v] == 0 else rng.choice(succ[v]) for v in range(n)]
        vv = vj.values(f); R["cn2rand_units"] += n; R["cn2rand"] += sum(prio[vv[v][0]] < 2 for v in range(n))
    return dict(N=N, M=M, n=n, T=T, Q=Q, W=W, L=L, sumDE=sumD, DEtot=max(len({C[t][v] for t in range(T + 1)}) for v in range(n)))


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "cmp":       # T on Γ vs T3 on Γ3 (Howard at the movers on both, own code), per genome; e-order lev
        from collections import Counter; A.EORDER = "lev"; C = Counter()
        for f in a[1:]:
            for G in ([json.loads(l) for l in open(f)] if f.endswith(".jsonl") else [json.load(open(f))]):
                R0 = Counter(); PADS = False; t = replay(G, R0, 0, random.Random(1), 0)["T"]
                PADS = True; t3 = replay(G, R0, 0, random.Random(1), 0)["T"]
                C["genomes"] += 1; C["T3_ne_T"] += t3 != t; C["T3_gt_T"] += t3 > t; C["maxT"] = max(C["maxT"], t); C["maxT3"] = max(C["maxT3"], t3)
            print(os.path.basename(f), " ".join(f"{k} {v}" for k, v in sorted(C.items())), flush=True); C = Counter()
        sys.exit()
    if a[0] == "gen":
        rng = random.Random(int(a[2]))
        with open(a[3], "w") as f:
            for _ in range(int(a[1])): f.write(json.dumps(gen(rng)) + "\n")
        sys.exit()
    BR = 0; K = 0; seed = 1; files = []; i = 0
    while i < len(a):
        if a[i] == "--brute": BR = int(a[i + 1]); i += 2
        elif a[i] == "--rand": K = int(a[i + 1]); i += 2
        elif a[i] == "--seed": seed = int(a[i + 1]); i += 2
        elif a[i] == "--eorder": A.EORDER = a[i + 1]; i += 2
        elif a[i] == "--gamma3": PADS = True; i += 1
        else: files.append(a[i]); i += 1
    rng = random.Random(seed); from collections import Counter
    for f in files:
        R = Counter({k: 0 for k in ('cn2', 'loc', 'ties', 'k2a', 'k2b', 'bonly', 'pidep', 'pival', 'brute', 'crossflip', 'backflip',
                                    'multiflip', 'q2a', 'q2b', 'wfail', 'Tfail', 'TQfail', 'Qsum')}); agg = Counter(); cnt = 0
        items = [json.loads(l) for l in open(f)] if f.endswith(".jsonl") else [json.load(open(f))]
        for G in items:
            r = replay(G, R, BR, rng, K); cnt += 1
            for k in ("T", "W", "DEtot"): agg["max" + k] = max(agg["max" + k], r[k])
            agg["maxWoverN"] = max(agg["maxWoverN"], round(r["W"] / r["N"], 3))
        info = " ".join(f"{k} {r[k]}" for k in ("N", "M", "n", "T", "Q", "W", "L", "DEtot", "sumDE")) if cnt == 1 else \
            f"genomes {cnt} " + " ".join(f"{k} {v}" for k, v in sorted(agg.items()))
        print(os.path.basename(f), "EORDER", A.EORDER, "GAMMA3" if PADS else "GAMMA", "|", info, "|", " ".join(f"{k} {v}" for k, v in sorted(R.items())), flush=True)
