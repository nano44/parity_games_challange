# Draft RESULTS R90 (Lead, 2026-10-30 02:48Z by date -u; subagent draft; packet, both reports, both §Cs and the fixes file K0-K12 filled; NO referee K12 line on origin yet; Lead revision 2026-10-30 04:31Z by date -u (subagent): title K12 → K15 per the Lead decision of 04:16Z (K16 superseded), both referees' K12 / K13 / K15 lines, fixes K0-K16, §C pins re-measured at the origin heads fetched 04:31Z) — to CHECKER C100
to check: (1) TITLE. The title is K15's line, docs/si/P-N5-CUT-fixes-box43.md l. 155-165 (under "## K15", l. 153) at l-si
4e6cc43d917ec167a5081be404586bacff15c9fa (2026-10-30T03:46:52Z; fixes sha1 b24e45102f18437e4d35562363ce400d99f6047c, 169 lines, = trunk
5754f213; `git diff --numstat 902b5b4f 4e6cc43d`: 54 added, 0 removed), verbatim: the file wraps it over 11 lines; it is joined here at each
line break with one space, the outer «…» are stripped, and it has no final period. The K15 text is unchanged at l-si db7c9e43 and bba03405
(append-only: +20/−0, +2/−0). Lead decision, docs/agents/LEAD-STATE.md (entry stamped 04:17Z; trunk commit 5754f213, 04:16:40Z, «Lead: K15
decided as R90 title (K16 superseded)»): «Lead decision: K15 is R90's title; K16 superseded (reopens free V) — L-SI to record one line.»
K15's text inside the quotes is 1,607 characters (1,645 bytes) and contains no "|" (K12-K14's «n = |V|» is gone). K15 carries NO date,
so " (2026-10-30)" is inserted immediately before " — a REDUCTION" (one occurrence; as R89's line has its date; the freeze 2678f6c6 and K15
4e6cc43d are both 2026-10-30); this is the only change to the K15 text. The checker fill ", CHECKER PASS (docs/checker/C100.md, checker
PENDING)" is appended as in R89. Checked by script (04:3xZ): the heading line equals "### R90 [refereed-only] " + that construction, byte
for byte. Word diffs re-measured (`git diff --no-index --word-diff`, both lines joined the same way; [-removed-] {+added+}): K13 (l.
101-111, 902b5b4f) → K15: exactly three edits, «n [-= |V|,-] {+the number of vertices of the game,+}», «re-entries {+j − 1 → j+} of Even
edges in R» (K14's edit, l. 131) and «(W [-read against τ_{j−1},-] {+:= the [S1-val] valuation of the (σ, τ_{j−1})-plays, σ the Even
strategy at the state compared;+} smallest anchor)» (the first and third are K15's, l. 166-168); nothing else. K12 (l. 82-92, fd1cb0bc) →
K15: those three plus K13's two, «per [-W-run,-] {+W-run F,+} R*_T» and «R*_T {+(one symbol)+} as in [-R88),-] {+R88, read on F),+}», five
in all; nothing else. K0 (l. 9-19) → K12 (first draft, unchanged): exactly K0-P1, K0-P2, K0-P3 (fixes l. 93-96).
(2) K15 CONFIRMED BY BOTH REFEREES. Fetch 04:31Z (date -u): origin/claude/referee fe9d0cf1 (04:06:52Z), origin/claude/referee-2 85e6d86e
(04:06:58Z), origin/claude/l-si bba03405 (04:16:51Z), trunk origin/claude/vibrant-johnson-nxvvxo 5754f213 (04:16:40Z). Each referee's line
on each step, with the commit that added it. REFEREE successor 19, docs/referee/R-N5-CUT-C.md: K12, l. 94, 40fd25a3 (02:42:04Z): «K12 = K0 +
P1-P3 exactly; MATCHES (Opus 5.5, D15).»; K13, l. 95, a455907e (03:24:13Z): «K13 = K12 + the two edits exactly («W-run F,», «R*_T (one
symbol) as in R88, read on F),»); every symbol bound (F by «per W-run F»; my K12 check had missed the unbound F, the Lead's catch); MATCHES
(Opus 5.5, D15).»; K15, l. 96, fe9d0cf1 (04:06:52Z; its own word diff K13 → K15): «exactly three edits» (the three above); «The W wording is
equivalent to my suggested σ_t form (it is §4's W^{τ_{j−1}}_t), and it is correct. Strict symbol test over the whole K15 line: every symbol
is bound in the line (T, n, m_E, K, B*, REP*, SC*, O*, R, j, W, σ, F, REP_F, R*_T, REPEAT) or by a named source (SPEC S1-S5: τ, S4c,
[S1-val]; R86: λ-, λ^U-runs; R88 / R89: W-run, late adoption, R*_T; P-N5-CUT §4: class S / C, anchor). No free symbol. MATCHES (Opus 5.5,
D15).» REFEREE-2 successor 21, docs/referee-2/R2-N5-CUT-C.md: K12, l. 104, b93dc4a7 (02:43:02Z; branch head 0140da67): «K12 = K0 + P1-P3
exactly (…); MATCHES.»; correction, l. 105, 1f5a9fbe (03:03:41Z; head 8a0f0ed6): «my K12 line above checked only K12 = K0 + P1-P3; it MISSED
that «F» is unbound in the "via" parenthetical (…), found by the Lead's symbol test. K12 is therefore NOT landable as written»; K13 with its
strict test, l. 106, 0aae9be6 (03:24:28Z; head 2bdda73d): «F is now bound. Full symbol test of the whole K13 line: … ONE DEFECT left, the
same kind as F: «τ_{j−1}» in the SC* clause uses j, never introduced in the line. Fix: «of re-entries j − 1 → j of Even edges in R …» (…).
With that edit: MATCHES.»; K15, l. 107, 895d7709 (04:06:57Z; head 85e6d86e): «K15 = K13 + exactly «n the number of vertices of the game»
(for «n = |V|»), «j − 1 → j» after «re-entries», and «(W := the [S1-val] valuation of the (σ, τ_{j−1})-plays, σ the Even strategy at the
state compared; smallest anchor)» (…) (difflib vs K13, nothing else). Strict symbol test of the whole K15 line: T, n, m_E, K, B*, REP*, SC*
(R, j, W, σ bound inside), O*, F, REP_F, R*_T bound; τ from SPEC; «anchor» via the cited §4. No unbound symbol. MATCHES.» REFEREE-2 is
PARKED: handover notes/REFEREE-2.md (895d7709, head 85e6d86e; «PARKED»): «IN FLIGHT / open … None. CHECKER (C100 / C101) may ask REFEREE-2
questions on R90 / R91: a successor answers from the reports above.» Strict symbol tests, history: K12's unbound F was found by the Lead
(LEAD-STATE 03:05Z) and missed by both referees' K12 lines (REFEREE l. 95 and REFEREE-2 l. 105 say so); K13's unbound j was found by
REFEREE-2 (l. 106); LEAD-STATE 04:00Z also records «REFEREE 19 on K13 found W unbound too (with j)», but REFEREE's own K13 line (l. 95) says
«every symbol bound»: that finding is on file only through LEAD-STATE, the K16 heading («REFEREE 19's single replacement (binds j and W;
Lead 03:55Z)») and the K15 line's «my suggested σ_t form»; K14's unbound V and W were found by L-SI's own strict test (fixes l. 133-151:
«two unbound symbols remain in K14 (V, W)»). On V the referees reason differently: REFEREE treats it as free (its H17 check,
docs/referee/R-N5-GAP-C.md l. 107, same commit fe9d0cf1: «SPEC's input line defines V = {0..n−1}, but that is not S1-S5; L-SI's K15 replaced
the same «n = |V|» for this reason»); REFEREE-2's K13 line lists V among the bound symbols and its handover says «TARGET.md l. 8 binds n =
|V| fleet-wide». K15 contains no V, so it passes both tests. K16 SUPERSEDED: l-si db7c9e43 (03:57:55Z) appended «## K16. K13 with REFEREE
19's single replacement (binds j and W; Lead 03:55Z) — the line to land» (fixes l. 171-189; sha1 267eb196da78f58641335da45664e36da1039440,
189 lines), saying «K14 and K15 are superseded. Per both referees, V comes from the SPEC, so K15's V edit is not needed.» Word diff K15 →
K16: «n [-the number of vertices of the game,-] {+= |V|,+}» and «valuation of the [-(σ,-] {+(σ_t,+} τ_{j−1})-plays, [-σ the Even strategy at
the state compared;-] smallest anchor)»; nothing else. Lead decision 04:16Z: K15 lands; K16 is superseded because it restores «n = |V|»,
whose V REFEREE's strict test at fe9d0cf1 flags as free (in the H17 line above; no referee line checks K16 itself: neither §C file mentions
K16). L-SI recorded it at bba03405 (04:16:51Z), fixes l. 191 (sha1 e30153d3a3cf8b068f4f8a0bc6dea335451cf29b, 191 lines; `git diff --numstat
4e6cc43d bba03405`: 22 added, 0 removed): «Lead decision 04:16Z: K15 is the line to land; K16 is superseded (it restores the free V, REFEREE
fe9d0cf1).» bba03405 is not yet on trunk 5754f213 (whose fixes file is the 4e6cc43d version).
(3) CLAIMS SIGNED = the twelve items (a)-(l) below, each SIGNED in BOTH verdict tables (REFEREE "## Verdicts" l. 19-38; REFEREE-2 "## 0.
Verdicts" l. 24-41), both §C tables "SIGNED by both" (REFEREE §C l. 10-22; REFEREE-2 §C C.1 l. 9-27), and K1 SIGNED in both §Cs (REFEREE §C
§3 l. 68-71; REFEREE-2 §C C.4 l. 73-79). Checked cell by cell for the first draft; the K13 / K15 lines appended since change no verdict cell
(each §C commit after 1a4e7571 / 443cf523 is +1 or +2 lines, 0 removed). No item is signed by one referee only. One-referee notes and
readings, and the CONJECTURE REP-WPAID, are under Referee strengthening only. (4) PREMISE LABELS (stale-label test, C96 lesson; re-run
04:3xZ). docs/RESULTS.md is unchanged since 4d85668e (R89 landed 2026-10-29 23:27Z): sha1 4d8d7fdfb1b6207de88e9c0895cfbad6e7ed5187, 6,636
lines, identical at 357930cc, at trunk 5754f213 and at the working head 54b8526f; the last entry heading is R89 (l. 5854), so no later entry
changes a cited label, and every line number below was re-printed and still holds. K15 cites the same labels as K12 (R15 (d), R17 (a), R47
(a), R57, R86, R88, R89). Each label used by the line or by the fixes, grepped in docs/RESULTS.md (at 357930cc, re-checked at 5754f213):
| label | where in RESULTS | says | verdict |
| --- | --- | --- | --- |
| R15 (d) | l. 640-643 | every iteration applies Switch_I (∅ ≠ I ⊆ Iσ) to σ and/or (∅ ≠ I ⊆ Iτ) to τ and changes at least one of them | ✓ = packet [R15d] |
| R17 (a) | l. 738-741 | (F1)/(F2): the optimum of a one-player game dominates every strategy of that game pointwise | ✓ = K2's use (OPT-OFF (i)); in R17's "Claims signed (both referees)"; R17's gaps all closed or DATA (l. 770-774) |
| R47 (a) | l. 2336-2341 | Lemma Φ (every game); the count "at most n(n − 1) transitions change λ and at most n(n − 1) change λ^U" is its sub-item (c) | ✓ = packet [R47a]; the line's "R47 (a)" names the item, not the sub-item |
| R57 (standing SPEC premise) | headline l. 2893; (b) l. 2913-2916 | "under the standing SPEC premise 1E-N3"; «that S1's procedure realises an optimal σ̄ is VJ00 §6 plus SPEC conformance … (1E-N3 = N-1E-1)» | ✓ = the line's «(S1's procedure realises the optimal counterstrategy)» |
| R57 (a) (VJ) (K2 only) | l. 2907-2909 | «Premise (VJ), on every game: … Ξσ(v) ⊴ V_{σ,τ′}(v) at every v» | ✓ in substance; K2's gloss «VJ: S1's Ξ is VJ00's Ω» is REFEREE's CUT-N1 paraphrase, not R57 (a)'s words (not in the title) |
| R51 (d) (K2 only) | l. 2591-2596 | Lemma OUT on 𝒞^1O; it does not itself name "1E-N3" or a standing premise (R57 (b) says «Standing premise, as in R51 (d)»; R51's limits l. 2606: code = SPEC is DATA) | minor: K2's "R57 / R51 (d) (1E-N3 …)" follows R57 (b)'s wording; not in the title |
| R84 (a) Fact DELTA (packet §1, K4) | l. 4967 | Fact DELTA (weights decided by the top differing rank) | ✓ |
| R86 (λ-run, λ^U-run; ENT_R, SW_R; m_E; COMPOSE-RUN) | headline l. 5269; l. 5276, 5291 | λ-run (λ^U-run) a maximal run of states with λ (λ^U) constant; ENT_R(v, c), SW_R(v); m_E | ✓ = packet [R86] and §8's bookkeeping |
| R88 (late adoption, BLOCKED, R*_T) | (f) l. 5738-5740 | «A LATE ADOPTION in F …», R*_T := the transitions of F containing at least one late adoption, F a FROZEN W-phase | ✓; on a W-run it is R88's definition read on F per RESULTS R89 (h) GP*-RUN (H6), as [GPR] says; K15 states that reading in the line («R*_T (one symbol) as in R88, read on F», K13) |
| R89 (W-run; DUAL-ORDER; GP*-RUN; STRETCH-RED's λ_W item) | headline l. 5854; (b) l. 5924; (h) l. 5959; (j) l. 5978-5986 (λ_W item l. 5983) | W-run := a maximal run of consecutive states of one τ-stretch none of whose transitions is an S4c fallback or changes λ_W; "blocked edges and late adoptions as in RESULTS R88" | ✓ = packet [DO], [GPR], [SR-λ]; K3: read "RESULTS R89 (landed, 4d85668e)" for "R89 draft" |
No mismatch that changes a claim. Three minor points recorded: R47 (a) vs its sub-item (c); K2's R57 (a) gloss; K2's R51 (d). (5) SYMBOL
TEST, re-run on K15 (04:3xZ). Every symbol of the title line and where it is bound (IN = in the line; CITE = a RESULTS entry the line names;
PKT = the cited packet section P-N5-CUT §n, docs/si/P-N5-CUT-box43.md at 2678f6c6; STD = SPEC, TARGET.md or GAPS):
| symbol | status (K15) |
| --- | --- |
| N5, SPEC S1-S5, Even S4c fallback, [S1-val] | STD (SPEC docs/new/N5-ssi-global.md; [S1-val] and [S4c] quoted in packet §1 l. 29-49) |
| standing SPEC premise | CITE R57 (headline, (b)), and stated IN the line |
| R15 (d), R17 (a), R47 (a) | CITE (table above) |
| T | IN («the number of transitions (iterations) of the run») |
| n | IN («n the number of vertices of the game», K15); the same n as TARGET.md §1 l. 8 («n = \|V\|») |
| V | not in K15 (K12-K14's «n = \|V\|» is replaced by K15) |
| m_E | IN |
| K | IN (= §8's K(n, m_E, REP*)) |
| B*, REP*, SC*, O* | IN (each "the largest number of …") |
| λ, λ-run, λ^U, λ^U-run | CITE R86 |
| W-run | CITE R89 |
| late adoption | CITE R88 (f) / R89 |
| REPEAT | IN («a second or later late adoption of the same Even edge») |
| τ, τ-changing transition, τ_{j−1} | STD (SPEC: Odd's strategy; τ_{j−1} is τ at state j − 1, j IN) |
| R (inside SC*) | IN («over λ-runs R») |
| j | IN («re-entries j − 1 → j», K14) |
| W (in «W-silent» and «W := …») | IN («W := the [S1-val] valuation of the (σ, τ_{j−1})-plays», K15; [S1-val] STD); = PKT §1 l. 72-83 W^τ_t with τ = τ_{j−1} |
| σ | IN («σ the Even strategy at the state compared», K15); the state is not named in the line: it is the state at which the cited §4 compares W (REFEREE l. 96: «it is §4's W^{τ_{j−1}}_t») |
| re-entry, class S (W-silent), class C (own-cycle), anchor, smallest anchor | PKT §4 l. 125-131 (classes, smallest anchor, frame), §3 l. 116-118 (anchor), §1 l. 72-83 (leave / re-entry, span); named IN the line; K8 (frame τ_{j−1}, incl. W*_j) |
| Theorem CUT-RED; Lemmas OPT-OFF, W-RETURN-G, LATE-SPLIT, WV-R; Corollary CUT-CHARGE; Corollary CUT-POLY | PKT §8, §2, §3, §6, §7, §4, §8 (named, not restated) |
| F | IN («per W-run F», K13) |
| "first late adoptions" | IN («≤ m_E per W-run F»; = §6 (i) FIRST) |
| REP_F | IN («REP_F the REPEATs in F») |
| R*_T | CITE R88 («R*_T (one symbol) as in R88, read on F», K13), read on a W-run per R89 (h); «(one symbol)» settles the first draft's note on the subscript T |
| "polynomial" | PKT §8 CUT-POLY (bounded by a polynomial in n on every run of every game; REFEREE-2 §C C.3 l. 69-70, optional precision); K7: m_E ≤ n² |
| converse, fixes K1 | fixes K1 (l. 23-26), signed by both |
| REDUCTION; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME | STD (TARGET.md, GAPS) |
| CONJECTURE REP-LIN, L-RED R128, latew_K20_m32 | docs/red/R128-rep-lin.md (l-red 0e91e875, addendum e55592d9); experiments/red/span/instances/latew_K20_m32.pg sha1 063d173c… (= trunk); REP-LIN := REP ≤ n per W-run (R128 l. 1; packet §8 l. 201) |
Result: no free symbol in K15; the same symbols as both referees' K15 strict tests (REFEREE l. 96, REFEREE-2 l. 107). The first draft's two
notes for CHECKER are settled in the line: «F» unbound (K13: «per W-run F») and the subscript clash T / R*_T (K13: «(one symbol)»); j (K14),
W and V (K15) likewise. One wording point, not a free symbol: «the state compared» (the σ clause) is fixed only by the cited §4. (6) FIXES.
K0-K16 are each listed below with a class and the referees' words; K1 is a NEW STATEMENT signed by both, not a clarification (REFEREE §C l.
86: «K1 is the only new signed statement; K0 the only line»); the class list clarification / reading / correction does not fit it, so it is
labelled "addition (signed)" (LEAD-STATE 03:05Z: «Lead ruling: K1 class 'ADDITION (signed by both)'.»). K12-K15 are successive CORRECTIONS
of the RESULTS line (precisions; F; j; V, W); K16 is SUPERSEDED. (7) REP-LIN: DEAD (L-RED R128); the packet does not depend on it (REFEREE
l. 37-38; REFEREE-2 §C l. 30). REP-LIN is not in RESULTS "## Dead ends" (grep: 0 hits in docs/RESULTS.md, re-run at 5754f213); it is
recorded in docs/red/R128-rep-lin.md and NOW only. (8) EXCLUDED: no lane work after the freeze 2678f6c6 is in the entry except the fixes
file (cc84e54c, fd1cb0bc, 902b5b4f, 4e6cc43d; K16 db7c9e43 and the note bba03405 only as superseded history): L-SI boxes 44-49 (incl.
P-N5-REPD, box 49, frozen, not refereed, a84e7eb5), L-RED R129-R130 and L-NEW boxes 70-71 are out. The only post-freeze sources cited are
K6's second citation docs/si/N5-SUB-box46.md (inside the fixes file; REFEREE-2 §C C.5: «not opened by me; R128 suffices») and R128's
addendum e55592d9 (00:58:24Z, 11 min after the freeze; it adds the K 24 point only). (9) PINS: re-run for the first draft (below, Data): all
pass. NOT re-run for this revision; re-measured instead (04:3xZ): the packet sha1 d6519d3d… at 2678f6c6, trunk 5754f213 and l-si bba03405
(same blob); the five pinned scripts have the same blob at 2678f6c6 and 5754f213; check.sh at 5754f213 adds 22 lines after l. 813 (`git diff
--numstat 2678f6c6 5754f213`: 22 added, 0 removed; 15 at 357930cc) and its l. 796-813 are byte-identical to 2678f6c6. (10) Small
discrepancies, recorded: REFEREE §C l. 2 says «written 02:03Z-02:08Z», its commit 1a4e7571 is 02:03:59Z; REFEREE pins «l. 796-813»,
REFEREE-2 «l. 797-813» (l. 796 is the block's comment line); REFEREE counts the quotes 13/13 «by fragments», REFEREE-2 10/13 strict + 3
faithful elisions, the lane's quotecheck.py 13 / bad 0; the Lead decision is «04:16Z» in L-SI's note and the brief, its LEAD-STATE entry is
stamped 04:17Z; REFEREE-2's K12-K15 lines carry no «(Opus 5.5, D15)» tag of their own (its handover: «Reports of record (all "(Opus 5.5,
D15)"; …»).

### R90 [refereed-only] N5 (SPEC S1-S5) on EVERY game, under the standing SPEC premise of RESULTS R57 (S1's procedure realises the optimal counterstrategy), with RESULTS R15 (d), R17 (a) and R47 (a): T ≤ 2n(n−1) + (n(n−1)+1)·(m_E·[1 + 2B* + (B*+1)·K] + SC* + O*), K := n(n−1) + (n(n−1)+1)(n−1)(m_E + REP* + 1), where T is the number of transitions (iterations) of the run, n the number of vertices of the game, m_E the number of edges leaving Even vertices, λ-runs and λ^U-runs are as in RESULTS R86, W-runs as in RESULTS R89 and late adoptions as in RESULTS R88 / R89; B* := the largest number of transitions inside one λ-run that are Even S4c fallbacks or change τ; REP* := the largest number of REPEAT late adoptions (a second or later late adoption of the same Even edge) inside one W-run; SC* := the largest number, over λ-runs R, of re-entries j − 1 → j of Even edges in R of class S (W-silent) or C (own-cycle) of P-N5-CUT §4 (W := the [S1-val] valuation of the (σ, τ_{j−1})-plays, σ the Even strategy at the state compared; smallest anchor); O* := the largest number of τ-changing transitions inside one λ^U-run (Theorem CUT-RED, via Lemmas OPT-OFF, W-RETURN-G, LATE-SPLIT (first late adoptions ≤ m_E per W-run F, R*_T ≤ m_E + REP_F; REP_F the REPEATs in F, R*_T (one symbol) as in R88, read on F), WV-R and Corollary CUT-CHARGE); so T is polynomial if and only if B*, REP*, SC* and O* are (Corollary CUT-POLY and its converse, fixes K1) (2026-10-30) — a REDUCTION (none of B*, REP*, SC*, O* is bounded here; CONJECTURE REP-LIN is DEAD (L-RED R128, latew_K20_m32); not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C100.md, checker PENDING)
- Object (L-SI successor 31, Opus 5.5, D15/D18, Lead reading L40; frozen, unchanged during review): packet P-N5-CUT,
  docs/si/P-N5-CUT-box43.md, sha1 d6519d3d72d67d25bafd21b7034092eaa4315457, 221 lines (l-si freeze 2678f6c6a343909bf51a2611e17cef8d4e6a288c,
  2026-10-30T00:47:30Z; the file is identical at l-si fd1cb0bc and trunk 357930cc (first draft) and at l-si head bba03405 and trunk 5754f213
  (re-measured 04:3xZ); both referees measured the sha1 at 2678f6c6:
  REFEREE l. 3-4, REFEREE-2 l. 6-7). Lead brief quoted at l. 3-6 («Freeze packet P-N5-CUT for the two referees … written as a REDUCTION in
  the style of R89's STRETCH-RED: every symbol defined, every hypothesis carried»). Quote base: SPEC docs/new/N5-ssi-global.md@7039eb524,
  P-N5-FRAME@938d87967, experiments/new/box64/late.py@9905dac36; 13 quotes, checked by experiments/si/rund/quotecheck.py (pinned «box 43»,
  with a shifted control that must fail), by REFEREE's own script (l. 13: «13/13 verbatim») and by REFEREE-2's qcheck.py (l. 27, l. 44-50: 10
  strict, 3 «faithful» "…" elisions; SHIFT=1 0/13). Sections: §0 what to sign (l. 13-23), §1 setting, symbols, premises (l. 25-83), §2 OPT-OFF,
  W-MON′, W-SUCC, §3 W-RETURN-G, §4 CUT-CHARGE, §5 FRESH-SPLIT, §6 LATE-SPLIT and R*-REP, §7 WV-R, §8 CUT-RED and CUT-POLY, §9 READING and DATA
  («NOT to sign», l. 23, l. 204-215). Working notes docs/si/N5-CUT-box40.md, N5-WVP-box41.md, N5-LATE-box42.md (l. 6-7): not refereed here.
  The RESULTS line, history. (1) The lane's 00:56Z proposal, Lead copy docs/agents/P-N5-CUT-line-proposal.md at trunk 09d6f0c4 (sha1
  10e91e67c36341f3c300086916933f1c62af496f). (2) Rejected by both, independently, for the same two E-items: SC* undefined (REFEREE CUT-E1,
  §10b l. 190-197; REFEREE-2 §8 l. 271-284, «UNDERDEFINED; REQUIRED fix», «a definitional defect, not a demonstrated falsity») and "iff"
  beyond CUT-POLY (REFEREE CUT-E2, l. 198-201; REFEREE-2 §8 l. 285-290, «As the line stands, it claims more than the packet»), both supplying
  the same converse; plus missing T, m_E, re-entry, W (REFEREE l. 207) and the R86 / R88 / R89 citations (REFEREE-2 l. 302-303,
  «REQUIRED»). REFEREE: «NOT YET» (l. 206); REFEREE-2: «Three things are REQUIRED before landing» (l. 302). (3) K0 (fixes l. 7-21, cc84e54c,
  2026-10-30T01:48:21Z, sha1 ff9946215da949f49057fc939292b3e668e646cb, 78 lines): «K0 MATCHES Theorem CUT-RED, Corollary CUT-POLY and K1,
  and claims nothing more. CUT-E1 and CUT-E2 are discharged» (REFEREE §C l. 65-66); «K0 MATCHES. My REQUIRED items (SC*, citations, "iff")
  and REFEREE's (CUT-E1, CUT-E2, T, m_E, re-entry, W) are all met.» (REFEREE-2 §C C.3 l. 71, bold in the source). (4) K12 (fixes l. 80-97,
  appended at fd1cb0bc7e985f9ec885fcdf07a327e07f641364, 2026-10-30T02:25:26Z; `git diff --numstat cc84e54c fd1cb0bc`: 19 added, 0 removed;
  sha1 95584f7e3e7c928e1aadf1ea684ebb9d764e3927, 97 lines): «K0 with REFEREE 19's three optional precisions (R-N5-CUT-C.md §2: K0-P1,
  K0-P2, K0-P3) and nothing else (Lead 02:21Z)»; «K12 supersedes it as the line to land.» (l. 97). Word diff re-measured (to check (1)).
  Referee K12 lines: REFEREE 40fd25a3 and REFEREE-2 b93dc4a7, both «MATCHES»; REFEREE-2's correction 1f5a9fbe: it «MISSED that «F» is
  unbound» (to check (2)). (5) K13 (fixes l. 99-115, 902b5b4f0b3733e6c56e1c24c99685a93d83a958, 2026-10-30T03:03:59Z; +18/−0 over fd1cb0bc;
  sha1 51764d300e9f81029835f106426902b1e13927ca, 115 lines): «K12 with the Lead's two edits (03:03Z: F unbound in the "via" parenthetical;
  R*_T is one symbol) and nothing else»; REFEREE a455907e «MATCHES»; REFEREE-2 0aae9be6: F bound, «ONE DEFECT left»: j unbound. (6) K14
  (fixes l. 117-131, 4e6cc43d917ec167a5081be404586bacff15c9fa, 2026-10-30T03:46:52Z): «K13 with REFEREE-2's one edit (claude/referee-2
  2bdda73d: j unbound in the SC* clause) and nothing else (Lead 03:45Z)»; L-SI's strict symbol test of K14 (l. 133-151): «two unbound
  symbols remain in K14 (V, W)». No referee line checks K14 alone (both word-diffed K13 → K15). (7) K15 (fixes l. 153-169, same commit
  4e6cc43d; +54/−0 over 902b5b4f; sha1 b24e45102f18437e4d35562363ce400d99f6047c, 169 lines): «K14 with the two edits of the symbol test
  above (proposed by L-SI; for both referees' word-diff)»; «If both referees accept, K15 supersedes K14 as the line to land» (l. 169);
  REFEREE fe9d0cf1 «No free symbol. MATCHES (Opus 5.5, D15).»; REFEREE-2 895d7709 «No unbound symbol. MATCHES.»; Lead decision 04:16Z: K15
  is R90's title. (8) K16 (fixes l. 171-189, db7c9e438a1bccfbc574f2e9596bc3307b2770df, 2026-10-30T03:57:55Z; +20/−0 over 4e6cc43d; sha1
  267eb196da78f58641335da45664e36da1039440, 189 lines): SUPERSEDED by the Lead decision of 04:16Z (it restores «n = |V|», V free per
  REFEREE fe9d0cf1); L-SI's note bba03405, l. 191 (to check (2)). The title is K15's line verbatim with the date inserted; the 00:56Z
  text, K0, K12, K13, K14 and K16 are superseded and are not this entry's title.
  Setting (every game): N5 = SPEC S1-S5 with FIX 1-4; G = (V, E, Ω, owner), n = |V|, m_E (m_O) the edges leaving Even (Odd) vertices; a run
  is the sequence of states (σ_t, τ_t), a TRANSITION is t → t + 1, T the transitions of the run (l. 26-28). [S1-val], [S1-ord], [S1-Xi],
  [S1-dual], [S2], [S4a], [S4b], [S4c] quoted (l. 29-49). Packet symbols (l. 71-83): W^τ_t := the [S1-val] valuation of the (σ_t, τ)-plays
  (G_τ: Odd fixed to τ), W_t := W^{τ_t}_t, λ_W its cycle-node map, CN^τ_t(v) its cycle node, v OFF-CYCLE if CN^τ_t(v) ≠ v; H_t := σ_t ∪ Iσ_t;
  an S4a STEP: a transition with Iσ_t ≠ ∅, not an S4c fallback, σ_{t+1} = [S4a]'s σ_new ≠ σ_t (τ_{t+1} may differ); BOUNDARY: an Even S4c
  fallback or a τ-changing transition; Fact B: every transition is an S4a step with τ kept, or a boundary; τ*-PIECE (guided stretch): a
  maximal run of states with τ_t = τ* and every inside transition an S4a step; for a λ-run R and an Even edge (v, c): LEAVE, next RE-ENTRY,
  OUT-WINDOW, span(v, c); B_R := the boundaries inside R. §1 cells: REFEREE «CHECKED (Fact B re-derived from S4a-S4d and R15 (d), §1
  below)» (l. 22); REFEREE-2 «well formed; 13 quotes: 10 strictly verbatim, 3 faithful "…" elisions (§1)» (l. 27); §Cs: "agree"
  (REFEREE-2 §C C.1 l. 12).
- Claims signed (both referees "(Opus 5.5, D15)": REFEREE successor 19, REFEREE-2 successor 21). Each item (a)-(k) is SIGNED in both
  verdict tables (REFEREE "## Verdicts" l. 19-38 of R-N5-CUT.md; REFEREE-2 "## 0. Verdicts" l. 24-41 of R2-N5-CUT.md; REFEREE §C table
  l. 10-22 and REFEREE-2 §C C.1 l. 9-27: "SIGNED by both"); (l) is SIGNED in both §Cs. In the frozen wording, read with the fixes named.
  Every game; plain N5. Premises LANDED: SPEC S1 ([S1-val], [S1-ord], [S1-Xi], [S1-dual]), S2, S4a, S4b, S4c (quote base 7039eb524);
  RESULTS R15 (d) ([R15d]); RESULTS R17 (a) (F1) with RESULTS R57 (a) (VJ), for OPT-OFF (i) (K2); RESULTS R47 (a) Lemma Φ ([R47a]); RESULTS
  R84 (a) Fact DELTA (K4); RESULTS R86 (λ-run, λ^U-run, ENT_R, SW_R; Corollary COMPOSE-RUN's bookkeeping); RESULTS R88 (f) (late adoption,
  BLOCKED, R*_T); RESULTS R89 (b) DUAL-ORDER ([DO]), the W-run definition and (h) GP*-RUN ([GPR]), and (j) STRETCH-RED's λ_W item ([SR-λ])
  (K3: «read "RESULTS R89 (landed, RESULTS 4d85668e)" for "R89 draft"»). Standing premise (disclosure, not a widening; K2, l. 28-32):
  «OPT-OFF (i) uses: S4a's σ_new is the pointwise optimum of the one-player arena A = G_{τ*}|H_t and its values are those of the
  (σ_new, τ*)-plays. That is RESULTS R17 (a) (F1) on A with R57 (a) (VJ …), under the standing SPEC premise of R57 / R51 (d) (1E-N3: S1's
  procedure realises the optimal counterstrategy). Every later item uses OPT-OFF (i), so the whole packet carries this premise, as R88's
  W-MON and R89's ODD-FREEZE do»; REFEREE CUT-N1 (l. 210-211), REFEREE-2 N-CUT-2 (l. 227-228) and §8 l. 291-299 («So YES: OPT-OFF (i), and
  through it every later item, uses that standing premise»). G-N5T-1 (code = SPEC) is used only by DATA (K2; REFEREE-2 §8 l. 299).
  REP* is a premise: «The packet does not depend on CONJECTURE REP-LIN (dead): REP* is a premise; no proof step of §2-§8 uses a bound on REP
  (checked line by line); REP-LIN appears only in the unsigned §8 notes.» (REFEREE l. 37-38); REFEREE-2 §C C.1 l. 30, same.
  (a) Lemma OPT-OFF (§2, l. 86-106), with K2 and K4: "At an S4a step t → t + 1, put τ* := τ_t, A := G_{τ*} restricted to H_t (Even keeps
      H_t's edges, Odd follows τ*), σ′ := σ_{t+1}. Then (i) σ′ is POINTWISE OPTIMAL for Even in A: W^{τ*}(σ′)(x) ⊵ W^{τ*}(σ″)(x) for every x
      and every Even strategy σ″ inside H_t; (ii) for every Even v that is off-cycle for τ* at t + 1 and every (v, y) ∈ H_t: W^{τ*}_{t+1}(y)
      ⊴ W^{τ*}_{t+1}(σ_{t+1} v)." ((i) [S4a] read on the dual with DUAL-ORDER; (ii) Cases 1-3 on where v lies on y's σ′-play; the off-cycle
      premise is necessary, red/so/instances/tog6b_n32.pg, DATA.) K4 (l. 39-44): the first bullet's «σ′v's play avoids v» is not literal for v
      on its cycle below c, «the identity W(v) = ext(v, W(σ′v)) still holds»; the ext step uses injective rewards and Fact DELTA; Case 3's «as
      in Case 1» is the triple identity. Cells: REFEREE «SIGNED; standing premise CUT-N1 (R17 (a) (F1) with R57 (a) (VJ))» ((i), l. 23),
      «SIGNED (Cases 1-3 re-derived, exhaustive; §2)» ((ii), l. 24); REFEREE-2 «SIGNED (case analysis of (ii) checked case by case, §2.1;
      standing premise as R89's FR-N1: N-CUT-2)» (l. 28).
  (b) Lemma W-MON′ (§2, l. 107-109): "At an S4a step t → t + 1 with τ* := τ_t: W^{τ*}_{t+1} ⊵ W^{τ*}_t pointwise." (σ_t ⊆ H_t; OPT-OFF (i).
      R88's W-MON is the case τ_{t+1} = τ_t.) Cells: REFEREE «SIGNED» (l. 25); REFEREE-2 «SIGNED» (l. 29).
  (c) Lemma W-SUCC (§2, l. 110-113): "Let [q, p] be states of one τ*-piece, v Even and off-cycle for τ* at every state of [q + 1, p]. Then
      W^{τ*}_t(σ_t v) is non-decreasing on [q, p]." Cells: REFEREE «SIGNED» (l. 26); REFEREE-2 «SIGNED» (l. 30).
  (d) Lemma W-RETURN-G (§3, l. 115-123), with K8: "Let R be a λ-run, (v, c) an Even edge, s → s + 1 a leave of c and j − 1 → j the next
      re-entry, and suppose j − 1 → j is an S4a step. Put τ* := τ_{j−1}, [a, b] the τ*-piece containing j − 1, W* := W^{τ*}. An ANCHOR is a
      state q with max(s, a) ≤ q − 1 ≤ j − 2 and (v, c) ∈ H_{q−1}. If an anchor q exists, v is off-cycle for τ* at every state of [q, j], and
      W*_t(c) is the same for all t ∈ [q, j], then W*_j(σ_{j−1} v) = W*_j(c)." K8 (l. 58-59): «every W* in §3-§5, including W*_j, is read
      against τ* = τ_{j−1}». Cells: REFEREE «SIGNED (every link's step and frame checked, §3)» (l. 27); REFEREE-2 «SIGNED» (l. 31).
  (e) Corollary CUT-CHARGE and its Remark (§4, l. 125-138), with K8 and K10: every re-entry j − 1 → j of v into c in R is exactly one of F
      (an Even S4c fallback), FR (an S4a step with no anchor), C (with q the smallest anchor, v its own τ*-cycle node at some state of [q, j]),
      P (otherwise, W*(c) changes on [q, j]), S (the rest, silent by §3); FC_R := #F + #FR, SIL_R := #S, CYC_R := #C, WCH*_R(v, c) := the
      transitions t → t + 1 inside span(v, c) with W^{τ_t}_{t+1}(c) ≠ W^{τ_t}_t(c). "ENT_R(v, c) ≤ 1 + FC_R(v, c) + WCH*_R(v, c) + SIL_R(v, c) +
      CYC_R(v, c), and FC_R(v, c) ≤ B_R." Remark: «#FR ≤ 1 per τ*-piece and pair». Cells: REFEREE «SIGNED (§4)» (l. 28, with the Remark);
      REFEREE-2 «SIGNED» (l. 32, «and its Remark»).
  (f) Lemma FRESH-SPLIT and its ENT bound (§5, l. 140-149; «not used by §8»), with K9: an FR re-entry is exactly one of (WC), (G0), (CY),
      (LATE), (SAME); "In case (LATE), (v, c) is BLOCKED at j − 2 for τ*"; ENT_R(v, c) ≤ 1 + BA + WCH*_R(v, c) + LATE + SIL + CYC + CY, BA +
      LATE + CY ≤ FC ≤ B_R. K9 (l. 61-63): «It is a late adoption in R89's W-run sense only if j − 2, j − 1, j lie in one W-run … §5 claims no
      more; §8 does not use §5.» Cells: REFEREE «SIGNED (not used by §8)» (l. 29); REFEREE-2 «SIGNED» (l. 33, «separately; not used by §8»).
  (g) Lemma LATE-SPLIT (i)-(iii) and its Consequence (§6, l. 151-165), with K5 and K10: in a W-run F, a late adoption of (y, z) is FIRST if
      it is the first in F, REPEAT otherwise, REP_F := the REPEATs in F. "(i) #FIRST in F ≤ m_E. (ii) Let u₁ < u₂ be consecutive late
      adoptions of (y, z) in F … Then y leaves z at a transition k → k + 1 with u₁ < k < u₂, and, if y is off-cycle (for F's τ) at every state
      of [k + 1, u₂ + 1], either W(z) changes on [k + 1, u₂ + 1] or the adoption is W-SILENT: W_{u₂+1}(σ_{u₂} y) = W_{u₂+1}(z). (iii) If
      moreover (y, z) is blocked at some state t with k < t ≤ u₂, then W_t(z) ▷ W_{k+1}(z)." Consequence: "#REPEAT_F(y, z) ≤ WCH_F(z) +
      SIL_F(y, z) + CYC_F(y, z)" (K10: these per-W-run classes are renamed SIL^REP_F / CYC^REP_F; «SIL_R / CYC_R (§4, the ones SC* sums) keep
      their names. §8 uses only §4's.»). K5 (l. 46-48): §0's §6 row reads «a REPEAT needs a W-rise of z, or is W-silent, or y is its own
      cycle node on the interval»; «The body (§6 (ii)) is the signed form». Cells: REFEREE «SIGNED» (l. 30); REFEREE-2 «SIGNED. The body has
      the CORRECT form (a REPEAT is W-paid, W-silent or own-cycle). §0's table summary omits own-cycle (N-CUT-4)» (l. 34).
  (h) Corollary R*-REP (§6, l. 166): "R*_T(F) ≤ #late adoptions in F ≤ m_E + REP_F." Cells: in the same rows as (g), REFEREE l. 30,
      REFEREE-2 l. 34: SIGNED.
  (i) Lemma WV-R (§7, l. 168-174): for a guided stretch Q, Λ_Q its λ_W-changing transitions, R*_Q (REP*_Q) the largest R*_T(F) (REP_F) over
      the W-runs F inside Q: "WCH_Q(w) ≤ Λ_Q + (Λ_Q + 1)·(n − 1)(R*_Q + 1) ≤ Λ_Q + (Λ_Q + 1)·(n − 1)(m_E + REP*_Q + 1), Λ_Q ≤ n(n − 1)." for
      every vertex w (GP*-RUN on each of ≤ Λ_Q + 1 W-runs; [SR-λ]; §6). Cells: REFEREE «SIGNED (W-runs inside Q = pieces of Q between
      λ_W-cuts, §7)» (l. 31); REFEREE-2 «SIGNED» (l. 35).
  (j) Theorem CUT-RED (§8, l. 176-194): with B* := max_R B_R (boundaries inside a λ-run), REP* := max_F REP_F over all W-runs F, SC* :=
      max_R Σ_{(v, c)} (SIL_R(v, c) + CYC_R(v, c)) over Even edges, O* := max_{R′} the τ-changing transitions inside a λ^U-run R′, and K(n,
      m_E, r) := n(n − 1) + (n(n − 1) + 1)(n − 1)(m_E + r + 1): "Every N5 run on every game has T ≤ 2n(n − 1) + (n(n − 1) + 1)·( m_E·[1 +
      B* + B* + (B* + 1)·K(n, m_E, REP*)] + SC* + O* )." (Bookkeeping as R86 COMPOSE-RUN with [R47a] and [R15d]; §4 per pair; WCH*_R ≤ B_R +
      (B_R + 1)K by Fact B and §7.) Cells: REFEREE «SIGNED (bookkeeping and each sum re-derived, §8)» (l. 32); REFEREE-2 «SIGNED» (l. 36).
  (k) Corollary CUT-POLY (§8, l. 195-196), as an implication, with K7: "If, for some polynomial p, every run on every game has [P-B] B* ≤ p(n),
      [P-REP] REP* ≤ p(n), [P-SC] SC* ≤ p(n) and [P-ODD] O* ≤ p(n), then T ≤ q(n) for a polynomial q (about n² · m_E · p · n³ m_E p):
      G-N5-TIME's iteration half." K7 (l. 54-56): «"T ≤ q(n)" uses m_E ≤ n² (E ⊆ V × V). The order "about n²·m_E·p·n³m_E p" is an upper
      estimate … Neither changes the statement.» Cells: REFEREE «SIGNED as an implication; its "about …" order is an upper estimate (CUT-N5)»
      (l. 33); REFEREE-2 «SIGNED as an implication. REP* is a PREMISE, not REP-LIN; R128's Θ(n²) does not touch [P-REP] (§8, N-CUT-5)» (l. 37).
  (l) K1, the converse of CUT-POLY (fixes l. 23-26): "For every run: B* ≤ T, O* ≤ T, REP* ≤ n·T, SC* ≤ n·T. So T ≤ q(n) implies all four
      ≤ n·q(n)." (B*, O* count transitions; a late adoption or a re-entry is one Even vertex switching at one transition.) Signatures:
      REFEREE §C §3 l. 69: «SIGNED (Opus 5.5, D15)» (and §10b l. 198: «The converse is TRUE and one line, which I sign»); REFEREE-2 §C C.4
      l. 73-79: «SIGNED (Opus 5.5, D15)» … «SIGNED as written in K1» (and §8 l. 289: «I sign it as stated here»). With (k) it backs the
      line's «if and only if».
  The RESULTS line (K15) states CUT-RED's inequality, the four counts and CUT-POLY with its converse; it names OPT-OFF, W-RETURN-G,
  LATE-SPLIT (with R*-REP's bound), WV-R and CUT-CHARGE as the route and omits W-MON′, W-SUCC and FRESH-SPLIT (it claims less; they are
  signed items (b), (c), (f) above).
- Not signed: §8 «Notes on the premises (what implies them; READING, not signed)» (l. 197-202), with K6 replacing the stale [P-REP] note;
  §9 READING and DATA (Data below); the working notes N5-CUT-box40, N5-WVP-box41, N5-LATE-box42; L-NEW's box 66 lemmas (LATE-W,
  LATE-PIECE, l-new 78e1fd24), «cited as lane input only and used nowhere» (l. 11); the superseded line texts (00:56Z proposal, K0,
  K12, K13, K14, K16). Lane work after the freeze, other than the fixes file, is not part of this entry (L-SI boxes 44-49 incl. P-N5-REPD,
  L-RED R129-R130, L-NEW boxes 70-71).
- Fixes (docs/si/P-N5-CUT-fixes-box43.md, L-SI successor 31; K0-K11 at cc84e54c, K12 appended at fd1cb0bc, K13 at 902b5b4f, K14 (with
  L-SI's strict symbol test) and K15 at 4e6cc43d, K16 at db7c9e43, the Lead-decision note at bba03405 (l. 191); header l. 5: «Every item below
  is a CLARIFICATION or a READING unless marked "to sign"; no signed statement of the packet changes.»; no quote check is pinned for the fixes
  file). Classes in the referees' words (REFEREE §C §4 table l. 74-86; REFEREE-2 §C C.5 l. 81-94):
  - K0: CORRECTION of the RESULTS line (REQUIRED items of both; «K0 MATCHES», both §Cs, see Object (3)); superseded by K12 (then K13, K14, K15).
  - K1: ADDITION, signed by both (the converse of CUT-POLY, item (l)); «K1 is the only new signed statement» (REFEREE §C l. 86).
  - K2: CLARIFICATION, the standing premise named (CUT-N1 = N-CUT-2): REFEREE «no (names a premise; answers CUT-N1 / N-CUT-2)»; REFEREE-2
    «clarification».
  - K3: CLARIFICATION (citation: R89 landed, 4d85668e; N-CUT-1): REFEREE «no»; REFEREE-2 «clarification (citation)».
  - K4: CLARIFICATION of OPT-OFF (ii)'s proof text (CUT-N2 = N-CUT-3): REFEREE «no (… matches both derivations)»; REFEREE-2 «clarification of
    the proof text; the statement is unchanged».
  - K5: CLARIFICATION of §0's §6 row (N-CUT-4): REFEREE «no (restores the signed body; N-CUT-4)»; REFEREE-2 «clarification (the summary is
    aligned with the signed body; no statement widened)».
  - K6: READING (the §8 [P-REP] note: «REP-LIN is DEAD (L-RED R128; also L-SI box 46 …). [P-REP] (REP* ≤ p(n), any polynomial) is OPEN and
    not implied by the packet.»; CUT-N3 = N-CUT-5): REFEREE «no (a READING; the added box-46 citation is DATA, not signed)»; REFEREE-2
    «clarification of a READING; cites docs/si/N5-SUB-box46.md as a second source (not opened by me; R128 suffices)».
  - K7: CLARIFICATION (m_E ≤ n²; the order estimate; CUT-N5, N-CUT-6): REFEREE «no»; REFEREE-2 «clarification».
  - K8: CLARIFICATION (the frame τ_{j−1}, also at j; N-CUT-7): REFEREE «no (the packet's definitions already say so)»; REFEREE-2
    «clarification».
  - K9: READING (FRESH-SPLIT's LATE vs a W-run late adoption; N-CUT-8): REFEREE «no: it claims less than nothing new ("only if" is a
    necessary condition, not asserted to hold)»; REFEREE-2 «READING that claims no more than §5 ("only if": a necessary condition, not
    signed)».
  - K10: CLARIFICATION (names; CUT-N4 = N-CUT-9): REFEREE «no (notation; §8 uses only §4's)»; REFEREE-2 «clarification (names)».
  - K11: CLARIFICATION (data notes; CUT-N6, CUT-N7, N-CUT-10) with a CONJECTURE (REP-WPAID, Referee strengthening): REFEREE «no: a labelled
    CONJECTURE, used by no signed item»; REFEREE-2 «clarification; the conjecture would be a WIDENING if ever claimed, and it is correctly
    labelled open».
  - K12: CORRECTION of the RESULTS line: K0 plus REFEREE's optional precisions K0-P1 (N5 (SPEC S1-S5)), K0-P2 (REP_F and R*_T defined in
    the "via" parenthetical), K0-P3 (R15 (d), R17 (a), R47 (a) named) «and nothing else» (l. 80, 97). REFEREE §C §2 called them «optional
    precisions, not blockers» (l. 66). REFEREE 40fd25a3 and REFEREE-2 b93dc4a7: «MATCHES»; REFEREE-2 1f5a9fbe: «it MISSED that «F» is
    unbound … K12 is therefore NOT landable as written». Superseded by K13.
  - K13: CORRECTION of the RESULTS line (F bound): K12 plus the Lead's two edits, «per W-run F» and «R*_T (one symbol) as in R88, read on
    F» (l. 99, 112-115). REFEREE a455907e: «every symbol bound … MATCHES (Opus 5.5, D15).»; REFEREE-2 0aae9be6: «F is now bound … ONE
    DEFECT left … j, never introduced in the line … With that edit: MATCHES.» Superseded by K14.
  - K14: CORRECTION (j): «of re-entries {+j − 1 → j+} of Even edges in R» (l. 131), REFEREE-2's edit (2bdda73d), «and nothing else»
    (l. 117); with L-SI's strict symbol test (l. 133-151): V and W still unbound. No referee line on K14 alone. Superseded by K15.
  - K15: CORRECTION (V, W): «n the number of vertices of the game» for «n = |V|» and «W := the [S1-val] valuation of the (σ, τ_{j−1})-plays,
    σ the Even strategy at the state compared;» for «W read against τ_{j−1},» (l. 166-168). REFEREE fe9d0cf1: «No free symbol. MATCHES
    (Opus 5.5, D15).»; REFEREE-2 895d7709: «No unbound symbol. MATCHES.» THE LINE TO LAND (Lead decision 04:16Z); this entry's title.
  - K16: SUPERSEDED (K13 + j + «W := the [S1-val] valuation of the (σ_t, τ_{j−1})-plays,», keeping «n = |V|»; l. 171-189, db7c9e43):
    by the Lead decision of 04:16Z, because it restores the free V (REFEREE fe9d0cf1); L-SI's note l. 191 (bba03405): «Lead decision
    04:16Z: K15 is the line to land; K16 is superseded (it restores the free V, REFEREE fe9d0cf1).» No referee line on K16.
  Both §Cs: «K2-K11 are clarifications / readings; none widens a signed statement.» (REFEREE §C l. 86); «None widens a signed statement.»
  (REFEREE-2 §C C.5 l. 94).
- Referee strengthening (NOT part of this entry; notes or readings of one referee, conjectures, and premise notes; none is in a verdict
  cell):
  (0) CONJECTURE REP-WPAID (lane, K11 l. 72-73: «N-CUT-10's question ("is every REPEAT W-paid?") is recorded as an open CONJECTURE of the
  lane (REP-WPAID), not used anywhere»). REFEREE-2 N-CUT-10 (l. 240-241): «CONJECTURE-level question for the lane: is every REPEAT W-paid?
  Open; not used.»; data: every REPEAT in every corpus is W-paid (REFEREE-2 §4.2 l. 162: 41 sbcg + 780 latew + 3 pins), W-silent and
  own-cycle REPEATs 0 (both referees). OPEN, unsigned.
  (i) CONJECTURE REP-LIN (REP_F ≤ n, packet §8 l. 201): DEAD, L-RED R128 (docs/red/R128-rep-lin.md, l-red 0e91e875, addendum e55592d9):
  latew_K20_m32, one W-run, REP = (K − 1)(m − 2) = 570 > n = 538 (874 at K 24, m 40); REPRODUCED by REFEREE-2 on its own engine (§4.2
  l. 153, l. 165: «REP* = 570 > n = 538 on latew_K20_m32 (REP-LIN false)»); REFEREE did not run latew (§C l. 30: «n 538 > my MAXN»). The
  packet does not depend on it (Claims signed). [P-REP] (polynomial REP*) and [P-SC] stay OPEN (packet §8 l. 201, K6).
  (ii) REFEREE-2 only: the leave k in LATE-SPLIT (ii) is UNIQUE in (u₁, u₂) (§5 l. 173-174, «every adoption of z after u₁ is late»);
  REFEREE «Any leave k in (u₁, u₂) works» (l. 113); REFEREE §C l. 25-26: «Both true; compatible.» Not in either verdict table.
  (iii) REFEREE only: MUT 5, W-MON′ compared in the NEW frame τ_{t+1} at τ-changing S4a steps, «22 violations — the old-τ frame is
  essential» (l. 75-76); OPT-OFF's necessity datum also at t = 0 → 1 on tog6b_n32 (l. 73-74); CUT-POLY «is the iteration half only; the
  time half needs R57 BIT-G (per-iteration bit cost)» (l. 141-142); the [SR-λ] quote elides the bound, which the source line carries (l.
  13-15; REFEREE-2 §1 l. 46-47 says the same).
  (iv) REFEREE-2 only, beyond the K-items: W-RETURN-G's conclusion holds for EVERY anchor, not only the smallest (§3 l. 110, DATA, 50
  checks); "polynomial" means «bounded by a polynomial in n on every run of every game, as in CUT-POLY» and "W" inside "W-silent" is defined
  by the cited §4 / §1 (§C C.3 l. 69-70, «Optional precision, not required»).
  (v) Off-cycle premise of LATE-SPLIT (ii) never exhibited: REFEREE CUT-N6 (l. 220-221; MUT 3 never bites), REFEREE-2 N-CUT-10 (l. 240):
  «The corrected form of LATE-SPLIT (ii) is required by the proof, not by data.» The premise stays; no signed item drops it.
- Honest limits: (i) A REDUCTION. CUT-RED bounds T through B*, REP*, SC* and O*, none bounded here; [P-B], [P-REP], [P-SC], [P-ODD] are
  OPEN. REP-LIN, the lane's candidate for [P-REP], is DEAD (R128: REP = Θ(n²) in one W-run on latew); [P-REP] needs some polynomial, not n.
  Packet l. 8-9: «a REDUCTION of N5's iteration count on every game to four counts that are NOT bounded here. … G-N5-TIME stays OPEN.»
  REFEREE l. 16-17 and REFEREE-2 l. 21-22 say the same. (ii) Standing premise: OPT-OFF (i), and through it every item, uses that S1's
  procedure realises the optimal counterstrategy (R57's 1E-N3; R17 (a) (F1) with R57 (a)); the code's match to SPEC is DATA (R15
  G-N5T-1), used by no proof (K2). (iii) Counts are transitions, not bit operations; CUT-POLY is the iteration half only; no running-time
  bound. (iv) The bound is far from tight on the data (REFEREE-2 §8 l. 281: «max T 1,072 against bounds of order 10⁸»); no claim on its
  order. (v) Not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open.
- Data (DATA, not proof): pinned (packet §9 l. 212-215: experiments/si/check.sh «box 40», «box 42», «box 43»; at 2678f6c6 check.sh sha1
  311a047c875686909f42c0151ad0fedc5a2c7bf1, 813 lines, blocks l. 796-813; trunk adds post-freeze blocks only, `git diff --numstat 2678f6c6
  357930cc`: 15 added, 0 removed). Files at 2678f6c6, all = trunk: odd/cuts.py b5dff8f45ffb8abd704340d2c28016e0cda6073d, odd/cutsx.py
  0e5edc8383127ec247380977aef078063fdf9954, odd/laterep.py 6eeb6e03a18a2c57f16b875bf2244ad466b923ca, rund/quotecheck.py
  29bb4a971680c9278f5f8c6f40eac17c0134db72, experiments/new/box64/frozen.py 7c47dd619889bafac8fd2380c11d90c09cec7b31. Re-run for this draft
  from a `git archive` of 2678f6c6 (experiments/si, new, red/so, harness and the packet; `python3 -I`; outputs to scratch files; exit codes
  read): l. 797-808 under `set -euo pipefail`: «si (box 40: W-RETURN-G and cut-attached re-entries): PASS», «si (box 42: late adoptions
  FIRST / REPEAT): PASS»; the box 43 lines need git for the quote check and were re-run with GIT_DIR set to this repository: quotecheck
  «quotes=13 bad=0», «QUOTES PASS», rc 0; --mut «quotes=13 bad=13», «QUOTES FAIL»; frozen.py hntop_n3 --start --wrun «… iters 61
  tau-stretches 1 … its-phases 13 its-causes {'fb': 0, 'sbar': 0, 'lx': 0, 'lw': 12} … worst-frozen-phase {'len': 18, 'wch': 18, 'flat':
  0, 'R': 0} FWR-viol 0», rc 0. Outputs: cuts.py rise_thin51_n40 «REENT 125 CUTRE 14 FRESH 92 CYC 0 WPAID 19 SILENT 0 VIOL 0 … PASS»; FR=1
  fc_3 «REENT 166 CUTRE 0 FRESH 97 … VIOL 0 … PASS»; MUT=nofresh «VIOL 16 … FAIL»; MUT=off1 «VIOL 92 … FAIL»; cutsx.py «FR_WC 68 FR_GAIN 24
  FR_SAME 0 FR_GAIN0 9 FR_CYC 0 FR_LATE 15 FR_LATE_V 0»; laterep.py so_th_n32 «'late': 6, … 'first': 4, 'repeat': 2, 'RV': 0, 'cyc': 0,
  'MAXE': 3», rise_thin51_n40 «'late': 23, … 'first': 23, 'repeat': 0, 'RV': 0». Packet §9 lane DATA (719 games of
  experiments/si/odd/sbcg.lst, S3 start): 11,669 re-entries, F 557, FR 6,031, C 4, P 5,035, S 42, W-RETURN-G failures 0; FR split WC 3,925,
  G0 1,787, LATE 313, CY 1, SAME 5; 1,141 late adoptions, FIRST 1,100, REPEAT 41, W-silent REPEATs 0, most REPEATs in one game 6; hntop_N
  max R* = 0; spanobs / carryobs 1,077 / 1,609 re-entries, all P. Both referees REPRODUCED these counts EXACTLY on independent engines
  (REFEREE §9 l. 152-155, CUT-N7; REFEREE-2 §4.2 l. 156-160; REFEREE §C l. 27-28). REFEREE (successor 19; own
  docs/referee/scratch/cut_probe.py, sha1 e28082e31aba20f5eec94188e4b4e749dbad24f6, on rl_engine, no lane code; pins re-run alone in a clean
  detached worktree at 2678f6c6, exit 0): n ≤ 120 (671 games, 765 runs, 13,137 transitions), 0 violations of FACTB, OPT1 (78,486), OPT2
  (492,243), WMON (545,448 vertex checks, 1,568 at τ-changing S4a steps), WRETG, CC (16,527 pair-run checks), FCB, FRREM, FS (573 LATE, all
  BLOCKED), LS2, LS3, RREP, LAM, WV (55,052, largest ratio 0.40), WRUN_CROSS, THM, BOOK; largest B* 61, REP* 2, SC* 31, O* 41, T 172 (both
  starts), on the 719 S3 runs B* 55, O* 55, SC* 31, T 264; MUT 1 / 2 / 4 / 5 bite (249 / 313 / 77 / 22), MUT 3 never; random n 8-20, 1,200
  runs, 0 violations («short runs, T ≤ 8: weak evidence»). REFEREE-2 (successor 21; own R2-N5-CUT/cut_check.py, sha1
  f19a43f05f9fd19e5582f23c452e57b8e689c181 (1a2b12da), on its lane's dual_check.Runner; the lane's scripts only run as the pinned blocks in a
  detached worktree at 2678f6c6, logs/pinned_check.txt, never imported): sbcg 719 runs / 11,621 transitions (OO1 / OO2 / WS 86,336 /
  647,486 / 473,219; WRG 50; max B* / REP* / T 55 / 6 / 264); lane pins 6 / 246; L-RED red/ 12 / 3,154 (5,502 re-entries, all P; d_wobs
  O* 279, T 1,072); hntop_n2..n8 14 / 1,267 (8,282, all P); latew_K8_m32, latew_K20_m32 4 / 986 (late 898 = 118 FIRST + 780 REPEAT; REP*
  570, n 538; K8: 210, n 370; T 700); random 9,900 runs / 16,717 transitions; every log RESULT PASS, 0 violations of FB, OO1, OO2, WM, WS,
  WRG, CC1-CC3, FS, LS1-LS3, RREP, WV, CR; controls OO2_own (534 sbcg) and WRG_cut (472 sbcg) bite. Caps: OO1 exhaustive for n ≤ 60,
  sampled above (OO1_sampled_steps 780 on sbcg); OPT-OFF (ii), W-SUCC and every counting check exhaustive (§4.2 l. 168-169). No signed
  statement uses any count.
- Signatures: REFEREE docs/referee/R-N5-CUT.md (report ff5a6f815ea82932f10be6fb45b53a891ba6ef62, 2026-10-30T01:30:28Z, sha1
  63d1f86b52e3f5e9ea5fc90ce2a25349b8ea5e91 there, 191 lines; §10b line check 8a7818a0067bca5a162bb5f3f3abdc74d1dde138, 01:40:15Z,
  append-only (`git diff --numstat ff5a6f81 8a7818a0`: 38 added, 0 removed; no verdict line changed), sha1
  bd4208e295e3096443752e75b6f59145fde86aa1, 229 lines, = trunk 5754f213 = referee head fe9d0cf1 (re-measured 04:3xZ; last commit touching
  it 8a7818a0); successor 19): §1 CHECKED; every PROVED item SIGNED;
  «No gap. Nothing FALSE. Notes CUT-N1..N7.» (l. 37). §C docs/referee/R-N5-CUT-C.md (1a4e757165c09dc94561d411f01d70aa79de2417,
  02:03:59Z, sha1 d8aedd5af80fdc155c342071c6b379c775e918ae, 92 lines there; then append-only: K12 line l. 94 at 40fd25a3 (+2/−0), K13 line
  l. 95 at a455907e (+1/−0), K15 line l. 96 at fe9d0cf1 (+1/−0); measured at referee head fe9d0cf1 (fetch 04:31Z): sha1
  1bdf40901e2ad84470b32b69d7296354b73865e9, 96 lines, last commit touching it fe9d0cf1199e85c4765b94551dd2aebedc5b42dee (04:06:52Z); trunk
  5754f213 still has the a455907e version, sha1 4bc6129fe5c982e1bf395895e4fdbec7d5c08988, 95 lines (fe9d0cf1 not merged yet)): «Verdicts identical. Gap map
  EMPTY (neither referee lists a gap; nothing FALSE). No disagreement on any proof step.» (l. 22); K0 MATCHES; K1 SIGNED; «K2-K11 are
  clarifications / readings; none widens a signed statement» (l. 86); «I missed N-CUT-4 (§0's row); recorded.» (l. 91). REFEREE-2
  docs/referee-2/R2-N5-CUT.md (report 6270f74532e69269f43bc5a1f07f791fb14fd2a6, 01:21:53Z, merged as
  7fd2aea8a1881edbf6dd4137e9b5436d94e564bb, 01:21:54Z, sha1 260f8e802a263aff558166eab498e26d39ff5466 there, 255 lines; §8 addendum
  72377b92202dcb8bf94d5891de1e29e709725ed5, 01:32:15Z, merged as 335814dcf48b9e153e97bb548bbfd9c37537abf9, append-only (48 added, 0
  removed), sha1 ace5e691baa42fd62fec100986243fa5fb52f934, 303 lines, = trunk; successor 21): all items SIGNED, CUT-POLY as an
  implication; «No gap. Nothing FALSE. Notes N-CUT-1..N-CUT-10 (§6).» (l. 41). §C docs/referee-2/R2-N5-CUT-C.md
  (443cf523dbefd3b4c51cde87bb2553ba3b36856f, 02:07:16Z, merged as 4d6a69d18ed4107bfb62de2815d5ba20b6b474de, sha1
  d33962fb90b3ba67b4e3aa23c9841681928c9391, 103 lines there; then append-only: K12 line l. 104 at b93dc4a7 (head 0140da67), correction
  l. 105 at 1f5a9fbe (head 8a0f0ed6), K13 line l. 106 at 0aae9be6 (head 2bdda73d), K15 line l. 107 at 895d7709 (head 85e6d86e), each
  +1/−0; measured at referee-2 head 85e6d86e (fetch 04:31Z): sha1 2d48a870d5467481b9e1196e5b05c944bb65f009, 107 lines, last commit touching
  it 895d770964463b69999e2ba3c6445b4707fdc13e (04:06:57Z; merged into the branch as 85e6d86e95caa223d3c426502153325c7cba18c8, 04:06:58Z);
  trunk 5754f213 has the 0aae9be6 version, sha1 00abe55da9554211e2e3ab5347c5719bf574b3c1, 106 lines (85e6d86e not merged there; the local
  working head 54b8526f, not on origin at the fetch, has the 107-line version); REFEREE-2 21 PARKED at 85e6d86e): «Joint gap map: EMPTY. Every item is
  signed by both referees; neither lists a gap.» (l. 27, bold in the source); K0 MATCHES; K1 SIGNED; «None widens a signed statement.»
  (l. 94). INDEPENDENCE: REFEREE l. 7: «Independence: no docs/referee-2/ file opened.»; REFEREE §C l. 3-4: its report and §10b were
  «pushed BEFORE I opened any docs/referee-2/ file», REFEREE-2's report «opened 02:02Z after the Lead's word». REFEREE-2 l. 16-19: CUT name
  count under docs/referee/ on origin/claude/referee «0 at 01:03Z and 01:21Z. Names only; no docs/referee/ file opened; no `git log` on
  origin/claude/referee»; REFEREE-2 §C l. 4-5: REFEREE's report «Opened only after the word». No review imported lane code. Notes map
  (REFEREE §C l. 31-35; REFEREE-2 §C C.2 l. 35-49): CUT-N1 = N-CUT-2, CUT-N2 = N-CUT-3, CUT-N3 = N-CUT-5, CUT-N4 = N-CUT-9, CUT-N5 ≈
  N-CUT-6, CUT-N6 = N-CUT-10, CUT-N7 ↔ REFEREE-2 §4.2; REFEREE-2 only N-CUT-1, -4, -7, -8 (all answered by fixes: K3, K5, K8, K9).
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (an upper bound on N5's iteration count on every game in terms of four counts of
  the run, none of which is bounded, with the matching converse; a REDUCTION; no bound on a run, no running-time bound, no algorithm claim).
  GAPS G-N5-TIME: open.

Proposed GAPS line-11 UPDATE (append-only), after the R89 UPDATE of G-N5-TIME (GAPS l. 11), built only from the title clauses (landing time
and CHECKER addendum to be filled at landing; K15 has no "|"; the "via" parenthetical's inner clause on F, R*_T and REP_F is dropped; Lead
revision 04:31Z: brought to K15's wording, the three K13 → K15 edits; K13's own two lie inside the dropped clause): «UPDATE 2026-10-30 <HH:MM>Z: RESULTS
R90 (P-N5-CUT; CHECKER C100 Add. <k>) [refereed-only] LANDED: N5 (SPEC S1-S5) on every game, under the standing SPEC premise of RESULTS R57
(S1's procedure realises the optimal counterstrategy), with RESULTS R15 (d), R17 (a) and R47 (a): T ≤ 2n(n−1) + (n(n−1)+1)·(m_E·[1 + 2B* +
(B*+1)·K] + SC* + O*), K := n(n−1) + (n(n−1)+1)(n−1)(m_E + REP* + 1), T the number of transitions (iterations) of the run, n the number of
vertices of the game, m_E the number of edges leaving Even vertices, λ-runs and λ^U-runs as in RESULTS R86, W-runs as in RESULTS R89, late
adoptions as in RESULTS R88 / R89; B* the largest number of transitions inside one λ-run that are Even S4c fallbacks or change τ; REP* the
largest number of REPEAT late adoptions (a second or later late adoption of the same Even edge) inside one W-run; SC* the largest number,
over λ-runs R, of re-entries j − 1 → j of Even edges in R of class S (W-silent) or C (own-cycle) of P-N5-CUT §4 (W := the [S1-val] valuation
of the (σ, τ_{j−1})-plays, σ the Even strategy at the state compared; smallest anchor); O* the largest number of τ-changing transitions
inside one λ^U-run (Theorem CUT-RED, via Lemmas OPT-OFF, W-RETURN-G, LATE-SPLIT, WV-R and Corollary CUT-CHARGE); so T is polynomial if and
only if B*, REP*, SC* and O* are (Corollary CUT-POLY and its converse, fixes K1): a REDUCTION; none of B*, REP*, SC*, O* is bounded here;
CONJECTURE REP-LIN is DEAD (L-RED R128, latew_K20_m32). G-N5-TIME stays open.»
