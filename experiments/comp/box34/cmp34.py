#!/usr/bin/env python3
"""L-COMP box 34 item 3: cross-check own34 (independent) against asc197 @ f98e93ee (fixed counter; compared on T3 and maxalt) and
asc197 @ b61c2029 (BOX 33's engine; compared on T3 always, on maxalt only where the definitions agree, i.e. where the fixed value != 1;
where fixed = 1 the old counter must print 0). Plus a game-level check: own34.build == gamma3.build (prio, owner, succ) on every genome.
Sampler (scope): N, M given; lev uniform over {(0,)} (N 1), {(0,0), (0,1)} (N 2), {(0,0,0), (0,1,2), (0,0,1), (0,1,1)} (N 3, every
nondecreasing level vector from 0 with each level reachable: (0,0,1) and (0,1,1) included); option split D uniform over compositions of
M into N parts >= 1; xt uniform in {-1} + movers per option; gate, br uniform permutations; bp uniform bits; start uniform; wt = the
first mover of level lev - 1 (as enum33 / eg195 schema). Not uniform over genomes (compositions weigh equally).
Usage: LNEW_OLD=<b61c2029 tree> LNEW_FIX=<f98e93ee tree> cmp34.py N M COUNT SEED OUT [--noelev] [--files F.json ...]"""
import sys, os, json, random, itertools, subprocess
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
import own34
a = [x for x in sys.argv[1:] if not x.startswith('--')]
NOELEV = '--noelev' in sys.argv; FILES = sys.argv[sys.argv.index('--files') + 1:] if '--files' in sys.argv else None
if FILES: a = a[:5]
N, M, COUNT, SEED, OUT = int(a[0]), int(a[1]), int(a[2]), int(a[3]), a[4]
LEVS = {1: [(0,)], 2: [(0, 0), (0, 1)], 3: [(0, 0, 0), (0, 1, 2), (0, 0, 1), (0, 1, 1)]}

def comps(M, N):
    return [c for c in itertools.product(range(1, M + 1), repeat=N) if sum(c) == M]

def sample(rng):
    lev = rng.choice(LEVS[N]); D = rng.choice(comps(M, N))
    gate = list(range(M)); rng.shuffle(gate); br = list(range(M)); rng.shuffle(br)
    opts = []; g = []; b = 0
    for x in range(N):
        oo = []; gg = []
        for _ in range(D[x]):
            wt = -1 if lev[x] == 0 else [y for y in range(N) if lev[y] == lev[x] - 1][0]
            oo.append([wt, rng.randrange(-1, N), b]); gg.append(gate[b]); b += 1
        opts.append(oo); g.append(gg)
    return {"N": N, "lev": list(lev), "opts": opts, "gate": g, "br": br, "bp": [rng.randrange(2) for _ in range(M)],
            "start": [rng.randrange(d) for d in D]}

if FILES:
    Gs = [json.load(open(f)) for f in FILES]; names = FILES
else:
    rng = random.Random(SEED); Gs = [sample(rng) for _ in range(COUNT)]; names = [f"s{i}" for i in range(COUNT)]
inp = "".join(json.dumps(G) + "\n" for G in Gs)
fl = ["--noelev"] if NOELEV else []
def ref(tree, extra=()):
    p = subprocess.run([sys.executable, os.path.join(H, "ref34.py"), *fl, *extra], input=inp, capture_output=True, text=True,
                       env=dict(os.environ, LNEW=tree), check=True)
    return [json.loads(l) for l in p.stdout.splitlines()]
games = ref(os.environ["LNEW_FIX"], ["--game"]); fix = ref(os.environ["LNEW_FIX"]); old = ref(os.environ["LNEW_OLD"])
mm = dict(game=0, T3fix=0, Afix=0, T3old=0, Aold=0, err=0); rows = []; hT = {}; hA = {}; hAo = {}; arg = {}
with open(OUT, "w") as f:
    f.write(f"# cmp34 N {N} M {M} count {len(Gs)} seed {SEED} elev {not NOELEV} files {bool(FILES)}\n")
    for nm, G, gr, rf, ro in zip(names, Gs, games, fix, old):
        gm, V = own34.build(G, not NOELEV)
        if [gm.prio, gm.owner, [sorted(s) for s in gm.succ]] != [gr["prio"], gr["owner"], gr["succ"]]:
            mm["game"] += 1; f.write(f"GAME-MISMATCH {nm} {json.dumps(G)}\n")
        me = own34.measure(G, not NOELEV)
        if "err" in rf or "err" in ro: mm["err"] += 1; f.write(f"REF-ERR {nm} {rf} {ro}\n"); continue
        hT[me["T3"]] = hT.get(me["T3"], 0) + 1; hA[me["maxalt"]] = hA.get(me["maxalt"], 0) + 1; hAo[ro["maxalt"]] = hAo.get(ro["maxalt"], 0) + 1
        for key in ("maxalt", "T3"):
            if key not in arg or me[key] > arg[key][0]: arg[key] = (me[key], nm, G)
        bad = []
        if me["T3"] != rf["T3"]: mm["T3fix"] += 1; bad.append("T3fix")
        if me["maxalt"] != rf["maxalt"]: mm["Afix"] += 1; bad.append("Afix")
        if me["T3"] != ro["T3"]: mm["T3old"] += 1; bad.append("T3old")
        if (me["maxalt"] != 1 and me["maxalt"] != ro["maxalt"]) or (me["maxalt"] == 1 and ro["maxalt"] != 0): mm["Aold"] += 1; bad.append("Aold")
        if bad:
            f.write(f"MISMATCH {nm} {bad} own T3 {me['T3']} maxalt {me['maxalt']} | fix T3 {rf['T3']} maxalt {rf['maxalt']} | old T3 {ro['T3']} maxalt {ro['maxalt']} | {json.dumps(G)}\n")
        elif FILES:
            f.write(f"OK {nm} own T3 {me['T3']} maxalt {me['maxalt']} | fix {rf['T3']} {rf['maxalt']} | old {ro['T3']} {ro['maxalt']}\n")
    for key in arg: f.write(f"ARGMAX_{key} {arg[key][0]} {arg[key][1]} {json.dumps(arg[key][2])}\n")
    f.write(f"SUMMARY N {N} M {M} count {len(Gs)} seed {SEED} elev {not NOELEV} mismatches {mm} T3hist {dict(sorted(hT.items()))} maxalt_hist(fixed) {dict(sorted(hA.items()))} maxalt_hist(old b61c2029) {dict(sorted(hAo.items()))}\n")
print(open(OUT).read().splitlines()[-1]); sys.exit(1 if any(mm.values()) else 0)
