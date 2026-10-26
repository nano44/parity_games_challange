# P-N5-H3 fixes (box 16 packet; repairs only)
L-SI successor 12 (Opus 5.5; D15, D18, L37, L40), session_01HYh7NTpb8ZcvdYpgAJiDgy. Prepared and frozen at the Lead's word of 06:17Z
(Lead's stamp), after both §Cs. Stamp: the commit (date -u).
- Object: docs/si/P-N5-H3-box16.md, sha1 680e45287aed82ea3d9ac05ed9decdf9c260e849 (l-si 10b11167; author L-SI successor 11). FROZEN,
  not edited.
- Repairs only. This file adds no new statement and no new proof. The one added sentence (H3-N2) is the referees' own, found by both.
- Sources (file sha1s by `git show <commit>:<path> | sha1sum`):
  - REFEREE successor 12, docs/referee/R-N5-H3.md: report at referee 7c2d9b49 (file sha1 346b6b3c…); Addendum A at ead5fdb3 (03c6f93e…);
    §C at 6b17eb58 (d98db74e…).
  - REFEREE-2 successor 14, docs/referee-2/R2-N5-H3.md: report at referee-2 5b251bed (5fe53f1f…); N-H3-6 and corrected counts at
    d449d72b (0cabbf39…); §C at b7b04fad (b2ffa987…) and 723909be (7c5fbf7c…, data-table arithmetic).
- Both §Cs: identical verdicts, no gap, no NOT SIGNED statement. All seven statements are SIGNED by both on every game: G_D-NC (b′),
  TC-CLASS, C2-H3, WM-G, P^c_L, CR-D, Corollary FRZ-U_H3 (in the 0-based reading, H3-N4 below). §7 (READING) and §8 (DATA) are not
  signed. Structural lemmas only; no running-time bound. G-N5-TIME stays OPEN.

## Lines (one per note)
- H3-N4 = N-H3-6 (INDEX; REFEREE Addendum A, REFEREE-2 d449d72b; the author's reading at l-si 2d021429). In packet §0's table, row §6,
  read "constant from the run's (n − 1)-th state on" as "constant from state k_0 + n − 1 on (after n − 1 transitions; the run's n-th
  state)". This is 0-BASED, as §5 (CR-D: "for every t ∈ S with t ≥ k_0 + n − 1") and §6 already say. The statement has content only
  on a run of ≥ n + 1 states (≥ n transitions). The 1-based reading (constant from k_0 + n − 2) is NOT given by the proof and is not
  signed: P^c_L at j = n − 2 covers only simple paths of ≤ n − 2 edges. A failure of the 1-based reading is not a counterexample.
- H3-N2 = N-H3-4 (found independently by both referees). In P^c_L, Case B, B1, sub-case "x on c′'s W-cycle", after "Then x's σ̂-play
  closes the cycle x → z → π → c′ → (the old arc) → x, whose top is t." read the added sentence: "This cycle is simple: if π enters c′'s
  W-cycle at e, then π's part on that cycle is the arc e … c′, the old arc is c′ … x, and these meet only at c′, since x ∉ π; every
  vertex of the cycle outside P(π) is ranked at most c′, so its top is t." The proof is otherwise unchanged. (This is the same point as
  REFEREE-2's N-NC-3 on the void R2-N5-NC, referee-2 4d54b6a5.)
- N-H3-1 (quote exactness; REFEREE §C accepts it: "missed by us"). Content verbatim; two quotes in packet §1 are not character-exact:
  - R55's proof of (b) (docs/new/P-N5-GD-box43.md l.54-59) is quoted with its three bullets joined into one paragraph.
  - The "(C1) … (C4)" quote (docs/si/P-N5-FB-box7.md §1, l.57-63) drops (C1)'s three sub-bullets, the parenthetical "(Definition.)"
    after (C2) and "(Σ ±2^rank is injective on sets)" after (C3), without "…". Read each omission as marked by "…".
- H3-N1 (landing note; REFEREE, accepted in REFEREE-2's §C). WM-G, and so P^c_L, CR-D and FRZ-U_H3, rest on the standing SPEC premise
  that S4a's S1 run returns Even's pointwise optimum on the arena H_k, as every N5 result does (1E-N3 in RESULTS R57). The code's match to
  SPEC is DATA (R15 G-N5T-1).
- N-H3-2 = REFEREE §1 (no change). In (b′), (NC) replaces (h_D) at the proof's one use of it ("would then follow x's play back to u").
- N-H3-3 = REFEREE §3 (no change). C2-H3's factorisation P_F(v) = (π_v ∩ V_{>c}) ⊔ P_F(u) rests on the lasso fact; it needs neither (h_D)
  nor (NC).
- H3-N3 / N-H3-5 (DATA; two corrections).
  - Both referees' first freeze counts included vacuous runs of exactly n states. Both are corrected (REFEREE Addendum A; REFEREE-2
    d449d72b, 723909be).
  - Non-vacuous freezes (≥ n + 1 states), 0 failures: lib41 3 runs; frz1_n24 (L-COMP); pftheta34_n32 (experiments/red/so/instances/);
    and REFEREE-2's constructed witness pft34_h3u_P32 (sha1 6032b40b…, a DECOUPLED union: the ¬(NC), ¬(h_D) vertex lies in a component
    disjoint from the freezing part), re-run by REFEREE on its own engine (2 runs, 0 failures).
  - Natural freezes occur only in the (h_D) regime. frz2_n24 (L-COMP) has a run of exactly n states, so it is vacuous for FRZ-U_H3.
  - Packet §8's "no fallback-free run under the hypotheses lasts n − 1 transitions" stands for the lane's own runs; the criterion for
    content is n transitions (H3-N4).
  - C2-H3 is exercised outside (NC): REFEREE 5,773 (h3_D) ∧ ¬(NC) states, REFEREE-2 201,701 checks at such states (+ 254 on the witness),
    0 failures; mutation controls bite on both engines.
