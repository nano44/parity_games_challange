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
