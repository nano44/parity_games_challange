# R2-N5-SETTLE-L4: word-diff of the P-N5-SETTLE line, revision L-4 (REFEREE-2 successor 24, Opus 5.5, D15)
- Object: docs/si/P-N5-SETTLE-line-L4.txt @ l-si b04a1bbb, sha1 6ed61d848613df4b501b785e9418c3e2c1e8fc43 (re-hashed: match).
- Compared with L-2 (86becaa0, sha1 1fcb33c5), which I found MATCHES at dd2333a2 (R2-N5-SETTLE-L2.md). On the Lead's word, L-3 is not
  diffed separately.
- Token diff (difflib over whitespace tokens, 805 → 844 tokens) has four changes and nothing else.

## 1. Changes
| change | item | check |
| --- | --- | --- |
| R57 gloss «… one-player arena H_t)» → «… H_t, H_t := S4a's arena at t (Even keeps σ_t ∪ Iσ_t, Odd follows τ_t))» | D-2 | ✓ H_t is now defined, and t is its parameter. Precision P-1 below |
| «… fixed on F;» → «… fixed on F and \|F\| its number of transitions;» | D-1 | ✓ \|F\| is bound. It is used in RUN-COUNT and HEAD-RED |
| RUN-SETTLE proof note: «… with W_(k+1)); Cases 2, 2b via Lemma ONE-STEP (REFEREE-2 R2-N5-SRC §3.2, claude/referee-2 e8c1b62d; signed by REFEREE R-N5-SETTLE Addendum 1, claude/referee 8951ef7c))» | G-SRC-1 | ✓ see below |
| «entries 1-2)» → «entries 1-4)» | bookkeeping | ✓ |
- The ONE-STEP citation is right in every part:
  - R2-N5-SRC.md §3.2 at e8c1b62d is the lemma, its proof, and its two instantiations (Case 2 at t = k − 1 with z = b; Case 2b at
    t = k with z = a).
  - REFEREE's R-N5-SETTLE.md Addendum 1 at 8951ef7c (an ancestor of origin/claude/referee) reads «(2) Lemma ONE-STEP … SIGNED (Opus 5.5,
    D15)», with REFEREE's own check, and confirms both instantiations.
  - Under L41 this is a referee-originated proof signed by its author and by the other referee.

## 2. Strict symbol test (changed text)
| symbol | binder |
| --- | --- |
| t in H_t, σ_t, Iσ_t, τ_t | the parameter of «H_t := S4a's arena at t» (Iσ_t by «for a state k: Iσ_k := …») |
| \|F\| | «\|F\| its number of transitions», F bound by «every W-run F of it» |
| ONE-STEP, G-SRC-1 | named lemmas with file, section and commit, like the line's other cited labels |
No new free symbol.

## 3. Items
- **SET-L4-1 (REQUIRED, L41).** RUN-SETTLE's Cases 2 and 2b now rest on a referee-originated proof (ONE-STEP, author REFEREE-2 24,
  signed by REFEREE 20).
  - Lead reading L41 asks the entry's scope tail to say the proof is referee-originated.
  - L-4's tail («— a REDUCTION (no count is bounded here; … XCN-POLY)») does not say it. «referee-originated» occurs 0 times in L-4.
  - The sibling SRC line L-3 has it («Lemma ONE-STEP is referee-originated»).
  - Fix: in the tail, after «XCN-POLY», add «; Lemma ONE-STEP is referee-originated».
- P-1 (precision). The R57 gloss still reads «for S4a, σ_new is the pointwise optimum of the one-player arena H_t». σ_new is not tied to
  t, and «Even keeps σ_t ∪ Iσ_t» unions a strategy with an edge set.
  - SRC L-2 already uses: «for S4a at a transition t → t + 1, σ_(t+1) is the pointwise optimum of the one-player arena H_t» and «(Even v
    keeps {σ_t(v)} ∪ Iσ_t(v), Odd follows τ_t)».
  - Optional; the reading is unambiguous next to the line's own H_k.

## Verdict
L-4 (6ed61d84): **REQUIRED CHANGE SET-L4-1** (the L41 «referee-originated» scope-tail clause) (Opus 5.5, D15). Everything else
MATCHES. P-1 is optional.
