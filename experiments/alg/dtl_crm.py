"""L-ALG (produced on Opus 5.5, 2026-10-16), GAP-A-M §13g: (deciding round r0, actual round count M) of successive DEF changes per context; counts repeats and r0 dips without an M rise. Usage (repo root): DTL_ORDER=oink python3 experiments/alg/dtl_crm.py EXTRA_DIR (EXTRA_DIR/def/*.pg and EXTRA_DIR/*.pg are added)."""
import sys, glob, os
sys.path.insert(0,'experiments/alg'); sys.path.insert(0,'experiments/harness')
import dtl_regvec as RV, pg
sys.setrecursionlimit(100000)
S=sys.argv[1]
files=sorted(glob.glob('experiments/alg/instances/*.pg')+glob.glob('experiments/alg/instances/climbs_1016/*.pg')+glob.glob(S+'/def/*.pg')+glob.glob(S+'/*.pg'))
tot={"runs":0,"steps":0,"repeat":0,"dip_without_Mrise":0}; ex=[]
for f in files:
    g=pg.read(f)
    if g.n>64: continue
    d=RV.build(g); d.run()
    for key,occ in d.calls.items():
        seq=[]
        for (s1,r1,v1,h1,tl1),(s2,r2,v2,h2,tl2) in zip(occ,occ[1:]):
            if h1!=h2 or r1==r2: continue
            if os.environ.get("CRM_IDEAL_STABLE") == "1" and h1[0] != 1: continue      # ideal-stable contexts only
            pick=lambda r,i: r[min(i,len(r)-1)]   # fixed box 4 (L-RED caveat): stable run stays at its fixpoint
            r0=next(i for i in range(1,max(len(r1),len(r2))+1) if pick(r1,i)!=pick(r2,i))
            M1=len([x for x in r1 if x]); M2=len([x for x in r2 if x])
            final = (h2[0]==1 and r2[-1] and not (len(r2)>1 and not r2[-1]) and frozenset(r2[-1])==h2[1])
            seq.append((r0,M1,M2,final))
        if not seq: continue
        tot["runs"]+=1; tot["steps"]+=len(seq)
        pairs=[(a,c) for a,b,c,fi in seq]
        if len(set(pairs))<len(pairs): tot["repeat"]+=1; ex.append((os.path.basename(f),len(key[1]),seq))
        for (a,b,c,fi),(a2,b2,c2,fi2) in zip(seq,seq[1:]):
            if a2<a and not c2>b2 and not fi2: tot["dip_without_Mrise"]+=1; ex.append(("dip",os.path.basename(f),len(key[1]),seq))
print(os.environ.get("DTL_ORDER"), tot); print([e for e in ex if e[0] != "dip"][:3])
