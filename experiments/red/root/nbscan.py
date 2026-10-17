#!/usr/bin/env python3
"""L-RED box 8 (produced on Opus 5.5): one-edge neighbourhood scan used to find R35. For each listed vertex: delete each edge
(out-degree > 1), add each missing edge, flip the owner; score with root/permgap.py (LALGR_DIR, DTL_ORDER). Keeps variants with
hit, incomplete, near2 >= 8, max depth >= 2 or max k >= 3 in OUTDIR. NBFIT=depthfit scores with root/depthfit.py instead. Usage: nbscan.py BASE.pg v1,v2,... OUTDIR"""
import sys, os, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib
P = importlib.import_module(os.environ.get('NBFIT', 'permgap'))   # NBFIT=depthfit: root/depthfit.py
base=sys.argv[1]; vs=[int(x) for x in sys.argv[2].split(",")]; out=sys.argv[3]
lines=[l for l in open(base).read().split("\n") if l.strip()]
hdr=lines[0]; rows={}
for l in lines[1:]:
    a=l.rstrip(";").split(" "); rows[int(a[0])]=[int(a[1]),int(a[2]),[int(x) for x in a[3].split(",")]]
n=len(rows)
def write(rr,path):
    with open(path,"w") as f:
        f.write(hdr+"\n")
        for v in sorted(rr): f.write(f"{v} {rr[v][0]} {rr[v][1]} {','.join(map(str,sorted(rr[v][2])))};\n")
sys.setrecursionlimit(100000)
for v in vs:
    muts=[("del",w) for w in rows[v][2] if len(rows[v][2])>1]+[("add",w) for w in range(n) if w not in rows[v][2]]+[("own",None)]
    for kind,w in muts:
        rr={u:[a,b,list(c)] for u,(a,b,c) in rows.items()}
        if kind=="del": rr[v][2].remove(w)
        elif kind=="add": rr[v][2].append(w)
        else: rr[v][1]=1-rr[v][1]
        path=f"{out}/m_{v}_{kind}_{w}.pg"; write(rr,path)
        try: m=P.measure_game(P.pg.read(path), os.environ.get("DTL_ORDER","stable"))
        except Exception as e: m={"err":str(e)}
        print(v,kind,w,m,flush=True)
        if not (m.get("hit") or m.get("incomplete") or m.get("near2",0)>=8 or m.get("maxd",0)>=2 or m.get("maxk",0)>=3): os.remove(path)
