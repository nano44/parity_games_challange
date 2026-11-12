#!/usr/bin/env python3
"""L-RED 68 R238: independent replay of L-SI box 105's Lemma KEY-MODEL (claude/l-si 516b6837 docs/si/box105-key.md §2):
«the N5 run from S3 on Gamma3*(G*) has states 0, ..., L* equal to the standard states of s_0, ..., s_(L*) of KEY(G*); its transitions
1, ..., L* are not fallbacks; transition L* + 1 is its only fallback (F* = L* + 1); it makes exactly L* + 3 iterations.»
What is L-RED's own here: the N5 run (n5s237 mode spec, SPEC-exact, L-RED 67), the valuation used by KEY (n5s237.vjproc = SPEC S1 on
the standard state, NOT si.Engine), the KEY simulator (written from §1's Definition KEY(G*) text), the counters and the controls.
What is borrowed (OBJECTS only): the free genome generator freereach104.rand_free and the game builder free104.build_free (box 104,
claude/l-si 26704e01), which also gives the standard state's non-mover part (sig, tau0) and the vertex map V.
Definition KEY(G*) (box105-key.md §1, as implemented): V_s(x, k) := Xi_(sigma_s)(m_(x,k)); A_s(x) := {s(x)} + {k : V_s(x, k) strictly
better than V_s(x, s(x))}; level by level, lowest first: s'(x) := the k in A_s(x) with the least key_(s')(x, k), key_(s')(x, k) :=
key_(s')(wt(x, k), s'(wt(x, k))) + (gate(x, k),), empty below level 0; stop at the first j with s_(j+1) = s_j (L* := j).
Must-0 counters (unit genomes unless said):
 s3fail  S3's pair (n5s237's start) is not the standard state (sigma_(s_0), tau0) at every vertex
 keyfail some state j <= L* of the N5 run is not the standard state of s_j at EVERY Even vertex (movers and the rest) or tau != tau0,
         or a transition j <= L* is a fallback, or the first fallback is not at L* + 1
 endfail fallbacks != 1 or iterations != L* + 3
 wrong   N5's regions != harness Zielonka on Gamma3*(G*)
 keymono (step, mover): key under s_(j+1) larger than under s_j, or the mover moved and its key did not strictly decrease (§3 KEY-MONO*)
Second simulator (sampled, XEVERY): box 105's own key105.key_run (si.Engine valuation) on the same genome: kdiff = genomes whose KEY
state sequences differ from mine.
Controls (CTRL): 1 keys read under the OLD state (box 105's own control); 2 the MOST key instead of the least; 3 A_s(x) with
«better or equal» (non-strict); keyfail must fire for 1-3. CTRL=4 is a NEUTRAL check (must NOT fire): the value of an option read at its
gate instead of its pad (pad -> gate is one step with no P-element, so the order of the options is the same).
Usage: key238.py rand SEED COUNT DMAX WMAX DEGMAX [XRATE]   (XRATE != 0.15: every Xi-target is redrawn, X with probability XRATE)
Env: BOX104 (box 104 dir), LNEW, LRED (as box 104's free104.py), BOX105 (box 105 dir, for the second simulator; optional), CTRL, XEVERY."""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [HERE, os.path.join(HERE, "..", "r237"), os.environ["BOX104"]]
import n5s237 as S
import free104 as F
import freereach104 as FR
import zielonka
CTRL = int(os.environ.get("CTRL", "0")); XEVERY = int(os.environ.get("XEVERY", "0"))
KEYS = ("s3fail", "keyfail", "endfail", "wrong", "keymono")

def prep(g):
    n = g.n; prio = list(g.prio); order = sorted(range(n), key=lambda v: (prio[v], v)); rk = [0] * n
    for r, v in enumerate(order): rk[v] = r
    ev = [p % 2 == 0 for p in prio]; succ = [sorted(set(s)) for s in g.succ]
    return rk, ev, succ, [o == 1 for o in g.owner]

def std(G, sig, V, s):
    st = dict(sig)
    for x in range(G["N"]): st[x] = V[("m", (x, s[x]))]
    return st

def key_run(G, g, sig, V, cap=100000):
    """my KEY(G*) simulator; returns (states, keymono count)"""
    rk, ev, succ, isO = prep(g); O = S.Ord(rk, ev); N = G["N"]; opts = G["opts"]; isE = [not o for o in isO]
    order = sorted(range(N), key=lambda x: (G["lev"][x], x)); s = list(G["start"]); states = [tuple(s)]; km = 0
    def keys(s_):
        kk = {}
        for x in order:
            wt = opts[x][s_[x]][0]; kk[x] = (kk[wt] if wt >= 0 else ()) + (G["gate"][x][s_[x]],)
        return kk
    old = keys(s)
    while len(states) <= cap:
        st = std(G, sig, V, s)
        vs, _ = S.vjproc(g.n, rk, ev, [[st[v]] if isE[v] else succ[v] for v in range(g.n)], isO)
        val = lambda x, k: vs[succ[V[("m", (x, k))]][0]] if CTRL == 4 else vs[V[("m", (x, k))]]
        new = list(s); memo = {}
        for x in order:
            cur = val(x, s[x])
            A = [k for k in range(len(opts[x])) if k == s[x] or O.better(val(x, k), cur) or (CTRL == 3 and not O.better(cur, val(x, k)))]
            ref = old if CTRL == 1 else memo
            kf = lambda k: (ref[opts[x][k][0]] if opts[x][k][0] >= 0 else ()) + (G["gate"][x][k],)
            new[x] = (max if CTRL == 2 else min)(A, key=kf)
            memo[x] = (memo[opts[x][new[x]][0]] if opts[x][new[x]][0] >= 0 else ()) + (G["gate"][x][new[x]],)
            km += int(memo[x] > old[x] or (new[x] != s[x] and not memo[x] < old[x]))
        if new == s: break
        s = new; old = memo; states.append(tuple(s))
    return states, km

def validate(G, pb, pe):
    g, sig, tau, V = F.build_free(G, pb, pe); states, km = key_run(G, g, sig, V); L = len(states) - 1
    tr = []; fbt = []
    its, fbs, win, _, _ = S.run(list(g.prio), list(g.owner), [list(x) for x in g.succ], "spec", trace=tr, fbtrace=fbt)
    c = dict(s3fail=0, keyfail=0, endfail=0, wrong=0, keymono=km)
    s0, t0 = tr[0]; st0 = std(G, sig, V, states[0])
    c["s3fail"] = int(any(s0[v] != w for v, w in st0.items()) or any(t0[v] != w for v, w in tau.items()))
    bad = 0
    for j in range(L + 1):
        if j >= len(tr): bad += 1; break
        sj, tj = tr[j]; stj = std(G, sig, V, states[j])
        bad += int(any(sj[v] != w for v, w in stj.items()) or any(tj[v] != w for v, w in tau.items()))
    F1 = fbt[0] if fbt else None
    c["keyfail"] = int(bad > 0 or F1 != L + 1); c["endfail"] = int(fbs != 1 or its != L + 3)
    c["wrong"] = int([0 if w else 1 for w in win] != zielonka.solve(g))
    return c, L, g.n, states, its, F1, fbs

def second(G, pb, pe):
    sys.path.insert(0, os.environ["BOX105"]); import key105
    st, _, _, _, _, _ = key105.key_run(G, pb, pe); return st

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "rand":
        seed, cnt, dmax, wmax, degmax = map(int, sys.argv[2:7]); xr = float(sys.argv[7]) if len(sys.argv) > 7 else 0.15
        rng = random.Random(seed); tot = {k: 0 for k in KEYS}; mL = sL = mV = 0; x = kd = 0; t0 = time.time(); ex = []
        for i in range(cnt):
            G, pb, pe = FR.rand_free(rng, dmax, wmax, degmax)
            if xr != 0.15:
                for xx in range(G["N"]):
                    for o in G["opts"][xx]: o[1] = -1 if rng.random() < xr else rng.randrange(G["N"])
            c, L, n, states, its, F1, fbs = validate(G, pb, pe)
            for k in KEYS: tot[k] += c[k]
            if sum(c.values()) and len(ex) < 3: ex.append((i, c, L, its, F1, fbs))
            mL = max(mL, L); sL += L; mV = max(mV, n)
            if XEVERY and i % XEVERY == 0 and not CTRL:
                x += 1; kd += int(tuple(second(G, pb, pe)) != tuple(states))
        print(f"KEY238 rand seed {seed} genomes {cnt} d<={dmax} w<={wmax} deg<={degmax} xrate {xr}" + (f" CTRL {CTRL}" if CTRL else "") + ": "
              + " ".join(f"{k} {tot[k]}" for k in KEYS) + f" | max L* {mL} sum L* {sL} max |V| {mV} | second simulator (key105): sampled {x} kdiff {kd}"
              + f" | {time.time() - t0:.0f} s" + (f" | first nonzero: {ex}" if ex else ""), flush=True)
