"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5): a family with S = |G'| - 1 searches in one phase (generalises the
n = 6 climb game sppc_s506). Vertices: a (pr 3, Even, edges b, a), b (pr 2, Odd, edges z, b), z (pr 2, Odd, edges z, x_k),
chain x_1..x_k (pr 0, Odd, self-loop; x_1 -> a, x_j -> x_{j-1}). n = k + 3. Each search of Even's phase learns exactly one
tangle {x_j} (escape x_{j-1}), which the next search absorbs into an earlier removal.
Variant UP=1: x_j priority 2(j-1) (see chain()). Usage: [UP=1] dtl_chainfam.py k [out.pg]  (prints the max phase per order datum)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg

def chain(k, up=False):
    """up=False: all x_j priority 0 (S = n - 1 in stable order; Oink's unstable sort breaks it above 16 equal priorities).
    up=True: x_j priority 2(j-1), a = 2k+1, b = z = 2k (S = n - 1 in both order data; pinned Oink verified at k = 40)."""
    # ids: 0 = a, 1 = b, 2 = z, 3.. = x_1..x_k
    a, b, z = 0, 1, 2; x = lambda j: 2 + j
    prio = ([2 * k + 1, 2 * k, 2 * k] + [2 * (j - 1) for j in range(1, k + 1)]) if up else ([3, 2, 2] + [0] * k)
    owner = [0, 1, 1] + [1] * k
    succ = [[b, a], [z, b], [z, x(k)]] + [[x(j), (a if j == 1 else x(j - 1))] for j in range(1, k + 1)]
    return pg.Game(prio, owner, [sorted(s) for s in succ])

if __name__ == "__main__":
    import dtl_spp as P
    sys.setrecursionlimit(100000)
    if sys.argv[1:] == ["--check"]:     # check.sh: UP chain, k = 12: S = n - 1 in both order data
        g = chain(12, True); ok = True
        for o in ("oink", "stable"):
            os.environ["DTL_ORDER"] = o; d = P.build(g); d.run(); ok &= max(r["S"] for r in P.phases(d)) == g.n - 1
        print("chainfam k=12 up: S = n - 1 in both order data:", "OK" if ok else "FAILED"); sys.exit(0 if ok else 1)
    k = int(sys.argv[1]); g = chain(k, os.environ.get("UP") == "1")
    if len(sys.argv) > 2: pg.write(g, sys.argv[2])
    for o in ("oink", "stable"):
        os.environ["DTL_ORDER"] = o; d = P.build(g); d.run(); ph = P.phases(d); r = max(ph, key=lambda r: r["S"])
        print(f"k={k} n={g.n} order={o} iterations={d.iterations} max phase S={r['S']} |G'|={r['G']} p={r['p']}")
