#!/usr/bin/env python3
"""L-LOWER 5 (BOX L5): per j-window of each doubling level j (levels j, j+1 doubling): the TYPE of the opening b-step (which member
of pair j-1 moved, to which option; () for the first window) and x2's new option, against the FEEDER set (movers on x2's chains that
move at u2-1; lpaudit.py logic). Prints whether the feeder set is a function of the type. Usage: fuelsrc.py genome.json"""
import sys,os,json
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l3'))
from sim import run,val
from trace import keys
G=json.load(open(sys.argv[1]));N=G['N'];d=N//2;S=run(G,G['start']);T=len(S)-1
O=[[0 if k[2*l]<k[2*l+1] else 1 for l in range(d)] for k in (keys(G,s) for s in S)]
F=[sum(O[t][l]!=O[t-1][l] for t in range(1,T+1)) for l in range(d)]
dbl=[l>=1 and F[l]==2*F[l-1]+2 for l in range(d)]
def pb(s,x): return val(G,s,x,1-s[x])>val(G,s,x,s[x])
def chainset(s,x):
    out=set()
    for k in (0,1):
        y=G['opts'][x][k][1]
        while y>=0: out.add(y); y=G['opts'][y][s[y]][1]
    return out
for j in range(1,d-1):
    if not(dbl[j] and dbl[j+1]): continue
    p,q=2*j,2*j+1
    bst=[t for t in range(1,T+1) if O[t][j-1]!=O[t-1][j-1]]
    cuts=[1]+bst+[T+1]; M={}; rows=[]
    for a,b in zip(cuts,cuts[1:]):
        if a>=b: continue
        mv=[(t,x) for t in range(a,b) for x in (p,q) if S[t][x]!=S[t-1][x]]
        (u1,x1),(u2,x2)=mv
        cs=chainset(S[u2-2],x2)|chainset(S[u2-1],x2)
        who=tuple(sorted(x for x in cs if S[u2-1][x]!=S[u2-2][x]))
        bm=tuple((x,S[a][x]) for x in (p-2,q-2) if a>1 and S[a][x]!=S[a-1][x]) if j>=1 else ()
        typ=(bm, S[u2][x2]); M.setdefault(typ,set()).add(who); rows.append(f"{typ}:{who}")
    ok=all(len(v)==1 for v in M.values())
    print('j',j,'types',len(M),'feeder=f(type)' if ok else 'NOT function', {str(k):sorted(v) for k,v in M.items()})
