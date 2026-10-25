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
