# Draft RESULTS R94 (Lead, 2026-10-30 17:49:20Z by date -u, read in the same command as the fill of this file; subagent draft; packet, fixes entries 1-3, line files ba09dd26 / L-1 / L-2 / L-3, both reports, both §Cs, REFEREE §C §4-§5 and REFEREE-2's L-3 verdict read at the origin heads fetched at the start of this draft and re-fetched 17:42:05Z (date -u in the same command; heads unchanged: l-new 85c12579, referee 345fcea9, referee-2 4d9a4318, origin trunk d1400cac; local trunk head 8e1a605c); pinned «box 77» and «box 79» FLATSRC blocks re-run 17:38:21Z-17:38:22Z (59d58d0d) and before 17:44:49Z (5027c17c); DATA re-summed 17:38:41Z) — to CHECKER C104 — LANDED in RESULTS Results 2026-10-30 18:40Z (CHECKER C104 5c4d6e45 PASS), after R93
to check: (1) TITLE. The title is the line file docs/new/P-N5-FIXD-box91-line-L3.txt (l-new 59d58d0dd0d60d4fc90bf46db0e4aedf77104d8b,
2026-10-30T16:59:49Z, the file's only commit, sha1 7d22165a7e0cbd1a556cb546d8d3c53efa640956; identical at l-new head 85c12579, at origin
trunk d1400cac and at the local trunk head 8e1a605c; first on trunk by the merge f7be1a10, 17:11:42Z): one line, no outer quotes, no
final period, 2,693 characters (2,787 bytes plus the newline). DEVIATION FROM THE R93 PRECEDENT (no precedent exists): the L-3 file
begins with its own heading marker and lane tag, «### R?? [proposed, P-N5-FIXD, revision L-3] » (44 characters, ending in one space;
the frozen line and L-1, L-2 begin the same way with their own tags). R93's line file (c930e26f, P-N5-WCH-box79-line-W1.txt) has no
such prefix: it begins «N5 on EVERY game», and R93's heading was the level-3 marker, then "R93 [refereed-only] ", then the file. No
draft R83-R93 in docs/agents/ meets a «R?? [» prefix (grep: 0). So this draft strips EXACTLY that 44-character prefix and puts
"### R94 [refereed-only] " in its place; every other byte of the file is kept. The tag is a lane label of the revision, not claim
text: REFEREE §C l. 81 lists «the label «L-3»» as a changed token and gives it no verdict; REFEREE-2 L3 l. 5-11 does not list
it. «2026-10-30» occurs exactly once in the line, in « (2026-10-30) — a REDUCTION» (by script), so NO date is inserted. The
line holds eight "|" characters, «|P|» four times; they stay in the heading (R91's and R93's headings carry "|") and are replaced in
the GAPS UPDATE only (see (8)). The checker fill ", CHECKER PASS (docs/checker/C104.md, checker PENDING)" is appended as in R90-R93
(no space before the comma). The heading was built by script (scratch build94.py: assert the prefix, strip it, prepend
"### R94 [refereed-only] ", append the fill) and re-checked after writing this file: equal, byte for byte. Heading: 2,727 characters,
2,821 bytes; sha1 of the heading line with its newline 342466c41a7665a6654719a557f842ae6f8edb8b.
(2) LINE HISTORY: frozen ba09dd26 (docs/new/P-N5-FIXD-box91-line.txt, l-new 5027c17c, 2,258 characters, the line both referees
reviewed) → L-1 7e99a4a9 (…-line-L1.txt, fe5c9e33, 16:21:52Z, 2,355 characters; fixes entry 1: FIXD-N1, N2, N4) → L-2 d553bbba
(…-line-L2.txt, 9460f011, 16:34:58Z, 2,375 characters; fixes entry 2: R2-L-2, R2-L-3; R2-L-1 = FIXD-N1 already in L-1) → L-3
7d22165a (59d58d0d, 2,693 characters; fixes entry 3: PHASE-RED′ unconditional). ba09dd26, L-1 and L-2 are history, not the title.
Each line file has one commit (git log on l-new). Word diffs measured two ways for this draft (`git diff --no-index
--word-diff=porcelain`; difflib over whitespace tokens):
- ba09dd26 → L-1: 448 → 468 tokens, 7 non-equal opcodes: the tag; «S1-S5;» → «S1-S5, under the standing SPEC premise of RESULTS R57;»
  (N2); «(a)» inserted and «LEX);» → «LEX, COMMON PREFIX);» (N4); «k → k + 1» inserted, «a switched» → «an», «switched at k» inserted
  (N1). = REFEREE-2 §C l. 46-47 («7 replace / insert ops, all of them FIXD-N1, N2, N4, plus the header»).
- L-1 → L-2: 468 → 472 tokens, 3 opcodes: the tag; «τ)» → «τ_t)» (R2-L-3); «every phase P has» inserted (R2-L-2). = REFEREE-2 L3 l. 4;
  REFEREE §C §4 l. 65-72 diffs ba09dd26 → L-2 and lists the union of the two steps.
- L-2 → L-3: 472 → 518 tokens, 8 opcodes: the tag; «(Corollary PHASE-RED′, an implication) if» → «(Theorem FLAT-SW, proof of record
  Theorem SW-KEEP (REFEREE R-N5-FIXD §4b, claude/referee 2c9d8040; signed by REFEREE-2 R2-N5-FIXD-C §C.4, claude/referee-2 73d44f3b),
  from RESULTS R15 (a), (d), the standing SPEC premise of RESULTS R57 and R93 (a))»; «of every N5 run at which Ξ changes at some vertex,
  in particular every transition» inserted; «(any» → «for any»; «P of any N5 run)» → «P,»; «Ξ_k(x) (CONJECTURE FLAT-SW, not proved
  here), then» → «Ξ_k(x); and (Corollary PHASE-RED′)»; «proved by» inserted; «conjecture;» → «referee-originated proof, SW-KEEP, signed
  by both referees;». = fixes entry 3 l. 143-147; = REFEREE §C §5 l. 80-88 («Nothing else changed.»); = REFEREE-2 L3 l. 5-11.
- ba09dd26 → L-3: 13 opcodes, the union. No definition inside the premise parenthesis changes after L-2; every inequality
  (FIXD-MON, PHASE-RED, PHASE-RED′) is token-identical from ba09dd26 to L-3; the PHASE-RED′ conclusion gains only «every phase P has»
  (L-2).
(3) THE LINE AT BOTH REFEREES. L-3 (the title): REFEREE successor 20, docs/referee/R-N5-FIXD-C.md §5 (l. 79-107), appended at 345fcea9
(2026-10-30T17:17:01Z; `git diff --numstat ed3bd945 345fcea9`: +30/−0): l. 79 names the file, l-new 59d58d0d, sha1 7d22165a… and fixes
sha1 eb3bd874…; l. 89 «(b) The clause states exactly what SW-KEEP gives, and no more.»; l. 93 «A transition that changes only τ leaves
Ξ unchanged, so it is not claimed. No transition without a σ-change is claimed.»; l. 105 «No free symbol.»; l. 107 «Verdict: L-3
MATCHES the packet's §2-§4 plus the two-referee-signed FLAT-SW (Opus 5.5, D15). No required change.» REFEREE-2 successor 23,
docs/referee-2/R2-N5-FIXD-L3.md (4d9a4318, 2026-10-30T17:20:00Z, new file, 44 lines, sha1 7c9a7b279f71ce8aab9c9408c24ba688adae144f):
l. 2 «sha1 7d22165a7e0cbd1a556cb546d8d3c53efa640956 (re-hashed: match)»; l. 18-19 «No transition has a Ξ-change without an Even
σ-change.»; l. 32 «Every symbol bound. ✓»; l. 39 «L-3 (7d22165a): **MATCHES** (Opus 5.5, D15). No required change.» TRUNK: 345fcea9 is on
the LOCAL trunk only (merge 5523052e, 17:35:59Z), not on origin trunk d1400cac at 17:42:05Z; 4d9a4318 is on origin/claude/referee-2
only, in NEITHER trunk at 17:42:05Z (`git merge-base --is-ancestor 4d9a4318 HEAD`: rc 1). The Lead merges both before landing.
Earlier lines: ba09dd26: REFEREE l. 26 «MATCHES §2-§4 and claims nothing more. The strict symbol test finds ONE free symbol: k in the
PHASE-RED′ clause (FIXD-N1). The standing premise is missing (FIXD-N2). Citation form (FIXD-N4)», l. 153 «Verdict: MATCHES once
FIXD-N1 and FIXD-N2 are applied.»; REFEREE-2 l. 22 «MATCHES §2-§4 in content | two REQUIRED symbol fixes L-1, L-2 (unbound k,
clause-scope P in PHASE-RED′); precision L-3». L-1: REFEREE-2 §C l. 46-47 and l. 100-101 «(5) Revision L-1 applies FIXD-N1 (= my
L-1), N2 and N4 correctly. My L-2 is still open.» L-2: REFEREE §C l. 75 «Verdict: L-2 MATCHES §2-§4 and every note of both referees
(Opus 5.5, D15).»; REFEREE-2 L3 l. 4 «Both as I asked.» Not revised for L-3 (the L-3 verdicts stand apart from them): REFEREE §C
NEEDS l. 116-117 «Lead: L-2 MATCHES (§4). The next revision (unconditional PHASE-RED′, after REFEREE-2 signs SW-KEEP) needs a
word-diff from me when it is frozen.»; REFEREE-2 §C NEEDS l. 102-103 (asks for the revised line).
(4) CLAIMS SIGNED = the items below, each SIGNED in BOTH referees' reports (re-read for this draft). Brief's candidates checked one by
one; nothing else of the packet or of the reports is in both tables as a claim:
| item | REFEREE (successor 20) | REFEREE-2 (successor 23) |
| --- | --- | --- |
| (a) Definition FIX-DEPTH and Lemma FIXD-MON (packet §2, l. 35-43) | R-N5-FIXD.md l. 21 «SIGNED»; §C l. 9 «agree» | R2-N5-FIXD.md l. 18 «SIGNED» / «none; N-3 (sharper range)»; §C l. 13 «SIGNED by both, no gap» |
| (b) Theorem PHASE-RED (i), (ii), combined (§3, l. 45-59) | l. 22 «SIGNED»; §C l. 10 «agree» | l. 19 «SIGNED» / «none; N-3 (sharper constants)»; §C l. 14 «SIGNED by both, no gap» |
| (c) Theorem FLAT-SW at every Ξ-changing transition of every N5 run, proof of record Theorem SW-KEEP (REFEREE report §4b, l. 57-98; not a packet item) | author: l. 24 «I PROVE it here (Theorem SW-KEEP, §4b), so PHASE-RED′ holds unconditionally»; l. 87 «Corollary FLAT-SW (the packet's CONJECTURE). It holds on every N5 run»; §C l. 20 «two independent proofs»; §C §5 l. 89-100 | §C l. 16 «I SIGN SW-KEEP (C.4)»; §C l. 58 «## C.4 Theorem SW-KEEP (REFEREE §4b): SIGNED (Opus 5.5, D15)»; l. 76-78 «Corollary FLAT-SW … ✓ The conclusion holds at every Ξ-changing transition, in a phase or not.»; l. 79 «Premises: R15 (a), (d), the R57 standing premise, R93 (a) COMMON PREFIX. All landed. No gap.» |
| (c′) second proof of FLAT-SW, in-phase form: Lemma OWN and Corollary FLAT-SW (strong form) (REFEREE-2 report §5, l. 96-135) | §C §3 l. 35 «Lemma OWN: SIGNED (Opus 5.5, D15).»; l. 48 «Corollary FLAT-SW (strong form, in-phase): SIGNED.»; exposition note FIXD-C1 l. 42-45 («not a gap») | author: l. 20 «see §5 (my own proof: FLAT-SW TRUE, one referee)»; l. 97 «PROVED by REFEREE-2 alone, unrefereed by a second party»; L3 l. 25-26 «signed by REFEREE in R-N5-FIXD-C §3, a3aa5b68» |
| (d) Corollary PHASE-RED′ as an implication (§4, l. 61-69) | l. 23 «SIGNED»; §C l. 11 «agree» | l. 20 «SIGNED (implication)»; §C l. 15 «SIGNED by both, no gap» |
| (d) PHASE-RED′ unconditional = (d) with (c) | l. 92-93 «So PHASE-RED′ holds unconditionally»; §C l. 106 «PHASE-RED′ is now a corollary of PHASE-RED and FLAT-SW. The packet's §4 proof applies verbatim with the hypothesis discharged.»; l. 107 (L-3 MATCHES) | l. 130-131 «Consequence (given a second signature): Corollary PHASE-RED′ unconditional»; L3 l. 39 (L-3 MATCHES) |
Two-referee status of FLAT-SW rests on a Lead reading, recorded verbatim: docs/agents/LEAD-STATE.md l. 2090 (entry «16:34Z (date -u,
shell)»): «Lead reading: FLAT-SW two-referee signed iff each referee signs the other's proof (REFEREE-2 checks SW-KEEP; REFEREE checks
OWN §5)»; REFEREE-2 §C.5 l. 89-90 quotes the Lead's message: «it counts as two-referee signed if EACH referee signs at least one proof
the other also signs. You sign SW-KEEP, and REFEREE checks your OWN-based proof (report §5).» Under it, each proof is signed by its
author (the report's own verdict label: REFEREE l. 6 «Every verdict is labelled (Opus 5.5, D15)»; REFEREE-2 l. 1, l. 15) and by the
other referee. LEAD-STATE l. 2092 (16:59Z): «Theorem SW-KEEP SIGNED by REFEREE-2 → FLAT-SW two-referee proved (REFEREE wrote + signed,
REFEREE-2 signed); proof of record SW-KEEP.» For CHECKER: authorship counted as the author's signature is this Lead reading, not an
owner ruling. NOT claims: §1 (REFEREE l. 20 «CHECKED»; REFEREE-2 l. 17 «CHECKED»); §5 DATA, DEAD, READING (REFEREE l. 25 «not
signed»; REFEREE-2 l. 21 «not signed»); FLAT-SW for N5-LZC (REFEREE l. 87, REFEREE-2 l. 131-132 and §C l. 77: true by the same proof,
but the packet claims nothing for N5-LZC, l. 9, and the line is about N5 only); N-3's sharper constants (REFEREE-2 l. 93-94; REFEREE
§C l. 18 «both are correct (I re-derived them). Precision only»); the statements of SW-KEEP (any Switch_I of Ξ_σ-improving edges) and
its «Moreover» clause, of Lemma OWN (equal Odd choices), and the strong form's strict rise: signed by both as proof steps, NOT stated
by the line (REFEREE-2 L3 l. 23-24: «MON makes it a strict rise; the clause does not claim that»); recorded under Claims as proofs.
(5) PREMISE LABELS (stale-label test; docs/RESULTS.md at the local trunk head 8e1a605c = origin trunk d1400cac: sha1
4b0f1c85827afd2689b478fe733c886ed956de3b, 7,792 lines, unchanged since 31f8c8a7, the R93 landing, 11:51:50Z). RESULTS ends at R93:
the last "### R" heading is R93 (l. 6972), «R94» occurs 0 times in RESULTS.md and in GAPS.md, «## Dead ends (kept;» follows at
l. 7272. RESULTS labels in L-3 (grep "R[0-9]+": R15 ×2, R38 ×2, R57 ×2, R93 ×3; «R2» once, inside the file name «R2-N5-FIXD-C», not a
RESULTS label); every one exists:
- R57 (l. 2893): «under the standing SPEC premise of RESULTS R57» (twice: premise list, FLAT-SW clause); the standing premise is R57
  (b) l. 2915-2916 («that S1's procedure realises an optimal σ̄ is VJ00 §6 plus SPEC conformance … (1E-N3 = N-1E-1)»). Bare form as
  in landed R92's title (l. 6656); R93's title adds the 1E-N3 gloss. Match by precedent. Added by FIXD-N2 (REFEREE l. 139-142).
- R15 (l. 624): (a) Lemma A l. 631, (d) l. 640; the packet's [R15] (l. 29-31) quotes both; REFEREE l. 11-12 («verbatim in RESULTS
  R15. I checked them mechanically»); REFEREE-2 l. 17 («4 «» quotes from landed text verbatim»). PHASE-RED's «4n(n − 1)» is (d)'s «at
  most 4n(n−1) consecutive N5 iterations leave both Ωσ and Ωτ unchanged». Match.
- R38 (a) (l. 1825): Remark KEY; the phase as a (λ_Ξ, τ)-phase, glossed in the line; used as in landed R91 and R93 (R93 to-check (5)
  «Match by precedent»); REFEREE l. 147 ««R38 (a)» for the phase definition follows the landed R93 line's usage ✓». Match.
- R93 (a) (l. 7031-7036): Fact REW, Fact LEX, COMMON PREFIX. «R93 (a) (Fact LEX, COMMON PREFIX)» per FIXD-N4; «RESULTS R93 Fact LEX» in
  the CS gloss names the same item. The CS gloss «(reward of the cycle node; … negated when the cycle node has even priority)» is
  byte-identical to the gloss inside R93's title (l. 6972; by script). Match.
- Not RESULTS labels: «Theorem SW-KEEP (REFEREE R-N5-FIXD §4b, claude/referee 2c9d8040; signed by REFEREE-2 R2-N5-FIXD-C §C.4,
  claude/referee-2 73d44f3b)» names a referee file, section and commit; SW-KEEP is not a landed RESULTS item before this entry and
  lands with it as the proof of record of (c). Both citations checked: REFEREE report §4b is «## 4b. Theorem SW-KEEP (REFEREE proof;
  FLAT-SW follows)» (l. 57) at 2c9d8040; REFEREE-2 §C l. 58 is «## C.4 …» at 73d44f3b (the fixes file l. 124 records the Lead's slip
  «R2-N5-FIXD-C §3»; L-3 cites §C.4, right; REFEREE-2 L3 l. 33-34 «the right file, section and commit»).
- No conflict with landed text: R93's entry lists «FIX-DEPTH / FIXD-MON / PHASE-RED» among the trimmed items «Not signed» (RESULTS
  l. 7130-7131; P-N5-WCH §8.1 l. 336-337: «a separate reduction of phase length … Proposed as its own packet if the Lead wants it»).
  R94 is that packet.
(6) SYMBOL TEST of the title (my own strict test of every symbol of L-3, by hand; IN = bound in the line; else the carrier):
| symbol | where |
| --- | --- |
| N5, SPEC S1-S5, «Even», «Odd» | SPEC (named) |
| standing SPEC premise of RESULTS R57; R15 (a), (d); R38 (a); R93 (a) | cited premises, each a landed RESULTS item; see (5) |
| run, states, σ_t, τ_t | IN («a run is the sequence of states (σ_t, τ_t)») |
| transition, t → t + 1 | IN («a transition is written t → t + 1 (states t, t + 1)») |
| n | IN («n the number of vertices of the game»); = TARGET.md §1 l. 8's n |
| Ξ_t, σ̄_t | IN («Ξ_t := Ξ_{σ_t} (SPEC S1: the valuation of every vertex under σ_t and Odd's optimal counterstrategy σ̄_t)»); soft spot: σ̄_t's optimality is glossed in words only (REFEREE-2 L-3 optional, «I do not require it», l. 63-65) |
| λ_Ξ | IN («its cycle-node map») |
| ⊴, ◁, ⊵, ▷ | IN («the SPEC S1 order (better for Even) and its strict and reverse forms») |
| phase, P = [a, b], a, b, «a, …, b» | IN + R38 (a) («a maximal run of consecutive states a, …, b with (λ_Ξ, τ_t) constant») |
| \|P\| | IN («\|P\| := b − a its transitions»); transitions with both states in P (REFEREE l. 50) |
| CS(x), x (a value), «reward», «cycle node», «path set», «length», «priority» | IN + R93 (a) (the gloss; values (c, Q, ℓ) as in R93 (a)) |
| rank r, «the vertex of rank r» | IN («for each rank r from n − 1 down to 0»); ranks are SPEC S1's injective ranks (REFEREE l. 9) |
| DEPTH_t(v), t, v | IN («for a phase P = [a, b], a state t ∈ P and a vertex v»); soft spot: DEPTH and K depend on P (reference Ξ_b) with P not in the subscript; unambiguous, since each state lies in exactly one phase (phases are maximal) |
| K_t, «K» | IN («K_t := Σ_v DEPTH_t(v) ∈ [0, n(n + 2)]»); «K does not change» / «K is non-decreasing» = K_t as a function of t, by use |
| Σ_v | over the vertices, by use |
| CH_P | IN |
| FLATTR_P, «Ξ changes at some vertex» | IN; unsubscripted Ξ at a transition k → k + 1 = Ξ_k vs Ξ_{k+1}, by use |
| «x is switched at k», k | IN («an Even vertex x is switched at k if σ_{k+1}(x) ≠ σ_k(x)»; k local to that definition) |
| FLATSW_P(x) | IN («the transitions k → k + 1 counted in FLATTR_P at which the Even vertex x is switched and Ξ_{k+1}(x) ≠ Ξ_k(x)»; k bound there) |
| t ≤ t′, «every vertex v» (FIXD-MON) | IN |
| 4n(n − 1), n(n + 2) | R15 (d); arithmetic |
| FLAT-SW clause: k, x, P | IN: k by «every transition k → k + 1 of every N5 run», x by «an Even vertex x switched at k», P by «for any phase P» (FIXD-N1 = R2-L-1 fixed in L-1) |
| PHASE-RED′: P, x | IN: P by «every phase P has» (R2-L-2 fixed in L-2); x by «Σ_{x Even}» |
| SW-KEEP, R-N5-FIXD §4b, R2-N5-FIXD-C §C.4, 2c9d8040, 73d44f3b | references, not symbols (REFEREE §C l. 104) |
| Lemma / Theorem / Corollary names | packet §2-§4; FLAT-SW, SW-KEEP: REFEREE report §4b |
| G-N5-TIME, M3, step-4, TARGET.md | scope tail; GAPS l. 11, TARGET.md |
Every symbol of L-3 is bound in the line, by SPEC or by a named landed entry. No free symbol found. Soft spots, as in landed titles:
«x» is used twice with clause-local scope (a value in «CS(x) … of a value x», an Even vertex from «an Even vertex x is switched at k»
on), with no clash inside either clause (R93's title reuses x the same way in its ⊕ gloss); σ̄_t's optimality in words; K and Ξ
unsubscripted by use; DEPTH_t and K_t without P. A mechanical first-occurrence check (scratch symcheck.py: for 28 symbol / binder pairs,
the binder occurs and, for IN symbols, no earlier than the symbol's first occurrence) gives «symbols 28 failures 0»; my first run of it
had one wrong row (Ξ_{k+1}(x) paired with the FLAT-SW clause, whose binder comes later than FLATSW_P(x)'s), corrected to FLATSW_P(x)'s
own «k → k + 1». Like the lane's symtest (REFEREE-2 N-5 at R93), it cannot see clause scope; the test of record is the hand test.
Agreeing tests of L-3: REFEREE §C l. 101-105 «No free symbol.»; REFEREE-2 L3 l. 30-32 «Every symbol bound. ✓».
(7) FLAT-SW: the Lead's words, in order (fixes file quotes, verbatim): entry 1 l. 4, «Lead 16:22Z: «apply the four line notes as a
revised line L-1, with its own sha1 … Do NOT yet make PHASE-RED′ unconditional.»»; entry 2 l. 33, «Lead 16:34Z: «Add fixes entry 2 and
a revision L-2 of the line … PHASE-RED′ stays conditional in L-2.»»; entry 3 l. 72, «Lead 16:59Z: «GO for FIXD fixes entry 3 and line
revision L-3 = L-2 with PHASE-RED′ made UNCONDITIONAL … Record the N-1 withdrawal as a correction of entry 2's erratum … Bind every
symbol.»». LEAD-STATE l. 2092 (16:59Z): «GO to L-NEW 39 for FIXD entry 3 + line L-3 (PHASE-RED′ unconditional via SW-KEEP; N-1
withdrawal).» Proof of record SW-KEEP: REFEREE-2 §C.5 l. 90-92 («For the revised line I propose citing SW-KEEP as the proof of record.
It needs no phase hypothesis and no reading of S1's procedure»); REFEREE-2 L3 l. 35-36 marks naming OWN in the line «Optional … Not
required.»
(8) GAPS: G-N5-TIME (GAPS l. 11) stays open; L-3 names no CONJECTURE (the frozen line's «CONJECTURE FLAT-SW» is now Theorem FLAT-SW).
A line-11 UPDATE is proposed at the end, after R93's UPDATE (the last one on l. 11 at origin trunk d1400cac and at local 8e1a605c:
«UPDATE 2026-10-30 11:51Z: RESULTS R93 (P-N5-WCH; CHECKER C103 cdef102a) …»; docs/GAPS.md sha1 2120e9e24ae6396cb5b8e6faddb7d1919ae3126b,
23 lines, unchanged since 31f8c8a7). Built by script (build94.py) from L-3's clauses only, with R93's construction: «LANDED: » + the
title body with each clause label moved behind its clause, the scope tail «(2026-10-30) — a REDUCTION (X; G-N5-TIME stays open; not M3,
…)» → «: a REDUCTION; X. G-N5-TIME stays open.». The UPDATE must hold no "|" (l. 11 is a table row), and L-3 holds eight, so two
replacements were made that are NOT title text (decision for the Lead / CHECKER): «|P| := b − a its transitions» → «b − a the number
of its transitions»; «|P| ≤» (three times) → «the number of transitions of P ≤» (after R93's «the number of transitions of F ≤»; stiff
but grammatical). Checked by script: with the four labels removed from both and the replacements undone, the UPDATE equals the title
body up to the tail; no "|"; «2026-10-30» once (the stamp).
(9) DATA of record = the packet's §5 DATA (l. 72-79) with fixes errata: FIXD-N3 = N-2 (entry 1 l. 21-22; entry 2 l. 65-66) «6568 of
16183 in-phase transitions (K-rise 9615 + FLATTR 6503 + 65 Ξ-unchanged); Ξ-changing transitions 16118»; entry 2's N-1 erratum VOID
(entry 3 l. 136-138: «the packet's totals K-rise 9615, FLATTR 6503 stand (valid runs from the repaired comp54_n80 start)»; «16071 on
valid runs» void with it). Re-summed for this draft (python3 -I over box79/flatsrc_sbcg.txt + flatsrc_alt.txt and box77/fixd_sbcg.txt
+ fixd_alt.txt from the 59d58d0d archive, 17:38:41Z by date -u, rc 0): 1132 games, 0 unparsed; N5 K-rise 9615, FLATTR 6503, FSW 6503,
Ξ-flat 65; box 77 N5 trans 16183, strict 9615, flat 6568, mono-viol 0; 9615 + 6503 + 65 = 16183, 6503 + 65 = 6568, 16183 − 65 = 16118:
equal to the packet and errata. Maxima FLATTR per phase 91, FLATSW per (x, phase) 14 (both engines). The referees' run sets are
recorded under Data; their totals differ from the lane's by run set only (REFEREE §C l. 30-32; REFEREE-2 §C l. 22-33).
(10) Discrepancies, recorded for CHECKER, no verdict affected: (i) stamps: REFEREE-2 §C l. 2 says its report was «pushed 16:2xZ»; its
commit 4a960ef9 is 16:07:59Z and its first trunk merge 0251cc86 is 16:34:10Z (push time not on record). The other «written» stamps fit
their commits (packet l. 5 «Written 15:33Z-15:36Z», 5027c17c 15:37:22Z; REFEREE l. 6 «report written from 15:58Z», 2c9d8040 16:01:45Z;
REFEREE §C l. 3 «read 16:44Z», a3aa5b68 16:47:28Z; fixes entries 16:21Z / 16:34Z / 16:59Z, commits 16:21:52Z / 16:34:58Z / 16:59:49Z).
(ii) comp54_n80 vertex 11: REFEREE-2 l. 86 and §C l. 34 wrote «σ(11) = 51» / «the FORCED vertex 11»; REFEREE §C l. 23 «Vertex 11 is
ODD (owner 1; «11 134 1 11;»), so this is τ(11)»; REFEREE-2 L3 l. 41-44 corrects to τ(11). My check: comp54_n80.pg l. 13 «11 134 1 11;»
(owner 1), and «11:51» is token 78 of the start file, after «TAU0» (token 74): τ(11). The fixes file's entry 2 quote (l. 53) and
LEAD-STATE l. 2090 carry «σ(11)» as quoted history. No count changes (55 / 22 / 32 on the repaired start at all three sides). (iii)
REFEREE §C is not strictly append-only: ed3bd945 is +17/−2 (the NEEDS lines of a3aa5b68 l. 71-72 rewritten, the DONE block moved below
the new §4); 345fcea9 is +30/−0. No verdict line was removed. (iv) REFEREE §C l. 30-31 lists the MAXN-skipped games as «4 games
(switchbestexp_8, fc_8, leanT_N32, n3cov_phi)»; REFEREE-2 §C l. 24-30 finds 14 games with n > 200 skipped and n3cov_phi a partial-start
fallback (not MAXN). Both give 6503 − 6460 = 43 (15 + 13 + 4 + 4 + 7). Wording only. (v) The pin «K-rise 19» (REFEREE-2 l. 84) is inside
the phase [6, 98]; the pinned block's «'K-rise': 20» is run-wide (fixdepth.py: «strict 20», longest phase «(92, 19, 34, 1551)»).
Consistent. (vi) Packet §5 l. 76 names «returns_rt64» for FLATSW 14; REFEREE l. 113 adds «returns_rt48 ties». (vii) The «box 79» label
is shared in check.sh: l. 400-405 is R93's WCH block; l. 406-411 is the FLATSRC block of this entry.
(11) Excluded: lane work after the freeze other than the FIXD parts of fe5c9e33, 9460f011 and 59d58d0d (fixes file, line files L-1,
L-2, L-3): P-N5-WRUN (box 92: 7668bc9b, 02a12a10, 85c12579, and the WRUN fixes file in 9460f011), REFEREE R-N5-WRUN 8c0b2e69 and its
Addendum in a3aa5b68 (docs/referee/R-N5-WRUN.md +10), REFEREE-2 R2-N5-WRUN a281189a. Not part of this entry.
(12) Commits: lane: 5027c17c (parent cb9217ce, a merge into l-new) → fe5c9e33 (parent 7668bc9b, the WRUN freeze) → 9460f011 → 02a12a10
(WRUN) → 59d58d0d. REFEREE commits directly on claude/referee: 2c9d8040 (parent 254fc758, a merge of trunk into the branch) → 8c0b2e69
(WRUN) → a3aa5b68 → ed3bd945 → 345fcea9, each the parent of the next. REFEREE-2 directly on claude/referee-2: 64bd0d24 (15:54:59Z,
pre-freeze tools and the OWN draft; parent b8807d9d) → 4a960ef9 → 73d44f3b; 4d9a4318's parent d2b74403 is a merge of trunk into the
branch. First trunk commits containing each (first-parent walk of the local trunk): 5027c17c → d8e6cf31 (15:58:32Z); fe5c9e33 →
d9b762a4 (16:34:10Z); 9460f011 → bb46eec8 (16:46:29Z); 59d58d0d → f7be1a10 (17:11:42Z); 2c9d8040 → 7c7eaec4 (16:21:35Z); a3aa5b68 →
4e57e225 (17:11:42Z); ed3bd945 → f7abc761 (17:23:39Z); 345fcea9 → 5523052e (17:35:59Z, LOCAL only); 4a960ef9 → 0251cc86 (16:34:10Z);
73d44f3b → 5fcc420d (16:59:13Z); 4d9a4318 → none yet. (13) Placement: after R93 (l. 6972; "## Dead ends (kept;" follows at l. 7272).

### R94 [refereed-only] N5 on EVERY game (SPEC S1-S5, under the standing SPEC premise of RESULTS R57; premises RESULTS R15 (a), (d), R38 (a) and R93 (a) (Fact LEX, COMMON PREFIX); a run is the sequence of states (σ_t, τ_t); a transition is written t → t + 1 (states t, t + 1); n the number of vertices of the game; Ξ_t := Ξ_{σ_t} (SPEC S1: the valuation of every vertex under σ_t and Odd's optimal counterstrategy σ̄_t), λ_Ξ its cycle-node map; ⊴, ◁, ⊵, ▷ the SPEC S1 order (better for Even) and its strict and reverse forms; a phase P = [a, b] as in RESULTS R38 (a) (a maximal run of consecutive states a, …, b with (λ_Ξ, τ_t) constant), |P| := b − a its transitions; CS(x) the coordinate sequence of a value x of RESULTS R93 Fact LEX (reward of the cycle node; for each rank r from n − 1 down to 0, +1, −1 or 0 as the vertex of rank r is in the path set with even priority, with odd priority, or not; length, negated when the cycle node has even priority), in which the SPEC S1 order is lexicographic; for a phase P = [a, b], a state t ∈ P and a vertex v, DEPTH_t(v) := the length of the longest common prefix of CS(Ξ_t(v)) and CS(Ξ_b(v)) (n + 2 iff Ξ_t(v) = Ξ_b(v)) and K_t := Σ_v DEPTH_t(v) ∈ [0, n(n + 2)]; CH_P := the transitions of P at which Ξ changes at some vertex; FLATTR_P := the transitions of P at which Ξ changes at some vertex and K does not change; an Even vertex x is switched at k if σ_{k+1}(x) ≠ σ_k(x); FLATSW_P(x) := the transitions k → k + 1 counted in FLATTR_P at which the Even vertex x is switched and Ξ_{k+1}(x) ≠ Ξ_k(x)): (Lemma FIXD-MON) for states t ≤ t′ of a phase P and every vertex v, DEPTH_{t′}(v) ≥ DEPTH_t(v), so K is non-decreasing inside every phase; (Theorem PHASE-RED) every phase P has |P| ≤ (4n(n − 1) + 1)·(CH_P + 1) and CH_P ≤ n(n + 2) + FLATTR_P, so |P| ≤ (4n(n − 1) + 1)·(n(n + 2) + FLATTR_P + 1); and (Theorem FLAT-SW, proof of record Theorem SW-KEEP (REFEREE R-N5-FIXD §4b, claude/referee 2c9d8040; signed by REFEREE-2 R2-N5-FIXD-C §C.4, claude/referee-2 73d44f3b), from RESULTS R15 (a), (d), the standing SPEC premise of RESULTS R57 and R93 (a)) every transition k → k + 1 of every N5 run at which Ξ changes at some vertex, in particular every transition counted in FLATTR_P for any phase P, has an Even vertex x switched at k with Ξ_{k+1}(x) ≠ Ξ_k(x); and (Corollary PHASE-RED′) every phase P has FLATTR_P ≤ Σ_{x Even} FLATSW_P(x) and |P| ≤ (4n(n − 1) + 1)·(n(n + 2) + Σ_{x Even} FLATSW_P(x) + 1) (2026-10-30) — a REDUCTION (FLATTR_P and FLATSW_P are not bounded here; FLAT-SW is proved by a referee-originated proof, SW-KEEP, signed by both referees; G-N5-TIME stays open; not M3, not a step-4 pass, not a TARGET.md claim), CHECKER PASS (docs/checker/C104.md, checker PENDING)
- Object (L-NEW successor 38, Opus 5.5, D14 / D18, Lead reading L40; frozen, unchanged during review): packet P-N5-FIXD,
  docs/new/P-N5-FIXD-box91.md, sha1 2050e167a300c676d54178cdc34ccf2daec87036, 89 lines (l-new freeze 5027c17c3dfda150dbaf5f03ba003acd51945b30,
  2026-10-30T15:37:22Z, the file's only commit; identical at l-new head 85c12579, at origin trunk d1400cac and at the local trunk head
  8e1a605c; first on trunk by d8e6cf31, 15:58:32Z). Both referees measured the sha1 at 5027c17c (REFEREE l. 3-5; REFEREE-2 l. 2-4, «in a
  detached worktree at 5027c17c: match»). The Lead's freeze word is quoted at l. 2-5 («Lead 2026-10-30 15:33Z: «Your short box is BOX
  91, a freeze … GO: freeze P-N5-FIXD now as a packet for the two referees. Contents: FIX-DEPTH, FIXD-MON, PHASE-RED with FLATTR.
  PHASE-RED′ goes in only as conditional on CONJECTURE FLAT-SW. …»»). Status (l. 8-9): «REDUCTION only. FLATTR_P (equivalently Σ FLATSW
  under FLAT-SW) is NOT bounded here. G-N5-TIME stays OPEN. Not M3, not a step-4 pass, not a TARGET.md claim. Object: N5 only (SPEC
  S1-S5). Nothing is claimed for N5-LZC.» Sources (l. 6-7): working notes N5-FIXD-box77 §1-§2 and N5-FLATSRC-box79 §1, §3, «unrefereed;
  THIS packet governs where they differ; none is cited as a proof»; not refereed here. Sections: §0 what to sign (l. 11-17), §1 setting
  and premises (l. 19-33: N5, run, transition, Ξ_t, λ_Ξ, the order; PHASE per R38 (a), |P| := b − a; [LEX] = R93 (a) quoted; [R15] (a),
  (d) quoted; MON «Ξ_{t+1} ⊵ Ξ_t pointwise at every transition»; Ωσ = Ξ_σ, Ωτ a function of τ), §2 FIX-DEPTH and FIXD-MON (l. 35-43),
  §3 PHASE-RED (l. 45-59), §4 PHASE-RED′ under CONJECTURE FLAT-SW (l. 61-69), §5 DATA, DEAD, READING (l. 71-85), §6 symbols (l. 87-89).
  The RESULTS line, history: (1) the frozen line docs/new/P-N5-FIXD-box91-line.txt (5027c17c), sha1
  ba09dd261d5c885441845e09104f5e60bf0a81ed, the line both referees reviewed (REFEREE l. 4-5; REFEREE-2 l. 2-3); REFEREE l. 26 «MATCHES
  §2-§4 and claims nothing more» with FIXD-N1 (free k), FIXD-N2 (premise), FIXD-N4 (citation); REFEREE-2 l. 22 «MATCHES §2-§4 in content»
  with L-1, L-2 REQUIRED (symbol binding) and L-3 optional. (2) L-1 7e99a4a9593cc9aa0d21efbe82dd647606a8ac59 (fe5c9e33). (3) L-2
  d553bbba9a996d5d400efa0bdd53947785ffd5f7 (9460f011), REFEREE §C l. 75 «L-2 MATCHES». (4) L-3 7d22165a7e0cbd1a556cb546d8d3c53efa640956
  (59d58d0d) = L-2 with PHASE-RED′ unconditional through Theorem FLAT-SW; REFEREE §C l. 107 and REFEREE-2 L3 l. 39: MATCHES (Opus 5.5,
  D15). L-3 supersedes the earlier lines; the title is L-3 verbatim with its own date, less its lane tag (to check (1)). No gap and no
  FALSE item was raised on any version by either referee; the REQUIRED fixes bind symbols and add the standing premise (REFEREE l. 141-142
  «This is a disclosure, not a widening»; REFEREE-2 l. 24 «symbol binding only; no change of content»).
  Setting (packet §1): N5 = SPEC S1-S5 (FIX 1-4), any parity game, V = {0, …, n − 1}; a PHASE P = [a, b] a maximal run of consecutive
  states with (λ_Ξ, τ) constant (R38 (a)), |P| := b − a; CS(x) := (rew(c); s_{n−1}, …, s_0; ℓ̂) for x = (c, P, ℓ) (R93 (a), n + 2
  coordinates); MON from R15 (a), (d) with Ξ_σ = Ωσ (the standing premise, FIXD-N2). §1 cells: REFEREE «CHECKED. MON is R15 (a) applied
  at every σ-changing transition (R15 (d): I ⊆ Iσ, one edge per vertex), and is trivial at the others. Ξ_σ = Ωσ is the standing SPEC
  premise of R57, which the line must carry (FIXD-N2)» (l. 20); REFEREE-2 «CHECKED» (l. 17; §2.1 l. 28-32).
- Claims signed (both referees "(Opus 5.5, D15)": REFEREE successor 20, REFEREE-2 successor 23). Items (a), (b), (d) are SIGNED in both
  verdict tables (REFEREE "## Verdicts" l. 17-27 of R-N5-FIXD.md; REFEREE-2 "## 1. Verdict table" l. 14-24 of R2-N5-FIXD.md) and «agree»
  / «SIGNED by both, no gap» in both §Cs (REFEREE §C l. 9-11; REFEREE-2 §C C.1 l. 13-15); item (c) is signed by both under the Lead
  reading quoted in to-check (4) (SW-KEEP: REFEREE author, REFEREE-2 §C.4; OWN: REFEREE-2 author, REFEREE §C §3). All four are about N5
  on every game. Premises LANDED (as line L-3 names them): SPEC S1-S5; RESULTS R15 (a), (d); R38 (a) (phase); R93 (a) (Fact LEX, COMMON
  PREFIX; Fact REW for the injectivity of CS); standing premise: RESULTS R57's SPEC premise (S1's procedure realises the pointwise
  optimum), used by MON (Ξ_σ = Ωσ) and by SW-KEEP (2), (4). The code's match to SPEC is DATA (R15 G-N5T-1). No item uses a count.
  (a) Definition FIX-DEPTH and Lemma FIXD-MON (§2, l. 35-43; any phase of any N5 run): fin(v) := Ξ_b(v); «DEPTH_t(v) is the length of
      the longest common prefix of CS(Ξ_t(v)) and CS(fin(v)), so DEPTH_t(v) = n + 2 iff Ξ_t(v) = fin(v). K_t := Σ_v DEPTH_t(v) ∈ [0,
      n(n + 2)].»; «Lemma FIXD-MON. For states t ≤ t′ of a phase P and every vertex v: DEPTH_{t′}(v) ≥ DEPTH_t(v). Hence K_{t′} ≥ K_t.»
      Proof: MON along t, …, t′, …, b and COMMON PREFIX. Cells: REFEREE «SIGNED» (l. 21; §2 l. 29-40: CS injective, «I re-derived COMMON
      PREFIX myself»); REFEREE-2 «SIGNED», «none; N-3 (sharper range)» (l. 18; §2.2 l. 33-40).
  (b) Theorem PHASE-RED (§3, l. 45-59): CH_P := «the transitions of P at which Ξ changes at some vertex»; FLATTR_P := «the transitions of
      P at which Ξ changes at some vertex and K does not change»; «For every phase P of every N5 run: |P| ≤ (4n(n − 1) + 1)·(CH_P + 1) and
      CH_P ≤ n(n + 2) + FLATTR_P; so |P| ≤ (4n(n − 1) + 1)·(n(n + 2) + FLATTR_P + 1).» Proof (i) K rises at most n(n + 2) times; (ii) R15
      (d) on the Ξ-unchanged runs (τ constant in a phase, so Ωτ unchanged). Cells: REFEREE «SIGNED» (l. 22; §3 l. 42-50); REFEREE-2
      «SIGNED», «none; N-3 (sharper constants)» (l. 19; §2.3 l. 41-47 «Arithmetic checked. Combination checked.»).
  (c) Theorem FLAT-SW: at every transition k → k + 1 of every N5 run at which Ξ changes at some vertex (in particular at every FLATTR_P
      transition) some Even vertex x switched at k has Ξ_{k+1}(x) ≠ Ξ_k(x). Not a packet item (packet §4 l. 62-63 states it as CONJECTURE
      FLAT-SW, «FLAT-SW itself NOT to sign»; superseded by fixes entry 3 l. 125-127). Proof of record, Theorem SW-KEEP (REFEREE report
      §4b, l. 57-98, quoted verbatim in fixes entry 3 l. 74-112): «Let I be a non-empty set of Ξ_σ-improving edges with at most one edge
      per vertex, σ′ := Switch_I(σ), and S the set of switched vertices. If Ξ_σ′(x) = Ξ_σ(x) for every x ∈ S, then Ξ_σ′ = Ξ_σ. Moreover,
      every x ∈ S with Ξ_σ′(x) = Ξ_σ(x) is its own cycle node under both σ and σ′.» (premises l. 58-59: R15 (a) and the standing SPEC
      premise of R57; Fact F, cases (1a)-(1c), (2) by COMMON PREFIX, (3) play surgery, (4) optimality and R15 (a)); «Corollary FLAT-SW
      … It holds on every N5 run» (l. 87-91: a Ξ-changing transition changes σ; by R15 (d) σ_{k+1} = Switch_I(σ_k) with ∅ ≠ I ⊆ Iσ_k,
      one edge per vertex). Cells: REFEREE: author (l. 24, l. 87-98; §C §5 l. 89-100: «the clause is SW-KEEP's contrapositive»);
      REFEREE-2: «## C.4 Theorem SW-KEEP (REFEREE §4b): SIGNED (Opus 5.5, D15)» (§C l. 58; step by step l. 61-79, «All landed. No
      gap.»), L3 l. 14-26. Second proof, in-phase form (REFEREE-2 report §5, l. 96-135): «Lemma OWN. Let σ, σ′ be Even strategies that
      differ only on a set X of Even vertices, and let every x ∈ X be its own Ξ-cycle node under σ and under σ′. Then Ξ_σ = Ξ_σ′, and
      S1's procedure returns the same choice at every Odd vertex.» (proof from the SPEC S1 procedure, l. 33-44; «No improvement hypothesis
      is used»); «Corollary FLAT-SW (strong form). At every in-phase transition k → k + 1 of N5 with Ξ_{k+1} ≠ Ξ_k there is a switched
      Even x with Ξ_{k+1}(x) ▷ Ξ_k(x).» (through λ_Ξ constant on the phase, OWN, and R91 (i) SW-IN's argument). Cells: REFEREE-2: author
      (l. 20, l. 97); REFEREE: «Lemma OWN: SIGNED (Opus 5.5, D15).» (§C l. 35), «Corollary FLAT-SW (strong form, in-phase): SIGNED.»
      (§C l. 48). The line states FLAT-SW only; it cites SW-KEEP as the proof of record and does not state SW-KEEP's general form, OWN,
      or the strict rise.
  (d) Corollary PHASE-RED′ (§4, l. 61-69, with its hypothesis discharged by (c)): FLATSW_P(x) := «the transitions k → k + 1 counted in
      FLATTR_P at which the Even vertex x is switched and Ξ_{k+1}(x) ≠ Ξ_k(x)»; for every phase P: «FLATTR_P ≤ Σ_x FLATSW_P(x), and so
      |P| ≤ (4n(n − 1) + 1)·(n(n + 2) + Σ_{x Even} FLATSW_P(x) + 1).» Cells, the implication: REFEREE «SIGNED» (l. 23; §4 l. 52-55);
      REFEREE-2 «SIGNED (implication)» (l. 20; §2.4 l. 48-50). Unconditional: REFEREE l. 92-93 and §C l. 106 («The packet's §4 proof
      applies verbatim with the hypothesis discharged.»); REFEREE-2 l. 130-131 («Consequence (given a second signature)»); both L-3
      verdicts MATCHES.
  Gap maps: REFEREE l. 27 «No gap in §2-§4. Nothing FALSE. Notes FIXD-N1..N4.»; REFEREE-2 l. 24 «No gap. Nothing FALSE. Two REQUIRED line
  fixes (symbol binding only; no change of content).»; REFEREE-2 §C l. 20 «Joint gap map for §2-§4: EMPTY. Nothing FALSE on either
  side.»; on the proofs of FLAT-SW: REFEREE-2 §C l. 79 «No gap.» (SW-KEEP); REFEREE §C l. 42 «Note FIXD-C1 (exposition, not a gap)»
  (OWN).
  The RESULTS line (L-3) claims less than the reports: FIXD-MON without its Remark (any transition kind); PHASE-RED with the packet's
  constants, not N-3's n(n + 1) and 2n(n − 1); FLAT-SW without the strict rise, without SW-KEEP's general form and without N5-LZC;
  PHASE-RED′ without «FLATSW_P(x) ≤ SW_P(x)». Every clause it states is one of (a)-(d).
- Fixes (docs/new/P-N5-FIXD-fixes-box91.md, L-NEW successor 39, APPEND-ONLY, three entries, three commits each +N/−0: fe5c9e33
  (+31/−0, sha1 dbb6f66a65c4e157abf796f9f1ed495a8177349f), 9460f011 (+39/−0, sha1 11118fff4a67e456dad5e641c840c250a7b15e73), 59d58d0d
  (+78/−0, sha1 eb3bd874bb91da35a901a14d1bfadb496c2c34f9, 148 lines; = l-new head 85c12579 = origin trunk d1400cac; the last commit
  touching the file)). Header (l. 1-2): «Frozen packet … and line … are NOT edited; revisions are given here.»; «Each entry quotes the
  referee verbatim, then the change.» Each item, with the referees' words:
  - Entry 1 (l. 4-31; REFEREE 2c9d8040): FIXD-N1 (free k; = R2-L-1) applied in L-1; FIXD-N2 (standing premise of R57) applied in L-1,
    «A disclosure; the claims are unchanged.» (l. 16); FIXD-N3 (DATA label) as an erratum to §5, «not in the line» (l. 21-22); FIXD-N4
    («R93 (a) (Fact LEX, COMMON PREFIX)») applied in L-1; «Not applied (Lead 16:22Z): PHASE-RED′ stays an IMPLICATION» (l. 27).
  - Entry 2 (l. 33-70; REFEREE-2 4a960ef9): R2-L-1 «Already applied in line L-1»; R2-L-2 («then every phase P has») applied in L-2;
    R2-L-3 (τ → τ_t) applied in L-2, σ̄_t wording left (l. 50-51); N-1 erratum (corrected totals 9596 / 6475; VOID in entry 3); N-2
    erratum («6568 of 16183 in-phase transitions … Ξ-changing transitions 16118»).
  - Entry 3 (l. 72-148): SW-KEEP quoted verbatim (l. 74-112) with REFEREE-2's signature (l. 114-122); «Status change: CONJECTURE FLAT-SW
    (packet §4) → Theorem FLAT-SW, two-referee proved, with SW-KEEP (a REFEREE-originated proof, not the lane's) as the proof of record.
    Packet §4's «FLAT-SW itself NOT to sign» is superseded.» (l. 125-126); REFEREE-2's N-1 correction quoted (l. 129-135) and entry 2's
    N-1 erratum VOID (l. 136-138); remaining notes: comp54_n80.start (L-RED's file) and n5x.py's start reader, «a lane TODO, not done in
    this entry» (l. 139-141); L-3 (l. 143-148).
  No fix changes a signed statement of the packet: N1, N2, R2-L-1..3 bind symbols or disclose the premise; N3, N-2 are DATA labels; N-1
  is void; entry 3 replaces the hypothesis of (d) by Theorem (c), signed by both.
- Not signed: §1 (setting and premises; «CHECKED» by both); §5 DATA, DEAD and READING (Data below; DEAD items: «"K rises at least once
  per O(1) transitions": snap_n80_s62 stalls 36 consecutive transitions, returns_ph64 stalls 91» and «FLAT-LIN (per-vertex dead-branch
  climbs FLAT_P(v) ≤ n): nep92_n40 (above), vertex 0, 66 = 1.65n in one phase» (l. 80-82), lane DEAD, reproduced as DATA by both
  referees (REFEREE l. 111, l. 121; REFEREE-2 l. 82-85), not a refereed dead end of this entry; READING l. 83-85); the packet §1 Remark
  and §4 Note; FLAT-SW for N5-LZC; N-3's sharper constants; the frozen line ba09dd26 and L-1, L-2 (history); the working notes box 77
  and box 79 (l. 6-7). Lane and referee work after the freeze, other than the FIXD fixes commits, is not part of this entry: P-N5-WRUN
  (box 92) and both referees' WRUN reports.
- Referee strengthening (NOT part of this entry; remarks of one referee, remarks of both outside the verdict cells, readings):
  (i) N-3 (REFEREE-2 l. 93-94): «In a phase λ_Ξ is constant, so every DEPTH_t(v) ≥ 1 and at most n(n + 1) transitions raise K; and with τ
  constant only φ (not φ^d) can rise on a Ξ-unchanged run, so 2n(n − 1) would do in (ii) via R15 (c).»; REFEREE §C l. 18 «both are
  correct (I re-derived them). Precision only». Not in the line.
  (ii) FLAT-SW for N5-LZC: REFEREE l. 87 «the same proof covers N5-LZC»; REFEREE-2 l. 131-132 and §C l. 77. The packet and the line
  claim nothing for N5-LZC.
  (iii) The strong form: «in every Ξ-changing in-phase transition (flat or not) a switched Even vertex strictly rises, and Ξ-unchanged
  in-phase transitions are exactly those whose switched vertices are all their own cycle nodes» (REFEREE-2 l. 133-135); REFEREE §C l.
  59-60: «SW-KEEP's step (1) gives the same strict rise for the non-own-cycle-node switch».
  (iv) SW-KEEP vs R15 (b): «This is the converse direction to R15 (b) (Lemma B)» (REFEREE l. 94-95); REFEREE-2 l. 135 «That is R15 (b)
  (Lemma B) seen from the other side.»
  (v) Comparison of the two proofs (REFEREE §C l. 55-60; REFEREE-2 §C l. 80-84): «SW-KEEP needs no phase hypothesis, because case (1a)
  disposes of the mixed case directly … SW-KEEP is therefore slightly more general (every Ξ-changing transition of the run)».
  (vi) Self-corrections: REFEREE §C l. 13 (R2-L-2): «I agree; I missed it.»; REFEREE-2 §C l. 48 (FIXD-N2): «AGREE. I missed it.»;
  REFEREE-2 §C l. 34-40 (N-1 withdrawn); REFEREE-2 L3 l. 41-44 (τ(11)).
  (vii) Controls that bite (DATA): REFEREE MUT 1 (reference Ξ_a instead of fin) bites KM 69 and PR3 1 on nep92_n40, MUT 3 (drop n(n + 2))
  bites PR2 2, MUT 4 (FLAT-SW only through x with an Even old successor) bites SW 1; MUT 2 (stall bound n) never bites (l. 108-109).
  REFEREE own_check.py: OWN 1963 pairs, 0 violations; control «own cycle node under σ only» 3927 / 3927 differ (§C l. 46-47). REFEREE-2
  own_check.py: 4,083 pairs, 0 violations; control X_ONE 8,104 / 8,104 (l. 119-121); X_KSTALL 267 phases, X_OWNC 65 (N5) / 51 (N5-LZC)
  (l. 78-79).
  (viii) READING (packet §5 l. 83-85): «Under FLAT-SW the count moves to Even's per-vertex flat decisions. Inside W-runs those are paid by
  W-changes of targets (R93 RET-WCH)». Not signed.
- Honest limits: (i) A REDUCTION. The line bounds the length of every phase by its Ξ-changing transitions without a DEPTH rise (FLATTR_P),
  and these by per-vertex flat Even switches (FLATSW_P); neither is bounded here (packet l. 8; REFEREE l. 14-15; REFEREE-2 l. 12). (ii)
  FLAT-SW is proved by a referee-originated proof (SW-KEEP), not by the lane; its two-referee status is a Lead reading (to-check (4)).
  (iii) Standing premise: R57's SPEC premise (S1's procedure realises the pointwise optimum), through MON and SW-KEEP (2), (4); the code's
  match to SPEC is DATA (R15 G-N5T-1). (iv) Nothing is claimed for N5-LZC. (v) Counts are transitions, not bit operations; no
  running-time bound. (vi) Not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open.
- Data (DATA, not proof): pinned (packet §5 l. 77: «Pins (check.sh "box 77", "box 79")»). experiments/new/check.sh at 5027c17c: sha1
  af2427b3e1d3e4677d4ffcfdfa6966f68aec883f, 472 lines; at 59d58d0d: sha1 b5201cec45715a837722c5d3b14020fba79e2b74, 478 lines (+6: the
  box 92 WRUN block l. 472-477, excluded); the two blocks of this entry, «box 77 FIXD» l. 388-393 and «box 79 FLATSRC» l. 406-411, are
  identical at 5027c17c, 59d58d0d and l-new head 85c12579 (l. 400-405 is R93's «box 79 WCH» block). Files (identical at 5027c17c and
  59d58d0d): experiments/n5-epoch/instances/nep92_n40.pg ce224ec31e56e18103290d4aac81a9f225f76bfc (41 lines; = packet l. 77 and both
  referees' re-hash, REFEREE l. 111, REFEREE-2 l. 84), nep92_n40.start 10fdf3a3c76c80cdae106d428729c480b165a797, box77/fixdepth.py
  23fdc21c030b14f51f47a773f4c28b16bf8c1bf4 (last changed 50724c74), box79/flatsrc.py 1a50b622db55c30fea096a081f6c905b08b2ccc6 (last
  changed c50a4985), box79/flatsrc_sbcg.txt 5cb24fe4f2b40f9acaccfbd3c34c579f9a242e2a (719 lines), box79/flatsrc_alt.txt
  64330e7aad6b8b5595bb92121c60b5feb3eb92c8 (413 lines), box77/fixd_sbcg.txt e37503da3416e372179823befd95975b6234df4c (719 lines),
  box77/fixd_alt.txt 121a714f4eff35432d5c258d3fdb05d17b723396 (413 lines). Re-run for this draft from a `git archive` of each commit
  (experiments/ and docs/new/; `python3 -I`; outputs to scratch files; exit codes read): 59d58d0d l. 388-393 and l. 406-411 under `set
  -euo pipefail`, 17:38:21Z-17:38:22Z by date -u (read before and after): «box 77 FIXD: nep92_n40 FIX-DEPTH monotone, 66 = 1.65n
  dead-branch climbs at v 0 in one phase (FLAT-LIN DEAD): PASS», «box 79 FLATSRC: nep92_n40 all 73 flat transitions carry a flat Even
  switch (<= 8 per vertex): PASS», rc 0; 5027c17c, the same two blocks, both PASS, rc 0 (date -u 17:44:49Z read after). Tool output
  (59d58d0d archive): «FIXD nep92_n40.pg n 40 iters 98 phases 6 mono-viol 0 trans 93 strict 20 flat 73 max-stall 34 longest-phase (len,
  strict, stall, gain) (92, 19, 34, 1551) max-flat-changes-per-(v,phase) (66, 0, 5, 92)», rc 0; «FLATSRC nep92_n40.pg n 40 iters 98
  {'K-rise': 20, 'FLATTR': 73, 'FSW': 73} max-FLATTR-phase 73 max-FLATSW-(x,phase) 8», rc 0.
  DATA OF RECORD (packet §5 l. 72-79 with the errata of fixes entries 1-3; corpus box59/sbcg.lst (719) + si/root/logs/alt_all.lst (413),
  N5): FIXD-MON 0 decreases of K in any phase; in-phase transitions 16183 = K-rise 9615 + FLATTR 6503 + 65 Ξ-unchanged; Ξ-changing 16118;
  FLATTR 6503, all with a flat Even switch (FSW 6503: FLAT-SW 0 exceptions); max FLATTR per phase 91 (red/n5inj returns_ph64, n 64); max
  FLATSW per (x, phase) 14 (returns_rt64, n 64). Re-summed for this draft: equal (to check (9)). N5-LZC (DATA only, not claimed): K-rise
  9454, FLATTR 6379 = FSW, Ξ-flat 51. Totals 9615 / 6503 are totals of valid runs: REFEREE §C l. 23-27 («the lane's totals (9615 / 6503)
  are totals of genuine runs») and REFEREE-2's N-1 withdrawal (§C l. 34-40, 73d44f3b: «So the lane's totals 9615 / 6503 ARE the totals
  of valid runs (the repaired start).»; «N-1 is withdrawn as a data correction.»).
  REFEREE (successor 20; own docs/referee/scratch/fixd_probe.py on rl_engine and fsw_strong.py; no lane code): pins nep92_n40 «FLAT(v0) =
  66 in a 92-transition phase [6, 98]; FLATTR 73; FSW 73; flat switches ≤ 8 per vertex», returns_ph64 91, returns_rt64 14 (returns_rt48
  ties), nep94_n48 69 — «all MATCH» (l. 110-114); corpus 1132 × 2 runs, every one RC 0, «ZERO violation lines of XM, KM, ST, PR1, PR2,
  PR3, PRp or SW in either engine»; N5 15275 in-phase transitions, 15210 Ξ-changing, 8750 with a K-rise, FLATTR 6460 = FSW; N5-LZC 14979
  / 14928 / 8592 / 6336 (l. 115-122); SW-KEEP strong form over the 719 distinct games, both engines: «27586 τ-constant transitions,
  27504 of them Ξ-changing; 0 STRONG violations. 96 switched vertices kept Ξ, all of them own cycle nodes» (l. 123-124). Run set
  reconciled: MAXN 200 and partial starts (§C l. 30-32).
  REFEREE-2 (successor 23; own docs/referee-2/R2-N5-FIXD/fixd_check.py, «the lane's box77 / box79 code NOT imported», l. 74-76): corpus
  as the lane's, N5 and N5-LZC «0 violations of every check» (l. 77-78); per game against box79/flatsrc_*.txt: sbcg 719 / 719 identical,
  alt_all 412 / 413 (comp54_n80, N-1, later withdrawn) (l. 80-81); maxima 91, 14, 69, 1.65n, K stall 91 (l. 82-83); pin nep92_n40 «phase
  [6, 98], |P| 92, K-rise 19, FLATTR 73, all with a flat Even switch, FLATSW ≤ 8 per vertex, FLAT_P(0) = 66» (l. 84-85); §C l. 42-43:
  «Maxima agree on all three sides»; s3quad_K8_m30 (n > 200) has the longest phase, 263, 0 violations. No signed statement uses any count.
- Signatures: REFEREE docs/referee/R-N5-FIXD.md (report 2c9d8040f50d516d9e43619f9d6a72db9dc7379d, 2026-10-30T16:01:45Z, committed directly
  on claude/referee, first on trunk by 7c7eaec4 (16:21:35Z); sha1 427de472cca14ecdded2db5d90be88f0cee09db6, 163 lines, unchanged since
  (= referee head 345fcea9 = local and origin trunk); successor 20): §1 CHECKED; §2, §3, §4 SIGNED; FLAT-SW proved (SW-KEEP, §4b); «No
  gap in §2-§4. Nothing FALSE. Notes FIXD-N1..N4.» (l. 27). §C docs/referee/R-N5-FIXD-C.md (a3aa5b68907ae7c2bc9a2afa3de795f64070c9e3,
  2026-10-30T16:47:28Z, new file, 72 lines, sha1 b62f10e43fd8e944394db29a76ebf32169b71a1d; first on trunk by 4e57e225, 17:11:42Z):
  cross-map «agree» on §2-§4 (l. 9-11), Lemma OWN and the strong form SIGNED (l. 35, l. 48); §4 ed3bd9453cf9c354bafa6fdd1420ce560162922e
  (17:01:58Z, +17/−2, sha1 4c9e2f0d5680b753b5225bcba4604cf7ff1f0c32, 87 lines; first on trunk by f7abc761, 17:23:39Z): «L-2 MATCHES»
  (l. 75); §5 345fcea9a0af0b1754b28b3e42cdde6bd548b090 (17:17:01Z, +30/−0, sha1 ef2cc86859660a6460b781baa0795f10d484d93a, 117 lines, =
  origin referee head = the last commit touching the file; merged into the LOCAL trunk by 5523052e (17:35:59Z), not on origin trunk
  d1400cac at 17:42:05Z): «L-3 MATCHES … (Opus 5.5, D15).» (l. 107). REFEREE-2 docs/referee-2/R2-N5-FIXD.md (report
  4a960ef92364e06f35517ea3b66d8eefae8f5898, 2026-10-30T16:07:59Z, committed directly on claude/referee-2 (parent 64bd0d24, its own
  pre-freeze commit 15:54:59Z with the OWN draft), first on trunk by 0251cc86 (16:34:10Z); sha1 ed082af9abf58ae5c7f0de98cba32f8f94431d01,
  143 lines, unchanged since (= referee-2 head 4d9a4318); successor 23): §1 CHECKED; §2, §3, §4 (implication) SIGNED; «No gap. Nothing
  FALSE.» (l. 24); FLAT-SW proved (OWN, §5). §C docs/referee-2/R2-N5-FIXD-C.md (73d44f3b629e0d77c7d345078acb6e542cc93058,
  2026-10-30T16:37:15Z, +103/−0, sha1 f32205a031a8fcafc424e830feffb97da3184f48, 103 lines, = referee-2 head; first on trunk by 5fcc420d,
  16:59:13Z): «Joint gap map for §2-§4: EMPTY.» (l. 20); «## C.4 Theorem SW-KEEP (REFEREE §4b): SIGNED (Opus 5.5, D15)» (l. 58); N-1
  withdrawn (l. 34-40). L-3 verdict docs/referee-2/R2-N5-FIXD-L3.md (4d9a43189265f9d59a3179f8de6d1c1dba676666, 2026-10-30T17:20:00Z, new
  file, 44 lines, sha1 7c9a7b279f71ce8aab9c9408c24ba688adae144f; parent d2b74403, a merge of trunk into the branch; = origin referee-2 head;
  on NO trunk at 17:42:05Z): «L-3 (7d22165a): **MATCHES** (Opus 5.5, D15).» (l. 39).
  INDEPENDENCE: REFEREE l. 7: «Independence: I opened no docs/referee-2/ file for this packet.»; REFEREE §C l. 3-4: «I opened
  docs/referee-2/R2-N5-FIXD.md @ 4a960ef9 (143 lines) only after that word, and after my report R-N5-FIXD.md (2c9d8040) was pushed.»
  REFEREE-2 l. 4-6: «Independence: written before opening any docs/referee/ file for this packet; the count of «fixd» in docs/referee/ on
  trunk was 0 at 15:58Z. REFEREE's FLAT-SW proof «SW-KEEP» (Lead 15:58Z) is not read: my own proof of FLAT-SW (§5) was committed at
  64bd0d24 (15:54:59Z), before that message.» (64bd0d24 checked: 2026-10-30T15:54:59Z, adds R2-N5-FIXD/own_proof-draft.md, 33 lines);
  REFEREE-2 §C l. 2-3: its report pushed «before I opened any docs/referee/ file for this packet», REFEREE's report «opened 16:34Z on the
  Lead's word». No review imported lane code (REFEREE: own rl_engine; REFEREE-2 l. 74-76); the lane's scripts ran only as the pinned
  blocks. The two proofs of FLAT-SW were written independently (SW-KEEP before 16:01:45Z; OWN at 15:54:59Z) and each was checked by the
  other referee after both reports were pushed.
  §C (both): verdicts on §2-§4 identical; no disagreement in substance. One difference of reading, resolved: R2-L-2 (REFEREE §C l. 13
  «I agree; I missed it»; REFEREE-2 §C l. 52-55 keeps it REQUIRED; applied in L-2). Notes map (REFEREE §C l. 12-19; REFEREE-2 §C C.3 l.
  45-56): FIXD-N1 = L-1, FIXD-N3 = N-2; REFEREE only FIXD-N2 (agreed by REFEREE-2 §C l. 48), FIXD-N4 (agreed, l. 51); REFEREE-2 only
  L-2 (agreed), L-3 and N-3 (optional), N-1 (withdrawn).
- TARGET.md diff: «n the number of vertices of the game» is TARGET.md §1 l. 8's n («n = |V|, m = |E|»); games are TARGET.md §1 games
  (REFEREE-2 l. 66-67). The line makes no M4 claim and no TARGET claim; its own scope clause reads «a REDUCTION (FLATTR_P and FLATSW_P are
  not bounded here; FLAT-SW is proved by a referee-originated proof, SW-KEEP, signed by both referees; G-N5-TIME stays open; not M3, not a
  step-4 pass, not a TARGET.md claim)». REFEREE-2 l. 66 «the line claims nothing about M4»; REFEREE l. 14-15 «Not a TARGET.md claim».
  Not a claim of TARGET.md section 1 or §2 (lemmas and inequalities about N5 runs on every game; a REDUCTION of phase length to FLATTR_P
  and FLATSW_P, neither bounded; no bound on a run, no running-time bound, no algorithm claim). GAPS G-N5-TIME: open.

Proposed GAPS line-11 UPDATE (append-only), after R93's UPDATE of G-N5-TIME (GAPS l. 11, «UPDATE 2026-10-30 11:51Z: RESULTS R93
(P-N5-WCH; CHECKER C103 cdef102a) …», the last on the line), built by script only from the clauses of the title line L-3, with R93's
construction (labels behind their clauses; the scope tail as in R93's UPDATE). L-3 holds eight "|"; the UPDATE holds none: «|P| := b −
a its transitions» → «b − a the number of its transitions», «|P| ≤» → «the number of transitions of P ≤» (three times); these
replacements are not title text (to check (8)). Landing time and CHECKER commit to be filled at landing:
UPDATE 2026-10-30 <HH:MM>Z: RESULTS R94 (P-N5-FIXD; CHECKER C104 <checker>) [refereed-only] LANDED: N5 on EVERY game (SPEC S1-S5, under the standing SPEC premise of RESULTS R57; premises RESULTS R15 (a), (d), R38 (a) and R93 (a) (Fact LEX, COMMON PREFIX); a run is the sequence of states (σ_t, τ_t); a transition is written t → t + 1 (states t, t + 1); n the number of vertices of the game; Ξ_t := Ξ_{σ_t} (SPEC S1: the valuation of every vertex under σ_t and Odd's optimal counterstrategy σ̄_t), λ_Ξ its cycle-node map; ⊴, ◁, ⊵, ▷ the SPEC S1 order (better for Even) and its strict and reverse forms; a phase P = [a, b] as in RESULTS R38 (a) (a maximal run of consecutive states a, …, b with (λ_Ξ, τ_t) constant), b − a the number of its transitions; CS(x) the coordinate sequence of a value x of RESULTS R93 Fact LEX (reward of the cycle node; for each rank r from n − 1 down to 0, +1, −1 or 0 as the vertex of rank r is in the path set with even priority, with odd priority, or not; length, negated when the cycle node has even priority), in which the SPEC S1 order is lexicographic; for a phase P = [a, b], a state t ∈ P and a vertex v, DEPTH_t(v) := the length of the longest common prefix of CS(Ξ_t(v)) and CS(Ξ_b(v)) (n + 2 iff Ξ_t(v) = Ξ_b(v)) and K_t := Σ_v DEPTH_t(v) ∈ [0, n(n + 2)]; CH_P := the transitions of P at which Ξ changes at some vertex; FLATTR_P := the transitions of P at which Ξ changes at some vertex and K does not change; an Even vertex x is switched at k if σ_{k+1}(x) ≠ σ_k(x); FLATSW_P(x) := the transitions k → k + 1 counted in FLATTR_P at which the Even vertex x is switched and Ξ_{k+1}(x) ≠ Ξ_k(x)): for states t ≤ t′ of a phase P and every vertex v, DEPTH_{t′}(v) ≥ DEPTH_t(v), so K is non-decreasing inside every phase (Lemma FIXD-MON); every phase P has the number of transitions of P ≤ (4n(n − 1) + 1)·(CH_P + 1) and CH_P ≤ n(n + 2) + FLATTR_P, so the number of transitions of P ≤ (4n(n − 1) + 1)·(n(n + 2) + FLATTR_P + 1) (Theorem PHASE-RED); and every transition k → k + 1 of every N5 run at which Ξ changes at some vertex, in particular every transition counted in FLATTR_P for any phase P, has an Even vertex x switched at k with Ξ_{k+1}(x) ≠ Ξ_k(x) (Theorem FLAT-SW, proof of record Theorem SW-KEEP (REFEREE R-N5-FIXD §4b, claude/referee 2c9d8040; signed by REFEREE-2 R2-N5-FIXD-C §C.4, claude/referee-2 73d44f3b), from RESULTS R15 (a), (d), the standing SPEC premise of RESULTS R57 and R93 (a)); and every phase P has FLATTR_P ≤ Σ_{x Even} FLATSW_P(x) and the number of transitions of P ≤ (4n(n − 1) + 1)·(n(n + 2) + Σ_{x Even} FLATSW_P(x) + 1) (Corollary PHASE-RED′): a REDUCTION; FLATTR_P and FLATSW_P are not bounded here; FLAT-SW is proved by a referee-originated proof, SW-KEEP, signed by both referees. G-N5-TIME stays open.
