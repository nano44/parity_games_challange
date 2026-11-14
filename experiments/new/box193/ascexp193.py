#!/usr/bin/env python3
"""Box 193 (L-NEW successor 61): Construction ASC-EXP in CS(M, unlimited A) (doc §3). Usage: ascexp193.py MMAX."""
# ASC-EXP construction: hub chain = S (binary counter value), visited in increasing rank; for x in S, next(x) = min(S above x);
# items not in S keep their last pointer. Check every chain (all items + hub) lex-nondecreasing over all 2^M steps.
import sys
def run(M):
    nxt={x:0 for x in range(1,M+1)}
    def chain(x):
        s=0
        while x: s|=1<<x; x=nxt[x]
        return s
    prev=None; hubs=[]
    for c in range(1<<M):
        S=[i+1 for i in range(M) if c>>i&1]
        for i,x in enumerate(S): nxt[x]=S[i+1] if i+1<len(S) else 0
        cur=[chain(x) for x in range(1,M+1)]+[chain(S[0]) if S else 0]
        if prev and any(a<b for a,b in zip(cur,prev)): return ("FAIL",c)
        prev=cur; hubs.append(cur[-1])
    return ("OK", len(set(hubs)), 1<<M)
for M in range(1, int(sys.argv[1]) + 1): print("ASC-EXP M", M, *run(M))
