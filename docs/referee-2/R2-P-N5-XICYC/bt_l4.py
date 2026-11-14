# REFEREE-2 succ. 30: byte test P-N5-XICYC L-3 -> L-4 (CHECKER C132 §5 R1-R7, typed from C132 §5 with wrapped lines joined by one space)
import sys, hashlib
L3 = open(sys.argv[1], encoding='utf-8').read(); L4 = open(sys.argv[2], encoding='utf-8').read()
R = [("CONDITIONAL on P-N5-REACH's S3-START, PAD, K3, TAU3, ESC3, W3, not landed,",
      "CONDITIONAL on P-N5-REACH's S3-START, PAD, K3, TAU3, ESC3, W3 for every genome (RESULTS R117's entry signs S3-START, PAD, K3 and TAU3 for every genome and ESC3, W3 for acyclic Ξ-graphs; its line states S3-START and PAD for acyclic Ξ-graphs only; P-N5-XICYC §7 reads ESC3's and W3's proofs for every genome),"),
     (" (P-N5-XICYC, docs/new/P-N5-XICYC.md; L-NEW successor 59)", " (P-N5-XICYC, docs/new/P-N5-XICYC.md with its fixes entries 1-2, docs/new/P-N5-XICYC-fixes.md; L-NEW successor 59)"),
     ("T-CYC: no separate DATA (it follows from BR-SEG and CYC-COUNT);", "T-CYC: no separate DATA (it follows from BR-SEG and CYC-COUNT); DOM, STRICT and PATH (BR-SEG's proof): no separate DATA;"),
     ("RED-XI: no separate DATA (a reduction);", "RED-XI: no separate DATA (a reduction); REACH3-CYC's bounds on T3 and C: no separate DATA (they are T-CYC and CYC-COUNT read on Γ3);"),
     ("every random set is rand191.rgen", "every random genome set is rand191.rgen"),
     ("H0 is not checked by the tool, and these runs include steps at which H0 fails", "H0 is not checked by the tool, and these runs include steps at which H0 fails (388 of their 2,072 steps, counted by REFEREE R-P-N5-XICYC with one counter added to brseg_gen191.py, docs/referee/scratch/xicyc_logs/brseg_gen191_H0fail_2000_3_12.out)"),
     ("so nothing about N5′-xi's or N5's running time follows;", "so nothing about N5′-xi's or N5's running time follows; BR-SEG-G's proof (STRICT-G, PATH-G) and Lemma K2-r are referee-originated (REFEREE R-P-N5-XICYC §2.2 and §3.2, restated in P-N5-XICYC's fixes entry 2), signed by both referees;")]
x = L3
for i, (a, b) in enumerate(R, 1): print('R%d old in L-3 %d, new in L-4 %d' % (i, L3.count(a), L4.count(b))); x = x.replace(a, b)
d = m = 0
for c in L4: d += (c == '(') - (c == ')'); m = min(m, d)
print('L-3 + R1..R7 == L-4', x == L4, hashlib.sha1(x.encode()).hexdigest(), len(x.encode()), 'lines', L4.count('\n'), '(', L4.count('('), ')', L4.count(')'), '|', L4.count('|'), 'mindepth', m)
