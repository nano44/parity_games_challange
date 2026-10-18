#!/usr/bin/env python3
"""R-N5T probe (REFEREE). Written from VJ00 (BRICS RS-00-48) §4.1-4.4 only; imports nothing from the repo.
Vertices 0..n-1, relevance order = index order (v < w means w more relevant); plus[v] = True iff v in R+ (player ⊕'s).
Omega_sigma(v) = min_⊴ over plays consistent with sigma (brute force over all positional ⊖ strategies; the min is attained by
a positional one, VJ00 (11)). Checks, for every ⊕-strategy sigma and EVERY non-empty unambiguous subset I of improvements:
  (A) Omega_sigma ⊴ Omega_{Switch_I(sigma)} pointwise (Lemma A);
  (B) if equal: each switched v has Lambda(v) = v, Lambda(w) = Lambda(sigma(v)) = v, empty path sets, and the length relation;
  (T) if equal: phi strictly increases (Theorem).
Usage: python3 -I n5t_probe.py [games] [nmax] [seed]"""
import sys, os, random, itertools
FLIP = os.environ.get("N5T_FLIP") == "1"   # negative control: wrong sign of epsilon must make (T) fail

def reward(v, plus): return v if plus[v] else -v

def setless(B, C, plus):              # B ≺ C on sets (B != C): MaxDiff in (B\C)∩R- or (C\B)∩R+
    d = B ^ C; m = max(d)
    return (m in B and not plus[m]) or (m in C and plus[m])

def key_le(x, y, plus):               # x ⊴ y on play values (l, B, k)
    (l, B, k), (l2, B2, k2) = x, y
    if l != l2: return reward(l, plus) < reward(l2, plus)
    if B != B2: return setless(B, B2, plus)
    return k <= k2 if not plus[l] else k2 <= k

def theta(start, succ_of):             # play value of the unique play from start
    seq, pos = [], {}
    x = start
    while x not in pos:
        pos[x] = len(seq); seq.append(x); x = succ_of(x)
    cyc = seq[pos[x]:]; lam = max(cyc)
    kidx = seq.index(lam)               # first occurrence of lambda (it is on the cycle, after the prefix)
    prefix = seq[:kidx]
    return (lam, frozenset(u for u in prefix if u > lam), len(prefix))

def omega(n, owner, succ, plus, sigma):
    odd = [v for v in range(n) if owner[v] == 1]
    best = [None] * n
    for choice in itertools.product(*[succ[v] for v in odd]):
        tau = dict(zip(odd, choice))
        f = lambda x: sigma[x] if owner[x] == 0 else tau[x]
        for v in range(n):
            t = theta(v, f)
            if best[v] is None or not key_le(best[v], t, plus): best[v] = t
    return best

def improvements(n, owner, succ, plus, sigma, Om):
    out = {}
    for v in range(n):
        if owner[v] == 0:
            ws = [w for w in succ[v] if w != sigma[v] and key_le(Om[sigma[v]], Om[w], plus) and not key_le(Om[w], Om[sigma[v]], plus)]
            if ws: out[v] = ws
    return out

def phi(n, owner, plus, sigma, Om):
    s = 0
    for v in range(n):
        if owner[v] == 0 and Om[v][0] == v:
            k = Om[sigma[v]][2]
            s += (k if not plus[v] else -k) * (-1 if FLIP else 1)
    return s

def check_game(n, owner, succ, plus, stats):
    evens = [v for v in range(n) if owner[v] == 0]
    for ch in itertools.product(*[succ[v] for v in evens]):
        sigma = [None] * n
        for v, w in zip(evens, ch): sigma[v] = w
        Om = omega(n, owner, succ, plus, sigma)
        imp = improvements(n, owner, succ, plus, sigma, Om)
        if not imp: continue
        verts = list(imp)
        # every non-empty unambiguous subset: per vertex, None or one improving target
        for pick in itertools.product(*[[None] + imp[v] for v in verts]):
            I = {v: w for v, w in zip(verts, pick) if w is not None}
            if not I: continue
            s2 = list(sigma)
            for v, w in I.items(): s2[v] = w
            Om2 = omega(n, owner, succ, plus, s2)
            stats["switches"] += 1
            if not all(key_le(Om[v], Om2[v], plus) for v in range(n)):
                stats["A_fail"] += 1; stats.setdefault("A_ex", (n, owner, succ, plus, sigma, I)); continue
            if Om2 != Om: continue
            stats["flat"] += 1
            for v, w in I.items():
                u = sigma[v]; L = Om[v][0]
                ok = (L == v and Om[w][0] == v and Om[u][0] == v and not Om[w][1] and not Om[u][1]
                      and ((Om[w][2] > Om[u][2]) if not plus[v] else (Om[w][2] < Om[u][2])))
                if not ok: stats["B_fail"] += 1; stats.setdefault("B_ex", (n, owner, succ, plus, sigma, I))
            if not phi(n, owner, plus, s2, Om2) > phi(n, owner, plus, sigma, Om):
                stats["T_fail"] += 1; stats.setdefault("T_ex", (n, owner, succ, plus, sigma, I))

def from_pg(prio, owner, succ, dual=False):
    """Map a parity game (max-parity, Even = owner 0 wins even) to VJ00 form: relevance = (prio, index) order,
    R+ = even priority. dual=True: owners swapped, prio+1 (⊕ = original Odd). Returns (perm-relabelled game, relabel map)."""
    n = len(prio)
    if dual: prio = [p + 1 for p in prio]; owner = [1 - o for o in owner]
    order = sorted(range(n), key=lambda v: (prio[v], v)); r = {v: i for i, v in enumerate(order)}
    o2 = [None] * n; s2 = [None] * n; plus = [None] * n
    for v in range(n):
        o2[r[v]] = owner[v]; s2[r[v]] = sorted(r[w] for w in succ[v]); plus[r[v]] = prio[v] % 2 == 0
    return o2, s2, plus, r

def main():
    games = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    nmax = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    rnd = random.Random(int(sys.argv[3]) if len(sys.argv) > 3 else 1)
    stats = dict(games=0, switches=0, flat=0, A_fail=0, B_fail=0, T_fail=0)
    # §0 instance of the reading, dual side
    o, s, p, r = from_pg([2, 6, 0, 1], [0, 1, 0, 0], [[0, 2], [1, 3], [0], [0, 1, 2]], dual=True)
    v1, v3 = r[1], r[3]
    sig = [None] * 4; sig[v1] = v1
    Om = omega(4, o, s, p, sig); sig2 = list(sig); sig2[v1] = v3; Om2 = omega(4, o, s, p, sig2)
    print("§0 instance (dual, VJ00 labels; orig 1 ->", v1, ", orig 3 ->", v3, ")")
    print("  Omega(tau: 1->1):", Om, " improvements:", improvements(4, o, s, p, sig, Om))
    print("  Omega(tau: 1->3):", Om2, " improvements:", improvements(4, o, s, p, sig2, Om2))
    print("  equal:", Om == Om2, " phi:", phi(4, o, p, sig, Om), "->", phi(4, o, p, sig2, Om2))
    check_game(4, o, s, p, stats); stats["games"] += 1
    for _ in range(games):
        n = rnd.randint(2, nmax)
        owner = [rnd.randint(0, 1) for _ in range(n)]
        plus = [rnd.random() < 0.5 for _ in range(n)]
        succ = [sorted(set(rnd.sample(range(n), rnd.randint(1, min(3, n))))) for _ in range(n)]
        if sum(len(succ[v]) for v in range(n) if owner[v] == 1) > 14: continue
        check_game(n, owner, succ, plus, stats); stats["games"] += 1
    print({k: v for k, v in stats.items() if not k.endswith("_ex")})
    for k in ("A_ex", "B_ex", "T_ex"):
        if k in stats: print(k, stats[k])

if __name__ == "__main__":
    main()
