# P-N5-FLIP fixes (box 18 packet; repairs only)
L-SI successor 15 (Opus 5.5; D15, D18, L37, L40). Written at the Lead's request of 12:32Z (Lead's stamp), after both §Cs. Stamp: the
commit (date -u).
- Object: docs/si/P-N5-FLIP-box18.md, sha1 96a7e088c2175f71ab1aef2577d6139f80a4efff (l-si 7ea3d8cf; pinned trunk d67fdb87). FROZEN, not
  edited.
- Repairs only. This file adds no new lemma. Every changed sentence is one a referee wrote or asked for, and each is quoted.
- Sources (file sha1 by `git show <commit>:<path> | sha1sum`):
  - REFEREE successor 14, docs/referee/R-N5-FLIP.md: report at referee 8317a435 (file sha1 86a12b7b…), §C at 72db1b18 (548f13ef…).
  - REFEREE-2 successor 16, docs/referee-2/R2-N5-FLIP.md: report at referee-2 e9044674 (7b691f21…), §C at 75b8b52a (3ecc2702…).
  - Not used: REFEREE-2's 12:13Z corrections, which were sent by message only and are not in its file (Lead 12:32Z).
- Quotes. Every «…» below is verbatim. Its tag [Q path@commit:lines] gives the source, and experiments/si/rund/quotecheck.py checks each one
  against `git show commit:path` at those lines (whitespace normalised; "…" inside a quote separates parts, and each part must occur).
  `python3 -I experiments/si/rund/quotecheck.py docs/si/P-N5-FLIP-fixes-box18.md` prints QUOTES PASS (pinned in experiments/si/check.sh).

## Verdicts (joint)
- REFEREE §C: [Q docs/referee/R-N5-FLIP.md@72db1b18:206-207] «Joint verdicts: ROOT, ROUTE-RELAY, SELF-FREE, STATIC, FLIP (a)-(c), N1 ∨ N2 ∨
  N3 SIGNED; ROOT-C SIGNED WITH GAPS G-FLIP-1, G-FLIP-2 (in the exits form, with the repair); N3-LEVEL SIGNED WITH GAP G-FLIP-3.»
- REFEREE-2 §C: [Q docs/referee-2/R2-N5-FLIP.md@75b8b52a:151-152] «My verdicts are unchanged, except that I adopt REFEREE's wording for
  ROOT-C: as written NOT SIGNED (false), corrected form ("path and exit") SIGNED WITH GAP ROOTC-1 = G-FLIP-2 closed.»
- So the packet's §2 ROOT, §3 ROUTE-RELAY and SELF-FREE, §5 STATIC, and §6 FLIP (a), (b), (c) and N1 ∨ N2 ∨ N3 are SIGNED by both with no
  gap.
- §4 ROOT-C as written is NOT SIGNED: it is FALSE. Its corrected form (R1 below) is SIGNED, with G-FLIP-1 (statement) and G-FLIP-2 (proof
  step) closed by R1 and R2.
- §6 N3-LEVEL is SIGNED WITH GAP G-FLIP-3 (minor), closed by R3.
- §7 and §8 were not reviewed, as the packet asked.

## R1. G-FLIP-1 = ROOTC-2: ROOT-C's statement (literal form FALSE; repaired)
- Packet text: [Q docs/si/P-N5-FLIP-box18.md@7ea3d8cf:78-80] «If at an in-phase transition t → t+1 every class exit path of every q′ ∈ Q_c
  (from every y ∈ succ(q′) ∩ U_c) is the same at t and t + 1, then κ_t(q) = κ_{t+1}(q) for every q ∈ Q_c. So every transition with a ρ
  event at a terminal of class c changes a class exit path of class c.»
- The gap. REFEREE-2: [Q docs/referee-2/R2-N5-FLIP.md@75b8b52a:63-64] «By §3's definition the class exit path is the part STRICTLY BEFORE the
  exit, and §3's ROUTE definition treats "class exit path or exit" as two things. An Even last vertex of a class exit path can switch from
  one exit to another without changing the path.»
  - Its witness: experiments/n5-exhaustive/instances/n4_thch_0.pg (sha1 77018c63…) from S3, transition 0 → 1.
  - REFEREE also has rootc_lit_n5 (sha1 602e6db6…, start 796b8d5e…) and the same n4_thch_0 case:
    [Q docs/referee/R-N5-FLIP.md@72db1b18:159-160] «ROOTC-2 = G-FLIP-1 (same gap). Witnesses: REFEREE-2 n4_thch_0 from S3 (sha1 77018c63…);
    mine the same instance and state».
- The repair, the same wording from both referees:
  - REFEREE-2: [Q docs/referee-2/R2-N5-FLIP.md@75b8b52a:70-71] «Repair: "every class exit path AND EXIT" in the hypothesis, "changes a class
    exit path or exit" in the consequence (as §3's ROUTE definition already says); the proof then reads Π_t(q) = Π_{t+1}(q) correctly.»
  - REFEREE: [Q docs/referee/R-N5-FLIP.md@72db1b18:161-162] «Joint repair: "class exit path AND EXIT" in the hypothesis and "changes a class
    exit path or exit" in the consequence (both referees, word for word the same fix).»
- Corrected statement (the signed form; the packet's sentence with the two insertions only):
  - If at an in-phase transition t → t+1 every class exit path AND EXIT of every q′ ∈ Q_c (from every y ∈ succ(q′) ∩ U_c) is the same at t
    and t + 1, then κ_t(q) = κ_{t+1}(q) for every q ∈ Q_c.
  - So every transition with a ρ event at a terminal of class c changes a class exit path or exit of class c.
- The proof's last line reads "Π_t(q) = Π_{t+1}(q) as walks with weights (equal paths AND EXITS, U_c fixed in the phase)". The exits fix
  each e_{i+1} in the walk's definition.

## R2. G-FLIP-2 = ROOTC-1: ROOT-C's proof of (≤) (a false step; repaired, P1 only)
- Packet text, to be deleted: [Q docs/si/P-N5-FLIP-box18.md@7ea3d8cf:84-86] «Hence each walk is the play from q of a positional Odd strategy
  in G_{σ_s} (choose y_i at e_i), with cycle node c and κ equal to the walk's weight up to c. (≤) By P1, Ξ_s(q) ⊴ the valuation of each
  such play. Both have cycle node c, so κ_s(q) ⪯ the walk's κ.»
- The gap. REFEREE-2: [Q docs/referee-2/R2-N5-FLIP.md@75b8b52a:72-74] «The sentence "Hence each walk is the play from q of a positional Odd
  strategy in G_{σ_s} (choose y_i at e_i), with cycle node c" is FALSE when a walk passes a vertex of Q_c that lies on c's honest cycle with
  a choice off the cycle». Witnesses: REFEREE-2's best_tog_83 (docs/referee-2/R2-N5-TOG/climb/best_tog_83.pg, sha1 01788acf…, S3, state 1)
  and REFEREE's leanT_N6 (S3, state 3).
- The repair carried here is REFEREE-2's inequality B(e, y), as REFEREE recommends:
  [Q docs/referee/R-N5-FLIP.md@72db1b18:172-174] «Which text for the fixes file: B(e, y) (REFEREE-2's form), because it is stated on the
  walk's own steps (e, p_y, e′) and slots into the packet's (≤) line without the extra additivity step; my LOCAL may be added as a one-line
  remark (it is B before additivity, and also covers y with exit e, which no walk uses). Either text closes the gap; there is no
  disagreement.»
- New (≤), verbatim from REFEREE-2, replacing the deleted text: [Q docs/referee-2/R2-N5-FLIP.md@75b8b52a:79-86] «prove "≤" by backward
  induction along the walk from B(e, y): κ_s(e) ⪯ κwt(e) + κwt(p_y) + κ_s(e′) for e ∈ Q_c, y ∈ succ(e) ∩ U_c with exit e′ ≠ e (p_y = y's
  class exit path). Proof of B: let ρ := σ̄_s[e ↦ y]. (1) If e′'s honest play never visits e, the ρ-play from e is e, p_y, e′'s honest play
  (cycle node c), whose value is the right side (additivity); P1. (2) If it visits e, the ρ-play closes a cycle Z through e. If Z's node is
  c (e on c's cycle, reached after c), the ρ-play still first reaches c along e, p_y, e′'s route, value = the right side; P1. Otherwise P1
  gives rew(top Z) > rew(c), so (FLIP (c)'s split) the part of Z ranked above c has an even top, or Z lies below an odd c; if e′ reaches e
  before c, the right side equals κ_s(e) + wt(Z) with wt(Z) ≻ 0; if after c, the right side's path set is (Z ∩ V_{>c}) with an even top
  while κ_s(e) has an empty path set (e on c's cycle): either way the right side ≻ κ_s(e). Summing B along the walk (κ_s(c) = (0, 0))
  gives κ_s(q) ⪯ the walk's κ.»
  - Here ρ is REFEREE-2's name for a modified Odd strategy, not the ρ-event count.
  - A walk's steps satisfy e′ = e_{i+1} ≠ e_i, because the e_i are distinct, so B applies at every step.
- One-line remark (REFEREE's LOCAL, the same inequality before additivity): [Q docs/referee/R-N5-FLIP.md@72db1b18:78] «Repair (referee-written;
  P1 only). LOCAL: for every s, e ∈ Q_c and y ∈ succ(e) ∩ U_c, κ_s(e) ⪯ κwt_c(e) + κ_s(y).» Its proof is at
  docs/referee/R-N5-FLIP.md@72db1b18 lines 78-86. Equivalence: [Q docs/referee/R-N5-FLIP.md@72db1b18:166-168] «By additivity κ_s(y) =
  κwt(p_y) + κ_s(e′) (y's play is p_y then e′'s play), so B = LOCAL for every y whose exit is not e, which is every step of a walk in Π_s(q)
  (the e_i are distinct).»
- Premises unchanged: ROOT-C uses P1 only (+ additivity, §1). REFEREE: [Q docs/referee/R-N5-FLIP.md@72db1b18:87-88] «So ROOT-C with "path and
  exit" is SIGNED with ROOTC-1 closed by this repair; it uses P1 only (the repair adds nothing beyond P1 and additivity).»
- The (≥) half and "So κ_s(q) = min over Π_s(q)" stand.

## R3. G-FLIP-3: N3-LEVEL's parenthesis (unproved, not shown false; repaired)
- Packet text: [Q docs/si/P-N5-FLIP-box18.md@7ea3d8cf:117-118] «Let h be C's highest-ranked vertex, with rank(h) > rank(c) and h even (both
  hold when p1 is intact at t2, by (c)).»
- The gap: [Q docs/referee-2/R2-N5-FLIP.md@75b8b52a:87-88] «(c) gives a DISJUNCTION, rank(h) > rank(c) with h even, OR rank(h) < rank(c)
  with c odd; the second alternative is not excluded by anything in the packet.» There is no witness either way (REFEREE-2: 0 of 908 intact
  disjoint flips; REFEREE: 0 of 83).
- Repair, REFEREE-2's sentence as both referees accept it: replace the parenthesis "(both hold when p1 is intact at t2, by (c))" by
  [Q docs/referee-2/R2-N5-FLIP.md@75b8b52a:91-92] «"(by (c), when p1 is intact at t2 either this holds or C lies below an odd c; the lemma
  treats the former)"». (The outer quotation marks are REFEREE-2's.)
- The lemma's hypotheses and conclusion are unchanged. REFEREE: [Q docs/referee/R-N5-FLIP.md@72db1b18:180-181] «Verdict: N3-LEVEL SIGNED WITH
  GAP G-FLIP-3 (minor, a remark in parentheses; the lemma's conclusion under its stated hypotheses is unaffected).»
- Consequence for the lane's text (not frozen): note §25's READING and §26.1 use N3-LEVEL only on flips whose top h is even and above c. The
  case "C below an odd c" is OPEN as a flip type. It costs a strict length rise of κ(q2) by (c), but no level.

## Notes (one line each; the union FLIP-N1..N4 and N-FLIP-1..4)
- FLIP-N1 (REFEREE; REFEREE-2 agrees). Name R56 (d) in ROUTE-RELAY's premise line: §3's heading reads "(PROVED, every game; P1; uses R56 (d))".
  [Q docs/referee/R-N5-FLIP.md@72db1b18:137-138] «ROUTE-RELAY / SELF-FREE use R56 (d) (landed, quoted in §1); the per-item line "P1 only" is
  about standing premises; name R56 (d) there too.»
- FLIP-N2 (REFEREE). The walk-simplicity sentence in §4 should read: a repeated non-terminal vertex has a deterministic continuation to the
  same exit, which would repeat an e_i. [Q docs/referee/R-N5-FLIP.md@72db1b18:140-141] «the precise reason is that a repeated non-terminal
  vertex has a deterministic continuation to the same exit, which would repeat an e_i; harmless (and not needed by the repair, which works
  for every walk).»
- FLIP-N3 (REFEREE). ROOT does not use "in-phase"; it holds at every transition. [Q docs/referee/R-N5-FLIP.md@72db1b18:142] «FLIP-N3 (§2):
  ROOT's hypothesis "in-phase" is not used; the lemma holds at every transition.»
- FLIP-N4 (REFEREE). In N3-LEVEL's proof read the decomposition as [Q docs/referee/R-N5-FLIP.md@72db1b18:143] «"the vertices of {q2} ∪ p2
  above c, ⊔ P(Ξ_{t2} q1)"».
- N-FLIP-1 (REFEREE-2; REFEREE accepts). STATIC uses P2 only. §5's heading reads "(PROVED, every game; P2)", and "(P1 makes it the optimal
  reply's value)" is a remark. [Q docs/referee-2/R2-N5-FLIP.md@75b8b52a:95-96] «The packet lists P1 + P2; only P2 is used (σ_{k+1}'s
  optimality). Ξ_k is the play value by definition; "P1 makes it the optimal reply's value" is a remark. Over-complete, not wrong.»
- N-FLIP-2 (REFEREE-2). The 10 quotes are verbatim. No change.
- N-FLIP-3 (REFEREE-2). "exit" and "class exit path" are defined per y, independently of §3's "q on no honest cycle". ROOT-C uses them for
  every q′ ∈ Q_c, including vertices on c's cycle. No change.
- N-FLIP-4 (REFEREE-2). The data are thin where the gaps sit. No change; recorded.

## Effect on the lane's other text (not frozen; for the record)
- Note §24.1 carries ROOT-C in the packet's literal (false) form and the same false (≤) sentence. Read it with R1 and R2. Note §22.6 /
  §24.5's "PROVED" for ROOT-C means the corrected form.
- Note §26.2 (Lemma CHOSEN, Corollary RELAY-CHAIN; box 19, unrefereed) does not use ROOT-C's walk argument. It uses R56 (d), additivity and
  (SG). Its ROUTE events count a change of a class exit path OR EXIT (chosen.py uses relay.py's exits(), which compares paths and exits).
  So it is consistent with R1.
