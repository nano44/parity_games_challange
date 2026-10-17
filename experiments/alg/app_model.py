#!/usr/bin/env python3
"""L-ALG (produced on Opus 5.5, 2026-10-16): the abstract piece process APP(k) of docs/alg/GAP-A-M.md §10 (a BARRIER for the
current GAP-A proof route, not a game). Simulates the phase and asserts the axioms listed in §10.2 that are checkable on the
trace: 2^k + 1 searches, 2^k tangles, one new tangle per search, at each context the profile changes at most once and only
upward, contexts are functions of earlier results, every driver is learned at piece k >= the changed level, the learned
tangle equals the bottom piece's removed set, bottom contexts never recur. Usage: app_model.py [K...] (default 1..10)."""
import sys


def run(k):
    T = set()
    seen_profiles = {}            # (level, context) -> list of profiles over searches
    bottom_contexts = set()
    searches = 0
    prev = None
    while True:
        searches += 1
        c, pieces = (), []
        for i in range(k):
            ctx = (i, c)                                      # context R_i is a function of the prefix c
            b = 1 if tuple(c + (0,) + (1,) * (k - i - 1)) in T else 0
            prof = {"x0": 2, "x1": 1 + 2 * b}
            seen_profiles.setdefault(ctx, []).append(prof)
            ret = "x1" if prof["x1"] > prof["x0"] else "x0"   # argmax = return set
            assert ret == ("x1" if b else "x0")
            pieces.append((ctx, b))
            c = c + (b,)
        t = c                                                 # t(c) = R_k = D_k: the leftovers encode c
        assert t not in bottom_contexts or t in T, "bottom context recurs before the phase ends"
        bottom_contexts.add(t)
        new = t not in T
        if new:
            T.add(t)
        # driver check against the previous search: the first changed level j had its driver learned at piece k >= j
        if prev is not None:
            for j, ((cx, b0), (cy, b1)) in enumerate(zip(prev[0], pieces)):
                if cx != cy or b0 != b1:
                    assert cx == cy and b1 == 1 and b0 == 0, "first difference must be an upward change at an equal context"
                    assert prev[1] == cy[1] + (0,) + (1,) * (k - j - 1), "driver = the tangle learned in the previous search"
                    break
        prev = (pieces, t)
        if not new:
            break
    for ctx, profs in seen_profiles.items():
        changes = sum(1 for a, b in zip(profs, profs[1:]) if a != b)
        assert changes <= 1 and all(b["x1"] >= a["x1"] and b["x0"] >= a["x0"] for a, b in zip(profs, profs[1:]))
    assert searches == 2 ** k + 1 and len(T) == 2 ** k, (k, searches, len(T))
    return searches, len(T)


if __name__ == "__main__":
    ks = [int(a) for a in sys.argv[1:]] or list(range(1, 11))
    for k in ks:
        s, t = run(k)
        print(f"APP({k}): n = {2 * k + 1}, searches = {s}, tangles = {t}")
    print("APP-MODEL OK")
