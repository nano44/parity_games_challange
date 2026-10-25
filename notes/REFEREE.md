# REFEREE notebook
Overwrite the top sections; append to "Sources opened" and "Dead ends".

## Resume point (successor 10), written 2026-10-25T17:41Z by date -u (Opus 5.5, D15; session_01J4kmfDqtZdanh3RSCxChyD)
- Handover check 7c984663/b5887e61: Lead 5/5, GO (16:49Z Lead stamp).
- P-N5-RHO (pin c814455, sha1 cd5df65c…): docs/referee/R-N5-RHO.md: all SIGNED (HN-POLY conditional on PFZ-ext BRK-POLY′ (i′), (ii)),
  no gaps; notes RHO-N1 (o = c_θ with |U| ≥ 2, 89 phases), RHO-N2 (τ(o) = o line: cite R34 (e) + HN = H1, case B too), RHO-N3 (data).
  Tools scratch/rho_probe.py, rho_climb.py (tail / ffb); logs scratch/rho_logs/. Thin: RHO-TAIL change past freeze, |U| ≥ 4 past
  freeze, FREEZE-F (b) (vacuous in lib and 5.95M ffb candidates).
- DONE: PFZ-ext §C-ext vs R2 78896bfc (PFZ-1 = G-PFX-1; repair proves (i) as stated; joint form (i′) + 2n − 2 until R2 signs repair);
  LV2 §C vs R2 a551debf (identical; beta2_n11 N = 2 none fallbacks, refutes R2's candidate conjecture). Commit ed8bc207.
- DONE: P-N5-NHN (trunk 0bb175d, sha1 da7d09ec…): docs/referee/R-N5-NHN.md: all SIGNED (T0-PIN, NHN-BOUND conditional on RHO's
  HAT-FREEZE; HN-POLY-ALL conditional on PFZ, PFZ-ext (i′)/(ii), RHO), no gaps; NHN-N1 (τ(o) = o: R39 (f)(c) case A only, §5 (b)'s
  own argument covers it), NHN-N2 ("there" in §6), NHN-N3 (T0-PIN vacuous: lib + 1.88M climb candidates). Tools nhn_probe.py,
  nhn_climb.py; logs scratch/nhn_logs/.
- DONE: RHO §C vs R2 269ae45a (identical; RHO-N2 missed by R2) 06d6e6db.
- DONE: P-N5-NEEDB (e6ee613, sha1 7471aef3…): docs/referee/R-N5-NEEDB.md: all SIGNED, no gaps; NEEDB-N1 (XG "in particular"),
  N2 (case (i) k = first fallback after k0), N3 (FBL R = today's R̄), N4 (general form: at every THR fb with r ≥ 0 the σ*-play from x0
  uses a non-exceptional gate; 1,818 checks, 0 failures). (LV+) occurs once: R2's block_9501.pg at its start pair (gate (10, 8)).
  Tool needb_probe.py (START=, RANDSTARTS= env); logs scratch/needb_logs/.
- DONE: P-N5-FBPOLY (42d8c3a9, sha1 de244dcd…): docs/referee/R-N5-FBPOLY.md: all SIGNED; GAP FBP-1 ((a)'s final bound: deg_U(o) ≤ n − 1
  fails with a self-loop at o; repair |succ(o) ∩ Û|), GAP FBP-2 ((b)'s proof assumes o ≠ c_θ; repair: v cannot switch in U = {o, v});
  FREEZE-EXIT / THETA-AFTER regime unreached (3.82M climb candidates, best −1). Tools fbpoly_probe.py, fbpoly_climb.py.
- DONE: P-N5-PHI (R-N5-PHI: all SIGNED; S1 untouched, S2 = the citation of R15 (a), (d) on G^d + Lemma R, not open math) and P-N5-FX
  (R-N5-FX: SIGNED, (b) conditional on FBPOLY (+ FBP-1 repair for F*); FX-N1: (a) weaker than landed R30 (c) SN-PREFIX). Tool phifx_probe.py.
- DONE: FBPOLY §C vs R2 2fef7c4a (d6248f7b; FBP-1/2 = N-FBP-2/1, repairs stand; N-FBP-4 loop witness re-run), NHN §C vs R2 04b5c1fd.
- DONE: PHI §C vs R2 b621f9a (identical). P-N5-NH-box42 (54ac72e6, sha1 93d19be8): R-N5-NH42.md all SIGNED, no gaps; notes NH42-N1..N3;
  my engine reproduces the lane's library K_W / E / class counts exactly. Tool nh42_probe.py.
- NEXT: §Cs for NEEDB, FX, NH42 after REFEREE-2's reports and the Lead's SHAs. NHN / NEEDB §Cs after R2's reports (do not open R2-N5-{NHN,NEEDB,FBPOLY,PHI,FX}* before).

## HANDOVER (successor 9 -> successor 10), written 2026-10-25T16:35Z by date -u, context ~490k (Opus 5.5 under D15; label "(Opus 5.5, D15)")
Lead: session_014FBi6o334DvwT5Uw2kDfoN (send_message via claude-code-remote MCP; first line "From REFEREE (<date -u>):"; self-contained).
Branch claude/referee. Start: git fetch origin; trunk = remote HEAD claude/vibrant-johnson-nxvvxo (`git ls-remote --symref origin HEAD`);
CHECK HEAD == origin/claude/referee (the container started stale at 73b46eb8 for successors 5-9, 1505 behind for me); fast-forward, then
merge trunk --no-ff. Push ONLY with scripts/push.sh > file 2>&1; echo $?. Build Oink first (scripts/setup_oink.sh). Never read
docs/referee-2/R2-<packet> before your own report on that packet is pushed. READ NOTIFICATIONS AT EVERY PUSH: Lead messages queue up
while you work (I read the 15:34Z / 15:41Z / 15:59Z messages late and did LV before PFZ).
### DONE (successor 9; all pushed, head after this commit)
| packet | report | my verdicts | §C / state |
| --- | --- | --- | --- |
| handover check | docs/agents/handover-checks/REFEREE.md "successor 9" (0d3a61a1) | Lead 5/5 | — |
| P-N5-NEB (ba15e51f, pin 314d220) | R-N5-NEB.md 40adbf1c | §1-§7 all SIGNED, no gaps; notes NEB-R1, N1-N5; NEB-B1: BAND FALSE in the rises form, the gates form later (tauw_A state 13) and the gates form at the base (R-N5-NEB/band_base_cex.pg sha1 468edac8, Lead re-ran OK) | §C 46a80300 vs R2 a4516df9: identical, gap map empty; N-NEB-2 MISSED by me |
| P-N5-LV (d0d797f0, pin 601df6e) | R-N5-LV.md 8054da2f | all SIGNED (CN-LAST discharged by R38); notes LV-N1..N3 | §C 46a80300 vs R2 b1038bea: same substance, gap map empty; N-LV-1 MISSED by me; N-LV-3 (u* = none reachable) re-run on my engine; NL= FALSE line (nleq_cex_n48 e72e4034) confirmed, not to sign |
| P-N5-PFZ (3c617e06, pin 283bcb6) + ext (b3702b1b, pin c61ecc4) | R-N5-PFZ.md 85953433 | all SIGNED, except ext BRK-POLY′ (i): SIGNED WITH GAP PFZ-1 (true, but the proof misses the ρ_S P-changing θ-changes; my repair: refined θ-LEN ≤ |A_low| − [o low], and ρ ≥ 1 ⇒ a high u ≠ o in U); notes PFZ-N1..N3 | main-packet §C (this commit) vs R2 37e55fde: identical, gap map empty. EXT §C PENDING: REFEREE-2 10 reviews ext |
| P-N5-LV2 (3b23a41f, pin 283bcb6) | R-N5-LV2.md b454ca32 + addendum 46a80300 | all SIGNED with the stated conditions, no gaps; note LV2-N1 (CYC-EV citation); addendum: the none part is non-empty (FLAT-ALL^none 351k checks OK; LV-NONE with N ≥ 2 never seen) | §C PENDING: after REFEREE-2 10's report |
### IN FLIGHT / NEXT
- Wait for the Lead's word on REFEREE-2 10's final SHAs for P-N5-PFZ-ext and P-N5-LV2. Then write:
  - the ext §C in R-N5-PFZ.md (central: does R2 find PFZ-1? check my repair against theirs);
  - the LV2 §C in R-N5-LV2.md.
- Nothing else is open.
### Tools (docs/referee/scratch/, own code on rl_engine.py, NO lane imports; `python3 -I`)
- neb_probe.py (+ rand mode), neb_climb.py (C^1O-preserving mutate(), write()), band_find.py (env BANDKEY).
- lv_probe.py, lv_climb.py, lvn_climb.py (u* = none climb); lv2_probe.py (STALE / EV-G / SAND / SCOPE-FB / FLAT-ALL^none).
- pfz_probe.py (θ-runs and P-epochs; env UMAX for exact DFS), pfz_climb.py.
- Logs: docs/referee/R-N5-{NEB,LV,PFZ,LV2}/ and scratch/{neb,lv,lvn,pfz}_logs/.
### Things only I know
- Random C^1O games never reach HN fallbacks or level −1 settings; mutation climbs from counterexample seeds do (NEB: 1.34M mutants hit
  every hypothesis).
- The |U| ≥ 3 post-freeze regime (PFZ) was not reached by me or by REFEREE-2 (both climbs plateau one fallback short or at |U| = 2).
- PFZ-1's repair argument, in full, is in R-N5-PFZ.md §7. The lane may instead state (i′) with (iii)'s constant 2n − 2.
- P-N5-NEB §9's base totals (13 / 6 / 34 / 27) come from an unnamed input set; the stated command gives 75 / 9 / 4 / 20 / 8.
- LV setting with r ≥ 0 (FLAT-ALL_{−1}, PL_{−1}, LV-PL, ENT-X_{−1}, LV-PL′'s block) never occurred anywhere; r = −1 occurs (R2 witness
  docs/referee-2/R2-N5-LV/climb/best_lv_9401.pg).
### Traps and lessons (keep)
- Clone starts stale; trunk is the remote HEAD branch, not main.
- Lead messages arrive mid-work: call ReadNotifications before each push and before starting the next packet.
- Lesson N-ENT-2 holds: count every hypothesis's occurrences, and say which are vacuous. A later climb (R2's) can overturn "vacuous":
  say "vacuous in MY data", with the file set.
- Check where an epoch-count proof puts the boundary transitions (PFZ-1): a θ-change at a P(θ) change is still a θ-change.
- A file under its final name on a peer branch can be a draft: compare only against the SHA the Lead names.

## HANDOVER (successor 8 -> successor 9), written 2026-10-25T13:11Z by date -u, context ~510k (Opus 5.5 under D15; label "(Opus 5.5, D15)")
Lead: session_014FBi6o334DvwT5Uw2kDfoN (send_message via claude-code-remote MCP; first line "From REFEREE (<date -u>):"; self-contained).
Branch claude/referee. Start: git fetch origin; trunk = remote HEAD claude/vibrant-johnson-nxvvxo (`git ls-remote --symref origin HEAD`);
CHECK HEAD == origin/claude/referee (container started stale at 73b46eb8 for successors 5-8); ff, then merge trunk --no-ff. Push ONLY
with scripts/push.sh > file 2>&1; echo $?. Build Oink first (scripts/setup_oink.sh, ~2 min). Never read docs/referee-2/R2-<packet>
before your own report is pushed.
### DONE (successor 8; all pushed)
| packet | report | my verdicts | §C / state |
| --- | --- | --- | --- |
| handover check | "Handover check (successor 8)" below (9c3a8655) | Lead 5/5 | — |
| P-N5-RL (0a3c70cb, pin 2fb698d) | R-N5-RL.md b7419da0, §8.1 257c3d81, A1 38863849, §C 5f52510b, A2 d104aac2 | BL-FORM, BL (a)(d), CONF-MONO SIGNED; BL (b)(c)(e), FREE-FREEZE, EV (RL-4), EV+ COND (P); EQ-END COND CN-LAST; MERGE WITH RL-2 (ℓ = ∞); TEV-RED NOT SIGNED as stated (RL-1 cycle case; RL-3 wording) -> A2: fixes ac027458 + CYC-EV close RL-1..4; restricted TEV-RED + Consequence COND (P) | §C vs R2 30dc5f54: labels differ on MERGE (RL-2 kept; R2 ruling on ℓ = ∞ requested) and TEV-RED (same substance); N-RL-3 MISSED by me |
| P-N5-SCOPE §C | R-N5-SCOPE.md §C (257c3d81) vs R2 6d6e4bcf | no verdict differs; N-SC-1, N-SC-4 MISSED by my lane | done |
| P-N5-P1 (b98ca794, pin 48a8a4c) | R-N5-P1.md 58a5b734, §C 5f52510b | Lemma B, M, P1 (+P1′), §4 SIGNED, no gaps | §C vs R2 e036e4c5: identical; N-P1-1 wording |
| P-N5-OUT (9f032e61, pin 719ce66) | R-N5-OUT.md fa086876 | all SIGNED, no gaps (OUT-R1, OUT-N1 notes) | §C a8b8ef3e vs R2 dfcaae67: identical; N-OUT-1..4 accepted (N-OUT-1 and N-OUT-2's CASE-B-LEN part MISSED by me) |
| P-N5-ENT (4fd22be7, pin 765e893) | R-N5-ENT.md 55a3f6fb | FZ, BF, RB, WALK, CYC-EV, TEV-FB SIGNED; ENT-X, NJB-A, D1, PL-S″ COND (P) -> lifted by R36; no gaps | §C d6b8aef9 vs R2 b7df84b8: identical; N-ENT-1..3 accepted (N-ENT-2 'vacuous' overstatement MISSED by me) |
### IN FLIGHT / NEXT
- Nothing open. RL (R37), P1 (R36), SCOPE, OUT and ENT all converged with REFEREE-2 (RL-2 accepted by R2 at 88571b0).
- PARKED by the Lead's plan (13:35Z): successor 9 starts from this table and the Lead's next brief.
- Lesson (N-ENT-2): do not copy a packet's "vacuous in data" line; check which hypotheses actually occur.
### Tools (docs/referee/scratch/, own code, NO lane imports (Lead 11:36Z rule); `python3 -I`; logs scratch/rl_logs/)
- rl_engine.py: own N5 from the SPEC text (S1 VJ procedure, S2-S5, FIX 1-4). Reproduces rl_a/b/c counts; regions = Oink zlk on 309/309
  (rl_oink.py). rl_probe.py: RL checks + states() (R̄, F, H1-H3, r, M, phase key, scope runs) — reuse it.
- p1_probe.py (P1, exhaustive strategies), cyc_probe.py (FZ/BF/RB/WALK/CYC on (Σ) pairs), out_probe.py (SPLIT, F-FLAT, FREEZE-STEP,
  EPOCH, NO-ENTRY-A INV, CASE-B-LEN), rl_climb.py.
### Traps and lessons (keep)
- Clone starts stale; trunk is not `main` but the remote HEAD branch.
- A file under its final name on a peer branch can be a DRAFT (R2-N5-SCOPE 1f8a9109): wait for the Lead's FINAL SHA.
- Peers' stamps are not my clock (Lead 11:46Z message arrived 11:42Z by date -u).
- "ℓ ≥ −1" with ∞ among level values includes ∞: test the top value of every range (RL-2).
- "The last X vertex on the play" is ambiguous on a lasso: check the cycle (RL-1).
- "before e" vs "up to and including e": check whether e itself can be in the counted set (RL-3; realised on tevlast_cex_n40).
- Proofs valid at fallback states may fail at S4a states (RB uses M_k ≤ L; tevlast_cex_n40 t = 7).
- Bash: never pkill -f / pgrep -f with the pattern in the same shell; Bash `sleep` is blocked: use until-loops.

## Resume point (successor 8), written 2026-10-25T12:02Z by date -u (Opus 5.5, D15; session_01YRPeH49wEXXq7vW5qK35Gz)
- Handover check 9c3a8655: Lead 5/5 (11:46Z Lead stamp; GO R-N5-RL).
- P-N5-RL (pin 2fb698d, sha1 0a3c70cb...): docs/referee/R-N5-RL.md.
  - BL-FORM, R-SAME, BL (a) (d), CONF-MONO: SIGNED.
  - BL (b) (c) (e), FREE-FREEZE, EV (with RL-4), EV+: SIGNED CONDITIONAL ON (P).
  - EQ-END: SIGNED CONDITIONAL ON CN-LAST.
  - MERGE: WITH RL-2 (level ∞ window gates: (c) has no common vertex; inr2_n32 state 0 gate (6, 29)).
  - TEV-RED: NOT SIGNED as stated (RL-1: an Ev vertex on the cycle of x_t's play is not excluded). TEV-RED′ SIGNED CONDITIONAL ON (P),
    with RL-3 ("before e" -> "up to and including e").
- Tools (own engine, NO lane imports; Lead 11:36Z rule): scratch/rl_engine.py (SPEC S1-S5 from the text), rl_probe.py,
  rl_oink.py (regions vs Oink zlk, 309/309), rl_climb.py; logs scratch/rl_logs/.
- DONE: climbs (0 hits) -> §8.1; SCOPE §C written against R2 FINAL 6d6e4bcf (no verdict differs; N-SC-1, N-SC-4 MISSED by my lane, notes).
- P-N5-P1 (pin 48a8a4c, sha1 b98ca794...): docs/referee/R-N5-P1.md: Lemma B, Lemma M, Lemma P1 (+ P1'), §4 match all SIGNED, no gaps;
  §5 reading corrected for TEV-RED (RL-1). Tool scratch/p1_probe.py (exhaustive strategies, n <= 13; 0 violations, control bites).
- DONE: RL §C vs R2 30dc5f54 (MERGE: RL-2 kept; TEV-RED: same substance, NOT SIGNED kept; N-RL-3 MISSED by me), P1 §C vs R2 e036e4c5 (identical).
- NEXT: CYC-EV / RL fixes when routed (check it covers every t in (k0, k]).
- Lesson: "ℓ ≥ −1" with ∞ among the level values silently includes the infinite level; test the top value of every range.
- Lesson: "the last X vertex on the play" is ambiguous on a lasso: check the cycle.

## Handover check (successor 8), written 2026-10-25T11:33Z by date -u (Opus 5.5 under D15; session_01YRPeH49wEXXq7vW5qK35Gz)
1. Branch, head, distance to trunk. Commands: `git status`; `git fetch origin`; `git ls-remote --symref origin HEAD` (trunk =
   claude/vibrant-johnson-nxvvxo at 2fb698da); `git rev-parse HEAD origin/claude/referee <trunk>`;
   `git rev-list --left-right --count HEAD...<ref>`; `git merge --ff-only origin/claude/referee`; `git merge --no-ff <trunk>`.
   - Local claude/referee started STALE at 73b46eb8 (0 ahead / 1254 behind origin/claude/referee 560ff4c4; 1283 behind trunk).
   - Fast-forwarded to 560ff4c4 (successor 7's handover): then 0 ahead / 29 behind trunk 2fb698da.
   - Merged trunk with --no-ff: d0a950fd, 1 ahead / 0 behind before this commit; 2 ahead / 0 behind after it.
   - Packet object: `git show 2fb698d:docs/si/P-N5-RL-box10.md | sha1sum` = 0a3c70cbf873b2e011a5a00be54d38926f7861f1 (matches the brief;
     same on origin/claude/l-si, last touched there at 01d69ac3).
   - Oink: scripts/setup_oink.sh built 8fbf0a7 into tools/oink/build, exit 0.
2. Open work and next step (successor 7 HANDOVER above; Lead brief 11:36Z):
   - P-N5-SCOPE §C: my report R-N5-SCOPE.md (fb6089b / 560ff4c) all SIGNED, no gaps. `git ls-tree --name-only origin/claude/referee-2
     docs/referee-2/` shows R2-N5-SCOPE.md exists, but head 1f8a9109 calls it a "draft ... climbs pending" (names and commit subject only;
     contents not read). Next: wait for the Lead's word that the final R2-N5-SCOPE exists; then §C in docs/referee/R-N5-SCOPE.md.
   - P-N5-RL (after GO): docs/si/P-N5-RL-box10.md (sha1 0a3c70cb…, pin 2fb698d, L-SI succ. 5). Next: read packet §0 (P), RESULTS R18
     and R25-R35, SPEC; own probe docs/referee/scratch/rl_probe.py (asserts exactly one Odd vertex of out-degree > 1); check that each
     "conditional" label is exact (conditions used but not declared = gaps); report docs/referee/R-N5-RL.md. No R2-N5-RL read before.
3. GAPS rows (`grep -n G-N5-TIME docs/GAPS.md`): G-N5-TIME | major | owner L-NEW (L-LIT T22; referees later) | **open** | N5 SSI-GLOBAL
   makes polynomially many iterations (gauntlet step 4). Latest UPDATE 11:18Z: R34 (P-N5-TOG) LANDED; "Open as before; in review:
   P-N5-NJB (CHECKER), P-N5-SCOPE (both referees)". Related, closed: G-N5-TERM (R15).
4. Owner rulings verbatim (`grep -n -F` in docs/DECISIONS.md) with DECISIONS-INDEX status (`grep -nE "^\| *D(1|15|18) *\|"`):
   - D1 (index: **active**, 2026-10-14; DECISIONS.md l.7): "A claimed polynomial algorithm is far more likely to be wrong than right.
     Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below."
   - D15 (index: **active**, 2026-10-22; l.278): "q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous,
     reason about it"
   - D18 (index: **active**, 2026-10-24; l.333): "Focus on N5 and work toward proving it. Explore novel approaches, especially by
     connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions
     where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and
     open problems."
5. Trap found: a DRAFT of the second referee's report already sits on origin/claude/referee-2 under the final file name
   (docs/referee-2/R2-N5-SCOPE.md, head 1f8a9109 "draft ... climbs pending"). "The file exists" is not "the report is final": a §C
   written against it could compare with verdicts that change. I wait for the Lead's word and pin the R2 SHA I compare against.
   Also again: the clone started stale (73b46eb8, 1254 behind origin/claude/referee); and trunk is not `main` but the remote HEAD
   claude/vibrant-johnson-nxvvxo (`git ls-remote --symref origin HEAD`).

## HANDOVER (successor 7 -> successor 8), written 2026-10-25T11:09Z by date -u (stamp corrected from an estimated 11:10Z), context ~530k by the Lead's WATCHDOG (Opus 5.5 under D15; label "(Opus 5.5, D15)")
Lead: session_014FBi6o334DvwT5Uw2kDfoN (send_message via claude-code-remote MCP; first line "From REFEREE (<date -u>):"; self-contained).
Branch claude/referee. Start: git fetch origin claude/referee claude/vibrant-johnson-nxvvxo; CHECK HEAD == origin/claude/referee (the
container started stale at 73b46eb8 for successors 5, 6, 7); merge trunk with a normal merge. Push ONLY with scripts/push.sh > file 2>&1;
echo $?. Build Oink first (scripts/setup_oink.sh). Never read docs/referee-2/R2-<packet> before your own report is pushed.
### DONE (successor 7; all pushed; every report has §C unless noted)
| packet | report | my verdicts | §C / state |
| --- | --- | --- | --- |
| handover check | notes/REFEREE.md "Handover check (successor 7)" (3e86cb10) | 5/5 | — |
| P-N5-L2 (R33 landed) | R-N5-L2.md 7626354e (+524d93f5 climbs, d3ccb9cd fixes check) | all SIGNED; L2-1 (τ(o) = o wording), L2-2 (H1-INT (b) phase exits, exitdrop_n3); FINDING DROP-LEN FALSE (droplen_cex_n12) | §C ce241061 (4 rows, no verdict differs) |
| P-N5-FRZ (R32) | predecessor's R-N5-FRZ.md; my §C 1f13a6f9 + C.6 9ad6bfba | N-FRZ-1 MISSED by my lane, accepted; BLOCK vacuous in all data | converged |
| P-N5-NJB (R35 waits on L-SI fixes2) | R-N5-NJB.md 524d93f5 | MINSET NJB-1 wording; G-NJB-1 MISSED by me (literal (c) = NJB); ENT-SHAPE (5) NOT SIGNED, (5′) SIGNED (NJB-2) | §C 5e85c706 + C.7 49dc13bf: converged, REFEREE-2 withdrew N-NJB-1 |
| P-N5-TOG (R34 at CHECKER) | R-N5-TOG.md fff6e624 | all SIGNED; X-SN-PHASE WITH TOG-1 (crossing out of the SN prefix; slack), TOG-2 (§11 → §7) | §C 49dc13bf (2 rows); fixes f15b58dd + fixes2 698539a9 consistent |
| P-N5-SCOPE (pin 8998ee6, sha1 c3f5ed37) | R-N5-SCOPE.md (this commit) | all SIGNED, no gaps | §C OPEN: when REFEREE-2 successor 8's R2-N5-SCOPE exists |
### IN FLIGHT / NEXT
- SCOPE §C (Lead will say when R2-N5-SCOPE exists). My climbs scope_climb.py seeds 91/92 finished: 0 failures over 766,585 candidates,
  maxima (3, 0, 3) / (4, 0, 4); recorded in R-N5-SCOPE §8.
- Nothing else open on my side. CHECKER N-2 (R-N5-TOG l.9 cited the L2 §C as 5e85c706; it is ce241061) fixed in this commit.
### Tools (docs/referee/scratch/, own code; every probe asserts exactly one Odd choice vertex where 𝒞^1O is meant; own trace = n5.run)
l2_probe.py (L2 checks), l2_pc.py (P^c_ℓ path enumeration, NEG=1 control), l2_exitdrop.py, l2_climb.py (frz|tog|h2s), l2_oink.py (N5 regions
vs Oink --zlk -v), njb_probe.py (RDROP, PL (c′), MINSET, NORF, ENTP pattern), tog_probe.py + tog_climb.py, scope_probe.py (KEY, WCH, SC,
FBI, NH1, CN-LAST; `gen` = general games) + scope_climb.py; frz_probe.py has §C counters (BLOCK_S4a_leaves, LEAVE_h_afterF, XRUN_*).
### Traps and lessons (keep)
- Stale local branch at start; peers' stamps are not my clock (Lead 08:07Z vs my 08:04Z); order by git, stamp by date -u at the moment
  of writing. I estimated two §C stamps and one notebook stamp and had to correct them: run date -u right before the header.
- An "iff" whose one side is forced nonempty by a sibling clause is a disguised conjecture (G-NJB-1); data on it is vacuous.
- "At some S4a step in (k0, k)": check where the vertex is AT k0; fallback evictions sit at the boundary (NJB-2).
- "In a phase" clauses about k and k+1: test phase-exit transitions (L2-2).
- Accounting with "both ends in P" versus counts "at states of P": the boundary transition recurs (FRZ-3, TOG-1).
- Check SHAs you cite against git log (I cited the NJB §C SHA for the L2 §C: CHECKER N-2).
- Random 𝒞^1O games are nearly vacuous for freezes, blocks, dirty intervals; name the thin spots; library + climbs carry the evidence.
- Bash: never pkill -f / pgrep -f with the pattern in the same shell.

## Resume point (successor 7), written 2026-10-25T09:07Z by date -u (stamp corrected from 09:05Z) (Opus 5.5, D15; session_01TWT1diK1Z9x2eK56iBVbZu)
- Handover check 3e86cb10 (Lead 5/5, 08:20Z).
- P-N5-L2 (pin 04b3f48, sha1 cbea0739…): docs/referee/R-N5-L2.md (7626354e; climb addendum 524d93f5).
  - H3-CONST, G′, R-CONST SIGNED. FREEZE′ and X-RUN′ SIGNED on premise P-N5-FRZ.
  - H2-STICK WITH L2-1 (τ(o) = o wording; 400 of 520 library cases). H1-INT WITH L2-2 (pre-drop clause only in-phase; exitdrop_n3.pg).
  - FINDING: §8 DROP-LEN and its per-run form FALSE (droplen_cex_n12.pg: two drops in one fallback-free run, θ constant).
  - Thin: FREEZE′'s new case is unexercised (climbs reach n−2 / n−1, never n).
  - Tools: scratch/l2_probe.py, l2_pc.py (P^c_ℓ by path enumeration, NEG=1 control), l2_exitdrop.py, l2_climb.py (frz|tog|h2s),
    l2_oink.py.
- P-N5-FRZ §C (1f13a6f9, C.6 9ad6bfba) vs R2-N5-FRZ 20a73ca/f546b43c:
  - No verdict differs. N-FRZ-1 (ARENA two routes, one base) MISSED by my lane, accepted. N-FRZ-4 accepted.
  - BLOCK vacuous in all data (0 leaves in 30 runs; 0 at 2,410 (h) S4a transitions after freezes). Post-F(⊥) and segment −1 unexercised.
  - Joint label PROVED, pending CHECKER.
- P-N5-NJB (pin a7d85b3, sha1 f43a8823…): docs/referee/R-N5-NJB.md (524d93f5).
  - RDROP, PL (c′), PL-S′, NO-RF-OLD + Cor., ENT-SHAPE (1)-(4) SIGNED. MINSET WITH NJB-1 ("absorbed" = "entered R").
  - ENT-SHAPE (5) NOT SIGNED as stated: NJB-2, the level-L rise of z may sit at the fallback k0 (z ∈ R_{k0} evicted). Seen
    locally 1,159× in the library, hand-checked on cycelim_cex_n32 fb 15. (5′) signed.
  - Tool: scratch/njb_probe.py. D_M = 0 everywhere (thin).
- §Cs (09:45-09:46Z): L2 §C ce241061 (earlier written as 5e85c706 = NJB §C; corrected) (no verdict differs; L2-2 REFEREE-only; N-L2-2 via Lemma X-RUN° accepted). NJB §C 5e85c706: G-NJB-1
  MISSED by me (literal MINSET (c) = NJB; survivor form signed); ENT-SHAPE (5) VERDICT DIFFERS (N-NJB-1 assumes z ∈ F_{k0}; literal (5)
  NOT SIGNED by me, (5′) signed); REFEREE-2 ruling requested. Stamps first estimated, corrected 0363a7be.
- P-N5-TOG (pin d3daae1, sha1 7dfda8c8…): docs/referee/R-N5-TOG.md fff6e624. All SIGNED; X-SN-PHASE WITH TOG-1 (X_SN counts the crossing
  out of the SN prefix; slack) and TOG-2 (§11 → §7). Tools scratch/tog_probe.py, tog_climb.py. NEXT: TOG §C when R2-N5-TOG exists.
- Lesson: an "iff" whose one side is forced by a sibling clause (Mn_{t+1} ≠ ∅ by (a)) is a disguised conjecture; data on it is vacuous.
- Lesson: never estimate a stamp; run date -u right before writing the header.
- NEXT: §C for L2 and NJB when the R2 reports exist; L-NEW / L-SI fixes files.
- Lessons:
  - A lemma that says "at some S4a step in (k0, k)" must exclude the boundary fallback transition. Check where the vertex is AT k0 (NJB-2).
  - "in a phase" clauses about a state k and k+1: test phase-exit transitions (L2-2).
  - Packet words defined in §0 (absorption) used loosely later (NJB-1).

## Handover check (successor 7), written 2026-10-25T08:12Z by date -u (Opus 5.5 under D15; session_01TWT1diK1Z9x2eK56iBVbZu)
1. Branch, head, distance to trunk. Commands: `git fetch origin claude/referee claude/vibrant-johnson-nxvvxo`; `git status -sb`;
   `git merge --ff-only origin/claude/referee`; `git merge --no-edit origin/claude/vibrant-johnson-nxvvxo`; `git rev-parse --short=8 <ref>`;
   `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo`.
   - Local claude/referee started STALE at 73b46eb8, 1002 behind origin/claude/referee. Fast-forwarded to 451b2922 (predecessor's handover).
   - Merged trunk 5071ce71 with a merge commit: head 6b665e27 before this commit; 2 ahead / 0 behind trunk (the handover commit + the merge).
     After this commit: 3 ahead / 0 behind.
2. Open work and next step (from the successor-6 HANDOVER section above and the Lead's 08:07Z brief; `grep -n "^## " notes/REFEREE.md`):
   - P-N5-FRZ §C (task 2): waits for REFEREE-2 successor 7's R2-N5-FRZ. `git fetch origin claude/referee-2`: head de9ff970 (handover merge,
     pin check 25fda0f); no R2-N5-FRZ file name under docs/referee-2/ (names listed only; contents not read). Next: the Lead's word, then §C in
     docs/referee/R-N5-FRZ.md (every differing verdict + joint gap map).
   - P-N5-L2 (task 1, after GO): object docs/new/P-N5-L2-box34.md at pin 04b3f48. `git show 04b3f48:docs/new/P-N5-L2-box34.md | sha1sum` =
     cbea07392521bcdfbce137ba361bb581f9df11d7 (matches the brief; same on trunk 5071ce71). Statements §1-§7 (H3-CONST, H2-STICK, G′, FREEZE′,
     R-CONST, H1-INT, X-RUN′); §8 not to sign. Next: own probe on scratch/frz_probe.py + sn_probe.py (one-Odd-chooser assertion), packet
     instances oneh_cex_n32 / onedrop_cex_n32, library, random, climbs; report docs/referee/R-N5-L2.md.
   - P-N5-NJB (task 3): docs/si/P-N5-NJB-box9.md, pin a7d85b3, sha1 f43a8823… (not yet verified by me). Next: after L2.
   - Oink: built by scripts/setup_oink.sh at 8fbf0a7 into tools/oink/build (exit 0).
3. GAPS rows relevant to me (`git show origin/claude/vibrant-johnson-nxvvxo:docs/GAPS.md | grep G-N5-TIME`):
   - G-N5-TIME | major | owner L-NEW (L-LIT T22; referees later) | **open** | N5 SSI-GLOBAL makes polynomially many iterations (gauntlet
     step 4, running time). The referees' part: each lane packet toward it (R15-R30 landed; P-N5-FRZ signed by me, R2 pending; P-N5-L2,
     P-N5-NJB queued). P-N5-L2 itself says "G-N5-TIME stays OPEN". Related, closed: G-N5-TERM (closed by R15).
4. Owner rulings, verbatim (`git show origin/claude/vibrant-johnson-nxvvxo:docs/DECISIONS.md`), with DECISIONS-INDEX status
   (`grep -E "^\| *D(1|15|18) " docs/DECISIONS-INDEX.md`):
   - D1 (index: **active**, 2026-10-14): "A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim,
     including the fleet's own, as wrong until it passes the gauntlet below." and "Never downgrade the referee to save money."
   - D15 (index: **active**, 2026-10-22): "q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it"
     (Lead reading L37 (1): referees on Opus 5.5; signatures labelled "(Opus 5.5, D15)").
   - D18 (index: **active**, 2026-10-24): "Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas
     from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state
     them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems."
5. Trap found: clocks disagree across sessions. The Lead's brief is stamped 08:07Z, but my first `date -u` after receiving it read
   08:04:24Z, and the predecessor's handover (stamped 08:04Z) reached origin only after that. A peer's stamp is not my clock: every
   time in my files comes from `date -u` at writing, and ordering questions are settled by commit order (git log), not by stamps.
   Also confirmed again: the container starts on a stale local branch (73b46eb8, 1002 behind); check HEAD == origin/claude/referee first.
   Also: the playbook puts handover checks in docs/agents/handover-checks/ (a Lead-only path where successors 5-6 wrote); the Lead's
   brief puts this one here in notes/REFEREE.md, and I followed the brief.

## HANDOVER (successor 6 -> successor 7), written 2026-10-25T08:04Z by date -u, context ~570k (Opus 5.5 under D15; label "(Opus 5.5, D15)")
Lead: session_014FBi6o334DvwT5Uw2kDfoN (send_message via claude-code-remote MCP; first line "From REFEREE (<date -u>):").
Branch claude/referee. Start: git fetch origin claude/referee claude/vibrant-johnson-nxvvxo; check HEAD == origin/claude/referee (stale
containers happened at every restart); merge trunk with a normal merge. Push ONLY with scripts/push.sh > file 2>&1; echo $?.
Build Oink first (scripts/setup_oink.sh, ~1-2 min). Never read docs/referee-2/ for a packet before your own report is pushed.
Objects not yet on trunk: read from origin/claude/<lane> by SHA (happened 3 times: l-new fixes, l-red instances, referee-2 report).
### DONE (successor 6; all pushed; every report with §C unless noted)
| packet | report | verdicts | §C |
|---|---|---|---|
| handover check | docs/agents/handover-checks/REFEREE.md (109721d3) | 5/5 | — |
| P-N5-OE (R28) | R-N5-OE.md 5e98e33c | U-loc, OE (OE-1..3 wording/closed), OX signed | 84748819 (= R2; N-OE-3 phase key MISSED by me) |
| P-N5-CLS (R29) | R-N5-CLS.md a0b92ecd | all signed; CLS-1..4 wording/closed; OG′ FALSE confirmed | 8af63475 (CLS-3 = G-CLS-1, R2's form adopted) |
| P-N5-SN (R30) | R-N5-SN.md 59a886d1 (+addenda 58dd6e86, 2f465ff1) | all signed; SN-1 ABS-COUNT d_o−1 form unproved (proved d_o+REL); fixes §2b H1-DROP/H1-KEEP/ABS-COUNT′ SIGNED (closes SN-1 except O_k = −1) | 3d49e0af (SN-1/2 = G-SN-1 (a)/(b)) |
| P-N5-FBW | R-N5-FBW.md 9a94dc7b | P-OPT VALID; all signed; FBW-1 (H1 not H2), FBW-2 (STRETCH k ≤ e) | a04615b5 (FBW-2 = N-FBW-1; FBW-1 kept against R2's text) |
| P-N5-FRZ | R-N5-FRZ.md 3a520ce7 (+Addendum 3171efc7: fixes l-new 1dc42ba close FRZ-1..3) | all signed; FRZ-1 (γ omitted again), FRZ-2, FRZ-3 (REL_Q boundary transition) | IN FLIGHT |
### IN FLIGHT
- FRZ §C: needs R2-N5-FRZ from REFEREE-2 successor 7 (session_01CE1xQNfGUgtJg9A7SWAkuE); the Lead will say when it exists. Compare against
  R-N5-FRZ.md verdict table + addendum; joint gap map, one fixes-file line per row.
### NEXT (in this order; Lead 08:06Z)
1. P-N5-L2: docs/new/P-N5-L2-box34.md, sha1 cbea0739…, pinned trunk 04b3f48 (L-NEW 14). FREEZE′ and X-RUN′ rest on P-N5-FRZ (my R-N5-FRZ).
2. P-N5-NJB: docs/si/P-N5-NJB-box9.md, sha1 f43a8823…, pinned trunk a7d85b3 (L-SI 4). NJB was a CONJECTURE in P-N5-FBW §6 (D_M = 0 in all data).
### Tools (docs/referee/scratch/; all assert exactly one Odd choice vertex where 𝒞^1O is meant; own N5 trace u1_probe.trace = n5.run)
- oe_probe.py (U-loc/OE/OX; lib|rand|randb), cls_probe.py (CLS: C5-C7, TRANSFER, OFFGATE, CN, NL, CLS1; fine phase key), sn_probe.py
  (OR, TC-SPLIT, R-STICK, SN-PREFIX, H3H2, LEAVE, ABS-COUNT/′, WK, ABS-L, H1-DROP/KEEP), absc_climb.py (FIT=h1drop), fbw_probe.py (P-OPT
  single-switch + control, FBW, FBW-S, CLS2, FLAT-ALL, STRETCH, PL), frz_probe.py (NL-MF, Fact 0, ARENA, Steps 1-2, FREEZE, RATCHET, BLOCK,
  X-RUN, SUB). 'lib' = every experiments/**/*.pg in 𝒞^1O with n ≤ 64 (252 files at 83bf81a1).
- Phase keys: SN/OE/FRZ packets use (λ_Ξ, τ); scope runs / CLS / FBW use (λ_Ξ, λ_U, τ). Check every citation's signed key (WM, NL transfer fine).
### Traps and lessons (keep)
- Stale local branch at start; objects referenced "on trunk" may not be merged yet: fetch the lane branch and check the SHA.
- Stamp times from date -u at writing (I slipped once, fixed in 696b08ce).
- Counting proofs "ends ≤ B": check the END state satisfies B's hypothesis (SN-1).
- A lemma signed for a TRANSITION inside a run: check both ends are inside (CLS-3 = G-CLS-1).
- "Including the repaired cases X": check the text actually carries each repair (FRZ-1, XA-3 (γ) omitted twice).
- Count tails as vertices, not gates (my first STRETCH check double-counted).
- "λ(o) ≠ o" is not "o off a cycle"; minimiser (CAP-1) and DF-trap checks at own cycle nodes for every minimiser / VJ00 5.8 step.
- Cycle through a switched own cycle node: the honest cycle; o is excluded by H1, not H2 (FBW-1).
- Random 𝒞^1O games are nearly vacuous for crossings, freezes (no n-state (h) windows), wakes, dirty intervals: name the thin spots.
- Bash: never pkill -f/pgrep -f with the pattern in the same shell (kills the tool shell); kill PIDs from ps.

## Resume point (successor 6): P-N5-FRZ (Lead 05:58Z; pin 25fda0f; docs/new/P-N5-FRZ-box34.md sha1 39df373c…; L-NEW succ. 14)
- docs/referee/R-N5-FRZ.md (from 06:16Z by date -u): all SIGNED; P^c_ℓ WITH FRZ-1 ((γ) omitted again = R20 XA-3), FRZ-2 (B-fallback B1
  own-cycle-node x: strictness by cycle node, not (V2)); X-RUN WITH FRZ-3 (REL_Q misses the transition leaving P; bound survives by slack).
  Tool scratch/frz_probe.py. Random games give no FREEZE windows (library only). NEXT: §C for FBW and FRZ when R2 reports exist.
- Lesson: when a packet says "including the repaired cases X", check the text actually carries each repair (FRZ-1).

## Resume point (successor 6): P-N5-FBW (GO 05:53Z Lead stamp; pin e69772b; docs/si/P-N5-FBW-box9.md sha1 88337bd6…; L-SI succ. 4)
- docs/referee/R-N5-FBW.md (from 06:01Z by date -u): P-OPT VALID (G-1OA-6 is about S4c's installed σ_{k+1}; P-OPT uses S4a's output at k = σ_k);
  FBW, FBW-S, CLS2, STRETCH, PL-S SIGNED; FLAT-ALL WITH FBW-1 (H1 not H2 for the cycle-node cycle); PL WITH FBW-2 (STRETCH k ≤ e for f_N).
  D_M = 0 everywhere (PL (b)/(c) unexercised). Tool scratch/fbw_probe.py (POPT single-switch check + control). NEXT: P-N5-FRZ (L-NEW 14), then §Cs.
- Lesson: count tails as vertices, not gates (my first STRETCH check double-counted a tail with two level-M gates).

## Resume point (successor 6): P-N5-SN (GO 03:42Z Lead stamp; pin 2c70ef6; docs/new/P-N5-SN-box33.md sha1 340d4f29…; L-NEW succ. 13)
- docs/referee/R-N5-SN.md (from 03:55Z by date -u): OR, TC-SPLIT, R-STICK, SN-PREFIX, H3H2, WK, ABS-L (premise = R29, signed by both) SIGNED;
  LEAVE WITH SN-3 (r=⊥ wording); ABS-COUNT WITH SN-1 (proof's "ends ≤ d_o−1" needs H1 at run end; proved d_o + REL; (d_o−1) form OPEN, 0 cex,
  climbs absc_climb.py) and SN-2 (+f for ε at fallbacks). WM transfer to (λ_Ξ, τ) VALID. Data vacuous: WK hypothesis, ABS-L absorptions.
  Tools scratch/sn_probe.py, absc_climb.py. Addendum 58dd6e86 (L-RED probes). §C vs R2-N5-SN (ddbecaf + 91d95e8): no verdict differs;
  SN-1/2 = G-SN-1 (a)/(b), same repair; N-SN-1 accepted (my Bellman route avoids it); 5-row map. NEXT: park on the Lead's word.
- Lesson: a counting proof "starts ≥ 0, ends ≤ B" needs B at the END state; check the end state satisfies the hypothesis giving B.

## Resume point (successor 6): P-N5-CLS (GO 02:40Z Lead stamp; pin 486107a; docs/si/P-N5-CLS-box8.md sha1 5bbfd872…; L-SI succ. 3)
- docs/referee/R-N5-CLS.md (written from 02:44Z by date -u): (C5)-(C7), Fact R, CLU, TRANSFER, NL SIGNED; OFFGATE WITH CLS-1 (M_k = ⊥ clause
  vacuous in a phase), CN WITH CLS-2 (Even y), CLS1 WITH CLS-3 (FBL at one state: statewise, closed), Corollary WITH CLS-4 ("evicting"
  undefined); OG′ FALSE confirmed (x31_re24 1→2, S4a). Lead's MF_up/FBR_EQ: MF_up = OG′ counter (S4a step), not a fallback M rise.
  Tool scratch/cls_probe.py (phase key (λ_Ξ, λ_U, τ)). §C written from 02:57Z (date -u) vs R2-N5-CLS (ffe10e1): no verdict differs;
  CLS-3 = G-CLS-1 (R2's form adopted: cite FBL's strong gate form at k1, not the stretch statement); N-CLS-1/2 accepted; 6-row map.
  Lead 03:08Z: merged, review closed, lands as R29 after L-SI's fixes file. PARKED. Likely next: L-NEW 13's R-STICK / SN-PREFIX / ABS-L.
- Lesson: when a signed lemma is stated for a TRANSITION inside a run, check both ends of the transition are inside before citing it.

## Resume point (successor 6, written 2026-10-25T01:5xZ, pushed 5e98e33c at 01:56Z by date -u; stamp corrected 01:56Z; Opus 5.5 under D15; label "(Opus 5.5, D15)")
Lead: session_014FBi6o334DvwT5Uw2kDfoN. Branch claude/referee. Push ONLY with scripts/push.sh > file 2>&1; echo $?.
- Handover check 109721d3 (Lead 5/5, 01:44Z). Local was stale (73b46eb8); predecessor's SO-1 addendum 2a0cb306 merged (afa95369).
  Lead: no §C on P-N5-SO needed (both reviews + R2's §C caee2ae on trunk; fixes cae3bb5b). Oink built at tools/oink (8fbf0a7).
- P-N5-OE (GO 01:44Z; pin 361d18c; docs/new/P-N5-OE-box32.md sha1 adeccd89…): docs/referee/R-N5-OE.md. U-loc SIGNED; OE SIGNED WITH GAPS
  OE-1 ("In particular": only level-≠⊥ changes excluded; tie changes occur off crossings, library 2 / random 50), OE-2 (CAP-1 at o on its
  honest cycle, ¬H1: R-N5-FB §4.2 re-derived, holds; closed), OE-3 (cite C1/C3); Corollary OX (i)-(v) SIGNED (OX-1 wording, FB-2 scope).
  Tool scratch/oe_probe.py (lib | rand | randb). Library numbers equal the lane's oddlev.py exactly (436/11/857/279/235).
  §C written 02:06Z-02:11Z (date -u) vs R2-N5-OE (ca6e5bd): no verdict differs; OE-1 = N-OE-1; MISSED N-OE-3 (phase key (λ_Ξ, τ) vs
  R25's (λ_Ξ, λ_U, τ): transfers valid, accepted); joint gap map 6 rows; pushed 84748819. Lead 02:25Z: merged, review closed, R28 with CHECKER C37. PARKED. NEXT: P-N5-CLS (L-SI succ. 3: OFFGATE, CN, TRANSFER, NL, CLS1), Lead sends it pinned; fresh report docs/referee/R-N5-CLS.md.
- Lesson (again): check the SETTING (phase key) each citation was signed under, not only the class.
- Lesson: "λ(o) ≠ o" (o not its own cycle node) is not "o off a cycle"; check the ¬H1 case of every minimiser citation separately.

## HANDOVER (successor 5 -> successor 6), written 2026-10-25T01:08Z by date -u, context ~525k (Opus 5.5 under D15; label "(Opus 5.5, D15)")
Lead: session_014FBi6o334DvwT5Uw2kDfoN (send_message via the claude-code-remote MCP tool; first line "From REFEREE (<date -u>):").
Branch claude/referee. Start: git fetch origin claude/vibrant-johnson-nxvvxo claude/referee; merge trunk with a normal merge (no rebase).
Push ONLY with scripts/push.sh > file 2>&1; echo $?. Never read docs/referee-2/ for a packet before your own report is pushed.
Build Oink first (scripts/setup_oink.sh). Stamps: take every time from date -u at the moment of writing (I slipped once: R-N5-U1 §C).
### State of my packets (all pushed)
| packet | report | my verdicts | §C |
|---|---|---|---|
| P-N5-U1 (R24) | R-N5-U1.md | U1, WC signed; CASC, TB, R signed with gaps (R-1 = G-R-2: Lemma R literal (c,P) form false at x = u) | done; N-U1-3 closure proved by me |
| P-N5-FB (R25) | R-N5-FB.md | all signed; CAP-1 (SPEC's σ̄ at an own cycle node is NOT a minimiser; full minimiser elsewhere, my §4.2 proof) | done |
| P-N5-U23 | R-N5-U23.md (+ App. A u2flat_n32) | CASC-U2 signed; CASC-U3 with gaps U3-1 (= G-U23-1, L_B = 0), U3-2, U3-3; R-1 (θ-changes under ¬H1 ≤ n − 1) closes N-U23-2 | done (R2 to confirm R-1) |
| P-N5-LP + P-N5-SO | R-N5-LP.md (Part 1 LP, Part 2 SO) | LP: Lemma DF NOT SIGNED, FALSE (docs/referee/R-N5-LP/df_cex.pg, n 11: own W-cycle node + FIX 2 = the VJ00 5.8 "2⇒3" gap); DF′ signed; WAKE via DF′ (W-1); rest signed (HI-1). SO: TH (SO-1 = dependency on my full-minimiser proof), SO signed (key-frozen step verified), XJ (XJ-1: f = O(n⁴(1+X)), not n³) | §C done (vs R2 4949d6c): no verdict differs; N-LP-1 accepted (missed). P-N5-SO second review moved to successor 6 by the Lead |
### NEXT for successor 6
- P-N5-SO (docs/new/P-N5-SO-box32.md @ 1ef02bb, sha1 deb5ee44): the Lead moved its review to successor 6. My own Part 2 of R-N5-LP
  (dcb41198) is a review already: TH (SO-1 CLOSED: R2-N5-FB §C.3 adopted my proof), SO signed, XJ (XJ-1). Ask the Lead whether
  successor 6 writes a fresh report or a §C of Part 2.
### Tools (docs/referee/scratch/; all assert exactly one Odd choice vertex where 𝒞^1O is meant)
u1_probe.py (own trace = n5.py loop asserted equal to n5.run; states(); TB/CASC/U1/WC; arena_test), lemr_probe.py (hooked evaluate),
casc_climb.py, fb_probe.py (lev/coarse/play_value; FB/CAP/SBMIN), eqfb_check.py, u23_probe.py + u23_climb.py, lp_probe.py (U/HI/UL/GR/NU/LP/DF),
so_probe.py (TH/SO). Library sweep = every experiments/**/*.pg in 𝒞^1O with n ≤ 64 (234 files now).
### Lessons (keep)
- VJ00 Lemma 5.8 "maximum ⇒ no improvement" (2⇒3) is BROKEN at own cycle nodes (length-only improvements); any lane citing it: test own cycle nodes.
- SPEC's σ̄ = VJ00's minimiser only away from own cycle nodes (FIX 2 DFS there). "Fully optimal" must include lengths (Lemma R).
- Every-game theorems that cite 𝒞^1O-signed results (R21, R23): check the scope of each citation (missed G-FB-2/3).
- Boundary cases of max-over-empty-set (L_B = 0) and own-cycle-node exclusions: test them explicitly.
- Bash: pkill -f / pgrep -f with the pattern in the same shell kills the tool shell (exit 144).


## HANDOVER (successor 4 -> successor 5), written 2026-10-24T20:56Z by date -u, context ~550k (Opus 5.5 under D15; label "(Opus 5.5, D15)")
Lead: session_014FBi6o334DvwT5Uw2kDfoN (send_message via the claude-code-remote MCP tool; first line "From REFEREE (<date -u>):").
Branch claude/referee. Start: git fetch origin claude/vibrant-johnson-nxvvxo claude/referee; merge trunk with a normal merge (no rebase).
Push ONLY with scripts/push.sh > file 2>&1; echo $?. Never read docs/referee-2/ for a packet before your own report is pushed.
Stamps: take every time from date -u at the moment of writing; never estimate an end time (I slipped twice: R-N5-RE §C, R-N5-XA).
### State of my packets (all pushed; every report has §C unless noted)
| packet | report | my verdicts | §C |
|---|---|---|---|
| P-N5-RE (R19) | R-N5-RE.md | G, Wo, RM signed; RE signed, (NC) not needed (SG argument); PIECE P-1 (R* contraction) | done; withdrawn later in R-N5-X §C: R19 (f) per-part "θ free" FALSE for Ξ on R (fbref_n48 56->57), total TRUE via X-1/TF |
| P-N5-XA (R20) | R-N5-XA.md | C, CR, XA signed; FBL u*!=none only; FBF all u* (R2's (h) base); Corollary signed in §C7 (O(n^3)/O(n^5)) | done (§C, §C7) |
| P-N5-X (R21) | R-N5-X.md | all signed; X-1 = TF (θ-change => F-change under H1, R constant) | done |
| P-N5-NH (R22) | R-N5-NH.md | all signed; P3-1 = G-NH-1 (R*_w unfaithful under λ_W(o)=o, closed by vacuity) | done |
| P-N5-Z | R-N5-Z.md | all signed; Z-1 = N-Z-1; Z-2 NOFE from FBL-N (ii); data appendix (s_rt32_final out of class) | done (this push) |
### NEXT (from the Lead 20:5xZ)
- Packet P-N5-U1: docs/new/P-N5-U1-box31.md, sha1 eb90788d…, pin trunk eee0d8a. Wait for the Lead's brief. Fresh report docs/referee/R-N5-U1.md.
### Tools (docs/referee/scratch/; all n5x.step read-only; all ASSERT exactly one Odd choice vertex)
re_probe.py (SW/NC/RE3/PSPLIT), xa_probe.py (throttled stretches, C/CR/FBL/FBF/XA), x_probe.py (phases, F-intervals, NF/F1/F2/EQ/sub-blocks/
Theorem X), nh_probe.py (crossing-free intervals, TC/F1°/P3′/Corollary), z_probe.py (ACT/LOOP/NOFE/NOFL-E/GAP/WM/LV′). Helpers come from
experiments/new/box25/common.py (rand_c1o, odd_choice = FIRST Odd chooser: hence the assertion).
### Lessons (keep)
- Check every "resp." / per-part claim separately, not only the sum (R19 (f)).
- When a proof chains through an intermediate value, try transitivity BEFORE the prefix (RE step 2).
- When a proof says "switching x makes the play return to o", ask what else switches in the same transition (G-XA-1 (b), missed by me).
- Contractions (R*, R*_w) are exact only when o's continuation leaves R; check the ¬H2 / λ_W(o)=o case.
- Glob-based data can pull in out-of-class games; assert the class.
- Random 𝒞^1O samples are nearly vacuous for throttled / route-form / re-entry structure; say so; named instances carry the evidence.

## Resume point (successor 5, written 2026-10-25T00:56Z by date -u): P-N5-LP (pin bc42f2c, docs/new/P-N5-LP-box32.md sha1 d2c8121a…)
- docs/referee/R-N5-LP.md: U, HI (Consequence gap HI-1), UL, GR, NU, Theorem LP, BAND, Corollary LP′ SIGNED; WAKE WITH GAP W-1 (closed
  via DF′); Lemma DF NOT SIGNED, FALSE: docs/referee/R-N5-LP/df_cex.pg (n 11, sha1 a128663e…; y = 7 own W-cycle node keeps 4 by FIX 2,
  (7, 8) gate at k+1, 4 ∉ R) = the VJ00 Lemma 5.8 "2 ⇒ 3" gap of R-N5T; DF′ (y not own W-cycle node) SIGNED. Tool scratch/lp_probe.py.
  NEXT: §C when R2-N5-LP exists. Context ~500k: HANDOVER after §C (successor 6 from this notebook).
- Lesson: any lane citation of VJ00 Lemma 5.8 "maximum ⇒ no improvement" is the broken direction; test it at own cycle nodes first.

## Resume point (successor 5, written 2026-10-24T23:45Z by date -u): P-N5-U23 (pin 7666336, docs/new/P-N5-U23-box31.md sha1 ee3e5d1e…)
- docs/referee/R-N5-U23.md: CASC-U2 + Corollary SIGNED (data vacuous: no U2 W-flat switch anywhere); CASC-U3 (i)/(iii) SIGNED WITH GAPS
  U3-2 (kinds constant, closed), U3-3 (c_θ = c_w wording); (ii) WITH GAP U3-1 (L_B = 0, no kind B: proof gives λ − 2, packet says λ − 3;
  repair max(L_B, 1); corner never realised, no counterexample); Corollary SIGNED; READING R-1 (θ-changes under ¬H1 ≤ |R| − 1).
  Tools scratch/u23_probe.py, u23_climb.py. Appendix A (u2flat_n32, 2 U2 switches OK). §C vs R2-N5-U23 (07b22b0): no verdict differs;
  U3-1 = G-U23-1 (same repair); R-1 closes N-U23-2 (θ = (c_θ, ∅, d) under ¬H1), pending R2. PARKED. Context ~450k.

## Resume point (successor 5, written 2026-10-24T22:47Z by date -u): P-N5-FB (pin 348393b, docs/si/P-N5-FB-box7.md sha1 9ece9994…)
- docs/referee/R-N5-FB.md: Theorem FB SIGNED WITH GAPS FB-1 (M < ∞ at a fallback needs the best-target line, NOINF covers switched edges
  only), FB-2 (phase-exit fallbacks, ≤ 1 per phase, 7 in named set); (T), MONO, NOINF, J1, OFF, TAME, Corollary, A SIGNED; COARSE-SI (a)
  WITH ENG-1 (inherited engine point), V-1 (Prog is VJ00 p. 15), V-2; CAP WITH CAP-1: SPEC's σ̄ at a cycle node (FIX 2 DFS) is NOT a
  minimiser (925 cases); closed: non-cycle-node σ̄ is a minimiser (case proof), λ(o) = o case direct. (JUMP-EQ) FALSE confirmed (x31_rx32
  53 → 54, last carry 51, L 24). Tool scratch/fb_probe.py. §C from 22:54Z vs R2-N5-FB (referee-2 7699593): no verdict differs; MISSED
  G-FB-2/G-FB-3 (𝒞^1O-only citations in an every-game theorem; accepted); CAP: R2 coarse-minimiser closure recommended. PARKED.
- Lesson: "σ̄ minimises" (VJ00's definition) is not SPEC's σ̄ at cycle nodes; check every VJ00 property against si.py's actual choice.

## Resume point (successor 5, written 2026-10-24T21:32Z by date -u, Opus 5.5 under D15; label "(Opus 5.5, D15)")
Lead: session_014FBi6o334DvwT5Uw2kDfoN. Branch claude/referee. Push ONLY with scripts/push.sh > file 2>&1; echo $?.
- Handover check bfbf4642 (scored 5/5 by the Lead 21:1xZ). Local branch was stale (73b46eb8); fetched + ff; trunk cf66bff merged (4b6456dc).
- P-N5-U1 (GO 21:1xZ; pin eee0d8a; docs/new/P-N5-U1-box31.md sha1 eb90788d…): docs/referee/R-N5-U1.md. Theorem U1 SIGNED; CASC SIGNED WITH
  GAPS C-1 (closed: only TB's CHOICE RULE is needed, not TB-even's whole-play hypothesis), C-2/C-3 wording; TB SIGNED WITH GAPS TB-1 (set-valued
  ⊕ sandwich, closed), TB-2 wording; Lemma R SIGNED WITH GAPS R-1 (literal (c,P)-only statement FALSE at x = u: 3-vertex instance, 4,074 random
  cases; fully optimal form holds and is the only one used), R-2 (VJ00 §6 (15), (22), Prop. 6.1 states only ONE shortest path survives:
  Lemma R is a strengthening); WC SIGNED; §6 READING correct. Tools: scratch/u1_probe.py (own trace, TBc/TB/R1/CASC/C1/U1/WC, arena_test),
  lemr_probe.py (hooked evaluate), casc_climb.py. DATA notes D-1 (|R| quoted as |R \ {o}|), D-2 (σ(10) switches once on u1t_cex_n32).
  §C written from 21:53Z (date -u) vs R2-N5-U1 (referee-2 28ddf6f): no verdict differs; C-1 downgraded to wording (R2 reading accepted); MISSED G-R-1 and
  N-U1-3 (accepted; N-U1-3 closure proved via VJ00 Lemma 5.7 in G_tau, eqfb_check.py 0/322). PARKED.
- Lesson: a lemma about "optimal edges" with set-valued ⊕ can fail where the optimal play from y passes x; test the formal statement on a
  3-vertex instance before signing, and check which form the later steps actually use.
- Trap: `pkill -f <pattern>` / `pgrep -f` + kill from the Bash tool kills the tool's own shell (exit 144); list PIDs with ps and exclude grep.

## Resume point (successor 4, 20:37Z by date -u): P-N5-Z (pin fba7177, docs/si/P-N5-Z-box5.md sha1 a027638f…)
- docs/referee/R-N5-Z.md: all SIGNED; LV′ WITH GAP Z-1 (runs broken by '±'; proof wording), Z-2 NOFE = one line from FBL-N (ii), Z-3 (F0)
  citation. Corollary Z: R21 (g) within hypotheses. LOOP's H1 needed (88 loop cases all without H1). Tool docs/referee/scratch/z_probe.py.
  NEXT: §C when the Lead says R2-N5-Z exists (docs/referee-2/ NOT read for Z).

## Resume point (successor 4, 19:48Z by date -u): P-N5-NH (pin c7981ee, object sha1 382c5143…)
- docs/referee/R-N5-NH.md: F1°, TC, P3′ step 2 + Corollary SIGNED; P3′ step 1 SIGNED WITH GAP P3-1 (R*_w not faithful when lambda_W(o)=o:
  C_W in R; closed: kappa-strict B-cases from C_W give an even top above c_theta, hence a better W cycle node, vacuous in J). Reduction READING
  with NH-1 (OTHER-block boundaries) and NH-2 (ROI W-changes via (SG)). P3′ data nearly vacuous. Tool docs/referee/scratch/nh_probe.py.
  §C vs R2-N5-NH (48da84a): no verdict differs; P3-1 = G-NH-1 same argument; accepted N-NH-2 (missed); R2's 'W-change <=> Xi-change, functions
  of route' is not an argument (mid vertices between c_w and c_theta), conclusion true via (SG). PARKED.

## Resume point (successor 4, 18:20Z by date -u): P-N5-X (pin afc88b0, object sha1 b21d2d06…)
- docs/referee/R-N5-X.md: F1, NF, Theorem X SIGNED WITH GAPS (X-1..X-4, all closed); XW, EQ, FBL-N, F2, FB-W SIGNED; §8 table checked.
  X-1: R19 (f) "theta free" PIECE count of Xi-or-W changes needs: theta-change => W-change on F (sigma-bar(o) is an F-exit under H1; min over exits
  + R15(a)). My own R-N5-RE §5.2 count sentence assumed theta constant. X-2: F empty edge case (my probe flagged it first). X-4: fixes §5 used as
  re-derivation. Tool docs/referee/scratch/x_probe.py.
  §C done vs R2-N5-X (059f492): no disagreement; WITHDREW 'R19 (f) as landed TRUE' (per-part 'resp.' false for Xi on R: fbref_n48 56->57,
  R={o}); confirmed docs/agents/R19-note-X1.md wording; TF = X-1 equivalent; accepted N-X-2. PARKED.
- Lesson: when a signed statement says 'resp.', check each part separately, not only the sum.
- Context at this point ~330k+; park with handover notes if past ~600k.

## Resume point (successor 4, 2026-10-24T15:28Z by date -u): P-N5-XA
- P-N5-XA (Lead 15:22Z; pin b70aa59; docs/new/P-N5-XA-box27.md sha1 832d0da2…): docs/referee/R-N5-XA.md. C SIGNED; FBL SIGNED WITH GAPS XA-1
  (F->R "none" not proved: S4c sends c to its BEST gate edge, may be F; true for u*!=none since flat forces P(w)=empty, P(theta) odd top;
  u*=none untested); FBF SIGNED WITH GAPS XA-2 (repair: after S4c, Xi_L(sigma_{L+1}(y)) >= Xi_L(z) for all successors z); P^c/CR SIGNED WITH
  GAPS XA-3 (R17 B1 omission inherited), XA-4 (Odd x); XA SIGNED (no data: 0 re-entries anywhere); Corollary READING, XA-5 (flat fallbacks are
  PIECE separators; R15(d) bound circular). Tool docs/referee/scratch/xa_probe.py. Random samples vacuous (throttled stretches ~1 in 1,000 runs).
  §C 15:47Z-15:47Z vs R2-N5-XA (referee-2 9d3f1fb): I MISSED R2's G-XA-1 (b) (c's switch into R can coincide with z's route leaving, so (h)
  at k+1 holds and FBL's statement is unproved for u*=none); withdrew "statement survives". R2's (h) argument (c never in R_t on S) closes FBF for
  all u* and supplies my repair's base. N-XA-1 accepted (CR fallback case vacuous). N-XA-3 does not close XA-5; my closure: PIECE's Lemma P
  invariant is about values, flat fallbacks preserve it (pending R2). PARKED.
  UNPARK 16:50Z: §C7 signs the Corollary (u*!=none, (h); pieces pass flat fallbacks; O(n^3) VC/crossings/non-flat FB; O(n^5) via R15(d),
  value-preserving = Xi and W unchanged, accepted). PARKED.
- Lesson: when a proof says "switching x to z makes the play return to o", ask what else switches in the same transition.

## Resume point (successor 4, written 2026-10-24T14:40Z by date -u, Opus 5.5 under D15; label verdicts "(Opus 5.5, D15)")
Lead: session_014FBi6o334DvwT5Uw2kDfoN. Branch claude/referee. Push ONLY with scripts/push.sh, output to a file, print $?.
- P-N5-RE (Lead 14:20Z 10-24; pin 52c7261; object docs/new/P-N5-RE-box26.md sha1 8dba4576…): docs/referee/R-N5-RE.md.
  G SIGNED; Wo SIGNED; RM SIGNED WITH GAPS (RM-1 wording); RE SIGNED WITH GAPS RE-1, RE-2 and (NC) NOT NEEDED: switched y with
  lambda_L(y) = lambda_{L+1}(y) != y gains strictly by V1 at both states + gate + R15(a) + ONE strict V2 on (Xi_L(sigma_L y), Xi_{L+1}(z))
  (no prefix of Xi_L(z), so no avoidance of y needed); the packet's caveat sentence is false (1,852 switches, none in RE's setting).
  PIECE SIGNED WITH GAPS P-1 (count |R|-1 needs contraction R* on R with o self-loop at c's priority; verbatim R17 gives |R|+|K|-1),
  P-2 (Consequence omits joint lambda-phase). Tool docs/referee/scratch/re_probe.py (SW/NC/CAV/RE3/PSPLIT); neg. control 57/446.
  Lane random reentry samples are VACUOUS (no re-entries); RE data = pinned instances only.
  §C written 14:57Z (referee 87beaa60 + stamp fix) against R2-N5-RE (referee-2 c66da44, trunk 8001ee8): no disagreement. RE-1=G-RE-1,
  RE-2=G-RE-2, P-1=G-RE-3 (R2 repairs via Lemma P base at o; mine via R*), P-2=N-RE-4. Accepted R2's sharper (SG) (only lambda_k(y) != y),
  N-RE-1..5; RM-1 downgraded to a note. My reading: Lemma RE does not use tau constant (41 leaves at tau-changing transitions, strict);
  N-RE-3 accepted as the safe wording fix. R2's nc_fail_n12 = (NC) in RE's setting, strict under my probe. PARKED.
- Lesson: take the §C stamp from date -u BEFORE writing it; never estimate an end time.
- Lesson: when a proof chains through an intermediate value (y ⊕ Xi_L(z)), ask whether transitivity BEFORE the prefix removes the
  side condition; here it removed a whole hypothesis.

## Resume point (successor 3, written 2026-10-24T03:48Z by date -u, Fable 5.1 under L36)
Lead: session_014FBi6o334DvwT5Uw2kDfoN (docs/NOW.md line 14). Branch claude/referee. Push ONLY with scripts/push.sh, output to a file, print $?.
- P-N5-1OA (Lead 03:20Z 10-24; pin 07f298d): docs/referee/R-N5-1OA.md. (A) L-RED Prop X / Cor. X1 (R58 §9) SIGNED WITH GAPS A1-A2 (S1
  tie-break locality checked step by step; "waits" case). (B) L-NEW box 24 theorem (N5 on o-acyclic C^1O < (C_X+d)(B+1) from any start)
  SIGNED CONDITIONAL ON (P) WITH GAPS B1-B6, all closed; (P) is used only on one-player G[X], the form R-N5-1P §3 route (a) re-derives.
  Lemma R SIGN; Lemma S SIGN WITH GAPS S1-S2 (citations). Lemma 1's flat case = R-N5-1P §4 G4 (arbitrary state); R17 Cor. 2 is
  start-independent. Tool: docs/referee/scratch/n5_1oa_probe.py (n5.py unmodified, (σ,τ) captured; PX/L1/L2/L2c/L3/BLK/TOT/GN1 from the
  definitions; biased generator gives ~1 pure transition per 2.5 runs). 7,200 runs + lane instances, 0 violations; negative controls fail as
  the lanes say. Re-pin d78e54f (full text, sha1 d3550267) read 03:43Z: verdicts stand; B1/B3/B4/B6 closed by the new text, new B7 (R17's
  omitted "c even, shorter" case inherited). L-RED's block_bk20/bk32 (blocks 27 / 49 > |Y|): 0 violations. NEXT: §C with REFEREE-2 when the Lead
  says R2-N5-1OA exists (docs/referee-2/ not read). Lead 03:50Z: re-pin WITHDRAWN, signed object = 07f298d. §C written 03:51Z-04:05Z
  after R2-N5-1OA (referee-2 603cb3a): identical verdicts; accepted R2's tie-break-free count (G-1OA-2), N-3 (Lemma 1 holds on all C^1O),
  and G-1OA-6 first half (Lemma S (c)/(d) are S4a-only), which I had MISSED. Lesson: when a lemma's heading scopes a claim ("Arena
  steps"), check the claim as the text states it over all k, not as the heading intends. Lead 03:57Z: signed object = d78e54f after all;
  §C2 written 04:01Z-04:08Z against R2 §7: B7 = N-4; N-5 (Lemma 3 length +1 for o) accepted as missed by me. PARKED.
- Lesson: the lane's start files are named <name>.start, not <name>.pg.start; read both.

## Resume point (successor 3, written 2026-10-22T00:08Z by date -u, Fable 5.1 under L36; P-N5-1P, done)
Lead: session_014FBi6o334DvwT5Uw2kDfoN (docs/NOW.md line 14). Branch claude/referee. Push ONLY with scripts/push.sh, output to a file, print $?.
Label every verdict "(Fable 5.1)". Never read docs/referee-2/ for a packet before my own report is pushed.
Trunk claude/vibrant-johnson-nxvvxo was merged into claude/referee at the start (639c3e8c; packet pin 26905f0 is an ancestor).
- P-N5-1P (Lead 23:32Z 10-21; pin 26905f0): docs/referee/R-N5-1P.md. Lemma P / (F1)(F2) / (V1)(V2) / Theorem PH / Cor. 1-3 of
  docs/new/N5-phase-bound-box10.md: SIGNED WITH GAPS G1-G9 (G1-G5 closed, G6 DATA note, G7-G9 citation slips in the addendum's §6); no step wrong. G1 = (F1) is VJ00 Lemma 5.8 (1=>2)
  whose source proof leans on unproved Lemma 5.9 / Prop. 5.10 (fleet G-N5T-3): I re-derived the one-player case by dualising Lemma 5.5's
  proof (report §3) + exhaustive data. G2 = B1's case list omits "c even, shorter" (conclusion survives). G3 = optimum not unique, stop
  rule, counts tie-break dependent. G6 = rel_g12 tightness holds for sbstep (11 = n-1) but n5.py takes 10; phase_vc.txt line 12 stale.
  Lead addendum 23:42Z (trunk 0f899f3): SCOPE line + §6 VJ00 dependency list; checked: right for the bounds ((F1) via (11) in the dual,
  no Lemma 5.8), with citation slips G7 (Improve is §4.4 (2), not §5.4), G8 ("2=>1" should be "1=>2"), G9 (Prop. 7.4 is p. 27).
  "switch-best = N5 on one-player games" checked against SPEC S4a-c: YES (dual order is the exact reverse; fallback only in the all-flat
  situation and terminal). Tool: docs/referee/scratch/n5_1p_probe.py (from the definitions; modes rand|keep|far, 'n5' compares n5.py
  unmodified, 'inst' reads .pg/.start). §C written 00:20Z-00:40Z 10-22 after R2-N5-1P (referee-2 f954070, trunk 12617fc): full agreement;
  accepted R2's N-2 (phase_vc counts the closing step: only rel_g12 is tight in-phase), G-1P-2 (the "no other switched vertex on the return
  path" line as its own gap), G-1P-4's sharpening (VJ00 asserts the ⊵ halves of (4)/(6); my route (a) via the dual of Lemma 5.5 avoids
  them); G-1P-7 CLOSED with scratch/n5_1p_ph48.py (Lemma P on n5.py's own ph_n48 sequence, every simple path, 430 s). PARKED after
  the push on the Lead's word; next packet from the Lead.
- Lesson (this packet): a wrong order makes switch-all CYCLE in a one-player game (VJ00 Lemma 5.7 breaks); my first probe had both
  MaxDiff signs reversed and hung. Test the order on a 3-vertex game before trusting any loop built on it.
- Lesson: si.py strategies hold -1 at Odd vertices; fill the forced edge before simulating plays.

## Resume point (successor 2, written 2026-10-18T23:04Z by date -u, session_017Tv79KB6LLrQUtLtVCnNDH, Opus 5.5 under D12)
Lead: session_014FBi6o334DvwT5Uw2kDfoN. Branch claude/referee. Push ONLY with scripts/push.sh, output to a file, print $?.
Local branch was stale at start (5ed56c5, 1947 behind): fetch, then check HEAD = origin/claude/referee before anything else.
- Handover check 18b0569 (scored 5/5 by the Lead 22:58Z).
- P-N5T (GO 22:58Z; box to ~01:30Z): docs/referee/R-N5T.md. N5 termination reading (docs/new/G-N5-TERM-reading.md @ 812ecba):
  SIGNED WITH GAPS (Opus 5.5, D12). Lemma A = VJ00 Lemma 5.7 (SIGN); Lemma B SIGN WITH GAPS (G-B1 =_ℓ on pairs includes
  length; G-B2 wording; closed); Theorem SIGN; N5 application SIGN WITH GAPS (G-N1 engine = Ωσ, DATA 0/22,969 mismatches;
  G-N2 closed). VJ00 Lemma 5.8 "2 ⇒ 3" gap CONFIRMED (also breaks VJ00's I2/P1); the reading does not use it.
  Tools: docs/referee/scratch/n5t_probe.py (VJ00-only brute force), n5t_engine_xcheck.py.
- §C written 23:15Z (agree; accepted R2's N1 and G-N5T-3; I1 failure confirmed with n5t_i1.py). Then PARK on the Lead's word.

- P-N5K9 (Lead 00:20Z 10-19): docs/referee/R-N5K9.md. K9 SIGNED conditional on (P*), gaps K9-G1 (computed σ̄ optimal, DATA
  0/21,373), K9-G2, K9-G3 (closed). (P*) = any-subset, adaptive, flat-included one-player bound for the improver: NO source.
  Switch-all does NOT suffice; (P_strict) (count only Ω-strict steps) does, with an extra (2n(n−1)+1) factor. VJ00 §7 read myself.
  Tools: scratch/n5k9_sbar.py, n5k9_longest.py, n5k9_r2chain.py. §C written 00:38Z (no conflict; accepted R2's Step 2 tightening;
  R2's 183-step n=10 chain confirmed; my random-game data withdrawn as evidence). PARKED.

- P-C1P (Lead 01:14Z 10-19; pin 01d63d7): docs/referee/R-C1P.md. CTRL SIGN, NOSTEAL-1P SIGN, OUTCOME-MONO-1P / SAME-CTX SIGN WITH
  GAPS (closed), LEX SIGN WITH GAPS (L-1 OPEN: strict all-pairs form = (CHAIN-CHANGE)), R46 §1 SIGN, §2b SIGN, §3 SIGN WITH GAPS
  (R-2 OPEN: S − 1 = |P| + I, I = chain-keeping transitions). Oink built at tools/oink (8fbf0a7). Lesson: "phase" = searches of one
  player between dominion-finding searches (R5 (g)); G′ fixed inside a phase. §C written 01:39Z (agree; accepted R2's G-SC-2: cite
  R9 (b) for the Dom step). A1 (R47, Lead 02:04Z, pin da63c40) written 02:06Z-02:09Z: EMPTY-REC, §2 (i), DOM-MONO SIGN; SPTL-SANDWICH, CK, §5 SIGN WITH
  GAPS (A1-1..A1-5 closed). Overall YES: GAP-A on 𝒞^1P ⇐ (NEST*-BOUNDED). §C-A1 written 02:26Z (agree; accepted A1-G2 cite R10 (a)/R9 (b);
  withdrew A1-4 'unproved' — R2's K ≤ (n²+n)n makes R47's K valid; A1-N2 once per player block). NEXT: CHECKER diff of RESULTS R16. 02:47Z: corrected my R46 §1 K count (arithmetic slip; bound true by R2's count).
  Lesson: multiply out every constant I tick.

## Sources opened (append)
- VJ00 BRICS RS-00-48, same pdf (sha256 485a12de432a2a8c88640b0718bd2042d855fa86d6a82092a0d538fd41ba9e65), downloaded and opened
  2026-10-24 21:18Z by date -u (successor 5): §6 "Efficient implementation" (pdf pp. 24-27): procedure Shortest paths lines 1-10, claims
  (15)-(19), Proposition 6.1 (clauses 1-4: G(r) contains A shortest path) and its proof with (20)-(22), Theorem 6.2; §5.1 (3)-(10) incl. (6), (7).
- VJ00 BRICS RS-00-48, same pdf (sha256 485a12de432a2a8c88640b0718bd2042d855fa86d6a82092a0d538fd41ba9e65), re-downloaded and opened
  2026-10-21 23:40Z by date -u (successor 3, Fable 5.1): §4.1 (play values), §4.2 (order, MaxDiff), §4.3-4.5 (multisets, ⊕), §5.1 (3)-(10),
  §5.2 Prop. 5.1, Lemma 5.2, §5.3 Props. 5.3, 5.4, 5.6 (proof read), Lemma 5.5 (proof read in full), §5.4 Lemma 5.7, §5.5 Lemma 5.8 (proof
  read: 1=>2 uses Lemma 5.9 "proved similarly to Lemma 5.5" and Prop. 5.10, both without proof), §5.6, §6 Prop. 6.1 end, Thm 6.2, §7
  Prop. 7.4 (p. 27, no proof, no rule named), Claim 7.2.
- VJ00 = Vöge & Jurdziński, BRICS RS-00-48 (Dec 2000), https://www.brics.dk/RS/00/48/BRICS-RS-00-48.pdf, sha256 485a12de432a2a8c..
  (opened 2026-10-18 between 22:59Z and 23:04Z by date -u): §3 postulates P1/P2/I1/I2; §4.1-4.5; §5.1 (3)-(11); Prop. 5.1, 5.3, 5.4, 5.6, 5.10; Lemmas 5.2,
  5.5, 5.7, 5.8, 5.9; §6 Prop. 6.1.


## Resume point (LANE-RESTART step 1; written 2026-10-18T01:25Z by session_01M28EFY9Ysyqj67kXt3YSje, Opus 5.5 under D12; context ~520k)
Lead: session_014FBi6o334DvwT5Uw2kDfoN. Branch claude/referee. Push ONLY with scripts/push.sh, output redirected to a file, print $?.
Rebuild Oink first (scripts/setup_oink.sh; tools/ is gitignored). Label every verdict "(Opus 5.5, D12)" while D12/L33 holds.
Independence: never read docs/referee-2/R2-Px.md before your own R-Px.md is pushed; then add §C. R2 files can land on
claude/referee-2 before trunk: read them there if the Lead says they exist.

### DONE (this session, packets 6-11; every report has a §C comparison with REFEREE-2)
- a13ad2f handover check (5/5). R-P6 9f77ff9 (+§C ad4be01). R-P7 299bc58 (+§C 1abe1d7, §C2 876c06e). R-P8 fe4be51 (+§C c0edb9c).
  R-P9 72313f3 (+§C 3785d3f). R-P10 a09a89d (+§C 434a552). R-P11 fc86762 (+§C abc5185). Landed as RESULTS R9-R13 (R14 pending CHECKER).
- Current joint state of GAP-A (A_DTL, given STR-DET): S−1 ≤ Σ_{R∈C_bv} #fired⁺(R) + n(|C_T|+|C_Dom|) + 1 (R2-P11 N11-b1, confirmed in
  R-P11 §C). So GAP-A ⇔ (CTX⁺) ∧ (FIRED⁺-R) up to polynomial factors (an equivalence, not a reduction). Alternative per-context
  route: (EXIT_c) (R-P10; F_R ≤ 3(c+1)(|R|+1)|R|²). All premises DATA only.

### IN FLIGHT
- None (parked 01:26Z 2026-10-18 on the Lead's instruction).

### NEEDS
- L-ALG (via Lead): open wording fixes from my reports: G9-b1 notation and N9-b1 cite (R-P9); V=∅ stop convention in §23q (R-P10
  G10-a1, with R2's fixed σ set); N11-a1 / G11-a1 citations in §23s (R-P11).
- Lead: successor from this notebook under LANE-RESTART.

### Session log (packets 6-11)
- Handover check a13ad2f (docs/agents/handover-checks/REFEREE.md), scored 5/5 by the Lead.
- R-P6.md (packet 6; pin 8ff4085; pushed 9f77ff9 13:17Z): §22f SIGN WITH GAPS (G6-a1 F_R must count every non-rise incl. Π-blind e*,
  closed; G6-a2 Dom term and +1, closed). §22j SIGN WITH GAPS (G6-b1 Dom step pushes only the top: base-triggered closure,
  monotone in T, closed; G6-b2 Dom input NOT fixed by (R, X): |C_Dom| counts inputs, OPEN inside (CTX⁺)). (c) SIGN.
  Tool docs/referee/scratch/p6probe.py (needs experiments/dtl-bench on the path for stdsort).
- R-P6 §C (ad4be01): full agreement with R2-P6 (G6-a1 = G-F1; R2's R-I = my Dom input).
- R-P7.md (packet 7; pin d461a76): EXACT SIGN WITH GAPS (G7-a1 line 137->138-139, G7-a2 remaining-instances step; closed),
  PREFIX-MONO-X SIGN (absorbed case closes with EXACT's closedness, which does not need τ processed in run 2), corollary
  SIGN WITH GAPS (G7-c1 Π-blind e* via POS-FALL+C4, closed; G7-c2 necessary not sufficient). fallv_viol_n28: both falls at
  new steals; same tangle stolen at both. (FALL) <= (NS-COUNT). Tool docs/referee/scratch/p7probe.py.
- R-P7 §C (1abe1d7): agree with R2-P7; ACCEPTED R2's G-P7-c2 (e*-pairs need not be consecutive visits; F_R <= 3 N_R) and
  corrected my R-P6 A4 (factor 2 in R9's per-context budget). Lesson: never assume a context is visited once per search.
- R-P8.md (packet 8; pin a907c46): EXACT* SIGN (corollary of EXACT), PREFIX-MONO-X* SIGN, corollary SIGN WITH GAPS (G8-1
  factor 3), §22u chain valid as conditional with factor 3. Tool docs/referee/scratch/p8probe.py.
- R-P7 §C2 (876c06e): R9 constants; Lead keeps the doubled display of record (16:08Z); my tighter STR-DET constants noted, single
  signature. R-P8 §C (c0edb9c): full agreement with R2-P8 (STEAL-ONCE*, G8-2 accepted). Standing by, nothing in flight (16:09Z).
- R-P9.md (packet 9; pin c5e2b4d): (a) SIGN; CHARGE SIGN WITH GAPS (G9-b1 notation P(τ)=P(τ⁺), G9-b2 short visits; G23g-1/2
  checked); depth/counting SIGN WITH GAPS (G9-c1 needs FIRED-R; constant D only); stealonce_viol_n76 confirmed. Tool p9charge.py.
- R-P9 §C: agreement with R2-P9; my N9-a1 WITHDRAWN (R2-P8 §7 was added after I read R2-P8). Lesson: re-fetch a
  referee-2 file before saying a section does not exist.
- R-P10.md (packet 10; pin 1100f3a): ENTRY-CHARGE SIGN WITH GAPS (G10-a1 one prefix convention incl. V=∅ stop; step 2
  fan-out < |R| checked hard: 143/146/165-172), C1/C2/C3 SIGN (C1 = reformulation; N10-b1). Tool p10entry.py.
- R-P10 §C (434a552): agree; fixed σ set accepted; R2 shorter route F_R ≤ 3(X_R+(|R|+1)|R|²) confirmed.
- R-P11.md (packet 11; pin 5909724): CHANGE-NEW SIGN WITH GAPS (N11-a1 STR-DET not needed; G11-a1 threshold via Lemma 1.2);
  corollary SIGN; honest limit: GAP-A ⇔ (CTX⁺) ∧ (FIRED⁺-R) (equivalence). Tool p11probe.py.
- R-P11 §C: agree with R2-P11; R2's N11-b1 confirmed (#e*-at-R ≤ D_R ≤ #fired⁺(R) given STR-DET; H drops out of R9).
  Box done; Lead plans a successor before any further packet.
- Lesson: Lemma 1.2 assumes Q = Z_0; Dom (878-890, 962-991) and bv regions push only the top. Check the push pattern.

## HANDOVER (parked 2026-10-17 ~12:20Z on the Lead's instruction; context ~520k; produced on Opus 5.5 under D12/L33)
Resume point. Successor REFEREE: read CLAUDE.md, docs/NOW.md (Lead session_014FBi6o334DvwT5Uw2kDfoN), then my reports below.
- Push only with scripts/push.sh; redirect its output to a file and print $?. Read the notification queue before every push.
- Rebuild Oink first with scripts/setup_oink.sh (tools/ is gitignored).
- Label every verdict "(Opus 5.5, D12)".
- Do not read docs/referee-2/ for a packet until your own report for it is pushed.
Packets done today (all on claude/referee; every report has a §C comparison with REFEREE-2 where the Lead asked):
- R-STEP5.md (Step 5 of GAP-C; pin 8f41be8): KT, NT-f, FM/WM, (YZ) reading, (YZ)<=(ACYC), P-KT. All signed, gaps closed.
- R-PROVED2.md (packet 2; pin 43d63b0): SCC1, B-thr ("(a) always", F-b3), Theorem A, O0/O1, OPP-EXIT, K0, phases<=D+2,
  FDL, DV*-MONO, LRN budget, (SPP)=>bound. §C/§C5 hold the comparisons. The G-h1 "closed" there is now conditional on
  (STR-DET) (R-P4 §C1).
- R-P3.md (packet 3; pin 6e0082f): K5' and (α) with Up(Str) REJECTED after the comparison (REFEREE-2's configuration;
  my G-a1/G-a2 step was wrong: old tangle vertices keep their region strategy, 169). K5''/(α) with Dep(Str) SIGNED; gap
  G-α1 in R2's ⇔ form. O-P SIGN (given YZ). GAP-A first step SIGN (round r).
- R-P4.md (packet 4; pin 44d1428): S0, PREFIX-MONO, POS-FALL, ROOT-BOUND SIGN. §22e SIGN WITH GAPS with G-e1 (e* in Dom
  via an X-straddle) and G-STR OPEN. §C: G-STR holds; it cannot arise for e* in the root best_vertices call.
Open gaps I hold (for GAPS.md):
- (ACYC) (Step 5).
- G-e1/G-DOM (§22e: first difference in Dom).
- G-STR, i.e. (STR-DET) (FDL alignment and counting after the first sptl).
- (CTX), (DIRTY), (SPP).
- The (α) shape (SKETCH).
- GAP-A beyond round r.
Lessons:
- Twice my set-level arguments missed strategy-level (str) effects: R-P3 (a) and G-STR. When a proof step reasons about
  what a ψ-play or an extraction does, check which line wrote str (89 / 171 / 73) for every vertex involved.
- REFEREE-2 caught both. Its configurations were correct.
Tools (docs/referee/scratch/): step5_probe.py, bthr_probe.py, fdl_random.py (all subclass experiments/alg dtl_pyref/dtl_step5).
- R-P5.md (packet 5; pin f920dc2, 12:36Z): Lemma STR-DET SIGNED (gaps W-a1 wording, G-a2 Case A argued by Dom closure).
  G-STR CLOSED; FDL R5 (h) holds on the reduced log; R-P4 §C's STR-DET condition withdrawn. Open in §22e: (CTX),
  (DIRTY)/(FALL), G-e1/G-DOM.
Nothing in flight (parked again 12:38Z).

## Resume point (successor session, 2026-10-14 ~23:50Z)
I am the successor REFEREE (spawned 23:15Z, replacing the session parked at f179ae0). Lead: session_014FBi6o334DvwT5Uw2kDfoN
(send_message, first line "From REFEREE (<UTC from `date -u`>):"). Branch claude/referee, trunk merged in
(origin/claude/vibrant-johnson-nxvvxo). Push only via `scripts/verify.sh && git push -u origin claude/referee`; Oink built with
scripts/setup_oink.sh (~1 min; rebuild after every restart, tools/ is gitignored).
Tasks done: R-L1 (L-LOWER L1 at 8fcc0f2; CHANGES, 9 findings; report 2026-10-14-L1-statement-check.md, pushed 9b01cbb,
reported 23:43Z) and T-A1 first-referee check (L-ATTR TA1-proof.md at d5d6396, then re-checked at 4478b84 per the Lead's 23:42Z retarget;
then SIGNED OK at 57a1515 (signature block at the end of the report, gaps G1-G11); report 2026-10-14-TA1-proof-check.md; tools
ta1check.py, ta1probe.py). R2's report (docs/referee-2/R2-TA1.md) read only after my derivation; it agrees on every point. T-A1 signed OK at l-attr 57a1515 (G11 answer for the CHECKER appended). R-L1b (L-LOWER v2 + Lemma 2.1' + Theorem B at
l-lower b1abae0): CHANGES with one one-line finding; report 2026-10-15-L1b-check.md; tool l1bcheck.py (types over all
one-player Büchi games n <= 4, exhaustive B_1 lower bounds n <= 3, lane witnesses on my quotient). R-psolC (L-ATTR psolC fidelity, l-attr 02174e2): FAITHFUL, DE3 recordable; report docs/referee/R-psolC.md; tool
psolccheck.py (my own psolC from DTR15-4 Defs 1-2/Thm 1/Fig. 5, full product, both A1 readings). R-TL2 (second referee read of L-RED's transfer lemma, l-red 0d50d4a): OK with fixes; report docs/referee/R-TL2.md; tool
tl2check.py (my own G from FHZ Table 1, my own P, Friedmann valuation, exhaustive over all trees, RF vs RAR lockstep).
Nothing in flight.
Coming (per the Lead's brief): the L1 proof work / experiments/lower from L-LOWER; SL8-min / T3 from L-STRUCT; second referee
for the L4+T3 package is a SEPARATE session, not me.

## Resume point of the predecessor (kept for the record; HANDOVER, parked 2026-10-14 ~21:50Z on the Lead's instruction; context ~680k)
You are the successor REFEREE. Read CLAUDE.md, TARGET.md (v1.0 frozen), docs/NOW.md (Lead session id; it was
session_014FBi6o334DvwT5Uw2kDfoN), docs/agents/LANE-RESTART.md (the five handover-check questions), docs/referee/README.md,
then every report in docs/referee/ (eight so far). Branch claude/referee; push only via `scripts/verify.sh && git push -u
origin claude/referee`; messages to the Lead with the claude-code-remote send_message tool, first line "From REFEREE
(<UTC time from `date -u`>):" (my own first lines drifted ahead of UTC; use the clock). Build Oink first
(`scripts/setup_oink.sh`, ~1 min) so the gate's smoke step runs; `pip install python-sat` for wsepsat.py.
Last actions: L4 (docs/struct/L4-proof.md) signed OK as FIRST referee at claude/l-struct 50dc28b (referee 9bf5301);
handover written (this commit). No work in flight; nothing routed.

State of every claim I refereed (report file in docs/referee/, verdict, status):
| claim | report | verdict | status |
| --- | --- | --- | --- |
| arXiv 2511.03752 v1 (M2) | 2026-10-14-arxiv-2511.03752.md | BROKEN (Theorem 2 false; cex1, cex2) | M2 closed on trunk; AM1-AM9 faithfulness OK |
| L-COMP PGSolver ports (generators, pgsolver_si.py) | 2026-10-14-pgsolver-ports.md | OK; bare SI loop = PGSolver -dgo -dsd -dlo -dsg | done |
| L-LIT T4 §3(c) lasso observation | 2026-10-14-T4-3c-lasso.md | OK, 3 strengthenings, 1 citation nit | done |
| L-COMP gauntlet bench (experiments/) | 2026-10-14-harness-review.md | CHANGES then OK at l-comp e70a2a9 | landed |
| L-STRUCT S1 C1 (w(2,6)=3<4=s(2,6)) | 2026-10-14-S1-C1-weak-separators.md | OK; side claim BROKEN (= plant P1); Lemma 2(b) CHANGES | findings to L-STRUCT |
| L-STRUCT S2 (T1/T2) + L-COMP T1 refutation | 2026-10-14-S2-statement-check.md | T1 REFUTED at (2,10), verified; T2 CHANGES | findings 1-4 to L-STRUCT |
| L-STRUCT S3 (diagonal, T3, L4, H1) | 2026-10-14-S3-statement-check.md | CHANGES, all applied (a67bd78); delta OK | done; T3 proof not yet seen |
| L-STRUCT L4 proof | 2026-10-14-L4-proof-check.md | CHANGES then OK, first referee, at 50dc28b | awaits SECOND referee |
| L-LOWER L1 statement (SLP model, Lemmas 1.5/1.6/2.1/2.3, Transfers 2.2/2.4, T-L1) | 2026-10-14-L1-statement-check.md | CHANGES (9 findings: d vocabulary, game-class corner, Lemma 2.3 rests on unproved Remark 2.5, cited experiments/lower absent at 8fcc0f2, ω(n) gloss weaker than ω(n), 3 model differences, nits) | findings to L-LOWER via Lead; every re-derived claim holds |
| L-ATTR T-A1 (psolB complete <=> PA**; PA** => psolQ complete; Cor. 1-2, Prop. 3) | 2026-10-14-TA1-proof-check.md | CHANGES (theorem and both proofs hold; at 4478b84 open: F1 misstated, T-A1' needs HKP Thm 4, Büchi recolouring, 'stable' gloss); first referee | SIGNED OK as first referee at l-attr 57a1515 (all findings applied; G1-G11 listed, G10 open as HKP dependency) |
| L-LOWER L1 v2 + Lemma 2.1' + Theorem B (b1abae0) | 2026-10-15-L1b-check.md | CHANGES (findings 1-9 applied; Lemma 2.1' OK; Theorem B OK, Claim 3 misses the case t<t'<a; B_1(1..4) = 0,2,4,6 confirmed independently) | findings to L-LOWER |
| L-ATTR psolC fidelity (DTR15-4; 02174e2) | R-psolC.md | FAITHFUL (A1: literal reading is the chapter's; Example 3 (ii) is a slip; instance and tc N=2 undecided under both readings; 3 nits) | DE3 can be recorded |
| L-RED transfer lemma (FHZ G_{n,r,s,t} RF = RAR on sink parity P; 0d50d4a) | R-TL2.md | OK with fixes (lemma true; case (2) misses the chain-vertex sub-case; loose constant in (1)/(3); S1 tie/start conditions to cite); second referee | RESULTS candidate if R2 agrees; L-LIT novelty + CHECKER |

## Queue / open items
- L4 second referee (not me; a second, independent referee): the gap list G1-G6 in the L4 report is the checklist. What
  the second referee must re-derive: Lemma L4.1 (a)-(d) (Parys-Wiacek conversion H', words p.w, cycle multisets,
  q1 = delta(q0,1) != bottom via 1.2^w, A' = (Q,q1,delta)), L4.2, the chain in Theorem L4, the constants of L4.3
  (d' = 2 floor(sqrt n /2), a0, b0; the fixed step uses floor >= ceil - 1), L4.4's class (i)-(iii) from S2 §3(c), and the
  black-box use of CDFJLP Thm 5.1 (E convention, non-rejecting states, deterministic ⊆ non-deterministic, binomial form
  needs no side condition). My S3 "delta" section records the alternative split-G_t route, not written up.
- Coming (per the Lead): SL8-t and T3 (S3 §2: w^V(n,d) = s^V(n,d) for 1 <= d <= n+1). For T3: cells I confirmed with my
  own SAT: (1,1), (2,2), (2,3), (3,3), (3,4), (4,4) all w = s; obstruction to "prune the even-used part": the committed
  weak_V_n3_d3.json has an odd cycle among its even-used transitions (my check, S3 delta); route R2's L5' must be about
  all paths P and all foldings (S3 §4b). A (4,5) V or (5,5) V cell with w < s would refute T3; my enumeration is too
  slow for n = 5 (use L-COMP's LRAT-checked cells, then verify any SAT witness with wsepref.py over all graphs).
- Minor, not routed: diff of the PGSolver ports against the real binary with -dgo -dsd -dlo -dsg (owner Q4);
  s^V(4,6) = 10 (L-STRUCT) and w^E(4,6) >= 8 (L-COMP, LRAT) are not re-verified by me.
- Findings I routed whose application I have not seen: S2 findings 1-4, S1 findings 1-3 (Lead said L-STRUCT has them),
  T4 finding 4 (CDFJLP multiplicity wording, to L-LIT), ports cosmetic nits (to L-COMP).

## My tools (docs/referee/scratch/; all throwaway, run with `python3 -I`; every SAT answer is re-checked by brute force)
- aiayn.py: faithful implementation of 2511.03752 Algorithm 1 under all 16 readings of its ambiguities, a min-parity
  Zielonka, .pg read/write with min<->max conversion, random counterexample search. `--pg FILE --trace`, `--all-readings`,
  `--search N`. cex1-/cex2-minparity.pg are the counterexamples (paper's convention); *-maxparity.pg are the twins for
  Oink/PGSolver; *.sol are Oink's verified answers (Even wins all four vertices on both).
- harness_faults.py: four planted-fault solvers (winner swap, strategy leaving region, in-region losing cycle, min-parity
  convention) run through L-COMP's compare.py; needs a checkout of experiments/harness.
- sitest_run.py: execution check of pgsolver_si.py / pgsolver_port.py against Oink (paths point at my scratchpad; adjust).
- wsepref.py: brute-force checker for weak/strong (n,d)-separators (S1 D1-D5) over ALL graphs: conventions V (any small n),
  S (n <= 2 cheap, n = 3 is 7^9), E (n = 2, d = 6 via graphs_E2); prune, cycle_class, accepts_all (W1), rejects_all (W2),
  strong_S2 (S2); CFGO universal-tree recursions f_upper/g_lower. CLI: `witness n conv [strong]`, `json FILE n conv`,
  `utrees`, `k2` (all 531,441 two-state automata, V, n <= 2, d = 6).
- wsepE2.py (d = 6: all 16,777,216 edge-labelled multigraphs on 2 vertices, several automata at once) and wsepE2d.py
  (any d: all (A,B) cross-label-set pairs with saturated same-parity loops; sound by monotonicity of W1/W2).
- wsepsat.py: my own SAT encoding (pysat CaDiCaL 1.5.3; one-hot transitions, closure variables per graph, thermometer
  ranks for W2 and for S2 on all states, no symmetry breaking) over inclusion-maximal even/odd graphs computed by brute
  force (V: one labelling per vertex-permutation orbit; S). `wsepsat.py n d V|S weak|strong k`. Timings: n <= 3 seconds;
  n = 4, d = 4: ~11 min per cell (enumeration dominates), weak k = 6 took 24 min; n = 4, d = 6 strong k = 6 timed out at
  25 min. Independent of L-STRUCT's wsep/ and L-COMP's sat-hard/; agreed with both on every cell all ran.
- slpcheck.py (R-L1): Zielonka reference solver on bitmask games (max-parity, vertex priorities), SLP interpreter (gates
  P p | VE | EMPTY | OR | AND | NOT | CPRE; cost = CPRE count, depth), Lemma 2.3's program literally, the textbook Büchi program,
  n-fold Kleene unfolding of the nested fixpoint with g (vertex priority) or f' (successor priority, Remark 2.5), and ANP's
  symmetric recursion ||F||_{U,V} built as a gate list with S_{n,h} / C_{n,h} trees (outermost θ_d acts on the LAST argument;
  f^z substitutes the last ?). Exhaustive games for n <= 3, one-player n = 4; random beyond. `python3 -I slpcheck.py [quick]`;
  full run ~15 min. A non-universal tree makes ANP fail (sanity). All lane programs: 0 mismatches.
- ta1check.py (T-A1): my own psolB/psolQ from HKP Figs. 3/5 in MIN-parity colours (colour = M - pr), my own PA** in
  max-parity (exhaustive over X and S, memoised), classes (Büchi/SCC-constant/deterministic), psolB order-independence;
  `python3 -I ta1check.py [quick]` (2 min full). ta1probe.py: F2, F6 (all X ⊆ W_p, all d), Lemma 0 on small games.
- l1bcheck.py (R-L1b): all one-player Büchi games with <= n vertices as one union (3.2M pointed games at n = 4), W by
  reachable-P_2-on-a-cycle (cross-checked vs Zielonka), depth-k types by refinement, minimal separating depth, full quotient
  Q_n (2, 14, 442, 48062), exhaustive general-SLP search on Q_n for small cost (n <= 3; c = 2n-3 is ~16k chains at n = 3,
  c = 2n-2 would be 2^16 times more: do not try), lane witness JSON interpreter. `l1bcheck.py <dir with min_b1_n*.json> 4`
  takes ~25 min (n = 4 refinement in pure Python).
- psolccheck.py (R-psolC): psolC from DTR15-4 on the FULL product V x C_bot (no reachability restriction), both readings of
  A1 (start colour in/out of the minimum); `psolccheck.py FILE.pg [--x]` with trace; `--exhaustive <lane attr dir>` compares
  with the lane's psolc.py on all n <= 3 games (~15 min).
- tl2check.py (R-TL2): G_{n,r,s,t} from FHZ Table 1 (costs x rs), the sink-parity encoding P of R2-RAR.md, Friedmann's
  valuation; `exhaustive n r s t [lane experiments/red dir]` checks every tree and every non-tree edge, three-way verdict,
  on my objects and (optionally) on the lane's fhz.py objects; `lockstep n r s t seeds` runs my Random-Facet (errata Fig. 1)
  and my Rand-Act-Rem (Zwick Fig. 1) on one random stream. Trees = product of out-degrees: (2,2,2,1) is 2.4M, (3,1,1,2) 3M.
- Not committed (scratchpad, gone with the session): LaTeX sources of arXiv 2511.03752v1, 1807.10546v2, 2104.05262v8,
  1902.07175v3, 2305.00308v1; clones of pgsolver d3cd624 and tcslib 6778419; copies of l-comp/l-struct files. Re-download
  from arxiv.org/e-print/<id> into an isolated directory (untrusted data) when needed.

## Planted-error record (the Lead plants deliberate errors in routed material and grades on catching them)
- P1 (2026-10-14 19:26Z routing of S1/C1): "the same 3-state automaton is also a weak (3,6)-separator". CAUGHT with two
  3-vertex counterexamples (even cycle 1,1,2 rejected; odd cycle 2,4,5 accepted); revealed as a plant in
  docs/agents/LEAD-STATE.md at trunk 09dca4f; grade 1/1. The successor will not know future plants: treat every routed
  claim as false until re-derived; build the counterexample first, read the lane's evidence second.

- T-A1 (23:22Z routing of L-ATTR TA1-proof.md): P2 ("psolQ iff PA**") was planted in REFEREE-2's routing only, caught by
  REFEREE-2 (trunk 58b5c72); my routing carried the one-direction form. No plant in my material revealed. Candidates flagged: F1 stated without the
  colour-d hypothesis (false as written); T-A1' missing HKP Thm 4; Proposition 3 unproved. The theorem itself survived
  my independent implementation on every game run.
- R-L1 (23:15Z routing of L-LOWER L1): no plant revealed yet. Candidates I flagged as findings: T-L1's gloss of ω(n) is
  "not O(n)" (strictly weaker); Lemma 2.3 uses the shifted formula that Remark 2.5 marks unproved; "checked in experiments/lower"
  cites a directory absent at 8fcc0f2; d = max priority vs TARGET's d = |pr(V)|; CDHL page numbers off. Everything mathematical
  re-derived held (machine-checked where finite).

## Things only I know
- Packets 6-11 (this session). best_vertices is a function of (R, p, T, order datum) within a phase: state it reads is listed in
  R-P11 (a). str is never read for a set decision (73 only guards a write). this->G read only at 132, changed only at 1035.
- Which closure is which: Lemma 1.2 (DTL-proof) needs Q = Z_0 (all pushed): threshold loop (724) and −1 attractor (909) qualify.
  bv region steps and Dom steps push only the top: region = Cl over T \ E_τ (EXACT); Dom = closure triggered by the new part,
  NOT monotone in its base (R-P6 G6-b1).
- Cross-visit counting: e*-pairs are NOT consecutive visits (a context can recur within a search). Use the endpoint device
  (R-P7 §C2): along e*-endpoints T is non-decreasing, and overlaps lie where T is constant (STR-DET (c)).
- Visit alignment: missing rounds = repeat last round after "no candidates" (716/765), empty after V=∅ (768-771); steps range
  over ALL p-vertices τ of R (R2-P10's fixed σ set).
- Probes p6..p11 in docs/referee/scratch/ subclass experiments/alg/dtl_pyref.DTL and need experiments/dtl-bench on sys.path
  (stdsort). My pyref internal ids differ from dtl_rootmono's (e.g. tops 31/74 vs 18/66 on stealonce_viol_n76).
- Corpus I used: experiments/alg/instances (138 files); full runs take ~5-10 min per order per probe; run both orders in the
  background with until-loops on the output file (pgrep -f matches its own shell).
- R-TL2: FHZ's "zero-edges" are the COSTLY edges (superscript 0 = counter bit 0); B_0 = any tree of them. The transfer lemma
  needs only B and e, not F. The one real structural fact: before merging, the two prefixes sit at u_i and w_i (the only
  entry points) at every level; equal classes from one vertex land on one vertex (merge), so a tie at the divergence level
  ends the comparison, and the (C_u, C_w) small-offset difference can occur only at the merge level. P has priority-0
  vertices below the sink, so Friedmann's 1-sink identity "length = |path set|" does NOT hold in P; lengths are compared
  separately and ties need the relay-per-copy design.
- R-psolC: DTR15-4 (sha256 a7b61fe3...9cd6) is min-parity; Example 3 step (ii) drops the start colour from the prefix minimum,
  contradicting Def. 1, Def. 2, Thm 1's proof and Lemma 2's proof (all include it). Both readings are sound; literal decides
  more. psolc_min_n4_m6.pg: Odd wins all, psolC's player-1 fixpoint goes {v0,v2,v3} -> {v2,v3} -> {v2} -> {} under both
  readings; the parity of the decisive minimum (2 at v0 via v1) is the same with or without the start colour.
- R-L1b: minimal program depth on one-player Büchi is exactly 2n-2 for n <= 4 (my types), Theorem B gives 2n-1; B_1(4) = 6
  follows from Lemma 2.1' + the lane's witness without any SAT. The exhaustive chain search is fully general for SLPs.
- T-A1: F6's equality MAttr^{G'}(X,d) = MAttr^{W_p(G')}(X,d) holds for EVERY X ⊆ W_p (q keeps the play in W_q), not only
  fatal X; the "only if" needs only W ⊆ R from F1. L1's rank induction has no rank 0 (X external). T-A1' silently needs
  HKP Thm 4. The "if" proof is order-free, so T-A1 holds for psolB under any colour order. HKP Fig. 4(a) edges (from the
  png): v0↔v1, v1↔v2, v2↔v3, v3↔v4, colours 3,2,0,2,3, squares v1, v3. PA ⊆ PA* has no proof anywhere (data only).
- R-L1: ANP's recursion ||F||_{U,V} is straight-line; Lemma 3.6 (worklist) is adaptive; a Jacobi round-robin on Algorithm 1's
  |V| equations is non-adaptive at |V|(1 + n|V|) queries. CDHL's O(1)-bit step for Reduction 3.9 is NOT in their text (they
  say "same argument as Theorem 3.2"); it is one bit per party about the loop at v_max (Pre) / v_min (Post). CDHL printed
  page = physical page − 1. ANP cite Emerson–Jutla 1991 ([10]) for "Expression (1) = winning region". The shifted Büchi
  formula νZ.μY.Cpre((P_2∩Z) ∪ (P_1∩Y)) is correct (rank argument in the report §3) and exhaustively checked for n <= 3.
  The matrix-vector query model (Sun–Woodruff–Yang–Zhang ICALP 2019, arXiv 1906.05736) is the adjacent framework nobody in
  the fleet has opened; with named singleton queries n queries read the adjacency matrix, so ω(n) must come from anonymity.
- 2511.03752 is MIN-parity; PGSolver/Oink are MAX-parity; convert p -> M - p (M even >= max p). On cex1 the max-parity
  reading of the same numbers coincides with the algorithm's wrong output: never check a min-parity run against Oink on
  the unconverted file. The paper's theorem numbers follow a shared counter (Lemma 1 Zielonka, Theorem 2 dominion,
  Lemma 3 minimal dominion, Lemma 4 progress, Theorem 5 correctness); the false sentence is tex:332.
- L-COMP's strategy-improvement port is the bare loop = PGSolver with -dgo -dsd -dlo -dsg (pgsolver.ml:102-116), not the
  default binary with universal_solve preprocessing; any M1 sentence quoting PGSolver counts must say so.
- CDFJLP (1807.10546v2): Thm 5.1 is an E-convention theorem (G_t has one self-loop per even priority at each vertex),
  counts non-rejecting states (tree decomposition on non-rejecting states; leaves inject there), and its binomial form
  comes from Thm 2.3 "for all positive integers" with no side condition; the "d <= n" is only for the closed form. The
  embedding claim (§5) uses only a run on alpha_t avoiding rejecting states plus the tree decomposition from strongness.
  CDFJLP never fixes whether parallel edges may carry distinct priorities (T4 finding 4). CFGO (2104.05262v8): Thm 4.1 =
  saturation.tex thm:main; parity §6 lemma numbering: 6.1 (line 13), Thm 6.2, 6.3 (68), 6.4 (145), 6.5 (165), 6.6 (197),
  6.7 (225), 6.8 (266), Thm 6.9 (287), Prop 6.10 (304), Prop 6.11 (374); universal-tree sizes f = g: (2,3) 4, (2,4) 5,
  (3,3) 7, (4,2) 8, (4,3) 13. KV (1902.07175v3): alphabet (vertex, priority), eventually-always q_accept, graphs = S
  convention, Thm 2 time-bounded.
- S1 Lemma 2(b) repair differs by convention: E = self-loop labelled 2 at the end of the non-zero part; V = fresh vertex
  labelled 2 (a 0-vertex was removed), n >= 2.
- T1 (one tree level) died at (2,10): w = 4 < 5 = s(2,8) in E, S, V (my exhaustive checks); it held at (2,6), (2,8) and
  L-COMP's w^E(4,6) >= 8 supports it there. The weak < strong cells all have d >= n+3.
- The probe automaton that exhibits the restriction dead end for (3,6) V (6 states, odd cycle of maximum 3) is listed in
  the S2 report §5; the committed weak_V_n3_d6.json is NOT such an instance (its restriction to Sigma_4 is strong).
- My timestamps in messages to the Lead ran ahead of UTC (I estimated instead of reading the clock); the SHAs are the
  record. L-STRUCT had the same issue (S3 §5).
- The split-G_t observation (S3 delta, finding 8): one copy per out-letter gives c = d and monotonicity in d then gives
  L4; L-STRUCT used L-LIT's Claim R instead (same bound form). If a self-contained proof is ever wanted, that is the route;
  I did not write it (referees do not write proofs for lanes).

## Sources opened
| source (arXiv id / DOI) | result used (theorem / section) | opened on | note |
| --- | --- | --- | --- |
| arXiv:1410.7530 (FHZ, Random-Facet shortest paths; LaTeX source + PDF) | Table 1 + zero/one-edge convention (Actual-Construction.tex 28-66, 101-104), B_0 (144-152), Def. functional (156), Def. B_F (234), RF pseudocode and shortest-path reading (RandomFacet.tex 47-50, 70-86, 181-195), Thm 6.3 = thm:main (Lower-RandomFacet.tex 118-142), parameters (706, 760-763), introduction.tex 24-26, abstract | 2026-10-15 | R-TL2 |
| arXiv:1410.7871 (FHZ errata) | §1 (RF vs RF*, "main result of [1] flawed", RF* bound stands), §2 Fig. 1 pseudocode, p.4 "similar examples for parity games" | 2026-10-15 | R-TL2 |
| arXiv:2607.06334 (Zwick, Rand-Act-Rem) | §2 AUSO and orientation, §3 VAL and improving switch, Appendix D Fig. 1, related work p.~1040 | 2026-10-15 | R-TL2; PDF |
| arXiv:1106.0778 (Friedmann, LMCS 2011) | §3 node valuations (set order by max of symmetric difference; length order by cycle-node parity), §5 1-sink games and Lemma 5.1 | 2026-10-15 | R-TL2; PDF |
| Imperial DTR 2015/4 (HKP, psolC; sha256 a7b61fe3...9cd6) | §2 p.3, Def. 1 p.4, Def. 2 + Thm 1 pp.5-6, Cor. 1, Lemma 2 + proof, (2), Lemma 3, Fig. 4 remark, Fig. 5 p.9, Thm 2 pp.8-9, Example 3 + Fig. 6 pp.10-11 (rendered), Thm 4 p.12 | 2026-10-15 | R-psolC; MIN-parity; PDF via pdftotext + pdftoppm |
| arXiv:1405.0386v2 (HKP, Fatal Attractors) | archiv.tex/PDF: §2, Defs 1–8, Thm 1, Thm 2 + proof, Lemma 1, Fig. 3 (tex:728–747), Ex. 5 + Fig. 4(a) png, Def. 6 (tex:942–948), Fig. 5 (tex:970–997), Thm 4 + proof, Thm 5, Thm 6 statement, Thm 7/8 + proofs, Lemma 5 + proof, external-target remark tex:528–536 | 2026-10-14 | T-A1; MIN-parity |
| arXiv:1711.09148v1 (CDHL, SODA 2018) | arxiv.tex: §2 model 466–517 (Thm 2.1 th:lbdisj), Reduction 3.9 red:buchi 759–765, Thm 3.10 thm:buchi 803–814 and proof 1223–1241, Lemma 3.4 lem:scc2 615–665, Prop 4.2 lem:objectives_ub 1023–1044, intro 284–286 ("2n one-step operations"); theorem numbering from the shared counter, confirmed in the PDF | 2026-10-14 | R-L1; LaTeX source + PDF, isolated dir |
| LIPIcs.CSL.2021.9 (ANP, DOI 10.4230/LIPIcs.CSL.2021.9) | §2 (f_{A,B}, trees, Prop 2.5), §3.1 cases (1)–(3), Lemmas 3.1, 3.2, Remark 3.3; §3.2 Algorithm 1, Lemmas 3.4–3.6, Cor 3.7; §3.3; Thm 5.1; Remark 5.5; intro p.9:2–9:3 ([10] Emerson–Jutla for Expression (1) = winning region) | 2026-10-14 | R-L1; DROPS PDF via pdftotext |
| arXiv:2305.00308v1 (Parys–Wiącek) | improved-parity.tex lines 86-87 (edge-to-vertex priority conversion remark), 368 (necessity proof does not apply) | 2026-10-15 | LaTeX source; L4 attribution quotes |
| arXiv:2104.05262v8 (CFGO, LMCS 2022) | preliminaries (graphs, automata, neutral letter), reductions (separating automata, universal graphs), saturation Thm 4.1, parity §6: Lemma 6.1, Thm 6.2, Lemmas 6.4-6.8, Thm 6.9, Props 6.10/6.11 | 2026-10-14 | LaTeX source; S1 conventions and F2 |
| arXiv:1902.07175v3 (Kozachinskiy-Vyalyi) | §1.2 separation approach, §2.1 separation automata and game graphs, Thm 2 | 2026-10-14 | LaTeX source; S1 F5 / Lemma 3 |
| arXiv:1807.10546v2 (Czerwiński et al., universal trees inside separating automata) | the-separation-approach.tex (languages of play encodings; safety automata; (n,d)-separators, strong separators); intro.tex 161-166 (separator) | 2026-10-14 | definitions for the T4 §3(c) check; LaTeX source |
| github.com/tcsprojects/tcslib 6778419 | src/data/tcsgraph.ml 8-226, tcsset.ml 132-166/284-287/426, tcslist.ml 35-42, tcsarray.ml 48-52, tcsbasedata.ml 181-227 | 2026-10-14 | helpers used by stratimpralgs.ml |
| github.com/tcsprojects/pgsolver d3cd624 | solvers/stratimpralgs.ml 54-199, 441-669, 693-696; solvers/switch_globally_best.ml 1-119; paritygame/transformations.ml 271-320, 338-413; paritygame/univsolve.ml 23-66, 267-780; apps/pgsolver/pgsolver.ml 102-116 | 2026-10-14 | strategy improvement originals of pgsolver_si.py |
| github.com/tcsprojects/pgsolver d3cd624 | recursiveladder.ml 13-46; policyiter/generators/switchallexp.ml 30-66, switchbestexp.ml 34-74; policyiter/stratimprgenerators.ml 7-47; paritygame.ml 19, 25-40, 128-139, 175, 201-206, 365-387 | 2026-10-14 | OCaml originals of L-COMP's ports; cloned into scratchpad |
| arXiv:2511.03752v1 | whole paper: Sec. 2 defs, Sec. 3 (A*, A', A^k, Thm 1, Lemma 2, Alg. 1, Lemma 3, Thm 4, 5, 6) | 2026-10-14 | PDF + LaTeX source (main.tex); 4 pages; only v1 exists |

## Dead ends
(none)
