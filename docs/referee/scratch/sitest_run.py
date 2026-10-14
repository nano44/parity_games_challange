# REFEREE throwaway: execution check of L-COMP pgsolver_si.py / pgsolver_port.py (claude/l-comp e3e7e4e) against Oink.
# Paths below point at my session scratchpad copies of the l-comp files; adjust to run elsewhere.
import sys, random, subprocess, tempfile, os, re, time
sys.path.insert(0, '/home/user/parity_games_challange/docs/referee/scratch'); import aiayn
S='/tmp/claude-0/-home-user-parity-games-challange/bf79b516-cc51-50c0-ab47-cd4e4df91359/scratchpad'
SI=S+'/lcomp/hard-families/pgsolver_si.py'; GEN=S+'/lcomp/hard-families/pgsolver_port.py'
O='/home/user/parity_games_challange/tools/oink/build/oink'
def oink(path):
    sol=tempfile.NamedTemporaryFile(suffix='.sol',delete=False).name
    subprocess.run([O,'--zlk',path,sol],capture_output=True,text=True); w={}
    for l in open(sol):
        p=l.strip().rstrip(';').split()
        if len(p)>=2 and p[0].isdigit(): w[int(p[0])]=int(p[1])
    os.unlink(sol); return w
def si(path, best=False):
    sol=tempfile.NamedTemporaryFile(suffix='.sol',delete=False).name
    r=subprocess.run([sys.executable,SI,path,sol]+(['--switchbest'] if best else []),capture_output=True,text=True,timeout=600)
    k=re.search(r'solved with (\d+) iterations',r.stderr); w={}
    if os.path.exists(sol):
        for l in open(sol):
            p=l.strip().rstrip(';').split()
            if len(p)>=2 and p[0].isdigit(): w[int(p[0])]=int(p[1])
        os.unlink(sol)
    return w,(int(k.group(1)) if k else None),r.stderr[-300:]
rng=random.Random(42); N=150; bad={False:0,True:0}; err={False:0,True:0}
for t in range(N):
    G=aiayn.random_game(rng, rng.randint(2,9), 6, 3)
    f=tempfile.NamedTemporaryFile('w',suffix='.pg',delete=False); f.write(aiayn.to_pg(G, maxparity=True)); f.close()
    z=oink(f.name)
    for best in (False,True):
        w,k,e=si(f.name,best)
        if k is None: err[best]+=1; print('ERROR',best,aiayn.to_pg(G),e)
        elif w!=z: bad[best]+=1; print('MISMATCH',best,aiayn.to_pg(G),z,w)
    os.unlink(f.name)
print(f'random: {N} games; switchall mismatches={bad[False]} errors={err[False]}; switchbest mismatches={bad[True]} errors={err[True]}')
for fam,best in (('switchallexp',False),('switchbestexp',True),('switchallexp',True),('switchbestexp',False)):
    row=[]
    for n in range(1,7):
        f=tempfile.NamedTemporaryFile('w',suffix='.pg',delete=False)
        txt=subprocess.run([sys.executable,GEN,fam,str(n)],capture_output=True,text=True).stdout; f.write(txt); f.close()
        nn=len([l for l in txt.splitlines() if l and not l.startswith('parity')])
        t0=time.time(); w,k,e=si(f.name,best); z=oink(f.name)
        row.append((n,nn,k,'ok' if w==z else 'REGION-MISMATCH',round(time.time()-t0,1))); os.unlink(f.name)
        if time.time()-t0>120: break
    print(fam,'policy',('switchbest' if best else 'switchall'),'(n, vertices, iterations, regions vs oink, sec):',row)
