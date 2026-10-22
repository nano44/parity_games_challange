import sys,random,re
src,seed,out=sys.argv[1],int(sys.argv[2]),sys.argv[3]
txt=open(src).read()
lines=[l.strip() for l in txt.replace('\n',' ').split(';')]
rows=[]
for l in lines:
    if not l or l.startswith('parity') or l.startswith('start'): continue
    l=re.sub(r'"[^"]*"','',l).strip()
    parts=l.split()
    if len(parts)<4: continue
    rows.append((int(parts[0]),int(parts[1]),int(parts[2]),[int(x) for x in parts[3].split(',') if x!='']))
ids=[r[0] for r in rows]; perm=ids[:]; random.Random(seed).shuffle(perm); m=dict(zip(ids,perm))
rows=[(m[i],p,o,[m[x] for x in s]) for (i,p,o,s) in rows]; random.Random(seed+1).shuffle(rows)
with open(out,'w') as f:
    f.write("parity %d;\n"%(max(m.values())))
    for (i,p,o,s) in rows: f.write("%d %d %d %s;\n"%(i,p,o,",".join(map(str,s))))
