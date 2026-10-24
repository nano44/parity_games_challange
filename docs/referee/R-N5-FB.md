# Referee report R-N5-FB: coarse super-solutions, the max gate level, and fallbacks per phase (L-SI box 7)

Referee: REFEREE (successor 5), Opus 5.5 (owner ruling D15, Lead reading L37). Packet P-N5-FB: the Lead's message of 2026-10-24 22:3xZ
(read 22:36Z). Pin: trunk claude/vibrant-johnson-nxvvxo 348393b (my HEAD after a merge of trunk). Object: docs/si/P-N5-FB-box7.md,
sha1 9ece9994a1251f904935048a605495cd325946e7, 235 lines (verified at the pin). L-SI successor 3, l-si 92f7985.
Context read: SPEC S1-S5 (FIX 2, FIX 3); experiments/new/n5.py; experiments/si/si.py evaluate; RESULTS R15, R21, R23; docs/si/N5-C-box5.md
§0, §1, §6.2 (the source of (JUMP-EQ)); VJ00 pp. 13-16 opened myself (below). docs/referee-2/ was NOT read for this packet.
Written 2026-10-24 22:42Z onward by date -u. Every verdict is labelled (Opus 5.5, D15). Labels (D18/L40): PROVED (by whom) / CONJECTURE /
OPEN / DATA / FALSE.

## Verdict
| item (brief order) | packet label | verdict (Opus 5.5, D15) |
|---|---|---|
| (1) §4 Theorem FB | PROVED (L-SI succ. 3) | SIGNED WITH GAPS: FB-1 (step (2)'s "M < ∞ by NOINF": NOINF covers only switched edges; one line closes it), FB-2 (the phase's transitions must have both ends in the phase; a phase-exit fallback, ≤ 1 per phase, is outside the count; 7 occur in the named set). Both closed |
| (1) §4 Corollary (W-lowerings, carries (C)) | PROVED | SIGNED (R23 (g) WM; a reversal is identified by its reversing transition) |
| (2) §2 Claim (T) | PROVED | SIGNED |
| (2) §2 COARSE-SI (a) under (NC), and its converse | PROVED | SIGNED WITH GAPS: ENG-1 (inherited, not new: (T) applies VJ00 Lemma 5.2 to SPEC's σ̄, which needs Θ_{σ_k σ̄_k} = Ξ_k; R15's engine point, DATA 0 failures here), V-1 (citation: Prog is on VJ00 p. 15, not p. 14), V-2 (the packet's (P3) quotes half of VJ00's clause 3; the omitted half is not used) |
| (2) §2 COARSE-SI (b) TAME | PROVED | SIGNED (ENG-1 as above) |
| (3) §3 Lemma MONO | PROVED | SIGNED |
| (3) §3 Lemma NOINF | PROVED | SIGNED ((P1) on every H-edge, at k and k+1, gives it in one line) |
| (4) §5 J1, OFF | PROVED | SIGNED |
| (4) §5 CAP | PROVED | SIGNED WITH GAP CAP-1: "b minimises Ξ_{k+1} over succ(o) (VJ00 p. 14)" holds for VJ00's σ̄, not always for SPEC's σ̄. At a cycle node, SPEC's σ̄ is the FIX-2 DFS choice, and it fails to be a minimiser in 925 of my observed cases (all at cycle nodes). Closed: if λ(o) ≠ o, SPEC's σ̄(o) is a minimiser (proof §4.2); if λ(o) = o, CAP holds without minimality (§4.2) |
| (5) §6 (JUMP-EQ) FALSE at x31_rx32, 53 → 54 | FALSE (DATA) | CONFIRMED, with my own trace and both readings of "carry" |
| (5) §6 A: L ≤ M_k at a tame carry | PROVED | SIGNED (immediate from the definition of tame). "L = M_k" stays DATA (201 / 201 here); "L ≥ M_k" OPEN |
No statement is NOT SIGNED. No counterexample to a PROVED item. (J-poly), (C) beyond FB, and G-N5-TIME stay OPEN.

## 1. §1 and §2: (C1)-(C4), Claim (T), COARSE-SI
### 1.1 (C1)-(C4)
- (C1): different cycle nodes, same verdict; same cycle node with top differing rank r > L, same top difference in the restriction to
  V_{>L}; otherwise the coarse values are equal. Correct. (C2) definition. (C3) correct. (C4): u enters the restricted path set iff
  rank u > rank c and rank u > L. Correct.
### 1.2 Claim (T)
- (i): (P1) for Ξ_k along H_k-edges, and (E) with L < ∞ keeps the cycle node, so λ_k is constant along the H′-play. Correct.
- (ii): the H′-cycle's top t has λ_k(t) = c by (i) and λ_k(t) = t by hypothesis. So the cycle is topped by c, and the prefix
  p_0..p_{s−1} consists of distinct vertices ≠ c. Θ_{H′}(p_i) = p_i ⊕ … ⊕ p_{s−1} ⊕ (c, ∅, 0) with set-valued ⊕ is right because the
  vertices are distinct. Correct.
- (iii): (P2) at p_i ≠ c holds in set form: p_i ∉ P(Ξ_k(succ_{H_k} p_i)), because a vertex on its own path prefix would lie on its cycle,
  and cycle vertices other than c are below c. Then (C4) + (E), and downward induction from (P3) at p_s = c. Correct.
- Only vertices of the play from v are used, which OFF relies on. Correct.
### 1.3 COARSE-SI (a), converse, (b)
- (a): (E) at switched vertices via R15 (d) + gate level ≤ L + (C2); at Odd vertices H′ = H_k. (T) gives COARSE_L(V) = COARSE_L(Ξ_k).
  Ξ_k ⊴ Ξ_{k+1} (R15 (a)) and Ξ_{k+1} = Ω_{σ_{k+1}} ⊴ Θ_{σ_{k+1} σ̄_k} = V (VJ00 (11), p. 16: Θ_{σσ̄} ⊴ Θ_{στ} for all τ). Then (C1) and
  (C3). Correct.
- Converse: V(t) has cycle node t (t tops its H′-cycle), Ξ_k(t) has λ_k(t) ≠ t; COARSE_L keeps the cycle node. Correct. (It is a
  statement about V, not about Ξ_{k+1}. The §5 Remark uses (a)'s contrapositive, which is right: non-tame ⇒ not (NC).)
- (b) TAME: M = ⊥ gives σ_{k+1} = σ_k (R15 (d)); otherwise (T) with H′ = H_{k+1}. Every H_{k+1}-cycle's top t has λ_{k+1}(t) = t
  (Lemma 5.2: the cycle node of a play is the max of its cycle), and λ_{k+1} = λ_k. Correct.
- ENG-1 (inherited). (T)'s (P1)-(P3) are Lemma 5.2 for Ξ_k and the strategy pair (σ_k, σ̄_k) with SPEC's σ̄ (si.py's counterstrategy).
  That needs Ξ_k = Θ_{σ_k σ̄_k}, i.e. the engine's valuation equals the play value of its own counterstrategy. This is the engine point
  of R15 (G-N1 in R-N5T, DATA there). DATA here: ENG (the play value of (σ, σ̄) at every vertex of every state) 0 failures on all runs.
  Not a new gap of this packet.
- V-1, V-2 (VJ00 citations, by page; VJ00 = BRICS RS-00-48, pdf sha256 485a12de…, page numbers are the printed footers):
  - definition of σ̄: p. 14 ✓ ("σ̄(v) = w, such that Ω_σ(w) ⊴ Ω_σ(u) for all u ∈ succ(v)").
  - Prog (P1)-(P3): p. 15 (pdf p. 17), not p. 14. VJ00's clause 3 reads "if Λ(v) = v then Π(v) ≅_{Λ(v)} Π(w) ⊕ v and Π(v) = (∅, 0)";
    the packet quotes only the second half. The first half is not used.
  - Lemma 5.2 and its proof (max≤(C) = ℓ): p. 15 ✓. (11) and "Θ_{σσ̄} ⊴ Θ_{στ} for all τ": p. 16 ✓.

## 2. §3 MONO and NOINF
- MONO: for (y, z) ∈ Iσ_{k+1}, u := σ_{k+1}(y): COARSE_M(Ξ_k u) = COARSE_M(Ξ_k σ_k y) (u = σ_k y or a gate target of level ≤ M). If
  COARSE_M(Ξ_k z) ▷_M COARSE_M(Ξ_k u), then Ξ_k z ▷ Ξ_k σ_k y with lev > M ((C1) contrapositive, (C2)), so (y, z) is a gate edge at k of
  level > M: impossible. Tameness transfers ⊴_M to k+1; Ξ_{k+1}(z) ▷ Ξ_{k+1}(u) gives ⊵_M; (C3) gives equality, so lev ≤ M at k+1. M = ⊥:
  Iσ depends only on σ, which is unchanged. Correct.
- NOINF: (P1) holds on every H-edge, cycle nodes included, so λ_k(σ_k y) = λ_k(y) = λ_{k+1}(y) = λ_{k+1}(z) = λ_k(z). The packet's
  two-case proof is this chain. Correct.

## 3. §4 Theorem FB and Corollary
- (1): σ_{i+1}(y) ∈ {σ_i(y)} ∪ Iσ_i(y) (R15 (d), S4a and S4c alike) gives Ξ_i(σ_{i+1} y) ⊵ Ξ_i(σ_i y) at level ≤ M. R15 (a) and
  tameness give Ξ_{i+1}(σ_{i+1} y) ⊵ Ξ_i(σ_{i+1} y) at level ≤ M. So COARSE_M(Ξ(σ y)) is constant and β(y) non-decreasing. Correct.
- (2): Even's fallback (R21 (c) FBL-N (i), τ constant); every vertex with a gate edge switches to its best target z* (S4c).
  - FB-1 (CLOSED). "M < ∞ by NOINF": NOINF covers the SWITCHED edge (y, z*), not every gate edge. Closure: if some gate edge (y, z′)
    had level ∞, then reward(λ(z′)) > reward(λ(σ_i y)), and Ξ_i(z*) ⊵ Ξ_i(z′) forces reward(λ(z*)) > reward(λ(σ_i y)), so the switched
    edge (y, z*) has level ∞, against NOINF.
  - Level of (y, z*) is M: if < M, COARSE_{M−1}(Ξ_i z*) = COARSE_{M−1}(Ξ_i σ_i y) ◁_{M−1} COARSE_{M−1}(Ξ_i z), so Ξ_i z* ◁ Ξ_i z. That
    contradicts the choice of z*. Then β_i(y) ◁ COARSE_{M−1}(Ξ_i z*) ⊴ COARSE_{M−1}(Ξ_{i+1} z*) = β_{i+1}(y). M = −1: full values, same
    chain. Correct.
- (3) M ≥ 0: COARSE_M constant leaves one bit (the rank-M vertex), so ≤ 1 strict rise per y. M = −1: only the length, in [0, n − 1],
  so ≤ n − 1 rises per y. Each fallback consumes a rise. Correct.
- (4) MONO: one block per value of M; ∞ and ⊥ blocks have no fallback (FB-1; Iσ = ∅). n blocks with ≤ n_E fallbacks + one with
  ≤ n_E(n − 1): n_E(2n − 1) per tame run; ≤ J + 1 tame runs + J non-tame transitions. Multiplied out: correct.
- FB-2 (wording; CLOSED). "Transitions of the phase" must be k → k+1 with both states in the phase. At a phase-exit transition λ or τ
  changes, NOINF and FBL-N (i) do not apply, and a fallback there is not covered. There is ≤ 1 such transition per phase, so the
  per-phase count is ≤ n_E(2n − 1)(J + 1) + J + 1 if the exit is included. DATA: 7 fallbacks at phase exits in the named set (the
  lane's 207 in-phase fallbacks exclude them, as do mine).
- Corollary: R23 (g) puts every in-phase W-decrease at a fallback; each '+−' reversal has one reversing transition. Correct.

## 4. §5 on 𝒞^1O: J1, OFF, CAP
### 4.1 J1, OFF
- J1: Odd u ≠ o are forced, so σ̄_{k+1}(u) = σ̄_k(u); if b = a or lev(Ξ_k a, Ξ_k b) ≤ M_k, TAME's hypothesis holds (λ constant in the
  phase), so the transition is tame. Correct (no minimality used).
- OFF: v ∉ R̄_{k+1} ⇒ v's H_{k+1}-play avoids o (on 𝒞^1O reaching o does not depend on Odd's earlier choices, all forced); (E) along it
  (Even: R15 (d) and gate level ≤ M_k; Odd: forced); its cycle's top t has λ_{k+1}(t) = t = λ_k(t). (T) with H′ = H_{k+1}, only the
  play from v. Correct.
### 4.2 CAP and CAP-1
- The proof uses "b minimises Ξ_{k+1} over succ(o)" and "the minimality of a" (VJ00 p. 14). VJ00 DEFINES σ̄ as a minimiser. SPEC's σ̄
  is si.py's counterstrategy: at a non-cycle-node it is the restricted-graph choice, and at a cycle node v it is the FIX-2 DFS choice
  (the first successor on a DFS cycle back to v through lower-rank vertices), which ignores path sets and lengths.
- DATA (fb_probe.py SBMIN): at Odd vertices that are their own cycle node, σ̄(v) is NOT a minimiser of Ξ over succ(v) in 55 / 588 +
  566 / 6,007 cases (random general games) and, with v = o, in 244 / 3,306 + 60 / 1,356 (random 𝒞^1O). At non-cycle-node Odd vertices it
  is always a minimiser (0 exceptions in 61,968). So the citation does not transfer when λ(o) = o.
- Closure, case λ(o) ≠ o (λ is constant in the phase, so this holds at k and k+1). Claim: SPEC's σ̄(v) minimises Ξ over succ(v) at every
  Odd v with λ(v) ≠ v. For u ∈ succ(v), let τ′ := σ̄[v → u].
  - If u's honest play avoids v, VJ00 (11) gives v ⊕ Ξ(σ̄ v) = Ξ(v) ⊴ Θ_{στ′}(v) = v ⊕ Ξ(u). v is in neither path set, so ⊕ v is
    strictly monotone and Ξ(σ̄ v) ⊴ Ξ(u).
  - If u's play passes v, the τ′-play from v closes a cycle v → u → … → v with top t. Ξ(u) = seg ⊕ Ξ(v), with D := (seg ∪ {v}) above c
    the extra path vertices relative to Ξ(σ̄ v).
    - D ≠ ∅ with even top: Ξ(u) ▷ Ξ(σ̄ v).
    - D ≠ ∅ with odd top t, or D = ∅ with c even: the cycle at t gives Odd a reward below reward(c), so Θ_{στ′}(v) ◁ Ξ(v), against (11).
      These cases do not occur.
    - D = ∅ with c odd: Ξ(u) is longer, which is better for Even, so Ξ(u) ▷ Ξ(σ̄ v).
  - So a and b are minimisers, and the packet's proof of CAP applies verbatim.
- Closure, case λ(o) = o. Let e ∈ succ(o) with lev(Ξ_k a, Ξ_k e) ≤ M_k < ∞. Then λ_k(e) = λ_k(a) = λ_k(o) = o (P1 on (o, a)), and
  λ_{k+1}(e) = λ_k(e) = o in the phase. So e's honest play at k+1 reaches o, and e ∈ R̄_{k+1}. CAP holds without minimality.
  (M_k = ∞: then lev ≤ ∞ holds for every exit, but a non-tame transition has M_k < ∞, since an ∞-level transition is tame trivially.)
- DATA: CAP 159 exit checks (named), 0 failures; J1 23 cases, 0 failures; OFF 40,704 vertex checks, 0 failures; no in-phase non-tame
  transition with λ(o) = o occurred anywhere (so case 2 is untested by data; it rests on the two-line proof).
- The Remark (non-tame ⇒ not (NC) ⇒ a new cycle through o): correct, by (a)'s contrapositive with L = M_k. DATA: 0 non-tame
  transitions with (NC), all runs.

## 5. §6: (JUMP-EQ) and A
- Statement checked against its source, docs/si/N5-C-box5.md §6.2 and §1: "carry" = a transition at which some W(v) decreases (§1); carry
  level = max over the carry's active leavers y of lev(Ξ_k y, Ξ_{k+1} y). The packet's restatement matches. jumpeq.py uses "evicting
  fallback" for carry; on this instance both readings pick the same transition.
- Re-run: x31_rx32.pg sha1 4fe9ec0ea39ea30df855c3738b8e0fdd08e621bc, exactly one Odd choice vertex, o = 0 (asserted); n5.py 55
  iterations / 3 fallbacks; check_sol2.py "zielonka(oink zlk) OK strategies verified".
- My own trace (u1_probe.trace = the n5.py loop, asserted equal to n5.run): the phase spans states 2..55. W-lowering transitions in it:
  24, 38, 51 (all fallbacks); the most recent before 53 is 51, leaver 21, L = 24; w is unchanged at 51, 52, 53.
  - 53 → 54: (NC) fails (bad cycle top 7), the old exit 24 ∉ R̄_53 enters R̄_54, σ̄(o) 24 → 31, θ rises (lev 25 > L = 24).
  - θ_53 = (36, −2146959360, −16), θ_54 = (36, −2113929216, −4), w_54 = (36, −1040187392, −4): θ_54 ≠ w_54. (h) holds at 54.
  - jumpeq.py on the file: the same case (k 53, L 24, M_k 24, θ-level 25, θ′ = w False) and a second case at 54 with θ′ = w.
  So (JUMP-EQ) is FALSE as stated. CONFIRMED.
- A: at a tame carry every Ξ(v) changes only at levels ≤ M_k (the definition of tame), and L is a max of such levels, so L ≤ M_k. SIGNED
  (it is scoped to tame carries). DATA: 201 in-phase evicting fallbacks in the named set, all tame, L = M_k at all 201. L ≥ M_k OPEN.

## 6. Data (DATA, not proof; docs/referee/scratch/fb_probe.py, written from the packet's §1 definitions, independent of
experiments/si/coarse/; own N5 trace asserted equal to n5.run on every game)
| run | games | key numbers | failures |
|---|---|---|---|
| named set (experiments/si/coarse/named.txt, 53 files, one Odd choice vertex asserted on each) | 53 | 65 phases; 207 in-phase fallbacks (+7 at phase exits); max J 3; max fallbacks in one block 25; (a) 1,473 NC / 366 non-NC (converse); TAME (b) 1,825; MONO 1,952; NOINF 3,706; J1 23; CAP 159; OFF 40,704 | 0 |
| random general games, n 4-12 (seed 801) / 4-14 (seed 812) | 300 / 3,000 | (a) 62 + 826 NC, 72 + 837 non-NC; TAME 169 + 1,852; MONO 236 + 2,648; NOINF 70 + 869; 5 + 75 in-phase fallbacks | 0 |
| random 𝒞^1O, n 6-24 (seed 811) / 24-40 (seed 813) | 3,000 / 1,000 | 941 / 667 phases; 136 / 80 in-phase fallbacks; (a) 1,401 / 999 NC; OFF 15,808 / 26,188; no in-phase non-tame (J = 0) | 0 |
| ENG (Θ_{σσ̄} = Ξ at every vertex, every state) | all of the above | — | 0 |
| SBMIN (σ̄ minimises Ξ over succ) | all of the above | non-cycle-node Odd vertices 61,968 checks | 0 exceptions; cycle nodes: 925 non-minimiser cases (CAP-1) |
- My named-set counts reproduce the packet's §7: 207 in-phase fallbacks, max 25 per block, max J 3, 23 non-tame in phase (J1), 159 CAP
  checks, 40,704 OFF checks, 201 evicting fallbacks with L = M_k.
- Honest limit: J ≤ 3 in all data here; random 𝒞^1O runs have J = 0. FB's (J + 1) factor and CAP's λ(o) = o case are unexercised.

## Signature
REFEREE (successor 5), Opus 5.5 (D15), 2026-10-24: Theorem FB SIGNED WITH GAPS FB-1, FB-2 (closed); Corollary SIGNED; Claim (T) SIGNED;
COARSE-SI (a) + converse SIGNED WITH GAPS ENG-1 (inherited), V-1, V-2 (citations); TAME SIGNED; MONO SIGNED; NOINF SIGNED; J1, OFF SIGNED;
CAP SIGNED WITH GAP CAP-1 (closed); (JUMP-EQ) FALSE CONFIRMED; A (L ≤ M_k at tame carries) SIGNED. Labels after two signatures
(D18/L40): these become PROVED (L-SI succ. 3; REFEREE, and REFEREE-2 if it signs), §2-§4 on all parity games, §5 on 𝒞^1O. Theorem FB
bounds fallbacks per phase by poly(n)·(J + 1); (J-poly), (C), G-N5-TIME OPEN.
