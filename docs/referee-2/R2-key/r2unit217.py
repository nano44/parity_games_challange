#!/usr/bin/env python3
"""REFEREE-2 successor 41: own engine for the PRE-READ (R2-key-preread Addendum 3) of box 217 §6 (Lemma 0, A1-A4, A2-POLY, §6.4 Lemma
BRIDGE) and §7 (A7 FLIP-SUPPLY, A7′) at claude/l-new a143d406 (docs/new/N5-QUIETKEY-box217.md). Written from the text of §6.1 (the
model 1P(G)); shares no code with the lane's one217.py / keyside215 / n5v / gamma3 / eg195. The Γ3 side (BRIDGE, RED) uses REFEREE-2's
own R2-P-N5-END/r2end.py (successor 34: build, s1, Order, s3, dual, ideal; from SPEC's text, R104, R117).

The model (§6.1): movers x with levels; option o = (x, k) has a W-target wt(o) (level lev(x) − 1; none at level 0), a Ξ-target xt(o)
(mover or exit; Ξ-graph acyclic), a weight ω(o) = ±2^rank (rank by the β priority 6 + 2·br + bp, + iff even), an index ε(o) (here the
genome's gate index = R104's layout). V_s(exit) = (0, 0); Ξ_s(o) = (ω(o), 1) + V_s(xt(o)); V_s(x) = Ξ_s(x, s(x)); pairs compared
lexicographically, larger better. key_s(o) = (ε(o)) at level 0, else μ_s(wt(o)) ++ (ε(o)); μ_s(x) = key_s(x, s(x)).
A_s(x) = {s(x)} ∪ {k : Ξ_s(x, k) > V_s(x)}. KEY step: by increasing level s′(x) = argmin over A_s(x) of key_s′(x, ·). Stop at s′ = s.

Must-0 counters (unit in brackets). A firing control is named after each group.
 Lemma 0  l0a_dup [(state, mover) with two options of equal key]  l0a_cnt [movers: |K(x)| by the recursion Σ_k |K(wt)| ≠ the number of
          distinct keys over ALL states, brute force, genomes with ≤ BRUTE states]  l0a_bnd [movers: |K(x)| > D^(lev + 1)]
          l0b_cnt [movers: |PΞ(x)| by recursion ≠ #distinct Ξ-paths over all states, brute]  l0b_val [movers: #distinct values ≠ #paths,
          brute]  l0b_bnd [movers: |PΞ(x)| > D^(hΞ + 1)]  l0c_tie [(state, mover, pair) with equal Ξ_s]
 A1       a1_v [(step, mover): V fell]  a1_mu [(step, mover): μ rose]  a1_vs / a1_mus [(step, mover): a switch without a strict
          rise of V / fall of μ]                                      control --ctrl howard (μ), --ctrl aall (V)
 A2       a2_k [movers: sw > |K| − 1]  a2_p [movers: sw > |PΞ| − 1]  a2_T [runs: T > Σ_x (min(|K|, |PΞ|) − 1)]
          a2_poly [runs: T > Σ_x (D^(1 + min(lev, hΞ)) − 1)]  a2_idle [steps with no switch]      control --ctrl khalf (|K|/2 for |K|)
 A3       a3_i [degree-2 movers with equal W-targets (level 0 included) and sw > 1]  a3_ii [degree-2 movers with equal Ξ-targets and
          sw > 1; also under the rules howard and rnd: a3_ii_h, a3_ii_r]      control --ctrl a3any (the test on every degree-2 mover)
 A4       for every mover with sw = |K| − 1 (nfull; by level in 'full_by_level'): a4_i_val [#distinct μ(x) ≠ |K|]  a4_i_sw [(step):
          μ(x) changed without a switch of x]  a4_ii [(mover, option): #distinct μ(wt) over the run ≠ |K(wt)|]  a4_iii [degree 2:
          XF_x < |K| − 2]                                             control --ctrl a4half (movers with sw ≥ |K|/2 − 1 count as full)
 A7       degree-2 movers x (options a, b; Ξ-targets y_a, y_b): XF_x := #{t ≥ 1 : the Ξ-order of a, b at s_t ≠ at s_(t−1)},
          P_x := #{t ≥ 1 : some mover on the Ξ-path of y_a or y_b under s_(t−1) has s_t ≠ s_(t−1)}, D_x := Σ sw(z) over the movers z ≠ x
          reachable from x in the Ξ-graph.  a7_a [XF > P]  a7_b [P > D]  a7_c [sw > 1 + XF]  a7_self [x reachable from itself]
          a7p [full degree-2 movers with D_x < |K| − 2 (A7′'s first sentence)]      control --ctrl a7direct (D_x over y_a, y_b only),
          --ctrl a7nop (sw ≤ XF, without the + 1)
 BRIDGE   on Γ3(G) (r2end.build, e-order lev) at the standard state for a mover state s (P-N5-REACH §3: σ(x) = m_(x,s(x)), σ(β) = xt
          or pb, σ(K0) = pA, σ(K1) = s, σ(K3) = K2), values and σ̄ by r2end.s1:  br_face [(state, gate): σ̄(g) ≠ pβ_g]  br_k2 [states:
          σ̄(K2) ≠ r]  br_val [(state, option): Ξσ(m_o) ≠ (K1, β's of the Ξ-path ∪ {K0, K3}, 5·hops + c), c one constant]
          br_cmp [(state, mover, pair): sign of Ξσ(m_(x,k)) vs Ξσ(m_(x,k′)) ≠ sign of Ξ_s(x, k) − Ξ_s(x, k′)]  br_A [(state, mover):
          {σ(x)} ∪ Iσ(x) read through the pads ≠ A_s(x)]  br_noe [(state, vertex other than e / pe): an e-vertex in Π]
          states: the key run's (--bridge run) and RAND random mover states per genome (--bridge rand)
                                                                     control --ctrl brpar (1P's top β parity flipped), --ctrl brstd
                                                                     (σ(β) = pb at every β: a non-standard state)
 ID       the identification 1P(G) = R104's IDEAL model (ε = gate index): id_state [runs: the key run's state sequence ≠ the IDEAL
          run's, the latter coded from R104's words: β-SETS compared by the largest-rank β of the symmetric difference, keys as gate-index
          chains]  red_ideal [runs: T ≠ r2end.ideal's L(G) (successor 34's code from P-REALIZE §2)]      control --ctrl l0w, brpar, kmax
 RED      N5 itself (SPEC S1-S5 by r2end's primitives, S4a = S1 on the dual of H) from S3 on Γ3(G) up to its first fallback, mover parts
          against the key run:  red_len [runs]  red_state [runs with a differing state]  red_flag [runs not ending in a fallback]
                                                                     control --ctrl kmax
 More controls: --ctrl l0k (|K|, |PΞ| by D·max instead of the sum: l0a_cnt / l0b_cnt), --ctrl l0w (weights ±(rank + 1) instead of
          ±2^rank: l0b_val / l0c_tie), --ctrl a7path (P_x over y_a's path only: a7_a), --ctrl xfhalf (XF over odd t only: a4_iii),
          --cyc COUNT SEED (Ξ-CYCLIC genomes at their start's standard state: br_face and br_noe must fire; br_k2 stays 0).
 Observations (not must-0): her [full movers of level ≥ 1 with a W-target that is not full], maxT, maxsw, k (enumeration depth, A6).
Usage: r2unit217.py [--ctrl NAME] [--bridge run|rand|both] [--red] [--gen COUNT SEED KIND] [--lad COUNT SEED D] [--xtw COUNT SEED D]
       [--mut COUNT SEED MAXMUT FILE] [--lift D FILE] [--list FILE] [--supply] [--quiet] FILES...     KIND: acyc (r2end.gen).  --mut: mutants of one genome (1 to
       MAXMUT random mutations each, Ξ-graph kept acyclic).  --lad: 2-wide degree-2 ladders with D levels, random acyclic Ξ-targets;
       --xtw: the same with Ξ-target = W-target (exit at level 0).  --supply: per-level supply table of the top full mover (§7 DATA)."""
import sys, os, json, random, itertools
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-P-N5-END"))
import r2end
BRUTE = 4000; RAND = 6

class M1P:
    def __init__(self, G, ctrl=""):
        self.G = G; N = self.N = G["N"]; self.lev = G["lev"]; opts = G["opts"]; self.ctrl = ctrl
        self.deg = [len(opts[x]) for x in range(N)]; self.D = max(self.deg)
        self.O = [(x, k) for x in range(N) for k in range(self.deg[x])]
        self.wt = {(x, k): opts[x][k][0] for (x, k) in self.O}; self.xt = {(x, k): opts[x][k][1] for (x, k) in self.O}
        self.b = {(x, k): opts[x][k][2] for (x, k) in self.O}
        for o in self.O:                                   # the genome's shape (§6.1)
            x = o[0]
            if self.lev[x] == 0: assert self.wt[o] < 0, "level-0 option with a W-target"
            else: assert self.wt[o] >= 0 and self.lev[self.wt[o]] == self.lev[x] - 1, "W-target not one level down"
        pr = {o: 6 + 2 * G["br"][self.b[o]] + G["bp"][self.b[o]] for o in self.O}
        assert len(set(pr.values())) == len(self.O), "β priorities not distinct"
        rk = {o: r for r, o in enumerate(sorted(self.O, key=lambda o: pr[o]))}
        self.om = {o: (1 << rk[o]) if pr[o] % 2 == 0 else -(1 << rk[o]) for o in self.O}
        if ctrl == "kswap":                               # control for the engine-agreement check: swap ε of mover 0's two options
            if self.deg[0] >= 2: self.eps[(0, 0)], self.eps[(0, 1)] = self.eps[(0, 1)], self.eps[(0, 0)]
        if ctrl == "l0w": self.om = {o: (rk[o] + 1) if pr[o] % 2 == 0 else -(rk[o] + 1) for o in self.O}
        if ctrl == "brpar":
            top = max(self.O, key=lambda o: rk[o]); self.om[top] = -self.om[top]
        self.eps = {(x, k): G["gate"][x][k] for (x, k) in self.O}
        assert len(set(self.eps.values())) == len(self.O), "ε not distinct"
        col = {}; self.topo = []
        def dfs(x):
            col[x] = 1
            for k in range(self.deg[x]):
                y = self.xt[(x, k)]
                if y >= 0:
                    assert col.get(y) != 1, "Ξ-graph not acyclic"
                    if y not in col: dfs(y)
            col[x] = 2; self.topo.append(x)
        sys.setrecursionlimit(100000)
        for x in range(N):
            if x not in col: dfs(x)
        self.bylev = sorted(range(N), key=lambda x: (self.lev[x], x))
        # |K(x)|, |PΞ(x)|, hΞ(x), Ξ-descendants
        self.K = {}
        agg = (lambda l: self.D * max(l)) if ctrl == "l0k" else sum
        for x in self.bylev: self.K[x] = self.deg[x] if self.lev[x] == 0 else agg([self.K[self.wt[(x, k)]] for k in range(self.deg[x])])
        self.PX = {}; self.hX = {}; self.desc = {}
        for x in self.topo:
            self.PX[x] = agg([1 if self.xt[(x, k)] < 0 else self.PX[self.xt[(x, k)]] for k in range(self.deg[x])])
            self.hX[x] = max(0 if self.xt[(x, k)] < 0 else 1 + self.hX[self.xt[(x, k)]] for k in range(self.deg[x]))
            d = set()
            for k in range(self.deg[x]):
                y = self.xt[(x, k)]
                if y >= 0: d.add(y); d |= self.desc[y]
            self.desc[x] = d

    def vals(self, s):
        V = {}; X = {}
        for x in self.topo:
            for k in range(self.deg[x]):
                o = (x, k); y = self.xt[o]; w, h = (0, 0) if y < 0 else V[y]
                X[o] = (self.om[o] + w, h + 1)
            V[x] = X[(x, s[x])]
        return V, X

    def keys(self, s):
        mu = {}; key = {}
        for x in self.bylev:
            for k in range(self.deg[x]):
                o = (x, k); key[o] = (self.eps[o],) if self.lev[x] == 0 else mu[self.wt[o]] + (self.eps[o],)
            mu[x] = key[(x, s[x])]
        return mu, key

    def avail(self, s, X):
        if self.ctrl == "aall": return [list(range(self.deg[x])) for x in range(self.N)]
        return [[k for k in range(self.deg[x]) if k == s[x] or X[(x, k)] > X[(x, s[x])]] for x in range(self.N)]

    def step(self, s, rule="key", rng=None):
        _, X = self.vals(s); A = self.avail(s, X)
        if all(len(a) == 1 for a in A): return None
        if rule == "howard": return tuple(max(A[x], key=lambda k: X[(x, k)]) for x in range(self.N))
        if rule == "rnd":
            t = [rng.choice(A[x]) for x in range(self.N)]
            if tuple(t) == tuple(s):
                x = rng.choice([x for x in range(self.N) if len(A[x]) > 1]); t[x] = rng.choice([k for k in A[x] if k != s[x]])
            return tuple(t)
        new = list(s); mu = {}
        pick = max if self.ctrl == "kmax" else min
        for x in self.bylev:
            kk = lambda k: (self.eps[(x, k)],) if self.lev[x] == 0 else mu[self.wt[(x, k)]] + (self.eps[(x, k)],)
            new[x] = pick(A[x], key=kk); mu[x] = kk(new[x])
        return tuple(new)

    def run(self, rule="key", rng=None, start=None, cap=200000):
        s = tuple(start if start is not None else self.G["start"]); S = [s]
        while len(S) <= cap:
            t = self.step(s, rule, rng)
            if t is None or t == s: break
            s = t; S.append(s)
        return S

    def xipath(self, y, s):                 # movers on the Ξ-path of y under s (y included; empty for the exit)
        P = []
        while y >= 0: P.append(y); y = self.xt[(y, s[y])]
        return P

sgn = lambda a, b: (a > b) - (a < b)

def analyse(m, S, C, ctrl, obs):
    N, T = m.N, len(S) - 1
    VX = [m.vals(s) for s in S]; MK = [m.keys(s) for s in S]
    sw = [sum(S[t + 1][x] != S[t][x] for t in range(T)) for x in range(N)]
    # Lemma 0 on the run's states
    for t in range(T + 1):
        V, X = VX[t]; mu, key = MK[t]
        for x in range(N):
            if len({key[(x, k)] for k in range(m.deg[x])}) != m.deg[x]: C["l0a_dup"] += 1
            for k in range(m.deg[x]):
                for k2 in range(k + 1, m.deg[x]):
                    if X[(x, k)] == X[(x, k2)]: C["l0c_tie"] += 1
    for x in range(N):
        if m.K[x] > m.D ** (m.lev[x] + 1): C["l0a_bnd"] += 1
        if m.PX[x] > m.D ** (m.hX[x] + 1): C["l0b_bnd"] += 1
    # A1
    for t in range(T):
        for x in range(N):
            v0, v1 = VX[t][0][x], VX[t + 1][0][x]; k0, k1 = MK[t][0][x], MK[t + 1][0][x]
            if v1 < v0: C["a1_v"] += 1
            if k1 > k0: C["a1_mu"] += 1
            if S[t + 1][x] != S[t][x]:
                if not v1 > v0: C["a1_vs"] += 1
                if not k1 < k0: C["a1_mus"] += 1
        if S[t + 1] == S[t]: C["a2_idle"] += 1
    # A2
    Kc = (lambda x: m.K[x] // 2) if ctrl == "khalf" else (lambda x: m.K[x])
    for x in range(N):
        if sw[x] > Kc(x) - 1: C["a2_k"] += 1
        if sw[x] > m.PX[x] - 1: C["a2_p"] += 1
    if T > sum(min(Kc(x), m.PX[x]) - 1 for x in range(N)): C["a2_T"] += 1
    if T > sum(m.D ** (1 + min(m.lev[x], m.hX[x])) - 1 for x in range(N)): C["a2_poly"] += 1
    # A3 (key rule)
    for x in range(N):
        if m.deg[x] != 2: continue
        a, b = (x, 0), (x, 1)
        if m.wt[a] == m.wt[b] or ctrl == "a3any":
            C["n3_i"] += 1
            if sw[x] > 1: C["a3_i"] += 1
        if m.xt[a] == m.xt[b] or ctrl == "a3any":
            C["n3_ii"] += 1
            if sw[x] > 1: C["a3_ii"] += 1
    # A4
    for x in range(N):
        full = sw[x] == m.K[x] - 1 or (ctrl == "a4half" and sw[x] >= m.K[x] // 2 - 1)
        if not full: continue
        C["nfull"] += 1; obs["full_by_level"][m.lev[x]] += 1
        if m.lev[x] >= 1:
            obs["k"] = max(obs["k"], m.lev[x] + 1); C["nfull_ge1"] += 1
            if any(sw[m.wt[(x, k)]] != m.K[m.wt[(x, k)]] - 1 for k in range(m.deg[x])): C["her"] += 1
        elif obs["k"] < 1: obs["k"] = 1
        if len({MK[t][0][x] for t in range(T + 1)}) != m.K[x]: C["a4_i_val"] += 1
        for t in range(T):
            if MK[t + 1][0][x] != MK[t][0][x] and S[t + 1][x] == S[t][x]: C["a4_i_sw"] += 1
        if m.lev[x] >= 1:
            for k in range(m.deg[x]):
                w = m.wt[(x, k)]
                if len({MK[t][0][w] for t in range(T + 1)}) != m.K[w]: C["a4_ii"] += 1
    # A7 (and A4 (iii), A7′)
    for x in range(N):
        if m.deg[x] != 2: continue
        a, b = (x, 0), (x, 1); ya, yb = m.xt[a], m.xt[b]
        order = [sgn(VX[t][1][a], VX[t][1][b]) for t in range(T + 1)]
        XF = sum(order[t] != order[t - 1] for t in range(1, T + 1) if ctrl != "xfhalf" or t % 2)
        P = 0
        for t in range(1, T + 1):
            on = set(m.xipath(ya, S[t - 1])) | (set() if ctrl == "a7path" else set(m.xipath(yb, S[t - 1])))
            if any(S[t][z] != S[t - 1][z] for z in on): P += 1
        desc = m.desc[x] - {x}
        if ctrl == "a7direct": desc = {y for y in (ya, yb) if y >= 0}
        Dx = sum(sw[z] for z in desc)
        if x in m.desc[x]: C["a7_self"] += 1
        if XF > P: C["a7_a"] += 1
        if P > Dx: C["a7_b"] += 1
        if sw[x] > (XF if ctrl == "a7nop" else 1 + XF): C["a7_c"] += 1
        C["n7"] += 1
        if sw[x] == m.K[x] - 1:
            if XF < m.K[x] - 2: C["a4_iii"] += 1
            if Dx < m.K[x] - 2: C["a7p"] += 1
    obs["maxT"] = max(obs["maxT"], T); obs["maxsw"] = max(obs["maxsw"], max(sw))
    return sw

def ideal_states(G, cap=200000):
    """R104's IDEAL run, written from R104's words (not from §6.1): the Ξ-value of an option is the SET of β's on its chain, compared by
    the β of largest rank in the symmetric difference (the set holding it is better iff its parity is even); the key of an option is
    the list of gate indices of the chain of W-targets under the NEW state, lowest level first; every mover goes to the least key
    among its current option and the strictly Ξ-better ones; stop when nothing is available or nothing changes."""
    N, opts, lev, br, bp, gate = G["N"], G["opts"], G["lev"], G["br"], G["bp"], G["gate"]
    s = list(G["start"]); S = [tuple(s)]
    def bset(x, k):
        B = set()
        while True:
            B.add(opts[x][k][2]); x = opts[x][k][1]
            if x < 0: return B
            k = s[x]
    def better(B1, B2):
        d = B1 ^ B2
        if not d: return False
        b = max(d, key=lambda b: br[b])
        return (b in B1) == (bp[b] == 0)
    while len(S) <= cap:
        cur = [bset(x, s[x]) for x in range(N)]
        A = [[k for k in range(len(opts[x])) if k == s[x] or better(bset(x, k), cur[x])] for x in range(N)]
        if all(len(a) == 1 for a in A): break
        new = [None] * N
        def chain(x, k):                       # gate indices from level 0 up to (x, k), under the new state at lower levels
            ch = []
            while True:
                ch.append(gate[x][k]); x = opts[x][k][0]
                if x < 0: return ch[::-1]
                k = new[x]
        for x in sorted(range(N), key=lambda x: lev[x]): new[x] = min(A[x], key=lambda k: chain(x, k))
        if new == s: break
        s = new; S.append(tuple(s))
    return S

def brute(m, C):
    """Lemma 0 (a), (b) over ALL states (small genomes only)"""
    tot = 1
    for d in m.deg: tot *= d
    if tot > BRUTE: return 0
    keys = defaultdict(set); paths = defaultdict(set); values = defaultdict(set)
    for s in itertools.product(*[range(d) for d in m.deg]):
        V, X = m.vals(s); mu, key = m.keys(s)
        for (x, k) in m.O:
            keys[x].add(key[(x, k)])
            p = [(x, k)]; y = m.xt[(x, k)]
            while y >= 0: p.append((y, s[y])); y = m.xt[(y, s[y])]
            paths[x].add(tuple(p)); values[x].add(X[(x, k)])
    for x in range(m.N):
        if len(keys[x]) != m.K[x]: C["l0a_cnt"] += 1
        if len(paths[x]) != m.PX[x]: C["l0b_cnt"] += 1
        if len(values[x]) != len(paths[x]): C["l0b_val"] += 1
    C["nbrute"] += 1
    return 1

def a3_other_rules(m, C, seed):
    rng = random.Random(seed)
    if m.ctrl == "aall": return                      # with A = every option the rnd rule never stops
    for rule, nm in (("howard", "a3_ii_h"), ("rnd", "a3_ii_r")):
        S = m.run(rule, rng, cap=50000); T = len(S) - 1
        for x in range(m.N):
            if m.deg[x] == 2 and m.xt[(x, 0)] == m.xt[(x, 1)]:
                if sum(S[t + 1][x] != S[t][x] for t in range(T)) > 1: C[nm] += 1
        if rule == "howard": C["Thoward_max"] = max(C["Thoward_max"], T)

def std_state(g, G, s, ctrl):
    V = g["V"]; n = g["n"]; ow = g["ow"]; E = g["E"]; sig = [None] * n
    for v in range(n):
        if ow[v] == 0 and len(E[v]) == 1: sig[v] = E[v][0]
    for x in range(G["N"]): sig[V[("x", x)]] = V[("m", (x, s[x]))]
    for o in g["O"]:
        xt = G["opts"][o[0]][o[1]][1]
        sig[V[("b", o)]] = V[("x", xt)] if (xt >= 0 and ctrl != "brstd") else V[("pb", o)]
    sig[V["K0"]] = V["pA"]; sig[V["K1"]] = V["s"]; sig[V["K3"]] = V["K2"]
    assert all(sig[v] is not None and sig[v] in E[v] for v in range(n) if ow[v] == 0)
    return sig

def bridge(m, G, states, C, ctrl, obs):
    g = r2end.build(G, "lev"); n, pr, ow, E, V = g["n"], g["pr"], g["ow"], g["E"], g["V"]; od = r2end.Order(pr)
    evs = {V[("e", o)] for o in g["O"]}; skip = evs | {V[("pe", o)] for o in g["O"]}
    for s in states:
        sig = std_state(g, G, s, ctrl); val, sbar = r2end.s1(pr, ow, E, sig, od); _, X = m.vals(s); A = m.avail(s, X)
        C["br_states"] += 1
        for o in g["O"]:
            C["br_gates"] += 1
            if sbar[V[("g", o)]] != V[("pB", o)]: C["br_face"] += 1
        if sbar[V["K2"]] != V["r"]: C["br_k2"] += 1
        for o in g["O"]:
            bs = set(); y, k = o
            while True:
                bs.add(V[("b", (y, k))]); y = m.xt[(y, k)]
                if y < 0: break
                k = s[y]
            want = (V["K1"], frozenset(bs | {V["K0"], V["K3"]}))
            c = val[V[("m", o)]][2] - 5 * len(bs)
            obs["brc"].add(c)
            if val[V[("m", o)]][:2] != want or len(obs["brc"]) > 1: C["br_val"] += 1
        for x in range(m.N):
            for k in range(m.deg[x]):
                for k2 in range(k + 1, m.deg[x]):
                    C["br_pairs"] += 1
                    if od.cmp(val[V[("m", (x, k))]], val[V[("m", (x, k2))]]) != sgn(X[(x, k)], X[(x, k2)]): C["br_cmp"] += 1
            xv = V[("x", x)]
            Ag = sorted(k for k in range(m.deg[x]) if V[("m", (x, k))] == sig[xv] or od.cmp(val[V[("m", (x, k))]], val[sig[xv]]) > 0)
            if Ag != sorted(A[x]): C["br_A"] += 1
        for v in range(n):
            if v not in skip and val[v][1] & evs: C["br_noe"] += 1

def cyc_ctrl(cnt, seed):
    """control for br_face / br_noe: Ξ-CYCLIC random genomes (r2end.gen 'any'), standard state for the genome start"""
    rng = random.Random(seed); C = defaultdict(int); c = 0
    while c < cnt:
        G = r2end.gen(rng, "any")
        if r2end.acyclic(G): continue
        c += 1; g = r2end.build(G, "lev"); V = g["V"]; od = r2end.Order(g["pr"])
        sig = std_state(g, G, G["start"], ""); val, sbar = r2end.s1(g["pr"], g["ow"], g["E"], sig, od)
        evs = {V[("e", o)] for o in g["O"]}; skip = evs | {V[("pe", o)] for o in g["O"]}
        C["br_face"] += sum(sbar[V[("g", o)]] != V[("pB", o)] for o in g["O"]); C["br_k2"] += sbar[V["K2"]] != V["r"]
        C["br_noe"] += sum(1 for v in range(g["n"]) if v not in skip and val[v][1] & evs)
    print(f"CYC-CTRL genomes {cnt} seed {seed} (Ξ-cyclic): br_face {C['br_face']} br_k2 {C['br_k2']} br_noe {C['br_noe']}")

def n5_movers(G, cap=100000):
    """N5 (SPEC, r2end's primitives) from S3 on Γ3(G): mover parts of the states before the first fallback"""
    g = r2end.build(G, "lev"); n, pr, ow, E, V = g["n"], g["pr"], g["ow"], g["E"], g["V"]
    od = r2end.Order(pr); dpr, dow = r2end.dual(pr, ow); dod = r2end.Order(dpr)
    st = r2end.s3(g); sig = [st[v] if ow[v] == 0 else None for v in range(n)]; tau = [st[v] if ow[v] == 1 else None for v in range(n)]
    inv = {V[("m", o)]: o[1] for o in g["O"]}; rd = lambda sg: tuple(inv[sg[V[("x", x)]]] for x in range(G["N"]))
    R = [rd(sig)]; flag = "cap"
    for it in range(cap):
        val, _ = r2end.s1(pr, ow, E, sig, od)
        Is = {v: [w for w in E[v] if w != sig[v] and od.cmp(val[w], val[sig[v]]) > 0] for v in range(n) if ow[v] == 0}
        Is = {v: l for v, l in Is.items() if l}
        dval, _ = r2end.s1(dpr, dow, E, tau, dod)
        It = any(dod.cmp(dval[w], dval[tau[v]]) > 0 for v in range(n) if ow[v] == 1 for w in E[v] if w != tau[v])
        if It: flag = "Itau"; break
        if not Is: flag = "opt"; break
        HE = [sorted(set([sig[v]] + Is.get(v, []))) if ow[v] == 0 else [tau[v]] for v in range(n)]
        _, hch = r2end.s1(dpr, dow, HE, tau, dod)
        snew = [(hch[v] if hch[v] is not None else HE[v][0]) if ow[v] == 0 else None for v in range(n)]
        if snew == sig: flag = "fallback"; break
        if any(snew[v] != sig[v] for v in range(n) if ow[v] == 0 and v not in {V[("x", x)] for x in range(G["N"])}): flag = "nonmover"; break
        sig = snew; R.append(rd(sig))
    return R, flag

def lad(rng, d, xtw=False, w=2):
    """w-wide degree-2 ladder with d levels; W-targets: two movers of the level below (distinct when w ≥ 2); Ξ-targets random
    earlier movers in a random order (acyclic) or the exit; xtw: Ξ-target = W-target (exit at level 0)"""
    N = w * d; lev = [x // w for x in range(N)]; order = list(range(N)); rng.shuffle(order); pos = {x: i for i, x in enumerate(order)}
    opts = []; b = 0
    for x in range(N):
        below = [y for y in range(N) if lev[y] == lev[x] - 1]; ox = []
        ws = rng.sample(below, 2) if len(below) >= 2 and rng.random() < 0.85 else ([rng.choice(below)] * 2 if below else [-1, -1])
        for j in range(2):
            wt = ws[j]
            if xtw: xt = wt
            else: xt = rng.choice([-1] + [y for y in range(N) if pos[y] < pos[x]])
            ox.append([wt, xt, b]); b += 1
        opts.append(ox)
    M = b; gp = rng.sample(range(M), M)
    return dict(N=N, lev=lev, opts=opts, gate=[gp[2 * x:2 * x + 2] for x in range(N)], br=rng.sample(range(M), M),
                bp=[rng.randint(0, 1) for _ in range(M)], start=[rng.randrange(2) for _ in range(N)])

def mutate(G, rng, cnt):
    """cnt random mutations of a genome, the Ξ-graph kept acyclic: swap two gate indices / two β ranks, flip a β parity, re-aim a
    Ξ-target (mover or exit) or a W-target (same level), flip a start"""
    G = json.loads(json.dumps(G)); N = G["N"]; O = [(x, k) for x in range(N) for k in range(len(G["opts"][x]))]; done = 0; tries = 0
    while done < cnt and tries < 1000:
        tries += 1; kind = rng.choice(["gate", "rank", "par", "xt", "xt", "wt", "start"]); (x, k) = rng.choice(O)
        if kind == "gate":
            (y, j) = rng.choice(O); G["gate"][x][k], G["gate"][y][j] = G["gate"][y][j], G["gate"][x][k]
        elif kind == "rank":
            (y, j) = rng.choice(O); b, c = G["opts"][x][k][2], G["opts"][y][j][2]; G["br"][b], G["br"][c] = G["br"][c], G["br"][b]
        elif kind == "par": b = G["opts"][x][k][2]; G["bp"][b] ^= 1
        elif kind == "xt":
            old = G["opts"][x][k][1]; G["opts"][x][k][1] = rng.choice([-1] + [y for y in range(N) if y != x])
            if not r2end.acyclic(G): G["opts"][x][k][1] = old; continue
        elif kind == "wt":
            if G["lev"][x] == 0: continue
            G["opts"][x][k][0] = rng.choice([y for y in range(N) if G["lev"][y] == G["lev"][x] - 1])
        else: G["start"][x] = rng.randrange(len(G["opts"][x]))
        done += 1
    return G

def lift(G, d):
    """G↑d (for item E-2): a chain of d degree-1 movers (levels 0..d − 1, Ξ-target the exit, new β's of the lowest ranks, new gate
    indices above the old ones) put under G: every old level-0 option gets the chain's top as W-target and every old level rises by d.
    Every old key gets the same d-entry prefix and no old Ξ-path meets the chain, so the run on the old movers is G's run."""
    G = json.loads(json.dumps(G)); N = G["N"]; M = len(G["br"]); gmax = max(max(r) for r in G["gate"])
    if d == 0: return G
    G["br"] = [r + d for r in G["br"]] + list(range(d)); G["bp"] = G["bp"] + [0] * d
    for x in range(N):
        if G["lev"][x] == 0:
            for o in G["opts"][x]: o[0] = N + d - 1
        G["lev"][x] += d
    for j in range(d):
        G["opts"].append([[N + j - 1 if j else -1, -1, M + j]]); G["lev"].append(j); G["gate"].append([gmax + 1 + j]); G["start"].append(0)
    G["N"] = N + d
    return G

def supply(m, S, sw):
    """§7 DATA: for the top full mover (largest level, then least index), switches at step t of movers on the current Ξ-paths of its two
    Ξ-targets, by W-level (whole run)"""
    full = [x for x in range(m.N) if sw[x] == m.K[x] - 1 and m.deg[x] == 2]
    if not full: return "no full degree-2 mover"
    x = max(full, key=lambda x: (m.lev[x], -x)); ya, yb = m.xt[(x, 0)], m.xt[(x, 1)]; by = defaultdict(int)
    for t in range(1, len(S)):
        on = set(m.xipath(ya, S[t - 1])) | set(m.xipath(yb, S[t - 1]))
        for z in on:
            if S[t][z] != S[t - 1][z]: by[m.lev[z]] += 1
    lv = lambda y: "exit" if y < 0 else f"{y} (level {m.lev[y]})"
    return (f"top full mover {x} level {m.lev[x]} sw {sw[x]} |K| {m.K[x]} Ξ-targets {lv(ya)}, {lv(yb)}; supply by level: "
            + ", ".join(f"{l}: {by[l]}" for l in sorted(by)) + f"; total {sum(by.values())}")

MUST0 = ["l0a_dup", "l0a_cnt", "l0a_bnd", "l0b_cnt", "l0b_val", "l0b_bnd", "l0c_tie", "a1_v", "a1_mu", "a1_vs", "a1_mus", "a2_k", "a2_p",
         "a2_T", "a2_poly", "a2_idle", "a3_i", "a3_ii", "a3_ii_h", "a3_ii_r", "a4_i_val", "a4_i_sw", "a4_ii", "a4_iii", "a7_a", "a7_b",
         "a7_c", "a7_self", "a7p", "br_face", "br_k2", "br_val", "br_cmp", "br_A", "br_noe", "red_len", "red_state", "red_ideal", "red_flag", "id_state"]
INFO = ["runs", "steps", "nbrute", "n3_i", "n3_ii", "nfull", "nfull_ge1", "her", "n7", "br_states", "br_gates", "br_pairs", "red_runs",
        "Thoward_max"]

def main(a):
    ctrl = ""; br = ""; red = False; sup = False; quiet = False; Gs = []; i = 0; skipped = 0
    while i < len(a):
        if a[i] == "--ctrl": ctrl = a[i + 1]; i += 2
        elif a[i] == "--bridge": br = a[i + 1]; i += 2
        elif a[i] == "--red": red = True; i += 1
        elif a[i] == "--supply": sup = True; i += 1
        elif a[i] == "--cyc": cyc_ctrl(int(a[i + 1]), int(a[i + 2])); return
        elif a[i] == "--quiet": quiet = True; i += 1
        elif a[i] == "--gen":
            rng = random.Random(int(a[i + 2])); c = 0
            while c < int(a[i + 1]):
                G = r2end.gen(rng, a[i + 3])
                if r2end.acyclic(G): Gs.append((f"gen{a[i + 3]}{a[i + 2]}#{c}", G)); c += 1
            i += 4
        elif a[i] in ("--lad", "--xtw"):
            rng = random.Random(int(a[i + 2]))
            Gs += [(f"{a[i][2:]}{a[i + 3]}_{a[i + 2]}#{c}", lad(rng, int(a[i + 3]), a[i] == "--xtw")) for c in range(int(a[i + 1]))]
            i += 4
        elif a[i] == "--list":                     # --list FILE: lines «sha1 N path» (a corpus list; paths relative to the cwd)
            for l in open(a[i + 1]):
                h, _, pth = l.split(None, 2); G = json.load(open(pth.strip())); Gs.append((h[:10], G.get("genome", G)))
            i += 2
        elif a[i] == "--lift":                     # --lift D FILE: G↑D (item E-2)
            G0 = json.load(open(a[i + 2])); Gs.append((f"lift{a[i + 1]}_{os.path.basename(a[i + 2])}", lift(G0.get("genome", G0), int(a[i + 1])))); i += 3
        elif a[i] == "--mut":                      # --mut COUNT SEED MAXMUT FILE: mutants of one genome
            rng = random.Random(int(a[i + 2])); G0 = json.load(open(a[i + 4])); G0 = G0.get("genome", G0)
            Gs += [(f"mut{a[i + 2]}_{os.path.basename(a[i + 4])}#{c}", mutate(G0, rng, rng.randint(1, int(a[i + 3])))) for c in range(int(a[i + 1]))]
            i += 5
        else:
            G = json.load(open(a[i])); G = G.get("genome", G)
            if r2end.acyclic(G): Gs.append((os.path.basename(a[i]), G))
            else: skipped += 1                       # 1P(G) is defined for Ξ-acyclic genomes only
            i += 1
    C = defaultdict(int); obs = dict(full_by_level=defaultdict(int), k=0, maxT=0, maxsw=0, brc=set())
    for j, (name, G) in enumerate(Gs):
        m = M1P(G, ctrl); rule = "howard" if ctrl == "howard" else "key"
        S = m.run(rule); T = len(S) - 1; C["runs"] += 1; C["steps"] += T
        sw = analyse(m, S, C, ctrl, obs); brute(m, C); a3_other_rules(m, C, j)
        L, why = r2end.ideal(G)
        if L != T: C["red_ideal"] += 1
        if rule == "key" and ideal_states(G) != S: C["id_state"] += 1
        line = f"{name} N {m.N} M {len(m.O)} T {T} L_ideal {L} maxsw {max(sw)}"
        if br:
            sts = []
            if br in ("run", "both"): sts += S
            if br in ("rand", "both"):
                rng = random.Random(1000 + j); sts += [tuple(rng.randrange(d) for d in m.deg) for _ in range(RAND)]
            bridge(m, G, sts, C, ctrl, obs)
        if red:
            R, flag = n5_movers(G); C["red_runs"] += 1
            if len(R) != len(S): C["red_len"] += 1
            if R != S: C["red_state"] += 1
            if flag != "fallback": C["red_flag"] += 1
            line += f" n5 {len(R) - 1} {flag}"
        if sup: line += " | " + supply(m, S, sw)
        if not quiet: print(line, flush=True)
    print(f"TOTAL ctrl {ctrl or '-'} bridge {br or '-'} red {int(red)}: " + " ".join(f"{k} {C[k]}" for k in MUST0))
    print("INFO " + " ".join(f"{k} {C[k]}" for k in INFO) + f" k {obs['k']} maxT {obs['maxT']} maxsw {obs['maxsw']} full_by_level "
          + ",".join(f"{l}:{c}" for l, c in sorted(obs["full_by_level"].items())) + f" bridge_len_const {sorted(obs['brc'])}")
    print("FIRED " + (" ".join(k for k in MUST0 if C[k]) or "none") + f" | files skipped as Ξ-cyclic {skipped}")

if __name__ == "__main__":
    main(sys.argv[1:])
