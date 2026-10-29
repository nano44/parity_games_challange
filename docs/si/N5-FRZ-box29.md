# N5-FRZ (box 29): the σ̄-frozen piece in the W frame — Lemma W-MON, Lemma CN-W, Theorem W-SPLIT (a phase reduces to fallbacks, σ̄-changes and FROZEN W-PHASES); CONJECTURE FW-BF (a frozen W-phase has ≤ n − 1 W-changing transitions)
L-SI successor 25 (Opus 5.5; D18, Lead reading L40). Lead's brief 2026-10-29 12:22Z, STEP 1: «the core case: a σ̄-FROZEN PIECE of a phase.
τ is fixed, σ̄ is fixed, and the set D (Odd vertices with σ̄ ≠ τ) is fixed. ... Find a polynomial bound on the piece length, or on carries
per vertex in the piece, or a kill.» Working note, unrefereed, not frozen. Not a TARGET.md claim. Nothing here bounds N5's running time;
G-N5-TIME stays OPEN. Labels (D18 / L40): PROVED (lane) / CONJECTURE / OPEN / DATA / READING / DEAD. Counts are TRANSITIONS.
Tools: experiments/si/frz/ (frozen.py, wphase.py, fwphase.py, phstat.py, settle.py, risedepth.py, caseA.py, blocked.py, fresh.py,
fwclimb.py); outputs frz/*.txt; climb logs frz/out/; pin frz/instances/s_elim24_final.{pg,start} (copy of orlens/instances/s_elim24_final.pg,
sha1 ddb99d6c…, with its S3 default start written out so that n5b can replay it).

## Summary
| § | item | label |
| --- | --- | --- |
| §1 | Lemma W-MON: inside a phase every non-fallback transition has W_{t+1} ⊵ W_t at every vertex (σ̄ free); Lemma XW: Ξ_t ⊴ W_t always | PROVED (lane) |
| §1 | Lemma CN-W: on a fallback-free stretch of a phase a vertex changes its W cycle node ≤ n − 1 times; ≤ n(n − 1) λ_W-changing transitions | PROVED (lane) |
| §2 | Theorem W-SPLIT: \|𝒫\| = FB + LWCH + SBCH′ + Σ (frozen W-phase lengths), LWCH ≤ n(n − 1)(FB + 1), #frozen W-phases ≤ FB + LWCH + SBCH′ + 1 | PROVED (lane), a REDUCTION |
| §2 | Corollary FW-D0: a frozen W-phase with D = ∅ has ≤ n − 1 W-changing and < n + m transitions (R17 on G_τ; contains R17-D0) | PROVED (lane) |
| §3 | the σ̄-frozen pieces: runquad / s3quad (\|D\| = 32): W has 0 P-changes, all 1,419 W-rises are cycle-node changes, every one of the 263 transitions changes λ_W, so the piece has NO frozen W-phase and L = LWCH ≤ n(n − 1) | DATA, explained by CN-W |
| §4 | CONJECTURE FW-BF (≤ n − 1 W-changing transitions per frozen W-phase) and FW-LEN (< n + m transitions) | CONJECTURE; DATA 0 failures in 2,644 frozen W-phases |
| §4 | W-phases (cut at fallbacks and λ_W changes only): ≤ n − 1 W-changing DEAD (x135_n59: 135 > 58); σ̄ changes restart waves | DEAD; DATA |
| §5 | the proof obstruction: R17's induction in the W frame needs the Ξ-form of the hypothesis at z; it fails at OPTIMISM-TRAPPED vertices (play into D, where τ flatters Even). Candidate lemmas SETTLE, RD (W frame), SETTLE_X, RDX (Ξ frame), Case A (W), Case B (Ξ), B monotone, FRESH, ENT1 | READING; DEAD (instances) |
| §6 | what is left: FB per phase (FB-LIN, OPEN), σ̄-changes per phase SBCH′ (OPEN; DATA ≤ 1.53n), FW-BF (CONJECTURE) | OPEN |

## 0. Setting
N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md), any game. A PHASE 𝒫: a maximal run of states with λ_Ξ (Ξ's cycle-node map) and τ constant
(RESULTS R38 (a)), S4c fallbacks included. Ξ_t = val(σ_t, σ̄_t) (σ̄_t = Odd's optimal counterstrategy to σ_t, S1); W_t = val(σ_t, τ) (the value
of the (σ_t, τ)-play, VJ00 valuation, S1's order); λ_W = W's cycle-node map. FB = in-phase S4c fallback transitions. A FROZEN W-PHASE: a maximal
run of in-phase transitions none of which is a fallback, changes λ_W, or changes σ̄ (so on it τ, σ̄, D = {Odd u : σ̄(u) ≠ τ(u)}, λ_Ξ, λ_W are
constant). LWCH = non-fallback in-phase transitions that change λ_W; SBCH′ = non-fallback in-phase transitions that keep λ_W and change σ̄.
G_τ (G_σ̄): G with Odd fixed to τ (σ̄), a one-player game of Even; on a σ̄-constant stretch Ξ_t = val_{G_σ̄}(σ_t), W_t = val_{G_τ}(σ_t).

## 1. PROVED (lane): W is monotone in the phase; Ξ ⊴ W; cycle-node changes of W
- Lemma W-MON. Let t → t + 1 be a transition inside a phase that is not an S4c fallback. Then W_{t+1}(v) ⊵ W_t(v) for every v.
  Proof. τ_{t+1} = τ_t = τ. A transition changes σ or τ (RESULTS R15 (d)), so σ_{t+1} ≠ σ_t, and σ_{t+1} is not a fallback, so it is S4a's
  σ_new: Iσ_t ≠ ∅ and σ_{t+1} is Even's optimal strategy (S1 procedure, pointwise optimal) in the one-player arena H_t in which Even v keeps
  {σ_t(v)} ∪ {w : (v, w) ∈ Iσ_t} and Odd v keeps only τ(v). σ_t is a strategy of H_t, and the (σ, τ)-plays of G and of H_t coincide for
  σ ∈ {σ_t, σ_{t+1}}. By RESULTS R17 (a) (F1) (the optimum of a one-player game dominates every strategy of that game pointwise),
  W_{t+1} = val_{H_t}(σ_{t+1}) ⊵ val_{H_t}(σ_t) = W_t. □ (No hypothesis on σ̄: W-MON holds on the whole phase. At fallbacks W can fall: DATA
  WMON_V counts only fallback transitions, e.g. frz/instances/s_elim24_final t = 16, 33, 43, 48, all S4c.)
- Lemma XW. Ξ_t(v) ⊴ W_t(v) for every v and t. Proof. σ̄_t is pointwise optimal for Odd against σ_t (S1; R17 (a) (F1) on the dual), and τ is one
  Odd strategy. □ Consequence: Ξ_t(v) = W_t(v) when v's (σ_t, τ)-play avoids D_t (both plays coincide); W ▷ Ξ only on plays that enter D.
- Lemma CN-W. On a stretch of a phase that contains no fallback, each vertex changes its W cycle node at most n − 1 times; so at most
  n(n − 1) transitions of the stretch change λ_W. Proof. By W-MON, W(v) is non-decreasing on the stretch; S1's order compares the cycle node's
  reward first, and rewards (±p′) of distinct vertices are distinct, so each change of v's cycle node strictly raises its reward, which takes
  ≤ n values. A λ_W-changing transition changes some vertex's cycle node. □ DATA: CNW_V = 0 everywhere (phstat.py, wphase.py).

## 2. PROVED (lane): Theorem W-SPLIT and Corollary FW-D0
- Theorem W-SPLIT. For every phase 𝒫 of N5 on any game, with L* := the longest frozen W-phase of 𝒫:
  |𝒫| = FB + LWCH + SBCH′ + Σ_{frozen W-phases F ⊆ 𝒫} |F|, LWCH ≤ n(n − 1)(FB + 1), #frozen W-phases ≤ FB + LWCH + SBCH′ + 1, hence
  |𝒫| ≤ (FB + 1)(n(n − 1) + 1) + SBCH′ + (FB + 1 + n(n − 1)(FB + 1) + SBCH′)·L*.
  Proof. Every in-phase transition is a fallback, or a non-fallback λ_W-change, or a non-fallback λ_W-keeping σ̄-change, or none of these
  (then it lies in a frozen W-phase); these are the cuts, and the frozen W-phases are the maximal runs between cuts, so their number is
  ≤ cuts + 1. The fallbacks cut 𝒫 into ≤ FB + 1 fallback-free stretches; CN-W bounds the λ_W-changes of each by n(n − 1). □
  (Check: WSPLIT_V = 0 on every corpus, phstat.py; the identity is bookkeeping, the content is CN-W.)
- Corollary FW-D0. A frozen W-phase F with D = ∅ has at most n − 1 W-changing transitions and fewer than n + m transitions.
  Proof. On F σ̄ = τ, so Ξ_t = W_t (both are S1's valuation of the same plays), Iσ_t is the improving set of σ_t in the one-player game G_τ,
  and S4a's step is a pointwise optimum of the arena {σ_t} ∪ Iσ_t: switch-best on G_τ (RESULTS R17 (d): any pointwise-optimal choice). No
  fallback occurs on F and λ_W (= λ of G_τ's valuation) is constant, so F is a run of switch-best on G_τ started at F's first state inside one
  λ-phase; RESULTS R17 (b), (c) apply. □ (Corollary R17-D0 of N5-CHG-box28 §14 is the case F = a whole phase.)
- READING. W-SPLIT moves the frame: the arena still comes from Ξ, but the counting is done in W, where the step is an optimum (W-MON) and the
  first component of the order cannot cycle (CN-W). It does not need σ̄ frozen; σ̄-changes enter only ADDITIVELY (each one cuts one more frozen
  W-phase). The open quantities are FB, SBCH′ and L*.

## 3. DATA: the σ̄-frozen pieces of the brief (frz/frozen.py, frz/wphase.py, frz/phstat.py)
| instance | piece | L | \|D\| | ESW | NMx (Ξ-carries, max/vertex) | NMw (W-carries) | W P-changes max | W cycle-node changes (sum) | LWCH | frozen W-phases |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| runquad_K8_m30_n192 (R106 pin, chg/instances/red/) | [0, 263] | 263 | 32 | 481 | 8 | 0 | 0 | 1,419 | 263 | 0 |
| s3quad_K8_m30 (R107 copy) | [0, 263] | 263 | 32 | 481 | 8 | 0 | 0 | — | — | — |
| frz/instances/s_elim24_final | [4, 63] | 59 | 1 | 73 | 4 | 4 | 7 | 0 | 0 | 5 (cut by 4 fallbacks), longest 16 |
| n5-exhaustive/instances/b6_xl2_n32 (S3 start) | [57, 81] (phase [4, 87] has 11 pieces) | 24 | 1 | 34 | 3 | 3 | 3 | 0 | 0 | phase: 6 W-phases, 10 fallbacks |
- FINDING (runquad / s3quad). In the W frame the Θ(n²) family is elementary: W never changes its P-set (0 P-changes, 0 W-carries, while Ξ has 8
  carries per vertex), every W-rise is a cycle-node change (1,419), every transition changes λ_W (LWCH = 263), FB = SBCH′ = 0, and there is no
  frozen W-phase. So W-SPLIT gives |𝒫| = LWCH ≤ n(n − 1) for this phase with nothing left to bound. The carries of §10-§13 of box 28 are an
  artefact of the Ξ frame here.
- FINDING (|D| = 1). b6_xl2_n32 and s_elim24_final: the long phases are cut by FALLBACKS (10 and 4) into W-phases of ≤ 22 and ≤ 16 transitions
  (< n − 1); λ_W never changes. The (n − 1)(|D| + 1) failure of box 28 §14 is a fallback effect.
- Library (frozen.py; σ̄-frozen pieces 877 alt_all pinned starts, 692 lib41, 634 experiments/si): longest piece L/n 3.31 (lend107_n32, |D| = 3),
  2.46 (s_elim24_final); W-carries per vertex per piece up to 20 (red/usplit/instances/grow_K40_n373, |D| = 4) and 8 at D = ∅ (new/box25/sc24),
  so a carry count in W is NOT the mechanism either (sc24: 8 W-carries in a D = ∅ piece of 20 < n − 1 transitions, R17 holds there).

## 4. CONJECTURE FW-BF / FW-LEN (DATA) and the dead W-phase form
- CONJECTURE FW-BF: every frozen W-phase has at most n − 1 W-changing transitions. CONJECTURE FW-LEN: every frozen W-phase has fewer than n + m
  transitions. (Both are R17 (b), (c) read in the W frame; FW-D0 proves them for D = ∅.) With FW-LEN, W-SPLIT gives
  |𝒫| < (FB + 1)(n(n − 1) + 1) + SBCH′ + (FB + 1 + n(n − 1)(FB + 1) + SBCH′)(n + m) = O((FB + 1)·n²·(n + m) + SBCH′·(n + m)).
- DATA (fwphase.py, settle.py): 0 failures of FW-BF and FW-LEN in 2,644 frozen W-phases (alt_all pinned starts 1,125; lib41 864;
  experiments/si 655). Largest WCH/(n − 1): 1.000 (lwp/out/rs1_64212_0, n 5, D = ∅); with |D| = 1: 0.870 (n5-epoch/instances/gci3_n24, 20 at
  n 24), 0.833 (runlin/instances/runfam_K100, 115 at n 139); |D| = 2: 0.800 (n5-epoch/instances/lend13_n16); |D| ≥ 3: 0.484 (lend107_n32).
  Largest L/(n + m): 0.286 (red/n5inj/instances/blockph_bp32). W-silent transitions (σ changes, W does not; Ξ always rises) exist in 38 frozen
  W-phases (FWSIL), so FW-LEN is not implied by FW-BF.
- Kill search (fwclimb.py: score = max over frozen W-phases with |D| ≥ 1 of WCH/(n − 1), kill = FW-BF or FW-LEN failure; mutations of
  chg/cclimb.py): seeds gci3_n24 (0.869), lend13_n16 (0.800), s_elim24_final (0.695, stopped), red/xing/instances/kw25_n32 (0.806):
  no kill (see the log lines in frz/out/fw_*.log at the commit).
- DEAD: «a W-phase (cut at fallbacks and λ_W changes only, σ̄ free) has ≤ n − 1 W-changing transitions»: runlin/instances/x135_n59 (sha1
  e71e8af0…, start 4afb7e8c…; n5b identical, 136 iterations, 0 fallbacks): W-phase [1, 136], 135 W-changing transitions, n 59, |D| = 1, 11
  σ̄-changes; also red/n3/instances/run49_n32 (49 > 31) and red/so/instances/pftheta_cex_n32 (34 > 31). Its seven frozen W-phases have ≤ 43
  each. Obstruction (as for RUN-LIN, DEAD.md box 24): every σ̄-change restarts a Bellman-Ford wave. FW-LEN-type L < n + m still holds on
  W-phases on all three corpora (max 0.601, runfam_K100, 291 < 484; wphase.py R17W PASS), and L ≤ m_E held on the three probes x135_n59, runfam_K100,
  run49_n32 (max 0.858; not run on the corpora) — CONJECTURE W-PHASE (< n + m), weaker than FW-LEN + SBCH′.

## 5. Why R17's proof does not transfer, and the candidate lemmas that died (READING; DEAD with instances)
- R17's Lemma P (W_k(x) ⪰ value(r) for every path r of ≤ k edges to a cycle node) needs Case A («(x, z) outside the arena ⇒ W_k(z) ⊴ W_k(ρ_k x)»)
  and Case B («inside the arena ⇒ the step's value ⪰ x ⊕ W_k(z)»). In the W frame Case B holds (W-MON's (F1)); Case A holds IF the
  hypothesis at z is available in Ξ: (x, z) ∉ H_k gives Ξ_k(z) ⊴ Ξ_k(ρ_k x) ⊴ W_k(ρ_k x) (Lemma XW), so W_{k+1}(x) ⪰ x ⊕ W_k(ρ_k x) ⪰ x ⊕ Ξ_k(z).
  So a two-frame Lemma P needs «Ξ_k(z) ⪰ value(r′)» for D-free r′; in the Ξ frame Case A is free and Case B fails exactly when x's W-optimal
  choice enters D (W flatters it, Ξ does not). OPTIMISM-TRAPPED vertices (current play into D with W ▷ Ξ, an honest D-free improving edge
  offered and refused) are the obstruction: s_elim24_final, frozen W-phase [4, 16], x = 3 sits on 3 → 8 → 18 (D) → τ 19 → 20 for the whole
  W-phase while (3, 14) is Ξ-improving (caseA.py EXAMPLE B).
- Measured inside frozen W-phases (all on n5b-identical runs):
  | candidate | statement | status | instance |
  | --- | --- | --- | --- |
  | CASEA-W | an edge outside the arena is never W-better than σ_t(x) | DEAD | x135_n59 (1,721 triples), runfam_K100 (2,669), s_elim24_final (409) |
  | CASEB-Ξ | an honest switch inside the arena is never Ξ-better than the step's choice | DEAD | x135_n59 (278), runfam_K100 (280), s_elim24_final (79) |
  | SETTLE (W) | W_{a+k}(x) = W_b(x) once W_b(x).length ≤ k | DEAD | frz/instances/s_elim24_final [17, 33], x = 11 (final length 3, still changes at k = 16); lib41 55 failures |
  | RD (W) | a W-rise at step k has length ≥ k | DEAD | the same (k = 16, x = 11, length 3) |
  | SETTLE_X, RDX (Ξ) | the same in Ξ | DEAD | red/ul/instances/ladderd0_k12_n48 (L-RED's ladder, sha1 c654bf9e…, start 674f6eeb…; n5b identical, 14 iterations), [0, 13], \|D\| = 14, x = 14: final length 2, Ξ changes at every step k = 2..13 (one rung per tick); also reader_L10/20/40 and ladderd0_k24/k48 |
  | B-MONO | the blocked set (W-better edges outside the arena) only shrinks / only grows | DEAD | x135_n59 (21 growth, 5 shrink events; 72 blocked edges used later) |
  | FRESH / ENT1 | every transition enters a new edge / each edge entered ≤ once per W-phase | DEAD | x135_n59 (59 re-entry-only transitions; an edge entered 3 times) |
  SETTLE_X holds on every frozen W-phase with |D| ≤ 2 of all three corpora (RDX: measured on lib41 and alt_all, the same); both fail only
  with |D| ≥ 3: L-RED's ladder and reader families and lay/out/ll41_k, ll42_k (SETTLE_X, experiments/si corpus), where one vertex climbs a ladder of D-gated rungs, one rung per tick of ONE Bellman-Ford wave (so FW-BF still holds there:
  13 ≤ 47).
- READING (the shape of a proof). Each tick of a frozen W-phase is caused by a predecessor event one tick earlier: a W-rise of a successor
  (propagated along G_τ edges) or a Ξ-rise of a successor that opens an arena edge (along G_σ̄ edges). A causal chain longer than n − 1
  revisits a vertex; in one frame R17's path values forbid it. With two frames a chain can pass a D vertex o once via σ̄(o) and once via τ(o),
  which suggests the weaker CONJECTURE FW-D: WCH ≤ (|D| + 1)(n − 1) per frozen W-phase (still ≤ n² + n, polynomial). No data separates FW-BF
  from FW-D yet (the ladder spends its D vertices inside one wave).

## 6. What is left (OPEN) and per-phase data (phstat.py)
- With FW-LEN: |𝒫| = O((FB + 1)·n²·(n + m) + SBCH′·(n + m)), so the σ̄-frozen piece is polynomial in its fallback count, and a whole phase in
  (FB, SBCH′). FB per phase: CONJECTURE FB-LIN (≤ n; L-RED 5 boxes without a kill; RESULTS R48 proves ≤ 1 + (n − 2)(2n − 1) on 𝒞^1O).
  SBCH′ per phase: OPEN — this is K9's «changes of σ̄» factor (L-NEW, docs/new/N5-brchanges-box11.md), now entering additively and per phase.
- DATA (lib41, 368 phases): FB ≤ 0.750n (si/xing/instances/ccl_fbx_n32: 24 at n 32), LWCH ≤ 0.646n (red/so/instances/post31_n48), SBCH′ ≤ 1.531n
  (si/orlens/instances/lev_l_x: 49 at n 32), frozen W-phases ≤ 0.600n (red/xing/instances/j4_n40: 24); runquad: LWCH 263 = 1.37n.
  alt_all pinned starts (457 phases): FB ≤ 0.781n (red/so/instances/farrise25_n32), LWCH ≤ 0.646n, SBCH′ ≤ 2.100n (n5-epoch/instances/nep92_n40:
  84 of the phase's 92 transitions, ONE frozen W-phase of length 1), frozen W-phases ≤ 0.700n (red/n3/instances/long121_n40: 28). experiments/si
  (345): FB ≤ 0.850n (coarse/instances/box9/cl9_mn_b), SBCH′ ≤ 1.805n (root/instances/l121reader_n41: 74), frozen W-phases ≤ 0.683n.
  WSPLIT_V = CNW_V = 0 everywhere (frz/phstat_*.txt).
- READING. SBCH′ is NOT intrinsic: Odd READER vertices (no predecessors; box 25 §3, RESULTS READER-INV) change σ̄ without changing any arena,
  and l121reader_n41 (1.8n) is the reader-inflated l121 instance. A sharper W-SPLIT cuts only at σ̄-changes that change some Iσ_t-relevant
  value (σ̄ on the Ξ-plays from successors of Even vertices); then the readers' changes stay inside frozen W-phases, and FW-BF must be
  re-measured with the coarser cut (not done yet; OPEN).

## DONE / FINDINGS / NEEDS
- DONE: this note; tools experiments/si/frz/ (10 scripts), data frz/*.txt, climbs frz/out/; pin frz/instances/s_elim24_final.{pg,start};
  DEAD.md «box 29»; check.sh «box 29» block.
- FINDINGS: (1) PROVED (lane): W-MON, XW, CN-W, Theorem W-SPLIT (a phase = fallbacks + ≤ n(n − 1)(FB + 1) λ_W-changes + σ̄-changes + frozen
  W-phases), Corollary FW-D0 (R17 on G_τ for D = ∅). (2) runquad / s3quad (Θ(n²), |D| = 32, σ̄ constant) are fully accounted for by CN-W: all
  263 transitions change λ_W; W has 0 carries. (3) CONJECTURE FW-BF / FW-LEN: 0 failures in 2,644 frozen W-phases; with them the σ̄-frozen
  piece is O((FB + 1)·n²·(n + m)). (4) DEAD: «≤ n − 1 per W-phase» (x135_n59), and the single-frame lemmas CASEA-W, CASEB-Ξ, SETTLE, RD,
  SETTLE_X, RDX, B-MONO, FRESH, ENT1 (instances above). (5) The proof obstruction is the optimism-trapped vertex (play into D).
- NEEDS: none from the owner.
