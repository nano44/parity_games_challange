#!/usr/bin/env python3
"""REFEREE successor 24: pinned-genome cross-check of L-COMP box 27 cnf.py (claude/l-comp 6f19564f) against my own simulator
t3r_sim.py (written from R104's text). Pinning code is mine (pinck.py not used).
For a genome G of 𝓛^R_d and a start s0 with my T:
  (1) CNF(d, T) + pins (genome + start) must be SAT, and the decoded states S[0..T] must EQUAL my simulator's states;
  (2) CNF(d, T + 1) + pins must be UNSAT;
  (3) GENOME-ONLY mode (start free; with GSTART=1): CNF(d, Tmax + 1) + genome pins UNSAT and CNF(d, Tmax) SAT,
      Tmax = my max of T over all 2^N starts.
Usage: CNFDIR=<dir with cnf.py> python3 -I t3r_pin.py MODE args
  MODE files f.json ...        every start of every listed genome (+ genome-only test)
  MODE mutants f.json n seed   n single-field mutants of each champion (rank swap, parity flip, gate swap, Xi-target change), all starts
  MODE random d n seed         n random genomes of 𝓛^R_d (Xi-targets anywhere, acyclic), hill-climbed for half of them, all starts
"""
import itertools, json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import t3r_sim as R
sys.path.insert(0, os.environ["CNFDIR"])
for v in ("SYM", "CUBE", "FREE0", "ISO", "KF", "P"):
    os.environ.pop(v, None)
import cnf
from pysat.solvers import Solver

SOLVER = os.environ.get("SOLVER", "cadical195")

def pins(G, I, start):
    cl = []
    N = G["N"]
    for (x, k) in I["opts"]:
        y = G["opts"][x][k][1]
        cl.append([I["Xv"][(x, k)][y]])                       # exactly-one is in the CNF
        b = G["opts"][x][k][2]
        cl.append([I["par"][(x, k)] if G["bp"][b] == 1 else -I["par"][(x, k)]])
    rank = {o: G["br"][G["opts"][o[0]][o[1]][2]] for o in I["opts"]}
    for (a, b), lit in I["rk"].items():
        cl.append([lit] if rank[a] < rank[b] else [-lit])
    for l, V in I["gord"].items():
        for (a, b), lit in V.items():
            cl.append([lit] if G["gate"][a[0]][a[1]] < G["gate"][b[0]][b[1]] else [-lit])
    if start is not None:
        for x in range(N):
            a = I["S"][0][x]
            cl.append([a] if start[x] else [-a])
    return cl

def solve(G, d, L, start):
    C, I = cnf.build(d, L, None, "R")
    s = Solver(name=SOLVER, bootstrap_with=C.cl + pins(G, I, start))
    r = s.solve()
    states = None
    if r:
        m = s.get_model()
        val = lambda l: l if isinstance(l, bool) else ((l > 0) == (m[abs(l) - 1] > 0))
        states = [tuple(int(val(I["S"][t][x])) for x in range(G["N"])) for t in range(L + 1)]
    s.delete()
    return r, states

STATS = {"runs": 0, "bad": 0, "hist": {}, "gonly": 0, "gbad": 0}

def check_run(G, d, st, tag):
    S = R.run(G, st)
    T = len(S) - 1
    STATS["runs"] += 1
    STATS["hist"][T] = STATS["hist"].get(T, 0) + 1
    ok = True
    if T >= 1:
        r, states = solve(G, d, T, st)
        if not r or [tuple(v) for v in states] != [tuple(v) for v in S]:
            ok = False
            print("DISAGREE-STATES", tag, st, T, r, states, S, flush=True)
    r2, _ = solve(G, d, T + 1, st)
    if r2:
        ok = False
        print("DISAGREE-LONGER", tag, st, T, flush=True)
    if not ok:
        STATS["bad"] += 1
    return T

def check_genome(G, d, tag, all_starts=True):
    starts = list(itertools.product((0, 1), repeat=G["N"])) if all_starts else [tuple(G["start"])]
    Ts = [check_run(G, d, st, tag) for st in starts]
    if all_starts and os.environ.get("GSTART") == "1":
        Tm = max(Ts)
        STATS["gonly"] += 1
        a = solve(G, d, Tm, None)[0] if Tm >= 1 else True
        b = solve(G, d, Tm + 1, None)[0]
        if not a or b:
            STATS["gbad"] += 1
            print("DISAGREE-GENOME", tag, Tm, a, b, flush=True)
    return max(Ts)

def rgen(rng, d):
    N = 2 * d
    order = list(range(N)); rng.shuffle(order); pos = {v: i for i, v in enumerate(order)}
    ranks = list(range(2 * N)); rng.shuffle(ranks)
    gates = list(range(2 * N)); rng.shuffle(gates)
    opts = []
    for x in range(N):
        later = [y for y in range(N) if pos[y] > pos[x]]
        o = []
        for k in range(2):
            xt = rng.choice(later + [-1, -1]) if later else -1
            o.append([-1 if x < 2 else 2 * (x // 2 - 1) + k, xt, 2 * x + k])
        opts.append(o)
    return {"N": N, "lev": [x // 2 for x in range(N)], "opts": opts,
            "gate": [[gates[2 * x], gates[2 * x + 1]] for x in range(N)], "br": ranks,
            "bp": [rng.randrange(2) for _ in range(2 * N)], "start": [0] * N}

def mutate(rng, G):
    H = json.loads(json.dumps(G))
    N = H["N"]
    while True:
        kind = rng.randrange(4)
        if kind == 0:
            a, b = rng.sample(range(2 * N), 2); H["br"][a], H["br"][b] = H["br"][b], H["br"][a]
        elif kind == 1:
            a = rng.randrange(2 * N); H["bp"][a] ^= 1
        elif kind == 2:
            x, y = rng.randrange(N), rng.randrange(N); k, j = rng.randrange(2), rng.randrange(2)
            H["gate"][x][k], H["gate"][y][j] = H["gate"][y][j], H["gate"][x][k]
        else:
            x, k = rng.randrange(N), rng.randrange(2)
            H["opts"][x][k][1] = rng.choice([y for y in range(N) if y != x] + [-1])
        if R.in_LR(H) and H != G:
            return H
        H = json.loads(json.dumps(G))

def tmax(G):
    return max(len(R.run(G, st)) - 1 for st in itertools.product((0, 1), repeat=G["N"]))

def climb(rng, G, iters):
    best, bt = G, tmax(G)
    for _ in range(iters):
        H = mutate(rng, best)
        t = tmax(H)
        if t >= bt:
            best, bt = H, t
    return best, bt

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "files":
        for f in sys.argv[2:]:
            G = json.load(open(f)); d = G["N"] // 2
            assert R.in_LR(G, d), f
            m = check_genome(G, d, os.path.basename(f))
            print("FILE", os.path.basename(f), "max T", m, flush=True)
    elif mode == "mutants":
        f, n, seed = sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
        rng = random.Random(seed); G0 = json.load(open(f)); d = G0["N"] // 2
        mx = {}
        for i in range(n):
            H = mutate(rng, G0)
            m = check_genome(H, d, f"mut{i}")
            mx[m] = mx.get(m, 0) + 1
        print("MUTANTS", os.path.basename(f), n, "max-T histogram", dict(sorted(mx.items())), flush=True)
    elif mode == "random":
        d, n, seed = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
        rng = random.Random(seed); mx = {}
        for i in range(n):
            G = rgen(rng, d)
            if i % 2 == 1:
                G, _ = climb(rng, G, int(os.environ.get("CLIMB", "60")))
            m = check_genome(G, d, f"rnd{i}")
            mx[m] = mx.get(m, 0) + 1
        print("RANDOM d", d, n, "max-T histogram", dict(sorted(mx.items())), flush=True)
    print("TOTAL runs", STATS["runs"], "T histogram", dict(sorted(STATS["hist"].items())), "run disagreements", STATS["bad"],
          "genome-only tests", STATS["gonly"], "genome-only disagreements", STATS["gbad"], flush=True)
