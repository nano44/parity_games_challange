# NOW (rewritten, never appended; max 150 lines)
Updated: 2026-10-14 by Lead. Phase: M0, M1, M2, M3 done; first attack lane L-STRUCT (weak separators) started 2026-10-14 18:54Z. Reporting: weekly checkpoint (D1, after M2).

## Milestones
| M | State | Evidence |
| --- | --- | --- |
| M0 Setup | done; TARGET v1.0 at a3777f1 (D2) | this commit; CI .github/workflows/verify.yml; backstop trigger in docs/agents/LEAD-BACKSTOP.md |
| M1 Reproduce hard families | DONE 2026-10-14 19:10Z (l-comp de7ea19): 12 of 13 families blow up as published, all strategies checked; counter_qpt superpolynomial but class open (targets a quasi-poly algorithm). Friedmann SI via REFEREE-checked PGSolver ports (reading L5). Bench LANDED on trunk (REFEREE OK ae532f6) | experiments/hard-families/README.md (l-comp) |
| M2 Audit arXiv 2511.03752 | DONE 2026-10-14 ~18:35Z: BROKEN (two independent 4-vertex counterexamples, cross-checked); RESULTS DE1 | docs/decisions/M2-arxiv-2511.03752.md |
| M3 Partial results | DONE 2026-10-15 00:17Z (novelty T10 NEW, rechecked T11 against the chapter text DTR15-4: still NEW): RESULTS R2 T-A1 [refereed-only] (psolB solves G completely iff PA**(G)); two referee signatures at l-attr 57a1515, CHECKER PASS 62cf1c4. Also R1 L4 (lemma). 2026-10-15 13:50Z: RESULTS R3 [refereed-only] original Random-Facet needs e^Omega(sqrt n) expected switches on parity games (FHZ Thm 6.3 + L-RED transfer lemma; REFEREE + REFEREE-2 signed at l-red 49ae306; CHECKER PASS 068f9de; T13 NEW as statement) | docs/RESULTS.md |
| M4 Target | not started | - |

## Roster (model, effort, one-line reason; revisit at each restart)
Lead session: session_014FBi6o334DvwT5Uw2kDfoN, environment env_013N6DGgsLr96BMjKj1hpw9i, branch claude/vibrant-johnson-nxvvxo.
Effort note: create_session exposes no effort knob; every session inherits effort "high" (verified per session with get_session).
Prices per Mtok in/out (platform docs, 2026-10-14): fable-5-1 $10/$50, opus-5-5 $4/$20, sonnet-5-5 $2/$10, haiku-5-5 $0.10/$0.50.

| Role | Session id | Branch | Model | Effort | State | Reason |
| --- | --- | --- | --- | --- | --- | --- |
| Lead | session_014FBi6o334DvwT5Uw2kDfoN | claude/vibrant-johnson-nxvvxo | opus-5-5 | high | working | Owner-chosen session; routing judgement; keeps context lean |
| REFEREE (old) | session_01Ki9osXiyYf9heTLNk3FKED | claude/referee | fable-5-1 | high | parked (handover f179ae0); keep 1 week |
| REFEREE | session_01R4yR8XskSK3ta94ewnN4cM | claude/referee | fable-5-1 | high | idle (R3 signed 42f11c6/5ed56c5) | Never downgrade the referee; most capable model |
| L-LIT | session_01MxWPJxeciDocEdfd89xCF8 | claude/l-lit | opus-5-5 | high | working (T16: DTL gauntlet step 3 barrier check + GandALF 'VULNERABLE' source, 2h from 15:35Z; T15 done e895ddd) | Source checking and barrier analysis need judgement |
| L-COMP | session_014bbtNwaVKxFymHpXynjURn | claude/l-comp | opus-5-5 | high | parked (handover 25a6e21; successor only when T3 revives or a new claim needs the bench) | n=5 diagonal cells cost 1-2 h/k; low value while T3 is parked |
| L-STRUCT | session_01VH4fd2Fq8XeXtyUfkwLJV1 | claude/l-struct | fable-5-1 | high | parked (handover 729c965; wake on n=5 diagonal gap, new T3 idea, or L4 second referee) | Attack lane (owner: most capable model at high effort); rank 1 approach, weak separators, T4 verdict OPEN |
| L-ATTR | session_01XDM3HXeuG3mqhQK92eNaru | claude/l-attr | fable-5-1 | high | parked (A3-psolC done 02174e2) | Attack lane, rank 3 |
| L-LOWER (old) | session_01U5n8mgXxgyGzvuUzxHbiKx | claude/l-lower | fable-5-1 | high | parked (handover f0e5e8f) | Replaced for cost (492k context) |
| L-LOWER | session_0153E4mCB2wqi65xdfpxozfK | claude/l-lower | fable-5-1 | high | working (T-L2 theory box, go 08:36Z, to 20:36Z) | Attack lane, rank 2; theory needs the most capable model (D1) |
| L-ALG | session_01WN44zjFXZSqaL5SwsoDn7d | claude/l-alg | fable-5-1 | high | handing over (LANE-RESTART step 1 requested 15:35Z; successor writes the DTL polynomial-bound proof attempt) | D5/L18 algorithm lane |
| L-SI | session_01HnGDSEHG3NHszV1y8ND6BF | claude/l-si | fable-5-1 | high | working (SI rule design loop, 12h box from ~10:10Z) | D6/L19: second algorithm lane, RANKING rank 4; attack lane, most capable model (D1) |
| L-RED | session_017WLo5xfMxRZ4f6n2Su6274 | claude/l-red | fable-5-1 | high | working (DTL: R8 HELD b72707e, Lemma M; continues on the killer requirement to ~21:06Z) | Designer and falsifier must differ (D1); referees kept clean for step 4 |
| REFEREE-2 | session_01C2sxysc8CzJQrNBhp1rKMs | claude/referee-2 | fable-5-1 | high | idle (R3 signed 94dde7b; context 495k) | Independent second referee; never downgraded |
| CHECKER | session_01JptdoF6eLabJzBHG28nWSS | claude/checker | opus-5-5 | high | parked (C2 PASS 068f9de, R3 landed) | Landing gate: mechanical re-runs and statement diffs; Opus suffices |
| HUMAN-DESK | session_01URpUgDVczmLPHmidyo4Jr6 | claude/human-desk | opus-5-5 | high | parked (packet 3b3bdde; owner decides distribution) | Owner D1: spawned when a claim reaches M3; writing quality matters, no deep math |
| WATCHDOG | session_01JQNTX8zT3T3mWMt6ZmYzkn | none (never edits) | haiku-5-5 | high | working (cron :30, trig_019xE43BZ5qaDGwxDkZ5h5ik) | Routine liveness/overage checks; reports to Lead only (deviation from playbook: does not wake lanes, so idle sessions never get messages) |
| OWNER-DESK | session_01Eq99qsTJBiTh6xLzwCPtqv | claude/owner-desk | opus-5-5 | high | idle between owner messages | Owner D3: owner Q&A and open questions; accuracy in plain explanation, no proofs; idle between owner messages |

## In flight (as of 2026-10-15 14:58Z)
- L-SI: strategy-improvement rule design loop toward M4/M4-R (D6, L19), box to ~22:10Z. Dead: S2a MSF (DE4), S1 RAR (DE6), S2b, S3, S4. S5/S6 'not covered, not defended'; HELD again by L-RED R6 (f5e6ea0) on the FHZ counter with adversarial numbering (index-fair rules switch the next higher bit promptly); L-RED R7 (b560aa8): S5 HELD: published Zadeh lower-bound runs have cyclic tie constraints, so no fixed order reproduces them; fixed-tie-break Zadeh: L-LIT T15 (e895ddd) verdict OPEN, no published lower bound outside abstract AUSOs (closest Thomas 1706.09380 Thm 8; DFH tie-break is strategy-dependent); Thomas §5 is a candidate template for L-RED later. S6 parked. L-RED now attacking DTL. LIVE: S7 most-improved (single switch maximising #vertices whose valuation strictly improves): linear/low-degree on all families incl. gated ones (gated_switchbestexp 80,203,314,658,974 for N=2..6); L-RED R3 (l-red 7edf1c8) HELD: faithful; unrefereed Lemmas T/D (count = traffic; upstream count > downstream) defeat padding; Friedmann G_n with pads degenerates after 2 increments (selector chain ordered wrong for S7). S7 KILLED (RESULTS DE7, l-red bf0922f): FHZ one-player RF counter P_{n,1,1,1} + linear pads, Theta(n^2) size, S7 iterations 16,44,104,228,480,988 (doubling); Earlier: S7 KEY QUESTION DF (L-RED R3 §3c adbfb40, unrefereed): every S7 switch is downstream-first; every published exponential single-switch run is not; so S7 is polynomial (sink games) iff every downstream-first run has poly length. L-RED: construct (6h); L-SI: prove. S7 gauntlet: step 2 data + proof attempt (L-SI), step 3 barrier check DONE (L-LIT T14 8dd2e55: NOT COVERED; outside B1-B17 with B9 caveat on index last-resort firings), kill box 3 (L-RED). S5/S6 HELD by L-RED R4 (0203590): no published bad order is a block order; numbering lifts counts (Cunningham 6->24 at N=3) but class-structured schemes stay linear.
- Working-session count (D1 cap 5 counts lanes, not Lead/WATCHDOG): L-SI, L-LOWER, L-RED, L-LIT = 4; L-ALG successor makes 5 (L-ALG old session parks on handover).
- MSF status 11:25Z: S3 DEAD (DLMM M_L port, 2^(L+1)); MSF 3L-2 there. L-SI unrefereed bound: MSF iterations <= (n^2+1)(n^2+X+1), X = escaped cycle-creating switches (max X 2..14 for n=5..10). L-SI argues Disser-Mosis D_n cannot port to lexicographic valuations. L-RED attacks all of it independently. 11:45Z L-RED FLAW: Claim F's 'cycle-creating' bit test is wrong (misses less-relevant cycle vertices; cf1/cf2 counterexamples; 2,649/11,795 switches misclassified); corrected play-notion F' holds on data; all measured X are undercounts; msfa/msfc mis-implemented. MSF not killed. 12:12Z L-SI fixed both (play notion incl. final cycle), F' 0 violations on 16k games; but cycle-creating switches are ~1/3 of all MSF switches, so the X-bound is empty until X is bounded: no proof route yet, MSF stands on data only.
- L-ALG: box to 21:55Z. Own designs C1-C4 dead (DE5 + C4 on tc). C5 = Oink's DTL (van Dijk research variant; exact pseudocode docs/alg/candidates/C5-DTL.md, l-alg 898d02d): correct with verified strategies on all tests; tangles linear/near-linear on every family (tc 2N+1 to n=4,068). Provenance: van Dijk GandALF 2019 slides call path-based variants 'VULNERABLE! (to a different version of the TC game)'. L-ALG DTL attack (473c7c8): every tc/tc+ variant polynomial for DTL (tc 2N+1, tc+ ~1.4N^2, best GA ~N^2.5); killer must make surviving best vertices cycle exponentially; next angle search_rec on Z. L-RED R8 (b72707e): HELD; Lemma M (unrefereed): DTL has no reset, the only non-monotone event is theft of a tangle vertex by a higher region (once per vertex per level), so a killer needs renewable thefts; strongest found family is a one-player chain, O(n^2) tangles; completeness probes clean. DTL GAUNTLET (15:35Z): step 1 done (C5-DTL + Oink); step 2 partial (L-ALG 67,000+ games, verified strategies; formal 10,000-game run + L-COMP strategy check pending); step 3 L-LIT T16 running; step 4 proof attempt by L-ALG successor (commissioning); L-RED keeps attacking independently. Treated as wrong until it passes. Bench note: tc+ beats PTL/SPPTL.
- L-LOWER (successor): T-L2 theory box to 20:36Z: human proof of B_2(4) >= 7 from the 100-game UNSAT core; test for a gap growing with n.
- Everyone else parked or idle: L-ATTR (psolC done, DE3), REFEREE (R-psolC done), REFEREE-2, L-LIT (T15 done), L-STRUCT, L-COMP,
  CHECKER, HUMAN-DESK. OWNER-DESK idle between owner messages. WATCHDOG hourly at :30.

## Findings to carry
- C1 (REFEREE-checked, a data point, not M3): w(2,6)=3 < 4=s(2,6) in E, S, V; w^V(3,6)=6 < 7=s^V(3,6). Weak separators can be strictly smaller than strong ones.
- Landscape doc corrections (L-LIT, docs/lit/BARRIERS.md): d = O(log n) poly result is Jurdzinski-Lazic Thm 7 / Fearnley et al., not Calude et al.; upper-bound exponent is Jurdzinski-Lazic's; attractor-decomposition barrier is formally only Arnold-Niwinski-Parys Thm 5.1; Two Counters bound partly empirical; Random-Facet parity lower bound withdrawn (arXiv 1410.7871).
- Oink mspm at 8fbf0a7 is wrong on some games (crash at mspm.cpp:486; one answer rejected by Oink's verifier); excluded from agreement claims. Instances: experiments/harness/regressions/ (l-comp).
- PGSolver SI families (switchallexp, switchbestexp) target PGSolver's switch-all/switch-best SI, not Oink psi/ssi; port of stratimpralgs.ml queued in L-COMP.

## Live approaches
- A2 attractor/partial solvers (L-ATTR, PARKED): T-A1 is M3 (RESULTS R2). psolC (HKP DTR15-4) measured (l-attr 02174e2): complete on all n<=3, partial on 1,380 of 27.3M n=4 games; solves 9/13 M1 families completely (incl. the 3 that defeat Zielonka and both Friedmann SI families), 0% on tc/tc+/counter_symsi/counter_rr. Smallest failure n=4 m=6 (psolc_min_n4_m6.pg): weak-parity prefix-minimum trap. Not an M4 route: DE3 (REFEREE R-psolC FAITHFUL, referee 1600917).
- A3 non-adaptive SLP lower bounds (L-LOWER): B_1(1..5) = 0,2,4,6,8 = 2n-2 (90f6928); B_2(1..4) = 0,2,4,7 (d00349a; n=4: UNSAT k=6 on a 400-game core, 7-gate witness checked on all 12.96M games; min depth 6, so cost > depth). Data only, unrefereed. T-L1 parked (data against). CDHL SODA'18 says nothing on games; adaptive two-player Büchi is Omega(n)..O(n^2) (CSL'17 Lemma 27). Next: T-L2 theory box 12h (successor): human proof of B_2(4) >= 7 from the core; does the argument grow with n? Kill criterion in notebook.
- A1 deterministic weak separators (L-STRUCT, PARKED 22:00Z): outside the strong-separator barrier (T4). Products: DE2 (T1 refuted), L4 (first referee OK), T3 data conjecture (w=s for d<=n+1, all cells to (4,5) V). Algorithmic quantity is the diagonal w^V(n,n) (REFEREE d96b686). Diagonal W=S=1,2,5,7 for n<=4 confirmed by three independent encodings (L-STRUCT, L-COMP LRAT, REFEREE b4a711c); TARGET alphabet n=2,3,4 also w=s; gaps only at d >> n. S3 to be framed as 'w=s on the TARGET alphabet' (barrier direction). Data: w=s on most small cells; w<s at (2,6),(2,10),V(3,6); s(2,2h)=h+1 but w(2,8)=w(2,10)=4. Lower-bound target T1 likely false; now measuring growth of w in d.

## Dead approaches (with obstruction): see docs/RESULTS.md "Dead ends"
- DE1 arXiv 2511.03752 (BROKEN, 4-vertex counterexamples). DE2 T1 weak-separator lower bound (refuted at (2,10)).

## Best result so far
- M3: RESULTS R2 [refereed-only] T-A1, psolB solves G completely iff PA**(G) (L-ATTR; both referees signed 57a1515).
- M3-type: RESULTS R3 [refereed-only] original Random-Facet on parity games, e^Omega(sqrt n) expected switches (L-RED; CHECKER 068f9de).
- RESULTS R1 [refereed-only]: L4, s^V(n,n) >= n^Omega(lg n) (supporting lemma, not M3 per L7).
- Algorithmic: no polynomial algorithm (M4) yet. Best results are R2 (T-A1) and R3 (Random-Facet lower bound). Known: quasi-polynomial upper bounds.

## Owner questions open
- Q3: DONE by owner 07:53Z (setup script set; applies to sessions started after it; verify on the next new session). Q2, Q4, Q5, Q6, Q7 closed (D4, L13-L17). No owner questions open.

## Spend
- 14:55Z last readings (cost_usd): Lead 86.2, L-LIT 93.5, L-RED 66.8, L-SI 58.6, REFEREE 55.0, L-ALG 53.6, REFEREE-2 39.6,
  L-LOWER (succ.) 30.1; earlier/parked: L-LOWER (old) 56.8, REFEREE (old) 47.6, L-COMP 38.1, L-STRUCT 33.4, L-ATTR ~31, WATCHDOG 1.3.
  Sum of readings about $692 (CHECKER, HUMAN-DESK, OWNER-DESK not read). Rate limit: seven_day "allowed_warning" since 12:02Z,
  no overage; resets 2026-10-21 21:00Z; owner D7: continue, stop on overage.
