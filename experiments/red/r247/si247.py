#!/usr/bin/env python3
"""L-RED 71 R247: classical ONE-SIDED Voege-Jurdzinski strategy improvement with a PLUGGABLE selection rule (own engine).
State: a positional Even strategy sigma. One iteration: Xi_sigma := the valuation of sigma against Odd's optimal counterstrategy sbar
(SPEC S1's procedure: n5s237.vjproc, experiments/red/r237, written from the SPEC text); I(v) := {w in succ(v) : Xi_sigma(w) strictly better
for Even than Xi_sigma(sigma(v))} for Even v; if no I(v) is nonempty, STOP (sigma is optimal; winners = parity of the cycle node);
otherwise a RULE returns a nonempty set of switches {v: w} with w in I(v), which are applied together. The number of ITERATIONS is the number
of applied switch sets (the final evaluation that finds no improving edge is not counted).
Rules (RULES dict; each gets the engine, sigma, val, sbar, I and returns {v: w}):
  howard   every improvable v switches to its Xi-best successor (ties: larger index): the locally optimising rule «switch-best» / Howard,
           Friedmann's lower-bound rule (LMCS 7 (3:19), arXiv 1106.0778, section 6: 9 * 2^n - 10 steps on G_n from iota).
  first    every improvable v switches to its improving successor of least index (a «switch-all, first edge» rule; control only).
  rf       ROOT-FIRST (candidate of L-SI 57 as relayed by the Lead; see rf247.py for the rule text and its readings).
Start: «s3» (SPEC S3 / FIX 1 for Even: the successor maximising (r(w), w if r(w) even else -w)), a dict, or the '% start v:w ...' line of
a .pg file written by gens_red.py (Friedmann's iota).
Usage: si247.py RULE GAME.pg [s3|file]     prints: iterations, switches (total applied), even_wins"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE, os.path.join(HERE, "..", "r237")]
import n5s237

class SI:
    def __init__(s, prio, owner, succ):
        s.n = n = len(prio); s.prio = list(prio); s.owner = list(owner); s.succ = [sorted(set(x)) for x in succ]
        order = sorted(range(n), key=lambda v: (prio[v], v)); s.rk = [0] * n
        for r, v in enumerate(order): s.rk[v] = r
        s.ev = [p % 2 == 0 for p in prio]; s.isE = [o == 0 for o in owner]; s.isO = [o == 1 for o in owner]
        s.O = n5s237.Ord(s.rk, s.ev); s.evals = 0
    def s3(s):
        r = lambda p: p if p % 2 == 0 else -p
        return {v: max(s.succ[v], key=lambda w: (r(s.prio[w]), w if s.prio[w] % 2 == 0 else -w)) for v in range(s.n) if s.isE[v]}
    def evaluate(s, sigma):
        """(val, sbar): Xi_sigma and Odd's optimal counterstrategy (SPEC S1)"""
        s.evals += 1
        return n5s237.vjproc(s.n, s.rk, s.ev, [[sigma[v]] if s.isE[v] else s.succ[v] for v in range(s.n)], s.isO)
    def improving(s, sigma, val):
        I = {}
        for v in sigma:
            ws = [w for w in s.succ[v] if w != sigma[v] and s.O.better(val[w], val[sigma[v]])]
            if ws: I[v] = ws
        return I
    def best(s, val, ws):
        b = ws[0]
        for w in ws[1:]:
            if s.O.better(val[w], val[b]) or (not s.O.better(val[b], val[w]) and w > b): b = w
        return b
    def run(s, rule, start="s3", cap=10 ** 7, trace=None, hook=None):
        sigma = s.s3() if start == "s3" else dict(start); it = sw = 0
        rulef = RULES[rule] if isinstance(rule, str) else rule
        while True:
            val, sbar = s.evaluate(sigma); I = s.improving(sigma, val)
            if trace is not None: trace.append(dict(sigma))
            if not I: break
            if it >= cap: return dict(its=it, switches=sw, capped=True, sigma=sigma, val=val, sbar=sbar)
            ch = rulef(s, sigma, val, sbar, I)
            assert ch and all(v in I and w in I[v] for v, w in ch.items()), ("rule returned a non-improving or empty switch set", ch)
            if hook is not None: hook(it, sigma, val, sbar, I, ch)
            for v, w in ch.items(): sigma[v] = w
            it += 1; sw += len(ch)
        win = [0 if s.ev[val[v][0]] else 1 for v in range(s.n)]
        return dict(its=it, switches=sw, capped=False, sigma=sigma, val=val, sbar=sbar, win=win)

def rule_howard(e, sigma, val, sbar, I): return {v: e.best(val, ws) for v, ws in I.items()}
def rule_first(e, sigma, val, sbar, I): return {v: ws[0] for v, ws in I.items()}
RULES = {"howard": rule_howard, "first": rule_first}

def read_start(fn):
    for line in open(fn):
        if line.startswith("% start"):
            return {int(a): int(b) for a, b in (x.split(":") for x in line.split()[2:])}
    return None

def parse(fn):
    prio, owner, succ = {}, {}, {}
    for line in open(fn):
        line = line.strip().rstrip(";")
        if not line or line.startswith("parity") or line.startswith("%") or line.startswith("start"): continue
        parts = line.split('"')[0].split(); v = int(parts[0]); prio[v], owner[v] = int(parts[1]), int(parts[2])
        succ[v] = sorted({int(x) for x in parts[3].split(",")})
    n = len(prio); assert sorted(prio) == list(range(n))
    return [prio[v] for v in range(n)], [owner[v] for v in range(n)], [succ[v] for v in range(n)]

if __name__ == "__main__":
    try:
        import rf247                                                    # the rule «rf» (registered there on the module si247;
        RULES.update(rf247.si247.RULES)                                 #  copied here because this file runs as __main__)
    except ImportError: pass
    rule, fn = sys.argv[1], sys.argv[2]; st = sys.argv[3] if len(sys.argv) > 3 else "s3"
    e = SI(*parse(fn)); start = "s3"
    if st == "file":
        start = e.s3(); given = read_start(fn); assert given is not None, "no '% start' line"
        start.update(given)
    r = e.run(rule, start)
    print("SI247", os.path.basename(fn), "n", e.n, "rule", rule, "start", st, "iterations", r["its"], "switches", r["switches"], "even_wins", sum(1 for w in r["win"] if w == 0), flush=True)
