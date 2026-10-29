# T33 checks (L-LIT). Run: python3 -I docs/lit/T33-match-phi-check.py
# Part A: Lemma MATCH-Phi, brute force over all pairs of subsets of K = 6 ranks, 40 random parity patterns (seed 1).
# Part B: the ascending binary counter of path sets under a fixed top (T33 section 2): strict weight rise, fixed top, NM count.
import itertools, random

def weight(A, par):  # SPEC S1 signed weight: +2^r for even rank, -2^r for odd rank
    return sum((1 if par[r] == 0 else -1) * 2 ** r for r in A)

def w(r, par):       # signed position, pos(r) = r + 1
    return (r + 1) if par[r] == 0 else -(r + 1)

def phi(A, par):
    return sum(w(r, par) for r in A)

def matched(A, B, par):
    """MATCHED: a matching of outs (A-B) to ins (B-A), pairs with w(in) > w(out), covering every even out and every odd in."""
    outs, ins = sorted(A - B), sorted(B - A)
    must_out = {o for o in outs if par[o] == 0}
    must_in = {i for i in ins if par[i] == 1}
    for k in range(min(len(outs), len(ins)) + 1):
        for so in itertools.combinations(outs, k):
            if not must_out <= set(so):
                continue
            for si in itertools.permutations(ins, k):
                if must_in <= set(si) and all(w(i, par) > w(o, par) for o, i in zip(so, si)):
                    return True
    return False

random.seed(1)
tot = bad = nm = 0
for trial in range(40):
    K = 6
    par = [random.randint(0, 1) for _ in range(K)]
    subs = [frozenset(c) for k in range(K + 1) for c in itertools.combinations(range(K), k)]
    for A in subs:
        for B in subs:
            if A != B and weight(B, par) > weight(A, par):
                tot += 1
                if matched(A, B, par):
                    if phi(B, par) - phi(A, par) < 1:
                        bad += 1
                else:
                    nm += 1
print("A: improving pairs", tot, "| matched with phi rise < 1:", bad, "| carries:", nm)

# Part B: ranks 0..k-1 are even bits b_1..b_k (rank i = bit i+1), rank k is the fixed even top. Path set at count x:
# {top} U {bit i : bit i of x set}. Successive counts 0..2^k - 1.
for k in range(1, 9):
    par = [0] * (k + 1)
    seq = [frozenset({k} | {i for i in range(k) if (x >> i) & 1}) for x in range(2 ** k)]
    rise = all(weight(seq[t + 1], par) > weight(seq[t], par) for t in range(len(seq) - 1))
    top = all(max(s) == k for s in seq)
    carries = sum(1 for t in range(len(seq) - 1) if not matched(seq[t], seq[t + 1], par))
    print(f"B: k={k} P-changes={len(seq) - 1} strict-rise={rise} fixed-top={top} carries(NM)={carries}")
