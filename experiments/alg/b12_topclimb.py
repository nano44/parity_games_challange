"""L-ALG succ. 10 (box 12, produced on Opus 5.5), GAP-A-M §30: adversarial climb against (TOP-UNIQUE@R) on 𝒞^1P: "in one phase, at
one best_vertices context R, at most one distinct tangle per top fires in R's region steps". Class-preserving moves
(fixd_oneplayer.mutate), priorities made all-distinct after every move. Score: (max distinct same-top tangles firing at one
context and phase, total distinct firing tangles over contexts, searches). Accept on ≥. A score ≥ 2 in the first slot is a violation: written to OUTDIR with its seed.
MODE=chain targets (TOP-CHAIN@R) instead: same-top firing tangles at one context and phase form a ⊆-chain (score
slot 1 = crossing same-top pairs; ≥ 1 is a violation).
Check: b12_topclimb.py --check instances/onep_topuniq_n20.pg (prints TOPUNIQ-VIOLATION).
Usage: [MODE=uniq|chain] [START=G.pg] DTL_ORDER=stable|oink b12_topclimb.py C N P STEPS SEED OUTDIR"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, fixd_stealentry as SE
from b12_topchain import firing
from fixd_ctx1p import distinct
from fixd_oneplayer import start, mutate
MODE = os.environ.get("MODE", "uniq")   # uniq: (TOP-UNIQUE@R), FALSE (onep_topuniq_n20); chain: (TOP-CHAIN@R)


def score(g, order):
    d = SE.run(g, order); best = tot = cross = 0
    for _, S in firing(d).items():
        tot += len(S); bt = {}
        for t in S: bt.setdefault(max(t), []).append(t)
        best = max([best] + [len(L) for L in bt.values()])
        if MODE == "chain":
            cross += sum(1 for L in bt.values() for i, a in enumerate(L) for b in L[i + 1:] if not (a <= b or b <= a))
    return ((cross, best, tot, d.iterations) if MODE == "chain" else (best, tot, d.iterations)), d


def main():
    sys.setrecursionlimit(100000)
    if sys.argv[1] == "--check":                      # pinned self-kill: max same-top firing count 2 at one context, both orders
        g = pg.read(sys.argv[2]); r = [score(g, o)[0][0] for o in ("stable", "oink")]
        print("TOPUNIQ-VIOLATION" if min(r) >= 2 else "no violation", r); return
    C, N, P, steps, seed = (int(a) for a in sys.argv[1:6]); out = sys.argv[6]
    order = os.environ.get("DTL_ORDER", "stable"); rnd = random.Random(seed); os.makedirs(out, exist_ok=True)
    g = distinct(pg.read(os.environ["START"]) if os.environ.get("START") else start(C, N, P, rnd)); sg, _ = score(g, order)
    for it in range(steps):
        h = mutate(g, C, P, rnd)
        if h is None: continue
        h = distinct(h); sh, _ = score(h, order)
        if sh >= sg:
            if sh > sg: print(it, sh, flush=True)
            g, sg = h, sh
            if sg[0] >= (1 if MODE == "chain" else 2):
                fn = os.path.join(out, f"top{MODE}_viol_C{C}_n{N}_s{seed}.pg"); pg.write(g, fn)
                print("VIOLATION", sg, fn, flush=True); return
    print("final", sg)


if __name__ == "__main__":
    main()
