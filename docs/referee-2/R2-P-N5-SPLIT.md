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

## Re-derivation, §3-§4 (box 2)
- Lemma REWIN, set-up. At t2 the split is u, and b = nx_t2(u) is its new successor, so a := nx_(t2−1)(u) ≠ b. If t2 = t1 + 1 then
  nx_(t2−1)(u) = nx_t1(u) = b, which is impossible. So t1 < t2 − 1.
- (a), u a mover. σ_t1(u) = b ≠ a = σ_(t2−1)(u), so a first s ∈ (t1, t2 − 1] with σ_s(u) ≠ σ_(s−1)(u) = b exists. u is never a cycle node
  (F6), so F3 gives Ω_r(u) = ext(u, Ω_r(σ_r(u))) at every r. The chain:
  - Ω_(t2−1)(u) ⊵ Ω_s(u) (F1);
  - Ω_s(u) ▷ Ω_(s−1)(u) (STRICT);
  - Ω_(s−1)(u) = ext(u, Ω_(s−1)(b)) ⊵ ext(u, Ω_t1(b)) (F1 at b, s − 1 ≥ t1; F4′ with u in no Π, CN2-3).
  So ext(u, Ω_(t2−1)(a)) ▷ ext(u, Ω_t1(b)). If Ω_(t2−1)(a) ⊴ Ω_t1(b), F4′ would give ext ⊴ ext. ⊴ is total, so Ω_(t2−1)(a) ▷ Ω_t1(b).
  Correct.
- (a), u a gate. u's two successors are its face pads, so a is the other face. At t1 Odd plays b, so Ω_t1(b) ◁ Ω_t1(a) (LOC-GATE3,
  NO-TIE3). F1 at a gives Ω_(t2−1)(a) ⊵ Ω_t1(a). Correct.
- (b) At t2, u moves from a to b. Mover: F5. Gate: Odd played a at t2 − 1, so a is the strictly smaller face. Then (a). Correct.
- (c)
  - Λ_t1(b) = Λ_(t2−1)(a) = w, by (PL) on v's plays at t1 and t2 − 1 (u lies on both, by §2 at t1 and at t2).
  - y ∈ E_t1(b): y ∈ E_t1(v) ∖ E_(t1−1)(v). The prefix A before u is common to t1 − 1 and t1, so y ∈ E_t1(u) = E_t1(b) (u is not an
    e-vertex). y ∉ E_(t2−1)(a), because y ∉ E_(t2−1)(v) ⊇ E_(t2−1)(a).
  - Suppose no U_y-letter lies in E_t1(b) Δ E_(t2−1)(a). Then y is its most relevant e-letter. b and a are non-core pads with node w,
    so by (LEX-Λ) (W-1: valid here) z = y. y is even and in Π_t1(b), so Ω_t1(b) ▷ Ω_(t2−1)(a), against (a). So the most relevant
    difference z is in U_y, and by (a) it lies in E_(t2−1)(a). Restricted to U_y, the most relevant difference is still z. Correct.
  - The top at t2 is y, so nothing in U_y changes at v: E_(t2−1)(v) ∩ U_y = E_t2(v) ∩ U_y. Both sides split as A′ ⊔ (successor part)
    with the same A′ (§2 (iv) at t2). Cancelling A′ ∩ U_y gives E_(t2−1)(a) ∩ U_y = E_t2(b) ∩ U_y. Correct.
- Corollary REWIN-COUNT.
  - Λ(b) = w at both ends of a re-win. Λ(b) only rises in reward (F1, F2), so it is w on the whole span, inside one Λ-interval J_b.
  - On J_b, E-MON3 makes E(b) lex-nondecreasing. Restriction to U_y keeps that: if the most relevant difference is outside U_y, the
    restrictions are equal. So, with (c), R_ub ≤ Dhi_y(b, J_b) − 1.
  - Each of the c_y − 1 consecutive couples is either one of the W couples with different pairs or a re-win. Correct.
- Lemma PAIR-SPLIT. I re-read §3's proof with (t1, t2) := (t, t′) and with y-tops of y strictly between t and t′ allowed.
  - Each step uses only: nx_t(u) = b ≠ nx_(t′−1)(u) (this gives s in the mover case and the faces in the gate case); y ∈ E_t(b); y ∉
    E_(t′−1)(a); and the top y at t′.
  - None of these needs consecutiveness. A y-top at t″ ∈ (t, t′) through another pair changes nothing used. (a′), (b′), (c′) are
    correct as stated.
  - (b′)'s second half, Ω_(t′−1)(b) ▷ Ω_t(b), is (b)'s chain Ω_(t′−1)(b) ▷ Ω_(t′−1)(a) ▷ Ω_t(b). Correct.
- Corollary SPLIT-COUNT.
  - Each y-top has one split pair (§2). The tops of one pair lie in one J_b (as in REWIN-COUNT). By (c′) their values E(b) ∩ U_y strictly
    increase, so they are pairwise distinct values from J_b: at most Dhi_y(b, J_b) tops per pair.
  - |SPL| ≤ 3M:
    - u is a mover or a gate (§2 (i)). Its successors in Γ3 are pads ([G3]): m_(x,k), one per option (M in all), and pe_g, pβ_g (2M in
      all).
    - Each such pad has a single in-edge, so b determines u.
  - c_y ≤ Σ_pairs Dhi_y(b, J_b) ≤ 3M · max Dhi. Correct.
  - Two pairs with the same b would have the same u, so «Σ over pairs» = «Σ over b». J_b is well defined per pair.
- Lemma RW-SHAPE (and RW-SHAPE*), t < t′ same-pair tops (any).
  - Decomposition.
    - y ∈ Π_s(b) at s = t (shown in (c)) and at s = t′ (the same argument at t′).
    - y is an e-vertex with one successor, frozen. m = wt(y) is a mover: m ≠ c_W, else the node would be c_W, above y.
    - By (PL) on b's play, E_s(b) = (letters before y) ⊔ {y} ⊔ E_s(m). Intersect with U_y (y ∉ U_y). Correct.
  - (i) Λ(m) = w at t and at t′ (m is on v's play), so Λ(m) = w on [t, t′] (F1, F2), and S is lex-nondecreasing there (E-MON3,
    restricted). If S_t = S_t′, (c′) says B_t′ ⊔ S >lex B_t ⊔ S. The most relevant difference lies in B_t′ Δ B_t, on the larger side,
    so B_t′ ≠ ∅. Correct.
  - (ii) Sandwich. The three values all have node w:
    - Ω_(t′−1)(a) ◁ Ω_(t′−1)(b) ((b′));
    - Ω_(t′−1)(b) ⊴ Ω_t′(b) (F1);
    - Λ_(t′−1)(b) = w, because t ≤ t′ − 1 ≤ t′.
    For non-core values with one node, (LEX-Λ) makes «value ↦ E ∩ U_y» weakly monotone. The two ends agree on U_y ((c)'s last step at t′).
    So the middle agrees too: E_(t′−1)(b) ∩ U_y = E_t′(b) ∩ U_y.
  - Take f ∈ B_t′. Then f ∈ E_(t′−1)(a) ∩ E_(t′−1)(b).
    - The plays from a and from b at t′ − 1 both pass f and coincide from f on.
    - y is an e-vertex more relevant than w. So if y were on the play from a it would be in Π, and it is not (y ∉ E_(t′−1)(a)). So the
      common suffix from f avoids y.
  - At t′, y follows f on b's play. So the plays from f at t′ − 1 and at t′ differ. f has one successor, so the first departure is
    strictly after f, and it comes before y. That departure is a mover or gate whose choice changed (§2 (i)). Correct.
- Corollary RW-1. b's play at t′ is the part of v's play after u. v's play is simple up to y, so u does not recur before y, and the
  departure from (ii) is a second vertex before y on v's play whose successor changes. A single-split t′-step therefore forces
  S_t ≠ S_t′. Correct.
- DATA (my engine, box 4): every same-pair couple (47,758 on the 28 pinned runs; 7,880 of them re-wins) has abfail, psa, psb, psc 0
  (rw_psa, rw_psb, rw_psc 0 on the re-wins). lamb, lamm, spfail (with Dhi over ALL of J_b), spl3M, rcfail, decfail, rws1, rws2, rw1fail
  are 0. Seq (couples with S_t = S_t′) is 31, all on RWX_n95, all multi-split. That is exactly where (i) and (ii) are not vacuous, and
  there rws1 = rws2 = 0.

## Re-derivation, §5-§7 (box 3)
- Lemma PAIR-HIGH (abstract: one lex-increasing sequence of sets; strict at each change, by E-MON3).
  - (c) At a change with top z, z enters and nothing more relevant than z changes. If z ∈ U_y, the restriction to U_y changes, and it
    rises (z enters). If z ∉ U_y, every letter of U_y is above z, so the restriction is unchanged. The restricted values strictly increase,
    so Dhi_y = 1 + Σ_(z∈U_y) c_z. Correct.
  - (a) Between consecutive y-tops, y leaves at some change. Its top z enters while y leaves, so z ≠ y and z is above y: z ∈ U_y. A y-top
    leaves U_y unchanged. So the restriction takes a new value strictly between consecutive y-tops, and values never return: c_y ≤ Dhi_y.
    Correct.
  - (b) An x/y alternation of length L has at least ⌊L/2⌋ y's, so ⌊L/2⌋ ≤ Dhi_y, and L ≤ 2·Dhi_y + 1. Correct.
- Lemma RA-PATHS.
  - Each gap between consecutive y-tops holds a top in U_y (as in (a)). The most relevant top of the gap is z ∈ RA(y) ⊆ U_y, so RA is a
    DAG pointing up.
  - Each gap contributes one top of its z, and the gaps are disjoint. So c_y − 1 ≤ Σ_(z∈RA(y)) c_z.
  - Induction from the most relevant letter down gives c_y ≤ P(y). Correct (also for c_y = 0).
- Lemma RE-COUNT. E-MON3 makes the sets of I pairwise distinct, so D_I = 1 + #changes. A change that is not a re-entry has a top in no
  E_s(v), s ∈ I, s ≤ t − 1. At t − 1 that holds because the top enters. So it is the top's first entry into ⋃_I E. At most Mact_I(v) such
  changes. Correct.
- Theorem RE-EQUIV.
  - Classes in different Λ-intervals differ in Λ, and each node gives one interval (F1, F2). So D^tot_E(v) = Σ_I D_I(v)
    ≤ (2M + 3)(1 + M) + Σ_I Rtop_I(v) (Mact ≤ M; CYC).
  - T-QUIET3 then gives the bound as stated:
    1 + Σ_v (D^tot_E(v) − 1) ≤ 1 + n3·((2M + 3)(M + 1) − 1) + Rtop.
  - Rtop ≤ n3·T3, because each vertex has at most one change per step. L3 and n3 are polynomial in N + M, so «T3 polynomial ⇔ Rtop
    polynomial». Correct.
- Lemma PAIR-COUNT (corrected).
  - Index i < |τ| goes to the pair {τ_i, τ_(i+1)}; the two letters differ.
  - For the pair {x, y}, the indices assigned to it are distinct letter changes of τ restricted to {x, y}. These are distinct switches of
    ρ (runs collapsed), so there are at most |ρ| − 1 ≤ A_xy − 1 of them, and none if only one letter occurs.
  - Summing: |τ| − 1 ≤ Σ max(0, A_xy − 1). The second inequality is trivial, and m ≤ 1 gives |τ| ≤ 1. Correct.
  - The correction (max(0, ·), A ≥ 1) answers the A = 0 case.
- Theorem ALT-EQUIV (corrected).
  - tops(v, I) has no equal neighbours: a y-top makes y enter, and a second y-top needs y to leave first, at a change whose top is not y.
  - D_I = 1 + |tops| ≤ 2 + C(M, 2)·(A − 1). Then sum over the ≤ 2M + 3 intervals and apply T-QUIET3: the bound is exactly as stated.
  - A ≤ max(1, T3), since an alternation has at most |tops(v, I)| ≤ T3 letters. Correct.
- Corollary C-EQUIV. |tops| = Σ_y c_y ≤ Mact·C ≤ M·C. Then as in RE-EQUIV, and C ≤ max(1, T3). Correct.
- Lemma ASC-WIT (under [E-LEV]).
  - SPLIT's form «f more relevant than f′ ⇒ lev(f) ≥ lev(f′)» is the contrapositive of [E-LEV] for e-vertices. Relevance on e-vertices
    is priority order, and e-priorities are distinct.
  - Set-up. By CHAIN-DECOMP3, y = succ(c_i) is a mover, and by [DEF] its level is lev(c_i) − 1. The play runs c_i → y → m → g1, with g1
    the gate of σ_t(y).
  - (a) If σ̄_t(g1) = pe, the play reaches e_(g1). e_(g1) is above w (B-ONLY3; v is no exception, since it has an ascent), so it is in
    Π. No e-vertex lies between c_i and it, so it is c_(i+1). But lev(e_(g1)) = lev(c_i) − 1, so by [E-LEV] it is less relevant than c_i:
    no ascent. Correct.
  - (b) LOC-GATE3 with NO-TIE3. Correct.
  - (c) pβ_(g1) is on v's play after c_1, …, c_i, so E_t(pβ) = {c_(i+1), …, c_p} and Λ = w ((PL)). If Λ(pe) = w, (LEX-Λ) (pads: W-1
    valid) and (b) put the most relevant difference on pe's side. If c_(i+1) ∉ E(pe), that difference is at least as relevant as
    c_(i+1). Correct.
  - (d) Different nodes are decided by reward, and rewards are distinct (F2). Correct.
- Lemma ASC-ROOT. Strong induction on ℓ = lev(c_i).
  - Case (d): g* = g1, with lev(g1) = ℓ − 1.
  - Otherwise Λ(pe_(g1)) = w.
    - lev(g1) = 0 would give pe → e_(g1) → c_W, node c_W ≠ w. (w is below the e's, since E_t(v) ≠ ∅ and only K0, K3 are above c_W.)
      So lev(g1) ≥ 1.
    - seq_t(pe_(g1)) starts with e_(g1). By (c) it holds a letter at least as relevant as c_(i+1). c_(i+1) is above c_i, and c_i is above
      e_(g1) ([E-LEV], the levels differ). So that letter is above e_(g1): an ascent.
    - Up to its first ascent the sequence descends, so the ascent starts at level ≤ ℓ − 1 ([E-LEV]). The induction gives g* with
      lev(g*) < ℓ − 1, the face conditions, and a reward above Λ(pe_(g1)) = w = Λ_t(v).
  - Base ℓ = 0 is vacuous: a level-0 c_i points to c_W. Correct.
- N-2 (premise lists, optional): the «To sign» row for §7 omits (LEX-Λ)'s own premises ((E-DOM), (Core), [DEF]) and [DEF]'s level
  structure. The row for §2 omits [DEF] (Odd vertices). Both are used and both are P-N5-CHAIN premises, so nothing outside the stated
  premise set enters.
- DATA (my engine, box 4): ph_a, ph_b, ph_c, rafail, rpfail, rptfail, recfail, dmon, pcfail, bdfail are 0 on the 28 pinned runs (every
  (v, I), every pair of letters, every gap). ASC-WIT (awa, awb, awc, awd, awmv) and ASC-ROOT (rootfail, a witness gate searched over ALL
  gates) are 0 on 113,238 ascents. The pinned instances satisfy [E-LEV]: my builder orders e-priorities by (lev, gate).
