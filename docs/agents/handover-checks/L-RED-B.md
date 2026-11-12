# Start check: L-RED-B (second adversary lane; model and effort: see the roster in docs/NOW.md; D1 / D18 / D21, Lead reading L51; written 2026-11-12 12:57Z by date -u)
Every answer is measured from the repository (commands named), not recalled. No predecessor: this is a new lane.
Target (my only object): L-NEW 72's box 208, claude/l-new 8db300fe3fd8e868e61851a9bff76673146d2f10, docs/new/N5-LEVEL-box208.md.
Its sha1, measured here on `git show 8db300fe…:docs/new/N5-LEVEL-box208.md`: 55e6538110d379fc695f1f06efbd1d7b3df97494 (502 lines).

## 1. Branch and head
- `git branch --show-current` -> claude/l-red-b.
- `git rev-parse HEAD origin/claude/vibrant-johnson-nxvvxo` -> both 471aba45214c9b4009332ef1d498dd5dbc42f3cb (trunk head; 0 ahead / 0 behind
  before this file's commit, by `git rev-list --left-right --count`).
- Read-only refs fetched: origin/claude/l-new 8db300fe3fd8e868e61851a9bff76673146d2f10, origin/claude/l-red
  ef026a6157690ad9f508eef06a60f759329901ee, origin/claude/l-formal 9dde15270248f8faa73bdd4ffc373ead5dcad3de (`git rev-parse`).
- Files I own: docs/red-b/, experiments/red-b/, notes/L-RED-B.md, and this file. Nothing else is edited.

## 2. Attack plan (5 lines)
1. Proof read (method a): re-quote every premise of box 208 from trunk docs/RESULTS.md (R104, R118, R121, R123, R126) and from the landed
   packets, then check (K1)-(K5), (L1)-(L5), (C1)-(C4), (P1)-(P7) step by step; scope watch: IDEAL-CYC vs Γ3, class = (Λ, E), Howard ties.
2. Own engine (method b): IDEAL-CYC written from R104 / R118 (a) and P-N5-REALIZE §3.1 only (own builder, own VJ valuation, own Odd
   best reply), cross-checked on small games against brute force over all Odd strategies; no lane's code is imported.
3. Own counters on that engine: Φ monotone, stall ⇒ Ξ_(σ_b)-cycle inside FRONT, plateau length vs N + 2M + 5, number of Φ values vs P,
   T_CYC vs P(N + 2M + 6) + N; each counter with a control that must fire.
4. Constructions (method c): exhaustive / dense random search at N + M ≤ ~12, then climbs on plateau length and on T_CYC / bound; targets:
   ties in Howard's choice, gates with both faces inside Y, e-faces in the front, K2 and the core, level-0 gates, Ξ self-loops.
5. BR-SEG-G fit: check sub-game H of PLATEAU against the hypotheses of R118 (i) and of L-FORMAL's Lean statement (claude/l-formal,
   lean/lemmas/PGLemmas/Statements.lean); verdict per lemma to the Lead: SURVIVES / GAP (wording, step) / DEAD (instance, sha1, numbers).

## 3. docs/GAPS.md rows
- Owned: none.
- Worked against: G-N5-TIME (docs/GAPS.md line 11: severity major, owner «L-NEW (L-LIT T22; referees later)», status **open**).
  Box 208's scope line keeps it open: «IDEAL-CYC on Γ(G) only; not Γ3, not N5′-xi, not M4; G-N5-TIME stays OPEN.»

## 4. Owner rulings, verbatim
- D1 (docs/DECISIONS.md line 5; full text docs/decisions/D001-launch-brief.md line 114), DECISIONS-INDEX status **active**:
  > Spawn no attack lane before I approve it.
- D1 (docs/DECISIONS.md line 7), same ruling:
  > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
- D18 (docs/DECISIONS.md line 333), DECISIONS-INDEX status **active**:
  > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
- The brief says this lane was approved by the owner on 2026-11-12. I have not seen the owner's words for that approval; the Lead holds them.

## 5. One trap I will avoid
- CLAUDE.md, Traps: «A "counterexample" from an unfaithful implementation is not a counterexample: the referee checks pseudocode against the
  paper first.» My engine is new, so a violation it reports is first a suspect bug: before any DEAD verdict I re-derive the instance by
  brute force (all Odd strategies, values compared by the VJ order as quoted from R118's premise [VJ]) and freeze it with its sha1.
  The mirror trap: zero violations on short runs test the logic, not the bound (box 208 §7 says the same of its own data).

## 6. State at this commit
- No CPU job started. No long CPU job starts before the Lead's «go». Reading and engine writing proceed while the push runs.
- Independence: I have not read L-RED 66's, REFEREE 32's or L-COMP 19's reports on box 208, and will not before my verdict is sent.
