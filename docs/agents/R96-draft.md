# Draft RESULTS R96 (Lead, 2026-10-30 21:55:22Z by date -u, read in the same command as the fill of this file; subagent draft; packet, fixes F0 and entries 1-2, line files 6aa094e3 / L-1 / L-2, both reports, both §Cs, REFEREE §C §4-§5, REFEREE-2's L1 and L2 files, L-RED R143 / R140 and L-LIT T54 read at the origin heads fetched at the start of this draft (l-si 86becaa0, referee d6a33b10, referee-2 dd2333a2, l-red 47fd9163, l-lit 0ee955c7, checker 8e93dfa4; origin trunk a93c4b78, local trunk head f7e070b7); pinned «box 52» SETTLE blocks re-run 21:38:19Z-21:38:21Z (6a70a520, 86becaa0); DATA re-summed 21:38:40Z) — to CHECKER C106
to check: (0) PLACEMENT, R95 PENDING. R96 goes after R95. R95 is NOT landed: docs/RESULTS.md at the local trunk head f7e070b7 = origin
trunk a93c4b78 has sha1 fd771a5e346f0037499e837682799e40dda33cf0, 7,996 lines, unchanged since 5fc792c8 (the R94 landing, 18:40:32Z); the
last "### R" heading is R94 (l. 7272); «R95» and «R96» occur 0 times in RESULTS.md and in GAPS.md; «## Dead ends (kept;» is at l. 7476.
The R95 draft (docs/agents/R95-draft.md, sha1 2e22dee3c31c4c5e114bffed04f1c48bd77a80b3, 550 lines, = local trunk f7e070b7; C105 Add. 1
pending) lands first. So every RESULTS line number below is at fd771a5e, BEFORE R95; R96's entry is to be inserted after R95's entry, before
«## Dead ends (kept;». The Lead re-checks (6) and (9) at landing against RESULTS / GAPS with R95 in.
(1) TITLE. The title is the line file docs/si/P-N5-SETTLE-line-L2.txt (l-si 86becaa09e1ac367e6ad41d9b386f35e7184e7aa,
2026-10-30T20:42:47Z, the file's only commit, sha1 1fcb33c5d96a20eb70abe06c29154ef343b33ae0; identical at l-si head 86becaa0, at origin
trunk a93c4b78 and at the local trunk head f7e070b7; first on trunk by the merge 62391de1, 21:07:19Z), verbatim: one line, no outer
quotes, no final period, 4,010 characters (4,174 bytes plus the newline), 805 whitespace tokens. NO HEADING MARKER, verified by script: the
file begins «N5 on EVERY game (SPEC S1-S5, under the standing SPEC premise», with no «#», no «R??» and no lane tag (fixes entry 1 l. 13
«one line, no heading marker, Lead reading L41»; entry 2 l. 70 «line L-2 = L-1 plus this change (no heading marker)»; Lead reading L41
«Lanes write line files without a heading marker (C104 N-1).»). So, as in R95, NOTHING is stripped: the heading is the level-3 marker, then
"R96 [refereed-only] ", then the file without its newline, then the fill. «2026-10-30» occurs exactly once in L-2, in « (2026-10-30) — a
REDUCTION» (by script), so NO date is inserted (the R93-R95 rule). The line holds eight "|": «|V|» once, «|F|» three times; they stay in
the heading (R91, R93-R95 carry "|") and are replaced in the GAPS UPDATE only ((9)). The checker fill ", CHECKER PASS
(docs/checker/C106.md, checker PENDING)" is appended as in R90-R95 (no space before the comma); L-2 ends «… fixes
docs/si/P-N5-SETTLE-fixes.md entries 1-2)», so the heading ends «… entries 1-2), CHECKER PASS (…)». Built by script (scratch build96.py:
assert the sha1 1fcb33c5…, one line, no marker, one «2026-10-30», eight "|"; prepend "### R96 [refereed-only] ", append the fill) and
re-checked after writing this file: equal, byte for byte. Heading: 4,088 characters, 4,252 bytes; sha1 of the heading line without its
newline 7371740682a09d4ff6956130a326d5bc603b11c0, with its newline 7b851dd6ee4c63e7aa3a9f92c7f9601bda1a8364.
Two title features without a precedent in R90-R95 (DECISION for CHECKER; no line change proposed, the title is the line both referees
signed): (i) the title ends with a source parenthesis «(P-N5-SETTLE, docs/si/P-N5-SETTLE-box52.md; L-SI successor 34; fixes
docs/si/P-N5-SETTLE-fixes.md entries 1-2)» after the scope tail (R95's title names referee files inside a clause, not a source note); (ii)
the scope tail says «not to sign: CONJECTURES FLIP-EV (DEAD, fixes F0), HX-POLY, CN-POLY, XCN-POLY», packet language in a landed title
(R95 says «… are open»). HX-POLY, CN-POLY and XCN-POLY are packet names (§8 l. 234), undefined in the line, like R95's BIP-POLY / INT-LIN
(C105 N-2). REFEREE l. 125 «The not-to-sign list and the REDUCTION tail are correct.» (on 6aa094e3, whose tail read «Not to sign: …»).
(2) LINE HISTORY: frozen 6aa094e3 (docs/si/P-N5-SETTLE-line.txt, l-si 6a70a520, 2,728 characters, beginning «### R?? [proposed,
P-N5-SETTLE] », no date; the line both referees reviewed) → L-1 997e39ee (…-line-L1.txt, a0970d36, 19:23:21Z, 3,937 characters; fixes entry
1: E1.1-E1.8 = SETTLE-L1..L4, R2 L-1..L-6; marker dropped) → L-2 1fcb33c5 (86becaa0, 20:42:47Z, 4,010 characters; fixes entry 2: E2.1
SETTLE-L5, E2.2 optional, E2.3 bookkeeping). 6aa094e3 and L-1 are history, not the title. Each line file has one commit (git log on l-si)
and L-1 / L-2 are byte-identical to their copies in the fixes file (l. 68, l. 82; by script). Word diffs measured for this draft (difflib
over whitespace tokens, scratch wdiff.py):
- 6aa094e3 → L-1: 532 → 793 tokens, 41 non-equal opcodes: the marker deleted; the premises «RESULTS R15 (a), (d) and R86 (a)»; the
  up-front bindings (run, transition, «switches at k», n, m_E (m_O), values, ⊴ / ◁ / ⊵ / ▷, ⊕ «as in RESULTS R93 TIE», «for a state k:»
  Ξ_k, σ̄_k, Iσ_k (E1.3, E1.4, E1.5)); «λ_W, the cycle-node map of W), with»; «for a state k of F:» before W_k, ℓ_k, D_k, U_k, H_k, dist
  (E1.3); «for a transition k → k + 1 of F: (y, z) is W_(k+1)-tight … iff …» (E1.3); «EVENT-FREE iff it is not an EVENT» (E1.5); «for Odd
  o, c ∈ C and u ∈ V:» and «the numbers of» (E1.5); the global binder «for every N5 run on every game and every W-run F of it:» (E1.1);
  «at every S4a step k → k + 1 of F» (E1.3); «every Even vertex v … every vertex v … ℓ_(k+1)(v)» (E1.6); the proof note with the R140 SHA
  and «as signed in this packet's review, read at one S4a evaluation with W_(k+1)» (E1.7); the sum and max ranges and «for every family of
  games …» (E1.5); «every N5 run, with T its number of transitions (N5 iterations),» (E1.2); «(U) over the whole run»; the date and the
  tail «— a REDUCTION (… not M3, not a step-4 pass, not a TARGET.md claim; … FLIP-EV (DEAD, fixes F0) …)» (E1.8, F0); «fixes … entry 1)».
  = REFEREE §C §4 l. 59-67 («Nothing else changed. The content equals the packet's §3, §5-§7.»); = REFEREE-2 L1 l. 4-17.
- L-1 → L-2: 793 → 805 tokens, 8 non-equal opcodes: «U» → «Ξ^d_k», «τ» → «τ_k», «at state k» inserted, «R86):» → «R86's U):» (E2.1);
  «Ξ (U)» → «Ξ_k (Ξ^d_k)» (E2.1); «and» → «and, for every family of games,», «over all runs» inserted (E2.2); «entry 1)» → «entries 1-2)»
  (E2.3). = fixes entry 2 l. 71 («L-2 = L-1 with the four replacements below and nothing else»); = REFEREE §C §5 l. 80-85 («Nothing else
  changed.»); = REFEREE-2 L2 l. 17-24 («793 → 805 tokens»; «Nothing else changed.»).
- 6aa094e3 → L-2: 532 → 805 tokens, 44 non-equal opcodes, the union. No inequality of a claim changes: RG′'s statement, RUN-SETTLE's
  «ℓ_(k+1) ≥ k − k0 + 1» and «k1 − k0 ≤ n − 1», RUN-COUNT's «|F| ≤ n(E_F + 1) − 1», HEAD-RED's two inequalities and T-XCH's «T ≤ m_E(1 +
  XE) + m_O(1 + XO)» are token-identical apart from the binding of their symbols (v, ℓ_(k+1)(v); the Σ / max ranges; T; Ξ_k (Ξ^d_k)).
  SETTLE-L5 is the one change that is not only a binder: under 6aa094e3 / L-1, U was the fixed W-run τ's valuation, so XO literally counted
  the changes of a fixed function (REFEREE §C l. 71-72; REFEREE-2 L2 l. 9-11: «Read literally, U is one fixed function, so XO = 0. The bound
  would then read T ≤ m_E(1 + XE) + m_O. That is wider than what was signed»); L-2 states what both signed (REFEREE l. 100 «R86 (a) on both
  sides with R = the whole run»; REFEREE-2 l. 87).
(3) THE LINE AT BOTH REFEREES. L-2 (the title): REFEREE successor 20, docs/referee/R-N5-SETTLE-C.md §5 (l. 79-88), appended at d6a33b10
(2026-10-30T21:08:23Z, parent aa5adfd4; `git diff --numstat aa5adfd4 d6a33b10`: +11/−0 on this file; the commit also adds REFEREE's WRUN
L-5 §7 in R-N5-WRUN-C.md): l. 79 names the file, l-si 86becaa0, sha1 1fcb33c5… and fixes sha1 42d9a381…; l. 85 «Nothing else changed.»;
l. 86-87 «Strict symbol test on the new tokens: τ_k is bound by «a run is the sequence of states (σ_k, τ_k)». k is bound by «at state k».
The name clash with U_k is gone. No free symbol.»; l. 88 «Verdict on L-2: MATCHES (Opus 5.5, D15).» REFEREE-2 successor 24,
docs/referee-2/R2-N5-SETTLE-L2.md (dd2333a2, 2026-10-30T21:08:40Z, parent b3bdc1a0, a trunk commit; new file, 37 lines, sha1
677b1486f216f35145567cf2ed51de82784f0373): l. 2 «sha1 1fcb33c5d96a20eb70abe06c29154ef343b33ae0 (re-hashed: match)»; l. 13 «This is a
REQUIRED line item of the C99 / R92-F16 / C105-E-1 class: the literal line is wider than the signed statement.»; l. 24 «Nothing else
changed.»; l. 33 «No symbol is free. I found no other point in the line.»; l. 36 «(a) SETTLE-L5 is REQUIRED: I agree.»; l. 37 «L-2
(1fcb33c5): **MATCHES** (Opus 5.5, D15). No required change.» Both d6a33b10 and dd2333a2 are on the LOCAL trunk only (merges 78dc15f8 and
38556650, 21:33:54Z), not on origin trunk a93c4b78 at the start of this draft.
Earlier lines: 6aa094e3: REFEREE l. 34 «does NOT match yet: SETTLE-L1 (F unquantified), SETTLE-L2 (T undefined), SETTLE-L3 (k free in RG′)
are REQUIRED; SETTLE-L4 is precision (§10)», l. 146 «Verdict: MATCHES the packet's signed items once SETTLE-L1, L2 and L3 are applied.»;
REFEREE-2 l. 24 «content MATCHES §3, §5-§7» with «REQUIRED: L-1 F unquantified; L-2 Iσ_k unbound; L-3 T unbound. Precision L-4..L-6».
Joint required set (REFEREE §C l. 50-54; REFEREE-2 §C l. 31): F, T, k, Iσ_k (REFEREE l. 19 of §C «I agree it is REQUIRED … I upgrade
it»; REFEREE-2 §C l. 24 «SETTLE-L3 … AGREE, REQUIRED. I missed it.»). L-1: REFEREE §C l. 77 «Verdict on L-1: REQUIRED CHANGE, SETTLE-L5
(Opus 5.5, D15). Everything else MATCHES.» (aa5adfd4, 20:01:17Z); REFEREE-2 successor 23, R2-N5-SETTLE-L1.md l. 25 «L-1 (997e39ee):
**MATCHES** (Opus 5.5, D15). No required change.» (b521c191, 20:00:44Z), CORRECTED by successor 24, R2-N5-SETTLE-L2.md l. 14
«Correction (my side): successor 23's L-1 report (b521c191) said MATCHES and missed this.» (R2-N5-SETTLE-L1.md itself is unchanged; the
correction is in the L2 file, as R95's REFEREE-2 L-2 supersession was in L3check). The two L-1 verdicts were written 33 s apart, each
before the other was visible (aa5adfd4 parent ea05b574; b521c191 parent 04020305). SETTLE-L5 was present since 6aa094e3 (fixes l. 70;
REFEREE §C l. 68 «it was already present in 6aa094e3»): both referees passed it on 6aa094e3, and REFEREE-2 23 on L-1.
(4) CLAIMS SIGNED = the items below, each SIGNED in BOTH referees' verdict tables (REFEREE "## Verdicts" l. 21-35 of R-N5-SETTLE.md;
REFEREE-2 "## 1. Verdict table" l. 12-26 of R2-N5-SETTLE.md) and in both §C cross-maps (REFEREE §C l. 6-24; REFEREE-2 §C C.1 l. 6-19), AND
stated by L-2. The brief's candidate list was checked item by item against L-2's clauses:
| item (packet §, lines) | REFEREE (successor 20) | REFEREE-2 (successor 23) |
| --- | --- | --- |
| (a) Claim RG′ (§3, l. 94-120; statement l. 103-104) | R-N5-SETTLE.md l. 28 «SIGNED»; §3 l. 37-51; §C l. 9 «agree. Both note that a good-u edge u → y with y ∈ M is never length-tight» | R2-N5-SETTLE.md l. 18 «SIGNED» / «none»; §2.2 l. 36-47; §C l. 13 «SIGNED by both» |
| (b) Theorem RUN-SETTLE (§5, l. 142-147, 150-199): S_j and X_j, «k1 − k0 ≤ … ≤ n − 1» | l. 30 «SIGNED» (S_j, X_j by induction; Cases 1, 2a, 2b, 2c); §5 l. 64-90; §C l. 12 «agree» | l. 20 «SIGNED» / «none»; §2.5 l. 67-83; §C l. 15 «SIGNED by both» |
| (c) Corollary RUN-COUNT (§5, l. 148-149) | l. 30 «SIGNED»; l. 91 «RUN-COUNT ✓»; §C l. 12 | l. 20; l. 84; §C l. 15 |
| (d) Theorem HEAD-RED (⇐, ⇒ and the family equivalence) (§6, l. 201-212) | l. 31 «SIGNED»; l. 94-97; §C l. 13 «agree» | l. 21 «SIGNED» / «none»; l. 86; §C l. 16 «SIGNED by both» |
| (e) Corollary T-XCH (§7, l. 216-228), the composition of landed R86 (a) (both sides) and R15 (d) | l. 32 «SIGNED (composition of landed R86 (a), both sides, with R15 (d))»; l. 98-101; §C l. 13 | l. 22 «SIGNED» / «none»; l. 87-88; §C l. 17 «SIGNED by both» |
Joint gap maps: REFEREE l. 35 «No gap in the packet. Nothing FALSE.»; REFEREE-2 l. 26 «No gap in the packet. Nothing FALSE among the
items to sign.»; REFEREE §C l. 44 «Packet items to sign: EMPTY on both sides. Nothing FALSE.»; REFEREE-2 §C l. 19 «Joint gap map for the
packet: EMPTY. Nothing FALSE on either side.» The only REQUIRED items of either referee are LINE items (F, T, k, Iσ_k; SETTLE-L5), all
closed in L-1 / L-2 ((3)).
DEVIATION FROM THE BRIEF: the brief lists §4 «PLAY-CAUSE, W-MON, PATH» among the claims to land. They are SIGNED by both (REFEREE l. 29,
§4 l. 53-62; REFEREE-2 l. 19, §2.4 l. 58-66; REFEREE §C l. 11; REFEREE-2 §C l. 14) but L-2 does NOT state them: «PLAY-CAUSE», «W-MON»,
«PATH» occur 0 times in L-2 (by script), and REFEREE-2 l. 104 records «PLAY-CAUSE / W-MON / PATH are not stated (allowed)». Under the brief's rule (SIGNED in BOTH reports AND
stated in L-2) they do NOT land as claims; they are recorded in the entry as signed proof steps (as R94 recorded
SW-KEEP's statement and R95 STEP-SW). PLAY-CAUSE's consequence for event-free blocks enters the title only through RUN-SETTLE's X_j half
(«every vertex v whose Ξ changes at k has ℓ_(k+1)(v) ≥ k − k0 + 1»), which is (b). Likewise T54 IDX-MONO / LEX-BFS «SIGNED as used»
(REFEREE l. 26; REFEREE-2 l. 17; both §Cs) are named in RUN-SETTLE's proof note («as signed in this packet's review, read at one S4a
evaluation with W_(k+1)»), not stated: proof steps, not landed. Signed by both, NOT stated by L-2, so NOT landed: PLAY-CAUSE (§4 l.
124-137), W-MON (l. 138), PATH (l. 139-140), T54 IDX-MONO / LEX-BFS as used (§2 l. 64-75; §5 Case 2a), RUN-SETTLE's intermediate «k1 − k0 ≤
max_x ℓ(x)» (l. 147; L-2 states «≤ n − 1»), HEAD-RED's (⇒) as a separate bound (L-2 states «as each count is ≤ |F|» inside the
equivalence; it is stated, so it lands as part of (d)). §1 setting (STEP-SW, MON) is «CHECKED» by both (REFEREE l. 24; REFEREE-2 l. 15),
not signed. What does NOT land at all: CONJECTURE FLIP-EV (DEAD, fixes F0), HX-POLY, CN-POLY, XCN-POLY (§8, «NOT to sign»); §9 DATA, DEAD,
READING; packet errata E1.9-E1.13 (fixes only); R143 SETTLE (B), (C) (not used: packet l. 90; REFEREE l. 27 «SETTLE (B), (C) are not used
(checked: §5 cites neither)»; REFEREE-2 §C l. 12 «the same»).
L41 does NOT apply: every item is lane-authored (L-SI successor 34) and checked by two referees; no referee-originated proof is landed.
(5) OTHER LANES' TEXTS THE PACKET DEPENDS ON (packet §2 l. 58-92), checked for this draft by script (scratch qcheck.py: every outermost
«…» of packet l. 58-92, whitespace joined, «…» elisions split): 13 quotes, all found, at L-RED R143 docs/red/R143-settle.md @ l-red
717f407a (sha1 6a26c144421cede6ebba0134c0244105a1310f46, 151 lines; = trunk), L-RED R140 docs/red/R140-friedmann-port.md @ 47000632 (sha1
4cbf36370123a955fb531e11d82595f7c59af1c0, 80 lines; = trunk) and L-LIT T54 docs/lit/T54-stalling.md @ 96cfda95 (sha1
8b320b4375582ff5b8440df817bc555684f7e444, 325 lines; = trunk). Exactly:
- R143 l. 13 «UPWARD HEADS: U_k := {σ̄_k(g) : g Odd, σ̄_k(g) ≠ τ(g)} ∪ {the Ξ-successor of c (σ_k(c), or σ̄_k(c) if c is Odd) : c ∈ C}.»
  and l. 14-15 «EVENT: a transition k → k + 1 of I at which (i) σ̄ changes, or (ii) σ changes at some Even c ∈ C (a CN switch), or (iii) Ξ
  changes at some vertex of U_k ∪ U_(k+1).» = packet l. 77-80. The packet uses R143's DEFINITIONS only, read on a whole W-run F (packet
  l. 87-90: «(a) §5 uses R143's DEFINITIONS of U_k and EVENT, read over a whole W-run F in place of I.»; «(c) SETTLE (B) and (C) are NOT
  used.»). L-2 restates U_k with D_k: «U_k := {σ̄_k(g) : g ∈ D_k} ∪ {…} (L-RED R143's upward heads)», D_k := {Odd o : σ̄_k(o) ≠ τ(o)}: the
  same set, written with the line's own D_k; and EVENT with «of F» for «of I» and without «(a CN switch)». Not a quote; equal in content
  (checked by hand). R143's Lemma SETTLE itself is lane-PROVED «modulo RG / LEX-BFS / IDX-MONO» (R143 l. 141) and is NOT landed here.
- R140 l. 42-46 ARENA-MAX = packet l. 59-62, modulo the list marker «- » before «Proof.» (R140 l. 45; REFEREE-2 N-2 = fixes E1.13) and the
  SHA the packet omitted (REFEREE SETTLE-N2 = E1.10; L-2's proof note carries «l-red 47000632»). Used as [R57] for S4a (REFEREE l. 25
  «quoted verbatim. Used as [R57]»; L-2 «the S4a half of the R57 premise above»). Not landed; ARENA-MAX = RESULTS R57's standing premise.
- T54 §4.1-§4.2 (l. 249-262) IDX-MONO, key, LEX-BFS and the two proof sentences = packet l. 65-72. L-LIT's own label «PROVED, L-LIT,
  elementary, modulo Claim RG»; both referees SIGN them «as used» in Case 2a, at one S4a evaluation with W_(k+1)-tightness (REFEREE l. 26,
  l. 76-82, re-derived from SPEC S1 (iv); REFEREE-2 l. 17, §2.3 l. 48-57, against si.py). Not landed (proof note only).
(6) PREMISE LABELS (stale-label test; RESULTS at fd771a5e, see (0)). RESULTS labels in L-2 (by script): «R15» 3, «R57» 2, «R86» 3, «R89»
1, «R93» 1; «R140», «R143» are L-RED report numbers, «T54» L-LIT's; none of these three is a RESULTS label. Every RESULTS label exists and
carries the named item:
- R57 (l. 2893): the standing SPEC premise; L-2's gloss «(1E-N3: S1's procedure realises the pointwise optimum; for S4a, σ_new is the
  pointwise optimum of the one-player arena H_t)» is byte-identical to the first part of R91's (l. 6384) and R93's (l. 6972) title gloss
  (by script: the fragment occurs 2 times in RESULTS), which continue «, H_t := S4a's arena at t (Even keeps σ_t ∪ Iσ_t, Odd follows
  τ_t)»; L-2 stops before that definition (see (7), D-2). «the R57 premise above» in the proof note refers to it.
- R15 (l. 624): (a) Lemma A l. 631, (d) l. 640; quoted in packet §1 l. 52-55; REFEREE-2 l. 16 «R143, T54, R89, R57, R15, R86 quotes
  verbatim at their SHAs»; my script: the packet's four RESULTS quotes in §1 l. 23-57 and two in §7 l. 216-229 are all found in RESULTS.
- R86 (a) (l. 5269 title; body l. 5311): Lemma SW-RETURN «ENT_R(v, c) ≤ 1 + RISE_R(c)» with «Dually for Odd v with U.» (found in
  RESULTS); «RESULTS R86's U» = R86's title «Odd's valuation U of τ on G^d» (found). R86's F1 (l. 5298: «|R| := #{t : t, t + 1 ∈ R}, the
  number of TRANSITIONS inside R (one less than its number of states)») is the landed carrier of |R| for any stretch (see (7), D-1).
- R89 (l. 5854): «a maximal run of consecutive states of one τ-stretch none of whose transitions is an S4c fallback or changes λ_W» —
  verbatim in R89's title (by script: 1 occurrence) and in L-2's W-run parenthesis.
- R93 (l. 6972): Lemma TIE's prefix operation «x ⊕ (c, Q, ℓ) := (c, Q ∪ {x if x is more relevant than c}, ℓ + 1)» — verbatim in R93's
  title (1 occurrence) and in L-2 («as in RESULTS R93 TIE»).
- No conflict with landed text: «RUN-SETTLE», «RUN-COUNT», «HEAD-RED», «RG′», «PLAY-CAUSE» occur 0 times in RESULTS and GAPS; «T-XCH» 0
  times in RESULTS (the R95 draft's 10 matches are «INT-XCH»). The R95 draft lists REFEREE R-N5-SETTLE (1df722e9) and REFEREE-2
  R2-N5-SETTLE (301042bb) as excluded work (R95-draft l. 252-253), so R95 claims nothing of this entry. A name note (no clash inside the
  title): landed R38 uses U_k for Odd's valuation («U_k = Ξ^d_{τ_k} is Odd's valuation», RESULTS l. 1822; R47 l. 2331); L-2 defines U_k
  as R143's upward heads, inside the title, and its new Ξ^d_k matches R38's Ξ^d_{τ_k} for Odd's valuation. CHECKER may want the entry to
  say so (done under Setting below).
- At landing (R95 in): re-run the grep for «R96», «RUN-SETTLE», «HEAD-RED», «T-XCH» (as a word) in RESULTS and GAPS; R95's landed text
  should not cite or claim any item here. L-2 does not cite R95 («R95» 0 times).
(7) SYMBOL TEST of the title (my own strict test of every symbol of L-2, by hand; IN = bound in the line; else the carrier). The four
binding fixes of the joint required set and SETTLE-L5 first:
| symbol | where |
| --- | --- |
| F (W-run) | IN: defined «W-run F := RESULTS R89's (…), with τ and C := {v : λ_W(v) = v} fixed on F»; QUANTIFIED by the global binder «for every N5 run on every game and every W-run F of it:», which every clause follows (SETTLE-L1 = R2 L-1; E1.1) |
| T | IN («every N5 run, with T its number of transitions (N5 iterations), has T ≤ …»; SETTLE-L2 = R2 L-3; E1.2) |
| k | IN everywhere: «a transition is written k → k + 1 (states k, k + 1)»; «for a state k:»; «for a state k of F:»; «for a transition k → k + 1 of F:»; «an EVENT := a transition k → k + 1 of F»; «(Claim RG′) at every S4a step k → k + 1 of F» (SETTLE-L3; E1.3); RUN-SETTLE «for k0 ≤ k < k1»; Ξ^d_k «at state k» (E2.1). Soft spot: in SB_F / CN_F / HXU_F, «the numbers of transitions of F at which … u ∈ U_k ∪ U_(k+1) …» binds k only through the transition convention |
| Iσ_k | IN («Iσ_k := Even's improving edges at k (SPEC S2: {(y, z) : Ξ_k(z) ▷ Ξ_k(σ_k(y))})», «for a state k»; R2 L-2; E1.4) |
| Ξ^d_k, τ_k | IN («Ξ^d_k := Odd's valuation of τ_k on G^d at state k (RESULTS R86's U)»; τ_k by «a run is the sequence of states (σ_k, τ_k)»; SETTLE-L5; E2.1). XO counts changes of Ξ^d_k over the whole run, as signed |
| U_k, U_(k+1) | IN («for a state k of F: … U_k := {σ̄_k(g) : g ∈ D_k} ∪ {…} (L-RED R143's upward heads)»). The letter U alone occurs only in «RESULTS R86's U» (REFEREE-2 L2 l. 25; by script) |
| N5, SPEC S1-S5, «Even», «Odd», S4a, S4c, [S1-val], σ_new | SPEC (named); σ_new as in landed R91 / R93 titles |
| standing SPEC premise of RESULTS R57; R15 (a), (d); R86 (a); R89; R93 TIE | cited premises, each a landed RESULTS item; see (6) |
| H_t (premise gloss) | NOT IN: see D-2 below |
| run, states, σ_k, τ_k; transition; «y switches at k» | IN |
| n := \|V\|, V | IN; V is TARGET.md §1's vertex set (l. 6-8 «V = V_E ⊔ V_O», «n = \|V\|») |
| m_E (m_O) | IN; m_E + m_O = TARGET's m (every edge leaves an Even or an Odd vertex) |
| values (c, P, ℓ), cycle node, path set, length; ⊴, ◁, ⊵, ▷; ⊕ | IN («as in SPEC S1»; «as in RESULTS R93 TIE») |
| Ξ_k, σ̄_k | IN («for a state k: Ξ_k := Ξ_{σ_k}, σ̄_k := S1's Odd counterstrategy to σ_k») |
| τ-stretch, S4c fallback, λ_W, W in «the cycle-node map of W» | R89 (cited: «RESULTS R89's (…)»); W there is R89's W_t (with τ_t), equal to the line's W_k on F, where τ_k = τ |
| τ, C | IN («with τ and C := {v : λ_W(v) = v} fixed on F») |
| W_k, ℓ_k(x), D_k, H_k, «dist and the remaining edges at k» | IN («for a state k of F: …»); dist / remaining edges by reference to si.py Engine.evaluate (no SHA; experiments/si/si.py sha1 e688b96327b7fd2770126e20bb00e459c1f18869 at 6a70a520 = 86becaa0 = trunk) |
| «(y, z) is W_(k+1)-tight at Even y ∉ C» | IN («for a transition k → k + 1 of F: … iff y ⊕ W_(k+1)(z) = W_(k+1)(y)») |
| EVENT (i)-(iii), EVENT-FREE, E_F | IN; «σ̄ changes», «σ changes», «Ξ changes» unsubscripted = at k vs k + 1, by use |
| SB_F(o), CN_F(c), HXU_F(u); o, c, u | IN («for Odd o, c ∈ C and u ∈ V: …») |
| Claim RG′: «round of cycle node c», c, (x, y), «arena edges of x», «W_(k+1)-cycle node» | IN by the clause («in the round of cycle node c, the remaining edges (x, y), x ≠ c, …»); «round» = si.py's evaluation per cycle node (soft spot); tightness is defined at Even y ∉ C, so at an Odd x the one arena edge τ(x) is read by the same equation (soft spot, as in the packet §1 l. 44 and §3 l. 103-104, signed as worded) |
| RUN-SETTLE: k0, k1, k, v | IN («if the transitions k0, …, k1 − 1 of F are all event-free, then for k0 ≤ k < k1 every Even vertex v … and every vertex v …»; R2 L-4) |
| \|F\| | NOT IN: see D-1 below |
| HEAD-RED: Σ / max ranges, «polynomially many», «polynomial over all W-runs F» | IN (ranges, E1.5); «polynomial» in the game size, by use (soft spot; R95 wrote Q-POLY with p(n) explicitly) |
| T-XCH: XE, XO, «every N5 run» | IN («XE (XO) the most changes of one vertex's Ξ_k (Ξ^d_k) over the whole run»); «every N5 run» re-quantified under the global binder, harmless (REFEREE-2 L1 l. 16) |
| ARENA-MAX, L-RED R140, l-red 47000632, T54, LEX-BFS, IDX-MONO | proof note; names, not claim symbols (REFEREE l. 139-140 «acceptable as a proof note») |
| FLIP-EV, HX-POLY, CN-POLY, XCN-POLY, «fixes F0», G-N5-TIME, M3, step-4, TARGET.md | scope tail; packet names (§8), the fixes file, GAPS l. 11, TARGET.md |
DOUBTS for CHECKER (neither referee raised them; I propose no line change, but D-1 is of the C105 E-1 kind and CHECKER decides):
D-1 «|F|» (three times: RUN-COUNT «|F| ≤ n(E_F + 1) − 1»; HEAD-RED «so |F| ≤ …» and «as each count is ≤ |F|») is NOT defined in L-2, and
not in the packet (packet l. 148, 208-209 use it undefined). It must mean the number of TRANSITIONS of F: RUN-COUNT's signed proof counts
transitions («the event-free transitions form at most E_F + 1 maximal blocks, each with ≤ n − 1 transitions», l. 149; REFEREE-2 l. 84).
Read as the number of STATES (b − a + 1), RUN-COUNT would claim one less transition than signed, i.e. a statement wider than (stronger
than) the signed one. Carriers: R86's F1 for any stretch, «|R| := #{t : t, t + 1 ∈ R}, the number of TRANSITIONS inside R» (R86 is a cited
premise of the line, (a) only); the landed convention «a W-run and, for a W-run F, |F| (its transitions) as in RESULTS R89» (R93's title;
R93 body l. 7008 «(τ-STRETCH, W-RUN; |F| := its transitions)») and the pending R95 title's «|F| := b − a its transitions». R89's own title does not define
|F| (its body defines |S| for τ-stretches, l. 5980). REFEREE-2's bound list (l. 102-103) and REFEREE's L-1 / L-2 symbol tests do not list
|F|. If CHECKER requires it, a one-phrase revision L-3 = L-2 with «with τ and C := {v : λ_W(v) = v} fixed on F» → «with τ and C := {v :
λ_W(v) = v} fixed on F and |F| its number of transitions» (occurs once) would close it; the GAPS UPDATE already reads «the number of
transitions of F». My reading: a soft spot with landed carriers (as R93 cites R89 for |F|), not an E-item; flagged because the
states-reading is not covered.
D-2 «H_t» in the R57 gloss («the pointwise optimum of the one-player arena H_t)»): t is free and H_t is not defined in L-2 (it was not in
6aa094e3 either). R91 / R93 / R95 define it in the same gloss («H_t := S4a's arena at t (…)»); L-2 defines H_k only «for a state k of F»
(Odd follows the W-run's τ). The gloss is a premise label quoted from landed text (packet §1 l. 50-51), so it adds no claim; same kind
as R95's σ_new note. Soft spot.
Other soft spots, as in landed titles: σ̄, σ, Ξ unsubscripted in EVENT and the counts; «round»; tightness at Odd x; «polynomial» without
p(n); si.py without SHA in a definition; «W» in R89's W-run parenthesis. A mechanical binder-presence check (each IN symbol's binder phrase
occurs in L-2: scratch symcheck96.py, 29 pairs) gives «binders missing 0»; it cannot see clause scope; the test of record is the hand test. Agreeing tests:
REFEREE §C l. 86-87 (new tokens of L-2) and §4 l. 68-77 (L-1, which found SETTLE-L5); REFEREE-2 L2 l. 27-33 (changed text) and L1 l. 15-16
(L-1, «No free symbol.», later corrected for U).
(8) PACKET ERRATA AND STATUS NOTES (fixes file; NOT in L-2, NOT landed; recorded under Fixes): F0 FLIP-EV DEAD (status, «§§3-7 (the items to
sign) do not use FLIP-EV.», l. 9); E1.9 RG′'s word-diff note lists two of three changes (SETTLE-N1; «a restriction, it is correct»); E1.10
R140 SHA (SETTLE-N2); E1.11 §9 «longest event-free block is 44 at n 48» is the largest RATIO (SETTLE-N3, R2 N-3; reconciled, (10)); E1.12
§1 «y ⊕ · preserves and reflects ⊴ and ◁» needs y in neither path set (R2 N-1; REFEREE-2's instance «x = (c, {w}, ℓ), x′ = (c, {y}, ℓ)
with y, w even, y above w above c»; every use satisfies it; REFEREE §C l. 14 «I agree; I missed it here.»); E1.13 ARENA-MAX list marker
(R2 N-2). Each entry says «No signed item changes.»; REFEREE §C l. 45-49 and REFEREE-2 §C C.3 l. 33-38 list the same errata. The fixes
file's quotes of the referees were checked for this draft by script against R-N5-SETTLE.md (1df722e9), R2-N5-SETTLE.md (301042bb) and
R-N5-SETTLE-C.md (d6a33b10): every quote of referee text is found (whitespace joined; E1.5's quote of SETTLE-L4 equal with its list
layout joined). Not found as quotes: the Lead's two words (l. 11 «The LINE needs a revision. …», l. 70 «Add fixes entry 2 …»; messages,
not on file) and three «…» that are summaries or L-SI's own text (l. 27 «for a state k: Ξ_k, σ̄_k, Iσ_k» and «for a state k of F: W_k,
ℓ_k, D_k, U_k, H_k, dist and the remaining edges at k» abbreviate L-1; l. 61 is the erratum's own reading).
(9) GAPS: G-N5-TIME (GAPS l. 11) stays open; L-2 states no CONJECTURE as a claim. A line-11 UPDATE is proposed at the end, to go AFTER
R95's UPDATE (pending: R95-draft l. 548); at present the last UPDATE on l. 11 is R94's («UPDATE 2026-10-30 18:40Z: RESULTS R94 (P-N5-FIXD;
CHECKER C104 5c4d6e45) …»; docs/GAPS.md sha1 7fc16836d13b6a0df31d9d5ce725f2f0c7931a06, 23 lines, unchanged since 5fc792c8). Built by
script (build96.py) from L-2's clauses only, with R94's / R95's construction: «LANDED: » + the title body with each clause label moved
behind its clause; the scope tail « (2026-10-30) — a REDUCTION (X) (source)» → «: a REDUCTION; X′ (source). G-N5-TIME stays open.», X′ = X
minus «G-N5-TIME stays OPEN» and «not M3, not a step-4 pass, not a TARGET.md claim» (R94 / R95 drop both). Choices: RUN-SETTLE's label goes
behind its proof note («… with W_(k+1)) (Theorem RUN-SETTLE)», two parentheses in a row, as R95's REL2-WRISE); the source parenthesis is
KEPT, before the final sentence, so that «fixes F0» keeps its anchor (R95 had none; decision for the Lead / CHECKER). The UPDATE must hold
no "|" (l. 11 is a table row); L-2 holds eight, so two replacements were made that are NOT title text: (r1) «n := |V|» → «n := the number
of vertices» (R94's «n the number of vertices of the game»); (r2) «|F|» → «the number of transitions of F» (three times; R93 / R94 / R95
wording; this also fixes D-1's reading in GAPS). Checked by script: with the five labels removed from both and (r1), (r2) undone, the
UPDATE equals the title body up to the tail (string equality); the tail equals the rule above; no "|"; «2026-10-30» once (the stamp).
(10) DATA of record = the packet's §9 (l. 236-245) with fixes E1.11 (the «longest» figure). Re-summed for this draft (python3 -I, scratch
sum52.py over experiments/si/heads52/{rwin,bffront,swcase}_{sbcg,alt,red}.txt from the 86becaa0 archive; these files are identical at
6a70a520 (cmp); 21:38:40Z by date -u, rc 0): 1,134 rows each (719 + 413 + 2). bffront: CH (in-block Ξ-changes) 36,834, BADW 0 (= packet
«36,834 in-block Ξ-changes, 0 with ℓ_(k+1)(x) ≤ j»). swcase: NE 13,998, WR 186, TT 13, RR 0, OT 0, all V* 0 (= packet «Case 1 13,998;
«WR» … 186; Case 2a 13; Case 2b 0; Case 2c 0; violations 0»; = REFEREE-2 l. 113 «These equal the packet's §9 figures exactly.»). rwin
(event-free blocks, WALL = the longest window over all W-runs of a run): no run has WALL ≥ n − 1; the longest is 67
(red/usplit/instances/gate_K64_n581, n 581, default best-reward start, rwin_sbcg.txt l. 479 «LMAX 68 E 1 WMAX 67 … WALL 67»; the same game
from its .start: WALL 3, rwin_alt.txt l. 413); on n ≤ 100 the longest is 63 (si/runlin/instances/runfam_K40, n 79, rwin_sbcg.txt l. 518);
the largest ratio WALL / n is 44 / 48 = 0.917 (red/xing/instances/x32_rand48). EVENT-FREE BLOCK RECONCILIATION, as recorded by both
referees: REFEREE §C §2 l. 26-41 (three engines; «Joint reading: the longest event-free block in the corpus is 67 at n 581 (best-reward
start), far below n − 1. The packet's §9 «the longest event-free block is 44 at n 48» is a mislabel. 44 / 48 = 0.92 is the largest ratio
WMAX / n, where x32_rand48 leads.»; l. 37 «My earlier «63» was the maximum over n ≤ 100 only (MAXN 100 skipped gate).»); REFEREE-2 §C C.4
l. 45 «Joint DATA reading: longest event-free block 63 on games with n ≤ 100 (runfam_K40), 67 on the whole corpus (gate_K64_n581). Both ≤
n − 1.»; REFEREE-2 L1 l. 20-22 corrects its «+ start» label to the default start; fixes E1.11 l. 55-57 agrees. All three figures (67, 63,
44 / 48) equal my re-sum. ONE DATA DISCREPANCY, not raised by anyone: E1.11's «Next: 63 (…runfam_K40 …); 55 (x32_rand64, n 64); 49
(ladderd0_k48_n156)» is not the lane's rank order: rwin_sbcg.txt has new/box52/out/topfix_n10.pg n 210 «WALL 58» (third longest), and the corpus
has red/so/instances/xsnf52_n64 at 52; REFEREE-2's 67 / 55 / 49 are its per-list maxima (logs at 301042bb: sbcg «max max_block: (67, …)», alns
«max max_block: (55, 'red/xing/instances/x32_rand64.pg#0')», alst «max max_block: (49,
'red/ul/instances/ladderd0_k48_n156.pg#start')», pins «max max_block: (32, 'red/free/instances/fx_K8_m32.pg#start')»), not a top three. Data wording only; every block ≤ n − 1; no signed
item uses a count.
(11) Discrepancies, recorded for CHECKER, no verdict affected: (i) stamps: both reports cite «Lead brief 2026-10-30 18:43Z» (REFEREE l. 2;
REFEREE-2 l. 4 «the Lead's 18:43Z figures») and were committed at 18:49:06Z (REFEREE; l. 6 «Runs 2026-10-30T18:45Z-18:48Z; report written
from 18:47Z») and 18:46:26Z (REFEREE-2, 3 minutes after the brief time, with a 1,134-run corpus check); the packet was frozen at 18:18:30Z
(6a70a520), so work may have begun before the brief's stamp; push times are not on record. REFEREE §C l. 3 «read 19:16Z», ea05b574
19:18:33Z; REFEREE-2 §C l. 3 «opened 19:07Z», 3fd4aaf0 19:14:21Z: consistent. The fixes file's F0 stamp «18:5xZ» vs its commit 051eb196
18:41:07Z (a time after its commit; as R95's «Lead 18:43Z»). (ii) REFEREE §C is not strictly append-only: aa5adfd4 is +22/−1 (the NEEDS
line rewritten); d6a33b10 is +11/−0, and its closing block (l. 96) still reads «NEEDS: Lead: SETTLE line L-2 with SETTLE-L5 (U scope and
name); I word-diff it.», not updated for §5. No verdict line was removed. The fixes file is append-only (three commits, each +N/−0:
051eb196 +9, a0970d36 +59, 86becaa0 +14; 82 lines). (iii) REFEREE-2 successor 23's L-1 MATCHES (b521c191) stands corrected by successor 24
in another file ((3)). (iv) REFEREE-2 §C C.4 l. 43 and its report l. 115 label 67 as «gate_K64_n581 + start»; corrected in R2-N5-SETTLE-L1
l. 20-22 (default start), as REFEREE §C l. 34-36 found from REFEREE-2's own log. (v) Counts that differ by run set (REFEREE n ≤ 100: 813
runs, 1,060 W-runs with transitions, 12,448 PLAY-CAUSE cases, 27,157 IDX-MONO and 266,486 LEX-BFS checks, l. 109-110; REFEREE-2 1,134 runs:
175,533 IDX and 651,871 LEX checks, l. 112), not by violations (0 everywhere). (vi) E1.11 «Next» list ((10)). (vii) REFEREE-2's line verdict on L-2 is by successor 24; its report, §C and L-1 file are by
successor 23 (all labelled (Opus 5.5, D15)); successor 24 corrected successor 23's L-1 verdict ((3)).
(12) Excluded: lane work after the freeze other than the SETTLE parts of 051eb196 (F0, the FLIP-EV DEAD pins), a0970d36 (entry 1, L-1) and
86becaa0 (entry 2, L-2): box 53 SBF (aeb8c311, accd388a), the box 52 §3 FLIP-CAUSE″ / FLIP-EV analysis in docs/si (051eb196, other than
F0); L-RED R144-R147 (incl. R147 SRC-SETTLE, 47fd9163), L-LIT T55-T62; REFEREE's and REFEREE-2's WRUN files in d6a33b10 / dd2333a2. Not
part of this entry.
(13) Commits: lane (claude/l-si): 6a70a520 (parent 71d1d0ac; freeze) → 051eb196 (F0) → … → a0970d36 (parent aeb8c311; entry 1, L-1) → …
→ 86becaa0 (parent accd388a; entry 2, L-2). REFEREE directly on claude/referee: 1df722e9 (parent ac78fb08) → fcea02e3 (WRUN) → ea05b574 →
aa5adfd4 → d6a33b10. REFEREE-2 directly on claude/referee-2: 301042bb (parent 284014ad) → … → 3fd4aaf0 (parent 9784fde6) → … → b521c191
(parent 04020305) → … → dd2333a2 (successor 24; parent b3bdc1a0, a Lead trunk commit). First trunk commits containing each (first-parent
walk of the local trunk since 12:00Z, binary search with git merge-base --is-ancestor, scratch firsttrunk.py): 6a70a520, 051eb196 → c5301e37
(18:54:18Z); 1df722e9 → ca0c1880 (19:07:41Z); 301042bb → 71e41ff7 (19:07:41Z); a0970d36 → 5a1be858 (20:00:31Z); ea05b574 → 8bb1c024
(20:00:31Z); 3fd4aaf0 → d7a3cb02 (20:00:32Z); b521c191 → e9165312 (20:16:16Z); aa5adfd4 → fb6c8e63 (20:42:26Z); 86becaa0 → 62391de1
(21:07:19Z); d6a33b10 → 78dc15f8 (21:33:54Z, LOCAL only); dd2333a2 → 38556650 (21:33:54Z, LOCAL only).
(14) Placement: after R95 (pending; at fd771a5e R94 is l. 7272 and "## Dead ends (kept;" l. 7476). A Dead-ends row for CONJECTURE FLIP-EV
(flipev_n20) is the Lead's call: it is lane-DEAD (L-SI F0, n5x and n5b agree; L-RED R145 independently, LEAD-STATE 19:07Z), NOT refereed
here (neither report re-ran it; both list §8 as not signed), and it is recorded in this entry under Not signed with its instance and
obstruction.

### R96 [refereed-only] N5 on EVERY game (SPEC S1-S5, under the standing SPEC premise of RESULTS R57 (1E-N3: S1's procedure realises the pointwise optimum; for S4a at a transition t → t + 1, σ_(t+1) is the pointwise optimum of the one-player arena H_t, H_t := S4a's arena at t (Even keeps σ_t ∪ Iσ_t, Odd follows τ_t)); premises RESULTS R15 (a), (d) and R86 (a)), with: a run is the sequence of states (σ_k, τ_k), a transition is written k → k + 1 (states k, k + 1), and an Even vertex y switches at k if σ_(k+1)(y) ≠ σ_k(y); n := |V|, m_E (m_O) := the number of edges leaving Even (Odd) vertices; values (c, P, ℓ) (cycle node, path set, length) as in SPEC S1, ⊴, ◁, ⊵, ▷ the SPEC S1 order (better for Even) and its strict and reverse forms, and x ⊕ (c, Q, ℓ) := (c, Q ∪ {x if x is more relevant than c}, ℓ + 1) (as in RESULTS R93 TIE); for a state k: Ξ_k := Ξ_{σ_k}, σ̄_k := S1's Odd counterstrategy to σ_k, and Iσ_k := Even's improving edges at k (SPEC S2: {(y, z) : Ξ_k(z) ▷ Ξ_k(σ_k(y))}); W-run F := RESULTS R89's (a maximal run of consecutive states of one τ-stretch none of whose transitions is an S4c fallback or changes λ_W, the cycle-node map of W), with τ and C := {v : λ_W(v) = v} fixed on F and |F| its number of transitions; for a state k of F: W_k := the [S1-val] valuation of the (σ_k, τ)-plays and ℓ_k(x) its length component at x; D_k := {Odd o : σ̄_k(o) ≠ τ(o)}; U_k := {σ̄_k(g) : g ∈ D_k} ∪ {the Ξ-successor of c (σ_k(c), or σ̄_k(c) if c is Odd) : c ∈ C} (L-RED R143's upward heads); H_k := S4a's arena at k (Even v keeps {σ_k(v)} ∪ Iσ_k(v), Odd follows τ); dist and the remaining edges at k := those of S4a's evaluation of H_k (si.py Engine.evaluate on the dual of H_k with dual-Even fixed to τ); for a transition k → k + 1 of F: (y, z) is W_(k+1)-tight at Even y ∉ C iff y ⊕ W_(k+1)(z) = W_(k+1)(y); an EVENT := a transition k → k + 1 of F at which (i) σ̄ changes, (ii) σ changes at some Even c ∈ C, or (iii) Ξ changes at some vertex of U_k ∪ U_(k+1), and a transition is EVENT-FREE iff it is not an EVENT; E_F := the number of events of F; for Odd o, c ∈ C and u ∈ V: SB_F(o), CN_F(c), HXU_F(u) := the numbers of transitions of F at which σ̄(o) changes, at which the Even vertex c switches, and at which u ∈ U_k ∪ U_(k+1) and Ξ(u) changes; Ξ^d_k := Odd's valuation of τ_k on G^d at state k (RESULTS R86's U): for every N5 run on every game and every W-run F of it: (Claim RG′) at every S4a step k → k + 1 of F, in the round of cycle node c, the remaining edges (x, y), x ≠ c, with dist(y) = dist(x) − 1 are exactly the W_(k+1)-tight arena edges of x with W_(k+1)-cycle node c; (Theorem RUN-SETTLE) if the transitions k0, …, k1 − 1 of F are all event-free, then for k0 ≤ k < k1 every Even vertex v switching at k and every vertex v whose Ξ changes at k has ℓ_(k+1)(v) ≥ k − k0 + 1, so k1 − k0 ≤ n − 1 (proof: induction on k − k0 with a least-ℓ violator, using R15 (a), Claim RG′, ARENA-MAX (L-RED R140, l-red 47000632; the S4a half of the R57 premise above) and L-LIT T54's LEX-BFS / IDX-MONO as signed in this packet's review, read at one S4a evaluation with W_(k+1); Cases 2, 2b via Lemma ONE-STEP (REFEREE-2 R2-N5-SRC §3.2, claude/referee-2 e8c1b62d; signed by REFEREE R-N5-SETTLE Addendum 1, claude/referee 8951ef7c), which closes gap G-SRC-1 (REFEREE R-N5-SRC §3, claude/referee 81f6b89c)); (Corollary RUN-COUNT) |F| ≤ n(E_F + 1) − 1; (Theorem HEAD-RED, an EQUIVALENCE) E_F ≤ Σ_(Odd o) SB_F(o) + Σ_(c ∈ C) CN_F(c) + Σ_(u ∈ V) HXU_F(u), so |F| ≤ n(1 + n·max_(Odd o) SB_F(o) + n·max_(c ∈ C) CN_F(c) + n·max_(u ∈ V) HXU_F(u)) − 1, and, as each count is ≤ |F|, for every family of games every W-run has polynomially many transitions iff max SB_F, max CN_F and max HXU_F are polynomial over all W-runs F; and (Corollary T-XCH, an EQUIVALENCE from RESULTS R86 (a) SW-RETURN on both sides and R15 (d)) every N5 run, with T its number of transitions (N5 iterations), has T ≤ m_E(1 + XE) + m_O(1 + XO), XE (XO) the most changes of one vertex's Ξ_k (Ξ^d_k) over the whole run, and, for every family of games, T is polynomial over all runs iff XE and XO are (2026-10-30) — a REDUCTION (no count is bounded here; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim; not to sign: CONJECTURES FLIP-EV (DEAD, fixes F0), HX-POLY, CN-POLY, XCN-POLY; Lemma ONE-STEP (Cases 2, 2b) is referee-originated) (P-N5-SETTLE, docs/si/P-N5-SETTLE-box52.md; L-SI successor 34; fixes docs/si/P-N5-SETTLE-fixes.md entries 1-5), CHECKER PASS (docs/checker/C106.md, checker PENDING)
- Object (L-SI successor 34, Opus 5.5, D18; frozen, unchanged during review): packet P-N5-SETTLE, docs/si/P-N5-SETTLE-box52.md, sha1
  aef403c3d8a003bcfc6742c4d1da084a1e21669f, 248 lines (l-si freeze 6a70a5207f3cb6b1613a0a2f5ec9c328af2b4f33, 2026-10-30T18:18:30Z, the
  file's only commit; identical at l-si head 86becaa0, at origin trunk a93c4b78 and at the local trunk head f7e070b7; first on trunk by
  c5301e37, 18:54:18Z; pinned in experiments/si/check.sh l. 927). Both referees measured the sha1 at 6a70a520 (REFEREE l. 3-5 «Both equal
  the Lead's figures.»; REFEREE-2 l. 2-4 «Both re-hashed in a detached worktree at 6a70a520: match»). The Lead's freeze word is quoted at
  l. 2-4 («FREEZE a small packet P-N5-SETTLE for the referees … Theorem RUN-SETTLE, Theorem HEAD-RED and Claim RG′, quoting L-RED R143's
  Lemma SETTLE verbatim (l-red 717f407a) with your proof's dependence on it explicit. …»; a message, not on file). Status (l. 7-9): «Status:
  REDUCTIONS and one EQUIVALENCE. No residual is bounded here. G-N5-TIME stays OPEN. This is not M3, not a step-4 pass, and not a TARGET.md
  claim.» «Object: N5 only (SPEC S1-S5).» Source (l. 6): docs/si/N5-HEADS-box52.md (l-si 71d1d0ac), «Where the two differ, THIS packet
  governs.»; not refereed here. Sections: §0 what to sign (l. 11-21), §1 setting and landed premises (l. 23-56: N5, priorities, run,
  values, ⊕, Ξ_k, W_k, val, ℓ_k, Iσ_k, H_k, W_k-tightness, W-run (R89 verbatim), STEP-SW, D_k, [R57], [R15] (a), (d), MON), §2 other lanes'
  lemmas and the packet's dependence on R143 (l. 58-92), §3 Claim RG′ (l. 94-120), §4 PLAY-CAUSE, W-MON, PATH (l. 122-140), §5 RUN-SETTLE
  and RUN-COUNT (l. 142-199), §6 HEAD-RED (l. 201-214), §7 T-XCH (l. 216-228), §8 CONJECTURES (l. 230-234), §9 DATA, DEAD, READING (l.
  236-245), proposed line (l. 247-248). Other lanes' texts inside the packet: verbatim at their SHAs (to check (5)).
  The RESULTS line, history: (1) the frozen line docs/si/P-N5-SETTLE-line.txt (6a70a520), sha1 6aa094e32b03317797a551ac2fc719749cf59ca7,
  the line both referees reviewed: REFEREE «does NOT match yet» (l. 34) with SETTLE-L1 (F), L2 (T), L3 (k) REQUIRED; REFEREE-2 «content
  MATCHES §3, §5-§7» with L-1 (F), L-2 (Iσ_k), L-3 (T) REQUIRED (l. 24). (2) L-1 997e39eee8d72ae94be4764bb1e3841914ffc78e (a0970d36): all
  joint items applied; REFEREE §C l. 77 REQUIRED SETTLE-L5; REFEREE-2 23 L1 l. 25 MATCHES, corrected by REFEREE-2 24 (L2 l. 14). (3) L-2
  1fcb33c5d96a20eb70abe06c29154ef343b33ae0 (86becaa0): REFEREE §C l. 88 and REFEREE-2 L2 l. 37: MATCHES (Opus 5.5, D15). L-2 supersedes
  the earlier lines; the title is L-2 verbatim with its own date (to check (1)). Neither referee found a FALSE statement; every REQUIRED
  item binds a symbol (F, T, k, Iσ_k) or fixes the scope of τ in Odd's valuation (SETTLE-L5).
  Setting (packet §1): N5 = SPEC S1-S5, any parity game, V = {0, …, n − 1}; priorities injective after SPEC's re-ranking; a run from any
  start pair; Ξ_k := the [S1-val] valuation of the (σ_k, σ̄_k)-plays; W_k := the valuation of the (σ_k, τ_k)-plays; a W-run as in R89 («a
  τ-stretch := a maximal run of consecutive states with τ constant; a W-run := a maximal run of consecutive states of one τ-stretch none of
  whose transitions is an S4c fallback or changes λ_W»), on which τ and C := {v : λ_W(v) = v} are fixed; «Every transition of F switches
  some Even vertex: with τ fixed and no S4c fallback, S4a changed σ (SPEC S4).» (l. 48); MON «Hence Ξ_(k+1) ⊵ Ξ_k pointwise at every
  transition.» (l. 56). §1 cells: REFEREE «CHECKED» (l. 24); REFEREE-2 «CHECKED» with N-1 (l. 15). Names: the line's U_k is R143's upward
  heads, not landed R38's U_k (Odd's valuation, RESULTS l. 1822); Odd's valuation is Ξ^d_k in the line (to check (6)).
- Claims signed (both referees "(Opus 5.5, D15)": REFEREE successor 20; REFEREE-2 successor 23, line L-2 also successor 24). Items (a)-(e)
  are SIGNED in both verdict tables (REFEREE "## Verdicts" l. 21-35 of R-N5-SETTLE.md; REFEREE-2 "## 1. Verdict table" l. 12-26 of
  R2-N5-SETTLE.md) and in both §C cross-maps (REFEREE §C l. 6-24; REFEREE-2 §C C.1 l. 6-19); the table is to-check (4). All are about N5 on
  every game, inside W-runs, except (e), about whole runs. Premises LANDED (as L-2 names them): SPEC S1-S5; RESULTS R15 (a), (d); R86 (a)
  SW-RETURN and its dual; R89's W-run; R93's ⊕; standing premise: RESULTS R57's SPEC premise (1E-N3), used by RG′ (the computed values are
  W_(k+1)) and, as ARENA-MAX, by W-MON and RUN-SETTLE Cases 2, 2b, 2c. Unlanded, signed as used here and named in the proof note only:
  L-LIT T54 LEX-BFS / IDX-MONO (Case 2a), L-RED R140 ARENA-MAX (= [R57] for S4a). The code's match to SPEC is DATA (R15 G-N5T-1). No item
  uses a count.
  (a) Claim RG′ (§3, l. 94-120): «Statement. In c's round, the remaining edges (x, y), x ≠ c, with dist(y) = dist(x) − 1 are exactly the
      W_(k+1)-tight arena edges of x whose W_(k+1)-cycle node is c.» (l. 103-104), at ANY transition k → k + 1 of a W-run; proof (A) bit
      invariant per processed u, (B) tight edges survive, «No step of the proof uses W_(k+1) = W_k.» (l. 119-120). Cells: REFEREE «SIGNED»
      (l. 28; §3 l. 37-51, «Nothing uses W_(k+1) = W_k ✓»); REFEREE-2 «SIGNED», «none» (l. 18; §2.2 l. 36-47, against si.py Engine.evaluate
      l. 112-149).
  (b) Theorem RUN-SETTLE (§5, l. 142-147): «Let F be a W-run, and let the transitions k0, k0 + 1, …, k1 − 1 of F all be event-free.»;
      «(S_j) Every Even y that switches at k has ℓ_(k+1)(y) ≥ j + 1.»; «(X_j) Every vertex x with Ξ_(k+1)(x) ≠ Ξ_k(x) has ℓ_(k+1)(x) ≥ j + 1.»;
      «Consequently k1 − k0 ≤ max_x ℓ(x) ≤ n − 1.» (j := k − k0). L-2 states S_j, X_j and «k1 − k0 ≤ n − 1». Proof: S_j ⇒ X_j by PLAY-CAUSE;
      S_j by induction with a least-ℓ violator, (MIN), PATH; Cases 1 (b ∉ H_(k−1)(y): R15, X_(j−1)), 2a (LEX-BFS / IDX-MONO at k − 1 → k and
      k → k + 1 give opposite strict orders), 2b and 2c (ARENA-MAX at k → k + 1). Cells: REFEREE «SIGNED» (l. 30; §5 l. 64-90, «The cases
      exhaust ✓»); REFEREE-2 «SIGNED», «none» (l. 20; §2.5 l. 67-83, «The four cases exhaust»).
  (c) Corollary RUN-COUNT (§5, l. 148-149): «For every W-run F with E_F event transitions, |F| ≤ E_F + (E_F + 1)(n − 1) = n(E_F + 1) − 1.»,
      |F| its transitions (to check (7), D-1). Cells: REFEREE l. 30, l. 91 «RUN-COUNT ✓»; REFEREE-2 l. 20, l. 84 «(event-free transitions
      form ≤ E_F + 1 blocks of ≤ n − 1)».
  (d) Theorem HEAD-RED (§6, l. 201-212): «(⇐) E_F ≤ Σ_(Odd o) SB_F(o) + Σ_(c ∈ C) CN_F(c) + Σ_u HXU_F(u).», hence by RUN-COUNT «|F| ≤
      n·(1 + n·max_o SB_F(o) + n·max_c CN_F(c) + n·max_u HXU_F(u)) − 1.»; «(⇒) Each of SB_F(o), CN_F(c), HXU_F(u) is ≤ |F|.»; so, for every
      family of games, polynomial W-runs ⇔ polynomial max SB_F, max CN_F, max HXU_F. Cells: REFEREE «SIGNED» (l. 31; l. 94-97); REFEREE-2
      «SIGNED», «none» (l. 21; l. 86).
  (e) Corollary T-XCH (§7, l. 216-228): «T ≤ Σ_v SW(v) (R15 (d): every iteration changes σ or τ)»; «Σ_v SW(v) = Σ_(edges (v, c)) ENT(v, c)
      ≤ Σ_(edges) (1 + RISE(c)) (R86 (a), both sides, R = the whole run)»; «hence T ≤ m_E(1 + XE) + m_O(1 + XO).»; «Conversely XE, XO ≤ T.»
      «an EQUIVALENCE and a reformulation of G-N5-TIME, not a bound» (l. 226-227). Only the composition is new; RISE^U(c) counts changes of
      Odd's valuation at each state (L-2: Ξ^d_k, SETTLE-L5). Cells: REFEREE «SIGNED (composition of landed R86 (a), both sides, with R15
      (d))» (l. 32; l. 98-101); REFEREE-2 «SIGNED», «none» (l. 22; l. 87-88, «R86 (a) on both sides (the landed text has «Dually for Odd v
      with U.»), R = the whole run»).
  Signed by both as PROOF STEPS, not stated by the line (to check (4)): Lemma PLAY-CAUSE (§4 l. 124-125: «If k → k + 1 is event-free and
  Ξ_(k+1)(x) ≠ Ξ_k(x), then some Even y with λ_W(y) ≠ y switches at k and lies on x's (σ_(k+1), τ)-path to λ_W(x).»), W-MON (l. 138: «In a
  W-run, W_(k+1) ⊵ W_k pointwise: ARENA-MAX with ρ = σ_k, a strategy of H_k.»), PATH (l. 139-140), T54 IDX-MONO / LEX-BFS as used (one S4a
  evaluation, W_(k+1)-tight, keys on (σ_(k+1), τ)-paths). Cells: REFEREE l. 26, l. 29, §4 l. 53-62; REFEREE-2 l. 17, l. 19, §2.3-§2.4 l.
  48-66; REFEREE §C l. 10-11 «agree. Two sources, the same derivation» / «agree. Both: Ξ(x) is a function of (y_0 … y_i, Ξ(y_(i+1))) even if
  the play re-enters the prefix»; REFEREE-2 §C l. 11, l. 14 «SIGNED by both».
  Gap maps: REFEREE l. 35 «No gap in the packet. Nothing FALSE.»; REFEREE-2 l. 26 «No gap in the packet. Nothing FALSE among the items to
  sign.»; REFEREE §C l. 44 «Packet items to sign: EMPTY on both sides. Nothing FALSE.»; REFEREE-2 §C l. 19 «Joint gap map for the packet:
  EMPTY. Nothing FALSE on either side.»
  The RESULTS line (L-2) claims less than the reports: no PLAY-CAUSE, W-MON, PATH, LEX-BFS / IDX-MONO as statements, no «≤ max_x ℓ(x)».
  Every clause it states is one of (a)-(e).
- Fixes (docs/si/P-N5-SETTLE-fixes.md, L-SI successors 34-35, APPEND-ONLY, F0 and two entries, three commits each +N/−0: 051eb196 (+9/−0,
  b0adbcff…, F0), a0970d36 (+59/−0, 87f48e2c…), 86becaa0 (+14/−0, sha1 42d9a381f91f106a8e3bc15e589fef0a05e64186, 82 lines; = l-si head =
  origin trunk a93c4b78 = local f7e070b7; the last commit touching the file)). Header (l. 1-2): «The frozen file is never edited. Each
  entry names the section, says whether a TO-SIGN item is affected, and gives the evidence.» Each item, with the referees' words:
  - F0 (l. 4-9; 18:5xZ): CONJECTURE FLIP-EV DEAD, instance experiments/si/heads52/inst/flipev_n20.pg (sha1
    3ebc110b630e5ca3de12bd5e13b751f9e20b2a1c, n 20) + .start (5065f1888fc936d5736f18019de351d5b0965bd5), «transition 2 → 3: Odd 10, not its
    own Ξ-cycle node, leaves D with both targets' Ξ fixed, in a W-run with no event (iii). The cause is Odd 14 entering D (Ξ(τ(14)) rose;
    its new target is tied).» (l. 6-7); «§§3-7 (the items to sign) do not use FLIP-EV.» (l. 9).
  - Entry 1 (l. 11-68; REFEREE 1df722e9, REFEREE-2 301042bb): E1.1-E1.4 REQUIRED (F; T; k; Iσ_k), E1.5-E1.8 precision (event-free, ⊕, Iσ_k,
    ranges, «for every family of games»; ℓ_(k+1)(v); proof-note status; scope tail), applied in L-1; packet errata E1.9-E1.13 (to check
    (8)); L-1 at l. 68.
  - Entry 2 (l. 70-82; REFEREE aa5adfd4): E2.1 SETTLE-L5 (REQUIRED; «U := Odd's valuation of τ on G^d (RESULTS R86)» → «Ξ^d_k := Odd's
    valuation of τ_k on G^d at state k (RESULTS R86's U)» and T-XCH «Ξ_k (Ξ^d_k)»), E2.2 (optional) «and, for every family of games, T is
    polynomial over all runs iff XE and XO are», E2.3 «entries 1-2)»; L-2 at l. 82.
  No fix changes a signed statement of the packet: E1.1-E1.8 and E2.1-E2.3 bind symbols or word the line; E1.9-E1.13 are packet-text errata
  outside the signed statements (each «No signed item changes.»); F0 touches only a CONJECTURE.
- Not signed: §1 (setting; «CHECKED» by both); §2 other lanes' texts: R143 U_k / EVENT used as definitions only, SETTLE (B), (C) not used;
  R140 ARENA-MAX «quoted verbatim. Used as [R57]» (REFEREE l. 25); T54 IDX-MONO / LEX-BFS signed only as used (proof steps, above); the
  packet errata; §8 CONJECTURES, «NOT to sign»: FLIP-EV (l. 231-233), HX-POLY («max HXU_F polynomial»), CN-POLY, XCN-POLY («σ̄-changes at own
  Ξ-cycle nodes») (l. 234), all open except FLIP-EV; §8's FLIP-RED sentence void (F0); §6's «Comparison (READING, not to sign)» (l.
  213-214); §9 DATA, DEAD, READING.
  DEAD, each with the instance that killed it: CONJECTURE FLIP-EV («every σ̄(o)-change at k → k + 1 of a W-run that moves o out of D or
  within D (old target ≠ τ(o)) happens at a transition with an event (iii), whenever o is not its own Ξ-cycle node at k or at k + 1», l.
  231-232): flipev_n20, transition 2 → 3, Odd 10 leaves D with no event (iii) in the W-run; obstruction (F0 l. 7): «The cause is Odd 14
  entering D (Ξ(τ(14)) rose; its new target is tied).»; pins check.sh l. 930-935 (re-run, Data); lane-DEAD (L-SI; n5x and n5b agree), not
  refereed here. Lane DEAD item of the packet (§9 l. 242-243), not a refereed dead end of this entry: the front «measured by the distance
  along the Ξ-play to D ∪ C» (red/ul/instances/ladderd0_k12_n48 + start, 11 violations; pinned «BAD1 11»). Lane and referee work after the
  freeze other than the SETTLE fixes commits is not part of this entry (to check (12)).
- Referee strengthening (NOT part of this entry; remarks of one referee, remarks of both outside the verdict cells, readings):
  (i) REFEREE l. 45-46 and REFEREE-2 l. 44: a good-u edge u → y with y ∈ M is never length-tight, so RG′'s «exactly … with dist(y) =
      dist(x) − 1» is unaffected (REFEREE §C l. 9 «Both note …»).
  (ii) PLAY-CAUSE when the play re-enters its prefix (path sets are sets): REFEREE-2 l. 62, REFEREE l. 57-58; §C l. 11.
  (iii) REFEREE-2 l. 76: «(c is the same cycle node at both transitions: λ_W is fixed on F.)»; l. 77-78 (Case 2b) N-1's condition holds.
  (iv) Mutation controls (REFEREE l. 113-117): MUT 4 (LEX with argmax) and MUT 2 (IDX with the largest index) bite; MUT 5 (fronts j + 2)
      bites on gci2_n12 + start, «so the front is attained, as the packet says»; «MUT 1 (block bound n − 2) and MUT 3 (event (iii) dropped)
      never bit on the pins», so the n − 1 block bound and event (iii) have no biting control on the pins.
  (v) Self-corrections: REFEREE §C l. 14 «I missed it here.» (R2 N-1); l. 23 «MISSED» (R2 L-6); REFEREE-2 §C l. 24 «I missed it.» (SETTLE-L3),
      l. 28 «I missed ⊕ and «event-free»»; REFEREE-2 24 L2 l. 14 (successor 23 missed SETTLE-L5 on L-1).
  (vi) READING (packet §6 l. 213-214): «XI-RUN (P-N5-WRUN §3) needs Ξ-changes at EVERY vertex. Here only upward heads are counted, plus
      σ̄-changes and W-cycle-node switches.»; packet l. 91-92: on a W-constant interval RUN-SETTLE gives |I| ≤ n(E_I + 1) − 1, «weaker than
      SETTLE's (D + 1)(E_I + 1) − 1». Not signed.
- Honest limits: (i) REDUCTIONS and two EQUIVALENCES: no count is bounded; HX-POLY, CN-POLY, XCN-POLY and G-N5-TIME stay open; T-XCH is a
  reformulation of G-N5-TIME, not a bound (packet l. 226-227). (ii) RUN-SETTLE, RUN-COUNT and HEAD-RED are inside W-runs; W-runs are not
  whole runs (τ-changes, S4c fallbacks and λ_W-changes cut runs into W-runs, R89). (iii) Case 2a rests on L-LIT T54's LEX-BFS / IDX-MONO,
  which are not landed: both referees signed them as used, at one S4a evaluation with W_(k+1)-tightness and RG′, re-derived from SPEC S1
  (iv) (REFEREE) and from si.py (REFEREE-2); the line names them in a proof note only. (iv) Claim RG′ and the tightness rules are about S1's
  evaluation procedure as SPEC S1 (iii)-(iv) and si.py Engine.evaluate define it (si.py named without a SHA in the line; e688b963 at
  6a70a520 = 86becaa0 = trunk); standing premise R57 (1E-N3); the code's match to SPEC is DATA (R15 G-N5T-1). (v) R143's Lemma SETTLE is
  NOT landed and NOT used beyond its definitions. (vi) No biting mutation control for the n − 1 block bound or for event (iii) on the pins
  (Referee strengthening (iv)). (vii) CONJECTURE FLIP-EV is DEAD (lane). (viii) Counts are transitions, not bit operations; no running-time
  bound. (ix) Not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open.
- Data (DATA, not proof): pinned (packet §9 l. 236: «pins in experiments/si/check.sh «box 52», tools experiments/si/heads52/ at l-si
  71d1d0ac»). experiments/si/check.sh at 6a70a520: sha1 7b7a61b921272fb9c00dae385b725ff377e28ad8, 929 lines; at 86becaa0: sha1
  117fdee6faa687a08464d1eda46b2778183c8717, 969 lines (= trunk); l. 1-929 identical (the diff only appends l. 930-969). The «box 52» label is
  shared: l. 853-857 is box 52 TXC-DESCENT (docs/si/N5-TXCD-box52.md, not this entry); this entry's blocks are l. 901-918 (RUN-SETTLE front,
  Ξ-front DEAD, proof cases, corpus outputs), l. 919-925 (§3 FLIP-EV data), l. 926-929 (packet and line 6aa094e3 frozen), and at 86becaa0
  l. 930-935 (FLIP-EV DEAD, flipev_n20), l. 964-966 (L-1 pinned), l. 967-969 (L-2 pinned). Re-run for this draft from a `git archive` of
  each commit (experiments/ and docs/si/; from experiments/si; `python3 -I`; outputs to scratch files; exit codes read): l. 901-929 at
  6a70a520 and l. 901-935 + l. 964-969 at 86becaa0, each under `set -euo pipefail`, 21:38:19Z-21:38:21Z by date -u (read before and after),
  rc 0 each: «si (box 52: RUN-SETTLE front, Xi-front DEAD, proof cases, defect set, flips): PASS», «si (box 52 §3: FLIP-CAUSE'' DEAD,
  FLIP-EV data): PASS», «si (box 52: P-N5-SETTLE frozen): PASS», and at 86becaa0 also «si (box 52 §3: FLIP-EV DEAD, flipev_n20): PASS»,
  «si (P-N5-SETTLE L-1 pinned): PASS», «si (P-N5-SETTLE L-2 pinned): PASS». Single pins (86becaa0 archive): «RWIN x32_rand48.pg n 48 LMAX
  44 E 0 WMAX 44 WN 0.917 EI 0 EII 0 EIII 0 WALL 44»; «BFF gci2_n12.pg n 12 CH 14 MINF0 -6 MINF1 1 NOD 0 BAD1 0 BAD0 7 MINW1 1 BADW 0 SWB
  0», with MUT=1 «… BADW 2 SWB 0»; «SWC u23sw64_n32.pg n 32 J0 19 NE 44 WR 0 TT 5 RR 0 OT 0 VNE 0 VWR 0 VTT 0 VRR 0 VOT 0 MINJ 3»; rc 0.
  Files (identical at 6a70a520 and 86becaa0): heads52/rwin.py 737335bbaadf30a9b959f1ee006c5e8f24bab966, bffront.py
  825fb253af0956c83595aa5c5c59d2033ea6011c, swcase.py 3617078eae4f3876cc67e1afa7e1cc608360ddec, rwin_sbcg.txt
  39d3275bf5aa49ed5fb8f799c91ee51418d220db, rwin_alt.txt f544a5dbe9e23ce7f5318e30784531596be592eb, rwin_red.txt
  a87f4c51639ab730949201cedaba2f12b1b31341; instances red/usplit/instances/gate_K64_n581.pg a93c7c8be2c39e333cd61755f7ae4cd8ebc0ff98,
  si/runlin/instances/runfam_K40.pg 287a185d6b82f3ed196abb65726152c982c71f60, red/xing/instances/x32_rand48.pg
  865321803e5b9bc67ccf67fc9b151789c2dbd82a, n5-epoch/instances/gci2_n12.pg 67b6e166049f3316b10c7c655c1082a334b281a0 (.start
  d60e70ee9efe210882dd2700ff556cbaaa23210f).
  DATA OF RECORD (packet §9 l. 237-241 with fixes E1.11; corpus box 50b's lists (719 + 413) plus latew_K16_m32 and fx_K8_m32, 1,134 runs,
  n5x): bffront 36,834 in-block Ξ-changes, 0 with ℓ_(k+1)(x) ≤ j; front attained on gci2_n12 + start (MUT=1 control BADW 2); swcase Case 1
  13,998, WR 186, Case 2a 13, Case 2b 0, Case 2c 0, violations 0; event-free blocks: longest 67 (gate_K64_n581, n 581, default best-reward
  start), 63 on n ≤ 100 (runfam_K40, n 79), largest ratio 44 / 48 (x32_rand48); every block ≤ n − 1. Re-summed for this draft: equal (to
  check (10)). Second engine: red/seg/xeng.py (n5b SPEC) agrees on the four instances in heads52/inst/ (packet l. 244-245); corpus tools n5x
  only.
  REFEREE (successor 20; own docs/referee/scratch/settle_probe.py, `python3 -I`; no lane code): run set box 83 / 50b lists, n ≤ 100: «813
  runs (740 games, 73 skipped for n > 100), all RC 0; 1,060 W-runs with transitions, 8,066 W-run transitions.» (l. 109); «VIOLATIONS 0 for
  every check.» (l. 111); «Longest event-free block: 63 (si/runlin/instances/runfam_K40, n 79, best-reward start).» (l. 112); mutations (l.
  113-117); §C §2: gate_K64_n581 67 from the best-reward start, 3 from its .start (l. 28).
  REFEREE-2 (successor 23; own docs/referee-2/R2-N5-SETTLE/settle_check.py, «lane heads52 code NOT imported», l. 109): the lane's 1,134
  runs; «**0 violations** of S, X, BLK, RC, PC, HR, WM, IDX, LEX, TX on every run» (l. 111); 175,533 IDX and 651,871 LEX checks, 0 failures
  (l. 112); case split «These equal the packet's §9 figures exactly.» (l. 113); events (i) 4,625, (ii) 37, (iii) 4,741, max E_F 528
  (latew_K16_m32) (l. 114); longest block 67 (gate_K64_n581, default start: L1 l. 20-22). No signed statement uses any count.
- Signatures: REFEREE docs/referee/R-N5-SETTLE.md (report 1df722e9b65bbb3ae6457b416d267ce594651cf4, 2026-10-30T18:49:06Z, committed
  directly on claude/referee (parent ac78fb08), first on trunk by ca0c1880 (19:07:41Z); sha1 f534ef331f20defa2586bbda69c0c0244266f523, 160
  lines, unchanged since (= referee head d6a33b10); successor 20): §1 CHECKED; §3-§7 SIGNED; T54 IDX-MONO / LEX-BFS «SIGNED as used in Case
  2a» (l. 26); «No gap in the packet. Nothing FALSE.» (l. 35). §C docs/referee/R-N5-SETTLE-C.md (ea05b574a9645d7764e7f1bbc35f7e1fd64a7abd,
  2026-10-30T19:18:33Z, new file, 64 lines, sha1 e7a0020b2fbbfd9d2590a40fac0188afe32ba764; trunk 8bb1c024, 20:00:31Z): cross-map «agree» on
  every item (l. 6-24), joint gap map EMPTY (l. 44), block reconciliation (§2); §4 aa5adfd46c7cff9a618c56475cf6b312930c4e54 (20:01:17Z,
  +22/−1, 85 lines, b58e19b0…; trunk fb6c8e63, 20:42:26Z): «Verdict on L-1: REQUIRED CHANGE, SETTLE-L5 (Opus 5.5, D15). Everything else
  MATCHES.» (l. 77); §5 d6a33b10923bb93d4b0b46aca810ba5fe59e8c69 (21:08:23Z, +11/−0, 96 lines, sha1
  8ab33803ae7ae8ecdcf7fd1abb852d73f7570da3, the last commit touching the file (= origin referee head); merged into the LOCAL trunk by 78dc15f8
  (21:33:54Z), not on origin trunk a93c4b78): «Verdict on L-2: MATCHES (Opus 5.5, D15).» (l. 88). REFEREE-2 docs/referee-2/R2-N5-SETTLE.md
  (report 301042bba58f59ea7bf0ecb97dd5764878483aac, 2026-10-30T18:46:26Z, committed directly on claude/referee-2 (parent 284014ad), first on
  trunk by 71e41ff7 (19:07:41Z); sha1 a8b4f4813eb4a8eda9af3e51ae0c127f72a33bd9, 125 lines, unchanged since; successor 23): §1 CHECKED; §3-§7
  SIGNED; «No gap in the packet. Nothing FALSE among the items to sign.» (l. 26). §C docs/referee-2/R2-N5-SETTLE-C.md
  (3fd4aaf09e00e2b24336b5a6f9c025b47a7dd4d5, 2026-10-30T19:14:21Z, new file, 53 lines, sha1 a5b3e53c9ec430e853b654d5a8e32d9d03a7b89c,
  unchanged since; first on trunk by d7a3cb02, 20:00:32Z): «Joint gap map for the packet: EMPTY. Nothing FALSE on either side.» (l. 19).
  Line files: R2-N5-SETTLE-L1.md (b521c191464c3dfb87f93ef1b2258008ced12ab2, 20:00:44Z, successor 23, 25 lines, a75eb308…; L-1 MATCHES,
  corrected by successor 24); R2-N5-SETTLE-L2.md (dd2333a2ea6ae9d7e5983a909dcd44d06da4db5e, 21:08:40Z, successor 24, 37 lines, sha1
  677b1486f216f35145567cf2ed51de82784f0373; = origin referee-2 head; merged into the LOCAL trunk by 38556650 (21:33:54Z), not on origin trunk
  a93c4b78): «(a) SETTLE-L5 is REQUIRED: I agree.» (l. 36); «L-2 (1fcb33c5): **MATCHES** (Opus 5.5, D15). No required change.» (l. 37).
  INDEPENDENCE: REFEREE l. 7 «Independence: I opened no docs/referee-2/ file for this packet.»; REFEREE §C l. 3-4 «I opened
  docs/referee-2/R2-N5-SETTLE.md @ 301042bb (125 lines) only after that word, and after my report R-N5-SETTLE.md (1df722e9) was pushed.»
  REFEREE-2 l. 4 «Independence: written before opening any docs/referee/ file for SETTLE.»; REFEREE-2 §C l. 2-3: its report «pushed before I
  opened any docs/referee/ SETTLE file», REFEREE's report «opened 19:07Z on the Lead's word». No review imported lane code (REFEREE
  settle_probe.py; REFEREE-2 l. 109); the lane's scripts ran only as the pinned blocks.
  §C (both): verdicts on every packet item identical; no disagreement in substance. Differences of reading, resolved: Iσ_k (REFEREE
  precision → REQUIRED, §C l. 19); SETTLE-L3 (REFEREE only; agreed REQUIRED by REFEREE-2 §C l. 24); the block-length figures (63 vs 67,
  reconciled: REFEREE's n ≤ 100 cap; REFEREE §C §2, REFEREE-2 §C C.4). Notes map (REFEREE §C l. 14-24; REFEREE-2 §C C.2-C.3): R2 N-1 (⊕) =
  packet erratum, agreed; R2 N-2 = REFEREE SETTLE-N2 (same observation); REFEREE SETTLE-N1 accepted by REFEREE-2 as a note (§C l. 37-38).
  Later: SETTLE-L5 (REFEREE §4; agreed REQUIRED by REFEREE-2 24, L2 l. 6-14).
- TARGET.md diff: «n := |V|» is TARGET.md §1 l. 8's n («n = |V|, m = |E|, d = |pr(V)| ≤ n + 1.»), V TARGET's vertex set (l. 6); m_E + m_O
  = TARGET's m; games are TARGET.md §1 games (REFEREE-2 l. 105 «No M4 claim. TARGET.md's n.»). The line makes no M4 claim and no TARGET
  claim; its own scope clause reads «a REDUCTION (no count is bounded here; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md
  claim; not to sign: CONJECTURES FLIP-EV (DEAD, fixes F0), HX-POLY, CN-POLY, XCN-POLY)». REFEREE l. 19 «Scope (D1): REDUCTIONS and two
  EQUIVALENCES (HEAD-RED, T-XCH), N5 only. No count is bounded. G-N5-TIME stays OPEN. Not a TARGET.md claim.»; REFEREE-2 l. 10 «Scope:
  REDUCTIONS and one EQUIVALENCE inside W-runs of N5, plus a whole-run reformulation (T-XCH). Nothing is bounded. G-N5-TIME stays OPEN.»
  Not a claim of TARGET.md §1 or §2 (a claim about S1's evaluation, a bound on event-free blocks and two equivalences about N5 runs on every
  game; no bound on a W-run, on a run or on running time; no algorithm claim); not a step-4 pass. GAPS G-N5-TIME: open.

Proposed GAPS line-11 UPDATE (append-only), to go AFTER R95's UPDATE of G-N5-TIME (pending, R95-draft l. 548; at present the last on l. 11
is R94's, «UPDATE 2026-10-30 18:40Z: RESULTS R94 (P-N5-FIXD; CHECKER C104 5c4d6e45) …»), built by script only from the clauses of the title
line L-2, with R94's / R95's construction (labels behind their clauses; the scope tail as in R95's UPDATE, the source parenthesis kept). L-2
holds eight "|"; the UPDATE holds none: (r1) «n := |V|» → «n := the number of vertices»; (r2) «|F|» → «the number of transitions of F»
(three times); these replacements are not title text (to check (9)). Landing time and CHECKER commit to be filled at landing:
UPDATE 2026-10-30 <HH:MM>Z: RESULTS R96 (P-N5-SETTLE; CHECKER C106 <checker>) [refereed-only] LANDED: N5 on EVERY game (SPEC S1-S5, under the standing SPEC premise of RESULTS R57 (1E-N3: S1's procedure realises the pointwise optimum; for S4a at a transition t → t + 1, σ_(t+1) is the pointwise optimum of the one-player arena H_t, H_t := S4a's arena at t (Even keeps σ_t ∪ Iσ_t, Odd follows τ_t)); premises RESULTS R15 (a), (d) and R86 (a)), with: a run is the sequence of states (σ_k, τ_k), a transition is written k → k + 1 (states k, k + 1), and an Even vertex y switches at k if σ_(k+1)(y) ≠ σ_k(y); n := the number of vertices, m_E (m_O) := the number of edges leaving Even (Odd) vertices; values (c, P, ℓ) (cycle node, path set, length) as in SPEC S1, ⊴, ◁, ⊵, ▷ the SPEC S1 order (better for Even) and its strict and reverse forms, and x ⊕ (c, Q, ℓ) := (c, Q ∪ {x if x is more relevant than c}, ℓ + 1) (as in RESULTS R93 TIE); for a state k: Ξ_k := Ξ_{σ_k}, σ̄_k := S1's Odd counterstrategy to σ_k, and Iσ_k := Even's improving edges at k (SPEC S2: {(y, z) : Ξ_k(z) ▷ Ξ_k(σ_k(y))}); W-run F := RESULTS R89's (a maximal run of consecutive states of one τ-stretch none of whose transitions is an S4c fallback or changes λ_W, the cycle-node map of W), with τ and C := {v : λ_W(v) = v} fixed on F; for a state k of F: W_k := the [S1-val] valuation of the (σ_k, τ)-plays and ℓ_k(x) its length component at x; D_k := {Odd o : σ̄_k(o) ≠ τ(o)}; U_k := {σ̄_k(g) : g ∈ D_k} ∪ {the Ξ-successor of c (σ_k(c), or σ̄_k(c) if c is Odd) : c ∈ C} (L-RED R143's upward heads); H_k := S4a's arena at k (Even v keeps {σ_k(v)} ∪ Iσ_k(v), Odd follows τ); dist and the remaining edges at k := those of S4a's evaluation of H_k (si.py Engine.evaluate on the dual of H_k with dual-Even fixed to τ); for a transition k → k + 1 of F: (y, z) is W_(k+1)-tight at Even y ∉ C iff y ⊕ W_(k+1)(z) = W_(k+1)(y); an EVENT := a transition k → k + 1 of F at which (i) σ̄ changes, (ii) σ changes at some Even c ∈ C, or (iii) Ξ changes at some vertex of U_k ∪ U_(k+1), and a transition is EVENT-FREE iff it is not an EVENT; E_F := the number of events of F; for Odd o, c ∈ C and u ∈ V: SB_F(o), CN_F(c), HXU_F(u) := the numbers of transitions of F at which σ̄(o) changes, at which the Even vertex c switches, and at which u ∈ U_k ∪ U_(k+1) and Ξ(u) changes; Ξ^d_k := Odd's valuation of τ_k on G^d at state k (RESULTS R86's U): for every N5 run on every game and every W-run F of it: at every S4a step k → k + 1 of F, in the round of cycle node c, the remaining edges (x, y), x ≠ c, with dist(y) = dist(x) − 1 are exactly the W_(k+1)-tight arena edges of x with W_(k+1)-cycle node c (Claim RG′); if the transitions k0, …, k1 − 1 of F are all event-free, then for k0 ≤ k < k1 every Even vertex v switching at k and every vertex v whose Ξ changes at k has ℓ_(k+1)(v) ≥ k − k0 + 1, so k1 − k0 ≤ n − 1 (proof: induction on k − k0 with a least-ℓ violator, using R15 (a), Claim RG′, ARENA-MAX (L-RED R140, l-red 47000632; the S4a half of the R57 premise above) and L-LIT T54's LEX-BFS / IDX-MONO as signed in this packet's review, read at one S4a evaluation with W_(k+1); Cases 2, 2b via Lemma ONE-STEP (REFEREE-2 R2-N5-SRC §3.2, claude/referee-2 e8c1b62d; signed by REFEREE R-N5-SETTLE Addendum 1, claude/referee 8951ef7c), which closes gap G-SRC-1 (REFEREE R-N5-SRC §3, claude/referee 81f6b89c)) (Theorem RUN-SETTLE); the number of transitions of F ≤ n(E_F + 1) − 1 (Corollary RUN-COUNT); E_F ≤ Σ_(Odd o) SB_F(o) + Σ_(c ∈ C) CN_F(c) + Σ_(u ∈ V) HXU_F(u), so the number of transitions of F ≤ n(1 + n·max_(Odd o) SB_F(o) + n·max_(c ∈ C) CN_F(c) + n·max_(u ∈ V) HXU_F(u)) − 1, and, as each count is ≤ the number of transitions of F, for every family of games every W-run has polynomially many transitions iff max SB_F, max CN_F and max HXU_F are polynomial over all W-runs F (Theorem HEAD-RED, an EQUIVALENCE); and every N5 run, with T its number of transitions (N5 iterations), has T ≤ m_E(1 + XE) + m_O(1 + XO), XE (XO) the most changes of one vertex's Ξ_k (Ξ^d_k) over the whole run, and, for every family of games, T is polynomial over all runs iff XE and XO are (Corollary T-XCH, an EQUIVALENCE from RESULTS R86 (a) SW-RETURN on both sides and R15 (d)): a REDUCTION; no count is bounded here; not to sign: CONJECTURES FLIP-EV (DEAD, fixes F0), HX-POLY, CN-POLY, XCN-POLY; Lemma ONE-STEP (Cases 2, 2b) is referee-originated (P-N5-SETTLE, docs/si/P-N5-SETTLE-box52.md; L-SI successor 34; fixes docs/si/P-N5-SETTLE-fixes.md entries 1-5). G-N5-TIME stays open.


Addendum 1 (Lead, 2026-10-31 00:38:27Z by date -u, read in the same command as this append; for C106): the title is now line revision L-5 (claude/l-si ce7bdc3b, docs/si/P-N5-SETTLE-line-L5.txt, sha1 39e44fe2b8b4cced9133270de0896e7652cc859c; fixes docs/si/P-N5-SETTLE-fixes.md entries 1-5, file sha1 0c593d03b3a06c6970236d367cdfdc3e727db79d). Chain after the L-2 this draft was built on: L-3 a79d33db (ae695c9e; D-1 «|F| its number of transitions», D-2 H_t gloss) → L-4 b04a1bbb (6ed61d84; RUN-SETTLE proof note cites Lemma ONE-STEP for Cases 2, 2b) → L-5 ce7bdc3b (SETTLE-L6 «for S4a at a transition t → t + 1, σ_(t+1)», G-SRC-1 naming, SETTLE-L7 «Lemma ONE-STEP (Cases 2, 2b) is referee-originated», «entries 1-5»). G-SRC-1: a proof-text gap in packet §5 Case 2 / Case 2b (joint miss of both SETTLE referees), found by REFEREE-2 24 (R2-N5-SRC.md §3, claude/referee-2 e8c1b62d) and independently by REFEREE 20 (R-N5-SRC.md §3, claude/referee 81f6b89c); closed by Lemma ONE-STEP (REFEREE-2, §3.2 e8c1b62d), SIGNED by REFEREE 20 (R-N5-SETTLE.md Addendum 1, claude/referee 8951ef7c), with Case 2 = ONE-STEP(t = k − 1, z = b), Case 2b = ONE-STEP(t = k, z = a) confirmed; REFEREE's four-sub-case argument SIGNED by REFEREE-2 (R2-N5-SRC-C.md, 824651dd) (Lead reading L41: referee-originated, both signatures). Word-diff verdicts on L-5: REFEREE 21 R-N5-SETTLE-C.md §8 (claude/referee 5f2fbba5) «MATCHES»; REFEREE-2 24 docs/referee-2/R2-N5-SETTLE-L5.md (claude/referee-2 0f864f7a) «MATCHES»; intermediate: L-3 REFEREE 21 §6 (957c3e90, preliminary), L-4 REFEREE 21 §7 (8a1ba423, REQUIRED L6/L7), REFEREE-2 R2-N5-SETTLE-L4.md (b441f3da, REQUIRED SET-L4-1). No claim of the five changes (RG′, RUN-SETTLE, RUN-COUNT, HEAD-RED, T-XCH): the statements are unchanged; only bindings, the proof note and the scope tail changed. Draft edits by Lead script (scratchpad r96/build96b.py = the drafter's build96.py with L-5's hash, its two extra '|' and the new tail; its checks pass: labels removed and replacements undone equal the title body): l. 276 title = «### R96 [refereed-only] » + L-5 + fill (checked equal); l. 476 GAPS UPDATE rebuilt from L-5 (0 '|'; the head's definition clause «and |F| its number of transitions» is DROPPED from the UPDATE (r3, as in the R97 draft), since every «|F|» there is already replaced by «the number of transitions of F»). Lines 1-275 and 277-475 unchanged (they describe the L-2 object as history). Placement: after R95 (landed 22:14Z 2026-10-30).