#!/usr/bin/env python3
"""Box 26: re-entries into R inside a (τ, joint-λ)-phase of C^1O N5 runs (any Even vertex x, any successor; R = σ-reach set of o,
following forced Odd edges and τ, as thtrace.Rset).
LEAVE of x at transition L: x ∈ R_L, x ∉ R_{L+1}; RE-ENTRY at E (> L, same phase): x ∉ R_E, x ∈ R_{E+1}.
Route values are compared with ONE terminal (Lemma G (c)): val(π) = π ⊕ T, T = W_{E+1}(o), π = x's path to o (o excluded).
Class of a re-entry, against x's LAST leave:
  ROUTE  val(π^{E+1}) ▷ val(π^L)        (strict route improvement inside R: the Lead's statement)
  WRISE  not ROUTE, w_{E+1} ▷ w_L        (o's own value rose: one-player progress of o's continuation in G_τ)
  THETA  not ROUTE, w_{E+1} = w_L, θ_{E+1} ▷ θ_L  (pure throttle release: the honest gate opened, nothing improved in G_τ)
  OTHER  none of these
Also: leave kind (arena / fallback / downstream = x did not switch), and (h) at L and E+1.
Usage: reentry.py game.pg [start] [-v] | reentry.py --random N nmin nmax seed [--randstart]"""
from common import *
from thtrace import Rset
from wdrop_h import oncycle
def path(g, s, t, x, o):
    nxt = [s[v] if g.owner[v] == 0 else t[v] for v in range(g.n)]; out, y = [], x
    while y != o:
        if y in out: return None
        out.append(y); y = nxt[y]
    return out
def run(g, start, cnt, verbose=False, ex=None):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, start)
    rows = []
    while True:
        Xi, sb = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t)); Eg, W = wvals(g, s, t)
        h = not oncycle(g, s, sb, o) and not oncycle(g, s, t, o) and Xi[o][0] == W[o][0]
        rows.append(dict(s=tuple(s), t=tuple(t), lam=(tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), th=E.key(Xi[o]),
                         w=E.key(W[o]), Wo=W[o], R=Rset(g, s, t, o), h=h, fb=0))
        r = step(g, E, Ed, s, t)
        if r is None: break
        ns, nt, Is, It, fb, _, _ = r; rows[-1]["fb"] = fb; s, t = ns, nt
    last = {}
    for k in range(len(rows) - 1):
        a, b = rows[k], rows[k + 1]
        if a["lam"] != b["lam"]: last = {}; continue
        for x in range(g.n):
            if g.owner[x] != 0 or x == o: continue
            if x in a["R"] and x not in b["R"]:
                kind = "downstream" if a["s"][x] == b["s"][x] else ("fallback" if a["fb"] else "arena")
                last[x] = (path(g, a["s"], a["t"], x, o), a["th"], a["w"], kind, a["h"], k)
                cnt["leave_" + kind] += 1
            elif x not in a["R"] and x in b["R"] and x in last:
                pL, thL, wL, kind, hL, kL = last[x]; pE = path(g, b["s"], b["t"], x, o)
                def val(p):
                    v = b["Wo"]
                    for u in reversed(p): v = E.extend(u, v)
                    return E.key(v)
                if pL is None or pE is None: c = "OTHER"
                elif val(pE) > val(pL): c = "ROUTE"
                elif b["w"] > wL: c = "WRISE"
                elif b["th"] > thL: c = "THETA"
                else: c = "OTHER"
                if c == "THETA": cnt["THETA_release" if b["th"] == b["w"] else "THETA_partial"] += 1
                cnt[c] += 1; cnt[c + "_after_" + kind] += 1
                if not (hL and b["h"]): cnt[c + "_noh"] += 1
                if c != "ROUTE" and ex is not None and not ex: ex.append((g, start, x, kL, k + 1, c, kind))
                if verbose: print(f"x={x} leave@{kL} ({kind}) route {pL} -> reenter@{k+1} route {pE}: {c}")
if __name__ == "__main__":
    a = sys.argv[1:]; cnt = Counter() if False else __import__("collections").Counter(); ex = []
    if a[0] == "--random":
        RS = "--randstart" in a; N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        for i in range(N):
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            start = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
            cnt["runs"] += 1; run(g, start, cnt, ex=ex)
        print(dict(sorted(cnt.items())))
        if ex: g, st, x, kL, kE, c, kind = ex[0]; print("first non-ROUTE:", c, "x", x, "leave", kL, kind, "reenter", kE, "n", g.n)
    else:
        g = load(a[0]); st = readstart(a[1]) if len(a) > 1 and not a[1].startswith("-") else None
        run(g, st, cnt, verbose="-v" in a); print(a[0], dict(sorted(cnt.items())))
