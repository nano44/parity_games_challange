# Box 205 (D18): where a gate can flip — Lemma BETA-LOC, a per-state form of R122's BETA-ACYC (L-NEW successor 69, Opus)
Written 2026-11-11 (date -u in the commit); probes run 2026-11-09. Brief (Lead): «Research (D18): T_CYC polynomial at k = 1, i.e. bound
the max mover class height at k = 1 … A lemma (state exactly what it gives, polynomial or not, on which premises) or an exact
obstruction with its instance.»
Labels: PROVED (lane, unrefereed) / CONJECTURE / DATA (unit, set, scope, counter) / DEAD / READING. Nothing here is a TARGET.md claim.
G-N5-TIME stays OPEN. N5′-xi stays a CANDIDATE (D1). Setting and notation: IDEAL-CYC(G), every genome, as in P-N5-QN §1 (frozen l-new
e252182d, sha1 97254bd2; its premises are landed R-ids). Ξ_σ: the functional graph on the movers x → xt(x, σ(x)) (options whose Ξ-target
is X have no edge). Tools: experiments/new/box205/betaloc205.py; outputs box205/out/; check205.sh (check.sh «BOX 205 BETA-LOC»).

## 0. Answer
- No bound on the mover class height at k = 1 is proved. What is proved is a LOCAL rule for where Odd can leave the β-face, at every
  state of every genome. It extends RESULTS R122's BETA-ACYC (a global statement on Ξ-acyclic genomes) to one state of any genome.
- **Lemma BETA-LOC (PROVED, lane).** At a state s and a gate g = (x, j): if (i) the Ξ_σs-path from xt(g) ends at X (xt(g) = X included),
  and (ii) Λ_s(e_g) is not an odd-priority vertex other than K1, then σ̄_s(g) = β_g.
- **Corollary NOCYC-NOFLIP (PROVED, lane; uses P-N5-QN (k+1)-Λ's case list).** At a state s where Ξ_σs has no cycle, σ̄_s(g) = β_g at every
  gate. So no gate flips at a step t with Ξ_σ(t−1) and Ξ_σt both acyclic.
- **Corollary K1-BASIN (PROVED, lane), at k = 1.** At a state s, Ξ_σs has at most one cycle Z_s (P-N5-QN (k+1)-Λ). A gate g can be on its
  e-face only if (a) xt(g)'s Ξ_σs-path enters Z_s, or (b) Z_s's most relevant vertex c_s is odd and Λ_s(e_g) = c_s. If c_s is even, only (a).
- What it does NOT give: a bound on the number of flips or of class changes. On MWR(n) the one cycle and its (even) top are the same at
  every state (box 204 §3.1: Ccyc = 0) and one gate still flips 2n + 1 times; BETA-LOC only says that gate lies in the cycle's basin.
- DEAD (probe, §3): «a gate flips only at steps where xt(g)'s Ξ_σ-path enters a Ξ_σ cycle» (case (a) alone). Instance
  box205/inst/naive_k1_s71.json (k = 1, N 9; 3 flips, each by case (b): Λ(e_g) = β_(7,0), odd priority 37, before the step).

## 1. Lemma BETA-LOC (PROVED, lane)
Premises: [DEF] of P-N5-QN §1 (RESULTS R104's definitions only; readings D2 E-DOM, D3 core entry at K0); R118's order ⊴ ([VJ]: first the
reward of Λ, even priorities positive and increasing, odd negative and decreasing; then Π by the most relevant vertex of the symmetric
difference); [OPT] as landed in R123 (σ̄_s is optimal at every vertex at once: Ω_s(v) ⊴ the value of the play from v under σ_s and any
Odd positional strategy); R123 B-ONLY, LOC-GATE, LOC-K2.
Proof. Let s be fixed and write Ω = Ω_s, Λ = Λ_s, Π = Π_s. By (i), the movers x_1 = xt(g), x_2 = xt(x_1, σ_s(x_1)), …, x_m are distinct and
x_m's chosen option has Ξ-target X (m = 0 if xt(g) = X).
- The all-β play P0 from β_g: β_g, x_1, (x_1, σ_s(x_1)), β_(x_1, σ_s(x_1)), x_2, …, β_(x_m, σ_s(x_m)), u = K0, K3, K2, K1, K1, … . Its
  vertices before K0 are distinct, so the Odd positional strategy «β-face at the gates of P0, K1 at K2, σ̄_s elsewhere» produces it. Its
  value V0 has cycle node K1 (priority 5) and Π0 = the vertices of P0 more relevant than K1: β's, K0, K3. No e-vertex is in Π0.
  By [OPT], Ω(β_g) ⊴ V0.
- Ω(e_g) ▷ V0, by Λ(e_g):
  - Λ(e_g) = c_W (W-target c_W) or any other even vertex: its reward is positive, K1's is negative, so V0 ◁ Ω(e_g).
  - Λ(e_g) = K1: by B-ONLY, K1 is less relevant than e_g, and e_g is the first vertex of its play, so e_g ∈ Π(e_g) and e_g ∉ Π0.
    The most relevant vertex z of Π(e_g) Δ Π0 is e_g or more relevant. By E-DOM (D2) z is an e-vertex, c_W, K0 or K3. c_W is in no Π
    of a play with node K1. A play from a non-core vertex with node K1 enters the core at K0 (D3), then K0 → K3 (frozen), so K0, K3 lie
    in both Π's. Π0 has no e-vertex. So z is an e-vertex of Π(e_g): even, and Ω(e_g) ▷ V0 ([VJ]).
  - Λ(e_g) odd and ≠ K1: excluded by (ii).
- So Ω(β_g) ⊴ V0 ◁ Ω(e_g), and LOC-GATE (σ̄_s(g) is the face of strictly smaller value) gives σ̄_s(g) = β_g. ∎
- (ii) cannot be dropped: §3's control (premise (i) alone) fires 1,142 times, and the DEAD instance shows why — an odd Ξ_σ-cycle top
  reached through the W-target is better for Odd than K1.

## 2. Corollaries (PROVED, lane)
- NOCYC-NOFLIP. If Ξ_σs has no cycle, every Ξ_σs-path ends at X, so (i) holds at every gate. For (ii): Λ(e_g) is c_W when the W-target is
  c_W; otherwise, by the case list in the proof of P-N5-QN Lemma (k+1)-Λ (signed by both referees, not landed; uses only B-ONLY, LOC-K2,
  [DEF]), Λ(e_g) is K1 or the most relevant vertex of a Γ-cycle through a Ξ_σs-cycle — there is none. So BETA-LOC applies at every gate. ∎
  This is R122 BETA-ACYC's conclusion «Odd takes the β-face at every gate», now at each state with Ξ_σ acyclic, on any genome.
- K1-BASIN (k = 1). By (k+1)-Λ, Ξ_σs has at most k = 1 cycle Z_s, and Λ(e_g) ∈ {c_W, K1, c_s}, c_s the most relevant vertex of the Γ-cycle
  through Z_s. If σ̄_s(g) = e_g, BETA-LOC's premise fails: (i) fails, so xt(g)'s path does not end at X, i.e. it enters Z_s (the only cycle);
  or (ii) fails, so Λ(e_g) = c_s and c_s is odd. ∎
- READING (what remains at k = 1). Case (a) is a «cheapest exit» problem: Odd's plays from the basin of Z_s run into Z_s and, if c_s is
  even, leave it through the e-face of one gate. A flip is a change of exit or a basin change. MWR's 2n + 1 flips are exit changes driven
  by the W-target's clock (box 204 M1). Bounding exit changes needs the class height of the exits' W-targets: Theorem EQ's question again.

## 3. DATA (betaloc205.py; IDEAL-CYC from the genome's start, box203 gfc203.hist_ideal + box191 idealcyc.run, cap 20,000 states)
Counters (TOTALS): prem (unit: (gate, state) pairs meeting (i) and (ii)); bfail (unit: such pairs with σ̄_s(g) ≠ β_g; must be 0);
acyc_steps (unit: steps with Ξ_σ acyclic at t − 1 and t); nfail (unit: gate flips at such steps; must be 0); flips (unit: gate flips);
naive (unit: flips at which xt(g)'s Ξ_σ-path ends at X at both t − 1 and t: the DEAD naive form). Control BL_CTRL=1: premise (i) only.
| set (unit genomes) | prem | bfail | acyc_steps | nfail | flips | naive | output |
| --- | --- | --- | --- | --- | --- | --- | --- |
| records: MWR4/8/16_2, K1F21_n48, K1C16_n400, k1fail_202, B400_r32 (7) | 2,008 / 6,648 / 23,992 / 1,902 / 7,072 / 150 / 5,824 | 0 | 0 / 0 / 0 / 1 / 1 / 0 / 0 | 0 | 13 / 25 / 49 / 40 / 125 / 3 / 60 | 0 | out/betaloc205_records.out |
| k = 1, k1srch202.mk seed 71 (1,000) | 29,340 | 0 | 390 | 0 | 2,951 | 862 | out/betaloc205_k1_s71.out |
| k = 2, K1_MODE=2 seed 72 (500) | 10,920 | 0 | 50 | 0 | 2,448 | 481 | out/betaloc205_k2_s72.out |
| rand191 d 1-6, w 1-3, degree 2-3, seed 73 (1,000) | 30,022 | 0 | 416 | 0 | 3,135 | 864 | out/betaloc205_rand_s73.out |
| control BL_CTRL=1, k = 1 seed 71 (1,000) | 30,699 | **1,142** | 390 | 0 | 2,951 | 862 | out/betaloc205_k1_s71_ctrl.out |
- DEAD witness: inst/naive_k1_s71.json (sha1 in inst/SHA1SUMS), the first genome of the seed-71 k = 1 stream with naive > 0: N 9, k 1,
  T_CYC 3; gates (6, 1), (7, 1), (8, 1) are on the e-face at state 0 with Λ_0(e_g) = β_(7,0) (priority 37, odd) and xt's path ending at X,
  and flip to β at t = 1, where Λ_1(e_g) = K1. Case (b) of K1-BASIN, as predicted.
- check205.sh (re-run by check.sh, ~3 s): MWR4_2, k1fail_202, the DEAD witness; 100 k = 1 genomes (seed 75) and 100 rand191 (seed 76):
  bfail 0, nfail 0; control (seed 75) bfail 63; witness naive 3.

## 4. Status
- PROVED (lane, unrefereed): BETA-LOC, NOCYC-NOFLIP, K1-BASIN. Premises landed except (k+1)-Λ's case list (P-N5-QN, both referees SIGN).
- DEAD: the naive «flips only where xt's path enters the cycle», with the instance above.
- OPEN: T_CYC polynomial at k = 1 (= max mover class height polynomial at k = 1, box 204 Theorem EQ). BETA-LOC reduces where flips can
  happen; it does not count them.
