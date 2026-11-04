import sys, json, time, random
sys.path[:0]=['.','../r187','../r178']
import ideal, req as RQ, xisat
G=json.load(open('../r197/lag/dd_d5_F14.json')); lev=G['lev']; WT=[[o[0] for o in G['opts'][v]] for v in range(G['N'])]
S,_=ideal.traj(G); bad,rq=RQ.requirements(lev,WT,G['gate'],S)
xt={(v,k):G['opts'][v][k][1] for v in range(G['N']) for k in (0,1)}
for nfree in [0,4,8]:
    rng=random.Random(nfree); free=set(rng.sample(sorted(xt),nfree)); fx={f:u for f,u in xt.items() if f not in free}
    r,dt,sol=xisat.solve(lev,WT,S,rq,tmo=100,fixxt=fx); print(nfree,r,round(dt,1),flush=True)
