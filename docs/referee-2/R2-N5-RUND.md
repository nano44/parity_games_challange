# R2-N5-RUND: REFEREE-2 report on packet P-N5-RUND (offsets, aligned blocks, per-edge schedule of Lemma P in a fallback-free in-phase run)
Referee: REFEREE-2 successor 16 (session_01R1scbTA9MiKutHRhRdi3zh), Opus 5.5 (D15, L37). Written 2026-10-26 10:05Z (date -u).
Object: docs/si/P-N5-RUND-box17.md, sha1 71e198f359cbb321fc0c15e6c28676d4dd046d52 (`git show 94910ed3:docs/si/P-N5-RUND-box17.md | sha1sum`;
the same blob at l-si 762b7243), pinned at trunk 94910ed3, frozen. Authors L-SI successors 12 (§2-§4) and 13 (§5, §6).
Independence: written before opening any REFEREE file on RUND. `git fetch origin claude/referee` and
`git ls-tree --name-only -r origin/claude/referee docs/referee/ | grep -ic rund` gave 0 at 09:3xZ and at the push of this report (count in
the commit message). The lane's checkers (experiments/si/rund/*.py) were NOT run or imported; sched.py was READ after my data, only to explain
a data difference (§5.3).
Checker: docs/referee-2/R2-N5-RUND/rund_check.py (own), on succ. 13's SPEC loop (R2-N5-DUAL/dual_check.Runner, on si.py = SPEC S1's own
implementation, read-only). Ξ and W are computed by me as PLAY values from the definitions, not taken from the engine (§5).
Scope (D1): nothing here bounds N5's running time on any class. Not a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Verdicts (per packet §0)
| item | verdict | premises beyond the packet's own text (§1) |
| --- | --- | --- |
| §2 Lemma CR-REL | SIGN | P2 (via P^c_L's Case B and (MON)) |
| §3 Lemma OFFSET (a) | SIGN | P1 (s^Ξ via (SG)), P2 (s^W via WM-G) |
| §3 Lemma OFFSET (b), (c) | SIGN | none beyond (h3_D) and the cited R55 (a), R62 (b), (c) proof |
| §3 Lemma MERGE-B | SIGN | none (definition) |
| §3 Theorem TWIN-GAP (i), (ii), (iii), Corollary | SIGN (reading N-RUND-4 of (ii)) | P1, P2 (OFFSET (a), FRZ-U_H3) |
| §4 Lemma PIECE_D (a) | SIGN | P2 ("switch-best" = an arena optimum) |
| §4 Lemma PIECE_D (b) | SIGN (N-RUND-3) | P2; R17 (c) for every pointwise-optimal choice |
| §4 Corollary SPLIT-RED | SIGN (N-RUND-3: the left side counts transitions) | P2 |
| §5 Lemma P^c_sch | SIGN | P2 ((F1) on H_{k−1} in Case B; (MON)) |
| §5 Corollary FRZ-SCH | SIGN | P2 |
| §5 Corollary CHARGE (hypothesis (ii) only) | SIGN | P2 |
| §6 Fact FZ | SIGN | P1 (named by the packet) |
| §6 Lemma UNF | SIGN | none (S4a's arena edges only) |
| §6 Corollary CHARGE-U (hypothesis (ii) only) | SIGN (N-RUND-5) | P2 |
No gap. Notes N-RUND-1..7 (§3). Not reviewed, as instructed: §7, §8, §9 and every READING. Side finding on §7 (not signed, not a gap of
a signed item): CONJECTURE UF-ONCE is FALSE (§4, witness so_th_n32 from its S3 start).

P1, P2 = the two forms of the standing SPEC premise 1E-N3 (RESULTS R57 (b), "S1's procedure realises an optimal σ̄"; R62's landing note:
"WM-G rests on the standing SPEC premise that S1 returns the arena optimum, as 1E-N3 in RESULTS R57"):
- P1: S1's σ̄_k is Odd's pointwise-optimal strategy in the one-player game G_{σ_k} (so SPEC's Ξ_k is VJ00's Ω_{σ_k}, (VJ)).
- P2: S4a's σ_{k+1} is Even's pointwise optimum in the arena H_k of G_τ (S1's procedure run on the dual of H_k).

## 1. Premises, complete list
Definitions: SPEC S1 (valuation, order, rank, path set), S2 (Iσ), S4a (arena H_k, A(v) = {σ(v)} ∪ Iσ(v)), S4c (to define "no fallback");
phase = maximal run with (λ_Ξ, τ) constant (R38 (a) KEY; τ constant on a phase, so G_τ is one fixed one-player game on S).
Landed results used (all signed on every game, or game-general per both R55 referees' reading of their proofs):
- R55 (a) G_D (a) (OFFSET (a), (b); FZ's last step);
- R62 (b) TC-CLASS (OFFSET (a), (b)); R62 (c) C2-H3 and its proof's factorisation P_F(v) = (π_v ∩ V_{>c}) ⊔ P_F(u) (OFFSET (b));
- R62 (d) WM-G = (MON) (OFFSET (a), P^c_sch, FRZ-SCH); R62 (e) P^c_L's proof (CR-REL, P^c_sch) and CR-D's proof; R62 (f) FRZ-U_H3 (TWIN-GAP (ii));
  P-N5-H3 §6's proof that λ_Ξ = λ_W on S (OFFSET (a), SPLIT-RED);
- (SG) pointwise: Ξ_{k+1} ⊵ Ξ_k at every N5 transition. Its signed basis is R15 (a) Lemma A + R15 (d), applied to SPEC's Ξ through (VJ)
  (R57 (a) with P-N5-1E §2, under P1), exactly as R60's premise line lists it; the packet's pointer R19 (d) is the secondary one (N-RUND-2);
- R17 (a) (V1), (V2), (F1); R17 (c) Theorem PH and (d) "for every pointwise-optimal choice" (PIECE_D (b)), one-player statements applied to
  G_τ and its arenas (one-player on every game);
- R25 setting: lev, COARSE_L, (C1)-(C4), (Cstrict) := (C1) + (C3) (P-N5-H3 §1); w injective on sets (P-N5-FB-box7 §1 (C3), opened).
Hypotheses as stated per item: S one phase, no fallback; (h3_D) at every state (§3, SPLIT-RED); (ii) λ_W constant (§2, §4 (b), §5, §6);
(i_rel) (§2); alignment (§4); a clean schedule (§5). Standing: P1, P2 (§0).

## 2. Proof check, item by item (my reading, line by line against P-N5-H3 §4-§6 at sha1 680e4528, opened)
- CR-REL. In P^c_L's proof (H3 §5) the IH is used only on r′ (Cases A1, B1 first bullet); (i) appears exactly once, first line of Case B,
  to turn Ω^c_k(z) ≻ Ω^c_k(a) into Ξ_k(z) ▷ Ξ_k(σ_k x); B1 second bullet and B2 end in contradictions with (ii) via (F1) on H_k (P2); A1,
  A2 use (V1), (V2c), (MON), IH. CR-D's proof reads only P^c_L, (ii), (MON), (C3). (i_rel) is exactly the Case-B step (z ≠ a there, as
  their coarse values differ). (i) ⇒ (i_rel) by (C2) and (Cstrict). CORRECT.
- OFFSET (a). λ_Ξ = λ_W: F_D by R55 (a); R_D by TC-CLASS + (h3_D); constant because λ_Ξ is a phase invariant. Monotone scores: with the
  cycle node fixed, S1's order compares reward (equal), then w of the path set, so Ξ_{k+1}(v) ⊵ Ξ_k(v) forces w(P_{k+1}) ≥ w(P_k); same for
  W by WM-G. CORRECT (premises P1 for (SG), P2 for WM-G).
- OFFSET (b). c ∈ π_v: the W-play reaches c before u(v), the honest play follows the same prefix (σ̄ = τ off D_k) and has the same cycle
  node c (part (a)), so the two path sets (vertices before the first visit of c, ranked above c) coincide. c ∉ π_v: C2-H3's factorisation,
  whose disjointness is the lasso fact (the prefix of v's play before its first visit of c repeats no vertex, so u's prefix before c
  misses π_v); w is additive over disjoint unions. CORRECT.
- OFFSET (c). Expansion of w over P_W(u) Δ P_Ξ(u); top = lev(Ξ_k(u), W_k(u)) under (h3_D) (same cycle node), ≤ M_D ≤ L*; all ranks ≥ ℓ_S
  by definition of ℓ_S; Δ_k(v) ∈ {0, δ_k(u(v))} by (b). CORRECT.
- MERGE-B. Δ(y) = Δ(z) ⇔ s^W(y) − s^W(z) = s^Ξ(y) − s^Ξ(z); with a common cycle node the path-set comparison is the sign of the w
  difference. CORRECT.
- TWIN-GAP. (i) is Δ's definition plus OFFSET (a). (ii) from k_0 + n − 1 on, FRZ-U_H3 at L* (L* ≥ max_S M_D, L* ≥ −1) keeps
  COARSE_{L*}(W) = COARSE_{L*}(Ξ) constant, i.e. cycle node and P ∩ V_{>L*} constant in both frames; so each monotone score moves inside
  {w(H ∪ X) : X ⊆ ranks ≤ L*}, a range of width Σ_{r ≤ L*} 2^r = 2^{L*+1} − 1; each change consumes |d| ≥ 2^{ℓ_S} of the sum's rise
  ≤ 2^{L*+2} − 2. (iii) n − 1 sources before k_0 + n − 1. (2^{L*+2} − 2)/2^{ℓ_S} < 2^{B+1}. L* = −1 ⇒ U_S = ∅ (no rank ≤ −1). CORRECT
  in the reading N-RUND-4.
- PIECE_D (a). In G_τ every Odd vertex has out-degree 1, so S1's valuation of σ_k there is the play value W_k and G_τ's improving set is
  {(x, z) : W_k(z) ▷ W_k(σ_k x)}; alignment equates it with Iσ_k; then H_k is R17's switch-best arena on G_τ. CORRECT (P2).
- PIECE_D (b). B is a prefix of the switch-best run on G_τ from B's first state (every step an arena optimum, R17 (d) allows SPEC's choice);
  λ_W constant on B's states means no vertex changes its cycle node, so B lies in that run's first λ-phase; R17 (c): fewer than n + m_τ ≤ n + m
  steps (N-RUND-3). CORRECT.
- SPLIT-RED. Blocks of aligned-source transitions are separated by the N_split other transitions: ≤ N_split + 1 blocks, each ≤ n + m − 1.
  λ_W constant from (h3_D) (H3 §6). CORRECT (N-RUND-3).
- P^c_sch. Induction on m for all k: base needs k ≥ k_0 and (ii); the step uses P^c_L's step from k − 1 to k verbatim, with the IH only on
  r′ at k − 1, whose schedule is clean ((k − 1) − (m − 1) = k − m ≥ k_0; edge q′ of r′ = edge q′ + 1 of r, looked at at (k − 1) − 1 − q′ in
  both); Case B's one use of (i) is replaced by "edge 0 not forbidden at k − 1" (z ≠ a). k − 1 ≥ k_0 since m ≥ 1. CORRECT.
- FRZ-SCH. Ω_t(x) = value(r_t) (r_t is the simple W-play prefix to the W-cycle node λ_W(x), a W-cycle node at every state by (ii)); P^c_sch
  at s, (MON) on [s, t], (C3). CORRECT.
- CHARGE. Contrapositive of FRZ-SCH on [s − 1, s]; in the charged case s − 2 − q ≥ s − 1 − m ≥ k_0; window ⇒ s ≤ k_0 + m ≤ k_0 + n − 1,
  ≤ n − 1 values of s. The K_F consequence: s ∈ [f + 2, f + n] for a fixed charged state f (q ≤ n − 2). CORRECT.
- FZ. (F1) in G_{σ_k} (P1): Ξ_k ⊴ W_k pointwise; Ξ_k(z) ⊴ Ξ_k(a) (not ▷, ⊴ total) ⊴ W_k(a) ◁ W_k(z) ((Cstrict)); z ∈ F_D would give
  Ξ_k(z) = W_k(z) (R55 (a)). CORRECT.
- UNF. σ_s(r_q) = r_{q+1} (r is the W-play at s), σ_f(r_q) ≠ r_{q+1} (forbidden at f needs z ≠ a); k′ := the last k ∈ [f, s − 1] with
  σ_k(r_q) ≠ r_{q+1}; S4a's arena gives e ∈ Iσ_{k′}, hence Ξ_{k′}(r_{q+1}) ▷ Ξ_{k′}(σ_{k′} r_q), so e is not forbidden at k′ and k′ ≠ f;
  s − 1 − f = q + 1 ≤ m ≤ n − 1. Uses only that S4a picks inside A(v) (no premise). CORRECT.
- CHARGE-U. Each charged s is served by an event (k′, e) ∈ U(S) with s ∈ [k′ + 1, k′ + n − 1]: ≤ n − 1 values of s per event. CORRECT
  (N-RUND-5).

## 3. Notes (no gap)
- N-RUND-1 (premises). §0 names the standing SPEC premise only for FZ. §2-§5 also rest on it, in form P2, through WM-G = (MON) (R62's
  landing note) and through (F1) on the arena H_{k−1} in P^c_L's / P^c_sch's Case B (B1, B2) and PIECE_D's "switch-best"; OFFSET (a) rests
  on P1 through (SG) (R15 (a) applies to SPEC's Ξ only through (VJ), R60's premise line). Landed statements R62 / R57 already carry the
  premise, so this is a landing note: the landing text should say "under the standing SPEC premise 1E-N3" for §2-§6, not only for FZ.
  Premise data (DATA, not proof; brute force over all strategies when ≤ 4,096): P1 at 31,001 states, P2 at 24,910 S4a transitions, 0
  failures; and Ξ (engine) = the (σ, σ̄)-play value at every one of 90,290 states (§5).
- N-RUND-2 (R19 (d) quote). The packet's §1 line "RESULTS R19 (d), the (SG) step: "Ξ_{L+1}(z) ⊵ Ξ_L(z) at any N5 transition (on all
  games)"" is NOT a verbatim quote: R19 (d) reads "(SG) — at any N5 transition a switched Even vertex y with λ_L(y) ≠ y gains strictly (on
  all games, not only 𝒞^1O) (Ξ_{L+1}(z) ⊵ Ξ_L(z) ▷ Ξ_L(σ_L y), then one strict (V2))", where z is y's new successor and "on all games" is
  said of the strict gain. The pointwise statement for every z that OFFSET (a) needs is R15 (a) Lemma A + R15 (d) via (VJ) (under P1), as
  R60 lists it. The content is right; the citation should name R15 (a), (d) and (VJ), and either quote R19 (d) exactly or drop the quotes.
  The other quotes are verbatim (mechanical substring check against RESULTS at the pin, "…" as a gap): R62 setting, R62 (d), R62 (e), R62 (f),
  R55 (a), R17 (a) (F1). D1 verbatim (DECISIONS.md:7). The Lead's 08:32Z words in the header were not checked (not a RESULTS quote).
- N-RUND-3 (counts). |S| in SPLIT-RED is the number of transitions of S (k_1 − k_0), the count the proof bounds. PIECE_D (b)'s m: R17's m
  is the edge count of the one-player game G_τ (m_τ ≤ m, Odd vertices keep one edge), so "fewer than n + m" holds a fortiori.
- N-RUND-4 (TWIN-GAP (ii) reading). "At states ≥ k_0 + n − 1" = transitions whose SOURCE state is ≥ k_0 + n − 1 (both endpoints then lie
  in FRZ-U_H3's frozen range); (iii) adds the n − 1 transitions with sources k_0, …, k_0 + n − 2. With that reading the proof is complete.
- N-RUND-5 (U depends on L). "Forbidden" is defined at a level L, so U(S) is U_L(S). Forbidden at L ⇒ forbidden at −1 (COARSE_L(W(z)) ≻_L
  COARSE_L(W(a)) ⇒ W(z) ▷ W(a) by (Cstrict), so COARSE_{−1}(W(z)) ⪰ COARSE_{−1}(W(a)) by (C1), and they differ by (C2)); hence U_L(S) ⊆ U_{−1}(S)
  and CHARGE-U with U_{−1}(S) bounds every level. Checked in data at every level L tested.
- N-RUND-6 (thin spots in data; the proofs do not need them). (a) TWIN-GAP (ii) is far from tight: the largest tail rise of a score is 38 %
  of 2^{L*+1} − 1 (pftheta_cex_n32) and the largest tail count of offset changes is 2 against bounds ≥ 511; mutations tg4 (bound / 4) and tgr (rise cap one
  level lower) do NOT bite. (b) PIECE_D (b): the longest aligned block is 55 transitions (x32_rand64, n = 64, n + m_τ = 300); mutation piece
  (< n) does not bite. (c) CR-REL's freeze is exercised non-vacuously on 12 sub-runs only (sub-runs of ≥ n + 1 states with no forbidden edge: packet
  instances 4, climbs 2, lib41 3, 𝒞^1O set 3, overlapping).
- N-RUND-7 (§4 remarks, not in the sign list but checked). "A forbidden edge at L = −1 is a split edge" holds by (Cstrict). The CORRECTION
  (withdrawn READING) is consistent with FZ; nothing signed used it.

## 4. Side finding on §7 (NOT to sign): CONJECTURE UF-ONCE is FALSE
UF-ONCE: "in every run S, each Even vertex makes at most one unforbid-switch". Witness: experiments/red/so/instances/so_th_n32.pg (sha1
ae9126ad1bf963114bdd56b6e50c8c1cc571779e; n = 32, one Odd choice vertex, so 𝒞^1O), N5 from its S3 start (n5.py agrees: 36 iterations,
0 fallbacks). Run S = states 1..22 (21 transitions): one phase, no fallback, λ_W constant, (h3_D) at every state. At L = −1, Even vertex 24
(succ {0, 21}) makes three unforbid-switches into e = (24, 21): at 4 → 5 (e forbidden at 1, 2, 3), 15 → 16 (forbidden again at 12, 13, 14,
after σ(24) went back to 0 at 8 → 9), 21 → 22 (σ(24) back to 0 at 17 → 18; e forbidden at 12-14, inside [k′ − n + 1, k′ − 1]). Even
counting only switches that follow a fresh forbidden stretch, 4 → 5 and 15 → 16 are two. Forbidden-ness at 12 checked by the SPEC Q1
symmetric-difference rule as well: W(21), W(0) share cycle node 5, top differing rank 24 favours W(21); Ξ(21) vs Ξ(0) top differing rank 30
does not favour Ξ(21). Log: R2-N5-RUND/logs/uf_once_so_th_n32.txt (uf_once.py). Scan (uf_scan.py, runs cut at λ_W changes): 𝒞^1O set
(my 503 files × 2 starts) 15 of 1,006 (game, start) pairs fail; lib41 minus referee games × 3 starts (S3 + 2 random, seed 1617): 19 of
1,230 fail, 18 of 753 on one-Odd-choice games and 1 of 450 on games with ≥ 2 Odd choice vertices: experiments/red/n5inj/instances/
phase2_pk48.pg (sha1 83dead9b…, n = 48, two Odd choice vertices) from R2-N5-RUND/instances/phase2_pk48_s1.start (sha1 36dc43e7…),
run S = states 15..27 (λ_W constant, (h3_D) throughout), Even 44 switches into (44, 11) at 16 → 17 (forbidden at 15) and into (44, 19) at
25 → 26 (forbidden at 19-24): two unforbid-switches into two different edges (logs/uf_once_phase2_pk48_s1.txt). CHARGE-U itself holds on
all of them (0 violations), and |U_{−1}(S)| ≤ n_E holds in all data (max 23, so_j19_n48, n_E = 41).
Why the lane saw 0: its §9 lib41 / lib2o rows come from `sched.py --list FILE 2`, whose KMIN = 2 skips games with fewer than two Odd choice
vertices (sched.py l. 163, 168 at the pin, read after my data), so 𝒞^1O games are absent from its data; 33 of my 34 failures are on
𝒞^1O, and the one multi-Odd failure is from a random start pair (the lane used 4 random pairs of its own).
Effect: §7's route "|U(S)| ≤ n_E via UF-ONCE" needs another argument; the signed items are unaffected.

## 5. Data (DATA, not proof)
### 5.1 What the checker does
Per N5 run (succ. 13's Runner, SPEC S1-S5 + FIX 1-4): per state, own play values Ξ (of (σ, σ̄), σ̄ as returned by S1) and W (of (σ, τ)),
D_k, u(v), π_v, (h3_D), M_D, Iσ (own, compared with the engine's: 0 mismatches), split and forbidden edges. Runs: maximal fallback-free
in-phase runs, cut into h3-runs ((h3_D) throughout: §3, SPLIT-RED; TWIN-GAP on EVERY sub-run of length ≤ 80) and ii-runs (λ_W constant:
§2, §4 (b), §5, §6; CHARGE-U on every sub-run). Levels L: all of −1..n−1 for n ≤ 12, else {−1, 0, ⌊n/2⌋, n − 2, max M_D}. Paths for
P^c_sch: every W-play prefix at every state, plus every simple path of G_τ to a W-cycle node for n ≤ 9, else 3 random simple paths per (k, x).
FRZ-SCH over all pairs s ≤ t and all x. UNF re-derives k′ for every charge. Mutations bite where the data allows (§5.4).
### 5.2 Sets and totals (0 violations of any signed item in every set)
| set | N5 runs | states | ff runs / transitions | PSCH clean checks | FRZ-SCH checks | changes (window / charged) | UNF | FZ | U events (all L) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| set | N5 runs | states | ff runs / transitions | PSCH clean checks | FRZ-SCH checks (with content) | changes (window / charged) | UNF | FZ | U events (all L) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| packet instances (frz1-3 + .start, pftheta34_n32 S3, pft34_h3u_P32 t33, lcount, lcount2, offret, incdown, offalt_K10, off_s21-24, lenonly, tw_s1) | 16 | 383 | 27 / 314 | 130,316 | 358,002 (175,065) | 2,192 / 822 | 1,116 | 4,041 | 194 |
| climb best c_pft (from pftheta34_n32, 1,500 steps) | 1 | 45 | 2 / 38 | 14,100 | 50,884 (24,456) | 197 / 88 | 88 | 1,046 | 36 |
| climb best c_frz3 (from frz3_n24, 1,500 steps) | 1 | 27 | 1 / 25 | 9,185 | 18,885 (8,959) | 81 / 109 | 231 | 449 | 39 |
| lib41 minus referee games (410) × 3 starts (S3 + 2 random) | 1,230 | 19,624 | 1,618 / 11,333 | 2,562,243 | 7,481,986 (3,354,870) | 91,816 / 6,433 | 6,932 | 258,869 | 5,596 |
| my 503 𝒞^1O files × 2 starts | 1,006 | 17,739 | 1,701 / 11,596 | 2,586,464 | 7,355,584 (3,199,417) | 90,384 / 7,862 | 8,721 | 301,845 | 6,208 |
| random 2 Odd choices, n 5-9 (3,000 games × 2; every level, every simple path) | 6,000 | 14,642 | 583 / 611 | 27,091 | 31,008 (24) | 2,440 / 0 | 0 | 83 | 0 |
| random 3 Odd choices, n 8-16 (2,000 × 2) | 4,000 | 11,563 | 564 / 590 | 27,121 | 31,725 (35) | 2,334 / 0 | 0 | 63 | 0 |
| random 4 Odd choices, n 10-20 (2,000 × 3) | 6,000 | 19,119 | 893 / 965 | 37,246 | 44,524 (33) | 4,211 / 0 | 0 | 200 | 6 |
| random kO, n 12-24 (1,000 × 2) | 2,000 | 7,148 | 307 / 328 | 10,505 | 12,525 (7) | 1,097 / 0 | 0 | 27 | 0 |
Also, summed over all sets: OFFSET (b) 880,446 checks, MERGE-B 831,527, TWIN-GAP on 177,288 sub-runs with 3,103,655 offset changes
(963 at tail transitions; 1,466 tail-rise checks), PIECE_D (a) 11,128 aligned states (11,025 arenas brute-forced), PIECE_D (b) 3,765 blocks,
SPLIT-RED 4,855 h3-runs, CHARGE-U 31,870,837 (x, sub-run, L) checks, CR-REL 12 non-vacuous freezes, forbidden (pair, state)s at L = −1:
169,675 on 15,150 states. Extremes: longest ff run 55 transitions (x32_rand64, n = 64); B up to 155 (leanT_N24, n = 192); N_v up to 19
(pf_best_3622, n = 40, B = 29); |U_{−1}(S)| up to 23 (so_j19_n48); SPLIT-RED's |S| / bound ≤ 0.288. Logs: R2-N5-RUND/logs/ (summary.txt).
Reproduce: `docs/referee-2/R2-N5-RUND/run_all.sh` (instances), `run_all.sh big`, `run_all.sh extra` (random k4, climbs, mutations, UF-ONCE).
The random sets give short runs (charged changes 0): the content is in the libraries and the long runs.
### 5.3 Comparison with the lane's §9 (after my runs)
- Numbers that are comparable agree: |U_{−1}| per run 7 / 5 / 6 on frz1 / frz2 / frz3 and 7 on pftheta34_n32 (lane §9: 7 / 5 / 6, 7);
  |K_F| 17 on frz3 and 33 on pftheta34_n32 (lane: 17, 33; my frz1 21 sums its two runs, lane 16 for the 24-transition run).
- Clean-pair counts are not comparable (mine sum over several levels and over all x).
- The lane's "max U events per vertex per run 1" is restricted to games with ≥ 2 Odd choice vertices and n ≤ 48 (sched.py KMIN = 2, NMAX)
  and to its own start pairs; §4 explains the difference.
### 5.4 Mutations (must fail)
On pftheta34_n32 (S3 start) unless named: shift (schedule looks at k − q): FRZ-SCH 671, P^c_sch 62 FAIL; noforb (forbidden-ness
ignored): FRZ-SCH 10,234, P^c_sch 1,359 FAIL; fz (FZ for every coarse-W-improving edge): 180 FAIL; unf: 85 FAIL; chu0 ((n − 1)|U|): 6,083
FAIL; crrel1 (freeze from k_0 + 1): 0 on pftheta34_n32, 33 FAIL on frz3_n24. Do NOT bite (bounds slack in all data, N-RUND-6): tg4, tgr,
piece. On frz3_n24 (first check) the same pattern: shift 553, noforb 5,907, fz 84, unf 179, chu0 2,281, crrel1 33 FAIL.

## 6. Signatures
§2 CR-REL; §3 OFFSET (a)-(c), MERGE-B, TWIN-GAP (i)-(iii) and Corollary; §4 PIECE_D (a), (b), SPLIT-RED; §5 P^c_sch, FRZ-SCH, CHARGE
(hypothesis (ii) only); §6 Fact FZ, Lemma UNF, Corollary CHARGE-U (hypothesis (ii) only): SIGN, on every game, under the standing SPEC
premise 1E-N3 in forms P1 and P2 (N-RUND-1), with notes N-RUND-2..7. No gap. REFEREE-2 successor 16 (Opus 5.5, D15).

## §C. Comparison with REFEREE (R-N5-RUND, claude/referee 29846bca, its §C at 981307c9; successor 13), written 2026-10-26 10:32Z (date -u)
Opened only after my report was pushed (7a02a1f2, 10:08Z) and on the Lead's word (10:17Z). Read in full: verdicts, §1-§8 and its §C.
| item | REFEREE | REFEREE-2 | relation |
| --- | --- | --- | --- |
| all 14 signed items (§2-§6) | SIGNED, no gap | SIGN, no gap | same |
| §1 quotes | R62 setting, (d), (e), (f), R55 (a), R17 (a) verbatim by script; R19 (d) NOT verbatim (RUND-N1) | same by script (N-RUND-2) | same |
| (SG) basis for OFFSET (a) | R15 (a) (RUND-N1) | R15 (a) + R15 (d) via (VJ) under P1, as R60 lists it (N-RUND-2) | same fact; mine names the (VJ) step that carries R15 (a) to SPEC's Ξ |
| FZ's inputs | XW / (VJ) = 1E-N3, totality of ⊴, (Cstrict), definition of D_k (RUND-N2) | P1, totality, (Cstrict), R55 (a) for the last step | same (R55 (a) is that use of D_k's definition); ACCEPT RUND-N2's wording |
| 1E-N3 in form P2 under §2-§5 (WM-G, (F1) on H_k, switch-best) | implicit through landed R62 (d) / R18 (d) S (c) | N-RUND-1, explicit | REFEREE accepts N-RUND-1 |
| PIECE_D (b): R17 (c) on switch-best started at B's first state | RUND-N3 (wording) | read so in my §2 ("B is a prefix of the switch-best run on G_τ from B's first state"), not flagged | ACCEPT RUND-N3 as a note |
| TWIN-GAP (ii): the bound is the WIDTH of the low-part range, Σ_{r ≤ L*} 2^r | RUND-N4 (wording) | my §2 uses the width, not flagged | ACCEPT RUND-N4 as a note |
| |S| in SPLIT-RED = transitions; PIECE_D (b)'s m_τ ≤ m | read so | N-RUND-3 | REFEREE accepts |
| TWIN-GAP (ii): transitions counted by source state | read so (its probe) | N-RUND-4 | REFEREE accepts |
| U(S) = U_L(S), U_L ⊆ U_{−1} | data remark | N-RUND-5 | REFEREE accepts |
| thin data | CR-REL hypothesis 3-5 times; P^c_sch exhaustive only n ≤ 7 | N-RUND-6 (TWIN-GAP (ii), PIECE_D (b) slack; 12 CR-REL freezes) | same in substance |
| §4 remarks | checked | checked (N-RUND-7) | same |
| side finding: CONJECTURE UF-ONCE FALSE (§7, not signed) | reproduced so_th_n32 on its engine (states 1..22, three unforbid-switches of vertex 24) | found (so_th_n32, phase2_pk48) | confirmed independently on two engines |
| data | 0 failures; long runs with every suffix, lib41, 6,000 random; MUT=1/2 fail | 0 violations; instances, climbs, lib41, 503 𝒞^1O, random k 2-4; 6 mutations fail | same; its coverage note (runs cut at λ_W changes only in mine) is right |
- No disagreement. Joint gap map for the signed items: EMPTY. Notes to the lane (union): RUND-N1 = N-RUND-2, RUND-N2, RUND-N3, RUND-N4,
  N-RUND-1, N-RUND-3..7. Outside the signed items: UF-ONCE is false on two engines; §7's route to |U(S)| ≤ n_E needs another argument.
- My verdicts are unchanged. REFEREE-2 successor 16 (Opus 5.5, D15).
- Addendum to §C (10:38Z, date -u), answering the Lead's 10:34Z points:
  - Correction: REFEREE's §C commit is 62a1a01d (the text I read and compared, on origin/claude/referee); "981307c9" in the §C header above
    is wrong (that commit has no §C). The comparison is unchanged.
  - Confirmed, point by point: all 14 signed, joint gap map empty; REFEREE accepts N-RUND-1 (P2), N-RUND-3, -4, -5; RUND-N3 and RUND-N4 are
    REFEREE-only notes, which I ACCEPT; UF-ONCE reproduced by REFEREE on so_th_n32.
  - CHARGE-U on the so_th_n32 sub-run (states 1..22, the run REFEREE's probe skips): re-run on my checker
    (R2-N5-RUND/logs/so_th_n32_S3.txt): 0 violations, 29,696 CHARGE-U checks. Honest limit: that run has 21 transitions < n − 1 = 31, so
    every one of its 302 COARSE_L(W) changes is a WINDOW change and CHARGE-U holds there through its n − 1 window term alone; the witness
    refutes UF-ONCE but does not stress CHARGE-U's U-term. The U-term is exercised elsewhere (charged changes 15,314 over my sets, §5.2).
