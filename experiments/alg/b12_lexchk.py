"""L-ALG succ. 10 (box 14, produced on Opus 5.5), GAP-A-M §35b: mechanical check of Lemma LEX on 𝒞^1P. For every pair s′ < s″ of
searches of a phase, at the first differing depth-0 position q the context set R_q is common and the state rises: higher rank
(−1 emptying round, stable = n + 2), or the same rank with V strictly larger, or the same outcome with the piece strictly larger.
Corpus: b12_topchain.classgames (3 trials, seed 2, n ≤ 200; use DIST=1). Usage: DTL_ORDER=stable|oink DIST=1 b12_lexchk.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
sys.setrecursionlimit(100000)
import b12_pot as B, b12_core as K
from b12_topchain import classgames
order=os.environ.get("DTL_ORDER","stable"); pairs=bad=0; ex=None
def less(x,y,n):   # states at the same R
    rx,ry=x[1],y[1]
    if rx!=ry: return rx<ry            # −1 with emptying round e < stable (n+2); e larger is higher
    if x[2]!=y[2]: return x[2]<y[2]    # same rank: V strictly nested upward
    return x[3]<y[3]                   # same outcome: piece strictly larger
for name,g in classgames(sys.argv[1:],3,2,200):
    try: d=B.run(g,order)
    except RecursionError: continue
    ph={}
    for p,c in d.log: ph.setdefault(p,[]).append(K.states(B.chain(c,g.n)))
    for L in ph.values():
        for a in range(len(L)):
            for b in range(a+1,len(L)):
                x,y=L[a],L[b]; q=next((p for p in range(min(len(x),len(y))) if x[p]!=y[p]),None)
                if q is None: continue
                pairs+=1
                if x[q][0]!=y[q][0] or not less(x[q],y[q],g.n): bad+=1; ex=ex or (name,a,b,q)
print(order,"pairs",pairs,"LEX violations",bad,"first",ex)
