#!/usr/bin/env python3
"""Box 206 Addendum C (L-NEW successor 70): step-by-step trace of an IDEAL-CYC run: for the watched movers (default 47) the top-block set
(bits = the level-L movers by gate index, high to low), the movers that switch (x:old Xi-target>new) and the gates that flip (owner + e/b).
Usage: trace206.py G.json [mover ...]"""
import sys, json
import os; R=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")); sys.path[:0]=[R+"/box203",R+"/box191"]
import gfc203, idealcyc
f=sys.argv[1]; G=json.load(open(f)); H,n,E,V,gates=gfc203.hist_ideal(G); ST=idealcyc.run(G); T=len(H)-1
L=max(G['lev']); bits=sorted([(G['gate'][x][0],x) for x in range(G['N']) if G['lev'][x]==L],reverse=True)
order=[x for g,x in bits]
watch=[int(a) for a in sys.argv[2:]] if len(sys.argv)>2 else [47]
def blk(v):
    m=H_t[0][v][1]; return ''.join('1' if (m>>E.rank[V[('e',(x,0))]])&1 else '.' for x in order)
print('bits high->low', order)
for t in range(T+1):
    H_t=H[t]
    sw=[] if t==0 else ['%d:%s>%s'%(x,G['opts'][x][ST[t-1][x]][1],G['opts'][x][ST[t][x]][1]) for x in range(G['N']) if ST[t][x]!=ST[t-1][x]]
    fl=[] if t==0 else ['%s%s'%(q[0],'e' if H[t][1][g]==a else 'b') for g,(q,a,b) in gates.items() if H[t-1][1][g]!=H[t][1][g]]
    print(t, ' '.join('%d=%s'%(w,blk(V[('x',w)])) for w in watch), '| sw', ' '.join(sw), '| fl', ' '.join(fl))
