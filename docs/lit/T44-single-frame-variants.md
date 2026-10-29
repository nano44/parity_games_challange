# T44: single-frame variants of N5 (N5-SF) against known algorithms, lower bounds, and DLM's lock (for L-NEW 32, BOX 54)
L-LIT successor 3 (Opus 5.5), D18. Lead's message 14:45Z: «(a) Which known algorithm is N5-SF closest to, for each natural single-frame
choice: "choose by Ξ", "arena by W", and "switch to the opponent-best-reply edge" (= SSI)? (b) For each, which known lower bound applies ...
with theorem numbers? (c) Does removing the frame split re-open DLM's lock? ... Run it on DLM's family if a variant definition is concrete
enough.» Written 2026-10-29 from 14:50Z (date -u). Working note, unrefereed. Not a TARGET.md claim; G-N5-TIME stays OPEN.
Labels (D18): PROVED (L-LIT, unrefereed) / DATA / READING / SOURCE (opened; notebook "Sources opened") / OPEN.
Tools (this note, committed): docs/lit/T44-sf-variants.py (the variants, run next to n5.run "n5" and "ssi"), docs/lit/T44-sfw-cycle-check.py
(independent re-check of the "arena by W" runs with a play-simulation valuation, no si.py Engine), docs/lit/T44-rcyc10.pg (10-vertex witness).
Read only: experiments/new/n5.py, experiments/si/si.py, experiments/new/dlm_gen.py, experiments/friedmann-hn/instances (L-COMP's H_n).

## Summary
| variant (§0) | arena | choice | closest known algorithm | known lower bound that applies | DLM's lock re-opened? | DATA (this note) |
| --- | --- | --- | --- | --- | --- | --- |
| N5 (SPEC) | Ξ (vs σ̄) | W (vs current τ) | — | none known (T20, T43) | no | dlm1 n 1..7: 1,2,4,4,6,7,8; H3-H5: 34,41,49 |
| SF-Ξ "choose by Ξ" | Ξ | Ξ (Odd free) | Schewe's globally optimal SI, Friedmann's I^glo, run by each player independently | Friedmann 1106.0778 Thm 8.4 (≥ 2^n steps on H_n from ι_{H_n}); with a per-vertex Ξ-best choice instead: I^loc, Thm 6.14 (G_n) | no (ignores the opponent; dlm1 in 1 iteration) | H3, H4, H5 from L-COMP's F start: 107, 235, 491 = I^glo's 16·2^n − 21 exactly |
| SF-W "arena by W" | W (vs current τ) | W | naive / simultaneous symmetric SI (STV Alg. 2, attributed to Condon; Pollatschek-Avi-Itzhak) with each best reply cut to one I^glo step of the one-player game | none needed: it does NOT TERMINATE | no (iteration 1 sets every level's final edge, as N5) | CYCLES on dlm1 n 5, 6, 7, dlm2 n 2, 3, 4 and on a 10-vertex random game (period 4) |
| SF-SSI "switch to the opponent-best-reply edge" | Ξ ∩ opponent best reply | — | = SSI (STV Alg. 3/5; DLM Alg. 2) | DLM 2309.02223 Thm 1 via Prop. 7 + Lemma 12 (2^(n+1) − 3, any rule in the candidate set), Thm 13 via Prop. 11 (7·2^(n−1) − 5) | YES, by definition | dlm1 n 1..7: 2^(n+1) − 3; dlm2 n 1..4: 7·2^(n−1) − 5 |
**Finding.** Each natural single-frame N5 is already covered by a known obstruction: SF-Ξ IS Friedmann's I^glo (exponential, Thm 8.4,
reproduced exactly on L-COMP's H_n), SF-W does not terminate (DATA, two independent checks), SF-SSI IS SSI (exponential, DLM Thm 1).
So the frame split is not incidental: Ξ in the arena is what gives N5 termination (R15), W in the choice is what makes N5 leave both
Friedmann's H_n and DLM's families. A single-frame variant to which R17's per-phase argument applies must give up one of the two.

## 0. The variants (concrete; T44-sf-variants.py)
- Common to all: SPEC S1 valuations, S3 start (or a given start pair), both steps from the SAME (σ, τ) applied together (S4), as n5.py.
  Only S4a/S4b change. Notation as T40 §0: Ξ = valuation vs Odd's optimal counterstrategy σ̄ (the improving frame); W = valuation of the
  (σ, τ) plays, i.e. Ξ of the one-player game G_τ (Odd fixed to τ); dually for Odd.
- SF-Ξ: arena A(v) = {σ(v)} ∪ Iσ(v) (S4a's arena); σ_new = an OPTIMAL strategy of the arena game with Odd FREE (all Odd edges), i.e.
  the Ξ-maximum over the arena; computed by switch-all SI inside the arena game from σ. Odd dually on G^d. No fallback is ever needed
  (Iσ ≠ ∅ ⇒ σ is not optimal in its arena). Stop: S5.
- SF-W: arena = {σ(v)} ∪ {w : (v, w) W-improving}, W-improving = improving in G_τ; σ_new = S4a's selection (Even's optimum in the
  arena against τ; the same Engine call and tie-breaks as n5.py). Odd dually against σ. Stop when both W-improving sets are empty (a mutual
  best reply, hence optimal), or when the selection changes nothing (§3: only length-degenerate W-edges; regions then checked).
- SF-SSI: n5.run mode "ssi" = DLM Alg. 2 with switch-all inside Iσ ∩ {(v, τ̄(v))} (τ̄ = Even's best reply to τ), dually for Odd.
- Extra (not single-frame; asked by no one, cheap): SF-INT, arena = {σ(v)} ∪ (Iσ ∩ W-improving), choice as S4a, S4c fallback. It
  terminates (every switch is Ξ-improving). DATA: its iteration counts EQUAL N5's on all 14 instances below (dlm1 1..7, dlm2 1..4, H3-H5).

## 1. SF-Ξ = Schewe's globally optimal strategy improvement (Friedmann's I^glo)
- SOURCE. Friedmann, "An exponential lower bound for the latest deterministic strategy iteration algorithms", arXiv 1106.0778 v2 (LMCS
  7(3:19) 2011), pdf sha256 46c96f44… (= L-COMP's file, experiments/friedmann-hn/README.md); v1 sha256 a35e4ef6… has the same wording.
  §3 p.5-6: improvement arena A_{G,σ}: «vE′u :⇔ vEu and (v ∈ V1 or (v ∈ V0 and σ(v) ⪯σ u))»; an improvement policy «selects a strategy for
  player 0 in a given improvement arena». §4 p.6-7: «The locally optimizing policy I^loc selects a most profitable strategy decision in
  every point with respect to the current valuation»; «The globally optimizing policy I^glo ... computes a globally optimal successor
  strategy in the sense that the associated valuation is the best under all allowed successor strategies ... we have for an arbitrary
  strategy σ′ in the arena A_{G,σ} that Ξσ′ ⪯ Ξσ*» (Schewe [Sch08], Thm 4.2: polynomial time). Theorem 6.14: I^loc «requires at least
  2^n improvement steps on G_n starting with ι_{G_n}». Theorem 8.4: «The Strategy Improvement Algorithm with the I^glo-policy requires at
  least 2^n improvement steps on H_n starting with ι_{H_n}» (pdftotext drops the superscript; "2n" in the text layer).
- PROVED (L-LIT, unrefereed). SF-Ξ's σ-sequence is an I^glo run on G from σ_0, and its τ-sequence an I^glo run on G^d from τ_0; the two do
  not interact (neither step reads the opponent's current strategy). Hence #iterations(SF-Ξ) = max(length of the two runs) ≥ the I^glo run
  of G from σ_0. Proof: the Even step reads only σ (Iσ and the arena game with Odd free); it returns an optimal strategy of the arena game,
  whose valuation is the maximum over the arena (SI on the arena game; optimal valuations are unique), which is I^glo's defining property;
  S5 stops only when Iσ = ∅. □ Caveats: (i) Friedmann's arena keeps edges with σ(v) ⪯σ u (ties), SPEC's Iσ only strict ones; (ii) I^glo
  fixes the valuation, not the strategy, so tie-breaks may differ. Neither changed the count below.
- DATA. On L-COMP's H_n (mode fig; sha1 H3 f7bdd38a, H4 66afd1d7, H5 700e3b2a) from the F start (ι_{H_n}, σ̄(ι)): SF-Ξ 107, 235, 491
  iterations = L-COMP's iglo.py count 16·2^n − 21 exactly (README §1); N5 (n5.run here) 34, 41, 49 = L-COMP's results/tables.md rows
  H3_F, H4_F, H5_F (start sha1 c552ac0d, 051ff741, 20ca0370). SF-Ξ on dlm1: 1 iteration for every n (DLM's optimal strategies differ from
  the start in one improving edge per player, p.10, so the arena optimum is the optimum); dlm2: 2, 3, 5, 7 (n = 1..4).
- READING. Choosing "by Ξ" makes N5 a pair of independent Schewe runs; Friedmann's H_n kills it (gauntlet step 4) with the start ι_{H_n}.
  Replacing the arena optimum by the per-vertex Ξ-best edge gives classical switch-all SI = I^loc, killed by Thm 6.14. Switch-best
  (PGSolver's name for I^glo; T14: Friedmann PhD Thm 4.45) is the same policy.

## 2. SF-SSI = symmetric strategy improvement (STV; DLM)
- SOURCE (opened 2026-10-14 and 2026-10-29, T40 §1 and T43 §(a); notebook rows 1501.06484 v1, 2309.02223 v1). STV Alg. 3 (p.2): «update σ
  using Prof(σ) ∩ σ^c_τ»; DLM Alg. 2 (p.7) the same with a rule f. DLM Proposition 7 (p.10): SWITCH-ALL SSI on family 1 from (σ0, τ0)
  takes 2^(n+1) − 3 iterations; Lemma 12 (p.14): every iteration has a single relevant move, so the count holds for every rule f inside
  the candidate set; Theorem 1 / Theorem 13: exponential lower bounds for SSI and generalised SSI (family 2, Proposition 11, 7·2^(n−1) − 5).
- DATA (n5.run "ssi"): dlm1 n = 1..7: 1, 5, 13, 29, 61, 125, 253 = 2^(n+1) − 3; dlm2 n = 1..4: 2, 9, 23, 51 = 7·2^(n−1) − 5. Instance sha1:
  dlm1 8deacde8, 22b64c39, d8408705, b9e3ffbb, e7c10ed3, fd1c8a75, 38c64e0e; dlm2 5402f5f5, b2efe873, 412fbbf9, a538ec61
  (experiments/new/dlm_gen.py 1|2 n; start pair from its stderr).
- READING. Restricting the choice to the opponent-best-reply edge is the only one of the three variants inside DLM's family; it is SSI
  itself, so the lock is back by definition (T43 (a)).

## 3. SF-W ("arena by W") does not terminate
- DATA (T44-sf-variants.py; each run re-checked by T44-sfw-cycle-check.py: arena = the W-improving edges by play simulation, selection
  optimal in its arena by simulation, every switch strictly W-improving; 0 assertion failures; logs in my scratchpad t44/):
  | instance | n | SF-W | Even / Odd switches until the repeat |
  | --- | --- | --- | --- |
  | dlm1 n = 5 (e7c10ed3) | 12 | state of step 47 = state of step 10 (period 37) | 87 / 79 |
  | dlm1 n = 6 (fd1c8a75) | 14 | step 18 = step 7 (period 11) | 37 / 43 |
  | dlm1 n = 7 (38c64e0e) | 16 | step 46 = step 33 (period 13) | 109 / 120 |
  | dlm2 n = 2, 3, 4 (b2efe873, 412fbbf9, a538ec61) | 22, 32, 42 | periods 17, 16, 21 | 70/68, 337/336, 1102/1073 |
  | docs/lit/T44-rcyc10.pg (sha1 699cc16a; random, seed 7, trial 727) | 10 | step 4 = start state (period 4) | 2 / 8 |
  SF-W terminates on dlm1 n ≤ 4, dlm2 n = 1, H3-H5 (31 iterations each). Random search (T44 scratch rnd.py, S3 start): 0 cycles in 2000
  games each at n = 3, 4, 5, 6, 0 in 1500 at n = 7 and 8; 2 in 1500 at n = 10.
- The 10-vertex cycle (S3 start; v = vertex id): step 1 Odd v6→v2; step 2 Odd v1→v4, v3→v4, Even v4→v8; step 3 Odd v2→v5, v6→v4,
  Even v4→v6; step 4 Odd v1→v9, v2→v0, v3→v7: back to the start pair. Each switch is a strict W-improvement for its owner against the
  opponent's strategy at that step; the two players' simultaneous moves undo each other's reasons.
- Degenerate W-edges (found while testing; why the stop rule has a second clause). In the one-player frame a W-"improving" edge at a cycle
  node can change only ℓ of the target, and switching it re-closes a cycle at the same node with ℓ = 0, so nothing improves (3-vertex
  example: prio [1, 4, 4], owner [E, E, O], succ [[1, 2], [0], [0, 1]], S3 start; Odd's (2, 1) is W-improving, the switch changes no
  valuation). SF-W treats this as a fixpoint; the regions at such fixpoints matched N5's in every random run (checked by rnd.py).
- SOURCE for the closest algorithm (opened, T40 §2): STV p.2 Alg. 2 «Naïve symmetric strategy improvement» (σ′ = σ^c_τ, τ′ = τ^c_σ)
  «earlier been suggested by Condon [5] where it was shown that a repeated application of this update can lead to cycles»; Bertsekas
  2107.10406 v4 §2 p.13 (Pollatschek-Avi-Itzhak oscillates, van der Wal's two-state example). Condon 1993 and van der Wal: primaries NOT
  opened. SF-W differs from Alg. 2 only in taking one I^glo step of the one-player game G_τ instead of the full best reply σ^c_τ.
- READING. SF-W fails gauntlet step "terminates" outright; no lower-bound theorem is needed. Inside a stretch with τ fixed the Even step is
  I^glo on the one-player game G_τ, where R17 bounds the phase; but τ moves in every iteration in which Odd has a W-improving edge, so the
  per-phase bound does not compose: there is no global potential. The cycling mechanism is the classical one (two best-reply dynamics
  chasing each other), now with one-step arenas.

## 4. (c) Does a single frame re-open DLM's lock?
- SF-Ξ: NO. It never reads the opponent's strategy; on dlm1 it stops after 1 iteration for every n (DATA). It is caught by a different
  lock, Friedmann's H_n (§1), which is built exactly for "best valuation in the Ξ arena".
- SF-W: NO. Its first iteration on dlm1 switches every a_i → d_{i+1} and every d_i → a_{i+1} at once (DATA: dlm1 n = 5 step 1, from
  T44-sfw-cycle-check.py), the same jump N5 makes (T43 (b)); it does not fall back to SSI's selection. It then cycles (§3).
- SF-SSI: YES, by definition (= SSI); DATA 2^(n+1) − 3.
- READING. DLM's lock lives in the opponent-best-reply restriction of the CHOICE, not in the frame of the arena (T43 (b)). Removing the
  split towards Ξ trades DLM for Friedmann's H_n; towards W trades it for non-termination; only the restriction to the best-reply edge
  brings DLM back. So for BOX 54: a single-frame N5-SF to which R17's per-phase argument applies needs an additional ingredient that is
  neither of the three, e.g. a Ξ-filter on the W-arena (SF-INT: terminates, and its counts equal N5's on all 14 instances here, DATA), but
  SF-INT is again two frames (arena Ξ ∩ W, choice W), so R17's Case A (a W-better edge outside the arena) is not removed by it. OPEN.

## DONE / FINDINGS / NEEDS
- DONE: this note; T44-sf-variants.py, T44-sfw-cycle-check.py, T44-rcyc10.pg; runs on dlm1 n 1..7, dlm2 n 1..4 (dlm_gen.py), H3-H5 F
  starts (L-COMP's pinned instances), random games n 3..10 (scratchpad). Opened Friedmann 1106.0778 v1 and v2 (§3, §4, Thm 6.14, 8.4).
  Not run: L-COMP's n5b (it implements N5 only; box 5 and box 16 already assert n5 = n5b on dlm and H_n); the counts of "n5" here come
  from n5.run.
- FINDINGS:
  - SF-Ξ = Friedmann's I^glo (Schewe) per player, independent: PROVED reduction; Thm 8.4 applies; H3-H5: 107, 235, 491 = 16·2^n − 21.
  - SF-W does not terminate: cycles on dlm1 n 5-7, dlm2 n 2-4, a 10-vertex random game (period 4); independent re-check passes.
  - SF-SSI = SSI: DLM Thm 1 / 13; counts 2^(n+1) − 3, 7·2^(n−1) − 5 reproduced.
  - DLM's lock returns only with the best-reply restriction; the frame split (Ξ arena, W choice) is what lets N5 escape both H_n and DLM.
- NEEDS: none from the owner.
