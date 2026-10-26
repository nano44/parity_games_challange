# R2-N5-HON: REFEREE-2 report on packet P-N5-HON (W-honest states per phase; u-runs; REC-1)
Referee: REFEREE-2 successor 16 (session_01R1scbTA9MiKutHRhRdi3zh), Opus 5.5 (D15, L37). Written 2026-10-26 10:27Z (date -u).
Object: docs/new/P-N5-HON-box46.md, sha1 07f8e767cfca12d29c8f6f2e3f03358326abbef1 (`git show 31835c4b:docs/new/P-N5-HON-box46.md | sha1sum`;
the same blob at l-new 67a7b54d), pinned at trunk 31835c4b, frozen. Author L-NEW successor 25.
Independence: written before opening any REFEREE file on HON. `git fetch origin claude/referee` and
`git ls-tree --name-only -r origin/claude/referee docs/referee/ | grep -ic hon` gave 0 at 10:13Z and 0 at 10:27Z (same turn as the push).
The lane's tools (experiments/new/box46/*.py) were NOT run or imported.
Checker: docs/referee-2/R2-N5-HON/hon_check.py (own), on succ. 13's SPEC loop (R2-N5-DUAL/dual_check.Runner, on si.py = SPEC S1's own
implementation, read-only); Ξ and W are my own play values (R2-N5-RUND/rund_check.py); N5^τ is my own loop (S4b^τ as in RESULTS R64).
Scope (D1): HON counts one kind of state; REC-1 is a reduction. Not a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Verdicts
| item | verdict | premises beyond the packet's text |
| --- | --- | --- |
| §1 Lemma HON | SIGN | P1 (R15 (a), (d) on SPEC's Ξ via (VJ)), P2 (WM; R18 (d) S (c)) |
| §2 Lemma SAT0 | SIGN (N-HON-1, wording) | none (R17 (V1), (V2) only) |
| §2 Lemma HON-FB (i)-(iv) | SIGN | P1 (R15 (a), XW), P2 (S (c) at a returned σ) |
| §2 Corollary HON′ | SIGN | as HON |
| §2 Corollary HON-0 (a)-(c) | SIGN | as HON |
| §2 relation to REC-0 (HON-0 ⇒ REC-0's inequality and corollary; difference f·n + 2; proofs independent) | CONFIRMED (both claims) | — |
| §3 Lemma RESTRICT_u (i)-(iv) | SIGN | P1 (Lemma S (a) on G and G^u), standing as in R64 (N-EPR-1) |
| §3 Corollary REPRO_u (with EPR-1) | SIGN | as RESTRICT_u |
| §3 Corollary EP-1u | SIGN as an IMPLICATION from (Στ) | (Στ) as in R64 (e); R51 (a) |
| §4 Theorem REC-1 (a) | SIGN | as HON |
| §4 Theorem REC-1 (b), (c), (d) | SIGN as IMPLICATIONS from (Στ) | via EP-1u |
| Q-R17 (in HON's own use) | YES (N-HON-2) | — |
No gap. Notes N-HON-1..5 (§3). Not reviewed, as instructed: §5 (HON-FF, OPEN; the DEAD items), §6 (DATA), every READING.
P1, P2 = the standing SPEC premise 1E-N3 (RESULTS R57) in its two forms (as in my R2-N5-RUND): P1 S1's σ̄ is Odd's pointwise optimum in
G_σ (so SPEC's Ξ is VJ00's Ω_σ, (VJ)); P2 S4a's output is Even's pointwise optimum in its arena against τ (R18 (d) Lemma S (c), landed "⇒"
form). The packet names 1E-N3 in its premise list (good).
R65 (landed at f7308227 after the pin): (Στ) as the packet uses it is word for word R64 (e)'s premise, which R65 finds to hold "at the strength
of that audit" (CHECKED, not signed). So EP-1u and REC-1 (b)-(d) hold at R65's audit strength; I sign them as the packet states them, as
implications.

## 1. Premises, complete list
SPEC S1, S2, S4a, S4b, S4c with FIX 3 (an in-phase fallback is Even's); phase = maximal run with (λ, τ) constant (R38 (a) KEY); R15 (a) (Ξ
non-decreasing, also across S4c fallbacks: R15 (d) says every N5 iteration is Switch_I with ∅ ≠ I ⊆ Iσ or ⊆ Iτ), R15 (d) (≤ 4n(n − 1)
consecutive iterations with Ωσ, Ωτ both unchanged), both on SPEC's Ξ through (VJ) (P1); R17 (a) (V1), (V2), (F1), (F2); R17 (b) Lemma P's
induction step (box 10 §2 A1, A2, B1, B2) and R17 (c)'s case split (box 10 §3), R17 (d); R18 (d) Lemma S (a) (= (VJ), R57 (a)) and S (c) (P2);
R21 (a) XW (P1); R23 (g) WM (P2; = R62 (d) WM-G); R64 (a), (b) proofs (P-N5-EPR §1, §2 at sha1 8fecca79, opened) with EPR-1; R64 (e)'s (Στ)
and R51 (a)'s T* for the implications. Context only: P-N5-REC0 (sha1 343239b5, opened; Lemma REC-0 and its Corollary read at §1 l. 43-48).

## 2. Proof check (line by line; my reading)
- HON step 0. Ξ_{k+1} ⊵ Ξ_k at every transition of P (R15 (a), fallbacks included); the simple paths of G_τ and the cycle nodes of λ are
  fixed on P; LEV ≥ 0 since Ξ_k(c) = (c, ∅, 0) at a cycle node. CORRECT.
- HON step 1. WM chain over a fallback-free gap; the sandwich W_h(v) ⊴ W_{h+1}(v) ⊴ W_{h′}(v) with both ends of cycle node λ(v) fixes
  W_{h+1}'s cycle node (reward first, rewards injective); at W-honest h, Iσ_h = W-improving set of G_τ, so S4a's arena is switch-best's;
  σ_{h+1} an arena optimum (P2); Lemma P's step with the hypothesis for ≤ LEV(h) edges gives W_{h+1} ⪰ value(r) for ≤ LEV(h) + 1 edges;
  WM to h′. CORRECT (Q-R17, N-HON-2).
- HON step 2. At W-honest h, Ξ_h(x) is value(r_x) for x's W-play prefix r_x (simple, to λ(x)), so Ξ_h ⊴ B; LEV = n − 1 gives ⊵. CORRECT.
- HON step 3. Saturation persists (step 0); i < s: fallback in the gap or a rise ≥ 1; LEV(h_1) ≥ 0, LEV(h_s) ≤ n − 2, LEV never drops, so
  ≤ n − 2 fallback-free gaps and ≤ f gaps with a fallback (gaps are disjoint): s ≤ f + n − 1. Tail: Ξ = B at t and h_N, so Ξ is constant on
  [t, h_N] (monotone + antisymmetric total order); τ constant ⇒ Ωτ constant; R15 (d): h_N − t ≤ 4n(n − 1). Arithmetic
  (f + n − 1) + 4n(n − 1) + 1 = f + 4n² − 3n; the cases s = 0 and s = N are inside the bound (n ≥ 1). CORRECT.
- SAT0. Even x: Case A of Lemma P (A1, A2) with W_k(z) ⪯ W_k(σ_k x) and the IH. Odd x, not its own W-cycle node: (V1), (V2) (N-HON-1).
  Odd x its own W-cycle node: W_k(z) has cycle node x, value(r′) has c ≠ x, so x is better than c. W-honest ⇒ W-cycle nodes = λ's ⇒ LEV =
  n − 1. CORRECT.
- HON-FB. Even's fallback (FIX 3, τ kept); S4a returned σ_h, so σ_h is an arena optimum (S (c), landed "⇒" form); arena = switch-best's.
  (i) I re-derived the case split: x off π and off c's cycle ⇒ x ⊕ W_h(z) ≻ W_h(x) (strict (V2), or a better cycle node if x is its own);
  x on c's cycle, off π ⇒ P(π) ≠ ∅ with even top gives a better cycle node, P(π) = ∅ gives x ⊕ W_h(z) ≻ W_h(x) by length; x ∈ π ⇒ D ≠ ∅ gives
  an even top above c (better cycle node), D = ∅ forces c odd and then top(Z) ≠ c is better for Even than c, so only top(Z) = c = x
  remains (box 10 §2 B2 says exactly this). (ii) two switched vertices are distinct cycle nodes, so no switched x′ lies on z*'s path to x;
  every play keeps its prefix to its cycle node. (iii) a new improving w would beat z* in Iσ_h(x). (iv) Ξ_h ⊴ Ξ_{h+1} ⊴ W_{h+1} = W_h = Ξ_h;
  Iσ_{h+1} = ∅ ⇒ τ changes (S4b or Odd's S4c) or the run stops. CORRECT.
- HON′. A fallback at h_i (i < s) would make h_{i+1} = h_i + 1 saturated (HON-FB (iv)); so each fallback-carrying gap holds a fallback at a
  non-W-honest state strictly inside it, counted by f_in. CORRECT.
- HON-0. D = ∅ ⇒ σ̄ = τ on Q and off Q ⇒ W-honest; epochs disjoint, non-empty; one source per transition. CORRECT.
- Relation to REC-0. REC-0 (P-N5-REC0 §1): N_0 ≤ (f + 1)(n + 1) + 4n(n − 1) + 1, corollary ×(n + m) over "the in-phase transitions of P whose
  source lies in a D = ∅ epoch", the same set as HON-0 (c). (f + 1)(n + 1) + 4n² − 4n + 1 − (f + 4n² − 3n) = f·n + 2 (checked symbolically and
  per phase in data); f_in ≤ f. HON's proof (§1, §2) cites none of REC-0, SN-PREFIX_D, EP-0. Both claims CONFIRMED.
- RESTRICT_u. R64 (a)'s proof uses the epoch only in (i) through "σ̄_E is an Odd strategy of G′_E and σ̄_k = σ̄_E" (quote verbatim, P-N5-EPR
  §1); here σ̄_k is a strategy of G^u (D_k ⊆ {u}; out-degree-1 Odd vertices; u keeps all edges), and Lemma S (a) on G and G^u gives Ξ′ = Ξ.
  (ii) same arena and switch-all; (iii) same graph for τ's dual valuation (Even keeps all edges in both); (iv) in-phase ⇒ S4b on G returned τ
  ⇒ τ optimal in H′_G ⊇ G^u's S4b arena. CORRECT.
- REPRO_u. R64 (b)'s induction at k ∈ [x, y′ − 1] ⊆ J (y′ = y + 1 iff y → y + 1 is in-phase); fallback types agree; λ′ = λ on J only (EPR-1).
  CORRECT.
- EP-1u. All len(J) transitions but possibly the one from y are in-phase transitions of the FIRST phase of the N5^τ run on G^u ∈ 𝒞^1O from
  (σ_x, τ) (d_o = deg(u) ≥ 2, any d_o is covered by (Στ)); that phase has ≤ T*(G^u) of them. CORRECT as an implication.
- REC-1 (a). An interval not at P's start starts after an in-phase transition k → k + 1 inside P whose source has D_k = ∅ (distinct k, HON-0
  (a)), or |D_k| = 1, D_k ≠ D_{k+1} (X_dir), or |D_k| ≥ 2 (X_big); + 1 for P's first state. CORRECT.
- REC-1 (b)-(d). I ⊆ one u-run J; every state of I but possibly P's last is a source counted in len(J): |I| ≤ len(J) + 1 ≤ T*(G^u) + 2;
  (c) = (a) × (b) and epochs ⊆ intervals; (d) states = D = ∅ states + |D| = 1 states. CORRECT as implications.

## 3. Notes (no gap)
- N-HON-1 (SAT0 wording). In the Odd case "x is not its own W-cycle node", the parenthesis "(r′ and z's play avoid x)" is false when x lies on
  its own W-cycle without being its cycle node (z = τ(x) is then on that cycle and z's play passes x). The conclusion stands by Lemma P's A1
  sentence: such an x is ranked below its cycle node, so it is in no path set, and (V1), (V2) apply. Suggested text: "(r′ avoids x; z's play
  avoids x or passes it only as a cycle vertex ranked below its cycle node)".
- N-HON-2 (Q-R17 in HON's use). YES. At h → h + 1 the step uses exactly: the hypothesis W_h ⪰ value(r′) for all r′ with ≤ LEV(h) edges to a
  cycle node of λ (= a W-cycle node at h, since λ_W = λ at a W-honest state); σ_{h+1} an optimum of the switch-best arena of G_τ at σ_h (P2);
  (F1)/(F2), including (MON) W_{h+1} ⊵ W_h; (V1) and strict (V2); and "no vertex changes its W-cycle node from h to h + 1", which HON proves by
  the sandwich, not from a phase start. Nothing else (same answer as succ. 15 for REC-0, with the W-cycle-node condition read at h).
- N-HON-3 (premises named). The packet's list is complete; P1 enters through R15 (a), (d) (on SPEC's Ξ only through (VJ), as R60 lists it)
  and XW; P2 through WM and S (c). HON-FB uses S (c) in its landed "⇒" form (σ_h returned by S4a); HON step 1 uses it for σ_{h+1} (an S4a
  output) — both are the standing premise, as in R55 / R62.
- N-HON-4 (R65). See §0: at R65's audit strength EP-1u and REC-1 (b)-(d) hold without the "(Στ)" hypothesis; signed here as implications.
- N-HON-5 (data thin where the proofs are subtle). In-gap fallbacks (f_in) occur in 9 phases (16 fallbacks) of my library runs and in none of
  my random runs; exact LEV (n ≤ 11) meets only 128 library step-1 checks; the HON bound is never approached (max 57 W-honest states in a
  phase, x32_rand64, n = 64; S3 tail spans ≤ 2); mutation hon (bound f_in + n − 1, the saturated tail dropped) does NOT bite. T* is
  astronomically large, so EP-1u and REC-1 (b)-(d) are tested only in their structural parts (|I| ≤ len(J) + 1; REPRO_u).

## 4. Data (DATA, not proof)
### 4.1 What the checker does
Per N5 run: phases, epochs, D_k (Q = Odd vertices of out-degree ≥ 2), W-honest states, f, f_in; LEV EXACT for n ≤ 11 (all simple paths of
G_τ to cycle nodes of λ, paths may pass other cycle nodes); HON / HON′ per phase; steps 0-3; SAT0 at every state with no W-improving edge
(exhaustive paths, n ≤ 11); HON-FB (i)-(iv) at every W-honest fallback; HON-0 (a)-(c) and REC-0's bound and difference per phase;
RESTRICT_u (i)-(iv) on G^u at every state with D_k ⊆ {u} (for D_k = ∅ the first ≤ 3 u ∈ Q); REPRO_u for every u-run by my own N5^τ on G^u
(states, fallback types, λ′ = λ on J); REC-1 (a) per phase with entries classified; (b) structural part; (b)-(d) against T* (vacuous).
### 4.2 Sets (0 violations in every set)
| set | N5 runs | states | phases | exact step-1 checks | SAT0 states | HON-FB cases | f_in (phases / total) | RESTRICT_u checks ((iv)) | REPRO_u runs | {u}-intervals (start / D = ∅ / X_dir / X_big) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| packet + lane instances (immp_cex_n11 + .start, immfail_n14, b5_o11, b4_n5_other_0, thclimb_n12_s11, so_th_n32, exitr_cex_n16, div_n8 + .start) | 8 | 97 | 21 | 2 | 9 | 1 | 0 / 0 | 104 (4) | 26 | 17 (7 / 10 / 0 / 0) |
| lib41 minus referee games × 3 starts | 1,230 | 19,667 | 7,173 | 55 | 1,773 | 69 | 4 / 6 | 17,274 (1,575) | 4,896 | 2,384 (2,160 / 208 / 1 / 15) |
| my 503 𝒞^1O files × 2 starts | 1,006 | 17,862 | 4,157 | 73 | 1,125 | 61 | 5 / 10 | 17,862 (1,422) | 4,157 | 2,641 (2,438 / 203 / 0 / 0) |
| random 2 Odd choices, n 5-11 (3,000 × 3) | 9,000 | 20,725 | 19,629 | 791 | 11,943 | 219 | 0 / 0 | 29,542 (74) | 27,570 | 6,489 (6,440 / 41 / 5 / 3) |
| random 3 Odd choices, n 6-11 (2,000 × 3) | 6,000 | 14,994 | 14,368 | 402 | 8,773 | 148 | 0 / 0 | 25,084 (66) | 23,513 | 4,280 (4,241 / 29 / 4 / 6) |
| random 4 Odd choices, n 8-11 (1,500 × 3) | 4,500 | 12,289 | 11,736 | 346 | 6,834 | 159 | 0 / 0 | 18,750 (34) | 17,358 | 3,092 (3,071 / 16 / 3 / 2) |
| random kO, n 12-20 (800 × 2; LEV not exact) | 1,600 | 5,185 | 4,894 | 0 | 2,327 | 55 | 0 / 0 | 6,881 (10) | 6,255 | 1,184 (1,173 / 7 / 1 / 3) |
Exact-LEV checks (n ≤ 11): S0 49,223 states, S2 22,803, S3 22,143 phases. Extremes: longest u-run reproduced by N5^τ on G^u 112 transitions
(xsn91_n48, u = 0); longest {u}-interval 111 states (same); max {u}-intervals in a phase 6 (so_th_n32); max N_0 5 (w24b_thc24_final).
Comparable lane numbers agree: max W-honest states in a phase 57 on lib41 (lane §6: 57). Logs: R2-N5-HON/logs/; reproduce `run_all.sh`.
### 4.3 Mutations (must fail)
On lib41 minus referee games, S3 start: fb4 (HON-FB (iv) asks h + 1 NOT last) 26 FAIL; ru (G^u with u cut to τ(u)) 5,722 RESTRICT_u (i) +
585 λ′ + 214 REPRO FAIL; r1 (REC-1 (a) without "1 +" and the D = ∅ term) 741 FAIL; s1 (Lemma P step with LEV(h) + 2) 4 FAIL. hon (N-HON-5)
does NOT bite.

## 5. Signatures
Lemma HON, Lemma SAT0, Lemma HON-FB (i)-(iv), Corollary HON′, Corollary HON-0 (a)-(c), Lemma RESTRICT_u (i)-(iv), Corollary REPRO_u (with
EPR-1), Theorem REC-1 (a): SIGN, on every game, under the standing SPEC premise 1E-N3 (P1, P2). Corollary EP-1u and Theorem REC-1 (b)-(d):
SIGN as IMPLICATIONS from (Στ) (which holds at R65's audit strength). The §2 relation to REC-0: both claims CONFIRMED. Q-R17: YES. No gap;
notes N-HON-1..5. REFEREE-2 successor 16 (Opus 5.5, D15).
