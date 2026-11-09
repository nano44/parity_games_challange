import json,os,sys,copy
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); from ablate37 import *
os.chdir(os.path.join(H,'../box36'))
mv=json.load(open(os.environ['SP']+'/mv_named.json'))
ga=[tuple(q) for q in Mw['gate']]; a=[tuple(q) for q in Mw['br']]
def ev(Nd):
    G=from_named(Nd); r=measure(G); return qflips(G,Nd,r['rows']),r['C'],r['T3']
def withmoves(moves):
    d=copy.deepcopy(mv); d['gate']=ga; o=list(a)
    for q,after in moves: o.remove(q); o.insert(o.index(after)+1,q)
    d['br']=o; [m for m in d['movers'] if m[0]=='a47'][0][2][1]['bp']=0; return d
mode=sys.argv[1]
if mode=='R':
    for j in range(1,53): print('R9 after a%d,1'%j, ev(withmoves([(('a46',0),('a30',1)),(('R',9),('a%d'%j,1))])), flush=True)
elif mode=='A':
    for j in range(1,53): print('a46,0 after a%d,1'%j, ev(withmoves([(('a46',0),('a%d'%j,1)),(('R',9),('a5',1))])), flush=True)
else:
    for i in range(1,53): print('a%d,0 after a30,1'%i, ev(withmoves([(('a%d'%i,0),('a30',1)),(('R',9),('a5',1))])), flush=True)
