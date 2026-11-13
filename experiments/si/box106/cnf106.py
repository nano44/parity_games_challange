#!/usr/bin/env python3
"""L-SI box 106 §3.2: ONE CNF for «some genome G* of the free depth-2 ladder 𝓛*_2 has L*(G*) >= LEN» (docs/si/box106-exact2.md),
built on Claim MG (§2): availability = Odd's optimum in the 4-node mover game M_s, written as local optimality of Odd's positional
choice RHO at the 4 active gates (one-player game: no improving switch <=> optimal; RESULTS R36 (c) Lemma P1 as cited in §2), and
the KEY run of mg106.abstract_run.

Free data (the genome): XT[q][t] (the Xi-target of option q = 2x + k: mover t = 0..3 or X = 4), GO (strict order of the 4 level-0 gates),
ORD (strict order of the 16 carriers: beta_q = q, e_q = 8 + q), PAR (carrier parity; 1 = odd), the start R[0].
Value of a play in M_s (as mg106.play_value / key): node (a carrier, cW or K1), P (carriers on the path before the node, above it),
LEN (number of mover steps before the node: lengths in Gamma3*'s edges are 5 LEN + 2 / 5 LEN - 2 / 5 LEN + 4 for a carrier node / cW /
K1, strictly increasing in LEN for a fixed node type, and only compared at equal nodes).
Usage: as a module (build(LEN) -> (clauses, nvars, varmap)); `cnf106.py dimacs LEN OUT.cnf` writes DIMACS with a comment header.
CTRL (env, mutation controls for the audit): 1 = availability ignores Odd's beta-face at the inactive gate (AV := its e-face play only);
2 = the length rule's parity reversed; 3 = reward parity of the node read reversed in GT (makes local optimality unsatisfiable)."""
import os, sys, itertools
CTRL = int(os.environ.get("CTRL", "0"))
MOV = range(4); NC = 16
STATES = list(itertools.product((0, 1), repeat=4))
CW, K1 = 16, 17            # node codes beyond the carriers
TCW, TK = 4, 5             # walk targets beyond the movers

def lev(x): return x // 2
def beta(q): return q
def ecar(q): return 8 + q
def opt(x, k): return 2 * x + k
def owner(c): return (c % 8) // 2      # mover of carrier c

class Enc:
    def __init__(self):
        self.n = 0; self.cl = []; self.names = {}
        self.T = self.new("TRUE"); self.cl.append([self.T])
    def new(self, name=None):
        self.n += 1
        if name is not None: self.names[name] = self.n
        return self.n
    def v(self, name):
        if name not in self.names: self.new(name)
        return self.names[name]
    def add(self, c): self.cl.append(list(c))
    def AND(self, lits, name=None):
        y = self.new(name)
        for a in lits: self.add([-y, a])
        self.add([y] + [-a for a in lits]); return y
    def OR(self, lits, name=None):
        y = self.new(name)
        for a in lits: self.add([y, -a])
        self.add([-y] + list(lits)); return y
    def XOR(self, a, b):
        y = self.new()
        self.add([-y, a, b]); self.add([-y, -a, -b]); self.add([y, -a, b]); self.add([y, a, -b]); return y
    def EQ(self, a, b):
        self.add([-a, b]); self.add([a, -b])
    def onehot(self, lits):
        self.add(lits)
        for a, b in itertools.combinations(lits, 2): self.add([-a, -b])
    def amo(self, lits):
        for a, b in itertools.combinations(lits, 2): self.add([-a, -b])

def build(LEN=None):
    E = Enc(); T = E.T; F = -T
    # ---- free data
    XT = [[E.v(("XT", q, t)) for t in range(5)] for q in range(8)]
    for q in range(8): E.onehot(XT[q])
    def ordv(c, d):            # literal «c below d» (pri c < pri d)
        if c < d: return E.v(("ORD", c, d))
        return -E.v(("ORD", d, c))
    for a, b, c in itertools.permutations(range(NC), 3):   # transitivity
        E.add([-ordv(a, b), -ordv(b, c), ordv(a, c)])
    PAR = [E.v(("PAR", c)) for c in range(NC)]
    def gov(q, r):             # level-0 gate order, q, r in 0..3
        if q < r: return E.v(("GO", q, r))
        return -E.v(("GO", r, q))
    for a, b, c in itertools.permutations(range(4), 3): E.add([-gov(a, b), -gov(b, c), gov(a, c)])
    # node relations: below(n, n2) and reward-greater RG(n, n2) for n, n2 in carriers + cW + K1
    def below(n, m):           # pri n < pri m
        if n == m: return F
        if n == CW: return F if m != CW else F
        if m == CW: return T
        if n == K1: return T
        if m == K1: return F
        return ordv(n, m)
    def odd(n):
        if n == CW: return F
        if n == K1: return T
        return PAR[n]
    RGc = {}
    def RG(n, m):              # reward(n) > reward(m); reward = pri if even else -pri
        if n == m: return F
        if (n, m) in RGc: return RGc[(n, m)]
        y = E.new(); RGc[(n, m)] = y
        on, om, bl = odd(n), odd(m), below(n, m)
        if CTRL == 3: on, om = -on, -om
        # even n, even m: n above m ; even n, odd m: true ; odd n, even m: false ; odd n, odd m: n below m
        for pn in (0, 1):
            for pm in (0, 1):
                cond = [on if pn else -on, om if pm else -om]
                if pn == 0 and pm == 0: val = -bl      # above (n != m)
                elif pn == 0 and pm == 1: val = T
                elif pn == 1 and pm == 0: val = F
                else: val = bl
                # cond -> (y <-> val)
                E.add([-cond[0], -cond[1], -y, val]); E.add([-cond[0], -cond[1], y, -val])
        return y
    # ---- per state: Odd's faces RHO, the walks, the values
    AV = {}
    for s in STATES:
        S = s
        RHO = [E.v(("RHO", S, u)) for u in MOV]
        def car_lits(u):       # (carrier, literal «mover u uses it») for the active option of u
            q = opt(u, S[u]); return [(ecar(q), -RHO[u]), (beta(q), RHO[u])]
        # successor one-hot SUCC[u][t], t in 0..3, TCW, TK
        SUCC = [[E.new() for t in range(6)] for u in MOV]
        for u in MOV:
            q = opt(u, S[u]); E.onehot(SUCC[u])
            et = TCW if lev(u) == 0 else S[u]          # option k of a level-1 mover W-points to mover k
            for t in range(6):
                bt = [XT[q][t]] if t < 4 else ([XT[q][4]] if t == TK else [])
                # RHO=0 -> SUCC[t] == (t == et); RHO=1 -> SUCC[t] == XT
                E.add([RHO[u], -SUCC[u][t]] if t != et else [RHO[u], SUCC[u][t]])
                if bt: E.add([-RHO[u], -bt[0], SUCC[u][t]]); E.add([-RHO[u], bt[0], -SUCC[u][t]])
                else: E.add([-RHO[u], -SUCC[u][t]])
        # POS[z][i][t]
        POS = {}
        for z in MOV:
            for i in range(5):
                POS[(z, i)] = [E.new() for t in range(6)]
                if i == 0:
                    for t in range(6): E.add([POS[(z, 0)][t]] if t == z else [-POS[(z, 0)][t]])
                    continue
                prev = POS[(z, i - 1)]
                for t in range(6):
                    for u in MOV: E.add([-prev[u], -SUCC[u][t], POS[(z, i)][t]])
                for t in (TCW, TK): E.add([-prev[t], POS[(z, i)][t]])
                E.amo(POS[(z, i)])
        CYC = [E.OR([POS[(u, i)][u] for i in range(1, 5)]) for u in MOV]
        W = {}
        for z in MOV:
            VIS = [E.OR([POS[(z, i)][u] for i in range(4)]) for u in MOV]
            TC, TKz = POS[(z, 4)][TCW], POS[(z, 4)][TK]
            ONC = {}
            for u in MOV:
                for c, sel in car_lits(u): ONC[c] = E.AND([VIS[u], CYC[u], sel])
            node = {}
            for c in ONC:
                node[c] = E.AND([ONC[c]] + [E.OR([-ONC[d], ordv(d, c)]) for d in ONC if d != c])
            node[CW] = TC; node[K1] = TKz
            # ABOVE[c]: c above the node (all 16 carriers; cW above every carrier, K1 below)
            ABOVE = {}
            for c in range(NC):
                terms = [TKz] + [E.AND([node[d], ordv(d, c)]) for d in ONC if d != c]
                ABOVE[c] = E.OR(terms)
            P = {}
            for c in range(NC):
                if c in ONC:
                    u = owner(c); sel = dict(car_lits(u))[c]
                    P[c] = E.AND([VIS[u], -CYC[u], sel, ABOVE[c]])
                else: P[c] = F
            # FIRST[i][t] and LEN
            FIRST = {}
            for i in range(5):
                for t in range(6):
                    FIRST[(i, t)] = E.AND([POS[(z, i)][t]] + [-POS[(z, j)][t] for j in range(i)])
            NM = [E.OR([node[c] for c, _ in car_lits(u)]) for u in MOV]
            LENv = []
            for l in range(6):
                terms = [E.AND([NM[u], FIRST[(l, u)]]) for u in MOV if l < 5] + \
                        ([E.AND([TC, FIRST[(l, TCW)]]), E.AND([TKz, FIRST[(l, TK)]])] if l < 5 else [])
                LENv.append(E.OR(terms) if terms else F)
            W[z] = dict(node=node, P=P, LEN=LENv, ABOVE=ABOVE)
        def prepend(c, tgt_lits):
            """value of the play gate -> carrier c -> target (tgt_lits: list over t in 0..5 of literals, one-hot)"""
            nodes = sorted(set([n for z in MOV for n in W[z]["node"]]))
            nd = {}
            for n in nodes:
                terms = [E.AND([tgt_lits[z], W[z]["node"][n]]) for z in MOV if n in W[z]["node"]]
                if n == CW: terms.append(tgt_lits[TCW])
                if n == K1: terms.append(tgt_lits[TK])
                nd[n] = E.OR(terms)
            P = {}
            for d in range(NC):
                terms = [E.AND([tgt_lits[z], W[z]["P"][d]]) for z in MOV if W[z]["P"][d] != F]
                if d == c: terms += [E.AND([tgt_lits[z], W[z]["ABOVE"][c]]) for z in MOV] + [tgt_lits[TK]]
                P[d] = E.OR(terms) if terms else F
            LENv = []
            for l in range(6):
                terms = [E.AND([tgt_lits[z], W[z]["LEN"][l - 1]]) for z in MOV if l >= 1 and W[z]["LEN"][l - 1] != F]
                if l == 1: terms += [tgt_lits[TCW], tgt_lits[TK]]
                LENv.append(E.OR(terms) if terms else F)
            return dict(node=nd, P=P, LEN=LENv)
        def tgt_e(x, k):
            t = TCW if lev(x) == 0 else k
            return [T if j == t else F for j in range(6)]
        def tgt_b(x, k):
            q = opt(x, k); return [XT[q][0], XT[q][1], XT[q][2], XT[q][3], F, XT[q][4]]
        def gate_val(z):
            return dict(node=W[z]["node"], P=W[z]["P"], LEN=W[z]["LEN"])
        def GT(a, b):
            """a strictly better than b for Even (SPEC S1's order), as mg106.key"""
            na, nb = a["node"], b["node"]
            ns = sorted(set(na) | set(nb))
            A = {n: na.get(n, F) for n in ns}; B = {n: nb.get(n, F) for n in ns}
            BEAT = {}
            for n in ns:
                y = E.new(); BEAT[n] = y
                for m in ns:
                    r = RG(n, m)
                    E.add([-B[m], -r, y]); E.add([-B[m], r, -y])
            RW = E.new()
            for n in ns: E.add([-A[n], -BEAT[n], RW]); E.add([-A[n], BEAT[n], -RW])
            SAME = E.new()
            for n in ns: E.add([-A[n], -B[n], SAME]); E.add([-A[n], B[n], -SAME])
            D = {c: E.XOR(a["P"][c], b["P"][c]) for c in range(NC)}
            PEQ = E.AND([-D[c] for c in range(NC)])
            TOP = {c: E.new() for c in range(NC)}
            for c in range(NC):
                E.add([-TOP[c], D[c]])
                for d in range(NC):
                    if d != c: E.add([-TOP[c], -ordv(c, d), -D[d]])
            E.add([PEQ] + [TOP[c] for c in range(NC)])
            PW = E.new(); E.add([-PEQ, -PW])
            for c in range(NC):
                pa = a["P"][c]
                E.add([-TOP[c], -pa, PAR[c], PW]); E.add([-TOP[c], pa, -PAR[c], PW])
                E.add([-TOP[c], -pa, -PAR[c], -PW]); E.add([-TOP[c], pa, PAR[c], -PW])
            NE = E.new()       # a's node is even
            for n in ns:
                o = odd(n)
                if CTRL == 2: o = -o
                E.add([-A[n], -o, -NE]); E.add([-A[n], o, NE])
            La, Lb = a["LEN"], b["LEN"]
            LT_ab = E.OR([E.AND([La[i], Lb[j]]) for i in range(6) for j in range(6) if i < j and La[i] != F and Lb[j] != F] or [F])
            LT_ba = E.OR([E.AND([La[i], Lb[j]]) for i in range(6) for j in range(6) if i > j and La[i] != F and Lb[j] != F] or [F])
            LW = E.OR([E.AND([NE, LT_ab]), E.AND([-NE, LT_ba])])
            return E.OR([RW, E.AND([SAME, E.OR([PW, E.AND([PEQ, LW])])])])
        # local optimality of RHO at the 4 active gates
        for u in MOV:
            q = opt(u, S[u]); cur = gate_val(u)
            for f in (0, 1):
                alt = prepend(beta(q) if f else ecar(q), tgt_b(u, S[u]) if f else tgt_e(u, S[u]))
                g = GT(cur, alt)           # the other face is strictly better for Odd
                E.add([(-RHO[u] if f == 0 else RHO[u]), -g])   # RHO[u] = 1 - f  ->  not GT(cur, alt with face f)
        # availability
        for x in MOV:
            k = 1 - S[x]; q = opt(x, k); cur = gate_val(x)
            g0 = GT(prepend(ecar(q), tgt_e(x, k)), cur); g1 = GT(prepend(beta(q), tgt_b(x, k)), cur)
            AV[(S, x)] = E.AND([g0] if CTRL == 1 else [g0, g1], ("AV", S, x))
    # ---- the KEY run
    NR = (LEN if LEN is not None else 6) + 1
    R = [[E.v(("R", j, x)) for x in MOV] for j in range(NR)]
    for j in range(NR - 1):
        SEL = {}
        for S in STATES: SEL[S] = E.AND([R[j][x] if S[x] else -R[j][x] for x in MOV])
        AVR = []
        for x in MOV:
            y = E.new(("AVR", j, x)); AVR.append(y)
            for S in STATES: E.add([-SEL[S], -AV[(S, x)], y]); E.add([-SEL[S], AV[(S, x)], -y])
        for x in (0, 1):
            g = gov(opt(x, 0), opt(x, 1))          # gate of option 0 below option 1
            # moves iff AVR and the other option's gate is lower: R=0 & not g, or R=1 & g
            mv = E.AND([AVR[x], E.OR([E.AND([-R[j][x], -g]), E.AND([R[j][x], g])])])
            nx = E.XOR(R[j][x], mv); E.EQ(R[j + 1][x], nx)
        PREF = E.OR([E.AND([R[j + 1][0] if a else -R[j + 1][0], R[j + 1][1] if b else -R[j + 1][1], -gov(opt(0, a), opt(1, b))])
                     for a in (0, 1) for b in (0, 1)])
        for x in (2, 3):
            E.add([-AVR[x], -PREF, R[j + 1][x]]); E.add([-AVR[x], PREF, -R[j + 1][x]])
            E.add([AVR[x], -R[j][x], R[j + 1][x]]); E.add([AVR[x], R[j][x], -R[j + 1][x]])
    if LEN is not None:
        for j in range(LEN):
            E.add([E.XOR(R[j][x], R[j + 1][x]) for x in MOV])
    return E

def dimacs(E, path, header):
    with open(path, "w") as f:
        for h in header: f.write("c " + h + "\n")
        f.write("p cnf %d %d\n" % (E.n, len(E.cl)))
        for c in E.cl: f.write(" ".join(map(str, c)) + " 0\n")

if __name__ == "__main__":
    if sys.argv[1] == "dimacs":
        L = int(sys.argv[2]); E = build(L)
        dimacs(E, sys.argv[3], ["L-SI box 106 cnf106.py: some G* in L*_2 has L* >= %d (CTRL %d)" % (L, CTRL)])
        print("CNF106 L* >= %d: vars %d clauses %d" % (L, E.n, len(E.cl)))
