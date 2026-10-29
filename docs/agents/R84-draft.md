# Draft RESULTS R84 (Lead, 2026-10-29 06:08Z by date -u; both reports, both §Cs and the fixes file filled) — to CHECKER C93 (Lead reviewed 06:15Z by date -u: wording choices accepted; N-TS-1 and N-TS-2 outside the entry)

### R84 [refereed-only] N5 on EVERY game, inside one phase: for a fixed vertex v, a phase P (λ and τ constant on P, c := λ(v)) and top_t := the highest rank in P_t := P(Ξ_t v), v's path set at state t (⊥, below every rank, if P_t = ∅), a rank being EVEN or ODD as the priority Ω of the vertex of that rank (not the parity of the rank number), at every transition t → t + 1 of P with P_t ≠ P_{t+1} the top rises only to an even rank (if top_{t+1} > top_t then top_{t+1} is even; Lemma TOP-SHAPE (a)) and an even top never falls (if top_t is even then top_{t+1} ≥ top_t; TOP-SHAPE (b)); hence along P, once the top is even it stays even and never falls, and before that it is odd or ⊥, an odd top only falling or staying until it is replaced (by a lower odd rank, by ⊥, or by a lower or higher even rank) (TOP-SHAPE (c)); so the sequence of distinct values of top_t on P is a strictly decreasing run of odd ranks, then at most one ⊥, then a strictly increasing run of even ranks, and top_t changes at most n − 1 times on P, for every vertex v and every phase P (Corollary); the proof reads the strict rise of the signed path-set weight (Ξ non-decreasing by RESULTS R15 (a), (d), the cycle node λ(v) fixed on P, distinct sets of ranks having distinct signed weights) through Fact DELTA (for sets A ≠ B of ranks, weight(B) > weight(A) iff the largest rank d in A Δ B is even and d ∈ B ∖ A, or d is odd and d ∈ A ∖ B) (2026-10-29) — structural lemmas for N5 (they bound the changes of the top only, NOT the P-changes under a fixed top, which are not bounded here; the Δ form of TOP-MONO is DEAD; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C93.md, checker PENDING)
- Object (L-NEW successor 30, Opus 5.5; frozen, unchanged during review): packet P-N5-TOPSHAPE, docs/new/P-N5-TOPSHAPE-box49.md, sha1
  c5b0e8d86745d6db5e0c9f6e1551b10c5b511b8f (l-new freeze 4c2ea43e, 2026-10-29T04:59:50Z; quote base e2da18b0; 2 quotes,
  experiments/new/box49/quotecheck3.py "quotes=2 bad=0", pinned with the sha1 and a shifted-line control in experiments/new/check.sh; both
  referees measured the pin), Fact DELTA, Lemma TOP-SHAPE (a)-(c) and its Corollary. Tool experiments/new/box49/topmono.py (sha1
  c8f470dfee2aa8cb104078b16d2bd09df553ff99, by git: committed only at 4c2ea43e; the packet's "sha1 in the push message" is not in that
  message); working note docs/new/N5-READER-box49.md §12 (a pointer to the packet). The referees' notes are collected by the lane in
  docs/new/P-N5-TOPSHAPE-fixes-box49.md (l-new 8e8f7238, sha1 be683e9fd1dcd64f48c9d02f2fac66fc214cff0d, L-NEW successor 30: F1-F5 for
  TOP-N1 = N-TS-3, N-TS-1, TOP-N2 with N-TS-2, TOP-N3 = N-TS-5, N-TS-4; 17 quotes checked by script, experiments/new/box49/quotecheck3.py
  "quotes=17 bad=0", pinned in experiments/new/check.sh with a shifted-line control and the sha1); on trunk; "Repairs only; no signed
  statement changes." (fixes l. 6): F1 corrects §3's rise count (DATA in a DEAD item); F2 adds the wider form of (a), (b) and of the
  Corollary as a REMARK outside the signed Lemma (bullet "Referee strengthening"); F3 adds the sharper count as a remark (same bullet); F4
  drops "of one class" from Fact DELTA, states (INJ) as the general fact and keeps RESULTS R38 (a) as the phase definition only; F5 adds to
  §2 that an even or odd rank is the parity of Ω of the vertex of that rank. The statements below are in that repaired wording.
  Setting (every game): N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md) with FIX 1-4; phases as in RESULTS R80's setting (λ := Ξ's cycle-node
  map; a phase is a maximal run of states with λ and τ constant, RESULTS R38 (a) KEY); a transition t → t + 1 of a phase P joins two states
  of P (in-phase S4c fallbacks included). Ξ_t(v): the S1 valuation (c, P, ℓ) of v's honest play; rank(u): the position of u in V sorted by
  (Ω(u), u) (S1); a rank r is EVEN or ODD as Ω of the vertex of rank r (F5: not the parity of the rank number); weight(A) := Σ_{r ∈ A}
  s(r)2^r for a set A of ranks, s(r) = +1 for even r and −1 for odd r (S1's signed weight); S1's order: the reward of c, then the weight of
  P, then ℓ. v: a fixed vertex; c := λ(v), constant on P; P_t := P(Ξ_t v) ⊆ {u : rank(u) > rank(c)}, read as a set of ranks; top_t := the
  largest rank in P_t, or ⊥ (below every rank) if P_t = ∅; for sets A ≠ B, d(A, B) := the largest rank in A Δ B. n: the number of vertices.
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: SPEC S1 (valuation (c, P, ℓ),
  rank, signed weight, order); RESULTS R15 (a) Lemma A and (d), as (MON): Ξ_{t+1}(v) ⊵ Ξ_t(v) at every N5 iteration, S4c fallbacks included
  (the packet quotes P-N5-HONFF's line "(MON): RESULTS R15 (a) with R15 (d)"); RESULTS R38 (a) KEY and R80's setting, as the phase
  definition only (F4). (INJ) is not a premise: it is the general fact that distinct sets of ranks have distinct signed weights, immediate
  from Fact DELTA (F4); RESULTS R56 (a) states it per honest class and is cited for comparison only.
  (a) Fact DELTA (§1, with F4): for sets A ≠ B of ranks, weight(B) > weight(A) iff d := d(A, B) is even and d ∈ B ∖ A, or d is odd and
      d ∈ A ∖ B. (weight(B) − weight(A) = Σ_{r ∈ B∖A} s(r)2^r − Σ_{r ∈ A∖B} s(r)2^r; the term at d dominates the sum of the others, Σ_{r<d} 2^r <
      2^d; its sign is s(d) if d ∈ B ∖ A and −s(d) if d ∈ A ∖ B.) Hence (INJ): distinct sets of ranks have distinct signed weights. F4:
      "Fact DELTA reads "For sets A ≠ B of ranks, weight(B) > weight(A) iff …"" (the packet's "path sets A ≠ B of one class": REFEREE TOP-N3, "of one class"
      "is not needed. Cosmetic."; REFEREE-2 N-TS-5: "(INJ) is just "distinct sets have distinct weights", which Fact
      DELTA itself proves").
  (b) Lemma TOP-SHAPE (§1): let t → t + 1 be a transition of the phase P with P_t ≠ P_{t+1}. Then (a) if top_{t+1} > top_t, then top_{t+1}
      is even; (b) if top_t is even, then top_{t+1} ≥ top_t; (c) hence, along P: once top is even it stays even and never falls; before
      that, top is odd or ⊥, and an odd top only falls or stays until it is replaced (by a lower odd rank, by ⊥, or by a lower or higher
      even rank). ((MON) gives Ξ_{t+1}(v) ⊵ Ξ_t(v); the cycle node c is the same at both states (λ constant on P), so the order compares the
      weights next: weight(P_{t+1}) ≥ weight(P_t), strictly since P_{t+1} ≠ P_t (INJ). (a): u′ := top_{t+1} > top_t is not in P_t and no
      rank above u′ is in either set, so d(P_t, P_{t+1}) = u′ ∈ P_{t+1} ∖ P_t, and DELTA with the strict rise forces u′ even; from ⊥ too.
      (b): an even u := top_t with top_{t+1} < u (⊥ included) gives d = u ∈ P_t ∖ P_{t+1}, and DELTA says the weight falls, a contradiction.
      (c): from an even top the next top is ≥ it and any rise is even, so tops stay even, non-decreasing, and P never empties again; from ⊥
      a change makes the top > ⊥, hence even; from an odd top a rise is even, otherwise the top stays or falls.)
  (c) Corollary (top changes, §1): for every vertex v and phase P, top_t changes at most n − 1 times on P. (By TOP-SHAPE (c) the sequence of
      distinct top values is a strictly decreasing run of odd ranks, then possibly ⊥, then a strictly increasing run of even ranks; the odd
      run has no ⊥ inside it, since from ⊥ the next top is even; so each rank above rank(c) occurs at most once and ⊥ at most once; there
      are at most n − 1 ranks above rank(c), so at most n values and at most n − 1 changes. A top changes only at a P-change, which the
      Lemma covers: REFEREE §1.)
- Not signed: the packet's §2 (DATA) and §3 (TOP-MONO in its Δ form, DEAD; bullet "Honest limits" (iii)), as the packet says. The
  packet's reader-proofness sentence (READING: "readers ... cannot raise a vertex's top changes above n − 1. What they raise is the
  P-changes under a fixed top"): REFEREE "not signed; true as a consequence of the Corollary"; REFEREE-2 "not signed. Follows from the
  Corollary being per vertex and on every game". The packet's wording as frozen, repaired by the fixes and not false where a statement:
  Fact DELTA "For path sets A ≠ B of one class" (F4; the proof never uses the class); the premise line "(INJ) (RESULTS R56 (a))", where R56
  (a) states it per honest class (F4); "Phases (RESULTS R38 (a))" as a premise beyond the phase definition (F4, REFEREE-2 N-TS-5: "R38 (a)
  is not needed beyond the phase definition"); §3's "with 20 rises in the phase" (F1: 17 for vertex 0; 20 is vertex 6's, the run's
  maximum: "vertex 0 has 35 P-changes and 17 rises; vertex 6 has 44 P-changes and 20 rises"); §2's "tops 31, 30, 29, 27, 26, 21, 20 (all
  odd ranks)" without the reminder that the parity is Ω's (F5, N-TS-4: it "reads as a contradiction without that definition at hand").
- Referee strengthening (NOT part of this entry; fixes F2 and F3 record both as remarks outside the signed Lemma and Corollary):
  (i) N-TS-1, the wider form: TOP-SHAPE (a) and (b) hold at every N5 transition at which λ(v) is unchanged, phase-leaving transitions
  included, and the Corollary holds per maximal run of states with λ(v) constant (which can be longer than a phase). REFEREE-2 states it
  in its verdict line ("It also holds at every N5 transition at which v's own cycle node is unchanged, phase or not (N-TS-1)") and checks
  it as XSAMEC, 0 failures in 115,702 checks; REFEREE's §C: "N-TS-1 SETTLED (Lead's question): a STRENGTHENING, not part of the signed
  statement. The packet's Lemma and Corollary are stated for transitions and runs inside one phase, and that is what both referees sign";
  it re-derives the wider form ("the proof uses only (MON), valid at every iteration since Ξ depends on σ alone, R15 (a), (d); the
  unchanged cycle node; and (INJ)") and checks it, 0 failures at 9,202 off-phase P-changes with λ(v) unchanged (scratch/ts_wide.py;
  top_logs/wide_lib41.txt 2,091, wide_lib1140.txt 7,111). REFEREE-2's CTL_cross shows the unchanged cycle node is needed: TSa / TSb fail
  17,907 + 50,151 + 666 + 40,331 + 28,705 times across phase-leaving transitions. The lane did not state it as a signed item (F2: "as a
  REMARK (not part of the signed Lemma)"). (ii) N-TS-2, the sharper count (F3, remark): top changes ≤ n − 1 − rank(λ(v)), ranks counted
  from 0 (F3), since the values are the ranks above rank(λ(v)) and ⊥. In REFEREE-2's Corollary verdict line as an addition ("SIGN. The same
  proof gives ≤ n − 1 − rank(λ(v)) (N-TS-2)"; CORc, 0 failures), not in REFEREE's verdict table; REFEREE's §C: "ACCEPTED, consistent".
- Honest limits: (i) TOP-SHAPE bounds only the changes of the top. The P-changes under a fixed top (the counting changes) are not bounded:
  P-changes of one vertex in one phase reach 71 (l121reader_n41, n 41; packet §2, reproduced by REFEREE) and 72 (l121_d29) and 67
  (nep92_n40) in REFEREE-2's data, which has P-changes per (v, phase) above n − 1 in 23 + 3 + 32 cases (CTL_counting). READING (Lead): a
  path set under a fixed top behaves like a binary counter below it (packet §3's obstruction), and L-RED's R104 (docs/red/R104-counting-gate.md,
  l-red 92754453; L-RED DATA, not refereed) counts low-digit resets under a fixed top (changes of an Odd choice vertex's path set that
  remove an element while its top is unchanged) as abundant: RESET 133 of PCH 157 (the changes of some Odd choice vertex's path set) in one
  phase of pl130_n40 (own start). So the Corollary does not bound the P-changes of a vertex, nor Ξ-changes, nor a phase's length. (ii) Whether
  n − 1 is attained is OPEN (REFEREE TOP-N2: "Whether n − 1 is attained by some game is open (an odd run down all odd ranks, then the even
  ranks upward)"; REFEREE-2 §C: "stays OPEN"). In data the count stays far below it: max 0.37 n (REFEREE; 48 at n = 156) and 0.43·(n − 1)
  (REFEREE-2, lend9_n8; 62 at n = 581, gate_K64_n581, vertex 573); REFEREE's MUT2 (the Corollary with n − 2) does not bite. (iii) DEAD:
  TOP-MONO in its Δ form (Lead, 04:57Z: "the top rank of the symmetric difference between successive path sets P(Ξ_t(v)) at its P-changes
  is monotone") is false: experiments/new/box48/instances/long121_n40 at its .start, phase [1, 122], vertex 0, Δ-tops at its P-changes
  35, 37, 32, 33, 26, 39, 21, 29, 33, 36, … (35 P-changes, 17 rises of the Δ-top, F1; 20 rises for vertex 6, the run's maximum; 47 Δ-top
  rises for one vertex in one phase on ladderd0_k48_n156, packet §3 and REFEREE). Obstruction (packet §3): "the Δ-top is the carry position
  of a counter ... a counter's carry positions go up and down. Only the top of P itself is monotone in the sense of (c)." Confirmed by both
  referees on the same instance with the same first ten Δ-tops; REFEREE MUT3 (Δ-tops non-increasing demanded) bites at 7,305 (vertex,
  phase) pairs (lib41), REFEREE-2 CTL_deltatop fails in 4,360 of 6,124 sequences with ≥ 2 P-changes (alt_all). (iv) Nothing here bounds
  N5's running time.
- Data (DATA, not proof): the packet's §2 (lane, experiments/new/box49/topmono.py; outputs experiments/new/box49/out/topmono_*.txt; VIOL
  counters rise-to-odd / even-top-fell / odd-after-even 0 / 0 / 0 everywhere): lib41 (n ≤ 48, own start or S3 + 2 random, seed 7) 1,047
  runs, 59,663 P-changes, max top rises per (v, P) 3 (b5_os_n28, vertex 10: tops 10, 11, 22, 27); L-RED instances (n ≤ 200, own start or
  S3) 311 runs, 27,587, max 48 (ladderd0_k48_n156, vertex 50: ⊥, 107, 108, …); long121, qpcclimb scale, pl130_n40, si/root/instances 13
  runs, 11,177, max 2 (cone_n69: ⊥, 67, 68); 1,371 runs in all; gate example sc32 (box25), vertex 0, phase [4, 48]: tops 31, 30, 29, 27,
  26, 21, 20 (odd in Ω's sense, F5), ⊥, 25, 28. REFEREE (successor 17; own docs/referee/scratch/topshape_probe.py (sha1 b9c0d284…) on its
  engine rl_engine; lane code not run; logs scratch/top_logs/; 0 failures in every MUT=0 run): lib1140 (n ≤ 40; given + S3 + 1 random)
  1,857 runs, 56,473 P-changes, 17,882 (v, P) pairs, (a) / (b) checks 5,572 / 6,858, max top changes 9 (0.37 n), max P-changes per (v, P)
  60; lib41 (n ≤ 48; given + S3 + 2 random) 1,076, 58,143, 15,873, 3,612 / 4,694, 10 (0.28), 37; L-RED instances (316 games, n ≤ 200)
  316, 29,196, 8,083, 2,756 / 5,248, 48 (0.30), 62; random rand_ck (n 6-24, k ≤ 6) 12,000, 3,286, 3,224, 1,209 / 625, 2 (0.22), 2;
  long121_n40 1, 769, 39, 9 / 54, 7, 44; DELTA's iff, the strict rise, the unchanged cycle node, (a), (b), (c) and per (v, P) the shape and
  the bound: 0 failures on 147,867 P-changes and 45,101 (v, P) pairs; MUT1 ((a) with odd) bites at 3,612 of 3,612 rises, MUT2 (n − 2) does
  not bite, MUT3 (Δ form) 7,305 pairs; reproduced: ladderd0_k48_n156 48 top changes, l121reader_n41 71 P-changes, §3's ten Δ-tops (distinct
  tops of long121 vertex 0: 39, 38, 37, 36, 35, 26, 14). REFEREE-2 (successor 19; own docs/referee-2/R2-N5-TOPSHAPE/topshape_check.py and
  repro.py on its lane's SPEC loop (si.py, read-only); lane tools not run; every run 0 violations): alt_all (413 runs, given start else S3)
  458 phases, 53,549 P-changes, TSa / TSb 6,082 / 10,282, 8,516 (v, phase) with a top change, 3,643 odd-then-even sequences; lib41_noref × 3
  (1,230 runs) 1,116, 72,783, 6,986 / 13,914, 14,277, 5,429; named (20 runs) 24, 12,716, 426 / 1,103, 779, 505; random kO n 8-20 / k2 n 6-16
  (30,000 runs) 4,880, 4,021, 1,465 / 1,212, 2,386, 599; Fact DELTA also on 8,236 + 24,488 + 400 + 299,807 + 299,144 random mask pairs; TSc
  and COR / CORc on every (v, phase); reproduced: sc32's tops exactly as §2, ladderd0_k48_n156's 48 top changes, the l121reader-type
  P-change counts (72 / 67); controls CTL_flip (bites at every rise), CTL_deltatop, CTL_cross, CTL_counting as above. Run counts differ by
  start set and corpus (lane lib41 1,047 runs, REFEREE 1,076, REFEREE-2 1,230; L-RED instances 311 runs (lane) and 316 games (REFEREE));
  not reconciled in any report. No signed statement uses any count.
- Signatures: REFEREE docs/referee/R-N5-TOPSHAPE.md (report 1a6d6a24, sha1 8e4afe5a87b5e8e96bf7fb19b3d63f27ed3fe830 there; §C e0499401;
  successor 17): Fact DELTA SIGNED; Lemma TOP-SHAPE (a)-(c) SIGNED; Corollary SIGNED; the reader-proofness sentence not signed (true as a
  consequence); §2, §3 not signed, §3's instance reproduced (DEAD); quotes 2 of 2 verbatim (own scratch/flip_quotes.py); notes TOP-N1..N3;
  no gap. REFEREE-2 docs/referee-2/R2-N5-TOPSHAPE.md (report 97db54fc, sha1 e409e4439a18c368f452ed9a1c5de0ac1eefbb50 there; §C 0e2063bf;
  successor 19): Fact DELTA SIGN; Lemma TOP-SHAPE (a), (b), (c) SIGN; Corollary SIGN; reader-proofness not signed; §3 DEAD CONFIRMED; quotes
  2/2 verbatim (own qcheck.py; SHIFT=1 control 0/2); notes N-TS-1..5; no gap. INDEPENDENCE: REFEREE opened no docs/referee-2/ file on
  TOPSHAPE (names at 05:13Z: 0 on its tree, 0 on origin/claude/referee-2, 0 on trunk) and ran no lane code; REFEREE-2 opened no TOPSHAPE
  file under docs/referee/ before pushing 97db54fc (names-only count 0 at 05:06:23Z and at 05:18:26Z; it opened REFEREE's REL report, not a
  TOPSHAPE file, on the Lead's word) and ran no lane tool. §C (both): verdicts identical (Fact DELTA, TOP-SHAPE (a)-(c), the Corollary;
  Δ-form TOP-MONO DEAD on the same instance); joint gap map EMPTY; TOP-N1 = N-TS-3 (same numbers, found independently), TOP-N3 = N-TS-5,
  TOP-N2 with N-TS-2 ACCEPTED, N-TS-4 ACCEPTED as wording, N-TS-1 SETTLED as a strengthening (bullet "Referee strengthening"); REFEREE-2:
  "No verdict changes"; REFEREE: "Nothing open on TOPSHAPE."
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (structural lemmas on N5 inside one phase bounding the changes of the top of a
  vertex's path set; no running-time bound, no algorithm claim). GAPS G-N5-TIME: open.
