import sys, os, json, collections
ROOT=os.environ.get("ROOT") or os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","..","..")); os.environ.setdefault("EG195_ROOT", ROOT)
sys.path[:0]=[os.path.join(ROOT,p) for p in ("experiments/new/box195","experiments/new/box191","experiments/new/box189","experiments/new/box190","experiments/new/box21","experiments/new","experiments/si","experiments/harness")]
import eg195, gamma3, n5v, n5x
def run(f):
    G=json.load(open(f)); g0,_,_,V=gamma3.build(G,eg195.PADS); g=eg195.topg(g0); n=g.n; name={v:k for k,v in V.items()}
    E,Ed=n5v.Engine(g),n5v.Engine(n5v.dual(g)); sigma,tau=n5x.start_pair(g,E,Ed,None); H=[]
    while len(H)<=20000:
        vs,tb=E.evaluate(tuple(sigma)); H.append((tuple(sigma),vs,tb)); res=n5v.step(g,E,Ed,sigma,tau,"xi")
        if res is None or res[4]: break
        sigma,tau=res[0],res[1]
    T=len(H)-1; odd=[u for u in range(n) if g.owner[u]==1 and len(g.succ[u])>=2]
    N=sum(1 for u in range(n) if g.owner[u]==0 and isinstance(name[u],tuple) and name[u][0]=='x')
    # step t (t-1 -> t) is a "break" of kind sb if sigma-bar changes at t, lam if some Lambda changes at t
    sb=[False]+[any(H[t-1][2][u]!=H[t][2][u] for u in odd) for t in range(1,T+1)]
    lam=[False]+[any(H[t-1][1][x][0]!=H[t][1][x][0] for x in range(n)) for t in range(1,T+1)]
    # maximal runs of steps t in (a, b] with no sb and no lam break: count consecutive steps without breaks
    best=cur=0; segs=0
    for t in range(1,T+1):
        if sb[t] or lam[t]: cur=0; segs+=1
        else: cur+=1; best=max(best,cur)
    bestS=cur=0
    for t in range(1,T+1):
        if sb[t]: cur=0
        else: cur+=1; bestS=max(bestS,cur)
    F=sum(sb); L=sum(lam)
    print(os.path.basename(f),"T3",T,"N",N,"sbsteps F",F,"lamsteps",L,"breaks",segs,"maxquiet(sb,lam)",best,"maxrun_no_sb",bestS,"segfail",int(best>N+1),flush=True)
for f in sys.argv[1:]: run(f)
