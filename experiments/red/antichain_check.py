#!/usr/bin/env python3
"""Downstream-first diagnostic for S7 (L-RED, R3 3c). Along the run of RULE on a game (vj.py: msf, lsf, most-improved;
or an explicit Bland/least-entered/round-robin order), count the steps at which the chosen vertex v is UPSTREAM of
another improving vertex u (v's (sigma,tau)-play visits u). By Lemma D, S7 can never make such a step in a generic game,
whatever pads are added; so a family whose run has such steps cannot be emulated by S7 with pads, and one with none could.
Usage: antichain_check.py game.pg RULE [--start best|first|file]   (RULE in msf, lsf, bland, zadeh, cunningham)"""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); import vj
path, rule = sys.argv[1], sys.argv[2]; start = "best"
if "--start" in sys.argv: start = sys.argv[sys.argv.index("--start") + 1]
if start == "file":
    start = "spec:" + [l for l in open(path) if l.startswith("% start")][0].split("start")[1].strip()
e = vj.VJ(*vj.read_pg(path)); sigma = e.initial(start); mem = {}; steps = 0; bad = 0; badsteps = []


def play_visits(sigma, tau, v, u):
    x = v; seen = set()
    while x not in seen:
        if x == u: return True
        seen.add(x); x = sigma[x] if e.owner[x] == 0 else tau[x]
    return False


while True:
    val, tau = e.evaluate(sigma); imp = e.improving(sigma, val)
    if not imp: break
    if rule in ("msf", "lsf"): v, w, _ = e.pick(sigma, val, imp, most=(rule == "msf"))
    elif rule == "most-improved": v, w, _, _ = e.pick_most_improved(sigma, val, imp)
    elif rule == "bland": v, w = min(imp)
    elif rule == "zadeh":
        cnt = mem.setdefault("c", {}); v, w = min(imp, key=lambda x: (cnt.get(x, 0), x)); cnt[(v, w)] = cnt.get((v, w), 0) + 1
    elif rule == "cunningham":
        last = mem.get("last", (-1, -1)); after = [x for x in imp if x > last]; v, w = min(after) if after else min(imp); mem["last"] = (v, w)
    others = {u for u, _ in imp if u != v}
    up = [u for u in others if play_visits(sigma, tau, v, u)]
    steps += 1
    if up: bad += 1; badsteps.append(steps)
    s = list(sigma); s[v] = w; sigma = tuple(s)
print(f"{os.path.basename(path)} {rule}: {steps} switches, chosen vertex upstream of another improving vertex at {bad} steps"
      + (f" (first: {badsteps[:8]})" if badsteps else " -> S7-with-pads could emulate this run"))
