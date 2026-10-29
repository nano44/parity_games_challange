#!/usr/bin/env python3
"""T44: three single-frame variants of N5 (docs/new/N5-ssi-global.md SPEC S1-S5), run side by side with N5 and SSI.
Each variant computes both players' steps from the SAME (sigma, tau) and applies them together (as S4). Only S4a/S4b change:
  n5    SPEC (arena from Xi = vs the opponent's optimal counterstrategy; choice = optimum vs the opponent's CURRENT strategy), via n5.run.
  ssi   n5.run mode ssi (= DLM arXiv 2309.02223 Alg. 2 with switch-all inside Prof ∩ opponent-best-reply).
  sfxi  "choose by Xi": arena = {sigma(v)} ∪ I_sigma (Xi frame, as S4a); choice = Even's OPTIMAL strategy of the arena game with Odd
        FREE (Schewe's optimal improvement step, frame Xi); computed by switch-all SI inside the arena game, started at sigma.
        Odd dually on G^d. Independent of the opponent's current strategy.
  sfw   "arena by W": arena = {sigma(v)} ∪ W-improving edges (one-player game G_tau, Odd fixed to tau); choice = S4a's selection
        (Even's optimum in the arena vs tau, same Engine call and tie-breaks as n5.py). Odd dually vs sigma. Stop when both
        W-improving sets are empty (then (sigma, tau) is a mutual best reply), or when the selection changes nothing (this happens
        only through length-degenerate W-edges at a cycle node; the regions are then checked against N5's). Cycle detection.
  sfint (not single-frame; the termination-guarded repair of sfw) arena = {sigma(v)} ∪ (I_sigma ∩ W-improving); choice as S4a;
        S4c fallback as SPEC when nothing moves. Terminates (every switch is Xi-improving).
Output per run: iterations, outcome (stop / CYCLE at step t with period p / cap), and whether the final Even region equals N5's.
Read-only use of experiments/new/n5.py, experiments/si/si.py, experiments/harness/pg.py. Run from the repo root:
  python3 -I docs/lit/T44-sf-variants.py game.pg [startfile]        (startfile: lines 'SIGMA0 v:w ...', 'TAU0 v:w ...')"""
import sys, os
ROOT = os.getcwd()
for p in ("experiments/new", "experiments/si", "experiments/harness"): sys.path.insert(0, os.path.join(ROOT, p))
import pg, n5
from si import Engine
dual = n5.dual

def restricted(g, keep):
    """keep[v] = list of successors kept at v."""
    return pg.Game(list(g.prio), list(g.owner), [sorted(keep[v]) for v in range(g.n)])

def si_opt(H, s):
    """Even's optimal strategy of game H by switch-all SI from s (Odd free). Returns tuple."""
    E = Engine(H); s = tuple(s)
    while True:
        val, _ = E.evaluate(s); imp = E.improving(s, val)
        if not imp: return s
        s = E.rule_switch_all(s, val, imp, None)

def sel_vs(g, arena_even, tau):
    """S4a's selection: Even's optimum in arena (Even edges arena_even[v], Odd fixed to tau) vs tau; n5.py's Engine call."""
    n = g.n
    succ = [sorted(arena_even[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)]
    _, best = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ))).evaluate(tuple(tau[v] if g.owner[v] == 1 else -1 for v in range(n)))
    return [best[v] if g.owner[v] == 0 else -1 for v in range(n)]

def sel_vs_odd(g, arena_odd, sigma):
    n = g.n
    succ = [sorted(arena_odd[v]) if g.owner[v] == 1 else [sigma[v]] for v in range(n)]
    _, best = Engine(pg.Game(list(g.prio), list(g.owner), succ)).evaluate(tuple(sigma[v] if g.owner[v] == 0 else -1 for v in range(n)))
    return [best[v] if g.owner[v] == 1 else -1 for v in range(n)]

def run(g, mode, start=None, cap=5000):
    n = g.n; E, Ed = Engine(g), Engine(dual(g))
    sigma, tau = list(E.initial("best")), list(Ed.initial("best"))
    if start:
        for v, w in start[0].items(): sigma[v] = w
        for v, w in start[1].items(): tau[v] = w
    seen = {(tuple(sigma), tuple(tau)): 0}; it = 0; even_sw = odd_sw = 0; degen = False; fbk = 0
    while it < cap:
        if mode == "sfxi":
            vs, _ = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
            vt, _ = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
            if not Is and not It: break
            ns, nt = list(sigma), list(tau)
            if Is:
                keep = [([sigma[v]] + [w for x, w in Is if x == v]) if g.owner[v] == 0 else g.succ[v] for v in range(n)]
                ns = list(si_opt(restricted(g, keep), sigma))
            if It:
                gd = dual(g)
                keep = [([tau[v]] + [w for x, w in It if x == v]) if g.owner[v] == 1 else g.succ[v] for v in range(n)]
                nt = list(si_opt(restricted(gd, keep), tau))
        elif mode == "sfint":
            vs, _ = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
            vt, _ = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
            if not Is and not It: break
            gt = restricted(g, [g.succ[v] if g.owner[v] == 0 else [tau[v]] for v in range(n)])
            Ew = Engine(gt); vw, _ = Ew.evaluate(tuple(sigma)); Isw = set(Ew.improving(tuple(sigma), vw)) & set(Is)
            gs = restricted(g, [g.succ[v] if g.owner[v] == 1 else [sigma[v]] for v in range(n)])
            Ewd = Engine(dual(gs)); vwd, _ = Ewd.evaluate(tuple(tau)); Itw = set(Ewd.improving(tuple(tau), vwd)) & set(It)
            ns, nt = list(sigma), list(tau)
            if Isw:
                ar = {v: {sigma[v]} | {w for x, w in Isw if x == v} for v in range(n) if g.owner[v] == 0}
                b = sel_vs(g, ar, tau); ns = [b[v] if g.owner[v] == 0 else -1 for v in range(n)]
            if Itw:
                ar = {v: {tau[v]} | {w for x, w in Itw if x == v} for v in range(n) if g.owner[v] == 1}
                b = sel_vs_odd(g, ar, sigma); nt = [b[v] if g.owner[v] == 1 else -1 for v in range(n)]
            if (ns, nt) == (sigma, tau):   # S4c fallback, as SPEC
                fbk += 1
                if Is:
                    for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
                else:
                    for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
        elif mode == "sfw":
            gt = restricted(g, [g.succ[v] if g.owner[v] == 0 else [tau[v]] for v in range(n)])
            Ew = Engine(gt); vw, _ = Ew.evaluate(tuple(sigma)); Isw = Ew.improving(tuple(sigma), vw)
            gs = restricted(g, [g.succ[v] if g.owner[v] == 1 else [sigma[v]] for v in range(n)])
            Ewd = Engine(dual(gs)); vwd, _ = Ewd.evaluate(tuple(tau)); Itw = Ewd.improving(tuple(tau), vwd)
            if not Isw and not Itw: break
            ns, nt = list(sigma), list(tau)
            if Isw:
                ar = {v: {sigma[v]} | {w for x, w in Isw if x == v} for v in range(n) if g.owner[v] == 0}
                b = sel_vs(g, ar, tau); ns = [b[v] if g.owner[v] == 0 else -1 for v in range(n)]
            if Itw:
                ar = {v: {tau[v]} | {w for x, w in Itw if x == v} for v in range(n) if g.owner[v] == 1}
                b = sel_vs_odd(g, ar, sigma); nt = [b[v] if g.owner[v] == 1 else -1 for v in range(n)]
            if (ns, nt) == (sigma, tau): degen = True; break   # only length-degenerate "improving" edges (see T44 §3): fixpoint
        else:
            raise ValueError(mode)
        it += 1
        even_sw += sum(1 for v in range(n) if ns[v] != sigma[v]); odd_sw += sum(1 for v in range(n) if nt[v] != tau[v])
        sigma, tau = ns, nt
        key = (tuple(sigma), tuple(tau))
        if key in seen:
            return it, f"CYCLE(enter {seen[key]}, period {it - seen[key]})", None, even_sw, odd_sw
        seen[key] = it
    else:
        return it, "CAP", None, even_sw, odd_sw
    win, _ = E.regions(tuple(sigma))
    return it, "stop" + ("(fixpoint, degenerate W-edges left)" if degen else "") + (f"(fb {fbk})" if fbk else ""), win, even_sw, odd_sw

def readstart(path):
    L = [l for l in open(path) if l.split() and l.split()[0] in ("SIGMA0", "TAU0")]
    return tuple(dict(map(int, t.split(":")) for t in L[j].split()[1:]) for j in (0, 1))

if __name__ == "__main__":
    g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%")))
    st = readstart(sys.argv[2]) if len(sys.argv) > 2 else None
    it5, fb5, win5, _, _ = n5.run(g, "n5", st); its, _, wins, _, _ = n5.run(g, "ssi", st)
    out = [f"n5 {it5} (fb {fb5})", f"ssi {its}" + ("" if wins == win5 else " REGION-MISMATCH")]
    for m in ("sfxi", "sfw", "sfint"):
        it, oc, win, es, os_ = run(g, m, st)
        out.append(f"{m} {it} {oc} sw {es}/{os_}" + ("" if win is None or win == win5 else " REGION-MISMATCH"))
    print(os.path.basename(sys.argv[1]), "n", g.n, "|", " | ".join(out))
