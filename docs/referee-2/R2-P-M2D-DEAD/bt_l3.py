# REFEREE-2 succ. 30: byte test P-M2D-DEAD L-2 -> L-3
import sys,hashlib
L2=open(sys.argv[1],encoding='utf-8').read(); L3=open(sys.argv[2],encoding='utf-8').read()
a="L-RED 52 (55557951, experiments/red/r214/lower3/)"; b="L-RED 52 (6e743ab1, experiments/red/r214/lower3/replay.out)"
print('old in L-2',L2.count(a),'new in L-3',L3.count(b)); x=L2.replace(a,b)
print('eq',x==L3,hashlib.sha1(x.encode()).hexdigest(),len(x.encode()),L3.count('('),L3.count(')'),L3.count('|'),L3.count('\n'))
d=m=0
for c in L3: d+=(c=='(')-(c==')'); m=min(m,d)
print('mindepth',m)
