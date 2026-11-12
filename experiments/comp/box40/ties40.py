#!/usr/bin/env python3
"""L-COMP box 40 item 2 (gap G1, L-RED 65 R232 §1): HOW3 with EVERY legal tie resolution, on MY Γ3 engine (box34/own34.py build, S3
standard start, my n5b SpecSI values with Odd's optimal counterstrategy). HOW3 (RESULTS R125 as quoted in R232 §1): «every mover moving to a
⊴-best successor and keeping a best current one»; non-mover Even vertices frozen. A TIE = a mover that must switch and has >= 2 ⊴-best
successors; branching = every combination of choices at the tied movers of a state.
Per genome (from S3, scope: the whole HOW3 run to its fixpoint):
  T3n   = the n5v-rule run (own34.run: N5'-xi's S4a, ties «by SPEC's choice, then the larger index»), first fallback at T3n + 1;
  legal = 1 if own34's state sequence is a HOW3-legal path (sanity, must be 1);
  Hmax / Hmin = max / min HOW3 length over all tie resolutions (memoised longest/shortest path over states; DAG: values strictly rise);
  tiestates = states (on any path) with a tie; paths = number of distinct HOW3 paths;
  if paths <= PCAP: every path is enumerated and box 99's census (scc40.census) taken on it: locmax = max over paths of maxloc(C),
  locbig_max = max over paths of loc(giant SCC), ratio_max = max over paths of the ratio column, H>M = max over paths and SCCs of
  loc(C) − M_C (> 0 would be an SCC-LIN-type violation on the run), locfail_any / chainfail_any over paths.
Caps: SCAP distinct states, PRODCAP tie combinations at one state (else «capped»: reported, not analysed). Usage: ties40.py G.json ... | ties40.py --rand SEED COUNT NMMAX OUT (random k = 1, resumable)"""
import sys, os, json, random, itertools
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "box34"), os.path.join(H, "..", "box36")]
import own34, scc40, own36
from own34 import build, standard, SpecSI, EVEN
SCAP = int(os.environ.get("SCAP", "20000")); PRODCAP = int(os.environ.get("PRODCAP", "4096")); PCAP = int(os.environ.get("PCAP", "5000")); BRDUP = os.environ.get("BRDUP") == "1"


def analyse(G):
    g, V = build(G); n = g.n; SG = SpecSI(g); s0, _ = standard(G, V, g)
    mv = [V[("x", x)] for x in range(G["N"])]
    base = list(s0)
    cache = {}
    def moves(key):
        if key in cache: return cache[key]
        sig = list(base)
        for x, c in zip(mv, key): sig[x] = c
        vs = SG.evaluate(sig); opts = []; tie = False
        for x, c in zip(mv, key):
            imp = [w for w in g.succ[x] if SG.nvo(vs[c], vs[w]) < 0]
            if not imp: opts.append([c]); continue
            b = [g.succ[x][0]]
            for w in g.succ[x][1:]:
                d = SG.nvo(vs[w], vs[b[0]])
                if d > 0: b = [w]
                elif d == 0: b.append(w)
            if c in b: opts.append([c])                # cannot happen (c not best when improving exists); kept for legality
            else: opts.append(sorted(b)); tie |= len(b) >= 2
        prod = 1
        for o in opts: prod *= len(o)
        if prod > PRODCAP: raise OverflowError
        nxt = [] if all(len(o) == 1 and o[0] == c for o, c in zip(opts, key)) else [tuple(p) for p in itertools.product(*opts)]
        cache[key] = (nxt, tie)
        if len(cache) > SCAP: raise OverflowError
        return cache[key]
    start = tuple(s0[x] for x in mv)
    LG, SH, NP = {}, {}, {}
    order = []; seen = set(); stack = [(start, False)]
    while stack:                                       # iterative post-order DFS over the state DAG
        k, done = stack.pop()
        if done: order.append(k); continue
        if k in seen: continue
        seen.add(k); stack.append((k, True))
        for k2 in moves(k)[0]:
            if k2 not in seen: stack.append((k2, False))
    for k in order:
        nx = moves(k)[0]
        if not nx: LG[k] = SH[k] = 0; NP[k] = 1
        else: LG[k] = 1 + max(LG[j] for j in nx); SH[k] = 1 + min(SH[j] for j in nx); NP[k] = sum(NP[j] for j in nx)
    r = own34.run(G); T3n = r["T3"]; seq = [tuple(s[x] for x in mv) for s in r["sigs"]]
    legal = int(all(seq[t + 1] in moves(seq[t])[0] for t in range(T3n)) and not moves(seq[-1])[0] if r["fallback"] else 0)
    out = dict(T3n=T3n, legal=legal, Hmax=LG[start], Hmin=SH[start], states=len(seen), tiestates=sum(moves(k)[1] for k in seen), paths=NP[start])
    out.update({("n5v_" + k): v for k, v in scc40.census(G, [s for s in seq], T3n).items() if k in ("maxloc", "locbig", "ratio")})
    if NP[start] <= PCAP:
        best = dict(locmax=-1, locbig_max=-1, ratio_max=-1, HM=-10 ** 9, locfail_any=0, chainfail_any=0)
        def paths(k, acc):
            nx = moves(k)[0]
            if not nx: yield acc; return
            for j in nx: yield from paths(j, acc + [j])
        for p in paths(start, [start]):
            c = scc40.census(G, p, len(p) - 1); hm = c.pop("HM")
            best["locmax"] = max(best["locmax"], c["maxloc"]); best["locbig_max"] = max(best["locbig_max"], c["locbig"])
            best["ratio_max"] = max(best["ratio_max"], c["ratio"]); best["HM"] = max(best["HM"], hm)
            best["locfail_any"] |= c["locfail"] > 0; best["chainfail_any"] |= c["chainfail"]
        out.update(best)
    return out


def rgen(r, NMMAX):
    """samp38's law (box38 draw) at random (N, M) with N + M <= NMMAX, N >= 3, M >= N, EXCEPT the Ξ-target: X (-1) with probability 0.6,
    else a uniform mover (uniform Ξ-targets give k = 1 almost never at N >= 12: 4/100 at N 12, 0/100 at N 20); resampled until k = 1."""
    while True:
        N = r.randint(3, NMMAX // 2); M = r.randint(N, min(3 * N, NMMAX - N)); lev = [0]
        for _ in range(N - 1): lev.append(lev[-1] + r.randrange(2))       # = uniform over gen36.levvecs(N), without enumerating 2^(N-1)
        cuts = sorted(r.sample(range(1, M), N - 1)); D = [b - a for a, b in zip([0] + cuts, cuts + [M])]
        gate = list(range(M)); r.shuffle(gate); br = list(range(M)); r.shuffle(br); opts, gg, b = [], [], 0
        if BRDUP: br = [r.randrange(max(1, M // 3)) for _ in range(M)]   # repeated β ranks (env BRDUP=1): equal β priorities -> ties
        for x in range(N):
            oo, g1 = [], []
            for _ in range(D[x]):
                lower = [y for y in range(N) if lev[y] == lev[x] - 1]
                oo.append([-1 if lev[x] == 0 else r.choice(lower), (-1 if r.random() < 0.6 else r.randrange(N)), b]); g1.append(gate[b]); b += 1
            opts.append(oo); gg.append(g1)
        G = {"N": N, "lev": lev, "opts": opts, "gate": gg, "br": br, "bp": [r.randrange(2) for _ in range(M)], "start": [r.randrange(d) for d in D]}
        if own36.kfvs(G, 1) == 1: return G


def rgen_lred(rng, d, w, D):
    """COPY of L-RED's generator r231/dep231.rgen (= r221q brute221.rgen; claude/l-red 078e2b29, dep231.py l. 88-97), used only to replay
    L-RED 65's rand232 set (r232/rand232.py at 59daaef2: rng = Random(SEED); per genome rgen(rng, randint(1, 5), randint(1, 4),
    choice([2, 3, 4])); Ξ-cyclic allowed)."""
    N = d * w; lev = [x // w for x in range(N)]; opts = []
    for x in range(N):
        opts.append([[(rng.choice([y for y in range(N) if lev[y] == lev[x] - 1]) if lev[x] else -1), rng.choice(list(range(N)) + [-1]), 0] for _ in range(D)])
    M = N * D; perm = list(range(M)); rng.shuffle(perm); gate = []; i = 0
    for x in range(N):
        gate.append([])
        for o in opts[x]: o[2] = i; gate[x].append(perm[i]); i += 1
    br = list(range(M)); rng.shuffle(br)
    return {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": [rng.randrange(2) for _ in range(M)], "start": [rng.randrange(D) for _ in range(N)]}


if __name__ == "__main__":
    if sys.argv[1] == "--lred":
        SEED, CNT, OUT = int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(SEED)
        done = sum(1 for _ in open(OUT)) if os.path.exists(OUT) else 0
        for i in range(CNT):
            G = rgen_lred(rng, rng.randint(1, 5), rng.randint(1, 4), rng.choice([2, 3, 4]))
            if i < done: continue
            try: res = analyse(G)
            except OverflowError: res = dict(capped=1)
            with open(OUT, "a") as f: f.write(json.dumps(dict(i=i, tag="r%d" % i, N=G["N"], M=sum(map(len, G["opts"])), k=own36.kfvs(G, 1), **res, G=G)) + "\n")
        print("DONE", CNT); sys.exit(0)
    if sys.argv[1] == "--rand":
        SEED, CNT, NMMAX, OUT = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
        done = sum(1 for _ in open(OUT)) if os.path.exists(OUT) else 0
        for i in range(done, CNT):
            G = rgen(random.Random(f"{SEED}-{i}"), NMMAX)
            try: res = analyse(G)
            except OverflowError: res = dict(capped=1)
            with open(OUT, "a") as f: f.write(json.dumps(dict(i=i, N=G["N"], M=sum(map(len, G["opts"])), **res, G=G)) + "\n")
        print("DONE", CNT)
    else:
        for fn in sys.argv[1:]:
            G = json.load(open(fn))
            try: res = analyse(G)
            except OverflowError: res = dict(capped=1)
            print(os.path.basename(fn), "N+M", G["N"] + sum(map(len, G["opts"])), json.dumps(res), flush=True)
