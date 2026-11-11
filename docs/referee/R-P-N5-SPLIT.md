# R-P-N5-SPLIT: first referee report on packet P-N5-SPLIT (boxes 197-199)
REFEREE successor 30 (Opus 5.5, D15; D1). Date -u at writing: 2026-11-09T09:28Z.
Object: claude/l-new 399cda07 (ancestor of origin/claude/l-new, checked), docs/new/P-N5-SPLIT.md sha1
5bc1b1f390ed81683fe5c93008c7ea0b338fe735, 30,949 B, 275 lines; fixes entry 1 at 63515442 (packet unchanged there: same sha1). Premise packet
P-N5-CHAIN frozen sha1 6e613ba7 (my lane's reviews: R-P-N5-CHAIN.md §0-§E; L-4 a69c8aa9 MATCHES). docs/referee-2/ and L-RED 62's
R228-box91 / R229 reads NOT read before this verdict.

## 0. Verdicts (every row CONDITIONAL on R125 = P-N5-CHAIN landing, as the packet states)
| § | statement | verdict |
| --- | --- | --- |
| §2 | Lemma SPLIT (i)-(iv) incl. TRANSFER | **SIGN** |
| §3 | Lemma REWIN (a)(b), REWIN-HI (c); Corollary REWIN-COUNT | **SIGN WITH SP-1** ((LEX-Λ) read for non-core vertices; every use is on pads) |
| §4 | Lemma PAIR-SPLIT (a′)(b′)(c′); Corollary SPLIT-COUNT (SPL ≤ 3M) | **SIGN WITH SP-1** |
| §4 | Lemma RW-SHAPE, RW-SHAPE*; Corollary RW-1 | **SIGN WITH SP-1** |
| §5 | Lemma PAIR-HIGH (a)(b)(c); Lemma RA-PATHS | **SIGN** (abstract; E-MON3 only) |
| §6 | RE-COUNT, RE-EQUIV, PAIR-COUNT (corrected), ALT-EQUIV (corrected), C-EQUIV | **SIGN** |
| §7 | ASC-WIT, ASC-ROOT | **SIGN** under HYPOTHESIS [E-LEV] (ASC-WIT (c) WITH SP-1) |
| §8 | DEAD D1-D7 | D1, D2, D4, D5, D6 reproduced by the lane's check199.sh (lane code, re-run, byte-equal); D3, D7 cited, not re-run |
No GAP; nothing refused. SP-2 is a citation requirement for the line, not a gap. TARGET.md diff CLEAN (§6).

## 1. Premises: each P-N5-CHAIN fact named in §1, located in P-N5-CHAIN (frozen text 6e613ba7) and in R125's line (L-4 a69c8aa9)
- In P-N5-CHAIN's «To sign» rows (signed by both referees): F1, F3, F4′, F5, F6, DOM, STRICT (§4); CN2-3, LOC-GATE3, LOC-K2-3, B-ONLY3,
  NO-TIE3 (§5); QUIET3 with L3, T-QUIET3 (§6; its Σ-form with the W-1 repair, R-P-N5-CHAIN §D follow-up 1); E-MON3, CHAIN-DECOMP3 (§7);
  HYPOTHESIS [E-LEV].
- In P-N5-CHAIN's text but NOT in its «To sign» rows: [OPT] (§1 premise: R118 (b) + R21 (a)), [G3] (R117 quote), [DEF] (R104 quote), (R),
  (P), (E-DOM), (Core) (§2 readings), F2 and CYC (§4, stated with reasons). R125's line names [OPT] and CYC but not F2, (Core) or (E-DOM).
  - Re-derived here: F2 ([VJ] compares the reward of Λ first; priorities are injective by rank, so distinct cycle nodes have distinct
    rewards); (E-DOM) ((R): above every e only c_W, K0, K3); CYC (CN2-3, (Core) in its repaired reading, F1, F2); (R), (P) are R104 / R117
    priority facts. All sound. **SP-2 (citation, REQUIRED in the line):** cite these as P-N5-CHAIN's frozen text (sha1 6e613ba7) or their
    landed sources ([DEF] R104, [G3] R117, [OPT] R118 (b) + R21 (a)), with (Core) in the W-1 repaired reading; not as «P-N5-CHAIN facts»
    of R125's line, which does not contain F2, (Core), (E-DOM).
- The packet quotes nothing itself (premises by name); none of its uses goes beyond the named fact's statement (checked at each use, §3).

## 2. SP-1: (LEX-Λ) restates the W-1 sentence
- §1 (LEX-Λ): «K0 and K3 lie on both plays or on neither, since a play passes K0 iff it passes K3 iff its cycle node is in the closed core
  ((Core))». As written this is false for plays from pA or K3 (R2-P-N5-CHAIN W-1; R-P-N5-CHAIN §D follow-up 1).
- Every use compares values of NON-core vertices, where the repaired reading holds (only edge into the core from outside is pb_g → K0):
  REWIN (c) and PAIR-SPLIT (c′): b and a are successors of a mover (m-pads) or of a gate (pe_g, pβ_g); RW-SHAPE (ii): the same a, b;
  ASC-WIT (c): pe_(g1), pβ_(g1). So every signed proof stands on the repaired reading.
- By the Lead's L41 standard (12:24Z ruling on P-N5-QUIET; 13:12Z on P-N5-CHAIN): a frozen sentence false as written whose needed
  restriction is not in the text. The line must name it: «(LEX-Λ) is applied only to non-core vertices (pads), where P-N5-CHAIN's W-1
  repair holds». No statement changes.
- SP-3 (optional wording): (PL) «E_s(v) is the disjoint union of the e-letters strictly before u … and E_s(u)» should say «the e-letters of
  Π_s(v) strictly before u». They coincide whenever E_s(v) ≠ ∅ (then w ≠ c_W and B-ONLY3 puts w below every e-vertex). Every use has
  E ≠ ∅, so nothing changes.

## 3. Proofs, each step re-derived (frozen text)
- SPLIT (i): plays differ, so they first leave at some u by different edges; only movers and gates have a choice in HOW3 (F6, [G3];
  σ̄(K2) = r by LOC-K2-3). (ii) F5. (iii) LOC-GATE3, NO-TIE3, F1: Ω_t(old) ▷ Ω_t(new) ⊵ Ω_(t−1)(new) ▷ Ω_(t−1)(old). (iv) (PL): Λ_s(u) = w,
  E_s(v) = A_s ⊔ E_s(u) with equal prefixes A. Correct.
- REWIN (a) mover: first s ∈ (t1, t2 − 1] with σ_s(u) ≠ b; Ω_(t2−1)(u) ⊵ Ω_s(u) ▷ Ω_(s−1)(u) = ext(u, Ω_(s−1)(b)) ⊵ ext(u, Ω_t1(b)) (F1,
  STRICT, F3, F6, F4′; u ∉ Π by CN2-3); Ω_(t2−1)(u) = ext(u, Ω_(t2−1)(a)); totality + F4′ give Ω_(t2−1)(a) ▷ Ω_t1(b). Gate: LOC-GATE3,
  NO-TIE3 at t1 and F1. (b) F5 / LOC-GATE3 at t2 − 1, then (a). (c) Λ_t1(b) = Λ_(t2−1)(a) = w ((PL)); y ∈ E_t1(b), y ∉ E_(t2−1)(a); if no
  U_y-letter differed, the top of Π Δ would be y (K0 / K3: SP-1; c_W in no Π) and Ω_t1(b) ▷ Ω_(t2−1)(a), against (a); so the top is in
  U_y and in E_(t2−1)(a); and E_(t2−1)(a) ∩ U_y = E_t2(b) ∩ U_y (top y at t2, equal prefix, u ∉ Π). Correct.
- REWIN-COUNT / PAIR-SPLIT / SPLIT-COUNT: Λ(b) = w at the ends, so constant between (F1, F2): one J_b. PAIR-SPLIT re-runs (a)-(c) for any
  t < t′ of one pair: only nx_t(u) = b ≠ nx_(t′−1)(u), y ∈ E_t(b), y ∉ E_(t′−1)(a) and the top y at t′ are used (checked line by line).
  SPLIT-COUNT: pairwise distinct E(b) ∩ U_y within J_b; b determines (u, b) since b is an m-pad (M) or a face pad (2M) on standard states.
  Correct.
- RW-SHAPE: decomposition B ⊔ S with S = E(m) ∩ U_y lex-nondecreasing (Λ(m) = w on [t, t′], E-MON3); (i) from (c′). (ii) the sandwich:
  Ω_(t′−1)(a) ◁ Ω_(t′−1)(b) ⊴ Ω_t′(b), all with Λ = w, and lex order on U_y when the U_y-parts differ (U_y is an upper set); the ends agree
  on U_y, so the middle does (the bracketed argument is right); f ∈ both plays at t′ − 1, common suffix avoids y (y more relevant than w
  would be in Π), at t′ y follows f: a departure strictly between f and y (f has one successor). RW-1 follows. Correct.
- PAIR-HIGH (a)-(c), RA-PATHS: abstract, from strict lex increase (E-MON3) with entering tops. Correct.
- RE-COUNT, RE-EQUIV (T-QUIET3's Σ-form; ≤ 2M + 3 intervals by CYC; Mact ≤ M; Rtop ≤ n3·T3), PAIR-COUNT (index ↦ pair {τ_i, τ_(i+1)} is a
  switch of the collapsed restriction), ALT-EQUIV (no equal consecutive tops), C-EQUIV: Correct; each «iff» uses n3, L3 polynomial in N + M.
- ASC-WIT (a)-(d), ASC-ROOT under [E-LEV]: (a) the next e on the play would be e_(g1), of lower level, so not more relevant: no ascent;
  (c) LEX-Λ on pe_(g1), pβ_(g1) (SP-1); ASC-ROOT's induction: c_(i+1) > c_i > e_(g1) gives an ascent in seq_t(pe_(g1)) whose first one
  starts at level ≤ ℓ − 1. Correct.

## 4. Replays with my own code (scratch/split_replay.py; split_logs/)
- Engine: xicyc_replay.howard(G, pad) (own Γ3 builder, own VJ, Howard at movers from the standard start; as R-P-N5-CHAIN §4); own
  generator. No lane code. Counters (must be 0): emon, playfail, kindfail, hwfail, gtfail, trfail (SPLIT), a2fail, rh2fail (PAIR-SPLIT
  (a′)(b′)(c′), all same-pair couples), jbfail (one J_b per pair), spfail (SPLIT-COUNT with Dhi over b's whole Λ-interval), splfail (> 3M),
  phafail, phcfail (PAIR-HIGH (a), (c)). Controls: ctrlU (rh2 with U_y := ∅), ctrlG (gate test negated).
- 28 pinned instances (box199/inst from git archive 63515442; SHA1SUMS all OK) and families rand, deep, wide, selfl × 200, seed 1992:
  **every counter 0**; ctrlU fires on every instance with couples (e.g. MW32_2 30,304 couples), ctrlG fires everywhere. Records equal to the
  packet: MW32_2 max c_y 65 and T3 199; C6G8_n54 6; FW6_4 / FW8_4 5 split pairs. Random families have no re-wins (max c_y 1): they test
  SPLIT only; the pinned instances carry PAIR-SPLIT / SPLIT-COUNT. (split_logs/sweep.out)
- Lane's checks from `git archive 63515442`: split.pins 59 rows (the packet's §11 says 58; the fixes entry added one), `sha1sum -c` all
  OK; box199/check199.sh re-run: rc 0, byte-identical to check199.out (split_logs/check199_rerun.out). DEAD witnesses in it (lane code):
  D1 dn_nobelow_all 192 (CX4_n21), D2 wcfail 18 (GROW7_n34), D4 ytopB_ne 65 (ROUTELOW_n21), D5 premono_no 18 (GROW7_n34), D6 rwfail 31
  (RWX_n95). Controls fire (ctrl1 hwfail 444, ctrl2 wbfail 200, ctrl3 dnfail 219, …).
- DATA predicates read in split199.py (l. 81-151): kindfail, hwfail, gtfail (CTRL 5 negates), trfail, rh2fail (all same-pair couples),
  spfail (bound with the pair's own values, a lower bound for Dhi: stronger), rhfail, dnfail: as §9.1 states. Fixes entry 1 (n1) restates
  max c_y with its set: CORRECT and needed.

## 5. Scope
- HOW3(G) on Γ3(G), every genome; by P-N5-CHAIN's REACH3-ALL the mover part of N5′-xi from S3 until its first fallback. Nothing on N5,
  nothing outside Γ3(G). §7 only under [E-LEV]. Correct as stated.

## 6. TARGET.md diff: CLEAN
- No running-time bound; equivalences (T3 polynomial ⇔ Rtop ⇔ A ⇔ C polynomial) and one reduction (C ⇐ max Dhi_y(b, J)). Not M3, not M4, not
  M4-R, not a step-4 pass; G-N5-TIME OPEN; N5′-xi a CANDIDATE.

## 7. Line requirements (no line exists yet)
- LS-1. Every row CONDITIONAL on R125 (P-N5-CHAIN); labels as §0; §7 under HYPOTHESIS [E-LEV]; DEAD D1-D7 with instances.
- LS-2. SP-1's clause (L41): «(LEX-Λ) is applied only to non-core vertices (pads), where P-N5-CHAIN's W-1 repair holds».
- LS-3. SP-2's citation form for [OPT], [G3], [DEF], (R), (P), (E-DOM), (Core), F2, CYC.
- LS-4. Scope as §5.
- LS-5. DATA with units and sets (28 frozen instances; fixes entry 1's max c_y clause); the four definitional counters named as having no
  control; «Large zero counts are DATA, not evidence» kept.
- LS-6. The equivalences and the reduction stated as such; no polynomial claim; the open core named (max over y, b, J of Dhi_y(b, J)).
- LS-7. TARGET tail in the landed form (R123 / R124).
- LS-8. Source note: packet sha1 5bc1b1f3 frozen at l-new 399cda07 with its fixes entries; L-NEW successors 65-67; attack record L-RED 60-62.

## 8. Tools and outputs (committed, docs/referee/scratch/)
split_replay.py; split_logs/: sweep.out, check199_rerun.out.
