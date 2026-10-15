# NOW (rewritten, never appended; max 150 lines)
Updated: 2026-10-14 by Lead. Phase: M0, M1, M2, M3 done; first attack lane L-STRUCT (weak separators) started 2026-10-14 18:54Z. Reporting: weekly checkpoint (D1, after M2).

## Milestones
| M | State | Evidence |
| --- | --- | --- |
| M0 Setup | done; TARGET v1.0 at a3777f1 (D2) | this commit; CI .github/workflows/verify.yml; backstop trigger in docs/agents/LEAD-BACKSTOP.md |
| M1 Reproduce hard families | DONE 2026-10-14 19:10Z (l-comp de7ea19): 12 of 13 families blow up as published, all strategies checked; counter_qpt superpolynomial but class open (targets a quasi-poly algorithm). Friedmann SI via REFEREE-checked PGSolver ports (reading L5). Bench LANDED on trunk (REFEREE OK ae532f6) | experiments/hard-families/README.md (l-comp) |
| M2 Audit arXiv 2511.03752 | DONE 2026-10-14 ~18:35Z: BROKEN (two independent 4-vertex counterexamples, cross-checked); RESULTS DE1 | docs/decisions/M2-arxiv-2511.03752.md |
| M3 Partial results | DONE 2026-10-15 00:17Z (novelty T10 NEW, rechecked T11 against the chapter text DTR15-4: still NEW): RESULTS R2 T-A1 [refereed-only] (psolB solves G completely iff PA**(G)); two referee signatures at l-attr 57a1515, CHECKER PASS 62cf1c4. Also R1 L4 (lemma) | docs/RESULTS.md |
| M4 Target | not started | - |

## Roster (model, effort, one-line reason; revisit at each restart)
Lead session: session_014FBi6o334DvwT5Uw2kDfoN, environment env_013N6DGgsLr96BMjKj1hpw9i, branch claude/vibrant-johnson-nxvvxo.
Effort note: create_session exposes no effort knob; every session inherits effort "high" (verified per session with get_session).
Prices per Mtok in/out (platform docs, 2026-10-14): fable-5-1 $10/$50, opus-5-5 $4/$20, sonnet-5-5 $2/$10, haiku-5-5 $0.10/$0.50.

| Role | Session id | Branch | Model | Effort | State | Reason |
| --- | --- | --- | --- | --- | --- | --- |
| Lead | session_014FBi6o334DvwT5Uw2kDfoN | claude/vibrant-johnson-nxvvxo | opus-5-5 | high | working | Owner-chosen session; routing judgement; keeps context lean |
| REFEREE (old) | session_01Ki9osXiyYf9heTLNk3FKED | claude/referee | fable-5-1 | high | parked (handover f179ae0); keep 1 week |
| REFEREE | session_01R4yR8XskSK3ta94ewnN4cM | claude/referee | fable-5-1 | high | idle (R-psolC FAITHFUL 1600917) | Never downgrade the referee; most capable model |
| L-LIT | session_01MxWPJxeciDocEdfd89xCF8 | claude/l-lit | opus-5-5 | high | parked (T12 done 706d5e1) | Source checking and barrier analysis need judgement; Fable reserved for referee |
| L-COMP | session_014bbtNwaVKxFymHpXynjURn | claude/l-comp | opus-5-5 | high | parked (handover 25a6e21; successor only when T3 revives or a new claim needs the bench) | n=5 diagonal cells cost 1-2 h/k; low value while T3 is parked |
| L-STRUCT | session_01VH4fd2Fq8XeXtyUfkwLJV1 | claude/l-struct | fable-5-1 | high | parked (handover 729c965; wake on n=5 diagonal gap, new T3 idea, or L4 second referee) | Attack lane (owner: most capable model at high effort); rank 1 approach, weak separators, T4 verdict OPEN |
| L-ATTR | session_01XDM3HXeuG3mqhQK92eNaru | claude/l-attr | fable-5-1 | high | parked (A3-psolC done 02174e2) | Attack lane, rank 3 |
| L-LOWER (old) | session_01U5n8mgXxgyGzvuUzxHbiKx | claude/l-lower | fable-5-1 | high | parked (handover f0e5e8f) | Replaced for cost (492k context) |
| L-LOWER | session_0153E4mCB2wqi65xdfpxozfK | claude/l-lower | fable-5-1 | high | working (T-L2 theory box, go 08:36Z, to 20:36Z) | Attack lane, rank 2; theory needs the most capable model (D1) |
| L-ALG | session_01WN44zjFXZSqaL5SwsoDn7d | claude/l-alg | fable-5-1 | high | working (design loop C1.., 12h box from ~10:00Z) | D5/L18: M4 primary aim; attack lane, most capable model (D1) |
| L-SI | session_01HnGDSEHG3NHszV1y8ND6BF | claude/l-si | fable-5-1 | high | working (SI rule design loop, 12h box from ~10:10Z) | D6/L19: second algorithm lane, RANKING rank 4; attack lane, most capable model (D1) |
| REFEREE-2 | session_01C2sxysc8CzJQrNBhp1rKMs | claude/referee-2 | fable-5-1 | high | idle (L4 d76c9e1, T-A1 2eb1a2d signed; P2 caught) | Independent second referee required for double-refereed results; never downgraded |
| CHECKER | session_01JptdoF6eLabJzBHG28nWSS | claude/checker | opus-5-5 | high | parked (C1 + recheck: R1, R2 PASS 62cf1c4) | Landing gate: mechanical re-runs and statement diffs; Opus suffices |
| HUMAN-DESK | session_01URpUgDVczmLPHmidyo4Jr6 | claude/human-desk | opus-5-5 | high | parked (packet 3b3bdde; owner decides distribution) | Owner D1: spawned when a claim reaches M3; writing quality matters, no deep math |
| WATCHDOG | session_01JQNTX8zT3T3mWMt6ZmYzkn | none (never edits) | haiku-5-5 | high | working (cron :30, trig_019xE43BZ5qaDGwxDkZ5h5ik) | Routine liveness/overage checks; reports to Lead only (deviation from playbook: does not wake lanes, so idle sessions never get messages) |
| OWNER-DESK | session_01Eq99qsTJBiTh6xLzwCPtqv | claude/owner-desk | opus-5-5 | high | starting | Owner D3: owner Q&A and open questions; accuracy in plain explanation, no proofs; idle between owner messages |

## In flight (as of 2026-10-15 09:50Z)
- L-SI: strategy-improvement rule design loop toward M4/M4-R (D6, L19), 12h box from ~10:10Z. Candidate S2a MSF (most-significant-first single switch) NOT KILLED so far (l-si c73f69e): linear on all 15 families incl. switchallexp, zadehexp, Random-Facet*, DLMM Bland; adversarial n<=9 maxima ~n^2.5-3. Unrefereed data, far from a claim. L-LIT T12 (706d5e1): no published lower bound covers MSF; killer must be two-player with mixed-owner cycles; candidate D_n-with-Odd-gates sent to L-SI.
- Working-session count (D1 cap 5 counts lanes, not Lead/WATCHDOG): L-ALG, L-SI, L-LOWER = 3.
- L-ALG: falsification-driven algorithm design loop toward M4 (D5, L18), 12h box from ~10:00Z.
- L-LOWER (successor): T-L2 theory box to 20:36Z: human proof of B_2(4) >= 7 from the 100-game UNSAT core; test for a gap growing with n.
- Everyone else parked or idle: L-ATTR (psolC done, DE3), REFEREE (R-psolC done), REFEREE-2, L-LIT (T11 done), L-STRUCT, L-COMP,
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
- RESULTS R1 [refereed-only]: L4, s^V(n,n) >= n^Omega(lg n) (supporting lemma, not M3 per L7).
- None of the fleet's own. Known: quasi-polynomial upper bound (to be source-checked by L-LIT).

## Owner questions open (held by OWNER-DESK since 2026-10-15, D3; docs/owner-desk/QUESTIONS.md)
- Q3: DONE by owner 07:53Z (setup script set; applies to sessions started after it; verify on the next new session). Q2, Q4, Q5, Q6, Q7 closed (D4, L13-L17). No owner questions open.

## Spend
- Spend: 21:43Z total $135.69 (Lead 22.79, REFEREE-old 47.61, L-COMP 31.82, L-STRUCT 33.42, WATCHDOG 0.06). 23:43Z: Lead 35.26, L-COMP 32.80, REFEREE-2 8.58; Fable sessions L-ATTR/L-LOWER/REFEREE report no cost field yet.
