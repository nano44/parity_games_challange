#!/usr/bin/env python3
"""Longest Zadeh run under ANY fixed total order of the edges (L-RED, R7). Exhaustive DFS over the tie decisions: at a tie
(>= 2 improving edges with the minimal occurrence record) every candidate that no earlier decision already placed after a
competitor is tried, and the decision 'chosen before every competitor' is added to the (transitively closed) order. Every
run of Zadeh with a fixed total order (index tie-break on any numbering included) is one leaf of this tree, so the maximum
over leaves bounds every fixed-order Zadeh run on the game from above. Initial strategy as zadeh_lb.py (exp-game start) or
'best'. Usage: zadeh_anyorder.py game.pg [--start exp|best] [--budget NODES]"""
import sys, os, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); import vj
sys.setrecursionlimit(100000)
path = sys.argv[1]; start = "exp"; budget = 2_000_000
if "--start" in sys.argv: start = sys.argv[sys.argv.index("--start") + 1]
if "--budget" in sys.argv: budget = int(sys.argv[sys.argv.index("--budget") + 1])
prio, owner, succ = vj.read_pg(path)
import re
lab = {}
for line in open(path):
    mm = re.match(r'^(\d+)\s+\d+\s+[01]\s+[\d,]+\s*(?:"([^"]*)")?', line.strip())
    if mm: lab[int(mm.group(1))] = mm.group(2) or mm.group(1)
e = vj.VJ(prio, owner, succ); n_v = len(prio)
edges = [(v, w) for v in range(n_v) if owner[v] == 0 and len(succ[v]) >= 2 for w in succ[v]]
eid = {x: i for i, x in enumerate(edges)}; E = len(edges)
if start == "exp":
    byname = {lab[v]: v for v in range(n_v)}; find = byname.get
    parse = lambda v: (lab[v][0], int(lab[v][1:])) if len(lab[v]) > 1 and lab[v][1:].isdigit() else (lab[v][0], 0)
    n = 0
    while find(f"E{n}") is not None: n += 1
    sigma = list(e.initial("best"))
    for v in range(n_v):
        if owner[v] == 0 and len(succ[v]) >= 2:
            c, j = parse(v)
            t = {"a": f"o{j}", "b": f"p{j}", "v": f"r{j}", "w": f"q{j}", "o": "m1", "p": "m1", "q": "m1", "r": "m1", "d": f"E{j}",
                 "g": f"c{j}", "s": "m0", "m": (f"m{j + 1}" if j < n - 1 else "Y")}.get(c)
            if t and find(t) is not None and find(t) in succ[v]: sigma[v] = find(t)
    sigma = tuple(sigma)
else:
    sigma = e.initial(start)
best = [0, None]; nodes = [0]; t0 = time.time(); leaves = [0]
prefer = []        # --prefer FILE: one edge "x->y" per line (e.g. the lower-bound run); the search follows it while allowed
if "--prefer" in sys.argv:
    byname = {lab[v]: v for v in range(n_v)}
    for line in open(sys.argv[sys.argv.index("--prefer") + 1]):
        a, b = line.split()[0].split("->"); prefer.append(eid[(byname[a], byname[b])])


onlb = [True]


def dfs(sigma, occ, after, depth, hist):
    """after[i] = bitmask of edges that must come AFTER edge i (closed under transitivity)"""
    nodes[0] += 1
    if nodes[0] > budget: raise TimeoutError
    val, _ = e.evaluate(sigma); imp = e.improving(sigma, val)
    if not imp:
        leaves[0] += 1
        if depth > best[0]: best[0] = depth; best[1] = list(hist)
        return
    m = min(occ[eid[x]] for x in imp); cands = [eid[x] for x in imp if occ[eid[x]] == m]
    if len(cands) == 1: opts = cands
    else:
        opts = [c for c in cands if not any(after[x] >> c & 1 for x in cands if x != c)]
    if onlb[0] and depth < len(prefer) and prefer[depth] in opts: opts = [prefer[depth]] + [c for c in opts if c != prefer[depth]]
    for c in opts:
        v, w = edges[c]
        was = onlb[0]; onlb[0] = was and depth < len(prefer) and c == prefer[depth]
        if len(cands) > 1:
            new_after = list(after)
            # c before every other candidate x: for every y with c in after[y] (y before c), after[y] |= after[x] | bit x
            addmask = 0
            for x in cands:
                if x != c: addmask |= (1 << x) | after[x]
            new_after[c] |= addmask
            for y in range(E):
                if y != c and (after[y] >> c) & 1: new_after[y] |= addmask
        else: new_after = after
        occ2 = list(occ); occ2[c] += 1
        s = list(sigma); s[v] = w
        hist.append((v, w)); dfs(tuple(s), occ2, new_after, depth + 1, hist); hist.pop(); onlb[0] = was


try:
    dfs(sigma, [0] * E, [0] * E, 0, []); done = True
except TimeoutError: done = False
print(f"{os.path.basename(path)} start={start}: longest fixed-order Zadeh run = {best[0]} switches ({'exhaustive' if done else 'budget hit'}; "
      f"{nodes[0]} nodes, {leaves[0]} leaves, {time.time() - t0:.0f}s)")
if best[1] is not None and "--trace" in sys.argv:
    print(" ".join(f"{lab[v]}->{lab[w]}" for v, w in best[1]))
