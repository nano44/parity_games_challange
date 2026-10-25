# Referee packet P-N5-SN: absorptions, the c_w = c_θ prefix, and who can leave R (box 33)
L-NEW successor 13 (Opus 5.5, D15/D18). Written 2026-10-25 03:33Z by date -u, at the Lead's request (03:28Z). Frozen at this commit:
corrections go in a fixes file, never here.
- Self-contained: definitions, statements, full proofs, the location of every dependency, the data and the scripts that produce it.
- Source text: docs/new/N5-K-box33.md §1, §5, §8, §9, §12, §13 (box 33 write-up). Where they differ, this packet governs.
- Status: L-NEW successor 13's proofs, unrefereed. All statements are about the candidate N5 on 𝒞^1O (exactly one Odd vertex o with
  out-degree > 1), inside a phase. Labels: PROVED (L-NEW succ. 13), CONDITIONAL, FALSE, DATA. Not a running-time bound, not a TARGET.md
  claim, not a step-4 pass. G-N5-TIME stays OPEN.
- Statements: §1 Lemma OR; §2 Lemma TC-SPLIT; §3 Lemma R-STICK and Corollary SN-PREFIX; §4 Lemma H3H2; §5 Lemma LEAVE; §6 Corollary
  ABS-COUNT; §7 Lemma WK; §8 Lemma ABS-L (CONDITIONAL on L-SI's Lemma NL, packet P-N5-CLS under review). §9 not to sign. §10 data.

## 0. Objects and dependencies (landed RESULTS unless said)
- N5, S4a / S4c, gates (improving edges), valuations x = (c, P, ℓ), Even's order ⊴, u ⊕ x, lev, COARSE_L, (C1)-(C4): as in RESULTS R25 /
  R27 (P-N5-LP §0-§1). Ξ_k = honest valuation of σ_k (play value in H_k, the (σ_k, σ̄_k)-graph); W_k = play value of (σ_k, τ_k).
  λ(v) = cycle node of Ξ(v). Keys: distinct cycle nodes compare by their reward alone, and the reward is injective
  (experiments/si/si.py l.42-44: pp = 2·rank + parity, rew = ±pp; VJ00's order on cycle nodes).
- PHASE: a run of transitions with λ_Ξ and τ constant (R27 / R28 setting). R_k := {o} ∪ {v : v's (σ_k, τ)-play reaches o} (o ∈ R here),
  F_k := V \ R_k, crossing: R_k ≠ R_{k+1}. θ := Ξ(o), w := W(o), c_θ := λ(o) (fixed in the phase), c_w(k) := the cycle node of w_k.
  H1: o lies on no honest cycle; H2: o lies on no W-cycle (⟺ τ(o) ∈ F); H3: c_θ = c_w; (h) := H1 ∧ H2 ∧ H3 (P-N5-NH §0).
  r_k := lev(θ_k, w_k) (finite under H3).
- Relevant changes, used level L_k, E_k (max relevant Even level), O_k (level of the relevant σ̄(o) change), ε-transition: O_k > E_k
  (R28 / P-N5-OE notation). An ABSORPTION is a transition at which σ̄(o) changes from x0 and x0 moves from F to R.
- On 𝒞^1O the H_k-graph and the (σ_k, τ)-graph agree everywhere except at o (every Odd vertex but o has one successor).
- Elementary facts (proved here; L-SI states them as P-N5-CLS §1):
  - (C5) a ◁ b ⊴ c ⇒ lev(a, b) ≤ lev(a, c). Proof: L := lev(a, c); if lev(a, b) > L, COARSE_L(b) ≠ COARSE_L(a) = COARSE_L(c) (C2), and
    (C1) gives COARSE_L(b) ▷_L COARSE_L(c) from b ▷ a while b ⊴ c gives ⊴_L; contradiction by (C3).
  - (C6) lev(a, c) ≤ max(lev(a, b), lev(b, c)), by (C2).
  - (C7) If π is disjoint from P(x), P(y) and from both cycle nodes, lev(π ⊕ x, π ⊕ y) = lev(x, y) with the same order: the same
    vertices are added to both path sets and both lengths grow by |π|.
- Signed results used: R15 (a) Ξ_k ⊴ Ξ_{k+1}; R19 (a) Lemma G: off R, Ξ = W (no (h) needed); under (h), on R, Ξ = π ⊕ θ and W = π ⊕ w,
  and the route order is the same at θ and at w; R21 (a) Lemma XW Ξ_k ⊴ W_k (VJ00 (11)); R22 (b) TC (i); R23 (g) Lemma WM: inside a
  phase, W_{k+1} ⊵ W_k at every transition that is not an S4c fallback; R24 Lemma R and Lemma TB (S4a's choice rule); R25 (e) CAP-1
  closure (σ̄(o) a FULL Ξ-minimiser over succ(o) when λ(o) ≠ o; R-N5-FB §4.2, R2-N5-FB §C.3); R28 Lemma U-loc and Lemma OE (with its
  step 2: σ̄_{k+1}(o)'s H_{k+1}-path avoids o, since H_{k+1} is functional).
- Phase keys: R19-R25 are signed under the key (λ_Ξ, λ_U, τ). Lemma G and XW are statewise; WM uses only τ_{k+1} = τ_k at an S4a step
  (σ_{k+1} is the optimum of an arena containing σ_k against the same τ); CAP-1 is statewise (R28 fixes N-OE-3 did the same transfer for
  FB, J1, TC (i)). Referees: please check WM's transfer.

## 1. Lemma OR (PROVED, L-NEW succ. 13): anatomy of an ε-transition
Statement. Let k → k+1 be a phase transition with O_k > E_k. Put c := λ(o) (≠ o), x0 := σ̄_k(o), x1 := σ̄_{k+1}(o), ℓ := O_k. Then
(a) x0's H_{k+1}-path to c visits o, hence x0 ∈ R_{k+1}; (b) under H1 at k, x0 ∈ F_k (k is an absorption); (c) lev(θ_k, θ_{k+1}) = ℓ and
θ_{k+1} ▷ θ_k.
Proof.
- (a) Suppose not. On 𝒞^1O the relevant changes on that path are Even ones, of level ≤ E_k; U-loc with L = E_k freezes COARSE_{E_k}(Ξ(x0))
  from k to k+1. x1's H_{k+1}-path avoids o (R28 OE step 2), so COARSE_{E_k}(Ξ(x1)) is frozen too. CAP-1 at k: Ξ_k(x0) ◁ Ξ_k(x1) at level
  ℓ > E_k, so by (C2), (C1) the COARSE_{E_k} values are strictly ordered; frozen, they stay so at k+1, and by (C1), (C3) Ξ_{k+1}(x0) ◁
  Ξ_{k+1}(x1), against CAP-1 at k+1. So the path visits o; the (σ_{k+1}, τ)-play of x0 follows it up to o: x0 ∈ R_{k+1}.
- (b) Under H1 x0's H_k-play, the tail of o's, never visits o (else o would lie on its own honest cycle). It equals x0's (σ_k, τ)-play,
  which therefore avoids o: x0 ∈ F_k.
- (c) θ_k = o ⊕ Ξ_k(x0), θ_{k+1} = o ⊕ Ξ_{k+1}(x1) ((P2) at o). Ξ_{k+1}(x1) has the COARSE_{E_k} of Ξ_k(x1), and level and direction of a
  difference above E_k are functions of COARSE_{E_k} values (R27 Lemma HI, second bullet), so lev(Ξ_k(x0), Ξ_{k+1}(x1)) = ℓ with
  Ξ_{k+1}(x1) ▷ Ξ_k(x0). o lies on neither path (x1's by (a)'s argument; x0's H_k-path to c: under H1 by (b); under ¬H1 x0 lies on o's
  honest cycle after o and reaches c before o), so (C7) gives the claim. □

## 2. Lemma TC-SPLIT (PROVED, L-NEW succ. 13)
Statement. At every phase transition with θ_{k+1} ≠ θ_k: lev(θ_k, θ_{k+1}) ≤ E_k, or k is an ε-transition and lev(θ_k, θ_{k+1}) = O_k.
Proof. λ(o) = o makes θ = (o, ∅, 0) constant, so λ(o) ≠ o. With x0, x1 as in §1, (C7) gives lev(θ_k, θ_{k+1}) = lev(Ξ_k(x0), Ξ_{k+1}(x1)).
U-loc on x1's H_{k+1}-path (avoids o; only Even relevant changes) gives lev(Ξ_k(x1), Ξ_{k+1}(x1)) ≤ E_k. If x0 = x1 this is the claim.
Otherwise lev(Ξ_k(x0), Ξ_k(x1)) = O_k and (C6) gives lev(θ_k, θ_{k+1}) ≤ max(O_k, E_k): ≤ E_k if O_k ≤ E_k; = O_k if O_k > E_k by §1 (c). □

## 3. Lemma R-STICK and Corollary SN-PREFIX (PROVED, L-NEW succ. 13)
For v ∈ R_k: λ(v) = c_θ and the W-cycle node of v is c_w(k) (v's (σ_k, τ)-play reaches o and the H_k-play agrees with it up to o; both
then follow o's play).
**Lemma R-STICK.** At an S4a transition s → s+1 of a phase, every v ∈ R_s whose W-cycle node differs from λ(v) lies in R_{s+1}. Hence if
c_w(s) ≠ c_θ then R_s ⊆ R_{s+1}.
Proof. Let v ∈ R_s ∩ F_{s+1}, c := λ(v), c′ := v's W-cycle node at s, c ≠ c′. Off R, Ξ = W (R19 (a)): W_{s+1}(v) = Ξ_{s+1}(v), cycle node c.
WM: W_{s+1}(v) ⊵ W_s(v); different cycle nodes, so rew(c) > rew(c′). XW: Ξ_s(v) ⊴ W_s(v), cycle nodes c and c′: rew(c) < rew(c′). □
**Corollary SN-PREFIX.** In a run of consecutive non-fallback transitions of a phase, the states with c_w = c_θ form a prefix of the run;
after the prefix R never loses a vertex until the run ends, so at most n − 1 crossings follow the prefix. Per phase, crossings ≤
(f + 1)(n − 1) + f + X_SN, X_SN := S4a crossings at states with c_w = c_θ.
Proof. WM makes w non-decreasing along the run, so rew(c_w) is non-decreasing; XW at o gives rew(c_w) ≥ rew(c_θ), with equality iff
c_w = c_θ. So equality holds on an initial part only. After it, R-STICK at each step; each crossing then adds a vertex. □

## 4. Lemma H3H2 (PROVED, L-NEW succ. 13)
Statement. If H1 and H3 hold at a state, then H2 holds, i.e. (h). So under H1, the regime c_w = c_θ of §3 is exactly (h), and R19 (a)'s
route-form statements apply there (both frames order R-vertices identically; an edge inside R is a gate iff it is W-improving).
Proof. Under H1, c_θ ∈ F: o's honest play does not return to o, so the honest cycle avoids o, and its vertices' (σ, τ)-plays (equal to
their honest plays, which avoid o) do not reach o. H3: o's W-play ends on the cycle of c_θ, which lies in F; so o is not on its W-cycle. □

## 5. Lemma LEAVE (PROVED, L-NEW succ. 13)
Statement. Let s → s+1 be an S4a transition of a phase with H1 at s, and q ∈ R_s \ {o} with q ∉ R_{s+1}. Then (h) holds at s, and q's
H_{s+1}-path before its cycle node carries a relevant change of level ≥ r_s; in particular L_s ≥ r_s.
Proof.
- q has W-cycle node c_w(s) and λ(q) = c_θ; by R-STICK c_w(s) = c_θ, i.e. H3; with H1, §4 gives (h).
- R19 (a) under (h): Ξ_s(q) = π_q ⊕ θ_s, W_s(q) = π_q ⊕ w_s, where π_q ⊆ R_s \ {o} avoids the paths of θ_s and w_s (they lie in F ∪ {o} by
  H1, H2) and the common cycle node; (C7): lev(Ξ_s(q), W_s(q)) = r_s, and Ξ_s(q) ◁ W_s(q) by XW when r_s ≠ ⊥ (if r_s = ⊥ the claim is empty).
- q ∈ F_{s+1}: W_{s+1}(q) = Ξ_{s+1}(q) (R19 (a)); WM: W_{s+1}(q) ⊵ W_s(q). So Ξ_s(q) ◁ W_s(q) ⊴ Ξ_{s+1}(q), and (C5) gives
  lev(Ξ_s(q), Ξ_{s+1}(q)) ≥ r_s.
- If every relevant change on q's H_{s+1}-path before its cycle node had level ≤ r_s − 1, U-loc with L = r_s − 1 (L = ⊥ if r_s = −1) would
  give lev(Ξ_s(q), Ξ_{s+1}(q)) ≤ r_s − 1. Contradiction. □
Remark. This is L-SI's Lemma NL key step (K*) (P-N5-CLS §5) without hypothesis (A), through U-loc.

## 6. Corollary ABS-COUNT (PROVED, L-NEW succ. 13)
Statement. In a run of consecutive non-fallback transitions of a phase, the ε-transitions with H1 number at most (d_o − 1) + REL_run,
where REL_run := the number of exits of o leaving R at transitions of the run. Every such leave happens in the run's c_w = c_θ prefix
(§3); if H1 holds there, at an (h) state via a relevant change of level ≥ r (§5). Per phase: ε_{H1} ≤ (d_o − 1)(f + 1) + REL.
Proof. Under H1 σ̄(o) ∈ F (§1 (b)'s argument at every state), so at most d_o − 1 exits are in R at any state. Each H1 ε-transition moves
the current minimiser exit from F to R (§1 (a), (b)), so the number of exits in R rises by ≥ 1; it falls only when exits leave R. It
starts ≥ 0 and ends ≤ d_o − 1. □

## 7. Lemma WK (PROVED, L-NEW succ. 13; from R24's choice rule)
Statement. Let y: a → z be a wake at k′ (R27 / P-N5-LP §3), with y not its own W-cycle node. If W_{k′+1} = W_{k′} at a and at z, then the
W-cycle node of y has even priority (S4a's BFS mode).
Proof. By P-N5-LP Lemma WAKE's proof (y, z) lies in the arenas H_{k′−1} and H_{k′}, and (y, a) does too (a = σ_{k′}(y)); both k′ − 1 → k′
and k′ → k′+1 are S4a steps. In the odd mode the choice at y is the smallest index among arena successors x fully optimal for the new
valuation W′ (W′(x) ⊕ y = W′(y)) (R24 Lemma R and TB step 4; SPEC S1 (iv) / FIX 4). At k′ − 1 the choice a gives W_{k′}(z) ◁ W_{k′}(a), or
equality with a < z. With the values at a and z unchanged at k′ + 1, z is then not fully optimal while a is available, or both are and
a < z: the choice is not z. The mode is the same at both steps (the cycle node of W(a) = W(z), or of the strictly better a). □
Consequence: in the odd mode every wake transition has a W-change on R (a, z ∈ R by Lemma WAKE).

## 8. Lemma ABS-L (CONDITIONAL on L-SI's Lemma NL and CLS1's proof, P-N5-CLS §5-§6, pinned 486107a, under review)
Statement. Let S be a scope run (P-N5-CLS §0), k0 < k fallbacks of S with none between, L := M_{k0}, and r_j > L for j ∈ [k0+1, k]. Then
every transition j ∈ [k0+1, k−1] with lev(θ_j, θ_{j+1}) > L is an absorption: σ̄(o) changes from x0, x0 ∈ F_j ∩ R_{j+1}, the level is
lev(Ξ_j(x0), Ξ_j(σ̄_{j+1}(o))) = O_j, and x0 ∈ R_t for t ∈ [j+1, k]. Hence at most d_o − 1 θ-changes above L in (k0, k).
Proof. (A_j) holds for L on [k0+1, k] (CLS1's proof). (h) at j and j+1 gives H1 and σ̄(o) ∈ F at both. If σ̄(o) does not change, x0 ∉
R_{j+1} and NL (i) freezes COARSE_L(Ξ(x0)), so lev(θ_j, θ_{j+1}) ≤ L by (C7). So it changes; x1 := σ̄_{j+1}(o) ∉ R_{j+1}, frozen above L by
NL (i). If x0 ∉ R_{j+1}, both are frozen above L and CAP-1 at j, j+1 forces lev(Ξ_j(x0), Ξ_j(x1)) ≤ L, so lev(θ_j, θ_{j+1}) ≤ L by (C6). So
x0 ∈ R_{j+1}; x0 ∈ F_j by H1; the level is as stated because Ξ(x1) is frozen above L. NL (ii) at each S4a step of [j+1, k−1] keeps x0 in
R. Distinct exits, one always in F. □

## 9. NOT TO SIGN: refuted forms, data findings, open items
- FALSE: EXIT-R (ε form) "an exit absorbed at an ε-transition stays in R until the next fallback", and ORX "each exit is x0 of at most one
  ε-transition per fallback-free run". experiments/red/so/instances/exitr_cex_n48.pg (L-RED box 37, l-red 9783ab7; sha1 7a663df2…; n 48;
  Lead re-run n5 22/1, Oink OK verified): ε-transition 4 absorbs exit 13; Even 13 leaves R at the S4a step 5 → 6 (an (h) state, r = 44,
  before any fallback of its scope run; Lemma LEAVE holds there); 13 is absorbed again at 9.
- FALSE: H-RE "re-absorbing the same exit inside a scope run needs r to drop" (b6_xl_n48, exit 28 at 70 and 88, r = 39 both).
- DATA FINDING: wakes per phase are Θ(n): experiments/new/box33/kchain.py K (n = 11K + 14) has K − 1 wakes in one phase (kchain4 / 10 /
  32: 3 / 9 / 31 wakes; Oink zlk OK, strategies verified; sha1 2be32f30… / 4af3726f… / 63c5b0dd…). N5 is fast there (K + 2 iterations).
- OPEN: REL (exit releases at S4a steps inside c_w = c_θ prefixes) per phase; the fallback ↔ absorption loop (R25 FB with ABS-COUNT).

## 10. Data (DATA, not proof; experiments/new/box33; every script asserts one Odd choice vertex; LIB = the 234 files of
experiments/new/box33/lib.txt, i.e. box32/c1o_list.py 64 without box33/out)
- orise2.py (Lemma OR at all O-rises): LIB 146 / 0 failures. TC-SPLIT and ABS-L coverage (scopecov.py): LIB 1,573 θ-changes / 0 (279 ε).
- sn.py (R-STICK, SN-PREFIX): LIB 894 runs, 2,473 S4a crossings in prefixes vs 61 after, 0 failures; random (--rand 2000 8 24 3302)
  172 vs 0.
- leave.py (Lemma LEAVE incl. "(h) at every H1 leave"): LIB 616 leaves, random (--rand 3000 8 32 3404) 561, exitr_cex_n48 1; 0 failures.
- wakes.py (Lemma WK): LIB 1 wake; climb products 5 (all BFS mode); K-chain 3 + 9 + 31 wakes (BFS mode, W changes at z).
- Random robustness (out/randcheck.txt, seeds 3401-3403, 4,800 games, n 8-48): R-STICK, SN-PREFIX, TC-SPLIT, Lemma OR 0 failures.
- Tool note: experiments/si/coarse/mono.py lev() uses 99 for ∞, wrong on n ≥ 100; box33/biglev.py patches it; all LIB data has n ≤ 64.
