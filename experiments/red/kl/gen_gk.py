"""L-RED box 21 (produced on Opus 5.5): explicit generator for the N8a pivot families of docs/red/R53-n8a-counter.md (Lead 02:46Z item (i)).
The gadgets are written out below (no file reads), so this script alone reproduces every member.
  G_k: gadget klglobal_n16 (16 vertices)  + 2k isolated self-loops (owner Even) with priorities 29, 30, ..., 28 + 2k.
       dual pivots: global 8·n^{1+k} + 6, switch-all 5·n^{1+k} + 1, n = 16 + 2k.  sha1 k=0 179b2cd0…, k=1 cb9004b7…, k=2 0ffbeaf1…
  F_k: gadget klcount_n16 (16 vertices)   + 2k self-loops with priorities 33, ..., 32 + 2k.  switch-all 4·n^{3+k} + 3 (global 8).
  H_k: gadget klmin_n13 (13 vertices, the SMALLEST gadget: greedy shrink of klglobal_n16) + 2k self-loops with priorities 29, ..., 28 + 2k.
       dual pivots 4·n^{k+1} under BOTH rules (and under every rule that switches every Odd node having an admissible arc).
Usage: gen_gk.py G|F|H k > out.pg"""
import sys
GADGETS = {
 "G": "0 25 1 2,4,5,8,11,15;1 24 1 3,8,11,12;2 28 1 1,3,7,9,13;3 22 1 2,3,4,5,6,8,9,11,14,15;4 5 0 0,3,7,8,9,14;5 9 0 0,3,5,7,10,11;6 18 1 2,3,4,6,7,8,9,13,14;7 7 0 3,6,8,12,13,14,15;8 13 0 0,3,4,8,9,11;9 8 1 2,3,4,7,9,10,13,15;10 19 0 0,1,2,4,5,6,7,13;11 15 0 0,3,4,9,11,13,14;12 27 0 1,4,5;13 5 1 0,2,3,6,9,15;14 12 1 1,4,5,7,8;15 20 1 2,12,15",
 "F": "0 11 1 1,4,5,9,11,13,14;1 17 0 3,4;2 29 1 1,2,5,7,8,9,10,11,13,15;3 20 1 0,5,9,10,11,14,15;4 10 0 1,8,9,13,15;5 7 0 0,2,3,4,5,7,9,12,13,15;6 3 0 1,2,3,4,13,14;7 7 1 3,7,9,10,12,13;8 31 1 1,3,4,6,10,11,12,15;9 27 0 2,3,11;10 25 0 0,1,2,10;11 15 0 0,3,6,8,9,13,15;12 32 0 0,3,4,6,10,11,12,13,15;13 12 1 3,5,9;14 28 1 1,5,6,9,13,14;15 10 0 7,10",
 "H": "0 25 1 7;1 28 1 10;2 22 1 5;3 5 0 6,11;4 9 0 6,8;5 18 1 10;6 7 0 12;7 13 0 2,3;8 19 0 1,6;9 27 0 3,4;10 5 1 0;11 12 1 7;12 20 1 9"}
fam, k = sys.argv[1], int(sys.argv[2])
lines = [x + ";\n" for x in GADGETS[fam].split(";")]
n0 = len(lines); mx = max(int(x.split()[1]) for x in lines); n = n0 + 2 * k
sys.stdout.write("".join([f"parity {n - 1};\n"] + lines + [f"{n0 + i} {mx + 1 + i} 0 {n0 + i};\n" for i in range(2 * k)]))
