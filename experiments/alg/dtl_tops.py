#!/usr/bin/env python3
"""L-ALG (2026-10-16, GAP-A data): tangles with their TRUE tops, from a Debug-build trace (`-t -t`: each `new tangle` line is
preceded by the `region P top ...` line of the closed region it was extracted from; the first vertex of a region line is its top).
Reports per search the (top, set) pairs, the per-top counts (sanity: <= searches, by sptl's W), and the coverage potential
P1: does every search add a (top, vertex) pair never covered before? Usage: dtl_tops.py GAME.pg TRACE"""
import sys, re, collections
game, trace = sys.argv[1], sys.argv[2]
def vid(tok): return int(tok.split("->")[0][1:])
search = 0; last_region_top = None; tangles = []  # (search, top, frozenset)
for line in open(trace):
    line = line.rstrip()
    if re.match(r"iteration \d+-(even|odd)", line): search += 1; continue
    m = re.match(r"region (\d+)(.*)", line)
    if m:
        vs = [vid(t) for t in m.group(2).split()]
        last_region_top = vs[0] if vs else None; continue
    m = re.search(r"new tangle (\d+) \((\d+)\) \(depth (\d+)\)(.*) with (\d+) escape", line)
    if m:
        S = frozenset(vid(t) for t in m.group(4).split())
        tangles.append((search, last_region_top, S))
per_top = collections.Counter(t[1] for t in tangles)
per_top_search = collections.Counter((t[0], t[1]) for t in tangles)
cov = set(); per_search_new = collections.Counter(); per_search_total = collections.Counter()
for s, top, S in tangles:
    per_search_total[s] += 1
    new = [(top, v) for v in S if (top, v) not in cov]
    if new: per_search_new[s] += 1
    cov.update((top, v) for v in S)
viol = [s for s in per_search_total if per_search_new[s] == 0]
# oscillation depth: for each (top, vertex), the number of membership changes across that top's tangles in creation order
seq = collections.defaultdict(list)
for s, top, S in tangles: seq[top].append(S)
osc = collections.Counter(); worst = (0, None, None)
for top, L in seq.items():
    verts = set().union(*L)
    for v in verts:
        bits = [v in S for S in L]; ch = sum(1 for a, b in zip(bits, bits[1:]) if a != b)
        osc[ch] += 1
        if ch > worst[0]: worst = (ch, top, v)
print(f"  oscillation depth histogram (membership changes per (top, vertex)): {dict(sorted(osc.items()))}; worst {worst}")
print(f"{game}: searches {search}, tangles {len(tangles)}, tops {len(per_top)}, max per top {max(per_top.values()) if per_top else 0}, max per (top, search) {max(per_top_search.values()) if per_top_search else 0}; P1 (every learning search adds a new (top, vertex) pair): {'OK' if not viol else 'VIOLATED in searches ' + str(viol)}")
