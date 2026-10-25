#!/usr/bin/env python3
"""REFEREE succ. 9: hill climb for P-N5-NEB (own code; neb_probe.run on rl_engine). Mutations keep C^1O: change an Even vertex's
successor set (add / drop / redirect an edge), redirect a forced Odd vertex, add / drop an edge at o, swap two priorities. Score =
RISE_events + 3 LOWR_c_events + CASEB_gates + 2 breaks + 4 (B!= breaks); a mutant is kept if its score is >= the current one.
Any *_FAIL is written to outdir as fail_<seed>_<i>.pg. Usage: neb_climb.py seed.pg rngseed minutes outdir"""
import sys, os, random, time
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P, neb_probe as NP


def score(g):
    c = Counter(); NP.EX.clear()
    try: NP.run(g, c, "climb")
    except (RuntimeError, AssertionError): return None, c
    s = c["RISE_events"] + 3 * c["LOWR_c_events"] + c["CASEB_gates"] + 2 * c["breaks"] + 4 * (c["breaks_A!="] + c["breaks_B!="])
    return s, c


def mutate(g, rng):
    n = g.n; succ = [list(x) for x in g.succ]; prio = list(g.prio); owner = list(g.owner)
    o = P.assert_c1o(g); r = rng.random()
    if r < 0.45:
        evens = [v for v in range(n) if owner[v] == 0]; v = rng.choice(evens); w = rng.randrange(n)
        if w in succ[v] and len(succ[v]) > 1 and rng.random() < 0.5: succ[v].remove(w)
        elif rng.random() < 0.5: succ[v].append(w)
        else: succ[v][rng.randrange(len(succ[v]))] = w
    elif r < 0.6:
        odds = [v for v in range(n) if owner[v] == 1 and v != o]
        if odds: succ[rng.choice(odds)] = [rng.randrange(n)]
    elif r < 0.75:
        w = rng.randrange(n)
        if w in succ[o] and len(succ[o]) > 2: succ[o].remove(w)
        else: succ[o].append(w)
    else:
        a, b = rng.sample(range(n), 2); prio[a], prio[b] = prio[b], prio[a]
    h = RE.Game(prio, owner, succ)
    P.assert_c1o(h)
    return h


def write(g, path):
    with open(path, "w") as f:
        f.write("parity %d;\n" % (g.n - 1))
        for v in range(g.n): f.write("%d %d %d %s;\n" % (v, g.prio[v], g.owner[v], ",".join(map(str, g.succ[v]))))


def main(seed, rs, minutes, out):
    os.makedirs(out, exist_ok=True); rng = random.Random(int(rs)); g = RE.parse(seed)
    cur, c = score(g); best = cur; tot = Counter(); i = 0; end = time.time() + 60 * float(minutes)
    while time.time() < end:
        i += 1
        try: h = mutate(g, rng)
        except AssertionError: continue
        s, c = score(h)
        if s is None: continue
        for k, v in c.items():
            if k.endswith("_FAIL") or k in ("RISE_events", "LOWR_c_events", "CASEB_gates", "breaks", "breaks_A!=", "breaks_B!=",
                                            "breaks_B=", "breaks_A=", "NOENT_states", "BAND_rise_viol", "BAND_gate_viol_later",
                                            "BAND_gate_viol_at_base", "HIGH_chk", "CHAIN_chk"): tot[k] += v
        if any(k.endswith("_FAIL") and v for k, v in c.items()):
            write(h, os.path.join(out, "fail_%s_%d.pg" % (rs, i))); tot["fail_files"] += 1
        if s >= cur:
            g, cur = h, s
            if s > best: best = s; write(g, os.path.join(out, "best_%s.pg" % rs))
    tot["iters"] = i; tot["best_score"] = best
    for k in sorted(tot): print("%-26s %d" % (k, tot[k]))
    print("FAILS", sum(v for k, v in tot.items() if k.endswith("_FAIL")))


if __name__ == "__main__":
    main(*sys.argv[1:5])
