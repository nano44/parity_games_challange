import sys,hashlib
L4=open(sys.argv[1],encoding='utf-8').read(); L5=open(sys.argv[2],encoding='utf-8').read()
R=[("REDUCE-XI 0 violations on 63,223 runs, equality on 59,502;",
    "REDUCE-XI 0 violations on 63,223 runs, equality T = 1 + #{t ≤ T − 1 : Mv_t ∩ Z ≠ ∅} on 59,502 (T = 1 + Σ_(z ∈ Z) moves(z) on 8,399);"),
   ("also pass_d3_D3.json and pass_d4_D4.json, D 3 and 4 with LM 0",
    "also pass_d3_D3.json from start 110100 and pass_d4_D4.json from start 01010111, D 3 and 4 with LM 0"),
   ("experiments/red/r213/out/m4_z4_r7.json, 𝓛^R_4: a Ξ-target",
    "experiments/red/r213/out/m4_z4_r7.json, 𝓛^R_4, its stored start 10111010: a Ξ-target")]
x=L4
for i,(a,b) in enumerate(R,1):
    print('R%d old count in L-4 %d, new count in L-5 %d'%(i,L4.count(a),L5.count(b))); x=x.replace(a,b)
print('L-4+R1..R3 == L-5:', x==L5, hashlib.sha1(x.encode()).hexdigest(), len(x.encode()))
print('lines',L5.count('\n'),'( )',L5.count('('),L5.count(')'),'|',L5.count('|'))
d=0;m=0
for c in L5:
    d+= (c=='(')-(c==')'); m=min(m,d)
print('min depth',m)
