#!/usr/bin/env python3
"""REFEREE climb for P-N5-L2 thin spots (own code; one Odd choice vertex asserted on every candidate).
FIT=frz : max over phases of (longest run of consecutive H3 states that contains a not-H1 state, or is followed in the phase by a
          not-H1 H3 state) - n.  >= 0 means a FREEZE' window with new content (§4); l2_probe's FRZ checks then run on it.
FIT=tog : max over fallback-free runs of t_Q (H1 toggles inside the SN prefix) (§7, §8 DROP-LEN context).
FIT=h2s : number of in-phase S4a steps with H1 and not H2 and tau(o) != o (§2 thin spot: non-self-loop cases).
Usage: l2_climb.py FIT seed minutes nmin nmax [start.pg]"""
import sys, os, random, time
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u1_probe as U, l2_probe as L


def fit(g, mode):
    E, o, st, it, fb = L.states(g); n = g.n; T = len(st) - 1
    inph = [st[k]["key"] == st[k + 1]["key"] for k in range(T)]
    if mode == "h2s":
        return sum(1 for k in range(T) if inph[k] and not st[k]["fb"] and st[k]["H1"] and not st[k]["H2"] and st[k]["t"][o] != o)
    best = -10 ** 6; k = 0
    while k < T:
        if not inph[k]: k += 1; continue
        j = k
        while j + 1 < T and inph[j + 1]: j += 1
        Ps = list(range(k, j + 2)); k = j + 1
        if mode == "frz":
            late = [t for t in Ps if st[t]["H3"] and not st[t]["H1"]]
            run_ = 0
            if not late:  # plateau: keep long H3 runs while waiting for a not-H1 H3 state in the same phase
                for t in Ps:
                    run_ = run_ + 1 if st[t]["H3"] else 0; best = max(best, run_ - n - 1000)
                continue
            for t in Ps:
                run_ = run_ + 1 if st[t]["H3"] else 0
                if run_ and any(x >= t - run_ + 1 for x in late): best = max(best, run_ - n)
        else:
            q = Ps[0]
            while q < Ps[-1]:
                if st[q]["fb"]: q += 1; continue
                e = q
                while e + 1 < Ps[-1] and not st[e + 1]["fb"]: e += 1
                Q = list(range(q, e + 2)); q = e + 1; cth = st[Q[0]]["Xi"][o][0]; P = []
                for t in Q:
                    if st[t]["W"][o][0] == cth: P.append(t)
                    else: break
                best = max(best, sum(st[t]["H1"] != st[t + 1]["H1"] for t in P[:-1]))
    return best


def mutate(g, rng):
    n = g.n; prio, owner, succ = list(g.prio), list(g.owner), [list(s) for s in g.succ]
    o = U.assert_c1o(g); r = rng.random(); v = rng.randrange(n)
    if r < 0.3: prio[v] = rng.randrange(n + 3)
    elif r < 0.85:
        if owner[v] == 1 and v != o: succ[v] = [rng.randrange(n)]
        else:
            s = set(succ[v])
            if len(s) > (2 if v == o else 1) and rng.random() < 0.5: s.discard(rng.choice(sorted(s)))
            else: s.add(rng.randrange(n))
            succ[v] = sorted(s)
    else:
        if v != o: owner[v] = 1 - owner[v]; succ[v] = succ[v][:1] if owner[v] == 1 else succ[v]
    h = U.pg.Game(prio, owner, succ)
    if sum(1 for x in range(n) if h.owner[x] == 1 and len(set(h.succ[x])) > 1) != 1: return None
    return h


def save(g, path):
    with open(path, "w") as f:
        f.write("parity %d;\n" % (g.n - 1))
        for v in range(g.n): f.write("%d %d %d %s;\n" % (v, g.prio[v], g.owner[v], ",".join(map(str, g.succ[v]))))


if __name__ == "__main__":
    mode, seed, mins, lo, hi = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    rng = random.Random(seed); t0 = time.time(); bestf = -10 ** 6; out = os.environ.get("OUT", "."); hits = 0; steps = 0; cnt = Counter()
    while time.time() - t0 < 60 * mins:
        if len(sys.argv) > 6: g = U.load(sys.argv[6])
        else:
            g = None
            while g is None: g = U.rand_c1o(rng, lo, hi)
        f = fit(g, mode); stall = 0
        while stall < 3000 and time.time() - t0 < 60 * mins:
            h = mutate(g, rng); steps += 1
            if h is None: continue
            try: fh = fit(h, mode)
            except AssertionError: continue
            if fh >= f:
                stall = 0 if fh > f else stall + 1; g, f = h, fh; bestf = max(bestf, f)
                if mode == "frz" and f >= 0 or mode != "frz" and f > cnt["best"]:
                    c = Counter(); L.run(g, c, "climb"); hits += 1
                    fails = {k: v for k, v in c.items() if "FAIL" in k}
                    cnt["best"] = max(cnt["best"], f)
                    for k in ("FRZ_windows_nH1", "FRZb_chk_H3notH2", "FRZ_windows"): cnt[k] += c[k]
                    if fails or (mode == "frz" and c["FRZ_windows_nH1"] + c["FRZb_chk_H3notH2"] > 0 and hits <= 20) or mode != "frz":
                        p = os.path.join(out, "l2c_%s_s%d_%d_n%d.pg" % (mode, seed, hits, g.n)); save(g, p)
                        print("HIT", mode, "fit", f, p, fails, {k: c[k] for k in ("FRZ_windows_nH1", "FRZb_chk_H3notH2", "max_tQ")}, flush=True)
                    if mode == "frz": break
            else: stall += 1
    print("END", mode, "seed", seed, "bestfit", bestf, "steps", steps, "hits", hits, dict(cnt), flush=True)
