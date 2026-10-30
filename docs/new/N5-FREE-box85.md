# N5-FREE (box 85): FREE returns classified exactly (LAT 93%, NT, GAP, IMM). Only GAP returns are blocked-edge late adoptions; LAT / NT / IMM are paid inside R89's GP* climb. Theorem FREE-RED (lane): FREE-POLY (indeed every return count) ⇐ R*_F and FL_F polynomial, R89's landed residuals. Lemma RET-ΞRISE (lane). No new per-class bound; the open core of R3-POLY is R*_F (W-better, Ξ-blocked edges)
L-NEW successor 38 (Opus 5.5), D14 / D18, Lead reading L40. Lead 2026-10-30 12:34Z: «BOX 85: FREE-POLY … Classify FREE returns exactly:
lateral, offered-not-taken, gap blocks. Then attempt a bound per class, or give the obstruction with an instance.» Written 12:36Z-13:10Z
(date -u). Working note, unrefereed. Labels: PROVED (lane) / CONJECTURE / DATA / READING. Not a TARGET.md claim. G-N5-TIME OPEN.

## 0. Sources and setting
- docs/new/N5-WAIT-box84.md (§1 definitions: self-routed block, REG / E0 / FREE returns; Theorem TRIPLE-RED).
- RESULTS R88 (l. 5630): BLOCKED edge at state q := «W-better than σ's choice at r_i but not a VJ00-improving edge of Ξ»; R*_T := «the
  transitions of F at which some Even vertex adopts an edge blocked at an earlier state of F»; Corollary FW-R*: «F has at most
  (n−1)(R*_T+1) W-changing transitions». RESULTS R89: Lemma GP*-RUN («R88's Lemma GP* and Corollary FW-R* hold on every W-run»), Lemma
  SUCC-MON, Lemma LATE-RISE, Corollary R*-RISE, Theorem STRETCH-RED (FL_S := «transitions with σ_{t+1} ≠ σ_t and W_{t+1} = W_t»).
- Facts used: W is non-decreasing inside a τ-stretch without S4c (S4a's σ_{t+1} is the one-player W-optimum of H_t ∋ σ_t); every
  transition of a W-run moves σ (box 84 §4).

## 1. Exact classification of FREE returns (Lead step 1)
- A FREE return of X to g (box 84 §1): last leave s → s + 1, return k → k + 1 inside a W-run F, and no state of [s + 1, k] has a
  self-routed block of (X, g). At state k, (X, g) ∈ Iσ_k and S4a takes it. Let Q := [s + 1, k − 1] (the states strictly in between).
  Exactly one class, by priority:
  - IMM: Q = ∅ (X returns at the next transition).
  - NT (offered, not taken): some q ∈ Q has (X, g) ∈ Iσ_q.
  - GAP: otherwise, some q ∈ Q has W_q(g) ▷ W_q(σ_q X) (then (X, g) is BLOCKED at q in R88's sense: W-better, not Ξ-improving).
  - LAT (lateral): otherwise. At every q ∈ Q, g is neither offered nor W-better than X's current choice, and g's σ̄-play avoids X.
- DATA (experiments/new/box85/freeclass.py on box 83's corpus, 1132 runs; freeclass_*.txt):

  | class | returns | max per (F, X, g) | instance of the max |
  | --- | --- | --- | --- |
  | LAT | 4,911 (93.4%) | 17 | topfix_n10 (n 210) |
  | NT | 231 | 1 | fc_3 (n 85) |
  | GAP | 115 | 1 | fc_3 |
  | IMM | 3 | 1 | nep76_n40 |
  | FREE total | 5,260 | 17 | topfix_n10 |

  5,174 of the 5,260 FREE returns have a W(g) change in [s, k]; the other 86 leave at a W-tie (TT; 88 counted at the leave). In the
  topfix family (n = 21N), the FREE maximum per edge (box 84 retclass) is 2N − 3 for N = 3, 4, 6, 8, 10 (3, 5, 9, 13, 17): linear
  (all LAT on topfix_n10).

## 2. Lemma RET-ΞRISE (PROVED, lane): every return is paid by a strict Ξ-rise of its target, with no tie term
- Statement. In every W-run F, for every Even edge (X, g): RET_F(X, g) ≤ ΞCH_F(g), the transitions of F at which Ξ(g) changes.
- Proof. Let the return at k → k + 1 have last leave s → s + 1, where X moved from g to h. S4a moves X only along Iσ_s, so
  Ξ_s(h) ▷ Ξ_s(g). At k, (X, g) ∈ Iσ_k, so Ξ_k(g) ▷ Ξ_k(σ_k X) ⊵ Ξ_(s+1)(σ_(s+1) X) = Ξ_(s+1)(h) ⊵ Ξ_s(h) ▷ Ξ_s(g) (R89 SUCC-MON;
  Ξ non-decreasing). So Ξ(g) changes at some transition in [s, k − 1]. The transition sets [s, k − 1] of successive returns of one edge
  are disjoint (the next leave comes after k). □
- This is the return-form of R89's LATE-RISE / R*-RISE; unlike RET-WCH (R93) it needs no TT term, but ΞCH can exceed WCH.
- DATA (xirise.py, corpus): 6,265 returns, 0 violations of the edge bound, 0 returns without a strict Ξ(g) rise. Max ΞCH_F(e) 63
  (gate_K64_n581); on pftheta34_n32 ΞCH reaches 34 = |F| while WCH is 7.

## 3. Theorem FREE-RED (PROVED, lane; a REDUCTION by composition of landed results)
- Statement. For every W-run F of N5 and every Even edge (X, g):
  FREE_F(X, g) ≤ RET_F(X, g) ≤ |F| ≤ (n − 1)(R*_F + 1) + FL_F,
  where R*_F is R88's count read on F (R89 GP*-RUN) and FL_F counts the transitions of F with W unchanged. Hence FREE-POLY, ALT-POLY and
  R3-POLY all follow from: R*_F ≤ p(n) and FL_F ≤ p(n) on every W-run.
- Proof. A return is a switch of X at one transition of F, and each transition carries at most one switch of X, so RET_F(X, g) ≤ |F|.
  Every transition of F changes W or is counted in FL_F. By R89 GP*-RUN, Corollary FW-R* holds on F: at most (n − 1)(R*_F + 1)
  transitions of F change W. □
- Which classes lie in R*. A GAP return adopts an edge that was BLOCKED at a state of Q ⊆ F, so its return transition is counted in R*_F
  (R88's definition). So is a REG return whose block state is W-better. LAT, NT and IMM returns never adopt a blocked edge: they are not
  in R*_F, and FREE-RED pays for them through GP*'s factor n − 1 per R*-epoch.
- DATA (xirise.py, corpus): FREE-RED's inequality 0 violations. Max R*_F 64 (gate_K64_n581, a W-run with 0 returns: all 64 are first
  adoptions of blocked edges); max FL_F 8 (u23sw64_n32). 886 of 1,132 runs have R*_F = 0 in every W-run, and 135 of those still have
  returns. Example: topfix_n10's 17 LAT returns of one edge lie in a W-run with R*_F = 0, FL_F = 0 and |F| = 58 ≤ n − 1 = 209.

## 4. Per-class bounds (Lead step 2): what is proved, what is open, the obstruction
- LAT, NT, IMM: no bound beyond FREE-RED. PROVED (lane, §3): each is at most |F| ≤ (n − 1)(R*_F + 1) + FL_F. So they are polynomial
  whenever R*_F and FL_F are. They are the GP* climb itself (box 80 ladder's "W(g) rises, then g is taken"), and R88 already bounds
  that climb by n − 1 between late adoptions.
- GAP: each is a late adoption of a blocked edge, counted by R*_F. R89 R*-RISE: late adoptions of an edge ≤ ΞCH_F(target). No polynomial
  bound on R*_F is known.
- CONJECTURE NT-1 / GAP-1 / IMM-1 (DATA only): at most one return of each of these classes per (F, X, g). Corpus maximum is 1 for all three.
  No proof attempted beyond the observation that NT needs S4a to decline an offered edge and then accept it later, which requires
  W(g) to overtake W(σX) (a W-change or a W-tie).
- OBSTRUCTION (exact). FREE returns add nothing to R3-POLY beyond R89's residuals R*_F and FL_F: the bulk (LAT) is paid inside GP*. So
  FREE-POLY is not a more tractable half. Its only hard part is R*_F, the same quantity that the REG side reduces to (box 84's REG
  returns with a W-better block are also late adoptions). R*_F counts adoptions of edges that are W-better but not Ξ-improving: the W/Ξ
  gap. This is R134's GAP-IN-PREFIX / TWO-SOURCE wall. The instance where R*_F is largest is gate_K64_n581 (R*_F = 64 ≈ 0.11n, with no
  returns), so R* can grow while returns stay 0. A bound on returns alone cannot control R*_F.
- READING. After boxes 84-85 the cleanest single target for R3-POLY is CONJECTURE R*-POLY: R*_F ≤ p(n) on every W-run, together with
  FL_F (the TIE residual; 0 in N5-LZC by R93 LZ-STRICT). Both are named residuals of the landed R89 STRETCH-RED, so this is a narrowing,
  not a new premise.

## DONE / FINDINGS / NEEDS
- DONE: experiments/new/box85/freeclass.py (FREE sub-classes), xirise.py (RET-ΞRISE, FREE-RED, R*_F, FL_F), run.sh / run2.sh,
  freeclass_*.txt, xirise_*.txt (corpus 1132 runs); check.sh "box 85".
- FINDINGS:
  1. DATA: FREE returns = LAT 4,911 / NT 231 / GAP 115 / IMM 3. Per (F, X, g): LAT ≤ 17 (topfix_n10; linear 2N − 3 in the family);
     NT, GAP and IMM ≤ 1.
  2. PROVED (lane) Lemma RET-ΞRISE: RET_F(X, g) ≤ ΞCH_F(g), with no tie term.
  3. PROVED (lane) Theorem FREE-RED: every return count ≤ |F| ≤ (n − 1)(R*_F + 1) + FL_F (R89 GP*-RUN with R88 FW-R*). GAP returns are
     late adoptions (in R*_F); LAT, NT and IMM are not, and are paid inside the GP* climb.
  4. CONJECTURES NT-1 / GAP-1 / IMM-1 (data) open; FREE-POLY open. Obstruction: FREE-POLY is not easier than R*-POLY. Its only hard part
     is R*_F (the W/Ξ gap, R134's wall); instance gate_K64_n581 has R*_F = 64 with 0 returns.
  5. READING: R3-POLY ⇐ R*-POLY ∧ FL-POLY, where R*-POLY := R*_F ≤ p(n) and FL-POLY := FL_F ≤ p(n) on every W-run (both R89 residuals).
     After the ladder recursion (box 84) and the GP* climb (here), the W/Ξ gap is the one place left.
- NEEDS: none from the owner. Lead: L-RED R136 aimed at FREE returns would meet GP*'s n − 1 per epoch. The productive adversary target is
  R*_F (blocked late adoptions) per W-run, now max 64 at n 581.
