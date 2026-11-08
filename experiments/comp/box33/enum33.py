#!/usr/bin/env python3
"""L-COMP box 33 (Lead 14:16Z): EXACT small-size maxima of A (longest two-letter alternation in one tops sequence, Theorem ALT-EQUIV,
L-NEW box 197 Add. 2) and T3 (N5'-xi from S3 on Gamma3, up to the first fallback) over ALL genomes of a given (N, M).
ENGINE (stated with every number): L-NEW's asc197.run (claude/l-new b61c2029, experiments/new/box197/asc197.py: gamma3.build box 189,
n5v.step mode xi box 190, start n5x.start_pair = S3), imported read-only from a checkout given by env LNEW. It is NOT an independent
engine: the independent cross-check (my n5b/n5v mode xi) is a NEEDS item.
Genome space (the schema of eg195.gen): N movers, levels lev = (0) | (0,0) | (0,1) (levels nondecreasing from 0, each level reachable);
every mover has >= 1 option, M options in all; option k of x = [wt, xt, b]: wt = -1 at level 0, else the unique mover of level lev-1
(N <= 2); xt in {-1} + movers; b = the option's global index; gate = a permutation of 0..M-1 over options; br = a permutation of 0..M-1;
bp in {0,1}^M; start = one option per mover. ALL of them are enumerated (no symmetry reduction), in a fixed order, index i.
--noelev: Gamma3 is built with e-priorities ordered by gate only (gamma3.build's key (lev, gate) replaced by (gate)), i.e. without [E-LEV].
Sharding: SHARD k/K processes i = k mod K; checkpoint every CK genomes to OUT.ck (resume skips done indices). Output OUT: one line per
checkpoint, final line SUMMARY with maxA, maxT3, counts, argmax genomes (json).
Usage: LNEW=<l-new checkout> enum33.py N M k/K OUT [--noelev] [--sample S --seed R]"""
import sys, os, json, itertools, random, types, time, hashlib
LNEW = os.environ['LNEW']
args = [a for a in sys.argv[1:] if not a.startswith('--')]
N, M = int(args[0]), int(args[1]); k, K = map(int, args[2].split('/')); OUT = args[3]
NOELEV = '--noelev' in sys.argv
SAMPLE = int(sys.argv[sys.argv.index('--sample') + 1]) if '--sample' in sys.argv else 0
SEED = int(sys.argv[sys.argv.index('--seed') + 1]) if '--seed' in sys.argv else 1
CK = 5000
sys.path[:0] = [os.path.join(LNEW, p) for p in ("experiments/new/box197", "experiments/new/box196", "experiments/new/box195", "experiments/new/box191",
                "experiments/new/box189", "experiments/new/box190", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
os.environ.setdefault("ROOT", LNEW); os.environ.setdefault("Q196_ROOT", LNEW); os.environ.setdefault("EG195_ROOT", LNEW)
if NOELEV:
    src = open(os.path.join(LNEW, "experiments/new/box189/gamma3.py")).read()
    old = 'sorted(O, key=lambda q: (lev[q[0]], gate[q[0]][q[1]]))): prio[V[("e", q)]]'
    assert src.count(old) == 1, 'gamma3 e-priority line not found'
    src = src.replace(old, 'sorted(O, key=lambda q: gate[q[0]][q[1]])): prio[V[("e", q)]]')
    mod = types.ModuleType("gamma3"); mod.__file__ = os.path.join(LNEW, "experiments/new/box189/gamma3.py")
    exec(compile(src, mod.__file__, "exec"), mod.__dict__); sys.modules["gamma3"] = mod
import asc197

def structures():
    """(lev, D) per mover: level vectors and option splits."""
    levs = {1: [(0,)], 2: [(0, 0), (0, 1)]}[N] if N <= 2 else None
    for lev in levs:
        for D in itertools.product(range(1, M + 1), repeat=N):
            if sum(D) == M: yield lev, D

def genomes():
    i = 0
    for lev, D in structures():
        owner = [x for x in range(N) for _ in range(D[x])]
        for xts in itertools.product(range(-1, N), repeat=M):
            for gate in itertools.permutations(range(M)):
                for br in itertools.permutations(range(M)):
                    for bp in itertools.product((0, 1), repeat=M):
                        for st in itertools.product(*[range(d) for d in D]):
                            yield i, (lev, D, owner, xts, gate, br, bp, st); i += 1

def make(lev, D, owner, xts, gate, br, bp, st):
    opts = []; g = []; b = 0
    for x in range(N):
        oo = []; gg = []
        for _ in range(D[x]):
            wt = -1 if lev[x] == 0 else [y for y in range(N) if lev[y] == lev[x] - 1][0]
            oo.append([wt, xts[b], b]); gg.append(gate[b]); b += 1
        opts.append(oo); g.append(gg)
    return {"N": N, "lev": list(lev), "opts": opts, "gate": g, "br": list(br), "bp": list(bp), "start": list(st)}

def sample_genomes():
    rng = random.Random(SEED)
    levs = [(0,) * N] + ([tuple(x // w for x in range(N)) for w in range(1, N) if True])
    for i in range(SAMPLE):
        lev = rng.choice(levs)
        while True:
            D = [rng.randint(1, M) for _ in range(N)]
            if sum(D) == M: break
        owner = [x for x in range(N) for _ in range(D[x])]
        xts = [rng.randrange(-1, N) for _ in range(M)]
        gate = list(range(M)); rng.shuffle(gate); br = list(range(M)); rng.shuffle(br)
        bp = [rng.randrange(2) for _ in range(M)]; st = [rng.randrange(d) for d in D]
        yield i, (lev, D, owner, xts, gate, br, bp, st)

def make_n(lev, D, owner, xts, gate, br, bp, st):   # general N (sample mode): wt = some mover of the level below (first one)
    opts = []; g = []; b = 0
    for x in range(N):
        oo = []; gg = []
        for _ in range(D[x]):
            lower = [y for y in range(N) if lev[y] == lev[x] - 1]
            wt = -1 if lev[x] == 0 else lower[0]
            oo.append([wt, xts[b], b]); gg.append(gate[b]); b += 1
        opts.append(oo); g.append(gg)
    return {"N": N, "lev": list(lev), "opts": opts, "gate": g, "br": list(br), "bp": list(bp), "start": list(st)}

ckp = OUT + '.ck'
st = dict(done=-1, n=0, maxA=-1, maxT3=-1, argA=None, argT3=None, hist={}, capped=0, err=0)
if os.path.exists(ckp): st = json.load(open(ckp))
t0 = time.time(); src_iter = sample_genomes() if SAMPLE else genomes()
for i, spec in src_iter:
    if i % K != k or i <= st['done']: continue
    G = make_n(*spec) if SAMPLE else make(*spec)
    try:
        r = asc197.run(G)
    except Exception as e:
        st['err'] += 1; st['done'] = i; continue
    A, T3 = r.get('maxalt', 0), r['T3']
    st['n'] += 1; st['hist'][str(A)] = st['hist'].get(str(A), 0) + 1
    if T3 >= 20000: st['capped'] += 1
    if A > st['maxA']: st['maxA'] = A; st['argA'] = G
    if T3 > st['maxT3']: st['maxT3'] = T3; st['argT3'] = G
    st['done'] = i
    if st['n'] % CK == 0:
        json.dump(st, open(ckp, 'w'))
        with open(OUT, 'a') as f: f.write(f"ck i {i} n {st['n']} maxA {st['maxA']} maxT3 {st['maxT3']} hist {st['hist']} err {st['err']} {time.time() - t0:.0f}s\n")
json.dump(st, open(ckp, 'w'))
with open(OUT, 'a') as f:
    f.write(f"SUMMARY N {N} M {M} shard {k}/{K} elev {not NOELEV} sample {SAMPLE} n {st['n']} maxA {st['maxA']} maxT3 {st['maxT3']} hist {st['hist']} capped {st['capped']} err {st['err']}\n")
    f.write("ARGMAX_A " + json.dumps(st['argA']) + "\n"); f.write("ARGMAX_T3 " + json.dumps(st['argT3']) + "\n")
