#!/usr/bin/env python3
"""L-RED 71 R247 section 8: RC_n, a counter DESIGNED AGAINST candidate RF (first version: QUADRATIC, not a kill).
Bits i = 1..n as in Friedmann's G_n (arXiv 1106.0778 section 6.4): d_i (Even) closes the cycle d_i -> e_i -> d_i, Odd's e_i leaves by
h_i -> k_i, the exit selector k_i (Even) -> x or g_j (j > i), the entry f_i -> e_i, the root s -> x or f_j. No deceleration lane, no r, c.
Three additions, each answering one way in which RF cancels Friedmann's counter (docs/red/R247-rf.md sections 2-4, 8):
  ARMED SELECTOR  g_i -> {b_i, k_i}, b_i -> {f_i, k_i}, b_i of small odd priority 3: when bit i closes, s and b_i see it at once, g_i one
                  iteration later, the exits k_j of the lower set bits one iteration after that; in that window the lower set bits j < i
                  see the root improved while their own exit is still stale and is NOT yet improvable, so RF lets them RESET (d_j -> s).
  SCAN            sc_i (Odd) -> {d_i, sc_(i-1), hh_i}, sc_0 -> s, hh_i -> h_i; an unset bit rests at d_i -> sc_(i-1). Odd's scan passes
                  through d_j when bit j is unset or stale, through the exit of bit j when its link is stale, and skips a settled set bit;
                  so RF's dependency makes every unset bit wait for every lower bit that is unset or in transition.
  REST MARKERS    priority(sc_(i-1)) is even and above e_i: from s an unset bit first returns to its rest, then closes.
Priorities (B = 8n): x 1; s B + 8; d_i 4i + 3; e_i 4i + 4; g_i 4i + 6; k_i B + 4i + 9; f_i B + 4i + 11; h_i B + 4i + 12; sc_i 4i + 10 (sc_0
10); hh_i 4i + 6; b_i 3. Start: d_i -> sc_(i-1), s -> x, k_i -> x, g_i -> k_i, b_i -> k_i. N = 9n + 3 vertices.
DATA (out/rc.out): RF makes n^2 + 3n - 2 iterations (n = 2..30), Howard 5n - 3; sets n(n+1)/2, resets n(n-1)/2: after a reset of several bits
the exits relink from the top down, one per iteration, and the bits close again highest first, so each bit pattern of the binary counter
is NOT visited. Options kept for the record: layers=K, hi=0, rest=0, viaE, chain (each breaks the count; see R247 section 8).
Usage: rc247.py n[,n...] [ev] [opt ...]      prints iterations of rf and howard, sets, resets, even_wins; ev lists RF's bit events
       rc247.py dump n OUT.pg                 writes RC_n (PGSolver text, labels, '% start' line) and prints its sha1"""
import sys, os, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE, os.path.join(HERE, "..", "r237")]
import si247, rf247
def build(n, K=1, opts={}):
    rows = []; idx = {}
    def new(lab, prio, owner, succ=None):
        idx[lab] = len(rows); rows.append([prio, owner, succ, lab]); return idx[lab]
    B = 8 * n
    new("x", 1, 1); new("s", B + 8, 0)
    if opts.get("sc0"): new("sc0", 10, 1)                        # rest of bit 1: one successor s
    for i in range(1, n + 1):
        new(f"d{i}", 4 * i + 3, 0); new(f"e{i}", 4 * i + 4, 1); new(f"g{i}", 4 * i + 6, 0)
        new(f"k{i}", B + 4 * i + 9, 0); new(f"f{i}", B + 4 * i + 11, 1); new(f"h{i}", B + 4 * i + 12, 1)
        new(f"sc{i}", (4 * i + 10) if opts.get("hi", "1") == "1" else (4 * i + 6), 1)   # scan vertex sigma_i (Odd): d_i or the scan below
        for b in range(K): new(f"b{i}_{b}", 3, 0)
        if opts.get("hh"): new(f"hh{i}", 4 * i + 6, 1)             # side door of the scan into the exit of bit i
    V = idx
    rows[V["x"]][2] = [V["x"]]
    if opts.get("sc0"): rows[V["sc0"]][2] = [V["s"]]
    rows[V["s"]][2] = [V["x"]] + [V[f"f{j}"] for j in range(1, n + 1)]
    start = {V["s"]: V["x"]}
    for i in range(1, n + 1):
        below = V[f"sc{i-1}"] if (i > 1 or opts.get("sc0")) else None
        rows[V[f"d{i}"]][2] = [V[f"e{i}"], V["s"]] + ([below] if below is not None else [])
        start[V[f"d{i}"]] = below if (below is not None and opts.get("rest", "1") == "1") else V["s"]
        rows[V[f"e{i}"]][2] = [V[f"d{i}"], V[f"h{i}"]]
        rows[V[f"h{i}"]][2] = [V[f"k{i}"]]
        if opts.get("chain"): rows[V[f"k{i}"]][2] = [V[f"g{i+1}"]] if i < n else [V["x"]]
        else: rows[V[f"k{i}"]][2] = [V["x"]] + [V[f"g{j}"] for j in range(i + 1, n + 1)]; start[V[f"k{i}"]] = V["x"]
        rows[V[f"f{i}"]][2] = [V[f"e{i}"]]
        prev = V[f"f{i}"]
        for b in range(K):
            rows[V[f"b{i}_{b}"]][2] = [prev, V[f"k{i}"]]; start[V[f"b{i}_{b}"]] = V[f"k{i}"]; prev = V[f"b{i}_{b}"]
        rows[V[f"g{i}"]][2] = [prev, V[f"k{i}"]]; start[V[f"g{i}"]] = V[f"k{i}"]
        rows[V[f"sc{i}"]][2] = [V[f"e{i}"] if opts.get("viaE") else V[f"d{i}"], below if below is not None else V["s"]] + ([V[f"hh{i}"]] if opts.get("hh") else [])
        if opts.get("hh"): rows[V[f"hh{i}"]][2] = [V[f"h{i}"]]
    return rows, start, V
def run(n, K, rule, ev=False):
    rows, start, V = build(n, K, OPTS); N = len(rows)
    e = si247.SI([r[0] for r in rows], [r[1] for r in rows], [sorted(r[2]) for r in rows]); L = lambda v: rows[v][3]
    start = {v: w for v, w in start.items() if len(rows[v][2]) > 1 or True}
    for v in range(N):
        if rows[v][1] == 0 and v not in start: start[v] = rows[v][2][0]
    bits = [0] * (n + 1); evs = []
    def hook(it, sigma, val, sbar, I, ch):
        for v, w in sorted(ch.items()):
            if L(v).startswith("d"):
                i = int(L(v)[1:])
                if L(w).startswith("e"): bits[i] = 1; evs.append(f"{it+1}:+{i}")
                elif bits[i]: bits[i] = 0; evs.append(f"{it+1}:-{i}({L(w)})")
                else: evs.append(f"{it+1}:{L(v)}>{L(w)}")
    r = e.run(rule, dict(start), hook=hook, cap=200000)
    return r, evs, N
OPTS = {"sc0": "1", "hh": "1"}
if __name__ == "__main__":
    if sys.argv[1] == "dump":
        n = int(sys.argv[2]); rows, start, V = build(n, 1, OPTS)
        for v in range(len(rows)):
            if rows[v][1] == 0 and v not in start: start[v] = rows[v][2][0]
        txt = f"parity {len(rows) - 1};\n" + "".join(f'{v} {r[0]} {r[1]} {",".join(map(str, sorted(r[2])))} "{r[3]}";\n' for v, r in enumerate(rows)) + "% start " + " ".join(f"{v}:{w}" for v, w in sorted(start.items())) + "\n"
        open(sys.argv[3], "w").write(txt); print("RC247 dump n", n, "N", len(rows), "sha1", hashlib.sha1(txt.encode()).hexdigest()); sys.exit(0)
    opts = dict(OPTS); opts.update(dict((a.split("=") + ["1"])[:2] for a in sys.argv[2:])); OPTS = opts; K = int(opts.get("layers", 1))
    for n in [int(x) for x in sys.argv[1].split(",")]:
        out = []
        for rule in ("rf", "howard"):
            r, evs, N = run(n, K, rule)
            out.append(f"{rule} {r['its']} (sets {sum(1 for x in evs if '+' in x)}, resets {sum(1 for x in evs if ':-' in x)}, even_wins {sum(1 for w in r['win'] if w == 0)})")
            if rule == "rf" and opts.get("ev"): print("   ", " ".join(evs)[:1500])
        print(f"RC n {n} N {N} layers {K}: " + "; ".join(out), flush=True)
