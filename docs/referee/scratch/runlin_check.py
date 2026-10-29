#!/usr/bin/env python3
"""REFEREE succ. 17: dead-end confirmation of CONJECTURE RUN-LIN's kill (L-SI, docs/si/N5-RUNLIN-box24.md §7 at l-si 90bcc50c).
Own engine rl_engine only (no lane code). Per game + start file: states, phases ((lambda_Xi, tau) constant), fallbacks, longest
fallback-free run inside a phase (transitions), I_tau = empty at every state, Q, |D| > 0 states, sigma-bar-changing transitions inside the
longest run and the sigma-bar-constant pieces, per-transition switch sets (WAVE=1 prints them). Final regions (S5) against Oink --zlk and
--tl (pinned build), and an own check that S5's strategies win: sigma on Even's region, sigmabar on Odd's (closed, every cycle of the
right parity). Usage: runlin_check.py game.pg[:start] ...   (env WAVE=1 to print the trace)"""
import sys, os, subprocess, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, core_probe as CP

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../.."))


def oink(path, flag):
    with tempfile.TemporaryDirectory() as d:
        sol = os.path.join(d, "s.sol")
        r = subprocess.run([os.path.join(ROOT, "tools/oink/build/oink"), flag, path, sol], capture_output=True, text=True)
        if r.returncode != 0: return None
        win = {}
        for l in open(sol):
            p = l.strip().rstrip(";").split()
            if len(p) >= 2 and p[0].isdigit(): win[int(p[0])] = int(p[1])
        return win


def wins(g, W, player, strat):
    """player's positional strategy strat (dict on player's vertices of W) wins on W: W closed under opponent moves and
    player's moves, and every cycle of the restricted graph has max priority of player's parity"""
    succ = {v: ([strat[v]] if g.owner[v] == player else list(g.succ[v])) for v in W}
    for v in W:
        if any(w not in W for w in succ[v]): return False, ("leaves", v)
    bad = [v for v in W if g.prio[v] % 2 != player]
    for v in bad:   # a cycle through v using only vertices of priority <= prio(v) would be losing
        p = g.prio[v]; seen = set(); st = [w for w in succ[v] if g.prio[w] <= p]
        while st:
            x = st.pop()
            if x == v: return False, ("cycle", v)
            if x in seen: continue
            seen.add(x); st.extend(w for w in succ[x] if g.prio[w] <= p)
    return True, None


def main(args):
    for a in args:
        path, _, sp = a.partition(":")
        g = RE.parse(path)
        if not sp: sp = path[:-3] + ".start"
        s0 = CP.parse_start(g, sp)
        st = RE.run(g, s0); n = g.n
        Q = [v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) > 1]
        T = len(st) - 1
        lam = [tuple(x["Xi"][v][0] for v in range(n)) for x in st]
        key = [(lam[k], tuple(st[k]["t"])) for k in range(T + 1)]
        phases = []; k = 0
        while k <= T:
            j = k
            while j < T and key[j + 1] == key[k]: j += 1
            phases.append((k, j)); k = j + 1
        fbs = [k for k in range(T) if st[k]["fb"]]
        best = (0, None)
        for (a0, b0) in phases:
            r = a0
            for t in range(a0, b0 + 1):
                if t == b0 or st[t]["fb"]:
                    if t - r > best[0]: best = (t - r, (r, t))
                    r = t + 1
        print("== %s n=%d m=%d states=%d iterations=%d" % (os.path.relpath(path), n, sum(len(s) for s in g.succ), T + 1, T))
        print("Q (Odd choice vertices) =", Q, " succ:", {q: g.succ[q] for q in Q}, " tau0:", {q: s0[1][q] for q in Q})
        print("phases =", phases)
        print("fallbacks =", len(fbs), fbs[:20])
        print("longest fallback-free run in a phase = %d transitions %s ; 2n = %d ; run - 2n = %d" % (best[0], best[1], 2 * n, best[0] - 2 * n))
        print("I_tau empty at every state:", all(not x["It"] for x in st), " I_tau nonempty at states:", [k for k, x in enumerate(st) if x["It"]][:10])
        D = [k for k in range(T + 1) if any(st[k]["sb"][q] != st[k]["t"][q] for q in Q)]
        print("states with D nonempty: %d of %d" % (len(D), T + 1))
        if best[1]:
            r0, r1 = best[1]
            chg = [t for t in range(r0, r1) if any(st[t]["sb"][q] != st[t + 1]["sb"][q] for q in Q)]
            cuts = [r0] + [t + 1 for t in chg] + [r1]
            pieces = [cuts[i + 1] - cuts[i] - (1 if i + 1 < len(cuts) - 1 else 0) for i in range(len(cuts) - 1)]
            print("sigmabar-changing transitions in the run: G = %d at %s" % (len(chg), chg))
            print("sigmabar(Q) along the run:", [(t, tuple(st[t]["sb"][q] for q in Q)) for t in [r0] + [t + 1 for t in chg]])
            print("sigmabar-constant pieces (transitions strictly between sigmabar changes):", pieces)
            if os.environ.get("WAVE"):
                for t in range(r0, r1):
                    sw = [(w, st[t]["s"][w], st[t + 1]["s"][w]) for w in range(n) if g.owner[w] == 0 and st[t]["s"][w] != st[t + 1]["s"][w]]
                    sb = [(q, st[t]["sb"][q], st[t + 1]["sb"][q]) for q in Q if st[t]["sb"][q] != st[t + 1]["sb"][q]]
                    print("  t=%3d switches %s %s" % (t, sw, ("GATE " + str(sb)) if sb else ""))
        fin = st[-1]
        mine = [0 if g.prio[fin["Xi"][v][0]] % 2 == 0 else 1 for v in range(n)]
        for flag in ("--zlk", "--tl"):
            w = oink(path, flag)
            if w is None: print("oink", flag, "FAILED to run"); continue
            print("oink %s regions agree: %s" % (flag, len(w) == n and all(w[v] == mine[v] for v in range(n))))
        W0 = {v for v in range(n) if mine[v] == 0}; W1 = set(range(n)) - W0
        ok0 = wins(g, W0, 0, {v: fin["s"][v] for v in W0 if g.owner[v] == 0})
        ok1 = wins(g, W1, 1, {v: fin["sb"][v] for v in W1 if g.owner[v] == 1})
        print("|W_Even| = %d, |W_Odd| = %d; sigma wins W_Even: %s; sigmabar wins W_Odd: %s" % (len(W0), len(W1), ok0, ok1))


if __name__ == "__main__":
    main(sys.argv[1:])
