import sys
tot={};mx={};bad=[];N=0;ratio=[]
for f in sys.argv[1:]:
    for l in open(f):
        if " DESC" not in l: continue
        t=l.split(" DESC",1)[1].split()[2:]; d=dict(zip(t[0::2],t[1::2])); n=int(d["n"]); N+=1
        for k,v in d.items():
            if k=="n": continue
            tot[k]=tot.get(k,0)+int(v); mx[k]=max(mx.get(k,0),int(v))
        for k in ("DMISS","ROOTMISS","WITVIOL_S","WITVIOL_SC","DT_"):
            if int(d.get(k,0)): bad.append((l.split()[1],k,d[k]))
        if int(d["DESC"]): ratio.append((int(d["DESC"])/max(1,int(d["DR"])+int(d["DS"])+int(d["DT_"])), l.split()[1]))
print("games",N); print("TOT",tot); print("MAX",mx); print("bad",len(bad),bad[:8]); ratio.sort(); print("max DESC/(R+S+T)",ratio[-3:])
