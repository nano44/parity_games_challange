# out16: DATA for P-N5-1E (L-SI successor 11, box 16)
outcheck.py runs N5 (experiments/new/n5.py run(), read-only import) and checks SPEC S5's output at the stop from definitions, on any game
class: (Z) W = own Zielonka's W_E; (SE) Even's output strategy wins W (plays stay in W, no odd-top cycle); (SO) the same for Odd's σ̄ on
V \ W; (B) on 𝒞^1E, ITER ≤ (n(n − 1) + d_e)(T*(n, m, Δ, d_e) + 1). MUT=1 reads the output at the start pair (cap 0): a control that must fail.
DATA, not proof. Rows of P-N5-1E §7 (run from this directory; each about a minute):
- python3 -I outcheck.py --rand 3000 4 14 11 any        > logs/rand_any.txt
- python3 -I outcheck.py --rand 3000 4 14 12 1E         > logs/rand_1E.txt
- python3 -I outcheck.py --rand 1000 15 30 13 1E        > logs/rand_1E_n15-30.txt
- MUT=1 python3 -I outcheck.py --rand 1000 4 14 14 any  > logs/mut_any.txt   (FAIL expected: 773 violations)
- python3 -I outcheck.py --list ../../new/box41/lib41.txt --starts 2 > logs/lib41.txt
Even-numbered random games start from S3, odd-numbered ones from a random start pair; list files from S3 and one random pair (seed 16).
