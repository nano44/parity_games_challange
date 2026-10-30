# Draft RESULTS R93 (Lead, 2026-10-30 11:21:17Z by date -u, read in the same command as the fill of this file; subagent draft; packet, fixes W1-1..W1-5, title line W1, both reports, both §Cs and both W1 verdict lines read at the origin heads fetched 11:06Z (date -u 11:06:29Z, read in the same command after the fetch; W1 verdicts 14bfa3cc and b7b0d54f already there) and re-fetched with origin trunk at 11:14:11Z (date -u in the same command); pinned «box 79» blocks re-run 11:11:42Z-11:12:02Z; §8.4 DATA re-summed 11:12:13Z) — to CHECKER C103
to check: (1) TITLE. The title is the line file docs/new/P-N5-WCH-box79-line-W1.txt (l-new c930e26fcdd66ffaf19e3c6d081b52d08a9037f3,
2026-10-30T10:34:06Z, the file's only commit, sha1 00f9e375c448153f19b7620037a2723f6d10a0b1; identical at l-new head 163342eb, at origin
trunk 200a9e2e and at the local trunk head 19f0d2f5; first on trunk by the merge 05f6c315, 10:54:07Z), verbatim: one line, no outer
quotes, no final period, 6,518 characters (6,760 bytes plus the newline). «2026-10-30» occurs exactly once, right before « — a REDUCTION»
(by script), so NO date is inserted. The line holds ten "|" characters: «|F|» four times and «|Z_a|» once; they stay in the heading
(R91's heading has «|Z_{k+1} ∖ Z_k|») and are replaced in the GAPS UPDATE only (see (8)). The checker fill ", CHECKER PASS
(docs/checker/C103.md, checker PENDING)" is appended as in R90-R92 (no space before the comma, as R92; the brief's « , » read as a
separator). The heading was built by script from the file at c930e26f (level-3 marker, then "R93 [refereed-only] ", then the file without
its newline, then the fill) and re-checked after writing: equal.
(2) LINE HISTORY: frozen 9ac6fdba (docs/new/P-N5-WCH-box79-line.txt, l-new 2ad78f51, 6,565 characters plus the newline, the line both
referees reviewed) → W1 00f9e375 (W1-3's four changes L-1..L-4). 9ac6fdba is history, not the title. Word diff 9ac6fdba → W1, measured
three ways for this draft: `git diff --no-index --word-diff=porcelain` (seven hunks: +«R84 (a) (Fact DELTA),»; +«k → k + 1»; «if» →
«if, for a function w : ℕ → ℕ,»; «which keeps σ_t(v) at every Even v where it is consistent» → «which,»; «W*,» → «W*»; «in the sense of
Lemma TIE's two forms» → «keeps σ_t(v) at every Even v whose W*(v) has length at least 1 and satisfies v ⊕ W*(σ_t v) = W*(v), and at every
Even v with W*(v) = (v, ∅, 0) for which W*(σ_t v) has cycle node v and empty path set,»; «elsewhere;» → «at every other Even v;») = the
fixes file's own list (l. 26-35) hunk for hunk; an exact string-replacement script («R56, R86» → «R56, R84 (a) (Fact DELTA), R86»; «Z-flat
in-phase fallbacks of P all of whose» → «… fallbacks k → k + 1 of P all of whose»; «Corollary WCH-ONE) if every» → «… if, for a function
w : ℕ → ℕ, every»; the σ′ clause from «replaced by σ′, which» to «; nothing transfers to N5)» → W1's; each old string occurs exactly once;
the result equals W1 byte for byte); difflib over whitespace tokens, 1,247 → 1,294 tokens, seven non-equal opcodes (= REFEREE-2 §C.6 l. 72
«1247 → 1294»). The seven hunks are exactly L-4, L-1, L-2 and L-3 (three hunks); nothing else changes, every inequality is token-identical,
and «under ASSUMPTION OPT-ONLY» is unchanged.
(3) THE LINE AT BOTH REFEREES. W1 (the title): REFEREE successor 19, docs/referee/R-N5-WCH-C.md l. 64, appended at b7b0d54f
(2026-10-30T10:55:21Z; `git diff --numstat 938537ed b7b0d54f`: +2/−0, a blank line and l. 64): «W1 check (Lead 10:53Z; l-new c930e26f
docs/new/P-N5-WCH-box79-line-W1.txt sha1 00f9e375c448153f19b7620037a2723f6d10a0b1, fixes sha1 8377a1b8baa0e53cb4df509d1aa91f427628983d,
re-measured; packet unchanged 31caa72e; my own word diff 9ac6fdba → W1, written 10:55Z by date -u): exactly the four changes. … L-3: σ′
defined directly, and the inlined rule equals §7.1's three cases verbatim in content … OPT-ONLY label kept (Lead option (a)). Strict
symbol test of the whole W1 line: no free symbol, no unlanded source. MATCHES (Opus 5.5, D15).» REFEREE-2 successor 22,
docs/referee-2/R2-N5-WCH-C.md §C.6 (l. 70-80, 14bfa3cc, 2026-10-30T10:54:44Z; +12/−0 against 6ff5d18a): l. 71 «MATCHES (Opus 5.5, D15).»;
l. 72 «Word-diff 9ac6fdba → W1 (my own, difflib over tokens, 1247 → 1294) shows exactly four changes, and nothing else changes:»; l. 78
««under ASSUMPTION OPT-ONLY» is unchanged, per option (a). Every inequality is token-identical.»; l. 79 «My strict symbol test: the new
tokens k, w, ℕ, ℓ / «length», ∅ are each bound in their clause. No free symbol remains.»; l. 80 ««box 79» at c930e26f: PASS, exit 0. It
includes the SPEC quote check (W1-1 fixes the four tags) and «line W1 strict symbol test PASS».» REFEREE-2's W1 line IS on origin
(origin/claude/referee-2 = 14bfa3cc at both fetches): not PENDING. Both W1 verdict commits are NOT on origin trunk 200a9e2e at the
11:14:11Z fetch; they are on the LOCAL trunk head 19f0d2f5 (Lead commit 11:13:53Z, local 8 commits ahead of origin, 0 behind) through
the merges e707d3df (b7b0d54f, 11:13:52Z) and a7ed06f2 (14bfa3cc, 11:13:53Z). Not revised for W1 (both W1 verdicts stand apart from
them): REFEREE §C l. 5 «Fixes and corrected line W1: not yet pushed. The word-diff goes in a later section.» and NEEDS l. 62 «Lead: the W1
line and fixes SHA for a word-diff.»; REFEREE-2 §C NEEDS l. 90 «Lead: send the corrected line W1 for the word-diff; your choice between
C.3 (a) and (b).» (C.6 precedes it). One small difference of reading, no verdict affected: REFEREE-2 l. 79 lists «ℓ» among W1's NEW tokens;
W1 adds the word «length» and «∅», no new «ℓ» token (ℓ was already in the frozen line's ⊕ clause). The line 9ac6fdba at the reports:
REFEREE l. 35 «MATCHES §2-§7 and claims nothing more; my strict symbol test finds no free symbol (§10)», l. 129 «Verdict on the line
(Opus 5.5, D15): MATCHES §2-§7, claims nothing more, every symbol bound.»; REFEREE-2 l. 31 «MATCHES §2-§7 | no REQUIRED fix; precision L-1
to L-4 (§3)», l. 145 «L-1 to L-4 are precisions. None is required». §Cs: REFEREE §C l. 55 «Joint position on the line: MATCHES, no
REQUIRED fix.»; REFEREE-2 §C l. 23 «agree on MATCHES; precisions C.4».
(4) CLAIMS SIGNED = the twelve items (a)-(l) below, each SIGNED in BOTH verdict tables (REFEREE R-N5-WCH.md "## Verdicts" l. 18-35;
REFEREE-2 R2-N5-WCH.md "## 1. Verdict table" l. 16-32), re-read for this draft, and «SIGNED by both» / «agree» in both §Cs (REFEREE §C
l. 10-18; REFEREE-2 §C C.1 l. 10-22). Each candidate of the brief was checked against both tables: Fact REW / LEX (with COMMON PREFIX),
Lemma TIE, NEW-BOUND, Theorem RET-WCH, Corollaries RUN-WCH and REP-WCH, SIL-Z, SC-GXC, GXC-CLOSE, GXC-SPLIT, LEVEL-MON, DROP-PAID,
FBO-R56, FBO-SPLIT, ZF-SPLIT, Theorem WCH-RED, Corollary WCH-ONE, and the §7 N5-LZC items LZ-OPT, W-MON_LZ, LZ-STRICT, RUN-WCH_LZ /
REP-WCH_LZ, LZ-NOSIL as the implication: every one is SIGNED in both; none is missing from either. NOT claims: §1 (REFEREE «CHECKED»;
REFEREE-2 has no §1 row); the §7.1 Definition of N5-LZC (a definition: REFEREE-2's row 7.1-7.4 names «definition» among SIGNED items,
REFEREE's row does not; recorded under Object); ASSUMPTION OPT-ONLY (CHECKED TRUE by both, a joint referee finding, not a claim of the
line: the paragraph «Joint referee finding» below); §8 (both «not signed»).
(5) PREMISE LABELS (stale-label test; grep of docs/RESULTS.md at the local trunk head 19f0d2f5 = origin trunk 200a9e2e for this file, sha1
0ded3a3c9ecfabd295677e37c85d89e95d7df709, unchanged since 9ebff160, the R92 landing; every RESULTS label of the title):
- R57 (l. 2893): «the standing SPEC premise of RESULTS R57 (1E-N3: S1's procedure realises the pointwise optimum; for S4a, σ_new is the
  pointwise optimum of the one-player arena H_t …)»: the same wording as landed R91's title (l. 6384). R57 states 1E-N3 for σ̄ (R57 (b),
  l. 2915-2916, «(1E-N3 = N-1E-1)»); the S4a form is RESULTS R67's P2 / R88's [OPT-H] / R90 (a) (i) OPT-OFF (i) (the packet's §1 l. 50-51
  cites R90 (a) (i)). The same label point as R91's to-check (4) and R92's (4); landed as such twice. Match by precedent.
- R15 (l. 624): «R15 (a), (d)»: (a) Lemma A l. 631, (d) l. 640 (the packet's [R15] l. 52-54 quotes both verbatim). Match.
- R17 (a) (F1) (l. 738): «(F1)/(F2) (the optimum of a one-player game dominates every strategy of that game pointwise …)» = the packet's
  [F1] (l. 55). Match.
- R56 (l. 2832): Theorem FB-RED, «ρ := the Ξ-changes at Odd choice vertices in the phase» (title of R56): match for «ρ_P := RESULTS R56's
  ρ of the phase P» and FBO-R56.
- R84 (a) (Fact DELTA) (l. 4967): «for sets A ≠ B of ranks, weight(B) > weight(A) iff …»; the packet uses it (§1 l. 41) for «Distinct
  triples are distinct in the order (… as in R88-R91)»; R88 (l. 5685) and R91 (l. 6427) cite it the same way. Match (W1-3 L-4).
- R86 (l. 5269): λ-run «a maximal run of states with λ (λ^U) constant». Match.
- R88 (f) (l. 5738): Corollary FW-R*, whose quote defines «A LATE ADOPTION in F …» (F a frozen W-phase); read on W-runs through R90 (g).
  Match for «late adoptions … as in RESULTS R88 (f) and R90 (g)».
- R89 (l. 5854): «a τ-stretch := a maximal run of consecutive states with τ constant; a W-run := a maximal run of consecutive states of one
  τ-stretch none of whose transitions is an S4c fallback or changes λ_W» (title): match for τ-stretch and W-run. MISMATCH (precision, no
  verdict affected): the line reads «for a W-run F, |F| (its transitions) as in RESULTS R89», but R89's entry (l. 5854-6115) has no «|F|»
  (grep: 0); the line's own gloss «(its transitions)» binds it, so the symbol is bound; the citation is only to R89 for «W-run». The
  packet's §1 (l. 69-70) lists «|F| := its transitions» under its «RESULTS R89» bullet as a packet definition.
- R90 (l. 6116): (a) OPT-OFF l. 6179, (b) W-MON′ l. 6188, (c) W-SUCC l. 6190, (d) W-RETURN-G l. 6192, (e) CUT-CHARGE l. 6197 (classes F,
  FR, C, P, S; «SIL_R := #S»), (g) LATE-SPLIT l. 6207 (FIRST / REPEAT, REP_F): names and contents match the packet's §1 quotes (l. 62-73,
  85-91). «R90 Fact B» (OPT-ONLY clause): R90's setting, l. 6159 («Fact B: every transition is an S4a step with τ kept, or a boundary»),
  not a lettered item: match. MISMATCH (precision, no verdict affected): the line reads «S4a steps, boundaries, B_R (…), class-S re-entries
  and SIL_R as in RESULTS R90 (e)»; class S and SIL_R are R90 (e) (l. 6197-6199), but «S4a STEP», «BOUNDARY» and «B_R» are defined in
  R90's setting (l. 6157-6161), not in (e). Neither referee raised it (REFEREE l. 121-122 lists them «(R90 (e))»; REFEREE-2 l. 125 «R86,
  R90 (e) | bound»). REP* is R90 (j) (l. 6222: «REP* := max_F REP_F over all W-runs F»); the line defines it in place. Name clash: R91
  also signs Lemmas OPT-OFF ((d)) and W-SUCC ((e)), different statements; the line cites R90 (a)-(e), (g) and R91 (a)-(c), (h), (i), (k),
  (m) by letter, so no ambiguity (as R92's C101 Add. 2 point).
- R91 (l. 6384): (a) XW l. 6448, (b) W-MON l. 6451, (c) FB-W l. 6454 (not R21 (h)'s FB-W: R91's own note), (h) GAP-MON l. 6492, (i)
  SW-IN l. 6494, (k) REOPEN-W l. 6503, (m) GAP-RED l. 6507 (f_P, ZF_P); WCH^S4a_P(v) in R91's title. All match the packet's quotes (l.
  74-84).
- R38 (a) (l. 1825): Remark KEY («a (λ_Ξ, τ)-phase is exactly a joint λ-phase …»); used as the phase definition, as landed R84 (F4: «keeps
  RESULTS R38 (a) as the phase definition only», l. 4953) and R91 do. Match by precedent.
No other RESULTS label occurs in the title (R92 is not cited; REFEREE l. 63 and REFEREE-2 N-3 l. 193: REP-WCH uses no FW-R*′).
(6) SYMBOL TEST of the title (my own strict test of every symbol of W1; IN = bound in the line; else the carrier):
| symbol | where |
| --- | --- |
| N5, SPEC S1-S5, S4a, S4c, [S1-val], «more relevant», «rank», «reward» | SPEC (named; [S1-rank], [S1-ord] carry rank, relevance, reward) |
| the standing SPEC premise of RESULTS R57, 1E-N3, σ_new | named with its content in the line; R57 label point in (5) |
| H_t | IN («H_t := S4a's arena at t (Even keeps σ_t ∪ Iσ_t, Odd follows τ_t)») |
| R15 (a), (d), R17 (a) (F1), R56, R84 (a), R86, R88 (f), R89, R90 (a)-(e), (g), R91 (a)-(c), (h), (i), (k), (m), R38 (a) | cited premises, each a landed RESULTS item; see (5) |
| run, σ_t, τ_t | IN («a run is the sequence of states (σ_t, τ_t)») |
| ⊴, ◁, ⊵, ▷ | IN («the SPEC S1 order (better for Even) and its strict and reverse forms») |
| Iσ_t | IN (SPEC S2) |
| n, n_E, m_E, d_E(e) | IN |
| transition, t, «switched» | IN («a transition is written t → t + 1 (states t, t + 1), and v is switched at t if …») |
| Ξ_t, λ_Ξ | IN |
| Ω, «own Ω-cycle node» | IN («for a valuation Ω (Ξ_t, W_t, or W′ below)»); soft spot: SPEC and the packet use Ω for the priority map; the line names priorities only in words, so no clash inside the line |
| W_t, W(v), λ_W | IN («W(v) := W_t(v) at the state in question») |
| Z_t | IN |
| τ-stretch, W-run | R89 (title) |
| F, \|F\| | IN («for a W-run F, \|F\| (its transitions)»); R89 has no \|F\| (see (5)) |
| phase, in-phase transition | R38 (a); «in-phase» IN |
| f_P, ZF_P, WCH^S4a_P(v), «in-phase fallbacks», «Z-flat» | R91 (m) and R91's title, glossed IN («those k → k + 1 with Z_{k+1} = Z_k») |
| λ-run | R86 |
| S4a steps, boundaries, B_R | R90's setting (cited as «R90 (e)»: label point in (5)); B_R glossed IN |
| class-S re-entries, SIL_R | R90 (e) |
| late adoptions, REPEATs, REP_F, REP* | R88 (f), R90 (g); REP* IN («REP* := max_F REP_F») |
| ρ_P | R56 («RESULTS R56's ρ of the phase P») |
| σ⁺, W′, d, ⊕, x, (c, Q, ℓ), «path set», «length» | IN (Lemma TIE's clause; Q, not P, for the path set) |
| e, returns, u, WCH_F(e), TT_F(v, e), k | IN (RET-WCH's clause; «at some earlier state of F» = the packet's r ≤ u, since σ_u(v) ≠ e) |
| TIE_F | IN (on a W-run every transition is an S4a step with τ kept: the packet's TIE event) |
| Σ_e, Σ_v | over the vertices, by use |
| R, GXC event, GXC_X, X, GXC_R, GXC_P, NC_R, NT_R, j, max_P | IN (SC-GXC's clause; X ∈ {R, P} by use; «P over the phases inside R») |
| a, \|Z_a\|, TIE_P, FBO_P | IN (GXC-SPLIT's clause) |
| LEV_t(v), the coordinate sequence, r, t′ | IN (LEVEL-MON's clause; the sequence is Fact LEX's CS) |
| DROP_P(v) | IN (the name is attached after its bound, «(DROP_P(v))») |
| FBOS_P, «FBO events» | IN (FBO events = the pairs of FBO_P) |
| NZ_P, k | IN (W1, L-1: «fallbacks k → k + 1 of P») |
| ZFS_P, «keeps LEV» | IN; «keeps LEV» = LEV_{k+1}(v) = LEV_k(v), defined there since such v lie in Z_k = Z_{k+1} (SW-IN, Z-flat): by use |
| w, ℕ, S, w(n), [P-WCHτ](w) | IN (W1, L-2: «for a function w : ℕ → ℕ») |
| TIE* | IN |
| N5-LZC, σ*, σ′, W*, ∅ | IN (W1, L-3) |
| S4a step, W-run, TIE_F, TT_F, \|F\|, REP_F, class-S re-entry, read for N5-LZC | by use («for every W-run F of N5-LZC», «N5-LZC has no class-S re-entry»); the packet's §7.1 (l. 296-297) says the §1 definitions are read verbatim on N5-LZC's states and defines N5-LZC's S4a step; the line does not say it. Soft spot |
| t, τ_t inside the N5-LZC clause | the state at which S4a is applied, by use (as in Lemma TIE's clause) |
| ASSUMPTION OPT-ONLY, «Fact B» | IN («ASSUMPTION OPT-ONLY that RESULTS R90 Fact B and (a) (ii), (b), (c), (d) hold verbatim for N5-LZC runs»); Fact B = R90's setting l. 6159 |
| Lemma / Theorem / Corollary names | packet §2-§7 |
| G-N5-TIME, M3, step-4, TARGET.md | scope tail; GAPS l. 11, TARGET.md |
Every symbol of W1 is bound in the line, by SPEC or by a named landed entry. No free symbol found. Soft spots, as in landed titles: σ_t
and τ_t by the run; «Ω» as a valuation variable; «keeps LEV» by use; the N5-LZC reading of the N5 definitions by use; «|F| … as in
RESULTS R89» and «S4a steps, boundaries, B_R … as in RESULTS R90 (e)» cite the right entries but, for |F| and for the first three, not
the exact place (label points in (5)). Agreeing tests of W1: REFEREE §C l. 64 «Strict symbol test of the whole W1 line: no free symbol,
no unlanded source.»; REFEREE-2 §C.6 l. 79 «No free symbol remains.»; the lane's symtest.py (fixes l. 36-38: «W1 186 symbols, 0
failures, SYMTEST PASS»; re-run for this draft, (9)). REFEREE-2 N-5 (l. 196-197): symtest.py «cannot see a clause-scope slip like L-1,
so it is not a substitute for the by-hand test» (REFEREE §C l. 50: «agreed»).
(7) OPT-ONLY. The line keeps «under ASSUMPTION OPT-ONLY …» (Lead decision (a)). The decision is recorded in docs/agents/LEAD-STATE.md
l. 2066, in the entry stamped «10:54Z (date -u, shell)»: «Lead decision (a): the line keeps «under ASSUMPTION OPT-ONLY», the RESULTS body
records the joint check.» The brief's «~10:44Z» is not the stamp of that entry; REFEREE's W1 line (l. 64, «Lead 10:53Z») cites «Lead
option (a)», so the word went out by 10:53Z. The exact time of the decision is for the Lead to state. The joint finding is in the paragraph
«Joint referee finding (not a claim of the line)» below; it is not in the title claims, and it transfers nothing to N5.
(8) GAPS: G-N5-TIME (GAPS l. 11) stays open; the title names no CONJECTURE (only the premise [P-WCHτ], «not proved here»). A line-11
UPDATE is proposed at the end, after R92's UPDATE (the last one on l. 11 at origin trunk 200a9e2e and at local 19f0d2f5: «UPDATE
2026-10-30 09:03Z: RESULTS R92 (P-N5-LATEP; CHECKER C102 c13477c2) …»; docs/GAPS.md sha1 60545880592f4e144ea34cd0aa9ddbf7aae38792,
unchanged since 9ebff160). Built by script from W1's clauses only, with R92's construction: «LANDED: » + the title with each lemma label
moved behind its clause, the scope tail «(2026-10-30) — a REDUCTION (X; G-N5-TIME stays open; not M3, …)» → «: a REDUCTION; X. G-N5-TIME
stays open.». The UPDATE must hold no "|", and W1 holds ten, so three replacements were made that are NOT title text (decision for the
Lead / CHECKER): «|Z_a|» → «the size of Z_a» (R91's UPDATE wording for the same symbol); «for a W-run F, |F| (its transitions) as in
RESULTS R89» → «for a W-run F, the number of its transitions as in RESULTS R89»; «|F| ≤» (three times) → «the number of transitions of F
≤» (one of them reads «every W-run F has the number of transitions of F ≤ …»: grammatical but stiff). Checked by script: with the labels
removed from both, the UPDATE equals the title up to these replacements and the tail; no "|"; «2026-10-30» once (the stamp).
(9) DATA of record = the packet's DATA (§8.2 and the §8.4 table, l. 345-359) and fixes W1-5 (NC_R = NT_R = 0 on REFEREE's whole corpus).
§8.4 re-summed for this draft (experiments/new/box79/sumpk.py over wchpk_sbcg.txt and wchpk_alt.txt at 2ad78f51, unchanged at c930e26f):
equal in every printed field. The referees' run sets are recorded beside it: REFEREE 722 runs (719 distinct games, n ≤ 80, given and S3
starts); REFEREE-2 1,131 runs per engine (all sizes; one invalid start skipped). Their counts differ from the lane's by run set, not by
definition (REFEREE §C l. 27; REFEREE-2 §C C.5 l. 62).
(10) Discrepancies, recorded for CHECKER, no verdict affected: (i) stamps: REFEREE's report says «report written 10:08Z by date -u» (l. 6),
its commit d71d6e55 is 10:06:43Z; REFEREE's §C says «written 10:32Z-10:36Z by date -u» (l. 2), its commit 938537ed is 10:33:03Z; the
fixes file says «Written 2026-10-30 from 10:35Z (date -u)» (l. 4), its commit c930e26f is 10:34:06Z. Each «written» stamp postdates (or
ends after) the commit that holds it. (ii) Section ranges for the OPT-ONLY check: REFEREE l. 88 «P-N5-CUT §1-§3», REFEREE §C l. 30
«P-N5-CUT §2-§4», REFEREE-2 l. 105 «P-N5-CUT §2-§4», REFEREE-2 §C l. 30 «P-N5-CUT §1-§3». (iii) experiments/new/box79/run.sh was
rewritten at bbd8fa74 (09:38:07Z) to run succ. 36's flatsrc.py; the packet's DATA run script is now run_wchpk.sh (sha1
c82f9085081c66a2dd2a206103d593debc7ea47f; «run_wchpk.sh split»), and wchpk.py, sumpk.py and the two data files are unchanged since
2ad78f51. The packet's §8.2 names wchpk.py and the wchpk_*.txt files only. (iv) The «box 79» label is shared: check.sh at c930e26f has
the WCH block (l. 400-405) and succ. 36's FLAT-SRC block (l. 406-411); only l. 400-405 belong to this entry. (v) REFEREE-2 l. 180: the
lane's «W-runs 1692 / 1658» counts W-runs of length ≥ 1 that hold a return; REFEREE-2's «8,941 / 8,892» counts all W-runs. (vi)
REFEREE-2 l. 178-179: its returns and paid counts are 19 below the lane's on both engines: one game skipped (invalid start file
comp54_n80, «non-edge 11 → 51»), which the lane's start_pair accepts. (vii) The fixes W1-2, W1-4 and W1-5 were not re-read by either
referee after c930e26f (both W1 lines cover the line and, at REFEREE-2, the pinned block with the quote check); W1-2 is the reading both
referees proposed (WCH-N2, N-1), W1-4 and W1-5 record their own notes.
(11) Excluded: lane work after the freeze other than the fixes commit c930e26f (fixes file, line file W1, quotecheck.py, symtest.py and
symtest_W1.out, check.sh «box 79»): L-NEW boxes 80-83 (3aac0638, ab2a15b7, 163342eb, box 83 not pushed at the fetch), the FLAT-SRC box
79 of L-NEW successor 36 (c50a4985, 9555501d, merged into l-new by bbd8fa74), and L-RED R131-R134 (011213ef, 7e85ead2, 125c7b15,
5d78e948, 59008d24) are not part of this entry. They appear only in the one exclusion sentence under Not signed.
(12) Commits: REFEREE commits its files directly on claude/referee (d71d6e55 → 938537ed → b7b0d54f, each the parent of the next; the
first's parent 9f4d5821 is a Lead trunk commit). REFEREE-2 commits directly on claude/referee-2; 24f32388's parent is 9f4d5821, 6ff5d18a's
parent e4eaaa99 and 14bfa3cc's parent 0f2ca021 are merges of trunk into claude/referee-2. First trunk commits containing each: packet
2ad78f51 → bf6985bf (09:57:42Z); fixes c930e26f → 05f6c315 (10:54:07Z); REFEREE d71d6e55 → fb210b9e (10:21:07Z), 938537ed → 5c8b11e2
(10:54:08Z), b7b0d54f → e707d3df (11:13:52Z, LOCAL only); REFEREE-2 24f32388 → 7a003a9b (10:32:21Z), 6ff5d18a → 51f1bdbf (10:54:09Z),
14bfa3cc → a7ed06f2 (11:13:53Z, LOCAL only). (13) Placement: after R92 (R92 landed at 9ebff160; "## Dead ends (kept;" follows it).

### R93 [refereed-only] N5 on EVERY game (SPEC S1-S5, under the standing SPEC premise of RESULTS R57 (1E-N3: S1's procedure realises the pointwise optimum; for S4a, σ_new is the pointwise optimum of the one-player arena H_t, H_t := S4a's arena at t (Even keeps σ_t ∪ Iσ_t, Odd follows τ_t)); premises RESULTS R15 (a), (d), R17 (a) (F1), R56, R84 (a) (Fact DELTA), R86, R88 (f), R89, R90 (a)-(e), (g) and R91 (a)-(c), (h), (i), (k), (m); a run is the sequence of states (σ_t, τ_t); ⊴, ◁, ⊵, ▷ the SPEC S1 order (better for Even) and its strict and reverse forms; Iσ_t the improving edges of σ_t (SPEC S2); n the number of vertices of the game, n_E the number of its Even vertices, m_E the number of edges leaving Even vertices, d_E(e) the number of Even vertices with an edge to the vertex e; a transition is written t → t + 1 (states t, t + 1), and v is switched at t if σ_{t+1}(v) ≠ σ_t(v); Ξ_t := Ξ_{σ_t} (SPEC S1), λ_Ξ its cycle-node map; for a valuation Ω (Ξ_t, W_t, or W′ below), v is its own Ω-cycle node if the cycle node of Ω(v) is v; W_t := the [S1-val] valuation of the (σ_t, τ_t)-plays (W(v) := W_t(v) at the state in question), λ_W its cycle-node map; Z_t := {v : Ξ_t(v) ≠ W_t(v)} the gap set; a τ-stretch, a W-run and, for a W-run F, |F| (its transitions) as in RESULTS R89; a phase as in RESULTS R38 (a), an in-phase transition one with both states in one phase, f_P, ZF_P and WCH^S4a_P(v) as in RESULTS R91 (the in-phase Even S4c fallbacks of the phase P, those k → k + 1 with Z_{k+1} = Z_k, and the in-phase S4a transitions of P changing W(v)); a λ-run as in RESULTS R86; S4a steps, boundaries, B_R (the boundaries inside the λ-run R), class-S re-entries and SIL_R as in RESULTS R90 (e); late adoptions, REPEATs, REP_F and REP* := max_F REP_F as in RESULTS R88 (f) and R90 (g); ρ_P := RESULTS R56's ρ of the phase P): (Lemma TIE) at an S4a step t → t + 1, for any pointwise-optimal Even strategy σ⁺ of H_t with W′ the [S1-val] valuation of the (σ⁺, τ_t)-plays, an Even v with d := σ_t(v) ≠ σ⁺(v) and W′(v) = W_t(v) has v ⊕ W′(d) = W′(v) (the prefix operation x ⊕ (c, Q, ℓ) := (c, Q ∪ {x if x is more relevant than c}, ℓ + 1) for a value (c, Q, ℓ) (cycle node c, path set Q, length ℓ)) if v is not its own W′-cycle node, and W′(d) with cycle node v and empty path set otherwise; (Theorem RET-WCH) in every W-run F, for every Even v and successor e, the returns of v to e (transitions u → u + 1 of F with σ_{u+1}(v) = e ≠ σ_u(v) at which v held e at some earlier state of F) number at most WCH_F(e) + TT_F(v, e), WCH_F(e) the transitions of F at which W(e) changes and TT_F(v, e) the transitions k → k + 1 of F at which v leaves e (σ_k(v) = e ≠ σ_{k+1}(v)) with W_{k+1}(v) = W_k(v); so, with TIE_F the pairs (v, t), t → t + 1 a transition of F and v switched at t with W_{t+1}(v) = W_t(v), (Lemma NEW-BOUND, Corollaries RUN-WCH and REP-WCH) |F| ≤ m_E + Σ_e d_E(e)·WCH_F(e) + TIE_F and REP_F ≤ Σ_e d_E(e)·WCH_F(e) + TIE_F; (Lemma SIL-Z, Corollary SC-GXC) on every λ-run R, SIL_R ≤ GXC_R + NC_R + NT_R ≤ (B_R + 1)·max_P GXC_P + NC_R + NT_R (P over the phases inside R), where a GXC event is a pair (v, t) with v Even switched at t, τ_{t+1} = τ_t, λ_Ξ the same at t and t + 1, v ∈ Z_t, Ξ_{t+1}(v) ▷ Ξ_t(v) and W_{t+1}(v) ⊴ W_t(v), GXC_X the GXC events with t, t + 1 in X, and NC_R (NT_R) the class-S re-entries j − 1 → j of R at which the re-entering vertex is its own Ξ-cycle node at j − 1 or j (at which τ_j ≠ τ_{j−1}); (Lemma GXC-CLOSE, Theorem GXC-SPLIT) every phase P with first state a has GXC_P ≤ TIE_P + |Z_a| + Σ_v WCH^S4a_P(v) + FBO_P, TIE_P the pairs (v, t) with t → t + 1 an in-phase S4a transition of P, v switched at t and W_{t+1}(v) = W_t(v), FBO_P the GXC events of P at in-phase fallbacks with v ∈ Z_{t+1}; (Lemma LEVEL-MON, Corollaries DROP-PAID, FBO-R56, FBO-SPLIT, ZF-SPLIT) with LEV_t(v), for v ∈ Z_t, the position of the first coordinate at which Ξ_t(v) and W_t(v) differ in the coordinate sequence (reward of the cycle node; for each rank r from n − 1 down to 0, +1, −1 or 0 as the vertex of rank r is in the path set with even priority, with odd priority, or not; length, negated when the cycle node has even priority) in which the SPEC S1 order is lexicographic, LEV_{t′}(v) ≥ LEV_t(v) for states t < t′ of a phase P with v ∈ Z_t ∩ Z_{t′} and no S4a transition between them changing W(v), the transitions k → k + 1 of P that are not S4a transitions changing W(v) and have v ∈ Z_k ∩ Z_{k+1} and LEV_{k+1}(v) > LEV_k(v) number at most (n + 1)(1 + WCH^S4a_P(v)) (DROP_P(v)), FBO_P ≤ n_E(1 + (n − 1)(2 + ρ_P)) and FBO_P ≤ Σ_v DROP_P(v) + FBOS_P, and ZF_P ≤ NZ_P + Σ_v DROP_P(v) + ZFS_P, FBOS_P the FBO events of P with LEV_{t+1}(v) = LEV_t(v), NZ_P the Z-flat in-phase fallbacks k → k + 1 of P all of whose switched Even vertices are their own Ξ-cycle node at k or k + 1, and ZFS_P the other Z-flat in-phase fallbacks of P at which every switched Even vertex that is its own Ξ-cycle node at neither state keeps LEV; and (Theorem WCH-RED, Corollary WCH-ONE) if, for a function w : ℕ → ℕ, every τ-stretch S of every run on games with n vertices has, for every vertex e, at most w(n) S4a steps inside S changing W(e) (premise [P-WCHτ](w), not proved here), then REP* ≤ m_E·w(n) + TIE* (TIE* := max_F TIE_F), every W-run F has |F| ≤ m_E(1 + w(n)) + TIE_F, every phase P has f_P ≤ n(1 + w(n)) + ZF_P and ZF_P ≤ NZ_P + n(n + 1)(1 + w(n)) + ZFS_P, GXC_P ≤ TIE_P + n(1 + w(n)) + FBO_P and FBO_P ≤ n(n + 1)(1 + w(n)) + FBOS_P; for the labelled VARIANT N5-LZC (N5 with S4a's output σ* replaced by σ′, which, with W* the [S1-val] valuation of the (σ*, τ_t)-plays, keeps σ_t(v) at every Even v whose W*(v) has length at least 1 and satisfies v ⊕ W*(σ_t v) = W*(v), and at every Even v with W*(v) = (v, ∅, 0) for which W*(σ_t v) has cycle node v and empty path set, and takes σ*(v) at every other Even v; nothing transfers to N5), (Lemma LZ-OPT, Theorem LZ-STRICT, Corollaries RUN-WCH_LZ, REP-WCH_LZ) the (σ′, τ_t)-plays have valuation W*, every Even vertex switched at an S4a step strictly raises its W-value read with τ_t, so TIE_F = TT_F = 0, |F| ≤ m_E + Σ_e d_E(e)·WCH_F(e) and REP_F ≤ Σ_e d_E(e)·WCH_F(e) for every W-run F of N5-LZC, and (Corollary LZ-NOSIL, under ASSUMPTION OPT-ONLY that RESULTS R90 Fact B and (a) (ii), (b), (c), (d) hold verbatim for N5-LZC runs) N5-LZC has no class-S re-entry (2026-10-30) — a REDUCTION (per-vertex W-changes per τ-stretch ([P-WCHτ]), TIE*, NZ_P, ZFS_P, FBOS_P, NC_R, NT_R, ρ_P and B_R are not bounded here; G-N5-TIME stays open; not M3, not a step-4 pass, not a TARGET.md claim), CHECKER PASS (docs/checker/C103.md, checker PENDING)
- Object (L-NEW successor 37, Opus 5.5, D14 / D18, Lead reading L40; frozen, unchanged during review): packet P-N5-WCH,
  docs/new/P-N5-WCH-box79.md, sha1 31caa72e5265b7373218ce64e38d253112189506, 550 lines (l-new freeze 2ad78f51646684a82e18b02f7ccf7f0d382a7984,
  2026-10-30T09:10:32Z, the file's only commit; identical at l-new c930e26f and head 163342eb, at origin trunk 200a9e2e and at the local
  trunk head 19f0d2f5; first on trunk by bf6985bf, 09:57:42Z). Both referees measured the sha1 at 2ad78f51 (REFEREE l. 3-5; REFEREE-2 l.
  2-3). The Lead's freeze word is quoted at l. 2-5 («Lead 2026-10-30 (after 08:52Z): «TASK 1, PACKET: freeze ONE packet, P-N5-WCH, for
  both referees … Mark ASSUMPTION OPT-ONLY wherever it is used … Keep N5 and N5-LZC statements separate. Every symbol must be bound in the
  line file … Cite only landed RESULTS or the packet's own sections.»»). Status (l. 8-9): «REDUCTION only. No count named below as a
  residual is bounded here. G-N5-TIME stays OPEN. Not M3, not a step-4 pass, not a TARGET.md claim.» Two objects (l. 10-11): «N5 (SPEC
  S1-S5, §1-§6) and the labelled VARIANT N5-LZC (§7). Nothing in §7 transfers to N5, and nothing proved for N5 in §2-§6 is claimed for
  N5-LZC unless §7 proves it.» Sources (l. 6-7): working notes N5-SC-box70, N5-LZ-box72, N5-FBO-box73, N5-SBQ-box76, N5-RETWCH-box78,
  «unrefereed; THIS packet governs where they differ; none is cited as a proof»; not refereed here. Quote base l-new aefb71a3 (l. 9): the
  seven SPEC quotes are verbatim; four S1 tags are one line low (REFEREE WCH-N1, l. 11-13; REFEREE-2 N-2, l. 155-156; REFEREE-2 checked
  all «35 «» quotes» verbatim, l. 152-153), corrected by W1-1 and checked by experiments/new/box79/quotecheck.py (pinned «box 79»; re-run
  for this draft: 7 OK, «QUOTECHECK PASS»; with the original tags: 4 «NOT FOUND», «QUOTECHECK FAIL»). Sections: §0 what to sign (l.
  13-28), §1 setting, premises, definitions (l. 30-116), §2 Facts REW, LEX (l. 118-128), §3 Lemma TIE (l. 130-161), §4 NEW-BOUND, RET-WCH,
  RUN-WCH, REP-WCH (l. 163-213), §5 SIL-Z, SC-GXC, GXC-CLOSE, GXC-SPLIT, LEVEL-MON, DROP-PAID, FBO-R56, FBO-SPLIT, ZF-SPLIT (l. 215-271),
  §6 WCH-RED, WCH-ONE (l. 273-287), §7 N5-LZC (l. 289-330), §8 NOT to sign: trimmed items, DATA, READING, the lane's symbol test (l.
  332-550).
  The RESULTS line, history. (1) The frozen line docs/new/P-N5-WCH-box79-line.txt (l-new 2ad78f51), sha1
  9ac6fdba5ca5910a4585babff5938a0d8d107a78, the line both referees reviewed (REFEREE l. 4; REFEREE-2 l. 2-3). Verdicts on it: REFEREE
  «MATCHES §2-§7 and claims nothing more; my strict symbol test finds no free symbol (§10)» (l. 35), with one precision (l. 127-128: «NZ_P
  uses «at k or k + 1» with k bound only through ZF_P's gloss … it reads correctly»); REFEREE-2 «MATCHES §2-§7 | no REQUIRED fix;
  precision L-1 to L-4 (§3)» (l. 31). §Cs: REFEREE §C l. 55-56 «Joint position on the line: MATCHES, no REQUIRED fix. Precisions for W1:
  L-1 (bind k inside NZ_P's clause), L-2 (declare w : ℕ → ℕ), L-3 (optional), L-4 (cite R84 (a)).»; REFEREE-2 §C l. 23 «agree on MATCHES;
  precisions C.4». (2) W1 (fixes W1-3, l. 19-38): docs/new/P-N5-WCH-box79-line-W1.txt (l-new c930e26f), sha1
  00f9e375c448153f19b7620037a2723f6d10a0b1 = 9ac6fdba + exactly four changes: «R84 (a) (Fact DELTA)» added to the premises (L-4); «k → k
  + 1» bound inside NZ_P's clause (L-1); «for a function w : ℕ → ℕ» (L-2); σ′ defined directly (L-3). Word diff re-measured for this draft
  three ways: those changes, nothing else (to check (2)). REFEREE §C l. 64 «MATCHES (Opus 5.5, D15).»; REFEREE-2 §C.6 l. 71 «MATCHES (Opus
  5.5, D15).» W1 supersedes 9ac6fdba; the title is W1 verbatim, with its own date. No E-item and no REQUIRED fix was raised on either
  version by either referee; L-1..L-4 are precisions (REFEREE-2 l. 145-146: «None is required: k's clause-local meaning is unambiguous, w is
  fixed by «[P-WCHτ](w)», σ′ is pinned by «in the sense of Lemma TIE's two forms», and Fact DELTA is landed.»).
  Setting (packet §1, l. 30-116): N5 = SPEC S1-S5 (FIX 1-4); G = (V, E, Ω, owner), n = |V|; m_E the edges leaving Even vertices, n_E the
  Even vertices, d_E(e) := |{v Even : (v, e) ∈ E}|, Σ_e d_E(e) = m_E; a run is the sequence of states (σ_t, τ_t), a TRANSITION is t → t +
  1; [S1-rank], [S1-val], [S1-ord], [S1-Xi], [S2], [S4a], [S4c] quoted (tags corrected by W1-1); [R15], [F1], [V1], [V2], [⊕] quoted; the
  symbols of RESULTS R90 (W^τ_t, W_t, λ_W, H_t, S4a STEP, BOUNDARY, Fact B, τ*-PIECE, B_R, the classes of R90 (e), SIL_R), of R89
  (τ-STRETCH, W-RUN; |F| := its transitions), of R88 (f) / R90 (g) (late adoption, FIRST, REPEAT, REP_F, REP*), of R91 (PHASE, in-phase,
  τ-fixed Even fallback, Z_t, WCH^S4a_P(v), f_P, ZF_P and its lemmas (a), (b), (c), (h), (i), (k), (m), quoted), of R90 (a) (ii), (b), (c),
  (d) (quoted) and R56 (FB-RED, ρ_P). Packet definitions (l. 94-116): TIE EVENT, TIE_X, TIE*; RETURN, its LEAVE, RET_F(v, e), WCH_F(e),
  TT_F(v, e); GXC EVENT (box 70), GXC_P, GXC_R; CL_P, FBO_P; NC_R, NT_R; GAP LEVEL LEV_t(v); DROP_P(v); FBOS_P; NZ_P, ZFS_P; WCH_S(e);
  PREMISE [P-WCHτ](w) («A premise; not proved here.»). Standing premise (l. 50-51): «the standing SPEC premise of RESULTS R57 (1E-N3: S1's
  procedure realises the pointwise optimum); for S4a, σ_new is the POINTWISE OPTIMUM of the one-player arena H_t (RESULTS R90 (a) (i),
  OPT-OFF (i)).» §1 cells: REFEREE «CHECKED; standing premise named (R57 1E-N3, R90 (a) (i))» (l. 20); REFEREE-2 has no §1 row (its l. 5-9
  list the landed sources it re-read).
  DEFINITION (not a claim): §7.1 (l. 290-298), N5-LZC := N5 except in S4a: with σ* := [S4a]'s σ_new and W* := val(σ*, τ_t), σ′(v) :=
  σ_t(v) «if ℓ(W*(v)) ≥ 1 and v ⊕ W*(σ_t v) = W*(v)», σ′(v) := σ_t(v) «if W*(v) = (v, ∅, 0), and W*(σ_t v) has cycle node v and empty
  path set», σ′(v) := σ*(v) otherwise; σ_new := σ′; S4b, S4c (on σ′), S4d, S5 unchanged; «the §1 definitions … are read verbatim on
  N5-LZC's states»; premise «the standing SPEC premise for σ* (R57 1E-N3: σ* is the pointwise optimum of H_t)». REFEREE-2's row 7.1-7.4
  names «definition» among its SIGNED items (l. 28); REFEREE's row (l. 31) names the lemmas only. Recorded here as a definition. W1's L-3
  inlines it; both W1 lines check that the inlined rule equals §7.1 (REFEREE §C l. 64: «equals §7.1's three cases verbatim in content»;
  REFEREE-2 §C l. 77: «These are §7.1's two keep rules verbatim.»).
- Claims signed (both referees "(Opus 5.5, D15)": REFEREE successor 19, REFEREE-2 successor 22). Each item (a)-(l) is SIGNED in both
  verdict tables (REFEREE "## Verdicts" l. 18-35 of R-N5-WCH.md; REFEREE-2 "## 1. Verdict table" l. 16-32 of R2-N5-WCH.md) and «SIGNED by
  both» / «agree» in both §Cs (REFEREE §C table l. 8-20; REFEREE-2 §C C.1 l. 8-23), in the frozen wording, read with W1-1 (tags) and W1-2
  (case-split wording; «the proofs are unchanged», fixes l. 15, l. 17). Items (a)-(j) are about N5 on every game; (k), (l) are about the
  labelled VARIANT N5-LZC only. Premises LANDED (as line W1 names them): SPEC S1 ([S1-rank], [S1-val], [S1-ord], [S1-Xi]), S2, S4a, S4c;
  RESULTS R15 (a), (d); R17 (a) (F1); R56 (FB-RED); R84 (a) Fact DELTA; R86 (λ-run); R88 (f) and R90 (g) (late adoption, REPEAT, REP_F);
  R89 (τ-stretch, W-run); R90 (a)-(e), (g) and Fact B; R91 (a)-(c), (h), (i), (k), (m); R38 (a) (phase). Standing premise: RESULTS R57's
  SPEC premise as quoted under Object. The code's match to SPEC is DATA (R15 G-N5T-1). No item uses a count.
  (a) Fact REW (R1, R2), Fact LEX and its Consequence COMMON PREFIX (§2.1, l. 119-128; game-general): "rew is injective. (R1) If u is even
      (Ω) and more relevant than x, then rew(u) > rew(x). (R2) If x is odd, every u less relevant than x has rew(u) > rew(x)."; for x = (c,
      P, ℓ), CS(x) := (rew(c); s_{n−1}, …, s_0; ℓ̂) (s_r ∈ {0, +1, −1} by membership and parity of the vertex of rank r; ℓ̂ := ℓ if Ω(c) is
      odd, −ℓ if even): "x ◁ y iff CS(x) < CS(y) lexicographically"; COMMON PREFIX: "if x ⊴ z ⊴ y and CS(x), CS(y) agree on their first L
      coordinates, so does CS(z) with both." Cells: REFEREE «SIGNED» (l. 21); REFEREE-2 «SIGNED», «none» (l. 18; l. 40: «Checked mechanically:
      CS order = SPEC key order on 0 of the sampled pairs failing (§4).»).
  (b) Lemma TIE (§3, l. 130-161), with W1-2: at an S4a step t → t + 1, τ := τ_t, σ⁺ ANY pointwise-optimal Even strategy of H_t against τ,
      W′ := val(σ⁺, τ), v Even with d := σ_t(v) ≠ σ⁺(v) and W′(v) = W_t(v): "(a) if v is not its own W′-cycle node: v ⊕ W′(d) = W′(v), and
      d's σ⁺-path to its cycle node avoids v; (b) if v is its own W′-cycle node: W′(d) has cycle node v and empty path set." W1-2 (l.
      14-15): read (a2) as «π reaches its cycle node c* before v» and (a3) as «π reaches v before its cycle node c*». Cells: REFEREE
      «SIGNED (cases (a1)-(a3), (b) re-derived; wording note WCH-N2)» (l. 22); REFEREE-2 «SIGNED», «none; N-1: the case split (a2) / (a3)
      must be read as «v reached after / before c* on π» (wording)» (l. 19).
  (c) Lemma NEW-BOUND (§4.1, l. 164-169): "For every W-run F: |F| ≤ m_E + Σ_{(v, e) ∈ E, v Even} RET_F(v, e)." Cells: REFEREE «SIGNED» (l.
      23); REFEREE-2 «SIGNED», «none» (l. 20).
  (d) Theorem RET-WCH (§4.2, l. 171-203), with W1-2: "For every W-run F, Even v and successor e: RET_F(v, e) ≤ WCH_F(e) + TT_F(v, e). More
      precisely, every return u of v to e whose leave k has W_{k+1}(v) ≠ W_k(v) has a transition s ∈ [k, u] at which W(e) changes; the
      others are charged to their leave k, a TT_F(v, e) transition." (Premises [F1], [V1], [V2], W-MON (R91 (b)), λ_W constant on F; Step
      1 tie-leave, Step 2 (i)-(iii), distinctness.) W1-2 (l. 16-17): Step 2 (ii) «π reaches the cycle node c before v», (iii) «π reaches v
      before the cycle node c». Cells: REFEREE «SIGNED (Steps 1-2, (i)-(iii), the cycle-node exclusion, distinctness re-derived; WCH-N2)»
      (l. 24); REFEREE-2 «SIGNED», «none; N-1 again for Step 2 (ii) / (iii)» (l. 21).
  (e) Corollaries RUN-WCH and REP-WCH (§4.3, l. 205-213): "For every W-run F: (RUN-WCH) |F| ≤ m_E + Σ_e d_E(e)·WCH_F(e) + TIE_F; (REP-WCH)
      REP_F ≤ Σ_e d_E(e)·WCH_F(e) + TIE_F; hence REP* ≤ max_F Σ_e d_E(e)·WCH_F(e) + TIE*." Cells: REFEREE «SIGNED; REP-WCH needs only
      RET-WCH and R90 (g)'s definitions, NOT FW-R*′ (§4)» (l. 25); REFEREE-2 «SIGNED», «none; REP-WCH uses only R90 (g)'s definitions and
      RET-WCH, not FW-R*′ (N-3)» (l. 22).
  (f) Lemma SIL-Z (a)-(c) and Corollary SC-GXC (§5.1, l. 216-239): for a class-S re-entry j − 1 → j of v into c in the λ-run R (R90 (e)),
      q its smallest anchor, τ* := τ_{j−1}, W* := W^{τ*}, d := σ_{j−1}(v): "(a) W*_{j−1}(d) = W*_j(d) = W*_j(c) = W*_{j−1}(c), and W*_j(v) =
      W*_{j−1}(v); (b) if v is not its own Ξ-cycle node at j − 1: d ∈ Z_{j−1} and v ∈ Z_{j−1}; (c) if v is its own Ξ-cycle node neither at
      j − 1 nor at j: Ξ_j(v) ▷ Ξ_{j−1}(v)."; SC-GXC: "For every λ-run R: SIL_R ≤ GXC_R + NC_R + NT_R, and GXC_R ≤ Σ_{phases P ⊆ R} GXC_P,
      with at most B_R + 1 phases inside R." Cells: REFEREE «SIGNED; uses only landed R90 (a) (ii), (b), (c), (d), Fact B, R91 (a), R15,
      [S2], [S4a], [V1], [V2] (§5)» (l. 26); REFEREE-2 «SIGNED», «none; every premise is landed (R90 (a) (ii), (b)-(e), R91 (a), R15, SPEC
      S2, S4a, [V1], [V2])» (l. 23).
  (g) Lemma GXC-CLOSE and Theorem GXC-SPLIT (§5.2, l. 241-250): "For every phase P with first state a: CL_P ≤ |Z_a| + Σ_x WCH^S4a_P(x)."
      and "For every phase P: GXC_P ≤ TIE_P + CL_P + FBO_P ≤ TIE_P + |Z_a| + Σ_x WCH^S4a_P(x) + FBO_P." Cells: REFEREE «SIGNED» (l. 27);
      REFEREE-2 «SIGNED», «none» (l. 24).
  (h) Lemma LEVEL-MON and Corollary DROP-PAID (§5.3, l. 252-262): "Let P be a phase, v a vertex, t < t′ states of P with v ∈ Z_t ∩ Z_{t′},
      and suppose no transition s → s + 1 with t ≤ s < t′ is an S4a step changing W(v). Then LEV_{t′}(v) ≥ LEV_t(v)."; "For every phase P
      and vertex v: DROP_P(v) ≤ (n + 1)(1 + WCH^S4a_P(v))." Cells: REFEREE «SIGNED» (l. 28); REFEREE-2 «SIGNED», «none» (l. 25).
  (i) Corollaries FBO-R56, FBO-SPLIT, ZF-SPLIT (§5.4, l. 264-271): "FBO_P ≤ n_E·f_P ≤ n_E·(1 + (n − 1)(2 + ρ_P))"; "FBO_P ≤ Σ_v DROP_P(v)
      + FBOS_P"; "ZF_P ≤ NZ_P + Σ_v DROP_P(v) + ZFS_P." Cells: REFEREE «SIGNED» (l. 29); REFEREE-2 «SIGNED», «none» (l. 26).
  (j) Theorem WCH-RED (W), (G), (X), (S) and Corollary WCH-ONE (§6, l. 273-287): (W) the bounds of (e); (G) "f_P ≤ n + Σ_v WCH^S4a_P(v) +
      ZF_P (R91 GAP-RED) and ZF_P ≤ NZ_P + (n + 1)·Σ_v (1 + WCH^S4a_P(v)) + ZFS_P"; (X) "GXC_P ≤ TIE_P + |Z_a| + Σ_v WCH^S4a_P(v) + FBO_P
      …, with FBO_P ≤ n_E(1 + (n − 1)(2 + ρ_P)) and FBO_P ≤ (n + 1)·Σ_v (1 + WCH^S4a_P(v)) + FBOS_P"; (S) "SIL_R ≤ (B_R + 1)·max_{P ⊆ R}
      GXC_P + NC_R + NT_R". WCH-ONE: "under [P-WCHτ](w), with w := w(n): REP* ≤ m_E·w + TIE*, and |F| ≤ m_E·(1 + w) + TIE_F for every
      W-run F; f_P ≤ n(1 + w) + ZF_P and ZF_P ≤ NZ_P + n(n + 1)(1 + w) + ZFS_P for every phase P; GXC_P ≤ TIE_P + n(1 + w) + FBO_P and FBO_P
      ≤ n(n + 1)(1 + w) + FBOS_P." Cells: REFEREE «SIGNED (each displayed inequality re-derived)» (l. 30); REFEREE-2 «SIGNED (composition
      and arithmetic checked)», «none» (l. 27).
  (k) N5-LZC (VARIANT; §7.2-§7.4, l. 299-320): Lemma LZ-OPT "val(σ′, τ_t) = W*. Hence σ′ is a pointwise optimum of H_t"; Lemma W-MON_LZ
      "At an S4a step t → t + 1 of N5-LZC, W^{τ_t}_{t+1} ⊵ W^{τ_t}_t pointwise"; Theorem LZ-STRICT "At an S4a step t → t + 1 of N5-LZC,
      every switched Even v has W^{τ_t}_{t+1}(v) ▷ W^{τ_t}_t(v)" («Hence in N5-LZC: TIE_X ≡ 0 and TT_F ≡ 0», l. 315); Corollaries
      RUN-WCH_LZ / REP-WCH_LZ "For every W-run F of N5-LZC: |F| ≤ m_E + Σ_e d_E(e)·WCH_F(e) ≤ m_E·(1 + max_e WCH_F(e)), and REP_F ≤ Σ_e
      d_E(e)·WCH_F(e)." («No fleet lemma is transferred: every premise is re-proved for N5-LZC here», l. 320.) Cells: REFEREE «SIGNED, for
      the VARIANT only» (l. 31); REFEREE-2 «SIGNED (VARIANT; nothing transfers to N5)», «none» (l. 28).
  (l) Corollary LZ-NOSIL AS THE IMPLICATION (§7.5, l. 321-330): "Under OPT-ONLY, N5-LZC has no class-S re-entry (R90 (e) classes read on
      N5-LZC)", ASSUMPTION OPT-ONLY := «RESULTS R90 Fact B and (a) (ii), (b), (c) and (d) hold verbatim for N5-LZC runs». Cells: REFEREE
      «SIGNED; and ASSUMPTION OPT-ONLY CHECKED TRUE (§7) …» (l. 32); REFEREE-2 «SIGNED as the implication; OPT-ONLY CHECKED: it holds (§2.7
      below)», «N-4» (l. 29). The entry signs the implication only; the check of OPT-ONLY is the joint finding below.
  N5-LZC IS A LABELLED VARIANT, NOT N5. Nothing in (k) or (l) transfers to N5 without proof, and nothing in (a)-(j) is claimed for N5-LZC
  except what (k) and (l) prove (packet l. 10-11; §7.5 l. 330 «Not claimed: anything about class C, phases, GXC, ZF, fallbacks or T for
  N5-LZC»; REFEREE-2 l. 13 «N5 (§2-§6) and the VARIANT N5-LZC (§7) are separate objects; I checked them separately.»). The N5 part never
  uses OPT-ONLY or any §7 statement (REFEREE l. 33, l. 92; REFEREE-2 l. 113; REFEREE §C l. 19 and REFEREE-2 §C l. 22: «not used»).
  Gap maps: REFEREE §C l. 21: «The verdicts are identical and the gap map is EMPTY: neither referee lists a gap, and nothing is false.»;
  REFEREE-2 §C C.2 l. 26-27: «Proof gaps: NONE in either report. Joint gap map: EMPTY.» «Required fixes: NONE in either report.» REFEREE
  l. 36: «No gap. Nothing FALSE. Notes WCH-N1..N4.»; REFEREE-2 l. 34: «No gap. Nothing FALSE. No REQUIRED fix.»
  The RESULTS line (W1) claims less than the packet: it states Lemma TIE without «d's σ⁺-path … avoids v» (REFEREE-2 l. 141: «a weakening
  that is allowed»); RET-WCH without its «more precisely» form; NEW-BOUND only through RUN-WCH; REP-WCH without «REP* ≤ max_F …»; SIL-Z
  only through SC-GXC's chain; GXC-CLOSE only through GXC-SPLIT; Fact LEX only as «the coordinate sequence … in which the SPEC S1 order is
  lexicographic» inside LEV's definition (Fact REW and COMMON PREFIX are signed items behind it); WCH-RED's (G) first half (landed R91
  GAP-RED) not restated; W-MON_LZ and «σ′ is a pointwise optimum of H_t» not stated; RUN-WCH_LZ without «≤ m_E·(1 + max_e WCH_F(e))».
  Every clause it states is one of (a)-(l). W1 changes no clause's claim: L-1, L-2 bind symbols, L-3 inlines §7.1, L-4 adds a premise
  label (REFEREE-2 §C l. 78: «Every inequality is token-identical.»).
- Fixes (docs/new/P-N5-WCH-fixes-box79.md, L-NEW successor 37, APPEND-ONLY, «Written 2026-10-30 from 10:35Z (date -u)» (l. 4); one
  commit: l-new c930e26fcdd66ffaf19e3c6d081b52d08a9037f3, 2026-10-30T10:34:06Z, sha1 8377a1b8baa0e53cb4df509d1aa91f427628983d, 46 lines,
  = l-new head 163342eb = origin trunk 200a9e2e; first on trunk by 05f6c315 (10:54:07Z); the last commit touching the file). The same
  commit adds the W1 line file, experiments/new/box79/quotecheck.py (19 lines, sha1 59bdfca06a7f0ee96dd79d9a3bf75426cdc8aba5),
  symtest.py's W1 table (+6/−5) and symtest_W1.out (191 lines, sha1 676b0273291319ba0dc17a719a43c8fbfb8ada70), and points check.sh «box
  79» at W1 with the quote check. Header (l. 2-4): «The frozen packet … is NOT edited; where this file and the packet differ, this file
  governs. Both referees: every item SIGNED, no gap, nothing false (Lead 10:32Z).» Classes (l. 4): «WORDING / TAGS / LINE PRECISION /
  FINDING / DATA». Each item, with its class and the referees' words:
  - W1-1 (TAGS) (l. 6-11) = REFEREE WCH-N1 = REFEREE-2 N-2: «[S1-rank] [Q SPEC:27] (packet says 26); [S1-val] [Q SPEC:28-29] (27-28);
    [S1-ord] [Q SPEC:30-31] (29-30); [S1-Xi] [Q SPEC:32] (31).» Quote check added and pinned: «7 / 7 OK, QUOTECHECK PASS; with the
    packet's original tags it reports 4 NOT FOUND (the check bites).» Re-run for this draft: both (Object). REFEREE l. 95-96: «Fix the tags,
    or quote at 7039eb524 … Add a quote check to «box 79».»; REFEREE-2 §C.6 l. 80: «It includes the SPEC quote check (W1-1 fixes the four
    tags)».
  - W1-2 (WORDING) (l. 13-17) = WCH-N2 = N-1: the case split by the position of v on π in Lemma TIE (a1)-(a3) and RET-WCH Step 2
    (i)-(iii): «The three cases are exhaustive and the proofs are unchanged.» (l. 15); «Proofs unchanged.» (l. 17). REFEREE l. 50: «so it is
    wording, not a gap»; REFEREE-2 l. 191: «One clause each in a fixes file.» Joint: REFEREE §C l. 46; REFEREE-2 §C l. 49 («the same
    configuration has now been mis-split twice»). Not re-read by either referee after c930e26f (to check (10) (vii)).
  - W1-3 (LINE PRECISION) (l. 19-38) = REFEREE-2 L-1..L-4 (L-1 = REFEREE's §10 precision): the line W1, «Nothing else changed.» (l. 35);
    symtest re-run «W1 186 symbols, 0 failures, SYMTEST PASS»; «Under the updated table the OLD line 9ac6fdba fails 4 (NZ_P, W*, σ′: their
    binding phrases were reworded in W1; w: undeclared, = L-2).» (l. 37-38). Both W1 lines: MATCHES (to check (3)). THE TITLE.
  - W1-4 (FINDING) (l. 40-42) = WCH-N3 = N-4: «Both referees checked ASSUMPTION OPT-ONLY against R90's proofs and find it TRUE, so
    Corollary LZ-NOSIL holds (REFEREE 19 WCH-N3: «OPT-ONLY is true (§7); LZ-NOSIL can be stated without the assumption»). Recorded only;
    the signed text is not changed.» (the quote of WCH-N3 is REFEREE l. 98, verbatim). See «Joint referee finding».
  - W1-5 (DATA) (l. 44-46) = WCH-N4: «NC_R = NT_R = 0 on the referee's whole corpus; SIL-Z (b)'s own-Ξ-cycle exclusion and the NT term are
    never exercised by data. Recorded: NC_R and NT_R are residuals with no instance; the statements are unaffected.» REFEREE l. 99-100;
    REFEREE-2 §C l. 51: «my data also has NC 0, NT 0 on 1,131 runs, but I did not record it as a note … I MISSED it as a note; accepted».
  No fix changes a signed statement: W1-1 tags only (text verbatim), W1-2 wording («proofs unchanged»), W1-3 the line only, W1-4 «the
  signed text is not changed», W1-5 «the statements are unaffected». REFEREE-2 §C.6 l. 78: «Every inequality is token-identical.»
- Not signed: §1 (setting and definitions; REFEREE «CHECKED»); the §7.1 Definition of N5-LZC (a definition: Object); ASSUMPTION OPT-ONLY
  (checked TRUE by both: the joint finding below, not a claim of the line and not a landed lemma); §8.1 the trimmed items (TXC-SRC /
  TXC-RHO, FIX-DEPTH / FIXD-MON / PHASE-RED, LZ-RUN, N5-LZC output correctness, GXC-CLOSE / FBO for N5-LZC: l. 333-344); §8.2 and §8.4
  DATA (Data below); §8.3 READING (l. 350-352); §8.5 the lane's symbol test of the frozen line (l. 360-550; superseded by W1-3's re-run);
  the frozen line 9ac6fdba (history); the working notes box70, box72, box73, box76, box78 (l. 6-7). Lane work after the freeze, other than
  the fixes commit c930e26f, is not part of this entry: L-NEW boxes 80-83 (3aac0638, ab2a15b7, 163342eb and later), the FLAT-SRC box 79 of
  L-NEW successor 36 (c50a4985, 9555501d) and L-RED R131-R134.
- Joint referee finding (not a claim of the line): ASSUMPTION OPT-ONLY is TRUE for N5-LZC, so Corollary LZ-NOSIL holds outright for
  N5-LZC: N5-LZC has no class-S re-entry. Both referees checked it independently against the landed proofs of R90's object, before the
  §C. REFEREE d71d6e55, R-N5-WCH.md l. 32 (cell): «SIGNED; and ASSUMPTION OPT-ONLY CHECKED TRUE (§7): R90's proofs of Fact B, (a) (ii), (b),
  (c), (d) use S4a's σ_new only through OPT-OFF (i) (pointwise optimality), never through S1's tie-break»; l. 88-91: «… No step uses S1's
  tie-break or the identity σ_new = S1's output. So OPT-ONLY HOLDS for N5-LZC (given LZ-OPT), and LZ-NOSIL holds outright, not only under
  the assumption.»; WCH-N3, l. 98: «OPT-ONLY is true (§7); LZ-NOSIL can be stated without the assumption.» REFEREE §C 938537ed, §2 l. 30:
  «JOINT FINDING, signed by both.»; l. 33: «LZ-OPT supplies (i) for σ′, so OPT-ONLY holds, and LZ-NOSIL holds for N5-LZC without the
  assumption.»; l. 39-40: «Joint position: the line may keep «under ASSUMPTION OPT-ONLY …». The RESULTS entry should record that both
  referees checked OPT-ONLY and found it TRUE for N5-LZC, a referee finding about a VARIANT. It transfers nothing to N5.» REFEREE-2
  24f32388, R2-N5-WCH.md l. 29 (cell): «SIGNED as the implication; OPT-ONLY CHECKED: it holds (§2.7 below)»; l. 106-107: «OPT-OFF (ii)
  (Cases 1-3), W-MON′, W-SUCC and W-RETURN-G use (i) … Nowhere do they use the S1 procedure or its tie-break; only (i)'s own proof does.»;
  l. 111-112: «So OPT-ONLY holds for N5-LZC, and LZ-NOSIL holds without the assumption. I recommend the line keep the label as is: the
  assumption is discharged by this report, not by a landed proof.» REFEREE-2 §C 6ff5d18a, C.3 l. 35-36: «Joint status (Opus 5.5, D15):
  OPT-ONLY is DOUBLE-REFEREED TRUE, and LZ-NOSIL holds for N5-LZC without the assumption. This is a referee finding about a landed proof,
  not a new landed lemma.»; l. 42-43: «My recommendation is (a) unless the lane wants (b), because (a) changes nothing that was signed.
  Either way, nothing in N5 (§2-§6) depends on it.» Lead decision (a) (docs/agents/LEAD-STATE.md l. 2066, entry «10:54Z»: «the line keeps
  «under ASSUMPTION OPT-ONLY», the RESULTS body records the joint check»); both W1 lines confirm the label is unchanged (REFEREE §C l. 64;
  REFEREE-2 §C l. 78); the lane records it (W1-4). Status: a joint finding of both referees about a VARIANT, recorded in this body; the
  line still states LZ-NOSIL under the assumption, and this entry does not claim the unconditional form. It transfers nothing to N5.
- Referee strengthening (NOT part of this entry; remarks of one referee, remarks of both outside the verdict cells, readings):
  (i) The case split (WCH-N2 = N-1, W1-2): with the literal tail / cycle reading, the configuration «v on the cycle between π's entry and
  c*» would fall into (a2) / (ii), «whose argument then uses «π's path to c* avoids v», which is false there. This is the configuration of
  P-N5-GAP's G-GAP-1. The proofs of (a3) / (iii) cover it verbatim» (REFEREE l. 46-50); REFEREE-2 l. 189-191 the same; REFEREE-2 §C l. 49:
  «REFEREE's link to G-GAP-1 (R91) is right and worth recording: the same configuration has now been mis-split twice».
  (ii) REFEREE-2 l. 51 (TIE (a3)): «In (a3) the top u may be v itself (v ∈ X); the argument «u ∉ P(W(d))» covers that, since d's σ_t-path
  avoids v.» REFEREE-2 only.
  (iii) NC_R and NT_R are never exhibited (WCH-N4, W1-5): REFEREE MUT 5 (SIL-Z (b) at own-Ξ-cycle v) «never (NC = 0: WCH-N4)» (l. 116);
  REFEREE-2's data NC 0 / NT 0 (l. 173). The premises are used by the proofs, not exhibited by data (REFEREE l. 99-100).
  (iv) The lane's symbol test cannot see clause scope (REFEREE-2 N-5, l. 196-197; REFEREE §C l. 50 «agreed»; REFEREE-2 §C l. 56: «both
  found L-1 by hand; the tool did not»).
  (v) Self-corrections: REFEREE §C l. 54 (L-4): «Agreed, and I MISSED it.»; REFEREE-2 §C l. 51 (WCH-N4): «I MISSED it as a note».
  (vi) Controls that bite: REFEREE MUT 1 (RET-WCH without TT) 43, MUT 2 (GXC-SPLIT without TIE) 17, MUT 3 (LEVEL-MON across W(v)-changing
  S4a steps) 1,176, MUT 4 (ZF-SPLIT without DROP) 3; MUT 5 never (l. 115-116). REFEREE-2: «dropping the hypothesis, (a)'s conclusion fails
  at 56,743 of 57,628 switched vertices (X_TIE_noeq)» (l. 182); «read across an S4a W(v)-change, LEV decreases 26,107 times (X_LM_s4a)» (l.
  183). REFEREE-2 §C l. 58: «REFEREE's MUT 3 = my X_LM_s4a». DATA.
  (vii) [P-WCHτ]'s w in the data: «max WCH_S(e) = 48 on both engines (DATA only)» (REFEREE-2 l. 186). Not a bound; [P-WCHτ] is not proved.
  (viii) §8.3 READING (l. 351-352): «Every residual of §6 for N5 except NZ, ZFS, FBOS, NC, NT is a TIE count or a per-vertex W-change count;
  N5-LZC removes TIE outright. The one shared premise is [P-WCHτ]». Not signed.
- Honest limits: (i) A REDUCTION. The line bounds Even returns by W(e)-changes and tie-leaves, W-run lengths and REPEATs by per-vertex
  W-changes and TIE events, silent re-entries by GXC events, GXC events by TIE, gap exits and FBO events, and FBO events and Z-flat
  fallbacks by gap-level drops; no residual is bounded: per-vertex W-changes per τ-stretch ([P-WCHτ]), TIE*, NZ_P, ZFS_P, FBOS_P, NC_R,
  NT_R, ρ_P and B_R are not bounded here. [P-WCHτ] is a premise, «not proved here». Packet l. 8: «No count named below as a residual is
  bounded here. G-N5-TIME stays OPEN.»; REFEREE l. 14-15 and REFEREE-2 l. 12-13 say the same. (ii) N5-LZC is a labelled VARIANT: (k) and
  (l) are about N5-LZC only; nothing transfers to N5 without proof; N5-LZC's output correctness is not claimed here (§8.1 l. 340); LZ-NOSIL
  is the only §5-type statement made for it (§7.5 l. 330). (iii) LZ-NOSIL is signed as an implication under ASSUMPTION OPT-ONLY; both
  referees find OPT-ONLY TRUE (joint finding above), which is not a landed lemma and not a claim of the line. (iv) Standing premise: R57's
  SPEC premise (1E-N3; for S4a, the pointwise optimum of H_t, R90 (a) (i)), through [F1] in H_t, XW and W-MON; the code's match to SPEC is
  DATA (R15 G-N5T-1). (v) NC_R and NT_R are residuals with no instance in any data (W1-5). (vi) Counts are transitions and events, not bit
  operations; no running-time bound. (vii) Not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open.
- Data (DATA, not proof): pinned (packet §8.5 l. 366: «pinned in experiments/new/check.sh, "box 79"»; W1-1 and W1-3 re-point it).
  experiments/new/check.sh at 2ad78f51: sha1 06bef37c4ea802e0bb5f862e8e941d5f281af5b8, 406 lines, «box 79» WCH block l. 400-405 (symtest on
  the frozen line); at c930e26f: sha1 ca6a90473ae952c320c3cd9b88698e56a414b5b8, 424 lines, WCH block l. 400-405 (symtest on W1 and
  quotecheck.py; identical at l-new head 163342eb); l. 406-411 there are succ. 36's FLAT-SRC block (excluded). Files at c930e26f:
  box79/wchpk.py 69aec39906e4508de8fc6133c0d3e44272bd16de, box79/sumpk.py 84352914ecf6077d53e3433dc68b76a80f7b1849 (both unchanged since
  2ad78f51), box79/symtest.py 66cf16deb4820e15298dfceb8a51bf57dde5bf4b (7e952aaa… at 2ad78f51), box79/quotecheck.py
  59bdfca06a7f0ee96dd79d9a3bf75426cdc8aba5, box79/symtest_W1.out 676b0273291319ba0dc17a719a43c8fbfb8ada70, box79/symtest.out
  1005d72b0c0d9e3cf84debda9fbb4a11ca614dce, box79/wchpk_sbcg.txt c21025d135554bcd3d1168055e722ceed4db5759 (719 lines),
  box79/wchpk_alt.txt cd78ba4889f9650208d9faca50d13d61ac5130a7 (413 lines) (both unchanged since 2ad78f51), red/so/instances/tog6b_n32.pg
  705695a6cef3e0e4a6f168527c28362ce4db4000, docs/new/N5-ssi-global.md 66fde9ef1726602fc0a52ca8d6d6fe8cbbcf110e. Re-run for this draft from
  a `git archive` of each commit (experiments/ and docs/new/; `python3 -I`; outputs to scratch files; exit codes read): c930e26f l. 400-405
  under `set -euo pipefail`, 11:11:42Z by date -u (read before and after, same second): «WCHPK tog6b_n32.pg n 32 wruns 1 {'returns': 4,
  'paid-W': 3, 'TT': 1, 'TIE': 2} …», «WCHPK tog6b_n32.pg n 32 wruns 1 {'returns': 3, 'paid-W': 3, 'TIE': 0} …», «SYMTEST PASS»,
  «QUOTECHECK PASS», «box 79 WCH: … PASS», rc 0; 2ad78f51 l. 400-405 (frozen line), rc 0, «box 79 WCH: P-N5-WCH RET-WCH (TT form) on
  tog6b_n32 (N5 TT 1, N5-LZC TIE 0); line-file strict symbol test PASS», 11:12:02Z by date -u (read after). Single runs from the c930e26f
  archive (same session, not separately stamped): symtest on W1 «symbols 186, failures 0: []», «SYMTEST PASS», rc 0, output byte-identical
  to symtest_W1.out; symtest (W1 table) on 9ac6fdba «symbols 182, failures 4: ['NZ_P', 'W*', 'w', 'σ′']», «SYMTEST FAIL», rc 1 (= fixes
  l. 37-38); quotecheck 7 «OK», «QUOTECHECK PASS», rc 0; quotecheck with the tag map emptied (the packet's original tags) 4 «NOT FOUND»,
  «QUOTECHECK FAIL», rc 1 (= fixes l. 10-11).
  DATA OF RECORD (packet §8.2 l. 345-349 and the §8.4 table l. 353-359; corpus box59/sbcg.lst (719) + alt_all (413), N5 and N5-LZC; run
  «2026-10-30 09:00Z-09:02Z by date -u», l. 346): N5: games 1132, W-runs (holding a return) 1692, returns 6265, paid by a W(e)-change in
  [k, u] 6177, TT 88, UNPAID 0, RET-WCH violations 0, RUN-WCH violations 0, TIE events in W-runs 397, max returns per (F, edge) 17, max |F|
  / RUN-WCH bound 0.30; N5-LZC: 1132, 1658, 6100, 6100, 0, 0, 0, 0, 0, 17, 0.30. «TIE = 0 and TT = 0 on N5-LZC everywhere (LZ-STRICT).»
  (l. 358). Pins (l. 358-359): tog6b_n32 N5 returns 4, paid-W 3, TT 1, TIE 2; N5-LZC returns 3, paid-W 3, TIE 0. Re-summed for this draft
  (sumpk.py over the two files from the 2ad78f51 archive, 11:12:13Z by date -u, read after, rc 0): «games 1132 unparsed halves 0», «N5
  {'TIE': 397, 'returns': 6265, 'paid-W': 6177, 'wruns': 1692, 'TT': 88} max-ret-per-edge 17 max |F|/bound 0.3», «LZC {'TIE': 0,
  'returns': 6100, 'paid-W': 6100, 'wruns': 1658} max-ret-per-edge 17 max |F|/bound 0.3»: equal; UNPAID = returns − paid-W − TT = 0 on
  both (arithmetic). sumpk.py prints no violation columns, so «violations 0» is the packet's figure, not re-derived here. Fixes W1-5
  (l. 44-46): «NC_R = NT_R = 0 on the referee's whole corpus»; NC 0 / NT 0 also on REFEREE-2's 1,131 runs (l. 173; §C l. 51). Earlier
  figures from the working notes (§8.2 l. 347-349: «RET-WCH (TL form) 12365 returns, 0 unpaid (box 78)» etc.) are history, not data of
  record (RET-WCH's TL form is replaced by TT, §8.1 l. 342-343).
  REFEREE (successor 19; own docs/referee/scratch/wch_probe.py on rl_engine, «no lane code»; N5-LZC by replacing S4a's σ_new with the
  §7.1 keep rule; pinned l. 400-405 run in a clean `git worktree add --detach` at 2ad78f51: PASS, exit 0, l. 103-104): the lane's sbcg.lst
  ∪ alt_all, 719 distinct games, given start and S3, n ≤ 80 (84 larger skipped): 722 runs, 12,087 transitions (l. 108). N5: 0 violations of
  TIE (260 W-flat switches), NEW-BOUND, RET-WCH (2,656 returns: 2,612 W-paid in [k, u], 44 TT), RUN-WCH, REP-WCH (15 REPEATs), SIL-Z
  (a)-(c) and SC-GXC (42 class-S re-entries, all GXC events; NC 0, NT 0), GXC-CLOSE (CL 1,813), GXC-SPLIT (GXC 2,222), LEVEL-MON (190,139
  segment checks), DROP-PAID (3,303 drops), FBO-R56, FBO-SPLIT (FBO 211, FBOS 178), ZF-SPLIT (ZF 90 = NZ 42 + ZFS 39 + drops), GAP-RED
  (783 in-phase fallbacks) (l. 109-112). N5-LZC: «LZ-OPT exact at all 11,456 S4a computations, LZ-STRICT 0 violations, TIE = TT = 0,
  RET-WCH 2,552 returns all W-paid, class-S re-entries 0 (LZ-NOSIL), 0 violations» (l. 113-114). Pins reproduced independently (l.
  105-107).
  REFEREE-2 (successor 22; own docs/referee-2/R2-N5-WCH/wch_check.py: N5 on its lane's R2-N5-DUAL/dual_check.Runner, N5-LZC its own
  subclass with the keep rule coded from §7.1; «The lane's box79 / box78 scripts are NOT imported», l. 157-160; pinned «box 79» from its
  own extraction, set -euo pipefail, detached worktree at 2ad78f51, exit 0, l. 149-150; at c930e26f, §C l. 80): corpus = the lane's,
  «1,131 runs per engine» (l. 167-169; 319 start-less alt_all lines from S3; one invalid start file skipped). N5: 21,790 transitions,
  8,941 W-runs, returns 6,246, paid 6,158, TT 88, TIE (W-runs) 397, max returns per (F, edge) 17, class S 84, S not GXC 0, NC / NT 0 / 0,
  GXC 3,602, CL / FBO / FBOS 2,985 / 232 / 196, DROP 4,690, ZF / NZ / ZFS 112 / 59 / 44, REP* max 6, max WCH_S(e) 48; N5-LZC: 21,487
  transitions, 8,892 W-runs, returns 6,081, all paid, TT 0, TIE 0, class S 0, REP* max 6, max WCH_S(e) 48 (table l. 171-174); 0
  violations on every check, both engines (l. 169). «TT, TIE and the maximum equal mine exactly» (l. 178); LZ-OPT «at all 20,845 N5-LZC
  S4a steps» (l. 184). Run sets (REFEREE §C l. 22-27; REFEREE-2 §C C.5 l. 60-68): the absolute counts differ by run set only («class S is
  42 for me and 84 for REFEREE-2, which runs both starts on all games», REFEREE §C l. 27); «Both find 0 violations, NC = NT = 0, every
  class-S re-entry a GXC event, N5-LZC with TIE = TT = 0 and no class-S re-entry, and LZ-OPT exact at every S4a computation.» (REFEREE-2 §C
  l. 66-67). No signed statement uses any count.
- Signatures: REFEREE docs/referee/R-N5-WCH.md (report d71d6e55df04f1beb345a055ca026dc162ec9b5b, 2026-10-30T10:06:43Z, committed directly
  on claude/referee (file commit = branch commit), first on trunk by fb210b9e (10:21:07Z); sha1 ce349a4ecd3e180ab2f45ff128ba2513ba2c072a,
  135 lines, unchanged since (= referee head b7b0d54f = local trunk head); successor 19): §1 CHECKED; every PROVED item of §2-§7 SIGNED,
  LZ-NOSIL as the implication; «No gap. Nothing FALSE. Notes WCH-N1..N4.» (l. 36). §C docs/referee/R-N5-WCH-C.md
  (938537edabf19f127939682982f1747173b82276, 2026-10-30T10:33:03Z, `git diff --numstat d71d6e55 938537ed`: +62/−0; sha1
  d2431cfa96075aa68eadca0eba8d3b4883262354 there, 62 lines; first on trunk by 5c8b11e2, 10:54:08Z): verdicts identical, gap map EMPTY
  (l. 21), OPT-ONLY a joint finding (§2 l. 29-40); W1 line b7b0d54f6eb1caa57c1e6af660f479ec234e53f0 (2026-10-30T10:55:21Z, +2/−0; sha1
  7418be9f5ac66bc7bc824bf32e9830773ad1d429, 64 lines, = origin referee head = the last commit touching the file; merged into the LOCAL
  trunk by e707d3df (11:13:52Z), not on origin trunk 200a9e2e at the 11:14:11Z fetch): «MATCHES (Opus 5.5, D15).» (l. 64). REFEREE-2
  docs/referee-2/R2-N5-WCH.md (report 24f32388969e1119dcb7f33ebd56705346b665f0, 2026-10-30T10:09:09Z, committed directly on
  claude/referee-2 (its parent 9f4d5821 is a Lead trunk commit), first on trunk by 7a003a9b (10:32:21Z); sha1
  185416fe118bfbc27c2f6916b0095abdb29a363e, 207 lines (= REFEREE §C l. 4's «sha1 185416fe…, 207 lines»), unchanged since; successor 22):
  every item of §2-§7 SIGNED; «No gap. Nothing FALSE. No REQUIRED fix.» (l. 34). §C docs/referee-2/R2-N5-WCH-C.md
  (6ff5d18afae42784f7fa904f9adaf1a1143431cd, 2026-10-30T10:33:04Z, +78/−0; its parent e4eaaa99 is a merge of trunk into the branch; sha1
  7cba08f4a44ba6b10c467c2314bd376b57f332aa there, 78 lines; first on trunk by 51f1bdbf, 10:54:09Z): C.1 «agree» on every row, C.2 «Joint
  gap map: EMPTY.», C.3 OPT-ONLY «DOUBLE-REFEREED TRUE»; §C.6 14bfa3cc12f3c35fd6c8a613b988cc740692cee7 (2026-10-30T10:54:44Z, +12/−0, l.
  70-81; its parent 0f2ca021 is a merge of trunk into the branch; sha1 7d43753186127b4bd409f388fe7ee0363ce80310, 90 lines, = origin
  referee-2 head = the last commit touching the file; merged into the LOCAL trunk by a7ed06f2 (11:13:53Z), not on origin trunk 200a9e2e at
  the 11:14:11Z fetch): «MATCHES (Opus 5.5, D15).» (l. 71). Its DONE / FINDINGS / NEEDS (l. 82-90) were not revised for W1 (to check (3)).
  INDEPENDENCE: REFEREE l. 7: «Independence: no docs/referee-2/ file for this packet opened.»; REFEREE §C l. 3-4: its report «pushed BEFORE
  I opened REFEREE-2's», REFEREE-2's report «opened 10:32Z after the Lead's word». REFEREE-2 l. 3-5: «Independence: written before opening
  any docs/referee/ file for this packet; the names-only count of «wch» in docs/referee/ was 0 at the start (10:0xZ).»; REFEREE-2 §C l.
  3-4: its report «pushed before any docs/referee/ file for this packet was opened», REFEREE's «opened after the Lead's word at 10:32Z».
  No review imported lane code (REFEREE l. 105 «no lane code»; REFEREE-2 l. 160); the lane's scripts ran only as the pinned block.
  §C (both): verdicts identical (REFEREE §C l. 21; REFEREE-2 §C C.2 l. 26); no disagreement in substance; one difference of presentation on
  OPT-ONLY (REFEREE §C l. 35-37: REFEREE-2 «recommends that the line keep the label, discharged by the reports»; REFEREE «wrote that the
  label "can be discharged"»), resolved by Lead decision (a). Notes map (REFEREE §C §3 l. 42-56; REFEREE-2 §C C.4 l. 45-58): WCH-N1 = N-2,
  WCH-N2 = N-1, WCH-N3 = N-4, REFEREE's §10 precision = L-1, REFEREE's §3-4 watch item = N-3; REFEREE only WCH-N4; REFEREE-2 only N-5,
  L-2, L-3, L-4.
- TARGET.md diff: «n the number of vertices of the game» is TARGET.md §1 l. 8's n («n = |V|, m = |E|»); m_E ≤ m; n_E ≤ n. «w : ℕ → ℕ» and
  [P-WCHτ](w) are a premise of this entry, not a TARGET.md notion. Not a claim of TARGET.md section 1 or §2 (lemmas and inequalities about
  N5 runs on every game and about a labelled VARIANT N5-LZC; a REDUCTION of returns, W-run lengths, REPEATs, silent re-entries, GXC events,
  FBO events and Z-flat fallbacks to residual counts and the premise [P-WCHτ], none bounded; no bound on a run, no running-time bound, no
  algorithm claim). GAPS G-N5-TIME: open.

Proposed GAPS line-11 UPDATE (append-only), after R92's UPDATE of G-N5-TIME (GAPS l. 11, «UPDATE 2026-10-30 09:03Z: RESULTS R92
(P-N5-LATEP; CHECKER C102 c13477c2) …», the last on the line), built by script only from the clauses of the title line W1, with R92's
construction (labels behind their clauses; the scope tail as in R92's UPDATE). W1 holds ten "|"; the UPDATE holds none: «|Z_a|» → «the
size of Z_a» (R91's UPDATE wording), «|F| (its transitions)» → «the number of its transitions», «|F| ≤» → «the number of transitions of
F ≤» (three times); these replacements are not title text (to check (8)). Landing time and CHECKER commit to be filled at landing:
UPDATE 2026-10-30 <HH:MM>Z: RESULTS R93 (P-N5-WCH; CHECKER C103 <checker>) [refereed-only] LANDED: N5 on EVERY game (SPEC S1-S5, under the standing SPEC premise of RESULTS R57 (1E-N3: S1's procedure realises the pointwise optimum; for S4a, σ_new is the pointwise optimum of the one-player arena H_t, H_t := S4a's arena at t (Even keeps σ_t ∪ Iσ_t, Odd follows τ_t)); premises RESULTS R15 (a), (d), R17 (a) (F1), R56, R84 (a) (Fact DELTA), R86, R88 (f), R89, R90 (a)-(e), (g) and R91 (a)-(c), (h), (i), (k), (m); a run is the sequence of states (σ_t, τ_t); ⊴, ◁, ⊵, ▷ the SPEC S1 order (better for Even) and its strict and reverse forms; Iσ_t the improving edges of σ_t (SPEC S2); n the number of vertices of the game, n_E the number of its Even vertices, m_E the number of edges leaving Even vertices, d_E(e) the number of Even vertices with an edge to the vertex e; a transition is written t → t + 1 (states t, t + 1), and v is switched at t if σ_{t+1}(v) ≠ σ_t(v); Ξ_t := Ξ_{σ_t} (SPEC S1), λ_Ξ its cycle-node map; for a valuation Ω (Ξ_t, W_t, or W′ below), v is its own Ω-cycle node if the cycle node of Ω(v) is v; W_t := the [S1-val] valuation of the (σ_t, τ_t)-plays (W(v) := W_t(v) at the state in question), λ_W its cycle-node map; Z_t := {v : Ξ_t(v) ≠ W_t(v)} the gap set; a τ-stretch, a W-run and, for a W-run F, the number of its transitions as in RESULTS R89; a phase as in RESULTS R38 (a), an in-phase transition one with both states in one phase, f_P, ZF_P and WCH^S4a_P(v) as in RESULTS R91 (the in-phase Even S4c fallbacks of the phase P, those k → k + 1 with Z_{k+1} = Z_k, and the in-phase S4a transitions of P changing W(v)); a λ-run as in RESULTS R86; S4a steps, boundaries, B_R (the boundaries inside the λ-run R), class-S re-entries and SIL_R as in RESULTS R90 (e); late adoptions, REPEATs, REP_F and REP* := max_F REP_F as in RESULTS R88 (f) and R90 (g); ρ_P := RESULTS R56's ρ of the phase P): at an S4a step t → t + 1, for any pointwise-optimal Even strategy σ⁺ of H_t with W′ the [S1-val] valuation of the (σ⁺, τ_t)-plays, an Even v with d := σ_t(v) ≠ σ⁺(v) and W′(v) = W_t(v) has v ⊕ W′(d) = W′(v) (the prefix operation x ⊕ (c, Q, ℓ) := (c, Q ∪ {x if x is more relevant than c}, ℓ + 1) for a value (c, Q, ℓ) (cycle node c, path set Q, length ℓ)) if v is not its own W′-cycle node, and W′(d) with cycle node v and empty path set otherwise (Lemma TIE); in every W-run F, for every Even v and successor e, the returns of v to e (transitions u → u + 1 of F with σ_{u+1}(v) = e ≠ σ_u(v) at which v held e at some earlier state of F) number at most WCH_F(e) + TT_F(v, e), WCH_F(e) the transitions of F at which W(e) changes and TT_F(v, e) the transitions k → k + 1 of F at which v leaves e (σ_k(v) = e ≠ σ_{k+1}(v)) with W_{k+1}(v) = W_k(v) (Theorem RET-WCH); so, with TIE_F the pairs (v, t), t → t + 1 a transition of F and v switched at t with W_{t+1}(v) = W_t(v), the number of transitions of F ≤ m_E + Σ_e d_E(e)·WCH_F(e) + TIE_F and REP_F ≤ Σ_e d_E(e)·WCH_F(e) + TIE_F (Lemma NEW-BOUND, Corollaries RUN-WCH and REP-WCH); on every λ-run R, SIL_R ≤ GXC_R + NC_R + NT_R ≤ (B_R + 1)·max_P GXC_P + NC_R + NT_R (P over the phases inside R), where a GXC event is a pair (v, t) with v Even switched at t, τ_{t+1} = τ_t, λ_Ξ the same at t and t + 1, v ∈ Z_t, Ξ_{t+1}(v) ▷ Ξ_t(v) and W_{t+1}(v) ⊴ W_t(v), GXC_X the GXC events with t, t + 1 in X, and NC_R (NT_R) the class-S re-entries j − 1 → j of R at which the re-entering vertex is its own Ξ-cycle node at j − 1 or j (at which τ_j ≠ τ_{j−1}) (Lemma SIL-Z, Corollary SC-GXC); every phase P with first state a has GXC_P ≤ TIE_P + the size of Z_a + Σ_v WCH^S4a_P(v) + FBO_P, TIE_P the pairs (v, t) with t → t + 1 an in-phase S4a transition of P, v switched at t and W_{t+1}(v) = W_t(v), FBO_P the GXC events of P at in-phase fallbacks with v ∈ Z_{t+1} (Lemma GXC-CLOSE, Theorem GXC-SPLIT); with LEV_t(v), for v ∈ Z_t, the position of the first coordinate at which Ξ_t(v) and W_t(v) differ in the coordinate sequence (reward of the cycle node; for each rank r from n − 1 down to 0, +1, −1 or 0 as the vertex of rank r is in the path set with even priority, with odd priority, or not; length, negated when the cycle node has even priority) in which the SPEC S1 order is lexicographic, LEV_{t′}(v) ≥ LEV_t(v) for states t < t′ of a phase P with v ∈ Z_t ∩ Z_{t′} and no S4a transition between them changing W(v), the transitions k → k + 1 of P that are not S4a transitions changing W(v) and have v ∈ Z_k ∩ Z_{k+1} and LEV_{k+1}(v) > LEV_k(v) number at most (n + 1)(1 + WCH^S4a_P(v)) (DROP_P(v)), FBO_P ≤ n_E(1 + (n − 1)(2 + ρ_P)) and FBO_P ≤ Σ_v DROP_P(v) + FBOS_P, and ZF_P ≤ NZ_P + Σ_v DROP_P(v) + ZFS_P, FBOS_P the FBO events of P with LEV_{t+1}(v) = LEV_t(v), NZ_P the Z-flat in-phase fallbacks k → k + 1 of P all of whose switched Even vertices are their own Ξ-cycle node at k or k + 1, and ZFS_P the other Z-flat in-phase fallbacks of P at which every switched Even vertex that is its own Ξ-cycle node at neither state keeps LEV (Lemma LEVEL-MON, Corollaries DROP-PAID, FBO-R56, FBO-SPLIT, ZF-SPLIT); and if, for a function w : ℕ → ℕ, every τ-stretch S of every run on games with n vertices has, for every vertex e, at most w(n) S4a steps inside S changing W(e) (premise [P-WCHτ](w), not proved here), then REP* ≤ m_E·w(n) + TIE* (TIE* := max_F TIE_F), every W-run F has the number of transitions of F ≤ m_E(1 + w(n)) + TIE_F, every phase P has f_P ≤ n(1 + w(n)) + ZF_P and ZF_P ≤ NZ_P + n(n + 1)(1 + w(n)) + ZFS_P, GXC_P ≤ TIE_P + n(1 + w(n)) + FBO_P and FBO_P ≤ n(n + 1)(1 + w(n)) + FBOS_P (Theorem WCH-RED, Corollary WCH-ONE); for the labelled VARIANT N5-LZC (N5 with S4a's output σ* replaced by σ′, which, with W* the [S1-val] valuation of the (σ*, τ_t)-plays, keeps σ_t(v) at every Even v whose W*(v) has length at least 1 and satisfies v ⊕ W*(σ_t v) = W*(v), and at every Even v with W*(v) = (v, ∅, 0) for which W*(σ_t v) has cycle node v and empty path set, and takes σ*(v) at every other Even v; nothing transfers to N5), the (σ′, τ_t)-plays have valuation W*, every Even vertex switched at an S4a step strictly raises its W-value read with τ_t, so TIE_F = TT_F = 0, the number of transitions of F ≤ m_E + Σ_e d_E(e)·WCH_F(e) and REP_F ≤ Σ_e d_E(e)·WCH_F(e) for every W-run F of N5-LZC (Lemma LZ-OPT, Theorem LZ-STRICT, Corollaries RUN-WCH_LZ, REP-WCH_LZ), and N5-LZC has no class-S re-entry (Corollary LZ-NOSIL, under ASSUMPTION OPT-ONLY that RESULTS R90 Fact B and (a) (ii), (b), (c), (d) hold verbatim for N5-LZC runs): a REDUCTION; per-vertex W-changes per τ-stretch ([P-WCHτ]), TIE*, NZ_P, ZFS_P, FBOS_P, NC_R, NT_R, ρ_P and B_R are not bounded here. G-N5-TIME stays open.
