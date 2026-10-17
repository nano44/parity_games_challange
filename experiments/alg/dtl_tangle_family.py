#!/usr/bin/env python3
"""L-ALG (2026-10-16, GAP-A data): structure of the family of stored tangle vertex sets.
Runs the pinned A_DTL with `-t -t` (release build prints every new tangle with its vertices, dtl.cpp 426-432, not NDEBUG
guarded), relabels vertices by their input id first so the trace is unambiguous, and reports:
  tangles, searches, laminarity (number of crossing pairs: sets that intersect without nesting),
  per-top counts (top = max-priority vertex, ties by max id), and for multi-tangle tops the inclusion structure.
Usage: dtl_tangle_family.py OINK GAME.pg [--idtl] [--sets]"""
import sys, re, subprocess, collections, itertools, os, tempfile
oink, game = sys.argv[1], sys.argv[2]
solver = "--idtl" if "--idtl" in sys.argv else "--dtl"
pr, own, succ, lines = {}, {}, {}, []
for line in open(game):
    if line.startswith("parity"): lines.append(line.strip()); continue
    f = line.strip().rstrip(";").split()
    if len(f) >= 4 and f[0].isdigit():
        v = int(f[0]); pr[v] = int(f[1]); own[v] = int(f[2]); succ[v] = [int(x) for x in f[3].split(",")]
        lines.append(f"{v} {pr[v]} {own[v]} {f[3]} \"v{v}\";")
tmp = tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False, dir=os.path.dirname(os.path.abspath(game)) if False else None)
tmp.write("\n".join(lines) + "\n"); tmp.close()
r = subprocess.run([oink, solver, "--no-single", "--no-wcwc", "--no-loops", "-t", "-t", tmp.name], capture_output=True, text=True, timeout=3600)
os.unlink(tmp.name)
out = re.sub(r"\x1b\[[0-9;]*m", "", r.stdout + r.stderr)
tangles = []   # (search, depth, top_pr, frozenset, strategy dict)
search = 0; doms = 0
for line in out.splitlines():
    if re.search(r"iteration \d+-(even|odd)", line): search += 1
    m = re.search(r"new tangle (\d+) \((\d+)\) \(depth (\d+)\)(.*) with (\d+) escape", line)
    if m:
        toks = m.group(4).split(); st = {}
        for tok in toks:
            a, _, b = tok.partition("->"); st[int(a[1:])] = int(b[1:]) if b else -1
        tangles.append((search, int(m.group(3)), int(m.group(1)), frozenset(st), st, int(m.group(5))))
    if line.startswith("[") and "dominion" in line and "depth" in line: doms += 1
sets = [t[3] for t in tangles]
cross = 0; nested = 0; disjoint = 0
for a, b in itertools.combinations(sets, 2):
    if a <= b or b <= a: nested += 1
    elif a & b: cross += 1
    else: disjoint += 1
def top(s): return max(s, key=lambda v: (pr[v], v))
per_top = collections.defaultdict(list)
for t in tangles: per_top[top(t[3])].append(t)
hist = collections.Counter(len(v) for v in per_top.values())
# (C-new): every new tangle at top tau contains a vertex that no earlier tangle at tau contains (=> <= n tangles per top)
cnew_viol = 0; shrink = 0; restart_viol = 0; chain_viol = 0
for tp, ts in per_top.items():
    cov = set(); last_search = None; prev = None
    for t in ts:
        if t[3] <= cov: cnew_viol += 1
        if any(t[3] < t2[3] for t2 in ts if t2[0] < t[0]): shrink += 1
        if t[0] != last_search:            # first tangle at this top in its search ("restart")
            if t[3] <= cov: restart_viol += 1
        elif not (prev < t[3]): chain_viol += 1   # within one search the tangles at a top should form a strictly growing chain
        cov |= t[3]; last_search = t[0]; prev = t[3]
sizes = sorted(len(s) for s in sets)
print(f"{os.path.basename(game)}: n {len(pr)} tangles {len(tangles)} dominions {doms} searches {search} | pairs nested {nested} crossing {cross} disjoint {disjoint} | tops {len(per_top)} max/top {max(hist) if hist else 0} hist {dict(sorted(hist.items()))} | C-new violations {cnew_viol} (restart {restart_viol}, in-search chain breaks {chain_viol}) strict-shrinks {shrink} | sizes min {sizes[0] if sizes else 0} med {sizes[len(sizes)//2] if sizes else 0} max {sizes[-1] if sizes else 0}")
if "--sets" in sys.argv:
    for tp, ts in sorted(per_top.items(), key=lambda kv: -len(kv[1])):
        if len(ts) < 2: continue
        print(f" top v{tp} pr {pr[tp]}: {len(ts)} tangles")
        for (s, d, p, S, st, esc) in ts:
            rel = []
            for (s2, d2, p2, S2, st2, e2) in ts:
                if S2 is S: continue
                rel.append("<" if S < S2 else ">" if S > S2 else "x" if S & S2 else "o")
            print(f"   search {s} depth {d} size {len(S)} esc {esc} minpr {min(pr[v] for v in S)} rel {''.join(rel)} set {sorted(S)}")
