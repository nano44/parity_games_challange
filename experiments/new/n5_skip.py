#!/usr/bin/env python3
"""Box 5 (Lead 23:03Z): characterise the states where N5 SKIPS a switch SSI makes (SSI moves v to u = τ̄(v) ∈ Iσ(v); N5 keeps
σ(v) or moves elsewhere). Per skip (Even side; Odd side on the dual, same tests) records:
  cur   = (v,u) improving against the opponent's CURRENT strategy (single switch, V_{σ,τ}(u) ▷ V_{σ,τ}(σ(v)))
  post  = under N5's NEW σ', u better than N5's choice σ'(v) against τ (V_{σ',τ}(u) ▷ V_{σ',τ}(σ'(v)))
  fb    = the iteration was a fallback
  dom   = after the step, N5's Ξ dominates SSI's Ξ pointwise (N5's own side), and 'worse' = SSI's Ξ strictly above N5's somewhere
Usage: n5_skip.py games seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from n5_lock import step, rgame, play_val
from n5 import pg, Engine, dual
games, seed = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed)
C = {}; wit = {}
def add(k, w):
    C[k] = C.get(k, 0) + 1; wit.setdefault(k, w)
for gi in range(games):
    g = rgame(rng.randint(4, 24), 3, rng); gd = dual(g); E, Ed = Engine(g), Engine(gd)
    for path in ("n5", "ssi"):
        s, t = list(E.initial("best")), list(Ed.initial("best"))
        for _ in range(500):
            vs, sbar = E.evaluate(tuple(s)); Is = E.improving(tuple(s), vs); vt, tbar = Ed.evaluate(tuple(t)); It = Ed.improving(tuple(t), vt)
            if not Is and not It: break
            ns, nt = list(s), list(t)
            for v, w in Is:
                if tbar[v] == w: ns[v] = w
            for v, w in It:
                if sbar[v] == w: nt[v] = w
            r = step(g, E, Ed, s, t)
            for side, (Eng, gg, cur_, opp, ssi_new, n5_new, own) in enumerate(((E, g, s, t, ns, r[0], 0), (Ed, gd, t, s, nt, r[1], 0))):
                for v in range(g.n):
                    if gg.owner[v] != 0 or ssi_new[v] == cur_[v] or n5_new[v] == ssi_new[v]: continue
                    u = ssi_new[v]
                    V0 = play_val(Eng, gg, cur_, opp); V1 = play_val(Eng, gg, n5_new, opp)
                    cur = Eng.key(V0[u]) > Eng.key(V0[cur_[v]]); post = Eng.key(V1[u]) > Eng.key(V1[n5_new[v]])
                    Xn = Eng.evaluate(tuple(n5_new))[0]; Xs = Eng.evaluate(tuple(ssi_new))[0]
                    worse = any(Eng.key(Xs[x]) > Eng.key(Xn[x]) for x in range(g.n)); dom = all(Eng.key(Xn[x]) >= Eng.key(Xs[x]) for x in range(g.n))
                    k = ("E" if side == 0 else "O", "keeps" if n5_new[v] == cur_[v] else "other", "cur" if cur else "notcur", "post" if post else "nopost", "fb" if r[2] else "sel", "dom" if dom else ("worse" if worse else "incomparable"))
                    add(k, (g.prio, g.owner, g.succ, path, list(s), list(t), v))
            s, t = (r[0], r[1]) if path == "n5" else (ns, nt)
for k in sorted(C): print(C[k], k)
print("TOTAL", sum(C.values()))
import json; json.dump({str(k): v for k, v in wit.items()}, open(os.path.join(HERE, "n5", "box5", "skip_witnesses.json"), "w"))
