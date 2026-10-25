# R-N5-OE: REFEREE report on packet P-N5-OE (Lemma U-loc, Lemma OE, Corollary OX)
Referee: REFEREE (successor 6), Opus 5.5 (owner ruling D15, Lead reading L37). Packet P-N5-OE: the Lead's message of 2026-10-25 01:44Z
(Lead's stamp). Object docs/new/P-N5-OE-box32.md at pinned trunk 361d18c, sha1 adeccd898ad1e4de6532fc3a77a9d600d8a0bc16 (checked:
`git show 361d18c:docs/new/P-N5-OE-box32.md | sha1sum`). Written 2026-10-25 01:51Z onward by date -u. Every verdict is labelled
(Opus 5.5, D15). Labels (D18/L40): PROVED (by whom) / CONJECTURE / OPEN. Independent of REFEREE-2: docs/referee-2/ not read for this packet.
Dependencies were read at trunk f99bd852 (merged into claude/referee): P-N5-LP (docs/new/P-N5-LP-box32.md, sha1 d2c8121a…) and its fixes
file docs/new/P-N5-LP-fixes-box32.md; RESULTS R25 (P-N5-FB, docs/si/P-N5-FB-box7.md §5 J1/OFF/CAP); R22 (b) TC; R19 (a); P-N5-U23 fixes §6 (R-1);
docs/referee/R-N5-FB.md §4.2 (my predecessor's full-minimiser proof); docs/new/N5-NH-box28.md l. 9 (definition of H1).

## Verdicts
| statement | lane label | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §1 Lemma U-loc (any game, inside a phase) | PROVED (L-NEW) | SIGNED |
| §2 Lemma OE (𝒞^1O) | PROVED (L-NEW) | SIGNED WITH GAPS: OE-1 (the "In particular" sentence is stronger than the proof: it gives no relevant σ̄(o) change of level ≠ ⊥, and level-⊥ (tie) changes do occur off crossings; wording), OE-2 (the CAP-1 citation must cover o lying on its honest cycle, case ¬H1: it does; closed by my re-derivation, §2.2), OE-3 (step 3's comparison: cite (C1) and (C3); wording) |
| §3 Corollary OX (i)-(v) (𝒞^1O) | PROVED (L-NEW) | SIGNED (OX-1 wording: f and T are counted over transitions with both ends in the phase, R25 FB-2) |
| §3 Reading | READING | not signed (not asked); one note in §3.6 |

Trap check asked by the Lead (every minimiser / VJ00 Lemma 5.8 step at own cycle nodes): the packet cites no VJ00 Lemma 5.8 and neither DF nor
DF′. It uses a minimiser in one place only, Lemma OE steps 3 and 4 (ℓ = −1), and only at o with λ(o) ≠ o, so o is not its own cycle node.
CAP-1's case split proves exactly that case. It also covers o on a cycle, which is not the same as o being its own cycle node (§2.2). The
known failure of the minimiser property at λ(o) = o (FIX-2 DFS) reproduces in my probe as a negative control: 102 of 527 states. Lemma OE
assumes λ(o) ≠ o from step 1, because O_k is defined only for relevant changes.

## 1. Lemma U-loc: SIGNED
- I checked P-N5-LP Lemma U steps 2-4 (signed by both referees) line by line with a general L in place of L_k:
  - Step 2 uses only the phase: c := λ(v) is fixed, and Ξ_k(c) = Ξ_{k+1}(c) = (c, ∅, 0) by (P3).
  - Step 3 uses the bound only at the path vertices p_0, …, p_{s−1}. These are not their own cycle nodes (λ = c ≠ p_i), so a successor
    change there is a relevant change, of level ≤ L by hypothesis, and (C2) applies.
  - Step 4 is the downward induction with (C4) and (P2).
  So the substitution is valid. For L = ⊥, COARSE_⊥ is the identity and (C4) holds trivially.
- The lemma's hypothesis quantifies over v's H_{k+1}-path. So does Lemma U's induction. Correct.
- L = ∞ is excluded by the statement. It is not needed, since relevant levels are finite inside a phase (Lemma U step 1).
- DATA: 194,981 (v, k) checks on the library and 142,094 on random games; 0 failures (oe_probe ULOC). L_v is computed per vertex from the
  relevant changes on its own H_{k+1}-path.

## 2. Lemma OE: SIGNED WITH GAPS OE-1, OE-2 (closed), OE-3
### 2.1 Step by step
- Step 1:
  - λ_k(x0) = c by (P1) on the H_k-edge (o, x0).
  - λ_k(x1) = λ_{k+1}(x1) = c by (P1) at k+1 and the phase.
  - So ℓ < ∞. ℓ ≠ ⊥, since O_k ≠ ⊥.
  - CAP-1 at k and at k+1 needs λ(o) ≠ o at both. This holds: λ is constant in the phase. Correct.
- Step 2 (x1's H_{k+1}-path to c avoids o):
  - Correct as written: (P2) applies along the path, because no vertex before c is its own cycle node.
  - A shorter argument: H_{k+1} is a functional graph. If o came before c, the path would return to x1 = σ̄_{k+1}(o) before reaching c,
    and so it would never reach c.
  - On 𝒞^1O the only possible changes on that path are Even ones, of level ≤ E_k by the definition of E_k. Odd vertices other than o are
    forced.
  - U-loc with L = E_k applies. Correct. (E_k = ⊥ ⟺ no relevant Even change, because a relevant Even switch goes to a gate edge,
    R15 (d), so its level is ≥ −1.)
- Step 3 (H1):
  - H1 means the honest play from o does not return to o (docs/new/N5-NH-box28.md l. 9). So x0's honest play, the tail of o's, never
    visits o. It therefore equals x0's (σ_k, τ)-play, and x0 ∈ F_k.
  - F_k = F_{k+1}, since there is no crossing.
  - x0's H_{k+1}-play agrees with its (σ_{k+1}, τ)-play until o, so it never visits o. (Direct; the R19 (a) citation is correct but not
    needed.)
  - U-loc with L = E_k gives COARSE_{E_k}(Ξ_{k+1}(x0)) = COARSE_{E_k}(Ξ_k(x0)).
  - Comparison: at k, Ξ_k(x0) ◁ Ξ_k(x1) strictly (full minimiser, values differ). Their COARSE_{E_k} values differ by (C2), since
    ℓ > E_k, so (C1) gives COARSE x0 ◁_{E_k} COARSE x1. These coarse values are the same at k+1.
  - If Ξ_{k+1}(x1) ⊴ Ξ_{k+1}(x0), then (C1) gives COARSE x1 ⊴_{E_k} COARSE x0, and (C3) makes them equal, a contradiction. ⊴ is total,
    so Ξ_{k+1}(x0) ◁ Ξ_{k+1}(x1), against CAP-1 at k+1.
  - Correct. The packet says "the top difference is above E_k and decides the comparison". That is this argument; OE-3 asks for (C1)
    and (C3) to be cited.
- Step 4 (¬H1, which also holds at k+1 by R22 (b) TC (i)):
  - o lies on its honest cycle, whose top is c ≠ o. Every vertex of that cycle has rank ≤ rank c. So P(Ξ_k(x0)) = ∅ (R-1), and likewise
    P(Ξ_{k+1}(x1)) = ∅, because x1 = σ̄_{k+1}(o) lies on o's honest cycle at k+1.
  - Case ℓ ≥ 0: the top of P(x0) Δ P(x1) = P(Ξ_k(x1)) has rank ℓ > E_k. Step 2 keeps it in P(Ξ_{k+1}(x1)) = ∅, a contradiction.
    Correct. This sub-case needs no minimality.
  - Case ℓ = −1: E_k = ⊥. x0's H_k-path runs along the honest cycle from x0 to c, before o (c ≠ o). None of its vertices changes its
    successor: its Even vertices are not their own cycle nodes, so any change would be relevant, and E_k = ⊥ says there is none. Odd
    vertices are forced, and o is not on the path.
  - So the H_{k+1}-path is the same path, and Ξ_{k+1}(x0) = Ξ_k(x0). With step 2, Ξ_{k+1}(x1) = Ξ_k(x1). So x0 is strictly better for Odd
    at k+1, against CAP-1 at k+1. Correct.
- The case split is complete: ℓ > E_k leads to a contradiction under H1 and under ¬H1, and ℓ ∈ {−1} ∪ {0, 1, …} under ¬H1.
- Fallback (S4c) transitions are covered. The proof uses neither S4a nor any property of σ_{k+1} beyond its being the next state.

### 2.2 OE-2: CAP-1 at o on a cycle (closed)
- R25 (e) records CAP-1's closure as "λ(o) ≠ o giving a full minimiser". Step 4 (ℓ = −1) uses it when o lies on its honest cycle (¬H1)
  without being its cycle node. So the citation must cover that case.
- I re-derived R-N5-FB §4.2 myself, for an Odd v with λ(v) = c ≠ v and u ∈ succ(v), τ′ := σ̄[v → u]:
  - (a) If u's honest play avoids v: (11) gives v ⊕ Ξ(σ̄ v) ⊴ v ⊕ Ξ(u). v is in neither path set (σ̄ v's path reaches c before returning
    to v, since the graph is functional), so ⊕ v preserves strict order, also across different cycle nodes. Hence Ξ(σ̄ v) ⊴ Ξ(u).
  - (b) If it passes v: Ξ(u) = (seg ∪ {v}) ⊕ Ξ(σ̄ v), where the extra set D := (seg ∪ {v}) ∩ V_{>rank c} is disjoint from P(Ξ(σ̄ v)) (one
    simple path to c).
    - D ≠ ∅ with even top: Ξ(u) ▷ Ξ(σ̄ v).
    - D ≠ ∅ with odd top t: the τ′-cycle has top t, odd, above c. That is worse for Even than c whatever c's parity, against (11).
    - D = ∅ with c even: the cycle's top is below c, worse for Even than an even c (lower even, or odd), against (11).
    - D = ∅ with c odd: same cycle node and path set, longer, so Ξ(u) ▷ Ξ(σ̄ v).
  - Nothing in (a) or (b) assumes v is off a cycle. So the full-minimiser property holds at o under ¬H1. CLOSED.
- This also matches R2-N5-FB §C.3 (read on trunk, as my predecessor's addendum 2a0cb306 cites it). The two-signature status of CAP-1 is
  REFEREE-2's adoption, not my reading.
- DATA: σ̄(o) is a full minimiser at all 5,694 library states and 9,085 random states with λ(o) ≠ o. Control at λ(o) = o: non-minimiser
  at 102 of 527 states (rand seed 7101). So the check can fire.

### 2.3 OE-1: the "In particular" sentence
- The packet says: "In particular, if Even makes no relevant change, σ̄(o) makes no relevant change."
- The proof gives O_k ≤ E_k = ⊥, i.e. O_k = ⊥. By P-N5-LP §1 a relevant change of σ̄(o) is any change with λ(o) ≠ o, including a
  change between successors of equal value (level ⊥). Such tie changes exist off crossings: library 2, random 50 (oe_probe so_tie_nX).
- With E_k = ⊥ none was seen (0 crossing-free σ̄(o) changes with no relevant Even change, library and random). So the sentence is not
  refuted, but it is not proved.
- Repair: "σ̄(o) makes no relevant change of level ≠ ⊥" (or "O_k = ⊥"). Nothing in §3 uses more: (i) and (iii) use the used level, and
  (ii) uses a level > M_k.

## 3. Corollary OX: SIGNED
- (i) ε counts relevant transitions whose used level is attained only by Odd changes. On 𝒞^1O these can only be σ̄(o) changes, so O_k > E_k.
  Lemma OE then makes the transition a crossing, so ε ≤ X. Correct.
- (ii) J ≤ X:
  - J1 (P-N5-FB §5, l. 172) says b ≠ a and lev(Ξ_k a, Ξ_k b) > M_k, with a = σ̄_k(o) and b = σ̄_{k+1}(o). This is O_k's level.
  - The change is relevant by P-N5-LP Corollary LP′ step 3, signed. If λ(o) = o, then L_k ≤ M_k, and Lemma U freezes COARSE_{M_k}, so
    the transition is tame.
  - M_k ≥ E_k: each relevant Even switch goes to a gate edge (R15 (d)), and its level is that edge's gate level.
  - So O_k > E_k, and Lemma OE makes the transition a crossing. Correct.
- (iii) The four cases of LP′ step 2 are checked. In the third case (no fallback, no crossing in [k, k′], all relevant Even levels at
  k′ ≤ L_k < L_{k′}), O_{k′} = L_{k′} > E_{k′}. So k′ is a crossing (Lemma OE), and the case is empty. The fourth case is a wake by the
  definition: R constant on [k, k′ + 1] ⟺ no crossing at transitions k, …, k′. So ρ ≤ 2f + 2X + K. Correct.
- (iv) R25 (d) with J ≤ X; the bound is monotone in J. Correct.
- (v) Theorem LP: T ≤ (m − n + 1)(T_rel + 1) and T_rel ≤ (n + 1)(ρ + 1)n(n − 1) + ε. Substituting gives exactly the packet's bound.
  Multiplied out: f ≤ 2n²(X + 1), so (n + 1)·n(n − 1)·(2f + 2X + K + 1) = O(n⁵(1 + X) + n³K), and T = O(m·n⁵·(1 + X + K)). Correct.
- OX-1 (wording): f is R25's in-phase fallback count, over transitions with both ends in the phase. A phase-exit fallback adds ≤ 1
  (FB-2). T counts the same transitions. Write that once.
- 3.6 Note on the Reading (not signed): "X ≡ Z up to a factor n" holds in one direction, X ≤ (n − 1)(Z + 1) + Z (R23 LV′). That is the
  direction a bound on Z needs.

## 4. Data (DATA, not proof; docs/referee/scratch/oe_probe.py, sha1 6f6bd7c1…, written from the packet's definitions and P-N5-LP §0-§1;
own N5 trace u1_probe.trace asserted equal to n5.run on every game; every game asserted in 𝒞^1O, exactly one Odd vertex with out-degree > 1)
| run | games | phases / in-phase transitions | key numbers | failures |
| --- | --- | --- | --- | --- |
| library (`oe_probe.py lib`: every experiments/**/*.pg in 𝒞^1O with n ≤ 64; the same 234 files as c1o_list.py 64 today; the packet's 220 was the list at its run) | 234 | 285 / 5,603 | crossing-free σ̄(o) changes 436 (H1) + 11 (¬H1); at crossings 857; O_k > E_k 279, all at crossings (H1); level −1 crossing-free 130; non-tame 235, all crossings; max J 18, max X 84, max ε 18, max ρ 14, max f 33, max T 110; rises 437 = 288 fallback + 148 crossing + 1 wake (nowake_cex_n32) | 0 |
| rand 4000, n 8-24, seed 7101 | 4,000 | 1,361 / 1,617 | σ̄(o) changes 72 crossing-free; ties 12 | 0 |
| rand 1500, n 20-40, seed 7102 | 1,500 | 936 / 1,250 | 64 crossing-free; ties 14 | 0 |
| randb 4000, n 8-24, seed 7103 (extra edges into o, more ¬H1) | 4,000 | 1,515 / 1,831 | 63 crossing-free (12 ¬H1) | 0 |
| randb 1500, n 20-40, seed 7104 | 1,500 | 941 / 1,314 | 54 crossing-free; 1 non-tame (a crossing) | 0 |
- Checks with 0 failures in every run: ULOC, OE, CAP (λ(o) ≠ o), ST2 (x1's path avoids o), ST3 (H1: x0 ∈ F_k), ST4 (¬H1: empty path sets),
  TC (H1 constant off crossings), (i)-(v), rises classified, non-tame ⇒ crossing.
- Cross-check against the lane's own script: experiments/new/box32/oddlev.py on the same 234 files gives so_H1 436, so_nH1 11, so_H1_x 857,
  ODD_ABOVE_H1_x 279, J_H1_x 235, identical to my counts from a separate implementation.
- Named instances, re-run: jcl_zcl_cu_n48 (experiments/si/coarse/instances, sha1 53c69d2d…): n5.py 23 iterations, 1 fallback;
  check_sol2.py "zielonka(oink zlk) OK strategies verified"; my probe J 17 = X 17 in one phase (the packet's tight case, confirmed).
  nowake_cex_n32 (sha1 3a56e3fb…): 9 / 2, Oink OK; the library's one wake.
- Random data is thin on crossings (max X 3). The library carries the crossing evidence. The ¬H1 crossing-free cases are few (11 library,
  21 random). The ¬H1 branch rests on the proof.

## 5. Labels after this report (D18/L40)
- PROVED (L-NEW; signed by REFEREE (Opus 5.5, D15), second referee pending): Lemma U-loc on every game inside a phase. Lemma OE (with OE-1's
  wording) and Corollary OX (i)-(v) on 𝒞^1O.
- OPEN: X and K per phase. G-N5-TIME OPEN. Not a TARGET.md claim, not a step-4 pass: TARGET.md diff is empty (no statement of section 1 is
  touched).

## Fixes-file lines (one per gap)
- OE-1: §2 "In particular": replace "σ̄(o) makes no relevant change" with "σ̄(o) makes no relevant change of level ≠ ⊥ (O_k = ⊥)".
- OE-2: §2 step 1: cite CAP-1 as R-N5-FB §4.2 (λ(o) ≠ o, valid also when o lies on its honest cycle, case ¬H1); no text change needed.
- OE-3: §2 step 3: "decide the comparison" → "by (C1) and (C3), Ξ_{k+1}(x0) ◁ Ξ_{k+1}(x1)".
- OX-1: §3: "f and T count transitions with both ends in the phase (R25 FB-2)".
