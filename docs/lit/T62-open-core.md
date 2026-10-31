# T62: the open core of N5's running time inside one W-run: statement, proved equivalent forms, the techniques tried and the exact hypothesis each lacks, and the current lower-bound evidence (synthesis for a later human-expert packet; the owner decides any contact)
L-LIT successor T59 (Opus 5.5), D18. Lead's brief 2026-10-30 20:42Z (T62). Written 2026-10-30 20:45Z-21:10Z (date -u). A SYNTHESIS: no new
claims. Every PROVED item cites a landed RESULTS entry, a referee-signed packet or a lane commit. Every CONJECTURE / OPEN item is marked
as such. Not a TARGET.md claim. G-N5-TIME stays OPEN.
Status words, used strictly:
- PROVED (landed) = in docs/RESULTS.md, refereed-only, CHECKER PASS;
- PROVED (pending) = signed packet whose RESULTS entry is drafted but not landed;
- PROVED (lane) = proved in a lane note, unrefereed;
- CONJECTURE = stated, with data, unproved;
- OPEN = no conjecture is preferred;
- DEAD = refuted, with its instance.

## 1. Setting (one paragraph)
- N5 is SPEC S1-S5 (docs/new/N5-ssi-global.md), a symmetric strategy-improvement scheme for parity games:
  - S4a: Even moves to the pointwise optimum of the one-player arena H_t, in which Even keeps σ_t ∪ Iσ_t and Odd follows τ_t;
  - Iσ_t are Even's Vöge-Jurdziński improving edges, against Odd's optimal counterstrategy σ̄_t;
  - Odd's τ moves symmetrically on the dual (S4b);
  - S4c is a fallback.
- Termination is RESULTS R15. The running time (gauntlet step 4) is GAPS G-N5-TIME, open.
- A W-run F (RESULTS R89) is a maximal run of consecutive states of one τ-stretch with no S4c fallback and no change of λ_W, the
  cycle-node map of W_t := val(σ_t, τ). Inside F, τ and the W-cycle nodes are fixed.
- How whole runs reduce to W-runs: RESULTS R89 Theorem STRETCH-RED (τ-stretches vs W-runs, fallbacks, ρ). The τ-side counts are in
  RESULTS R86 / R89 COMPOSE-FREEZE. P-N5-SETTLE Corollary T-XCH: T ≤ m_E(1 + XE) + m_O(1 + XO). This note is only about the inside of
  one W-run.

## 2. The open core, stated once
- **OPEN: XI-CH-POLY.**
  - Statement: there is a polynomial p with max_v ΞCH_F(v) ≤ p(n) for every W-run F of N5 on every game, where ΞCH_F(v) is the number
    of transitions of F at which Ξ_t(v) changes.
  - Equivalently (§3), WRUN-POLY: |F| ≤ p(n).
  - Data: every family seen is at most quadratic (§5). No proof, no super-quadratic instance.
- The same core in the per-vertex event form (L-SI's HEAD-RED′; PROVED (lane), §3): polynomial W-runs ⇔ three per-vertex counts are
  polynomial:
  - CN_F(c): switches at W-cycle nodes c;
  - XCN_F: σ̄-flips at Odd vertices that are their own Ξ-cycle node;
  - HXU′_F(u): Ξ-changes at heads u ∈ U′_k := U_k ∪ τ(Odd), with U_k = L-RED R143's upward heads {σ̄_k(g) : σ̄_k(g) ≠ τ(g)} ∪ {Ξ-successors of
    the W-cycle nodes}.
  - CONJECTURES on these: HX′-POLY (data linear, max 36 per W-run), XCN-POLY (corpus total 5), CN-POLY. All unproved (l-si accd388a,
    docs/si/N5-SBF-box53.md §4).

## 3. Proved equivalent and reducing forms
| statement | status | where |
| --- | --- | --- |
| FW-R*: a frozen W-phase has ≤ (n − 1)(R*_T + 1) W-changing transitions (R*_T = transitions with a late adoption of a blocked edge) | PROVED (landed) | RESULTS R88 (CHECKER C97 767bb71e) |
| GP*-RUN: FW-R* on every W-run; R*-RISE (late adoptions of (y, z) ≤ Ξ-changes at z); STRETCH-RED | PROVED (landed) | RESULTS R89 (C99 3d9ce0ef) |
| PHASE-RED, FLAT-SW (proof of record SW-KEEP, REFEREE 2c9d8040), PHASE-RED′: a phase has \|P\| ≤ (4n(n−1)+1)(n(n+2) + Σ_x FLATSW_P(x) + 1) | PROVED (landed) | RESULTS R94 (C104, checker 5c4d6e45; Add. 1 c34d98a2) |
| XI-RUN: \|F\| ≤ m_E + Σ_c d_E(c)·ΞCH_F(c); WRUN-EQ: WRUN-POLY ⇔ XI-CH-POLY ⇔ P*-POLY ⇔ DEEP_k-POLY ⇔ R*-POLY ∧ FL-POLY ⇔ ALT-POLY ∧ FREE-POLY ⇔ R3-POLY ∧ TIE-POLY ⇔ R*-POLY ∧ [P-INT] ⇔ SB-POLY ∧ R°-POLY ∧ FL-POLY | PROVED (pending) | P-N5-WRUN (l-new 7668bc9b; both referees, complete); R95 draft docs/agents/R95-draft.md (CHECKER C105 pending) |
| RUN-SETTLE: an event-free stretch of a W-run has ≤ n − 1 transitions; RUN-COUNT \|F\| ≤ n(E_F + 1) − 1; HEAD-RED (E_F ≤ Σ SB + Σ CN + Σ HXU); T-XCH | PROVED (pending) | P-N5-SETTLE (l-si 6a70a520), both referees' §C SIGNED (REFEREE ea05b574, REFEREE-2 3fd4aaf0); not landed |
| ROOT-FLIP; HEAD-RED′ (§2) | PROVED (lane) | l-si accd388a, docs/si/N5-SBF-box53.md §2-§3; L-RED R146 (no kill) |
| ARENA-MAX: W_(t+1)(v) ⊵ val(ρ, τ_t)(v) for every strategy ρ of H_t | PROVED (lane; immediate from SPEC S4a) | L-RED R140 (l-red 47000632) |
| BETA-MON, ELIM-ORD-β (ordinal action elimination); counting \|F\| ≤ (m_E + 1)·HW_F | PROVED (lane) | L-LIT T58 (d78e1815) |
| HW-LB: HW ≥ T/(m₀ + 1) for any run | PROVED (lane) | L-LIT T59 (c7dc03db) §3.1 |
| PAIR-CROSS: SB_F(o) ≤ strict reversals of successor pairs + tie re-orders | PROVED (lane) | L-LIT T60 (54584c0c) §4.2 |
| One-player games: a λ-phase has ≤ n − 1 value-changing steps; N5 polynomial there | PROVED (landed) | RESULTS R17 |
- CONJECTURE ELIM-WIN (T58): HW_F ≤ p(n). It implies WRUN-POLY by the T58 counting. Data: HW = m + 1 on fx.

## 4. Techniques tried (L-LIT T52-T61), each with its nearest opened theorem, the exact hypothesis N5 lacks, and the instance
| technique (lane note) | nearest opened theorem | hypothesis that fails for N5 | instance / reason | status |
| --- | --- | --- | --- | --- |
| Davenport-Schinzel / forbidden patterns on per-vertex choice sequences (T52, fe53f69f) | Pettie arXiv 1204.1086 (λ_s); Nivasch 0807.0484 Thm 1.5 | no alternation a…b…a… of length s + 2 for a fixed s | L-RED R137 chooser X: one edge re-adopted 128 times in one W-run (n 362/378) | DEAD (DS-1) |
| Matroid best-response dynamics (T52, T53, 60bb9a56) | Ackermann-Röglin-Vöcking ECCC TR06-067 Thm 3 (upper), Thm 7 (lower) | additive costs on a matroid, so a best reply decomposes into 1-1 exchanges | per-vertex choices form a partition matroid (no 1-2 exchange at one vertex, T53 table), but VJ values are not additive costs | no transfer (READING) |
| Monotone value + levels (T53) | Friedmann arXiv 0901.2731 Thm 8; Koh-Loho 2108.13338 Thm 5.3 | a polynomial level bound for any Ξ-monotone run at a fixed cycle node | Friedmann G_n: switch-all, cycle node fixed, 13·2^n − 9 iterations | DEAD as a template |
| Network-simplex stalling / strongly feasible trees (T54, 96cfda95) | Muramatsu (2000) Lemma 5; Kukharenko-Sanità Thm 1 | a history rule, alternating dual tree or oracle direction; S1's tie-break is static index | abstract LEX-ARENA: runs 2^(L+1) − 2L − 2 (T54-lexarena.py) | DEAD (lex potential alone) |
| Fixed-gain PI (T54) | Zhong-Ye 2609.40147 eq. (7.6); Post-Ye 1208.5083 Lemma 3.4; Scherrer 1306.0386 Lemma 8 | one player and a Dantzig or Howard rule; S4a is neither | – | no transfer |
| Label-correcting orders (T54) | Shier-Witzgall 1981 Results 5-8 | FIFO / pass-based order | LIFO / Pape exponential with weights ~2^n, the parity regime | no transfer |
| LexBFS / LBFS+ multi-sweeps (T55, cd671830) | Corneil et al.; Charbit-Habib-Mouatadid-Naserasr p.3 | a fixed undirected graph with the previous order as tie-break | S1's EVEN branch is a plain BFS on a changing directed arena: 25 / 180 differing choices (u23sw64_n32) | no transfer; LAYER-WINDOW, COUNTER Π(1 + m_d) PROVED (lane) |
| Path algebras / k-stability (T56, 0569df31) | Minoux 1976 Thms 2, 4, 5; Mohri 2002 Thm 1 | k-stable for some poly k, with event counts under adversarial order | fixed-c VJ valuation = max-plus with n-bit weights (ISO, PROVED lane); k-stable ⇔ 0-stable; Shier-Witzgall LIFO type | no bound |
| Tropical pivots (T57, 1eaa8f63) | ABGJ arXiv 1308.0454 Thm 1; 1309.5925 Thm 4.2 / Cor 4.3 | a pivot rule (one exchange per step) | S4a switches sets (u23sw64_n32: 17 / 15 / 6 / …) | no transfer |
| Action elimination, discounted (T58, d78e1815) | Ye MOR 2011 Thm 4.1; HMZ 1008.0530 Lemma 6.4; Scherrer §7-8; Post-Ye Lemma 3.6 | (C): a per-step contraction from the rule (Dantzig or Howard, factor γ) | – (R) and the threshold transfer: ELIM-ORD-β PROVED (lane); the extend form is DEAD (tog6a_n32) | (C) missing |
| Undiscounted windows / Dantzig contraction (T59, c7dc03db) | Zhong-Ye 2609.40147 Thm 7.1, (7.2)-(7.6) | the step captures the largest residual over the REFERENCE's edges (BLOCK-RATIO_K with K = poly) | fx_K16_m16: BLOCK-RATIO 2^32, the gap falls by n² only at the last transition (WINC = \|F\| = 304), HW = 17 | DEAD as a route |
| Arena-optimum rules (T59) | Friedmann arXiv 1106.0778 p.7 (I^glo), §8.2, Thm 8.4 | arena maximality alone excludes exponential windows | H_n: I^glo is an arena optimum and still takes ≥ 2^n steps (stubborn cycles = Ξ-blocked closures) | ARENA-MAX alone insufficient |
| Discounted shadow of HMZ (T59) | HMZ Lemma 5.3-5.5 | GREEDY-IN (the greedy edge lies in the arena); rate 1 − γ = n^−Θ(d) for parity | blocked edges violate GREEDY-IN | C-DISC PROVED (lane), conditional |
| Symmetric SI (T60, 54584c0c) | Schewe-Trivedi-Varghese 1501.06484 §4; van Dijk-Loho-Maat 2309.02223 Thm 1 | a formal settling lemma for the counterstrategy | vDLM: exponential for every rule | no bound |
| Best-response counts (T60) | HMZ Lemma 6.4 (player-1 elimination only); Friedmann LMCS Lemma 6.1 | a rule-free bound from Ξ's monotonicity | G_n under switch-all: σ̄(e_1) flips 2^Θ(n) times | impossible rule-free |
| Monotone comparative statics (T60) | Topkis / Milgrom-Shannon as stated in Etessami et al. 1909.03210 §5.1 | single crossing of −Ξ_t(w) in (w, t) for some order of succ(o) | latew_K16_m32: degree-2 Odd vertex, 32 flips, pair reverses 32 times; gate_K64_n581: 62 / 61; L-SI box 53 thetaA_n7 | DEAD |
| Order charging (T61, 1ad851ee) | Gimbert-Horn LMCS 5(2:9) Thm 4.1, Lemma 4.4; Auger et al. 2102.04922 Thm 23, 29, 30 | (S2) reward-free transit; (S5a) the improving strategy is a function of the order (no-repeat); (S5b) a q^−r value quantum | §3 example (VJ prefixes); gate_K64_n581: 5 head orders, 60 returns; Ξ has 2^Θ(n) values; max \|U_k\| = 64 on latew_K8_m32 | S4 = HEAD-RED; S5a DEAD; S5b = XI-CH-POLY |
- Common reading (READING, not a claim). Every polynomial bound opened uses one of four things:
  - a discount or a polynomial value range: contraction, quantum, or pseudo-polynomial value iteration;
  - a single-exchange (pivot) rule with coordination;
  - reward-free transit between few distinguished values;
  - a fixed order with single crossing.
- N5 inside a W-run has none of these. Its valuations carry 2^rank weights, S4a switches sets, Ξ is two-player while W is
  one-player, and the gap between them (blocked edges, heads) is where every transfer breaks.

## 5. Lower-bound evidence: three quadratic one-W-run families
All three are single W-runs (τ fixed, λ_W fixed, no fallback), built by L-RED. Pins are in experiments/red/.
- **latew** (L-RED R127 caad61ce, R138 5374e0a5; generator span/mkrw.py LATE=1).
  - |F| = 280 at latew_K8_m32 (n 370) and 560 at latew_K16_m32 (n 482).
  - R*_F = K·m (512 at n 482; 640 = 1.19n at n 538).
  - σ̄ flips 2K at one degree-2 Odd vertex (T60), and max |U_k| = 64 at K = 8 (T61).
  - Θ(n²) in total, linear per vertex.
- **fx** (L-RED R137 b656d2a8; span/mkrw.py + free/obsx.py ABOVE=a OWNER=0 BLK=2; pin fx_K8_m32 sha1 e995709e…).
  - |F| = 76 / 152 / 304 at K = 4 / 8 / 16 (m = 16).
  - One edge is adopted K·m/4 + 1 times (FREE returns quadratic).
  - HW = m + 1 regardless of K (T58).
  - BLOCK-RATIO = 2^(2K) (T59).
- **obs / sbq2** (L-RED R142 81a6ffac; R145 4bab6f29).
  - obs_K12_m24: a realised BIP run of 324 transitions (= BIP(σ̄_0, τ_0), quadratic). R142: «There is no super-quadratic BIP run» in its
    data.
  - sbq2_K8_m16 (mkrw LATE=1 → obs2 → obs3): σ̄ flips K·m times at ONE Odd vertex of out-degree 2 in one W-run (512 at n 517). SB per
    vertex is quadratic.
- What the evidence shows (DATA): every count in §2-§3 has been driven to Θ(n²) inside one W-run (|F|, R*, FREE, SB per vertex, ΞCH).
  None has been driven beyond quadratic. L-RED R144 (composition does not multiply).
- R140 (DECEL-RED) and T59 §3 say what a super-quadratic family would need: Ξ-blocked closures released in counter order (R135 waiting
  gates with fresh patterns, R136). None is built.
- No super-polynomial lower bound for N5 is known. No polynomial upper bound is known. Both are OPEN.

## 6. The question for an expert, in one sentence
- Inside one W-run of N5, Even improves a one-player valuation W (against a fixed τ) by arena optima. The arenas are cut by a two-player
  valuation Ξ (against Odd's best reply σ̄).
- Must the number of Ξ-changes at a vertex be polynomial (XI-CH-POLY), given that:
  - every opened technique needs a discount, a quantum, a pivot rule, reward-free transit or single crossing, which N5 lacks;
  - every adversarial family so far stops at Θ(n²)?

## DONE / FINDINGS / NEEDS
- DONE: this note (no new claims).
- FINDINGS:
  1. The core is XI-CH-POLY, equivalently WRUN-POLY (R95 pending) or HEAD-RED′'s three counts (lane).
  2. Seventeen technique rows (T52-T61), each with its nearest theorem, the failing hypothesis and the instance.
  3. latew, fx and obs/sbq2 are all quadratic inside one W-run; nothing super-quadratic is known.
- NEEDS: none from the owner. Any contact with an expert is the owner's decision (HUMAN-DESK).
