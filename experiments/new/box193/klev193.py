#!/usr/bin/env python3
"""Box 193 (L-NEW successor 61): K-levels (doc Addendum 3). Inside a stretch where the top-K prefix (R95 PREFIX-MON, k = K) of every
item's tail and of the hub chain is constant, the exact maximum of distinct hub chains in CS(M, A). Usage: klev193.py M A K"""
import sys, os, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import chain193
import numpy as np
M,A,K=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])
def pref(S,k):
    out=[]; 
    while S and len(out)<k: t=S.bit_length()-1; out.append(t); S&=~(1<<t)
    return tuple(out)
groups=collections.defaultdict(set)
for k in chain193.forests(M,A):
    key=tuple(pref(k[x-1]&~(1<<x),K) for x in range(1,M+1))
    for h in range(M+1):
        c=k[h-1] if h else 0
        groups[key+(pref(c,K),)].add(k+(c,))
best=0
for st in groups.values():
    S=np.array(sorted(st,key=lambda s:s[-1]),dtype=np.int64); b=np.ones(len(S),dtype=np.int64)
    for j in range(len(S)):
        m=(S[:j,-1]<S[j,-1])&np.all(S[:j]<=S[j],axis=1)
        if m.any(): b[j]=b[:j][m].max()+1
    best=max(best,int(b.max()))
print(f"M {M} A {A} K {K}: k-level keys {len(groups)}, max hub chains inside one k-level {best}")
