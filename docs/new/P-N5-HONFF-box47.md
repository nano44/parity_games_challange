# Packet P-N5-HONFF (box 47): an in-phase Even fallback is a Bellman-Ford step for Ξ (Lemma FB-RISE), so in every phase of N5 the W-honest states number at most 4n² − 3n with no fallback term (Theorem HON-FF), and the D = ∅ part of every phase is O(n²) states (HON-0-FF) — every game
L-NEW successor 26 (Opus 5.5), D14 / D18, Lead reading L40; Lead's word of 11:48Z (Lead's stamp): "THEN freeze packet P-N5-HONFF-box47: FB-RISE (both forms), Theorem HON-FF, HON-0-FF, REC-1-FF (a) as PROVED; REC-1-FF (c), (d) as implications.". Written 2026-10-26 11:56Z onward (date -u). FROZEN at push: later text goes
into a fixes file.
Source: docs/new/N5-HONFF-box47.md (working doc, l-new 4881a1e7 … 385a5534; this packet governs). Tools: experiments/new/box47/ffdeep.py.
Labels: PROVED (L-NEW 26, unrefereed) / IMPLICATION / OPEN / DATA / READING. Not a TARGET.md claim. Nothing here bounds N5's running time on any
class; HON-FF is a count of one kind of state. It does NOT bound f (the in-phase fallbacks per phase) on any class: it removes f from the
count of W-honest states only (§4). G-N5-TIME stays open.
Relation to P-N5-HON (frozen, sha1 07f8e767cfca12d29c8f6f2e3f03358326abbef1; signed by REFEREE-2 16 and REFEREE 14, no gap; to land as RESULTS R68; notes in docs/new/P-N5-HON-fixes-box46.md, sha1
54985acfbfb0feb0e8bb3b04d882df78eaf72f1b, l-new 0238b1cb): this packet proves that
packet's CONJECTURE HON-FF (its §5) and so strengthens its Lemma HON / Corollary HON′ / HON-0 / REC-1 (a); it does not edit or replace them.

## To sign, and what is not to sign
| § | statement | label |
| --- | --- | --- |
| §1 | Lemma FB-RISE, general form: at an in-phase S4c fallback t → t + 1, LEV(t + 1) ≥ min(LEV(t) + 1, LEV_odd(t), n − 1) | PROVED (to sign) |
| §1 | Lemma FB-RISE, honest form: if a W-honest state h ≤ t lies in the phase, LEV(t + 1) ≥ min(LEV(h) + 1, n − 1) | PROVED (to sign) |
| §2 | Theorem HON-FF: the W-honest states of a phase number ≤ 4n² − 3n | PROVED (to sign) |
| §2 | Corollary HON-0-FF (D = ∅ states, N_0, D = ∅-epoch transitions ≤ 4n² − 3n); Corollary REC-1-FF (a) ({u}-intervals ≤ 1 + 4n² − 3n + X_dir + X_big) | PROVED (to sign) |
| §2 | Corollary REC-1-FF (c), (d) (P-N5-HON's REC-1 (c), (d) with f deleted) | IMPLICATION from (Στ) (to sign as an implication) |
| §3 | data | DATA (not to sign) |
| §4 | what FB-RISE does not give (f per phase) | OPEN / READING (not to sign) |
- Premises (LANDED or signed):
  - SPEC S1-S5 of docs/new/N5-ssi-global.md (FIX 1-4, Q1-Q4); in particular S2 (Iσ(x) = {w ∈ succ(x) : Ξ(w) ≻ Ξ(σ(x))}), S4c (Even's fallback
    switches every x with Iσ(x) ≠ ∅ to the (Ξ(w), w)-maximum of Iσ(x)) and FIX 3 (an Even fallback leaves τ; so an in-phase fallback is Even's).
    Standing premise 1E-N3 (RESULTS R57), as in P-N5-HON.
  - (MON): RESULTS R15 (a) with R15 (d) (Ξ non-decreasing along a run, S4c fallbacks included: every N5 iteration is Switch_I with ∅ ≠ I ⊆ Iσ or
    ⊆ Iτ).
  - RESULTS R17 (a) (V1), (V2); RESULTS R17 (b) Lemma P, its Case A only (box 10 §2, A1 and A2), applied with Ω := Ξ_t (question Q-A below).
  - P-N5-HON (signed by both, to land as RESULTS R68): Lemma HON's proof (steps 0-3), Lemma SAT0's Odd case with REFEREE-2's wording N-HON-1, Corollary HON-0's proof, Theorem
    REC-1's proof. RESULTS R21 (a) XW and R23 (g) WM enter only through HON step 1 (fallback-free gaps).
  - For the IMPLICATIONS only: premise (Στ) as in P-N5-HON §3 / RESULTS R64 (e); RESULTS R65 (landed) finds it to hold at audit strength.
- QUESTION Q-A for the referees. §1 applies Lemma P's Case A (A1, A2) with Ω := Ξ_t, the valuation of the strategy pair (σ_t, σ̄_t), and with
  S2's Iσ_t as the improving set. As I read box 10 §2, Case A uses only: Ω(z) ⪯ Ω(ρ(x)) with ρ := σ_t; the bound Ω(z) ⪰ value(r′); (V1) for Ω at
  the Even x (Ω(x) = x ⊕ Ω(ρ(x)), and ρ(x)'s path to λ(x) avoids x, when x is not its own cycle node; Ω(ρ(x)) has cycle node x when it is); and
  (V2). It does not use that Ω is a one-player valuation (P-N5-HON's SAT0 uses it with Ω := W). Please confirm.

## 0. Setting (every game)
- N5 = SPEC S1-S5. State k = (σ_k, τ_k); σ̄_k = S1's Odd counterstrategy to σ_k; Ξ_k := V_{σ_k,σ̄_k} (the value of the HONEST play, which
  follows σ_k at Even and σ̄_k at Odd vertices); W_k := V_{σ_k,τ_k}; λ := Ξ's cycle-node map. A PHASE P: a maximal run with (λ, τ) constant
  (RESULTS R38 (a)); an in-phase transition has both ends in P. k is W-HONEST if Ξ_k = W_k pointwise.
- G_τ: G with every Odd v cut to τ(v). For a cycle node u of λ (λ(u) = u) and a simple path r of G_τ from x to u: value(r) := (u, P(r), |r|),
  P(r) := the vertices of r before u more relevant than u (R17 Lemma P). LEV(k) := the largest j ≤ n − 1 such that Ξ_k(x) ⪰ value(r) for every
  vertex x and every such r with ≤ j edges (as P-N5-HON §0). LEV_odd(k): the same, with x ranging over the Odd vertices only (r still runs
  through any vertices). So LEV(k) ≤ LEV_odd(k).

## 1. Lemma FB-RISE (PROVED, every game)
Statement. Let t → t + 1 be an in-phase S4c fallback of a phase P, and j := min(LEV(t) + 1, LEV_odd(t), n − 1).
(a) (General form.) LEV(t + 1) ≥ j.
(b) (Honest form.) If h ≤ t is a W-honest state of P, then LEV(t + 1) ≥ min(LEV(h) + 1, n − 1).
Proof of (a). In-phase, so τ_{t+1} = τ_t and, by FIX 3, the fallback is Even's: σ_{t+1}(x) = z*(x) := the (Ξ_t(w), w)-maximum of Iσ_t(x) for
every Even x with Iσ_t(x) ≠ ∅, and σ_{t+1}(x) = σ_t(x) otherwise. Both t and t + 1 lie in P, so λ_{t+1} = λ_t = λ.
Let x be a vertex, u a cycle node of λ and r a simple path of G_τ from x to u with |r| ≤ j; we show Ξ_{t+1}(x) ⪰ value(r). If |r| = 0 then
x = u and Ξ_{t+1}(u) = (u, ∅, 0) = value(r). Otherwise write r = x → z → r′: r′ is a simple path of G_τ from z to u that avoids x, and |r′| ≤
j − 1 ≤ LEV(t), so Ξ_t(z) ⪰ value(r′).
1. x Odd. |r| ≤ j ≤ LEV_odd(t), so Ξ_t(x) ⪰ value(r), and Ξ_{t+1}(x) ⪰ Ξ_t(x) (MON).
2. x Even and z ∉ Iσ_t(x), i.e. Ξ_t(z) ⪯ Ξ_t(σ_t(x)). Lemma P's Case A (A1 if λ(x) ≠ x, A2 if λ(x) = x) with Ω := Ξ_t, ρ := σ_t (Q-A) gives
   value(r) ⪯ Ξ_t(x) ⪯ Ξ_{t+1}(x) (MON). This covers every Even x that the fallback does not switch, and every non-improving edge of one it does.
3. x Even and z ∈ Iσ_t(x). Then x is switched, σ_{t+1}(x) = z* := z*(x), and Ξ_t(z*) ⪰ Ξ_t(z) ⪰ value(r′) (z* maximises Ξ_t over Iσ_t(x) ∋ z);
   by (MON) Ξ_{t+1}(z*) ⪰ value(r′).
   3a. λ(x) ≠ x. By (V1) at t + 1 (x's honest play is x followed by z*'s), Ξ_{t+1}(x) = x ⊕ Ξ_{t+1}(z*), and z*'s honest path at t + 1 to λ(x)
       avoids x. r′ avoids x. By (V2) (both paths avoid x, or the cycle nodes differ), Ξ_{t+1}(x) ⪰ x ⊕ value(r′) = value(r).
   3b. λ(x) = x. Then Ξ_{t+1}(x) = (x, ∅, 0), and z* = σ_{t+1}(x) has an honest play at t + 1 that returns to x, so λ(z*) = x and Ξ_t(z*) has cycle
       node x. value(r′) has cycle node u, and u ≠ x since r is simple with |r| ≥ 1. Ξ_t(z*) ⪰ value(r′) with different cycle nodes means x is
       better than u, so (x, ∅, 0) ≻ value(r). □
Proof of (b). If LEV(h) = n − 1 then LEV(t + 1) ≥ LEV(h) by (MON) (HON step 0). Let L := LEV(h) ≤ n − 2; by (MON), LEV(t) ≥ L. For an Odd x
and r = x → τ(x) → r′ with |r′| ≤ L: at h, W_h(τ(x)) = Ξ_h(τ(x)) ⪰ value(r′) (h is W-honest, LEV(h) = L), and the W-cycle nodes at h are those
of λ (W_h = Ξ_h). SAT0's Odd case at h (with N-HON-1's wording) gives W_h(x) ⪰ value(r). So Ξ_t(x) ⪰ Ξ_h(x) = W_h(x) ⪰ value(r) (MON):
LEV_odd(t) ≥ L + 1. By (a), LEV(t + 1) ≥ min(LEV(t) + 1, LEV_odd(t), n − 1) ≥ min(L + 1, n − 1). □
- READING. S4c, read in the Ξ frame, is Lemma P's relaxation at the Even vertices; Case B needs only Ξ_t(z*) ⪰ Ξ_t(z) and (MON), not that
  σ_{t+1} is an arena optimum. An S4a step is not such a relaxation (it optimises W over the Ξ-gated arena), which is why the immediate-rise
  conjectures IMM and IMM′ are false (P-N5-HON §5). Odd vertices are not relaxed by Even's move; a W-honest state puts them one level ahead.

## 2. Theorem HON-FF and corollaries (PROVED, every game; REC-1-FF (c), (d) IMPLICATIONS)
Theorem HON-FF. In every phase P of N5, the W-honest states number at most 4n² − 3n.
Proof. Lemma HON's proof (P-N5-HON §1), with step 3's fallback clause replaced. Let h_1 < … < h_N be the W-honest states of P and h_1, …, h_s
the unsaturated ones (LEV ≤ n − 2; step 2: saturation is inherited, step 0). For i < s, every transition of the gap h_i → … → h_{i+1} is
in-phase. If none of them is an S4c fallback, step 1 gives LEV(h_{i+1}) ≥ LEV(h_i) + 1. Otherwise let t ∈ [h_i, h_{i+1} − 1] be the source of
one of its fallbacks: FB-RISE (b) with h := h_i gives LEV(t + 1) ≥ LEV(h_i) + 1 (LEV(h_i) ≤ n − 2), and LEV(h_{i+1}) ≥ LEV(t + 1) (step 0).
So LEV rises across every one of the s − 1 gaps; with 0 ≤ LEV(h_1) and LEV(h_s) ≤ n − 2, s − 1 ≤ n − 2. The saturated part is step 3's:
N − s ≤ 4n(n − 1) + 1. Hence N ≤ (n − 1) + 4n(n − 1) + 1 = 4n² − 3n. □
- What is replaced, exactly (REFEREE 14's note HON-N3 on P-N5-HON: both uses of the fallback-free hypothesis, the rise and the sandwich). A gap
  that contains a fallback does not use step 1: FB-RISE uses no W-value, no WM step and no W-cycle node after h; at h it uses Ξ_h = W_h and
  λ_W = λ, which are honesty. A fallback-free gap uses step 1 as signed, with both hypotheses in force.
Corollary HON-0-FF. In every phase P: (a) the D = ∅ states, (b) N_0 (the epochs with D_E = ∅), (c) the in-phase transitions whose source lies in
a D = ∅ epoch each number at most 4n² − 3n. Proof: P-N5-HON §2's proof of HON-0, with HON-FF in place of HON. □
- Against REC-0 (P-N5-REC0, landed as RESULTS R66): (f + 1)(n + 1) + 4n(n − 1) + 1 − (4n² − 3n) = f(n + 1) + 2 > 0 for every f ≥ 0, n ≥ 1.
Corollary REC-1-FF. P-N5-HON §4 Theorem REC-1 with f deleted: (a) the {u}-intervals of P, over all u ∈ Q, number at most 1 + (4n² − 3n) + X_dir
+ X_big (PROVED); (c) the |D_k| = 1 states, and the epochs with |D_E| = 1, number at most (1 + 4n² − 3n + X_dir + X_big)·(T*_Q + 2); (d) if every
state of P has |D_k| ≤ 1, P has at most (4n² − 3n) + (1 + 4n² − 3n + X_dir)·(T*_Q + 2) states ((c), (d): IMPLICATIONS from (Στ), through EP-1u).
Proof: REC-1's proof; f enters it only through HON-0 (a). □

## 3. DATA (not to sign; experiments/new/box47/ffdeep.py, outputs in experiments/new/box47/out/)
Exact LEV and LEV_odd by simple-path DFS with a budget (UNK = over budget, skipped). GEN_V = (a) fails; FBRISE_V = (b) fails; CTRL_T = the
control "LEV(t + 1) ≥ min(LEV(t) + 1, n − 1)" (no Odd term; not claimed) fails; GEN_ODDBIND = LEV_odd(t) ≤ LEV(t); XI_AT = LEV(t) ≥ LEV(h) + 1
already at the fallback's source.
| sample | runs | non-honest in-phase fallbacks | GEN_V | CTRL_T (control) | GEN_ODDBIND | after a W-honest state | FBRISE_V | XI_AT | DEEP | STEP_V |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all pinned instances of experiments/ and docs/referee*/ (735 files, out/liball.txt), n ≤ 20, S3 + 6 random, seed 5 | 2,128 | 269 | 0 | 79 | 79 | 0 | — | — | — | 0 |
| random 3,000 𝒞^kO (n 5-18, gseed 111), S3 + 4 random, seed 8 | 15,000 | 7 | 0 | 4 | 4 | 0 | — | — | — | 0 |
| random 3,000 𝒞^kO (n 6-24, gseed 222), S3 + 4 random, seed 9 | 15,000 | 3 | 0 | 2 | 2 | 0 | — | — | — | 0 |
| L-COMP 5's pinned gaps (l-comp 15bcfa06, experiments/n5-epoch/instances): ffin12_n32 (sha1 6bae375b…), ffin5_n32 (d20ea0f2…), ffin4_n24 (e1c4043c…), each with its .start, budget 3·10⁷ | 3 | 21 | 0 | 20 | 20 | 21 | 0 | 21 | 0 | 0 |
| experiments/red/xing/instances j10_n24, j7_n32, j8_n32, S3, budget 3·10⁷ | 3 | 4 | 0 | 4 | 4 | 4 | 0 | 4 | 0 | 0 |
| the 735-file list, n ≤ 34, S3 + 2 random, seed 6, budget 3·10⁶ (UNK 15 phases skipped) | 1,527 | 724 | 0 | 527 | 526 (+1 UNK) | 3 | 0 | 3 | 0 | 0 |
| lib41 (experiments/new/box41/lib41.txt), n ≤ 34, S3 + 2 random, seed 7, budget 3·10⁶ (UNK 14; GEN not in the script for this row) | 816 | 560 | — | 402 | — | 3 | 0 | 3 | 0 | 0 |
- Every failure of the control has the Odd term binding (one more hit the budget before LEV_odd was computed): the checker sees failed rises.
- The six known gaps with an inside fallback (j10_n24, j7_n32, j8_n32; L-COMP 5's ffin12_n32, ffin5_n32, ffin4_n24) have 25 inside fallbacks,
  all with FBRISE_V = 0 and XI_AT (the Ξ-level had reached LEV(h) + 1 before the fallback). L-COMP 5's own HON-FF checker (l-comp 15bcfa06,
  experiments/n5-epoch/README.md "Add-on", relayed by the Lead): 0 failures, about 46,000 inside-fallback gaps checked along its climbs.

## 4. OPEN, and what FB-RISE does not give (READING)
- f per phase on general games (RESULTS R56's ρ question) is not bounded here: a fallback whose source has LEV_odd(t) ≤ LEV(t) (an Odd vertex of
  D undercutting its τ-path) need not raise LEV, and the data have many such (CTRL_T). Fallbacks with no W-honest state before them in the phase
  are not touched by (b).
- For phases with all |D_k| ≤ 1, REC-1-FF (d) leaves X_dir as the only unbounded term (docs/new/N5-XDIR-box47.md, Corollary XD-ρ: X_dir ≤ the
  ρ events at the leaving vertex plus flat exits).

## 5. Quotes and pins (checked by script)
Every quote below, set in curly double quotes, is verbatim from the file and line named, at l-new 0238b1cb (trunk fb3302f5 merged at 2600a860).
- SPEC S4c, docs/new/N5-ssi-global.md (sha1 66fde9ef1726602fc0a52ca8d6d6fe8cbbcf110e) l. 56-57: “FALLBACK, if σ_new = σ and τ_new = τ: if Iσ ≠ ∅,
  for every Even v with an improving edge set σ_new(v) = the w with (v, w) ∈ Iσ maximising (Ξσ(w), w) (best valuation, ties: larger index);
  otherwise do the same for Odd on Iτ with G^d's valuations.” FIX 3, l. 88: “In a fallback iteration with Iσ ≠ ∅ only σ changes (τ_new = τ)”;
  “Odd falls back only if Iσ = ∅.”
- (MON): RESULTS R15 (a), docs/RESULTS.md l. 631: “Lemma A: for any non-empty unambiguous set I of improvements of σ (VJ00 §4.4), Ωσ ⊴
  Ω_{Switch_I(σ)}.” R15 (d), l. 640: “N5: every iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ (on G) and/or with ∅ ≠ I ⊆ Iτ to Odd's τ
  (on G^d)”. P-N5-HON step 0, docs/new/P-N5-HON-box46.md l. 56: “LEV is non-decreasing along P: Ξ_{k+1} ⊵ Ξ_k (R15 (a))”.
- (V1), (V2): docs/new/N5-phase-bound-box10.md (sha1 e1a275294232ca4d94d44952fa91312b2f1fcf2e) l. 20-21: “(V1) if x is not its own cycle node then
  Ω_ρ(x) = x ⊕ Ω_ρ(ρ(x)) and the ρ-path from ρ(x) to λ(x) avoids x.” and “(V2) PREFIX MONOTONICITY: if a ⪯ b are values whose paths both avoid x
  (or whose cycle nodes differ), then x ⊕ a ⪯ x ⊕ b”.
- Lemma P's Case A: box 10 l. 32: “Case A: (x, z) ∉ I_k, i.e. Ω_k(z) ⪯ Ω_k(ρ_k(x)). So value(r') ⪯ Ω_k(ρ_k(x)) (transitivity).”; l. 33: “A1: x is not
  its own cycle node.”; l. 36: “A2: x = λ_k(x) (its own cycle node), so Ω_k(x) = (x, ∅, 0).” P-N5-HON's SAT0 uses it the same way, l. 84-85:
  “Lemma P's Case A (A1, A2), which uses only this inequality, the induction hypothesis, (V1) and (V2), gives value(r) ⪯ W_k(x).” REFEREE on that
  sentence, docs/referee/R-N5-HON.md l. 68-69: “the packet's "uses only this inequality, the induction hypothesis, (V1) and (V2)" is exact.”
- SAT0's Odd case: P-N5-HON l. 86: “If x is not its own W-cycle node, W_k(x) = x ⊕ W_k(z) ⪰ x ⊕ value(r′) = value(r) by (V1), (V2)”, read with
  N-HON-1 as settled (docs/referee-2/R2-N5-HON.md l. 142: “keep N-HON-1 as a wording note ("z's path to its cycle node avoids x")”; fixes file
  docs/new/P-N5-HON-fixes-box46.md §2). Own-cycle-node case, l. 88: “W_k(z) ⪰ value(r′) then forces x better than c, so W_k(x) ≻ value(r).”
- HON-N3: R-N5-HON.md l. 170: “so a proof of HON-FF has to replace both, not only the first.” (§2's "What is replaced, exactly".)
- Pins: P-N5-HON-box46.md sha1 07f8e767cfca12d29c8f6f2e3f03358326abbef1; P-N5-HON-fixes-box46.md sha1 54985acfbfb0feb0e8bb3b04d882df78eaf72f1b;
  working doc docs/new/N5-HONFF-box47.md sha1 544ae76a5d22b046151daa7eba8eede60d8513b2 (l-new 385a5534); experiments/new/box47/ffdeep.py sha1 92b39f601fa9c04013b659372ed073abc5c8dca1.
- Script: `python3 experiments/new/box47/quotecheck.py docs/new/P-N5-HONFF-box47.md 0238b1cb docs/new/N5-ssi-global.md docs/RESULTS.md
  docs/new/P-N5-HON-box46.md docs/new/N5-phase-bound-box10.md docs/referee/R-N5-HON.md docs/referee-2/R2-N5-HON.md` (output
  experiments/new/box47/out/quotecheck_honff.txt); every quote found at the line cited, none missing.
