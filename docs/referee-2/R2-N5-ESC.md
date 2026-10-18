# R2-N5-ESC: does N5 (SSI-GLOBAL) leave van Dijk-Loho-Maat's candidate sets? — REFEREE-2, 2026-10-18 20:57Z (date -u)
Signature: (Opus 5.5, D12). This is the small packet from the Lead (20:53Z).

Read:
- docs/new/N5-ssi-global.md and experiments/new/dlm_gen.py at claude/l-new bdd53ae, in a detached worktree (l-new was not
  merged). I did NOT use n5.py.

Source opened: arXiv 2309.02223 (e-print main.tex, and pdf sha256 10e6794d82aba465…, which matches L-NEW's). Pages checked
with pdftotext:
- Algorithm 2 (SSI) p. 7;
- Algorithm 3 (generalized SSI) and the sets Jσ(τ), Jτ(σ) p. 8;
- Table 1 (family 1) p. 9;
- Lemma 12 ("the results … hold for any improvement rule f") p. 14;
- Theorem 13 (generalized SSI) p. 15;
- Table 2 (family 2) p. 13.
Tool: R2-N5-ESC/n5trace.py (my own code; output in trace.txt).
- It implements N5's steps 1-5 from N5-ssi-global.md.
- It computes valuations by brute force with the paper's sink-game play value Θ and the order ⊴ (§2):
  Ξσ = min over ALL Odd strategies, Ξτ = max over ALL Even strategies, pointwise.
- τ̄(v) is taken as the SET of choices of every pointwise-optimal Even response to τ, so "w ≠ τ̄(v)" holds for every
  admissible tie-break.
- Jσ(τ) and Jτ(σ) are exactly as in Algorithm 3.
- Each restricted one-player optimum of N5 (steps 2 and 3) is the pointwise optimum over all strategies in the restricted
  arena. It was unique at every iteration traced here (#optimal = 1), so no tie-breaking enters.

## Verdict: CONFIRMED (Opus 5.5, D12)
N5's step leaves Algorithm 2's candidate set on DLM family 1, n = 3. It leaves Algorithm 3's set Jσ(τ) on DLM family 2, n = 2.
On family 1 every N5 switch stays inside Algorithm 3's candidate sets. That is expected, since DLM note (opening of their §5: "The generalized version can solve the games from the previous section quickly") that
generalized SSI already solves family 1 quickly. The Algorithm 3 escape therefore needs family 2, and it occurs there at
exactly the move DLM's proof says generalized SSI postpones.

## 1. Generator against Table 1 (and Table 2)
Family 1 (Table 1, p. 9). Every node, owner, priority and successor list matches dlm_gen.py lines 14-18, and so does the start
pair (σ0(a_i) = a_{i+1}, τ0(d_i) = d_{i+1}, a_{n+1} and d_{n+1} → a_{n+1}). Node by node:
- a1: P0, priority 3, successors {a2, d2};
- a_i: P0, 2i+1, {a1, a_{i+1}, d_{i+1}};
- d1: P1, 4, {a2, d2};
- d_i: P1, 2i+2, {d1, a_{i+1}, d_{i+1}};
- a_{n+1}: P0, 1, self-loop;
- d_{n+1}: P1, 2n+4, {a_{n+1}}.
Family 2 (Table 2, p. 13). All ten node types, the N = 16n + 16 offsets, the bracketed (a1)/(d1) edges for i > 1, and all
twelve σ0/τ0 entries match lines 20-29. CORRECT.

## 2. Family 1, n = 3, from (σ0, τ0): the Algorithm 2 escape
The trace has 4 iterations, the same as n5.py's CSV row (dlm1, n = 3: 4 iterations, 0 fallbacks).
Iteration 1:
- Iσ = {(a1,d2), (a2,d3), (a3,d4)} and Iτ = {(d1,a2), (d2,a3), (d3,a4)}.
- N5's restricted Even optimum against τ0 switches all three: (a1,d2), (a2,d3), (a3,d4).
- Every optimal Even response τ̄ to τ0 has τ̄(a2) = a1 and τ̄(a3) = a1 (a unique optimum).
- So the switches (a2,d3) and (a3,d4) have w ≠ τ̄(v): they are NOT in Iσ ∩ {(v, τ̄(v))}, Algorithm 2's candidate set. In SSI only
  (a1,d2), with τ̄(a1) = d2, could be switched at this iteration.
- Likewise the Odd switches (d2,a3) and (d3,a4) have w ≠ σ̄(v) = d1.
- All six switches ARE in Iσ ∩ Jσ(τ) and Iτ ∩ Jτ(σ), so this step is also a generalized-SSI SWITCH-ALL step.
Iterations 2-4: (a2,a1), then (a2,a3), then (a1,a2) and (d1,d2). Each is the τ̄ or σ̄ edge and inside J. The run stops at the
optimum (σ(a3) = d4, τ(d3) = a4) after 4 iterations. SSI with SWITCH-ALL needs 2^{n+1} − 3 = 13 (Proposition 7).

## 3. Family 2, n = 2, from (σ0, τ0): the Algorithm 3 escape
The trace has 4 iterations, the same as N5-ssi-global.md's dlm2 row (2, 4, … for n = 1, 2). Generalized SSI needs
7·2^{n−1} − 5 = 9 (Proposition 11). n = 1 has 2 iterations, as in DLM's base case.
Iteration 1:
- Iσ = {(m1,f1), (m2,f2)} and Iτ = {(g1,k1), (g2,k2)}.
- N5 switches (m2, f2). Every optimal τ̄ has τ̄(m2) = a1, and Ξτ(f2) ◁ Ξτ(σ(m2)) = Ξτ(c2), so (m2,f2) ∉ Jσ(τ). It is outside
  Algorithm 3's candidate set Iσ ∩ Jσ(τ), and outside Algorithm 2's.
- Symmetrically, N5's Odd switch (g2,k2) ∉ Jτ(σ) (σ̄(g2) = d1).
- This is precisely the move DLM's proof of Proposition 11 relies on being postponed (p. 13: "So Ξτ(c_j) is much bigger …
  than Ξτ(f_j). Hence generalized SSI never makes the switch (m_j, f_j) in the beginning"). N5 makes it at once, because its
  choice is a one-player optimum in the arena restricted to Iσ, not a filter on Ξτ.

## 4. Comparison with n5.py's counts
| instance | my trace (pseudocode, brute-force valuations) | n5.py (L-NEW CSV) |
|---|---|---|
| family 1, n = 3 | 4 | 4 |
| family 2, n = 1 | 2 | 2 |
| family 2, n = 2 | 4 | 4 |
- No fallback occurred in my traces.

## Scope
This confirms the escape condition behind L-LIT's caveat 2 (T20): N5's step is not an instance of Algorithm 2 or Algorithm 3
with any improvement rule f, because on family 2 it selects an edge outside f's domain. So DLM's Theorem 1, Lemma 12 and
Theorem 13 do not apply to N5 as stated.

It says nothing about N5's worst case. Being outside DLM's barrier is a gauntlet step-3 fact, not a running-time bound.
