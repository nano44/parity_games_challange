# N5-FC (box 59): why SBC = N² on fcN, why its resets do not compound, and a per-vertex conjecture (PV) for the degree
L-NEW successor 34 (Opus 5.5), D14 / D18, Lead reading L40. Lead's brief 2026-10-29 17:15Z, BOX 59 (a)-(c). Written 2026-10-29 from
17:40Z (date -u). Working note, unrefereed, not a TARGET.md claim. CONJECTURE SF-POLY (P-N5-SF-box55.md §5) stays OPEN; G-N5-TIME untouched.
Labels: PROVED (lane, unrefereed) / DATA / READING / CONJECTURE / OPEN / DEAD.
Symbols as in P-N5-SF-box55.md §0 (frozen): F, σ^(j) (the distinct-σ sequence), σ̄(σ), Ξσ, Iσ, SBC_σ. Engine: experiments/new/box54/n5sf.py
(default MODE, SPEC S3 start). Family fcN = experiments/red/sf/sbev.py N --drop fc (L-RED R115; PGSolver switchbestexp N minus the N edges
f_i → c; n = 25N + 10). Vertex names are sbev.py's labels: h_i cycle centre (Odd; e_i = stay, m_i = escape), e_i f_i g_i the cycle's Even
nodes, z_i upper selector, v_i its helper chain, r_i / l_i / k_i access to cycle i, d lane root, x / w / y bit selectors, a_* b_* the lane,
p sink. "Bit i set" = σ̄(h_i) = m_i (Odd escapes a cycle Even has closed). A RECORD is a set of a bit above every bit set before.

## Summary
- (a) DATA (own engine; the word for N = 3..10, SBC_σ = N² for N = 3..12): fcN's σ̄-flip word is exactly W_N = ∏_k [h_k+, h_(k−1)−, …, h_0−,
  h_0+, …, h_(k−1)+]: one flip per SBC transition, resets only in a cascade right after a record, top down, at consecutive σ-steps.
  Lemma COUNT (PROVED) turns that shape into SBC ≤ N², with equality on W_N.
- (a) The mechanism (DATA + READING): information LATENCY of F. F switches only along edges that are improving NOW. At a record k
  the lane reaches l_k in one F-step. The escape chain of bit k − 1 needs two: v_(k−1) → r_k first, then z_(k−1) → v_(k−1). In that
  one-step gap every escaping lower cycle opens to the lane. Then each escape catches up and Odd reverts, top down: that is the cascade.
  At a re-set, d enters at the lowest set bit and the lower escape chains already skip straight to the record. So the news travels up
  ONE shared chain, reaches the lane and every closed lower cycle at the same F-step, and nothing opens. That is why the walks do not
  compound: a re-set never triggers a cascade.
- (b) READING, not a proof: on this mechanism an EXTERNAL reset of a lower block costs O(its bit count), not its counter length. A
  reset is a cascade plus a record-free re-climb. Nesting raises the degree only if the lower block's reset source gets superlinearly
  many events that bypass the lower escape chain. A necessary condition is stated (§3). It is OPEN whether a gadget meets it.
- (c) CONJECTURE PV (per vertex): along F's run each Odd vertex changes its best reply at most n times. Then SBC_σ ≤ k_O · n ≤ n², and
  by SF-RED (b) N5-SF makes O(n²(n + m)) iterations. DATA: 720 games, 0 violations. The maximum is flips(u)/n = 0.917 (so_sor5_n24,
  one Odd branching vertex). fcN gives 2N − 1 ≈ 0.08n, switchbestexp_12 gives 51 = 0.16n, random games ≤ 0.10n. PV is falsifiable
  by L-RED's nested families: it predicts that no Odd vertex flips more than n times there.
- DEAD: FLIP-REC° (flips(u) ≤ 2·REC°(u) + 1, where REC° counts changes of the top non-sink vertex of Ξ(u)). It holds on fcN exactly
  (2N − 1 = 2N − 1) and fails on 44 / 514 corpus games: so_sorl_n32 has 22 flips with REC° = 0.

## 1. (a) fcN: the count and its mechanism
### 1.1 Lemma COUNT (PROVED, lane; elementary)
Let a run flip bits of {0, …, N − 1} one at a time. Call a set of bit k a RECORD if k exceeds every bit set before it. Assume:
(R1) a bit is reset only in the cascade of a record r, i.e. between r's set and the next set event; (R2) a cascade resets each bit
below r at most once and no bit at or above r. Then the number of flips is at most N². If moreover every record resets all bits below
it and every reset bit is set again before the next record (the word W_N), the number is exactly N².
Proof. A bit is set at most once more than it is reset, so sets ≤ N + resets. By (R1) and (R2), resets ≤ Σ over records r of r. The
records are distinct bits, so this is ≤ 0 + 1 + … + (N − 1) = N(N − 1)/2. Total ≤ N + 2 · N(N − 1)/2 = N². Under W_N every bound is
attained: records 0..N − 1, k resets after record k, k re-sets. □
Note that (R1)-(R2) are what fcN satisfies (DATA, §1.2). The lemma is the counting, not a statement about F.

### 1.2 DATA: the word, the cascade, who opens, and the latency
Checker experiments/new/box59/fcword.py fc_N.pg N (log box59/fcword.txt, N = 3..10). It prints:
- FCWORD W: the σ̄-flip word equals W_N, one flip per SBC transition.
- FCWORD C: the k resets after record k sit at consecutive transitions.
- FCOPEN: after a record, every escaping lower cycle leaves its cycle (σ at e_i, f_i or g_i) before the next flip. After a re-set, none does.
- FCLAT: at every record k ≥ 1, at the state just before cycle k − 1 opens, Ξ(a_0) (the lane) contains m_k and Ξ(f_(k−1)) does not.
  There (z_(k−1), v_(k−1)) ∉ Iσ, while (v_(k−1), r_k) ∈ Iσ.
| N | n | SBC_σ | W | C | FCOPEN | FCLAT | sha1 (12) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 85 | 9 | PASS | PASS | PASS | PASS | 9af7ca12ace1 |
| 4 | 110 | 16 | PASS | PASS | PASS | PASS | 3562ec4d15eb |
| 5 | 135 | 25 | PASS | PASS | PASS | PASS | 6e9163038da7 |
| 6..10 | 160..260 | 36, 49, 64, 81, 100 | PASS | PASS | PASS | PASS | box59/out/sha1s.txt (fc_6 2fbe13a615f6, fc_10 53a8f01c3bfa) |
| 11, 12 | 285, 310 | 121, 144 (frec, §4) | not run | | | | |
The sha1s of fc_3, fc_6 and fc_10 equal R115's. SBC = N² holds for N = 3..12 with my engine; R115 had it for N = 3..10 with sf2.py.

Anatomy of one record (fc_5, k = 3; box59/window.py; states of the distinct-σ sequence):
- State 130: h_3 escapes (record).
- State 132: w → l_3. The lane (b_* → x → w → l_3) now carries m_3.
- State 133: x → w, so d carries m_3. f_2 and f_1 have left their cycles into the lane. v_2 → r_3 is switched now, one step after
  the lane. z_2 is still → p, so the escape route of h_2 (m_2 → z_2 → p) lacks m_3. Odd at h_2 keeps m_2: it AVOIDS the even m_3.
- State 134: z_2 → v_2 and e_2 → d. Now both routes from h_2 carry m_3. The escape carries m_2 on top, so Odd reverts: h_2: m_2 > e_2.
- States 135, 136: h_1 and h_0 revert the same way, one per step. Each opened cycle i + 1 puts k_(i+1) (odd) on the chain of
  cycle i before the chain can skip it.
- After the cascade (state 137): v_0 → v_1, v_1 → v_2, v_2 → r_3. Every lower escape chain skips the open bits straight to the
  record. d enters at the lowest set bit (y → l_0 once h_0 is set again, state 145).

### 1.3 The F-invariant, stated
Lemma LATENCY (PROVED, lane; immediate from P-N5-SF SF-TERM (i)). For every σ with Iσ ≠ ∅ and every Even v: F(σ)(v) ∈ {σ(v)} ∪
{w : (v, w) ∈ Iσ}. So a new value at a vertex w can reach σ(v) only through edges that are improving w.r.t. Ξσ when they are
switched. If a route to w runs through a vertex x whose current Ξσ(x) does not beat the alternative at its predecessor, the route
costs at least one extra F-step per such x.
Proof. SF-TERM (i) (frozen packet): S4a′'s arena gives every Even v only σ(v) and the targets of Iσ(v), and S4c picks an edge of Iσ(v). □
READING (fcN, backed by FCOPEN / FCLAT for N = 3..10):
- At a record k the lane reaches l_k by a one-edge switch (w → l_k; its head's value just improved).
- The escape chain of the top lower bit needs v_(k−1) → r_k and THEN z_(k−1) → v_(k−1). The second is not improving until Ξ(v_(k−1))
  has changed. Before the record, v_(k−1)'s route into l_k ran through the open cycle k and the lane back into the lower bits, so it
  was worth less than p.
- In the one-step gap every escaping lower cycle opens to the lane (FCOPEN). Then the cascade follows.
- At a re-set of bit j below the top, the news enters at l_j. It reaches d (which enters at the lowest set bit) and every closed lower
  cycle's escape (which runs up the same chain) through the same edges at the same F-step: fcword's "SET" rows give lag 3 for d and
  for every f_i in 215 of 216 events, N = 3..10, records included (the exception: a set of bit 0 in fc_10 at transition 1381, lag 2
  for d, no lower cycle). Nothing opens (FCOPEN).
- The difference is WHERE f_i gets m_k from: from the lane after opening (records), or from its own escape (re-sets).
- Lane walks: each re-set bit closes after its own lane walk (deceleration timing). That is iterations, not SBC. The walks do not
  compound because a re-set triggers no cascade.
What is NOT proved: that W_N holds for every N. The table is DATA for N ≤ 12 (W) and N ≤ 10 (FCOPEN, FCLAT). A proof would be an
induction over the run of fcN, which I have not written.

## 2. Why this is F's step structure, not monotonicity (READING)
- T48 (L-LIT, opened by L-LIT): MONO-XI + argmin allows n^Ω(log n) argmin changes, the parametric shortest path lower bound. So any
  degree bound must use F's discrete steps.
- The fcN count does use them. The reset is a race of HOP COUNTS: lane 1 hop versus escape chain 2 hops. LATENCY is the only property
  of F involved.
- I^glo (switch-best against the true reply, box 57 / 58) closes the same race differently: by Lemma STALE its lags come from the stale
  frame. Look-ahead (box 58) equalises hop counts and restores the binary counter. That fits: the cascade needs a hop-count gap.

## 3. (b) Nesting (READING + OPEN)
- Cost of an external reset (READING). Suppose an upper block U resets a lower fc block L through L's lane (L's lane gets U's news and
  L's escape chains get it later). By §1.2 this is a cascade: ≤ N_L reverts. After it, L's chains point past every open bit to the
  exit (the post-cascade state of §1.2). Every later L-set is then a re-set, with no records. So one external reset costs ≤ 2 N_L
  flips, linear in the block, not N_L². The lower block's own N_L² is paid once.
- So SBC_nest ≈ N_U² + N_L² + 2 N_L · (number of external resets of L). Degree 3 needs superlinearly many external resets, i.e.
  superlinearly many events at which L's lane gets news by a strictly shorter hop route than L's top escape chain does.
- Necessary condition N-COND (READING): each such event needs a vertex on L's escape route whose current Ξ does not yet beat its
  alternative (a stale intermediate, LATENCY). In fcN that vertex is v_(k−1). It is stale only because its route into the new event
  ran through an open cycle and the lane back into the block.
  - For an upper RE-set (not a record of U) the route from L's escape into U's chain does not loop through L. It is then prepared
    exactly as in fcN's re-climb.
  - So with U's reset source outside L, external resets ≤ U's records + O(1) per record = O(N_U), and the degree stays 2.
  - A degree-3 gadget must route U's reset source (or U's chain) back THROUGH L. Then every U event makes L's escape intermediates
    loop, hence stale.
- OPEN: whether such a routing keeps U's own counter alive. U's lane would then receive L's news too. This is the test for L-RED 28's
  nested families. I do not coordinate with it; the Lead relays.
- Prediction (CONJECTURE PV, §4): in any nested family, the maximum per-vertex flip count stays ≤ n.

## 4. (c) Candidate potentials tested on the corpus
Tools: box59/flips.py (per flip: the decisive vertex of Odd's comparison before and after), box59/frec.py (per game: SBC, k_O = #Odd
vertices with ≥ 2 successors, max flips(u), FLIP-REC° excess), box59/corpus.sh. Logs: box59/frec_all.txt (514 games, the 413 of
P-N5-SF's alt_all list at the S3 start, NOT their pinned starts; box55/hard.lst 73; box54/fam.lst 20; fc_3..10), box59/frec_rnd.txt
(200 seeded random games, box59/rnd.py: 150 with n = 20..80 and out-degree ≤ 3, 50 with n = 60 and out-degree ≤ 2),
box59/frec_big.txt (fc_11, fc_12, switchbestexp 9..12). No timeouts, every game printed a line.
| candidate | statement | result |
| --- | --- | --- |
| FLIP-REC° | flips(u) ≤ 2 REC°(u) + 1 (REC° = changes of the top non-sink vertex of Ξ(u)) | DEAD: 44 / 514 fail; so_sorl_n32 (sha1 ce8f7013…): u = 13, 22 flips, REC° 0; switchbestexp_12: 51 flips, REC° 5. Exact on fcN |
| (u, decisive vertex) multiplicity | each Odd vertex flips O(1) times per decisive vertex | DEAD on fcN: h_i's decisive vertex alternates between h_i and m_i, 2N − 1 times |
| PV | flips(u) ≤ n for every Odd u | 0 violations on 720 games. Max 0.917n (so_sor5_n24, k_O = 1, 22 flips), random ≤ 0.10n, fc_12 23 = 0.074n, switchbestexp_12 51 = 0.165n (39, 41, 47, 51 for N = 9..12) |
| SBC ≤ k_O · n | the sum of PV | 0 violations; max SBC/(k_O n) = 0.917 (so_sor5_n24). fcN: N²/(N(25N + 10)) → 1/25 |
- CONJECTURE PV (OPEN): for every game and every start, along F's distinct-σ sequence every Odd vertex u has at most n indices j with
  σ̄(σ^(j+1))(u) ≠ σ̄(σ^(j))(u); the mirror for τ. Consequences:
  - SBC ≤ k_O·n + k_E·n ≤ n².
  - By P-N5-SF Theorem SF-RED (b), I < (n + m + 1)(2(n² − n + 1) + n²): N5-SF would be polynomial.
  - PV is not implied by MONO-XI (T48's barrier). A proof must use LATENCY-type step structure.
- Proof plan (OPEN, not attempted beyond §1): (i) every revert at u follows an opening of u's cycle in a hop-count gap (§1.3);
  (ii) the gaps seen by one u are injective into the records of one source; (iii) each source has ≤ n records. (iii) is plausible
  (my argument from SPEC S1's order, unchecked by a referee): along improvements the most relevant vertex of a path set either rises
  to an even vertex or drops an odd one, so once it is even it only rises; ≤ n changes per cycle node. Caveat: the SINK-MASKED top of
  FLIP-REC° is not covered by this argument, and FLIP-REC° is DEAD.
  (ii) is where switchbestexp's leapfrog vertex (box 55: 2^N − 1 flips for N ≤ 4, 41 at N = 10) must be checked first.

## 5. Dead ends (also in notes/L-NEW.md)
- FLIP-REC° (§4): DEAD, experiments/red/so/instances/so_sorl_n32.pg (sha1 ce8f7013…): Odd vertex 13 makes 22 best-reply changes while
  the top non-sink vertex of Ξ(13) never changes. Obstruction: the flips are driven by low path vertices; the top does not see them.
- Decisive-vertex multiplicity (§4): DEAD, box59/out/fc_5.pg (sha1 6e916303…): h_0's decisive vertex alternates m_0 / h_0 nine times.

## DONE / FINDINGS / NEEDS
- DONE: box59/flips.py, frec.py, corpus.sh, rnd.py, fcword.py, window.py, probe.py; logs fcword.txt, frec_all.txt, frec_rnd.txt,
  frec_big.txt; this note; check.sh block "Box 59".
- FINDINGS: (1) DATA: fcN's flip word is W_N for N ≤ 10 (SBC = N² for N ≤ 12) (resets only in cascades after records). Lemma COUNT (PROVED) gives N².
  (2) The mechanism is F's one-step latency (Lemma LATENCY, PROVED, plus FCLAT DATA): a record reaches the lane one F-step before
  the escape chain; a re-set reaches both together, so it never cascades.
  (3) READING: an external reset of a fc block costs O(bits). Degree 3 needs the upper source routed back through the lower block
  (N-COND); OPEN.
  (4) CONJECTURE PV (each Odd vertex ≤ n flips; implies SBC ≤ n² and N5-SF polynomial): 0 violations on 720 games, max 0.917n.
  (5) DEAD: FLIP-REC°, decisive-vertex multiplicity.
- NEEDS: none from the owner. For the Lead: run frec.py on L-RED's nested families when they land. Max flips(u) > n kills PV.
