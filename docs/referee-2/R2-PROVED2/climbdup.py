import sys,random,re,subprocess,os
src,seed,steps,outdir=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),sys.argv[4]
R=random.Random(seed); O=sys.argv[5]
def parse(fn):
    rows={}
    for l in open(fn).read().replace('\n',' ').split(';'):
        l=re.sub(r'"[^"]*"','',l).strip()
        if not l or l.startswith('parity') or l.startswith('start'): continue
        p=l.split(); rows[int(p[0])]=[int(p[1]),int(p[2]),[int(x) for x in p[3].split(',') if x]]
    return rows
def write(rows,fn):
    with open(fn,'w') as f:
        f.write("parity %d;\n"%max(rows))
        for i in sorted(rows): p,o,s=rows[i]; f.write("%d %d %d %s;\n"%(i,p,o,",".join(map(str,sorted(set(s))))))
def probe(fn):
    best={}
    for rev in (0,1):
        env=dict(os.environ); 
        if rev: env['R2_REV']='1'
        else: env.pop('R2_REV',None)
        r=subprocess.run([O,'--dtl','--no-single','--no-wcwc','--no-loops',fn],capture_output=True,text=True,env=env,timeout=60).stderr
        m=re.search(r'R2PROBE(.*)',r)
        if not m: continue
        d={k:int(v) for k,v in re.findall(r'(\w+)=(-?\d+)',m.group(1))}
        best[rev]=d
    return best
rows=parse(src); ids=list(rows); cur=rows; tmp=os.path.join(outdir,'cur%d.pg'%seed)
def score(b): return sum(d['dup'] for d in b.values())
write(cur,tmp); b=probe(tmp); sc=score(b); found=0
for it in range(steps):
    new={i:[p,o,list(s)] for i,(p,o,s) in cur.items()}
    for _ in range(R.randint(1,3)):
        v=R.choice(ids); k=R.randrange(4)
        if k==0: new[v][2].append(R.choice(ids))
        elif k==1 and len(new[v][2])>1: new[v][2].remove(R.choice(new[v][2]))
        elif k==2: new[v][0]=max(0,new[v][0]+R.choice([-2,-1,1,2]))
        else: new[v][1]^=1
    write(new,tmp); b=probe(tmp); s2=score(b)
    bad=any(d[k]>0 for d in b.values() for k in ['ntf_viol','fm_viol','yz_viol','dom_nonstr','acyc_viol','tpr_bad','notop','dup_same'])
    if bad:
        found+=1; fn=os.path.join(outdir,'viol_s%d_i%d.pg'%(seed,it)); write(new,fn); print("VIOL",fn,b,flush=True)
    if s2>=sc and s2>0 or (sc==0):
        cur=new; sc=s2
print("END seed",seed,"score",sc,"viol",found,flush=True)
