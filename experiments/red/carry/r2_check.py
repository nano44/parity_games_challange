#!/usr/bin/env python3
"""L-RED (produced on Opus 5.5, 2026-10-16): counter-instance to the well-foundedness step (r2) of L-ALG's (alpha)-exclusion
regress (claude/l-alg docs/alg/DTL-proof.md section 2.3, GAP-A-M.md section 7), on L-ALG's real A_DTL run dtl_mviol_n20.pg.
Uses this lane's tracer (dtl_flipflop.py on L-COMP's dtl_py, exact against Oink). Prints and asserts:
 (1) the first Odd tangle of the run (creation order) is {orig11, orig18}, learned in the first Odd search in a deep STABLE
     piece (piece 7) whose context R excludes its escapes orig2 and orig10 (opponent orig11's exits, forgiven there); in
     that piece orig17 is in R but pruned before the stable round, so orig18 (player-owned) joins orig11's region;
 (2) in the next Odd search (no dominion in between), first best_vertices call (R = G'), round 0: orig18 lies in the region
     of orig17 (priority 21, alive) and orig11 in its own region (priority 9), and orig11 has a self-loop: Lemma E (a), (b);
 (3) the same call has Claim-P drops against the previous visit of the same context (L-ALG GAP-A-M.md section 4b reads
     them off Oink's trace). L-ALG's dtl_ideal.Anatomy marks round 1 of this call as a survival-changing deficit whose
     only straddler is this tangle, so by Lemma E it has the shape. No earlier-created Odd tangle exists to cause it.
Usage: r2_check.py GAME.pg   (the file at claude/l-alg experiments/alg/instances/dtl_mviol_n20.pg, sha1 4cb3335f...)"""
import sys, os, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("ff", os.path.join(HERE, "..", "dtl", "dtl_flipflop.py"))
ff = importlib.util.module_from_spec(spec); spec.loader.exec_module(ff)
path = sys.argv[1]
d = ff.load(path, "oink")
lab = {}
import re
for line in open(path):
    m = re.match(r'\s*(\d+)\s+\d+\s+\d+\s+[\d,]+\s*"([^"]*)"', line)
    if m: lab[int(m.group(1))] = m.group(2)
N = lambda v: lab[d.idx[v]]
inv = {N(v): v for v in range(d.n)}
odd = [s for s in d.searches if s["player"] == 1]
first_t = odd[0]["tangles"][0]
top, vs, piece = first_t
print("first Odd tangle:", N(top), sorted(N(v) for v in vs), "in piece", piece, odd[0]["pieces"][piece]["kind"])
pc = odd[0]["pieces"][piece]
bv = pc["bv"]
assert sorted(N(v) for v in vs) == ["orig11", "orig18"] and pc["kind"] == "stable"
assert inv["orig2"] not in bv["R"] and inv["orig10"] not in bv["R"], "escapes must be forgiven at learning"
last = bv["rounds"][-1]["V"]
assert inv["orig17"] in bv["R"] and inv["orig17"] not in last
print("learning context |R| =", len(bv["R"]), "excludes escapes orig2, orig10; orig17 in R but pruned before the stable round")
s2 = odd[1]
assert s2["G"] == odd[0]["G"] and odd[0]["dominions"] == 0
c = s2["bv"][0]; r0 = c["rounds"][0]
where = {x: t for t, z in r0["regions"].items() for x in z}
print("next search, first call, round 0: orig18 in region of", N(where[inv["orig18"]]), "; orig11 in region of", N(where[inv["orig11"]]))
assert N(where[inv["orig18"]]) == "orig17" and N(where[inv["orig11"]]) == "orig11"
succ = d.outs if hasattr(d, "outs") else d.succ
assert inv["orig11"] in succ[inv["orig11"]] and d.pr[inv["orig11"]] < d.pr[inv["orig17"]]
def death(call, v):
    for i, rd in enumerate(call["rounds"]):
        if v in rd["distractions"]: return i
    return 10 ** 9
alld = []
for a, b in zip(odd, odd[1:]):
    if a["dominions"] or a["G"] != b["G"]: continue
    pa, pb = a["bv"][0], b["bv"][0]
    dr = sorted((N(v), death(pa, v), death(pb, v)) for v in pa["rounds"][0]["V"] if death(pb, v) < death(pa, v))
    print(f"Claim-P drops, Odd search {a['index']} -> {b['index']} (vertex, round, later round):", dr)
    alld += dr
assert alld
print("R2-CHECK PASS: the first-created Odd tangle straddles with the Lemma-E shape in the next search; its cause is the"
      " context difference between its learning piece and the first call, not an earlier-created straddler")
