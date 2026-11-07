# REFEREE-2 succ. 30: byte test L-2 -> L-3 (W-3 + RC-2 in the Lead-ruled form)
import sys,hashlib
L2=open(sys.argv[1],encoding='utf-8').read(); L3=open(sys.argv[2],encoding='utf-8').read()
R=[("PAD 0 on 693,030 (state, vertex, world) triples of the S3 runs on Γ3,","PAD 0 on 693,030 (state, vertex, world) triples of the S3 runs on Γ3 (every vertex but the unused even self-loop of priority 2),"),
("1 (Odd, start edge) or 0 has an N5 run","1 (Odd, start edge) or 0, the pads indexed after the game's vertices in (a, b) order, has an N5 run")]
x=L2
for i,(a,b) in enumerate(R,1): print('R%d'%i,L2.count(a),L3.count(b)); x=x.replace(a,b)
print('eq',x==L3,hashlib.sha1(x.encode()).hexdigest(),len(x.encode()),L3.count('('),L3.count(')'),L3.count('|'),L3.count('\n'),'c_X' in L3)
d=m=0
for c in L3: d+=(c=='(')-(c==')'); m=min(m,d)
print('mindepth',m)
