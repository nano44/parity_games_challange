# Draft RESULTS R91 (Lead, 2026-10-30 02:58Z by date -u; subagent draft; packet, both reports, both §Cs and the fixes file H1-H16 filled; REVISED 03:24Z by date -u by the Lead: both H16 lines and REFEREE-2's explicit OPT-OFF signature recorded, see (2), (3)) — to CHECKER C101
to check: (1) TITLE. The title is the H16 line file docs/new/P-N5-GAP-box69-line-H16.txt (l-new 996d9a57, sha1 e3a23a9ae8091817576a88ade9d85ea07543719a,
= trunk = l-new head), verbatim: one line, no outer quotes, no final period, 2,988 characters (3,070 bytes plus the newline). It ALREADY carries
" (2026-10-30)" right before " — a REDUCTION" (as R89's H0 line did), so no date is inserted. The checker fill ", CHECKER PASS
(docs/checker/C101.md, checker PENDING)" is appended as in R89. The line contains "|" four times (|Z_a| and |Z_{k+1} ∖ Z_k|): harmless in the
heading; the GAPS proposal below writes them without "|". Re-measured: `git diff --no-index --word-diff` of H14 (a9e8bcae…) against H16 shows
one replacement only, «H_t);» → «H_t, H_t := S4a's arena at t (Even keeps σ_t ∪ Iσ_t, Odd follows τ_t));», as H16 (fixes l. 137-142) states.
(2) H16 CHECKED BY BOTH (Lead revision 03:24Z): REFEREE ab32b618, R-N5-GAP-C.md appended line «H16 = H14 + GAP-L4 exactly; every symbol defined or cited; MATCHES»; REFEREE-2 2c77907c, R2-N5-GAP-C.md appended line (difflib word diff vs H14: exactly the H_t insertion; «MATCHES»). The subagent's text that follows is history from the 02:53Z fetch: At the fetch of 02:53Z (date -u), origin/claude/referee head is 40fd25a3 (CUT K12 line) and
R-N5-GAP-C.md is unchanged since d21723b5; origin/claude/referee-2 head is 0140da67 and R2-N5-GAP-C.md is unchanged since ffb1eb3d; neither
file contains "H16" (git grep on both heads and on trunk). Both checked H14: REFEREE §C §5 l. 96-97 «It is complete once GAP-L4 is added: a
five-word edit, which I will word-diff check»; REFEREE-2 §C.6 l. 124 «H14 MATCHES … every symbol is defined or cited … Landable» (it did not
flag H_t; see (8)). LEAD-STATE 02:54Z: «GAP H16 … → both referees word-diff». Landing waits for both H16 lines, to be recorded in Signatures.
(3) Claims signed = the 13 items (a)-(m), each SIGNED in both verdict tables, re-read for this draft (REFEREE cd1c29d6 l. 18-29; REFEREE-2
aee8971e l. 24-35). OPT-OFF's path is recorded in item (d) with the cells and §C sentences quoted. Exactness point: REFEREE's cell (l. 21) reads
«STATEMENT TRUE; PROOF HAS A HOLE (G-GAP-1, …); SIGNED WITH MY REPAIR GAP-R1», not the words "SIGNED WITH GAP"; REFEREE-2's cell (l. 27) reads
«SIGNED with gap G-GAP-1». REFEREE's §C says in words that OPT-OFF is now SIGNED (l. 44-45, l. 101); REFEREE-2's §C says «G-GAP-1 CLOSED»
(C.2 l. 51; C.6 l. 102, l. 125) and does not repeat "OPT-OFF SIGNED"; SUPERSEDED (Lead revision 03:24Z): REFEREE-2 now signs explicitly, R2-N5-GAP-C.md l. 127 at claude/referee-2 8a0f0ed6: «Lemma OPT-OFF (§2.4): SIGNED (Opus 5.5, D15) — statement as in the packet, with the proof of fixes H1 (l-new 15044625 / c1aa183d), which closes G-GAP-1 (§C.2)»; no Lead reading is needed. One-referee notes and readings are under Referee strengthening only. (4) PREMISE LABELS (grep of
docs/RESULTS.md at trunk c46f4bb8): R15 (a) l. 631 Lemma A and (d) l. 640 «N5: every iteration applies Switch_I …»: match; R17 (a) l. 738
(F1) «the optimum of a one-player game dominates every strategy of that game pointwise»: match; R21 (a) l. 933 Lemma XW: match in content, but
R21's setting line (l. 929) is 𝒞^1O; the packet says so (§2.1 l. 70) and carries the game-general proof, and both referees sign XW on every game;
R38 (a) l. 1825 Remark KEY, the (λ_Ξ, τ)-phase: match; R57 (a) l. 2907 Premise (VJ): match; R88: blocked edges are defined in R88 (c) l.
5712-5713 «at state t ∈ [a, b)» of a frozen W-phase (the packet's §1 l. 63 reads the same condition at any state; R89 read it the same way on
W-runs); R88's W-MON (a) l. 5701 is stated inside a phase, the packet re-proves its W-MON for any S4a step (§2.2). MISMATCH (wording, for
CHECKER): the line's «the standing SPEC premise of RESULTS R57 (1E-N3: S1's procedure realises the pointwise optimum; for S4a, σ_new is the
pointwise optimum of the one-player arena H_t …)». R57 states 1E-N3 only for σ̄ (R57 (b) l. 2915-2916: «that S1's procedure realises an optimal
σ̄ is VJ00 §6 plus SPEC conformance»); the S4a form is RESULTS R67's P2 (l. 3462-3463) and R88's [OPT-H] (l. 5689-5692, «the standing SPEC
premise 1E-N3 (RESULTS R57 (b) …) in the form RESULTS R67 calls P2»). So the label is right as a name (1E-N3), and the S4a form is R67's/R88's
reading of it, not R57's text. R88 and R89 already cite it so; both referees accept it (REFEREE-2 l. 25 «standing SPEC premise of R57: S4a's
σ_new is the optimum of H_t»). (5) SYMBOL TEST of the title (IN = defined in the line; else the carrier):
| symbol | where |
| --- | --- |
| N5, SPEC S1-S5, S4a, S4c, σ_new, S1's procedure | SPEC (quoted in packet §1 l. 30-43, quote base da3fa7fa) |
| 1E-N3, pointwise optimum | RESULTS R57 (b) l. 2915-2916 (σ̄ form); S4a form R67 P2 / R88 [OPT-H] (see (4)); R17 (a) (F1) |
| H_t | IN (H16) |
| σ_t, τ_t, Iσ_t | SPEC S1, S2 (packet §1 l. 28-29 runs and states, l. 38 [S2]) |
| R15 (a), (d), R17 (a) (F1), R57 (a) (VJ), R21 (a), R38 (a), R88 | cited premises, see (4) |
| Ξ_t | IN («Ξ_t := Ξ_{σ_t} (SPEC S1)») |
| W_t, [S1-val] | IN; [S1-val] is SPEC S1 (packet l. 30-32) |
| Z_t, gap set | IN |
| phase, in-phase transition | IN (phase via RESULTS R38 (a)) |
| τ-fixed Even fallback | IN |
| piece, S4a step | IN (S4a step: SPEC S4a) |
| blocked | IN by citation, RESULTS R88 (c) l. 5712-5713 (see (4)) |
| ⊴, ▷ | SPEC S1 [S1-ord] (packet l. 33-35); not in the line, as in R88 and R89 |
| "read with τ_t" | packet §2.2 (W^τ := val(σ, τ) on G_τ) |
| one-player game of Even, ρ, Ω_ρ, Ω_ρ-cycle node | IN |
| own W-cycle node, own Ξ-cycle node | by use; packet §1 l. 54-55 |
| [p, q] | IN |
| s → s + 1, "leaves", t′ | IN (LATE-W clause) |
| re-blocked late adoption, Q | IN (parenthetical) |
| WCH_Q(c), CL_Q(v, c), u → u + 1 | IN |
| k, Z_k, Z_{k+1} | by use: k → k + 1 the fallback or step of the clause (packet §4.1-§4.4); k itself is not named in the line |
| P, a, f_P, \|Z_a\|, RO_P, WCH^S4a_P(v), ZF_P | IN |
| n | not in the line; packet §1 l. 28 (n = \|V\|); R88's and R89's titles use n the same way |
| Σ_v | by use, over V |
| CONJECTURE FB-LIN | scope tail only; packet §5 l. 148 (≤ n in-phase fallbacks per phase), RESULTS R81 l. 4596 «FB-LIN (f ≤ n per phase) is OPEN» |
| G-N5-TIME, M3, step-4 | GAPS l. 11, TARGET.md |
Every symbol is defined in the line or carried by SPEC, a cited RESULTS entry or a packet section; the two soft spots are k (by use) and n
(standard), both as in landed titles. (6) GAPS: FB-LIN has no row of its own; it is a CONJECTURE inside G-N5-TIME (GAPS l. 11, the R81 UPDATE:
«CONJECTURE FB-LIN open»). A line-11 UPDATE is proposed below, after R90's UPDATE (R90's draft proposes one), built from the title clauses only,
with no "|". (7) DATA of record is H8 / H15's corrected count set (782 / 8,442 / ZF 56; alt_all only 725), with the comp54_n80 start quarantined;
the packet's 788 / 8,532 / 731 appear only as superseded. The LATE-W «182 checks» and the nep22f_n64 record are packet figures that H8 does not
revise (H8 does not say whether comp54 entered the 182). (8) Discrepancies, recorded for CHECKER, no verdict affected: REFEREE-2 report l. 112
writes «sets σ(11) = 51» for comp54_n80; vertex 11 is Odd and the start's TAU0 sets τ(11) = 51 (REFEREE-2 §C C.3 l. 67 and H8 say τ;
re-measured: comp54_n80.pg l. 13 «11 134 1 11;», start «TAU0 … 11:51 …»); REFEREE-2 §C.6 l. 124 calls H14 complete («every symbol is defined
or cited») while REFEREE §C §5 l. 93-95 found H_t undefined (GAP-L4), which H16 adds. (9) Excluded: no lane work after the freeze except the
fixes file; L-NEW boxes 70-71 (c90503a9, 2f21ea01, 6b1466dc) are out, and so are the box 70 bullet of H8 (l. 81) and H12's last sentence
(«The same reading covers SIL-Z-type uses», l. 118), which point at box 70. H8's start-file validation in box67/energy.py and
box68/zflat.py (+3 lines each, at 15044625) is part of the fixes commit and is recorded. (10) Placement: after R90 (Lead brief: R90 lands
first).

### R91 [refereed-only] N5 on EVERY game (SPEC S1-S5, under the standing SPEC premise of RESULTS R57 (1E-N3: S1's procedure realises the pointwise optimum; for S4a, σ_new is the pointwise optimum of the one-player arena H_t, H_t := S4a's arena at t (Even keeps σ_t ∪ Iσ_t, Odd follows τ_t)); premises RESULTS R15 (a), (d), R17 (a) (F1) with R57 (a) (VJ), R21 (a), R38 (a), R88; Ξ_t := Ξ_{σ_t} (SPEC S1); W_t := the [S1-val] valuation of the (σ_t, τ_t)-plays; Z_t := {v : Ξ_t(v) ≠ W_t(v)} the gap set; a phase as in RESULTS R38 (a), an in-phase transition one with both states in one phase; a τ-fixed Even fallback an S4c transition with Iσ ≠ ∅; a piece a maximal run of consecutive states with τ constant all of whose transitions are S4a steps; blocked edges as in RESULTS R88): (Lemmas XW, W-MON, FB-W, OPT-OFF, W-SUCC) Ξ_t ⊴ W_t pointwise, W does not fall at an S4a step (read with τ_t) and does not rise at a τ-fixed Even fallback, for a one-player game of Even (Odd fixed), a pointwise-optimal Even strategy ρ (R17 (a) (F1)) with Ω_ρ its [S1-val] valuation has Ω_ρ(c) ⊴ Ω_ρ(ρ(v)) for every edge (v, c) at every Even v that is not its own Ω_ρ-cycle node, and W_t(σ_t(v)) is non-decreasing on an interval [p, q] of a piece on which v is not its own W-cycle node at any state of [p + 1, q]; (Lemma LATE-W) in a piece, if v leaves c at s → s + 1 and (v, c) is blocked at a later state t′ of the piece, with v not its own W-cycle node on [s + 1, t′], then W_{t′}(c) ▷ W_{s+1}(c), so (Corollary LATE-PIECE) the re-blocked late adoptions of (v, c) in a piece Q (S4a transitions of Q switching v to c at which (v, c) was blocked at some state of Q since v's latest leave of c in Q, or, if v has not left c in Q, at some earlier state of Q) number at most 1 + WCH_Q(c) + CL_Q(v, c) (WCH_Q(c) the transitions of Q changing W(c), CL_Q(v, c) those, other than the first, whose window [s + 1, t′] — u → u + 1 the adoption, s → s + 1 the latest leave of c by v with s + 1 ≤ u, t′ the earliest state of [s + 1, u] at which (v, c) is blocked — contains some state at which v is its own W-cycle node); (Lemma GAP-MON) at a τ-fixed Even fallback Z_{k+1} ⊆ Z_k and Ξ, W are unchanged outside Z_k; (Lemma SW-IN) a vertex switched there that is its own Ξ-cycle node at neither state has a strict Ξ-rise and lies in Z_k; (Lemma Z-FLAT) at a fallback with Z_{k+1} = Z_k all changes of Ξ and W lie in Z_k, W only falls and Ξ only rises; (Lemma REOPEN-W) an in-phase S4a step puts v into Z only with a strict rise of W(v); and (Theorem GAP-RED) every phase P with first state a has f_P ≤ |Z_a| + RO_P + ZF_P ≤ n + Σ_v WCH^S4a_P(v) + ZF_P, with f_P its in-phase (Even S4c) fallbacks, RO_P := Σ over its in-phase S4a transitions of |Z_{k+1} ∖ Z_k|, WCH^S4a_P(v) its in-phase S4a transitions changing W(v), and ZF_P its in-phase fallbacks with Z_{k+1} = Z_k (2026-10-30) — a REDUCTION of CONJECTURE FB-LIN (Σ_v WCH^S4a_P(v) and ZF_P are not bounded here; FB-LIN and G-N5-TIME stay open; not M3, not a step-4 pass, not a TARGET.md claim), CHECKER PASS (docs/checker/C101.md, checker PENDING)
- Object (L-NEW successor 35, Opus 5.5, D14/D18, Lead reading L40; frozen, unchanged during review): packet P-N5-GAP,
  docs/new/P-N5-GAP-box69.md, sha1 d67f8e04b54d5621ebecf27e7fe7151ce57793cd, 175 lines (l-new freeze
  28ceeadc39b1e4bc92f07b98acef08bfbfe90fad, 2026-10-30T00:55:29Z, the file's first commit; identical at l-new head 996d9a57 and at trunk
  c46f4bb8; the Lead's freeze word is quoted at l. 2-4 as «Lead 2026-10-30 00:52Z»; quote base l-new da3fa7fa (2026-10-30T00:52:35Z; «SPEC
  docs/new/N5-ssi-global.md lines 28-57 unchanged since 2a435f8f4», l. 6)): §0 what to sign (l. 10-25), §1 setting, premises, definitions (l.
  27-65), §2 carried lemmas (XW, W-MON, FB-W, OPT-OFF, W-SUCC), §3 late adoptions inside a piece (LATE-W, LATE-PIECE), §4 the gap set
  (GAP-MON, SW-IN, Z-FLAT, REOPEN-W, REOPEN-CHARGE), §5 Theorem GAP-RED, §6 DEAD, DATA, READING («NOT to sign», l. 25, l. 153-170). Packet
  l. 7-8: «No file of L-SI's box 40 / 42 (P-N5-CUT, LATE-SPLIT, REP-LIN) is used as a proof. L-SI's box 37 lemmas OPT-OFF and W-SUCC are NOT
  cited: both are re-proved here (§2.4, §2.5).» No quote check and no sha1 assertion for the packet is pinned in experiments/new/check.sh
  (`grep -c "d67f8e04\|P-N5-GAP"` = 0 at 996d9a57). Quotes: REFEREE l. 9-10 («the 6 [Q SPEC] quotes: 6/6 verbatim by my script», «the 3
  RESULTS quotes verbatim», box10 [⊕], [V1], [V2] «verbatim»); REFEREE-2 l. 23 («11/11 quotes verbatim (gquote.py; SHIFT=1 0/6 SPEC
  quotes)»); re-checked for this draft by a whitespace-insensitive script on da3fa7fa's SPEC, RESULTS and box10: 6/6, 3/3, 2/2. Both referees
  measured the packet sha1 at 28ceeadc (REFEREE l. 3-4; REFEREE-2 l. 6).
  The RESULTS line, history. (1) The proposal docs/new/P-N5-GAP-box69-line.txt (l-new 19dba634, 01:02:09Z; amended at 901f242d, 01:08:36Z,
  «define re-blocked late adoption (packet §3.2)»), sha1 f1c5c5d5f4ec824da68df6b56a0b60322fe1b0ec, the line both referees reviewed (REFEREE
  l. 4-5; REFEREE-2 l. 7; Lead re-hash LEAD-STATE 01:21Z). Verdicts on it: REFEREE «MATCHES §2-§5 and claims nothing more, after three small
  additions (§8: GAP-L1..L3); no E-item» (l. 31); REFEREE-2 «MATCHES §2-§5. Every symbol is defined or cited; it claims nothing beyond.
  Precision only: name the standing premise; fix CL's window (N-GAP-3)» (l. 37), «Verdict on the line: MATCHES. No required change.» (l. 138).
  (2) H9 (fixes l. 84-92): docs/new/P-N5-GAP-box69-line-H9.txt, sha1 28b7e5506a5419181c9bca8b316694c3cd21ccb3 = f1c5c5d5 + (i) the standing
  premise (N-GAP-1) + (ii) CL's fixed window (N-GAP-3); REFEREE §C §4 l. 60 («exactly the two changes H9 lists, nothing else (checked)»),
  GAP-L4 new (l. 62-63: H_t «the line does NOT define»); REFEREE-2 §C C.4 l. 75, «Verdict on H9: MATCHES, pending the H10+ definitions» (l.
  87). (3) H14 (fixes l. 121-131): docs/new/P-N5-GAP-box69-line-H14.txt, sha1 a9e8bcae1d6caec7cded179ead78f1cfedf756f9 = H9 + GAP-L3, GAP-L1
  (premise list, Ξ_t) + GAP-L2 (OPT-OFF's one-player clause); CL keeps the packet's «other than the first» (Lead decision, LEAD-STATE 02:33Z;
  fixes H14 l. 129-130). REFEREE §C §5 l. 87-97 («exactly two insertions and one replacement»; «it MATCHES §1-§5 with H1-H15 and claims
  nothing more. GAP-L1, L2 and L3 are present. It is complete once GAP-L4 is added»); REFEREE-2 §C.6 l. 113-124 («H14 MATCHES §1-§5 with
  H1-H13 … Landable»). (4) H16 (fixes l. 137-142): docs/new/P-N5-GAP-box69-line-H16.txt, sha1 e3a23a9ae8091817576a88ade9d85ea07543719a, =
  H14 + one insertion defining H_t (GAP-L4, REFEREE §C §5 l. 93-95: «Precision, not an E-item»); re-measured for this draft (word diff: that
  replacement only). H16 supersedes H14 and H9; the title is the H16 line verbatim. H16 MATCHES at both referees (REFEREE ab32b618; REFEREE-2 2c77907c).
  No E-item was raised on any version of the line by either referee.
  Setting (every game): N5 = SPEC S1-S5 with FIX 1-4; G = (V, E, Ω, owner), n = |V|; a run is the sequence of states (σ_t, τ_t), a
  TRANSITION is t → t + 1. [S1-val], [S1-ord] (⊴, ◁ strict; distinct triples distinct by RESULTS R84 (a) Fact DELTA), [S1-Xi] (Ξ_t := Ξ_{σ_t},
  σ̄_t, λ_Ξ), [S2], [S4a], [S4c], quoted at da3fa7fa (l. 30-43); [R15], [F1] (RESULTS R17 (a)); [V1], [V2], [⊕] from R17's object
  docs/new/N5-phase-bound-box10.md (l. 48-52). Definitions (l. 53-65): W_t, G_τ, «v is its own W-cycle node at t» (same for Ξ); PHASE «a
  maximal run of consecutive states with (λ_Ξ, τ) constant (RESULTS R38 (a))»; IN-PHASE (τ kept, so an S4a step or an Even S4c fallback);
  τ-FIXED EVEN FALLBACK «a transition that is an S4c fallback with Iσ_k ≠ ∅ (S4c's Even branch)»; PIECE «a maximal run of consecutive states
  with τ constant, all of whose transitions are S4a steps. H_t := σ_t ∪ Iσ_t, S4a's arena for Even at t, a one-player game (Odd follows τ_t)»;
  BLOCKED (RESULTS R88) «an Even edge (v, c), c ≠ σ_t(v), with W_t(c) ▷ W_t(σ_t v) and (v, c) ∉ Iσ_t»; GAP SET Z_t; WCH^S4a_P(v). §1 cells:
  REFEREE «CHECKED (the in-phase dichotomy re-derived)» (l. 17); REFEREE-2 «well formed; 11/11 quotes verbatim» (l. 23); both §Cs agree
  (REFEREE-2 §C l. 13 «agree»).
- Claims signed (both referees "(Opus 5.5, D15)": REFEREE successor 19, REFEREE-2 successor 21). Each item below is SIGNED in both verdict
  tables (REFEREE "## Verdicts", l. 14-31 of R-N5-GAP.md; REFEREE-2 "## 0. Verdicts", l. 20-37 of R2-N5-GAP.md; REFEREE §C table l. 9-19 and
  REFEREE-2 §C C.1 l. 10-25, "SIGNED by both" in the joint column for every item except OPT-OFF, whose joint cell records the same gap,
  CLOSED by H1: item (d)), in the frozen wording, read with H1, H2 = H11, H4, H6 = H13 and H12. Every game; plain N5. Premises LANDED: SPEC
  S1 ([S1-val], [S1-ord], [S1-Xi]), S2, S4a, S4c (quote base da3fa7fa); RESULTS R15 (a), (d); RESULTS R17 (a) [F1] and its object's [V1],
  [V2], [⊕]; RESULTS R21 (a) (XW, stated there in a 𝒞^1O setting, proof game-general, packet l. 70); RESULTS R38 (a), as the phase definition;
  RESULTS R57 (a) (VJ); RESULTS R84 (a) Fact DELTA; RESULTS R88 (blocked edges; W-MON's object §2). Standing premises (disclosure, not a
  widening; H2, l. 44-48, and H11, l. 111-113): «XW uses RESULTS R57 (a) (VJ): σ̄ is the pointwise minimum over Odd's replies. W-MON, FB-W, and
  the uses of OPT-OFF in W-SUCC and LATE-W use the standing SPEC premise of RESULTS R57 (1E-N3; as in R88, R89 FR-N1 and P-N5-CUT): S1's
  procedure realises the pointwise optimum. For S4a this means σ_new is the pointwise optimum of the one-player arena H_t, realised by plays.»
  (= RESULTS R67's P2, R88's [OPT-H]); «The code link G-N5T-1 is used by no proof.» REFEREE GAP-N1 (l. 89-90), REFEREE-2 N-GAP-1 (l.
  141-143). The code's match to SPEC is DATA (R15 G-N5T-1).
  (a) Lemma XW (§2.1, l. 68-70): "Ξ_t(v) ⊴ W_t(v) for every v and t." (σ̄_t minimises [S1-ord] at every vertex at once; τ_t is one of Odd's
      strategies.) Cells: REFEREE «SIGNED; standing premise GAP-N1» (l. 18); REFEREE-2 «SIGNED (standing premise R57 (a) (VJ): N-GAP-1)» (l.
      24).
  (b) Lemma W-MON (§2.2, l. 71-74): "If t → t + 1 is an S4a step, then W^{τ_t}_{t+1} ⊵ W^{τ_t}_t pointwise, where W^τ_s := val(σ_s, τ) on
      G_τ. In particular W_{t+1} ⊵ W_t when τ_{t+1} = τ_t." (σ_{t+1} optimal in H_t, σ_t ⊆ H_t, plays of H_t and G_{τ_t} coincide, [F1].)
      Cells: REFEREE «SIGNED» (l. 19); REFEREE-2 «SIGNED (standing SPEC premise of R57: S4a's σ_new is the optimum of H_t; N-GAP-1)» (l. 25).
  (c) Lemma FB-W (§2.3, l. 75-78; box 21 §2.5 Lemma W, fallback half, not landed; not RESULTS R21 (h)'s Lemma FB-W, a different statement (CHECKER C101 N-2)): "If k → k + 1 is a τ-fixed Even fallback, then W_{k+1} ⊴
      W_k pointwise." (S4c fires only if σ_new = σ_k, so σ_k is optimal in H_k; σ_{k+1} is a strategy of H_k; τ kept; [F1].) Cells: REFEREE
      «SIGNED» (l. 20); REFEREE-2 «SIGNED (same premise)» (l. 26).
  (d) Lemma OPT-OFF (§2.4, l. 79-93; statement unchanged, proof as repaired by H1, with H3 and H10): "Let H be a one-player game of Even (Odd
      fixed), ρ an optimal strategy of H, Ω_ρ its valuation, v an Even vertex that is not its own Ω_ρ-cycle node, and (v, c) an edge of H.
      Then Ω_ρ(c) ⊴ Ω_ρ(ρ(v))." The path to this signature, quoted:
      - Reports. REFEREE (l. 21): «STATEMENT TRUE; PROOF HAS A HOLE (G-GAP-1, Case 2 (ii) when c's ρ-play meets v's cycle node u before v);
        SIGNED WITH MY REPAIR GAP-R1 (§2), to go into the fixes file». REFEREE-2 (l. 27): «SIGNED with gap G-GAP-1 (proof step). Case 2's
        «Ω_ρ(c) is |π| + 1 longer» and (ii)'s «longer wins, so u is odd» are false when the cycle node u lies on π (v on u's cycle, c's play
        meets u before v). The statement is TRUE: the repair (§2.4) is two lines, and the data show 0 violations.» (bold «SIGNED with gap
        G-GAP-1» in the source). Found independently (REFEREE §C l. 13: «the SAME gap, found independently»; REFEREE-2 §C l. 17: «SAME GAP,
        found independently»); REFEREE-2's 3-vertex instance case2u_inst.pg (l. 57-61), accepted by hand by REFEREE (§C l. 21-22). Joint gap
        map {G-GAP-1} (REFEREE §C l. 19; REFEREE-2 §C l. 26).
      - The repair H1 (fixes l. 10-42): split by the ρ-PATH from c to its own cycle node u_c: (1a) the path avoids v and v is not on u_c's
        cycle; (1b) the path avoids v and v is on u_c's cycle (= REFEREE's (2b), REFEREE-2's u ∈ π); Case 2 the path visits v (the packet's
        computation, «|π| + 1 longer» kept only here). H10 (l. 100-110) maps REFEREE's GAP-R1 onto H1.
      - §Cs. REFEREE §C §2 l. 44-45: «G-GAP-1 is CLOSED. With H1, OPT-OFF is SIGNED (no longer conditional on my GAP-R1, which H1
        contains).»; §5 l. 82: «G-GAP-1: CLOSED via H1, and H10 correctly maps my GAP-R1 onto it.»; FINDINGS l. 101: «H1 CLOSES it (OPT-OFF
        now SIGNED outright)». REFEREE-2 §C C.2 l. 51: «The three cases are exhaustive and correct. The statement is unchanged. G-GAP-1
        CLOSED.» (bold in the source); C.6 l. 102: «H1 closes G-GAP-1: YES (C.2).»; l. 125: «Final: P-N5-GAP's only gap G-GAP-1 is CLOSED by
        H1, and H14 is the line to land.»; explicit signature, R2-N5-GAP-C.md l. 127 (1f5a9fbe, merged as 8a0f0ed6): «Lemma OPT-OFF (§2.4):
        SIGNED (Opus 5.5, D15) — statement as in the packet, with the proof of fixes H1 (l-new 15044625 / c1aa183d), which closes G-GAP-1
        (§C.2)» (CHECKER C101 N-4).
      So OPT-OFF was SIGNED WITH GAP G-GAP-1 in both reports (REFEREE: with its repair GAP-R1), H1 closes the gap in both §Cs, and OPT-OFF is
      SIGNED. Both referees' data: 0 violations of the statement (REFEREE 436,677 (v, c) pairs, 11,948 in (2b); REFEREE-2 65,486 one-player +
      647,486 run checks).
  (e) Lemma W-SUCC (§2.5, l. 94-98): "On an interval [p, q] of one piece with τ := its τ, if v is not its own W-cycle node at any state of
      [p + 1, q], then W_t(σ_t v) is non-decreasing (⊴) for t ∈ [p, q]." (W-MON; OPT-OFF in H_t at t + 1.) Cells: REFEREE «SIGNED (given
      OPT-OFF as repaired)» (l. 22); REFEREE-2 «SIGNED (uses OPT-OFF's statement, which holds)» (l. 28).
  (f) Lemma LATE-W (§3.1, l. 101-105): "Let Q be a piece. Let v leave c at s → s + 1 in Q (σ_s(v) = c ≠ σ_{s+1}(v)). Let t′ > s be a state of
      Q at which (v, c) is blocked, and let v not be its own W-cycle node at any state of [s + 1, t′]. Then W_{t′}(c) ▷ W_{s+1}(c)." (blocked,
      W-SUCC on [s + 1, t′], OPT-OFF in H_s at s + 1.) Cells: REFEREE «SIGNED (given OPT-OFF as repaired)» (l. 23); REFEREE-2 «SIGNED» (l.
      29).
  (g) Corollary LATE-PIECE (§3.2, l. 106-116), with H4 (CL's t′ := the EARLIEST state of [s + 1, u] at which (v, c) is blocked): "#(re-blocked
      late adoptions of (v, c) in Q) ≤ 1 + WCH_Q(c) + CL_Q(v, c)", WCH_Q(c) := the transitions of Q at which W(c) changes, CL_Q(v, c) := the
      re-blocked late adoptions (other than the first) whose window [s + 1, t′] contains a state at which v is its own W-cycle node. (Disjoint
      windows; LATE-W on each off-cycle window.) Cells: REFEREE «SIGNED» (l. 24); REFEREE-2 «SIGNED (CL's t′ should be fixed, e.g. as the
      earliest blocked state: N-GAP-3)» (l. 30). H4 (l. 54-57): «The proof is unchanged: it works for any fixed choice of t′».
  (h) Lemma GAP-MON (§4.1, l. 119-121): "If k → k + 1 is a τ-fixed Even fallback, then Z_{k+1} ⊆ Z_k, and every v ∉ Z_k has Ξ_{k+1}(v) =
      Ξ_k(v) and W_{k+1}(v) = W_k(v)." (FB-W, [R15], XW.) Cells: REFEREE «SIGNED» (l. 25); REFEREE-2 «SIGNED» (l. 31).
  (i) Lemma SW-IN (§4.2, l. 122-127), with H12 ([V2] as a statement about triples, for values of two strategy pairs): "Let k → k + 1 be a
      τ-fixed Even fallback, and v an Even vertex with σ_{k+1}(v) ≠ σ_k(v) that is its own Ξ-cycle node neither at k nor at k + 1. Then
      Ξ_{k+1}(v) ▷ Ξ_k(v); hence v ∈ Z_k." Cells: REFEREE «SIGNED» (l. 26); REFEREE-2 «SIGNED» (l. 32).
  (j) Lemma Z-FLAT (§4.3, l. 128-134), CONSEQUENCES, NOT A CHARACTERISATION (REFEREE GAP-N3, REFEREE-2 N-GAP-5, fixes H6 l. 64-66 and H13 l.
      119-120: «Read its title as "Lemma Z-FLAT (consequences)"»): at a Z-flat fallback (Z_{k+1} = Z_k), "(a) Ξ and W change only at
      vertices of Z_k (GAP-MON); (b) every switched Even vertex that is its own Ξ-cycle node neither at k nor at k + 1 lies in Z_k and has a
      strict Ξ-rise (SW-IN); (c) W_{k+1} ⊴ W_k pointwise (FB-W), and Ξ_{k+1} ⊵ Ξ_k pointwise ([R15]); (d) no vertex of Z_k has Ξ_{k+1}(v) =
      W_{k+1}(v) (definition)." Cells: REFEREE «SIGNED (consequences, not a characterisation: GAP-N3)» (l. 27); REFEREE-2 «SIGNED (a list of
      consequences, not a characterisation: N-GAP-5)» (l. 33).
  (k) Lemma REOPEN-W (§4.4, l. 136-138): "Let k → k + 1 be an in-phase S4a transition. If v ∉ Z_k and v ∈ Z_{k+1}, then W_{k+1}(v) ▷
      W_k(v)." (W-MON, [R15], XW.) Cells (one row with (l)): REFEREE «SIGNED» (l. 28); REFEREE-2 «SIGNED» (l. 34).
  (l) Corollary REOPEN-CHARGE (§4.4, l. 139-140): "For a phase P, RO_P := Σ over the in-phase S4a transitions k → k + 1 of P of |Z_{k+1} ∖
      Z_k|. Then RO_P ≤ Σ_v WCH^S4a_P(v)." Cells: as (k).
  (m) Theorem GAP-RED (§5, l. 142-147): "For every phase P with first state a: let f_P := its in-phase fallbacks, ZF_P := its Z-flat in-phase
      fallbacks. Then f_P ≤ |Z_a| + RO_P + ZF_P ≤ n + Σ_v WCH^S4a_P(v) + ZF_P." (|Z| drops at each non-Z-flat in-phase fallback by GAP-MON,
      grows at an S4a step by at most |Z_{k+1} ∖ Z_k|; then REOPEN-CHARGE.) Cells: REFEREE «SIGNED (it uses OPT-OFF nowhere: XW, W-MON, FB-W,
      GAP-MON, REOPEN-W, [R15] only)» (l. 29); REFEREE-2 «SIGNED. The bullet after the proof overstates: FB-LIN (≤ n) does not follow from
      polynomial bounds, only a polynomial form does (N-GAP-4; not in the line)» (l. 35); REFEREE-2 §C l. 23: «I agree it does not use
      OPT-OFF». The bullet (l. 148-151) is not signed: see Not signed and H5.
  The RESULTS line: H16 claims less than the packet. It omits Corollary REOPEN-CHARGE by name (RO_P is defined inside GAP-RED's clause),
  Z-FLAT's (b) and (d), and the §5 bullet. Every clause it states is one of (a)-(m).
- Fixes (docs/new/P-N5-GAP-fixes-box69.md, L-NEW successor 35, APPEND-ONLY): H1-H9 at l-new 15044625 (2026-10-30T02:10:17Z, sha1
  1e223dc2e08daf88ee40e46421f2d859889230a7, 97 lines); H10-H15 at c1aa183d (02:18:12Z, `git diff --numstat 15044625 c1aa183d`: 38 added, 0
  removed; sha1 955bcea2c5dae4c6016d5f9cfeaa8bae004587e0, 135 lines); H16 at 996d9a57 (02:42:07Z, 7 added, 0 removed; sha1
  3de5bc3e5b4284c17a87c754fb78d93a214beef8, 142 lines, = trunk = l-new head). Header (l. 7-8): «H1 repairs a proof step (G-GAP-1); the
  statement of OPT-OFF is unchanged. H2-H8 are clarifications or DATA corrections. H9 is the corrected RESULTS line. No signed statement
  changes.» Each item with its class (REFEREE §C §3 l. 48-57 and §5 l. 84-86; REFEREE-2 §C C.3 l. 55-64 and C.6 l. 106-112):
  H1 PROOF REPAIR of OPT-OFF (G-GAP-1; statement unchanged; closes the gap, item (d)). H2 CLARIFICATION (standing premise named; GAP-N1 =
  N-GAP-1). H3 CLARIFICATION (Case 1 wording «paths to the cycle node», N-GAP-2; folded into H1 (1a)). H4 PRECISION (REFEREE: «fixes a choice
  the proof leaves free … Not a widening») / clarification (REFEREE-2) (CL's t′, N-GAP-3). H5 NARROWING of the unsigned §5 bullet (N-GAP-4;
  REFEREE «a NARROWING of an unsigned READING bullet; correct»). H6 CLARIFICATION (Z-FLAT = consequences; GAP-N3 = N-GAP-5). H7 READING
  (REFEREE: «READING; correct (CUT's Case 3 = H1's (1b))») / clarification (REFEREE-2) (relation to P-N5-CUT, N-GAP-6). H8 DATA CORRECTION
  (comp54_n80 non-edge start quarantined; corrected counts; N-GAP-7). H9 CORRECTED LINE (superseded by H14, then H16). H10 MAPPING (GAP-R1 onto
  H1; REFEREE-2 «a correspondence between the two repairs»). H11 CLARIFICATION (= H2 with R57 (a) named; GAP-N1). H12 CLARIFICATION ([V2] as a
  statement about triples; GAP-N2; REFEREE «exactly my GAP-N2: correct»). H13 = H6 (GAP-N3). H14 COMPLETE CORRECTED LINE (GAP-L1..L3;
  superseded by H16). H15 = H8 (DATA). H16 LINE CORRECTION (GAP-L4: H_t defined; one insertion), MATCHES at both referees (REFEREE ab32b618; REFEREE-2 2c77907c). Neither
  referee finds a widening: REFEREE §C §5 l. 86: «With §3: H2-H15 are clarifications, one narrowing (H5), one precision (H4) and DATA (H8 /
  H15). No signed statement widens.»; REFEREE-2 §C.6 l. 112: «None widens a signed statement.» The statements above are in the frozen
  wording, read with H1, H2, H4, H6, H11, H12, H13. No quote check is pinned for the fixes file.
- Not signed: §6 (DEAD, DATA, READING, «NOT to sign», l. 25): DEAD energies and DATA (Data below); READING «Z-flat fallbacks are Ξ-climbs
  inside a gap that stays open (the Ξ-route)» and «Re-openings are W-changes, i.e. the WCH ↔ R* quantity of RESULTS R88 / R89 (FW-R*,
  GP*-RUN) read per vertex» (l. 167-169). §5's bullet (l. 148-151, «CONJECTURE FB-LIN … and any polynomial form of it follow from …»), as
  narrowed by H5 (l. 59-62: «polynomial bounds per phase on Σ_v WCH^S4a_P(v) and ZF_P give a POLYNOMIAL form of FB-LIN. FB-LIN itself (≤ n)
  would need, for example, RO_P + ZF_P ≤ n − |Z_a|»). The working notes docs/new/N5-LATE-box66.md, N5-FBENERGY-box67.md, N5-ZFLAT-box68.md
  («THIS packet governs where they differ», l. 4-5): not refereed here. L-NEW boxes 70-71 (SIL-Z, SC-GXC, the s2piece_n32 kill; l-new c90503a9,
  2f21ea01, 6b1466dc), committed after the freeze, are excluded from this entry, as are H8's box 70 bullet and H12's SIL-Z sentence.
- Referee strengthening (NOT part of this entry; remarks of one referee, or of both outside the verdict cells, or optional wording):
  (0) LATE-PIECE's CL and "other than the first": REFEREE §8 l. 122: the proposal's CL «drops "other than the first" from CL: a superset, the
  bound stays true»; the line keeps the packet's form (Lead decision 02:33Z; H14 l. 129-130: «Either reading is a true statement; H14 keeps the
  packet's»). One referee.
  (i) REOPEN-W's in-phase premise: REFEREE §4 l. 78: «MUT 2 (the same at τ-changing S4a steps, W in the new frame): 0 violations in 4,401
  checks: the in-phase premise is used by the proof (W-MON needs τ kept) but its necessity is not exhibited.» One referee; nothing claimed.
  (ii) H5's sharper sufficient condition for FB-LIN itself (RO_P + ZF_P ≤ n − |Z_a|): REFEREE §C l. 53 «correct»; REFEREE-2 N-GAP-4 (l.
  147-149) «FB-LIN needs RO_P + ZF_P ≤ n − |Z_a|, or the like». A READING, not signed.
  (iii) H7 / N-GAP-6: P-N5-GAP's OPT-OFF is P-N5-CUT's OPT-OFF (ii) in general one-player form; «The Lead may route one shared statement and
  proof for both packets» (H7 l. 69-70); REFEREE l. 58-59 (GAP-R1 «is the argument of Case 3 in L-SI's independent OPT-OFF (ii), P-N5-CUT
  §2»). A READING; this entry signs GAP's OPT-OFF on its own text (REFEREE l. 7-8).
  (iv) H12's general triple reading of [V2]: REFEREE-2 §C.6 l. 109-110 adds «for different cycle nodes, the rewards are unchanged» (one
  referee). H12's last sentence («The same reading covers SIL-Z-type uses») refers to post-freeze box 70 and is not part of this entry.
  (v) GAP-L4: REFEREE §C §5 l. 94: «Precision, not an E-item: "for S4a" makes the reading natural.» REFEREE-2 did not raise it.
  (vi) Self-corrections: REFEREE §C l. 24-25 «N-GAP-3 … I MISSED it», «N-GAP-4 … I MISSED it».
- Honest limits: (i) A REDUCTION of CONJECTURE FB-LIN. GAP-RED bounds the in-phase fallbacks of one phase by n + Σ_v WCH^S4a_P(v) + ZF_P;
  neither Σ_v WCH^S4a_P(v) nor ZF_P is bounded here. Packet l. 5: «Status: REDUCTION only. FB-LIN and G-N5-TIME stay OPEN. Not a TARGET.md
  claim.» REFEREE l. 11-12, REFEREE-2 l. 17-18: the same. Polynomial bounds on both would give a POLYNOMIAL form of FB-LIN, not FB-LIN itself
  (H5). (ii) Per phase; the entry does not combine GAP-RED with any count of phases or of fallbacks outside phases. (iii) LATE-PIECE counts
  re-blocked late adoptions only, and CL_Q is not bounded here; REFEREE-2 counts late adoptions that are not re-blocked (X_LP_nore 38 on sbcg,
  7 on alt_all, l. 91-92), which the corollary does not count. (iv) Standing premises: R57 (a) (VJ) for XW; 1E-N3 in its S4a form (R67 P2,
  R88 [OPT-H]) for W-MON, FB-W and OPT-OFF's uses (H2, H11); the code's match to SPEC is DATA (R15 G-N5T-1). (v) Counts are transitions, not
  bit operations; no running-time bound. (vi) Not M3, not a step-4 pass, not a TARGET.md claim; FB-LIN and G-N5-TIME stay open.
- Data (DATA, not proof): pinned (packet §6 l. 170: «experiments/new/check.sh blocks "box 66", "box 67", "box 68"»; check.sh at 28ceeadc sha1
  44f4d83a07e54130a531828004d0cf368968a809, 333 lines, blocks at l. 315-332; at 996d9a57 check.sh adds 12 lines after l. 332 (box 70, 71
  pins, excluded) and leaves l. 315-332 unchanged). "box 66" l. 315-320 (box66/latepair.py on ../n5-exhaustive/instances/b6_xl2_n32.pg);
  "box 67" l. 321-326 (box67/energy.py on n5-epoch/instances/lend9_n8.pg with .start); "box 68" l. 327-332 (box68/zflat.py on
  n5-epoch/instances/nep22f_n64.pg with .start). Files at 28ceeadc: latepair.py e76a3c8566ddc3703c69e376f8c54efe2f0de5a9 (unchanged at
  996d9a57), energy.py 60bb23b8245325f74883ce230fd462fe60bbba46 (13a1b845b52e9b92bc7d0aae955b48f7693036b6 at 15044625 and 996d9a57: +3 lines,
  H8's start validation), zflat.py 807bedeb03f412e0316cef97ce434717e88a2b00 (f5302e4021bf85bd0392681f3040a7606c3894cc, +3 lines, H8),
  b6_xl2_n32.pg 909c737192e39d8e2b80f9ba5180d39eb0009cfe, lend9_n8.pg c2d575e8c5dbb55845be64d177fdb400414979bd (.start c75d0a40…),
  nep22f_n64.pg d98de59fb84821bafc15128fd928c70ea6c71f1d (.start a7ecb00e…); instances unchanged at 996d9a57 and trunk. Re-run for this draft
  from a `git archive` of 28ceeadc and of 996d9a57 (experiments/; `python3 -I`, outputs to scratch files, exit codes read; the two archives
  give identical output): «LATEPAIR b6_xl2_n32.pg n 32 late 16 max-per-lambda-run-edge 4 max-per-piece-edge 1 max-per-Wrun-edge 1 LATE-W
  checked 1 viol 0», rc 0; «ENERGY lend9_n8.pg n 8 inphase-fb 3 fmax 3 FBUP [3, 2, 3, 3, 3, 1] SAUP [0, 0, 2, 0, 2, 1] worst-phase {'f': 3,
  'e3s': 4, 'up3': 2, 'drop3': 0} ZGROW 0», rc 0; «ZFLAT nep22f_n64.pg n 64 {'fb': 10, 'zflat': 10, 'zflat_wch': 10, 'swout': 0, 'reop': 0,
  'reopnw': 0, 'sa': 11} worst-phase {'zf': 10, 'reop': 0, 'wch': 39} max-cyclenodes-of-Z-at-zflat (1, 2)», rc 0. Each of the three greps
  matches.
  Lane corpus DATA (packet §6 l. 161-166, CORRECTED by H8 / H15; corpus experiments/si/root/logs/alt_all.lst, 413 games with starts, +
  fb38_n48, pl130_n40, long121_n40 with starts, WITHOUT the comp54_n80 run): GAP-MON: Z grows at 0 of 782 in-phase fallbacks; SW-IN: 0
  switched off-cycle vertices outside Z; REOPEN-W: 8,442 / 8,442 re-openings with a W-rise; Z-flat: 56 of 782, record nep22f_n64 (10 in one
  phase, |Z| = 59 of 64, 1 Ξ cycle node in Z; check.sh "box 68"); LATE-W: 182 checks, 0 violations (box 66, latepair.py; a packet figure H8
  does not revise); the inversion-potential import for LATE is DEAD at piece boundaries: b6_xl2_n32 (sha1 909c7371…), one edge late-adopted 4
  times in one λ-run, once per piece (check.sh "box 66"). The comp54_n80 quarantine (H8 l. 72-82, H15 l. 132-135): its start file
  experiments/red/n3/instances/comp54_n80.start (L-RED's, not edited) sets τ(11) = 51 while vertex 11 is Odd with the single successor 11 (a
  NON-EDGE), so «That run is not an N5 run»; re-measured: comp54_n80.pg l. 13 «11 134 1 11;», the start's «TAU0 … 11:51 …»; energy.py at
  996d9a57 on it: «INVALID-START comp54_n80.pg non-edges [(11, 51)]», exit 2. The packet's 788 in-phase fallbacks and 8,532 re-openings
  (and box 67's 731) included that run and are SUPERSEDED; they are not data of record. REFEREE-2 §C C.3 l. 68-70: «in-phase fallbacks 782,
  re-openings 8,442 (all with a W-rise), ZF 56. Equal to mine»; «box 67, alt_all only: 725 in-phase fallbacks. Equal to mine».
  DEAD in the packet (§6 l. 154-160, box 67, experiments/new/box67/energy.py): six candidate Lyapunov energies for "drops at every in-phase
  fallback": E1 = #Even v with Iσ(v) ≠ ∅; E2 = Σ(rank + 1) over those; E3 = |Z|; E4 = |D|, D = {Odd u : σ̄(u) ≠ τ(u)}; E5 = #v whose (σ,
  τ)-play meets D; E6 = #blocked edges. Fallbacks at which each does NOT strictly drop, on alt_all only, corrected by H8 (l. 79-80) to 725
  in-phase fallbacks (was 731): E1 532, E2 408, E3 56, E4 679, E5 55, E6 298 (rises at S4a steps: 1207, 2930, 2424, 469, 2413, 1102); «The
  DEAD verdicts and lend9_n8 are unchanged.» Smallest killing instance for E3 / E5: experiments/n5-epoch/instances/lend9_n8.pg with its
  .start (n 8), 3 in-phase fallbacks in one phase with no drop of E3 (check.sh "box 67"). REFEREE-2 §C C.3 l. 71: «The FBUP / SAUP energy
  figures … are lane tools' counts I did not recompute.»; both referees reproduce lend9_n8's 3 in-phase fallbacks (REFEREE §7 l. 104;
  REFEREE-2 §4 l. 114-115).
  REFEREE (successor 19; own docs/referee/scratch/gap_probe.py on rl_engine, no lane code; pinned l. 315-332 run alone in a clean `git worktree
  add --detach` at 28ceeadc: three PASS lines, exit 0, l. 96-97): corpus alt_all.lst + fb38_n48, pl130_n40, long121_n40, given start and S3
  start, 394 games with n ≤ 140 (22 larger skipped), 481 runs, 11,064 transitions: 0 violations of XW (493,493 vertex checks), FBW and GAP-MON
  (948 τ-fixed Even fallbacks), SW-IN (2,945), Z-FLAT (74 Z-flat fallbacks; most in one phase 10), REOPEN-W (9,050 re-openings, every one with
  a W-rise), GAP-RED (2,624 phases; most in-phase fallbacks in one phase 38), OPT-OFF (436,677 (v, c) pairs; (2b) 11,948, with S′ = ∅
  11,781), LATE-W (1,075), LATE-PIECE (1,918 (piece, edge) checks; most re-blocked adoptions 2); controls MUT 1 / 3 / 4 / 5 bite (36 / 3,375 /
  10 / 33), MUT 2 does not; pins nep22f_n64 10, lend9_n8 3, b6_xl2_n32 LP_max 1 (l. 98-105). Its alt_all counts include comp54 from a
  repaired valid start (§C l. 26-27: «my parser repaired that start (a NOTE: «forced vertex 11 → 51; using 11») and ran a valid N5 run from
  the repaired start … No verdict rests on it.»).
  REFEREE-2 (successor 21; own R2-N5-GAP/gap_check.py on its lane's dual_check.Runner (SPEC N5 on si.py), case2u.py, gquote.py; the lane's
  box66-box68 scripts only as the pinned blocks, detached worktree at 28ceeadc under `set -euo pipefail`, exit 0, three PASS lines,
  logs/pinned_check.txt, l. 12-15): corpora sbcg 719 games (S3), alt_all 413 (pinned starts, and start-or-S3), the named six with starts + S3
  + random, random 2,000 games n 5-14, one-player random 10,500 games; every log RESULT PASS, 0 violations of XW, WM, FBW, OO, WS, LW, LP, GM,
  SI, ZF, RW, RC, GR (l. 117-122); OO 65,486 one-player checks (optimality of ρ itself checked in 31,500) and 647,486 run checks; u ∈ π census
  8,907 (6,957 with S = ∅, u even) one-player, 17,139 (15,355) sbcg; WS 473,219 (sbcg); LW 3,558 sbcg, 2,417 alt_all; LP 1,581 re-blocked
  adoptions (sbcg); controls X_OO_own bites, X_SI_own 31 (sbcg) and 168 (random); lane corpus with start validation 782 / 56 / 8,442 /
  GAP-MON 0; X_FBLIN 0 («In no phase of any corpus does f_P exceed n», max f_P 38 on fb38_n48, n 48; DATA, not a claim of FB-LIN). Instance
  case2u_inst.pg (n 3) for G-GAP-1. No signed statement uses any count.
- Signatures: REFEREE docs/referee/R-N5-GAP.md (report cd1c29d611692e19d515958a3b662ff904450cb3, 2026-10-30T01:53:43Z, sha1
  9bb4387d654927091b17c50c9d71bfb063a1ecf2, 133 lines, = referee head = trunk; successor 19): §1 CHECKED; XW, W-MON, FB-W, W-SUCC, LATE-W,
  LATE-PIECE, GAP-MON, SW-IN, Z-FLAT, REOPEN-W, REOPEN-CHARGE, GAP-RED SIGNED; OPT-OFF «STATEMENT TRUE; PROOF HAS A HOLE (G-GAP-1 …); SIGNED
  WITH MY REPAIR GAP-R1»; «One gap (G-GAP-1), in a proof, with a repair; the statement is true and nothing FALSE is claimed.» (l. 32). §C
  docs/referee/R-N5-GAP-C.md (0f3caaabda5efb42eb759d931e122b6042c7e04e, 2026-10-30T02:23:14Z, sha1 1ed56613d890a567403d5273dc1b38ab66fd0ce9
  there, 85 lines; §5 addendum d21723b5056b4deae38bfbb9c2a8f5e09e79ea59, 02:32:32Z, `git diff --numstat 0f3caaab d21723b5`: 20 added, 1
  removed (the old NEEDS line, replaced), sha1 dcbd5d3dca69f063d900c7be6abbfd5ec2516e24 there, 104 lines; H16 line ab32b618, 02:52:56Z, 2 added, 0 removed, sha1 27419e3075c02ad39f056656d66ef79e343eec51, 106 lines, = trunk, unchanged at referee head a455907e); H16 line: MATCHES (ab32b618). REFEREE-2 docs/referee-2/R2-N5-GAP.md (report 6e645c5acacabfb2f27078d94b083cd4e776bd65, 2026-10-30T01:48:04Z,
  merged on claude/referee-2 as aee8971e0f304c119f2e8b12d77fc17d2bf6e6bc, 01:48:05Z, the SHA the Lead, REFEREE §C and REFEREE-2 §C cite; sha1
  84a495d7270a825f350718d1d7dcde5e5ef1a667, 163 lines, = trunk; successor 21): §1 well formed; twelve items SIGNED, OPT-OFF «SIGNED with gap
  G-GAP-1»; «One gap, G-GAP-1: a proof step of OPT-OFF, repaired here; the statement is not in doubt. Nothing FALSE. Notes N-GAP-1..N-GAP-7.»
  (l. 39). §C docs/referee-2/R2-N5-GAP-C.md (949be74e73c6eaa763e1c396de40ceebd6b06fa5, 02:22:46Z, merged as 1b29329d, sha1
  1554be21abdb3ca948f0774f91aa034d4e65b59c there, 95 lines; §C.6 899d98384342681a90aebed82e6e46c7bbe2c23e, 02:32:51Z, merged as ffb1eb3d,
  02:32:52Z, `git diff --numstat 1b29329d ffb1eb3d`: 30 added, 0 removed; sha1 f6898956e35c4d84878448370349daea7b5290d0 there, 125 lines; H16 line e9aaaa6e, 02:53:15Z, merged as 2c77907c, 1 added, 0 removed, sha1 f10479f7e04c632527cb1cf568146a5b5140860e, 126 lines; OPT-OFF explicit signature 1f5a9fbe, 03:03:41Z, merged as 8a0f0ed6, 1 added, 0 removed (l. 127), sha1 6ae1c91e8863b725d226ab9517c14f1373ebe3c7, 127 lines, = trunk = referee-2 head 8a0f0ed6); H16 line: MATCHES (2c77907c); OPT-OFF explicit signature l. 127 (8a0f0ed6). INDEPENDENCE: REFEREE l. 7: «Independence: no docs/referee-2/ file opened.»;
  REFEREE §C l. 3-4: its report «pushed BEFORE I opened any REFEREE-2 GAP file», REFEREE-2's «opened 02:21Z after the Lead's word». REFEREE-2
  l. 12-13: «`git ls-tree --name-only -r origin/claude/referee docs/referee/ | grep -ic gap`: 0 at 01:41Z and at push time (see commit). Names
  only; nothing opened; no `git log` on origin/claude/referee.»; REFEREE-2 §C l. 4: REFEREE's report «opened only after the word». No review
  imported lane code.
  §C (both): verdicts identical (REFEREE §C l. 19: «Gap map = {G-GAP-1} (one proof step, both referees, same configuration, equivalent
  repairs). Nothing FALSE. No disagreement on any verdict.»; REFEREE-2 §C l. 26: «Joint gap map: one entry, G-GAP-1 (OPT-OFF, a proof step;
  the statement is true; found by both).» (bold in the source)); G-GAP-1 CLOSED by H1 in both (item (d)). Fixes: REFEREE §C §3 l. 57: «None
  widens a signed statement.»; §5 l. 86 (quoted under Fixes); REFEREE-2 §C.6 l. 106-112 «H2-H15: clarifications only … None widens a signed
  statement.»; l. 125 «Final: P-N5-GAP's only gap G-GAP-1 is CLOSED by H1, and H14 is the line to land.» Two discrepancies, no verdict
  affected: REFEREE-2 l. 112 «sets σ(11) = 51» (τ(11) = 51: §C C.3 l. 67, H8); REFEREE-2 §C.6 l. 124 «every symbol is defined or cited» for
  H14, which lacked H_t's definition (REFEREE's GAP-L4, added by H16).
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (structural lemmas on N5 inside a phase and inside a piece, and a REDUCTION of the
  in-phase fallbacks of one phase to Σ_v WCH^S4a_P(v) and ZF_P, neither of which is bounded; no bound on a run, no running-time bound, no
  algorithm claim). GAPS G-N5-TIME: open; CONJECTURE FB-LIN: open.

Proposed GAPS line-11 UPDATE (append-only), after R90's UPDATE of G-N5-TIME (GAPS l. 11; after the R89 UPDATE if R90 adds none), built only
from the title clauses (landing time and CHECKER addendum to be filled at landing; no "|": |Z_a| is written "the size of Z_a" and |Z_{k+1} ∖
Z_k| "the number of vertices of Z_{k+1} ∖ Z_k"): «UPDATE 2026-10-30 <HH:MM>Z: RESULTS R91 (P-N5-GAP; CHECKER C101 Add. <k>) [refereed-only]
LANDED: on every game, under the standing SPEC premise of RESULTS R57 (1E-N3; for S4a, σ_new is the pointwise optimum of the one-player arena
H_t, S4a's arena at t: Even keeps σ_t ∪ Iσ_t, Odd follows τ_t) (Ξ_t := Ξ_{σ_t}; W_t the [S1-val] valuation of the (σ_t, τ_t)-plays; Z_t :=
{v : Ξ_t(v) ≠ W_t(v)} the gap set; a phase as in RESULTS R38 (a), an in-phase transition one with both states in one phase; a τ-fixed Even
fallback an S4c transition with Iσ ≠ ∅; a piece a maximal run of consecutive states with τ constant all of whose transitions are S4a steps;
blocked edges as in RESULTS R88), Ξ_t ⊴ W_t pointwise, W does not fall at an S4a step (read with τ_t) and does not rise at a τ-fixed Even
fallback, for a one-player game of Even (Odd fixed) a pointwise-optimal Even strategy ρ with Ω_ρ its [S1-val] valuation has Ω_ρ(c) ⊴
Ω_ρ(ρ(v)) for every edge (v, c) at every Even v that is not its own Ω_ρ-cycle node, and W_t(σ_t(v)) is non-decreasing on an interval [p, q]
of a piece on which v is not its own W-cycle node at any state of [p + 1, q] (Lemmas XW, W-MON, FB-W, OPT-OFF, W-SUCC); in a piece, if v
leaves c at s → s + 1 and (v, c) is blocked at a later state t′ of the piece, with v not its own W-cycle node on [s + 1, t′], then W_{t′}(c)
▷ W_{s+1}(c) (Lemma LATE-W), so the re-blocked late adoptions of (v, c) in a piece Q (S4a transitions of Q switching v to c at which (v, c)
was blocked at some state of Q since v's latest leave of c in Q, or, if v has not left c in Q, at some earlier state of Q) number at most 1 +
WCH_Q(c) + CL_Q(v, c), WCH_Q(c) the transitions of Q changing W(c), CL_Q(v, c) those, other than the first, whose window [s + 1, t′] (u → u
+ 1 the adoption, s → s + 1 the latest leave of c by v with s + 1 ≤ u, t′ the earliest state of [s + 1, u] at which (v, c) is blocked)
contains some state at which v is its own W-cycle node (Corollary LATE-PIECE); at a τ-fixed Even fallback Z_{k+1} ⊆ Z_k and Ξ, W are
unchanged outside Z_k (Lemma GAP-MON); a vertex switched there that is its own Ξ-cycle node at neither state has a strict Ξ-rise and lies in
Z_k (Lemma SW-IN); at a fallback with Z_{k+1} = Z_k all changes of Ξ and W lie in Z_k, W only falls and Ξ only rises (Lemma Z-FLAT); an
in-phase S4a step puts v into Z only with a strict rise of W(v) (Lemma REOPEN-W); every phase P with first state a has f_P ≤ the size of Z_a
+ RO_P + ZF_P ≤ n + Σ_v WCH^S4a_P(v) + ZF_P, f_P its in-phase (Even S4c) fallbacks, RO_P the sum over its in-phase S4a transitions of the
number of vertices of Z_{k+1} ∖ Z_k, WCH^S4a_P(v) its in-phase S4a transitions changing W(v), ZF_P its in-phase fallbacks with Z_{k+1} = Z_k
(Theorem GAP-RED): a REDUCTION of CONJECTURE FB-LIN; Σ_v WCH^S4a_P(v) and ZF_P are not bounded here. FB-LIN and G-N5-TIME stay open.»
