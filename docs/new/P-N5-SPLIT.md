# Packet P-N5-SPLIT (boxes 197-199): on the Howard run HOW3(G) of N5′-xi from S3 on Γ3(G), every change of a vertex's e-set is a change at a split vertex, and the number of times a letter y is top at v is at most the sum, over the split pairs (u, b), of the number of high parts above y of b; T3 is polynomial iff C := max c_y is
L-NEW successor 67 (Opus 5.5), D1 / D14 / D18. Lead brief 2026-11-08 (successor 67 start; «go» 23:22Z): «FREEZE PACKET P-N5-SPLIT …
premises named exactly (P-N5-CHAIN facts by name, conditional on R125; no other R-id unless quoted by script); DROP C-WT and REWIN-ASC;
a DEAD list with instances …; DATA with counters …; a TARGET.md scope paragraph …; the attack record». FROZEN at push. Later text goes to
docs/new/P-N5-SPLIT-fixes.md, append-only. Sources, history only: docs/new/N5-SPLIT-box199.md (box 199 + Addenda 1-5, successor 66),
docs/new/N5-PAIR-box198.md (box 198), docs/new/N5-CORE-box197.md (box 197 + Addenda 1-3, successor 65). Every proof is carried here in
full; nothing is cited from those files.
Labels: PROVED (L-NEW 65 / 66, unrefereed; each survived the L-RED attacks listed in §9) / DEAD / DATA / READING (not to sign).
This packet is NOT a TARGET.md claim, NOT M3 and NOT M4. It does not decide G-N5-TIME. It is a REDUCTION / EQUIVALENCE (§10).

## Scope (explicit)
- Games: Γ3(G) for a genome G, exactly as in P-N5-CHAIN (every genome; Ξ-cycles and Ξ self-loops allowed). Run: HOW3(G), the Howard run
  on Γ3(G) of P-N5-CHAIN §2, states 0, …, T3. By P-N5-CHAIN's Theorem REACH3-ALL this is the mover part of N5′-xi from S3 on Γ3(G) until
  its first fallback; nothing here is about N5 (SPEC S4a) or about other games.
- What it implies: (i) a game lemma that an abstract lex-increasing set sequence lacks: every change of E(v) is a change of the same symmetric difference at one vertex u, a mover
  making a strict Howard switch or a gate whose face order flipped (SPLIT, TRANSFER); (ii) at any two y-tops of v through the same split
  pair (u, b), the high part E(b) ∩ U_y strictly rises (REWIN, REWIN-HI, PAIR-SPLIT); hence (iii) SPLIT-COUNT: c_y(v, I) ≤ Σ_(u,b)
  Dhi_y(b, J_b) ≤ 3M · max_b Dhi_y(b, J_b); (iv) exact reductions of «T3 polynomial» to one-letter or two-letter quantities (RE-EQUIV,
  ALT-EQUIV, C-EQUIV), and the abstract recursions PAIR-HIGH, RA-PATHS.
- What it does NOT imply: any polynomial bound. The open core after this packet is max over y, b, J of Dhi_y(b, J) (§10). Nothing for N5,
  nothing outside Γ3(G), nothing about general parity games, nothing about N5′-xi's iteration count beyond T3 (the conversion is
  P-N5-CHAIN §8's, through P-N5-END, and is not used here).

## To sign
| § | statement | label | premises |
| --- | --- | --- | --- |
| §2 | Lemma SPLIT (i)-(iv), incl. TRANSFER | PROVED | P-N5-CHAIN [OPT], F3, F5, F6, F1, LOC-GATE3, LOC-K2-3, NO-TIE3, [G3] |
| §3 | Lemma REWIN (a)(b), Lemma REWIN-HI (c); Corollary REWIN-COUNT | PROVED | §2 plus F1, F3, F4′, F5, F6, STRICT, CN2-3, (E-DOM), (Core), F2, E-MON3 |
| §4 | Lemma PAIR-SPLIT (a′)(b′)(c′); Corollary SPLIT-COUNT (SPL ≤ 3M) | PROVED | as §3 |
| §4 | Lemma RW-SHAPE, RW-SHAPE*; Corollary RW-1 | PROVED | as §3, plus E-MON3 |
| §5 | Lemma PAIR-HIGH (a)(b)(c); Lemma RA-PATHS | PROVED | E-MON3 only (abstract: any lex-increasing set sequence) |
| §6 | Lemma RE-COUNT; Theorem RE-EQUIV; Lemma PAIR-COUNT (corrected); Theorem ALT-EQUIV (corrected); Corollary C-EQUIV | PROVED | E-MON3, F1, F2, CYC, T-QUIET3 (PAIR-COUNT: none) |
| §7 | Lemmas ASC-WIT, ASC-ROOT (optional) | PROVED | HYPOTHESIS [E-LEV]; B-ONLY3, LOC-GATE3, NO-TIE3, CHAIN-DECOMP3, F2 |
| §8 | DEAD list (seven items, with instances) | DEAD | instances frozen, §8 |
| §9-§11 | DATA, attack record, machine checks, TARGET diff | DATA / READING (not to sign) | |
Every row is conditional on P-N5-CHAIN (lane packet, frozen at l-new 93531b03, sha1 6e613ba762b6ecf67247ef6d8674b4c960013039, fixes
entries 1-3, line L-4 sha1 a69c8aa96fb0b67c6c0a3f6d11670a0b57ba9331; both referees MATCH L-4; landing as R125, pending) and on that
packet's standing premises, quoted there by script. Nothing else is a premise: no other packet, no landed R-id, no L-RED or L-SI lemma.
DROPPED from the sources (no standing here): Corollary C-WT and Corollary REWIN-ASC (both implications from the DEAD CONJECTURES of §8),
CONJECTURES RW-WT, RW-WT*, RW-B0, RW-B0*, DS-TOPS, RA-LOG, ALT-POLY (the last is a restatement of the open core), Corollary DS-POLY.

## 1. Premises and notation
- From P-N5-CHAIN, by name (its §2, §4-§7): HOW3(G), T3, n3 = N + 7M + 10, Ω_t (the [VJ] value against σ̄_t), [OPT], [G3], [DEF], (R),
  (P), (E-DOM), (Core); Facts F1, F2, F3, F4′, F5, F6, DOM, STRICT, CYC (§4); Lemmas CN2-3, LOC-GATE3, LOC-K2-3, B-ONLY3, Corollary
  NO-TIE3 (§5); Corollary T-QUIET3 and L3 (§6); Lemmas E-MON3, CHAIN-DECOMP3 (§7); HYPOTHESIS [E-LEV] (§1), used only in §7 here.
- seq_t(v), E_t(v) (the e-vertices of Π_t(v), in play order resp. as a set), lexicographic order on sets of e-vertices (by the most relevant
  differing element): as in P-N5-CHAIN §7.
- A Λ-interval I of v: a maximal interval of states on which Λ_t(v) = w is constant. By F1 and F2, Λ_t(v) changes only to a vertex of
  strictly larger reward, so the Λ-intervals of v have distinct cycle nodes, and by CYC there are at most 2M + 3.
- Inside I a change is a step t − 1 → t with E_(t−1)(v) ≠ E_t(v). Its top is the most relevant element of E_(t−1)(v) Δ E_t(v). By
  E-MON3 the change is a strict lex increase, so the top lies in E_t(v) \ E_(t−1)(v): a top ENTERS. tops(v, I) := the sequence of tops.
- For an e-vertex y: U_y := the e-vertices more relevant than y. c_y(v, I) := the number of changes in I with top y (y-tops).
  Dhi_y(v, I) := the number of distinct values of E_t(v) ∩ U_y, t ∈ I. C := max over v, I, y of c_y(v, I). Mact_I(v) := |⋃_(t∈I) E_t(v)|.
- P_s(v): the play from v under (σ_s, σ̄_s): a simple path followed by one cycle ([OPT], positional strategies); Ω_s(v) is read off it (F3).
  nx_s(u) := σ_s(u) for Even u, σ̄_s(u) for Odd u.
- Facts used repeatedly:
  - (PL) If u lies on P_s(v) then P_s(u) is the suffix of P_s(v) from u, closed by the same cycle; so Λ_s(u) = Λ_s(v), and E_s(v) is the
    disjoint union of the e-letters strictly before u on P_s(v) and E_s(u). (Positional strategies; every e-letter of Π is more relevant than
    Λ and so lies on the prefix, since cycle vertices other than Λ are less relevant than Λ.)
  - (LEX-Λ) If Λ_s(p) = Λ_s′(q) = w, then Ω_s(p) and Ω_s′(q) are compared by [VJ] through z, the most relevant vertex of Π_s(p) Δ Π_s′(q):
    z is in the larger one if z is even, in the smaller one if odd. Vertices more relevant than an e-vertex are e-vertices, c_W, K0, K3
    (E-DOM); c_W is in no Π (its loop is its own cycle, of top priority); K0 and K3 lie on both plays or on neither, since a play passes
    K0 iff it passes K3 iff its cycle node is in the closed core ((Core)), and both nodes are w. So if the e-parts differ, z is the most
    relevant e-vertex of E_s(p) Δ E_s′(q), it is even (e-priorities are even, [DEF]), and the larger value has z in its e-set: the larger
    value has the lex-larger e-set. In particular the comparison restricted to U_y is lexicographic whenever the two e-sets differ in U_y.

## 2. Lemma SPLIT (PROVED, lane)
Let t − 1, t ∈ I with E_(t−1)(v) ≠ E_t(v). The plays P_(t−1)(v), P_t(v) differ; let u be the first vertex of P_t(v) at which they leave
by different edges (u is on both; old := nx_(t−1)(u), new := nx_t(u)). Then:
- (i) u is a mover with σ_(t−1)(u) ≠ σ_t(u), or a gate with σ̄_(t−1)(u) ≠ σ̄_t(u).
- (ii) Mover: Ω_(t−1)(new) ▷ Ω_(t−1)(old).
- (iii) Gate: Ω_(t−1)(old) ◁ Ω_(t−1)(new) and Ω_t(new) ◁ Ω_t(old), so Ω_t(old) ▷ Ω_t(new) ⊵ Ω_(t−1)(new) ▷ Ω_(t−1)(old): the abandoned
  face rose strictly.
- (iv) TRANSFER: Λ_(t−1)(u) = Λ_t(u) = w, and E_(t−1)(v) Δ E_t(v) = E_(t−1)(u) Δ E_t(u). The change at v is a change of u's e-set inside a
  Λ-interval of u, with the same symmetric difference and the same top.
Proof.
- (i) Non-mover Even vertices and pads have one successor in HOW3 (F6, [G3]). The only Odd vertices are the gates and K2, and σ̄_s(K2) = r
  at every state (LOC-K2-3). So the vertex where the plays first leave by different edges is a mover or a gate whose choice changed.
- (ii) F5: σ_t(u) is ⊴-best under Ω_(t−1) and strictly better than σ_(t−1)(u) when they differ.
- (iii) LOC-GATE3: Odd's chosen face is the ◁-smaller one where the values differ; NO-TIE3: they never tie. At t − 1 Odd chose old, at t
  new. With F1 (Ω_(t−1)(new) ⊴ Ω_t(new)) the chain follows.
- (iv) u is on both plays, so by (PL) Λ_s(u) = Λ_s(v) = w for s = t − 1, t, and E_s(v) = A_s ⊔ E_s(u), A_s the e-letters strictly
  before u on P_s(v). The parts of the two plays before u are equal (u is the first point of departure), so A_(t−1) = A_t. Hence the
  symmetric differences are equal. ∎

## 3. Lemma REWIN, Lemma REWIN-HI (PROVED, lane), Corollary REWIN-COUNT
Let t1 < t2 be two consecutive y-tops of (v, I) with the same split u (§2) and the same new successor b := nx_t1(u) = nx_t2(u). Let
a := nx_(t2−1)(u); a ≠ b, since u moves to b at t2. Then
- (a) Ω_(t2−1)(a) ▷ Ω_t1(b);
- (b) REWIN: Ω_(t2−1)(b) ▷ Ω_(t2−1)(a) ▷ Ω_t1(b): b's value rose strictly on [t1, t2 − 1];
- (c) REWIN-HI: E_t2(b) ∩ U_y >lex E_t1(b) ∩ U_y.
Proof.
- (a), u a mover. σ_t1(u) = b ≠ σ_(t2−1)(u), so there is a first s ∈ (t1, t2 − 1] with σ_s(u) ≠ σ_(s−1)(u) = b. By F3 and F6,
  Ω_r(u) = ext(u, Ω_r(σ_r(u))) at every r. Then Ω_(t2−1)(u) ⊵ Ω_s(u) (F1) ▷ Ω_(s−1)(u) (STRICT) = ext(u, Ω_(s−1)(b)) ⊵ ext(u, Ω_t1(b))
  (F1 and F4′; u is in no Π, CN2-3). So ext(u, Ω_(t2−1)(a)) ▷ ext(u, Ω_t1(b)). Since ⊴ is total and F4′ gives X ⊴ Y ⇒ ext X ⊴ ext Y,
  Ω_(t2−1)(a) ▷ Ω_t1(b).
- (a), u a gate. Its successors are its two face pads, so a is the face other than b. At t1 Odd plays b: Ω_t1(b) ◁ Ω_t1(a) (LOC-GATE3,
  NO-TIE3). By F1, Ω_(t2−1)(a) ⊵ Ω_t1(a).
- (b) At t2, u moves from a to b. Mover: Ω_(t2−1)(b) ▷ Ω_(t2−1)(a) (F5). Gate: Odd played a at t2 − 1, so Ω_(t2−1)(a) ◁ Ω_(t2−1)(b)
  (LOC-GATE3, NO-TIE3). Then (a).
- (c)
  - Λ_t1(b) = Λ_(t2−1)(a) = w: b is on P_t1(v) after u and a is on P_(t2−1)(v) after u ((PL); §2 (iv) gives Λ(u) = w).
  - y ∈ E_t1(b): y enters E(v) at t1 and the part of v's play before u is common to t1 − 1 and t1 (§2 (iv)), so y lies after u, i.e. in
    E_t1(b) (u is not an e-vertex). y ∉ E_(t2−1)(a): y enters at t2, so y ∉ E_(t2−1)(v) ⊇ E_(t2−1)(a) ((PL)).
  - So y ∈ E_t1(b) Δ E_(t2−1)(a). If no e-letter of U_y were in that difference, then by (LEX-Λ) z = y, y is even and in Π_t1(b), so
    Ω_t1(b) ▷ Ω_(t2−1)(a), against (a). So z ∈ U_y, and by (a) and (LEX-Λ) z ∈ E_(t2−1)(a): E_(t2−1)(a) ∩ U_y >lex E_t1(b) ∩ U_y.
  - At t2 the top of v's change is y, so E_(t2−1)(v) ∩ U_y = E_t2(v) ∩ U_y. By (PL) and §2 (iv) both split as A ⊔ (the successor's part)
    with the same prefix part A (u is not an e-vertex), so E_(t2−1)(a) ∩ U_y = E_t2(b) ∩ U_y. ∎
- Corollary REWIN-COUNT (PROVED). Fix (v, I, y) and a pair (u, b); R_ub := the number of re-wins through (u, b) (consecutive y-tops as
  above). Λ(b) = w at every y-top through (u, b) ((PL)), so by F1 and F2 Λ(b) = w on their whole span, inside one Λ-interval J_b of b. On
  J_b, E(b) ∩ U_y is lex-nondecreasing (E-MON3), and by (c) it rises strictly across each re-win. Hence R_ub ≤ Dhi_y(b, J_b) − 1 and
      c_y(v, I) ≤ 1 + W_y(v, I) + Σ_(u,b) (Dhi_y(b, J_b) − 1),
  W_y(v, I) := the number of consecutive y-top couples with different split pairs. (Superseded by SPLIT-COUNT, §4, which has no W term.)

## 4. Lemma PAIR-SPLIT, Corollary SPLIT-COUNT, Lemma RW-SHAPE(*), Corollary RW-1 (PROVED, lane)
**Lemma PAIR-SPLIT.** Let t < t′ be ANY two y-tops of (v, I) whose splits are the same pair (u, b); a := nx_(t′−1)(u) (a ≠ b). Then
(a′) Ω_(t′−1)(a) ▷ Ω_t(b); (b′) Ω_(t′−1)(b) ▷ Ω_t(b); (c′) E_t′(b) ∩ U_y >lex E_t(b) ∩ U_y.
Proof: §3's proof with (t1, t2) := (t, t′). It uses only: nx_t(u) = b ≠ nx_(t′−1)(u), which gives a first departure s ∈ (t, t′ − 1] (for a
gate, its two faces and Odd's choice at t); y ∈ E_t(b) (y enters at t); y ∉ E_(t′−1)(a) (y enters at t′, so y ∉ E_(t′−1)(v)); and the
top y at t′. No step uses that no y-top lies between t and t′ (checked line by line by L-RED 62, R228-box199 §1). ∎
**Corollary SPLIT-COUNT.** SPL_y(v, I) := the set of split pairs (u, b) of the y-tops of (v, I). Then
    c_y(v, I) ≤ Σ_((u,b) ∈ SPL_y(v,I)) Dhi_y(b, J_b) ≤ 3M · max_((u,b)) Dhi_y(b, J_b),
J_b the Λ-interval of b containing the y-tops through (u, b).
Proof.
- Every y-top has exactly one split pair (§2). For a fixed pair, the y-tops through it lie in one Λ-interval J_b of b (as in REWIN-COUNT:
  Λ(b) = w at each, F1, F2), and by (c′) their values E(b) ∩ U_y are pairwise distinct (strictly lex-increasing in time). So at most
  Dhi_y(b, J_b) y-tops go through (u, b). Sum over the pairs.
- |SPL_y(v, I)| ≤ 3M: u is a mover or a gate (§2 (i)), and b is one of u's edges in Γ3. Mover edges go to the M pads m_(x,k), one per
  option; gate edges go to the 2M face pads pe_g, pβ_g ([G3]). So b determines the pair and there are at most M + 2M pairs. This uses that
  β_g, K0, K1, K3 have a frozen choice in HOW3 (F6, (Core)); off standard states a split at β_g would add M edges. ∎
**Lemma RW-SHAPE (and RW-SHAPE*).** Take same-pair y-tops t < t′ through (u, b) (consecutive for RW-SHAPE, any for RW-SHAPE*); a :=
nx_(t′−1)(u), m := wt(y) (the single successor of the e-vertex y, its W-target mover). Write E_s(b) ∩ U_y = B_s ⊔ S_s, with B_s the
U_y-letters of b's play at s before y and S_s := E_s(m) ∩ U_y (s = t, t′). If S_t = S_t′, then
(i) B_t′ ≠ ∅; (ii) for every f ∈ B_t′ some vertex of P_t′(b) strictly between f and y has nx_(t′−1) ≠ nx_t′ (a second split after f).
Proof.
- The decomposition: y lies on P_s(b) (shown in §3 (c) for s = t; at t′ since y enters E(v) at t′ through the split (u, b)), and m follows
  y on it, so E_s(b) = (letters before y) ⊔ {y} ⊔ E_s(m) by (PL); intersect with U_y.
- Λ(m) = w at t and at t′ ((PL): m is on v's play), so by F1, F2 Λ(m) = w on [t, t′], and by E-MON3 S is lex-nondecreasing there. If
  S_t = S_t′, (c′) gives B_t′ ⊔ S >lex B_t ⊔ S, so the most relevant difference lies in B_t′: (i).
- (ii) Sandwich: Ω_(t′−1)(a) ◁ Ω_(t′−1)(b) (§3 (b), with t′) and Ω_(t′−1)(b) ⊴ Ω_t′(b) (F1); all three have Λ = w ((PL), F1, F2). By
  (LEX-Λ), wherever these e-sets differ in U_y they are ordered lexicographically in the same way. E_(t′−1)(a) ∩ U_y = E_t′(b) ∩ U_y
  (§3 (c), last step). A set lex-sandwiched between two sets that agree on U_y agrees with them on U_y [if it differed from the lower end,
  its most relevant difference d ∈ U_y would be in it; the upper end equals the lower end on U_y, so the middle would exceed the upper end
  at d]. So f ∈ E_(t′−1)(a) ∩ E_(t′−1)(b). The plays from a and from b at t′ − 1 both pass f and coincide from f on (positional), and this
  common suffix avoids y, since y ∉ E_(t′−1)(a). At t′, y lies after f on b's play, so the plays from f at t′ − 1 and at t′ differ; their
  first point of departure is strictly after f and before y (§2 (i)). ∎
- Corollary RW-1. At every y-top couple through (u, b) whose t′-step is single-split (u is the only vertex of v's play before y at t′ whose
  successor changes at t′), S_t ≠ S_t′: the second split of (ii) would lie on b's play, which is part of v's play before y.

## 5. Lemma PAIR-HIGH, Lemma RA-PATHS (PROVED, lane; abstract: E-MON3 only)
For letters x, y of tops(v, I) with y more relevant than x, A_xy := the length of the longest x/y-alternating subsequence of tops(v, I).
**Lemma PAIR-HIGH.** (a) c_y ≤ Dhi_y; (b) A_xy ≤ 2·Dhi_y + 1; (c) Dhi_y = 1 + Σ_(z ∈ U_y) c_z (all on (v, I)).
Proof.
- At a change with top z, z enters and nothing more relevant than z changes (E-MON3: strict lex increase).
- (c) E ∩ U_y changes exactly at the changes whose top lies in U_y, and each such change raises it lexicographically, so its values are
  pairwise distinct: Dhi_y = 1 + #(changes with top in U_y).
- (a) Let t1 < t2 be consecutive y-tops. After t1, y ∈ E; just before t2, y ∉ E. So some change in (t1, t2) removes y; its top z enters,
  y leaves, z is the most relevant element of the symmetric difference, so z ∈ U_y. That change alters E ∩ U_y; a y-top alters nothing in
  U_y. So between consecutive y-tops E ∩ U_y takes a new value, and no value returns (lex monotone): c_y ≤ Dhi_y.
- (b) An x/y alternation of length L contains at least ⌊L/2⌋ y's, all y-tops: ⌊L/2⌋ ≤ c_y ≤ Dhi_y. ∎
**Lemma RA-PATHS.** RA(y) := the letters z that are the most relevant top strictly between two consecutive y-tops of (v, I) (each is in U_y,
by (a)'s proof: RA is a DAG pointing up). P(y) := 1 + Σ_(z ∈ RA(y)) P(z), the number of directed paths from y in RA. Then c_y ≤ P(y).
Proof. Each of the c_y − 1 gaps between consecutive y-tops contains a top of its most relevant letter z ∈ RA(y); the gaps are disjoint, so
c_y − 1 ≤ Σ_(z ∈ RA(y)) c_z. Induction from the most relevant letter down. ∎
- Both lemmas hold for any lex-increasing set sequence; the abstract counter (every subset in binary order) makes them tight with c_y and
  P(y) exponential. They are recorded as the frame in which §3-§4 are the game input.

## 6. Exact reductions (PROVED, lane)
**Lemma RE-COUNT.** D_I(v) := |{E_t(v) : t ∈ I}| ≤ 1 + Mact_I(v) + Rtop_I(v), Rtop_I(v) := the number of changes in I whose top lies in
E_s(v) for some s ∈ I, s < t − 1 (top re-entries).
Proof. By E-MON3 every change is a strict lex increase, so the sets of I are pairwise distinct and D_I(v) = 1 + #changes. A change whose
top is not a re-entry is the first entry of its top into ⋃_(t∈I) E_t(v): at most Mact_I(v) of those. ∎
**Theorem RE-EQUIV.** With Rtop := Σ_v Σ_I Rtop_I(v): T3 ≤ (1 + n3·((2M + 3)(M + 1) − 1) + Rtop)·(L3 + 1), and Rtop ≤ n3·T3. So T3 is
polynomial in N + M iff Rtop is.
Proof. Classes of different Λ-intervals differ in Λ, so D^tot_E(v) = Σ_I D_I(v) ≤ Σ_I (1 + M + Rtop_I(v)) ≤ (2M + 3)(M + 1) +
Σ_I Rtop_I(v) (RE-COUNT, Mact ≤ M, at most 2M + 3 intervals by CYC). Sum D^tot_E(v) − 1 over the n3 vertices and apply T-QUIET3. Each top
re-entry is one change of one vertex at one step. ∎
**Lemma PAIR-COUNT (corrected form).** Let τ be a sequence over m letters with no two equal consecutive letters, and A_xy the longest
x/y-alternating subsequence. Then |τ| ≤ 1 + Σ_(x<y) max(0, A_xy − 1) ≤ 1 + C(m, 2)·max(0, A − 1), A := max A_xy.
Proof. Assign each index i < |τ| to the pair {τ_i, τ_(i+1)}. For a pair {x, y} let ρ be τ restricted to {x, y} with runs collapsed; ρ
alternates, so |ρ| ≤ A_xy, and the indices assigned to {x, y} are distinct switches of ρ: at most |ρ| − 1 of them, and none unless
A_xy ≥ 2. Sum; add the last index. ∎
**Theorem ALT-EQUIV (corrected form).** With A := max(1, max over v, I of the longest two-letter alternation in tops(v, I)):
T3 ≤ (1 + n3·((2M + 3)·(2 + C(M, 2)·(A − 1)) − 1))·(L3 + 1), and A ≤ max(1, T3). T3 is polynomial iff A is.
Proof. tops(v, I) has no equal consecutive letters (a top enters, so it is in E_t; the next change with the same top would need it to have
left in between, which is a change with another top) and at most M letters; PAIR-COUNT; D_I(v) = 1 + |tops(v, I)|; then as in RE-EQUIV.
An alternation has at most |tops(v, I)| ≤ T3 letters (one change of v per step). ∎
**Corollary C-EQUIV.** |tops(v, I)| = Σ_y c_y(v, I) ≤ Mact_I(v)·C ≤ M·C, so T3 ≤ (1 + n3·((2M + 3)(1 + M·C) − 1))·(L3 + 1); and
C ≤ max(1, T3). T3 is polynomial iff C is. Proof: D_I = 1 + |tops|, then as in RE-EQUIV. ∎

## 7. Lemmas ASC-WIT, ASC-ROOT (PROVED, lane; optional rows; under HYPOTHESIS [E-LEV])
lev(e_(x,k)) := lev(x); lev(g) := lev(x) for the gate g = (x, k). Under [E-LEV], f more relevant than f′ implies lev(f) ≥ lev(f′).
**Lemma ASC-WIT.** Let seq_t(v) = (c_1, …, c_p), w := Λ_t(v), c_(i+1) more relevant than c_i, y the successor of c_i, g1 the gate of
σ_t(y). Then (a) σ̄_t(g1) = pβ_(g1); (b) Ω_t(pe_(g1)) ▷ Ω_t(pβ_(g1)); (c) if Λ_t(pe_(g1)) = w, E_t(pe_(g1)) contains an e-vertex at least
as relevant as c_(i+1); (d) if Λ_t(pe_(g1)) ≠ w, its reward is strictly larger than w's.
Proof.
- y is a mover of level lev(c_i) − 1 (CHAIN-DECOMP3); the play runs c_i → y → m → g1.
- (a) If σ̄_t(g1) = pe_(g1), the play goes on to e_(g1), which is more relevant than w (B-ONLY3), so e_(g1) ∈ Π_t(v) and no e-vertex lies
  between c_i and e_(g1): e_(g1) = c_(i+1). But lev(e_(g1)) < lev(c_i), so by [E-LEV] e_(g1) is less relevant than c_i: no ascent.
- (b) LOC-GATE3, NO-TIE3.
- (c) The play from pβ_(g1) is a suffix of v's: Λ_t(pβ_(g1)) = w and E_t(pβ_(g1)) = {c_(i+1), …, c_p}. By (b) and (LEX-Λ), either the
  e-parts are equal (then c_(i+1) ∈ E_t(pe_(g1))) or the most relevant difference z is in E_t(pe_(g1)); if c_(i+1) ∉ E_t(pe_(g1)) then
  c_(i+1) is in the difference and z is at least as relevant.
- (d) [VJ] compares the cycle node's reward first; distinct vertices have distinct rewards (F2); with (b). ∎
**Lemma ASC-ROOT.** If seq_t(v) has an ascent and (c_i, c_(i+1)) is its first one, there is a gate g* with lev(g*) < lev(c_i),
σ̄_t(g*) = pβ_(g*) and Ω_t(pe_(g*)) ▷ Ω_t(pβ_(g*)), whose W-face's cycle node has strictly larger reward than Λ_t(v).
Proof. Induction on ℓ := lev(c_i). ASC-WIT at (v, i); if (d), g* := g1. Else Λ_t(pe_(g1)) = w. If lev(g1) = 0, e_(g1)'s successor is c_W,
so Λ_t(pe_(g1)) = c_W ≠ w (E_t(v) ≠ ∅, and only K0, K3 lie above c_W); so lev(g1) ≥ 1, and seq_t(pe_(g1)) starts with e_(g1) (level
ℓ − 1) and by (c) contains an e-vertex more relevant than e_(g1): it has an ascent, whose first one starts at level ≤ ℓ − 1 ([E-LEV]: up to
it the sequence descends). Induction (base ℓ = 0 vacuous: a level-0 c_i has successor c_W). ∎
- Static (any σ against an optimal σ̄); not a bound. Recorded because any embedding of the abstract counter must supply these witnesses.

## 8. DEAD list (each with the instance that kills it; instances frozen in experiments/new/box199/inst, sha1 in SHA1SUMS and in split.pins)
| # | claim | obstruction | instance (sha1, first 8) | counter (unit) |
| --- | --- | --- | --- | --- |
| D1 | downward charge: «each re-win of y at u is paid by a class change of a vertex on the y-route below y» | on 192 of 219 re-wins no vertex of the y-route changes Λ or a letter less relevant than y; first: v = x0, y = e(10,0), t1 4, t2 6, u = x0, b = m_(0,0). REWIN-HI places the forced change ABOVE y | CX4_n21 (ef29debb) | dn_nobelow_all 192 (re-win) |
| D2 | W-target charge for all re-entries (E(wt(y)) ∩ U_y changes between any two consecutive y-tops) | y expelled by a PREFIX letter e(10,0) and re-entering under it by another split; E(wt(y)) constant; first: v = x10, y = e(15,1), wt(y) = x0, t 4 → 6 | GROW7_n34 (42bbd562) | wcfail 18 (re-entry) |
| D3 | W-target bound c_y(v) ≤ #values of E(wt(y)) ∩ U_y on the span | same mechanism | HOLD2K_n84 (423a4a88) | wbfail 18 ((v, I, y)) |
| D4 | ROUTE-LOW: no U_y-letter on v's new play between u and y at a y-top | two splits in one Howard step: gate (10,0) re-routes, re-merging before e(13,0); x2's switch after e(13,0) brings y; v = x0, t 2, y = e(11,0) | ROUTELOW_n21 (80f9b977) | ytopB_ne 65 (y-top) |
| D5 | product-chain (Dilworth / Greene–Kleitman) idea: Pre := the U_y-letters before y on v's play lex-monotone at y-tops, so c_y additive | Pre not monotone; and where it holds #Pre + #Suf − 1 ≤ Dhi_y(v), no gain over PAIR-HIGH | GROW7_n34 (42bbd562); also GROW8_n53, HOLD3K_n125, DU21_h4 | premono_no 18 ((v, I, y)) |
| D6 | CONJECTURES RW-WT, RW-WT*, RW-B0, RW-B0* (the change above y forced by REWIN-HI / PAIR-SPLIT sits at wt(y); b's route to y carries no U_y-letter) | the forced rise sits on b's route BEFORE y: E(wt(y)) ∩ U_y = ∅ at both same-pair y-tops while E(b) ∩ U_y goes ∅ → {647}, 647 before y (L-RED ids: v = u = 17, b = 240, y = 764, wt(y) = 20, t 3, t′ 6); all 31 failures at multi-split re-wins (RW-1 consistent). Hence C-WT and REWIN-ASC (dropped) have no premise | RWX_n95 (da8b3a30), L-RED 62 | rwfail 31, Bne_t2 31, rw2fail 31, spwfail 31 (re-win / couple / (v, I, y)) |
| D7 | fan-in 1 of RA (one «High» per letter), and RA-LOG / bounded multiplicity as game properties | fan-in 3 (NK6_cl21), 4 (DSALT9_n416); RA depth linear on L-SI's FW, multiplicity m(y, z) = n on MW (L-SI 47 box 90) | NK6_cl21 (408b9988); FW16_2 (94df42b7); MW32_2 (445031d1) | pair198 fan-in; L-SI's census (cited as DATA of another lane, not re-proved) |
- Also recorded (not a claim of this packet): the earlier hope that random and climbed data decide RW-B0: about 346,700 re-wins over four
  sources had 0 fails before L-RED 62's climb found RWX_n95. Large zero counts are DATA, not evidence of a lemma.

## 9. DATA and attack record (not to sign)
### 9.1 DATA (tool experiments/new/box199/split199.py on P-N5-CHAIN's engine: box 189 gamma3.build, box 190 n5v.step mode xi from S3, up
### to the first fallback; record box199/split199.out, 28 frozen instances)
- Units: change at (v, I) (playfail, kindfail, hwfail, gtfail, trfail: SPLIT); re-win (dnfail: REWIN; rhfail: REWIN-HI; rw1fail: RW-1);
  same-pair couple, all pairs t < t′ (rh2fail: PAIR-SPLIT); (v, I, y) (spfail: SPLIT-COUNT's first inequality with Dhi_y(b, J_b)
  replaced by the number of distinct values of E(b) ∩ U_y at the pair's own y-tops, a lower bound for Dhi_y(b, J_b), so spfail 0 is the
  stronger statement); re-entry (wlamfail: Λ(wt(y)) = w at both y-tops). Totals per instance. Scope: [E-LEV] holds on every instance (gamma3.py builds
  e-priorities by (lev, gate)); every lemma above is for every genome.
- Every PROVED-lemma counter is 0 on all 28 instances (split199.out, one line each): playfail, kindfail, hwfail, gtfail, trfail, dnfail,
  rhfail, rh2fail, spfail, rw1fail, wlamfail. DEAD witnesses: as §8 (wcfail 18 GROW7_n34, wbfail 18 HOLD2K_n84, ytopB_ne on ROUTELOW_n21,
  rwfail 31 RWX_n95).
- Controls (CX4_n21, check199.out): ctrl1 (Howard direction reversed) hwfail 444; ctrl2 (W-target bound with one value) wbfail 200; ctrl3
  (strict rise on [t1, t1]) dnfail 219; ctrl4 (U_y := ∅) rhfail 219, rh2fail 313, spfail 161, rw1fail 127; ctrl5 (gate test negated)
  gtfail 284; ctrl6 (Bne counted always) Bne_t1 219, Bne_t2 219. Each PROVED-lemma counter has a firing control except playfail, kindfail,
  trfail and wlamfail, which test definitions (READING: L-RED 61 / 62 reproduced them with their own code, §9.2).
- Maxima (per (v, I, y), per instance; split199.out descriptive fields after «|»): max c_y ≤ 6 outside MW (C6G8_n54 6), MW 2n + 1 (65 on MW32_2); max split
  pairs ≤ 5 (FW6_4, FW8_4: k + 1), W ≤ 4. Tightness: MW (one split pair, Dhi_y(b) = c_y) and FW (c_y = #split pairs = k + 1, Dhi 1) make
  SPLIT-COUNT tight; the high parts at b on MW and the split pairs on FW grow linearly, with T3 linear.
- Box 198 / 197 tools (records, not re-run for this packet): box198/pair198.py (ph1fail, ph2fail, rafail, rpfail; output pair198.out,
  check198.out with ctrl1 / ctrl2 firing); box197/asc197.py (awA, awB, rootfail, dfail, lexdec; output sweep197_fix.out, check197.out with
  four controls firing). All lemma counters 0 there.
- Random search srch199.py seed 8 (log srch199_s8.log): 315,065 re-wins, every PROVED counter 0 (it measured the dead RW-B0 too, 0 there).
- Limits: every run is short (T3 ≤ 199, MW32_2); nothing here tests a polynomial bound.
### 9.2 Attack record (L-RED, cited; not re-run here except where said)
- L-RED 61, R227-box198 (claude/l-red 1c802d82): PAIR-HIGH, RA-PATHS, C-EQUIV SURVIVE.
- L-RED 61, R227-box199 (claude/l-red 1ea37d91, c482e0d8): SPLIT, REWIN, REWIN-HI, RW-SHAPE, RW-1 SURVIVE; own engine (own.py, Γ without
  pads); DEAD claims D1-D3 reproduced.
- L-RED 62, R228-box199 (claude/l-red 0eb43a7a §1-§3, 68639e7a Addendum A, 6540fbb6 Addendum B, 4b309716 Addendum C): PAIR-SPLIT,
  SPLIT-COUNT, RW-SHAPE* SURVIVE («consecutive» unused, line by line; 3M = edges out of movers and gates on standard states); 0 fails on
  4,822 couples / 25 genomes on its own engine; RW-WT / RW-WT* / RW-B0 / RW-B0* DEAD on RWX_n95 (two engines; L-NEW's split199 re-run gives
  the counts of §8 D6); C6G8_n54 C = 6; Addendum C: Dhi_y(b) climb, Dhib 26 / sumD 45 at C 4 (DHIB26_2804), no fail.
- Box 197: L-RED 60 R226-core197 (claude/l-red 677b4edb): PAIR-COUNT SURVIVES, ALT-EQUIV SURVIVES for A ≥ 1 (the corrected forms above
  answer its W-2: A = 0).

## 10. TARGET.md diff and scope
- TARGET.md §2 (M4) asks for an algorithm polynomial on EVERY parity game. This packet proves no running-time bound. Its theorems are
  (a) structural lemmas on one run (HOW3(G), i.e. N5′-xi from S3 on Γ3(G) until its first fallback, by P-N5-CHAIN's REACH3-ALL) and
  (b) EQUIVALENCES on that run: T3 polynomial ⇔ Rtop ⇔ A ⇔ C polynomial (RE-EQUIV, ALT-EQUIV, C-EQUIV), and a REDUCTION: C polynomial ⇐
  max over y, b, J of Dhi_y(b, J) polynomial (SPLIT-COUNT, with the factor 3M). Neither side is proved polynomial.
- Not M3, not M4, not a gauntlet step-4 pass (TARGET.md §5). G-N5-TIME stays OPEN; N5′-xi stays a CANDIDATE (D1). TARGET.md §4: even a
  bound proved from this packet would be about Γ3(G) only (a restricted class), until connected to N5 on all parity games.
- Limits: nothing for N5 (SPEC S4a), nothing outside Γ3(G), nothing on iteration counts beyond T3, no [E-LEV] except §7.

## 11. Machine checks
- check.sh block «BOX 199 SPLIT»: re-runs box199/check199.sh (split199.py on CX4_n21, GROW7_n34, NK6_cl21, ROUTELOW_n21, RWX_n95 and six
  controls on CX4_n21), diffs check199.out, requires every PROVED-lemma counter 0, the DEAD witnesses present and the controls firing.
  Blocks «BOX 198 PAIR» and «BOX 197 CORE» do the same for pair198.py and asc197.py.
- check.sh block «P-N5-SPLIT»: sha1 of this packet, its three source files, P-N5-CHAIN (packet and line L-4), and every tool, output and
  instance cited, and of the seven engine modules split199.py loads (eg195, gamma3, n5v, n5x, n5, si, pg: the same sha1s as in
  P-N5-CHAIN's box196/chain.pins), against experiments/new/box199/split.pins (58 rows).
