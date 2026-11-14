import sys, os, json, glob, itertools
sys.argv=['x','frozen/experiments/new']
src=open('docs/referee-2/R2-P-IDEAL-MOVES/r2moves.py').read().replace("if __name__ == '__main__':\n    main()","")
exec(src)
P0='frozen/experiments/new/box150/check.py'; ns={"__file__":P0,"__name__":"lib"}; exec(open(P0).read().split("\nif __name__")[0], ns); Gen=ns["Gen"]
root='frozen/experiments/new'; n=bad=0
for f in sorted(glob.glob(root+'/box1[5-8][0-9]/**/*.json', recursive=True)):
    if not 150<=int(os.path.relpath(f,root)[3:6])<=187: continue
    try: raw=json.load(open(f)); g=G(raw)
    except Exception: continue
    if not isinstance(raw,dict) or not g.ok_lr(): continue
    L=Gen(raw)
    for st in (itertools.product((0,1),repeat=g.N) if g.N<=10 else [tuple(g.start)]):
        a=[tuple(s) for s in g.run(list(st))]; b,_=L.run(st); b=[tuple(s) for s in b]; n+=1
        if a!=b: bad+=1
print('runs',n,'mismatch',bad)
