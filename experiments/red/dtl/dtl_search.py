#!/usr/bin/env python3
"""Free-form hill-climb over small parity games maximising Oink DTL's learned-tangle count (L-RED, DTL box).
Fitness = tangles found by `oink --dtl --no-single --no-wcwc --no-loops` (raw solver, no preprocessing, self-loops kept;
before 16:02Z the runs used --no-single --no-wcwc only). Mutations: add/remove an edge,
change a priority, flip an owner. Usage: dtl_search.py OINK n [--steps 20000] [--seed 0] [--maxpr P] [--even-min FRAC] [--fitness tangles|unsolved|wrong|perhead|perheadsearch|persearch|prunemono|dups|straddles|alpha|strch|newrecur|maxsets|pairs|iters|restarts|maxrestarts|osc|rep|excess|carries|pviol|resets|ogate|evens] [--maxeven K] [--grow k] [--injective] [--loops] [--solver dtl|idtl] [--from game.pg] [--eval game.pg] [--out best.pg]"""
import sys, os, random, subprocess, tempfile, time, re
oink, n = sys.argv[1], int(sys.argv[2]); arg = lambda k, d: type(d)(sys.argv[sys.argv.index(k) + 1]) if k in sys.argv else d
steps, seed, maxpr = arg("--steps", 20000), arg("--seed", 0), arg("--maxpr", 2 * int(sys.argv[2])); rng = random.Random(seed)
evenmin = arg("--even-min", 0.0)
maxeven = arg("--maxeven", 0)                  # if > 0: reject games with more than this many Even-priority vertices
SOLVER = "--" + arg("--solver", "dtl")         # dtl | idtl
OINKFLAGS = ["--no-single", "--no-wcwc", "--no-loops"]   # the pinned algorithm (CHECKER C3): no preprocessing, self-loops kept
loops = "--loops" in sys.argv                  # bias mutations toward self-loops and toward renumbering equal-priority vertices
fitness = arg("--fitness", "tangles")   # tangles | unsolved (vertices DTL leaves unsolved) | perhead (max tangles learned at one top priority; use --injective)
injective = "--injective" in sys.argv    # priorities = a permutation of 0..n-1, so a tangle's priority names its top      # reject games with fewer than this fraction of Even-owned vertices (two-player search)
tmp = tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False).name


def dumps(g):
    pr, ow, succ = g
    return f"parity {n - 1};\n" + "".join(f"{v} {pr[v]} {ow[v]} {','.join(map(str, sorted(succ[v])))};\n" for v in range(n))


def score_py(g):
    """Exact per-top-vertex measures via the instrumented Python DTL (dtl_flipflop.py; slower than Oink).
    rep: sum over top vertices of (number of searches in which the top learns a tangle - 1), plus the number of searches
    (a chain of singleton tangles scores ~searches; a counter re-learns at the same tops). Fails closed on any exception."""
    import importlib.util, os as _os, io, contextlib
    spec = importlib.util.spec_from_file_location("ff", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "dtl_flipflop.py"))
    ff = importlib.util.module_from_spec(spec); spec.loader.exec_module(ff)
    try:
        d = ff.load(tmp, "oink")
    except Exception:
        return -1
    per = {}
    for sr in d.searches:
        for top, vs, _ in sr["tangles"]: per.setdefault((sr["player"], top), set()).add(sr["index"])
    if fitness == "pviol":     # adversarial test of Claim P/Q (dtl_ctxmono.check): violations, plus recurring context pairs/1000
        spec2 = importlib.util.spec_from_file_location("cm", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "dtl_ctxmono.py"))
        cm = importlib.util.module_from_spec(spec2); spec2.loader.exec_module(cm)
        ctx, pairs, P, Q, M = cm.check(d)
        return 100 * (P + Q) + pairs / 1000.0
    if fitness == "carries":   # (CARRY) moves: consecutive same-player searches whose depth-0 piece 0 differs (removed set or kind),
        c = 0                  # plus searches/1000 as a tie-break; dominion searches excluded
        for pl in (0, 1):
            ss = [sr for sr in d.searches if sr["player"] == pl and sr["pieces"]]
            for a, b in zip(ss, ss[1:]):
                if a["dominions"] or b["G"] != a["G"]: continue
                x, y = a["pieces"][0], b["pieces"][0]
                if (x["kind"], x.get("removed")) != (y["kind"], y.get("removed")): c += 1
        return c + d.iterations / 1000.0
    if fitness == "ogate":     # CARRY box (Opus 5.5): order-gate events (same sptl region set, different top SCC); OTHER weighs 100
        spec3 = importlib.util.spec_from_file_location("og", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "carry", "dtl_ogate.py"))
        og = importlib.util.module_from_spec(spec3); spec3.loader.exec_module(og)
        try:
            e = og.run(tmp).events
        except Exception:
            return -1
        return sum(100 if x["cls"] == "OTHER" else 1 for x in e) + d.iterations / 1000.0
    if fitness == "resets":    # CARRY box (Opus 5.5): (searches - dominions) * (1 + visits of a recurring (player, R) at which some
        spec2 = importlib.util.spec_from_file_location("cm", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "dtl_ctxmono.py"))
        cm = importlib.util.module_from_spec(spec2); spec2.loader.exec_module(cm)   # pruning round DROPS, i.e. fixed-context resets)
        seen, rv = {}, 0
        for sr in d.searches:
            for bv in sr["bv"]:
                if not bv["rounds"]: continue
                key = (sr["player"], bv["R"]); prof = cm.profile(bv)
                if key in seen and any(v in seen[key] and prof[v] < seen[key][v] for v in prof): rv += 1
                seen[key] = prof
        return (d.iterations - d.dominions) * (1 + rv)
    if fitness == "excess":    # searches minus distinct (player, top vertex) pairs that learn: a chain of singletons scores ~0,
        return d.iterations - d.dominions - len(per)   # a counter (few tops, many searches) scores high; dominion searches do not count
    return sum(len(x) - 1 for x in per.values()) + d.iterations


def score(g):
    open(tmp, "w").write(dumps(g))
    if fitness in ("rep", "excess", "carries", "pviol", "resets", "ogate"): return score_py(g)
    try:
        r = subprocess.run([oink, SOLVER] + OINKFLAGS + (["-t", "-t", "-t"] if fitness in ("strch", "newrecur", "maxsets", "pairs") else ["-t", "-t"] if fitness.startswith("per") or fitness in ("prunemono", "dups", "alpha", "straddles", "restarts", "maxrestarts", "osc") else []) + (["-v"] if fitness == "wrong" else []) + [tmp, tmp + ".sol"], capture_output=True, text=True, timeout=20)
    except subprocess.TimeoutExpired:
        return 10 ** 6          # a timeout is interesting in itself
    if fitness in ("unsolved", "wrong"):
        try: solved = sum(1 for l in open(tmp + ".sol") if l.strip() and not l.startswith("paritysol"))
        except FileNotFoundError: solved = n
        bad = 0
        if fitness == "wrong":      # Oink's own verifier (-v): a failed verification or a solver error counts 1000
            out = r.stdout + r.stderr
            bad = 1000 if ("error" in out.lower() or "verified" not in out) else 0
        return n - solved + bad
    if fitness in ("maxsets", "pairs"):   # (D): max distinct region vertex sets at one top / total distinct (top, set) pairs, all pieces
        import importlib.util, os as _os
        spec = importlib.util.spec_from_file_location("sc", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "dtl_strchanges.py"))
        sc = importlib.util.module_from_spec(spec); spec.loader.exec_module(sc)
        out = re.sub(r"\x1b\[[0-9;]*m", "", r.stdout + r.stderr)
        regions, seen, changes, occ, sets_per_top = sc.measure(out)
        return max((len(v) for v in sets_per_top.values()), default=0) if fitness == "maxsets" else len(seen)
    if fitness == "newrecur":        # new tangles learned at a (top, region set) seen before (the end state of the Lead's 18:02Z item 1)
        import importlib.util, os as _os
        spec = importlib.util.spec_from_file_location("sc", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "dtl_strchanges.py"))
        sc = importlib.util.module_from_spec(spec); spec.loader.exec_module(sc)
        out = re.sub(r"\x1b\[[0-9;]*m", "", r.stdout + r.stderr)
        return sc.measure(out)[2].get("__newrecur__", 0)
    if fitness == "strch":          # GAP-A: strategy changes at a fixed (top, region set), detector build at -t -t -t
        import importlib.util, os as _os
        spec = importlib.util.spec_from_file_location("sc", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "dtl_strchanges.py"))
        sc = importlib.util.module_from_spec(spec); spec.loader.exec_module(sc)
        out = re.sub(r"\x1b\[[0-9;]*m", "", r.stdout + r.stderr)
        return sum(sc.measure(out)[2].values())
    if fitness in ("alpha", "straddles"):
        # with the L-RED detector build (scratchpad oink-det): "STRADDLE tangle ..." lines at every stable pruning result,
        # "REGION top X closed 0/1" lines from sptl. straddles: count of STRADDLE lines. alpha: stable sets that have a
        # STRADDLE line and whose first sptl pass has its LOWEST top's region open (the (alpha) precondition + containment proxy)
        out = re.sub(r"\x1b\[[0-9;]*m", "", r.stdout + r.stderr)
        if fitness == "straddles": return out.count("STRADDLE tangle")
        score, straddle, regions, instable = 0, False, [], False
        def close_set():
            nonlocal score, straddle, regions, instable
            if instable and regions and straddle:
                # first sptl pass = the REGION lines until the top priority rises again; its last line is the lowest top
                first = [regions[0]]
                for prv, cur in zip(regions, regions[1:]):
                    if cur[0] > prv[0]: break
                    first.append(cur)
                if not first[-1][1]: score += 1
            instable = False; straddle = False; regions = []
        for line in out.splitlines():
            line = re.sub(r"^\[\s*[0-9.]+\]\s*", "", line)
            if line.startswith("STRADDLE tangle"): straddle = True
            if line.startswith("best vertices:"):
                close_set()
                if "(stable)" in line: instable = True
                continue
            if line.startswith("iteration") or line.startswith("current region"): close_set(); continue
            if instable and line.startswith("REGION top"):
                w = line.split(); regions.append((int(w[w.index("pr") + 1]), w[-1] == "1"))
        close_set()
        return score
    if fitness in ("prunemono", "dups"):
        # prunemono: vertices pruned by the first best_vertices call of a search but not by that of the previous search of
        # the same player (a non-monotone pruning, R8 section 12 / proof lane (r1)); dups: "duplicate tangle" lines
        out = re.sub(r"\x1b\[[0-9;]*m", "", r.stdout + r.stderr)
        if fitness == "dups": return out.count("duplicate tangle")
        searches = []; cur = None
        for line in out.splitlines():
            line = re.sub(r"^\[\s*[0-9.]+\]\s*", "", line)
            m2 = re.match(r"iteration (\d+)-(even|odd)", line)
            if m2: cur = {"player": m2.group(2), "pruned": set(), "done": False}; searches.append(cur); continue
            if cur is None or cur["done"]: continue
            if line.startswith("distance "): cur["pruned"].update(re.findall(r"(\S+?)/\d+", line.split(":", 1)[1]))
            if line.startswith("best vertices:"): cur["done"] = True
        return sum(len(b["pruned"] - a["pruned"]) for a, b in zip(searches, searches[1:]) if a["player"] == b["player"])
    if fitness == "evens":          # Even's searches only ("even iterations: k"); with --maxeven K (<= K Even-priority vertices,
        m2 = re.search(r"even iterations: (\d+)", r.stdout + r.stderr)   # i.e. <= K possible tops) more than K+1 searches force repeated learning at a top
        return int(m2.group(1)) if m2 else -1
    if fitness == "iters":          # searches in the whole run (each search after the first learns a new tangle or dominion)
        m2 = re.search(r"solved in (\d+) iterations", r.stdout + r.stderr)
        return int(m2.group(1)) if m2 else -1
    if fitness == "osc":
        # membership oscillation (L-ALG F8 shape): over the sequence of tangles learned at one top P, a vertex that leaves and
        # re-enters (or enters, leaves, re-enters) counts one per change beyond the first; summed over (P, vertex) pairs
        seq = {}
        for line in re.sub(r"\x1b\[[0-9;]*m", "", r.stdout + r.stderr).splitlines():
            m2 = re.search(r"new tangle (\d+) \((\d+)\) \(depth (\d+)\)(.*) with (\d+) escape", line)
            if m2: seq.setdefault(m2.group(1), []).append(frozenset(tok.split("->")[0] for tok in m2.group(4).split()))
        tot = 0
        for P, sets in seq.items():
            for v in set().union(*sets):
                ch = sum(1 for a, b in zip(sets, sets[1:]) if (v in a) != (v in b))
                tot += max(0, ch - 1)
        return tot
    if fitness in ("restarts", "maxrestarts"):
        # chain restarts: a new tangle at top P whose vertex set is not a superset of the previous tangle learned at P
        # (within one search tangles at a top form a growing chain, L-ALG 2026-10-16; a restart happens across searches).
        # restarts: total over tops; maxrestarts: the most at one top. Use --injective so P names the top.
        last = {}; tot = 0; per = {}
        for line in re.sub(r"\x1b\[[0-9;]*m", "", r.stdout + r.stderr).splitlines():
            m2 = re.search(r"new tangle (\d+) \((\d+)\) \(depth (\d+)\)(.*) with (\d+) escape", line)
            if not m2: continue
            P = m2.group(1); vs = frozenset(tok.split("->")[0] for tok in m2.group(4).split())
            if P in last and not vs >= last[P]: tot += 1; per[P] = per.get(P, 0) + 1
            last[P] = vs
        return tot if fitness == "restarts" else max(per.values(), default=0)
    if fitness in ("perhead", "perheadsearch", "persearch"):
        import collections
        c = collections.Counter(); it = 0
        for line in re.sub(r"\x1b\[[0-9;]*m", "", r.stdout + r.stderr).splitlines():
            if "iteration" in line: it += 1
            m2 = re.search(r"new tangle (\d+) \(", line)
            if m2: c[("*" if fitness == "persearch" else m2.group(1), 0 if fitness == "perhead" else it)] += 1
        return max(c.values(), default=0)
    m = re.search(r"found (\d+) dominions and (\d+) tangles", r.stdout + r.stderr)
    return int(m.group(2)) if m else -1


def okeven(g): return not maxeven or sum(1 for q in g[0] if q % 2 == 0) <= maxeven


def random_game():
    pr = rng.sample(range(n), n) if injective else [rng.randrange(maxpr + 1) for _ in range(n)]; ow = [rng.randrange(2) for _ in range(n)]
    if maxeven:
        ev = rng.sample(range(n), maxeven)
        pr = [(q | 1) if v not in ev else (q & ~1) for v, q in enumerate(pr)]
    succ = [{rng.randrange(n)} | {rng.randrange(n) for _ in range(rng.randrange(3))} for _ in range(n)]
    return pr, ow, succ


def mutate(g):
    pr, ow, succ = list(g[0]), list(g[1]), [set(s) for s in g[2]]
    v = rng.randrange(n); k = rng.random()
    if loops and k < 0.3:                      # self-loop on/off (never removed as the only edge)
        if v in succ[v] and len(succ[v]) > 1: succ[v].discard(v)
        else: succ[v].add(v)
        return pr, ow, succ
    if loops and k < 0.45:                     # swap the ids of two vertices of equal priority (tie order of the sort)
        same = [w for w in range(n) if pr[w] == pr[v] and w != v]
        if same:
            w = rng.choice(same)
            def sw(x): return w if x == v else v if x == w else x
            pr[v], pr[w] = pr[w], pr[v]; ow[v], ow[w] = ow[w], ow[v]
            succ = [set(map(sw, succ[sw(x)])) for x in range(n)]
        return pr, ow, succ
    if k < 0.4:
        w = rng.randrange(n)
        if w in succ[v] and len(succ[v]) > 1: succ[v].discard(w)
        else: succ[v].add(w)
    elif k < 0.75:
        if injective: w = rng.randrange(n); pr[v], pr[w] = pr[w], pr[v]
        else: pr[v] = rng.randrange(maxpr + 1)
    else: ow[v] ^= 1
    return pr, ow, succ


if "--eval" in sys.argv:          # print the fitness of one game and exit
    pr, ow, succ = [], [], []
    for line in open(sys.argv[sys.argv.index("--eval") + 1]):
        m = re.match(r"^(\d+)\s+(\d+)\s+([01])\s+([\d,]+)", line.strip())
        if m: pr.append(int(m.group(2))); ow.append(int(m.group(3))); succ.append({int(x) for x in m.group(4).split(",")})
    n = len(pr); print(f"{sys.argv[sys.argv.index('--eval') + 1].split('/')[-1]} {fitness}: {score((pr, ow, succ))}"); os.unlink(tmp); sys.exit(0)
t0 = time.time(); g = random_game()
if "--from" in sys.argv:      # start from a given game (perturbation search); n is taken from the file
    pr, ow, succ = [], [], []
    for line in open(sys.argv[sys.argv.index("--from") + 1]):
        m = re.match(r"^(\d+)\s+(\d+)\s+([01])\s+([\d,]+)", line.strip())
        if m: pr.append(int(m.group(2))); ow.append(int(m.group(3))); succ.append({int(x) for x in m.group(4).split(",")})
    n = len(pr); maxpr = max(maxpr, max(pr)); g = (pr, ow, succ)
    if "--grow" in sys.argv:      # append k fresh vertices (random priority/owner/edges, each with one edge from an old vertex)
        k = int(sys.argv[sys.argv.index("--grow") + 1])
        for j in range(k):
            pr.append(rng.randrange(maxpr + 1)); ow.append(rng.randrange(2)); v = n + j
            succ.append({rng.randrange(v + 1)} | {rng.randrange(v + 1) for _ in range(rng.randrange(3))})
            succ[rng.randrange(v)].add(v)
        n = len(pr); g = (pr, ow, succ)
while evenmin and g[1].count(0) < evenmin * n: g = random_game()
cur = score(g); best = (cur, g)
for i in range(steps):
    h = mutate(g)
    if evenmin and h[1].count(0) < evenmin * n: continue
    if not okeven(h): continue
    sc = score(h)
    if sc >= cur:
        g, cur = h, sc
        if sc > best[0]:
            best = (sc, h); print(f"step {i}: {sc} tangles ({time.time() - t0:.0f}s)", flush=True)
            if "--out" in sys.argv: open(sys.argv[sys.argv.index("--out") + 1], "w").write(dumps(h))
if "--out" in sys.argv: open(sys.argv[sys.argv.index("--out") + 1], "w").write(dumps(best[1]))
os.unlink(tmp)
print(f"n={n} seed={seed}: best {best[0]} tangles after {steps} steps ({time.time() - t0:.0f}s)")
