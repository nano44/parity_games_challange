#!/usr/bin/env python3
"""L-RED R178 CAUSE: classify each move of a fastabs run. Move of v at step t (state t-1 -> t) to option w:
  XI   : w was not available at state t-2 (became Xi-better at state t-1), or t = 1;
  KAPPA: w was already available at state t-2 but not chosen (kappa then larger); now kappa-least.
Also: per step, does it contain an XI move? Steps with only KAPPA moves are 'kappa-only steps'.
Usage: cause.py genome.json ..."""
import sys, os, json
def run(G):
    N, lev, opts, gate, br, bp = G["N"], G["lev"], G["opts"], G["gate"], G["br"], G["bp"]
    order = sorted(range(N), key=lambda v: lev[v]); s = list(G["start"]); prev_av = None; res = []
    while True:
        X = [0] * N
        def face(v, k):
            wt, xt, b = opts[v][k]; return (1 << br[b] if bp[b] == 0 else -(1 << br[b])) + (0 if xt < 0 else X[xt])
        for v in reversed(G["xorder"]): X[v] = face(v, s[v])
        avail = [[k for k in range(len(opts[v])) if k == s[v] or face(v, k) > X[v]] for v in range(N)]
        if all(len(a) == 1 for a in avail): break
        key = [None] * N; ns = list(s)
        for v in order:
            bb = None
            for k in avail[v]:
                wt = opts[v][k][0]; kk = ((gate[v][k],) if wt < 0 else key[wt] + (gate[v][k],))
                if bb is None or kk < bb[0]: bb = (kk, k)
            key[v] = bb[0]; ns[v] = bb[1]
        if ns == s: break
        step = []
        for v in range(N):
            if ns[v] != s[v]:
                k = "KAPPA" if prev_av is not None and ns[v] in prev_av[v] else "XI"
                step.append((v, k))
        res.append(step); prev_av = avail; s = ns
    return res
for p in sys.argv[1:]:
    R = run(json.load(open(p))); mv = sum(len(s) for s in R); kap = sum(1 for s in R for _, k in s if k == "KAPPA")
    konly = sum(1 for s in R if all(k == "KAPPA" for _, k in s))
    print(f"CAUSE {os.path.basename(p)} steps {len(R)} moves {mv} kappa_moves {kap} kappa_only_steps {konly}")

def lowest_check(G):
    """Lemma XI-NEW: at every step t >= 2 the mover(s) of least W-level include one whose new option was not available at t-2."""
    lev = G["lev"]; R = run(G); bad = 0
    for t, st in enumerate(R):
        if t == 0 or not st: continue
        m = min(lev[v] for v, _ in st)
        if not any(k == "XI" for v, k in st if lev[v] == m): bad += 1
    return len(R), bad
