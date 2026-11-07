#!/usr/bin/env python3
"""L-NEW box 162: machine checks (DATA, not proofs) for packet P-IDEAL-FLIP, on 2-wide degree-2 ladders in L-RED's R197 convention
(class LR: levels 0..d-1, movers 2l, 2l+1 on level l, degree 2, option k of a level-l >= 1 mover W-points to mover 2(l-1)+k).
Simulator: the box 150 checker's Gen (box150/check.py; IDEAL step rule of RESULTS R104's definition).
c-step (packet §1): level-0 movers stay; a level-1 option pointing to level-0 mover w gets the key (kappa^c_w, own gate) with
kappa^1 = (0, 1), kappa^0 = (1, 0); higher keys are built as usual; A-sets are the IDEAL A-sets under the old state.
Checks (each prints a count line; the packet's check.sh block greps them):
  WONLY  real step on levels >= 1 = c-step with c = b_0(new state)      (random LR genomes, ISO and not, + every LR genome in
         box160/out and box162/out; every start for d <= 4)
  ISOA   under ISO, the A-sets of levels >= 1 do not depend on the level-0 options     (random ISO genomes, random states)
  FROZ   run of H_q (level 0 frozen at q) = forced run with constant c = b_0(q), same states, same length
  CONS   real ISO run: b_0 changes <= 2, and #(steps moving a level >= 1 mover) <= V_2(G, s_0)  (V_k: exact per-genome max, below)
  SWAP   c-step of G at 1 - c = c-step of G^swap at c (level-1 W-targets exchanged)   (+ control SWAPNEG: G^swap at 1 - c differs)
  NOWONCE real runs: on a maximal interval with b_0 constant, each level-1 mover moves <= 1  (+ control: level-1 double moves overall)
  FLIP1  m = 1 (d = 2) ISO genomes, every start: V_0 <= 2 and V_k <= 3 for k <= 6
  INST   instance box160/out/iso_d4_st9.json: LR, ISO, T 11, level-0 steps [7, 8], seg1 6, tail 3
  WIT    V_k on the SAT witnesses box162/out/kf<k>_d<d>_t<t>.json (lower bounds of the T_k(m) table)
V_k(G, s_0) := max over bit sequences c_1, c_2, ... with <= k changes of #{t : u_t != u_(t-1)}, u_t = c_t-step(u_(t-1)) (exact,
memoised search over (state, c, flips left); a flip without a step is a flip at the next frame).
Usage: flipcheck.py [seed] [count]   (env NEG=1: break the c-step (kappa ignored: always c = 1); WONLY / SWAP / FROZ must then fire)"""
import os, sys, json, random, glob
sys.setrecursionlimit(100000)
H = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": P}; exec(open(P).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]; restrict = ns["restrict"]
NEG = os.environ.get("NEG", "0")

def rand_lr(d, rng, iso=True):
    N = 2 * d; lev = [v // 2 for v in range(N)]
    order = list(range(N)); rng.shuffle(order); pos = {v: i for i, v in enumerate(order)}
    opts, M = [], 0
    for x in range(N):
        o = []
        for k in range(2):
            wt = 2 * (lev[x] - 1) + k if lev[x] > 0 else -1
            later = [v for v in range(N) if pos[v] > pos[x] and (lev[v] > 0 or not iso)]
            xt = rng.choice(later) if later and rng.random() < 0.8 else -1
            o.append([wt, xt, M]); M += 1
        opts.append(o)
    g = list(range(M)); rng.shuffle(g); it = iter(g); gate = [[next(it), next(it)] for _ in range(N)]
    br = list(range(M)); rng.shuffle(br); bp = [rng.randint(0, 1) for _ in range(M)]
    return {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": bp, "start": [rng.randint(0, 1) for _ in range(N)],
            "xorder": order}

def is_lr(G):
    N = G["N"]; d = N // 2
    if N % 2 or G["lev"] != [v // 2 for v in range(N)]: return False
    return all(len(G["opts"][x]) == 2 and all(G["opts"][x][k][0] == (2 * (G["lev"][x] - 1) + k if G["lev"][x] > 0 else -1)
                                               for k in (0, 1)) for x in range(N))

def is_iso(G): return all(o[1] not in (0, 1) for oo in G["opts"] for o in oo)

def b0(g, s): return int(g.gate[0][s[0]] < g.gate[1][s[1]])

def cstep(g, s, c):
    """the c-step from state s (tuple); level-0 options kept"""
    kap = (0, 1) if (c == 1 or NEG == "1") else (1, 0)
    A = [g.avail(s, v) for v in range(g.N)]; key = [None] * g.N; nw = list(s)
    def ok(v, k):
        wt = g.opts[v][k][0]
        if g.lev[v] == 0: return (g.gate[v][k],)
        if g.lev[v] == 1: return (kap[wt], g.gate[v][k])
        return key[wt] + (g.gate[v][k],)
    for v in g.byl:
        k = s[v] if g.lev[v] == 0 else min(A[v], key=lambda k: ok(v, k))
        nw[v] = k; key[v] = ok(v, k)
    return tuple(nw)

def up(g, s): return tuple(s[v] for v in range(g.N) if g.lev[v] >= 1)

def Vk(g, s0, k):
    memo, onstack = {}, set()
    def best(u, c, f):
        kk = (u, c, f)
        if kk in memo: return memo[kk]
        if kk in onstack: raise RuntimeError("cycle in forced dynamics")
        onstack.add(kk); u2 = cstep(g, u, c); r = (1 + best(u2, c, f)) if up(g, u2) != up(g, u) else 0
        if f > 0: r = max(r, best(u, 1 - c, f - 1))
        onstack.discard(kk); memo[kk] = r; return r
    return max(best(tuple(s0), c, k) for c in (0, 1))

def swapped(G):
    S = json.loads(json.dumps(G))
    for x in range(G["N"]):
        if G["lev"][x] == 1:
            for k in (0, 1): S["opts"][x][k][0] = 1 - G["opts"][x][k][0]
    return S

def allstates(N):
    for m in range(1 << N): yield tuple((m >> v) & 1 for v in range(N))

def main():
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 162; cnt = int(sys.argv[2]) if len(sys.argv) > 2 else 300
    rng = random.Random(seed); C = dict.fromkeys(["WONLY", "ISOA", "FROZ", "CONS", "SWAP", "SWAPNEG", "NOWONCE", "NOWCTRL", "FLIP1"], 0)
    nrun = nsteps = nstate = 0; n = dict.fromkeys(["WONLY", "ISOA", "FROZ", "CONS", "SWAP", "NOWONCE", "FLIP1"], 0)
    corpus = sorted(glob.glob(os.path.join(H, "..", "box160", "out", "*.json")) + glob.glob(os.path.join(H, "out", "*.json")))
    corpus = [json.load(open(f)) for f in corpus]; corpus = [G for G in corpus if is_lr(G)]; ncorp = len(corpus)
    for i in range(cnt + ncorp):
        if i < cnt: d = 2 + i % 3; iso = (i % 4 != 3); G = rand_lr(d, rng, iso)
        else: G = corpus[i - cnt]; d = G["N"] // 2; iso = is_iso(G)
        g = Gen(G); N = G["N"]
        Gs = swapped(G); gs = Gen(Gs)
        for s0 in (allstates(N) if d <= 4 else [tuple(rng.randint(0, 1) for _ in range(N)) for _ in range(40)]):
            S, _ = g.run(s0); nrun += 1; nsteps += len(S) - 1
            for t in range(1, len(S)):   # WONLY
                n["WONLY"] += 1
                if up(g, S[t]) != up(g, cstep(g, S[t - 1], b0(g, S[t]))): C["WONLY"] += 1
            # NOW-ONCE on maximal intervals with b_0 constant (over the states s_t, t in the interval)
            last = {};
            for t in range(1, len(S)):
                for x in (2, 3):
                    if S[t][x] != S[t - 1][x]:
                        if x in last and all(b0(g, S[u]) == b0(g, S[t]) for u in range(last[x], t + 1)): C["NOWONCE"] += 1
                        if x in last: C["NOWCTRL"] += 1; n["NOWONCE"] += 1
                        last[x] = t
            if iso:
                n["CONS"] += 1; fl = sum(1 for t in range(1, len(S)) if b0(g, S[t]) != b0(g, S[t - 1]))
                nu = sum(1 for t in range(1, len(S)) if up(g, S[t]) != up(g, S[t - 1]))
                if fl > 2 or nu > Vk(g, s0, 2): C["CONS"] += 1
        if iso:
            for _ in range(30):
                s = tuple(rng.randint(0, 1) for _ in range(N)); nstate += 1
                for q in allstates(2):   # ISOA
                    s2 = q + s[2:]; n["ISOA"] += 1
                    if any(g.avail(s, v) != g.avail(s2, v) for v in range(2, N)): C["ISOA"] += 1
                for c in (0, 1):   # SWAP
                    n["SWAP"] += 1
                    if up(g, cstep(g, s, 1 - c)) != up(g, cstep(gs, s, c)): C["SWAP"] += 1
                    if up(g, cstep(g, s, 1 - c)) != up(g, cstep(gs, s, 1 - c)): C["SWAPNEG"] += 1
            for q in allstates(2):   # FROZ
                n["FROZ"] += 1; sa = q + tuple(G["start"][2:]); Hq = restrict(G, [0, 1], sa); Sh, _ = Gen(Hq).run(tuple(0 if v < 2 else sa[v] for v in range(N)))
                cur = sa; Sf = [up(g, cur)]
                while True:
                    nw = cstep(g, cur, b0(g, sa))
                    if up(g, nw) == up(g, cur): break
                    cur = nw; Sf.append(up(g, cur))
                if [up(g, x) for x in Sh] != Sf: C["FROZ"] += 1
            if d == 2:
                for s0 in allstates(N):
                    v = [Vk(g, s0, k) for k in range(7)]; n["FLIP1"] += 1
                    if v[0] > 2 or max(v) > 3: C["FLIP1"] += 1
    print(f"RANDOM seed {seed} genomes {cnt} + corpus {ncorp} runs {nrun} steps {nsteps} states {nstate} " + " ".join(f"{k} {v}" for k, v in C.items()))
    print("CHECKED " + " ".join(f"{k} {v}" for k, v in n.items()) + "   (WONLY: real steps; ISOA: (state, q) pairs; FROZ: (genome, q) "
          "pairs; CONS: ISO runs; SWAP: (state, c) pairs; NOWONCE: consecutive move pairs of level-1 movers; FLIP1: (d = 2 ISO genome, start) "
          "pairs, k = 0..6 each)")
    # instance of the DEAD item
    I = json.load(open(os.path.join(H, "..", "box160", "out", "iso_d4_st9.json"))); gi = Gen(I); S, _ = gi.run(tuple(I["start"]))
    z = [t for t in range(1, len(S)) if any(S[t][v] != S[t - 1][v] for v in (0, 1))]
    print(f"INST iso_d4_st9 LR {is_lr(I)} ISO {is_iso(I)} d {I['N'] // 2} T {len(S) - 1} level-0 steps {z} seg1 {z[0] - 1} tail {len(S) - 1 - z[-1]}")
    wit = [os.path.join(H, "..", "box160", "out", f) for f in ("kf1_d4_t10.json", "ISO_1_d4_t12.json")]
    for f in sorted(glob.glob(os.path.join(H, "out", "kf*_d*_t*.json"))) + wit:
        W = json.load(open(f)); gw = Gen(W); k = 2 if "ISO_1" in f else int(os.path.basename(f)[2:].split("_")[0])
        print(f"WIT {os.path.basename(f)} LR {is_lr(W)} ISO {is_iso(W)} V_{k} {Vk(gw, tuple(W['start']), k)}")

if __name__ == "__main__":
    main()
