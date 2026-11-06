#!/usr/bin/env python3
"""L-SI box 70: SAT frame ABS-m + IM (docs/si/N5-FRAME-box70.md §1). Variables:
 - an acyclic ISO Xi-graph on the 2m upper movers (option o = 2z + k -> target mover y != z or X); acyclicity by a transitive irreflexive
   reach relation R;
 - on[z][k][s][y]: y lies on the chain from option (z, k)'s target under state s (exact least-fixpoint definition, unique on a DAG);
 - C[z][s]: z's strictly better option at s (bit); LOCAL (C_z(s) depends only on the states on z's two chains; not on s_z) and, unless
   NOIM=1, IM (Lemma IM, box 69: an improving switch of a chain mover y moves z's preference only toward the option whose chain passes y,
   and not at all if both chains pass y);
 - key bits c[l][k] (BIT-CHAIN, levels 1..m-1); runs: states S[t][z], external bit B, flip indicators F[t] (monotone: at most one flip);
   step rule = BIT-CHAIN form of R104 (A-sets from the OLD state, keys from the NEW state, bottom level first).
Every ENC genome (R104 / R105) maps into the frame (LOCAL = R105 LOCAL, IM = Lemma IM, keys = BIT-CHAIN), so the frame is a RELAXATION:
UNSAT in the frame => no ENC genome. SAT models are frame systems, not necessarily ENC genomes.
Usage: frame.py m MODE T [T2]   MODE: t0 (flip-free run of T steps), t1 (run of T steps with <= 1 flip),
       sum (one flip-free run of T steps and one <= 1-flip run of T2 steps on the same system).  Env NOIM=1 drops IM (control).
Prints SAT / UNSAT, time, and for SAT the Xi-graph, c bits and runs."""
import sys, os, time, itertools
from pysat.formula import IDPool
from pysat.solvers import Cadical153
m, MODE, T = int(sys.argv[1]), sys.argv[2], int(sys.argv[3]); T2 = int(sys.argv[4]) if len(sys.argv) > 4 else 0
NOIM = os.environ.get("NOIM") == "1"
K = int(os.environ.get("K", "1"))                       # flips for modes tk / sumk
DUMP = os.environ.get("DUMP")                           # directory: write DIMACS (and the DRUP proof on UNSAT) there
PROOF = bool(DUMP) and os.environ.get("NOPROOF") != "1"  # box 72: NOPROOF=1 writes the DIMACS only (proofs at m >= 3 run to GBs)
U = 2 * m; NS = 1 << U; lev = [z // 2 + 1 for z in range(U)]
P = IDPool(); cl = []
def v(*a): return P.id(a)
TRUE = v("TRUE"); cl.append([TRUE])
def AND(*ls):
    o = P.id(("and",) + tuple(ls)); [cl.append([-o, l]) for l in ls]; cl.append([o] + [-l for l in ls]); return o
def OR(*ls):
    o = P.id(("or",) + tuple(ls)); [cl.append([o, -l]) for l in ls]; cl.append([-o] + list(ls)); return o
def XOR(a, b):
    o = P.id(("xor", a, b)); cl.extend([[-o, a, b], [-o, -a, -b], [o, -a, b], [o, a, -b]]); return o
def EQV(a, b): return -XOR(a, b)
def ITE(c, a, b):
    o = P.id(("ite", c, a, b)); cl.extend([[-c, -a, o], [-c, a, -o], [c, -b, o], [c, b, -o]]); return o
# Xi-graph
targets = {z: [-1] + [y for y in range(U) if y != z] for z in range(U)}
for z in range(U):
    for k in (0, 1):
        o = 2 * z + k; xs = [v("x", o, t) for t in targets[z]]
        cl.append(xs)
        for a, b in itertools.combinations(xs, 2): cl.append([-a, -b])
for a in range(U):
    for k in (0, 1):
        for b in range(U):
            if b != a: cl.append([-v("x", 2 * a + k, b), v("R", a, b)])
for a, b, c in itertools.permutations(range(U), 3): cl.append([-v("R", a, b), -v("R", b, c), v("R", a, c)])
for a, b in itertools.combinations(range(U), 2): cl.append([-v("R", a, b), -v("R", b, a)])
# chain membership
def on(z, k, s, y): return v("on", z, k, s, y)
for z in range(U):
    for k in (0, 1):
        for s in range(NS):
            for y in range(U):
                if y == z: continue
                terms = [v("x", 2 * z + k, y)]
                for w in range(U):
                    if w in (z, y): continue
                    terms.append(AND(on(z, k, s, w), v("x", 2 * w + ((s >> w) & 1), y)))
                o = on(z, k, s, y); [cl.append([o, -t]) for t in terms]; cl.append([-o] + terms)
def C(z, s): return v("C", z, s)
for z in range(U):
    for s in range(NS):
        s2 = s ^ (1 << z); cl.extend([[-C(z, s), C(z, s2)], [C(z, s), -C(z, s2)]])   # not on own state
        for y in range(U):
            if y == z: continue
            s2 = s ^ (1 << y); o0, o1 = on(z, 0, s, y), on(z, 1, s, y); a, b = C(z, s), C(z, s2)
            cl.extend([[o0, o1, -a, b], [o0, o1, a, -b]])                             # LOCAL
            if NOIM: continue
            u = -C(y, s) if (s >> y) & 1 else C(y, s)                                  # y unhappy at s
            cl.extend([[-o0, -o1, -u, -a, b], [-o0, -o1, -u, a, -b]])                   # IM (b): both chains
            cl.append([-o1, o0, -u, b, -a])                                             # IM (c): only option 1 -> C' in {C, 1}
            cl.append([-o0, o1, -u, -b, a])                                             # IM (c): only option 0 -> C' in {C, 0}
cbit = {(l, k): v("c", l, k) for l in range(1, m) for k in (0, 1)}
MV = {}
def run(tag, L, flip, kflips=None, idle=False):
    S = [[v("S", tag, t, z) for z in range(U)] for t in range(L + 1)]; B = v("B", tag)
    F = [v("F", tag, t) for t in range(L + 1)]
    if kflips is None:
        for t in range(L): cl.append([-F[t], F[t + 1]])
        if not flip: [cl.append([-f]) for f in F]
    else:                                                # F[t+1] = bit offset of step t (free); changes counted below
        D = [XOR(F[t], F[t + 1]) for t in range(1, L)]
        if kflips >= 0 and D:
            from pysat.card import CardEnc, EncType
            enc = CardEnc.atmost(lits=D, bound=kflips, top_id=P.top, encoding=EncType.seqcounter)
            for c2 in enc.clauses: cl.append(c2)
            P.top = max(P.top, enc.nv)              # later fresh ids come after the encoder's auxiliaries
    for t in range(L):
        eqs = []
        for s in range(NS):
            lits = [S[t][z] if (s >> z) & 1 else -S[t][z] for z in range(U)]; e = AND(*lits); eqs.append(e)
        Cs = []
        for z in range(U):
            c = v("Cs", tag, t, z)
            for s in range(NS): cl.extend([[-eqs[s], -C(z, s), c], [-eqs[s], C(z, s), -c]])
            Cs.append(c)
        bit = XOR(B, F[t + 1]); moves = []
        for l in range(1, m + 1):
            kp = -bit                                     # key-preferred option index: 0 iff b_(l-1) = 1
            for z in (2 * (l - 1), 2 * (l - 1) + 1):
                mv = AND(XOR(Cs[z], S[t][z]), EQV(Cs[z], kp)); moves.append(mv)
                cl.extend([[-S[t + 1][z], S[t][z], mv], [S[t + 1][z], -S[t][z], mv], [-S[t + 1][z], -S[t][z], -mv], [S[t + 1][z], S[t][z], -mv]])
            if l < m:
                a, b2 = S[t + 1][2 * (l - 1)], S[t + 1][2 * (l - 1) + 1]
                bit = ITE(XOR(a, b2), ITE(a, -bit, bit), ITE(a, cbit[(l, 1)], cbit[(l, 0)]))
        if not idle: cl.append(moves)                     # every step moves some mover (idle steps allowed in mode pm)
        MV.setdefault(tag, []).append(moves)
    return S, B, F
if MODE == "t0": runs = [run("a", T, False)]
elif MODE == "t1": runs = [run("a", T, True)]
elif MODE == "sum": runs = [run("a", T, False), run("b", T2, True)]
elif MODE == "tk": runs = [run("a", T, True, kflips=K)]                      # T-step run with <= K bit changes (K = -1: unlimited)
elif MODE == "sumk": runs = [run("a", T, False), run("b", T2, True, kflips=K)]
elif MODE == "pq":                                                               # box 73: flip-free run a (T) + one-flip run b (T2) with
    runs = [run("a", T, False), run("b", T2, True)]                              # the flip after exactly PRE steps; REL=pre: run a has the
    PRE = int(os.environ["PRE"]); Fb = runs[1][2]                                # pre-segment's bit; REL=post: the post-segment's bit
    for t in range(T2 + 1): cl.append([Fb[t]] if t >= PRE + 1 else [-Fb[t]])
    REL = os.environ.get("REL", "")
    if REL == "pre": cl.extend([[runs[0][1], -runs[1][1]], [-runs[0][1], runs[1][1]]])
    if REL == "post": cl.extend([[runs[0][1], runs[1][1]], [-runs[0][1], -runs[1][1]]])
elif MODE == "bits":                                                             # box 73: two flip-free runs, opposite external bits
    runs = [run("a", T, False), run("b", T2, False)]; cl.extend([[runs[0][1], runs[1][1]], [-runs[0][1], -runs[1][1]]])
elif MODE == "pm":
    # L-NEW CONJECTURE PM (degree 2): moves(x) <= 1 + desc(x). Query: mover x = PMX with desc(x) = PMD and moves(x) >= PMD + 2 within a
    # run of T steps (idle steps allowed, so every run of length <= T is covered) with <= K bit changes.
    from pysat.card import CardEnc, EncType
    X, Dd = int(os.environ["PMX"]), int(os.environ["PMD"])
    runs = [run("a", T, True, kflips=K, idle=True)]
    def edge(w, y): return OR(*[v("x", 2 * w + k, y) for k in (0, 1)])
    def dsc(y): return v("desc", X, y)
    for y in range(U):
        if y == X: continue
        terms = [edge(X, y)] + [AND(dsc(w), edge(w, y)) for w in range(U) if w not in (X, y)]
        o = dsc(y); [cl.append([o, -t]) for t in terms]; cl.append([-o] + terms)
    dl = [dsc(y) for y in range(U) if y != X]
    enc = CardEnc.equals(lits=dl, bound=Dd, top_id=P.top, encoding=EncType.seqcounter); cl.extend(enc.clauses); P.top = max(P.top, enc.nv)
    mx = [MV["a"][t][X] for t in range(T)]                 # move indicator of mover X at each step (moves list is in mover order)
    enc = CardEnc.atleast(lits=mx, bound=Dd + int(os.environ.get("PMPLUS", "2")), top_id=P.top, encoding=EncType.seqcounter); cl.extend(enc.clauses); P.top = max(P.top, enc.nv)
else: raise SystemExit("mode")
import hashlib
tag = "m%d_%s_T%d_T2%d_K%d_NOIM%d" % (m, MODE, T, T2, K, int(NOIM))
if DUMP:
    os.makedirs(DUMP, exist_ok=True); nv = max(abs(l) for c in cl for l in c)
    with open(os.path.join(DUMP, tag + ".cnf"), "w") as fo:
        fo.write("p cnf %d %d\n" % (nv, len(cl)))
        for c in cl: fo.write(" ".join(map(str, c)) + " 0\n")
    print("DIMACS", tag + ".cnf", "sha1", hashlib.sha1(open(os.path.join(DUMP, tag + ".cnf"), "rb").read()).hexdigest(), flush=True)
t0 = time.time()
from pysat.solvers import Solver
sol = Solver(name="cadical153", with_proof=PROOF, bootstrap_with=cl); r = sol.solve(); dt = time.time() - t0
print("m", m, "MODE", MODE, "T", T, "T2", T2, "K", K, "NOIM", int(NOIM), "vars", P.top, "clauses", len(cl), "->", "SAT" if r else "UNSAT", "%.1fs" % dt, flush=True)
if PROOF and not r:
    pf = os.path.join(DUMP, tag + ".drup")
    with open(pf, "w") as fo:
        for line in sol.get_proof(): fo.write(line + "\n")
    print("DRUP", tag + ".drup", "sha1", hashlib.sha1(open(pf, "rb").read()).hexdigest(), "bytes", os.path.getsize(pf), flush=True)
if r:
    M = set(l for l in sol.get_model() if l > 0)
    xt = [next(t for t in targets[o // 2] if v("x", o, t) in M) for o in range(2 * U)]
    print("xt", xt, "c", {k: int(cb in M) for k, cb in cbit.items()})
    for S, B, F in runs:
        print("B", int(B in M), "F", [int(f in M) for f in F], "states", ["".join(str(int(S[t][z] in M)) for z in range(U)) for t in range(len(S))])
