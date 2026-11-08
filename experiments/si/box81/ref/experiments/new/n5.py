#!/usr/bin/env python3
"""N5 SSI-GLOBAL (docs/new/N5-ssi-global.md) and, for validation, original SSI (2309.02223 Algorithm 2, SWITCH-ALL).
Engine: L-SI's experiments/si/si.py (imported read-only): Vöge-Jurdziński valuations, Engine.evaluate(σ) = (Ξσ, σ̄) with σ̄ Odd's
optimal counterstrategy. Odd's side runs on the DUAL game (owners swapped, priorities + 1), where Odd's strategy τ is the
"Even" strategy: Ed.evaluate(τ) = (Ξτ, τ̄), τ̄ = Even's optimal counterstrategy to τ.
  ssi: I = (Iσ ∩ {(v, τ̄(v))}) ∪ (Iτ ∩ {(v, σ̄(v))}); apply all (switch-all on I).
  n5 : Even: σ' = Even's optimum in the arena where Odd is fixed to τ and Even v may use only {σ(v)} ∪ {w : (v,w) ∈ Iσ}
       (one-player problem, solved by Engine.evaluate on the dual of that arena = VJ00's counterstrategy computation);
       Odd: τ' = Odd's optimum where Even is fixed to σ and Odd v may use only {τ(v)} ∪ {w : (v,w) ∈ Iτ} (Engine.evaluate);
       apply both. If neither changes although Iσ ∪ Iτ ≠ ∅: one classical switch-all step for Even on Iσ (Odd on Iτ if Iσ = ∅),
       counted as 'fallback' (DLM's Lemma 5 is for sink games; on general games N5's selection and SSI's I can both be empty).
Stop: Iσ = Iτ = ∅ (both optimal, 2309.02223 Lemma 5). Output: regions and strategies of the final σ (Engine.regions).
Usage: n5.py ssi|n5 game.pg out.sol [--start "SIGMA0 ..." "TAU0 ..."] [--cap K]   (prints RESULT iterations=.. fallback=..)"""
import sys, os, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "si")); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg
from si import Engine
def dual(h): return pg.Game([p + 1 for p in h.prio], [1 - o for o in h.owner], [list(s) for s in h.succ])
def run(g, mode="n5", start=None, cap=10 ** 6):
    """Returns (iterations, fallback, win, strategies, evals). start = (sigma dict, tau dict) or None (best-reward)."""
    n = g.n
    E, Ed = Engine(g), Engine(dual(g))
    sigma, tau = list(E.initial("best")), list(Ed.initial("best"))
    if start:
        for v, w in start[0].items(): sigma[v] = w
        for v, w in start[1].items(): tau[v] = w
    it = fb = 0
    while it < cap:
        vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
        vt, tbar = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
        if not Is and not It: break
        it += 1
        def ssi_step():
            ns, nt = list(sigma), list(tau)
            for v, w in Is:
                if tbar[v] == w: ns[v] = w
            for v, w in It:
                if sbar[v] == w: nt[v] = w
            return ns, nt
        if mode == "ssi":
            sigma, tau = ssi_step(); continue
        ns, nt = list(sigma), list(tau)
        if Is:
            opt = {v: {sigma[v]} for v in range(n) if g.owner[v] == 0}
            for v, w in Is: opt[v].add(w)
            succ = [sorted(opt[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)]
            Er = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ)))
            _, best = Er.evaluate(tuple(tau[v] if g.owner[v] == 1 else -1 for v in range(n)))
            for v in range(n):
                if g.owner[v] == 0: ns[v] = best[v]
        if It:
            opt = {v: {tau[v]} for v in range(n) if g.owner[v] == 1}
            for v, w in It: opt[v].add(w)
            succ = [sorted(opt[v]) if g.owner[v] == 1 else [sigma[v]] for v in range(n)]
            Er = Engine(pg.Game(list(g.prio), list(g.owner), succ))
            _, best = Er.evaluate(tuple(sigma[v] if g.owner[v] == 0 else -1 for v in range(n)))
            for v in range(n):
                if g.owner[v] == 1: nt[v] = best[v]
        if ns == sigma and nt == tau:   # no progress from N5's selection: one classical switch-all SI step (always improves)
            fb += 1
            if Is:
                for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
            else:
                for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
        sigma, tau = ns, nt
    win, ws = E.regions(tuple(sigma))
    return it, fb, win, ws, E.evals + Ed.evals

if __name__ == "__main__":
    mode, path, out = sys.argv[1], sys.argv[2], sys.argv[3]
    cap = int(sys.argv[sys.argv.index("--cap") + 1]) if "--cap" in sys.argv else 10 ** 6
    g = pg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%")))
    st = None
    if "--start" in sys.argv:
        k = sys.argv.index("--start")
        st = tuple(dict(map(int, t.split(":")) for t in sys.argv[k + j].split()[1:]) for j in (1, 2))
    t0 = time.time(); it, fb, win, ws, ev = run(g, mode, st, cap)
    with open(out, "w") as f:
        f.write(f"paritysol {g.n - 1};\n")
        for v in range(g.n): f.write(f"{v} {win[v]} {ws[v]};\n" if ws[v] is not None else f"{v} {win[v]};\n")
    print(f"RESULT mode={mode} n={g.n} iterations={it} fallback={fb} capped={int(it >= cap)} evals={ev} secs={time.time() - t0:.2f}")
