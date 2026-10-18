"""L-ALG succ. 10 (box 12, produced on Opus 5.5), GAP-A-M §32h: (FD-WITNESS) — at a chain-changing transition, let j* be the first
depth-0 position whose (R_j, rank_j, V_j) differs (b12_pot.sig). Does a vertex with a NEW key (b12_pot.keys: (v, ρ, |V|),
(v, ρ, |R|), (v, ρ, j, |R|, |V|)) lie in the piece at j*, or at j* − 1 (where R_{j*} changed because that piece grew)?
Corpus: CLASS=1 [DIST=1] (b12_topchain.classgames, 3 trials, seed 2, n ≤ 200), else the files with n ≤ 100.
Usage: DTL_ORDER=stable|oink [CLASS=1 DIST=1] b12_fdwit.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
sys.setrecursionlimit(100000)
import pg, b12_pot as B
from b12_topchain import classgames
from b12_fdkey import plain
order=os.environ.get("DTL_ORDER","stable"); KS=("K-v-rV","K-v-rs","K-v-all")
src = classgames(sys.argv[1:],3,2,200) if os.environ.get("CLASS")=="1" else plain(sys.argv[1:],100)
tot=0; nowit={k:0 for k in KS}; nowit_prev={k:0 for k in KS}; ex={}
for name,g in src:
    try: d=B.run(g,order)
    except RecursionError: continue
    prev=None
    for ph,calls in getattr(d,"log",[]):
        ch=B.chain(calls,g.n); kk=B.keys(ch); sg=B.sig(ch)
        if prev is None or prev[0]!=ph: seen={k:set() for k in KS}
        elif sg!=prev[1]:
            tot+=1; js=next(j for j in range(max(len(sg),len(prev[1]))) if j>=len(sg) or j>=len(prev[1]) or sg[j]!=prev[1][j])
            piece=ch[js][4] if js<len(ch) else frozenset()
            prevpiece=ch[js-1][4] if js>=1 else frozenset()
            for k in KS:
                newv={x[0] for x in kk[k]-seen[k]}
                if not (newv & piece):
                    nowit[k]+=1; ex.setdefault(k,(name,g.n,js))
                    if not (newv & (piece|prevpiece)): nowit_prev[k]+=1
        for k in KS: seen[k]|=kk[k]
        prev=(ph,sg)
print(order,"chain-changing transitions",tot,"| no new-key vertex in the piece at j*:",nowit,"| nor in the piece at j*-1:",nowit_prev,"| first",ex)
