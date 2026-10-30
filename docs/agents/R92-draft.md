# Draft RESULTS R92 (Lead, 2026-10-30 07:37Z by date -u; subagent draft; packet, both reports, both §Cs (with REFEREE §C §4 and REFEREE-2 §C.5) and the fixes file F0-F15 + F-SYM read at the origin heads fetched 07:23Z (date -u in the same command); pinned blocks re-run 07:30Z; Lead revision 2026-10-30 08:25Z by date -u (read in the same command as this edit; subagent revision): title → line F16 (l-si baa8a48a, sha1 65277add…; fixes F16, sha1 66c85a16…), both F16 verdicts (REFEREE 11259154, REFEREE-2 aa366149), §C pins re-measured at the origin heads fetched in this revision before 08:20:47Z (date -u not read in the fetch commands; origin trunk 978d5a8e), symbol test and stale-label test re-run on F16, GAPS UPDATE re-built) — to CHECKER C102 — LANDED in RESULTS Results 2026-10-30 09:03Z (CHECKER C102 c13477c2 PASS), after R91
to check: (1) TITLE. The title is the line file docs/si/P-N5-LATEP-line-F16.txt (l-si baa8a48ad2d98f5cb67aee47e6468d80465edcd8,
2026-10-30T07:45:41Z, the file's only commit, sha1 65277addc8be558922dcdcc7d035426ba3062b8e; identical at l-si head baa8a48a, at origin
trunk 978d5a8e and at the local trunk head 92dd9a6d; merged into trunk by a98e0f3b, 08:06:51Z), verbatim: one line, no outer quotes, no
final period, 2,731 characters (2,876 bytes plus the newline), no "|". It ALREADY carries " (2026-10-30)" right before " — a REDUCTION"
("2026-10-30" occurs exactly once in the line and exactly once in the heading, by script), so no date is inserted. The checker fill
", CHECKER PASS (docs/checker/C102.md, checker PENDING)" is appended as in R90 and R91. The heading was built by script from the file at
baa8a48a (level-3 marker, then "R92 [refereed-only] ", then the file without its newline, then the fill) and re-checked after writing:
equal.
LINE HISTORY: frozen 4a68934d (docs/si/P-N5-LATEP-line.txt, l-si b63f2554, 2,435 characters) → F1 a85759a2
(docs/si/P-N5-LATEP-line-F1.txt, l-si 17a3ecec, 2,681 characters; F0's five changes) → F16 65277add (F16's five changes). 4a68934d and F1
are history, not the title. Word diff F1 → F16, measured three ways for this revision: `git diff --no-index --word-diff=porcelain`
(−«R15,» +«R15 (a), (d),»; +«R57 (a) (premise (VJ)),»; −«W-MON,»; +«W-MON′,»; +«it is LATE′ and»); an exact string-replacement script
(«RESULTS R15, R17 (a), R47 (a), R88 (Lemmas W-MON, XW,» → «RESULTS R15 (a), (d), R17 (a), R47 (a), R57 (a) (premise (VJ)), R88 (Lemmas
XW,»; «R90 (Lemmas OPT-OFF (ii), W-SUCC)» → «R90 (Lemmas OPT-OFF (ii), W-MON′, W-SUCC)»; «a REPEAT′ if (y, z)» → «a REPEAT′ if it is LATE′
and (y, z)»; each old string occurs exactly once; the result equals F16 byte for byte); difflib over whitespace tokens, 529 → 539 tokens,
five non-equal opcodes (= REFEREE-2 §C.6 l. 107 «529 → 539»). Nothing else changes: these are exactly F16's five changes (fixes l.
176-181). Word diff 4a68934d → F1 (F0's five changes, fixes l. 16-26): measured three ways for the pre-F16 draft; difflib re-run for this
revision: 486 → 529 tokens (= REFEREE-2 §C.5.1 l. 62).
(2) THE LINE AT BOTH REFEREES. F16 (the title): REFEREE successor 19, docs/referee/R-N5-LATEP-C.md l. 83, one line appended at
11259154 (2026-10-30T08:07:56Z): «F16 check (Lead 08:06Z; l-si baa8a48a, docs/si/P-N5-LATEP-line-F16.txt sha1
65277addc8be558922dcdcc7d035426ba3062b8e and fixes sha1 66c85a168022bf08af630ddcd0df494b09a5733c, re-measured; fixes append-only vs
17a3ecec; my own word diff F1 → F16, written 08:07Z by date -u): exactly the five changes «R15» → «R15 (a), (d),», «+R57 (a) (premise
(VJ)),», «−W-MON,» (R88's list), «+W-MON′,» (R90's list), «a REPEAT′ if {+it is LATE′ and+} …». Use-by-use claim checked at b63f2554: …
✓ The REPEAT′ restriction matches packet §2 («A LATE′ adoption is FIRST′ … REPEAT′ otherwise»). I MISSED both defects in my F1 test; the
drafter caught them. Strict symbol test of the whole F16 line: no free symbol, no unlanded source. MATCHES (Opus 5.5, D15).» REFEREE-2
successor 22, docs/referee-2/R2-N5-LATEP-C.md §C.6 (l. 106-126, aa366149, 2026-10-30T08:07:48Z): l. 107-109 «Word-diff F1 (a85759a2) →
F16, my own (difflib over tokens, 529 → 539), all of it: … Exactly F16's five changes, nothing else; every displayed inequality, date and
scope tail token-identical.»; l. 110 «Use-by-use check, against the frozen packet and RESULTS. Every W-monotonicity use in §3-§7 is covered
by a landed W-run form:»; l. 119 «REPEAT′ (F16 (1)): a real line defect that BOTH referees MISSED.»; l. 121 «W-MON scope (F16 (2)): BOTH
referees MISSED it too.»; l. 125 «No free symbol, no unlanded binder.»; l. 126 «Verdict (Opus 5.5, D15): line F16 MATCHES §3-§7. F16's two
items are corrections, with no widening; the REPEAT′ change narrows the line.» Not revised for F16 (both F16 verdicts stand apart from
them): REFEREE §C NEEDS l. 82 («§4: F1 MATCHES»; the F16 line follows it); REFEREE-2 §C DONE / FINDINGS / NEEDS l. 128-137 (NEEDS l. 136:
«… for landing P-N5-LATEP on the new line a85759a2»; §C.6 precedes it). One difference of reading, no verdict affected: REFEREE l. 83
«R88's W-MON is stated for a frozen W-phase; R89 GP*-RUN carries it to W-runs, so either citation works, and W-MON′ is the direct one»;
REFEREE-2 l. 121-122 «Both reports accepted «W-MON on F» without checking that R88's form is per phase. The packet's proofs remain correct
with R90 (b) W-MON′ in its place». F1 (history): REFEREE §C §4 (R-N5-LATEP-C.md l. 47-76, 9d47dcbb): l. 49-56 «My own word diff (`--word-diff=porcelain`) of
the frozen line 4a68934d against F1 shows exactly F0's five changes … Nothing else changes.»; l. 59-61 «Strict symbol test of the whole F1
line (mine): a and b are now bound; t is bound in both cases of LATE′ (t < u always, which closes L-1); X′_F's t is fixed (the earliest;
[k + 1, t] is non-empty by F10); GXC_F is self-contained; every other symbol is as in my §9 of R-N5-LATEP. No free symbol, and no unlanded
source. The F-SYM table agrees.»; l. 75-76 «Verdict (Opus 5.5, D15): F1 MATCHES §3-§7 with F0-F15, has no free symbol, and claims nothing
more. P-N5-LATEP is landable as far as REFEREE is concerned, with F1 as the line.» REFEREE-2 §C.5 (R2-N5-LATEP-C.md l. 58-104, 42ab528b):
l. 71-72 «Nothing else changes: every displayed inequality, the date and the scope tail are token-identical. The diff equals F0's list of
five changes (F0 counts #1 and #2 as one).»; l. 82-83 «Result: no free symbol, no unlanded binder. The new line MATCHES the packet's §3-§7
(the statements are unchanged from the frozen line, which I diffed against §3-§7 in my report §4).»; NEEDS l. 114-115 «Lead: none from
REFEREE-2 for landing P-N5-LATEP on the new line a85759a2 (the CHECKER's exact-commit run is next). F14's new box-41 claim is READING and
unchecked: do not land it.»
(3) CLAIMS SIGNED = the eight items (a)-(h) below, each SIGNED in BOTH verdict tables (REFEREE R-N5-LATEP.md l. 15-31; REFEREE-2
R2-N5-LATEP.md l. 12-26), re-read for this draft. The §2 Definition LATE′ and its diff against R88 §4 is a DEFINITION: both tables say
«CHECKED» (not «SIGNED»), both §Cs say «agreed» / «agree»; it is recorded under Object, not as a claim. §8 READING (R1)-(R3) on landed R90
is NOT signed (both tables) and sits under Referee strengthening (ii). F14's new sentence is excluded (Fixes, F14).
(4) PREMISE LABELS (stale-label test, re-run on F16; grep of docs/RESULTS.md at origin trunk 978d5a8e = the local trunk head 92dd9a6d,
sha1 cd5f38a19b9625c4764ed0f4e61414102e6b847f, unchanged since 5bf4fe6b, the R91 landing):
- R15 (l. 624): F16 names «R15 (a), (d)»: (a) Lemma A at l. 631, (d) at l. 640. Match. The packet's use (§1 l. 40: «each S4a / S4c step
  applies improving switches only, so Ξ is non-decreasing along the run») is (a) with (d); F16 (3) (fixes l. 173-174): «(a) Lemma A,
  improving switches do not lower Ξ; (d) every N5 iteration applies such switches». F1's «R15» with no item (a precision) is RESOLVED.
- R17 (a) (l. 738): «(V1)/(V2) (prefix equation and prefix monotonicity of values) and (F1)/(F2)»: match ([V1], [V2] in TXC-DESCENT; (F1)
  only inside R88's W-MON and R90's OPT-OFF).
- R47 (a) (l. 2336-2339), Lemma Φ (c): «along a run at most n(n − 1) transitions change λ» (λ := Ξ's cycle-node map, R47 setting l. 2330):
  match for «the sum of LCT_F over the W-runs of a run at most n(n − 1)».
- R88 (l. 5630): F16 names (b) XW l. 5707, (c) GP* l. 5712 (BLOCKED, «at state t ∈ [a, b)»), (f) FW-R* l. 5738 (its «A LATE ADOPTION
  in F …» = the packet's §2 quote of P-N5-GP l. 144-145): names match. (a) W-MON l. 5701 is no longer named (F16 (2)). The F1 MISMATCH
  below is RESOLVED by F16 (2), which names R90 (b) W-MON′ instead (see R90); kept as the record. F1 MISMATCH (scope): R88 (a) states W-MON for «a
  transition inside a phase that is not an S4c fallback» (l. 5701; phase = RESULTS R38 (a), R88 l. 5685), while the packet uses W-MON at
  every transition of a W-run (GAP-CLIMB: «⊴ W_s(z) (W-MON)»; CHAIN: GXC ⊆ TXC), and a W-run may change λ_Ξ (R89's title, l. 5854, on GP*-RUN: «σ̄ and
  λ_Ξ need not be constant there»; R89 (h) l. 5971-5972: «a W-run lies in a τ-stretch, not in one phase»). The statement used is landed as RESULTS R90 (b) W-MON′ (l. 6188: «At an S4a step t → t + 1 with τ* := τ_t:
  W^{τ*}_{t+1} ⊵ W^{τ*}_t pointwise»; on F every transition is an S4a step with τ kept) and R91 (b); R89 (h)'s parenthetical (l. 5965)
  records that «R88's W-MON, GP* and FW-R* proofs use τ constant, no S4c fallback, λ_W constant and [S4a]». F1 named R90 but only
  «OPT-OFF (ii), W-SUCC» from it. Neither referee raised this on F1 (REFEREE l. 57 «W-MON on F»; REFEREE-2 l. 49 «W-MON on F»); both
  say so at F16 (to check (2)); no verdict affected. R88 (b) XW is stated «for every v and t» (l. 5707) inside R88's frozen-W-phase entry; its proof is pointwise (also RESULTS R91
  (a), every game): match in content.
- R89 (l. 5854): the W-run (title), (g) LATE-RISE l. 5957, (h) GP*-RUN l. 5959: match. (f) SUCC-MON l. 5955 is listed in the packet's §1
  (l. 39) but used by no proof; the line omits it (F3 l. 42; REFEREE §C l. 67 «I checked this: W-SUCC (R90) carries the W chains, and
  SUCC-MON is Ξ-based.»; REFEREE-2 §C l. 66 «SUCC-MON is used by none, so its omission is right»).
- R90 (l. 6116): F16 names OPT-OFF (ii), W-MON′, W-SUCC. (a) OPT-OFF l. 6179 ((ii) is read with (i)'s optimality; R90's standing
  premise: «Every later item uses OPT-OFF (i), so the whole packet carries this premise»), (b) W-MON′ l. 6188 («At an S4a step t → t + 1
  with τ* := τ_t: W^{τ*}_{t+1} ⊵ W^{τ*}_t pointwise.» (σ_t ⊆ H_t; OPT-OFF (i). R88's W-MON is the case τ_{t+1} = τ_t.)): match; on F
  every transition is an S4a step with τ kept, so W^{τ*} = W (F16 (2), fixes l. 161-162). W-MON′'s proof uses OPT-OFF (i), which the line
  does not name; it names W-MON′ as a landed lemma, and R90's standing premise covers (i) (my reading, for CHECKER). (c) W-SUCC l. 6190
  (= the packet's quote of P-N5-CUT l. 111-112, verbatim); «off-cycle for τ
  (P-N5-CUT §2)» = R90's setting l. 6157 «v OFF-CYCLE if CN^τ_t(v) ≠ v»: match. Name clash: RESULTS R91 also signs Lemmas XW, W-MON,
  OPT-OFF and W-SUCC (different statements); the line attaches each name to its entry (R88, R90), so no ambiguity (as C101 Add. 2).
- R57 (l. 2893): F16 names «R57 (a) (premise (VJ))»: R57 (a) l. 2907 «Premise (VJ), on every game: for every positional σ and every
  positional Odd strategy τ′, Ξσ(v) ⊴ V_{σ,τ′}(v) at every v»: match. The same label is used in RESULTS (R88 l. 5686: «RESULTS R57 (a)
  premise (VJ), for XW's first part (G7 …»; l. 4804: «RESULTS R57 (a) premise (VJ)»). F16 (3) (fixes l. 175): «XW's first part, Ξσ ⊴
  V_{σ,τ′} for every Odd τ′, is R57 (a)'s (VJ) premise, as R88 names it (P-N5-GP G7)». The F1 point below («R57 (a) (VJ) … is not named
  in the line») is RESOLVED; the standing-premise point stays. «the standing SPEC premise of RESULTS R57», content not spelled in the line (R90's and R91's titles spell it). The packet
  (§1 l. 48-49) reads it as «S1's procedure realises the optimal counterstrategy; S4a's σ_{u+1} is Even's pointwise optimum in its arena».
  R57 states 1E-N3 for σ̄ only (R57 (b) l. 2915-2916); the S4a form is RESULTS R67's P2 (l. 3462-3463) and R88's [OPT-H]: the same label
  point as R91's to-check (4). R57 (a) (VJ), used through R88's XW and R90's OPT-OFF (i), is not named in the line (REFEREE LATEP-N1, l. 76:
  «OPT-OFF (i)'s R17 (a) (F1) + R57 (a) chain is inherited from R90 (P-N5-CUT K2)»).
- R91 (l. 6545-6546): «L-NEW boxes 70-71 … are excluded from this entry»: matches F2 l. 35-36 («RESULTS R91 excludes boxes 70-71»).
(5) SYMBOL TEST of the title (my own strict test of every symbol, re-run on the F16 text for this revision; rows changed by F16 are
marked «F16»; IN = bound in the line; else the carrier):
| symbol | where |
| --- | --- |
| F, a, b, W-run | IN («In every W-run F = [a, b]»; W-run «as in RESULTS R89: τ and λ_W constant on F, no S4c fallback»; R89 title l. 5854) |
| N5, SPEC S1-S5, S4c fallback | SPEC (named) |
| the standing SPEC premise of RESULTS R57 | named only, content not in the line; see (4) |
| R15 (a), (d), R17 (a), R47 (a), R57 (a) (premise (VJ)), R88 (XW, GP*, FW-R*), R89 (…), R90 (OPT-OFF (ii), W-MON′, W-SUCC) | cited premises, each a landed RESULTS item; see (4). F16: R15's items, R57 (a), W-MON′ added, W-MON dropped |
| W_t, λ_W | «as in RESULTS R89» (R89 title: «W_t := the [S1-val] valuation of the (σ_t, τ_t)-plays, λ_W its cycle-node map») |
| τ | F's constant τ («τ and λ_W constant on F»); used in D_s and in «off-cycle for τ» |
| σ_u, σ_k, σ_s (the Even strategy of a state) | NOT in the line: the states (σ_t, τ_t) of the N5 run (SPEC; R89's W_t); REFEREE-2 l. 75 and §C l. 76: «acceptable» |
| Ξ_t, σ̄_t, Iσ_t, ⊴, ▷ | «as in SPEC S1-S2»; «(▷ strict)»: SPEC's strict order is ◁ and ▷ its converse; reads naturally |
| λ_Ξ | IN («the cycle-node map of Ξ_t») |
| BLOCKED | RESULTS R88 (c) l. 5712 («at state t ∈ [a, b)»), read on F by R89 (h) l. 5959 |
| n, n_E, m_E, d_E(z) | IN; «Even edges» is by use (edges leaving Even vertices, as R90's title: «m_E the number of edges leaving Even vertices») |
| Even, Odd | SPEC (owner of a vertex) |
| adoption, y, z, u | IN («an adoption of (y, z) at u: σ_{u+1}(y) = z ≠ σ_u(y)») |
| LATE′, t, p | IN; t < u in both branches (F1) |
| REPEAT′, «it» | IN. F16: «a REPEAT′ if it is LATE′ and (y, z) has an earlier LATE′ adoption in F»; «it» = the adoption of (y, z) at u being classified; REPEAT′ ⊆ LATE′ as packet §2 (F16 (1); was the defect in (5b)) |
| R*′_T, REP′_F | IN («T» is part of the name, as R88's R*_T) |
| X′_F, k, t (second use) | IN; t re-bound as «the earliest blocked state as in the definition of LATE′» (F4). F16: t now exists for every REPEAT′, since a REPEAT′ is LATE′; k exists, y leaving z after the earlier adoption (F10) |
| off-cycle for τ | «(P-N5-CUT §2)» = RESULTS R90's object; R90 setting l. 6157 |
| WCH_F, WCH_F(z), W(z) | IN (W(z): the map t ↦ W_t(z)) |
| Z_s, D_s, o, v | IN (Z_s and D_s for a generic state s, before the «over the transitions» clause) |
| s, «transitions of F» | IN («over the transitions s → s + 1 of F (s, s + 1 in F)»); LCT_F sits inside that clause (REFEREE-2 l. 86) |
| ZXC_F(z), TXC_F(z), WZ_F(z) | IN |
| GXC_F, v | IN (inlined by F2; box 70's τ-clause is automatic on F) |
| GATE_F, CNW_F, x, LCT_F | IN |
| TXC_F, ZXC_F as sets; «a set stands for its number of elements» | IN |
| Σ_z | z over the vertices of the game, by use |
| «a run» (the LCT sum) | an N5 run (SPEC) |
| Lemma / Corollary / Proposition names | packet §3-§7 (CIRCLE′ labelled by F3) |
| G-N5-TIME, M3, step-4, TARGET.md | scope tail; GAPS l. 11, TARGET.md |
Every symbol of F16 is bound in the line, by SPEC or by a named landed entry. Soft spots, as in landed titles: σ_t (by the run), «Even
edges» (by use), the R57 standing premise (named, content elsewhere); R90's W-MON′ is stated for W^{τ*}, read as W on F (F16 (2); τ
constant on F). No new point found on F16. Agreeing tests of F16: REFEREE §C l. 83 «Strict symbol test of the whole F16 line: no free
symbol, no unlanded source.»; REFEREE-2 §C.6 l. 123-125 («No free symbol, no unlanded binder.»); the lane's (fixes l. 182-185: «Result: no
free symbol, no unlanded source.»). On F1, both referees and F-SYM (fixes l. 117-141) found no free symbol; the two defects in (5b) were
missed there.
(5b) DEFECTS IN F1, RESOLVED BY F16 (record). Two defects of line F1 were found by the R92 drafter's strict test of F1 (the pre-F16 draft,
docs/agents/R92-draft.md at fce982d1: the REPEAT′ point in its symbol test (5b), the W-MON scope in its premise-label test (4)). Neither
referee nor F-SYM raised them on F1; at F16 both referees record that they missed both (REFEREE §C l. 83 «I MISSED both defects in my F1
test; the drafter caught them.»; REFEREE-2 §C.6 l. 119 and l. 121, quoted in (2)). F16 is headed «Lead 07:46Z (the R92 drafter's strict
symbol test of line F1, a85759a2)» (fixes l. 150). F16 classes both LINE-REQ (fixes l. 153, l. 158).
- W-MON scope: R88 (a) W-MON is stated inside a phase; F1 used it on a W-run (to check (4), R88, kept as the record). F16 (2) drops W-MON
  from R88's list and names R90 (b) W-MON′; both referees checked the use-by-use claim (§3, §4, §5 l. 99, §6 l. 109, §7) at F16.
- REPEAT′ (the record of the pre-F16 reading point follows; F16 (1) adopts the minimal edit it suggested, verbatim). F1 read
«call an adoption of the Even edge (y, z) at u LATE′ if …, a REPEAT′ if (y, z) has an earlier LATE′ adoption in F». Read literally, «a
REPEAT′» is said of ANY adoption of such an edge, not only of a LATE′ one. The packet has REPEAT′ ⊆ LATE′ (§2 l. 56-57: «A LATE′ adoption is
FIRST′ if (y, z) has no earlier LATE′ adoption in F, REPEAT′ otherwise») and so do the proofs (§4 l. 76: «Blocked at some t ∈ [p + 1, u) by
LATE′»). Under the literal reading, REP′_F ≤ n_E·R*′_T need not follow (a non-LATE′ re-adoption is not in R*′_T), and X′_F's «t the earliest
blocked state as in the definition of LATE′» need not exist. The signed reading is REPEAT′ ⊆ LATE′ (packet §2; the lane's §9 row l. 173 and
REFEREE-2's table l. 82 read the clause as «bound»). It is the same kind of point as REFEREE-2's L-1 (a literal reading of the line wider
than §2). The pre-F16 draft asked CHECKER / the Lead to decide on a minimal edit (for example «a REPEAT′ if it is LATE′ and (y, z) has an
earlier LATE′ adoption in F») with both referees' word-diff. Decided: F16 (1) makes that edit (fixes l. 157), both referees' word-diffs
are in (2), and the title below is F16 verbatim.
(6) GAPS: G-N5-TIME (GAPS l. 11) stays open; the title names no CONJECTURE. A line-11 UPDATE is proposed at the end, after R91's UPDATE (the
last one on l. 11, still the last at origin trunk 978d5a8e: «UPDATE 2026-10-30 05:59Z: RESULTS R91 (P-N5-GAP; CHECKER C101 Add. 3
c17ff164) …»), re-built for this revision from F16's clauses only, by script; F16 contains no "|", and the UPDATE contains none.
(7) DATA of record = the corrected txcd.py figures (F5 / F6; odd/out/txcd_corpus_f1.txt at 17a3ecec, summed for this draft by script):
corpus TXC 14,739; terminals T1 292, T2 (GXC) 306, T3 14,136, T4 5; GXC events 191; CNW 71; pins so_th_n32 TXC 73 / gate terminals 16,
tiedmut_so_th_n32_11 TXC 77 / 10, b5_o11 CNW 1. The pre-fix figures (corpus TXC 14,526, T1 356, T2 292, T3 13,878, GXC events 227, «0 T4»;
so_th 63 / 15; tiedmut 66 / 9) appear only as SUPERSEDED.
(8) Discrepancies, recorded for CHECKER, no verdict affected: (i) txcd.py's «GATE» counts DISTINCT (x, s) gate terminals (its docstring at
17a3ecec), not the line's GATE_F (TXC events at gates): corpus 2,416 (txcd_corpus_f1.txt; REFEREE-2 §C l. 99 «gate terminals 2,416») vs
REFEREE-2's table column «GATE» 2,464 (l. 120); the pins' «gates 16» (so_th) are gate terminals. (ii) F6 l. 77-78 calls REFEREE's set «its
subset (n ≤ 120, given starts)»; REFEREE l. 113 ran «given start and S3»; REFEREE §C l. 73 reads it «(n ≤ 120, given starts plus S3), as F6
says». (iii) Packet §10 l. 197 «13,878 gates» counts T3-terminated descents, not GATE_F. (iv) Packet §9 row «GXC_F … landed» (l. 180) was
wrong (F2 l. 35-36). (v) Packet §10 l. 198 glosses TIED-RB as «TXC alone pays every REPEAT′»; the statement killed (box 51 §1, l-si 7dd85b02:
«every re-blocked REPEAT of (y, z) has a tied Ξ-climb of z on [k, u − 1]») is about R88-late REPEATs (box 50 §6); R131 states it the same way
as box 51. (vi) docs/red/R131-tied-rb.md's «written» stamps (header «from 06:35Z»; addendum «written 06:40Z») postdate its commits
(011213ef 05:52:06Z; 7e85ead2 06:33:17Z): L-RED's file, cited for the Oink check only.
(9) Excluded: lane work after the freeze other than the fixes commits 17a3ecec (F0-F15, line F1) and baa8a48a (F16, line F16; it touches
only docs/si/P-N5-LATEP-fixes.md, +39/−0, and the new line file): L-SI's handover 1f678c1c (notes/L-SI.md only) and any later L-SI work
other than baa8a48a; L-NEW boxes 72-75 (177dbfb1, d0619575, 29a4dc17, 01588402) and later; L-RED R131-R133 (011213ef, 125c7b15, R133), except R131's addendum
7e85ead2 cited under Data for the Oink check of the box-51 TIED-RB instance; the working notes N5-ADD-box50, N5-LATEP-box51, N5-TXCD-box52.
(10) Commits: REFEREE and REFEREE-2 commit their files directly on their branches (each file commit is the branch commit; no branch-side
merge; REFEREE-2's aa366149 has as parent a3b42e1e, a Lead trunk commit of 07:55:43Z). The trunk merges of 9d47dcbb (04705e43) and
42ab528b (0396db78), both 07:23:16Z, are now on origin trunk 978d5a8e. The F16 verdict commits 11259154 (merged by 809941a6, 08:19:19Z)
and aa366149 (merged by 30be80e0, 08:19:20Z) are on the LOCAL trunk head 92dd9a6d only: not on origin trunk 978d5a8e at this revision's
fetch (date -u 08:20:47Z, read in a later command than the fetch; local trunk 5 commits ahead, 0 behind). F16 itself (baa8a48a) is on origin trunk (a98e0f3b). (11) Placement: after R91 (R90 and R91 are landed; "## Dead ends (kept;" follows).
(12) TIED-RB: the packet records the kill (§10 l. 198); RESULTS has no TIED-RB record yet (grep: 0 in docs/RESULTS.md and docs/GAPS.md).
Whether it also goes to "## Dead ends" is the Lead's call; this entry records it under Data only.

### R92 [refereed-only] In every W-run F = [a, b] of N5 (SPEC S1-S5) on any game, under the standing SPEC premise of RESULTS R57, with RESULTS R15 (a), (d), R17 (a), R47 (a), R57 (a) (premise (VJ)), R88 (Lemmas XW, GP*, Corollary FW-R*), R89 (Lemmas GP*-RUN, LATE-RISE) and R90 (Lemmas OPT-OFF (ii), W-MON′, W-SUCC) (W-run, W_t, λ_W as in RESULTS R89: τ and λ_W constant on F, no S4c fallback; Ξ_t, σ̄_t, Iσ_t and the order ⊴ (▷ strict) as in SPEC S1-S2, λ_Ξ the cycle-node map of Ξ_t; BLOCKED as in RESULTS R88; n the number of vertices, n_E of Even vertices, m_E of Even edges, d_E(z) of Even edges into z; an adoption of (y, z) at u: σ_{u+1}(y) = z ≠ σ_u(y)), call an adoption of the Even edge (y, z) at u LATE′ if (y, z) is blocked at some state t of F with p + 1 ≤ t < u, p its previous adoption in F (a ≤ t < u if there is none), a REPEAT′ if it is LATE′ and (y, z) has an earlier LATE′ adoption in F, and let R*′_T be the transitions of F containing a LATE′ adoption, REP′_F the REPEAT′s of F, X′_F those REPEAT′s of (y, z) at u for which y is not off-cycle for τ (P-N5-CUT §2) at some state of [k + 1, t], k the last k < u with σ_k(y) = z ≠ σ_{k+1}(y) and t the earliest blocked state as in the definition of LATE′, WCH_F the W-changing transitions of F and WCH_F(z) those changing W(z), Z_s := {v : Ξ_s(v) ≠ W_s(v)}, D_s := {Odd o : σ̄_s(o) ≠ τ(o)}, and, over the transitions s → s + 1 of F (s, s + 1 in F): ZXC_F(z) those with z ∈ Z_s and Ξ_{s+1}(z) ▷ Ξ_s(z), TXC_F(z) those with Ξ_{s+1}(z) ▷ Ξ_s(z) and W_{s+1}(z) = W_s(z), WZ_F(z) those of ZXC_F(z) with W_{s+1}(z) ≠ W_s(z), GXC_F the pairs (v, s) with v Even, σ_{s+1}(v) ≠ σ_s(v), λ_Ξ unchanged at s → s + 1, v ∈ Z_s, Ξ_{s+1}(v) ▷ Ξ_s(v) and W_{s+1}(v) ⊴ W_s(v), GATE_F the pairs (o, s) with o Odd in D_s ∪ D_{s+1} and s in TXC_F(o), CNW_F the pairs (x, s) with λ_W(x) = x and s in TXC_F(x), LCT_F the transitions at which λ_Ξ changes, TXC_F and ZXC_F the sets of pairs (z, s) with s in TXC_F(z), resp. ZXC_F(z), and in every inequality a set stands for its number of elements: (Corollary FW-R*′) WCH_F ≤ (n − 1)(R*′_T + 1); (Lemma LATE-SPLIT′, Corollary CIRCLE′) R*′_T ≤ m_E + REP′_F, REP′_F ≤ n_E·R*′_T and REP′_F ≤ X′_F + Σ_z d_E(z)·WCH_F(z); (Lemma GAP-CLIMB) the LATE′ adoptions of each Even edge (y, z) in F number at most ZXC_F(z); (Proposition CHAIN) GXC_F ⊆ TXC_F ⊆ ZXC_F as sets of pairs (vertex, transition), and ZXC_F(z) is the disjoint union of TXC_F(z) and WZ_F(z); (Lemma TXC-DESCENT, Corollary TXC-RED) TXC_F ≤ n·(GXC_F + GATE_F + CNW_F) + n²·LCT_F, with the sum of LCT_F over the W-runs of a run at most n(n − 1) (2026-10-30) — a REDUCTION (GATE_F, CNW_F, GXC_F, WZ_F(z) and REP′_F are not bounded here; G-N5-TIME stays open; not M3, not a step-4 pass, not a TARGET.md claim), CHECKER PASS (docs/checker/C102.md, checker PENDING)
- Object (L-SI successor 32, Opus 5.5, D15 / D18, Lead reading L40; frozen, unchanged during review): packet P-N5-LATEP,
  docs/si/P-N5-LATEP-box53.md, sha1 b15223e53157d7d0a14767bb3c71dae07066a4da, 204 lines (l-si freeze b63f2554e63072c4d8b491fc4c34bb30ef6e7b5c,
  2026-10-30T06:16:38Z, the file's last commit (first commit fd8c2231, 06:04:49Z, the unfrozen draft); identical at l-si head 17a3ecec, at
  origin trunk 8bb9799d and at the local trunk head (`git diff --stat b63f2554 17a3ecec` on the packet and the old line file: empty); merged
  into trunk by 84614aee, 06:26:58Z). Both referees measured the sha1 at b63f2554 (REFEREE l. 3-5; REFEREE-2 l. 2-3). The Lead's freeze word
  is quoted at l. 2-4 («Lead 2026-10-30 06:11Z: «P-N5-LATEP: GO, with your item list §1-§6 as proposed, plus two edits: (a) Add a §7
  READING, explicitly NOT TO SIGN: R90's REP* and LATE term may be read with LATE′ … (b) The line file must bind every symbol in the line
  …»»; the Lead's §7 is the packet's §8). Quote base: six [Q path@170e5316:lines] quotes (SPEC S4a l. 51, P-N5-GP l. 85-86 and l. 144-145,
  box10 l. 20-22, P-N5-CUT l. 111-112, box 70 l. 48-49), checked by experiments/si/rund/quotecheck.py (pinned «box 53», with a shifted
  control that must fail), by REFEREE (l. 11: «my script scratch/cut_quotes.py finds 6/6 verbatim») and by REFEREE-2 (l. 68: «tags 6, ok 6,
  miss 0; control SHIFT=1: ok 0, miss 6»); re-run for this draft: «quotes=6 bad=0», --mut «quotes=6 bad=6», «QUOTES FAIL». Sections: §0
  what to sign (l. 12-23), §1 setting, symbols, premises (l. 25-49), §2 Definition LATE′ (l. 51-58), §3 FW-R*′, §4 LATE-SPLIT′ and CIRCLE′,
  §5 GAP-CLIMB, §6 CHAIN, §7 TXC-DESCENT and TXC-RED, §8 READING on R90 («NOT TO SIGN», l. 147-159), §9 the lane's strict symbol test of the
  line (l. 161-187), §10 DATA and pins («NOT to sign», l. 189-199). Scope (l. 8-9): «lemmas about one W-run of N5 on every game. Each one is a
  REDUCTION or a structural fact. No count is bounded here; G-N5-TIME stays OPEN. Not a TARGET.md claim, not an algorithm claim.» Working
  notes docs/si/N5-ADD-box50.md, N5-LATEP-box51.md, N5-TXCD-box52.md (l. 7): not refereed here.
  The RESULTS line, history. (1) The frozen line docs/si/P-N5-LATEP-line.txt (l-si b63f2554; first version fd8c2231), sha1
  4a68934d832c483c5b28c552fd26526f7de4abea, the line both referees reviewed (REFEREE l. 4-5; REFEREE-2 l. 2-3). Verdicts on it: REFEREE
  «MATCHES §3-§7 and claims nothing more, after LATEP-L1 (required by the every-symbol rule) and two precisions (LATEP-L2, L3)» (l. 31),
  «Verdict on the line (Opus 5.5, D15): MATCHES; NOT YET landable by the every-symbol rule until LATEP-L1; L2, L3 are precisions.» (l. 107);
  REFEREE-2 «DISAGREE in one row: «LATE′, p, t» is not correctly bound (L-1); three precision points (L-2, L-3, L-4)» (l. 25), «With L-1
  fixed, the line MATCHES the packet's §3-§7 statements» (l. 103). §Cs: the union of the two REQUIRED fixes, J-1 = REFEREE-2's L-1 (the
  parenthetical «(any t of F if none)» drops t < u) and J-2 = REFEREE's LATEP-L1 = REFEREE-2's L-2 (GXC_F cites the unlanded, unpinned L-NEW
  box 70): REFEREE §C §3 l. 43 «REQUIRED before landing: L-1 (t < u in the no-previous-adoption case) and LATEP-L1 = L-2 (GXC inlined or
  pinned; I hold REQUIRED).»; REFEREE-2 §C C.2 l. 23-29 («I accept REQUIRED», l. 29). (2) F1 (fixes F0, l. 15-27): docs/si/P-N5-LATEP-line-F1.txt,
  sha1 a85759a26b38b8bb6e3958bb19745d2aa9fd397c = 4a68934d + exactly five changes: «F = [a, b]» and the landed premises named (F3); «(a ≤ t
  < u if there is none)» (F1 = J-1); «t the earliest blocked state» (F4 = J-4); GXC_F inlined (F2 = J-2); «(Lemma LATE-SPLIT′, Corollary
  CIRCLE′)» (F3 = J-3). Word diff re-measured for this draft: those changes, nothing else (to check (1)). REFEREE §C §4 l. 75 «F1 MATCHES §3-§7
  with F0-F15, has no free symbol, and claims nothing more.»; REFEREE-2 §C.5.2 l. 82-83 «no free symbol, no unlanded binder. The new line
  MATCHES the packet's §3-§7». F1 supersedes 4a68934d. (3) F16 (fixes F16, l. 150-187): docs/si/P-N5-LATEP-line-F16.txt (l-si baa8a48a),
  sha1 65277addc8be558922dcdcc7d035426ba3062b8e = F1 + exactly five changes: «R15» → «R15 (a), (d)» and «R57 (a) (premise (VJ))» added
  (F16 (3), precisions); «W-MON» removed from R88's list and «W-MON′» added to R90's list (F16 (2), LINE-REQ); «a REPEAT′ if it is LATE′
  and …» (F16 (1), LINE-REQ). Word diff re-measured for this revision: those changes, nothing else (to check (1)). REFEREE §C l. 83
  «MATCHES (Opus 5.5, D15)»; REFEREE-2 §C.6 l. 126 «line F16 MATCHES §3-§7». F16 supersedes F1; the title is F16 verbatim, with its own
  date. No E-item was raised on any version by either referee; the two REQUIRED items on 4a68934d are line fixes (every-symbol rule and
  t < u), and F16's two LINE-REQ items are line fixes (REPEAT′ ⊆ LATE′; W-MON's scope), not proof gaps (REFEREE-2 §C.6 l. 122: «The
  packet's proofs remain correct with R90 (b) W-MON′ in its place, so no verdict changes.»).
  Setting (one W-run, every game; packet §1 l. 25-49): N5 = SPEC S1-S5 with FIX 1-4; G = (V, E, Ω, owner), n := |V|, n_E the Even vertices,
  m_E the Even edges, d_E(z) the Even edges into z; a run is the sequence of states (σ_t, τ_t), a TRANSITION is t → t + 1; Ξ_t := Ξ_{σ_t}
  with σ̄_t ([S1-Xi]), Iσ_t ([S2]), W_t := the valuation of the (σ_t, τ_t)-plays, λ_W, λ_Ξ their cycle-node maps; D_t := {Odd u : σ̄_t(u) ≠
  τ_t(u)}, Z_t := {v : Ξ_t(v) ≠ W_t(v)}; W-RUN (RESULTS R89) F = [a, b]: τ and λ_W constant, every transition an S4a step; BLOCKED (RESULTS
  R88, P-N5-GP §3, quoted); ADOPTION of (y, z) at u: σ_{u+1}(y) = z ≠ σ_u(y); LEAVE of z by y at k: σ_k(y) = z ≠ σ_{k+1}(y). Standing
  premise (l. 48-49): «RESULTS R57's SPEC premise (S1's procedure realises the optimal counterstrategy; S4a's σ_{u+1} is Even's pointwise
  optimum in its arena), as R88 / R89 / R90 use it.» §1 cells: REFEREE «CHECKED; standing premise named (R57) ✓» (l. 18); REFEREE-2 has no
  §1 row (its §2 l. 31-32 re-derives the setting's uses).
  DEFINITION (not a claim). §2 (l. 51-58): R88 §4's late adoption (quoted verbatim: «… blocked at some state t ∈ [a, τ).») with «t ∈ [a, τ)»
  replaced by «t ∈ [max(a, p + 1), τ), p the previous adoption transition of (y, z) in F (no constraint if there is none)» (LATE′);
  R*′_T(F) := the transitions of F containing at least one LATE′ adoption; FIRST′ / REPEAT′ (a LATE′ adoption with no / with an earlier
  LATE′ adoption of the same edge in F); REP′_F := the REPEAT′ adoptions of F; «Every LATE′ adoption is late in R88's sense, so R*′_T ≤
  R*_T»; «every REPEAT′ is a REPEAT of P-N5-CUT §6 and REP′_F ≤ REP_F». Cells: REFEREE «CHECKED: the diff is exactly «t ∈ [a, τ)» → «t ∈
  [max(a, p + 1), τ)»; LATE′ ⊆ late, R*′_T ≤ R*_T, REP′_F ≤ REP_F ✓» (l. 19); REFEREE-2 «CHECKED: the diff is exactly the stated replacement
  of «t ∈ [a, τ)» by «t ∈ [max(a, p + 1), τ)» (quote verbatim, §3 below); LATE′ ⊆ R88-late, so R*′_T ≤ R*_T; REPEAT′ ⊆ P-N5-CUT §6 REPEAT,
  so REP′_F ≤ REP_F» (l. 15). §Cs: «CHECKED, exact | CHECKED, exact | agreed» (REFEREE §C l. 10); «… | agree» (REFEREE-2 §C l. 9). Neither
  referee signs a definition; both check its diff and its two inclusions, which items (a)-(h) use.
- Claims signed (both referees "(Opus 5.5, D15)": REFEREE successor 19, REFEREE-2 successor 22). Each item (a)-(h) is SIGNED in both
  verdict tables (REFEREE "## Verdicts" l. 15-31 of R-N5-LATEP.md; REFEREE-2 "## 1. Verdict table" l. 12-26 of R2-N5-LATEP.md) and «SIGNED
  by both» / «agree» in both §Cs (REFEREE §C table l. 8-19; REFEREE-2 §C C.1 l. 6-19), in the frozen wording, read with F4, F8-F13 and F15
  (clarifications; no statement text changes). One W-run of plain N5 on every game. Premises LANDED (as line F16 names them: F3 l. 40-41
  with F16 (2), (3)): SPEC S1 ([S1-val], [S1-ord], [S1-Xi]), S2, S4a ([Q] l. 37), S4c; RESULTS R15 (a), (d) (Ξ non-decreasing); RESULTS
  R17 (a) [V1], [V2] (quoted l. 41-43, read for the plays of a fixed positional pair); RESULTS R47 (a) (Σ LCT ≤ n(n − 1)); RESULTS R57 (a)
  premise (VJ) (XW's first part); RESULTS R88 (XW, GP*, FW-R* and its proof); RESULTS R89 (GP*-RUN, LATE-RISE; the W-run); RESULTS R90
  (OPT-OFF (ii), W-MON′ (W monotone at every transition of F: F16 (2)), W-SUCC; off-cycle). The packet's §1 list (l. 38) still names R88's
  W-MON; F16 (2) (fixes l. 170-171): «The packet's §1 premise list (l. 38) should read «R88: Lemma XW, Lemma GP*, Corollary FW-R*; R90 (b):
  Lemma W-MON′»; the frozen packet is not edited.» Standing premise: RESULTS
  R57's SPEC premise as quoted under Object; REFEREE LATEP-N1 (l. 76): «named (R57) ✓; OPT-OFF (i)'s R17 (a) (F1) + R57 (a) chain is
  inherited from R90 (P-N5-CUT K2)». The code's match to SPEC is DATA (R15 G-N5T-1). No item uses a count.
  (a) Corollary FW-R*′ (§3, l. 60-68), with F9: "Every W-run F has WCH_F ≤ (n − 1)(R*′_T(F) + 1), WCH_F := the transitions t → t + 1 of F
      with W_{t+1} ≠ W_t." (R88's proof of FW-R* on F by GP*-RUN, with τ := the first adoption of (y_i, y_{i+1}) after t; its previous
      adoption p satisfies p + 1 ≤ t, so the block at t is in LATE′'s window.) F9 (l. 89-91): «Read «verbatim up to the choice of τ»». Cells:
      REFEREE «SIGNED (§3)» (l. 20); REFEREE-2 «SIGNED», «none. «verbatim» is accurate up to one added choice (τ := the first adoption after
      t), which is valid: N-1» (l. 16).
  (b) Lemma LATE-SPLIT′ (i), (ii) (§4, l. 70-80), with F10: "(i) FIRST′ adoptions of F number at most m_E (one per edge). (ii) Let ρ be a
      REPEAT′ of (y, z) at u, with previous adoption p < u and y's last leave of z at k (p < k < u). Then (y, z) is blocked at some t_b with
      k + 1 ≤ t_b ≤ u − 1. If y is off-cycle for τ (P-N5-CUT §2) at every state of [k + 1, t_b], then W(z) changes at some transition of
      [k + 1, t_b − 1]: W_{t_b}(z) ▷ W_{k+1}(z)." (OPT-OFF (ii) at k → k + 1, W-SUCC on [k + 1, t_b], blocked at t_b.) F10 (l. 93-95): «y
      leaves z exactly once in (p, u), at k. Hence every LATE′ block t ∈ [p + 1, u) has t ≥ k + 1». Cells: REFEREE «SIGNED (§4)» (l. 21);
      REFEREE-2 «SIGNED», «none; N-2 (uniqueness of the leave is implicit)» (l. 17).
  (c) Corollary CIRCLE′ (§4, l. 83-89), with F4 and F15: per W-run, "REP′_F ≤ n_E·R*′_T(F); R*′_T(F) ≤ m_E + REP′_F; REP′_F ≤ X′_F + Σ_z
      d_E(z)·WCH_F(z), where WCH_F(z) := the transitions of F changing W(z) …; WCH_F ≤ (n − 1)(R*′_T + 1) (§3). Hence REP′ polynomial ⟺
      R*′_T polynomial ⟺ (WCH_F polynomial ∧ X′_F polynomial), up to polynomial factors.", X′_F := the REPEAT′s «where y is not off-cycle
      for τ at some state of [k + 1, t_b] (own-cycle)» (l. 81-82). F4 (l. 44-49): t := «the EARLIEST blocked state of [max(a, p + 1), u)»;
      «CIRCLE′'s inequality … holds for every fixed choice»; «Reading the packet's §4 with this choice changes no signed statement.» F15 (l.
      113-115): on F the own-cycle condition «is the same as «λ_W(y) = y»». Cells: REFEREE «SIGNED; X′_F depends on the choice of the
      blocked state t (any fixed choice works): LATEP-N2» (l. 22); REFEREE-2 «SIGNED», «none; the line files them under «Lemma LATE-SPLIT′»
      (L-3)» (l. 18). Both sign the four inequalities and the ⟺ (REFEREE l. 22 «(four inequalities and the ⟺)»; REFEREE-2 l. 18 «(four
      inequalities and the equivalence)»). On LATEP-N2 the referees differ in substance and agree on the fix (Referee strengthening (0)).
  (d) Lemma GAP-CLIMB (§5, l. 91-101), with F11: ZXC_F(z) := the transitions s → s + 1 of F with z ∈ Z_s and Ξ_{s+1}(z) ▷ Ξ_s(z). "Let the
      LATE′ adoption of (y, z) at u have last blocked state t_b (max(a, p + 1) ≤ t_b < u). Let s be the first transition of [t_b, u − 1] at
      which Ξ(z) changes. Then s exists, z ∈ Z_s, and Ξ_{s+1}(z) ▷ Ξ_s(z). Distinct LATE′ adoptions of one edge give distinct s. Hence, per
      W-run, #LATE′(y, z) ≤ ZXC_F(z) and Σ_{(y, z)} #LATE′(y, z) ≤ Σ_z d_E(z)·ZXC_F(z)." (LATE-RISE, R15, [S2], XW, blocked, W-MON on F;
      disjoint windows by LATE′; «W-MON on F» = R90 (b) W-MON′ at each transition of [t_b, s]: F16 (2), fixes l. 165.) Cells: REFEREE «SIGNED (§5)» (l. 23); REFEREE-2 «SIGNED», «none; it sharpens R89 R*-RISE (N-3)» (l. 19).
  (e) Proposition CHAIN (§6, l. 103-111), with F2 and F12: TXC_F(z) := the transitions s of F with Ξ_{s+1}(z) ▷ Ξ_s(z) and W_{s+1}(z) =
      W_s(z); WZ_F(z) := those of ZXC_F(z) with W_{s+1}(z) ≠ W_s(z); GXC_F := the GXC events (v, t) with t, t + 1 ∈ F, GXC as quoted from L-NEW
      box 70 §3 @170e5316 l. 48-49 (l. 106-107; the line inlines it without the τ-clause, automatic on F: F2). "As sets of pairs (vertex,
      transition of F): GXC_F ⊆ TXC_F ⊆ ZXC_F, and ZXC_F(z) = TXC_F(z) ⊔ WZ_F(z) with WZ_F(z) ≤ WCH_F(z)." (W-MON on F, = R90 (b) W-MON′ at t → t + 1: F16 (2), fixes l. 166; XW.) F12 (l. 101-102):
      «(§8 DATA)» reads «(§10 DATA)». Cells: REFEREE «SIGNED» (l. 24); REFEREE-2 «SIGNED», «none; cross-reference «(§8 DATA)» in l. 111
      should be §10 (N-4)» (l. 20).
  (f) Lemma TXC-DESCENT (§7, l. 114-133), with F8 and F13: "Let (z, s) be a TXC event of F, and x_0 = z, x_1, … z's (σ_{s+1},
      σ̄_{s+1})-play. Call x TERMINAL if one of: (T1) λ_Ξ(x) changes at s; (T2) x Even and σ_{s+1}(x) ≠ σ_s(x); (T3) x Odd and x ∈ D_s ∪
      D_{s+1}; (T4) λ_W(x) = x. Let j be the least index with x_j terminal. Then j exists, x_0, …, x_j are distinct, and every (x_i, s), i ≤
      j, is a TXC event. If x_j is T2 and λ_Ξ is unchanged at s, then (x_j, s) is a GXC event." ([V1], strict [V2] both ways; termination on
      the simple prefix to the lasso's cycle node.) F13 (l. 104-106): «before any repetition» holds because c lies on the play's cycle. F8
      (l. 84-87): T4 «is necessary for the proof as written»; no instance shows it necessary for the conclusion. Cells: REFEREE «SIGNED (§7)»
      (l. 25); REFEREE-2 «SIGNED», «none; N-5 (termination argument spelled out)» (l. 21; its row: «(termination included)»).
  (g) Corollary TXC-RED (§7, l. 134-144): with GATE_F := the TXC events (o, s) of F with o Odd, o ∈ D_s ∪ D_{s+1}; CNW_F := the TXC events
      (x, s) of F with λ_W(x) = x; LCT_F := the transitions of F at which λ_Ξ changes: "TXC_F ≤ n·(GXC_F + GATE_F + CNW_F) + n²·LCT_F, and
      over a whole run Σ_F LCT_F ≤ n(n − 1)." (Fibres of the terminal map have size ≤ n; ≤ n TXC events at a λ_Ξ-changing transition; R15
      and injective rewards.) Cells: REFEREE «SIGNED» (l. 26; row «Corollary TXC-RED (and Σ_F LCT_F ≤ n(n − 1))»); REFEREE-2 «SIGNED», «none»
      (l. 22; row «Corollary TXC-RED (and Σ_F LCT_F ≤ n(n − 1) per run)»).
  (h) The composed bound (§7, l. 145): "Σ LATE′_F ≤ n_E·TXC_F + Σ_z d_E(z)·WZ_F(z) ≤ n_E·[n(GXC_F + GATE_F + CNW_F) + n² LCT_F] + Σ_z
      d_E(z)·WZ_F(z)." Cells: REFEREE «SIGNED (d_E(z) ≤ n_E)» (l. 27; row «closing sentence»); REFEREE-2 «SIGNED (arithmetic from §5, §6,
      TXC-RED)» (l. 23; row «composed bound l. 145»). Both §Cs: «SIGNED by both» (REFEREE §C l. 17, with TXC-RED) / «agree» (REFEREE-2 §C l.
      17).
  Gap maps: REFEREE §C l. 20: «Verdicts identical. The gap map is EMPTY: neither referee lists a gap in any proof, and nothing in §2-§7 is
  false.»; REFEREE-2 §C C.2 l. 22: «Proof gaps: NONE in either report. Joint gap map for §2-§7: EMPTY.» REFEREE l. 32: «No gap. Nothing
  FALSE in §2-§7.»; REFEREE-2 l. 28: «No gap in any proof. One REQUIRED fix in the line file (L-1). Everything else is a note.»
  The RESULTS line (F16) claims less than the packet: it states FW-R*′, CIRCLE′'s three inequalities (not FW-R*′'s repeat in CIRCLE′ nor
  the ⟺), GAP-CLIMB's per-edge form (not its sum form nor «z ∈ Z_s»; REFEREE-2 l. 104: «a weakening, allowed»), CHAIN without «WZ_F(z) ≤
  WCH_F(z)», and TXC-RED with the LCT sum; LATE-SPLIT′ (ii), TXC-DESCENT itself and the composed bound (h) are signed items behind it, not
  stated in it. Every clause it states is one of (a)-(g). F16 changes no clause: its REPEAT′ edit narrows the defined set back to
  packet §2 (REFEREE-2 §C.6 l. 126: «the REPEAT′ change narrows the line»), and its label edits change premises named, not statements.
- Fixes (docs/si/P-N5-LATEP-fixes.md, L-SI successor 32, APPEND-ONLY, written «from 2026-10-30 06:50Z (date -u)» (l. 2); two commits:
  (1) l-si 17a3ecec6deaecc26090f0ccf313f8314623f2ec, 2026-10-30T06:51:07Z, F0-F15 and F-SYM, sha1 a690dc2504ed8c11c554d83bc0dc45a3051973de,
  148 lines, merged into trunk by c3c20012; (2) l-si baa8a48ad2d98f5cb67aee47e6468d80465edcd8, 2026-10-30T07:45:41Z, F16 appended
  (`git diff --numstat 17a3ecec baa8a48a`: +39/−0; the first 148 lines hash to a690dc25… unchanged), sha1
  66c85a168022bf08af630ddcd0df494b09a5733c, 187 lines, = l-si head = origin trunk 978d5a8e, merged into trunk by a98e0f3b (08:06:51Z); the
  last commit touching the file. Commit (1) adds the F1 line file, fixes txcd.py
  (`git diff --numstat b63f2554 17a3ecec -- experiments/si/odd/txcd.py`: +7/−3), adds odd/out/txcd_corpus_f1.txt (719 lines) and re-derives
  si/check.sh «box 52» (+3/−2). Classes (l. 8-13): LINE-REQ, LINE-PREC, DATA, NOTE-ACC («accepted as a clarification of the packet's text,
  with no change to any signed statement»), NOTE-READ («concerns the §8 READING, not signed»). Each item, with its class and the referees'
  words (REFEREE §C §4 (2) l. 62-68; REFEREE-2 §C C.5.3 l. 85-93):
  - F0 (l. 15-27): the corrected line F1 (sha1 a85759a2…), F0's five word changes «and nothing else»; the title until F16. Both: MATCHES
    (Object (2)); superseded by F16.
  - F1 (l. 29-31) LINE-REQ: «(a ≤ t < u if there is none)» (REFEREE-2 L-1 = J-1). REFEREE-2: «F1 NARROWS the literal frozen line back to
    §2» (l. 87).
  - F2 (l. 33-36) LINE-REQ: GXC_F inlined (REFEREE LATEP-L1 = REFEREE-2 L-2 = J-2); «The packet's §9 row «GXC_F … landed» was wrong». REFEREE-2:
    «F2 is equivalent on F» (l. 87).
  - F3 (l. 38-42) LINE-PREC: «F = [a, b]», the landed premises named, CIRCLE′ labelled (LATEP-L3 / LATEP-N3 = L-3 = J-3); SUCC-MON not named
    (used by no proof; both referees checked, to check (4)).
  - F4 (l. 44-49) LINE-PREC: X′_F's t := the earliest blocked state (LATEP-N2 / LATEP-L2 = L-4 = J-4). REFEREE: «F4 (earliest t) changes no
    signed statement (CIRCLE′ holds for every fixed choice).» (l. 68); REFEREE-2: «F4 fixes a choice that does not affect X′ on F» (l. 88).
  - F5 (l. 51-67) DATA: txcd.py read W with the old τ after a τ-change (LATEP-D1 = N-7); fix «if nt != t: w1, wk1 = W(ns, nt)»; corrected
    counts (Data). REFEREE: «D1 and D2 are closed.» (l. 74); REFEREE-2: «N-7 and N-8: CLOSED.» (l. 104).
  - F6 (l. 69-78) DATA: T4 test and CNW counter added (LATEP-D2 = N-8); «§10's «0 T4» is corrected to «5 T4 terminals, CNW 71»»; box 52's
    «a T4 vertex … would appear as a failure» «Withdrawn».
  - F7 (l. 80-82) NOTE-READ: §8 «REP′* ≤ REP* ≤ T» reads «REP′* ≤ REP* ≤ n·T» (LATEP-N4). Not signed (§8).
  - F8 (l. 84-87) NOTE-ACC: T4 used by the proof, not exhibited (LATEP-N5; REFEREE MUT 4, REFEREE-2 X_noT4 0 / 5).
  - F9 (l. 89-91) NOTE-ACC: «verbatim up to the choice of τ» (N-1).
  - F10 (l. 93-95) NOTE-ACC: the leave in (p, u) is unique; every LATE′ block has t ≥ k + 1 (N-2; REFEREE §4).
  - F11 (l. 97-99) NOTE-ACC: GAP-CLIMB refines R89's R*-RISE (N-3; REFEREE MUT 5).
  - F12 (l. 101-102) NOTE-ACC: «(§8 DATA)» → «(§10 DATA)» (N-4).
  - F13 (l. 104-106) NOTE-ACC: termination in §7 (N-5).
  - F14 (l. 108-111) NOTE-READ: NOT LANDED (unchecked READING). Its first sentence restates REFEREE-2 N-6's hypothesis for §8's box-40
    remark («holds when j − 2, j − 1, j lie in one W-run»); its new claim «Box 41 §4 already charges the other case to the λ_W-change (≤ Λ)»
    was checked by neither referee. REFEREE-2 §C l. 90-91: «F14 adds a new claim, «Box 41 §4 already charges the other case to the
    λ_W-change (≤ Λ)». I did not check that claim. It is READING only and not to land.»; REFEREE §C l. 65 classes it with F7 («correct the
    §8 READING (not signed)») without checking the new claim. This entry carries neither.
  - F15 (l. 113-115) NOTE-ACC: on F, own-cycle = «λ_W(y) = y» (N-9); the line keeps P-N5-CUT's wording.
  - F-SYM (l. 117-141): the lane's strict symbol test of F1: «no free symbol … No unlanded source remains (box 70 is gone from the line).»
    REFEREE §C l. 61: «The F-SYM table agrees.»; REFEREE-2 §C.5.2 (own test): «no free symbol, no unlanded binder». (This draft's own test
    found the two defects of F1 that F16 resolves: to check (5b).)
  - F16 (l. 150-187), classes LINE-REQ ((1) REPEAT′, «the same class as F1», l. 153; (2) the W-MON label, l. 158) and (3) «Precisions
    (the Lead's optional items, both included)» (l. 172; no class word; LINE-PREC by content): the line F16 (sha1 65277add…) = F1 + the five
    changes (l. 176-181); THE TITLE. Heading (l. 150): «Lead 07:46Z (the R92 drafter's strict symbol test of line F1, a85759a2)». (1) «a
    REPEAT′ if it is LATE′ and (y, z) has an earlier LATE′ adoption in F» (l. 157); (2) W-MON dropped from R88's list, W-MON′ added to R90's,
    with a use-by-use check of §3-§7 (l. 164-171); (3) «R15 (a), (d)» and «R57 (a) (premise (VJ))» (l. 173-175). Its own strict symbol test
    (l. 182-185): «Result: no free symbol, no unlanded source.» DONE l. 186: «FINDINGS: two LINE-REQ items accepted; no signed statement
    changes.» REFEREE §C l. 83: «MATCHES (Opus 5.5, D15).»; REFEREE-2 §C.6 l. 126: «F16's two items are corrections, with no widening; the
    REPEAT′ change narrows the line.» Both referees re-measured the fixes sha1 66c85a16… (REFEREE l. 83; REFEREE-2 l. 106).
  Header (l. 5): «Both referees SIGNED every PROVED item (§3-§7) with no gap.»; DONE l. 146-147: «No signed statement changes.» Neither
  referee finds a widening: REFEREE §C l. 62: «F0-F15 are corrections or clarifications only; nothing widens.»; REFEREE-2 §C l. 93: «No
  statement of §3-§7 is widened. No new hypothesis is dropped. The new line claims nothing the frozen line did not.» No quote check is pinned
  for the fixes file. F16 (written after both referees' §C on F0-F15) is covered by their F16 checks (REFEREE §C l. 83; REFEREE-2 §C.6).
- Not signed: §2 Definition LATE′ (a definition, CHECKED by both: Object); §8 READING (R1)-(R3) on landed R90 read with LATE′ and the box-40
  remark (l. 147-159; «NOT TO SIGN»), with F7 and F14's first sentence (Referee strengthening (ii), (iii)); §9 the lane's symbol test of the
  frozen line (superseded by F-SYM; its row «GXC_F … landed» was wrong, F2); §10 READING and DATA (Data below); the frozen line 4a68934d
  (history); the line F1 a85759a2 (history, superseded by F16); F14's new claim (not landed); the working notes N5-ADD-box50, N5-LATEP-box51, N5-TXCD-box52 (l. 7). Lane work after the freeze,
  other than the fixes commits 17a3ecec and baa8a48a (F16), is not part of this entry (L-SI's handover 1f678c1c and later work; L-NEW boxes 72-75; L-RED
  R131-R133, except R131's addendum 7e85ead2, cited under Data for the Oink check of the TIED-RB instance).
- Referee strengthening (NOT part of this entry; remarks of one referee, remarks of both outside the verdict cells, readings):
  (0) X′_F and the choice of t: REFEREE LATEP-N2 (l. 50-52): «If several blocked states exist, X′ depends on the choice (existential and
  universal readings differ); the inequality holds under every fixed choice»; REFEREE-2 N-9 (l. 163-164) and §C C.3 l. 38: «DISAGREE in
  substance, agree on the fix. On a W-run λ_W is constant (R89), and P-N5-CUT §2's off-cycle is «v is not the cycle node of its
  W^τ-value», so it does not depend on the state, hence not on t: X′_F is choice-free.»; REFEREE §C l. 34: «I accept that: it makes L-4 /
  my L2 a wording point only». F4 fixes the earliest t; F15 records λ_W(y) = y. No signed statement depends on the choice.
  (i) TXC-RED's n²: REFEREE l. 71 «at λ_Ξ-changing s at most n TXC events (the packet's n² is a weaker valid bound)»; REFEREE-2 §C l. 44
  «agreed (both sign; n·LCT_F suffices)». Outside the verdict cells; the entry signs the packet's n²·LCT_F.
  (ii) §8 READING (R1)-(R3), NOT signed: with LATE′, R90's R*-REP, WV-R and CUT-RED would read with R*′_T, REP′_F and REP′* := max_F REP′_F ≤
  REP* (l. 151-157). REFEREE-2 l. 24: «not signed (READING); checked for consistency: (R1)-(R3) follow from §3-§4 and REP′* ≤ REP*»;
  REFEREE l. 28: «not signed; one slip: «REP′* ≤ REP* ≤ T» should read «≤ n·T» (K1 gives REP* ≤ n·T)» (LATEP-N4; F7; REFEREE-2 §C l. 40
  «REFEREE right; I MISSED it.»). Landed R90 is unchanged; nothing here restates it.
  (iii) §8's box-40 remark («box 40's LATE re-entries ([C1]) are LATE′», l. 158-159), NOT signed: REFEREE-2 N-6 (l. 149-151) «j − 2 and j − 1
  are in the same W-run only if the transition j − 2 → j − 1 keeps λ_W. Not signed»; F14's first sentence accepts that hypothesis; F14's
  second sentence is unchecked and not landed (Fixes).
  (iv) T4's necessity not exhibited: REFEREE MUT 4 «never bites» (l. 73, l. 119); REFEREE-2 «X_noT4 never bit (0 of the T4-only
  terminals)» (l. 136); F8. The T4 case stays in the signed lemma.
  (v) Controls that bite: REFEREE (l. 118-119) MUT 1 (LATE-SPLIT′ (ii) on R88-late REPEATs) 20, MUT 2 (GAP-CLIMB's s searched from a) 490
  (+2 token collisions), MUT 3 (no T3) 22,586, MUT 5 (GAP-CLIMB on R88-late adoptions) 20 token collisions; REFEREE-2 X_noT3, X_noT2 «bite
  often» (l. 135). DATA.
  (vi) «So W-silent and SELF repeats (P-N5-CUT §6 (iii)) do not occur under LATE′» (packet l. 81): REFEREE l. 46 «W-silent and SELF repeats
  are excluded ✓ (the block lies after the leave)»; REFEREE-2 XSIL 0 on every set (l. 115). Not a row of either table.
  (vii) §10 READING (l. 190-191): «the descent of §7 breaks only at Odd gates (σ̄ ≠ τ) and own W-cycle nodes, never at τ-changes … The live
  terms are GATE (tied Ξ-climbs at gates) and WZ (the W-change circle at gap climbs).» F5 l. 67: «The READING «gates carry the descent»
  stands: 14,136 / 14,739 = 95.9 %.» Not signed.
  (viii) Self-corrections: REFEREE §C l. 39: «I MISSED this in my symbol test» (L-1); REFEREE-2 §C C.4 l. 53-54: «I MISSED: that box 70 is
  not landed (J-2 is REQUIRED, not precision); §8's «≤ T» slip (LATEP-N4); naming the landed premises in the line (part of J-3).»
  At F16: REFEREE §C l. 83 «I MISSED both defects in my F1 test; the drafter caught them.»; REFEREE-2 §C.6 l. 119 «BOTH referees
  MISSED» (REPEAT′) and l. 121 «BOTH referees MISSED it too» (W-MON scope).
- Honest limits: (i) A REDUCTION, per W-run. The line bounds W-changes by R*′_T, R*′_T and REP′_F by each other, REP′_F by X′_F and the
  W(z)-changes, LATE′ adoptions by gap climbs, and tied climbs TXC_F by GXC_F, GATE_F, CNW_F and LCT_F; GATE_F, CNW_F, GXC_F, WZ_F(z) and
  REP′_F are not bounded here (nor X′_F); only Σ_F LCT_F is bounded on a run. Packet l. 8-9: «No count is bounded here; G-N5-TIME stays OPEN.
  Not a TARGET.md claim, not an algorithm claim.»; REFEREE l. 12-13 and REFEREE-2 l. 9-10 say the same. (ii) LATE′ is a new, narrower
  notion of late adoption (R*′_T ≤ R*_T, REP′_F ≤ REP_F); the landed R88, R89 and R90 bounds are unchanged; reading R90 with LATE′ is §8's
  unsigned READING. (iii) CIRCLE′'s ⟺ is «up to polynomial factors». (iv) TIED-RB is DEAD (Data): tied climbs alone do not pay every repeat;
  the live terms named by the lane are GATE_F and WZ_F (unsigned READING). (v) Standing premise: R57's SPEC premise (1E-N3; for S4a, R67's
  P2 / R88's [OPT-H] form), through R88's XW (with R57 (a) (VJ)) and R90's OPT-OFF and W-MON′; the code's match to SPEC is DATA (R15 G-N5T-1). (vi) Counts are
  transitions and events, not bit operations; no running-time bound. (vii) Not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME
  stays open.
- Data (DATA, not proof): pinned (packet §10 l. 199: «Pinned checks: si/check.sh «box 51», «box 52», «box 53».»). experiments/si/check.sh at
  b63f2554: sha1 18525efc0719c0878fbda9d78fb41e162da9c7e1, 860 lines, blocks l. 845-860; at 17a3ecec: sha1
  3bc97c247d301002e53c615495e0391531c03b9c, 861 lines, blocks l. 845-861 (`git diff b63f2554 17a3ecec -- experiments/si/check.sh`: +3/−2,
  only «box 52»: the two txcd.py pins re-derived (F5, F6) and the new b5_o11 pin). Files at 17a3ecec: odd/txcd.py
  1a991675bdd9d16a2f65eaf6cc4ac78ae8dcc3aa (83b3d18cd98c6fa7c0e393f14084216190258879 at b63f2554), odd/latep.py
  6e7652a91336bc94cc2f995bda94e3a1558c4646 and odd/tied.py daf3951683a571c1d55b64fbcd08f894cc562d96 (both unchanged since b63f2554),
  rund/quotecheck.py 29bb4a971680c9278f5f8c6f40eac17c0134db72, odd/inst/si51/tiedmut_so_th_n32_11.pg
  4ce2df5704937437f9f8617ab580b85053c35aba (.start c3430f635c928e59a84e75423d9bf75867164f02), red/so/instances/so_th_n32.pg
  ae9126ad1bf963114bdd56b6e50c8c1cc571779e, n5-exhaustive/instances/b5_o11.pg db4fe55a650236dfe1bc5030f0ca123c75754764,
  odd/out/txcd_corpus_f1.txt 6d9fd80dcd75486c2cf16792845fc5c471e16bd2. Re-run for this draft from a `git archive` of 17a3ecec (experiments/
  and docs/si/; `python3 -I`; GIT_DIR set to this repository for the quote check; outputs to scratch files; exit codes read): l. 845-861
  under `set -euo pipefail`, 07:30:47Z-07:30:50Z by date -u: «si (box 51: LATE', GAP-CLIMB, TIED-RB dead): PASS», «si (box 52: TXC descent):
  PASS», «si (box 53: P-N5-LATEP quotes): PASS», rc 0. Single outputs from the same archive (same session, not separately stamped): txcd.py
  so_th_n32 «TXC 73 T1 0 T2G 0 T2L 0 T3 73 T4 0 DESC_V 0 CYC_V 0 TERM_V 0 GXC 0 GATE 16 CNW 0 MULT 13»; tiedmut_so_th_n32_11 «TXC 77 … T3 77
  T4 0 … GATE 10 CNW 0 MULT 14»; wdepth_K4_m16 «TXC 184 … T3 184 T4 0 … GATE 93 CNW 0 MULT 32»; b5_o11 «TXC 1 … T3 1 T4 0 … GATE 1 CNW 1 MULT
  1»; tied.py tiedmut «rep 1 tied 0 untied 1 reblk 1 untied_reblk 1 tsh 0»; latep.py tiedmut «WCH 19 RT 4 RTP 4 REPP 1 XP 0 FWV 0 RSUB_V 0 LP
  6 GAPV 0 GTOKV 0 TIEDG 4»; quotecheck «quotes=6 bad=0», «QUOTES PASS»; --mut «quotes=6 bad=6», «QUOTES FAIL». Every run rc 0.
  DATA OF RECORD (F5 / F6, l. 56-62 and l. 71-74; corpus odd/sbcg.lst, 719 games, S3 start; file odd/out/txcd_corpus_f1.txt, summed for
  this draft by script: equal): TXC 14,739; terminals T1 292, T2 (GXC) 306, T2L 0, T3 14,136, T4 5 (all in tcR4_N6: «TXC 71 … T3 66 T4 5 …
  CNW 1 MULT 40»); GXC events 191; CNW 71; descent failures (DESC_V, CYC_V, TERM_V) 0; txcd.py's distinct gate terminals 2,416; largest MULT
  83. Pins: so_th_n32 TXC 73 / gate terminals 16; tiedmut_so_th_n32_11 TXC 77 / 10; wdepth_K4_m16 TXC 184 / 93 (unchanged); b5_o11 CNW 1,
  terminal T3 (REFEREE-2's N-8 instance: «Odd 7 has τ(7) = 7 (own W-cycle node …) and σ̄(7) = 2 (a gate)», l. 159-161). REFEREE-2 §C C.5.4
  l. 98-100: «TXC 14,739; T1 292; T2 (GXC) 306; T2L 0; T3 14,136; T4 5; GXC events 191; gate terminals 2,416; CNW 71; MULT 83; DESC_V / CYC_V
  / TERM_V 0. These equal my engine's corpus figures in every field»; REFEREE §C l. 70: «so_th_n32 TXC 73 / gates 16 and
  tiedmut_so_th_n32_11 TXC 77. These equal my engine (73; 77) and REFEREE-2's.» SUPERSEDED, not data of record (F5 l. 63-65, F6 l. 77):
  box 52 §4 / packet §10 (l. 197) corpus TXC 14,526, T1 356, T2 292, T3 13,878, GXC events 227 (the old file odd/out/txcd_corpus.txt, kept
  as the record; summed for this draft: TXC 14,526, T1 356, T2G 292, T3 13,878, GXC 227), «0 T4»; the old «box 52» pin so_th «TXC 63 … GATE
  15» and tiedmut 66 / 9; box 52's «CNW is 0 in all data».
  Other packet DATA (§10 l. 192-198, not revised by F5 / F6): «FW-R*′ violations 0; LATE′ adoptions that are not R88-late 0»; latep.py's
  REPP «≥ REP′_F», its W-silent count 0; «GAP-CLIMB violations 0, repeated tokens 0»; «TXC descent failures 0». REP′ of record (REFEREE-2 l.
  128-130): corpus REP′ 4 (max 3 per W-run) = the re-blocked REPEATs; «box 51 §5's «max REP′ 9» is the tool's REPP; the frozen REP′ maximum
  is 3».
  KILL recorded with this packet (packet §10 l. 198): «TIED-RB (TXC alone pays every REPEAT′) is DEAD: odd/inst/si51/tiedmut_so_th_n32_11
  (two engines identical; Oink NOT RUN).» CONJECTURE TIED-RB (L-SI box 50 §6; statement killed, box 51 §1 (l-si 7dd85b02): «every re-blocked
  REPEAT of (y, z) has a tied Ξ-climb of z on [k, u − 1]», tied meaning Ξ_{s+1}(z) ▷ Ξ_s(z) and W_{s+1}(z) = W_s(z)) is DEAD. Instance:
  L-SI box 51, odd/inst/si51/tiedmut_so_th_n32_11.pg / .start (sha1 4ce2df57… / c3430f63…), n 32, 34 iterations, 0 fallbacks: one
  re-blocked REPEAT with no tied climb (tied.py «rep 1 tied 0 untied 1 reblk 1 untied_reblk 1», re-run above); two engines identical
  (red/seg/xeng.py «state sequences identical: True», «box 51»). Oink-verified by L-RED 7e85ead2 (docs/red/R131-tied-rb.md addendum l.
  76-83): «zielonka(oink zlk) OK strategies verified»; «So L-SI's kill and R131's family are two independent TIED-RB kills: box 51 is one
  REPEAT at n 32; R131 is Θ(n²) per W-run.» (L-RED R131, 011213ef: (K − 1)(m − 2) untied re-blocked REPEATs in one W-run.) Both referees
  re-ran «box 51» (PASS; REFEREE l. 110-111, REFEREE-2 l. 64); REFEREE-2 reproduces tiedmut's latep.py figures («tiedmut RTP 4, REPP 1, LP 6,
  TIEDG 4», l. 133-134). DATA; no signed item uses it.
  REFEREE (successor 19; own docs/referee/scratch/latep_probe.py on rl_engine, no lane code; pinned l. 845-860 run in a clean `git worktree add
  --detach` at b63f2554: three PASS lines, exit 0, l. 110-111): corpus sbcg.lst + wdepth_K4_m16 and tiedmut_so_th_n32_11 with their starts,
  given start and S3, n ≤ 120: 672 games (49 with n > 120 skipped), 767 runs, 13,205 transitions, 1,089 W-runs of length ≥ 1; 0 violations
  of SUB (LATE′ ⊆ late), FW-R*′, LATE-SPLIT′ (ii), CIRCLE′ (all four), GAP-CLIMB (1,500 LATE′ adoptions), CHAIN (ZXC 28,114 = TXC 23,975 ⊔
  WZ 4,139; GXC 198 ⊆ TXC), TXC-DESCENT (23,975 descents: T1 497, T2 319, T3 23,123, T4 36), TXC-RED, Σ LCT ≤ n(n − 1); REPEAT′ 2 (X′ 0)
  against 1,520 R88-late adoptions; MUTs as in Referee strengthening (v) (l. 112-119). Its T4 36 / CNW 110 are on that run set, not the
  data of record (F6 l. 77-78; REFEREE §C l. 73-74).
  REFEREE-2 (successor 22; own docs/referee-2/R2-N5-LATEP/latep_check.py on its lane's R2-N5-DUAL/dual_check.Runner («SPEC N5 written from
  S1-S5 + FIX 1-4 on si.py's Engine, read-only»), own play value; «The lane's odd/latep.py, txcd.py, tied.py and new/box21/n5x.py are NOT
  imported», l. 108-109; pinned «box 51»-«box 53» re-run from its own extraction in a detached worktree at b63f2554, set -euo pipefail, exit 0,
  l. 63-67; at 17a3ecec, §C l. 59-60): brute-force Ξ control on 1,600 runs / 400 random games n 5-9 (3,819 states, 0 mismatches, l.
  112-113); corpus sbcg 719 runs, 5,419 W-runs, max WCH 159, max R*_T 17, max R*′_T 17, max REP′ 3 (sum 4), REPA 9 (sum 40), LATE′ 1,104,
  GAP-CLIMB tied / WZ 1,003 / 101, TXC 14,739, GXC 191, GATE 2,464, CNW 71, violations 0; latew_K20_m32 (n 538) REP′ 570, TXC 3,941;
  wdepth_K4_m32 (n 234); pins; random n 5-80, 3,800 runs (l. 118-125); every check 0 on every set (l. 114-116); its counts equal latep.py's
  printed figures (l. 131-134). No signed statement uses any count.
- Signatures: REFEREE docs/referee/R-N5-LATEP.md (report 5bdd5d6d0caf2c5895c803aab0e6360d2d0d250e, 2026-10-30T06:32:36Z, committed
  directly on claude/referee (file commit = branch commit), merged into trunk by 9a7a5af1 (06:48:53Z); sha1
  477ff68d4c510bb12b50acfa8167012a1ad23e0c, 125 lines, unchanged since, = local trunk head; successor 19): §1 CHECKED; §2 CHECKED; FW-R*′,
  LATE-SPLIT′, CIRCLE′, GAP-CLIMB, CHAIN, TXC-DESCENT, TXC-RED, the closing sentence SIGNED; «No gap. Nothing FALSE in §2-§7. Two DATA
  defects in the lane's txcd.py (LATEP-D1 frame bug, LATEP-D2 no T4 test), affecting no proof.» (l. 32). §C docs/referee/R-N5-LATEP-C.md
  (ce923e20f29467a1c62e3111914131199812ced4, 2026-10-30T06:49:48Z, sha1 0e0dd5881eb44ed5c1a1513d28c31adef0be4112 there, 51 lines; merged into
  trunk by ac4fae23, 07:11:26Z); §4 addendum 9d47dcbbe9e2c5ed08269da0c6d1fd41090c2ba5 (2026-10-30T07:01:49Z, `git diff --numstat ce923e20
  9d47dcbb`: 32 added, 1 removed (the old NEEDS line, replaced); sha1 1d1fd20045378566954795f4fcbd0217dff9c676, 82 lines there; merged
  into trunk by 04705e43 (07:23:16Z), now on origin trunk 978d5a8e): «F1 MATCHES» (l. 75); F16 line
  11259154c8efaeb3eb34181e921df0116d0ed61a (2026-10-30T08:07:56Z, `git diff --numstat 9d47dcbb 11259154`: 1 added, 0 removed; re-measured
  at the origin head for this revision: sha1 c597afbd630a51bdecf3c9c3c93c5ea56c84a2cd, 83 lines, = referee head = the last commit touching
  the file; merged into the local trunk by 809941a6 (08:19:19Z), not on origin trunk 978d5a8e at this revision's fetch): «MATCHES (Opus
  5.5, D15)» (l. 83), with «I MISSED both defects in my F1 test; the drafter caught them.» REFEREE-2 docs/referee-2/R2-N5-LATEP.md (report e7b538a9f0f97cbb37b55ef0ff76e398a66ee082, 2026-10-30T06:32:02Z, committed
  directly on claude/referee-2 (file commit = branch commit; its parent 282f241f is a merge of trunk into the branch), merged into trunk by
  a44f3b30 (06:48:53Z); sha1 00ca428a58c50e23e534229819000d67fd2e3636, 178 lines (= REFEREE §C l. 4's «sha1 00ca428a…, 178 lines»),
  unchanged since; successor 22): §2 CHECKED; every PROVED item SIGNED; «No gap in any proof. One REQUIRED fix in the line file (L-1).
  Everything else is a note.» (l. 28). §C docs/referee-2/R2-N5-LATEP-C.md (917b32d4c43914a6f7671e2299f1cb6f98706010, 2026-10-30T06:55:27Z,
  sha1 9217d1b1e586210332d014b3fff020d8368c7326 there, 64 lines; merged into trunk by 134ecf4e, 07:11:27Z); §C.5
  42ab528b77d9cef9a4920879cf171eddab580edd (2026-10-30T07:07:34Z, `git diff --numstat 917b32d4 42ab528b`: 53 added, 2 removed (the old NEEDS
  lines, replaced); sha1 3ffc286befd6386b83990958f9f537b520536f27, 115 lines there; merged into trunk by 0396db78 (07:23:16Z), now on
  origin trunk 978d5a8e): «line MATCHES» (§C.5.2 l. 82-83; FINDINGS l. 111-113 there, l. 133-135 now); §C.6
  aa3661494a734e5ca10d2a7f7976ba0b09f72168 (2026-10-30T08:07:48Z, `git diff --numstat 42ab528b aa366149`: 22 added, 0 removed, l. 106-127;
  its parent a3b42e1e is a Lead trunk commit; re-measured at the origin head for this revision: sha1
  83283e5836ccabc2b71eb33efeaa5a197b18d6bc, 137 lines, = referee-2 head = the last commit touching the file; merged into the local trunk
  by 30be80e0 (08:19:20Z), not on origin trunk 978d5a8e at this revision's fetch): «Verdict (Opus 5.5, D15): line F16 MATCHES §3-§7.»
  (l. 126); it confirms the use-by-use claim (l. 110-118) and records that both referees missed both defects (l. 119, l. 121). Its DONE /
  FINDINGS / NEEDS (l. 128-137) were not revised for F16 (to check (2)). INDEPENDENCE: REFEREE l. 7: «Independence: no docs/referee-2/ file opened for this packet.»; REFEREE §C l. 3-4: its report
  «pushed BEFORE I opened REFEREE-2's», REFEREE-2's report «opened 06:49Z after the Lead's word». REFEREE-2 l. 4: «Independence: written
  before opening any docs/referee/ file (names-only count of «latep» in docs/referee/ at the start: 0).»; REFEREE-2 §C l. 2-3: its report
  «pushed before any docs/referee/ file was opened», REFEREE's «opened after the Lead's word at 06:49Z». No review imported lane code
  (REFEREE l. 112 «no lane code»; REFEREE-2 l. 108-109); the lane's scripts ran only as the pinned blocks.
  §C (both): verdicts identical (REFEREE §C l. 20, quoted under Claims signed; REFEREE-2 §C C.2 l. 22); one disagreement in substance, on
  a note, not a verdict (LATEP-N2 vs N-9; Referee strengthening (0)). Fixes: REFEREE §C l. 62 «F0-F15 are corrections or clarifications
  only; nothing widens.»; REFEREE-2 §C l. 86-93 «YES. … No statement of §3-§7 is widened.» Notes map (REFEREE §C §2 l. 28-40; REFEREE-2 §C
  C.3 l. 34-50): LATEP-D1 = N-7, LATEP-D2 / LATEP-N5 = N-8, LATEP-L1 = L-2, LATEP-L2 / LATEP-N2 = L-4 / N-9, LATEP-L3 / LATEP-N3 = L-3;
  REFEREE only LATEP-N1, LATEP-N4 (and LATEP-L3's premise names); REFEREE-2 only L-1, N-1..N-6.
- TARGET.md diff: «n the number of vertices» is TARGET.md §1 l. 8's n («n = |V|, m = |E|»); m_E ≤ m. Not a claim of TARGET.md section 1
  or §2 (structural lemmas and inequalities on one W-run of N5, a REDUCTION of W-changes, late adoptions and tied climbs to counts that are
  not bounded; no bound on a run, no running-time bound, no algorithm claim). GAPS G-N5-TIME: open.

Proposed GAPS line-11 UPDATE (append-only), after R91's UPDATE of G-N5-TIME (GAPS l. 11, «UPDATE 2026-10-30 05:59Z: RESULTS R91 (P-N5-GAP;
…)», the last on the line), re-built for this revision only from the clauses of the title line F16 (no "|" in F16 or in the UPDATE; the same
construction as the pre-F16 draft, which reproduces its F1 UPDATE exactly; landing time and CHECKER commit to be filled at landing): «UPDATE
2026-10-30 <HH:MM>Z: RESULTS R92 (P-N5-LATEP; CHECKER C102 <checker>) [refereed-only] LANDED: in every W-run F = [a, b] of N5 (SPEC S1-S5)
on any game, under the standing SPEC premise of RESULTS R57, with RESULTS R15 (a), (d), R17 (a), R47 (a), R57 (a) (premise (VJ)), R88
(Lemmas XW, GP*, Corollary FW-R*), R89 (Lemmas GP*-RUN, LATE-RISE) and R90 (Lemmas OPT-OFF (ii), W-MON′, W-SUCC) (W-run, W_t, λ_W as in
RESULTS R89: τ and λ_W constant on F, no S4c fallback; Ξ_t, σ̄_t, Iσ_t and the order ⊴ (▷ strict) as in SPEC S1-S2, λ_Ξ the cycle-node map
of Ξ_t; BLOCKED as in RESULTS R88; n the number of vertices, n_E of Even vertices, m_E of Even edges, d_E(z) of Even edges into z; an
adoption of (y, z) at u: σ_{u+1}(y) = z ≠ σ_u(y)), call an adoption of the Even edge (y, z) at u LATE′ if (y, z) is blocked at some state t
of F with p + 1 ≤ t < u, p its previous adoption in F (a ≤ t < u if there is none), a REPEAT′ if it is LATE′ and (y, z) has an earlier LATE′
adoption in F, and let R*′_T be the transitions of F containing a LATE′ adoption, REP′_F the REPEAT′s of F, X′_F those REPEAT′s of (y, z) at
u for which y is not off-cycle for τ (P-N5-CUT §2) at some state of [k + 1, t], k the last k < u with σ_k(y) = z ≠ σ_{k+1}(y) and t the
earliest blocked state as in the definition of LATE′, WCH_F the W-changing transitions of F and WCH_F(z) those changing W(z), Z_s := {v :
Ξ_s(v) ≠ W_s(v)}, D_s := {Odd o : σ̄_s(o) ≠ τ(o)}, and, over the transitions s → s + 1 of F (s, s + 1 in F): ZXC_F(z) those with z ∈ Z_s and
Ξ_{s+1}(z) ▷ Ξ_s(z), TXC_F(z) those with Ξ_{s+1}(z) ▷ Ξ_s(z) and W_{s+1}(z) = W_s(z), WZ_F(z) those of ZXC_F(z) with W_{s+1}(z) ≠ W_s(z),
GXC_F the pairs (v, s) with v Even, σ_{s+1}(v) ≠ σ_s(v), λ_Ξ unchanged at s → s + 1, v ∈ Z_s, Ξ_{s+1}(v) ▷ Ξ_s(v) and W_{s+1}(v) ⊴ W_s(v),
GATE_F the pairs (o, s) with o Odd in D_s ∪ D_{s+1} and s in TXC_F(o), CNW_F the pairs (x, s) with λ_W(x) = x and s in TXC_F(x), LCT_F the
transitions at which λ_Ξ changes, TXC_F and ZXC_F the sets of pairs (z, s) with s in TXC_F(z), resp. ZXC_F(z), and in every inequality a set
stands for its number of elements: WCH_F ≤ (n − 1)(R*′_T + 1) (Corollary FW-R*′); R*′_T ≤ m_E + REP′_F, REP′_F ≤ n_E·R*′_T and REP′_F ≤ X′_F
+ Σ_z d_E(z)·WCH_F(z) (Lemma LATE-SPLIT′, Corollary CIRCLE′); the LATE′ adoptions of each Even edge (y, z) in F number at most ZXC_F(z)
(Lemma GAP-CLIMB); GXC_F ⊆ TXC_F ⊆ ZXC_F as sets of pairs (vertex, transition), and ZXC_F(z) is the disjoint union of TXC_F(z) and WZ_F(z)
(Proposition CHAIN); TXC_F ≤ n·(GXC_F + GATE_F + CNW_F) + n²·LCT_F, with the sum of LCT_F over the W-runs of a run at most n(n − 1) (Lemma
TXC-DESCENT, Corollary TXC-RED): a REDUCTION; GATE_F, CNW_F, GXC_F, WZ_F(z) and REP′_F are not bounded here. G-N5-TIME stays open.»
