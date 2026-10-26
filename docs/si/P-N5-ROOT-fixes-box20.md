# P-N5-ROOT fixes (box 20 packet and its addendum; repairs only)
L-SI successor 19 (Opus 5.5; D15, D18, L37, L40). Written at the Lead's request of 19:19Z (Lead's stamp), after both reports and both §Cs.
Stamp: the commit (date -u).
- Objects, both FROZEN and not edited:
  - docs/si/P-N5-ROOT-box20.md, sha1 d3788bc0ce0e3da2d54298c58e227e437242419a (l-si freeze ced5cf27);
  - docs/si/P-N5-ROOT-add-box20.md, sha1 af1c7ad4581cce4a9830b4ed01e2370d26ef850b (l-si freeze 829003b2).
  Both were written by L-SI successor 16. I write these repairs as its successor.
- Repairs only. This file adds no lemma and changes no signed statement. Every changed sentence is one a referee wrote or asked for, and each is
  quoted.
- Sources, all on trunk 77f2664e:
  - REFEREE, docs/referee/R-N5-ROOT.md: report by successor 15 at 619fccf2; §C by successor 16 at da0c1902, with its stamp corrected at
    65f55427 (§C text quoted at 65f55427).
  - REFEREE-2, docs/referee-2/R2-N5-ROOT.md: report by successor 17 at 3febbfaf; §C at f5381a5c.
- Quotes. Every «…» below is verbatim. Its tag [Q path@commit:lines] gives the source, and experiments/si/rund/quotecheck.py checks each one
  against `git show commit:path` at those lines (whitespace normalised; "…" inside a quote separates parts, and each part must occur in order).
  `python3 -I experiments/si/rund/quotecheck.py docs/si/P-N5-ROOT-fixes-box20.md` prints QUOTES PASS (pinned in experiments/si/check.sh, with a
  shifted-line control that must fail).

## Verdicts (joint)
- REFEREE §C: [Q docs/referee/R-N5-ROOT.md@65f55427:159] «Verdicts identical. Joint gap map: EMPTY.»
- REFEREE-2 §C: [Q docs/referee-2/R2-N5-ROOT.md@f5381a5c:166] «No disagreement. Joint gap map: EMPTY. Notes to the lane (union): ROOT-N1..N5,
  ADD-N1..N2, N-ROOT-3, N-ROOT-4, N-ROOT-7 (N-ROOT-1, -2, -5, -6»
- So every item is SIGNED by both referees with no gap:
  - P-N5-ROOT: §2 Lemma BF-F_D; §3 Theorem FREEZE-A (a)-(c) and (R-LEN); §4 Corollary ROOT-PIECE, as a REDUCTION in G_c; §5 Lemma DL-SPLIT.
    DL-SPLIT's condition (RELAY-CHAIN) is MET: it landed as RESULTS R72.
  - P-N5-ROOT-add: §2 Lemma GATE-SHIFT (a), (b); §3 Theorem FREEZE-G (a)-(c); §4 Corollary RELAY-PIECE (i), (ii).
  - Not reviewed, as both packets asked: ROOT §6 and addendum §5-§6 (READING / DATA / OPEN).
- Notes matched by the two §Cs: ROOT-N1 = N-ROOT-1; ROOT-N4 = N-ROOT-2; ROOT-N5 = N-ROOT-6. N-ROOT-5 replaces ROOT-N2: REFEREE's §C row
  [Q docs/referee/R-N5-ROOT.md@65f55427:164] «REFEREE-2's fuller form ACCEPTED». The others stand alone: ROOT-N3, ADD-N1, ADD-N2 (REFEREE);
  N-ROOT-3, N-ROOT-4, N-ROOT-7 (REFEREE-2). F1-F10 below take them one at a time.

## F1. ROOT-N1 = N-ROOT-1: FREEZE-A (c) at q = c (one sentence; ROOT §3 (c), first branch)
- Packet text: [Q docs/si/P-N5-ROOT-box20.md@ced5cf27:106-107] «As q ∈ A_{s+L}, q ∉ D_{s+L}, so next_{s+L}(q) = τ(q), which lies on q's play and so
  in A_{s+L}; (Aκ): M_{s+L}(q) = wt(q) + M_{s+L}(τ q) ∈ V_q.»
- REFEREE: [Q docs/referee/R-N5-ROOT.md@619fccf2:131-132] «For an Odd cycle node q = c with σ̄_t(c) ∈ A_t, (Aκ) does not apply (it is stated for z ≠
  c); the claim holds because τ(c) lies on c's cycle and both sides are 0. One sentence.»
- REFEREE-2: [Q docs/referee-2/R2-N5-ROOT.md@3febbfaf:102-103] «For q = c: σ̄_t(c) ∈ A_t forces c ∉ D_t (c's honest play would return to c ∈ D_t),
  M(c) = 0, and τ(c) is c's successor on its cycle with M = 0 (every other vertex of the cycle has rank < rank(c)), so 0 ∈ V_q.»
- Repaired branch: after "(Aκ): M_{s+L}(q) = wt(q) + M_{s+L}(τ q) ∈ V_q", add "for q ≠ c. For q = c (an Odd cycle node), (Aκ) is not used:
  M(c) = 0, and τ(c) is c's successor on its cycle with M = 0, so 0 ∈ V_q." (REFEREE-2's reason, which REFEREE's sentence matches.)

## F2. ROOT-N2 replaced by N-ROOT-5: name P1 / P2 per item (citation; both packets, §1)
- Packet text (both packets, §1): [Q docs/si/P-N5-ROOT-box20.md@ced5cf27:18] «with the standing premise 1E-N3, as in RESULTS R55-R69» and
  [Q docs/si/P-N5-ROOT-add-box20.md@829003b2:19] «with the standing premise 1E-N3, as in RESULTS R55-R69».
- REFEREE: [Q docs/referee/R-N5-ROOT.md@619fccf2:133-134] «(F1) on S4a's arena (BF-F_D Case 2, GATE-SHIFT (b), FREEZE-G (a)) and WM-G use 1E-N3 in
  its P2 form (S1 returns the arena optimum); name P2 as P-N5-FLIP §1 does.»
- REFEREE-2: [Q docs/referee-2/R2-N5-ROOT.md@3febbfaf:111-113] «BF-F_D, GATE-SHIFT (b), FREEZE-A / FREEZE-G use (F1) on S4a's arena, i.e. the standing
  premise 1E-N3 in form P2 … FREEZE-A (c), GATE-SHIFT (a) and DL-SPLIT use κ-Y-FORM_D (P1). The packets say "1E-N3" globally; naming P1 / P2 per
  item (as P-N5-FLIP does) would help the landing.»
- P1 and P2 as P-N5-FLIP §1 names them: [Q docs/si/P-N5-FLIP-box18.md@7ea3d8cf:27] «P1: σ̄_k is Odd's pointwise-optimal strategy in the one-player
  game G_{σ_k}.» and [Q docs/si/P-N5-FLIP-box18.md@7ea3d8cf:31] «P2: S4a's σ_{k+1} is Even's pointwise optimum in the arena H_k of G_τ».
- Repaired §1 sentence (both packets): "with the standing premise 1E-N3 in its two forms P1 and P2 (P-N5-FLIP §1)". Added per-item line, as
  REFEREE-2 assigns them:
  | item | P2 ((F1) on S4a's arena, or WM-G) | P1 (κ-Y-FORM_D) |
  | --- | --- | --- |
  | ROOT §2 BF-F_D | yes (Case 2) | — |
  | ROOT §3 FREEZE-A (a), (b) | yes (via BF-F_D) | — |
  | ROOT §3 FREEZE-A (c), (R-LEN) | yes (via (b)) | yes ((c)) |
  | ROOT §4 ROOT-PIECE | yes | yes (via FREEZE-A (c)) |
  | ROOT §5 DL-SPLIT | — | yes |
  | add §2 GATE-SHIFT (a) | — | yes |
  | add §2 GATE-SHIFT (b) | yes ((F1) and WM-G) | — |
  | add §3 FREEZE-G (a)-(c) | yes ((F1), WM-G) | — |
  | add §4 RELAY-PIECE | yes (via FREEZE-A (b), FREEZE-G (c)) | — |
  The P1 / P2 columns of the derived rows (FREEZE-A (a), (b), (c) via (b), ROOT-PIECE, RELAY-PIECE) follow the proofs' references. The
  referees named the direct uses only.

## F3. ROOT-N3: DL-SPLIT's split step (wording; ROOT §5, proof, "Split")
- Packet text: [Q docs/si/P-N5-ROOT-box20.md@ced5cf27:142] «unsplit at t, and since τ and σ̄(u) are unchanged on its old route up to u, some Even
  vertex of that route switched: (B).»
- REFEREE: [Q docs/referee/R-N5-ROOT.md@619fccf2:135] «"since τ and σ̄(u) are unchanged" → "since τ is unchanged": the route is a (σ, τ)-play.»
- Repaired: "unsplit at t, and since τ is unchanged (the route is a (σ, τ)-play), some Even vertex of its old route up to u switched: (B)."

## F4. N-ROOT-4: DL-SPLIT's quantifier (wording; ROOT §5, statement)
- Packet text: [Q docs/si/P-N5-ROOT-box20.md@ced5cf27:130-131] «Then (A) some entering vertex z ∈ A_{t+1} ∖ A_t has its first D_t-vertex u not in
  D_{t+1} … or (B) z is unsplit at t»
- REFEREE-2: [Q docs/referee-2/R2-N5-ROOT.md@3febbfaf:109-110] «"(A) some entering vertex z … or (B) z is unsplit" — (B) has no binder; the proof shows
  the stronger "every entering z has (A) or (B)", which is what the data check (DLS_A + DLS_B = DLS_entering in every set).»
- Repaired statement: "Then every entering vertex z ∈ A_{t+1} ∖ A_t satisfies (A) or (B): (A) its first D_t-vertex u is not in D_{t+1} (a D-LEAVE at
  u: σ̄_{t+1}(u) = τ(u) ≠ σ̄_t(u)); (B) z is unsplit at t (λ_{W,t}(z) = λ_t(z) = c) and leaves R_D by an Even switch." The proof's "Split" bullet
  already argues per entering z. The rest of the statement (the clean case (A) and (i)-(iii)) is unchanged.

## F5. N-ROOT-3: "ROUTE event" in DL-SPLIT (ii) and in the Consequence (wording; ROOT §5)
- Packet text: [Q docs/si/P-N5-ROOT-box20.md@ced5cf27:137] «(ii) u has a ROUTE event at t → t+1 (some class exit path or exit of u differs at t and
  t + 1);» and [Q docs/si/P-N5-ROOT-box20.md@ced5cf27:150-151] «Consequence: G_c ≤ #(B-gains) + #(S4a transitions carrying a ROUTE / CYC / TOG event of
  class c, or a tie or a non-clean change at a D-leaving vertex).»
- REFEREE-2: [Q docs/referee-2/R2-N5-ROOT.md@3febbfaf:106-108] «So (ii) is a "route change at u", and the consequence line's "transitions carrying a
  ROUTE / CYC / TOG event" should read "… or a route change at a D-leaving vertex".»
- REFEREE's §C (it checked whether the wording hides a case): [Q docs/referee/R-N5-ROOT.md@65f55427:166] «ACCEPTED, as wording. I checked whether it
  hides a case: in clean case (A) with no TIE, u has a ρ event … With (ii) that IS a FLIP ROUTE event at u, so the Consequence's list holds in FLIP's
  sense too (with a tie, "a tie" covers it).»
- Repaired (ii): "(ii) u has a ROUTE CHANGE at t → t+1 (some class exit path or exit of u's options differs at t and t + 1)". Repaired
  Consequence: "G_c ≤ #(B-gains) + #(S4a transitions carrying a ROUTE / CYC / TOG event of class c, or a route change, a tie or a non-clean change
  at a D-leaving vertex)." Added, as REFEREE's §C showed: in the clean case (A) without a tie, u also has a ρ event, so a route change there is a
  ROUTE event in P-N5-FLIP's sense. The bound's content is unchanged.

## F6. ROOT-N4 = N-ROOT-2: (R-LEN) wording (ROOT §3)
- Packet text: [Q docs/si/P-N5-ROOT-box20.md@ced5cf27:114-116] «(R-LEN) On [s + L, e], Ξ on A_t changes only in its length … So the Ξ-changes of q
  at the transitions counted in (c) are at most deg(q)·(|U| − 1) − 1.»
- REFEREE: [Q docs/referee/R-N5-ROOT.md@619fccf2:136-137] «The count deg(q)(|U| − 1) − 1 follows from the chain of distinct (M, length) pairs of q at
  the counted states; the sentence about Ξ on A_t is true but is not the step q needs (q may lie in D_t).»
- REFEREE-2: [Q docs/referee-2/R2-N5-ROOT.md@3febbfaf:104-105] «the count deg(q)(|U| − 1) − 1 follows directly: M(q) ∈ V_q (≤ deg(q) values), and for each
  value the length is monotone in [1, |U| − 1].»
- Repaired (R-LEN): "(R-LEN) At the states counted in (c), M(q) ∈ V_q takes ≤ deg(q) values (FREEZE-A (c)); for each value the length of Ξ(q) is
  monotone (Ξ non-decreasing, cycle node c) and lies in [1, |U| − 1]. So Ξ(q) runs through ≤ deg(q)·(|U| − 1) distinct values there, and its
  changes at the counted transitions are at most deg(q)·(|U| − 1) − 1. (On A_t, Ξ moves only in its length after s + L. That is true, but q
  may lie in D_t, so it is not the step used.)"

## F7. ROOT-N5 = N-ROOT-6: the data sentence on case (iii) (ROOT §6, DATA; not signed, corrected for accuracy)
- Packet text: [Q docs/si/P-N5-ROOT-box20.md@ced5cf27:161] «every leave without a ROUTE at u was a COPY, so case (iii) never occurred»
- REFEREE: [Q docs/referee/R-N5-ROOT.md@619fccf2:138-140] «The (iii) alternatives occur (library n ≤ 24: 237 ties, 221 TOG steps at e1; non-exclusive
  counts), but never as the only case … This agrees with the packet's "case (iii) never occurred" read as "never alone".»
- REFEREE-2: [Q docs/referee-2/R2-N5-ROOT.md@3febbfaf:114-115] «(iii) (TOG or TIE) holds at 579 clean D-leaves in my data, but never alone: always
  together with (i) or (ii) (DLS_case_iii_only = 0).»
- Repaired: "case (iii) never occurred ALONE: (iii) does occur (237 ties and 221 TOG steps in REFEREE's library; 579 clean D-leaves in REFEREE-2's
  data), always together with (i) or (ii)."

## F8. ADD-N1: FREEZE-G (a)'s base case (one sentence; addendum §3, proof of (a))
- Packet text: [Q docs/si/P-N5-ROOT-add-box20.md@829003b2:97] «(a) Induction on t − s; base: N_t(c) = 0.»
- REFEREE: [Q docs/referee/R-N5-ROOT.md@619fccf2:141] «N_t(c) = 0 needs c ∉ R_u(t); true (σ̄_t(u)'s play in A_t reaches c's cycle, so c ∈ F_D(t)); say so.»
- Repaired: "(a) Induction on t − s; base: N_t(c) = 0, which needs c ∉ R_u(t): σ̄_t(u)'s honest play lies in A_t and reaches c's cycle, so c ∈ F_D(t)."

## F9. ADD-N2: RELAY-PIECE (i), the G-intervals are disjoint blocks (wording; addendum §4, statement (i))
- Packet text: [Q docs/si/P-N5-ROOT-add-box20.md@829003b2:125-126] «is the union of ≤ deg(u) G-intervals for u (consecutive ones sharing a transition at
  which Δ changes);»
- REFEREE: [Q docs/referee/R-N5-ROOT.md@619fccf2:142] «The G-intervals are disjoint blocks; the Δ-changing transition lies between two of them.»
- Repaired (i): "… is the union of ≤ deg(u) disjoint G-intervals for u (blocks of consecutive states; each transition at which Δ changes lies
  between two consecutive blocks, in neither);". (ii)'s count already treats those transitions as boundaries, counted once each, so (ii) is
  unchanged.

## F10. N-ROOT-7 and the vacuity record: what rests on proof alone (addendum §5 DATA; a record for the landing text)
- Packet text: [Q docs/si/P-N5-ROOT-add-box20.md@829003b2:148] «FREEZE-G (b), (c) and RELAY-PIECE are VACUOUS in the data: no G-interval is longer than
  |E_s| − 1 (0 of 22 / 25 / 120 / 729).»
- REFEREE: [Q docs/referee/R-N5-ROOT.md@619fccf2:34] «its freeze sentence rests on PROOF ALONE (vacuous in all data and searches, §5)» and
  [Q docs/referee/R-N5-ROOT.md@619fccf2:35] «SIGNED on PROOF ALONE (vacuous in all data and searches; its inner step checked at every state, §5)».
- REFEREE-2: [Q docs/referee-2/R2-N5-ROOT.md@3febbfaf:116-117] «FREEZE-G (b), (c) and RELAY-PIECE's multi-interval content are untested on natural games
  and only weakly tested on constructed unions (§2). The landing text should carry "rests on proof alone" for them.»
- REFEREE's §C: [Q docs/referee/R-N5-ROOT.md@65f55427:172] «the landing text should carry "rests on proof alone" for FREEZE-G (b)'s freeze sentence,
  (c) and RELAY-PIECE's multi-value content» and its re-run of REFEREE-2's unions: [Q docs/referee/R-N5-ROOT.md@65f55427:179-181] «FREEZE-G: 6
  intervals, 3 of them past their freeze window (max excess 45). FRG (c) 563 checks, FRGC 720, FREEZE-A pieces past s + L 3, RELAY-PIECE
  non-vacuous 3. 0 failures».
- Recorded plainly:
  - FREEZE-G (b)'s freeze sentence, FREEZE-G (c), and RELAY-PIECE's multi-value / multi-interval content rest on PROOF ALONE. Both referees
    checked the proofs line by line.
  - They are never reached on natural games: no G-interval outlives its freeze window in the lane's, REFEREE's or REFEREE-2's data, nor in
    REFEREE's hill climbs. Δ(u) never changes after FREEZE-A's freeze index in any run, so RELAY-PIECE's multi-value case is not exercised.
  - They are reached only in REFEREE-2's constructed disjoint-union games (docs/referee-2/R2-N5-ROOT/union/). REFEREE successor 16 re-ran three
    of them (u7101_1900, u7201_1948, u7202_374) with its own engine: 3 G-intervals past their freeze window, 0 failures.
  - What IS exercised on natural data: FREEZE-G (a), FREEZE-G (b)'s first sentence, GATE-SHIFT (a), (b), BF-F_D, FREEZE-A (a)-(c), and DL-SPLIT.
    Their controls bite in all three data sets.
- The packet's "VACUOUS in the data" stands for the lane's data. The repaired sentence adds: "Reached only in REFEREE-2's constructed unions
  (3 G-intervals past the freeze window in REFEREE's re-run, 0 failures); FREEZE-G (b)'s freeze sentence, (c) and RELAY-PIECE's multi-value
  content rest on proof alone."

## Not changed
No signed statement changes in content. F1 adds a case sentence. F2 names premises. F3-F6, F8 and F9 are wording. F7 and F10 correct or extend
the unsigned data record. Scope as both packets state it: ROOT-PIECE and RELAY-PIECE are reductions (G_c, f and the number of G-intervals are
not bounded); nothing here bounds ρ, N_ep, f or N5's running time; not a TARGET.md claim; G-N5-TIME stays OPEN.
