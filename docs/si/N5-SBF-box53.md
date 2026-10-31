# N5-SBF (box 53): Odd's reply σ̄ is NOT monotone in any fixed order while Ξ rises (the Topkis angle is DEAD: thetaA_n7, n = 7). Theorem ROOT-FLIP (PROVED, lane): a σ̄-flip at a vertex that is not its own Ξ-cycle node, if the old target's Ξ is fixed, is a tie re-order. It descends to a lower flip whose old target's Ξ changed. Hence HEAD-RED′: the SB term of HEAD-RED is replaced by Ξ-changes at τ(Odd) plus own-cycle-node flips
L-SI successor 35 (Opus 5.5), D18. Lead 2026-10-30 18:55Z, BOX 53: «bound per-vertex σ̄-flips (SB_F(o)) inside one W-run, or give the
exact obstruction with an instance … D18 angle …: monotone comparative statics (Topkis) … Find that order, or kill it with an instance.»
Written 19:0xZ-19:4xZ (date -u; see commit).
- Status:
  - §1 is a DEAD END with an instance.
  - §2 is a lane proof (PROVED, lane; not refereed) of a REDUCTION.
  - §3 is a REDUCTION / EQUIVALENCE.
  - SB_F(o) is NOT bounded here. G-N5-TIME stays OPEN. This is not M3, not a step-4 pass, and not a TARGET.md claim.
- Object: N5 only (SPEC S1-S5). Notation as in the frozen packet docs/si/P-N5-SETTLE-box52.md §1-§2 (Ξ_k, σ̄_k, W-run, U_k, D_k, ⊕, ⊴,
  EVENT (i)-(iii), E_F, RUN-COUNT).
- Sources: no outside theorem is used.
  - Topkis (monotone comparative statics) was NOT opened: L-LIT T60 is not on claude/l-lit at 19:0xZ. §1 kills EVERY fixed partial
    order, so it needs no statement from that literature.
  - Premises used (landed or frozen, quoted as stated there): [R57] (S1 realises the pointwise optimum); [R15] (a) and (d); Claim RG′
    (P-N5-SETTLE §3) and T54's LEX-BFS / IDX-MONO proofs (quoted in P-N5-SETTLE §2), read on S1's evaluation (§2.1 below says exactly
    how).
- Tools: experiments/si/sb53/ (topkis.py, rootflip.py, rsearch.py; run*.sh; outputs). Pins: experiments/si/check.sh «box 53 SBF».

## 1. DEAD: σ̄ monotone in a fixed (lattice) order on Odd strategies (the D18 Topkis angle)
- Candidate (Lead's D18 angle). Inside a W-run F, Ξ rises monotonically (R15 (a)). Is Odd's reply σ̄_k monotone, σ̄_k ≤ σ̄_(k+1), in some
  partial order ≤ on Odd strategies fixed for F? (The candidate allows ≤ to be any lattice, a product of per-vertex chains, or any other
  partial order.) Such an order of height h would give SB_F ≤ h.
- Obstruction (exact). If σ̄ changes and later returns to an earlier profile inside F (σ̄_a = σ̄_b ≠ σ̄_(a+1), a < b), then
  σ̄_a ≤ σ̄_(a+1) ≤ … ≤ σ̄_b = σ̄_a. Antisymmetry gives σ̄_(a+1) = σ̄_a, a contradiction. So no fixed partial order works.
  - Per vertex: if σ̄(o) returns to a successor it held earlier, no order whose restriction to o is a fixed order of succ(o) works.
    Products of chains are an example.
- Instance: experiments/n5-exhaustive/instances/thetaA_n7.pg + .start (L-COMP's exhaustive family; read, not edited).
  - n = 7. One Odd vertex, 6, with successors 1 and 5; τ(6) = 5.
  - The whole run (states 0-3) is ONE W-run.
  - σ̄(6): 5, 5, 1, 5.
    - At 1 → 2, σ switches at 5 and Ξ(5) rises, so 6 moves to 1.
    - At 2 → 3, σ switches at 1 and Ξ(1) rises, so 6 moves back to 5.
  - n5b SPEC agrees (si/heads52/flipx.py: «FLIP k 1 o 6 tau 5 old 5 new 1», «FLIP k 2 o 6 tau 5 old 1 new 5»).
- Why (the comparative-statics reading). σ̄(o) is an argmin over succ(o) of Ξ-values. Ξ rises, but at different successors at different
  times, and the order of the rises is set by Even's switches.
  - Increasing differences / single crossing would need the rises ordered consistently by successor.
  - In thetaA_n7 the rises alternate (5, then 1), so the argmin alternates.
  - The monotone object is the VALUE vector Ξ, not the selection.
- DATA (topkis.py, 1,134 corpus runs, box 52's corpus):
  - 242 W-runs revisit a whole σ̄-profile. Smallest: thetaA_n7; also immp_cex_n11, canonA_1.
  - Per-vertex returns: max 61 in one W-run (gate_K64_n581). latew_K16_m32: 31; its profile at state 0 recurs at state 33.
- What survives (used in §2): «σ̄(o) changes only when the incumbent's value rises, or when a tie is re-ordered from below.» That is a
  property of the argmin (an incumbent-rise rule), not a monotone selection.

## 2. Theorem ROOT-FLIP (PROVED, lane; not refereed)
- Setting: ANY transition k → k + 1 of an N5 run. W-runs are not needed.
- Definitions:
  - Odd o is NON-OWN at k if the cycle node c of Ξ_k(o) is not o.
  - A FLIP at o is σ̄_(k+1)(o) ≠ σ̄_k(o), with old target t1 := σ̄_k(o) and new target t2 := σ̄_(k+1)(o).
  - T_k(o) := {t ∈ succ(o) : o ⊕ Ξ_k(t) = Ξ_k(o)}, the TIGHT successors.
  - For t with Ξ_k(t) of cycle node c: path_k(t) := t's (σ_k, σ̄_k)-play t = x_0, x_1, …, x_ℓ = c (the first visit of c), and
    key_k(t) := (x_(ℓ−1), …, x_1, x_0) as vertex indices, compared lexicographically (T54's key).
- Two facts used throughout (from §1 of the packet):
  - (⊕) For y ∉ the paths of X and Y and y not their cycle node, y ⊕ · preserves and reflects ⊴ and ◁, and is injective. This holds for
    the same cycle node by the packet. For different cycle nodes, ⊕ keeps the cycle node and the order is decided by reward first; reward
    is injective.
    - Prefix form: for a simple sequence Q avoiding both paths, Q ⊕ · has the same properties.
  - If o is non-own at k, Ξ_k(o) = o ⊕ Ξ_k(σ̄_k(o)), and path_k(σ̄_k(o)) avoids o. (The play from o is simple up to c.)

### 2.1 Lemma SEL (S1's choice at a non-own Odd vertex; engine-level, PROVED modulo the reading below)
- Statement. Let o be non-own at k with cycle node c. Then σ̄_k(o) ∈ T_k(o), and:
  - (SEL-E) if c is even, σ̄_k(o) is the least-index element of T_k(o);
  - (SEL-O) if c is odd, σ̄_k(o) is the element of T_k(o) with the least key_k.
- Proof.
  - σ̄_k is computed by S1 = si.Engine.evaluate(σ_k) on G: Odd chooses, Even is fixed to σ_k. This is the same code as S4a's call on
    the dual of H_k, with the roles of the fixed and the choosing player exchanged.
  - Claim RG′'s proof (packet §3 (A), (B)) is about that code's deletions in c's round. No step uses which original player chooses,
    and it uses [R57] only to identify the computed values with the optimum (here Ξ_k).
  - So: in c's round, the remaining edges (o, t) with dist(t) = dist(o) − 1 are exactly the tight edges, i.e. T_k(o).
  - c even (longest()): o takes the first successor of maximal dist in hs[o], which is Engine.succ[o] sorted by index and filtered. By
    RG the maximal-dist edges are T_k(o), so σ̄_k(o) = min-index T_k(o). This is T54 IDX-MONO's argument.
  - c odd (BFS from c over hp):
    - o is discovered from the first queued vertex of layer dist(o) − 1 that has the remaining edge (o, ·).
    - hp lists predecessors in increasing index: gp is built for v ascending, and restrict() only removes entries.
    - By T54 LEX-BFS's induction, queue order within a layer is lexicographic order of keys along the BFS tree.
    - The BFS tree path of t is path_k(t): an Even vertex's only edge is σ_k(x); an Odd vertex's tree parent is σ̄_k(x).
    - So σ̄_k(o) = the key-least element of T_k(o).
  - □
- READING to sign: «Claim RG′ (A)-(B) and T54's LEX-BFS / IDX-MONO proofs apply verbatim to Engine.evaluate(σ_k) on G». This is the
  same transfer the packet's §2 asks for S4a.
- DATA (rootflip.py): SEL fails 0 times at 809,844 non-own (state, o) pairs over the 1,134-run corpus (NOTT 0, SELX 0). The control
  MUT=1, with max in place of min, bites: flipev_n20 SELX 7, nep13_n24 SELX 13.

### 2.2 Lemma NOCLOSE (PROVED, lane)
- Statement. Let o be non-own at k with cycle node c and t* := σ̄_k(o). If a successor y of o has o on path_k(y), then
  Ξ_k(y) ▷ Ξ_k(t*).
- Proof.
  - path_k(y) = y … q, o, t*, …, c. Put Z := {y, …, q, o}, a set of vertices; c ∉ Z because the path is simple and o ≠ c. So
    Ξ_k(y) = (y … q o) ⊕ Ξ_k(t*): same cycle node c, path set enlarged by R := {z ∈ Z : z more relevant than c}, length enlarged by |Z|.
  - Suppose Ξ_k(y) ⊴ Ξ_k(t*). They are not equal (the lengths differ). By the order of the packet's §1, either:
    - R ≠ ∅ and max R is odd; or
    - R = ∅ and c is even (when R = ∅, a longer path is better for Even iff c is odd).
  - Let ρ := σ̄_k with o ↦ y. The (σ_k, ρ)-play from o runs o, y, …, q, o and closes the cycle Z, whose cycle node z* is the most
    relevant vertex of Z.
    - If R ≠ ∅: z* = max R, odd, p′(z*) > p′(c), so reward(z*) = −p′(z*) < −p′(c) ≤ reward(c).
    - If R = ∅ and c is even: p′(z*) < p′(c), so reward(z*) ≤ p′(z*) < p′(c) = reward(c).
  - So val(σ_k, ρ)(o) ◁ Ξ_k(o): a strictly better Odd strategy, contrary to [R57]. □
- This is the Odd mirror of P-N5-SETTLE Case 2c.
- DATA: NCX 0 on the corpus.

### 2.3 Lemma TIE (PROVED, lane)
- Statement. Let o be non-own at k and at k + 1, and let it flip t1 → t2 at k → k + 1 with Ξ_(k+1)(t1) = Ξ_k(t1). Then:
  - Ξ(o) and Ξ(t2) are fixed;
  - Ξ_k(t2) = Ξ_k(t1);
  - t1, t2 ∈ T_k(o) ∩ T_(k+1)(o).
- Proof.
  - At k + 1, by [R57]:
    - If o ∉ path_(k+1)(t1): deviating to t1 gives Ξ_(k+1)(o) = o ⊕ Ξ_(k+1)(t2) ⊴ o ⊕ Ξ_(k+1)(t1), so Ξ_(k+1)(t2) ⊴ Ξ_(k+1)(t1)
      by (⊕).
    - Otherwise NOCLOSE at k + 1 gives Ξ_(k+1)(t1) ▷ Ξ_(k+1)(t2).
    - Either way Ξ_(k+1)(t2) ⊴ Ξ_(k+1)(t1) = Ξ_k(t1).
  - At k:
    - If o ∈ path_k(t2), NOCLOSE gives Ξ_k(t2) ▷ Ξ_k(t1).
    - Otherwise [R57] gives Ξ_k(t1) ⊴ Ξ_k(t2).
  - With R15 (a): Ξ_k(t1) ⊴ Ξ_k(t2) ⊴ Ξ_(k+1)(t2) ⊴ Ξ_k(t1). So all are equal, and the strict NOCLOSE alternative at k is impossible.
  - The NOCLOSE alternative at k + 1 is impossible too: Ξ_(k+1)(t1) = Ξ_k(t1) = Ξ_(k+1)(t2).
  - So both paths avoid o at both times, and Ξ_k(o) = o ⊕ Ξ_k(t1) = o ⊕ Ξ_(k+1)(t2) = Ξ_(k+1)(o). Tightness is the same identities. □
- (Step 1 of box 52 §3, made rigorous: it needed NOCLOSE for successors whose play runs through o.)
- DATA: TIEX 0.

### 2.4 Lemma DESCENT (PROVED, lane, given SEL)
- Statement. In the situation of TIE:
  - c := the cycle node of Ξ(o) is odd;
  - some Odd w ≠ o with Ξ_k(w) = Ξ_(k+1)(w), cycle node c, on path_k(t1) or path_k(t2), flips at k → k + 1;
  - ℓ(w) ≤ ℓ(o) − 1.
- Proof.
  - By TIE, t1, t2 ∈ T_k(o) ∩ T_(k+1)(o).
  - If c is even, SEL-E at k and at k + 1 gives index(t1) < index(t2) < index(t1). Impossible.
  - So c is odd. SEL-O gives key_k(t1) < key_k(t2) and key_(k+1)(t2) < key_(k+1)(t1). Hence path_k(t) ≠ path_(k+1)(t) for some
    t ∈ {t1, t2}.
  - Both paths have length ℓ(t) = ℓ(o) − 1 (Ξ(t) fixed). Write x := path_k(t) and y := path_(k+1)(t). Let i be least with
    x_(i+1) ≠ y_(i+1), and w := x_i = y_i. Then i < ℓ(t), so w ≠ c.
  - Ξ(t) = (x_0 … x_(i−1)) ⊕ Ξ(w) at both times, with the same prefix, and the prefix avoids both tails. By injectivity (⊕),
    Ξ_k(w) = Ξ_(k+1)(w), with cycle node c ≠ w.
  - w is not Even.
    - If it were, σ switched at w, a := σ_k(w) → b := σ_(k+1)(w), with (w, b) ∈ Iσ_k by R15 (d), i.e. Ξ_k(b) ▷ Ξ_k(a).
    - Then Ξ_(k+1)(w) = w ⊕ Ξ_(k+1)(b) and Ξ_(k+1)(b) ⊵ Ξ_k(b) ▷ Ξ_k(a), where w ⊕ Ξ_k(a) = Ξ_k(w). Both paths avoid w.
    - By (⊕), Ξ_(k+1)(w) ▷ Ξ_k(w). Contradiction.
  - So w is Odd and σ̄(w) changes: x_(i+1) → y_(i+1).
  - ℓ(w) = ℓ(t) − i ≤ ℓ(o) − 1. w is non-own at k and at k + 1 (cycle node c ≠ w). □
- DATA: EVENX 0 and DESCX 0.
  - The tie case is rare: 2 corpus flips (nep22f_n64), the box-52 kill instances (flipev_n14 / n20, flipnonex_a / b), and 100 in the
    first 300k random games.

### 2.5 Theorem ROOT-FLIP
- Statement. At every transition k → k + 1 of an N5 run: if some Odd o that is non-own at k and at k + 1 flips, then some Odd o* that is
  non-own at k and at k + 1 flips with Ξ_(k+1)(σ̄_k(o*)) ≠ Ξ_k(σ̄_k(o*)).
  - If o's own old target is fixed, o* can be chosen in o's (odd) cycle-node class, with ℓ(o*) < ℓ(o).
  - Corollary EVEN-ROOT: every non-own flip whose cycle node is even has its old target's Ξ changed.
- Proof. Induction on ℓ(o).
  - If Ξ(t1) changes, take o* := o.
  - Otherwise TIE and DESCENT give a non-own flipping w with ℓ(w) < ℓ(o); apply the induction hypothesis to w. □
- Premises: [R57], [R15] (a) and (d), and SEL (that is, Claim RG′ and T54's proofs read on S1's evaluation).
- DATA:
  - Corpus: ROOTX2 0 at every transition (1,134 runs, 25,781 non-own flips).
  - Random search (rsearch.py, in-process, the same seven checks): 10 batches × 100k games, n 10-20, out-degree ≤ 2-3.
    - BIAS = 1, the box-52 form that built flipev_n20: vertex 0 Odd with the top, odd priority, so S1's BFS branch and many ties.
    - Two batches are unbiased.
    - Result: BAD 0 in all ten (si/sb53/rs_out.txt): 1,000,000 games, 778,084 non-own flips, 528 of them in the descent case.
- What it corrects. box 52's FLIP-EV asked for an event (iii) at the old target. The flipev_n20 kill is the case o* ∉ D_k: o*'s old
  target is τ(o*), which is not in U_k. ROOT-FLIP says that is the ONLY way FLIP-EV fails, apart from own-node flips.

### 2.6 ERRATUM (the Odd mirror of REFEREE-2's G-SRC-1; written after R2-N5-SRC §3.2, claude/referee-2 e8c1b62d)
- The gap. §2.3 (TIE: «deviating to t1 gives Ξ_(k+1)(o) … ⊴ o ⊕ Ξ_(k+1)(t1)», and «[R57] gives Ξ_k(t1) ⊴ Ξ_k(t2)») and §5
  (ORDER-CHG′: «[R57] if t2's path avoids o*») read a one-vertex Odd deviation o ↦ t as having value o ⊕ Ξ(t).
  - That holds only up to c. After c the play follows c's (σ_k, σ̄_k)-cycle Z_c. If o lies on Z_c (o non-own but on c's cycle), the
    deviation closes a different cycle.
  - This is REFEREE-2's G-SRC-1 for Odd. NOCLOSE is not affected (its cycle closes at o), and neither are SEL, DESCENT or the
    Even-switch step (they use actual plays only).
- Lemma ONE-STEP-O (PROVED, lane; the Odd mirror of REFEREE-2 24's Lemma ONE-STEP, R2-N5-SRC §3.2).
  - Statement. Let o be Odd and non-own at state k, with c := the cycle node of Ξ_k(o), and t ∈ succ(o) with cycle node c and
    path_k(t) avoiding o. Then Ξ_k(o) ⊴ o ⊕ Ξ_k(t).
  - Proof.
    - ρ := σ̄_k with o ↦ t. The (σ_k, ρ)-play from o is o, then path_k(t) to c, then c's cycle Z_c.
    - (α) o ∉ Z_c. Then val(σ_k, ρ)(o) = o ⊕ Ξ_k(t), and [R57] gives Ξ_k(o) ⊴ val(σ_k, ρ)(o).
    - (β) o ∈ Z_c. Write Z_c = c → … → o → σ̄_k(o) → … → c.
      - path_k(t) meets Z_c only after o: entering the segment from c to o would reach o before c.
      - So Z′ := (the segment of Z_c from c to o) ∪ (o → t) ∪ path_k(t) is a simple cycle. Its top z* is c or the most relevant vertex of
        path_k(t), because c is the top of Z_c.
      - z* = c: the value is o ⊕ Ξ_k(t), as in (α).
      - z* ≠ c, odd: reward(z*) = −p′(z*) < −p′(c) ≤ reward(c). So val(σ_k, ρ)(o) ◁ Ξ_k(o), contrary to [R57]. This case does not occur.
      - z* ≠ c, even:
        - Ξ_k(o)'s path is the segment of Z_c from o to c, whose vertices are less relevant than c, so P(Ξ_k(o)) = ∅.
        - z* ∈ P(Ξ_k(t)) is its most relevant vertex, and it is even. So o ⊕ Ξ_k(t) ▷ Ξ_k(o).
    - □
- Repair. Read every «by [R57], deviating o ↦ t» step of §2.3 and §5 as ONE-STEP-O, at k + 1 and at k respectively.
  - The hypotheses hold there: o is non-own at both states, and the target's path avoids o in the case used.
  - If the target t has cycle node c1 different from o's cycle node, then o is not on c1's cycle (every vertex of that cycle has cycle
    node c1). So case (α) applies and the deviation's value is o ⊕ Ξ(t). ONE-STEP-O is needed only when the cycle nodes agree.
  - No statement of §2-§5 changes. Data: TIEX 0 and ORDX 0 already cover the configurations.
- DATA (rootflip.py ONEX / OBETA, 1,134-run corpus): ONEX 0. The case (β) configuration (o on c's cycle, a vertex above c on t's path)
  occurs 11,129 times (ret22_n40: 18, nep13_n24: 24). All other checks stay 0.

## 3. Corollary HEAD-RED′ (REDUCTION, PROVED, lane, from ROOT-FLIP + RUN-COUNT)
- Definitions. Fix a W-run F (τ fixed).
  - U′_k := U_k ∪ τ(Odd), where τ(Odd) := {τ(o) : o Odd}, a vertex set fixed on F.
  - HXU′_F(u) := the transitions of F with u ∈ U′_k ∪ U′_(k+1) and Ξ_(k+1)(u) ≠ Ξ_k(u).
  - XCN_F := the transitions of F with a σ̄-flip at an Odd o that is its own Ξ-cycle node at k or at k + 1.
  - CN_F as in the packet (transitions switching an Even c ∈ C).
- Claim. Every event transition of F (R143's sense) has:
  - (ii) a CN switch; or
  - (iii′) a Ξ-change at a vertex of U′_k ∪ U′_(k+1); or
  - an own-node σ̄-flip.
- Proof.
  - Events (ii) and (iii) are covered, since U_k ⊆ U′_k.
  - Take an event (i) transition with no own-node flip. Every flipping o is non-own at k and k + 1, so ROOT-FLIP gives o* whose old
    target t* changed.
    - If o* ∈ D_k, then t* = σ̄_k(o*) ∈ U_k.
    - Otherwise t* = τ(o*) ∈ τ(Odd).
  - Either way it is (iii′). □
- Hence E_F ≤ Σ_c CN_F(c) + XCN_F + Σ_u HXU′_F(u), and by RUN-COUNT |F| ≤ n(E_F + 1) − 1.
  - Conversely each term is ≤ |F|.
  - So: polynomial W-runs ⟺ per-vertex CN switches, own-node σ̄-flips and Ξ-changes at U′-heads are polynomial.
- Against HEAD-RED (READING):
  - The SB_F(o) term (all σ̄-flips, data max 61 per vertex) is gone.
  - In its place: own-node flips (corpus: 5 flips in total), and Ξ-changes at the FIXED set τ(Odd).
  - The heads are now «where Odd deviates OR where Odd's τ points». This is box 52's last READING, now proved.
- DATA (topkis.py, corpus):
  - EVX2 0 (transitions with a σ̄-flip, no CN switch, no own-node flip and no Ξ-change on U′): the claim's prediction.
  - TXR: Ξ-changes at one τ(o) per W-run, max 36 (latew_K16_m32: 32 = 2K). Linear on every family seen.

## 4. What is open, exactly
- SB_F(o) is NOT bounded. HEAD-RED′ moves the burden to:
  - (a) HX′-POLY: Ξ-changes at τ(Odd) ∪ U per W-run. Data linear (max 36). Unproved.
  - (b) XCN-POLY: own-cycle-node flips (S1's DFS choice). Corpus 5. Unproved; no kill attempted.
  - (c) CN-POLY.
- A kill target for L-RED (READING): make Ξ(τ(o)) rise super-polynomially often inside one W-run.
  - Each rise is a W-run event (iii′), and between events RUN-SETTLE allows ≤ n − 1 transitions.
  - So the rises must come from feedback through the heads, as in the HX-POLY kill target (box 52 §4).
- Cross-field READING (D18; no source opened). S1's Odd reply is a shortest-path / longest-path tree with a fixed tie-break.
  - ROOT-FLIP is the stability property of such trees under monotone (here: only rising) edge costs: a node re-parents only if its
    parent's label rises, or a re-parenting below re-orders its ties.
  - The dynamic-SSSP literature (incremental shortest paths) has this as a folklore invariant. NOT opened; no claim is imported.

## 5. The [ABS] / [GH] order-charging route (Lead 20:00Z; L-LIT T60 §3.3, l-lit 54584c0c): ROOT-FLIP gives the one-step order change; NO-REPEAT on a fixed head set is DEAD; |U| is linear
- T60's ORDER-DET as written («σ̄_k is determined by σ_k and the ⊴-ORDER of Ξ_k on U_k») is vacuous: S1 computes σ̄_k from σ_k alone.
  The form that the [ABS] Thm 29 charging needs is ORDER-CHG: «σ̄ changes only at transitions where the weak ⊴-order of Ξ on the heads
  changes». (T60's NO-REPEAT of (σ-pattern, order) pairs is vacuous too: σ never repeats in an N5 run, since Ξ strictly rises at each
  improving switch, R15 (a).) The order-only forms are the ones tested below.
- Corollary ORDER-CHG′ (PROVED, lane, from ROOT-FLIP, NOCLOSE and [R57]).
  - Setting: a transition k → k + 1 of a W-run with a σ̄-flip at a non-own Odd vertex, and o* the root flip given by ROOT-FLIP
    (non-own at k and k + 1, old target t1 with Ξ(t1) changed, new target t2).
  - Statement: unless Ξ_k(t1) = Ξ_k(t2) AND Ξ_(k+1)(t1) = Ξ_(k+1)(t2) (a PAIR-TIE), the weak ⊴-order of Ξ on {t1, t2} ⊆ U′_k ∪ U′_(k+1)
    changes at k → k + 1.
  - Proof.
    - t1 ∈ U_k if o* ∈ D_k, and t1 = τ(o*) otherwise. Likewise t2 ∈ U_(k+1) or t2 = τ(o*). So {t1, t2} ⊆ U′_k ∪ U′_(k+1).
    - At k: Ξ_k(t1) ⊴ Ξ_k(t2). This is [R57] if t2's path avoids o*, and NOCLOSE (strict) otherwise.
    - At k + 1: Ξ_(k+1)(t2) ⊴ Ξ_(k+1)(t1), in the same way.
    - So the sign of the comparison of t1 with t2 goes from ≤ 0 to ≥ 0. It is unchanged only if it is 0 at both times. □
  - The PAIR-TIE case (both targets tied before and after, both rising together) is NOT excluded by the proof.
  - DATA (orderchg.py, 1,134 runs):
    - PAIRTIE 0.
    - ORDX 0: every flip transition with no own-node flip and no CN switch changes the weak order on U′_k ∪ U′_(k+1). 4,613
      transitions.
    - With U alone in place of U′ the order is unchanged at 917 of them (ORDX0; thetaA_n7: both flips). So τ(Odd) must be among the
      heads, as in HEAD-RED′.
- DEAD: NO-REPEAT for orders on a fixed head set.
  - Statement killed: «inside a W-run, the weak order of Ξ on a fixed head set never recurs after a different one, and σ̄ is a function
    of it».
  - Instance: experiments/red/so/instances/exitr_cex_n16.pg (L-RED; read, not edited; default start). It has one W-run, states 1-8,
    with fixed head set H_1 := U′_1 = {3, 4, 8, 11}.
    - The weak order on H_1 is the same at states 1, 5, 6 and 7, with a different order at states 2-4 in between.
    - σ̄ of the second Odd vertex is 3, 7, 3, 13 at those four states.
  - So the order on a fixed set neither avoids repeats nor determines σ̄. The heads that decide (7, 13) enter U′ later.
  - Corpus: RREP in 128 W-runs (orderchg.py).
- The parameter is not small. max_k |U_k| is linear in n on L-RED's mkrw family (LATE=1, m = 16): K = 4 / 8 / 12 / 16 gives UMAX
  32 / 48 / 64 / 80 = 4K + 16 at n = 14K + 130.
  - It is also 96 on latew_K16_m32 (n 482). |U′| is up to 385 on the corpus.
  - Distinct head orders per W-run ≈ the W-run length (NORD 19K + 1 on mkrw; 561 on latew).
  - So «FPT in max |U_k|» gives 2^Θ(n) or Θ(n)! on these families: nothing.
- Answer to the Lead's question. ROOT-FLIP IS the one-step part of ORDER-CHG: every non-own σ̄-flip comes with an order change on
  U′_k ∪ U′_(k+1), up to the PAIR-TIE case. This is PROVED (lane) except for PAIR-TIE (data 0).
  - It does NOT give a count: the counting half of [ABS] / [GH] (no repeat, or a value quantum, over a SMALL fixed set) fails on two
    counts:
    - the set is not small (Θ(n));
    - the order on a fixed set does recur (exitr_cex_n16).
  - A quantum is XI-CH-POLY again, as T60 says.

## 6. Own-cycle-node σ̄-flips (XCN): XCN-ONE DEAD; kind A PROVED ≤ n(n − 1) per run (from R47); kind B (DFS re-orders) OPEN
- Split an own-node flip at o, k → k + 1 (o its own Ξ-cycle node at k or at k + 1), into two kinds:
  - KIND A: o is its own Ξ-cycle node at exactly one of k, k + 1;
  - KIND B: at both (S1's DFS re-picks o's cycle edge while Ξ(o) = (o, ∅, 0) stays fixed).
- DEAD: CONJECTURE XCN-ONE (at most one XCN transition per W-run), with instances in experiments/si/sb53/inst/. n5b agrees on each.
  - xcn2_n8 + .start (n 8), one W-run of 3 transitions with two kind-A transitions:
    - at 0 → 1, Odd 0 stops being its own cycle node (cycle node 0 → 7; σ̄(0) 2 → 7);
    - at 1 → 2, Odd 5 becomes its own cycle node (σ̄(5) 4 → 5).
  - xcnb2_n12 + .start (n 12), one W-run of 3 transitions with two kind-B transitions at the SAME vertex: σ̄(3) = 9 → 11 (0 → 1) and
    11 → 9 (2 → 3). Ξ(3) = (3, ∅, 0) throughout, and λ_Ξ never changes (LAMCH 0).
  - Found by xcnrs.py (BIAS 1 / 2) and a kind-B variant of it, after 70k + 360k games. The corpus never shows two in one W-run
    (XCN_TR max 1).
- Corollary KIND-A (PROVED, lane, from RESULTS R47 Lemma Φ).
  - Statement: every N5 run has at most n(n − 1) transitions carrying a kind-A flip. In particular so has every W-run.
  - Proof.
    - A kind-A flip at o changes λ_Ξ(o): it is o at one state and not at the other.
    - By R47 Lemma Φ («cycle nodes only rise … along a run»), each change of λ_Ξ(v) moves to a cycle node of strictly larger reward.
    - Rewards are injective, so each vertex's λ_Ξ changes at most n − 1 times. Hence at most n(n − 1) transitions change λ_Ξ at all. □
  - DATA (xcn.py, corpus): XANL 0 (no kind-A transition without a λ_Ξ change); whole-run kind A 472, LAMCH 3,179 (max 30).
- So HEAD-RED′'s XCN term splits as XCN_F ≤ n(n − 1) + XB_F, where XB_F := the kind-B transitions of F.
  - Polynomial W-runs ⟺ CN-POLY ∧ HX′-POLY ∧ XB-POLY (per W-run).
- OPEN: XB-POLY.
  - Corpus: 17 kind-B transitions over whole runs, at most 2 per run.
  - Mechanism (xcnb2_n12): S1's DFS at an own node takes the first cycle-closing successor; the stack order makes it depend on the
    Even choices below. Even switches below can make it alternate (9, 11, 9).
  - No bound is known. This is the Odd analogue of the CN term (Even cycle-node switches).

## 7. Box 53b (Lead 01:57Z, KEYCH-POLY, proof side): KEYCH-POLY ⟺ INT-POLY; Lemmas LEX-TREE and TREE-STABLE (PROVED, lane); KEYCH_I(x) ≤ 1 + INS_I(c), insertions = tight-sibling Ξ-overtakes
- Source read (not edited): L-NEW 40 box 106, docs/new/N5-TIE-box106.md at claude/l-new 8591166d (ODD-NORET, KEY-MON, TIE-RED,
  CONJECTURE KEYCH-POLY), and its experiments/new/box105/keymon.py. Premise: T54 LEX-BFS as P-N5-SETTLE reads it (signed there as used).
- Setting.
  - I = [p, q] is a W-constant interval of a W-run F (W, λ_W, the lengths ℓ and the W-tight edge set are fixed on I).
  - c is an EVEN W-cycle node, X_c := {x ≠ c : λ_W(x) = c}, and T(y) := the W-tight successors of an Even y ∈ X_c (all with cycle
    node c).
  - For a state k of I: A_k(y) := ({σ_k(y)} ∪ Iσ_k(y)) ∩ T(y), the tight arena of y.
  - LexTree(A) := the strategy on X_c in which every Even y takes the element of A(y) of least key. Keys are T54's, built layer by
    layer from c (key(c) := (), key(x) := key(next x)·x); Odd vertices follow τ.
- Proposition KEYCH-EQ (PROVED, lane, from L-NEW's KEY-MON and ODD-NORET). For every W-constant interval I:
  |I| ≤ m_E + CN_I + n·max_x KEYCH_I(x), and KEYCH_I(x) ≤ |I|, where CN_I := the transitions of I switching an Even vertex of C.
  - Proof.
    - Every transition of a W-run switches some Even vertex (P-N5-SETTLE §1).
    - A switch at y ∈ X_c with c even strictly lowers key(y) (KEY-MON), so such y switches ≤ KEYCH_I(y) times.
    - With c odd, y switches ≤ deg(y) − 1 times (ODD-NORET); summed, ≤ m_E.
    - The rest are CN switches.
    - The converse holds since a key changes at most once per transition. □
  - So KEYCH-POLY is EQUIVALENT to polynomial W-constant intervals (modulo CN_I). It is not a smaller statement than INT-POLY
    (box 51b's INT-LIN family).
- Lemma LEX-TREE (PROVED, lane; premise LEX-BFS). For p ≤ k < q, σ_(k+1) restricted to X_c equals LexTree(A_k).
  - Proof. Induction on ℓ.
    - LEX-BFS: σ_(k+1)(y) minimises key_(σ_(k+1))(z) over the W_(k+1)-tight arena edges of H_k at y. Since W_(k+1) = W, those are
      exactly A_k(y).
    - Keys of the lower layers are those of LexTree by induction (Odd vertices follow τ in both).
    - The minimiser is unique, since distinct z give keys with distinct last entries. □
- Lemma TREE-STABLE (PROVED, lane). For p ≤ k and k + 2 ≤ q: if A_(k+1)(y) ⊆ A_k(y) for every Even y ∈ X_c (no INSERTION), then
  σ_(k+2) = σ_(k+1) on X_c.
  - Proof. By LEX-TREE, σ_(k+2) = LexTree(A_(k+1)) and σ_(k+1) = LexTree(A_k). Induction on layers:
    - Lower keys agree.
    - m := σ_(k+1)(y) is the key-least element of A_k(y), and m ∈ A_(k+1)(y). (It is the current target at k + 1, and W-tight because
      W(y) = y ⊕ W(σ_(k+1) y) on y's own play, y ∉ C.)
    - A_(k+1)(y) ⊆ A_k(y), so m is also the key-least element of A_(k+1)(y). □
  - In words: a lex-min path tree is unchanged by deletions of non-tree arena edges. The current edge is never deleted, because the
    arena always contains σ.
- Corollary INS-RED (PROVED, lane). Let INS_I(c) := the k with p ≤ k ≤ q − 2 at which some A_(k+1)(y) ⊄ A_k(y), y ∈ X_c Even.
  - The transitions of I switching a vertex of X_c number ≤ 1 + INS_I(c), and KEYCH_I(x) ≤ 1 + INS_I(c) for every x ∈ X_c.
  - So |I| ≤ m_E + CN_I + Σ_(c even) (1 + INS_I(c)), with no factor n or ℓ (compare RUN-SETTLE's n(E + 1)).
- Lemma OVERTAKE (PROVED, lane). Every insertion z ∈ A_(k+1)(y) ∖ A_k(y) is a strict Ξ-overtake of y's target:
  - Ξ_k(z) ⊴ Ξ_k(σ_k y) ⊴ Ξ_k(σ_(k+1) y) and Ξ_(k+1)(z) ▷ Ξ_(k+1)(σ_(k+1) y). So Ξ(z) strictly rises at k → k + 1.
  - Proof. z is tight and z ∉ A_k(y), so z ≠ σ_k(y) and not Ξ_k(z) ▷ Ξ_k(σ_k y).
    - z ≠ σ_(k+1)(y), because σ_(k+1)(y) ∈ A_k(y) by LEX-TREE.
    - So z ∈ Iσ_(k+1)(y), i.e. Ξ_(k+1)(z) ▷ Ξ_(k+1)(σ_(k+1) y).
    - σ_(k+1)(y) ∈ {σ_k y} ∪ Iσ_k(y) gives the middle inequality, and R15 (a) the rest. □
- Fact CEILING (PROVED, lane; with [R57]).
  - Tight siblings share their W-value: y ⊕ W(z) = W(y) = y ⊕ W(a) gives W(z) = W(a), by injectivity of y ⊕ · on paths avoiding y.
  - Ξ_k ⊴ W_k pointwise (σ̄_k is Odd's optimum against σ_k, and τ is one Odd strategy).
  - So all tight siblings' Ξ-values rise under ONE common ceiling W(a), fixed on I. An overtaken target a satisfies Ξ_k(a) ◁ W(a): it
    is in the gap set Z_k = {Ξ_k ≠ W_k}.
- Reduction (the named smaller statement). KEYCH-POLY ⟺ INT-POLY (mod CN_I) ⟸ INS-POLY, where INS-POLY := «per W-constant interval and
  even cycle node c, the transitions with a strict Ξ-overtake among W-tight siblings below the common ceiling are polynomial».
  - INS ≤ |I|, so the three are equivalent (mod CN_I, m_E). The gain is that the count is now:
    - of transitions, not of keys;
    - per class, with no factor n;
    - charged to sibling ORDER reversals of Ξ under a fixed ceiling, i.e. T60's PAIR-CROSS on the Even side, restricted to tight
      siblings in the gap set.
  - INS-POLY is NOT proved. A value space with exponentially many points below the ceiling allows many reversals a priori.
- DATA (experiments/si/sb53/treestab.py, corpus 1,134 runs, 35 W-constant intervals with switches):
  - LTX 0 (LEX-TREE), TSX 0 (TREE-STABLE), NOVT 0 (OVERTAKE), KB 0 (KEYCH ≤ 1 + INS).
  - MAXKEYCH 8 and MAXINS 7, both on u23sw64_n32, where the bound is attained (8 = 1 + 7).
  - MUT=1 control (LexTree with max) bites: u23sw64_n32 LTX 8.
- READING (D18; no source opened). LEX-TREE / TREE-STABLE are the dynamic lex-min path-tree facts:
  - the tree is a function of the current arena;
  - deletions of non-tree edges never change it;
  - only insertions can.
  - So the interval is an incremental lex-min tree driven by Ξ-overtakes. Bounding the insertions is the remaining, Ξ-side, question.

## 8. Box 53c (Lead 06:43Z, compounding of k-SOURCE up the levels): R94's K is flat on the leapfrog instances; the CEILING agreement A pays them; the residue is A-flat transitions
- Sources read (not edited): L-RED R156 (docs/red/R156-twosource.md, claude/l-red at fetch 06:4xZ: k-SOURCE and its composition corollary);
  the L-RED instances experiments/red/wlev/instances/src2_K3, src1_K4 (read from claude/l-red into the scratchpad; not in this tree) and
  red/xich/instances/obs_K12_m24.
- The question. k-SOURCE composes as WCH(h) ≤ K_0 + Σ_b (K_b + 1)(1 + WCH(u_b)), a factor of about (deg + 1) per level. The Lead asks for a
  global potential, or a charging scheme, that pays the re-openings once across all levels.
- (a) R94's potential does NOT pay them (DATA, si/sb53/phasek.py).
  - K := Σ_v DEPTH(v) is monotone inside a phase (R94 FIXD-MON), bounded by n(n + 2), and level-free. But on the leapfrog instances the
    whole run is one phase in which K is flat:
    - src2_K3 (n 285): one phase of 324 transitions, KUP 1, FLAT 323;
    - src1_K4 (n 289): one phase of 325 transitions, KUP 2, FLAT 323.
  - So R94's PHASE-RED puts everything in FLATTR, and K charges nothing.
- (b) The ceiling agreement A_k := Σ_v lcp(CS(Ξ_k(v)), CS(W_k(v))) (R93 coordinate sequences; Ξ ⊴ W by Fact CEILING, §7).
  - Accounting Lemma CEIL-ACC (PROVED, lane, elementary). 0 ≤ A_k ≤ n(n + 2), so every W-run F has
    |F| ≤ (1 + AUP_F)·n(n + 2) + ANDN_F. Here AUP_F is the number of transitions of F at which A rises, and ANDN_F the number at which A
    does not strictly fall.
    - Proof. Between two rises, A strictly falls at every transition counted outside ANDN_F, and it can fall at most n(n + 2) times in a
      row. □
  - The lemma is level-free: a transition is charged once, whatever the depth of the selector hierarchy that caused it.
  - DATA (si/sb53/ceilpot.py; W-runs as treestab.py). The compounding / leapfrog / head-feedback families are paid by A:
    - src2_K3: one W-run of 324, AUP 1, ANDN 1;
    - src1_K4: one W-run of 325, AUP 1, ANDN 2;
    - obs_K12_m24: one W-run of 324, AUP 1, ANDN 1;
    - latew_K16_m32: one W-run of 560, ANDN 1;
    - fx_K8_m32: one W-run of 280, ANDN 1.
    - On all of them A falls at every other transition: W pulls away from Ξ one coordinate-prefix at a time.
  - Corpus (1,134 runs, 14,868 W-run transitions): AUP 1,265 (max 39 in a run, 33 in one W-run); ADN 5,245; AEQ 8,358 (A flat).
    - AUPZ 350: rises of A without a gap-set shrink. So a rise is not only a gap closing.
  - The A-FLAT regime is the other face. runfam_K40 (n 79): its longest W-run of 159 has ANDN 147.
    - u23sw64_n32: its W-constant interval is A-flat (ANDN 8 of 8). That interval is what §7's INS-RED bounds.
- Reduction (PROVED, lane, from CEIL-ACC): every W-run has polynomially many transitions if AUP-POLY and AFLAT-POLY hold. Here
  AUP-POLY := rises of A per W-run are polynomial, and AFLAT-POLY := transitions per W-run at which A does not fall are polynomial.
  - The k-SOURCE compounding needs neither on the instances in hand: A falls throughout.
  - A multiplying counter must therefore make A rise often (each rise worth ≤ n(n + 2) transitions) or keep it flat. This is a concrete
    target for L-RED R157.
  - Neither AUP-POLY nor AFLAT-POLY is proved. AFLAT contains the tie face (§7, INS-POLY) and runfam's regime.
- READING (no source opened). A is a «distance to the ceiling» in the lexicographic lattice of values: W rises, Ξ lags, and their common
  prefix shortens. A strict fall is W gaining a coordinate on Ξ. A rise is Ξ catching up, which needs Ξ's own rise at a prefix coordinate.
  Why A falls at almost every leapfrog transition is not proved.

## 9. Box 53d (Lead 07:25Z): joining CEIL-ACC to R97 SRC-COUNT. DEAD: «A falls at every source-free transition» (u23sw64_n32, runfam_K40)
- Question. Are A's rises and non-falls confined to SOURCE EVENTS? R97 (P-N5-SRC, landed, trunk 9777660f) defines a source event as a
  Ξ-change at S_k = D_k ∪ D_(k+1) ∪ C, and proves |F| ≤ E^S_F + (E^S_F + 1)(n − 1 + m_C) (Corollary SRC-COUNT). If AUP_F and ANDN_F were
  ≤ f(E^S_F), CEIL-ACC would join SRC-COUNT.
- DEAD (si/sb53/ceilpot.py, SRC / AUPSF / ANDNSF / AEQ0SF / AEQMAXSF / AMIDSF).
  - First test, u23sw64_n32 (default start): 13 W-run transitions, 1 source event. At the 12 source-free ones A never falls.
    - 8 flats are at the FLOOR A = 0. These are states 1-9, the W-constant interval of §7: D = {27}, and Ξ has a different cycle node from
      W at every vertex, so A is blind to everything below the first coordinate.
    - 3 are at the CEILING A = n(n + 2) (Ξ = W).
    - 1 lies strictly inside: 13 → 14, A = 1087 flat.
  - Corpus (1,134 runs; 14,868 W-run transitions, 5,114 source events): at source-free transitions A rises 142 times (max 32 in a run)
    and does not fall 7,161 times.
    - Of those non-falls, 78 are floor flats, 3,430 ceiling flats, and 3,653 lie strictly inside (0, n(n + 2)).
    - runfam_K40 (n 79) alone has 81 strictly-inside source-free non-falls. lend107_n32 has 3 source-free rises.
  - So neither AUP_F nor ANDN_F is bounded by a function of E^S_F. CEIL-ACC and SRC-COUNT do not combine into a sharper reduction.
- What survives (DATA). On the leapfrog / k-SOURCE families A falls at EVERY source-free transition (ANDNSF 0: src2_K3, obs_K12_m24).
  There the 324-transition W-runs carry 24 source events.
  - CEIL-ACC is the bound that applies there. It also explains R157's cap: the passive re-climbing is paid by A's descent, at most
    n(n + 2) per rise of A.
- Why A is the wrong potential on the other face (READING). A compares coordinate sequences from the top: it is 0 as soon as Ξ and W
  have different cycle nodes, and saturates at Ξ = W. A finer potential would compare, per vertex, the PATH of Ξ with the path of W
  below their first difference. Not built.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/si/sb53/ (topkis.py, rootflip.py, rsearch.py, runtopk.sh, runroot.sh, runrs.sh, topk_*.txt,
  root_*.txt, rs_out.txt); pins in si/check.sh «box 53 SBF». SHA: see the commit.
- FINDINGS:
  - DEAD: σ̄ monotone in any fixed partial order on Odd strategies (Topkis angle). Instance thetaA_n7: σ̄(6) 5 → 1 → 5 in one W-run
    (n5b agrees); 242 corpus W-runs revisit a profile.
  - PROVED (lane): Lemmas NOCLOSE, TIE, DESCENT; Theorem ROOT-FLIP (any N5 transition); Corollary EVEN-ROOT; Corollary HEAD-RED′
    (REDUCTION: SB term → τ(Odd)-head Ξ-changes + own-node flips). SEL is proved modulo the reading «RG′ and T54 apply to S1's own
    evaluation».
  - CONJECTURE (data only): HX′-POLY.
  - §6: XCN-ONE DEAD (xcn2_n8 kind A; xcnb2_n12 kind B, σ̄(3) 9 → 11 → 9); Corollary KIND-A PROVED (≤ n(n − 1) per run, from R47);
    XB-POLY (DFS re-orders at own nodes) OPEN.
  - §2.6 ERRATUM: the Odd mirror of G-SRC-1; repaired by Lemma ONE-STEP-O (PROVED, lane; ONEX 0).
  - §7 (box 53b, KEYCH-POLY): KEYCH-EQ (KEYCH-POLY ⟺ INT-POLY mod CN), LEX-TREE, TREE-STABLE, INS-RED, OVERTAKE, CEILING PROVED (lane);
    reduction to INS-POLY (tight-sibling Ξ-overtakes per interval; open).
  - §8 (box 53c, k-SOURCE compounding): R94's K flat on src2_K3 / src1_K4 (DATA); CEIL-ACC PROVED (lane, |F| ≤ (1 + AUP)n(n + 2) + ANDN);
    the leapfrog / head-feedback families have AUP ≤ 1, ANDN ≤ 2; reduction to AUP-POLY ∧ AFLAT-POLY (open).
  - §9 (box 53d): DEAD «A falls at every source-free transition» (u23sw64_n32: 12 source-free non-falls; corpus 7,161, 3,653 strictly
    inside); CEIL-ACC does not join R97 SRC-COUNT; A falls at every source-free transition only on the leapfrog families (DATA).
  - §5 (Lead 20:00Z): Corollary ORDER-CHG′ PROVED (lane) up to PAIR-TIE (data 0). DEAD: NO-REPEAT / order-determination on a fixed
    head set (exitr_cex_n16). max |U_k| = 4K + 16 on mkrw, so FPT in |U| is empty.
- NEEDS: Lead: route ROOT-FLIP (§2) and HEAD-RED′ (§3) to L-RED for a kill attempt, and, if wanted, to a packet. L-LIT T60: Topkis
  sources are now only needed for §1's framing; the kill does not depend on them.
