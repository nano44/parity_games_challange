## 12. Stage 4 (written 2026-11-13T17:17Z, date -u): the lane's fixes entries 2-5, ENTRY 4 checked (the Lead's order of 16:30Z / 16:43Z)
Stages 1-3 (§0-§11) are unchanged. Object: claude/l-red-b 24f4d436, docs/red-b/P-N5-EXP-fixes.md. NOT read: docs/referee-2/ (the
strings entry 4 quotes from it were matched by script only); the lane's DATA §4.7 (l. 460-647) and its tools were not run.
- (a) By script (log gkx_logs/fixes4.out, written by a one-off command of this session, not by s36_run.sh; its inputs are the
  git objects the lines name, the quote script is gkx_quotes.py):
  ```
@@FIXES4@@
  ```
- (b) ENTRY 4, read in full from 4.1 to 4.6 (l. 331-459):
  - 4.1 (S1) «State» means every wire AND u_0 at option 0: **E-4 CLOSED.** (S2) s⁺ is defined for every state and a hypothesis on
    the key input of step τ is a hypothesis on (s_(τ−1))⁺, «so no hypothesis is vacuous at a stopped state»; 4.4 Remark 1 shows
    that my instance (1, 1, 2^k − 1) and the triples (j, 0, 2^k − 1) are excluded: **E-1 CLOSED.**
  - 4.2 STABLE in step form (REST_i(b) under s, E_(i−1)(s) = b, C_(i−1)(s⁺) = b ⟹ s⁺ = s on unit i; then on U_i if the units above
    are at rest 0), with its proof and its two uses: correct; **E-5 CLOSED.**
  - 4.3 CAUSAL: my statement verbatim; its proof (L1)-(L3) is my argument in a well-founded order (pair and e_j; the input of unit
    j + 1; the observers): correct.
  - 4.4 LEMMA′: my statement verbatim, replacing the frozen l. 192-204; (H1), (H2′_T) read as «input (c, a) in step t, (c, c) in
    the steps t + 1..T»: correct. 4.5 the proof: downward induction on j, inside it induction on T, each step decided in the order
    (1) level-j movers, (2) the input of unit j + 1, (3) LEMMA′ for j + 1 with the same T, (4) the observers; the two inner windows'
    hypotheses and step t_2 + 1 by STABLE: this is the proof of my §5.3, complete, without a circle: **E-2 CLOSED.** 4.6 (§7 with
    LEMMA′): as my derivation. The concordance with REFEREE-2's prefix form (4.4) I read as quoted there; I did not open REF2.
  - **Verdict on entry 4: it closes E-1, E-2, E-4, E-5. RESPONSE LEMMA SIGNED as restated in fixes entry 4 (= LEMMA′ of §5.3 with
    CAUSAL and STABLE in step form).** Under L41 the lemma is referee-originated in statement, so it also needs REFEREE-2's
    independent signature.
- (c) Entries 2, 3, 5: read IN PART only (context); what I read is right, the rest is for successor 37:
  - entry 2 (l. 150-244): (a) UNCONDITIONAL: EXP-IDEAL (a)-(c); (b) «PROVED-CONDITIONAL on RESULTS R117's Theorem REACH3 AS LANDED»
    for Corollary EXP-N5; (c) the dead-end paragraph carries the condition; (d) MEASURED; (e) «CORRECT» is DATA for k ≤ 12 and
    landed R57 (b) for every k: the headings and (e) read: **P-1 and E-7 answered as asked**; its sentences not checked word by word.
  - entry 3 (l. 245-287): Corollary EXP-N5′ (exactly 2^k + 1 iterations, one fallback at iteration 2^k − 1, conditional on R124's
    EXACT-L as landed): statement read; it agrees with R124 as landed and with every measured run (§7, §10): **O-1 taken up**; its
    proof text not read.
  - entry 5 (l. 648-829): 5.1 (rank tie rule) and 5.3 (`QUOTESUMMARY`) take up **E-3 and E-6**: headings and quoted items read; the
    fix sentences not read.
- Verdict line of stage 4: **P-N5-EXP: Theorem EXP-IDEAL (a)-(c) SIGNED; RESPONSE LEMMA SIGNED as restated in fixes entry 4 (LEMMA′;
  L41: REFEREE-2's independent signature needed); Corollary EXP-N5 and the dead-end sentence SIGNED AS CONDITIONAL on R117's
  premises, as entry 2 (b), (c) now label them. Entries 1 and 4 fully checked; entries 2, 3, 5 checked in part as listed above.**
- Addendum to stage 4 (2026-11-13T17:28Z, date -u; the Lead's 17:16Z item): entry 3's **Corollary EXP-N5′, the STATEMENT, is SIGNED AS
  PROVED-CONDITIONAL on RESULTS R124 and R117 as landed**, by my own two-line derivation from the landed line R124 (l. 15371):
  ENDGAME-3-N5 gives exactly one fallback, at an iteration F, and exactly F + 2 iterations; EXACT-L gives exactly L(G) + 3 iterations
  for G ∈ IDEAL-ACYC; so F = L + 1; with MEMBER (G_k ∈ IDEAL-ACYC) and EXP-IDEAL (b) (L = 2^k − 2): exactly 2^k + 1 iterations and one
  fallback at iteration 2^k − 1, which every measured run shows (§7, §10: counter EXACT 0). Entry 3's own proof text is unread by
  me; successor 37 (session_01V5yGRXMfSsQpBQK2zihYD6) reads entries 2, 3, 5 word by word as stage 5 (the Lead's ruling, 17:20Z).
