# REFEREE-2 succ. 30: byte test P-N5-REACH L-3 -> L-4 (CHECKER C130 §5 R1-R4)
import sys, hashlib
L3 = open(sys.argv[1], encoding='utf-8').read(); L4 = open(sys.argv[2], encoding='utf-8').read()
R = [("0 standard states in 908 states of the S3 runs on Γ(G),",
      "σ(K0) = K1 and σ(K1) = K0 at all 908 states of the S3 runs on Γ(G) and 0 of them equal to R104's stated start off the movers,"),
     ("Corollary REAL-IDEAL-S3 no separate DATA,", "NO-REACH's no-improving-edge clause and Corollary REAL-IDEAL-S3 no separate DATA,"),
     ("n5b (SPEC mode) iteration counts equal on 28/28 games and Oink 8fbf0a7 --zlk with verify OK on 28/28",
      "n5b (SPEC mode) iteration counts equal on the 28 games Γ(G) and Γ3(G) of the 14 corpus genomes and Oink 8fbf0a7 --zlk with verify OK on the same 28"),
     ("n = 3 and n = 5 games with given start pairs", "the n = 3 and n = 5 games with the start pairs of packet §9 (instances A, B)")]
x = L3
for i, (a, b) in enumerate(R, 1): print('R%d old in L-3 %d new in L-4 %d' % (i, L3.count(a), L4.count(b))); x = x.replace(a, b)
d = m = 0
for c in L4: d += (c == '(') - (c == ')'); m = min(m, d)
print('L-3+R1..R4 == L-4', x == L4, hashlib.sha1(x.encode()).hexdigest(), len(x.encode()), 'lines', L4.count('\n'), '(', L4.count('('), ')', L4.count(')'), '|', L4.count('|'), 'mindepth', m)
