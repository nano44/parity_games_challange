# Draft RESULTS R82 (Lead, 2026-10-29 05:13Z by date -u; both reports, both §Cs and the fixes file filled) — to CHECKER C91 (Lead reviewed 05:16Z by date -u: (H4′) failure count taken from F5; the 'cycle forms inside the piece' limit kept as a labelled READING (Lead)) (rev. 05:35Z by date -u: C91 N-1; N-2 not applied) — LANDED in RESULTS Results 2026-10-29 05:46Z (CHECKER C91 Add. 1 81502454 PASS), after R81

### R82 [refereed-only] N5 on EVERY game, inside one phase: on states [a, b] of one phase with (H1′) every transition an S4a step (no fallback) and τ, λ constant (λ_W need not be constant), (H2) σ̄_t = σ̄_a on [a, b], (H3′) every W-cycle of state b a W-cycle at every state of [a, b] and every honest cycle of b an honest cycle at every state of [a, b] (T_W, T_H the vertices of those end-state cycles, T := T_W ∪ T_H; the two frames' cycles may differ and other cycles may come and go), (H4′) the depth recursion (dW := 0 on T_W, dH := 0 on T_H, through τ (W) or σ̄ (honest) at Odd vertices and σ_b at Even vertices of T, d(v) := dW(v) := dH(v) := 1 + max(dW(σ_b v), dH(σ_b v)) at Even v ∉ T) well founded, equivalently the graph J_b on the Even vertices outside T (v → the first Even vertex outside T after v on v's W-play or honest play at b) acyclic, d(v) then being the number of vertices of a longest J_b-path from v, and GEN_W (RESULTS R77 (c)'s: for every v, different W-plays from v to the same cycle have different W-valuations), every vertex v has its W-play at b at every state of [a + dW(v), b] and its honest play at b at every state of [a + dH(v), b], so σ_t = σ_b on [a + max d, b] and b − a ≤ max d ≤ |Even ∖ T| ≤ n − 1 (Theorem STATIC-DEPTH′; its proof uses W-MONO and Ξ-SUCC at in-phase S4a transitions at which λ_W may change, a proof step signed by both referees for this entry: λ_W is not used); under RESULTS R77's (H1)-(H4), (H1′), (H3′) (with T_W = T_H) and (H4′) hold and d ≤ d*, so STATIC-DEPTH′ contains RESULTS R77 (c) (Remark); and a piece [a, b] (a maximal stretch of a fallback-free run of one phase with σ̄ constant), cut backwards into epochs that satisfy (H1′), (H2), (H3′) by construction, has b − a ≤ (CF + 1)·n − 1 transitions, CF the transitions of the piece at which a W-cycle or an honest cycle appears, if (H4′) holds at every epoch end, and GEN_W holds (Corollary EPOCH) (2026-10-29) — structural lemmas for N5 and a REDUCTION of a piece's length to its cycle-appearance count CF (CF is not bounded here; CONJECTURE PIECE, every piece ≤ n − 1 transitions, and CONJECTURE STATIC-DEPTH′-TIE, STATIC-DEPTH′ without GEN_W, are OPEN; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C91.md, checker PENDING)
- Object (L-SI successor 21, Opus 5.5; frozen, unchanged during review): packet P-N5-SDPRIME, docs/si/P-N5-SDPRIME-box25.md, sha1
  54678c38a04842bd936a9bf4b241d47ad8ab90a3 (l-si freeze edc14c51, 2026-10-29T03:58:27Z; quote base 55e0bcbda; 12 quotes,
  experiments/si/rund/quotecheck.py "quotes=12 bad=0", pinned with the sha1 in experiments/si/check.sh; both referees measured the pin),
  Theorem STATIC-DEPTH′ extending RESULTS R77 (c); working note with data docs/si/N5-PIECE-box25.md (l-si 6bb0ec34). The referees' notes are
  collected by the lane in docs/si/P-N5-SDPRIME-fixes-box25.md (l-si fc0312e2, sha1 f0bc5f4594e67fa483738f51b9e99065c4b2a2c1, L-SI
  successor 21: F1-F6 for SDP-N2 = N-SD-5, SDP-N3 = N-SD-1, SDP-N4 = N-SD-2, SDP-N1 = N-SD-7, SDP-N5 ⊇ N-SD-3 with N-SD-4, N-SD-6; 12 quotes
  checked by script, experiments/si/rund/quotecheck.py "quotes=12 bad=0", pinned in experiments/si/check.sh with a shifted-line control); on
  trunk; repairs only, "This file changes NO signed statement" (fixes l. 3-4): F1 replaces the packet §1's citation of W-MONO and Ξ-SUCC
  (as R77 (c)'s landed steps "on in-phase S4a transitions (R77's (H1))") by a proof step signed by both referees, item (a) below; F2 makes
  the (SW) quote strictly verbatim; F3 rewords EPOCH's hypothesis ("if (H4′) holds at every epoch end, and GEN_W holds": GEN_W is a property
  of (G, τ)); F4-F6 are records and change no statement. The statements below are in that repaired wording.
  Setting (every game): N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md) with FIX 1-4; state t = (σ_t, τ); phases as in RESULTS R80's setting
  (λ and τ constant). Ξ_t(v): the S1 valuation (c, P, ℓ) of v's honest play (σ_t at Even vertices, σ̄_t at Odd ones); W_t(v): that of v's
  (σ_t, τ)-play; ▷, ⊵ the S1 order, TOTAL on valuations (p′ injective, distinct sets have distinct signed weights); a valuation is a function
  of the play. A W-cycle (honest cycle) at t: a cycle of the successor map v ↦ σ_t(v) / τ(v) (v ↦ σ_t(v) / σ̄_t(v)), as a vertex sequence up
  to rotation; a vertex on such a cycle has that cycle as its play. Depths: dW(v) := 0 on T_W, dH(v) := 0 on T_H; Odd v: dW(v) := dW(τ v)
  (v ∉ T_W), dH(v) := dH(σ̄ v) (v ∉ T_H); Even v ∈ T_H ∖ T_W: dW(v) := dW(σ_b v); Even v ∈ T_W ∖ T_H: dH(v) := dH(σ_b v); Even v ∉ T:
  dW(v) := dH(v) := d(v) := 1 + max(dW(y), dH(y)), y := σ_b(v); max d is taken over Even v ∉ T (0 if there is none). n: the number of
  vertices.
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: SPEC S1 (valuation, order), S2
  (Iσ), S4a (arena {σ(v)} ∪ Iσ(v); Even's one-player optimum), S4c (FALLBACK); RESULTS R15 (a) Lemma A and (d); RESULTS R18 (d) Lemma S (a)
  on S4a's arena, the standing premise P2 as listed in RESULTS R69; (SW) "every Even switch of N5 is to an edge of Iσ", as listed among
  RESULTS R72's landed premises; RESULTS R77 (c) (GEN_W's definition; its proof steps W-MONO and Ξ-SUCC, landed under R77's (H1), which
  includes λ_W constancy; for the Remark its (H1)-(H4), H_b and d*); RESULTS R80 (a) EVERY-SWITCH and R80's phase setting:
  (a) Facts used as proof steps, signed by both referees for this entry (SDP-N2 = N-SD-5, F1): W-MONO (P2 / R18 (d) Lemma S (a) at one S4a
      step) and Ξ-SUCC (R15 (a), (d) + (SW)) hold at every in-phase S4a transition; λ_W is not used. (W-MONO: W_{t+1} ⊵ W_t, since σ_t uses
      only arena edges and σ_{t+1} is pointwise W-optimal over the strategies using arena edges. Ξ-SUCC: Ξ_t(σ_t v) is non-decreasing along
      in-phase S4a transitions: if v keeps, Ξ_{t+1}(σ_t v) ⊵ Ξ_t(σ_t v) by R15 (a), (d); if v switches, (SW) gives Ξ_t(σ_{t+1} v) ▷ Ξ_t(σ_t v)
      and R15 (a), (d) give Ξ_{t+1}(σ_{t+1} v) ⊵ Ξ_t(σ_{t+1} v).) This extends RESULTS R77's landed facts, which are stated under λ_W
      constancy, to the transitions at which λ_W changes; STATIC-DEPTH′ needs it. REFEREE §C (d693a6fe): "SDP-N2 SETTLED (Lead's question):
      the extension of W-MONO and Ξ-SUCC to in-phase S4a transitions at which λ_W changes is a SIGNED PROOF STEP of this entry, not a note."
      REFEREE-2 §C C.3 (9784229a): "YES, it is signed as a proof step, with a citation repair." The (M2κ) citation R77 gives for Ξ-SUCC is
      replaced by R15 (a), (d) (N-SD-5: "fine but stronger than needed").
  (b) Theorem STATIC-DEPTH′ (§2): on states [a, b] of one phase with (H1′) every transition t → t + 1, a ≤ t < b, an S4a step (no fallback),
      τ and λ constant on [a, b] (λ_W need not be constant); (H2) σ̄_t = σ̄_a for t ∈ [a, b]; (H3′) every W-cycle at b is a W-cycle at every
      t ∈ [a, b], and every honest cycle at b is an honest cycle at every t ∈ [a, b] (T_W / T_H := the vertices of the W-cycles / honest
      cycles at b; T := T_W ∪ T_H; the two frames' cycles may differ, and other cycles may come and go); (H4′) the depth recursion of the
      setting is well founded; and GEN_W: every v has its W-play at b at every t ∈ [a + dW(v), b] and its honest play at b at every
      t ∈ [a + dH(v), b]. Hence σ_t = σ_b on [a + max d, b], and b − a ≤ max d ≤ |Even ∖ T| ≤ n − 1 (T ≠ ∅: every play ends in a cycle).
      (Induction along the recursion: item 1, an end-state cycle keeps its vertices settled from a and fixes σ_t = σ_b on Even vertices of T;
      items 2-3, settling passes back one step through Odd vertices and through Even vertices of the other frame's T; item 4 at Even v ∉ T:
      (A) y = σ_b(v) is kept or improving at v from a + max(dW(y), dH(y)) on, by (SW) and Ξ-SUCC; (B) W_{t+1}(v) = W_b(v) by P2's pointwise
      optimality and W-MONO; (C) the W-play of v at t + 1 ends in the same end-state cycle, and GEN_W makes it the play at b; item 5, a
      transition with σ unchanged would contradict R80 (a).) The proof does not use R77's (CV) (cycle vertices constant); item 1, from (H3′),
      replaces it, which is what lets other cycles come and go (N-SD-6 = F6, ACCEPTED by REFEREE).
  (c) (H4′)'s equivalence (§2; REFEREE: "SIGNED (checked by proof)"; REFEREE-2: "SIGN (proof steps; checked)"): the recursion is well
      founded ⇔ the graph J_b on the Even vertices outside T, with an edge v → v′ when v′ is the first Even vertex outside T after v on v's
      W-play at b or on v's honest play at b, is acyclic; and then d(v) is the number of vertices of a longest J_b-path from v, so
      max d ≤ |Even ∖ T|. Parenthesis: a cycle of the recursion that meets no Even vertex outside T would be a cycle of one frame's successor
      map at b outside that frame's end-state cycles, which does not exist.
  (d) Remark (§2): STATIC-DEPTH′ contains RESULTS R77 (c). Under R77's (H1)-(H4): (H1) gives (H1′); (H3) gives (H3′) with T_W = T_H = the
      common cycle vertices; a J_b-edge follows σ_b at Even vertices and τ or σ̄ at Odd ones through vertices outside T, i.e. it is a path of
      R77's H_b, so (H4) gives (H4′); and d(v) ≤ R77's d*(v) (both count the Even non-cycle vertices of a path, J_b's paths being H_b's). So
      R77 (c)'s bound follows from STATIC-DEPTH′. New: the W- and honest cycles may differ, cycles other than the end state's may come and go,
      and λ_W may change.
  (e) Corollary EPOCH (§3, with F3), a REDUCTION. A PIECE: a maximal stretch [a, b] of states of a fallback-free run of one phase on which σ̄
      is constant (so (H1′), (H2) hold on it). Epochs: b_k := b; a_k := the least state of [a, b_k] such that every W-cycle (honest cycle) of
      state b_k is a W-cycle (honest cycle) at every state of [a_k, b_k]; then b_{k−1} := a_k − 1, and so on down to a; each epoch
      [a_i, b_i] satisfies (H1′), (H2), (H3′) with end state b_i, by construction. CF := the transitions t → t + 1 of [a, b] at which some
      W-cycle (honest cycle) of state t + 1 is not a W-cycle (honest cycle) of state t. Claim: if (H4′) holds at every epoch end b_i, and
      GEN_W holds, then |[a, b]| = b − a = Σ_i (b_i − a_i) + (k − 1) ≤ k(n − 1) + k − 1, and k − 1 ≤ CF; so b − a ≤ (CF + 1)·n − 1. (STATIC-DEPTH′
      per epoch; for i ≥ 2 the minimality of a_i gives a cycle of b_i that appears at a_i − 1 → a_i, and these k − 1 transitions are distinct.)
- Not signed: the packet's §4 (as the packet says): the DATA, CONJECTURE PIECE (every piece has ≤ n − 1 transitions, OPEN) and CONJECTURE
  STATIC-DEPTH′-TIE (STATIC-DEPTH′ without GEN_W, OPEN). The packet §1's premise line as written (W-MONO and Ξ-SUCC cited as R77 (c)'s landed
  steps, whose scope (H1) includes λ_W constancy, which (H1′) drops): it does not cover the transitions at which λ_W changes; not false;
  repaired by F1 into (a). The packet's (SW) quote with "…" where the source has only a line break (SDP-N3 = N-SD-1; content identical;
  repaired by F2). EPOCH's "GEN_W at every epoch end" as written (SDP-N4 = N-SD-2: redundant, GEN_W being a property of (G, τ) with τ fixed on
  the phase; reworded by F3).
- Honest limits: (i) EPOCH is a REDUCTION, not a bound: CF is not bounded, nor is the number of pieces of a phase. CONJECTURE PIECE stays
  OPEN; the packet's §3: "CONJECTURE PIECE ... reduces to the pieces with CF ≥ 1". READING (Lead), from EPOCH's construction: a piece in which
  every cycle of its end state b is a cycle at every state of the piece is one epoch (k = 1), and then (H4′) at b and GEN_W give b − a ≤ n − 1
  by STATIC-DEPTH′; so the pieces this entry leaves open are those in which an end-state cycle forms inside the piece (a cycle of b appears
  at a transition of the piece), besides those where (H4′) fails at an epoch end or GEN_W fails. (ii) GEN_W is a hypothesis; CONJECTURE
  STATIC-DEPTH′-TIE is OPEN (the conclusion held wherever the used form of GEN_W failed: packet §4, 22 pieces; REFEREE 161 intervals;
  REFEREE-2 132 + 173). (iii) Thin spots (SDP-N5 ⊇ N-SD-3, F5): "other cycles come and go" is exercised in only 3 + 0 + 3 intervals
  (REFEREE-2; REFEREE did not count it); EPOCH with CF ≥ 1 on few pieces (REFEREE 25 / 41 / 137 / 438; REFEREE-2 24 + 50 with every
  hypothesis), and (CF + 1)n − 1 is far from reached (no piece longer than n − 1 in any referee's data); MUT=1 (settling from d − 1) bites
  only where the bound is sharp. The other new freedoms are well exercised: T_W ≠ T_H in 3,409 intervals (REFEREE, all corpora) and 6,158 +
  4,811 + 159 (REFEREE-2), λ_W changing in 585 and 562 + 681 + 159. (iv) Every hypothesis carries weight in data: (H4′) is not vacuous
  (N-SD-4 = F5: fails at 4 + 28 (H3′)-intervals, REFEREE-2; 4 + 2 + 1 (H4′) failures in the lane's data (alt_all, lib41, random; F5 counts the first two), N5-PIECE-box25 §2); both halves of (H3′) (REFEREE MUT2,
  W-cycles only: SDV 77, SD 1, SB 1 on lib41; REFEREE-2 onlyH 3,009 + 38 with the length bound failing 23 + 1 times, onlyW 368 + 30, LEN 7);
  the dH half of d (REFEREE MUT3, W-frame depth only: SD 17, SDV 3,924 on lib41); honest-cycle appearances in CF (REFEREE MUT4: 5 + 2 on k − 1 ≤ CF); the depth is exact
  (REFEREE MUT1 14,126 on lib41; REFEREE-2 dm1 19,355 + 923), and b − a = max d is attained (REFEREE 369 / 383 / 359 / 152 intervals,
  REFEREE-2 369 + 429). (v) Nothing here bounds N5's running time.
- Data (DATA, not proof): the packet's §4 (lane, experiments/si/piece/sdprime.py and epochs.py; one engine, n5x; DEFAULT S3 starts, F4):
  STATIC-DEPTH′'s hypotheses hold on 844 of 872 alt_all pieces (R77's: 708), 914 / 943 lib41, 940 / 1,080 random 𝒞^kO; 0 violations of the
  per-vertex settling, of b − a ≤ max d and of b − a ≤ n − 1; MUT=1 (d − 1) fails 912 / 74 times; EPOCH ≤ 6 epochs and CF ≤ 5 per piece, 0
  violations; pieces outside STATIC-DEPTH′ ≤ 0.43(n − 1) in alt_all, a climb found none above 0.71(n − 1). Recount with the pinned starts
  (F4, piece/sdprime_alt_start.txt): 1,140 alt_all pieces (1,131 without the 9 games with no Odd choice vertex), (H3′) fails 25, (H4′) 2, the
  hypotheses hold on 1,113 (97.6 %; the 9 GEN_W-failure pieces counted, not excluded), 0 violations. REFEREE (successor 17; own
  docs/referee/scratch/sdprime_probe.py (sha1 11d9b745…) on its engine rl_engine; lane code not run; 0 failures in every MUT=0 run):
  alt_all (413 games, n ≤ 600, given start else S3; 413 runs) 4,791 STATIC-DEPTH′ intervals (905 with T_W ≠ T_H, 153 with λ_W changing),
  pieces 5,765 (1,132 with ≥ 1 transition), the hypotheses on 1,098 of 1,132 (97.0 %) and R77's on 918 (81.1 %); lib41 (727 runs) 5,440
  intervals; lib1140 (1,857 runs) 7,929; random rand_ck (n 6-20, k ≤ 6; 12,000 runs) 2,175; Remark: (H3′) and max(dW, dH) ≤ d* at 3,878 +
  4,538 + 6,380 + 2,080 R77 instances, 0 failures; at most 6 epochs and CF ≤ 5 per piece; λ_W-changing in-phase S4a transitions: W-MONO and
  Ξ-SUCC 0 failures at 285 (alt_all) + 214 (lib41) (scratch/lw_facts.py). REFEREE-2 (successor 19; own
  docs/referee-2/R2-N5-SDPRIME/sdprime_check.py on its lane's Runner (si.py); lane tools not run; every non-mutation run 0 violations):
  alt_all (413 runs) 1,133 pieces, 32,404 (H3′)-intervals (every sub-interval of a piece up to length 60); lib41_noref × 3 (1,230 runs)
  1,812 pieces, 52,303 intervals; named (8 runs) 91 pieces, 634 intervals; random kO / k2 / k4 (24,000 runs); item 4 (A) checked at
  10,540,227 + 8,589,064 + 38,414 instances, (B) at 9,531,639 + 7,602,983 + 29,715; H4EQ and DEQ ((c)) 0 failures; Remark on 26,103 + 47,270
  + 475 R77 intervals, 0 failures; EPOCH's cut, sum, appearance and length checks 0 failures; W-MONO and Ξ-SUCC 0 failures at 283 + 657 + 24
  + 56 λ_W-changing transitions; longest STATIC-DEPTH′ interval 55 transitions (x32_rand64, n 64, max d 56). Piece counts (SDP-N1 = N-SD-7,
  F4): the referees agree with each other (alt_all pieces with ≥ 1 transition: 1,132 and 1,133); the lane found the cause of §4's 872: its
  corpus run used the default S3 start for every file (the list's second column, a pinned .start file on 94 of its 413 lines, was not
  read); the remaining 1-9 difference to 1,140 / 1,131 is not determined (fixes F4). No signed statement uses any count.
- Signatures: REFEREE docs/referee/R-N5-SDPRIME.md (report 573d2695, sha1 47d5287569a739ec4e491e26fb1a263ee785733f there; §C d693a6fe;
  successor 17): STATIC-DEPTH′ SIGNED; (H4′)'s "Equivalently" and its parenthesis SIGNED (checked by proof); the Remark (contains R77 (c))
  SIGNED; Corollary EPOCH SIGNED (a REDUCTION: CF unbounded); quotes 12/12 (own scratch/flip_quotes.py, which treats "…" as a separator);
  notes SDP-N1..N5; no gap. REFEREE-2 docs/referee-2/R2-N5-SDPRIME.md (report bf48b8f4, sha1 e12e36413fe3e7e25ca9eea63fbe6c67c67ab94c there;
  §C 9784229a; successor 19): STATIC-DEPTH′ SIGN; (H4′)'s equivalence and d(v) = vertices of a longest J_b-path SIGN (proof steps; checked);
  the Remark SIGN; Corollary EPOCH SIGN (a REDUCTION; GEN_W wording, N-SD-2); quotes 11/12 strictly verbatim, the twelfth with a spurious
  "…" (N-SD-1, content identical), SHIFT=1 control 0/12; notes N-SD-1..7; no gap. INDEPENDENCE: REFEREE opened no docs/referee-2/ file on
  SDPRIME (names only at 04:33Z: 0 on its tree, 25 on origin/claude/referee-2, 18 on trunk docs/referee-2/; none read) and ran no lane code;
  REFEREE-2 opened no docs/referee/ file on SDPRIME before pushing bf48b8f4 (names-only count 0 at 04:04:20Z and at 04:12:45Z) and ran no
  lane tool. §C (both): verdicts identical (STATIC-DEPTH′, (H4′)'s equivalence with d = longest J_b-path count, the Remark, EPOCH); joint
  gap map EMPTY; SDP-N2 = N-SD-5 SETTLED as a signed proof step (item (a)); SDP-N3 = N-SD-1, SDP-N4 = N-SD-2, SDP-N1 = N-SD-7 matched;
  SDP-N5 ⊇ N-SD-3, N-SD-4 and N-SD-6 ACCEPTED by REFEREE; quotes 12/12 in content, one cosmetic "…"; nothing open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (structural lemmas on N5 inside one phase and a reduction of a piece's length to
  its cycle-appearance count; no running-time bound, no algorithm claim). GAPS G-N5-TIME: open.
