# P-N5-SN fixes (box 33): the referees' repairs, written out
L-NEW successor 13 (Opus 5.5, D15/D18). Lead relay 03:59Z (read 04:01Z). Written 2026-10-25 04:01Z by date -u.
- Object: packet docs/new/P-N5-SN-box33.md, pinned at trunk 2c70ef6, sha1 340d4f298d8ee137b53ff76d7dd81de49f8fa542 (re-checked at this
  commit: unchanged). The packet is NOT edited; this file is its correction layer.
- Sources: REFEREE-2 docs/referee-2/R2-N5-SN.md (referee-2 ddbecafc; §A 91d95e8); REFEREE docs/referee/R-N5-SN.md (59a886d), §7. §C rows
  will follow in §8 when relayed.
- Rule: one line per item, then the repair written out. A line of my own is marked "L-NEW".

## 0. Verdicts and items (REFEREE-2; REFEREE pending)
| statement | REFEREE-2 (Opus 5.5, D15) | items |
| --- | --- | --- |
| §0 WM phase-key transfer | VALID (P-N5-Z §8 uses only τ_{k+1} = τ_k and the S4a optimum, statewise; R18 Lemma S (c)) | §1 |
| §1 Lemma OR, §2 TC-SPLIT, §3 R-STICK + SN-PREFIX, §4 H3H2, §5 LEAVE | SIGN | none |
| §6 Corollary ABS-COUNT | SIGN WITH GAPS G-SN-1 (a), (b) | §2 |
| §7 Lemma WK | SIGN, note N-SN-1 | §3 |
| §8 Lemma ABS-L | SIGN as CONDITIONAL; premises NL + CLS1 signed by both (R29 landed, cf6801e) | §4 |

## 1. WM on the (λ_Ξ, τ) phase
- Add to §0 "Phase keys": WM (R23 (g)) transfers: its proof (P-N5-Z §8) uses only τ_{k+1} = τ_k and that σ_{k+1} is the S4a optimum of
  an arena containing σ_k, statewise (R18 Lemma S (c)). (REFEREE-2.)

## 2. G-SN-1: ABS-COUNT's count
- (a) The proof's "it ends ≤ d_o − 1" needs H1 at the run's LAST state. After an H1 ε-transition, x1 = σ̄_{k+1}(o) may lie in R_{k+1}
  (¬H1 at k+1), and then all d_o exits can be in R. Counting only up to the last H1 ε-transition gives the same.
- (b) The per-phase line sums the runs and so misses ε-transitions AT fallback transitions (≤ f of them).
- Replace §6's statement by (PROVED; REFEREE-2's repair):
  - per fallback-free run: ε_{H1} ≤ d_o + REL_run, and ε_{H1} ≤ d_o − 1 + REL_run if the run's last state has H1;
  - per phase: ε_{H1} ≤ d_o(f + 1) + f + REL.
  Proof: N := #exits in R; each H1 ε-transition raises N by ≥ 1 net of the leaves at that transition (Lemma OR (a), (b)); N falls only by
  leaves (REL_run); 0 ≤ N ≤ d_o, and N ≤ d_o − 1 at an H1 state (σ̄(o) ∈ F). Fallback transitions add ≤ 1 ε-transition each.
  The sentence "every such leave happens in the run's c_w = c_θ prefix; if H1 holds there, at an (h) state via a relevant change of level
  ≥ r" stands (R-STICK, LEAVE).
- The packet's form ε_{H1} ≤ (d_o − 1) + REL_run per run (and (d_o − 1)(f + 1) + REL per phase) becomes a CONJECTURE. DATA (REFEREE-2):
  max excess 0 on the library (1,271 runs), 5,500 random games and three climbs aimed at it (30,400 runs, one seeded from
  exitr_cex_n48); 0 ε-transitions at fallbacks in every sample. The open scenario: d_o = 2, REL_run = 0, e1 absorbed, then e2 absorbed
  while e1 stays in R, ending ¬H1; no instance known.
- L-NEW: the error is mine (I used "σ̄(o) ∈ F" at the end state without H1 there). ABS-L's own count d_o − 1 is right, because its end
  state is in a scope run and has H1 (REFEREE-2 §8).

## 2b. L-NEW (added 04:09Z by date -u, Lead 04:04Z): the d_o − 1 form, proved except for ε-transitions with O_k = −1
**Lemma H1-DROP (PROVED, L-NEW succ. 13).** Inside a phase, if H1 holds at k and fails at k+1, then P(θ_k) = ∅.
Proof.
- c := c_θ = λ(o), fixed. Under ¬H1 at k+1, o lies on its H_{k+1}-cycle C, whose top is c; every y ∈ C reaches c along C, through vertices
  of rank ≤ rank c, so P(Ξ_{k+1}(y)) = ∅ (cycle node c). Under H1 at k, c's H_k-play is a cycle C_k avoiding o, all of rank ≤ rank c.
- Walk C from c: c = q_0 → q_1 → … → q_m = o (H_{k+1}-successors; q_t ≠ o for t < m). At k, c's H_k-play never reaches o, so some q_t
  (t < m) has a different H_k-successor: a DIVERGENCE. q_t is Even (every Odd vertex but o is forced). By R15 (d) its new successor is a
  gate target at k: Ξ_k(q_{t+1}) ▷ Ξ_k(s_t), s_t its old successor (also for t = 0, a cycle-node switch).
- Claim: at every divergence, P(Ξ_k(s_t)) = ∅ and P(Ξ_k(q_{t+1})) = ∅. Induction along the walk.
  - Old successor. First divergence: q_0 … q_t agree at k and k+1, so s_t lies on C_k after q_t; its path to c runs along C_k: P = ∅.
    Later divergence: q_{t′+1} … q_t (t′ the previous divergence) agree at k, so Ξ_k(q_{t′+1}) = (q_{t′+1} … q_t) ⊕ Ξ_k(s_t) ((P2), none of
    them is c); P(Ξ_k(q_{t′+1})) = ∅ by induction, and P only grows under ⊕, so P(Ξ_k(s_t)) = ∅.
  - New successor. Ξ_k(s_t) ◁ Ξ_k(q_{t+1}) (gate) ⊴ Ξ_{k+1}(q_{t+1}) (R15 (a)); all three have cycle node c (phase). The outer two have
    P = ∅, so lev(Ξ_k(s_t), Ξ_{k+1}(q_{t+1})) ≤ −1, and (C5) gives lev(Ξ_k(s_t), Ξ_k(q_{t+1})) ≤ −1: P(Ξ_k(q_{t+1})) = ∅.
- Take the LAST divergence q_j. After it H_k and H_{k+1} agree on q_{j+1} … q_m = o, so q_{j+1}'s H_k-path reaches o and
  Ξ_k(q_{j+1}) = (q_{j+1} … q_{m−1}) ⊕ θ_k ((P2); λ = c ≠ these vertices), whose path set contains P(θ_k). By the claim it is empty. □
**Corollary H1-KEEP (PROVED).** At an ε-transition k of a phase with H1 at k and O_k ≥ 0, H1 holds at k+1.
Proof. Suppose not. x1 := σ̄_{k+1}(o) lies on C, so P(Ξ_{k+1}(x1)) = ∅; x1's H_{k+1}-path avoids o (functional graph), its relevant changes
are Even ones ≤ E_k, and U-loc gives P(Ξ_k(x1)) ∩ V_{>E_k} = ∅. lev(Ξ_k(x0), Ξ_k(x1)) = O_k > E_k with O_k ≥ 0, so the top difference, of rank
O_k, lies in P(Ξ_k(x0)) ⊆ P(θ_k) (θ_k = o ⊕ Ξ_k(x0)). So P(θ_k) ≠ ∅, against H1-DROP. □
(O_k > E_k ≥ −1 forces O_k ≥ 0; so the only excluded case is O_k = −1 with E_k = ⊥: no relevant Even change at all.)
**Corollary ABS-COUNT′ (PROVED).** In a fallback-free run of a phase, let k* be the last H1 ε-transition. If O_{k*} ≥ 0, then
ε_{H1} ≤ (d_o − 1) + REL_run (the packet's form). Per phase: ε_{H1} ≤ (d_o − 1)(f + 1) + REL + f + ε⁽⁻¹⁾, where ε⁽⁻¹⁾ counts the runs whose last
H1 ε-transition has O = −1 (then that run gets d_o), and f covers ε-transitions at fallback transitions (G-SN-1 (b)).
Proof. Count N (exits in R) from the run's start to k*+1: each H1 ε-transition up to k* raises N by ≥ 1 net of leaves; N_{k*+1} ≤ d_o − 1
because H1 holds at k*+1 (H1-KEEP), so σ̄(o) ∈ F. □
- DATA (this session; library, L-RED's three instances, 3,000 random games n 8-32): 6 in-phase H1 → ¬H1 transitions, all with P(θ_k) = ∅;
  317 H1 ε-transitions, ALL with O_k ≥ 0 (none with O_k = −1). epsseg_cex_n48 matches REFEREE-2 §A: its run ends with H1.
- OPEN: ε-transitions with O_k = −1 (and E_k = ⊥), and ε-transitions at fallbacks. Neither occurs in any data.

## 3. N-SN-1: WK's "z is not fully optimal while a is available"
- Insert after that sentence: y ⊕ is strictly monotone between W(z) and W(a) because y lies on neither W-path: y ∈ R_{k′} = R_{k′+1}; at
  k′+1 σ(y) = z, so z's play cannot pass y before o (that would be an o-free cycle through y); after o, y can lie only on o's W-cycle,
  whose vertices have rank < c_w and so are in no path set; the same for a at k′; and a pass of z's k′-play through y with rank y > rank c_w
  would put y in P(W_{k′}(z)) but not in P(W_{k′+1}(z)), against W_{k′+1}(z) = W_{k′}(z). (REFEREE-2, avoiding the R24 TB-1 (b) trap.)
- DATA (REFEREE-2): all 52 wakes in its data change W at a or z, so WK's hypothesis is never met; it rests on the proof and on the
  choice-rule check (14,186 odd-mode S4a choices, 0 failures).

## 4. ABS-L
- Label: CONDITIONAL on NL (i), (ii) and CLS1's (A_j) chain; both now signed (RESULTS R29, cf6801e). With them, ABS-L is PROVED. DATA
  (REFEREE-2): 583 intervals with r_j > L, 0 θ-changes above L: vacuous in data.

## 5. Thin spots (REFEREE-2)
- 0 ¬H1 ε-transitions anywhere: Lemma OR (c)'s ¬H1 branch rests on the proof only. WK and ABS-L are vacuous in data (§3, §4).

## 7. REFEREE (docs/referee/R-N5-SN.md, referee 59a886d; added 04:14Z by date -u)
| statement | REFEREE (Opus 5.5, D15) | items |
| --- | --- | --- |
| OR, TC-SPLIT, R-STICK, SN-PREFIX, H3H2, WK, ABS-L (conditional, premises signed) | SIGNED | none |
| LEAVE | SIGNED WITH GAP SN-3 (wording) | below |
| ABS-COUNT | SIGNED WITH GAPS SN-1 (= G-SN-1 (a)), SN-2 (= G-SN-1 (b)) | §2, §2b |
- SN-1 = G-SN-1 (a): handled in §2 (proved form d_o + REL_run; d_o − 1 + REL_run when H1 holds at the run's end) and §2b (H1-KEEP closes
  it for O ≥ 0). REFEREE DATA: 0 transitions from an H1 ε-transition into a ¬H1 state, in all data including 5 climbs scoring exactly
  that event. REFEREE, like REFEREE-2, suggested proving "an H1 ε-transition keeps H1"; §2b does so for O_k ≥ 0.
- SN-2 = G-SN-1 (b): per phase + f for ε-transitions at fallback transitions (§2, §2b).
- SN-3 (LEAVE, wording): replace "(if r_s = ⊥ the claim is empty)" by: "if r_s = ⊥, a relevant change still exists: some Even p on q's old
  route before o switches; it precedes λ(q) = c_θ ∈ F_s on q's H_{s+1}-path, and λ(p) ≠ p." (REFEREE.)
- §C of both referees: §8.

## 8. §C joint gap map (REFEREE-2 §C.3, referee-2 80d2e45; REFEREE's §C to follow; added 04:19Z by date -u)
| row | REFEREE | REFEREE-2 | line (where here) |
| --- | --- | --- | --- |
| 1 | SN-1 | G-SN-1 (a) | §6: #H1-ε per fallback-free run ≤ d_o + REL_run (proved); ≤ (d_o − 1) + REL_run if H1 holds at the run's last state; the unconditional (d_o − 1) form is OPEN as signed (§2; L-NEW's §2b H1-KEEP, under addendum review, closes it when the run's last H1 ε-transition has O ≥ 0). An H1 ε-transition into a ¬H1 state was seen once, at a PHASE EXIT (epsseg_cex_n48, 25 → 26), which H1-KEEP (inside a phase) does not cover. ABS-COUNT is tight on epsseg_cex_n48 |
| 2 | SN-2 | G-SN-1 (b) | §6 per phase: + f for ε-transitions at fallback transitions; with row 1: d_o(f + 1) + REL + f |
| 3 | SN-3 | accepted | §5 LEAVE: "if r_s = ⊥, a relevant change still exists: some Even p on q's old route before o switches; it precedes λ(q) = c_θ ∈ F_s on q's H_{s+1}-path, and λ(p) ≠ p" (this file §7) |
| 4 | §7 wording remark | N-SN-1 | §7 WK: "y ⊕ is strictly monotone between W(z) and W(a): y ∈ R constant, so z's and a's plays reach o without passing y, and after o y can lie only on o's W-cycle, below c_w; the mode is set by c_w, the common W-cycle node of a and z" (this file §3, with this wording) |

## 6. Labels after REFEREE-2 (REFEREE pending)
- Signed by REFEREE-2: OR, TC-SPLIT, R-STICK, SN-PREFIX, H3H2, LEAVE, WK (with §3), ABS-COUNT in §2's repaired form, ABS-L (with R29).
- ABS-COUNT with d_o − 1 (the packet's form): PROVED by L-NEW in §2b for runs whose last H1 ε-transition has O ≥ 0 (unrefereed);
  CONJECTURE in the remaining case (O = −1; never seen) and for ε-transitions at fallbacks (never seen).

## 9. §C of both referees: the final joint map (REFEREE 3d49e0a, REFEREE-2 80d2e45; Lead relay 04:22Z; added 04:24Z by date -u)
No verdict differs. The rows of §8 stand, with these final readings:
- (1) SN-1 = G-SN-1 (a): per run ε_{H1} ≤ d_o + REL_run, ≤ (d_o − 1) + REL_run if the run's last state has H1; the unconditional (d_o − 1)
  form is a CONJECTURE as signed (tight on epsseg_cex_n48; N = d_o only at the phase exit 25 → 26). §2b (H1-KEEP) is under addendum review.
- (2) SN-2 = G-SN-1 (b): per phase ε_{H1} ≤ d_o(f + 1) + f + REL.
- (3) N-SN-1 (WK): y lies on neither W-path, so y ⊕ is strictly monotone (§3, §8 row 4); REFEREE's Bellman route via R24 G-TB-1 also
  closes it.
- (4) SN-3 (LEAVE, r_s = ⊥): the existence line of §7; REFEREE-2 reads the case as vacuous; true either way.
- (5) ABS-L: drop "CONDITIONAL"; its premises NL and CLS1 are signed and landed as RESULTS R29 (cf6801e). ABS-L is PROVED (L-NEW succ. 13;
  both referees).
Labels after both reports (D18/L40): PROVED (L-NEW successor 13; REFEREE and REFEREE-2, Opus 5.5, D15), pending CHECKER: Lemma OR,
TC-SPLIT, R-STICK, Corollary SN-PREFIX, Lemma H3H2, Lemma LEAVE (with §7), Corollary ABS-COUNT in the repaired form (2), Lemma WK (with
§3), Lemma ABS-L. CONJECTURE: ABS-COUNT with d_o − 1 unconditionally. Under review: §2b. OPEN: REL per phase; G-N5-TIME.
