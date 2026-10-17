import sys,re,collections
tot=collections.Counter(); runs=0; empty=0; hits=[]
for fn in sys.argv[1:]:
    for l in open(fn):
        if 'R2PROBE' not in l: empty+=1; continue
        runs+=1; d=dict(re.findall(r'(\w+)=(-?\d+)',l.split('R2PROBE')[1]))
        for k,v in d.items(): tot[k]+=int(v)
        if int(d['dom_str'])>0 or any(int(d[k])>0 for k in ['ntf_viol','fm_viol','yz_viol','dom_nonstr','acyc_viol','tpr_bad','notop']): hits.append(l.strip()[:220])
print("runs",runs,"no-probe-line",empty); print(dict(tot)); print(len(hits),"runs with a straddle or a violation"); print("\n".join(hits[:40]))
