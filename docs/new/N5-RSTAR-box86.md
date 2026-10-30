# N5-RSTAR (box 86): R*-POLY stays OPEN. Lemma GAP-DEV (lane): every blocked target has a strict W/Ξ gap carried by an Odd deviation from τ on its σ̄-play. DEV-CAP DEAD (gate_K16_n197). RSTAR-PCH: R*_F ≤ m_E·n·(n + P*_F), a composition of landed R86 / R89 lemmas, so R*-POLY routes back to R86's P* (Ξ path-set changes). D18 screen: WQO / Dickson DEAD (tight lower bounds, opened source); exchange / simplex READING only (Friedmann); potential over GP* chosen, it ends at P*
L-NEW successor 38 (Opus 5.5), D14 / D18, Lead reading L40. Lead 2026-10-30 13:06Z: «BOX 86 = R*_F per W-run (blocked late adoptions);
FL_F is secondary. Goal: R*-POLY … Alternatively, an exact obstruction plus the instance that kills it.» D18 (owner, verbatim): "Explore
novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together."
Written 2026-10-30 13:10Z-13:50Z (date -u). Working note, unrefereed. Labels: PROVED (lane) / DEAD / CONJECTURE / DATA / READING. Not a
TARGET.md claim. G-N5-TIME OPEN.

## 0. Sources, definitions, the R137 line
- RESULTS R88 (BLOCKED edge, R*_T, Lemma GP*, Corollary FW-R*), R89 (W-run, GP*-RUN, SUCC-MON, LATE-RISE, Corollary R*-RISE: «in a W-run
  F the late adoptions of each Even edge (y, z) are at most the transitions of F at which Ξ(z) changes»), R86 (Lemma LEN-MONO: «RISE_R(c) ≤
  PCH_R(c) + (PCH_R(c) + 1)(n − 1) on every λ-run R»; Theorem COMPOSE, Corollary COMPOSE-RUN, Corollary COMPOSE-NM; P*, NM*).
  docs/new/N5-FREE-box85.md (Theorem FREE-RED).
- R*_F (R88, read on a W-run F by R89 GP*-RUN) := the transitions of F at which some Even y adopts an edge (y, z) that was BLOCKED at an
  earlier state q of F: W_q(z) ▷ W_q(σ_q y) and (y, z) ∉ Iσ_q. R*-POLY := R*_F ≤ p(n) on every W-run of N5.
- Opened outside sources (D18): [FFSS] D. Figueira, S. Figueira, S. Schmitz, Ph. Schnoebelen, "Ackermannian and Primitive-Recursive Bounds
  with Dickson's Lemma", arXiv 1007.2989 (LICS 2011), Proposition 5.2 and Proposition 6.3, Remark 6.4, and the introduction ("these
  bounds are tight even when considering the coarser lexicographic ordering"). [Fr09] O. Friedmann, "A Super-Polynomial Lower Bound for the
  Parity Game Strategy Improvement Algorithm as We Know it", arXiv 0901.2731: abstract only («a family of games of quadratic size on
  which the algorithm requires exponentially many strategy iterations»). The abstract does not name the improvement rule, and I did not
  open the body.
- R137 line (Lead's request; L-RED pin experiments/red/free/instances/fx_K8_m32.pg, sha1 e995709e…, with its .start; my tools
  box85/freeclass.py, box85/xirise.py): n 250, one W-run, |F| = 280; FREE 836, all LAT (max 64 at one edge), REG = E0 = NT = GAP = IMM = 0;
  R*_F = 16, FL_F = 0, max WCH 137, max ΞCH 137. FREE-RED holds: 280 ≤ (n − 1)(R*_F + 1) + FL_F = 4233.

## 1. Lemma GAP-DEV (PROVED, lane): a blocked target carries a strict W/Ξ gap, and the gap is an Odd deviation from τ
- Statement. If (y, z) is BLOCKED at state q of a W-run (τ = τ_q), then Ξ_q(z) ◁ W_q(z). Moreover the (σ_q, σ̄_q)-play from z contains an
  Odd vertex o with σ̄_q(o) ≠ τ(o).
- Proof. σ̄_q is Odd's pointwise optimum against σ_q (S1), so Ξ_q(v) ⊴ val(σ_q, τ)(v) = W_q(v) for every v. Hence W_q(z) ▷ W_q(σ_q y)
  ⊵ Ξ_q(σ_q y) ⊵ Ξ_q(z), the last step because (y, z) ∉ Iσ_q (S2). If the σ̄_q-play from z used τ at each of its Odd vertices, it would
  be the (σ_q, τ)-play, and Ξ_q(z) = W_q(z). □
- DATA (box86/rstar.py, corpus 1132 runs): 116,086 blocked (edge, state) records, 0 violations.
- READING. R* is a count of DELAYED RELAXATIONS in R88's Bellman-Ford picture (GP*): W climbs like Bellman-Ford over G_τ, an edge whose
  target is "poisoned" by an Odd deviation σ̄ ≠ τ is withheld, and each release restarts at most n − 1 rounds. GAP-DEV names the poison.

## 2. DEAD: DEV-CAP (R*_F ≤ the number of distinct Odd deviation edges seen in F)
- Motivation: if every release used up one deviation edge, R*_F ≤ m_O.
- Instance: red/usplit/instances/gate_K16_n197.pg with its .start (box86/rstar.py): one W-run, R*_F = 16, but the union over F of
  DEV_t := {(o, σ̄_t(o)) : σ̄_t(o) ≠ τ(o)} has 5 edges. DEV_t changes 16 times (= R*_F). Corpus: DEV-CAP fails in 60 W-runs (58 games,
  e.g. fc_3, b6_xl_n32-n48). Obstruction: one deviation edge poisons a whole lateral fan of targets, and they are released one per
  transition as Even's switches move the deviation's effect. The same edge serves many releases. In R137's fx_K8_m32 DEV_t changes once
  while R*_F = 16.

## 3. RSTAR-PCH (PROVED, lane; a COMPOSITION of landed lemmas, no new premise)
- Statement. For every W-run F: R*_F ≤ Σ_(y, z) Even edge ΞCH_F(z) ≤ m_E · n · (n + 1 + P*_F), where P*_F := max_z PCH_F(z) and PCH_F(z)
  counts the transitions of F at which the path set of Ξ(z) changes while λ(Ξ(z)) does not.
- Proof. A transition counted in R*_F carries at least one late adoption, so R*_F ≤ Σ_(y, z) LATE_F(y, z) ≤ Σ_(y, z) ΞCH_F(z)
  (R89 R*-RISE). Fix z and follow Ξ(z) over F; it is non-decreasing. (i) λ(Ξ(z)) changes at most n − 1 times in the whole N5 run: the
  order compares rew(λ) first, rew is injective, and so each change strictly raises rew(λ). (ii) Between changes of the pair
  (λ, P)(Ξ(z)) only the length moves. With (λ, P) fixed the valuations form an interval of the order (box 84 Fact CONVEX) with at most n
  members (ℓ ∈ [0, n − 1]), so each such block has at most n − 1 changes. The blocks number at most 1 + (n − 1) + PCH_F(z). So
  ΞCH_F(z) ≤ (n − 1) + PCH_F(z) + (n + PCH_F(z))(n − 1) ≤ n(n + 1 + PCH_F(z)), and R*_F ≤ m_E·n·(n + 1 + P*_F). (This is R86 LEN-MONO's
  argument, read per vertex rather than per λ-run.) □
- DATA tests the slightly sharper ΞCH_F(z) ≤ n(n + PCH_F(z)); 0 violations.
- This adds nothing beyond R86. R86 Corollary COMPOSE-RUN already bounds the WHOLE run by m_E·n·(P* + 1)-type terms. RSTAR-PCH only
  records that R* sits under the same P*.
- DATA (box86/pch.py on pins; the corpus run is reported in §5): gate_K16_n197 λ-changes 0, PCH 15, length-only changes ≤ 1, R*_F 16;
  j10_n24 (largest R*_F / n in the corpus, 10 / 24 = 0.42) PCH 11, R*_F 10; pftheta34_n32 PCH 10, length changes 24, R*_F 4.
  0 violations of each inequality.

## 4. D18 screen (Lead: at least two outside approaches; pick one)
- (A) Well-quasi-orders / Higman-Dickson (order theory, verification of well-structured systems). Idea: the adoption sequence per W-run as a
  bad sequence in a wqo, so its length is bounded by a length function. DEAD for a polynomial bound. [FFSS] Proposition 5.2: controlled
  bad sequences over r copies of N^k with a control function in F_γ have length in F_{γ+k−1}. Proposition 6.3 and Remark 6.4: this is tight
  (in F_{γ+k−1} \ F_{γ+k−2}), and the introduction says it is tight "even when considering the coarser lexicographic ordering". With linear
  control (γ = 1) and dimension k = 2 the class is F_2 (elementary, exponential growth). The natural encodings here have k ≥ n (one
  coordinate per vertex), and Ξ's order is lexicographic. So a wqo argument alone cannot give less than F_n-type bounds. Exact obstruction:
  monotonicity in a lexicographic order is exactly the setting of [FFSS]'s lower bound.
- (B) Exchange / simplex pivots (combinatorial optimisation). Idea: S4a steps as basis exchanges, blocked adoptions as delayed entering
  variables. READING only. Exchange sequences that are monotone in a potential can be exponential: Klee-Minty-type paths, and for parity
  games [Fr09]'s family with exponentially many VJ strategy-improvement iterations (abstract opened). An exchange argument must therefore use
  N5-specific structure: τ, S4a's one-player optimum, GP*. Not a bound, not a kill.
- (C) Potential over the GP* climb (shortest paths / LP duality: Bellman-Ford with delayed relaxations). CHOSEN. GP* already supplies the
  potential inside an epoch (n − 1 rounds). The open part is the number of releases, and §1-§3 show what a release is: a rise of Ξ(z) past
  Ξ(σy) while z is poisoned (GAP-DEV). By R*-RISE and LEN-MONO the releases are paid by changes of Ξ's path-set coordinate. The release
  count is not governed by the deviation set (DEV-CAP dead).
- (D) Not attempted: sorting-network / monotone-circuit depth.
- Obstruction (exact). Every route tried from R* (deviation edges, Ξ-rises, λ-changes, lengths) ends at P*_F, the per-vertex path-set
  changes of Ξ at a fixed cycle node. That is R86's P*, which R86 COMPOSE-NM reduces to carries NM*. So R*-POLY is not a new, smaller
  target: R*-POLY ⇐ P*-POLY, and P*-POLY already implies N5 polynomial by R86. A proof of R*-POLY that does not go through P* would need a
  release potential independent of Ξ's path set. On gate_K the path set at the poisoned targets is a K-step counter that moves once per
  release (PCH = K − 1 = 15, R*_F = 16 at K = 16): the release count is that counter's length.
- Instance (growth benchmark). gate_K16_n197: R*_F = 16. gate_K64_n581: R*_F = 64. So R*_F = K with n ≈ 9K: linear. Corpus max R*_F / n is
  0.42 (j10_n24). No super-linear R*_F is known.

## 5. DATA, corpus
- rstar.py (rstar_*.txt): GAP-DEV 0 violations; DEV-CAP violated in 60 W-runs; max R*_F 64 (gate_K64_n581), max distinct deviation edges in
  a W-run 50 (ladderd0_k48_n156), max DEV changes 64 (gate_K64_n581).
- pch.py (pch_*.txt, 1132 runs): 0 violations of (i) λ-values ≤ n per vertex, (ii) ≤ n − 1 length changes per (λ, P) block,
  (iii) ΞCH_F(z) ≤ n(n + PCH_F(z)), (iv) R*_F ≤ m_E·n·(n + P*_F). Maxima per W-run: λ-changes 2 (kt6_n58), PCH 63 and ΞCH 63
  (gate_K64_n581), length-only changes 24 (pftheta34_n32), R*_F 64 (gate_K64_n581).

## DONE / FINDINGS / NEEDS
- DONE: experiments/new/box86/rstar.py, pch.py, run.sh, run2.sh, rstar_*.txt, pch_*.txt; check.sh "box 86"; this note.
- FINDINGS:
  1. Line for R137: fx_K8_m32 is one W-run, all FREE returns LAT (836; 64 at one edge), REG = E0 = 0, R*_F = 16, FL_F = 0, |F| = 280.
  2. PROVED (lane) Lemma GAP-DEV: a blocked target has Ξ ◁ W and an Odd deviation σ̄ ≠ τ on its σ̄-play (0 violations, 116,086 records).
  3. DEAD: DEV-CAP (R*_F ≤ distinct deviation edges). Instance gate_K16_n197 (R*_F 16, 5 deviation edges); 60 W-runs in the corpus.
  4. PROVED (lane, a composition of R89 R*-RISE and R86 LEN-MONO) RSTAR-PCH: R*_F ≤ m_E·n·(n + 1 + P*_F). It adds nothing beyond R86's P*.
  5. D18 screen: WQO / Dickson DEAD for polynomial bounds ([FFSS] Prop. 5.2 / 6.3, tight even lexicographically); exchange / simplex
     READING only ([Fr09] abstract); GP* potential chosen, and its release count ends at P*. CONJECTURE R*-POLY OPEN. Exact obstruction:
     the path-set coordinate of Ξ at poisoned targets (gate_K: a K-step counter, one release per step, linear).
- NEEDS: none from the owner. Lead: boxes 84-86 close a loop. R3-POLY ⇐ R*-POLY ∧ FL-POLY ⇐ P*-POLY, and P*-POLY is already R86's target
  (⇐ carries NM* under MATCH-Φ). L-RED R138 can count Ξ path-set changes at blocked targets directly (pch.py prints them).
