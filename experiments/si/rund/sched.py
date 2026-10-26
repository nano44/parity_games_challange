#!/usr/bin/env python3
"""L-SI box 17 (successor 13): DATA for Lemma P^c_sch and Corollary CHARGE (docs/si/N5-RUND-box17.md §14).
Setting: S = a maximal run of states inside one phase (key (lambda_Xi, tau) constant), no fallback, lambda_W map constant (CR-D's (ii)).
Level L (env L, default -1). Even edge (x, z) FORBIDDEN AT k: z != sigma_k(x), COARSE_L W_k(z) > COARSE_L W_k(sigma_k x), not Xi_k(z) > Xi_k(sigma_k x).
Path r = (r_0..r_m) to a W-cycle node; its SCHEDULE at state k is clean if every Even edge (r_i, r_i+1) is not forbidden at state k-1-i, and k-m >= k_0.
  P^c_sch: clean schedule at k  =>  COARSE_L W_k(r_0) >= COARSE_L value(r).
  GEN check: for all s <= t in S and every x, with r = x's W-play prefix at t: clean at s => COARSE W_s(x) == COARSE W_t(x) (with MON).
  CHARGE: every change of COARSE W(x) at s-1 -> s has r = x's play at s with dirty schedule at s-1 (a WINDOW change if s-1-m < k_0,
  else CHARGED to a forbidden (i, edge, state s-2-i)).
Also per forbidden edge: #states forbidden, first / last forbidden state (relative to k_0), PERSISTENT if forbidden at the last state j-1.
MUT=1: schedule shifted by one (edge i at k-i); MUT=2: forbidden-ness ignored (CR-D without (i)). Usage: sched.py --one GAME [START] [-v] | --list FILE [KMIN] (env RS random start pairs, NMAX)"""
import sys, os, random
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "fb2o"))
from n5x import step, start_pair, Engine, dual, load, readstart
from tcdir import lasso, wval
L = int(os.environ.get("L", "-1")); MUT = os.environ.get("MUT", "0"); VERB = "-v" in sys.argv
C = Counter(); VIOL = []

def ck(E, x):
    m = (x[1] >> (L + 1)) << (L + 1) if L >= 0 else x[1]
    return (E.rew[x[0]], E.weight(m))

def check(g, name, start=None):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []
    while len(rows) <= 3000:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        wn = (lambda s, t: (lambda v: s[v] if g.owner[v] == 0 else t[v]))(list(s), tuple(t))
        W = [wval(E, wn, v) for v in range(g.n)]
        rows.append(dict(key=(tuple(x[0] for x in vs), tuple(t)), lw=tuple(w[0] for w in W), s=list(s), wn=wn, vs=vs, W=W,
                         fb=r[4] if r else 0))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while (j + 1 < len(rows) and not rows[j]["fb"] and rows[j + 1]["key"] == rows[i]["key"]
               and rows[j + 1]["lw"] == rows[i]["lw"]): j += 1
        if j > i: run(g, E, name, rows, i, j)
        i = j + 1

def forb(g, E, R):
    out = set()
    for x in range(g.n):
        if g.owner[x] != 0: continue
        a = R["s"][x]
        for z in set(g.succ[x]):
            if z != a and ck(E, R["W"][z]) > ck(E, R["W"][a]) and not E.key(R["vs"][z]) > E.key(R["vs"][a]): out.add((x, z))
    return out

def play(R, x):
    pl, ci = lasso(R["wn"], x); return pl[:pl.index(R["W"][x][0]) + 1]

def dirty(g, F, R, r, k, i0):
    """None if the schedule of r at state k is clean, 'window' if k - m < k_0, else the list of forbidden (i, edge, state)."""
    m = len(r) - 1
    if k - m < i0: return "window"
    bad = []
    for q in range(m):
        if g.owner[r[q]] != 0: continue
        st = k - q if MUT == "1" else k - 1 - q
        if MUT != "2" and st in F and (r[q], r[q + 1]) in F[st]: bad.append((q, (r[q], r[q + 1]), st))
    return bad or None

def run(g, E, name, rows, i, j):
    C["runs"] += 1; C["states"] += j - i + 1
    F = {k: forb(g, E, rows[k]) for k in range(i, j)}
    first, last, cnt = {}, {}, Counter()
    for k in range(i, j):
        for e in F[k]: first.setdefault(e, k - i); last[e] = k - i; cnt[e] += 1
    pers = {e for e in last if last[e] == j - 1 - i}
    C["forbidden_edges"] += len(last); C["persistent_edges"] += len(pers); C["forbidden_pairs"] += sum(cnt.values())
    if cnt:
        mc = max(cnt.values()); C["max_forb_states_per_edge"] = max(C["max_forb_states_per_edge"], mc)
        if mc > g.n - 1: C["FORB_GT_N1"] += 1; print("FORB_GT_N1", name, i, j - i, g.n, cnt.most_common(1))
        C["max_last_forb_rel"] = max(C["max_last_forb_rel"], max(last.values()))
        if max(last.values()) > g.n - 1: C["LASTFORB_GT_N1"] += 1
    if VERB:
        print(f"RUN {name} k0={i} len={j - i} edges_forbidden={len(last)} persistent={len(pers)}")
        for e in sorted(last, key=lambda e: last[e]):
            print(f"  EDGE {e} first={first[e]} last={last[e]} count={cnt[e]} {'PERSISTENT' if e in pers else ''}")
    cv = [[ck(E, rows[k]["W"][x]) for x in range(g.n)] for k in range(i, j + 1)]
    # GEN: every pair s <= t
    for tt in range(i, j + 1):
        for x in range(g.n):
            r = play(rows[tt], x)
            for ss in range(i, tt):
                if dirty(g, F, rows[tt], r, ss, i) is None:
                    C["gen_clean"] += 1
                    if cv[ss - i][x] != cv[tt - i][x]:
                        C["GEN_V"] += 1; VIOL.append(("GEN", name, i, ss, tt, x))
                    elif len(r) > 1: C["gen_clean_content"] += 1
    # CHARGE: every change at s-1 -> s
    pervx = defaultdict(lambda: Counter()); charged_edges = defaultdict(set)
    for ss in range(i + 1, j + 1):
        for x in range(g.n):
            if cv[ss - i][x] == cv[ss - 1 - i][x]: continue
            C["changes"] += 1; pervx[x]["changes"] += 1
            r = play(rows[ss], x); d = dirty(g, F, rows[ss], r, ss - 1, i)
            if d is None: C["CHARGE_V"] += 1; VIOL.append(("CHARGE", name, i, ss, x)); continue
            if d == "window": C["window"] += 1; pervx[x]["window"] += 1; continue
            C["charged"] += 1; pervx[x]["charged"] += 1
            es = {e for _, e, _ in d}; charged_edges[x] |= es
            if es & pers: C["charged_persistent"] += 1
            if VERB: print(f"  CHANGE x={x} s={ss - i} m={len(r) - 1} charged={d}")
    for x, c in pervx.items():
        C["max_changes_per_vertex"] = max(C["max_changes_per_vertex"], c["changes"])
        C["max_charged_per_vertex"] = max(C["max_charged_per_vertex"], c["charged"])
        C["max_charged_edges_per_vertex"] = max(C["max_charged_edges_per_vertex"], len(charged_edges[x]))
    if VERB:
        for x in sorted(pervx): print(f"  VERTEX {x} {dict(pervx[x])} charged_edges={sorted(charged_edges[x])}")

def main():
    a = [x for x in sys.argv[1:] if x != "-v"]
    if a[0] == "--one":
        g = load(a[1]); check(g, a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        kmin = int(a[2]) if len(a) > 2 else 2
        for line in open(a[1]):
            f = line.strip()
            if not f: continue
            g = load(os.path.join(ROOT, f))
            if g.n > int(os.environ.get("NMAX", "48")) or sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2) < kmin:
                continue
            check(g, f); rng = random.Random(f)
            for _ in range(int(os.environ.get("RS", "0"))):
                check(g, f + " rs", ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                     {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}))
    print(f"L={L} MUT={MUT}", " ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for v in VIOL[:8]: print("VIOLATION", v)
    print("SCHED PASS" if not VIOL else "SCHED FAIL")

if __name__ == "__main__":
    main()
