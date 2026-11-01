# R170 TWO-FIX windows: freezing the Odd vertices where σ̄ = τ turns a window into an N5 run on a game with ODIFF Odd choice vertices (FREEZE), so ODIFF ≤ 1 windows are polynomial (R17 / R51); quadratic windows exist at ODIFF = Θ(n) (runquad, R106), none beyond c·n·(ODIFF + 1) is known (L-RED successor 40)
Started 2026-11-01 02:51Z (date -u), written ~03:2xZ. Lead brief (R170): attack L-NEW box 121's Lemma TWO-FIX; target a family of TWO-FIX
windows longer than any polynomial, or at least super-quadratic, ideally with ODIFF 1 or 2; if ODIFF-bounded windows are provably short,
state the obstruction with the instance (L-NEW box 122). Labels: PROVED (lane) = proved here, not refereed; DATA; READING; CONJECTURE; OPEN.
L-LIT T64 (one-player pivot rules) had NOT landed when this was written (claude/l-lit 49d4bd41 has T60-T63 only); nothing here uses it. (It landed at claude/l-lit 6895fb31 after this was written, with L-NEW box 122
(claude/l-new 4c889bba); both are for the next box.)
Not a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Answer
- No super-quadratic and no super-polynomial TWO-FIX family was found. ODIFF ≤ 1 cannot give one:
  - Lemma FREEZE (PROVED, lane, §1): a TWO-FIX window is an initial segment of the N5 run, from (σ_a, τ_a), on the game G_F in which
    every Odd vertex with σ̄ = τ keeps only that edge. G_F has exactly ODIFF Odd choice vertices.
  - Hence ODIFF = 0 windows are one-player N5 runs (RESULTS R17: < (n² − n + 1)(n + m)), and ODIFF = 1 windows are 𝒞^1O runs
    (RESULTS R51 (a), any start pair: ≤ (n(n − 1) + d_o)(T* + 1) = O(m·Δ·d_o·n¹³)). Both polynomial. Hypothesis (NT) of §1 is
    needed only when some ODIFF vertex has I_τ ≠ ∅; REPLAY (§2) held at all 1,157 corpus windows and every build tried.
  - Conversely every τ- and σ̄-constant segment of an N5 run on a 𝒞^kO game is a TWO-FIX window with ODIFF ≤ k. So
    «TWO-FIX windows are polynomial for ODIFF ≤ k» is the same question as «τ-constant epochs (RESULTS R61's word) of N5 on 𝒞^kO are
    polynomial». For k ≥ 2 it is OPEN.
- Quadratic windows EXIST, but with ODIFF = Θ(n) (DATA, §3): L-RED's own R106 family runquad (mkr.py K, m = 4K) is ONE fallback-free
  TWO-FIX window of L = 4K² + 3K − 1 transitions at n = 24K + 6 (K 2..12: 21 … 611), with ODIFF = 4K = (n − 6)/6. Box 121's s3quad_K8_m30
  is this family's K = 8 member embedded for the S3 start.
  - Every one of the 4K ODIFF vertices is load-bearing: freezing any one of them to τ or to σ̄ costs a ladder level (oreduce.py, §4).
  - So for fixed ODIFF, runquad's L is LINEAR in n: L ≈ (ODIFF/4)(m + 3) with n ≈ 3m + 3·ODIFF.
- Every window measured satisfies FFSEG ≤ 1.5·n·(ODIFF + 1), with FFSEG the longest fallback-free stretch (DATA, §3: corpus 1,132 runs,
  54 climbs at n 8-64 with KO 0-3 Odd choice vertices (16 forced to ODIFF ≥ 1 / 2), runquad, the box 121 builds). The largest ratio, 1.5, is at ODIFF 0: a
  one-player climb at n 8 (L 12). The largest corpus ratio is block_bk32, ODIFF 0, 49 at n 36.
- CONJECTURE TWO-FIX-NL (proposed as L-NEW box 122's target): every fallback-free stretch of a TWO-FIX window has at most c·n·(ODIFF + 1)
  transitions, with c = 2 consistent with all data. With FREEZE and RESULTS R48 this would give O(n⁴) windows at ODIFF 1. The PROVED
  part (§1) is the polynomial bound for ODIFF ≤ 1. The conjecture's content is «linear per portal».
- Obstruction to small ODIFF (READING, §4): in runquad, each ladder level needs its own pair of two-faced Odd vertices. One (C_i) shows
  Ξ the η-ladder and shows W the gate route. The other (the W-loop T_i) is the gate's closed state in G_τ and the escape into the reactor
  chain in G_σ̄. With one shared portal, both worlds see the same prefix after it. In a one-player game (ODIFF 0) the pivot that is behind
  can reach the other pivot's newer, better value through the reactor chain, so it takes it at once: no gate, no wave wait.

## 1. Lemma FREEZE (PROVED, lane)
- Setting: N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md), under the standing SPEC premise of RESULTS R57 (S1's procedure realises the
  pointwise optimum). Window: L-NEW box 121 §4: a ≤ j ≤ b with τ_j = τ and σ̄_j = σ̄ (σ̄_j := si.Engine's / S1's optimal counterstrategy
  to σ_j). D := {o Odd : σ̄(o) ≠ τ(o)}, ODIFF := |D|. G_F := G with succ_F(v) := {τ(v)} for every Odd v ∉ D (where τ(v) = σ̄(v)), all
  other edges kept. G_F is a game (every vertex keeps a successor). Its Odd vertices of out-degree > 1 are exactly D, since each o ∈ D has
  σ̄(o) ≠ τ(o), two distinct successors.
- (NT): for every a ≤ j < b and every o ∈ D with I_τ(o) ≠ ∅, τ(o) is the only successor in {τ(o)} ∪ I_τ(o) that attains Odd's pointwise
  optimum at o in S4b's arena H′ against σ_j.
- Statement: under (NT), the states (σ_j, τ_j), a ≤ j ≤ b, are the first b − a + 1 states of the N5 run on G_F from the start pair
  (σ_a, τ_a).
- Proof: induction on j. Assume state j (a ≤ j < b) agrees on G and G_F, and compare SPEC's steps.
  - S1, Ξ_j: on both games Ξ_j(x) = min over positional Odd ρ of val(σ_j, ρ)(x) (R57 premise; RESULTS R18 (d) Lemma S (a)). G_F's
    Odd strategies are a subset of G's, and they contain σ̄ (σ̄ = τ off D, and σ̄ is an edge of G_F on D). So the minimum is the same at
    every x: Ξ_j^F = Ξ_j. Hence S2 gives I_σ^F = I_σ, since Even's edges are unchanged.
  - S1 on G^d, Ξ_τ: the dual procedure for the fixed τ runs on the graph in which every Odd vertex keeps only τ(v) and every Even vertex
    keeps all its edges. That graph is the same for G and G_F, so Ξ_τ and τ̄ are identical outputs, with no premise needed.
    I_τ^F(v) = I_τ(v) ∩ succ_F(v): I_τ(o) for o ∈ D, and ∅ off D (the only edge there is τ(v)).
  - S4a: arena H has Even edges {σ_j(v)} ∪ I_σ(v) and Odd edges {τ(v)}. This is the same arena on G and G_F (τ(v) ∈ succ_F(v)), so
    S4a's output is the same σ_new.
  - S4b: if I_τ^F = ∅, τ_new^F = τ. Otherwise H′_F ⊆ H′ (fewer options off D, the same on D) and τ ∈ H′_F. τ is the pointwise optimum
    in H′ (τ_new = τ on G, R57 premise), so it is one in H′_F, and the optimum values agree. Off D, S1's output is τ(v), the only edge.
    On D, (NT) makes τ(o) the only optimal choice, so S1's output is τ(o). Hence τ_new^F = τ.
  - S4c: identical inputs (σ_new, τ_new, I_σ, Ξ_j), so identical outputs. In a window I_σ ≠ ∅ at every j < b (box 121 TWO-FIX (ii)),
    so only Even's fallback branch can occur. ∎
- Corollary FREEZE-01 (PROVED, lane):
  - ODIFF = 0: G_F has no Odd choice vertex (one-player), so b − a < (n² − n + 1)(n + m) (RESULTS R17; start-free per
    docs/referee/R-N5-START.md, its supporting row).
  - ODIFF = 1: G_F ∈ 𝒞^1O with d_o = deg_G(o), so b − a ≤ (n(n − 1) + d_o)(T*(n, m, Δ, d_o) + 1) (RESULTS R51 (a), «from any start pair»;
    start-free per R51 (b)). Polynomial.
  - (NT) is needed only if I_τ(o) ≠ ∅ for the ODIFF vertex. When τ is optimal for Odd (I_τ = ∅; the case in b5_os_n40, returns_ph64 and
    runquad), FREEZE holds unconditionally (given R57's premise).
- Corollary FREEZE-k (PROVED, lane): the longest TWO-FIX window with ODIFF ≤ k, over games with n vertices and m edges, equals the
  longest τ- and σ̄-constant segment of an N5 run over 𝒞^(≤k)O games with n vertices and ≤ m edges (under (NT)). «≤» is FREEZE.
  «≥» holds because such a segment is itself a window (its game's non-choice Odd vertices have one edge, so σ̄ = τ there).
- What FREEZE does not give: any bound for ODIFF ≥ 2 (the 𝒞^2O / 𝒞^kO line, RESULTS R58 / R61, bounds fallbacks per phase only, not
  transitions), and nothing for windows that end because σ̄ or τ moves.

## 2. DATA: REPLAY (freeze.py: the window's states equal the first L + 1 states of the G_F run)
| set | runs | windows (L ≥ 2) | REPLAY False | notes |
| --- | --- | --- | --- | --- |
| box 53 corpus (new/box59/sbcg.lst + si/root/logs/alt_all.lst, repaired starts as box121/runcorp.sh) | 1,132 | 1,157 | 0 | out/corp.txt |
| box 121 builds cp_K4, suf_K8, s3quad_K8_m30, b5_os_n40, lend107_n32 (+start), returns_ph64, fbA_K8 | 7 | 6 long | 0 | ODIFF 16 / 32 / 32 / 1 / 3 / 1 |
| runquad (mkr.py K, 4K), K = 2, 4, 6, 8, 10, 12, pins runquad_K3_m4_n54, runquad_K8_m30_n192 | 8 | 8 | 0 | out/rq_big.txt |
| climb champions (§3) | 54 | all | 0 | out/champs.txt (the 38 unfiltered ones re-run through freeze.py) |

## 3. DATA: window length against n and ODIFF
| family / source | n | ODIFF | L (fallbacks) | FFSEG | FFSEG / (n(ODIFF + 1)) |
| --- | --- | --- | --- | --- | --- |
| runquad K 2 / 4 / 6 / 8 / 10 / 12 (m = 4K) | 54 / 102 / 150 / 198 / 246 / 294 | 8 / 16 / 24 / 32 / 40 / 48 | 21 / 75 / 161 / 279 / 429 / 611 (0) | = L | ≤ 0.05 |
| pin runquad_K8_m30_n192 (R106) | 192 | 32 | 263 (0) | 263 | 0.042 |
| s3quad_K8_m30 (box 121) | 479 | 32 | 263 (0) | 263 | 0.017 |
| cp_K4 / suf_K8 (box 121) | 192 / 199 | 16 / 32 | 43 / 151 (0) | = L | ≤ 0.03 |
| b5_os_n40 / returns_ph64 / lend107_n32 | 40 / 64 / 32 | 1 / 1 / 3 | 77 (9) / 93 (15) / 107 (10) | 17 / 9 / 15 | 0.21 / 0.07 / 0.12 |
| corpus maximum (block_bk32) | 36 | 0 | 49 (0) | 49 | 1.36 |
| climbs KO = 0, one-player, MAXDEG n − 1 (climbp_n8..n20) | 8 / 10 / 12 / 16 / 20 | 0 | 12 / 15 / 15 / 21 / 29 | = L | 1.50 / 1.50 / 1.25 / 1.31 / 1.45 |
| climbs KO = 1-3, unfiltered (champions' windows have ODIFF 0, one has 1: σ̄ = τ even where Odd can choose) | 12 / 16 / 24 / 32 / 64 | 0 | best 16 / 20 / 27 / 37 / 58 | = L | ≤ 1.33 |
| climbs MINODIFF = 1 (window must have ODIFF ≥ 1; KO = 1) | 12 / 16 / 24 / 32 | 1 | best 11 / 18 / 23 / 33 | = L | ≤ 0.56 (L/n ≤ 1.13) |
| climbs MINODIFF = 2 (KO = 2) | 12 / 16 / 24 / 32 | 2 | best 8 / 17 / 20 / 23 | = L | ≤ 0.36 (L/n ≤ 1.06) |
- Climbs: climb170.py (genome = game + valid start; score = longest fallback-free window; 20,000 mutations each; 54 climbs: 33 unfiltered
  KO 0-3 at n 12-64, 5 one-player dense (MAXDEG n − 1) at n 8-20, 16 with MINODIFF = KO at n 12-32; the n 48 runs were stopped by me and
  are not reported). Champions: out/champs.txt (freeze.py lines). Every best is ≈ n: no super-linear growth at fixed ODIFF. The
  unfiltered climbs found only ODIFF 0 windows, so only the MINODIFF rows speak for ODIFF ≥ 1.
- runquad: L = K(m + 3) − 1 (R106 §3), so at fixed K (fixed ODIFF = 4K) L is linear in m, i.e. in n. Quadratic only along m = 4K.
- Score items asked for: runquad_K8_m30_n192 startck OK; Oink 8fbf0a7 --zlk + verify «OINK OK» (rel2/oinkcmp.sh); xeng «state sequences
  identical: True»; r167/score167.py: |F| 0 (wruns [], no W-run of the kind score167 counts), |F|/n² 0.0000. Same for runquad_K3_m4_n54.

## 4. ODIFF reduction on runquad (oreduce.py), and the obstruction (READING)
- Greedy cuts on mkr.py K 4, m 16 (n 102, L 75, ODIFF 16), keeping a cut while L ≥ 0.5 × current: each cut of a ladder vertex costs a
  level. C3 → MP3: L 54; then T1 → T1: 35; then Tp1 → Gp1: 18; ending at ODIFF 0 with L 19 (log in out/oreduce_K4.txt). No ODIFF vertex
  is free.
- Why (READING, from R106 §2 and the run): Is comes from G_σ̄ and the choice from G_τ (TWO-FIX).
  - h's next level C_(i+1) must be Ξ-improving: G_σ̄ shows the η-ladder via Bq → EQ.
  - h's next level must also be withheld by G_τ until the reactor wave reaches r_m: G_τ shows MP_(i+1) → w_i, whose loop T_i is a
    closed odd self-loop under τ and an escape G_i → r_m under σ̄.
  - Both faces are per level (distinct markers η_i, MP_i and loop priorities T_i), and a single portal gives both worlds a common
    continuation, after which the prefix is read the same way up to the cycle node.
  - At ODIFF 0 (one-player) the behind pivot can reach the newer pivot's better value through the chain itself. The arena optimum takes it
    at once, so the pivots do not leapfrog.
- OPEN: a 𝒞^1O or 𝒞^2O window of length ω(n) (the conjecture says impossible; R51 allows up to O(n¹⁷) at ODIFF 1).

## 5. Tools (experiments/red/r170/)
- freeze.py G START: windows, ODIFF, G_F, REPLAY, FRUN, FFSEG. runcorp.sh: the corpus run (out/corp.txt).
- climb170.py N KO SEED ITERS OUT (env FBFREE, MAXDEG, ODD); runclimb.sh, runclimb0.sh, runclimb1p.sh; out/climb*_*.txt, champions
  out/c_*.pg / .start, out/p_*.pg / .start.
- wtrace.py (per-transition switches, |Is|, |It|, τ / σ̄ moves), wsw.py (switches per vertex inside windows), oreduce.py (greedy ODIFF
  cuts).
- check.sh block «R170»: freeze.py on runquad_K3_m4_n54 and on b5_os_n40.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/red/r170/*; check.sh block R170; notebook. SHAs in the push / message.
- FINDINGS:
  - FREEZE PROVED (lane): a TWO-FIX window is an N5 run on the game with only the ODIFF Odd choice vertices. ODIFF ≤ 1 windows are
    polynomial (R17 / R51). REPLAY on 1,157 corpus windows, 0 failures.
  - Quadratic TWO-FIX windows exist at ODIFF = Θ(n): runquad, one fallback-free window, L = 4K² + 3K − 1 at n = 24K + 6, ODIFF 4K.
    None is super-quadratic.
  - At fixed ODIFF, nothing beats linear: runquad is linear in n at fixed K, and the 54 climbs are ≈ n. Max
    FFSEG / (n(ODIFF + 1)) = 1.5 (n 8, ODIFF 0).
  - Every runquad ODIFF vertex is load-bearing (oreduce).
  - CONJECTURE TWO-FIX-NL: fallback-free window stretches ≤ 2n(ODIFF + 1).
- NEEDS: Lead: route TWO-FIX-NL (or its ODIFF ≥ 2 polynomial form via FREEZE-k) to L-NEW box 122. GO or redirect for L-RED's next box. My
  suggestion: attack TWO-FIX-NL at ODIFF 1-2 (a 𝒞^1O / 𝒞^2O window of ω(n), e.g. by sharing runquad's ladder portals), after T64 lands.
