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

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/si/sb53/ (topkis.py, rootflip.py, rsearch.py, runtopk.sh, runroot.sh, runrs.sh, topk_*.txt,
  root_*.txt, rs_out.txt); pins in si/check.sh «box 53 SBF». SHA: see the commit.
- FINDINGS:
  - DEAD: σ̄ monotone in any fixed partial order on Odd strategies (Topkis angle). Instance thetaA_n7: σ̄(6) 5 → 1 → 5 in one W-run
    (n5b agrees); 242 corpus W-runs revisit a profile.
  - PROVED (lane): Lemmas NOCLOSE, TIE, DESCENT; Theorem ROOT-FLIP (any N5 transition); Corollary EVEN-ROOT; Corollary HEAD-RED′
    (REDUCTION: SB term → τ(Odd)-head Ξ-changes + own-node flips). SEL is proved modulo the reading «RG′ and T54 apply to S1's own
    evaluation».
  - CONJECTURE (data only): HX′-POLY, XCN-POLY.
- NEEDS: Lead: route ROOT-FLIP (§2) and HEAD-RED′ (§3) to L-RED for a kill attempt, and, if wanted, to a packet. L-LIT T60: Topkis
  sources are now only needed for §1's framing; the kill does not depend on them.
