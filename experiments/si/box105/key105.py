#!/usr/bin/env python3
"""L-SI box 105: KEY(G*), the one-sided key rule on a FREE genome G* (docs/si/box105-key.md, Definition KEY), simulated directly
(no N5 engine), and its validation against N5 (box190 n5v.py mode spec) from S3 on Gamma3*(G*).
KEY(G*): a state is one option per mover. Step: V(x, k) := the SPEC S1 valuation of the pad m_(x,k) in the STANDARD state of the
current s on Gamma3*(G*) (si.Engine: Even's strategy fixed, Odd's optimal counterstrategy); A(x) := {s(x)} + {k : V(x, k) strictly
better than V(x, s(x))}; s_new(x) := the option of A(x) with the lexicographically least key, key(x, k) := (gate indices of the chain
of W-targets under s_new, lowest level first), computed level by level. The run stops at the first step that changes nothing;
L* := the number of steps before it.
Must-0 counters: keymono (unit (step, mover): the mover's key under the new state is lexicographically larger than under the old
state, or the mover moved and its key did not strictly decrease); valmono (unit (step, vertex of Gamma3*): the valuation decreased).
Validation (unit genomes): s3fail (S3's pair is not the standard state of the start), keyfail (some state 0..L* of the N5 run does
not carry KEY's state at the movers, or the first fallback is not at L* + 1), endfail (fallbacks != 1 or iterations != L* + 3),
wrong (regions != harness Zielonka). CTRL=1 (control): keys read under the OLD state (keyfail must fire).
Usage: key105.py rand SEED COUNT DMAX WMAX DEGMAX     random free genomes (box104 freereach104.rand_free)
       key105.py json FILE.json...                    R104 genomes (gamma3.build's format) with R104's own (E-DOM) priorities: one line each
                                                      (a file whose W-targets are not all one level down is reported as SKIPPED)
(env LNEW, LRED as box104/free104.py; this file imports box104's free104.py and freereach104.py)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.environ.get("BOX104", os.path.join(HERE, "..", "box104")))
import free104 as F
import freereach104 as FR
import n5v, n5, n5x, zielonka
from si import Engine
CTRL = int(os.environ.get("CTRL", "0"))

def standard(G, g, sig, V, s):
    """the standard state's Even strategy vector for the mover state s"""
    st = [(-1 if g.owner[v] == 1 else g.succ[v][0]) for v in range(g.n)]
    for v, w in sig.items(): st[v] = w
    for x in range(G["N"]): st[x] = V[("m", (x, s[x]))]
    return st

def keys_of(G, s_low, x, k, memo):
    wt = G["opts"][x][k][0]
    return (memo[wt] if wt >= 0 else ()) + (G["gate"][x][k],)

def key_run(G, pb, pe, cap=100000):
    """returns (states, counters, game, sig, tau, V)"""
    g, sig, tau, V = F.build_free(G, pb, pe); E = Engine(g); N = G["N"]; opts = G["opts"]
    order = sorted(range(N), key=lambda x: G["lev"][x]); s = list(G["start"]); states = [tuple(s)]; c = dict(keymono=0, valmono=0)
    old = {}
    for x in order: old[x] = keys_of(G, s, x, s[x], old)
    pv = None
    while len(states) <= cap:
        vs, _ = E.evaluate(tuple(standard(G, g, sig, V, s))); kv = [E.key(vs[v]) for v in range(g.n)]
        if pv is not None: c["valmono"] += sum(1 for v in range(g.n) if kv[v] < pv[v])
        pv = kv; new = list(s); memo = {}
        for x in order:
            A = [k for k in range(len(opts[x])) if k == s[x] or kv[V[("m", (x, k))]] > kv[V[("m", (x, s[x]))]]]
            ref = old if CTRL == 1 else memo
            new[x] = min(A, key=lambda k: keys_of(G, new, x, k, ref)); memo[x] = keys_of(G, new, x, new[x], memo)
            c["keymono"] += int(memo[x] > old[x] or (new[x] != s[x] and not memo[x] < old[x]))
        if new == s: break
        s = new; old = memo; states.append(tuple(s))
    return states, c, g, sig, tau, V

def validate(G, pb, pe):
    states, c, g, sig, tau, V = key_run(G, pb, pe); L = len(states) - 1; N = G["N"]
    E, Ed = Engine(g), Engine(n5.dual(g)); inv = {V[("m", (x, k))]: k for x in range(N) for k in range(len(G["opts"][x]))}
    sigma, tau_ = n5x.start_pair(g, E, Ed, None); st0 = standard(G, g, sig, V, list(G["start"]))
    c["s3fail"] = int(any(g.owner[v] == 0 and len(g.succ[v]) > 1 and sigma[v] != st0[v] for v in range(g.n)) or any(tau_[v] != w for v, w in tau.items()))
    its = fbs = 0; F1 = None; bad = 0
    while its < 10 ** 6:
        if F1 is None:
            cur = tuple(inv.get(sigma[x], -1) for x in range(N)); bad += int(its > L or cur != states[min(its, L)])
        r = n5v.step(g, E, Ed, sigma, tau_, "spec")
        if r is None: break
        ns, nt, _, _, fb = r; its += 1; fbs += fb
        if fb and F1 is None: F1 = its
        sigma, tau_ = ns, nt
    c["keyfail"] = int(bad > 0 or F1 != L + 1); c["endfail"] = int(fbs != 1 or its != L + 3)
    vs, _ = E.evaluate(tuple(sigma)); win = [0 if g.prio[vs[v][0]] % 2 == 0 else 1 for v in range(g.n)]
    c["wrong"] = int(win != zielonka.solve(g))
    return c, L, g.n

def edom_prios(G):
    """R104's priorities of the carriers, as box189 gamma3.build sets them"""
    gm, _, _, V = F.gamma3.build(G, F.PADS); O = F.options(G)
    return {q: gm.prio[V[("b", q)]] for q in O}, {q: gm.prio[V[("e", q)]] for q in O}

if __name__ == "__main__":
    if sys.argv[1] == "json":
        import json
        for fn in sys.argv[2:]:
            G = json.load(open(fn))
            if any((wt < 0) != (G["lev"][x] == 0) or (wt >= 0 and G["lev"][wt] != G["lev"][x] - 1) for x in range(G["N"]) for (wt, xt, b) in G["opts"][x]):
                print(f"KEY105 json {os.path.basename(fn)}: SKIPPED, not a genome in R104's sense (some W-target is not one level down), so KEY(G*) is not defined", flush=True); continue
            pb, pe = edom_prios(G); c, L, n = validate(G, pb, pe)
            print(f"KEY105 json {os.path.basename(fn)} (E-DOM priorities) N {G['N']} M {sum(len(o) for o in G['opts'])} |V| {n}: "
                  + " ".join(f"{k} {c[k]}" for k in ("s3fail", "keyfail", "endfail", "wrong", "keymono", "valmono")) + f" | L* {L}", flush=True)
    elif sys.argv[1] == "rand":
        seed, cnt, dmax, wmax, degmax = map(int, sys.argv[2:7]); rng = random.Random(seed); tot = {}; mL = 0; sL = 0; mV = 0
        for _ in range(cnt):
            G, pb, pe = FR.rand_free(rng, dmax, wmax, degmax); c, L, n = validate(G, pb, pe)
            for k, v in c.items(): tot[k] = tot.get(k, 0) + v
            mL = max(mL, L); sL += L; mV = max(mV, n)
        print(f"KEY105 rand seed {seed} genomes {cnt} d<={dmax} w<={wmax} deg<={degmax}" + (f" CTRL {CTRL}" if CTRL else "") + ": "
              + " ".join(f"{k} {tot[k]}" for k in ("s3fail", "keyfail", "endfail", "wrong", "keymono", "valmono")) + f" | max L* {mL} sum L* {sL} max |V| {mV}", flush=True)
