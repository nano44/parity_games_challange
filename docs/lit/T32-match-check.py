# Brute-force check of the T32 MATCH lemma on all pairs of subsets of K ranks with random parities.
import itertools, random
def weight(A, par): return sum((1 if par[r]==0 else -1) * 2**r for r in A)
def w(r, par): return (r+1) if par[r]==0 else -(r+1)       # signed position, pos(r) = r+1
def phi(A, par): return sum(w(r, par) for r in A)
def match(A, B, par):
    outs = sorted(A-B); ins = sorted(B-A)
    must_out = [o for o in outs if par[o]==0]   # even outs must be matched
    must_in = [i for i in ins if par[i]==1]     # odd ins must be matched
    # bipartite matching outs x ins, edge iff w(i) > w(o); need a matching covering must_out and must_in
    best = None
    for k in range(0, min(len(outs), len(ins))+1):
        for so in itertools.combinations(outs, k):
            for si in itertools.permutations(ins, k):
                if all(w(i,par) > w(o,par) for o,i in zip(so,si)):
                    if set(must_out) <= set(so) and set(must_in) <= set(si): return True
    return False
random.seed(1); bad = 0; nm = 0; tot = 0
for trial in range(40):
    K = 6; par = [random.randint(0,1) for _ in range(K)]
    subs = [frozenset(c) for k in range(K+1) for c in itertools.combinations(range(K), k)]
    for A in subs:
        for B in subs:
            if A != B and weight(B, par) > weight(A, par):
                tot += 1
                if match(A, B, par):
                    if phi(B, par) - phi(A, par) < 1: bad += 1
                else: nm += 1
print("improving pairs", tot, "MATCH with phi rise < 1:", bad, "non-MATCH:", nm)
# carry example: ranks 0,1,2 all even; A={0,1}, B={2}: improving, non-MATCH, phi drops? 
par=[0,0,0]; A=frozenset({0,1}); B=frozenset({2})
print("carry", weight(B,par)>weight(A,par), match(A,B,par), phi(A,par), phi(B,par))
