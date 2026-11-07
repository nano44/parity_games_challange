# P-N5-GATE fixes (box 120; APPEND-ONLY)
- Frozen packet: docs/new/P-N5-GATE-box120.md at l-new 516717da, sha1 ac88915dfb07fc8b5644db99762671eee8ef7312 (135 lines). Line
  docs/new/P-N5-GATE-line.txt, sha1 245ce9feac30a6462ec31edca2c724e1409d9f06. Neither is edited.
- Author: L-NEW successor 44 (Opus 5.5), D14 / D18. Newest entry last.

## F0 (2026-11-01 01:3xZ by date -u): reports, verdicts, item map
- REFEREE 21: docs/referee/R-N5-GATE.md, claude/referee c9bc161c (file sha1 c5fff4c5; unchanged at 65b74579).
  - SIGNS SETTLE-MON, BRACKET-MON, SETTLE-RED / BRACKET-RED, CONSISTENT-RED and its Corollary. Confirms the §6 DEAD on both instances.
    No gap.
  - Line: MATCHES. Precision P-1 to P-4, optional.
- REFEREE-2 25: docs/referee-2/R2-N5-GATE.md, claude/referee-2 e35e8280 (file sha1 70484101).
  - SIGNS every item. No gap in the mathematics.
  - Line: REQUIRED GATE-L1. Optional P-1 to P-3. Note N-1.
- Lead reading on the Lemma S citation (Lead brief to successor 44, 2026-11-01): «Cite it as «RESULTS R18 (d) Lemma S (a)-(b) (its proof
  uses no 𝒞^1O hypothesis: VJ00 (11), Lemma R, R15 (a), (d))». That meets REFEREE P-4 and REFEREE-2 P-1 / P-2.»
- Line L-1: docs/new/P-N5-GATE-line-L1.txt (one line, no heading marker).

| item | source | met by |
| --- | --- | --- |
| GATE-L1 (lend107_n32: 106, not 107) | REFEREE-2 §4, §5 (REQUIRED) | entry 1 (a); line L-1 |
| N-1 (packet §7: 116 runs, not 118) | REFEREE-2 §5 (note) | entry 1 (a); recorded here only (DATA is not in the line) |
| P-1 (B vs B_k) | REFEREE §8 | entry 1 (b); line L-1 |
| P-2 (τ := τ_(k0)) | REFEREE §8 | entry 1 (c); line L-1 |
| P-3 (local index j) | REFEREE-2 §5 | entry 1 (c); line L-1 |
| P-3 (pin the DEAD instances) | REFEREE §8 | entry 1 (d); line L-1 |
| P-4 / §1 precision (why Lemma S holds on every game) | REFEREE §1, §8 | entry 1 (e); line L-1, in the Lead's citation form |
| P-1 (add R15 (d)) | REFEREE-2 §2, §5 | entry 1 (e); line L-1 |
| P-2 (Lemma S proof uses no 𝒞^1O hypothesis) | REFEREE-2 §2, §5 | entry 1 (e); line L-1. Formal status: the Lead's reading above |

Not applied: none. Two forms were not taken as suggested; the reasons are in entry 1 (c) and (e).

## Entry 1: GATE-L1, N-1 and the precision items
### REFEREE (verbatim, docs/referee/R-N5-GATE.md l. 36-38 and l. 99-105, claude/referee c9bc161c)
>   - Precision: the landed R18 entry names its setting «𝒞^1O» in its Setting line. A line using Lemma S «on every game» should say why,
>     as this line does («used on every game»). CHECKER may want the citation «(proof: VJ00 (11), Lemma R, R15 (a), (d); no 𝒞^1O
>     hypothesis)».

> - Precision (not required):
>   - P-1. Notation clash: B := (n² − n + 1)(n + m) and B_k := Σ_v lcp(…); «BG := … at none of which … B rises» means B_k. Write «B_k rises»
>     (or rename one of them).
>   - P-2. In CONSISTENT-RED, «τ_k = τ» binds τ as the common value. «τ := τ_(k0)» would be explicit.
>   - P-3. The DEAD clause names its instances without path or sha1. Add experiments/new/box116/inst/fbg_K12_m6_m24.pg (2f035ca0…) with
>     fbg_K12_m6_m24_fixed.start (9f03f81f…), and experiments/n5-epoch/instances/lend107_n32 (ab4c9811…, start 9df4ea2c…).
>   - P-4. The Lemma S premise: see §1's precision.

### REFEREE-2 (verbatim, docs/referee-2/R2-N5-GATE.md l. 40-45, l. 101-107 and l. 112-118, claude/referee-2 e35e8280)
> - Formal status (NEEDS): R18's heading scopes the R-line to o-acyclic 𝒞^1O, while item (d) itself is stated and proved class-free.
>   - Citing «R18 (d) … used on every game» is therefore correct as mathematics.
>   - Whether a CHECKER accepts a class-free item of a subclass R-line as a premise «on every game» is a Lead reading (cf. L42).
>   - I recommend the line say so explicitly, e.g. «R18 (d) (Lemma R and Lemma S (a)-(b), whose proof (box 21 §2.1-§2.2) uses no 𝒞^1O
>     hypothesis)».
>   - Also add R15 (d) to [SQZ]'s citation, as the packet's parenthesis «τ moves only along Iτ» already says (P-1 = R18's S2).

>   - lend107_n32.pg (ab4c9811b311…) with lend107_n32.start (9df4ea2ceafe…): n 32, K 112, 10 fallbacks. The τ-stretch is transitions 1-109,
>     with λ_W changing at transitions 1 and 108 (logs/lend107_phases.txt, tool phases.py).
>     - So the phase's in-phase transitions are 2-107: **106** W-changing, all > 31.
>     - The lane's box118/gate.py assigns a transition to the phase of its FIRST state (`lam` from W0 only), which also counts the closing
>       transition 108. That gives 107.
>     - The packet's definition («consecutive transitions at whose states λ_W is constant») gives 106.
>     - The DEAD stands either way.

> | id | where | kind | status |
> | --- | --- | --- | --- |
> | GATE-L1 | line DEAD clause (and packet §6 instance 2) | **REQUIRED**: «lend107_n32, 107 > 31» → «106 > 31» under the line's own λ_W-phase definition. Alternatively, redefine the phase by first states (then fbg is unchanged and lend107 is 107) | open (line) |
> | P-1 | packet §1 [SQZ] / line R18 (d) | cite R15 (d) with R15 (a) for the monotone halves (R18's S2) | optional |
> | P-2 | line R18 (d) | state that Lemma S (a)-(b)'s proof uses no 𝒞^1O hypothesis (§2) | recommended; formal status is a Lead reading |
> | P-3 | line CONSISTENT-RED | «τ_k = τ for k0 ≤ k ≤ k1» uses k as a local index while the binder already has «every transition k → k + 1». Write «τ_j = τ for k0 ≤ j ≤ k1» and «every transition j → j + 1 with k0 ≤ j < k1» | optional precision |
> | N-1 | packet §7 DATA | «118 runs exceed» is 116 under the in-phase definition (same cause as GATE-L1). Not to sign | note |

### Repairs (line L-1, docs/new/P-N5-GATE-line-L1.txt)
- (a) GATE-L1, taken in its first form (keep the line's λ_W-phase definition, correct the count).
  - «lend107_n32, 107 > 31» becomes «… lend107_n32.pg (ab4c9811…) with lend107_n32.start (9df4ea2c…), n = 32, 106 > 31».
  - Cause, confirmed by my own recount: box118/gate.py groups a transition k → k + 1 by λ_W at its FIRST state only. So it also counts each
    phase's closing transition, where λ_W changes. The packet's and the line's definition needs λ_W equal at both states.
  - Packet §6 instance 2 should read 106, not 107. Packet §7's «118 runs exceed the §6 bound» should read 116 (N-1). Both are recorded here;
    the frozen packet is not edited. The DEAD stands under either grouping.
  - fbg_K12_m6_m24 is unchanged: 403 under both groupings (one phase, transitions 1-403).
  - Tool: experiments/new/box120/inphase.py G START prints both counts (maxFirst = gate.py's grouping, maxInPhase = the line's).
  - Pins: experiments/new/box120/pincheck.sh → box120/pincheck.txt.
    - lend107_n32: maxFirst 107, maxInPhase 106, phase = transitions 2-107. fbg_K12_m6_m24: 403 / 403, phase = transitions 1-403.
    - Oink 8fbf0a7 --zlk and --tl «solution verified» on both; N5's regions = Oink's (box107/pinwin.py, AGREE True).
    - L-COMP's n5b and n5x give identical state sequences (112 / 404 iterations; 10 / 0 fallbacks).
  - Corpus: experiments/new/box120/runinphase.sh (L-SI box 53's 1,132 runs, box 118's lists and repaired starts) → box120/i_sbcg.txt,
    i_alt.txt.
    - 118 runs exceed n − 1 under the first-state grouping (= box 118's figure) and 116 under the in-phase one (= REFEREE-2's).
    - maxFirst equals box 118's maxWchPerPhase on every compared run (0 mismatches). The two groupings differ by at most 1.
- (b) REFEREE P-1. «at none of which SET grows (B rises)» becomes «at none of which SET_k grows (B_k rises)». The constant B :=
  (n² − n + 1)(n + m) keeps its name: it is the only use without an index, and both referees read it so.
- (c) REFEREE P-2 and REFEREE-2 P-3, merged: «(Lemma CONSISTENT-RED) with τ := τ_(k0), if τ_j = τ for k0 ≤ j ≤ k1 and every transition
  j → j + 1 with k0 ≤ j < k1 is consistent, …».
  - j is bound locally by «for k0 ≤ j ≤ k1» / «with k0 ≤ j < k1». SETTLE-MON's j is bound locally in its own clause («for every j ≥ k»).
    The two scopes do not meet. I kept REFEREE-2's letter rather than a new one, so the line has no fresh symbol.
- (d) REFEREE P-3. The DEAD clause now pins both instances by path and sha1 prefix: experiments/new/box116/inst/fbg_K12_m6_m24.pg (sha1
  2f035ca0…) with fbg_K12_m6_m24_fixed.start (9f03f81f…, L-NEW box 116b), and experiments/n5-epoch/instances/lend107_n32.pg (ab4c9811…)
  with lend107_n32.start (9df4ea2c…). «n = 32» is added for lend107, matching the fbg clause's «n = 290».
  - Full sha1s: 2f035ca0a99946217bde6b740b87dd77bf884baf, 9f03f81fae5984fe92290f11c90dfaac3aecd419,
    ab4c9811b311e303e5d41a9e923766a4b3fdae33, 9df4ea2ceafe43c4a7d88ef1e1f262101d7f0c35 (sha1sum at this commit).
- (e) REFEREE §1 / P-4, REFEREE-2 P-1 / P-2: the Lead's citation form.
  - «R18 (d) (Lemma R and Lemma S (a)-(b), the sandwich, used on every game)» becomes «R18 (d) (Lemma R and Lemma S (a)-(b), the sandwich,
    used on every game: its proof uses no 𝒞^1O hypothesis: VJ00 (11), Lemma R, R15 (a), (d))».
  - This names R15 (d) (REFEREE-2 P-1) and states the class-free proof (REFEREE-2 P-2, REFEREE P-4).
  - Not taken: REFEREE-2's example form «whose proof (box 21 §2.1-§2.2) …». It cites a lane file in a line; the Lead's form cites only
    landed labels and VJ00.
  - Formal status: REFEREE-2 asked for a Lead reading on citing a class-free item of the subclass R-line R18 «on every game». The Lead's
    reading above is the one applied. It is the Lead's, not mine.
- (f) Provenance tail: «(P-N5-GATE, docs/new/P-N5-GATE-box120.md; L-NEW successor 43)» becomes «(P-N5-GATE, docs/new/P-N5-GATE-box120.md
  with its fixes entry 1, docs/new/P-N5-GATE-fixes-box120.md; L-NEW successors 43-44)».
- Nothing else changes. The L41 clause («the premises R17 (F1) and R18 (d) Lemma S (a) rest on derivations written by REFEREE and REFEREE-2
  (R17 (a))») stays word for word.

### Pre-check of L-1 against CHECKER's recurring E-items
- Free symbols: the new symbols are j (bound locally, (c)), τ (defined := τ_(k0)) and SET_k, B_k (defined in the line). 𝒞^1O and VJ00 (11)
  are citation labels. None free.
- DATA: the line states no DATA. The corpus count 116 is recorded here only.
- Asymptotic DEADs: none (L43). The only DEAD is at the explicit bound n − 1, with both counts and both instances pinned.
- L41: no proof in this packet is referee-originated. The premise clause for R17 (F1) / R18 (d) Lemma S (a) is unchanged.
- Landed labels: R15 (a), (d), R17, R18 (c) / (d), R57, R93, R99. No lane commit is pinned. The instance paths are files, not premises.
- TARGET.md scope words: unchanged («REDUCTIONS and EQUIVALENCES», «no count is bounded here», «G-N5-TIME stays OPEN», «not M3, not a
  step-4 pass, not a TARGET.md claim»).

### DONE / FINDINGS / NEEDS (entry 1)
- DONE: this file; line L-1; experiments/new/box120/{inphase.py, pincheck.sh, pincheck.txt, runinphase.sh, i_sbcg.txt, i_alt.txt}.
- FINDINGS: GATE-L1 confirmed (lend107 106 in-phase, 107 first-state); N-1 confirmed (116 vs 118); every precision item applied.
- NEEDS: Lead: route line L-1 to both referees for a word-diff verdict, then CHECKER.
