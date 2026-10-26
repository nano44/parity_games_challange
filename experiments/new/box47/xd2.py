#!/usr/bin/env python3
"""Box 47 DATA (L-NEW successor 26; docs/new/N5-XDIR-box47.md): direct D-changes X_dir ({u} -> {u'}, u != u', in-phase) and the
2-Odd-choice game G^U, U = {u, u'} (every Odd v outside U cut to tau(v); u, u' keep ALL their edges).
Per phase of N5 on G, for every U-RUN J (maximal run of consecutive states of the phase with D_k a subset of U) that contains an X_dir
transition or a state with D_k = U, checks Corollary REPRO_U: N5^tau on G^U from (sigma_x, tau) reproduces sigma, the fallback flag,
sigma-bar and Xi at every state of J and through J's last in-phase transition (REP_V, SB_V, XI_V must be 0).
Per X_dir transition k -> k+1 it classifies (all DATA):
  SAME   lambda(u) = lambda(u') (both in one honest class)        POS   k minus the phase's first state
  HB     a W-honest state at or before k in the phase              RHO_U / RHO_U2   Xi(u) / Xi(u') changes at k -> k+1
  TIE_U  at k, Xi_k(tau(u)) = Xi_k(sigma-bar_k(u)) (u deviates on a value tie)
  VIA    the honest play from u at k+1 passes u' (u now routes through u')
  DIR    ROUTE-2 directness (RESULTS R58 (c)) of (u, u') at k and at k+1, when SAME: 'd' direct, '-' not
  FB     the transition is an S4c fallback
  A2U / A2U1  the honest play from tau(u') at k / at k+1 passes u (u' copies u's rise: a RELAY in the sense of docs/si/N5-RUND-box17.md §22)
  SCH    some Even vertex on tau(u')'s honest play at k switches at k -> k+1 (a ROUTE-type cause)
Usage: xd2.py STARTS SEED (--list FILE | --rand C LO HI GSEED | files [--start F])   (MUT=1: drop u' from U; REP_V must bite)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
for p in ("../box43", "../box21", "../box45"): sys.path.insert(0, os.path.join(HERE, p))
from multi import rand_ckO
from n5x import load, step, start_pair, Engine, dual, pg, readstart
from eprestrict import step_tau
C = {}
MUT = os.environ.get("MUT") == "1"
def inc(k, v=1): C[k] = C.get(k, 0) + v
def mx(k, v): C[k] = max(C.get(k, v), v)
VERB = os.environ.get("VERB") == "1"

def cutU(g, U, tau):
    return pg.Game(list(g.prio), list(g.owner), [list(g.succ[v]) if (g.owner[v] == 0 or v in U) else [tau[v]] for v in range(g.n)])

def play(g, s, sb, v):
    seen = []; x = v
    while x not in seen:
        seen.append(x); x = s[x] if g.owner[x] == 0 else sb[x]
    return seen, x                               # visited vertices in order, first repeated vertex

def direct(g, row, q, Qc, c):
    seq, rep = play(g, row["s"], row["sb"], q)
    if rep == q: return True                     # q on its own honest cycle
    for x in seq[1:]:
        if x == c: return True
        if x in Qc: return False
    return False

def wvals(g, s, t):
    succ = [[t[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(g.n)]
    return Engine(pg.Game(list(g.prio), list(g.owner), succ)).evaluate(tuple(s))[0]

NM = ""; ST = None
def writestart(path, start):
    with open(path, "w") as f:
        f.write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in sorted(start[0].items())) + "\n")
        f.write("TAU0 " + " ".join(f"{v}:{w}" for v, w in sorted(start[1].items())) + "\n")
def run(g, start, nm, cap=4000):
    global NM, ST; NM, ST = nm, start
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []; inc("runs")
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2]
    while len(rows) <= cap:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        rows.append(dict(s=tuple(s), t=tuple(t), sb=tuple(sb), vs=vs, lam=tuple(x[0] for x in vs), fb=r[4] if r else 0,
                         D=frozenset(q for q in Q if sb[q] != t[q])))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and (rows[j + 1]["lam"], rows[j + 1]["t"]) == (rows[i]["lam"], rows[i]["t"]): j += 1
        phase(g, E, rows, i, j, Q, nm, start); i = j + 1

def phase(g, E, rows, a, b, Q, nm, start):
    inc("phases"); done = set(); nx = 0
    for k in range(a, b):
        x, y = rows[k], rows[k + 1]
        if len(x["D"]) == 2 and (x["D"], k) not in done: urun(g, rows, a, b, x["D"], k, done)
        if len(x["D"]) != 1 or len(y["D"]) != 1 or x["D"] == y["D"]: continue
        nx += 1; inc("XDIR"); (u,), (u2,) = tuple(x["D"]), tuple(y["D"]); U = frozenset((u, u2))
        if (U, k) not in done: urun(g, rows, a, b, U, k, done)
        same = x["lam"][u] == x["lam"][u2]; inc("SAME", same)
        hb = any(wvals(g, rows[h]["s"], rows[h]["t"]) == rows[h]["vs"] for h in range(a, k + 1)); inc("HB", hb)
        rho_u = x["vs"][u] != y["vs"][u]; rho_u2 = x["vs"][u2] != y["vs"][u2]; inc("RHO_U", rho_u); inc("RHO_U2", rho_u2)
        tie = x["vs"][x["t"][u]] == x["vs"][x["sb"][u]]; inc("TIE_U", tie)
        via = u2 in play(g, y["s"], y["sb"], u)[0]; inc("VIA", via); inc("FB", x["fb"])
        a2u = u in play(g, x["s"], x["sb"], x["t"][u2])[0]; inc("A2U", a2u)        # tau(u')'s honest play at k passes u
        a2u1 = u in play(g, y["s"], y["sb"], y["t"][u2])[0]; inc("A2U1", a2u1)     # ... at k+1
        sch = any(x["s"][v] != y["s"][v] for v in play(g, x["s"], x["sb"], x["t"][u2])[0] if g.owner[v] == 0); inc("SCH", sch)
        mx("POSMAX", k - a); inc("POS0", k == a)
        dirs = ""
        if same:
            c = x["lam"][u]; Qc = {q for q in Q if x["lam"][q] == c and q != c}
            dirs = "".join("d" if direct(g, r, q, Qc, c) else "-" for r in (x, y) for q in (u, u2))
            inc("DIR_" + dirs)
        if VERB:
            print(f"{nm} n {g.n} {'S3' if start is None else 'rand'} phase [{a},{b}] k {k} u {u}->{u2} same {int(same)} hb {int(hb)} "
                  f"rho_u {int(rho_u)} rho_u' {int(rho_u2)} tie {int(tie)} via {int(via)} fb {x['fb']} a2u {int(a2u)}{int(a2u1)} sch {int(sch)} dir(k: u u', k+1: u u') {dirs}")
    mx("XDIR_PH", nx)

def urun(g, rows, a, b, U, k, done):
    x = k
    while x - 1 >= a and rows[x - 1]["D"] <= U: x -= 1
    y = k
    while y + 1 <= b and rows[y + 1]["D"] <= U: y += 1
    for h in range(x, y + 1): done.add((U, h))
    inc("URUNS"); mx("URUN_LEN", y - x)
    nd2 = sum(1 for h in range(x, y + 1) if rows[h]["D"] == U); mx("URUN_D2", nd2)
    nxd = sum(1 for h in range(x, y) if len(rows[h]["D"]) == 1 and len(rows[h + 1]["D"]) == 1 and rows[h]["D"] != rows[h + 1]["D"])
    mx("URUN_XDIR", nxd)
    tau = rows[x]["t"]; UU = frozenset(list(U)[:1]) if MUT else U
    gp = cutU(g, UU, tau); Ep, Edp = Engine(gp), Engine(dual(gp))
    s, t = list(rows[x]["s"]), list(tau); bad = sbb = xib = False
    last = y + 1 if y < b else y
    for h in range(x, last + 1):
        vs, sb = Ep.evaluate(tuple(s))
        if h <= y:
            if tuple(sb) != rows[h]["sb"]:
                if VERB and not sbb:
                    dif = [v for v in range(g.n) if sb[v] != rows[h]["sb"][v]]
                    if ST is not None and os.environ.get("SBDUMP"): writestart(os.path.join(os.environ["SBDUMP"], f"sb_{NM}.start"), ST)
                    print(f"SB {NM} {'S3' if ST is None else 'rand'} U {sorted(U)} run [{x},{y}] h {h} D {sorted(rows[h]['D'])} diff " + " ".join(
                        f"{v}:{rows[h]['sb'][v]}/{sb[v]} tau {tau[v]} inU {int(v in U)} tie {int(rows[h]['vs'][rows[h]['sb'][v]] == rows[h]['vs'][sb[v]])}" for v in dif))
                sbb = True
            if list(vs) != list(rows[h]["vs"]): xib = True
        if h == last: break
        r = step_tau(gp, Ep, Edp, s, t)
        if r is None or tuple(r[0]) != rows[h + 1]["s"] or tuple(r[1]) != tau or r[2] != rows[h]["fb"]: bad = True; break
        s, t = r[0], r[1]
    inc("REP_V", bad); inc("SB_V", sbb); inc("XI_V", xib)

if __name__ == "__main__":
    a = sys.argv[1:]; K = int(a[0]); RNG = random.Random(int(a[1])); a = a[2:]; fixed = None
    if "--start" in a: i = a.index("--start"); fixed = readstart(a[i + 1]); a = a[:i] + a[i + 2:]
    if a[0] == "--list":
        R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        gs = [(l.split()[0], load(os.path.join(R0, l.split()[0]))) for l in open(a[1]) if l.strip() and not l.startswith("#")]
    elif a[0] == "--rand":
        cnt, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        gs = [(f"rand{i}", g) for i, g in enumerate(rand_ckO(rng, lo, hi, rng.randint(2, 4)) for _ in range(cnt)) if g is not None]
    else: gs = [(f, load(f)) for f in a]
    for nm, g in gs:
        if g.n > 64: continue
        sts = [fixed] if fixed else [None] + [({v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                                {v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) for _ in range(K)]
        for st in sts:
            try: run(g, st, nm)
            except RecursionError: inc("RECERR")
    print(" ".join(f"{k} {v}" for k, v in sorted(C.items())))
