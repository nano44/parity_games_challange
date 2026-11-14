import sys, os, json, collections
ROOT=os.environ.get("ROOT") or os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","..","..")); os.environ.setdefault("EG195_ROOT", ROOT)
sys.path[:0]=[os.path.join(ROOT,p) for p in ("experiments/new/box195","experiments/new/box191","experiments/new/box189","experiments/new/box190","experiments/new/box21","experiments/new","experiments/si","experiments/harness")]
import eg195, gamma3, n5v, n5x
for f in sys.argv[1:]:
    G=json.load(open(f)); g0,_,_,V=gamma3.build(G,eg195.PADS); g=eg195.topg(g0); n=g.n; name={v:k for k,v in V.items()}
    E,Ed=n5v.Engine(g),n5v.Engine(n5v.dual(g)); sigma,tau=n5x.start_pair(g,E,Ed,None); H=[]
    while len(H)<=20000:
        vs,tb=E.evaluate(tuple(sigma)); H.append((tuple(sigma),vs,tb)); res=n5v.step(g,E,Ed,sigma,tau,"xi")
        if res is None or res[4]: break
        sigma,tau=res[0],res[1]
    nx=lambda t,x: H[t][0][x] if g.owner[x]==0 else H[t][2][x]
    R=collections.Counter(); nsw=collections.Counter()
    for t in range(1,len(H)):
        k=0
        for u in range(n):
            if len(g.succ[u])>=2 and nx(t-1,u)!=nx(t,u):
                if g.owner[u]==0: k+=1
                if H[t-1][1][u][0]==H[t][1][u][0]: R[(u,nx(t,u),H[t][1][u][0])]+=1
        nsw[k]+=1
    top=sorted(R.items(),key=lambda kv:-kv[1])[:4]
    deg=collections.Counter(len(g.succ[u]) for u in range(n) if g.owner[u]==0 and len(g.succ[u])>=2)
    print(os.path.basename(f),"T3",len(H)-1,"top R",[(str(name[u]),str(name[b]),k,len(g.succ[u])) for (u,b,w),k in top],"maxdeg",max(deg),"switches/step hist",dict(sorted(nsw.items())),flush=True)
