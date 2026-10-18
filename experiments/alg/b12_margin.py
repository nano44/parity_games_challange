"""L-ALG succ. 10 (box 12, produced on Opus 5.5), GAP-A-M §32g: how many vertices supply a NEW key at each chain-changing transition,
for the surviving keys (v, ρ, |V|), (v, ρ, |R|), (v, ρ, j, |R|, |V|) (b12_pot.keys) on the forced class set (b12_topchain.classgames,
3 trials, seed 2, n ≤ 200; use DIST=1 for 𝒞^1P). A count of 1 means one vertex carries the statement at that transition.
Usage: DTL_ORDER=stable|oink DIST=1 b12_margin.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
sys.setrecursionlimit(100000)
import pg, b12_pot as B
from b12_topchain import classgames
from collections import Counter
order=os.environ.get("DTL_ORDER","stable"); KS=("K-v-rV","K-v-rs","K-v-all")
hist={k:Counter() for k in KS}
for name,g in classgames(sys.argv[1:],3,2,200):
    try: d=B.run(g,order)
    except RecursionError: continue
    prev=None
    for ph,calls in getattr(d,"log",[]):
        ch=B.chain(calls,g.n); kk=B.keys(ch)
        if prev is None or prev[0]!=ph: seen={k:set() for k in KS}
        elif B.sig(ch)!=prev[1]:
            for k in KS: hist[k][len({key[0] for key in kk[k]-seen[k]})]+=1
        for k in KS: seen[k]|=kk[k]
        prev=(ph,B.sig(ch))
for k in KS: print(k, "transitions by number of vertices with a new key (smallest first):", sorted(hist[k].items())[:6], "total", sum(hist[k].values()))
