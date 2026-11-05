#!/usr/bin/env python3
"""L-SI box 65: per-flip gain and flip footprint in the external-flip model E_m (L-NEW box 160/161; BIT-CHAIN of box 64).
For a genome G (box 150 JSON, ISO R197 ladder), a state s of levels >= 1 and a bit b:
  L_b(s)      = length of the flip-free run of H_b from s;   M(s) = max_b L_b(s);
  g(s, b)     = max over t in [0, L_b(s)] of (t + L_(1-b)(s_t)) - M(s), s_t the b-run from s (one flip at time t, then never again);
  j(s)        = flip footprint = least l in 1..m with s(A_l) = s(B_l) (m if none): a flip at s inverts the key-preferred option at
                levels 1..j exactly (box 64 BIT-CHAIN corollary).
Lemma GAIN-IND (docs/si/N5-FOOT-box65.md §1): T_k(G) <= T_0(G) + k * g*(G), g*(G) = max over s, b of g(s, b); checked here (IND).
Per genome, prints g*(G), the largest gain per footprint j (over the maximising flip times), the largest gain of a flip at time t
over flip states of footprint j: GJ[j] = max over s, b, t with j(s_t) = j of (t + L_(1-b)(s_t) - M(s)), and T_k for k <= K.
Usage: gain.py genome.json ...  |  gain.py --random m count seed  |  gain.py --climb m seed iters out (maximise g*)"""
import sys, os, json, itertools, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box64"))
from flipdp import Ext, analyse

def foot(E, u):
    m = max(E.lev); st = E.full(u, 0)
    for l in range(1, m + 1):
        if st[2 * l] == st[2 * l + 1]: return l
    return m

def gains(G, K=4, check=True):
    E = Ext(G); m = max(E.lev)
    states = list(itertools.product(*[range(len(E.opts[v])) for v in E.UP]))
    nxt = {(u, b): E.step(u, b) for u in states for b in (0, 1)}
    L = {}
    def run(u, b):
        if (u, b) in L: return L[(u, b)]
        seq = [u]
        while True:
            w = nxt[(seq[-1], b)]
            if w == seq[-1]: break
            seq.append(w)
        L[(u, b)] = len(seq) - 1, seq; return L[(u, b)]
    gstar = -1; GJ = {}; arg = None
    for u in states:
        Mu = max(run(u, 0)[0], run(u, 1)[0])
        for b in (0, 1):
            n, seq = run(u, b)
            for t, st in enumerate(seq):
                val = t + run(st, 1 - b)[0] - Mu; j = foot(E, st)
                GJ[j] = max(GJ.get(j, -99), val)
                if val > gstar: gstar = val; arg = (list(u), b, t, j)
    res = {"m": m, "g": gstar, "GJ": dict(sorted(GJ.items())), "arg": arg}
    if check:
        r = analyse(G, K, check=False); res["T"] = r["T"]
        res["IND"] = sum(1 for k in range(K + 1) if r["T"][k] > r["T"][0] + k * gstar)
    return res

if __name__ == "__main__":
    a = sys.argv[1:]; bad = 0
    if a[0] == "--random" or a[0] == "--climb":
        sys.path.insert(0, os.path.join(HERE, "..", "box64")); from climb import rand_iso, mutate
    if a[0] == "--random":
        m, cnt, seed = int(a[1]), int(a[2]), int(a[3]); rng = random.Random(seed); agg = {}; gmax = -1; done = 0
        while done < cnt:
            G = rand_iso(m + 1, rng)
            try: r = gains(G, K=3)
            except AssertionError: continue
            done += 1; bad += r["IND"]; gmax = max(gmax, r["g"])
            for j, v in r["GJ"].items(): agg[j] = max(agg.get(j, -99), v)
        print("random m", m, "genomes", cnt, "g* max", gmax, "GJ", dict(sorted(agg.items())), "IND", bad)
    elif a[0] == "--climb":
        m, seed, iters, out = int(a[1]), int(a[2]), int(a[3]), a[4]; rng = random.Random(seed); os.makedirs(out, exist_ok=True)
        def sc(G):
            try: r = gains(G, K=0, check=False)
            except AssertionError: return None
            return (r["GJ"].get(1, -99), r["g"]) if os.environ.get("OBJ") == "j1" else (r["g"],)
        cur = None
        while cur is None:
            G = rand_iso(m + 1, rng); s = sc(G)
            if s: cur, cs = G, s
        best = cs; stale = 0
        for it in range(iters):
            H = mutate(cur, rng); s = sc(H)
            if s is None: continue
            if s >= cs: stale = 0 if s > cs else stale; cur, cs = H, s
            else: stale += 1
            if cs > best:
                best = cs; json.dump(cur, open(os.path.join(out, "%s_m%d_s%d.json" % (os.environ.get("OBJ", "g"), m, seed)), "w"))
                print("it", it, "g*", best, gains(cur, K=0, check=False)["GJ"], flush=True)
            if stale > 3000:
                G = rand_iso(m + 1, rng); s = sc(G)
                if s: cur, cs, stale = G, s, 0
        print("FINAL m", m, "seed", seed, "g*", best)
    else:
        for p in a:
            r = gains(json.load(open(p))); bad += r["IND"]; print(os.path.basename(p), r)
    print("TOTAL IND", bad); sys.exit(1 if bad else 0)
