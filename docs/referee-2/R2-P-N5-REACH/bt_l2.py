import sys,hashlib
L1=open(sys.argv[1],encoding='utf-8').read(); L2=open(sys.argv[2],encoding='utf-8').read()
R=[("0 failures of REACH3 in 454 genomes,","0 failures of REACH3 in 454 genomes, the β-free P-sets of NO-REACH 0 on 42,880 (state, vertex) pairs, S3-START 0 on 454 genomes, PAD 0 on 693,030 (state, vertex, world) triples of the S3 runs on Γ3, both DEAD SUBDIV instances re-run, Corollary REAL-IDEAL-S3 no separate DATA,"),
("the statement «S3 can be simulated on every game by subdividing every edge» is DEAD","the statement that, for every game and start pair, the game with every priority + 4 and every edge subdivided by an Even pad of priority 2 (Even, start edge), 1 (Odd, start edge) or 0 has an N5 run from S3 equal state for state and transition for transition (fallbacks included) to the run of the game from that start pair is DEAD"),
("outside {K2, K3, c_X}","outside K2, K3 and the unused even self-loop of priority 2")]
x=L1
for i,(a,b) in enumerate(R,1): print(i,L1.count(a),L2.count(b)); x=x.replace(a,b)
print('eq',x==L2,hashlib.sha1(x.encode()).hexdigest(),len(x.encode()),'c_X' in L2, L2.count('('),L2.count(')'),L2.count('|'),L2.count('\n'))
d=m=0
for c in L2: d+=(c=='(')-(c==')'); m=min(m,d)
print('mindepth',m)
