# P-N5-COMPOSE (box 28): a switch is paid by a value rise of its successor, a value rise by a path-set change, so every N5 run on every game has ≤ 2n(n − 1) + (n(n − 1) + 1)·n·(m_E(P* + 1) + m_O(P*^U + 1)) iterations, P* the most path-set changes of one vertex in one λ-run
L-SI successor 24 (Opus 5.5; D18, Lead reading L40). Packet for the referees, FROZEN at its push; the sha1 goes to the Lead; repairs go in
a NEW file docs/si/P-N5-COMPOSE-fixes-box28.md. Lead 2026-10-29 11:27Z: «Freeze it now as packet docs/si/P-N5-COMPOSE-box28.md for both
referees ... Contents: Lemma LEN-MONO, Lemma SW-RETURN (on any stretch), Theorem COMPOSE, Corollary COMPOSE-RUN, each with every symbol
defined and its premises quoted with line numbers (quote check). MATCH-Φ is named as an ASSUMED premise (P-N5-MPGS (A), under review); the
packet's own claims are the reductions up to P*.» Working note with data: docs/si/N5-CHG-box28.md §9. Labels (D18 / L40): PROVED (lane,
unrefereed) / ASSUMED / DATA / READING.
SCOPE (D1): a REDUCTION of N5's iteration count on every game to a per-vertex count of path-set changes. Not a TARGET.md claim, not an
algorithm claim, no running-time bound (P* and the carry counts are NOT bounded here); G-N5-TIME stays OPEN.
Every [Q path@commit:lines] «…» below is verbatim, checked by experiments/si/rund/quotecheck.py (pinned in experiments/si/check.sh with a
shifted-line control that must fail).

## 0. What to sign, and what not
| § | statement | label |
| --- | --- | --- |
| §2 | Lemma SW-RETURN (any stretch of any N5 run, both players) | PROVED (to sign) |
| §3 | Lemma LEN-MONO (any λ-run, both players) | PROVED (to sign) |
| §4 | Theorem COMPOSE (switches of one player inside one λ-run ≤ Σ over its edges (v, c) of n·(PCH(c) + 1); a phase is bounded by it) | PROVED (to sign) |
| §5 | Corollary COMPOSE-RUN (every N5 run on every game) | PROVED (to sign) |
| §6 | Corollary COMPOSE-NM: with MATCH-Φ, P* ≤ (n²/2)(NM* + 1) + NM* | PROVED from an ASSUMED premise (sign only the implication) |
| §7 | data with each inequality's slack; pinned check | DATA (NOT to sign) |

## 1. Setting, symbols, premises
- N5 = SPEC S1-S5 of docs/new/N5-ssi-global.md (FIX 1-4 as in RESULTS); any parity game G = (V, E, Ω, owner), n = |V|. A run is the sequence of
  states (σ_t, τ_t), t = 0, …, T, from a start pair; a TRANSITION is t → t + 1. m_E (m_O) := the number of edges leaving Even (Odd) vertices.
- [S1-val] [Q docs/new/N5-ssi-global.md@b025560c9:28-29] «valuation of v under (σ, σ̄): (c, P, ℓ), c = the most relevant (max p') vertex of
  the cycle the play from v ends in, P = set of vertices on the play before reaching c with p' > p'(c), ℓ = number of steps to reach c.»
- [S1-ord] [Q docs/new/N5-ssi-global.md@b025560c9:30-31] «order (better for Even): compare reward of c (p'(c) if even, −p'(c) if odd); then P
  by the signed weight Σ_{u∈P} (+2^rank(u) if Ω(u) even else −2^rank(u)); then ℓ: if c is odd, longer is better for Even; if c even, shorter
  is better.» "c is odd" means Ω(c) odd. ⊴ / ◁ denote this order (◁ strict), ⊵ / ▷ the reverse.
- [S1-Xi] [Q docs/new/N5-ssi-global.md@b025560c9:32] «Ξσ = valuation of every vertex under σ and Odd's OPTIMAL counterstrategy σ̄ (minimising
  this order at every vertex at once).» Ξ_t := Ξ_{σ_t}. It depends on σ_t only (RESULTS R15 (d) below).
- [S2] [Q docs/new/N5-ssi-global.md@b025560c9:47] «Improving edges: Iσ = {(v, w) : owner(v) = Even, w ≠ σ(v), Ξσ(w) strictly better than
  Ξσ(σ(v))}; Iτ the same on G^d for τ.»
- [S4a] [Q docs/new/N5-ssi-global.md@b025560c9:51] «a. If Iσ ≠ ∅: A(v) = {σ(v)} ∪ {w : (v, w) ∈ Iσ} for Even v.» and σ_new is a strategy of
  the arena H in which [Q docs/new/N5-ssi-global.md@b025560c9:51] «Even v keeps only edges to A(v)».
- [S4b] [Q docs/new/N5-ssi-global.md@b025560c9:54] «b. If Iτ ≠ ∅: A(v) = {τ(v)} ∪ {w : (v, w) ∈ Iτ} for Odd v. Arena H': Odd v keeps only
  edges to A(v)».
- [S4c] [Q docs/new/N5-ssi-global.md@b025560c9:56-57] «c. FALLBACK, if σ_new = σ and τ_new = τ: if Iσ ≠ ∅, for every Even v with an improving
  edge set σ_new(v) = the w with (v, w) ∈ Iσ maximising (Ξσ(w), w) (best valuation, ties: larger index); otherwise do the same for Odd on Iτ with
  G^d's valuations.»
- [MON] RESULTS R15 (a): [Q docs/RESULTS.md@b025560c9:631] «(a) Lemma A: for any non-empty unambiguous set I of improvements of σ (VJ00 §4.4),
  Ωσ ⊴ Ω_{Switch_I(σ)}.» (Ω_σ = Ξ_σ, R47's setting below.)
- [STEP] RESULTS R15 (d): [Q docs/RESULTS.md@b025560c9:640-642] «(d) N5: every iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ (on G)
  and/or with ∅ ≠ I ⊆ Iτ to Odd's τ (on G^d), and changes at least one of them (S4a/S4b, or the S4c fallback, a switch-all); Iσ depends on σ
  alone (Ωσ is against ⊖'s optimal reply, not against τ).»
- [Φ] RESULTS R47, setting and Lemma Φ (signed for EVERY game; we use nothing of its Corollary Φ-1O, which is for one-Odd-choice games only):
  [Q docs/RESULTS.md@b025560c9:2330-2331] «Ξ_k := Ξ_{σ_k} (Even's valuation, R15's Ω_σ), λ_k(v) its cycle node; U_k := Odd's valuation of τ_k
  in the dual game G^d (R38 (a)'s U_k), λ^U_k(v) its cycle node» and [Q docs/RESULTS.md@b025560c9:2336] «(a) Lemma Φ (every game):» with
  [Q docs/RESULTS.md@b025560c9:2338] «(c) along a run at most n(n − 1) transitions change λ and at most n(n − 1) change λ^U».
- [DELTA] RESULTS R84 (a): [Q docs/RESULTS.md@b025560c9:4967-4968] «(a) Fact DELTA (§1, with F4): for sets A ≠ B of ranks, weight(B) > weight(A)
  iff d := d(A, B) is even and d ∈ B ∖ A, or d is odd and d ∈ A ∖ B.» In particular distinct sets have distinct weights.
- [MΦ] (ASSUMED, under review: L-LIT's packet P-N5-MPGS (A), claude/l-lit a23179b01) [Q docs/lit/P-N5-MPGS.md@a23179b01:97-98] «Added statement
  (A), Corollary.…For every game, vertex v and phase 𝒫: PCH_𝒫(v) ≤ (K(K+1)/2)·(NM_𝒫(v) + 1) + NM_𝒫(v).» Its proof's premises:
  [Q docs/lit/P-N5-MPGS.md@a23179b01:105] «Uses: distinct ranks [S1-rank], P_t ⊆ R_c [S1-val] with c fixed on 𝒫 [PHASE].» (K := the number of
  ranks above c's rank, NM_𝒫(v) := the number of CARRIES, P-changes that are not MATCHED, as defined there.)
- Symbols. A λ-RUN: a maximal run of consecutive states with λ_t constant (τ free). A λ^U-RUN: the same with λ^U_t. A PHASE: a maximal run
  with (λ_t, τ_t) constant (RESULTS R38 (a)); a phase lies inside one λ-run. For a run of states R (a "stretch") and vertices v, c:
  ENT_R(v, c) := #{t : t, t + 1 ∈ R, σ_t(v) ≠ c = σ_{t+1}(v)} (Even v; for Odd v the same with τ), SW_R(v) := Σ_c ENT_R(v, c), the switches
  of v in R; RISE_R(c) := #{t : t, t + 1 ∈ R, Ξ_{t+1}(c) ≠ Ξ_t(c)}; PCH_R(c) := #{t : t, t + 1 ∈ R, P(Ξ_{t+1} c) ≠ P(Ξ_t c)}. For Odd's side
  RISE^U, PCH^U are the same with U_t on G^d. P*_R := max_c PCH_R(c); P* := max over λ-runs R of P*_R; P*^U likewise over λ^U-runs.
- Two facts used throughout.
  (F-SW) Every Even switch of N5 goes along an edge of Iσ_t: S4a's σ_new uses only edges to A(v) [S4a], and A(v) ∖ {σ(v)} ⊆ Iσ; S4c switches v
  to a w with (v, w) ∈ Iσ [S4c]. Every Odd switch goes along Iτ_t: [S4b], [S4c].
  (F-MON) Ξ_{t+1} ⊵ Ξ_t at every vertex and every transition of every run: if σ changes, σ_{t+1} = Switch_I(σ_t) with ∅ ≠ I ⊆ Iσ_t [STEP], and
  [MON] applies (I is unambiguous: σ_{t+1} is a strategy); if σ does not change, Ξ_{t+1} = Ξ_t (Ξ depends on σ alone, [STEP]). Dually
  U_{t+1} ⊵ U_t in G^d's order ([MON] on G^d with [STEP]'s «with ∅ ≠ I ⊆ Iτ to Odd's τ (on G^d)»; U depends on τ alone).

## 2. Lemma SW-RETURN (PROVED, lane)
Statement. For every run of states R of an N5 run, every Even v and every vertex c: ENT_R(v, c) ≤ 1 + RISE_R(c). Dually for Odd v with U.
Proof. First, Ξ-SUCC: Ξ_t(σ_t v) is non-decreasing in t. If v does not switch at t, Ξ_{t+1}(σ_{t+1} v) = Ξ_{t+1}(σ_t v) ⊵ Ξ_t(σ_t v) by (F-MON);
if v switches to w, Ξ_{t+1}(w) ⊵ Ξ_t(w) ▷ Ξ_t(σ_t v) by (F-MON) and (F-SW), [S2].
Let e < e′ be consecutive entries of v into c in R (σ_{e+1}(v) = σ_{e′+1}(v) = c, σ_e(v) ≠ c ≠ σ_{e′}(v), and σ_t(v) ≠ c for some t in between).
Let s ∈ [e + 1, e′ − 1] be the step at which v leaves c (σ_s(v) = c ≠ σ_{s+1}(v)). Then
Ξ_{e′}(c) ▷ Ξ_{e′}(σ_{e′} v) (F-SW at e′) ⊵ Ξ_{s+1}(σ_{s+1} v) (Ξ-SUCC) ⊵ Ξ_s(σ_{s+1} v) (F-MON) ▷ Ξ_s(c) (F-SW at s, σ_s(v) = c) ⊵ Ξ_{e+1}(c) (F-MON).
So Ξ(c) changes at some transition in [e + 1, e′ − 1] ⊆ R; the intervals [e + 1, e′ − 1] of successive pairs of entries are disjoint. Hence
the entries number ≤ 1 + RISE_R(c). Odd's side: the same on G^d with U, τ, Iτ. □

## 3. Lemma LEN-MONO (PROVED, lane)
Statement. For every λ-run R and every vertex c: RISE_R(c) ≤ PCH_R(c) + (PCH_R(c) + 1)(n − 1). Dually for λ^U-runs with U.
Proof. On R the cycle node of Ξ_t(c) is a fixed vertex c₀ (λ constant). By (F-MON) Ξ_t(c) is non-decreasing on R, and by [S1-ord] with c₀ fixed
the order compares weight(P) first, then ℓ. At a transition with P(Ξ_{t+1} c) ≠ P(Ξ_t c) the weights differ ([DELTA]) and so weight rises
strictly. Hence each P-value occupies one contiguous block of R, and there are PCH_R(c) + 1 blocks. Inside a block, a change of Ξ(c) is a change
of ℓ alone, and by (F-MON) and [S1-ord] it moves ℓ strictly in the direction [S1-ord] prefers for Ω(c₀) (shorter if even, longer if odd). By
[S1-val] ℓ is the number of steps from c to c₀ along the play, a lasso on at most n vertices, so ℓ ∈ {0, …, n − 1}, and a block holds at most
n − 1 changes. So RISE_R(c) ≤ PCH_R(c) + (PCH_R(c) + 1)(n − 1) = n·PCH_R(c) + n − 1. U: the same on G^d. □

## 4. Theorem COMPOSE (PROVED, lane; a REDUCTION)
Statement. For every λ-run R of an N5 run on any game, the Even switches inside R satisfy
Σ_v SW_R(v) ≤ Σ_{(v, c) ∈ E, owner(v) = Even, SW_R(v) > 0} (1 + RISE_R(c)) ≤ Σ_{(v, c)} n·(PCH_R(c) + 1) ≤ m_E·n·(P*_R + 1).
For every phase 𝒫 (inside a λ-run R): |𝒫| ≤ Σ_v SW_𝒫(v) ≤ the same sums with R replaced by 𝒫. Dually for Odd's switches in a λ^U-run.
Proof. SW_R(v) = Σ_{c ∈ succ(v)} ENT_R(v, c) ≤ Σ_c (1 + RISE_R(c)) (Lemma SW-RETURN); 1 + RISE_R(c) ≤ n·(PCH_R(c) + 1) (Lemma LEN-MONO); sum over
Even v (only those that switch contribute a non-zero SW). In a phase τ is constant, so by [STEP] every transition of 𝒫 changes σ, i.e. contains
an Even switch: |𝒫| ≤ Σ_v SW_𝒫(v). □

## 5. Corollary COMPOSE-RUN (PROVED, lane; a REDUCTION)
Statement. Every N5 run on every game has T ≤ 2n(n − 1) + Σ_{λ-runs R} Σ_v SW_R(v) + Σ_{λ^U-runs R′} Σ_{Odd v} SW_{R′}(v)
≤ 2n(n − 1) + (n(n − 1) + 1)·n·(m_E·(P* + 1) + m_O·(P*^U + 1)) transitions (iterations).
Proof. Classify each transition t → t + 1 (S4a and/or S4b steps and S4c fallbacks alike) by the first case that applies:
(i) λ_{t+1} ≠ λ_t; (ii) σ_{t+1} ≠ σ_t (then t, t + 1 lie in one λ-run R and the transition contains an Even switch counted in SW_R);
(iii) λ^U_{t+1} ≠ λ^U_t; (iv) otherwise σ is unchanged, so by [STEP] τ changes, t and t + 1 lie in one λ^U-run R′, and the transition contains
an Odd switch counted in SW_{R′}. By [Φ] (c) — the every-game Lemma Φ — at most n(n − 1) transitions are of kind (i) and at most n(n − 1) of
kind (iii). The λ-runs are the maximal runs between kind-(i) transitions, so there are at most n(n − 1) + 1 of them; likewise at most
n(n − 1) + 1 λ^U-runs. Theorem COMPOSE bounds Σ_v SW_R(v) by m_E·n·(P*_R + 1) on each λ-run and the Odd switches by m_O·n·(P*^U_{R′} + 1) on each
λ^U-run. □
Fallback transitions (Lead's point (2)). An Even fallback (S4c with Iσ ≠ ∅) changes σ along Iσ (F-SW) and not τ: it is of kind (i) or (ii),
charged to an Even switch of its λ-run. An Odd fallback (S4c with Iσ = ∅) changes τ along Iτ and not σ: kind (iii) or (iv), charged to an Odd
switch of its λ^U-run. A transition applying S4a and S4b together is charged to its Even switch (kind (ii)) unless λ changes. No transition is
uncharged ([STEP]: σ or τ changes).
The λ-run counts (Lead's point (1)). They come from [Φ] (c) alone: «at most n(n − 1) transitions change λ and at most n(n − 1) change λ^U»,
read separately for each map, on EVERY game (Lemma Φ is signed «(every game)»); the joint count 2n(n − 1) + 1 of R47 is not used, nor R47's
phase count or R48, which hold only on one-Odd-choice games.

## 6. Corollary COMPOSE-NM (the implication only; [MΦ] is ASSUMED)
Statement. If [MΦ] holds with "phase" replaced by "λ-run" (resp. "λ^U-run" on G^d), then P*_R ≤ (n²/2)(NM*_R + 1) + NM*_R with NM*_R the most
carries of one vertex in R, and Corollary COMPOSE-RUN bounds T by a polynomial in n, m and the largest carry count NM* (over both players).
Proof. K ≤ n − 1 gives K(K + 1)/2 ≤ n²/2. □
Note for the referees. [MΦ] is signed (if signed) for phases. Its proof uses only «c fixed on 𝒫» (its Uses line, quoted in §1): c is fixed on
every λ-run (that is what λ constant means), and τ is not used. The replacement of "phase" by "λ-run" is therefore a reading of [MΦ]'s proof,
to be confirmed by its referees, and it is the only place this packet uses [MΦ]. For phases alone (Theorem COMPOSE's second statement), [MΦ]
applies as signed.

## 7. Data and pinned check (DATA, NOT to sign)
Tool experiments/si/chg/compose.py (per phase: L, S1 = Σ SW, S2 = Σ(1 + RISE), S3 = Σ n(PCH + 1), S4 = the [MΦ] bound; MODE=run: the whole run,
Even side on λ-runs, Odd side on λ^U-runs with U = Odd's dual valuation of τ on G^d). Pinned in experiments/si/check.sh (box 28 §9 block), run
from experiments/si:
- `python3 -I chg/compose.py --one chg/instances/red/runquad_K8_m30_n192.pg chg/instances/red/runquad_K8_m30_n192.start` prints
  `TOP (263, 'chg/instances/red/runquad_K8_m30_n192.pg', 0, 263, 481, 1016, 195072, 265890048, 8, 15, 15, 15, 192)` and I0, I1, LDIR, LBLK, I2,
  I3 PASS (L = 263 ≤ S1 = 481 ≤ S2 = 1,016 ≤ S3 = 195,072 ≤ S4; max NM 8, max PCH = max RISE = max SW = 15; n = 192). The instance is a
  byte-identical copy of L-RED's R106 pin (claude/l-red 86f24219), sha1 ebaa6ac57ec60948fb986210c27479cb3a7961d9.
- `python3 -I chg/compose.py --one chg/instances/dlsep_kill_n70.pg chg/instances/dlsep_kill_n70.start` prints
  `TOP (12, 'chg/instances/dlsep_kill_n70.pg', 0, 12, 39, 387, 26810, 14059640, 5, 6, 7, 4, 70)` (sha1 e500ea47e1dc0163b32a97042ff9752daf6db83a).
- `MODE=run python3 -I chg/compose.py --one lay/instances/seglast_kill_n110.pg lay/instances/seglast_kill_n110.start` prints
  `TOP (16, 'lay/instances/seglast_kill_n110.pg', 0, 16, 27, 152, 16066, 0, 20, 1, 4, 2, 110)`: T = 16 ≤ 20 Even + 1 Odd in-run switches + 4 λ-
  and 2 λ^U-changes = 27; RUNI0, R47, EI1, OI1, ELDIR, OLDIR, ELBLK, OLBLK PASS (also on L-RED's segcount_kill_n20).
- Corpora (chg/compose_*.txt, chg/composerun_*.txt): every inequality holds on all phases of alt_all pinned starts (457), lib41 (418), all
  experiments/si instances (345) and all runs (413, 412, 276); L/S1 ≤ 1, S1/S2 ≤ 0.75 per phase; largest per vertex per phase NM 42 and PCH 71 at
  n 41 (experiments/si/root/instances/l121reader_n41); at most 31 λ-runs and 28 λ^U-runs in one run. L-RED's families: R106 mkr.py (K, m) up to
  (12, 4), (6, 40): NM = K, PCH = 2K − 1, L ≤ S2; ladderd0_k48_n156: NM 0, PCH 48.
- Slack (READING): L ≤ S1 ≤ S2 are within a factor ≤ 4 in all data; the slack sits in LEN-MONO's factor n (length-only rises are rare: at most
  0.875n per vertex per phase, 0 on runquad) and in [MΦ]'s n²/2.
