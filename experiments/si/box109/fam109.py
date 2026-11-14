#!/usr/bin/env python3
"""L-SI box 109: the families of the hybrid table, and the table runner.
Families (name ARG):
  gk k      Gamma3(G_k): G_k by box 108's gk108.build(k) with gate numbers ranked onto 0..M-1, L-NEW's gamma3.build(G, eg195.PADS) +
            eg195.topg (the calls of L-RED-B's b6n5.py; the game equals the one built from L-RED-B's gk.py, vertex by vertex, for
            k = 3..12: gkeq mode); n = 135k - 230; start S3
  du a      the disjoint union Gamma3(G_a) + W(G_a, iota) (a >= 3); start S3
  wl n      W(G_n, iota): Friedmann's G_n (arXiv 1106.0778v2, Figure 4's injective priorities; L-LIT's transcription T66) inside box
            104's W-flat wrapper (wrap() and lmcs_game() below are copies of experiments/si/box104/wrap104.py's); start S3
  fr n      G_n itself; start: iota for Even, S3 for Odd
  sae n     PGSolver switchallexp_n (experiments/hard-families/pgsolver_port.py); start S3
  sbe n     PGSolver switchbestexp_n; start S3
  ws n      W(switchallexp_n, best-reward start) (box 104's frozen W_n); start S3
  rfs n | zad n | cun n | dlb n | dml n    experiments/si/gens.py: randomfacetsubexp, zadehexp, cunninghamexp, dlmm_bland, dlmm_ML; S3
Env: LLIT (a tree holding claude/l-lit 5c53efbd's docs/lit/T66-depth-check.py; needed by wl, fr, du only); REDB (a tree holding
claude/l-red-b's experiments/red-b; needed by «gkeq» only). Everything else is read from this repository (L-NEW's box 21 / 189 /
190 / 195 files, experiments/si/si.py, experiments/harness, experiments/hard-families, experiments/si/gens.py), read-only.
Usage: fam109.py gkeq k..   |   fam109.py sinks FAMILY ARGS..   (RF's switching sets S against the improvable sets Imp)   |
       fam109.py table FAMILY ARGS.. -- MODE.. [--cap K] [--secs S] [--check]   one line per (family arg, mode):
  n, m, iterations (unit: iterations of the rule's own loop; one-sided rules count Even's improvement steps), fallbacks, switches
  (unit: (Even vertex, iteration) pairs with a changed successor), capped, wrong (vertices whose winner differs from harness
  Zielonka; with --check), badstrat (complaints of harness verify.check about the positional strategies; with --check), seconds."""
import sys, os, time, importlib.util, signal
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.environ.get("ROOT109") or os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [HERE] + [os.path.join(ROOT, p) for p in ("experiments/new/box195", "experiments/new/box189", "experiments/new/box190",
                                                         "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
sys.path.append(os.path.join(ROOT, "experiments/si/box108")); sys.path.append(os.path.join(ROOT, "experiments/hard-families"))
os.environ.setdefault("EG195_ROOT", ROOT)
import pg, n5x, n6


def gk_genome(k):
    """G_k as box 108's gk108.build(k) (four sha1 equal to the Lead's values, docs/si/box108-gk-proof.md par. 1.2), with the gate
    numbers 100 * level + eps replaced by their ranks 0..M-1 (R104's bijection clause; L-RED-B's gk.py does the same)."""
    import gk108
    G = gk108.build(k); G = G[0] if isinstance(G, tuple) else G
    vals = sorted(x for row in G["gate"] for x in row); assert len(set(vals)) == len(vals); rk = {x: i for i, x in enumerate(vals)}
    G = dict(G); G["gate"] = [[rk[x] for x in row] for row in G["gate"]]; return G


def wrap(H, s0):
    n = H.n; prio = [p + 6 for p in H.prio]; own = list(H.owner); succ = [None] * n
    def new(p, o, s=None): prio.append(p); own.append(o); succ.append(s); return len(prio) - 1
    cW = new(0, 0); succ[cW] = [cW]; K = [new(0, 0) for _ in range(4)]; own[K[2]] = 1
    pA = new(0, 0, [K[3]]); s_ = new(0, 0, [K[1]]); q = new(1, 0, [K[0]]); r = new(0, 0, [K[1]])
    succ[K[0]] = [K[1], pA]; succ[K[1]] = [q, s_]; succ[K[2]] = [r, K[2]]; succ[K[3]] = [K[1], K[2]]
    def valve(w):
        pb = new(1, 0, [K[0]]); y = new(2, 0, [w]); b = new(0, 0, [y, pb]); return b
    for v in range(n):
        out = []
        if H.owner[v] == 0:
            for w in H.succ[v]:
                b = valve(w); pbeta = new(0, 0, [b]); pe = new(1, 0, [cW]); g = new(1, 1, [pe, pbeta])
                m = new(2 if w == s0[v] else 0, 0, [g]); out.append(m)
        else:
            for w in H.succ[v]:
                b = valve(w); x3 = new(0, 0, [b]); x2 = new(0, 0, [x3]); x1 = new(0, 0, [x2]); out.append(x1)
            pe = new(1, 0, [cW]); out.append(pe)
        succ[v] = out
    top = max(prio) + 2; top += top % 2
    prio[cW] = top; prio[K[0]], prio[K[1]], prio[K[2]], prio[K[3]] = top + 2, 5, 3, top + 3
    return pg.Game(prio, own, [sorted(s) for s in succ])


def lmcs_game(n):
    spec = importlib.util.spec_from_file_location("t66", os.path.join(os.environ["LLIT"], "docs/lit/T66-depth-check.py")); t66 = importlib.util.module_from_spec(spec)
    sys.argv, keep = [sys.argv[0]], sys.argv
    try: spec.loader.exec_module(t66)
    finally: sys.argv = keep
    g, start, names = t66.lmcs(n); prio = list(g.prio)
    for v, nm in enumerate(names):
        if nm[0] in "degkfh": prio[v] -= 2
    assert len(set(prio)) == g.n and max(prio) == 12 * n + 8
    return pg.Game(prio, list(g.owner), [list(x) for x in g.succ]), list(start)


def family(name, a):
    """returns (game, start_pair or None)"""
    if name == "gk":
        import gamma3, eg195
        g0, _, _, V = gamma3.build(gk_genome(a), eg195.PADS); return eg195.topg(g0), None
    if name == "wl":
        H, s0 = lmcs_game(a); return wrap(H, s0), None
    if name == "du":        # disjoint union Gamma3(G_a) + W(G_a, iota): the vertices of W(G_a, iota) are renumbered after Gamma3(G_a)'s
        g1, _ = family("gk", a); g2, _ = family("wl", a); n1 = g1.n
        return pg.Game(list(g1.prio) + list(g2.prio), list(g1.owner) + list(g2.owner), [list(s) for s in g1.succ] + [[w + n1 for w in s] for s in g2.succ]), None
    if name == "fr":
        H, s0 = lmcs_game(a); E, Ed = n6.Engine(H), n6.Engine(n6.dual(H)); sg, tau = n5x.start_pair(H, E, Ed, None)
        sg = [s0[v] if H.owner[v] == 0 else sg[v] for v in range(H.n)]; return H, (sg, tau)
    if name in ("sae", "sbe", "ws"):
        import pgsolver_port as P
        H = pg.parse(P.GENS["switchbestexp" if name == "sbe" else "switchallexp"](a))
        if name != "ws": return H, None
        E, Ed = n6.Engine(H), n6.Engine(n6.dual(H)); sg, _ = n5x.start_pair(H, E, Ed, None); return wrap(H, sg), None
    import gens
    f = dict(rfs=gens.randomfacetsubexp, zad=gens.zadehexp, cun=gens.cunninghamexp, dlb=gens.dlmm_bland, dml=gens.dlmm_ML)[name]
    r = f(a); g = r[0] if isinstance(r, tuple) else r
    if isinstance(g, str): g = pg.parse(g)
    return g, None


class TimeUp(Exception): pass
def _alarm(*_): raise TimeUp()


if __name__ == "__main__":
    av = sys.argv[1:]
    if av[0] == "gkeq":      # fam109.py gkeq k..: Gamma3 of box 108's G_k against Gamma3 of L-RED-B's gk.build(k)
        sys.path.append(os.path.join(os.environ["REDB"], "experiments/red-b")); import gk, gamma3, eg195
        for k in map(int, av[1:]):
            a = family("gk", k)[0]; b = eg195.topg(gamma3.build(gk.build(k)[0], eg195.PADS)[0])
            same = list(a.prio) == list(b.prio) and list(a.owner) == list(b.owner) and [sorted(s) for s in a.succ] == [sorted(s) for s in b.succ]
            print(f"GKEQ109 k {k} n {a.n} equal {same}", flush=True)
        sys.exit(0)
    if av[0] == "sinks":     # fam109.py sinks FAMILY ARGS..: the sizes of RF's switching sets S against the improvable sets Imp
        import rf109
        for a in map(int, av[2:]):
            g, sp = family(av[1], a); tr = []; r = rf109.run(g, start=(sp[0] if sp else None), trace=tr)
            print(f"MS109 {av[1]} {a}: iterations {r['its']} max|S| {r['maxsink']} sum|S| {sum(len(s) for _, s in tr)} max|Imp| {max(ni for ni, _ in tr)} "
                  f"sum|Imp| {sum(ni for ni, _ in tr)} iterations with S = Imp {sum(1 for ni, s in tr if len(s) == ni)}", flush=True)
        sys.exit(0)
    assert av[0] == "table"
    cap = int(av[av.index("--cap") + 1]) if "--cap" in av else 10 ** 6
    secs = int(av[av.index("--secs") + 1]) if "--secs" in av else 0
    chk = "--check" in av
    i = av.index("--"); fam = av[1]; args = [int(x) for x in av[2:i]]
    modes = [x for x in av[i + 1:] if not x.startswith("--") and not x.isdigit()]
    if chk: import zielonka, verify
    for a in args:
        g, sp = family(fam, a); m = sum(len(s) for s in g.succ)
        for mode in modes:
            t0 = time.time(); signal.signal(signal.SIGALRM, _alarm)
            if secs: signal.alarm(secs)
            try:
                r = n6.run(g, mode, cap=cap, start_pair=sp); signal.alarm(0)
            except TimeUp:
                print(f"T109 {fam} {a} mode {mode} n {g.n} m {m} TIMEOUT after {secs} s", flush=True); continue
            extra = ""
            if chk and not r["capped"]:
                z = list(zielonka.solve(g)); wrong = sum(1 for v in range(g.n) if r["win"][v] != z[v])
                st = [r["strat"][v] if r["win"][v] == g.owner[v] else None for v in range(g.n)]
                extra = f" wrong {wrong} badstrat {len(verify.check(g, r['win'], st))}"
            print(f"T109 {fam} {a} mode {mode} n {g.n} m {m} iterations {r['its']} fallbacks {r['fb']} switches {r['sw']} capped {r['capped']}{extra} secs {time.time() - t0:.1f}", flush=True)
