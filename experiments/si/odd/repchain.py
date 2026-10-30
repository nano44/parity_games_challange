#!/usr/bin/env python3
"""L-SI box 44 (docs/si/N5-REPCH-box44.md): cause chains of REPEAT late adoptions inside W-runs (plain N5, S3 start or START file).
W-runs, BLOCKED and late adoptions as in L-NEW's box64/late.py (W-run: tau constant, no S4c fallback, lambda_W constant; (y, z) BLOCKED at
state t: W_t(z) > W_t(sigma_t y) and (y, z) not in I_sigma_t; a late adoption: sigma(y) becomes z at a transition of the W-run after (y, z)
was blocked at an earlier state of it). For a REPEAT late adoption of (y, z) at u (an earlier late adoption of (y, z) in the same W-run,
y's last leave of z at k -> k+1): t* := the last transition t in [k+1, u] with W_{t+1}(z) != W_t(z) (none: SILENT). CAUSES: the Even x on
the (sigma_{t*+1}, tau)-play from z (z included) with sigma_{t*+1}(x) != sigma_{t*}(x). PARENT: a REPEAT late adoption among the causes if
any, else a FIRST one ("F"), else a plain switch ("S"). DEPTH: 1 + DEPTH(parent) for a REPEAT parent, else 1. LDEC: the parent switch x
has W-length l(x) < l(z) at t*+1 (l = steps to the cycle node); LDEC_V counts parents with l(x) >= l(z). Counters: rep, silent, parF,
parR, parS, maxdepth, LDEC_V; PLAINW = the largest number, over W-runs, of W-changing transitions at which no late
adoption happens (the "plain-wave" lemma would say <= n - 1); PLAINV = the same per vertex (most W-changes of one vertex at plain transitions in one W-run). Box 46 (LOCAL): per W-run, WCH (W-changing
transitions), RT (transitions with a late adoption), RLOC (transitions with a LOCAL late adoption: the edge was blocked at some state
>= u - n + 1 of the W-run, u the adoption transition), REPW (REPEATs in the W-run); maxima over W-runs: WCHW, RTW, RLOCW, REPW;
LOC_V counts W-runs with WCH > (n - 1)(RLOC + 1) (Corollary LOC-R*, must be 0). Box 48 (WINDOW): the WINDOW of a transition t is
[the last transition <= t of the W-run that contains a late adoption, t] (INIT if none). For each REPEAT with enabling W-rise at t*, WIN0 /
WINF / WINR count windows of t* opened by INIT / a transition with FIRST late adoptions only / a transition with a REPEAT; PERWIN = the most
REPEATs charged to one window; WINCH_V counts windows with more than n - 1 W-changing transitions (GP*-SUB: must be 0). WDEPTH: 1 + the WDEPTH of the REPEATs
opening the window of t* (0 for INIT / FIRST windows); MAXWD its maximum. SELF: REPEATs whose only W(z)-change after the leave is at the adoption transition itself (excluded from the
chain; t* is taken < u). Usage: repchain.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
args = sys.argv[1:]; g = load(args[0]); n = g.n
E, Ed = Engine(g), Engine(dual(g))
s, t = start_pair(g, E, Ed, readstart(args[1]) if len(args) > 1 else None); s, t = tuple(s), tuple(t)
WE = {}
def W(s, t):
    if t not in WE: WE[t] = Engine(pg.Game(list(g.prio), list(g.owner), [[t[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(n)]))
    e = WE[t]; w = e.evaluate(s)[0]; return w, [e.key(x) for x in w]
ev = [v for v in range(n) if g.owner[v] == 0]
def blocked(s, t, wk):
    vx, _ = E.evaluate(s); Is = set(E.improving(s, vx))
    return {(v, x) for v in ev for x in g.succ[v] if x != s[v] and wk[x] > wk[s[v]] and (v, x) not in Is}
def play(s, t, z):
    seen, out, x = set(), [], z
    while x not in seen: seen.add(x); out.append(x); x = s[x] if g.owner[x] == 0 else t[x]
    return out
c = dict(rep=0, silent=0, parF=0, parR=0, parS=0, maxdepth=0, LDEC_V=0, late=0, PLAINW=0, PLAINV=0, WCHW=0, RTW=0, RLOCW=0, REPW=0, LOC_V=0, WIN0=0, WINF=0, WINR=0, PERWIN=0, WINCH_V=0, MAXWD=0, SELF=0)
# W-run state
def reset(s, t):
    w, wk = W(s, t); return dict(S=[s], WV=[w], WK=[wk], bl=set(blocked(s, t, wk)), late={}, adopt={}, leave={}, pw=0, pv=[0] * n, win=[], wch=0, rt=0, rloc=0, rep=0, bt={}, lastlate=None, lkind={}, wcount={}, wwch={}, lwd={})
R = reset(s, t)
for e in R['bl']: R['bt'][e] = 0
def close(R):
    c['WCHW'] = max(c['WCHW'], R['wch']); c['RTW'] = max(c['RTW'], R['rt']); c['RLOCW'] = max(c['RLOCW'], R['rloc']); c['REPW'] = max(c['REPW'], R['rep'])
    if R['wch'] > (n - 1) * (R['rloc'] + 1): c['LOC_V'] += 1
while True:
    r = step(g, E, Ed, list(s), list(t))
    if r is None: break
    ns, nt, _, _, fb, _, _ = r; ns, nt = tuple(ns), tuple(nt)
    w2, wk2 = W(ns, t)
    if nt != t or ns == s or fb or any(w2[x][0] != R["WV"][-1][x][0] for x in range(n)):
        close(R); s, t = ns, nt; R = reset(s, t)
        for e in R['bl']: R['bt'][e] = 0
        continue
    u = len(R["S"]) - 1                                         # transition u -> u+1 inside the W-run (local indices)
    anylate = anyloc = False
    for y in ev:
        if ns[y] == s[y]: continue
        R["leave"][(y, s[y])] = u
        z = ns[y]
        if (y, z) in R["bl"]:
            c["late"] += 1; k = R["adopt"].get((y, z), 0); anylate = True
            if R['bt'][(y, z)] >= u - n + 1: anyloc = True
            if k: R['rep'] += 1
            rec = dict(kind="F" if k == 0 else "R", depth=1)
            if k:
                c["rep"] += 1; kl = R["leave"].get((y, z))
                WK = R["WK"] + [wk2]
                ts0 = [x for x in range(kl + 1, u + 1) if WK[x + 1][z] != WK[x][z]]
                ts = [x for x in ts0 if x < u]                         # box 48: the enabling rise strictly before the adoption transition
                if not ts0: c["silent"] += 1
                elif not ts: c["SELF"] += 1
                else:
                    tt = ts[-1]; wid = R['win'][tt] if tt < len(R['win']) else R['lastlate']
                    kd = 'I' if wid is None else R['lkind'][wid]
                    c['WIN0' if kd == 'I' else ('WINR' if kd == 'R' else 'WINF')] += 1
                    rec['wd'] = 1 + (R['lwd'].get(wid, 0) if wid is not None else 0); c['MAXWD'] = max(c['MAXWD'], rec['wd'])
                    R['wcount'][wid] = R['wcount'].get(wid, 0) + 1; c['PERWIN'] = max(c['PERWIN'], R['wcount'][wid])
                    S1 = R["S"][tt + 1] if tt + 1 < len(R["S"]) else ns; S0 = R["S"][tt]
                    causes = [x for x in play(S1, t, z) if g.owner[x] == 0 and S1[x] != S0[x]]
                    recs = [R["late"].get((tt, x)) for x in causes]
                    pr = [(x, q) for x, q in zip(causes, recs) if q and q["kind"] == "R"]
                    pf = [(x, q) for x, q in zip(causes, recs) if q and q["kind"] == "F"]
                    WV1 = R["WV"][tt + 1] if tt + 1 < len(R["WV"]) else w2
                    if pr: c["parR"] += 1; x, q = max(pr, key=lambda e: e[1]["depth"]); rec["depth"] = 1 + q["depth"]
                    elif pf: c["parF"] += 1; x = pf[0][0]
                    else: c["parS"] += 1; x = causes[0] if causes else None
                    if x is not None and not WV1[x][2] < WV1[z][2]: c["LDEC_V"] += 1
                c["maxdepth"] = max(c["maxdepth"], rec["depth"])
            R["adopt"][(y, z)] = k + 1; R["late"][(u, y)] = rec
    if not any((u, y) in R["late"] for y in ev):
        ch = [x for x in range(n) if wk2[x] != R["WK"][-1][x]]
        if ch:
            R["pw"] += 1; c["PLAINW"] = max(c["PLAINW"], R["pw"])
            for x in ch: R["pv"][x] += 1; c["PLAINV"] = max(c["PLAINV"], R["pv"][x])
    if anylate:
        R['lwd'][u] = max([R['late'][(u, y)].get('wd', 0) for y in ev if (u, y) in R['late']] + [0])
        R['lastlate'] = u; R['lkind'][u] = 'R' if any(R['late'].get((u, y), {}).get('kind') == 'R' for y in ev) else 'F'
    R['win'].append(R['lastlate'])
    if wk2 != R['WK'][-1]:
        R['wwch'][R['lastlate']] = R['wwch'].get(R['lastlate'], 0) + 1
        if R['wwch'][R['lastlate']] > n - 1: c['WINCH_V'] += 1
    R['rt'] += anylate; R['rloc'] += anyloc; R['wch'] += wk2 != R['WK'][-1]
    nb = blocked(ns, t, wk2)
    for e in nb: R['bt'][e] = u + 1
    R["S"].append(ns); R["WV"].append(w2); R["WK"].append(wk2); R["bl"] |= nb; s = ns
close(R)
print(f"REPCH {os.path.basename(args[0])} n {n} " + " ".join(f"{k} {v}" for k, v in c.items()))
