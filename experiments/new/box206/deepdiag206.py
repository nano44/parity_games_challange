#!/usr/bin/env python3
"""Box 206 Addendum A (L-NEW successor 70): per k = 1 run, the loud steps of loud depth >= 2 (scope all): step, loud depth, the kind of
vertex attaining it (mov / gate / oth; Lemma DIV-LOUD says mov or gate), #switching movers, #flipping gates, CC = the cycle set of
Xi_sigma changes. Usage: deepdiag206.py G.json ..."""
import sys, os, json, collections
R=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")); sys.path[:0]=[R+"/box203",R+"/box191",R+"/box202"]
import gfc203, idealcyc
def xicycles(G, s):
    nxt={x:G['opts'][x][s[x]][1] for x in range(G['N'])}
    cyc=set()
    for x0 in range(G['N']):
        seen=[];x=x0
        while x>=0 and x not in seen: seen.append(x); x=nxt[x]
        if x>=0: i=seen.index(x); cyc.add(frozenset(seen[i:]))
    return cyc
if __name__=='__main__':
  for f in sys.argv[1:]:
      G=json.load(open(f)); H,n,E,V,gates=gfc203.hist_ideal(G); ST=idealcyc.run(G); T=len(H)-1
      emask=0
      for k,v in V.items():
          if isinstance(k,tuple) and k[0]=='e': emask|=E.bit[v]
      movers={V[('x',x)] for x in range(G['N'])}
      rows=[]
      for t in range(1,T+1):
          ld=None; arg=None
          for v in range(n):
              (l0,p0,_),(l1,p1,_)=H[t-1][0][v],H[t][0][v]
              if l0!=l1: ld=-1; arg='lam'; break
              e0,e1=p0&emask,p1&emask
              if e0==e1: continue
              z=(e0^e1).bit_length()-1; d=bin((e0|e1)>>(z+1)).count('1')
              if ld is None or d<ld: ld=d; arg=('mov' if v in movers else ('gate' if v in gates else 'oth'))
          if ld is None: continue
          sw=sum(ST[t][x]!=ST[t-1][x] for x in range(G['N'])); fl=sum(H[t-1][1][g]!=H[t][1][g] for g in gates)
          cc=xicycles(G,ST[t])!=xicycles(G,ST[t-1])
          rows.append((t,ld,arg,sw,fl,cc))
      deep=[r for r in rows if r[1]>=2]
      print(os.path.basename(f),'T',T,'deep(ld>=2):',[(t,ld,a,'sw%d'%sw,'fl%d'%fl,'CC' if cc else '-') for t,ld,a,sw,fl,cc in deep])
      print('   ld<=1 steps with CC:',sum(1 for r in rows if r[1]<=1 and r[5]),'of',sum(1 for r in rows if r[1]<=1))
