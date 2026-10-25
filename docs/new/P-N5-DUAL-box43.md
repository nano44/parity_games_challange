# Packet P-N5-DUAL (box 43): N5 is mirror-symmetric under G ↔ G^d up to S4c's tie rule; 𝒞^1E inherits 𝒞^1O phase bounds
L-NEW successor 22 (Opus 5.5), D14 / D18, Lead reading L40; Lead's order 22:48Z (Lead's stamp). Written 2026-10-25 ~23:00Z (date -u).
FROZEN at push: later text goes into a fixes file. Source: docs/new/N5-MULTI-box43.md §1 (working doc; this packet governs).
Labels: PROVED (L-NEW 22) / CONJECTURE / DATA / READING. Not a TARGET.md claim: nothing here bounds N5's running time on any class;
G-N5-TIME stays open. Theorem MIRROR is an IMPLICATION whose hypothesis (H-OF) is NOT proved here.

## 0. Setting
- N5 = SPEC S1-S5 of docs/new/N5-ssi-global.md (with FIX 1-4). Game G = (V, E, Ω, owner), n = |V|. G^d := n5.py's dual: owners
  swapped, Ω + 1, same ids and successor lists. A state is a pair (σ, τ); the N5 run from a start pair is its state sequence.
- N5^OF ("Odd first"): N5 with S4c replaced by: if σ_new = σ and τ_new = τ, then if I_τ ≠ ∅ Odd falls back (switch-all on I_τ,
  each Odd v with an improving edge takes the w maximising (Ξ_τ(w), w) on G^d, σ unchanged), else Even falls back as in S4c. All
  other steps as in N5.
- A TWO-SIDED FALLBACK is an iteration where S4c applies (σ_new = σ, τ_new = τ) with I_σ ≠ ∅ and I_τ ≠ ∅.
- MIRROR of a state (σ, τ) of G: the state (τ, σ) of G^d (G^d's Even strategy is G's τ). Mirror of a sequence: statewise.
- Classes: a choice vertex has out-degree ≥ 2. 𝒞^1O: exactly one Odd choice vertex o, d := deg(o) (RESULTS R17-R48). 𝒞^1E: exactly
  one Even choice vertex e, d_e := deg(e), any number of Odd choice vertices. 𝒞^kO: exactly k Odd choice vertices o_1..o_k.
- Phase (of a run of N5 or N5^OF): maximal run of states with (λ, τ) constant (RESULTS R38 (a) KEY: on every game, = joint λ-phase).
  Dual phase: maximal run with (λ^U, σ) constant. λ, λ^U as in RESULTS R47.
- Premises used (landed): RESULTS R15 (a)-(d) (termination potential; no strategy repeats under any non-empty improving switch set,
  on G and G^d), R47 (a) Lemma Φ (λ changes ≤ n(n − 1), λ^U changes ≤ n(n − 1) along a run).

## 1. To sign
### Lemma DUAL (PROVED, every game)
For every game G and start pair (σ_0, τ_0): the N5 run on G from (σ_0, τ_0) is the mirror of the N5^OF run on G^d from (τ_0, σ_0)
(same length, state k ↦ mirror of state k). Consequently the N5 run on G^d from (τ_0, σ_0) agrees with that mirror up to and
including the state right after the first two-sided fallback's source, i.e. it can differ first at state j + 1 where j → j + 1 is
the first two-sided fallback of the run on G; with no two-sided fallback the two runs are mirrors.
Proof.
- (E) Engine invariance. (G^d)^d is G with Ω + 2. SPEC S1 uses Ω only through rank(v) = position of v in V sorted by (Ω(v), v) and
  through Ω(v) mod 2 (p′(v) = 2·rank(v) + (Ω(v) mod 2), reward, the order on valuations, the VJ procedure's case split "Ω(u) even /
  odd"), plus owners and successor lists. Ω ↦ Ω + 2 changes none of these. So every S1 output (valuations, improving sets, optimal
  counterstrategies with their tie-breaks) on any arena equals the output on that arena with Ω + 2.
- (S2) G^d's Even improving set for its strategy τ is computed on G^d: it is N5's I_τ. G^d's Odd improving set for its strategy σ
  is computed on (G^d)^d = G with Ω + 2: by (E) it is N5's I_σ.
- (S4a on G^d) A(v) = {τ(v)} ∪ I_τ(v) for G^d-Even v (= G-Odd v); arena H″: G^d with these restrictions and G^d-Odd (= G-Even) fixed
  to σ; new strategy := Odd's optimal counterstrategy in the dual of H″ to its dual-Even strategy σ. The dual of H″ is N5's S4b arena
  H′ (G-Odd v restricted to A(v), G-Even fixed to σ) with Ω + 2, and "Odd's optimal counterstrategy to σ" is N5's S4b output; by (E)
  the results are equal: G^d's new Even strategy = N5's τ_new.
- (S4b on G^d) A(v) = {σ(v)} ∪ I_σ(v) for G^d-Odd v (= G-Even v), by (S2); arena H‴: G^d with these restrictions and G^d-Even
  (= G-Odd) fixed to τ; new strategy := Odd's optimal counterstrategy (S1, on H‴ itself) to τ. H‴ is exactly the dual of N5's S4a arena
  H (G-Even v restricted to A(v), G-Odd fixed to τ), and N5's S4a output is "Odd's optimal counterstrategy in the dual of H to the
  dual-Even strategy τ": the same computation. So G^d's new Odd strategy = N5's σ_new.
- (S4c) Both runs fall back exactly when the S4a/S4b outputs leave the state unchanged (same outputs, above). N5 on G falls back
  for G's Even (on I_σ) if I_σ ≠ ∅, else for G's Odd (on I_τ). N5^OF on G^d falls back for G^d's Odd (= G's Even) if its improving
  set (= I_σ) is non-empty, else for G^d's Even (= G's Odd) on I_τ. Same side in both cases; the switch-all target rule "(valuation,
  index) maximal" uses the same valuations (Ξ_σ on G for G's Even side, by (E) for G^d's Odd side; Ξ_τ on G^d for G's Odd side) and
  the same index order. FIX 3 (only the falling-back side changes) holds in both.
- (S4 count, S5 stop) One iteration = one pass with I_σ ∪ I_τ ≠ ∅; the stop rule I_σ = I_τ = ∅ is symmetric. (S5's output formula is
  not part of the state sequence.)
- Induction on k gives the first sentence. Second sentence: N5 and N5^OF on G^d apply the same rule except at a fallback where both
  improving sets are non-empty, and on G^d the improving sets are I_τ and I_σ, i.e. exactly at G's two-sided fallbacks. ∎
DATA (experiments/new/box43/mirror.py, sha1 7ed95913fb9c5d36a21c56ab9f8692ff0af11d8c; engine box21/n5x.py step = n5.py's loop):
- lib41 (experiments/new/box41/lib41.txt, 412 files, any class) and `mirror.py --rand 3000 4 14 11` (3,000 random C^kO, k = 1..4,
  n 4-14): N5 on G = mirror of N5^OF on G^d in 3,412 / 3,412 runs.
- The one observed break of the PLAIN mirror (N5 on G^d), stated plainly: 15 lib41 runs have two-sided fallbacks (54 such fallbacks,
  dblfb.py, sha1 ca3c2298…); in all 15 the plain mirror first differs at the state right after the first two-sided fallback, never
  earlier; 0 of the other 3,397 runs differ. Example: experiments/red/so/instances/exitr_cex_n48.pg (sha1 7a663df25ba44e15022ad94fe5f0709662dbca8d;
  n 48): first two-sided fallback at transition 2 → 3, plain mirror differs first at state 3; N5 on G 22 iterations, N5 on G^d 23.
- dualsym.py (sha1 a5f74af9…): 1,999 / 2,000 random runs are plain mirrors; the one difference follows a fallback.

### Theorem MIRROR (PROVED, as an implication)
(a) On 𝒞^1E, along any N5 run σ changes at most d_e − 1 times, and the run has at most n(n − 1) + d_e dual phases.
(b) Hypothesis (H-OF), NOT proved here: there is L(n) such that for every 𝒞^1O game with n vertices and every start pair, the FIRST
    phase of the N5^OF run from that start pair has at most L(n) transitions.
    Under (H-OF), N5 on every 𝒞^1E game with n vertices, from every start pair, makes at most (n(n − 1) + d_e)(L(n) + 1) iterations.
(c) (H-OF) follows from (H-N5): "for every 𝒞^1O game with n vertices and every start pair, the first phase of the N5 run has at most
    L(n) transitions".
Proof. (a) On 𝒞^1E, σ is determined by σ(e); the σ's along the run form a strict ≺_G-chain (R15 (c), (d): every iteration applies a
non-empty improving switch set to σ or τ, and Iσ depends on σ alone), so no σ repeats and σ takes at most d_e values. Dual phases
end only at a λ^U-change (≤ n(n − 1), R47 Lemma Φ) or a σ-change (≤ d_e − 1). (b) Let G ∈ 𝒞^1E; G^d ∈ 𝒞^1O with Odd choice vertex e.
By DUAL the N5 run on G is the mirror of the N5^OF run on G^d, and dual phases of the former are phases of the latter. By (a) there
are at most n(n − 1) + d_e of them, and by (H-OF) applied to the first state x of each (N5^OF is memoryless: the next state is a
function of the current state, so the run from x is the suffix of the run from the start pair) each has at most L(n) transitions;
adding the ≤ n(n − 1) + d_e − 1 boundary transitions gives the bound. (c) Take the N5^OF run from x on G^d ∈ 𝒞^1O. Until its first
two-sided fallback it coincides with the N5 run from x (the rules differ only there). At a two-sided fallback N5^OF switches G^d's
Odd strategy on a non-empty improving set, i.e. changes τ of G^d, which ends the phase. So the first N5^OF phase from x is a prefix
of the first N5 phase from x (or equals it), and has at most L(n) transitions. ∎
Scope (READING): 𝒞^1E has games with arbitrarily many Odd choice vertices, so any polynomial (H-N5) proved by the 𝒞^1O program
gives N5 polynomial on a class with unboundedly many Odd choice vertices. (H-N5) is open: G-N5-TIME on 𝒞^1O needs crossings (FX)
and T per phase (P-N5-KW); fallbacks per phase are RESULTS R48.

### Corollary Φ-kO (PROVED, every game)
Along any N5 run the number of distinct τ's is at most ∏ over Odd choice vertices o_i of deg(o_i), and the run has at most
n(n − 1) + ∏_i deg(o_i) phases. Mirror: at most n(n − 1) + ∏ over Even choice vertices of deg dual phases. On 𝒞^kO with k fixed,
phases ≤ n(n − 1) + n^k (polynomial).
Proof. τ is determined by its values at the Odd choice vertices; no τ repeats (R15 (c), (d) on G^d), so distinct τ's ≤ ∏ deg(o_i)
and τ changes ≤ ∏ deg(o_i) − 1; a phase ends only at a λ-change (≤ n(n − 1), R47 Lemma Φ) or a τ-change. Mirror: the same with σ, λ^U. ∎
Remark (DATA, docs/new/N5-MULTI-box43.md §3.2): the per-vertex sharpening "τ(o_i) changes ≤ deg(o_i) − 1" is false on games where both
players have ≥ 2 choice vertices (experiments/new/box43/instances/retf_n6.pg, sha1 8b936bfb…; tx2_n8.pg, sha1 c0f7b214…). It was never
claimed beyond 𝒞^1O; it is not a dead end of anything signed.

### Lemma ENDGAME (PROVED, every game)
If I_σ = ∅ at state k of an N5 run, then σ_j = σ_k for every j ≥ k. Mirror: if I_τ = ∅ at state k, then τ_j = τ_k for every j ≥ k.
Proof. I_σ depends on σ alone (R15 (d)). With I_σ = ∅, S4a sets σ_new = σ, and S4c falls back for Odd only (I_σ = ∅), so σ_{k+1} =
σ_k and again I_σ = ∅; induction. Mirror: with I_τ = ∅, S4b sets τ_new = τ and S4c falls back for Even only (Odd needs I_τ ≠ ∅). ∎

## 2. To check (not to sign): hypothesis (H-OF) / (H-N5) per landed result
(H-N5) needs per-phase bounds valid FROM ANY START PAIR (by memorylessness, "every phase of every run from every start pair" = "the
first phase from every state"). Column "start": does the RESULTS entry's statement or its packet's statement/proof restrict the start?
(READING: grep for "start" / "initial" / "S3" in each entry and packet, 22:50Z; hits are segment / stretch starts, data lines, or
"any start".) Column "N5^OF": does it hold for N5^OF? READING for all rows: a per-transition statement about a transition k → k+1 of a
phase holds for N5^OF because every in-phase transition of N5^OF is an N5 transition from the same state (an N5^OF transition that is
not an N5 transition is an Odd fallback, which ends the phase); a count over a phase holds for N5^OF phases because they are prefixes
of N5 first phases (MIRROR (c)), PROVIDED the N5 statement holds from any start pair; a whole-run statement holds for N5^OF if its
proof uses only R15 (c), (d)-type facts (every iteration applies a non-empty improving switch set).
| result | kind | start in statement / proof | N5^OF (READING) |
| --- | --- | --- | --- |
| R17 (one-player phases) | per phase, one-player | "valid from ANY start" (Cor. 2) | yes (prefix) |
| R18 (o-acyclic run bound, Prop X) | whole run | "from any start pair" | Prop X yes; (c) to check (its count uses N5's fallback rule) |
| R19 Lemma G, Wo, RM, RE, PIECE | per transition / phase | none (P-N5-RE: "valid from any start" for R17's use) | yes |
| R20 C, FBL, FBF, CR, XA | per stretch | none | yes (prefix) |
| R21 XW, EQ, FBL-N, NF, F1, F2, X | per transition / phase | none ("start" = a transition's source state) | yes; FBL-N (i) is about Even fallbacks, identical in N5^OF |
| R22 F1°, TC, P3′ | per interval | none | yes |
| R23 (K), ACT, LOOP, GAP, WM, LV′ | per transition / fallback | none (data only) | yes |
| R24 R, TB, CASC, U1, WC | per transition / piece | none | yes |
| R25 (T), TAME, MONO, FB, J1, OFF, CAP | per phase | none | yes (prefix) |
| R26 CASC-U2, CASC-U3 | per run of a phase | none (data: "run step 0") | yes (prefix) |
| R27 U, HI, LP, DF′, BAND, TH, SO | per phase | none | yes (prefix) |
| R28 U-loc, OE, OX | per phase | none (data: 3 starts) | yes |
| R29 Fact R, TRANSFER, OFFGATE, CN, NL, CLS1 | per scope run / phase | none | yes |
| R30 OR, TC-SPLIT, R-STICK, H3H2, LEAVE, H1-DROP, WK, ABS-L | per transition / prefix | none ("initial part" = of a run) | yes |
| R31 P-OPT, FBW, FBW-S, STRETCH, PL | per fallback / phase | none | yes; S4c's Even case identical |
| R32 Fact 0, FREEZE, X-RUN, SUB | per phase | none ("initial segment" = SN prefix) | yes (prefix) |
| R33 H3-CONST, H2-STICK, G′, R-CONST, H1-INT | per phase | none | yes |
| R34 L-MONO, Z-COUNT, TOGGLE, TOGGLE-COUNT, RESTARTS | per phase | none ("start a new (h)-run" = within a phase) | yes (prefix) |
| R35 RDROP, MINSET, ENT-SHAPE | per block / phase | none | yes |
| R36 P1 (one-player) | one-player | none | yes (not about N5 runs) |
| R37 BL, CONF-MONO, FREE-FREEZE, EV | per fallback | none | yes |
| R38 KEY, WCH, SCOPE-COUNT, FB-INT, NH1-FB, CN-LAST | per phase | none | yes (prefix) |
| R39 SPLIT, EPOCH, F-FLAT, NE-COUNT | per phase / stretch | none | yes |
| R40 FZ, BF, CYC-EV, TEV-FB | per scope run | none | yes |
| R41 LV-SHAPE, LV-COUNT, PL_{−1} | per fallback / phase | none | yes |
| R42 RISE, NO-ENTRY-A′, BRK, OUT-1 | per HN stretch | "S's start" = the stretch's first state | yes |
| R43 STALE-GATE, SAND, LV-NONE, SCOPE-FB | per fallback / phase | none (a referee instance is "from a start pair") | yes |
| R44 FB-ROUND, P-FREEZE, BRK-POLY | per fallback / θ-run | none | yes; FB-ROUND is about Even fallbacks |
| R45 Y-FORM, HAT-FREEZE, RHO-TAIL, RHO-HN | per phase | none (data: canonical start) | yes (prefix) |
| R46 T0U, SG-EV, T0-PIN, NHN-BOUND, HN-POLY-ALL | per phase | none | yes (prefix) |
| R47 Φ, Φ-1O | whole run | none | yes (proof uses R15 (a), (d), R18 (d) only) |
| R48 FB-POLY (fallbacks per phase) | per phase | none in statement (data: random start pairs) | yes (prefix; N5^OF's in-phase fallbacks are a subset) |
| in review: P-N5-FX, P-N5-KW, P-N5-NH-box42 | per phase | to check | to check |
To check by the referees, per row: (i) no proof step uses a property of the S3 start or of the history before the phase; (ii) the
row's statement is prefix-closed where marked "prefix" (a bound on a count over a phase also bounds the count over a prefix).

## 3. Not signed here
- docs/new/N5-MULTI-box43.md §2 (ledger, READING), §3 (frontier data), §4 (routes, CONJECTURES Δ1, Δ2).
- The cross-field reading of DUAL (self-dual pivoting with a symmetry-breaking tie rule) is a READING, no literature claim.
## 4. Reproduce
`python3 experiments/new/box43/mirror.py --list experiments/new/box41/lib41.txt` → "runs 412: runs with a two-sided fallback 15; DUAL
violations 0; N5 on G != N5^OF on G^d mirrored: 0". `python3 experiments/new/box43/mirror.py --rand 3000 4 14 11` → "runs 3000: runs
with a two-sided fallback 0; DUAL violations 0; ...: 0". (Run from experiments/new/box43; ~40 min and ~20 min.)
