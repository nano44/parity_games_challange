# R2-N5-FIXD: independent second-referee report on P-N5-FIXD (REFEREE-2 successor 23, Opus 5.5, D15)
Object: docs/new/P-N5-FIXD-box91.md @ l-new 5027c17c (sha1 2050e167a300c676d54178cdc34ccf2daec87036, 89 lines); line
docs/new/P-N5-FIXD-box91-line.txt (sha1 ba09dd261d5c885441845e09104f5e60bf0a81ed). Both re-hashed here in a detached worktree at 5027c17c:
match (the Lead's 15:58Z values). Independence: written before opening any docs/referee/ file for this packet; the count of «fixd» in
docs/referee/ on trunk was 0 at 15:58Z. REFEREE's FLAT-SW proof «SW-KEEP» (Lead 15:58Z) is not read: my own proof of FLAT-SW (§5) was
committed at 64bd0d24 (15:54:59Z), before that message.
Landed sources re-read: RESULTS R15 (a)-(d); R38 (a) (KEY: the phase); R93 (a) Fact LEX / COMMON PREFIX and its object P-N5-WCH-box79.md
§2.1; R91 (i) SW-IN and its proof (P-N5-GAP-box69.md §4.2); SPEC docs/new/N5-ssi-global.md l. 24-60 (identical at 5027c17c and on trunk, as
are experiments/si/si.py and experiments/harness/pg.py).
Owner rulings applied: D1 «Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.»; D18 «Clearly
distinguish proven results from conjectures and open problems.»
Scope: a REDUCTION for N5 only (packet l. 9). FLATTR_P is not bounded. G-N5-TIME stays OPEN. Not M3, not a step-4 pass, not a TARGET.md claim.

## 1. Verdict table
| § | item | verdict (Opus 5.5, D15) | gaps / notes |
| --- | --- | --- | --- |
| 1 | premises [LEX], [R15] (a), (d), MON, Ωσ = Ξ_σ, Ωτ a function of τ | CHECKED | 4 «» quotes from landed text verbatim (the 5th is the Lead's brief); MON derivation correct (§2.1) |
| 2 | Definition FIX-DEPTH, Lemma FIXD-MON | SIGNED | none; N-3 (sharper range) |
| 3 | Theorem PHASE-RED (i), (ii) | SIGNED | none; N-3 (sharper constants) |
| 4 | Corollary PHASE-RED′ as an implication from FLAT-SW | SIGNED (implication) | none. FLAT-SW itself: not signed as part of the packet; see §5 (my own proof: FLAT-SW TRUE, one referee) |
| 5 | DATA, DEAD, READING | not signed | DATA reproduced per game (§4); N-1 (one corpus run from an invalid start), N-2 (a mislabelled total) |
| line | ba09dd26 | MATCHES §2-§4 in content | two REQUIRED symbol fixes L-1, L-2 (unbound k, clause-scope P in PHASE-RED′); precision L-3 |

No gap. Nothing FALSE. Two REQUIRED line fixes (symbol binding only; no change of content).

## 2. The items, as I checked them
### 2.1 Premises
- MON. A transition that changes σ applies Switch_I with ∅ ≠ I ⊆ Iσ (R15 (d)); I is unambiguous (one target per vertex: σ_{k+1} is a
  strategy), so R15 (a) gives Ξ_{k+1} ⊵ Ξ_k pointwise. A transition that does not change σ leaves Ξ = Ξ_σ unchanged. So MON holds at every
  transition (S4a, S4b, S4c), as the packet says. Mechanically: XMON 0 on every in-phase transition of the corpus (§4).
- [LEX] is R93 (a) as landed (RESULTS l. 7031-7036): the quote and COMMON PREFIX are verbatim. CS has 1 + n + 1 = n + 2 coordinates.
- Ωτ depends on τ alone (SPEC S1 «Odd's side»; R38 (a) KEY uses the same fact); τ is constant on a phase by R38 (a).
### 2.2 FIX-DEPTH and FIXD-MON
- DEPTH_t(v) ∈ [0, n + 2] and = n + 2 iff CS(Ξ_t(v)) = CS(fin(v)) iff Ξ_t(v) = fin(v) (CS is injective: c, the path set and ℓ are read
  back from it). K_t ∈ [0, n(n + 2)]. Correct.
- Proof: x := Ξ_t(v) ⊴ z := Ξ_{t′}(v) ⊴ y := fin(v) by MON along t, …, b (all in P); COMMON PREFIX with L := DEPTH_t(v) gives
  DEPTH_{t′}(v) ≥ L. Correct, and it uses nothing about the kind of transition. (The phase is used only so that fin is a later state of the
  same run segment; MON alone would give it on any interval [t, b].)
- DEPTH does not depend on the orientation of the coordinates (it is a first-difference position), so «P-bits» as 0/1 (box 77) and as
  0/±1 (R93's CS) give the same DEPTH.
### 2.3 PHASE-RED
- (i) Every Ξ-changing transition either raises K (strictly, FIXD-MON) or not; K is an integer in [0, n(n + 2)], so at most n(n + 2)
  transitions of P raise it; the others are FLATTR_P by definition. The parenthesis «K unchanged iff every DEPTH is» is correct (a sum of
  non-decreasing terms). Correct.
- (ii) The CH_P transitions cut the remaining |P| − CH_P transitions into at most CH_P + 1 maximal runs of consecutive transitions with Ξ
  unchanged; τ is constant on P, so Ωτ is unchanged; R15 (d) bounds each run by 4n(n − 1). |P| ≤ CH_P + 4n(n − 1)(CH_P + 1) ≤
  (4n(n − 1) + 1)(CH_P + 1). Arithmetic checked. Combination checked.
### 2.4 PHASE-RED′
- Under the hypothesis, each FLATTR_P transition k → k + 1 yields one pair (x, k) counted in FLATSW_P(x); distinct transitions give distinct
  pairs; so FLATTR_P ≤ Σ_x FLATSW_P(x), and PHASE-RED gives the bound. Correct as an implication. The note FLATSW_P(x) ≤ SW_P(x) is immediate.

## 3. The proposed RESULTS line (ba09dd26): strict symbol test and TARGET.md diff
Checked symbol by symbol by hand (not with a tool). Bound: N5, SPEC S1-S5, the premises, run, state (σ_t, τ_t), transition t → t + 1, n,
Ξ_t and σ̄_t (inline SPEC S1 gloss), λ_Ξ, ⊴ ◁ ⊵ ▷, phase P = [a, b] (a, b), |P|, CS(x) and x, rank r, DEPTH_t(v) (t, v), K_t, CH_P, FLATTR_P,
«switched at k», FLATSW_P(x) (its k bound by «transitions k → k + 1»), t ≤ t′ in FIXD-MON, x Even in the sums.
- **L-1 (REQUIRED).** In Corollary PHASE-RED′ the hypothesis reads «if every transition counted in FLATTR_P (any phase P of any N5 run) has
  a switched Even vertex x with Ξ_{k+1}(x) ≠ Ξ_k(x)»: k is not bound in that clause, and «switched» is defined only «at k». Fix: «if every
  transition k → k + 1 counted in FLATTR_P (any phase P of any N5 run) has an Even vertex x switched at k with Ξ_{k+1}(x) ≠ Ξ_k(x)». (The
  packet's own §4 text has «k → k + 1»; only the line dropped it.)
- **L-2 (REQUIRED).** In the same clause P is bound inside the parenthesis of the hypothesis («any phase P of any N5 run»), and the
  conclusion «then FLATTR_P ≤ Σ_{x Even} FLATSW_P(x) and |P| ≤ …» uses P outside that scope. Fix: «then every phase P has FLATTR_P ≤ … and
  |P| ≤ …» (as in packet §4: «then for every phase P»). Same pattern as the clause-scope binders of earlier lines (handover note).
- L-3 (precision, optional). τ appears only as «(λ_Ξ, τ) constant»; «τ_t» would match «states (σ_t, τ_t)». The words «Odd's optimal
  counterstrategy σ̄_t» could cite «(minimising the SPEC S1 order at every vertex at once)» as SPEC does; the R91-R93 lines use the same
  short form, so I do not require it.
- TARGET.md diff: the line claims nothing about M4. n is TARGET.md's n = |V|; games are TARGET.md §1 games (priorities on vertices,
  max-parity, read through SPEC S1's injective p′). The closing clause «a REDUCTION (FLATTR_P and FLATSW_P are not bounded here; FLAT-SW is a
  conjecture; G-N5-TIME stays open; not M3, not a step-4 pass, not a TARGET.md claim)» is correct for the packet as frozen. (If FLAT-SW is
  landed separately, «FLAT-SW is a conjecture» becomes stale; that is a later line.)
- Content: the line states exactly §2 FIXD-MON, §3 PHASE-RED, §4 PHASE-RED′ (with L-1, L-2), nothing from §5. Scope «N5 on EVERY game»
  matches packet l. 9 (nothing for N5-LZC).

## 4. DATA: re-run with my own engine
Tool: docs/referee-2/R2-N5-FIXD/fixd_check.py (my R2-N5-DUAL Runner for N5; my R2-N5-WCH LZRunner for N5-LZC; my wch_check.CS; the lane's
box77 / box79 code NOT imported). Checks XMON, LEXK, MON, KR, CH, STALL, PR, FSW (FLAT-SW), PR2 (PHASE-RED′), OWNC (my Lemma OWN on runs),
SWS (strict rise of a switched non-own-cycle-node vertex). Logs in R2-N5-FIXD/logs/.
- Corpus as the lane's (box59/sbcg.lst 719 runs from the default start; alt_all 413: 93 with start files, 319 + comp54_n80 from the default
  start, see N-1). N5 and N5-LZC: **0 violations of every check**. Controls: X_KSTALL 267 phases (N5) with K stalling > 1 transition;
  X_OWNC 65 (N5) / 51 (N5-LZC) transitions to which Lemma OWN applies (all Ξ-unchanged, as it says).
- Per game (PERRUN=1 against box79/flatsrc_*.txt, N5): sbcg 719 / 719 identical (iterations, K-rise, FLATTR; totals 11621, 5265, 2801);
  alt_all 412 / 413 identical; the one difference is comp54_n80 (N-1).
- Maxima reproduced: FLATTR per phase 91 (returns_ph64), FLATSW per (x, phase) 14 (returns_rt64), FLAT_P(v) 69 (nep94_n48), 1.65n
  (nep92_n40), K stall 91 (returns_ph64), 48 on nep56_n32.
- Pin nep92_n40 (sha1 ce224ec3… re-hashed): phase [6, 98], |P| 92, K-rise 19, FLATTR 73, all with a flat Even switch, FLATSW ≤ 8 per vertex,
  FLAT_P(0) = 66 (box 77's per-vertex definition, any transition; 59 if counted only inside FLATTR transitions).
- N-1 (DATA). experiments/red/n3/instances/comp54_n80.start sets σ(11) = 51, but vertex 11's only edge is 11 → 11 (comp54_n80.pg l. «11 134
  1 11;»). The lane's tools ran N5 from this non-strategy (55 iterations, K-rise 22, FLATTR 32); it is not an N5 run of the game. From the
  default start: 11 iterations, K-rise 3, FLATTR 4. Corrected N5 corpus totals: K-rise 9596, FLATTR 6475 (lane 9615, 6503); FLAT-SW 0
  exceptions either way. (REFEREE-2 succ. 22 found the same invalid start file during LATEP.)
- N-2 (DATA wording, §5 l. 75). «Flat transitions 6568 of 16183 Ξ-changing»: 16183 = K-rise 9615 + FLATTR 6503 + 65 Ξ-unchanged in-phase
  transitions, i.e. ALL in-phase transitions, and 6568 = FLATTR + those 65. The Ξ-changing transitions are 16118 (lane, with comp54) /
  16071 (valid runs). Not signed material; for the fixes file.
- N-3 (precision). In a phase λ_Ξ is constant, so every DEPTH_t(v) ≥ 1 and at most n(n + 1) transitions raise K; and with τ constant only
  φ (not φ^d) can rise on a Ξ-unchanged run, so 2n(n − 1) would do in (ii) via R15 (c). The packet's constants are valid as stated.

## 5. FINDING: CONJECTURE FLAT-SW is TRUE (my own proof; one referee; not a signature of the packet)
Under D18 this is labelled: PROVED by REFEREE-2 alone, unrefereed by a second party. It makes PHASE-RED′ unconditional once a second
referee signs it. Data: FSW 0 and OWNC 0 on the whole corpus (§4); own_check.py below.
### Lemma OWN
Let σ, σ′ be Even strategies that differ only on a set X of Even vertices, and let every x ∈ X be its own Ξ-cycle node under σ and under σ′.
Then Ξ_σ = Ξ_σ′, and S1's procedure returns the same choice at every Odd vertex.
Proof (SPEC S1 procedure, l. 33-44). Run the procedure for σ and for σ′ side by side; the loop order (increasing reward) does not depend on
the strategy. Induction: at the start of v's turn the alive sets agree and every dead vertex has the same valuation and Odd choice.
- Fact 0. λ(x) = x iff x is alive at its own turn and passes test (i) (otherwise x dies inside R(c) for some c ≠ x). So in both runs every
  x ∈ X is alive until its own turn and dies exactly then.
- Fact 1. In a run in which v is a cycle node, no alive x ∈ X ∖ {v} reaches v through alive vertices: x would lie in R(v) and get cycle
  node v ≠ x. In a run in which test (i) for v finds a return walk through such an x, v is a cycle node in that run and x reaches v: the
  same contradiction.
- (i) For v ∉ X, a return walk of either run avoids the out-edges of X (Fact 1), so it is a walk of the other run: the test has the same
  outcome. For v ∈ X it passes in both runs (Fact 0).
- (ii) R(v) (alive vertices reaching v through alive vertices): a walk to v in either run avoids the out-edges of X ∖ {v} (Fact 1), and a
  walk that stops at its first visit of v never uses v's out-edges. So R(v) is the same set.
- (iii)-(iv) X ∩ R(v) ⊆ {v}, so the restricted graphs differ at most at v's out-edges. Even u: M = the vertices of R reaching v without
  passing u; Odd u: M = the vertices reaching u without passing v; neither uses an out-edge of v. The deletions agree off v's out-edges.
  The longest-path recursion has length(v) = 0 as its base; the BFS from v over predecessors starts at v. So path sets, lengths and Odd's
  choices on R(v) ∖ {v} agree, and v's value is (v, ∅, 0) in both.
- (v) If v is Odd (so v ∉ X), its DFS-found return walk avoids the out-edges of X (Fact 1).
- (vi) Equal valuations and choices on R(v); the alive sets stay equal. □
No improvement hypothesis is used. own_check.py (random games n 3-30 with duplicate priorities, random σ, random X of own-cycle-node
vertices, arbitrary new successors): 4,083 pairs with the hypothesis, 0 violations. Control X_ONE (x own cycle node under σ only): 8,104 /
8,104 pairs have Ξ_σ ≠ Ξ_σ′, so the hypothesis «under σ′ too» cannot be dropped.
### Corollary FLAT-SW (strong form)
At every in-phase transition k → k + 1 of N5 with Ξ_{k+1} ≠ Ξ_k there is a switched Even x with Ξ_{k+1}(x) ▷ Ξ_k(x). In particular every
FLATTR_P transition has a switched Even x with Ξ_{k+1}(x) ≠ Ξ_k(x): FLAT-SW holds.
Proof. Ξ is a function of σ, so σ_{k+1} ≠ σ_k; let X be the switched Even vertices. λ_Ξ is constant on the phase (R38 (a)), so each x ∈ X is
its own Ξ-cycle node at both states or at neither. If at both for every x ∈ X, Lemma OWN gives Ξ_{k+1} = Ξ_k: excluded. So some x ∈ X is
its own Ξ-cycle node at neither state. Its new target w satisfies (x, w) ∈ Iσ_k (S4a: σ_new(x) ∈ A(x) ∖ {σ_k(x)}; S4c: by definition).
From here the proof of R91 (i) SW-IN (P-N5-GAP §4.2) applies word for word; it uses only (x, w) ∈ Iσ_k, R15 (a), [V1], [V2], not that the
step is a fallback: Ξ_{k+1}(x) = x ⊕ Ξ_{k+1}(w) ▷ x ⊕ Ξ_k(σ_k x) = Ξ_k(x). □
- Consequence (given a second signature): Corollary PHASE-RED′ unconditional:
  |P| ≤ (4n(n − 1) + 1)(n(n + 2) + Σ_{x Even} FLATSW_P(x) + 1) for every phase P of every N5 run. The same proof covers N5-LZC (switches
  ⊆ Iσ_k by box 73 §4 (a); R15 (a) holds), but the packet claims nothing for N5-LZC.
- Remark. The strong form says more than FLAT-SW: in every Ξ-changing in-phase transition (flat or not) a switched Even vertex strictly
  rises, and Ξ-unchanged in-phase transitions are exactly those whose switched vertices are all their own cycle nodes (the 65 OWNC
  transitions of the corpus). That is R15 (b) (Lemma B) seen from the other side.

## DONE / FINDINGS / NEEDS (this report)
- DONE: this report; tools fixd_check.py, own_check.py; logs in R2-N5-FIXD/logs/.
- FINDINGS: (1) §2, §3, §4 SIGNED, no gap, nothing FALSE. (2) Line: L-1, L-2 REQUIRED (unbound k; clause-scope P), L-3 optional. (3) DATA
  reproduced per game; N-1 comp54_n80 invalid start inflates the lane totals (corrected 9596 / 6475); N-2 «6568 of 16183 Ξ-changing»
  mislabelled. (4) FLAT-SW TRUE by my own proof (Lemma OWN + R91 SW-IN's argument), one referee.
- NEEDS: Lead: route L-1 / L-2 to the lane's fixes file; decide whether FLAT-SW (mine, and REFEREE's SW-KEEP) is checked crosswise for a
  later line.
