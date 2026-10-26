# N5-RISE (box 13): after a rise, no fallback while r > L ⇐ INTO; OLD-THREAT; three dead conjectures
L-SI successor 8 (Opus 5.5; D14, D15, D18, L37, L40). Written 2026-10-25 ~17:10Z (date -u). Lane write-up, unrefereed, not a packet.
Item (3) of the Lead's box-13 GO (15:59Z): the Lead's D18 suggestion, to prove REFEREE-2's DATA observation (R2-N5-ENT §6) unconditionally.
- Labels: PROVED (L-SI succ. 8, unrefereed); CONJECTURE; OPEN; DATA; FALSE (with the instance).
- Everything is on 𝒞^1O (one Odd vertex o with a choice). This is not a running-time bound, and G-N5-TIME stays OPEN.
- Status of the attempt: it STALLS at CONJECTURE INTO (§3). Per the Lead's rule I switch to NEED-β case A2* next.

## 0. Setting and the target
Objects as in RESULTS R31, R35, R40 (scope run S, fallbacks, gates, M_k, lev, COARSE_L, (C1)-(C7), θ, w, r, R̄ / R / F, (h), THR, (A_s)).
- RISE SETTING (R2-N5-ENT rise_end.py's definition):
  - k0 is an in-scope fallback of S with L := M_{k0} ≥ 0.
  - j > k0 is the first S4a step after k0 that changes COARSE_L(θ). Between k0 and j there is no fallback, every transition is in S,
    and r > L.
  - A POST-RISE STATE is a state t > j such that every transition s → s+1 with k0 < s < t is an in-scope S4a step with r_s > L.
- TARGET (REFEREE-2's DATA observation, R2-N5-ENT §6): after a rise, the scope run S has no further fallback.
  - Case (i): a later fallback k with r > L on [k0+1, k]. Then k is a post-rise state, and the transition k → k+1 lies in S.
  - Case (ii): r drops to ≤ L at some state before the next fallback.

## 1. Lemma OLD-THREAT (PROVED, L-SI succ. 8)
Let t be a post-rise state. Let x be an exit of o (x ≠ o) with x ∈ F_{k0} and COARSE_L(o ⊕ Ξ_{k0} x) = COARSE_L(θ_{k0}). Then x ∈ R_t.
In particular, the k0-threat x_{k0} := σ̄_{k0}(o), which is in F_{k0} by H1, lies in R_t.
Proof. Suppose x ∈ F_t.
- FREEZE (Lemma FZ's proof, R40 (b), with the fallback k replaced by t; FZ's proof never uses that k is a fallback).
  - Each s ∈ [k0, t − 1] is the source of a transition of S, so (h) holds there.
  - (A_s) holds on [k0+1, t − 1]: OFFGATE at k0+1, then NL (iii).
  - NL (ii) at each S4a step gives F_{s+1} ⊆ F_s, so x ∈ F_s for every s ∈ [k0+1, t].
  - Across k0, FLAT-ALL (iii) (R31; M_{k0} = L ≥ 0, (h) at k0 and k0+1) gives COARSE_L(Ξ_{k0+1} x) = COARSE_L(Ξ_{k0} x).
  - At each S4a step s → s+1 with k0 < s < t, NL (i) (r_s > L, (A_s), x ∉ R̄_{s+1}) gives COARSE_L(Ξ_{s+1} x) = COARSE_L(Ξ_s x).
  - Hence COARSE_L(Ξ_t x) = COARSE_L(Ξ_{k0} x).
- SANDWICH.
  - x ∈ F_t, so x's (σ_t, τ_t)-play avoids o. o is the only Odd vertex with a choice, so this is x's play under σ_t and every Odd
    strategy.
  - Lemma S (a) (R18 (d)), with Odd choosing x at o, gives θ_t ⊴ o ⊕ W_t(x) = o ⊕ Ξ_t(x) (Lemma G, R19 (a): Ξ = W off R̄).
  - (C1), and (C7) through o ⊕ (o lies on neither path), give
    COARSE_L(θ_t) ⊴_L COARSE_L(o ⊕ Ξ_t x) = COARSE_L(o ⊕ Ξ_{k0} x) = COARSE_L(θ_{k0}).
- MONOTONICITY. θ is ⊴-monotone (R15 (a)), so COARSE_L(θ) is ⊴_L-monotone (C1).
  - The rise at j ∈ (k0, t) is a strict step, and it cannot be undone (C3; as in (Σ6)). So COARSE_L(θ_t) ▷_L COARSE_L(θ_{k0}).
  - This contradicts the sandwich. So x ∈ R̄_t ∖ {o} = R_t. □
- Reading. A rise happens only because Odd's L-best exits at k0 have all been absorbed into R. Odd's new threat is a different exit whose
  COARSE_L value has been frozen since k0.
- DATA (experiments/si/lv13/oldthreat.py, REFEREE-2's traces imported read-only; logs experiments/si/lv13/logs/oldthreat_lib*.txt):
  - REFEREE-2's 295-file 𝒞^1O library (R2-N5-ENT/files.lst), S3 + 2 random starts, own + spec traces: 137 rises, 562 post-rise
    states, 0 failures;
  - 12 climb seeds (REFEREE-2's rise / LV climbs and my box-13 bests): 30 rises, 40 states, 0 failures.
  - The script's minimality test is COARSE_L(Ξ_{k0} x) = COARSE_L(Ξ_{k0} x_{k0}), which is equivalent by (C7).

## 2. Reduction: case (i) ⇐ CONJECTURE INTO (PROVED, L-SI succ. 8)
**CONJECTURE INTO.** At every post-rise state t with r_t > L, some gate (y, z) has z ∈ R̄_t.
**Reduction.** INTO implies that case (i) never occurs.
- Proof. Let k be a case (i) fallback. It is an in-phase S4c fallback with (h) at k and r_k > L ≥ 0, so THR with u* ≠ none.
- FBL (R20 (b), strong form) then says: no F → R̄ and no R → R̄ gate at k. So every gate at k has its target in F_k.
- k is a post-rise state with r_k > L, so this contradicts INTO. □
- This uses neither ENT-X nor (P). Compare R40: ENT-X excludes case (i) with M_k = L; INTO would also exclude M_k < L.
- DATA: INTO held at all 425 post-rise states with r > L in the library, 0 failures (logs/oldthreat_lib4.txt).
  - In 241 of them some gate into R̄ has level > L.
  - In the other 184, every gate has level ≤ L (§4, GATE-ABOVE).
  - The INTO gates are F → R̄ (absorptions) or R → R̄ (route improvements).
- Why it stalls (OPEN). An R → R̄ gate is a pure route comparison. Ξ(z) = π_z ⊕ θ against Ξ(σ y) = π_{σy} ⊕ θ, so it is W-improving
  exactly when it is Ξ-improving. An F → R̄ gate is always W-improving (R31 P-OPT reasoning).
  - So INTO says: after a rise, while r > L, Even always has a W-improving switch onto o's region.
  - The data shows absorption chains: each S4a step puts a new vertex into R̄, and its Even predecessor gains a gate into it
    (tevlast7_n32, s = 18-40; §4).
  - I found no argument that the chain cannot stop with r > L. Nothing above links "a vertex entered R̄ at t − 1" to "some Even
    predecessor gains".
- Case (ii) (r ≤ L before the next fallback): OPEN. Not attempted beyond the data (REFEREE-2: no fallback there either).

## 3. Dead conjectures (FALSE, each with the instance that kills it; also in docs/si/DEAD.md)
- RISE-DROP: "after a rise at j, r_{j+1} ≤ L whenever j+1 is still in scope". FALSE.
  - Instance: experiments/red/so/instances/tevlast7_n32.pg, sha1 d905038c651d7e49080ffd2fd9f7cde0744adb76 (L-RED).
  - S3 start, own trace: k0 = 11, L = 26, rise at j = 17. r = 30 at states 18-24 and r = 27 > L at states 25-40, all in-scope S4a.
  - Then EQ at state 41, and N5 stops. There is no fallback after the rise, so the target survives.
  - Library: 39 of 137 rises continue in scope with r_{j+1} > L. The rise level is < r_j in 29 of them.
- GATE-ABOVE: "at a post-rise state with r_t > L, M_t > L". FALSE.
  - Instance: experiments/red/so/instances/rise_thin51_n40.pg, sha1 47aaf46e4d068a95918978f840bf465658178fc3, S3 start, own trace:
    k0 = 72, L = 33, rise at j = 75, t = 76, r_76 = 38, M_76 = 32.
  - It is not a fallback: there are 8 gates of level 32, one R → R̄ and seven F → R̄.
  - Library: 184 of 425 states.
- FEED: "at a post-rise state with r_t > L, some gate runs from F_t into R̄_t". FALSE.
  - Instance: experiments/red/so/instances/tevlast11_n40.pg, sha1 8421ab3002beaab0b51191a20aad9f94b46e192b, S3 start, own trace:
    k0 = 5, L = 33, rise at j = 8, t = 22, r = 38. The only gate is (16, 23), level 36, R → R̄.
  - Library: 76 of 425 states.

## 4. Box-13 item (1) DATA (LV-NONE / SCOPE-FB from REFEREE-2's start pairs; Lead 15:59Z)
- Scripts: experiments/si/lv13/none_count.py and none_climb.py. Traces are REFEREE-2's (imported read-only). Scope runs as in
  R2-N5-ENT ent_check.py. Logs: experiments/si/lv13/logs/climb_130*.txt, best_130*.pg.
- On REFEREE-2's witnesses best_lv_9401-9404, from the S3 start (spec, own) and 5 random starts (own, rand, spec):
  - 71 scope runs, 362 in-scope fallbacks, 2 of them u* = none;
  - max 1 u* = none fallback per scope run (bound n·n_E + 1);
  - max 16 fallbacks per scope run; worst ratio 0.011 to 4·n·n_E + 3;
  - 0 failures of LV-NONE, SCOPE-FB, SAND.
  - On 9401 the u* = none fallback is the last transition of its scope run.
- 4 climbs × 25 min (fitness 1000·(max u* = none per scope run) + 10·(max fallbacks per scope run) + total u* = none):
  - climb 1301 (from 9401): 43,406 evaluations, 238,073 scope runs, 131,558 u* = none fallbacks, max 1 per scope run;
  - climbs 1302-1304 (from 9402-9404): 0 u* = none, max 17 fallbacks per scope run;
  - 0 failures of LV-NONE, SCOPE-FB or SAND in any evaluation.
- This agrees with REFEREE's R-N5-LV2 addendum (no scope run with ≥ 2). LV-NONE still rests on its proof.
- CONJECTURE NONE-LAST (DATA only): a THR fallback with r = −1 is the last transition of its scope run, so there is at most 1 per scope run.
  - none_count.py, re-run (17:1xZ) on 9401-9404 and the four climb bests: 117 scope runs, 4 u* = none fallbacks, in-scope transitions
    after the first one in its run = 0.
  - The climbs above ran before this counter existed and did not record it.
