#!/usr/bin/env python3
"""L-SI box 37 (docs/si/N5-WRET-box37.md): Lemma W-RETURN check, Even side. On a GUIDED STRETCH (consecutive states with tau constant
and every transition an S4a step: sigma_{t+1} = Even's optimum against tau in G restricted to sigma_t ∪ I_sigma_t, or sigma_t if
I_sigma_t = ∅), W_t := val(sigma_t, tau) on G_tau. Lemma W-RETURN: if Even v left w at k -> k+1 and re-enters w at j-1 -> j (inside one
guided stretch) and W(w) did not change on [k+1, j], then W_j(sigma_j v) = W_{j-1}(sigma_{j-1} v): v's SUCCESSOR valuation is
unchanged (the re-entry is W-SILENT). Premise: v is not the cycle node of its own W-valuation at any state of [k+1, j] (re-entries failing it: CYC, excluded;
at its own cycle node S4a's optimum need not be successor-optimal, tog6b_n32 v 13). OPT_V: successor-form optimality failures at
vertices that are not their own W-cycle node (must be 0). VFORM_V counts re-entries where the vertex form W_j(v) = W_{j-1}(v) fails (not claimed).
Counters: WMON_V (W falls somewhere; Lemma W-MON, must be 0), WRET_V (must be 0; --mut drops the "W(w) unchanged" premise and must
fire), REENT (re-entries inside a stretch), WPAID (W(w) rose since the leave), SILENT (W-silent re-entries), maxSW (most switches of
one vertex in one stretch), maxWR (most W-changes of one vertex in one stretch), stretches, longest stretch (transitions).
MODE: n5 (default; the N5 run, optional START file) or fg:TAU (FG(tau) of fg.py from start "best", TAU first|last|sbar0|rand:S;
stall steps end a stretch), or sa:TAU (CONTROL: plain switch-all, W read against the fixed TAU; W-RETURN's S4a premise is
absent, so WRET_V may fire). Usage: wret.py GAME.pg [START] [--mut]   (MODE=fg:first ...)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import load, trace, Engine, dual, readstart
import pg
args = [a for a in sys.argv[1:] if not a.startswith("--")]; MUT = "--mut" in sys.argv
g = load(args[0]); n = g.n; E = Engine(g); MODE = os.environ.get("MODE", "n5")
ev = [v for v in range(n) if g.owner[v] == 0]
def br(sigma, tau):
    val, _ = E.evaluate(tuple(sigma)); imp = E.improving(tuple(sigma), val)
    if not imp: return tuple(sigma), False
    opt = {v: {sigma[v]} for v in ev}
    for v, w in imp: opt[v].add(w)
    succ = [sorted(opt[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)]
    Er = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ)))
    _, best = Er.evaluate(tuple(tau[v] if g.owner[v] == 1 else -1 for v in range(n)))
    return tuple(best[v] if g.owner[v] == 0 else -1 for v in range(n)), True
if MODE == "n5":
    st, _ = trace(g, readstart(args[1]) if len(args) > 1 else None, check=False)
    S = [tuple(s[0]) for s in st]; TAU = [tuple(s[1]) for s in st]
    ok = [S[t + 1] == br(S[t], TAU[t])[0] and TAU[t + 1] == TAU[t] for t in range(len(S) - 1)]
else:
    spec = MODE[3:]; s0 = E.initial("best")
    if spec == "first": tau = tuple(min(g.succ[v]) if g.owner[v] == 1 else -1 for v in range(n))
    elif spec == "last": tau = tuple(max(g.succ[v]) if g.owner[v] == 1 else -1 for v in range(n))
    elif spec == "sbar0": tau = tuple(E.evaluate(s0)[1])
    else: r = random.Random(int(spec[5:])); tau = tuple(r.choice(g.succ[v]) if g.owner[v] == 1 else -1 for v in range(n))
    S = [tuple(s0)]; ok = []
    while len(S) < 20000:
        s2, moved = br(S[-1], tau)
        val, _ = E.evaluate(S[-1]); imp = E.improving(S[-1], val)
        if not imp: break
        if MODE.startswith("sa:"): s2 = tuple(E.rule_switch_all(S[-1], val, imp, None)); ok.append(True)   # control: switch-all, W read vs tau
        elif s2 == S[-1]: s2 = tuple(E.rule_switch_all(S[-1], val, imp, None)); ok.append(False)
        else: ok.append(True)
        S.append(s2)
    TAU = [tau] * len(S)
WE = {}
def W(t):
    tau = TAU[t]
    if tau not in WE:
        WE[tau] = Engine(pg.Game(list(g.prio), list(g.owner), [list(g.succ[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)]))
    e = WE[tau]; return [e.key(x) for x in e.evaluate(S[t])[0]]
stretches = []; a = 0
for t in range(len(ok) + 1):
    if t == len(ok) or not ok[t]:
        if t > a: stretches.append((a, t))         # states a..t, transitions a..t-1 all guided
        a = t + 1
wmon = wret = reent = wpaid = silent = vsil = optv = cyc = maxwrspan = maxwrout = maxsw = maxwr = longest = 0; ex = None
for a, b in stretches:
    Wk = [W(t) for t in range(a, b + 1)]; longest = max(longest, b - a)
    CN = [WE[TAU[t]].evaluate(S[t])[0] for t in range(a, b + 1)]       # W-valuations (cycle node in [0])
    for t in range(a, b):                                               # (OPT) at vertices that are not their own W-cycle node
        imp = E.improving(S[t], E.evaluate(S[t])[0])
        for v, u in imp + [(v, S[t][v]) for v in ev]:
            if CN[t + 1 - a][v][0] != v and Wk[t + 1 - a][u] > Wk[t + 1 - a][S[t + 1][v]]: optv += 1
    for t in range(a, b):
        if any(Wk[t + 1 - a][v] < Wk[t - a][v] for v in range(n)): wmon += 1
    for v in range(n):
        maxwr = max(maxwr, sum(1 for t in range(a, b) if Wk[t + 1 - a][v] != Wk[t - a][v]))
    for v in ev:
        sw = 0; left = {}                             # left[w] = k + 1, the state at which v last left w
        for j in range(a + 1, b + 1):
            if S[j][v] == S[j - 1][v]: continue
            sw += 1; w = S[j][v]; left[S[j - 1][v]] = j
            if w in left:
                k1 = left[w]; reent += 1
                same = all(Wk[t - a][w] == Wk[k1 - a][w] for t in range(k1, j + 1))
                if not same: wpaid += 1
                if any(CN[t - a][v][0] == v for t in range(k1, j + 1)): cyc += 1; continue   # premise: v not its own W-cycle node
                if same or MUT:
                    if Wk[j - a][w] == Wk[j - 1 - a][S[j - 1][v]]: silent += 1     # successor form (the proved statement)
                    else: wret += 1; ex = ex or (v, w, k1, j)
                    if Wk[j - a][v] != Wk[j - 1 - a][v]: vsil += 1                  # vertex form W(v) unchanged: counted only
        maxsw = max(maxsw, sw)
        sws = [j for j in range(a + 1, b + 1) if S[j][v] != S[j - 1][v]]      # window-only W counts per pair (v, w), box 38
        for w in {S[j][v] for j in sws}:
            ent = [j for j in sws if S[j][v] == w]; lv = [j for j in sws if S[j - 1][v] == w]
            outs = set()
            for l in lv:
                nx = [e for e in ent if e > l]
                if nx: outs |= set(range(l, nx[0]))                          # states l..e-1: transitions l -> l+1 .. e-1 -> e
            if lv and ent and max(ent) > lv[0]:
                wsp = sum(1 for t in range(lv[0], max(ent)) if Wk[t + 1 - a][w] != Wk[t - a][w]); maxwrspan = max(maxwrspan, wsp)
            maxwrout = max(maxwrout, sum(1 for t in outs if t + 1 <= b and Wk[t + 1 - a][w] != Wk[t - a][w]))
print(f"WRET {os.path.basename(args[0])} mode {MODE} n {n} iter {len(S) - 1} stretches {len(stretches)} longest {longest} WMON_V {wmon} "
      f"WRET_V {wret} REENT {reent} WPAID {wpaid} SILENT {silent} VFORM_V {vsil} CYC {cyc} OPT_V {optv} maxSW {maxsw} maxWR {maxwr} maxWRspan {maxwrspan} maxWRout {maxwrout} ex {ex} {'PASS' if wmon == wret == optv == 0 else 'FAIL'}")
