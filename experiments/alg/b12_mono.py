"""L-ALG succ. 10 (box 12, produced on Opus 5.5), GAP-A-M §30: vertex-indexed monotone candidates for (CTX⁺) on 𝒞^1P. For each
search, the depth-0 chain R_0 ⊋ R_1 ⊋ ... (fixd_outcome.OC) cuts G′ into pieces R_j \\ R_{j+1}. Across consecutive searches s, s+1 of
a phase of q:
  (STABLE-MASS)  S(s) := union of the pieces whose depth-0 call was stable;  S(s) ⊆ S(s+1)?
  (STABLE-TOPS)  T(s) := union of V* over the stable depth-0 calls;           T(s) ⊆ T(s+1)?
  (NEG-TOPS)     N(s) := union of prevV over the −1 depth-0 calls;            N(s) ⊆ N(s+1) ∪ T(s+1)?
Either of the first two, with a bound on the transitions between its increases, would be a potential that survives re-cuts.
per_position(log): the most distinct contexts one depth-0 position holds in one phase.
Class set as b12_topchain.py. Usage: DTL_ORDER=stable|oink TRIALS=k SEED=s NMAX=n b12_mono.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import fixd_outcome as OCm
from b12_topchain import classgames


def chain_sets(calls):
    S, T, N = set(), set(), set()
    for j, (R, res, V) in enumerate(calls):
        piece = R - (calls[j + 1][0] if j + 1 < len(calls) else frozenset())
        if res == 1: S |= piece; T |= V
        elif res == -1: N |= V
    return S, T, N


def per_position(log):
    """max over (phase, depth-0 position j) of the number of distinct contexts R_j seen in that phase, and the phase's searches."""
    best = (0, 0, 0)
    ph = {}
    for p, calls in log: ph.setdefault(p, []).append(calls)
    for p, L in ph.items():
        for j in range(max(len(c) for c in L)):
            k = len({c[j][0] for c in L if j < len(c)})
            if k > best[0]: best = (k, j, len(L))
    return best


if __name__ == "__main__":
    sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable")
    trials, seed, nmax = int(os.environ.get("TRIALS", "2")), int(os.environ.get("SEED", "1")), int(os.environ.get("NMAX", "120"))
    pairs = 0; bad = {"STABLE-MASS": 0, "STABLE-TOPS": 0, "NEG-TOPS": 0}; ex = {}
    for name, g in classgames(sys.argv[1:], trials, seed, nmax):
        d = OCm.run(g, order); log = getattr(d, "log", [])
        for (pa, ca), (pb, cb) in zip(log, log[1:]):
            if pa != pb: continue
            pairs += 1; Sa, Ta, Na = chain_sets(ca); Sb, Tb, Nb = chain_sets(cb)
            for k, ok in (("STABLE-MASS", Sa <= Sb), ("STABLE-TOPS", Ta <= Tb), ("NEG-TOPS", Na <= Nb | Tb)):
                if not ok:
                    bad[k] += 1; ex.setdefault(k, (name, g.n))
    print("order", order, "same-phase pairs", pairs, "violations", bad, "first", ex)

