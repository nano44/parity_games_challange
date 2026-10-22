import sys,random
out,seed=sys.argv[1],int(sys.argv[2]); R=random.Random(seed)
def game(n,k):
    return [(R.randrange(k+1),R.randrange(2),sorted(set(R.randrange(n) for _ in range(R.randint(1,3))))) for i in range(n)]
parts=[game(R.randint(4,25),R.randint(2,8)) for _ in range(R.randint(1,4))]
rows=[];off=0
for g in parts:
    for (p,o,s) in g: rows.append([p,o,[x+off for x in s]])
    off+=len(g)
n=len(rows)
for _ in range(R.randint(0,4)):  # cross edges
    a=R.randrange(n); rows[a][2]=sorted(set(rows[a][2]+[R.randrange(n)]))
with open(out,'w') as f:
    f.write("parity %d;\n"%(n-1))
    for i,(p,o,s) in enumerate(rows): f.write("%d %d %d %s;\n"%(i,p,o,",".join(map(str,s))))
