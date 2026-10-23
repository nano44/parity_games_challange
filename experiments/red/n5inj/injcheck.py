"""L-RED box 26 (produced on Opus 5.5): test of (SAME-I => SAME-VAL) for N5's improving sets (R58 §2). For one player of a game, enumerate every
positional strategy (or SAMPLE of them), compute its improving-edge set exactly as n5.py does (si.py Engine.improving on G for Even,
on the dual G^d for Odd), and report: collisions sigma1 != sigma2 with I(sigma1) = I(sigma2) (each one also shows the tie
Xi(a) = Xi(b) at a vertex where they differ, R58 Lemma 2), whether every collision has the SAME valuation vector (R58 Lemma 1's premise), and the histogram of |I| vs C(m', k).
Usage: injcheck.py G.pg even|odd [SAMPLE SEED]   (no SAMPLE: exhaustive)"""
import itertools, math, os, random, sys
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
for d in ("new", "si", "harness"):
    sys.path.insert(0, os.path.join(R, "experiments", d))
import n5  # noqa: E402
import pg  # noqa: E402
from si import Engine  # noqa: E402


def check(g, side, sample=None, seed=1, out=sys.stdout):
    h = g if side == "even" else n5.dual(g)
    E = Engine(h)
    ch = [v for v in range(h.n) if h.owner[v] == 0 and len(E.succ[v]) > 1]
    fixed = {v: E.succ[v][0] for v in range(h.n) if h.owner[v] == 0 and len(E.succ[v]) == 1}
    mprime = sum(len(E.succ[v]) - 1 for v in ch)
    total = math.prod(len(E.succ[v]) for v in ch)
    if sample is None:
        it = itertools.product(*[E.succ[v] for v in ch])
    else:
        rng = random.Random(seed)
        it = (tuple(rng.choice(E.succ[v]) for v in ch) for _ in range(sample))
    seen, hist, coll, valof, bad = {}, {}, [], {}, 0
    for choice in it:
        s = [-1] * h.n
        for v, w in fixed.items(): s[v] = w
        for v, w in zip(ch, choice): s[v] = w
        s = tuple(s)
        val, _ = E.evaluate(s)
        I = frozenset(E.improving(s, val))
        vv = tuple(val)
        if I in valof and valof[I] != vv:
            bad += 1
        valof.setdefault(I, vv)
        if I in seen and seen[I] != s:
            a = seen[I]; v = next(u for u in ch if a[u] != s[u])
            coll.append((a, s, v, val[a[v]], val[s[v]]))
        seen.setdefault(I, s)
        E.cache.clear()
        hist[len(I)] = hist.get(len(I), 0) + 1
    n_strat = sum(hist.values())
    print(f"{side}: choice vertices {len(ch)}, m' {mprime}, strategies {total} ({'sample ' + str(sample) if sample else 'all'}), "
          f"distinct I {len(seen)}, collisions {len(coll)}, collisions with DIFFERENT valuation vectors {bad}", file=out)
    print("  |I| : count / C(m',k)  " + "  ".join(f"{k}:{hist[k]}/{math.comb(mprime, k)}" for k in sorted(hist)), file=out)
    for a, s, v, va, vb in coll[:3]:
        print(f"  collision at v {v}: {a[v]} vs {s[v]}; I = same; tie example Xi values {va} / {vb}", file=out)
    return len(coll), bad, n_strat, hist


if __name__ == "__main__":
    g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%")))
    smp = int(sys.argv[3]) if len(sys.argv) > 3 else None
    check(g, sys.argv[2], smp, int(sys.argv[4]) if len(sys.argv) > 4 else 1)
