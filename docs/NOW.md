# NOW (rewritten, never appended; max 150 lines)
Updated: 2026-10-14 by Lead. Phase: M0, M1, M2, M3 done; first attack lane L-STRUCT (weak separators) started 2026-10-14 18:54Z. Reporting: weekly checkpoint (D1, after M2).

## Milestones
| M | State | Evidence |
| --- | --- | --- |
| M0 Setup | done; TARGET v1.0 at a3777f1 (D2) | this commit; CI .github/workflows/verify.yml; backstop trigger in docs/agents/LEAD-BACKSTOP.md |
| M1 Reproduce hard families | DONE 2026-10-14 19:10Z (l-comp de7ea19): 12 of 13 families blow up as published, all strategies checked; counter_qpt superpolynomial but class open (targets a quasi-poly algorithm). Friedmann SI via REFEREE-checked PGSolver ports (reading L5). Bench LANDED on trunk (REFEREE OK ae532f6) | experiments/hard-families/README.md (l-comp) |
| M2 Audit arXiv 2511.03752 | DONE 2026-10-14 ~18:35Z: BROKEN (two independent 4-vertex counterexamples, cross-checked); RESULTS DE1 | docs/decisions/M2-arxiv-2511.03752.md |
| M3 Partial results | DONE 2026-10-15 00:17Z (novelty T10 NEW; caveat: HKP LNCS 9560 chapter unopened): RESULTS R2 T-A1 [refereed-only] (psolB solves G completely iff PA**(G)); two referee signatures at l-attr 57a1515, CHECKER PASS 62cf1c4. Also R1 L4 (lemma) | docs/RESULTS.md |
| M4 Target | not started | - |

## Roster (model, effort, one-line reason; revisit at each restart)
Lead session: session_014FBi6o334DvwT5Uw2kDfoN, environment env_013N6DGgsLr96BMjKj1hpw9i, branch claude/vibrant-johnson-nxvvxo.
Effort note: create_session exposes no effort knob; every session inherits effort "high" (verified per session with get_session).
Prices per Mtok in/out (platform docs, 2026-10-14): fable-5-1 $10/$50, opus-5-5 $4/$20, sonnet-5-5 $2/$10, haiku-5-5 $0.10/$0.50.

| Role | Session id | Branch | Model | Effort | State | Reason |
| --- | --- | --- | --- | --- | --- | --- |
| Lead | session_014FBi6o334DvwT5Uw2kDfoN | claude/vibrant-johnson-nxvvxo | opus-5-5 | high | working | Owner-chosen session; routing judgement; keeps context lean |
| REFEREE (old) | session_01Ki9osXiyYf9heTLNk3FKED | claude/referee | fable-5-1 | high | parked (handover f179ae0); keep 1 week |
| REFEREE | session_01R4yR8XskSK3ta94ewnN4cM | claude/referee | fable-5-1 | high | working (R-L1b: L1 v2 + Lemma 2.1' + Theorem B) | Successor; never downgrade the referee | Most capable model; finding the error in a claimed proof decides M2 and every claim after |
| L-LIT | session_01MxWPJxeciDocEdfd89xCF8 | claude/l-lit | opus-5-5 | high | parked (T10 done 1f9e9f8) | Source checking and barrier analysis need judgement; Fable reserved for referee; move to Fable when step-3 sign-offs start |
| L-COMP | session_014bbtNwaVKxFymHpXynjURn | claude/l-comp | opus-5-5 | high | working (SAT hard cells for L-STRUCT, 6h box; ~380k ctx) | SAT engineering needs care; successor near 600k | Paper-to-code fidelity for M1 generators and the M2 implementation; drop to sonnet-5-5 for routine benchmarks after M2 |
| L-STRUCT | session_01VH4fd2Fq8XeXtyUfkwLJV1 | claude/l-struct | fable-5-1 | high | parked (handover 729c965; wake on n=5 diagonal gap, new T3 idea, or L4 second referee) | Attack lane (owner: most capable model at high effort); rank 1 approach, weak separators, T4 verdict OPEN |
| L-ATTR | session_01XDM3HXeuG3mqhQK92eNaru | claude/l-attr | fable-5-1 | high | parked (T-A1 final 57a1515, signed) | Attack lane, rank 3 per L-LIT T7 recommendation (M2 counterexample in hand); cheap, near-certain result |
| L-LOWER | session_01U5n8mgXxgyGzvuUzxHbiKx | claude/l-lower | fable-5-1 | high | working (L1, 24h box to 2026-10-15 23:00Z) | Attack lane, rank 2 (non-adaptive SLP lower bounds), T7-1' first target |
| REFEREE-2 | session_01C2sxysc8CzJQrNBhp1rKMs | claude/referee-2 | fable-5-1 | high | idle (L4 d76c9e1, T-A1 2eb1a2d signed; P2 caught) | Independent second referee required for double-refereed results; never downgraded |
| CHECKER | session_01JptdoF6eLabJzBHG28nWSS | claude/checker | opus-5-5 | high | parked (C1 + recheck: R1, R2 PASS 62cf1c4) | Landing gate: mechanical re-runs and statement diffs; Opus suffices |
| HUMAN-DESK | session_01URpUgDVczmLPHmidyo4Jr6 | claude/human-desk | opus-5-5 | high | parked (packet 3b3bdde; owner decides distribution) | Owner D1: spawned when a claim reaches M3; writing quality matters, no deep math |
| WATCHDOG | session_01JQNTX8zT3T3mWMt6ZmYzkn | none (never edits) | haiku-5-5 | high | working (cron :30, trig_019xE43BZ5qaDGwxDkZ5h5ik) | Routine liveness/overage checks; reports to Lead only (deviation from playbook: does not wake lanes, so idle sessions never get messages) |

## In flight
- L-COMP: parked after notebook handover; wakes for a new claim, review changes, or L-STRUCT SAT engineering.
- L-LIT: parked; T1-T4 on trunk (docs/lit/). T4: weak separators OPEN (Czerwinski et al. 1807.10546 §6).
- L-STRUCT: T3 sub-lemma SL8-min: every MINIMAL weak (n,d)-sep, d<=n+1, is within 2 transition changes of a strong one on the same states (exhaustive data 6985a5a: E t<=1, V t<=2 at minimum; non-minimal needs up to 4). Proof attempt OBSTRUCTED at Lemma C (l-struct 283ebbc; Lemma A false as stated, C target rule false on data, minimality step unformulated). Now (a): extract target rule from 64 rewires, 2h box to ~23:55Z; else (b) structural hypothesis. L4 signed by first referee (9bf5301); second referee pending with T3 package. w^V(4,5)=10=s^V(4,5) (b9f4d78, SAT+checker; LRAT confirmation queued for L-COMP successor). T3 holds on all 8 computed cells with d<=n+1.
- REFEREE: parked after handover (f179ae0). L4 signed as first referee (9bf5301). Next: fresh REFEREE for SL8-min/T3; separate REFEREE-2 for the L4+T3 package. Second independent referee to be spawned for the T3+L4 package (GAPS G1).
- L-COMP: diagonal V cells (4,5),(5,5),(5,6), TARGET n=4 strong, n=5; LRAT standard. Box ends ~01:30Z.
- WATCHDOG: hourly at :30.

## Findings to carry
- C1 (REFEREE-checked, a data point, not M3): w(2,6)=3 < 4=s(2,6) in E, S, V; w^V(3,6)=6 < 7=s^V(3,6). Weak separators can be strictly smaller than strong ones.
- Landscape doc corrections (L-LIT, docs/lit/BARRIERS.md): d = O(log n) poly result is Jurdzinski-Lazic Thm 7 / Fearnley et al., not Calude et al.; upper-bound exponent is Jurdzinski-Lazic's; attractor-decomposition barrier is formally only Arnold-Niwinski-Parys Thm 5.1; Two Counters bound partly empirical; Random-Facet parity lower bound withdrawn (arXiv 1410.7871).
- Oink mspm at 8fbf0a7 is wrong on some games (crash at mspm.cpp:486; one answer rejected by Oink's verifier); excluded from agreement claims. Instances: experiments/harness/regressions/ (l-comp).
- PGSolver SI families (switchallexp, switchbestexp) target PGSolver's switch-all/switch-best SI, not Oink psi/ssi; port of stratimpralgs.ml queued in L-COMP.

## Live approaches
- A2 attractor/partial solvers (L-ATTR): M3 CANDIDATE T-A1 (l-attr d5d6396): psolB solves G completely iff PA**(G); PA** => psolQ solves; HKP Thm 7/8/Lemma 5 as corollaries; data: all n=3, n=4 samples + 27.3M enumeration. REFEREE-2: OK in substance, CHANGES F1-F7 (58b5c72); BOTH referees: theorem HOLDS (REFEREE 8ee2d08, REFEREE-2 58b5c72); final wording fixes (F1 hypothesis, Thm 4 dependency) with L-ATTR; then both sign one commit -> M3. Reading L9.
- A3 non-adaptive SLP lower bounds (L-LOWER): statement v2 l-lower b1abae0 (REFEREE re-check R-L1b). Data: B_1(n) = 2n-2 for n <= 4 (exact SAT); Lemma 2.1' B_1 >= 2n-2 and Theorem B (depth-(2n-1) bisimulation type decides one-player Büchi; depth arguments capped at Theta(n)), both unrefereed. n=5 k=8 decides direction: =8 -> try uniform O(n) program (refutes T-L1); >8 -> first super-linear step.
- A1 deterministic weak separators (L-STRUCT, PARKED 22:00Z): outside the strong-separator barrier (T4). Products: DE2 (T1 refuted), L4 (first referee OK), T3 data conjecture (w=s for d<=n+1, all cells to (4,5) V). Algorithmic quantity is the diagonal w^V(n,n) (REFEREE d96b686). Diagonal W=S=1,2,5,7 for n<=4 confirmed by three independent encodings (L-STRUCT, L-COMP LRAT, REFEREE b4a711c); TARGET alphabet n=2,3,4 also w=s; gaps only at d >> n. S3 to be framed as 'w=s on the TARGET alphabet' (barrier direction). Data: w=s on most small cells; w<s at (2,6),(2,10),V(3,6); s(2,2h)=h+1 but w(2,8)=w(2,10)=4. Lower-bound target T1 likely false; now measuring growth of w in d.

## Dead approaches (with obstruction): see docs/RESULTS.md "Dead ends"
- DE1 arXiv 2511.03752 (BROKEN, 4-vertex counterexamples). DE2 T1 weak-separator lower bound (refuted at (2,10)).

## Best result so far
- M3: RESULTS R2 [refereed-only] T-A1, psolB solves G completely iff PA**(G) (L-ATTR; both referees signed 57a1515).
- RESULTS R1 [refereed-only]: L4, s^V(n,n) >= n^Omega(lg n) (supporting lemma, not M3 per L7).
- None of the fleet's own. Known: quasi-polynomial upper bound (to be source-checked by L-LIT).

## Owner questions open
- Q5: library/Springer access to HKP, LNCS 9560 (2016) pp. 159-177, needed before any external novelty claim for T-A1.
- Q6: whether and to whom docs/HUMAN-REVIEW.md goes (owner only).
- Q7: second-referee/L4 as M3? (Lead reading L7: lemma only.)
- Q4: L-COMP built PGSolver (tcsprojects/pgsolver d3cd624) but the session's permission classifier refused to run the binaries; generators were ported to Python instead. Owner: allow running them (to diff the port against the original), or keep port + referee check?
- Q2: trunk branch: keep claude/vibrant-johnson-nxvvxo as trunk, or create `main`?
- Q3: environment setup script (Boost dev packages + scripts/setup_oink.sh) to save each session ~1 min of setup.

## Spend
- Spend: 21:43Z total $135.69 (Lead 22.79, REFEREE-old 47.61, L-COMP 31.82, L-STRUCT 33.42, WATCHDOG 0.06). 23:43Z: Lead 35.26, L-COMP 32.80, REFEREE-2 8.58; Fable sessions L-ATTR/L-LOWER/REFEREE report no cost field yet.
