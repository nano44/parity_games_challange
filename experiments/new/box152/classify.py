#!/usr/bin/env python3
"""L-NEW box 152: classify the CEGAR cores of cegar.py (log + per-iteration witnesses w<it>.json in the workdir).
MERGE: a 2-core {(s, x): b, (s+1, x): 1-b} (C(x) flips at step s+1) where no mover on the two PRE-MERGE segments of x's face chains
(under s) moves at step s+1 (Lemma MERGE-CANCEL forbids exactly this). FLIP2: other 2-cores on one mover. Larger cores: by size.
Usage: classify.py workdir log"""
import sys, os, json, re, ast, collections
wd, log = sys.argv[1], sys.argv[2]
def chain(S, xt, s, x, k):
    out = [(x, k)]; z = xt[(x, k)]
    while z >= 0: out.append((z, S[s][z])); z = xt[(z, S[s][z])]
    return out
cnt = collections.Counter(); it = None
for line in open(log):
    m = re.match(r"IT (\d+) ", line)
    if m: it = int(m.group(1)); continue
    m = re.match(r"\s+core (\d+) (\[.*\]) nogood", line)
    if not m or it is None: continue
    core = dict(ast.literal_eval(m.group(2))); W = json.load(open(os.path.join(wd, f"w{it}.json"))); S = W["states"]
    xt = {(int(a.split(",")[0]), int(a.split(",")[1])): v for a, v in W["xt"].items()}
    ks = sorted(core)
    if len(ks) == 2 and ks[0][1] == ks[1][1] and ks[1][0] == ks[0][0] + 1 and core[ks[0]] != core[ks[1]]:
        (s, x) = ks[0]; A = chain(S, xt, s, x, 0); B = chain(S, xt, s, x, 1)
        ma = [y for (y, _) in A[1:]]; mb = [y for (y, _) in B[1:]]; common = [y for y in ma if y in mb]
        if common:
            m0 = common[0]; pre = ma[:ma.index(m0)] + mb[:mb.index(m0)]
        else: pre = ma + mb
        moved = [y for y in pre if S[s + 1][y] != S[s][y]]
        cnt["MERGE" if not moved else "FLIP2-premerge-moved"] += 1
    else: cnt[f"size{len(ks)}"] += 1
print("CORES", dict(cnt))
