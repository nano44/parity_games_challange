#!/usr/bin/env python3
"""L-RED 68 R239: box 212 RF-D's hypothesis [IMP3] (claude/l-new 5fa64fe6 docs/new/N5-RFLEVEL-box212.md §6) tested on L-RED's SPEC-exact
N5 engine (experiments/red/r237/n5s237.py mode spec), state by state:
[IMP3] «every step of N5 (SPEC S1-S5) from S3 on Γ3(G) before its first fallback visits only standard states and changes σ exactly at a
non-empty set of movers, each to a gate of strictly larger Ω_t (VJ value against Odd's pointwise-optimal reply).»
Γ3(G): box 189's gamma3.build(G, box 195's PADS) (OBJECTS only; env LNEW = archive of claude/l-new fcba92fc). A mover's options are its
pads m_(x,k) (pad -> gate is one step with no P-element, so comparing pads compares gates).
Must-0 counters (unit: one transition before the first fallback, or one state up to it):
 nonstd   a state 0..F1-1 whose sigma differs from S3's off the movers, or whose tau differs from S3's
 nomove   a non-fallback transition that changes no mover
 offmover a non-fallback transition that changes an Even vertex that is not a mover
 notimp   a mover that moves to a pad whose Xi_sigma value (n5s237.vjproc at the state) is not strictly above its current pad's
 tauch    a non-fallback transition that changes tau
 fbn      genomes with no fallback (the run ends without one) [descriptive: N5 ends with a fallback by R15]
Second engine (sampled, XEVERY): box 190's n5v mode spec from S3 (box 21 n5x.start_pair), sigma compared state by state up to F1:
 xdiff (genomes whose state sequences differ).
CTRL=1: notimp's comparison inverted (must fire on every genome with a non-fallback transition).
Usage: imp239.py rand SEED COUNT NMAX DMAX DEGMAX   |   imp239.py json FILE.json ...     (env LNEW; LRED must be UNSET: box 195 imports an optional module when it is set; XEVERY default 20)"""
import sys, os, json, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); LNEW = os.environ["LNEW"]
sys.path[:0] = [HERE, os.path.join(HERE, "..", "r237")] + [os.path.join(LNEW, p) for p in ("experiments/new/box195", "experiments/new/box190", "experiments/new/box189", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
import n5s237 as S
import gamma3
import rf239
PADS = {"K", "pe", "pb", "m"}; CTRL = os.environ.get("CTRL") == "1"; XEVERY = int(os.environ.get("XEVERY", "20"))
KEYS = ("nonstd", "nomove", "offmover", "notimp", "tauch")

def one(G, second=False):
    g, _, _, V = gamma3.build(G, PADS); n = g.n; prio = list(g.prio); owner = list(g.owner); succ = [sorted(set(s)) for s in g.succ]
    N = G["N"]; mv = {V[("x", x)] for x in range(N)}
    order = sorted(range(n), key=lambda v: (prio[v], v)); rk = [0] * n
    for r, v in enumerate(order): rk[v] = r
    ev = [p % 2 == 0 for p in prio]; O = S.Ord(rk, ev); isE = [o == 0 for o in owner]; isO = [o == 1 for o in owner]
    tr = []; fbt = []; its, fbs, win, _, _ = S.run(prio, owner, succ, "spec", trace=tr, fbtrace=fbt)
    F1 = fbt[0] if fbt else len(tr); c = {k: 0 for k in KEYS}; s0, t0 = tr[0]; steps = 0
    for t in range(min(F1, len(tr))):
        sg, tu = tr[t]
        c["nonstd"] += int(any(sg[v] != s0[v] for v in sg if v not in mv) or tu != t0)
        if t + 1 <= F1 - 1 and t + 1 < len(tr):
            sg2, tu2 = tr[t + 1]; steps += 1
            ch = [v for v in sg if sg2[v] != sg[v]]
            c["nomove"] += int(not any(v in mv for v in ch)); c["offmover"] += int(any(v not in mv for v in ch)); c["tauch"] += int(tu2 != tu)
            vs, _ = S.vjproc(n, rk, ev, [[sg[v]] if isE[v] else succ[v] for v in range(n)], isO)
            for x in ch:
                if x in mv: c["notimp"] += int(O.better(vs[sg2[x]], vs[sg[x]]) == CTRL)
    xd = None
    if second:
        import n5v, n5x, n5
        from si import Engine
        import eg195
        g2 = eg195.topg(g); E, Ed = Engine(g2), Engine(n5.dual(g2)); sigma, tau = n5x.start_pair(g2, E, Ed, None); xd = 0
        for t in range(min(F1, len(tr))):
            xd |= int(any(sigma[v] != w for v, w in tr[t][0].items()))
            r = n5v.step(g2, E, Ed, sigma, tau, "spec")
            if r is None: break
            sigma, tau = r[0], r[1]
    return c, F1, its, fbs, steps, n, xd

if __name__ == "__main__":
    mode = sys.argv[1]; t0 = time.time()
    if mode == "rand":
        seed, cnt, nmax, dmax, degmax = map(int, sys.argv[2:7]); rng = random.Random(seed); gens = [rf239.rand_genome(rng, nmax, dmax, degmax) for _ in range(cnt)]
    else:
        gens = []
        for fn in sys.argv[2:]:
            G = json.load(open(fn)); G = G.get("genome", G); G.pop("_evals", None); gens.append(G)
    tot = {k: 0 for k in KEYS}; mF = 0; sF = 0; st = 0; mn = 0; nofb = 0; x = xd = 0; first = None; lines = []
    for i, G in enumerate(gens):
        sec = (XEVERY > 0 and i % XEVERY == 0 and not CTRL) or mode == "json"
        c, F1, its, fbs, steps, n, d = one(G, sec)
        for k in KEYS: tot[k] += c[k]
        mF = max(mF, F1); sF += F1; st += steps; mn = max(mn, n); nofb += int(fbs == 0)
        if d is not None: x += 1; xd += d
        if first is None and sum(c.values()): first = (i, c)
        if mode == "json": lines.append(f"  {os.path.basename(sys.argv[2 + i])}: N {G['N']} |V| {n} F1 {F1} iterations {its} fallbacks {fbs} " + " ".join(f"{k} {c[k]}" for k in KEYS) + f" xdiff {d}")
    for l in lines: print("IMP239" + l, flush=True)
    print(f"IMP239 {mode} {' '.join(sys.argv[2:7]) if mode == 'rand' else len(gens)}" + (" CTRL 1" if CTRL else "") + ": " + " ".join(f"{k} {tot[k]}" for k in KEYS)
          + f" | genomes {len(gens)} non-fallback steps {st} max F1 {mF} sum F1 {sF} no-fallback runs {nofb} max |V| {mn} | second engine (n5v spec) sampled {x} xdiff {xd} | {time.time() - t0:.0f} s"
          + (f" | first nonzero {first}" if first else ""), flush=True)
