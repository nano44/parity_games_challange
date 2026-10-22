"""L-ALG succ. 10 (box 12, produced on Opus 5.5), GAP-A-M §32f: (NO-RETURN) "no vertex returns to a piece signature it held
earlier in the phase and then left", per signature kind: all = (ρ, j, |R_j|, |V_j|), rV = (ρ, |V_j|), rs = (ρ, |R_j|) (b12_pot.chain).
It would explain (VR-NEW_*) vertex by vertex. Corpus: CLASS=1 [DIST=1] (b12_topchain.classgames, 3 trials, seed 2, n ≤ 200), else
the files with n ≤ 100. Usage: DTL_ORDER=stable|oink [CLASS=1 DIST=1] b12_noret.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
sys.setrecursionlimit(100000)
import pg, b12_pot as B
from b12_topchain import classgames
from b12_fdkey import plain
order=os.environ.get("DTL_ORDER","stable")
src = classgames(sys.argv[1:],3,2,200) if os.environ.get("CLASS")=="1" else plain(sys.argv[1:],100)
SIG={"all":lambda j,R,r,V:(r,j,len(R),len(V)),"rV":lambda j,R,r,V:(r,len(V)),"rs":lambda j,R,r,V:(r,len(R))}
trans=0; ret={k:0 for k in SIG}; ex={}
for name,g in src:
    try: d=B.run(g,order)
    except RecursionError: continue
    prev=None
    for ph,calls in getattr(d,"log",[]):
        ch=B.chain(calls,g.n)
        cur={k:{v:f(j,R,r,V) for j,R,r,V,pc,_ in ch for v in pc} for k,f in SIG.items()}
        if prev is None or prev[0]!=ph: hist={k:{} for k in SIG}
        else:
            trans+=1
            for k in SIG:
                bad=[v for v,sg in cur[k].items() if sg in hist[k].get(v,set()) and prev[1][k].get(v)!=sg]
                if bad: ret[k]+=1; ex.setdefault(k,(name,g.n,bad[:3]))
        for k in SIG:
            for v,sg in cur[k].items(): hist[k].setdefault(v,set()).add(sg)
        prev=(ph,cur)
print(order,"transitions",trans,"transitions where some vertex RETURNS to a signature it left:",ret,"first",ex)
