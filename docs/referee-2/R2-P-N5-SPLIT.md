# R2-P-N5-SPLIT: second-referee report on packet P-N5-SPLIT (L-NEW successor 67, boxes 197-199)
REFEREE-2 successor 36 (Opus 5.5, D1). Written 2026-11-09 by date -u (times in the commits). Independent: docs/referee/ (REFEREE 30's
R-P-N5-SPLIT.md, ca091557) NOT read before this report's verdict is committed. L-RED 61 / 62 records (R227, R228-box199, R228-box91, R229)
are context only, and I did not read them; I used only what the packet and its fixes entry quote from them. I read the lane tool
split199.py only to learn the units of §8's DEAD counters (lines 10-34, 96-166), so that my own counters measure the same objects; no lane
code is imported or run.
Committed in boxes (one commit each): box 1 = object, premises, W-1, §1-§2; box 2 = §3-§4; box 3 = §5-§7; box 4 = DEAD and DATA replay;
box 5 = TARGET.md diff, line requirements, verdict table.

## Object (claude/l-new, FROZEN at 399cda07)
- docs/new/P-N5-SPLIT.md at 399cda07: sha1 5bc1b1f390ed81683fe5c93008c7ea0b338fe735, 30,949 B (= the brief), re-hashed by `git show`.
- Fixes entry 1 at 63515442: docs/new/P-N5-SPLIT-fixes.md, sha1 4df415ad…. It is DATA-only: (n1) restates §9.1's «max c_y ≤ 6 outside
  MW» clause with its set (the 28 frozen instances) and relays L-RED 62's MW-mutant climb (C 12 at N + M ≤ 200, C 26 at N + M ≤ 400; not
  re-run by the lane, not by me); (n2) no change. No statement, proof, premise or DEAD row changes. Packet unchanged at 63515442 (same sha1).
- No line exists yet. This report reviews the packet; the line will be byte-tested when sent.
- Pins: experiments/new/box199/split.pins, 58 rows at 399cda07, 59 at 63515442 (the fixes file added). On git archives of both commits,
  the check.sh «P-N5-SPLIT» sed (run inside box199/) gives `sha1sum -c --quiet` exit 0: every row matches.
- The DEAD instances' sha1 prefixes in the pins equal §8's: CX4_n21 ef29debb, GROW7_n34 42bbd562, HOLD2K_n84 423a4a88, ROUTELOW_n21
  80f9b977, RWX_n95 da8b3a30, NK6_cl21 408b9988, FW16_2 94df42b7, MW32_2 445031d1 (also GROW8_n53 57758f40, HOLD3K_n125 2c3e610b, DU21_h4
  48da0ccb, DSALT9_n416 da3308b5, which §8 names without a hash).
- Premise packet: P-N5-CHAIN at 93531b03, sha1 6e613ba762b6ecf67247ef6d8674b4c960013039 (= SPLIT's), fixes entries 1-3
  (docs/new/P-N5-CHAIN-fixes.md at 63515442) and line L-4 sha1 a69c8aa96fb0b67c6c0a3f6d11670a0b57ba9331, 9,082 B (= SPLIT's), re-hashed.

## Premises (own script R2-P-N5-SPLIT/r2q.py, out r2q.out)
- SPLIT §1 names its premises: P-N5-CHAIN facts only, by name and section. r2q.py looks up each name's defining text in P-N5-CHAIN
  (whitespace collapsed) and the section it sits in. All 30 are defined, each in the section SPLIT gives: HOW3(G), T3, n3 (§2); [OPT],
  [G3], [DEF], [E-LEV] (§1); (R), (P), (E-DOM), (Core) (§2); F1, F2, F3, F4′, F5, F6, DOM, STRICT, CYC (§4); CN2-3, LOC-GATE3, LOC-K2-3,
  B-ONLY3, NO-TIE3 (§5); T-QUIET3, L3 (§6); E-MON3, CHAIN-DECOMP3, seq / E / lex order (§7).
- Where SPLIT restates a premise's content, r2q.py checks SPLIT's words in SPLIT and the matching words in P-N5-CHAIN: 23 pairs, all found
  verbatim. I compared each pair's meaning by hand. 22 say the same thing. The 23rd is (LEX-Λ)'s use of (Core), which is W-1 below.
- The 11 «…» in SPLIT: none is a premise. They are the Lead's freeze words (one), DEAD claim names (2), labels («T3 polynomial», «High»)
  and check.sh block names (3). None of them carries mathematical content that a proof uses.
- Conditional status: P-N5-CHAIN is R125, pending at CHECKER C139. Every statement used is SIGNed in my predecessor's R2-P-N5-CHAIN.md
  (0e5c7c37, with Addenda 1-5; L-4 MATCHES, 3c5264e0), with CHAIN's W-1 repaired in its fixes entry 3 (signed by both referees). The Lead
  states that REFEREE also MATCHES L-4; I will check that on claude/referee after my verdict (my rule: no docs/referee/ before it). So every
  SPLIT statement is CONDITIONAL on R125 landing as signed, as the packet's «To sign» table says.
- Not used, as the packet says: no other packet, no landed R-id, no L-RED or L-SI lemma. §8 D7 cites L-SI's census as DATA of another lane;
  that is not a premise of any PROVED row.

## W-1 (wording defect in §1 (LEX-Λ); closed here; every use holds)
- (LEX-Λ) says, for any p, q with Λ_s(p) = Λ_s′(q) = w: «K0 and K3 lie on both plays or on neither, since a play passes K0 iff it passes
  K3 iff its cycle node is in the closed core ((Core)), and both nodes are w. So if the e-parts differ, z is the most relevant e-vertex of
  E_s(p) Δ E_s′(q)».
- Over ALL vertices this is false. It is the same sentence that P-N5-CHAIN's fixes entry 3 records as false («(Core)'s «a play passes K0
  iff it passes K3» (plays from pA or K3 pass K3, not K0)»). (Core)'s own words are «a play passes K0 iff it passes K3, iff it enters the
  core through some pb_g», not «iff its cycle node is in the closed core».
  - Witness: p = K3 (play K3 → K2 → r → K1 → s → K1, node K1, Π = {K3}), q = any non-core vertex with node K1 and an e-letter in Π
    (its play passes pb → K0 → pA → K3, so Π(q) ⊇ {K0, K3}). Then z = K0, not an e-vertex.
- What holds, and what SPLIT uses:
  - The core's eight vertices {K0, pA, K3, K1, s, r, K2, q} have constant plays (frozen core, σ̄(K2) = r by LOC-K2-3), all with node K1
    and E = ∅. For non-core p, q the only way into the core is pb_g → K0, so K0, K3 ∈ Π (node K1) or neither, and the sentence holds.
  - The conclusion «the larger value has the lex-larger e-set» holds for ALL pairs: a mismatch in K0 / K3 needs a core start with E = ∅
    and Π ⊆ {K3}. If the other e-set is non-empty, that other play is non-core or K0 / q, so it contains K0, and z = K0 is even and on the
    side with the lex-larger e-set.
  - Every application of (LEX-Λ) in SPLIT is to pads: §3 (c) (a, b: successors of a mover or a gate), RW-SHAPE (ii) (a and b at t′ − 1,
    b at t′), ASC-WIT (c) (pe_g1, pβ_g1). Pads of movers and gates are non-core. So every use holds as written.
- Status: a defect in the proof text (one sentence), not in any statement. It closes as P-N5-CHAIN's W-1 closed: by restricting the
  sentence to non-core vertices. The line must not restate (LEX-Λ) over all vertices (R-1, box 5).

## Re-derivation, §1-§2 (every step redone by hand)
- §1 Λ-intervals. Λ_t(v) moves only to strictly larger reward (CYC: F1, F2), so a value never returns, and there are at most 2M + 3
  intervals. Correct.
- Changes and tops. E-MON3 makes each change a strict lex increase. So the most relevant element of the symmetric difference lies in the
  later set: a top ENTERS. Correct. (E-MON3 is signed for non-core vertices with its repaired reason. Core vertices are constant, so
  E-MON3 holds for every vertex.)
- (PL). Positional strategies make the play from u the suffix of v's play from u, with the same cycle, so Λ_s(u) = Λ_s(v). Every element
  of Π_s(v) is more relevant than the node, so it lies on the prefix (cycle vertices other than the node are less relevant). Hence
  E_s(v) = A ⊔ E_s(u), with A the e-letters of Π_s(v) strictly before u. If u is on the cycle, E_s(u) = ∅ and A = E_s(v).
  - Reading N-1: «the e-letters strictly before u on P_s(v)» means those of Π_s(v). An e-letter less relevant than w cannot sit on the
    prefix anyway (by B-ONLY3, for every v that has a non-empty E). Correct.
- Lemma SPLIT.
  - The plays differ: equal plays give equal Π. Both start at v. Let u be the first vertex of P_t(v) whose successor differs. u lies on
    both plays, and the plays agree up to u.
  - (i) Non-mover Even vertices (β, e, c_W, c_X, K0, K1, K3 and all pads) have one successor in HOW3 (F6). The Odd vertices are the gates
    and K2 ([DEF]; pads are Even, [G3]). σ̄(K2) = r at every state (LOC-K2-3). So u is a mover whose σ changed or a gate whose σ̄ changed.
    Correct.
  - (ii) F5 at the step t − 1 → t. Correct.
  - (iii) LOC-GATE3 with NO-TIE3: σ̄ picks the strictly smaller face. So Ω_(t−1)(old) ◁ Ω_(t−1)(new) and Ω_t(new) ◁ Ω_t(old). With F1 at
    new, the chain follows. Correct.
  - (iv) t − 1, t ∈ I, so Λ_(t−1)(v) = Λ_t(v) = w, and (PL) gives Λ_s(u) = w. The prefixes before u are equal, so A_(t−1) = A_t, and the
    symmetric differences of v and u are equal: the same top. Correct.
- DATA (my engine, box 4): entfail, playfail, prefail, kindfail, hwfail, gtfail, trfail are 0 on 66,335 changes of the 28 pinned runs.
