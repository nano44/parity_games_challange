#!/usr/bin/env python3
"""P-TOWER-FUEL check block (L-LOWER successor 5; docs/lower/P-TOWER-FUEL.md). Python only, deterministic, run by
experiments/lower/check.sh. Simulator: l3/sim.py (R104 definition; own implementation, cross-checked in the packet's DATA section).
(1) pins: sha1 of the two instance genomes and of the line file L-1;
(2) the instance counts of §4 (G7_best_d28: room; SL41_d28: fuel), asserted exactly;
(3) lemma counters of §5 on the corpus (l3/kill/*.json, l4/rec/*.json, the two instances): violations must be 0; tightness and
    hypothesis counters are printed (and asserted) as stated in the packet.
Prints «P-TOWER-FUEL CHECK PASS» at the end."""
import sys, os, json, hashlib, glob
H = os.path.dirname(os.path.abspath(__file__)); L = os.path.join(H, '..')
sys.path.insert(0, os.path.join(L, 'l3'))
from sim import run, val
from trace import keys
from txt2json import tojson

def sha(p): return hashlib.sha1(open(p, 'rb').read()).hexdigest()
def rdtxt(p):
    D = {}
    for ln in open(p):
        w = ln.split()
        if w and w[0] == 'd': D['d'] = int(w[1])
        if w and w[0] in ('xt', 'br', 'bp', 'gate', 'start'): D[w[0]] = list(map(int, w[1:]))
    return tojson(D)

G7 = os.path.join(L, 'l4', 'rec', 'G7_best_d28.txt'); SL = os.path.join(H, 'rec', 'SL41_d28.txt')
LINE = os.path.join(L, '..', '..', 'docs', 'lower', 'P-TOWER-FUEL-line-L1.txt')
PINS = {G7: "b995fff21c1f8558eb3e1868ec5ce59a3d4ccfb3", SL: "c1b46c319fd614e5bcb0909b616a9f2833e0dfee"}
if os.environ.get("PTF_LINE_SHA"): PINS[LINE] = os.environ["PTF_LINE_SHA"]
LINE_SHA = "408470adbb1d80f0ed4f29b363867da3d6d430d4"
if LINE_SHA != "LINE_SHA_PLACEHOLDER": PINS[LINE] = LINE_SHA
for p, h in PINS.items(): assert sha(p) == h, (p, sha(p), h)
print("pins OK:", len(PINS), "files")

class Run:
    def __init__(s, G):
        s.G = G; s.N = G['N']; s.d = s.N // 2; s.S = run(G, G['start']); s.T = len(s.S) - 1
        s.O = [[0 if k[2*l] < k[2*l+1] else 1 for l in range(s.d)] for k in (keys(G, x) for x in s.S)]
        s.F = [sum(s.O[t][l] != s.O[t-1][l] for t in range(1, s.T + 1)) for l in range(s.d)]
        s.dbl = [l >= 1 and s.F[l] == 2 * s.F[l-1] + 2 for l in range(s.d)]
    def windows(s, j):
        """j-windows: maximal runs of consecutive steps with no j-b-step (flip of pair j-1) except possibly the first."""
        b = [t for t in range(1, s.T + 1) if s.O[t][j-1] != s.O[t-1][j-1]]; cuts = [1] + [t for t in b if t > 1] + [s.T + 1]
        out = []
        for a, e in zip(cuts, cuts[1:]):
            mv = [(t, x) for t in range(a, e) for x in (2*j, 2*j+1) if s.S[t][x] != s.S[t-1][x]]
            typ = tuple((x, s.S[a][x]) for x in (2*j-2, 2*j-1) if a > 1 and s.S[a][x] != s.S[a-1][x])
            out.append((a, e - 1, typ, mv))
        return out
    def chain(s, st, x, k):
        out = []
        while True:
            wt, xt, m = s.G['opts'][x][k]; out.append(m)
            if xt < 0: return out
            x, k = xt, st[xt]
    def dec(s, st, x):
        """the deciding element: the beta (option index m) of largest rank in the symmetric difference of x's two chains, and its side"""
        a = set(s.chain(st, x, 0)); b = set(s.chain(st, x, 1)); m = max(a ^ b, key=lambda m: s.G['br'][m])
        return m, (0 if m in a else 1)
    def pi(s, st, x): return 0 if val(s.G, st, x, 0) > val(s.G, st, x, 1) else 1   # the option of larger Xi-value (R116's pi)

# (2) instances
def slack(R, j, need):
    W = R.windows(j); pu = gp = 0; per = {}
    for i, (a, e, typ, mv) in enumerate(W):
        assert len(mv) == 2, "doubling level expected"
        p = mv[1][0] - mv[0][0] < need; g = i + 1 < len(W) and W[i+1][3][0][0] - mv[1][0] < need
        pu += p; gp += g; per.setdefault(typ, [0, 0]); per[typ][0] += p; per[typ][1] += g
    return pu, gp, per
R7 = Run(rdtxt(G7)); RS = Run(rdtxt(SL))
assert R7.T == 270 and R7.F[:8] == [2, 6, 14, 30, 62, 126, 222, 158], (R7.T, R7.F[:8])
assert RS.T == 290 and RS.F[:8] == [2, 6, 14, 30, 62, 126, 222, 158], (RS.T, RS.F[:8])
for R in (R7, RS): assert all(R.dbl[1:6]) and R.F[0] == 2 and not R.dbl[6]
c7 = {j: slack(R7, j, 7 - j)[:2] for j in range(1, 6)}; cs = {j: slack(RS, j, 7 - j)[:2] for j in range(1, 6)}
assert c7 == {1: (0, 0), 2: (0, 0), 3: (0, 0), 4: (0, 0), 5: (16, 14)}, c7
per = slack(R7, 5, 2)[2]; assert per[((9, 1),)] == [15, 14] and per[()] == [1, 0] and sum(v[0] + v[1] for k, v in per.items() if k not in (((9, 1),), ())) == 0, per
assert cs == {j: (0, 0) for j in range(1, 6)}, cs
print("G7_best_d28: T 270, levels 0-5 capped; 7-capped PULSE/GAP violations: levels 1-4: 0; level 5: 30 = 15 pulses + 14 gaps of type (9, 1) + 1 pulse of the first window")
print("SL41_d28: T 290, levels 0-5 capped; 7-capped PULSE/GAP violations at levels 1-5: 0")
def fail6(R):
    W = R.windows(6); bad = [w for w in W if len(w[3]) != 2]; return W, bad
for R, name in ((R7, "G7_best_d28"), (RS, "SL41_d28")):
    W, bad = fail6(R); assert len(W) == 127 and len(bad) == 48, (name, len(W), len(bad))
print("both: level 6 has 127 windows, 48 without exactly one move of each member of pair 6")
W, bad = fail6(RS); badset = {w[0] for w in bad}; dec_fail = dec_good = 0
for a, e, typ, mv in W:
    ds = {RS.dec(RS.S[t], x) for t in range(a - 1, e) for x in (12, 13)}
    has = any(m == 19 for m, _ in ds)                     # option 19 = (mover 9, option 1), rank 87
    if a in badset: dec_fail += has
    else: dec_good += has
assert RS.G['br'][19] == 87 and RS.G['bp'][19] == 1 and RS.G['opts'][12][0][1] == 22 and RS.G['opts'][12][1][1] == 11 and RS.G['opts'][13][0][1] == 11 and RS.G['opts'][13][1][1] == 22
assert dec_fail == 48 and dec_good == 0, (dec_fail, dec_good)
print("SL41_d28: pair 6 is CROSS onto (22, 11); (rank 87, mover 9, option 1) decides 12 or 13 in all 48 failing 6-windows and in none of the 79 others")

# (3) lemma counters on the corpus
files = sorted(glob.glob(os.path.join(L, 'l3', 'kill', '*.json')) + glob.glob(os.path.join(L, 'l4', 'rec', '*.json')))
runs = [(os.path.basename(f), Run(json.load(open(f)))) for f in files] + [("G7_best_d28", R7), ("SL41_d28", RS)]
C = dict(levels=0, E3=0, E4=0, E5=0, windows=0, PN_units=0, PN_viol=0, PN_tight=0, GN_units=0, GN_viol=0, GN_tight=0,
         DF_pairs=0, DF_viol=0, DFa_pairs=0, DFa_viol=0, CE_pairs=0, CE_windows=0, CE_viol=0, CE3_units=0, CE3_viol=0)
for name, R in runs:
    # DOMINANCE-FREEZE (a): consecutive states with the same decider (element and side) have the same preference, every mover
    for t in range(1, R.T + 1):
        for x in range(R.N):
            if R.dec(R.S[t-1], x) == R.dec(R.S[t], x):
                C['DFa_pairs'] += 1; C['DFa_viol'] += R.pi(R.S[t-1], x) != R.pi(R.S[t], x)
    for j in range(1, R.d):
        if not R.dbl[j]: continue
        C['levels'] += 1; W = R.windows(j); p, q = 2*j, 2*j+1
        # DOUBLE-EQ' (E3): flips of pair j exactly at the steps moving p or q, never both; (E4): one move each per window
        for t in range(1, R.T + 1):
            mp, mq = R.S[t][p] != R.S[t-1][p], R.S[t][q] != R.S[t-1][q]
            C['E3'] += (mp and mq) or ((mp or mq) != (R.O[t][j] != R.O[t-1][j]))
        firsts = set()
        for a, e, typ, mv in W:
            C['windows'] += 1; C['E4'] += sorted(x for _, x in mv) != [p, q] or len({t for t, _ in mv}) != 2
            if len(mv) == 2: firsts.add(min(mv)[1])
        C['E5'] += R.F[j-1] >= 1 and len(firsts) > 1
        # PULSE-NEST / GAP-NEST with k = the number of further doubling levels above j
        k = 0
        while j + k + 1 < R.d and R.dbl[j + k + 1]: k += 1
        for i, (a, e, typ, mv) in enumerate(W):
            if len(mv) != 2: continue
            pu = mv[1][0] - mv[0][0]; C['PN_units'] += 1; C['PN_viol'] += pu < k + 1; C['PN_tight'] += pu == k + 1
            if k >= 1 and i + 1 < len(W) and len(W[i+1][3]) == 2:
                g = W[i+1][3][0][0] - mv[1][0]; C['GN_units'] += 1; C['GN_viol'] += g < k + 1; C['GN_tight'] += g == k + 1
        # DOMINANCE-FREEZE (b): between consecutive moves t < t' of a member, the decider is not constant on s_(t-1) .. s_(t'-1)
        for x in (p, q):
            ts = [t for t in range(1, R.T + 1) if R.S[t][x] != R.S[t-1][x]]
            for t, t2 in zip(ts, ts[1:]):
                C['DF_pairs'] += 1; C['DF_viol'] += len({R.dec(R.S[v], x) for v in range(t - 1, t2)}) == 1
        # CROSS-ECONOMY: pair j CROSS onto movers A_0 = xt(p,0) = xt(q,1), A_1 = xt(p,1) = xt(q,0) outside pair j; D = cv(A_0) - cv(A_1);
        # (ii) [D(s_(u1-1)) > th_f] != [D(s_(u2-1)) > th_x2] (exact); (iii) RANK hypothesis at both states => sign D changes in the pulse
        xp, xq = [o[1] for o in R.G['opts'][p]], [o[1] for o in R.G['opts'][q]]
        if xp[0] == xq[1] and xp[1] == xq[0] and xp[0] != xp[1] and min(xp) >= 0 and not set(xp) & {p, q}:
            C['CE_pairs'] += 1; A0, A1 = xp
            eps = lambda x, k: (1 if R.G['bp'][R.G['opts'][x][k][2]] == 0 else -1) << R.G['br'][R.G['opts'][x][k][2]]
            th = {p: eps(p, 1) - eps(p, 0), q: eps(q, 0) - eps(q, 1)}
            own = max(R.G['br'][R.G['opts'][x][k][2]] for x in (p, q) for k in (0, 1))
            def D(st): return val(R.G, st, A0, st[A0]) - val(R.G, st, A1, st[A1])
            def rankhyp(st):
                a = set(R.chain(st, A0, st[A0])); b = set(R.chain(st, A1, st[A1])); sd = a ^ b
                return bool(sd) and max(R.G['br'][m] for m in sd) > own
            for a, e, typ, mv in W:
                if len(mv) != 2: continue
                (u1, f), (u2, x2) = mv; C['CE_windows'] += 1
                C['CE_viol'] += (D(R.S[u1-1]) > th[f]) == (D(R.S[u2-1]) > th[x2])
                if rankhyp(R.S[u1-1]) and rankhyp(R.S[u2-1]):
                    C['CE3_units'] += 1; C['CE3_viol'] += (D(R.S[u1-1]) > 0) == (D(R.S[u2-1]) > 0)
print("corpus:", len(runs), "runs (stored start):", ', '.join(n for n, _ in runs))
print("counters:", C)
for v in ('E3', 'E4', 'E5', 'PN_viol', 'GN_viol', 'DF_viol', 'DFa_viol', 'CE_viol', 'CE3_viol'): assert C[v] == 0, (v, C[v])
EXP = {'levels': 62, 'E3': 0, 'E4': 0, 'E5': 0, 'windows': 757, 'PN_units': 757, 'PN_viol': 0, 'PN_tight': 215, 'GN_units': 260, 'GN_viol': 0,
       'GN_tight': 12, 'DF_pairs': 1390, 'DF_viol': 0, 'DFa_pairs': 65885, 'DFa_viol': 0, 'CE_pairs': 4, 'CE_windows': 65, 'CE_viol': 0,
       'CE3_units': 43, 'CE3_viol': 0}
assert C == EXP, C
print("P-TOWER-FUEL CHECK PASS")
