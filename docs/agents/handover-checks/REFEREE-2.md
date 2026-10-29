# Handover check: REFEREE-2

## successor 6 (2026-10-25T01:33Z by date -u; Opus 5.5 under D15/L37; predecessor successor 5 session_01VbMVVvPYCY47wY5MbtLG8w, handover d6093b3a)
Measured from the repository at the time of writing (commands named), not recalled.

### 1. Branch, head, distance to trunk
- Branch `claude/referee-2`. The container's local branch was STALE (77f9cf71, 1369 behind origin). After
  `git fetch origin claude/referee-2 claude/vibrant-johnson-nxvvxo` and `git merge --ff-only origin/claude/referee-2`:
  HEAD = origin/claude/referee-2 = d6093b3a (predecessor's handover commit).
- `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` -> 0 ahead, 26 behind (trunk 361d18ca;
  merge-base d6093b3a, so all REFEREE-2 work is on trunk). I then merged trunk with a merge commit (8bae1c67): 1 ahead, 0 behind;
  this file's commit adds one more. 361d18c is also the pin of my first packet.

### 2. Open work and next step of each
- Nothing in flight (predecessor parked 01:28Z after R2-N5-LP + §8 SO + combined §C caee2aec).
- NEXT (after GO, orientation only): packet P-N5-OE, docs/new/P-N5-OE-box32.md, sha1 adeccd898ad1e4de6532fc3a77a9d600d8a0bc16
  (sha1sum of the trunk blob; added by L-NEW db35220e), pin trunk 361d18c: Lemma U-loc, Lemma OE, Corollary OX.
  Next step: read the packet, N5-ssi-global.md S1-S5 and every signed result it cites (R19-R26, R2-N5-LP for DF/DF′); build my own
  checker on R2-N5-RE/re_check.py + R2-N5-LP/lp_check.py with the one-Odd-choice assert; run the packet instances, the library
  sweep, then climbs. Output docs/referee-2/R2-N5-OE.md. docs/referee/ has no OE report on this tree; I do not read one before mine.
- Open question held for the Lead (predecessor NEEDS): whether P-N5-SO needs a fresh independent second review (successor 5's
  R2-N5-LP §8 exists and stands). Fix routings (DF → DF′, G-LP-1/2, N-LP-1, G-SO-1, N-SO-1..3, G-U23-1, G-FB-1..4) are the Lead's.
- Oink is NOT built in this container (tools/oink/build absent): run scripts/setup_oink.sh before any zlk cross-check.

### 3. docs/GAPS.md rows relevant to me (trunk 361d18c)
- REFEREE-2 owns no row.
- G-N5-TIME | major | L-NEW (L-LIT T22; referees later) | open: N5 makes polynomially many iterations. Latest: R26 landed 00:48Z
  (CASC-U2/U3); P-N5-LP (Theorem LP, Corollary LP′: phase O(m n⁵ (1 + S_o + X + K)) on 𝒞^1O) refereed; S_o, X, K OPEN.
  P-N5-OE (Corollary OX: phase O(m n⁵ (1 + X + K)), J ≤ X) is the packet under this row.
- G-N5-TERM closed (R15). GAP-A, G-S5-6, G-NEST, G-N1-LB not routed to me.

### 4. Three owner rulings that most constrain me (verbatim), with DECISIONS-INDEX status
1. D1 (index: active), docs/DECISIONS.md:7-8:
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never downgrade the referee to save money.
2. D15 (index: active; Lead reading L37 active, signatures labelled "(Opus 5.5, D15)"), docs/DECISIONS.md:278:
   > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
3. D18 (index: active; Lead reading L40 active: labels PROVED / CONJECTURE / OPEN), docs/DECISIONS.md:333:
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.

### 5. One trap that bit this lane, and the check that prevents it
- Trap (R2-N5-LP, R15 side finding): packets cite VJ00 Lemma 5.8 "maximum ⇒ no improvement" / "σ̄ minimises" at every Odd vertex,
  but SPEC's σ̄ at an own cycle node is FIX 2's DFS choice, where 2 ⇒ 3 ⇒ 1 is FALSE (DF NOT SIGNED, df_cex.pg n 5).
  Check: every such citation in P-N5-OE gets the side condition "not its own cycle node" (DF′: λ(y) ≠ y) checked in the text and
  asserted per state in my checker; every 𝒞^1O probe asserts exactly one Odd vertex with out-degree > 1.
- Also this session: the local branch was stale (77f9cf71); checked `git rev-parse HEAD origin/claude/referee-2` equal after fetch.

## successor 10 (2026-10-25T16:15Z by date -u; Opus 5.5 under D15/L37; predecessor successor 9 session_0163ejRshYhYxVW2CD2XUEB2, handover c74648b6)
Measured from the repository at the time of writing (commands named), not recalled.

### 1. Branch, head, distance to trunk
- Branch `claude/referee-2`. Local branch at container start was STALE (`git status`: 2265 behind origin).
  `git fetch origin claude/referee-2` then `git checkout -B claude/referee-2 origin/claude/referee-2`;
  `git rev-parse HEAD origin/claude/referee-2` -> both c74648b6 (the handover commit). `git log --oneline c74648b6..origin/claude/referee-2` -> empty
  (no late push from the predecessor at 16:14Z).
- Trunk claude/vibrant-johnson-nxvvxo (docs/NOW.md:15) at e05382f4. `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo`
  -> 4 ahead, 46 behind (merge-base b1038bea = R2-N5-LV, merged by trunk 3ef67f44).
  The 4 ahead, NOT on trunk (`git merge-base --is-ancestor` each -> no): fe3c098b (merge trunk), cf54523b (R2-N5-ENT §C addendum),
  37e55fde (R2-N5-PFZ), c74648b6 (handover).
- `git merge --no-ff origin/claude/vibrant-johnson-nxvvxo` -> 90262e03 (no conflict): 5 ahead, 0 behind. This file's commit adds one.

### 2. Open work and next step of each
- P-N5-LV2 (docs/si/P-N5-LV2-box12.md): `sha1sum` -> 3b23a41f…b03; same at pin 283bcb6 and at trunk e05382f4. Not started by successor 9.
  - Lead's ask: check the lane's claim (l. 60-65) that N-LV-1 / N-LV-2 are not inherited. Read so far: l. 63-65 say STRETCH_{-1} is
    used only for k < e; §4 (iii) (l. 141-143) and §7 (2) (l. 209-211) use s := f_1 (g_1), e := f_{N-1} + 1 (g_{N-1} + 1).
    Next step: find where LV2 proves COARSE_{-1}(Ξ) constant on [s, e] for that e (the STRETCH_{-1} hypothesis, one step past f_{N-1}),
    then check the 8 statements (STALE-GATE, EV-G, ENT-X_{-1}, LV-PL', SAND, FLAT-ALL_{-1}^{none}, LV-NONE, SCOPE-FB), checker on
    R2-N5-LV/lv_check.py (already reaches u* = none (LV) states). Output docs/referee-2/R2-N5-LV2.md. Depends on R40 (P-N5-ENT, landed
    48bb74ce) and P-N5-LV (signed by both; not yet a RESULTS row as far as I have read).
  - Independence: `git ls-tree -r --name-only origin/claude/vibrant-johnson-nxvvxo docs/referee | grep -i LV2` -> empty. Not opened.
- §Cs for NEB and LV: DONE by successor 9 AFTER its handover. My first scripts/push.sh (16:1xZ) got VERIFY PASS, then
  "! [rejected] (fetch first)": `git fetch origin claude/referee-2`; `git log HEAD..origin/claude/referee-2` -> a802ef3c (merge trunk) and
  a769ff54 (§C NEB vs R-N5-NEB 40adbf1c, §C LV vs R-N5-LV 8054da2f: identical verdicts, empty gap maps; NEB-N1..N3, LV-N3 accepted;
  LV data difference: u* = none reached by successor 9's climbs). Commit stamps 16:11-16:12Z but absent at my 16:14Z fetch (pushed
  later, or stamps ahead). Merged --no-ff, no conflict. So no §C for NEB/LV is open. PFZ: no REFEREE report on trunk yet; §C PFZ
  when it lands (my R2-N5-PFZ 37e55fde rides this push).
- P-N5-PFZ-ext (docs/new/P-N5-PFZ-ext-box39.md): `sha1sum` -> b3702b1b…d2a; same at pin c61ecc4. To sign: P-FREEZE′, θ-LEN,
  BRK-POLY′. Not started (predecessor's 937535e5, a second late push, merged --no-ff). Lead wants it as a new section of
  docs/referee-2/R2-N5-PFZ.md. Next step: read it; base checker R2-N5-PFZ/pfz_check.py theta_run(), keyed by P(θ) (lane's PFZ_KEY=P).
- Added to LV2 by the Lead (via 937535e5): count r = -1 THR in-scope fallbacks PER SCOPE RUN on the u* = none climbs, to test LV-NONE
  (<= n·n_E + 1 per scope run) and SCOPE-FB; lv_check.py needs a per-run maximum (mxu()).
- Predecessor NEEDS (Lead routes N-NEB-1..3, N-PFZ-1..3 to L-NEW; N-LV-1..3 to L-SI; u* = none witness to L-RED): Lead's. NOW.md:34
  shows L-SI 8 GO'd on "LV-NONE / SCOPE-FB on REFEREE-2 u* = none climbs", so N-LV-3 reached L-SI.
- Oink not built in this container (`ls tools/oink/build` -> absent); scripts/setup_oink.sh started 16:14Z.

### 3. docs/GAPS.md rows
- `grep -n 'REFEREE-2\|G-N5-TIME' docs/GAPS.md`: REFEREE-2 owns no row. Relevant: G-N5-TIME | major | L-NEW | open (docs/GAPS.md:11),
  latest update R40 LANDED (P-N5-ENT): open items include level -1 (P-N5-LV signed by both; LV2 = my in-flight packet), out-of-scope
  fallbacks, NJB's straddle; NL= FALSE (L-RED nleq_cex_n48).

### 4. Three owner rulings that most constrain me (verbatim), with DECISIONS-INDEX status
1. D1 (index line 5: active), docs/DECISIONS.md:7-8:
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never downgrade the referee to save money.
2. D15 (index line 26: active; L37 line 27 active: label "(Opus 5.5, D15)"), docs/DECISIONS.md:278:
   > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
3. D18 (index line 32: active), docs/DECISIONS.md:333:
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.

### 5. One trap that bit this lane, and the check that prevents it
- Trap: a packet's "we only use X for k < e" can still need X's hypothesis one step past the last counted fallback (N-LV-2 was
  exactly STRETCH_{-1} at k = e). LV2 §4 (iii) / §7 (2) set e := f_{N-1} + 1, so STRETCH_{-1} needs COARSE_{-1} constant up to
  f_{N-1} + 1, i.e. across fallback f_{N-1} itself. Check: write the hypothesis instance out with the packet's own s, e and find the
  line that proves it before signing; assert it per state in the checker (count every (s, e) where it fails).
- Also (recurring, prevented this time): stale local branch (2265 behind) and unmerged predecessor commits; checked with
  `git rev-parse`, `git log c74648b6..origin/claude/referee-2`, and `--is-ancestor` against trunk (3 report commits were not on trunk).
  It bit anyway: the predecessor's a769ff54 arrived after my fetch (item 2). Check now: re-fetch and `git log HEAD..origin/claude/referee-2`
  immediately before every push.sh, and read a rejected push as "the branch moved", never retry blind.

## successor 11 (2026-10-25T18:1xZ by date -u; Opus 5.5 under D15/L37; predecessor successor 10 session_012VrKctzqedu9x1gVAMchV7, handover cd3b7cd0)
Measured from the repository at the time of writing (commands named), not recalled.

### 1. Branch, head, distance to trunk
- Branch `claude/referee-2`. Local branch at container start was STALE (`git status`: 2474 behind origin).
  `git fetch origin claude/referee-2`; `git checkout -B claude/referee-2 origin/claude/referee-2`;
  `git rev-parse HEAD origin/claude/referee-2` -> both cd3b7cd0 (the handover commit). No late predecessor push at 18:11Z.
- Trunk claude/vibrant-johnson-nxvvxo (docs/NOW.md:15) at e6ee6130 (`git fetch` 18:11Z).
  Before merge: `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` -> 5 ahead, 8 behind (merge-base 7841c347).
  `git merge-base --is-ancestor`: a551debf (R2-N5-LV2) and 78896bfc (R2-N5-PFZ §X) ON trunk; 269ae45a (R2-N5-RHO), f2209fa4 (LV2 block
  witness addendum), c2c326c7, cd3b7cd0 NOT on trunk.
- `git merge --no-ff origin/claude/vibrant-johnson-nxvvxo` -> b93966b0 (no conflict): 6 ahead, 0 behind. This file's commit adds one.

### 2. Open work and next step of each (queue order from the handover, re-checked against trunk)
- §C PFZ (main + ext). My reports: R2-N5-PFZ.md §1-§6 (37e55fde, succ. 9) + §X (78896bfc, succ. 10), both pushed, so REFEREE's
  docs/referee/R-N5-PFZ.md may now be read. On trunk: R-N5-PFZ 8595343 + §C 4859e63e and REFEREE 10's §C-ext ed8bc207 (its commit
  subject, read via `git log -- docs/referee/`: "PFZ-1 = G-PFX-1; repair proves (i)"). Next step: read R-N5-PFZ.md; check whether
  REFEREE's PFZ-1 is my G-PFX-1, diff the repaired (i) statement "(θ_S ≤ (ρ_S + 1)(|U| − 2))" against BRK-POLY′ (i) as I left it;
  write the §C section into R2-N5-PFZ.md.
- §C LV2 vs REFEREE R-N5-LV2 b454ca32 (+ addendum 46a80300, + REFEREE 10's §C in ed8bc207, "identical" per its subject). Mine
  a551debf + f2209fa4 pushed. Next: read R-N5-LV2.md, gap map; also note L-SI's fixes file docs/si/P-N5-LV2-fixes-box12.md
  (sha1 f76fd1d1, l-si 680c0294, "DEAD: NONE-LAST / M=-1-last FALSE on beta2_n11") bears on the CONJECTURE successor 10 sent to L-RED;
  check the fixes file only if the Lead routes it.
- §C RHO vs REFEREE 10's R-N5-RHO (59278313, on trunk). Mine 269ae45a pushed (rides this push to trunk). Next: read R-N5-RHO.md, diff
  verdicts and notes (my N-RHO-1/2 vs its RHO-N1..N3).
- P-N5-NHN: docs/new/P-N5-NHN-box40.md `sha1sum` -> da7d09ec (= handover's pin, trunk 0bb175d). Not started. Independence:
  `ls docs/referee | grep -i NHN` -> empty. Next: read packet, build R2-N5-NHN/ on R2-N5-RHO/rho_check.py, write R2-N5-NHN.md.
- New on trunk, not routed to me yet: docs/si/P-N5-NEEDB-box13.md (sha1 7471aef3, "Lead: P-N5-NEEDB pinned" e6ee6130). Wait for the Lead.
- Predecessor NEEDS (N-LV2-1..3 -> L-SI, G-PFX-1 -> L-NEW, M = −1 last-fallback CONJECTURE -> L-RED): sent; Lead's.
- Oink: `ls tools/oink/build` -> absent; scripts/setup_oink.sh started 18:12Z.

### 3. docs/GAPS.md rows
- `grep -n 'REFEREE-2\|G-N5-TIME' docs/GAPS.md`: REFEREE-2 owns no row. Relevant: G-N5-TIME | major | L-NEW | open (docs/GAPS.md:11);
  latest UPDATE 17:41Z: R42 LANDED (P-N5-NEB); "In review: P-N5-PFZ + ext (BRK-POLY′ (i) proof gap PFZ-1 = G-PFX-1; (i′) signed),
  P-N5-LV2, P-N5-RHO, P-N5-NHN" = exactly my queue in item 2.

### 4. Three owner rulings that most constrain me (verbatim), with DECISIONS-INDEX status
1. D1 (docs/DECISIONS-INDEX.md:5: active), docs/DECISIONS.md:7-8:
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never downgrade the referee to save money.
2. D15 (index:26 active; L37 index:27 active, label "(Opus 5.5, D15)"), docs/DECISIONS.md:278:
   > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
3. D18 (index:32 active; L40 index:33 active), docs/DECISIONS.md:333:
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.

### 5. One trap that bit this lane, and the check that prevents it
- Trap (bit successors 9 and 10): the predecessor pushed after its handover / after the successor's first fetch, so push.sh was
  rejected "fetch first" and §C work was nearly duplicated. Check: `git fetch origin claude/referee-2` and
  `git log HEAD..origin/claude/referee-2` immediately before every push.sh; a rejected push means "the branch moved", merge --no-ff, never retry blind.
- Independence hazard noticed this time: `git log -- docs/referee/` commit subjects carry REFEREE verdicts (ed8bc207 states its PFZ-ext
  §C result). For a packet whose own report is not yet pushed (NHN, NEEDB), list file names only (`ls docs/referee | grep`), never
  `git log` subjects on docs/referee/.

### Correction after first push attempt (2026-10-25 18:2xZ by date -u)
- First scripts/push.sh: VERIFY PASS, then "! [rejected] (fetch first)" (exit 1). `git fetch origin claude/referee-2`;
  `git log HEAD..origin/claude/referee-2` -> 11126df8 (R2-N5-LV2 Addendum B: N-LV2-3's conjecture withdrawn, FALSE on L-RED
  beta2_n11.pg; LV-NONE induction checked at N = 2, 0 violations) and eed4efd2 (merge trunk), both by successor 10, stamped
  18:10Z, after its cd3b7cd0 handover and absent at my 18:11Z fetch. Merged --no-ff, no conflict.
- So answer 1's head is now this merge, and answer 2's LV2 item changes: N-LV2-3's conjecture to L-RED is closed (withdrawn); the
  §C LV2 must cover Addendum B too. The trap in answer 5 bit a third successor, exactly as described; the check caught it.
- Second push attempt (18:1xZ): rejected again. `git log HEAD..origin/claude/referee-2` -> 2fef675c (succ. 10, stamped 18:13Z: notebook
  handover adds the Lead's 17:56Z items). Merged --no-ff. Effect on answer 2, §C PFZ: the Lead asks whether BRK-POLY′ (i) would be
  SIGNED once REFEREE's repair is in the fixes file; REFEREE's repair (refined θ-LEN ≤ |A_low| − [o low] per P-epoch; ρ_S ≥ 1 forces a
  high u ≠ o; θ_S ≤ (ρ_S+1)(|U|−2) − 1) is to be checked by me independently (pfzx_check.py: count length moves vs |A_low|).

## successor 12 (2026-10-25T20:26Z by date -u; Opus 5.5 under D15/L37; predecessor successor 11 session_01VrcXfBuNYKJ3uBUc7ETARQ, handover a41f2c13 + late push ea5cc217)
Measured from the repository at the time of writing (commands named), not recalled.

### 1. Branch, head, distance to trunk
- Branch `claude/referee-2`. Local branch at container start was STALE (2621 behind origin). `git fetch origin claude/referee-2`;
  `git checkout -B claude/referee-2 origin/claude/referee-2`; `git rev-parse HEAD origin/claude/referee-2` -> both ea5cc217
  (succ. 11's C.5 addendum, pushed after its a41f2c13 handover; `git log a41f2c13..` shows 9761ff10 merge + ea5cc217).
- Trunk claude/vibrant-johnson-nxvvxo (docs/NOW.md:15) at 27b1cc0a (fetched 20:26Z). Before merge:
  `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` -> 3 ahead, 9 behind (merge-base 04b5c1fd).
  `git merge-base --is-ancestor`: 04b5c1fd (NHN), 2fef7c4a (FBPOLY), b621f9af (PHI) ON trunk; a41f2c13 (NHN §C + handover) and
  ea5cc217 (PFZ C.5) NOT on trunk.
- `git merge --no-ff origin/claude/vibrant-johnson-nxvvxo` -> ab0dac71 (no conflict): 4 ahead, 0 behind. This file's commit adds one.

### 2. Open work and next step of each (Lead's 20:2xZ queue, which supersedes the handover's)
- DONE after the handover: PFZ fixes §1 diff = C.5 (ea5cc217), BRK-POLY′ (i)-(iii) signed unconditionally. This also answers the
  GAPS G-N5-TIME UPDATE 19:40Z/20:15Z correction ("C.2 ... conditional on its own diff of the fixes text ... CHECKER C53 E-1"):
  ea5cc217 rides this push to trunk.
- 1. P-N5-NEEDB: docs/si/P-N5-NEEDB-box13.md `sha1sum` -> 7471aef3 (= pin). Not started. Next: read packet + cited results, build
  R2-N5-NEEDB/ on R2-N5-LV2/lv2_check.py (+ files.lst 492 𝒞^1O), batch + climbs + mutation control; write R2-N5-NEEDB.md.
- 2. §C FBPOLY vs docs/referee/R-N5-FBPOLY.md (sha1 e4389a59 in this tree; referee 3de7cab): mine 2fef7c4a is pushed, so readable.
  Next: diff verdicts and notes (my N-FBP-1/2/4) with REFEREE's; write §C into R2-N5-FBPOLY.md.
- 3. §C PHI vs docs/referee/R-N5-PHI.md (sha1 1df761ea; referee 843ba1f8): mine b621f9af pushed. Same procedure, R2-N5-PHI.md.
- 4. P-N5-FX: docs/si/P-N5-FX-box14.md sha1 aa227b0b (= pin). Not started. INDEPENDENCE: `ls docs/referee | grep -i fx` ->
  R-N5-FX.md EXISTS; I do not open it (nor `git log` it) before my R2-N5-FX.md is pushed. Conditional on FBPOLY.
- 5. P-N5-NH-box42: docs/new/P-N5-NH-box42.md sha1 93d19be8 (pinned by Lead 54ac72e6). Not started. `ls docs/referee | grep -i nh`
  -> R-N5-NH.md EXISTS (also R-N5-NHN.md, already read by succ. 11 for its §C); R-N5-NH.md stays unopened until mine is pushed.
- Also present and NOT to be opened before my report: docs/referee/R-N5-NEEDB.md (item 1).
- Oink: `ls tools/oink/build` -> absent in this container; scripts/setup_oink.sh started 20:26Z (log in my scratchpad).

### 3. docs/GAPS.md rows
- `grep -n 'REFEREE-2\|G-N5-TIME' docs/GAPS.md`: REFEREE-2 owns no row. Relevant: G-N5-TIME | major | L-NEW (L-LIT T22; referees
  later) | open (docs/GAPS.md:11); latest UPDATE 20:15Z corrects 19:40Z's R44 status (my C.2 signature pending its fixes diff = now
  C.5 ea5cc217). GAP-A (L-ALG) open, not routed to me.

### 4. Three owner rulings that most constrain me (verbatim), with DECISIONS-INDEX status
1. D1 (docs/DECISIONS-INDEX.md:5: active), docs/DECISIONS.md:7-8:
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never downgrade the referee to save money.
2. D15 (index:26 active; L37 index:27 active, label "(Opus 5.5, D15)"), docs/DECISIONS.md:278:
   > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
3. D18 (index:32 active; L40 index:33 active), docs/DECISIONS.md:333:
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.

### 5. One trap that bit this lane, and the check that prevents it
- Trap (bit successors 9, 10, 11, and again here: ea5cc217 landed after the a41f2c13 handover): a HANDOVER section is not the branch
  head, and a predecessor may push after it. Check: `git log <handover SHA>..origin/claude/referee-2` at start (done: 9761ff10,
  ea5cc217), and `git fetch origin claude/referee-2 && git log HEAD..origin/claude/referee-2` right before every push.sh.
- Independence hazard live now: REFEREE's R-N5-NEEDB.md, R-N5-FX.md and R-N5-NH.md are already in docs/referee/ for three packets I
  have not reported. Check: before opening any docs/referee/ file, confirm my own R2 report for that packet is in
  `git log origin/claude/referee-2 -- docs/referee-2/`; list file names only, never `git log` subjects on docs/referee/.
- Caught at my first push (20:2xZ): `git log HEAD..origin/claude/referee-2` -> 2173b54f (succ. 11, handover update: C.5 timestamp
  20:2xZ -> 20:1xZ; resume point NEEDB; NH42 report name docs/referee-2/R2-N5-NH42.md, pin trunk 54ac72e6, sha1 93d19be8 = my
  measurement in answer 2). Merged --no-ff, no conflict; answers 1-4 unchanged in substance (head is now this merge + this commit).
- Second push attempt (20:3xZ): VERIFY PASS, then rejected "fetch first". `git log HEAD..origin/claude/referee-2` -> f8cb3ef3
  (succ. 11, stamped 20:26:55Z: §C PHI vs R-N5-PHI, identical, empty gap map; handover queue updated). Merged --no-ff. Effect on
  answer 2: queue item 3 (§C PHI) is DONE by the predecessor; remaining order NEEDB -> §C FBPOLY -> FX -> NH42.

## successor 13 (2026-10-26T00:02Z by date -u; Opus 5.5 under D15/L37; predecessor successor 12 session_01S8gi5khZfh16sXZ4fcHvZr, handover dd79fb25 + update 20fea7d7)
Measured from the repository at the time of writing (commands named), not recalled.

### 1. Branch, head, distance to trunk
- Branch `claude/referee-2`. `git fetch origin claude/referee-2` (77f9cf71..20fea7d7); `git checkout -B claude/referee-2
  origin/claude/referee-2`; `git rev-parse HEAD origin/claude/referee-2` -> both 20fea7d7. `git log dd79fb25..origin/claude/referee-2`
  -> d915e781 (merge trunk) + 20fea7d7 (§C KW): the handover was updated after it was written, as the brief says.
- Trunk claude/vibrant-johnson-nxvvxo (docs/NOW.md:15) at d5889f8c (fetched 00:01Z). Before merge:
  `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` -> 5 ahead, 10 behind (merge-base 84b57e9c).
  `git merge-base --is-ancestor`: 8a47fd92 (KW report), 75372604 (§C FBPOLY) ON trunk; dd79fb25 (handover), fafea30e (§C NEEDB),
  20fea7d7 (§C KW) NOT on trunk.
- `git merge --no-ff origin/claude/vibrant-johnson-nxvvxo` -> 61fe6389 (no conflict): 6 ahead, 0 behind. This file's commit adds one.

### 2. Open work and next step of each (brief's queue; supersedes the handover's item 4 "ask the Lead for DUAL")
- DONE by successor 12: §C KW (20fea7d7), §C NEEDB (fafea30e); both reach trunk with this push.
- 1. P-N5-FX: docs/si/P-N5-FX-box14.md, `git show <trunk>:… | sha1sum` -> aa227b0b (= pin). Not started. Next: read packet + cited
  RESULTS rows (R44-R48), build docs/referee-2/R2-N5-FX/ checker on 𝒞^1O files (reuse R2-N5-KW/ tools), batch + climb + mutation
  control; write R2-N5-FX.md. `ls docs/referee | grep -i fx` -> R-N5-FX.md EXISTS: unopened until mine is pushed.
- 2. P-N5-NH-box42: docs/new/P-N5-NH-box42.md sha1 93d19be8 (= pin). Not started. Same procedure, R2-N5-NH42.md.
  `ls docs/referee` -> R-N5-NH.md and R-N5-NH42.md EXIST: both unopened until mine is pushed (R-N5-NHN.md was read by succ. 11 for NHN).
- 3. P-N5-DUAL: docs/new/P-N5-DUAL-box43.md, sha1 at pin df073cb5 -> a51f7c30 (= brief), df073cb5 is on trunk. Not started.
  R-N5-DUAL.md EXISTS, and this merge brought docs/referee/scratch/dual_probe.py (REFEREE's): both unopened until mine is pushed.
- Oink: `ls tools/oink/build` -> absent; scripts/setup_oink.sh started 00:02Z (log in my scratchpad).

### 3. docs/GAPS.md rows
- `grep -n 'REFEREE-2' docs/GAPS.md`: REFEREE-2 owns no row (mentions only, in closed G-Bthr/G-K5 and GAP-A text). Relevant:
  G-N5-TIME | major | L-NEW (L-LIT T22; referees later) | open (docs/GAPS.md:11); latest UPDATE 22:36Z: R48 (FB-POLY) landed; on
  𝒞^1O G-N5-TIME waits on P-N5-KW and, for the second route, P-N5-FX and P-N5-NH-box42 (two of my queue items); beyond 𝒞^1O OPEN.
  GAP-A (L-ALG) open, not routed to me.

### 4. Three owner rulings that most constrain me (verbatim), with DECISIONS-INDEX status (trunk d5889f8c)
1. D1 (docs/DECISIONS-INDEX.md:5: active), docs/DECISIONS.md:7-8:
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never downgrade the referee to save money.
2. D15 (index:26 active; L37 index:27 active, label "(Opus 5.5, D15)"), docs/DECISIONS.md:278:
   > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
3. D18 (index:32 active; L40 index:33 active), docs/DECISIONS.md:333:
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.

### 5. One trap that bit this lane, and the check that prevents it
- Trap (bit successor 12: NEEDB report disclosed it): a repo-wide grep printed LEAD-STATE / RESULTS lines on REFEREE's verdict for
  a packet I had not reported. All three of my packets now have REFEREE reports on trunk (R-N5-FX, R-N5-NH/NH42, R-N5-DUAL, plus
  scratch/dual_probe.py). Check: grep only the packet's own dir (docs/si/, docs/new/) and my docs/referee-2/; never grep docs/,
  docs/agents/, notes/ or RESULTS repo-wide; list docs/referee by file name only; before opening any docs/referee/ file confirm my
  R2 report on that packet is in `git log origin/claude/referee-2 -- docs/referee-2/`. Merge outputs list file names (seen:
  dual_probe.py name only) — names are fine, contents are not.
- Standing check (bit successors 9-12): `git fetch origin claude/referee-2 && git log HEAD..origin/claude/referee-2` before every push.sh.

## successor 14 (2026-10-26T04:1xZ by date -u; Opus 5.5 under D15/L37; predecessor successor 13 session_01Hjrye27AzEi22tE6LHsM4Y, handover 3e5bc009 + merge e931730c)
Measured from the repository at the time of writing (commands named), not recalled.

### 1. Branch, head, distance to trunk
- Branch `claude/referee-2`. Local branch at container start was STALE: HEAD 77f9cf71 (R2-N5-1OA §C2);
  `git merge-base --is-ancestor e931730c HEAD` -> no. After `git fetch origin` and `git merge --ff-only origin/claude/referee-2`:
  HEAD = origin/claude/referee-2 = e931730c (is-ancestor -> yes).
- Trunk claude/vibrant-johnson-nxvvxo at 5e5fe3dc. Before my merge: 4 ahead (a28b0955 merge, f0e82d8a R2-N5-VILB/ACCEL,
  3e5bc009 handover, e931730c merge), 1 behind. ceed1f63 (R2-N5-1E) is on trunk; f0e82d8a is NOT (is-ancestor -> no).
- `git merge --no-ff origin/claude/vibrant-johnson-nxvvxo` -> 039be605 (no conflict). `git rev-list --left-right --count
  HEAD...origin/claude/vibrant-johnson-nxvvxo` -> 5 ahead, 0 behind; merge-base 5e5fe3dc. This file's commit adds one.

### 2. Open work and next step of each
Nothing in flight. Three §Cs, each blocked on REFEREE successor 12's report landing (Lead sends the SHA):
- §C 1E: object docs/si/P-N5-1E-box16.md, `sha1sum` -> e613db13 (= report's); my side R2-N5-1E (ceed1f63, on trunk).
- §C VILB: docs/new/P-N5-VILB-box44.md, sha1 872d4400 (= report's); my side R2-N5-VILB (f0e82d8a, on my branch, reaches trunk with this push's merge).
- §C ACCEL: docs/new/P-N5-ACCEL-box44.md, sha1 301f0be0 (= report's); my side R2-N5-ACCEL (f0e82d8a).
- Independence state: `git ls-tree --name-only` of docs/referee/ on trunk and on origin/claude/referee, filtered for 1E|VILB|ACCEL -> empty.
  None opened. Next step of each, after the SHA: read packet + predecessor's report enough to stand behind it (say where I only accept
  its reading), then open docs/referee/R-N5-<X>.md, append "## §C" (verdict table, joint gap map, data comparison), push, send SHA.
- Oink not built in this container (tools/oink/build absent); scripts/setup_oink.sh before any zlk cross-check.

### 3. docs/GAPS.md rows I own
- None (`awk` over the tables: owners are L-ALG, L-RED, L-NEW, L-STRUCT; no REFEREE-2). The open row these packets sit under:
  G-N5-TIME | major | L-NEW (L-LIT T22; referees later) | open (docs/GAPS.md:11).

### 4. Three owner rulings that most constrain me (verbatim), with DECISIONS-INDEX status
1. D1 (index row 5: active), docs/DECISIONS.md:7-8:
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never downgrade the referee to save money.
2. D15 (index: active; Lead reading L37 active: signatures "(Opus 5.5, D15)"), docs/DECISIONS.md:278:
   > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
3. D18 (index: active; Lead reading L40 active: labels PROVED / CONJECTURE / OPEN), docs/DECISIONS.md:333:
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.

### 5. One trap that bit this lane, and the check that prevents it
- Trap (succ. 12, R2-N5-NEEDB independence slip): a repo-wide grep printed LEAD-STATE / RESULTS lines on REFEREE's verdict before
  REFEREE-2's own report. Check: before a §C I list docs/referee/ by NAME only (`git ls-tree --name-only`), grep only the packet's own
  dirs, and open R-N5-<X>.md only after `git log origin/claude/referee-2 -- docs/referee-2/R2-N5-<X>.md` shows my report pushed.
- It bit again this session in its other form: the container started stale (77f9cf71, without e931730c); caught by fetch +
  `git merge-base --is-ancestor e931730c HEAD` before any edit.

## successor 15 (2026-10-26T07:3xZ by date -u; Opus 5.5 under D15/L37; predecessor successor 14 session_01Mx2amUjD2RPaFRD5Re2ZHs, handover a50c0371 + merge c5ea9acb)
Measured from the repository at the time of writing (commands named), not recalled.

### 1. Branch, head, distance to trunk
- Branch `claude/referee-2`. Local branch at container start was STALE: HEAD 77f9cf71 (R2-N5-1OA §C2);
  `git merge-base --is-ancestor a50c0371 HEAD` -> no. After `git fetch origin claude/referee-2 claude/vibrant-johnson-nxvvxo` and
  `git merge --ff-only origin/claude/referee-2`: HEAD = origin/claude/referee-2 = c5ea9acb (predecessor's trunk merge); a50c0371 is-ancestor -> yes.
- Trunk claude/vibrant-johnson-nxvvxo at ca0a4e97 (also the STAU pin). `git merge --no-ff origin/claude/vibrant-johnson-nxvvxo` -> 4c78127e
  (no conflict). `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` -> 1 ahead, 0 behind (merge-base ca0a4e97,
  so all predecessor work is on trunk). This file's commit adds one.

### 2. Open work and next step of each
- Nothing in flight (predecessor: IN FLIGHT none; all §Cs done; NC report VOID).
- NEXT (after GO): P-N5-STAU, docs/new/P-N5-STAU-box45.md, sha1 7446d9a9 (Lead), frozen at l-new 010bfdae, pin trunk ca0a4e97.
  Sign §1 Lemma Στ-STEP (a)-(d) + corollary; CHECK §2 (audited table; answer (1) whole citation chain of R48 (i) and R50 (h)? (2) any proof
  using S4b's output implicitly?); not §3, §4. Next step: sha1sum the blob at the pin, read the packet, the SPEC S1-S5 and every cited result;
  reuse/extend docs/referee-2/R2-N5-EPR/epr_check.py (own N5^τ, SELF-checked against the Runner); compare with L-COMP l-comp 16c960b5 only
  after my own runs. Output docs/referee-2/R2-N5-STAU.md.
- Independence state: `git ls-tree --name-only -r origin/claude/vibrant-johnson-nxvvxo docs/referee/ | grep -i STAU` -> empty. Not opened.
- Fix routings in predecessor's NEEDS (2T, FBK, XEP, EPR, H3) are the Lead's.
- Oink not built in this container (tools/oink/build absent).

### 3. docs/GAPS.md rows I own
- None (owner column of docs/GAPS.md: L-ALG, L-RED, L-NEW, L-STRUCT, owner; no REFEREE-2). The open row STAU sits under:
  G-N5-TIME | major | L-NEW (L-LIT T22; referees later) | open (docs/GAPS.md:11; latest UPDATE 07:25Z R61/R63).

### 4. Three owner rulings that most constrain me (verbatim), with DECISIONS-INDEX status
1. D1 (index line 5: active), docs/DECISIONS.md:7-8:
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never downgrade the referee to save money.
2. D15 (index line 26: active; L37 line 27 active: signatures "(Opus 5.5, D15)"), docs/DECISIONS.md:278:
   > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
3. D18 (index line 32: active; L40 line 33 active: labels PROVED / CONJECTURE / OPEN), docs/DECISIONS.md:333:
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.

### 5. One trap that bit this lane, and the check that prevents it
- Trap: the container starts on a stale local branch (again this time: 77f9cf71 without a50c0371). Check: fetch, then
  `git merge-base --is-ancestor <handover SHA> HEAD` before any edit; fast-forward to origin/claude/referee-2, then --no-ff trunk merge.
- Second trap (succ. 12 independence slip): repo-wide greps can print REFEREE verdict lines (LEAD-STATE, RESULTS) before my report.
  Check: list docs/referee/ by name only, grep only the packet's own dirs, open R-N5-STAU only after my report is pushed.

## successor 16 (2026-10-26T09:3xZ by date -u; Opus 5.5 under D15/L37; predecessor successor 15 session_01VJosSHA8jpworMYkRKh9T4, handover ed6addd8)
Measured from the repository at the time of writing (commands named), not recalled.

### 1. Branch, head, distance to trunk
- Branch `claude/referee-2`. Local branch at container start was STALE: HEAD 77f9cf71 (R2-N5-1OA §C2; `git status` claimed "up to date"
  before the fetch). After `git fetch origin claude/referee-2 claude/vibrant-johnson-nxvvxo` and `git merge --ff-only origin/claude/referee-2`:
  HEAD = origin/claude/referee-2 = ed6addd8 (predecessor's handover); `git merge-base --is-ancestor ed6addd8 HEAD` -> yes.
- Trunk claude/vibrant-johnson-nxvvxo at 21e9d0c6. Before merging: `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo`
  -> 2 ahead (2acee863 trunk merge, ed6addd8 handover), 1 behind (21e9d0c6); merge-base a67dca63.
  `git merge --no-ff origin/claude/vibrant-johnson-nxvvxo` -> 742ceaf6 (no conflict): 3 ahead, 0 behind. This file's commit adds one.

### 2. Open work and next step of each
- Nothing in flight (predecessor: IN FLIGHT none; RUND not started).
- NEXT (after GO): P-N5-RUND, docs/si/P-N5-RUND-box17.md. `git show 94910ed3:docs/si/P-N5-RUND-box17.md | sha1sum` and the same at l-si 762b7243
  -> both 71e198f359cbb321fc0c15e6c28676d4dd046d52 (matches the brief). Sign per its §0: §2 CR-REL; §3 OFFSET (a)-(c), MERGE-B, TWIN-GAP (i)-(iii)
  + corollary; §4 PIECE_D (a), (b), SPLIT-RED; §5 P^c_sch, FRZ-SCH, CHARGE; §6 Fact FZ, Lemma UNF, Corollary CHARGE-U. Not §7-§9.
  Next step: read the packet, SPEC S1-S5 and every cited result; check its quotes of RESULTS R55 / R62 verbatim; list every premise (incl. 1E-N3);
  build my own checker on the predecessors' engines (dual_check.Runner, epr_check.step); output docs/referee-2/R2-N5-RUND.md.
- Independence state: `git fetch origin claude/referee`; `git ls-tree --name-only -r origin/claude/referee docs/referee/ | grep -ic rund` -> 0;
  same on HEAD -> 0. Not opened.
- Predecessor NEEDS (STAU-1 repair, REC0 notes to L-NEW's fixes files) are Lead routings.
- Oink: scripts/setup_oink.sh run in this container: exit 0, "oink built at 8fbf0a7" (tools/oink/build).

### 3. docs/GAPS.md rows I own
- None (`grep -n REFEREE-2 docs/GAPS.md` hits only closed rows G-Bthr, G-K5, G-STR, G-DOM, where REFEREE-2 is cited, not owner).
  The open row RUND sits under: G-N5-TIME | major | L-NEW (L-LIT T22; referees later) | open (docs/GAPS.md:11).

### 4. Three owner rulings that most constrain me (verbatim), with DECISIONS-INDEX status
1. D1 (index line 5: active), docs/DECISIONS.md:7-8:
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never downgrade the referee to save money.
2. D15 (index line 26: active; L37 line 27: signatures "(Opus 5.5, D15)"), docs/DECISIONS.md:278:
   > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
3. D18 (index line 32: active; L40 line 33: labels PROVED / CONJECTURE / OPEN), docs/DECISIONS.md:333:
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.

### 5. One trap that bit this lane, and the check that prevents it
- Trap: an independence line written from a stale listing (succ. 15 at REFEREE0, corrected 82fdc8d4): REFEREE writes in parallel, so
  "no RUND file" goes stale. Check: `git fetch origin claude/referee` and `git ls-tree --name-only -r origin/claude/referee docs/referee/ | grep -ic rund`
  in the same turn as writing the independence line; report the count.
- Also again this time: stale container (77f9cf71); caught by fetch + is-ancestor ed6addd8.

## successor 17 (2026-10-26T13:3xZ by date -u; Opus 5.5 under D15/L37; predecessor successor 16 session_01R1scbTA9MiKutHRhRdi3zh, handover 11e3cfb1 + merge e650e58e)
Measured from the repository at the time of writing (commands named), not recalled.

### 1. Branch, head, distance to trunk
- Branch `claude/referee-2`. Local branch at container start was STALE again: HEAD 77f9cf71 (R2-N5-1OA §C2; `git status` said "up to date"
  before the fetch). After `git fetch origin claude/vibrant-johnson-nxvvxo claude/referee-2` and `git merge --ff-only origin/claude/referee-2`:
  HEAD = origin/claude/referee-2 = e650e58e (predecessor's trunk merge); `git merge-base --is-ancestor 11e3cfb1 HEAD` -> yes.
- Trunk claude/vibrant-johnson-nxvvxo at 16b330d9. Before merging: `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo`
  -> 2 ahead (11e3cfb1 handover, e650e58e merge), 6 behind; merge-base 90457ab0.
  `git merge --no-ff origin/claude/vibrant-johnson-nxvvxo` -> 9545f342 (no conflict): 3 ahead, 0 behind. This file's commit adds one.

### 2. Open work and next step of each
- Nothing in flight (predecessor: IN FLIGHT none; all §Cs done).
- NEXT (after GO), in order:
  (1) P-N5-FBC, docs/new/P-N5-FBC-box47.md. `git show de02d37e:<path> | sha1sum` and the same at l-new 1f8d6d7d -> both
      32d3776cf4090fb15c1d0cb4c8b4f59276f64e21 (matches the brief). Sign FB-RISE_C, SAT_C, Theorem FB-C, Corollaries (a)-(d); check the header's
      claim that (a)'s N_ep form and (d) are weaker than landed RESULTS R60 (c) EPOCH; premise P-N5-HONFF Q-A (my predecessor: Q-A YES, R2-N5-HONFF).
      Next step: read the packet, SPEC, R60 verbatim and every cited result; extend R2-N5-HONFF/honff_check.py into my own checker; output
      docs/referee-2/R2-N5-FBC.md with every count in the file.
  (2) P-N5-CHOSEN, docs/si/P-N5-CHOSEN-box19.md. `git show 9196c318:<path> | sha1sum` and the same at l-si b7189738 -> both
      764cfbb331a1aaefa819a01d64ee6b7cfbbd7316 (matches). Sign CHOSEN, RELAY-CHAIN (a), (b), TV-END. Next step: read packet + cited results;
      own checker on R2-N5-FLIP/flip_check.py and the Runner; output docs/referee-2/R2-N5-CHOSEN.md.
- Independence state, same turn as the fetch of origin/claude/referee:
  `git ls-tree --name-only -r origin/claude/referee docs/referee/ | grep -ic -e fbc -e chosen` -> 0; same on HEAD -> 0. Not opened.
- Predecessor NEEDS (route N-RUND-*, N-HON-*, G-FLIP-1..3 + N-FLIP-1..4, N-HONFF-1..4) are Lead routings.
- Oink: scripts/setup_oink.sh run in this container: exit 0, "oink built at 8fbf0a7" (tools/oink/build).

### 3. docs/GAPS.md rows I own
- None (`grep -n REFEREE-2 docs/GAPS.md` hits only closed rows G-Bthr, G-K5, G-STR, G-DOM (lines 20-23), REFEREE-2 cited, not owner).
  The open row both packets sit under: G-N5-TIME | major | L-NEW (L-LIT T22; referees later) | open (docs/GAPS.md:11).

### 4. Three owner rulings that most constrain me (verbatim), with DECISIONS-INDEX status
1. D1 (index line 5: active), docs/DECISIONS.md:7-8:
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never downgrade the referee to save money.
2. D15 (index line 26: active; L37 line 27: signatures "(Opus 5.5, D15)"), docs/DECISIONS.md:278:
   > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
3. D18 (index line 32: active; L40 line 33: labels PROVED / CONJECTURE / OPEN), docs/DECISIONS.md:333:
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.

### 5. One trap that bit this lane, and the check that prevents it
- Trap (succ. 16, HONFF): REFEREE pushed its report 25 min before my push; my commit message said independence count 0 from a template,
  while the push-turn count was 1 (corrected by addendum 1306c31e). Check: in the push turn, fetch origin/claude/referee and run the
  `git ls-tree --name-only ... | grep -ic` count, write the number from that output into the report and message, never from a template;
  no `git log` on origin/claude/referee before the §C word (its subjects carry verdicts).
- Also again this time: stale container (77f9cf71); caught by fetch + is-ancestor 11e3cfb1 before any edit.

## successor 18 (2026-10-26T19:0xZ by date -u; Opus 5.5 under D15/L37; predecessor successor 17 session_01P2K6kCftytexWsuJfNFtV4, handover 549dea7e updated at f5381a5c, merge 8779d1de)
Measured from the repository at the time of writing (commands named), not recalled.

### 1. Branch, head, distance to trunk
- Branch `claude/referee-2`. Local branch at container start was STALE again: HEAD 77f9cf71 (`git status` said "up to date" before the fetch).
  After `git fetch origin claude/vibrant-johnson-nxvvxo claude/referee-2` and `git merge --ff-only origin/claude/referee-2`:
  HEAD = origin/claude/referee-2 = 8779d1de; `git merge-base --is-ancestor f5381a5c HEAD` -> yes (549dea7e is in it too).
- Trunk claude/vibrant-johnson-nxvvxo at 1ba37bf3. Before merging: `git rev-list --left-right --count origin/claude/referee-2...origin/claude/vibrant-johnson-nxvvxo`
  -> 4 ahead (549dea7e handover, 9d2c039c merge, f5381a5c ROOT §C, 8779d1de merge), 14 behind; merge-base e92d50c2.
  `git merge origin/claude/vibrant-johnson-nxvvxo` -> df26519d (no conflict): 5 ahead, 0 behind. This file's commit adds one.

### 2. Open work and next step of each
- Nothing in flight (predecessor: IN FLIGHT none; ROOT §C pushed at f5381a5c).
- NEXT (after GO), in the Lead's order. Pins measured with `git show origin/claude/vibrant-johnson-nxvvxo:<path> | sha1sum`:
  (1) P-N5-OFFMONO as one unit: docs/new/P-N5-OFFMONO-box49.md d9705ac6, -add- 5911aba8, -add2- f2d123ef (all match the brief, on trunk);
      add3 (OFFSET-MONO⁺, CHAIN-COUNT‴) NOT yet frozen/pinned: wait for the Lead's sha1 before signing the unit.
      Next step: read packet + add + add2 + cited results; own checker (add2 §4 is code-level against si.py: check it against si.py, run my own engine).
  (2) P-N5-GCX docs/si/P-N5-GCX-box21.md 5a91bebb (matches); note R91 (UL_C), R93 (C-ONCE_X) kills; no to-sign item touched.
  (3) P-N5-DEPTH docs/si/P-N5-DEPTH-box22.md 549c7fb7 (matches, trunk); P-N5-DEPTH-add docs/si/P-N5-DEPTH-add-box22.md 4d51aa5e:
      NOT on trunk (trunk path absent, sha1sum of empty = da39a3ee); found on origin/claude/l-si (aa6061d1, sha1 4d51aa5e matches the brief).
  (4) P-N5-RESTRICT docs/new/P-N5-RESTRICT-box48.md 48c63a8e (matches).
- Independence state, same turn as the fetch of origin/claude/referee (19:04:54Z):
  `git ls-tree --name-only -r origin/claude/referee docs/referee/ | grep -ic <key>` -> offmono 8, gcx 26, depth 0, restrict 0 (same on HEAD).
  Names only; none opened. REFEREE 15 reported on OFFMONO/OFFMONO-add before; GCX files exist (first referee). I open none until my report is pushed.
- Predecessor NEEDS (route N-FBC/N-CHOSEN/N-EPC/N-ROOT notes; ROOT §C word; start successor 18) are Lead routings; the ROOT §C is done (f5381a5c).
- Oink: scripts/setup_oink.sh run in this container: exit 0, "oink built at 8fbf0a7" (tools/oink/build).

### 3. docs/GAPS.md rows I own
- None (`grep -n REFEREE-2 docs/GAPS.md` hits line 6 GAP-A (REFEREE-2 cited in its text) and closed rows G-Bthr, G-K5, G-STR, G-DOM (lines 20-23); owner column never REFEREE-2).
  The open row the queue sits under: G-N5-TIME | major | L-NEW (L-LIT T22; referees later) | open (docs/GAPS.md:11).

### 4. Three owner rulings that most constrain me (verbatim), with DECISIONS-INDEX status
1. D1 (index line 5: active), docs/DECISIONS.md:7-8:
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never downgrade the referee to save money.
2. D15 (index line 26: active; L37 line 27: signatures "(Opus 5.5, D15)"), docs/DECISIONS.md:278:
   > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
3. D18 (index line 32: active; L40 line 33), docs/DECISIONS.md:333:
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.

### 5. One trap that bit this lane, and the check that prevents it
- Trap (succ. 16, HONFF; again succ. 17 three times): the independence count changes between reads (REFEREE pushes during my reviews); a
  count copied from a template was wrong once (addendum 1306c31e). Check: fetch origin/claude/referee in the push turn, run the
  `git ls-tree --name-only ... | grep -ic` count, and write the number from that output; no `git log` on origin/claude/referee before the §C word.
- Also again this time: stale container (77f9cf71); caught by fetch + is-ancestor f5381a5c before any edit. And a "pin" can be a file sha1
  on a lane branch rather than trunk (DEPTH-add 4d51aa5e lives on l-si only): measure each pin with `git show <ref>:<path> | sha1sum`.

## successor 19 (2026-10-28T23:3xZ by date -u; Opus 5.5 under D15/L37; predecessor successor 18 session_01WT4cukhJyjxHKaBJWikCkK, handover 864302d0)
Measured from the repository at the time of writing (commands named), not recalled.

### 1. Branch, head, distance to trunk
- Branch `claude/referee-2`. Container NOT stale this time: `git status` / `git log -1` at start -> 864302d0 = origin/claude/referee-2 (the handover commit).
- After `git fetch origin claude/vibrant-johnson-nxvvxo`: `git rev-list --left-right --count 864302d0...origin/claude/vibrant-johnson-nxvvxo` -> 2 ahead
  (516b374b merge, 864302d0 RESTRICT §C + HANDOVER), 13 behind; merge-base f86a4145.
- `git merge origin/claude/vibrant-johnson-nxvvxo` -> 73250d93 (no conflict); trunk head 908e4333; `git rev-list --left-right --count HEAD...trunk` -> 3 ahead, 0 behind.
  This file's commit adds one.

### 2. Open work and next step of each
- Nothing in flight (handover: IN FLIGHT none; RESTRICT §C in 864302d0).
- NEXT: P-N5-CORE, docs/si/P-N5-CORE-box23.md, items (C1)-(C6). Pin measured: `git show 081ae740:docs/si/P-N5-CORE-box23.md | sha1sum`,
  same for origin/claude/l-si and origin/claude/vibrant-johnson-nxvvxo -> 7b66f1bae1a1b675c0fda0af1e5eaabf13f128a0 (all three match the brief).
  Next step: read the packet and every result it cites; own checker on my lane's engines (no lane code); mutation controls + vacuity checks;
  write docs/referee-2/R2-N5-CORE.md; push; then §C only on the Lead's word.
- Independence state (23:29:20Z, same turn as the fetch of origin/claude/referee): `git ls-tree --name-only -r origin/claude/referee docs/referee/ | grep -ic core`
  -> 16 (names only; none opened; no `git log` on origin/claude/referee). REFEREE's R-N5-CORE.md (9d831869) exists per the Lead.
- Predecessor NEEDS (route OFFMONO/GCX/DEPTH/DEPTH-add/RESTRICT notes and gaps; start successor 19) are Lead routings; successor 19 = this session.
- Oink: tools/oink/build absent at start; scripts/setup_oink.sh started in this container (result reported in the message).

### 3. docs/GAPS.md rows I own
- None (`grep -n REFEREE-2 docs/GAPS.md` -> lines 6 GAP-A (cited in text), 20-23 closed G-Bthr, G-K5, G-STR, G-DOM; owner column never REFEREE-2).
  The open row the queue sits under: G-N5-TIME | major | L-NEW (L-LIT T22; referees later) | open (docs/GAPS.md:11).

### 4. Three owner rulings that most constrain me (verbatim), with DECISIONS-INDEX status
1. D1 (index line 5: active), docs/DECISIONS.md:7-8:
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never downgrade the referee to save money.
2. D15 (index line 26: active; L37 line 27: signatures "(Opus 5.5, D15)"), docs/DECISIONS.md:278:
   > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
3. D18 (index line 32: active; L40 line 33), docs/DECISIONS.md:333:
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.

### 5. One trap that bit this lane, and the check that prevents it
- Trap (succ. 18, RESTRICT): `git log origin/claude/referee -- <file>` printed a LATER commit subject carrying REFEREE's verdict (exposure, declared
  in R2-N5-RESTRICT). Check: before my own report on a packet is pushed, the only command run on origin/claude/referee is
  `git ls-tree --name-only -r origin/claude/referee docs/referee/ | grep -ic <key>`, run in the push turn, number copied from its output.
- Recurring content trap (succ. 18 GCX, DEPTH, DEPTH-add): "any deterministic rule" claims fail for non-keep tie rules; per-class intervals not cut
  at freeze; telescoping lemmas need "at or before c". Check: each CORE item is tested with keep / flip / random tie rules and at freeze cuts.

## successor 20 (2026-10-29T11:20Z by date -u; Opus 5.5 under D15/L37; predecessor successor 19 session_01V5yGRZzoAVpZvqB1LedCVF, handover c5ee7fc3)
Measured from the repository at the time of writing (commands named), not recalled.

### 1. Branch, head, distance to trunk
- `git fetch origin claude/referee-2 claude/vibrant-johnson-nxvvxo claude/l-lit`; local was 864302d0 (stale), `git merge --ff-only` -> HEAD =
  origin/claude/referee-2 = c5ee7fc3 (predecessor's handover).
- `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` -> 2 ahead, 9 behind (trunk 1ccf04f1; merge-base 81264723).
  Merged trunk with a merge commit 04ab4a72 (`git merge --no-edit`, no rebase).

### 2. Open work and next step of each
- Predecessor DONE table ends with P-N5-MATCHPHI (report 5ba3e21d, §C NOT YET). P-N5-MATCHPHI is superseded by P-N5-MPGS (trunk a23179b0,
  Lead 1ccf04f1), so its §C folds into the MPGS §C.
- NOW: packet P-N5-MPGS, docs/lit/P-N5-MPGS.md @ a23179b0. Part (A): diff against P-N5-MATCHPHI @ 12b7d12a; carry identical verdicts.
  Part (B) GATE-SHUT: full review, re-run T34-gateshut-check.py and P-N5-MPGS-quotecheck.py, own control. Output docs/referee-2/R2-N5-MPGS.md.
- `git ls-tree --name-only -r origin/claude/referee docs/referee/ | grep -ic mpgs` -> 0 (REFEREE has no MPGS file yet; not opened anyway).
- Oink NOT built in this container (`ls tools/oink/build` -> no such directory).

### 3. docs/GAPS.md rows relevant to me
- `grep -n REFEREE-2 docs/GAPS.md` -> 6 lines, all as attester inside rows owned by other lanes (GAP-A, G-N5-TIME, G-Bthr, G-K5, G-STR, G-DOM).
  REFEREE-2 owns no row.

### 4. Three owner rulings that most constrain me (verbatim), with DECISIONS-INDEX status
1. D1 (index row 5: active), docs/DECISIONS.md:7-8:
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never downgrade the referee to save money.
2. D15 (index row 26: active), docs/DECISIONS.md:278:
   > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
3. D18 (index row 32: active), docs/DECISIONS.md:333:
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.

### 5. One trap that bit this lane, and the check that prevents it
- Trap (succ. 19, trap 5): pinned lane scripts read the packet from the working tree, so a run on a later tree checks the wrong text.
  Check: run T34-gateshut-check.py and P-N5-MPGS-quotecheck.py in a detached worktree at a23179b0, sha1 of each script compared first.
- Also this session: local branch stale (864302d0 vs origin c5ee7fc3); checked `git rev-parse HEAD origin/claude/referee-2` equal after ff.

## successor 21 (2026-10-29T20:58Z by date -u; Opus 5.5 under D15/L37; predecessor successor 20 session_01V5yGRW4aXFYpk1wXFkEfTp, last push d1575e61)
Measured from the repository at the time of writing (commands named), not recalled.

### 1. Branch, head, ahead/behind trunk
- `git ls-remote origin` first (15 branch refs; claude/referee-2 d1575e61, trunk claude/vibrant-johnson-nxvvxo 5057c0a2); fetched only those names.
- Local container was stale at 864302d0 (succ. 18's handover). `git merge --ff-only origin/claude/referee-2` -> d1575e61.
- `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` at d1575e61: **0 ahead / 101 behind**; merge-base = d1575e61
  (my branch is fully on trunk). Merged trunk (fast-forward) -> HEAD 5057c0a2 = trunk, 0/0. This section is the first commit on top.

### 2. Open work and next step of each
- Predecessor (succ. 20) wrote no HANDOVER section; its last notebook entry is Resume point 3 (18:1xZ): SF and GP closed with §Cs
  (R2-N5-SF-C.md, R2-N5-GP-C.md), queue empty. After it: R2-N5-DW (fef9dd1b) + addendum (d1575e61), both on trunk. Nothing in flight.
- NOW (Lead brief 20:56Z): P-N5-FRAME, docs/new/P-N5-FRAME-box65.md @ l-new 938d8796: `git show 938d8796:docs/new/P-N5-FRAME-box65.md | sha1sum`
  = ce8c4803ee18dc90ee761863d006d0aca0476542, 194 lines (match); 938d8796 is an ancestor of origin/claude/l-new. Line file sha1 acf3234f… (match,
  read at origin/claude/l-new). Next step: full review -> docs/referee-2/R2-N5-FRAME.md with own checker.
- Independence: `git ls-tree --name-only -r origin/claude/referee docs/referee/ | grep -ic frame` -> 0. No git log on origin/claude/referee.
- Oink: not built in this container (`ls tools/oink/build/oink` -> no such file); scripts/setup_oink.sh started.

### 3. docs/GAPS.md rows I own
- `awk -F'|' 'NR>4 && $4 ~ /REFEREE-2/' docs/GAPS.md | wc -l` -> 0 owner cells. `grep -c REFEREE-2 docs/GAPS.md` -> 6, all as attester inside
  other lanes' rows. REFEREE-2 owns no row.

### 4. Three owner rulings (verbatim) with DECISIONS-INDEX status
1. D1 (index: active): > Never downgrade the referee to save money.
2. D15 (index: active): > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
3. D18 (index: active): > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.

### 5. One trap and its check
- Trap: stale container (this one sat at 864302d0, three successors back) and an aborted multi-ref fetch on a missing ref.
  Check: `git ls-remote origin` first, fetch only listed names, `git rev-parse` local vs origin after ff. Plus the independence trap
  (git log on origin/claude/referee leaks verdicts): only the names-only count is used.
