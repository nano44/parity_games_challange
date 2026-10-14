# M2 counterexamples (PROVISIONAL: the pseudocode's faithfulness check by the REFEREE is pending)

## CE1: Theorem 2 / Algorithm 1 give the wrong winner (ce1_4v.pg)
Found 2026-10-14 by `compare.py` on a 100-game seeded corpus (`gen.py corpus DIR 100 5 --nmax 50`, game
`r00036_n18_d9_deg1-3_pe0.0_sl0_s992026059`, saved as ce1_18v_found.pg). `shrink.py` reduced it to 8 vertices
(ce1_8v_shrunk.pg); ce1_4v.pg is the same pattern written by hand. An exhaustive search found no counterexample with
<= 3 vertices and priorities in 0..2.

ce1_4v.pg (TARGET.md / Oink format, max-parity, owner 1 = Odd):
```
parity 3;
0 1 1 1;      v0: priority 1, Odd, -> v1
1 0 1 2,3;    v1: priority 0, Odd, -> v2 or v3
2 2 1 0;      v2: priority 2, Odd, -> v0
3 0 1 1;      v3: priority 0, Odd, -> v1
```
Every vertex is Odd's; Odd only chooses at v1. The two simple cycles are v1 v3 (priorities 0,0) and v0 v1 v2
(priorities 1,0,2, max 2). Both are even, so **Even wins every vertex** (brute force over positional strategies,
py Zielonka and Oink uzlk agree).

**avh.py returns Odd for every vertex.** Hand trace in the paper's min-parity (rho = 2 - priority:
rho(v0)=1, rho(v1)=2, rho(v2)=0, rho(v3)=2; the min-parity winner is the same, Even everywhere):
1. No self-loops, so the pre-routine does nothing. Algorithm 1: dhat = 2 (O = Even), dbar = 1 (tex:378-380).
2. A(G,1), player Odd. U_1(G) = {v0} (D1). A*_1(G) = {} (D2: only k = 0, and U_{-1} = {}).
3. A^0 = Odd-Attr(G,{v0}) = {v0,v1,v2,v3} (v2 -> v0; v1 is Odd's and moves to v2; v3 -> v1).
4. A'_1(G,A^0) = Even-Attr(G, {v in A^0 \ ({} u {v0}) : rho(v) < 1}) = Even-Attr(G,{v2}) = {v2}
   (v1 is Odd's and can move to v3 instead).
5. U^1 = U^0 \ Even-Attr(G, (V \ A^0) u A') = {v0} \ Even-Attr(G,{v2}) = {v0} \ {v2} = {v0} = U^0: fixpoint.
6. A(G,1) = A^0 = V. Algorithm 1 adds V to W_Odd (tex:383) and stops.
Theorem 2 (tex:322) says A(G,1) is an Odd-dominion; Even in fact wins all of it. Odd's only way to dodge A' is
the cycle v1 v3, which never returns to U = {v0}. The proof's case analysis (tex:326-332) does not cover plays that
avoid both A' and U forever.

Dependence on the ambiguities in notes/L-COMP.md: none of AM2-AM9 is involved (no self-loops; A = V, so
attractors in G or in A coincide; both players have priorities). AM1 (min-parity) is used as written in the paper.
Re-run: `python3 experiments/m2/avh.py experiments/m2/counterexamples/ce1_4v.pg --trace`.
