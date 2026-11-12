# Box 101: LAM-GAP proved (lane): in a one-player game, a Howard window with every Λ constant lasts at most |Ch| + 1 iterations; so SCC-LIN (polynomial form) ⇐ DEEP3 alone
L-SI successor 51 (Opus 5.5), D18 / D14 / D1; Lead 09:07Z («BOX 101 = the LAM-GAP proof attempt, approved, with one gate in front of it:
STEP 0 (literature, short)»). Labels: PROVED (L-SI lane, unrefereed) / CONJECTURE / DATA (unit, set, scope, counter) / OPEN (literature) /
READING. Not a TARGET.md claim; not M3 or M4; not a gauntlet step; G-N5-TIME stays OPEN; N5′-xi stays a CANDIDATE (D1). Tools:
experiments/si/box101/ (lamgap101.py, run101.sh, check101.sh); VJ engine L-RED 65 own.py (claude/l-red 59daaef2, read-only).

## 0. Answer
- STEP 0 (§1). The general statement behind L1 is OPEN in the literature: «Howard on a deterministic MDP makes at most #edges iterations»
  is Hansen's conjecture (quoted in arXiv 2506.12254 as Conjecture 3.1, citing Hansen 2012, Conjecture 6.1.1), and «the best known upper
  bound is exponential» (same paper, abstract and §1). So a polynomial bound for Howard on general weighted one-player games is not
  something to expect from this lane.
- Our case is narrower in one exact way. Under the VJ valuation the «gain» of a play is its cycle's top vertex Λ, so a vertex has at most
  n distinct gains, and they rise monotonically. In mean-payoff DMDPs the gain is a cycle mean, and there are exponentially many. With
  the gain counted by DEPTH-COUNT3's Λ part, what is left is the fixed-gain window: §5.1's missing step.
- Lemma LAM-GAP (PROVED, lane; §2). In every one-player game under the VJ valuation, a maximal window of a Howard run in which Λ(v) is
  constant for every vertex v has at most |Ch| + 1 iterations (Ch = the Even vertices with a choice). §5.1's obstacle (a switch that
  closes a cycle) is harmless:
  - a closed cycle that avoids the window's top ℓ has another top, so Λ changes and the window ends;
  - a closed cycle through ℓ leaves val(ℓ) = (ℓ, ∅, 0) unchanged.
- Corollary L1-POLY (PROVED, lane; §3). L1(C) ≤ (n3(n3 − 1) + 1)·(N_C + 2). Howard on every one-player game G_C[φ] is polynomial.
- Corollary (PROVED, lane, from box 100 WINDOW with LAM-GAP; §3), for every c ≥ 0:
  H-run(C) after t0 ≤ (1 + E_C + n3(n3 − 1) + 2·I_C·(n3 − 1 + n3(S_c(n3) − 1)) + Deep_c(C))·(N_C + 2).
  So SCC-LIN in polynomial form, and with SCC-RED a polynomial T3, now rest on CONJECTURE DEEP3 ALONE (box 100 §5.2).
- Not claimed: H(C) ≤ M_C (the exact SCC-LIN); novelty of LAM-GAP (it is an elementary Bellman–Ford argument; I did not find it in the
  sources opened, which treat mean-payoff, not VJ, valuations).

## 1. STEP 0: literature (sources opened; notebook entry «Sources opened», box 101)
- arXiv 2506.12254v1 (Asadi, Chatterjee, de Raaij, «Lower Bound on Howard Policy Iteration for Deterministic Markov Decision
  Processes»; full text, pdftotext of the arXiv PDF):
  - Abstract: «the best known upper bound is exponential».
  - §3, Conjecture 3.1 «([Hansen, 2012, Conjecture 6.1.1]). The number of iterations performed by Howard's algorithm, when applied to
    a DMDP, is at most the number of edges.»
  - Theorem 3.2 (Main Result; fractions as rendered by pdftotext): a DMDP with 2n vertices and (3n² + n)/2 edges on which Howard
    performs (n² + 7n − 6)/2 iterations
    (fewer than the edges, so it is consistent with Conjecture 3.1).
  - §1 describes Hansen–Zwick 2010 as «DMDPs with 2n vertices, m edges, and edge weights of O(n^(n²)), on which the algorithm requires
    m − n + 1 iterations», and adds: «the best known upper bound is exponential as the weights are exponential».
  - Hansen 2012 and Hansen–Zwick 2010 are cited here only as quoted by 2506.12254 (not opened themselves).
- arXiv 1008.0530 (Hansen, Miltersen, Zwick; abstract): strategy iteration is strongly polynomial for turn-based stochastic games with a
  CONSTANT discount factor, O((m/(1 − γ))·log(n/(1 − γ))) iterations. Not our case: VJ / parity corresponds to no fixed discount.
- arXiv 1208.5083 (Post, Ye; abstract): the SIMPLEX method with the highest-gain rule is strongly polynomial on discounted DMDPs,
  O(n³m²log²n) iterations at uniform discount. It concerns simplex, not Howard; the page states no open problem.
- Plain answer to the Lead's gate. LAM-GAP plus the Λ count does NOT imply Hansen's conjecture or any polynomial bound for Howard on
  mean-payoff DMDPs: the VJ valuation is a different, coarser algorithm state (gain = top vertex, then the set Π, then the length). It
  implies only the VJ statement «Howard on one-player games under the VJ valuation makes O(n²·|Ch|) iterations» (§3). That statement is
  narrower than the open one, and §2 proves it.

## 2. Lemma LAM-GAP (PROVED, lane)
Setting: a one-player game (every non-Even vertex has one successor; for G_C[φ]: Odd fixed by φ at C's gates and constant elsewhere
after t0; non-mover Even vertices frozen). Ch := the Even vertices allowed to switch (for G_C[φ]: C's movers). VJ value of v under σ:
(Λ, Π, len), where the play is a lasso, Λ is the most relevant vertex of its cycle, and the path from v to the first visit of Λ is
simple, of length len, with Π its vertices more relevant than Λ. Order ⊴ as in box 100 §3. Howard: every v ∈ Ch with a successor of
strictly larger value moves to a ⊴-best successor; otherwise it keeps its current one (any tie resolution).

Premise. (M) val_(t+1) ⊵ val_t pointwise: RESULTS R15 (a) («a switch set of improvements does not lower any value»), in the one-player
case. Elementary facts about VJ path values:
- (P1) If v ≠ Λ(v), then val(v) = ext(v, val(σ(v))). Here ext(v, (ℓ, Π, len)) := (ℓ, Π ∪ ({v} if v is more relevant than ℓ), len + 1),
  and σ(v)'s path to ℓ is the suffix of v's, so it avoids v.
- (P2) ext(v, ·) is strictly order-preserving on values whose paths avoid v: Λ is unchanged, v enters both Π or neither, and len rises
  by 1 on both.
- (P3) If Λ(v) = v, then val(v) = (v, ∅, 0).

Statement. Let a..b be a maximal run of states of a Howard run with Λ_t(v) = Λ_a(v) for every vertex v and a ≤ t ≤ b. Then b − a ≤ |Ch| + 1.

Proof.
Notation: Tops := {ℓ : Λ_a(ℓ) = ℓ}, constant on the window. For a simple path P from v to ℓ ∈ Tops: value(P) := (ℓ, its vertices
before ℓ more relevant than ℓ, its length), and c(P) := the number of vertices of Ch on P before ℓ. opt(v) := the ⊴-maximum of value(P)
over the simple paths P from v to Λ_a(v).
- (U) Upper bound. For t in the window, val_t(v) = value(the path of v's play to Λ(v)) ⊴ opt(v).
- (L) Claim: for a + k ≤ b, every vertex v and every simple path P from v to any ℓ ∈ Tops with c(P) ≤ k: val_(a+k)(v) ⊵ value(P).
  Induction on k, and inside one k along P from ℓ backwards. Let P = v, u, …, ℓ, with P′ the suffix from u.
  - v = ℓ: trivial.
  - v not in Ch (deterministic): by the induction, val_(a+k)(u) ⊵ value(P′).
    - If v ≠ Λ(v), then val(v) = ext(v, val(u)) ⊵ ext(v, value(P′)) = value(P) (P1, P2; both paths avoid v).
    - If Λ(v) = v, then u's play returns to v, so Λ(u) = v. Then val(u) ⊵ value(P′) forces rew(v) > rew(ℓ) (v ≠ ℓ), so
      (v, ∅, 0) ▷ value(P).
  - v ∈ Ch: c(P′) ≤ k − 1, so val_(a+k−1)(u) ⊵ value(P′). Howard at a + k − 1 gives v a successor w := σ_(a+k)(v) with
    val_(a+k−1)(w) ⊵ val_(a+k−1)(u) (w is ⊴-best, or the kept current one is best). By (M), val_(a+k)(w) ⊵ value(P′).
    - If v ≠ Λ(v): val_(a+k)(v) = ext(v, val_(a+k)(w)) ⊵ ext(v, value(P′)) = value(P). This uses P1 and P2 at time a + k, where w's
      path avoids v. It never applies ext to val_(a+k−1)(w), whose path may pass v: this is the point where §5.1's «same-top cycle»
      worry is avoided.
    - If Λ(v) = v: as in the deterministic case.
- (O) By (L) with k = |Ch| (every simple path has c ≤ |Ch|) and (U): if t* := a + |Ch| ≤ b, then val_(t*) = opt on every vertex.
- (E) Exit. Suppose t* + 1 ≤ b, and v ∈ Ch with v ≠ Λ(v) has an improving switch at t* to w, with val_(t*)(w) ▷ val_(t*)(σ v). Let
  ℓ := Λ(v).
  - If Λ(w) ≠ ℓ: at t* + 1, v → w gives Λ(v) = Λ(w) ≠ ℓ (whether or not v lies on w's cycle). This contradicts Λ constant at t* + 1.
  - If Λ(w) = ℓ and w's path Q at t* avoids v: ext(v, value(Q)) is a simple-path value ⊴ opt(v) = ext(v, opt(σ v)), so by P2
    value(Q) ⊴ opt(σ v) = val_(t*)(σ v). Not improving: contradiction.
  - If Q passes v: at t* + 1, v → w, and (U) with (M) give val_(t*+1)(w) = opt(w), by a path that now avoids v (it is the suffix of
    v's). So ext(v, opt(w)) = val_(t*+1)(v) ⊴ opt(v) = ext(v, opt(σ_(t*) v)). By P2, opt(w) ⊴ opt(σ_(t*) v), which contradicts the
    improving switch.
  So at t* only top vertices ℓ ∈ Ch switch. At t* + 1 all values are unchanged (= opt, by (U) and (M)), so each such ℓ is already at a
  best successor, and by the same case analysis every non-top improving switch at t* + 1 ends the window. Hence b ≤ t* + 1 =
  a + |Ch| + 1. ∎
- Where the earlier attempt (box 100 §5.1) stuck: it asked for optimal substructure of opt paths. The proof does not need it, because
  (L) quantifies over ALL simple paths and is driven by monotonicity (M), not by suffix-optimality.
- DATA (lamgap101.py; unit: Howard run on a random one-player game; set: seeds 1, 2 (3,000 games each, n ≤ 9, 30% with an added fuse
  path), seed 3 (2,000 games, n ≤ 40); both tie rules; out/lamgap_*.out). Must-0 counters, all 0:
  - pathfail: claim (L) brute-forced at n ≤ 7, 23,412 / 23,124 path checks on seeds 2 / 1;
  - gapfail: the bound;
  - optfail: (O), 269 / 238 windows reaching t*;
  - lfail: L ≤ (#Λ-steps + 1)(|Ch| + 2).
  Controls fire: CTRL=1 (bound ⌊|Ch|/2⌋) gapfail 137; PCTRL=1 (paths with ≤ k + 1 choices) pathfail 2,117.
  - Limit of this data: random games have short runs (max window 6, max T 9). The long windows are on Γ3 (box 100 §5.1:
    MWR4/8/16_2 gap 26 / 50 / 98 ≤ N_C 44 / 80 / 152), which agrees.

## 3. Consequences (PROVED, lane)
- Corollary L1-POLY. A Howard run of G_C[φ] splits into windows at the states where some Λ changes. By (M) every Λ only rises in
  reward, so at most n3(n3 − 1) such states over the vertices of Γ3(G). Each window has ≤ N_C + 2 states (LAM-GAP with Ch = C's
  movers). So L1(C) ≤ (n3(n3 − 1) + 1)(N_C + 2).
- Corollary SCC-POLY ⇐ DEEP3. This is box 100 Theorem WINDOW with Λ constancy over all vertices, so that windows match LAM-GAP's.
  - The Λ-change count becomes n3(n3 − 1) instead of N_C(n3 − 1); the proof is unchanged, by DEPTH-COUNT3 per vertex.
  - Gap(C) ≤ N_C + 1 by LAM-GAP, applied to G_C[σ̄_a]: a two-player window is a one-player window of that game (box 100 §4).
  - Result: H-run(C) after t0 ≤ (1 + E_C + n3(n3 − 1) + 2·I_C·(n3 − 1 + n3(S_c(n3) − 1)) + Deep_c(C))·(N_C + 2), for every c ≥ 0.
  - With SCC-RED (box 99 §2, with Addendum A): if for some fixed c Deep_c is polynomial on a family, T3 is polynomial on it.
- What stays open: CONJECTURE DEEP3 (box 100 §5.2; the Γ3 form of L-NEW 70's DEEP-k1, for internal gates of one SCC). It is now the only
  open premise of this route to SCC-LIN in polynomial form. L-RED 66 is queued to attack it (Lead 09:07Z); the start is DHIB26_2804's
  24 deep flips (sha1 2c49fd10).

## 4. Sources opened (this box)
- arXiv 2506.12254v1 full text (abstract; §1; §3 Conjecture 3.1, Theorem 3.2; §5).
- arXiv 1008.0530 (abstract). arXiv 1208.5083 (abstract).
- Not opened, cited only as quoted by 2506.12254: Hansen 2012 (thesis, Conjecture 6.1.1); Hansen–Zwick 2010 (ISAAC, LNCS 6506).

## Addendum A (L-SI successor 51, 2026-11-12T09:54Z (date -u); append-only, §0-§4 unchanged): the chain to a polynomial T3, and its scope
Lead 09:56Z: «write this first, before box 102 work». Everything below is a CONDITIONAL of lane lemmas. All of them are unrefereed except
the landed R-ids named. DEEP3 is a CONJECTURE. Nothing here is a TARGET.md claim, M3 or M4.

### A.1 The chain (polynomial T3 ⇐ DEEP3)
Columns: link | statement (short) | status | attacked by, verdict | premises (landed R-ids).

| link | statement | status | attacked by, verdict | premises |
| --- | --- | --- | --- | --- |
| REACH3-ALL, END-T3 | N5′-xi from S3 on Γ3(G) is a HOW3 run at the movers until its first fallback at T3 + 1; it makes exactly T3 + 3 iterations | LANDED (R125; R124 END-T3, its condition discharged by R125) | both referees (signed) | R104, R117, R118, R124, R125 |
| SCC-RED (box 99 §2 + Add. A) | T3 ≤ max over SCC chains of D(G) of Σ (H(C) + 1), H(C) over all legal tie resolutions | PROVED, lane | L-RED 65 R232: SURVIVES, with wording gap G1 (fixed in Add. A) | R125 (HOW3, reachability from R104's edges) |
| CAP (box 99 §3) | an option's value is capped by its β-face | PROVED, lane (not used by the bound itself) | L-RED 65 R232: SURVIVES | R125 (f) LOC-GATE3, (i) NO-TIE3, CN2-3, F4′ |
| ONE-CROSS3 + INT-ONLY (L-RED 65, R232 §0) | a gate with a constant face flips ≤ 1 time; in G_C after t0 only internal gates re-flip | PROVED, lane (L-RED's own) | not attacked by another lane | R125 (d) F1, (f), (i) |
| TWO-CROSS (box 100 §2) | each flip away from a face = a change of that face; flips ≤ ch(pe) + ch(pβ) | PROVED, lane | not yet attacked | R125 (d) F1, (f), (i) |
| DEPTH-COUNT3 (box 100 §3) | per vertex ≤ n3 − 1 Λ changes and ≤ n3(S_c(n3) − 1) changes of depth ≤ c | PROVED, lane (transfer of L-NEW 70's box 206 lemma) | not yet attacked | R125 (d) F1; the VJ order (VJ00 §4.2, R118's premise list) |
| WINDOW (box 100 §4; all-vertex form in §3 here) | the run in C after t0 ≤ (#windows) · (window length) | PROVED, lane | not yet attacked | R125 (HOW3, [OPT] best response), box 99 §1 |
| LAM-GAP (§2 here) | a one-player Howard window with every Λ constant lasts ≤ \|Ch\| + 1 iterations | PROVED, lane | queued: L-RED 66 first item (Lead 09:56Z) | R15 (a) |
| L1-POLY, SCC-POLY (§3 here) | L1(C) ≤ (n3(n3 − 1) + 1)(N_C + 2); H-run(C) ≤ (…)·(N_C + 2) | PROVED, lane (corollaries of the rows above) | not yet attacked | as the rows above |
| DEEP3 (box 100 §5.2) | for some fixed c, internal-gate flips charged to depth > c are polynomially many | CONJECTURE (DATA only) | queued: L-RED 66 (kill side); L-SI box 102 (proof side) | none |

The conditional, as one sentence: if DEEP3 holds on a family of genomes, then by SCC-POLY and SCC-RED, T3 is bounded by a polynomial in
N + M on that family. By END-T3, N5′-xi from S3 on Γ3(G) then makes a polynomial number of iterations.

### A.2 Scope, in TARGET.md's terms
- What T3 counts: the number of HOW3 states of N5′-xi's run (R118's [N5XI], SPEC with box 190's S4a tie rule) from S3 on Γ3(G) before
  its first fallback (R125 REACH3-ALL; T3 + 1 = the first fallback). The run's total is exactly T3 + 3 iterations (R124 ENDGAME-3 /
  END-T3).
- Inputs: the games Γ3(G) for every genome G of R104 (R117's Γ3; Ξ-cycles and Ξ self-loops allowed; any Ξ-feedback number k). This is
  under the standing SPEC premise 1E-N3 of R57 (b), as in R104 / R117 / R124.
  - The chain does NOT use [E-LEV], a bound on k, or IDEAL-ACYC: every premise above is stated for every genome.
  - DEEP3 itself is stated for every genome. Its DATA (box 100 §5.2) covers 26 frozen instances and 400 random genomes only.
- What ENDGAME-3 adds (R124, landed): after the first fallback there are exactly 2 more iterations, so the WHOLE run of N5′-xi (and of
  N5) is T3 + 3, resp. F + 2 iterations. A bound on T3 is therefore a bound on the run. For N5 (SPEC's own S4a tie rule), R125's REACH3-ALL
  is stated for N5′-xi only. The chain would cover N5 only if N5's mover phase is also a HOW3 run (any legal tie resolution, as H(C) now
  allows). That is NOT established here.
- What the chain would NOT give:
  - M4. TARGET.md §2 asks for an algorithm polynomial on EVERY parity game; §4: «Polynomial only on a restricted class … does not
    count as M4». The Γ3(G) games are a restricted class (the genome games of R104), and the chain says nothing about N5 or N5′-xi on
    any other game.
  - TARGET.md §4 also excludes «Correctness or running time resting on an unproved conjecture»; this rests on DEEP3.
  - It counts iterations only: the cost of one iteration at bit cost (TARGET.md §3, gauntlet step 4) is a separate item.
  - It gives no exact bound (H(C) ≤ M_C, U-FREE's T3 ≤ N + M + 4); the polynomial is crude (degree about c + 4 in n3).
- Plainly: a chain of lane lemmas, unrefereed (except the landed rows), ending in CONJECTURE DEEP3. G-N5-TIME stays OPEN; N5′-xi stays a
  CANDIDATE (D1).
