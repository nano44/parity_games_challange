# Handover check: REFEREE

## successor 15 (2026-10-26T13:31Z by date -u; Opus 5.5 under D15, label "(Opus 5.5, D15)"; predecessor successor 14, handover 502f55dc)
Measured from the repository at the time of writing, not recalled.

### 1. Branch, head, distance to trunk
- Branch `claude/referee`. Local branch started STALE at 73b46eb8 again (`git rev-list --count 73b46eb8..502f55dc` = 3027).
  `git fetch origin`; `git merge --ff-only origin/claude/referee`: HEAD = 502f55dc (`git merge-base --is-ancestor 502f55dc HEAD` true).
- Trunk `claude/vibrant-johnson-nxvvxo` at 16b330d9 ("Lead: C78 revision sent; NOW; log"). Before merging, 502f55dc was 2 ahead / 47
  behind trunk (merge-base cce5ea5e, my predecessor's HONFF report). The 2 ahead: HONFF §C (e7db1ab4) and the successor-14 HANDOVER (502f55dc).
- Merged trunk with `git merge` (merge commit cfcc6a83): 3 ahead / 0 behind before this file's commit.
- Oink: scripts/setup_oink.sh built 8fbf0a7 into tools/oink/build, exit 0.

### 2. Open work and next step
- Handover "IN FLIGHT: none" checked: R-N5-HON, R-N5-FLIP, R-N5-HONFF exist in docs/referee/ with their §C sections.
- New (Lead brief to successor 15), both as FIRST referee (REFEREE-2 successor 17 in parallel):
  (1) P-N5-FBC, docs/new/P-N5-FBC-box47.md, sha1 32d3776cf4090fb15c1d0cb4c8b4f59276f64e21 (re-measured on the tree, at l-new 1f8d6d7d and
      at pin de02d37e: match; de02d37e ancestor of HEAD). Next, after "go": sign or not FB-RISE_C, SAT_C, Theorem FB-C, Corollaries (a)-(d);
      check the header claim that (a)'s N_ep form and (d) are weaker than landed R60 (c) EPOCH; it rests on P-N5-HONFF Q-A (YES by both).
      Report docs/referee/R-N5-FBC.md.
  (2) P-N5-CHOSEN, docs/si/P-N5-CHOSEN-box19.md, sha1 764cfbb331a1aaefa819a01d64ee6b7cfbbd7316 (re-measured on the tree, at l-si b7189738
      and at pin 9196c318: match; 9196c318 ancestor of HEAD). Next: sign or not CHOSEN, RELAY-CHAIN (a), (b), TV-END. Report
      docs/referee/R-N5-CHOSEN.md.
  Own engine for both; check every parenthetical inside a signed statement; no docs/referee-2/ file on FBC or CHOSEN opened before my report
  is pushed (none on the tree or trunk at this fetch: `ls docs/referee-2 | grep -ic "fbc\|chosen"` = 0).
- Handover NEEDS (not mine; Lead routes): HON / FLIP / HONFF notes to the lanes' fixes files.

### 3. docs/GAPS.md rows relevant to me (trunk 16b330d9)
- REFEREE owns no row. The row my packets feed: G-N5-TIME (l.11), major, owner "L-NEW (L-LIT T22; referees later)", **open**; last UPDATE
  12:47Z: R68 (P-N5-HON; CHECKER C77) landed (W-honest states per phase ≤ f + 4n² − 3n; HON-0; RESTRICT_u, REPRO_u; REC-1 (a); EP-1u and
  REC-1 (b)-(d) as implications from (Στ)). RESULTS runs to R68 (`grep -n "^### R6[5-9]" docs/RESULTS.md`: R65..R68; R69 at CHECKER C78,
  revised per docs/NOW.md l.85).
- Other open rows (not mine): GAP-A, GAP-C, G-S5-6, G-NEST, G-N1-LB. G-N5-TERM closed.

### 4. Three owner rulings that most constrain me (verbatim, docs/DECISIONS.md), with DECISIONS-INDEX status
1. D1 (index l.5: **active**; DECISIONS.md l.7-8):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never downgrade the referee to save money.
2. D15 (index l.26: **active**; DECISIONS.md l.278):
   > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
3. D18 (index l.32: **active**; DECISIONS.md l.333):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.

### 5. One trap that bit this lane, and the check that prevents it
- Trap (successors 5-15): the container starts stale at 73b46eb8 (3027 behind the handover SHA this time). Check: `git fetch origin`,
  fast-forward, `git merge-base --is-ancestor <handover SHA> HEAD` before any work.
- Content trap (successor 14, FLIP): a parenthetical inside a signed statement (N3-LEVEL's "(… hold …)") was not checked and became joint
  gap G-FLIP-3 found only by REFEREE-2. Check: list every parenthetical and every "by (x)" inside each statement to be signed as its own
  numbered claim in the report, and check each (by proof and by probe) before signing.

## successor 14 (2026-10-26T10:29Z by date -u; Opus 5.5 under D15, label "(Opus 5.5, D15)"; predecessor successor 13, handover 62a1a01d)
Measured from the repository at the time of writing, not recalled.

### 1. Branch, head, distance to trunk
- Branch `claude/referee`. Local branch started STALE at 73b46eb8 again (`git rev-list --count 73b46eb8..62a1a01d` = 2790).
  `git fetch origin`; `git merge --ff-only origin/claude/referee`: HEAD = 62a1a01d (`git merge-base --is-ancestor 62a1a01d HEAD` true).
- Trunk `claude/vibrant-johnson-nxvvxo` at e03e7565 ("Lead: L-SI 14 check 5/5, GO; R79 logged; ..."). Before merging, 62a1a01d was
  2 ahead / 82 behind trunk (merge-base 981307c9, the REC0 §C commit). The 2 ahead: R-N5-RUND §C and the successor-13 HANDOVER (62a1a01d).
- Merged trunk with `git merge` (merge commit 6984f0f0): 3 ahead / 0 behind before this file's commit.
- Oink: scripts/setup_oink.sh built 8fbf0a7 into tools/oink/build, exit 0.

### 2. Open work and next step
- Handover "IN FLIGHT: none" checked: R-N5-STAU, R-N5-REC0, R-N5-RUND all exist in docs/referee/ with their §C sections.
- New (Lead brief to successor 14): P-N5-HON, docs/new/P-N5-HON-box46.md, sha1 07f8e767cfca12d29c8f6f2e3f03358326abbef1 (re-measured on the
  tree and at l-new 67a7b54d: match), pin trunk 31835c4b (ancestor of HEAD). I am the FIRST referee (the handover said "second"; the Lead's
  brief governs). Next, after "go": sign or not the lane-PROVED items HON, SAT0, HON-FB, HON′, HON-0, RESTRICT_u, REPRO_u, REC-1 (a); sign
  EP-1u and REC-1 (b)-(d) as implications from (Στ); check Q-R17 in HON's own use; check §2's two claims (HON-0 ⇒ signed REC-0; proofs
  independent); §5 HON-FF not signed. Report docs/referee/R-N5-HON.md; own engine; no docs/referee-2/ HON file opened before my report is
  pushed (none on the tree at this fetch: `ls docs/referee-2/ | grep -ic hon` = 0).
- Handover NEEDS (not mine; Lead routes): STAU fixes (STAU-1, N-STAU-1..4, STAU-N1..N3) to L-NEW 25; REC0 / RUND notes to their fixes files.

### 3. docs/GAPS.md rows relevant to me (trunk e03e7565)
- REFEREE owns no row. The row my packets feed: G-N5-TIME (l.11), major, owner L-NEW ("referees later"), **open**; last UPDATE 09:56Z:
  R65 (P-N5-STAU) landed; at audit strength (Στ) holds and R64 (e) EP-1 holds without it; "N_ep / ρ and epochs with |D_E| ≥ 2 OPEN;
  general games OPEN." RESULTS runs to R65 (`grep -n "^### R6[5-9]" docs/RESULTS.md`: R65 at l.3324 only).
- Other open rows (not mine): GAP-A, GAP-C, G-S5-6, G-NEST, G-N1-LB. G-N5-TERM closed.

### 4. Three owner rulings that most constrain me (verbatim, docs/DECISIONS.md), with DECISIONS-INDEX status
1. D1 (index l.5: **active**; DECISIONS.md l.7-8):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never downgrade the referee to save money.
2. D15 (index l.26: **active**; DECISIONS.md l.278):
   > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
3. D18 (index l.32: **active**; DECISIONS.md l.333):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.

### 5. One trap that bit this lane, and the check that prevents it
- Trap (successors 5-14): the container starts stale at 73b46eb8 (2790 behind the handover SHA this time). Check: `git fetch origin`,
  fast-forward, `git merge-base --is-ancestor <handover SHA> HEAD` before any work.
- Content trap (successor 13, STAU): a citation-chain audit that excluded docs/referee* missed referee-written proof steps that RESULTS
  cites as gap closures. Check: for HON's §2 independence claim and REC-0 implication, build the citation closure including referee-written
  sections (scratch/stau/closure2.py), and verify every quoted parenthetical by script against the cited file.

## successor 13 (2026-10-26T07:33Z by date -u; Opus 5.5 under D15, label "(Opus 5.5, D15)"; predecessor successor 12, handover 010924c7)
Measured from the repository at the time of writing, not recalled.

### 1. Branch, head, distance to trunk
- Branch `claude/referee`. Local branch started STALE at 73b46eb8 again (`git rev-list --count 73b46eb8..010924c7` = 2629).
  `git fetch origin`; `git merge --ff-only origin/claude/referee`: HEAD = origin/claude/referee = 010924c7 (`git merge-base --is-ancestor
  010924c7 HEAD` true).
- Trunk `claude/vibrant-johnson-nxvvxo` at ca0a4e97 ("Lead: land R61 (FBK, C70 761bcc73) then R63 (XEP, C72 a42e44f8); R62 rev. (C71 E-3);
  pin P-N5-STAU; ..."). Before merging: 0 ahead / 61 behind (010924c7 is already an ancestor of trunk via bbb6b80c; merge-base = 010924c7).
- Merged trunk with `git merge --no-ff` (e4f5eee1): 1 ahead / 0 behind before this file's commit.
- Oink: scripts/setup_oink.sh built 8fbf0a7 into tools/oink/build, exit 0.

### 2. Open work and next step (notebook "HANDOVER (successor 12 -> successor 13)", checked against the tree)
- IN FLIGHT: none (handover says so; every §C in its DONE table exists in docs/referee/).
- New, from the Lead's brief (07:31Z): P-N5-STAU (L-NEW succ. 24), docs/new/P-N5-STAU-box45.md, sha1 7446d9a9..., frozen at l-new 010bfdae,
  pin trunk ca0a4e97. Next, after "go": check the sha1, review §1 Lemma Στ-STEP (a)-(d) + corollary (sign or not), CHECK the §2 audit table
  and answer its two audit questions ((1) is the §2.1 list the whole citation chain of R48 (i) and R50 (h); (2) does any proof use S4b's
  output implicitly beyond its value); §3/§4 not signed. Write docs/referee/R-N5-STAU.md; no docs/referee-2/ file on STAU before it is pushed.
- Not mine but pending at the lanes (handover NEEDS): fixes files FBK-1/N-FBK-1/2, EPR-1/EPR-N1, H3 notes, 2T notes, ACC-2, 1E-N1.

### 3. docs/GAPS.md rows relevant to me (trunk ca0a4e97)
- REFEREE owns no row. The row my packets feed: G-N5-TIME (l.11), major, owner L-NEW ("referees later"), **open**; last UPDATE 07:25Z:
  R61 (FBK) and R63 (XEP) landed; "N_ep / ρ and X_SN^pre OPEN; general games OPEN."
- G-FBK-1 and G-EPR-1 are gap labels inside RESULTS (R61 l.3108-3151; R64 draft), not GAPS rows. Other open rows (not mine): GAP-A, GAP-C,
  G-S5-6, G-NEST, G-N1-LB. G-N5-TERM closed.

### 4. Three owner rulings that most constrain me (verbatim, docs/DECISIONS.md), with DECISIONS-INDEX status
1. D1 (index: **active**; DECISIONS.md l.7-8):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never downgrade the referee to save money.
2. D15 (index: **active**; DECISIONS.md l.278):
   > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
3. D18 (index: **active**; DECISIONS.md l.333):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.

### 5. One trap that bit this lane, and the check that prevents it
- Trap (successors 5-13): the container starts stale at 73b46eb8 (2629 behind the handover SHA). Check: `git fetch origin`, fast-forward,
  `git merge-base --is-ancestor <handover SHA> HEAD` before any work.
- Content trap for this packet type (successor 12's misses N-2T-1, N-H3-1, N-FBK-1/2): quotes and "landed premise" lists checked by eye.
  Check: verify every quoted parenthetical and every cited RESULTS letter by script against the cited file.

## successor 12 (2026-10-26T03:25Z by date -u; Opus 5.5 under D15, label "(Opus 5.5, D15)"; predecessor successor 11, handover 76a02311)
Measured from the repository at the time of writing, not recalled.

### 1. Branch, head, distance to trunk
- Branch `claude/referee`. Local branch started STALE at 73b46eb8 again (`git rev-list --count 73b46eb8..76a02311` = 2316).
  `git fetch origin`; `git merge --ff-only origin/claude/referee`: HEAD = origin/claude/referee = 76a02311 (checked with
  `git merge-base --is-ancestor` and `git rev-list --left-right --count`, 0/0).
- Trunk = remote HEAD `claude/vibrant-johnson-nxvvxo` (`git ls-remote --symref origin HEAD`) at e54d8a48 ("Lead: land R53 (P-N5-NH-box42)
  and R54 (P-N5-DUAL) ..."). Before merging: 3 ahead / 3 behind trunk, merge-base c3f6f2bf (the FBRED pin). The 3 ahead: 59b070c2
  (trunk merge), 1feff548 (R-N5-FBRED), 76a02311 (handover). The 3 behind: 1e163a67, c8ded866, e54d8a48 (Lead).
- Merged trunk with `git merge --no-ff` (f7a93dc3): 4 ahead / 0 behind before this file's commit.
- Oink: scripts/setup_oink.sh built 8fbf0a7 into tools/oink/build, exit 0.

### 2. Open work and next step (notebook "HANDOVER (successor 11 -> successor 12)", checked against the tree)
- §C on P-N5-FBRED. My lane's report docs/referee/R-N5-FBRED.md (1feff548, by successor 11; sections Verdicts, §1-§5, no §C:
  `grep -n "§C"` finds none). REFEREE-2's report: commit 814ac456 on origin/claude/referee-2 (not yet on trunk; I have not opened it).
  Packet docs/new/P-N5-FBRED-box44.md, sha1 11b15455f70d439c93a48d7e82fcdc14ef73854d (re-measured, matches). Next, after "go": read the
  packet and the report's §2 port table, then R2-N5-FBRED, then append "§C. Comparison with REFEREE-2" (verdict table, joint map
  FBRED-N1, N2 vs N-FBRED-1..4, data), saying where I only accept successor 11's reading.
- P-N5-1E (L-SI): docs/si/P-N5-1E-box16.md is on trunk; no pin received from the Lead. Next: wait for the pin; start after FBRED §C.
- Nothing else open (handover DONE table: every earlier §C written).

### 3. docs/GAPS.md rows relevant to me (trunk e54d8a48)
- REFEREE owns no row. The row my packets feed: G-N5-TIME (l.11), major, owner L-NEW (L-LIT T22; "referees later"), **open**. Last
  UPDATE 03:19Z: R53 (P-N5-NH-box42) and R54 (P-N5-DUAL) LANDED [refereed-only]; 𝒞^1O part closed by R51; "The 𝒞^1E iteration bound
  O(n¹⁷) is a READING (N-DUAL-3) until P-N5-1E is signed and landed. General games OPEN."
- Other open rows (not mine): GAP-A, GAP-C, G-S5-6 (L-ALG), G-NEST (L-RED), G-N1-LB (L-NEW). G-N5-TERM (l.16) closed (R15).

### 4. Three owner rulings that most constrain me (verbatim, docs/DECISIONS.md), with DECISIONS-INDEX status
1. D1 (index l.5: **active**; DECISIONS.md l.7-8):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never downgrade the referee to save money.
2. D15 (index l.26: **active**; DECISIONS.md l.278):
   > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
3. D18 (index l.32: **active**; DECISIONS.md l.333):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.

### 5. One trap that bit this lane, and the check that prevents it
- Trap (again now, successors 5-12): the container starts stale at 73b46eb8, 2316 commits behind origin/claude/referee. Check:
  `git fetch origin` then `git merge-base --is-ancestor 76a02311 HEAD` / `rev-list --left-right --count HEAD...origin/claude/referee`
  = 0/0 before any work.
- Content trap (successor 10, FBP-1 / FBP-2): proofs silently assuming the generic case. Check: test self-loop at o, o = c_θ, |U| = 2
  in every bound, and report my own count for every "vacuous" hypothesis with the file set.
- Process trap (successor 11): `grep -v "^EX"` also hid counters named EXS_*; filter with "^EX (".

## successor 11 (2026-10-25T21:00Z by date -u; Opus 5.5 under D15/L37, label "(Opus 5.5, D15)"; predecessor successor 10, handover 1c6c3448)
Measured from the repository at the time of writing, not recalled.

### 1. Branch, head, distance to trunk
- Branch `claude/referee`. Local branch started STALE at 73b46eb8 again (`git rev-list --count 73b46eb8..1c6c3448` = 1952).
  `git fetch origin claude/referee`; `git checkout -B claude/referee origin/claude/referee`: HEAD = origin/claude/referee = 1c6c3448
  (checked with `git rev-parse`).
- Trunk = remote HEAD `claude/vibrant-johnson-nxvvxo` (`git ls-remote --symref origin HEAD`) at f23b9c4b ("Lead: R47 draft (P-N5-NHN)
  pending fixes file; log"). Before merging: 2 ahead / 21 behind trunk, merge-base 39dee725. The 2 ahead: 271ac79f (trunk merge),
  1c6c3448 (handover).
- Merged trunk with `git merge --no-ff` (1c8a1fa3): 3 ahead / 0 behind before this file's commit.
- Oink: scripts/setup_oink.sh built 8fbf0a7 into tools/oink/build, exit 0.

### 2. Open work and next step (notebook "HANDOVER (successor 10 -> successor 11)")
- §C on P-N5-NEEDB: my report docs/referee/R-N5-NEEDB.md (008ad8ab; all SIGNED, no gaps; notes NEEDB-N1..N4). Next: when REFEREE-2
  successor 12 pushes R2-N5-NEEDB and the Lead sends its SHA, write §C in R-N5-NEEDB.md (verdict comparison, joint gap map,
  accept/reject notes).
- §C on P-N5-FX: my report docs/referee/R-N5-FX.md (843ba1f8; SIGNED, (b) conditional on FBPOLY (+ FBP-1 repair for F*); FX-N1).
  Next: same, after R2-N5-FX and the Lead's SHA. Check whether R2's (b) condition matches mine.
- §C on P-N5-NH-box42: my report docs/referee/R-N5-NH42.md (a47f8540; all SIGNED, no gaps; NH42-N1..N3). Next: same, after R2's report.
- Then the K packet (P-N5-KW) when the Lead routes it. On trunk now (unrefereed, not yet routed): L-SI box 15 N5-KW note
  (experiments/si/kw15/), L-NEW N5-KW-box42 v3 (b9ee6918: Theorem E-HI). Not started by me.
- Checked on trunk f23b9c4b: no docs/referee-2/R2-N5-{NEEDB,FX,NH42}* yet (`git ls-tree`), so nothing to compare; I have not opened
  any R2 file for these packets. Order per the predecessor: NEEDB -> (R2's §C FBPOLY) -> FX -> NH42.

### 3. docs/GAPS.md rows relevant to me (trunk f23b9c4b)
- REFEREE owns no row. The row my packets feed: G-N5-TIME (l.11), major, owner L-NEW (L-LIT T22; "referees later"), **open**. Last
  UPDATE 20:36Z: R44 (P-N5-PFZ + ext + fixes) and R45 (P-N5-RHO + fixes) LANDED [refereed-only]; "Still open for G-N5-TIME: N_HN for
  τ(o) ≠ o (P-N5-NHN ...), fallbacks per phase (P-N5-FBPOLY), phases (P-N5-PHI), crossings (P-N5-FX), the NH count (P-N5-NH-box42),
  and K." (Trunk also carries Lead drafts R46 (PHI) and R47 (NHN) pending fixes files, not yet in this row.)
- G-N5-TERM (l.16) closed (RESULTS R15). DTL rows (GAP-A l.6, etc.) open but paused (D18/L40).

### 4. Three owner rulings that most constrain me (verbatim, docs/DECISIONS.md), with DECISIONS-INDEX status
1. D1 (index l.5: **active**; DECISIONS.md l.7-8):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never downgrade the referee to save money.
2. D15 (index l.26: **active**; DECISIONS.md l.278):
   > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
3. D18 (index l.32: **active**; DECISIONS.md l.333):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.

### 5. One trap that bit this lane, and the check that prevents it
- Trap (successor 10, FBP-1 / FBP-2): a bound's proof silently assumed the generic case (no self-loop at o; o ≠ c_θ). Check: in every
  bound, test the corner cases explicitly with my own probe: self-loop at o, o = c_θ, |U| = 2; and for every hypothesis a packet
  calls vacuous or unreached, report my own count with the file set, never the packet's word (N-ENT-2, N-NEB-2 lessons).
- Process trap (successor 10): `pkill -f` in the same shell killed its own wait loop (exit 144). Check: never pkill -f from the shell
  that runs the loop; keep each Bash wait < 600 s.
- Again this restart: the clone started stale (73b46eb8); checked `git rev-parse HEAD origin/claude/referee` equal before any work.

## successor 10 (2026-10-25T16:41Z by date -u; Opus 5.5 under D15/L37, label "(Opus 5.5, D15)"; predecessor successor 9, handover 4859e63e)
Measured from the repository at the time of writing, not recalled.

### 1. Branch, head, distance to trunk
- Branch `claude/referee`. Local branch started STALE at 73b46eb8 (1621 behind origin/claude/referee; `git rev-list --count
  73b46eb8..4859e63e`). `git fetch origin claude/referee`; `git checkout -B claude/referee origin/claude/referee`:
  HEAD = origin/claude/referee = 4859e63e (checked with `git rev-parse`).
- Trunk = remote HEAD `claude/vibrant-johnson-nxvvxo` (`git ls-remote --symref origin HEAD`) at f7b6e688 ("Lead: REFEREE NEB/LV §Cs
  merged ..."). Before merging: 1 ahead / 71 behind trunk, merge-base 46a80300.
- Merged trunk with `git merge --no-ff` (efe0ab7a): 2 ahead / 0 behind before this file's commit.
- Oink: scripts/setup_oink.sh built 8fbf0a7 into tools/oink/build, exit 0.

### 2. Open work and next step (notebook "HANDOVER (successor 9 -> successor 10)")
- P-N5-PFZ-ext (b3702b1b, pin c61ecc4): my report docs/referee/R-N5-PFZ.md (all SIGNED except ext BRK-POLY′ (i): SIGNED WITH GAP
  PFZ-1, repair in §7). Main-packet §C done (vs R2 37e55fde: identical). Next: ext §C in R-N5-PFZ.md once the Lead names
  REFEREE-2 10's FINAL SHA for the ext review; central question: does R2 find PFZ-1, and does their repair agree with mine
  (refined θ-LEN ≤ |A_low| − [o low]; ρ ≥ 1 ⇒ a high u ≠ o in U)?
- P-N5-LV2 (3b23a41f, pin 283bcb6): my report docs/referee/R-N5-LV2.md + addendum (all SIGNED with stated conditions, no gaps;
  LV2-N1). Next: LV2 §C in R-N5-LV2.md after REFEREE-2 10's report and the Lead's SHA. No docs/referee-2/R2-N5-LV2* on trunk yet.
- Trunk log since 4859e63e shows REFEREE-2 10 at handover (490dd0ea, 5ca9ac38: "PFZ-ext and LV2 in flight, not started"). Nothing
  else is open for me.

### 3. docs/GAPS.md rows relevant to me (trunk f7b6e688)
- REFEREE owns no row. The row my packets feed: G-N5-TIME (l.11), major, owner L-NEW ("referees later"), **open**. Last UPDATE
  15:55Z: RESULTS R40 LANDED (P-N5-ENT + fixes); "Open: level −1 (P-N5-LV signed by both, P-N5-LV2 in review ...), ...
  out-of-scope fallbacks (P-N5-NEB signed by both; P-N5-PFZ in review), θ_ph / ρ, OTHER states, S4a steps, phases, X."
- G-N5-TERM (l.16) closed (RESULTS R15).

### 4. Three owner rulings that most constrain me (verbatim, docs/DECISIONS.md), with DECISIONS-INDEX status
1. D1 (index l.5: **active**; DECISIONS.md l.7-8):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never downgrade the referee to save money.
2. D15 (index l.26: **active**; DECISIONS.md l.278):
   > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
3. D18 (index l.32: **active**; DECISIONS.md l.333):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.

### 5. One trap that bit this lane, and the check that prevents it
- Trap (successor 9): Lead messages queue up while a referee works; successor 9 read the 15:34Z / 15:41Z / 15:59Z messages late and
  did P-N5-LV before P-N5-PFZ, against the Lead's order. Check: ReadNotifications before each push and before starting the next
  packet (done before this push: queue empty).
- Content trap the predecessor caught (PFZ-1), kept as a check: in an epoch/phase counting proof, list the transitions at each epoch
  boundary and confirm each is charged exactly once (a θ-change at a P(θ) change is still a θ-change; pfz_probe.py counts θ-runs
  and P-epochs separately). Misses N-NEB-2 / N-LV-1 (found only by REFEREE-2): count every hypothesis's occurrences, say which are
  vacuous "in MY data", with the file set.
- Again this restart: the clone started stale (73b46eb8). And a peer file present is not final: docs/referee-2/R2-N5-PFZ.md is on my
  tree after the trunk merge (main-packet review, 37e55fde); the ext §C compares only against the SHA the Lead names.

## successor 9 (2026-10-25T14:45Z by date -u; Opus 5.5 under D15/L37, label "(Opus 5.5, D15)"; predecessor successor 8, handover 4efa2a6f)
Measured from the repository at the time of writing, not recalled.

### 1. Branch, head, distance to trunk
- Branch `claude/referee`. Local branch started STALE (1505 behind origin/claude/referee). `git fetch origin claude/referee` and
  `git checkout -B claude/referee origin/claude/referee`: HEAD = origin/claude/referee = 4efa2a6f (checked with `git rev-parse`).
- Trunk = remote HEAD `claude/vibrant-johnson-nxvvxo` (`git ls-remote --symref origin HEAD`) at efa00f59 (Lead: R39 draft -> C48).
  Before merging: 3 ahead / 8 behind trunk (merge-base 1aeff933). The 8 behind: REFEREE-2 succ. 9's R2-N5-ENT (b7df84b8), OUT §C
  (2a9e8db0), ENT §C (f33884e6), their merges, and Lead commits 3a086cca, efa00f59.
- Merged trunk with `git merge --no-ff` (00bea06f): 4 ahead / 0 behind before this file's commit (merge-base efa00f59).

### 2. Open work and next step of each
- Nothing in flight. Successor 8's table: RL (R37), P1 (R36), SCOPE (R38), OUT (R39 draft, CHECKER C48), ENT all signed with §C done;
  REFEREE-2's OUT and ENT §Cs (2a9e8db0, f33884e6) report identical verdicts and an empty gap map, so nothing returns to me from them.
- Next: wait for the Lead's GO and next packet brief. On a new packet: verify the packet sha1 at its pin, build Oink
  (scripts/setup_oink.sh; not yet built in this container), reuse own tools in docs/referee/scratch/ (rl_engine.py, rl_probe.py, NO
  lane imports), report under docs/referee/R-<packet>.md before reading any docs/referee-2/R2-<packet>.
- Small item seen in LEAD-STATE 14:24Z (CHECKER 30fda11): my lane's SCOPE climb maxima rest on report text only, no committed log.
  If the Lead wants it, I can re-run the SCOPE climbs and commit the log under docs/referee/ (not started; awaiting routing).

### 3. docs/GAPS.md rows relevant to me (trunk efa00f59)
- REFEREE owns no row. The row my packets feed: G-N5-TIME | major | owner L-NEW (L-LIT T22; referees later) | **open**. Latest
  UPDATE 14:16Z: R38 (P-N5-SCOPE) LANDED; open: out-of-SN fallbacks (OUT-POLY CONJECTURE; P-N5-OUT signed by both referees, landing
  next = R39), NJB = ENT, REL(S), level −1. Related closed: G-N5-TERM (R15). DTL rows (GAP-A, GAP-C, G-S5-6, G-NEST) open but paused (D18/L40).

### 4. Three owner rulings that most constrain me (verbatim, docs/DECISIONS.md), with DECISIONS-INDEX status
1. D1 (index l.5: **active**, 2026-10-14; DECISIONS.md l.7): "A claimed polynomial algorithm is far more likely to be wrong than right.
   Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below."
2. D15 (index l.26: **active**, 2026-10-22; DECISIONS.md l.278): "q18 b. , q16 b,c. BUt I dont want it to ask these questions from me.
   Be autonomous, reason about it"
3. D18 (index l.32: **active**, 2026-10-24; DECISIONS.md l.333): "Focus on N5 and work toward proving it. Explore novel approaches,
   especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable
   assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from
   conjectures and open problems."

### 5. One trap that bit this lane, and the check that prevents it
- Trap (successor 8, N-ENT-2, missed by me, caught by REFEREE-2): copying a packet's "vacuous in data" line. REFEREE-2 found the NJB-A
  hypothesis actually occurs (698 / 601 / 701 cases). Check: for every hypothesis a packet calls vacuous or unreached, count its
  occurrences with my own probe and report the count, never the packet's word.
- Also again this restart: the clone started stale (1505 behind origin/claude/referee); checked `git rev-parse HEAD origin/claude/referee`
  equal before any work.

## successor 6 (2026-10-25T01:24Z by date -u; Opus 5.5 under D15/L37, label "(Opus 5.5, D15)"; predecessor successor 5, handover bb6f60f5)
Measured from the repository at the time of writing, not recalled.

### 1. Branch, head, distance to trunk
- Branch `claude/referee`. Local branch was STALE (73b46eb8, 672 behind origin). After `git fetch origin claude/referee
  claude/vibrant-johnson-nxvvxo` and `git merge --ff-only origin/claude/referee`: HEAD = origin/claude/referee = bb6f60f5.
- `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` -> 2 ahead, 16 behind (trunk 32f0a5e2;
  merge-base 82ba756f). The 2 ahead: 94df88bc (trunk merge) and bb6f60f5 (R-N5-LP §C). The 16 behind are Lead/lane merges
  (latest 32f0a5e2; includes L-NEW's P-N5-LP fixes file 459660c3).
- UPDATE 01:30Z (date -u): my first push was rejected: origin/claude/referee had moved to 2a0cb306 (predecessor successor 5,
  session_01VQrdgN…, 01:19Z: "R-N5-LP Part 2 addendum: SO-1 closed", via R2-N5-FB §C.3, referee-2 eb10cf7). Merged it with a
  normal merge (afa95369). Now 6 ahead / 14 behind trunk 32f0a5e2, merge-base 956359fc (before this file's commit).

### 2. Open work and next step of each
- In flight: none. Routed by the Lead's brief, waiting for GO: REFEREE's §C on packet P-N5-SO, object docs/new/P-N5-SO-box32.md
  at pin 1ef02bb (ancestor of HEAD; `git show 1ef02bb:docs/new/P-N5-SO-box32.md | sha1sum` = deb5ee4422da3ab7389ce35e4542977927b53886,
  54 lines: matches the brief). Inputs: my predecessor's review = docs/referee/R-N5-LP.md Part 2 (dcb4119; TH with SO-1 = dependency
  on R-N5-FB §4.2 full-minimiser proof, SO signed, XJ with XJ-1: f = O(n⁴(1+X)), not n³); REFEREE-2's R2-N5-LP.md §8 (ba67f41) and
  R2-N5-FB.md §C.3. Next step after GO: compare the two reviews row by row, write the joint gap map (one fixes-file line per row),
  rule on whether SO-1 is closed by REFEREE-2's adoption of the §4.2 proof (re-reading §4.2 myself; the predecessor's addendum
  2a0cb306 already says CLOSED and Lemma TH SIGNED: I check that independently, I do not inherit it), in docs/referee/R-N5-LP.md as
  §C-SO (or a section the Lead names). Probes, if any, assert exactly one Odd vertex with out-degree > 1.
- Earlier packets (P-N5-U1, FB, U23, LP; R19-R22, Z) all signed with §C done (notebook table). Open items held: none routed.
- Before running probes: rebuild Oink (scripts/setup_oink.sh; tools/ is gitignored).

### 3. docs/GAPS.md rows relevant to me (trunk 32f0a5e2)
- REFEREE owns no row. The row my packets feed: G-N5-TIME, major, owner L-NEW ("referees later"), OPEN. Last update: RESULTS R26
  landed; L-NEW box 32 packet P-N5-LP (Theorem LP, Corollary LP′, phase O(m n⁵ (1 + S_o + X + K)) on 𝒞^1O) with both referees;
  (KW-M) FALSE, NO-WAKE FALSE; S_o, X, K OPEN; L-SI (CL-S) CONJECTURE.
- G-N5-TERM closed (RESULTS R15). DTL rows GAP-A, GAP-C, G-S5-6, G-NEST open but DTL paused (D18/L40).

### 4. Three owner rulings that most constrain me (verbatim, docs/DECISIONS.md), with DECISIONS-INDEX status
1. D1 (index: active; docs/DECISIONS.md lines 7-8):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never downgrade the referee to save money.
2. D15 (index: active; Lead reading L37 active: referees on Opus 5.5, label "(Opus 5.5, D15)"):
   > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
3. D18 (index: active; Lead reading L40 active: labels PROVED (by whom) / CONJECTURE / OPEN):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.

### 5. One trap that bit this lane, and the check that prevents it
- Trap (R-N5-LP / R-N5-FB, notebook lesson): VJ00 Lemma 5.8 "maximum ⇒ no improvement" (2 ⇒ 3) and "SPEC's σ̄ is VJ00's minimiser"
  both FAIL at own cycle nodes (FIX 2 DFS): Lemma DF was false (docs/referee/R-N5-LP/df_cex.pg, n 11) and CAP-1 had 925 cases.
  This is exactly what SO-1 turns on. Check: before signing any step that uses σ̄ as a minimiser or cites Lemma 5.8, test it at own
  cycle nodes explicitly (fb_probe.py / lp_probe.py modes), and verify which form (coarse vs full minimiser) the step uses.
- Also again this restart: stale local branch (73b46eb8, 672 behind); check `git rev-parse HEAD origin/claude/referee` equal before work.
