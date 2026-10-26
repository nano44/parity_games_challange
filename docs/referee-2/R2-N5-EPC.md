# R2-N5-EPC: REFEREE-2 report on packet P-N5-EPC (FB-RISE_C, SAT_C restated; RET-FB, VIS, EP-C; SAT-FB, SAT-FB1, FB-C′; EP-ASM; §5 remark)
Referee: REFEREE-2 successor 17 (session_01P2K6kCftytexWsuJfNFtV4), Opus 5.5 (D15, L37). Written 2026-10-26 16:55Z (date -u).
Object: docs/new/P-N5-EPC-box48.md, sha1 9f48ded742d7f44bbf82ae8ec9e0e88c46457700 (= the Lead's pin "9f48ded7", which is the FILE sha1:
`git show 81ab0b72:… | sha1sum`, l-new freeze commit 81ab0b72, which is on trunk; the same sha1 at origin/claude/l-new and on trunk), 185 lines,
frozen. Author L-NEW successor 27. Its quotes are pinned at trunk f4562054, an ancestor of the freeze.
Independence: written before opening any REFEREE file on EPC. `git fetch origin claude/referee` + `git ls-tree --name-only -r
origin/claude/referee docs/referee/ | grep -ic epc` gave 0 at 15:06Z and 16 at 16:53Z (REFEREE pushed EPC material in between; I saw file NAMES
in that listing only and opened nothing; this report's verdicts and notes were fixed before that listing). The packet itself quotes two lines
of REFEREE's FBC report (FBC-N3), which I had already read at my FBC §C; that is the only REFEREE text involved. Lane tools
(experiments/new/box48/*.py) NOT run or imported.
Checker: docs/referee-2/R2-N5-EPC/epc_check.py (own; on my R2-N5-FBC/fbc_check.py machinery: SPEC loop, my own play values with the ENGXI
cross-check, LEV_C exact per (phase, configuration) by simple-path enumeration in H_C, and the iterative-deepening mode when over budget).
LEV_C is computed for EVERY configuration visited in a phase that has a fallback or a return to check, not only for configurations at fallback
sources, because RET-FB and VIS speak about every configuration. Quote check: my R2-N5-FBC/quotes.py.
Scope (D1): EP-C and EP-ASM reduce N_ep to NCONF, R⁰, X_dir, X_big, NCONF_{≥2}, R⁰_{≥2}, none of which is bounded here; FB-C′ bounds f by
n·|𝒞_f(P)|, and |𝒞_f(P)| is not bounded on general games. Nothing here bounds N5's running time. Not a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Verdicts
| item | verdict | premises (checked) |
| --- | --- | --- |
| §1 Lemma FB-RISE_C, Lemma SAT_C (restated, with proofs) | SIGN (as in my R2-N5-FBC; identical text up to SAT_C (2) no longer carrying the 4n(n − 1) bound) | as R2-N5-FBC §0 |
| §2 Lemma RET-FB | SIGN | FB-RISE (a) items 2-3 (frame- and state-free), Case A with Ω := Ξ_t (Q-A), (MON), (V1), (V2), induction on \|r\| |
| §2 Corollary VIS | SIGN | SAT_C (2) + R15 (d) via R57 (a); RET-FB; LEV_C monotone and ≥ 0 |
| §2 Theorem EP-C (including R⁰ ≤ Σ_S REV(S)) | SIGN | VIS; one configuration per epoch |
| §3 Lemma SAT-FB | SIGN | SAT_C (2); S2; S4a "Else σ_new = σ"; S4c's (Ξ_t(w), w)-maximum; FIX 3; S5; R68's HON-FB (iv) last-state argument |
| §3 Corollary SAT-FB1, Theorem FB-C′ (f ≤ n·\|𝒞_f(P)\|) and its consequences bullet | SIGN | SAT-FB; FB-RISE_C |
| §3 the Lead's question: does FB-C′'s proof stand without REFEREE's FBC-N3 route? | YES (§1 below) | — |
| §4 Corollary EP-ASM | SIGN as an assembly; its second term SIGN as an IMPLICATION from (Στ) | HON-0-FF (b) (RESULTS R70); REC-1-FF (c) (R70, implication); VIS |
| §5 remark ((D changes) + 1 ≤ N_ep) | SIGN | τ fixed in the phase |
| §5 DEAD ("a saturated fallback is flat and ends the phase") | DEAD CONFIRMED (DATA, my own runs) | — |
| §7 quotes (22) | all VERBATIM at f4562054; pins match | own quotes.py |
No gap. Notes N-EPC-1..6 (§3). Not reviewed (as the packet asks): §6 (DATA, OPEN, READINGs) and the READINGs elsewhere.

## 1. Proof check
### §1 (restated lemmas)
- FB-RISE_C and SAT_C are the P-N5-FBC statements and proofs I signed in R2-N5-FBC (same text; SAT_C (2) now stops at "Ξ is constant", and the
  window bound moves to VIS (a) with R15 (d) and R57 (a) named). CORRECT; this packet does not depend on the FBC review.

### §2 RET-FB, VIS, EP-C
- RET-FB (fallback t → t+1 from ANY configuration; C any configuration; s ≥ t + 1 a C-state). Induction on \|r\| over all vertices at state s.
  - Even y: |r′| ≤ L − 1 ≤ LEV_C(t), so Ξ_t(z) ⪰ value(r′); FB-RISE (a)'s items 2-3 at the fallback t give Ξ_{t+1}(y) ⪰ value(r), and (MON)
    carries it to s. The packet's parenthetical claim that items 2-3 "do not need t to be a C-state" is right: I made the same observation as
    note N-FBC-2 on P-N5-FBC (the Even case uses LEV_C's definition at t, S4c, Case A, (MON), (V1), (V2), λ_{t+1} = λ, never σ̄_t).
  - Odd y: s is a C-state, so z = σ̄_C(y) = σ̄_s(y); the induction hypothesis (all paths shorter than r, every start vertex) gives
    Ξ_s(z) ⪰ value(r′), and FB-RISE_C's Odd case read at s ((V1)/(V2), or the own-cycle-node comparison) gives Ξ_s(y) ⪰ value(r).
  CORRECT. The C-state requirement on s is essential, not cosmetic: my control asserting RET-FB at EVERY state s ≥ t + 1 fails 11,424 times on
  the library (§4), which is the packet's remark that an Odd vertex with σ̄ ≠ C can sit below its H_C-paths.
- VIS. (a) LEV_C(s_i) = n − 1: from the least such i₀, SAT_C (2) makes Ξ constant from s_{i₀} to any later C-state t′, τ is constant, so R15
  (d) (through R57 (a)) gives t′ − s_{i₀} ≤ 4n(n − 1); C-epochs start ≥ 2 apart, so V_C − i₀ ≤ 2n(n − 1). (b) a fallback source t ∈
  [s_i, s_{i+1}): t + 1 ≤ s_{i+1}, and RET-FB with LEV_C(t) ≥ LEV_C(s_i) gives LEV_C(s_{i+1}) ≥ LEV_C(s_i) + 1 from {0, …, n − 2}: ≤ n − 1 of
  them. (c) R⁰_C by definition. 1 + 2n(n − 1) + (n − 1) + R⁰_C = 2n² − n + R⁰_C. CORRECT.
- EP-C. N_ep = Σ_C V_C (each epoch has one configuration), summed over the NCONF(P) configurations. A return in R⁰_C has no fallback source in
  [s_i, s_{i+1}), so both starts lie in one maximal fallback-free run S, and C's starts in S give at most (their number − 1) such returns:
  R⁰ ≤ Σ_S REV(S); fallbacks split P into ≤ f + 1 runs. CORRECT.

### §3 SAT-FB, SAT-FB1, FB-C′ — and the Lead's question
- SAT-FB. Suppose a C-state t′ > t. SAT_C (2) gives Ξ_{t+1} = Ξ_t. S4c switched exactly the Even x with Iσ_t(x) ≠ ∅, each to the
  (Ξ_t(w), w)-maximum z* of Iσ_t(x). At t + 1, Iσ is read from Ξ_{t+1} = Ξ_t and σ_{t+1}: an unswitched x has Iσ_{t+1}(x) = Iσ_t(x) = ∅; a
  switched x would need w with Ξ_t(w) ≻ Ξ_t(z*) ≻ Ξ_t(σ_t x), i.e. w ∈ Iσ_t(x) beating the maximum. So Iσ_{t+1} = ∅. Then S4a returns σ ("Else
  σ_new = σ"), and S4b changes τ, or the Odd fallback fires (FIX 3: Odd falls back only if Iσ = ∅) and changes τ, or S5 stops: the next
  transition leaves the phase. That is R68's HON-FB (iv) argument, which uses only Iσ = ∅ and the SPEC. CORRECT.
- SAT-FB1 and FB-C′: two saturated C-sources t₁ < t₂ make t₂ a C-state after t₁, so t₁ + 1 is P's last state, but t₂ ≥ t₁ + 1 sources an in-phase
  transition; contradiction. Then per C: ≤ n − 1 unsaturated (FB-RISE_C) + ≤ 1 saturated = n. CORRECT.
- Consequences bullet: |𝒞_f| ≤ N_ep gives f ≤ n·N_ep, which implies R60 (c)'s 1 + n·N_ep; f ≤ n·Δ^k on 𝒞^kO (\|Q\| = k, Π_q deg q ≤ Δ^k); f ≤
  n(1 + m) when every \|D_k\| ≤ 1 (the configuration count of P-N5-FBC (c)). CORRECT.
- THE LEAD'S QUESTION: FB-C′'s proof stands on its own. Its premises are FB-RISE_C and SAT_C (both proved in §1 of this packet), S2, S4a, S4c,
  FIX 3, S5 and R68's last-state argument. It does NOT use R15 (b) or R38 (f) CN-LAST, which are what REFEREE's FBC-N3 route uses, and the
  §3 Remark cites FBC-N3 as a remark, not a premise. The two routes share SAT_C (2) and reach the same last-state conclusion: FBC-N3 through
  "Ξ-flat ⇒ every gate is a length-only switch at a cycle node ⇒ CN-LAST", SAT-FB through "Ξ-flat ⇒ S4c's maximum leaves no improving edge".
  The SAT-FB route is the more elementary one, and it shows in passing that EVERY Ξ-flat in-phase fallback ends its phase (my ISE / FLATLAST
  checks: Iσ_{t+1} = ∅ at all 734 Ξ-flat in-phase fallbacks, §4).
- SAT-FB's disjunction is the right form: the DEAD guess (drop the second disjunct) fails on rho3_253_n32 from my own random starts 5 and 7
  (23 saturated fallbacks, 23 not Ξ-flat, 21 not the phase's last transition) and on cond_stuck_symsi3_YE (2 / 2 / 2), while SAT-FB and
  SAT-FB1 hold at every one of them: each such fallback is the last visit of its configuration.

### §4 EP-ASM, §5 remark
- EP-ASM: N_ep = N_0 + N_1 + N_{≥2} by \|D_E\| (D_E is a function of the epoch's configuration, τ fixed); N_0 ≤ 4n² − 3n is HON-0-FF (b) (landed,
  RESULTS R70); N_1's bound is REC-1-FF (c), an implication from (Στ) (R70, signed as such); N_{≥2} is VIS summed over the configurations with
  \|D_C\| ≥ 2, whose epochs are exactly the epochs with \|D_E\| ≥ 2. CORRECT as an assembly, the second term as an implication.
- §5 remark: in a phase τ is fixed, so D_k is a function of σ̄_k|Q; a change of D is a change of configuration, hence an epoch boundary:
  (D changes) + 1 ≤ N_ep. CORRECT (59,874 phase checks, 0 failures).

## 2. Premises, complete list
SPEC S1-S5 with FIX 1-4 (S2, S4a, S4c, S5, FIX 3 quoted); 1E-N3 with R57 (a) (VJ) as the bridge Ξ = Ω (used for (MON) and for R15 (d) in VIS
(a)); R15 (a), (d); R17 (a) (V1), (V2) and R17 (b) Lemma P Case A with Ω := Ξ_t (Q-A, YES from both referees); R38 (a) phases; R64 epochs; R68
(HON-FB (iv)'s argument; X_dir, X_big, T*_Q, (Στ)); R70 = P-N5-HONFF (FB-RISE (a) items 2-3, HON-0-FF (b), REC-1-FF (c)); R60 (c) only for the
comparison. All landed. The packet's list matches; P-N5-FBC and FBC-N3 are correctly kept out of the premises.

## 3. Notes (no gap)
- N-EPC-1 (pin wording). The packet's header says "Pinned at trunk f4562054", which is the revision of its quotes; the Lead's "pinned 9f48ded7"
  is the packet file's sha1, and the frozen file is at l-new 81ab0b72 (on trunk). Both are right, but they name different things; a referee
  looking for a commit 9f48ded7 will not find one.
- N-EPC-2 (definition). §0 and §4 use \|D_C\| (NCONF_{≥2}, R⁰_{≥2}) but define only D_E; D_C := {q ∈ Q : C(q) ≠ τ(q)} (the same set, since
  D_E is a function of the epoch's configuration). One line.
- N-EPC-3 (citation). SAT-FB's last step cites HON-FB (iv), whose quoted sentence is written for a W-honest state h ("S4a returns σ_{h+1}"). The
  step itself uses only Iσ = ∅ and the SPEC, so citing S4a / S4b / S4c / S5 directly (as the proof text already does) is enough; the citation
  is correct but not needed.
- N-EPC-4 (RET-FB's Even step). The relaxation of the Even vertices at a fallback holds in every frame H_C at once: my EVEN check (Even
  vertices reach min(LEV_C(t) + 1, n − 1) already at t + 1, for every configuration C visited, whatever the fallback's own configuration)
  passed 7,126 times. This is the frame-free fact behind both RET-FB and my FBC note N-FBC-2.
- N-EPC-5 (thin spots, DATA). VIS's kind (a) (returns after saturation) NEVER occurs in my data (0 of 1,340 returns), so its 2n(n − 1) term
  is untested, consistent with the packet's CONJECTURE SAT-1. VIS's bound is never close: my control "VIS without R⁰_C" does not bite on the
  library (the 2n² − n slack is huge against at most 10 epochs of one configuration). The random sets carry almost no returns (2 in 19,500
  runs); the content is in the library sets (1,310 returns).
- N-EPC-6 (what the data say about the reduction, DATA). Of the 1,340 returns classified exactly, 611 are kind (b) (a fallback in between, so
  LEV_C rises) and 729 are R⁰ (fallback-free). So the fallback-free returns are the larger part, and they are exactly the term EP-C does not
  bound — the packet's own OPEN item R⁰_{≥2}.

## 4. Data (DATA, not proof; logs in docs/referee-2/R2-N5-EPC/logs/, reproduce with run_all.sh and run_lib.sh)
| set | runs | states | phases | configurations with exact LEV_C (deepened / UNK) | RET-FB checks (from another configuration's fallback) | EVEN checks | returns (kind a / b / R⁰) | EP-C phases | saturated fallbacks (non-flat / not last) | Ξ-flat fallbacks (Iσ_{t+1} = ∅) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| named: long121_n40, nep90_n40, nep76_n40 (lane starts); rho3_253_n32 × 8 random starts; cond_stuck_symsi3_YE, gapb_dup_n20 × 3 | 17 | 522 | 149 | 250 (52 / 64) | 615 (587) | 821 | 28 (0 / 27 / 1) | 146 | 25 (25 / 23) | 0 |
| lib41 minus referee games × 3 starts | 1,230 | 19,421 | 7,141 | 813 (317 / 504) | 10,880 (4,539) | 2,194 | 623 (0 / 250 / 373) | 6,994 | 43 (0 / 0) | 71 |
| my 503 𝒞^1O files × 2 starts | 1,006 | 17,831 | 4,161 | 955 (407 / 534) | 12,974 (5,074) | 3,507 | 687 (0 / 334 / 353) | 3,990 | 51 (0 / 0) | 69 |
| random 2 Odd choice vertices, n 5-14 (3,000 × 3) | 9,000 | 21,722 | 20,320 | 20,452 (0 / 0) | 295 (0) | 296 | 1 (0 / 0 / 1) | 20,320 | 294 (0 / 0) | 294 |
| random 4 Odd choice vertices, n 6-16 (2,000 × 3) | 6,000 | 16,576 | 15,883 | 15,935 (0 / 0) | 153 (0) | 153 | 0 | 15,883 | 152 (0 / 0) | 152 |
| random, all Odd vertices with choices, n 6-18 (1,500 × 3) | 4,500 | 12,970 | 12,220 | 12,301 (0 / 0) | 148 (0) | 155 | 1 (0 / 0 / 1) | 12,220 | 148 (0 / 0) | 148 |
0 violations in every set, of: RET-FB (25,065 checks, 10,200 of them across configurations), its Even step (7,126), LEV_C's monotonicity, VIS
with its kinds (a) ≤ 2n(n − 1), (b) ≤ n − 1 and the rise along (b), EP-C and R⁰ ≤ Σ_S REV(S) (59,553 phases without an UNK configuration),
SAT-FB and SAT-FB1 (713 saturated fallbacks), Iσ_{t+1} = ∅ and "last state" at every Ξ-flat in-phase fallback (734), FB-C′ (1,198 phases with a
fallback), EP-ASM's N_0 and N_{≥2} parts and the §5 remark (59,874 phases). Reproductions: long121_n40 at its start gives N_ep 37, NCONF 14;
nep90_n40 N_ep 90, NCONF 48; nep76_n40 N_ep 76, NCONF 40 (the packet's §6). Maxima: NCONF 23 in one phase (pft35_n48), N_ep 53
(rise_thin51_n40), epochs of one configuration 10 (j4_n40), saturated fallback sources per configuration 1 everywhere.
Controls: plus2 (RET-FB with + 2) 609 failures on lib41 (1 start, budget 4·10⁵); nonC (RET-FB at every state s ≥ t + 1) 11,424 failures; last
(SAT-FB without its second disjunct = the DEAD guess) 21 failures on rho3_253_n32 (starts 5, 7; logs/mut_last_rho3.txt) and 0 on the library's
single start (every saturated fallback there is flat and last); noR0 (VIS without R⁰_C) 0 failures — it does not bite (N-EPC-5).
UNK: 1,102 configurations stayed over budget even after deepening (3·10⁶ paths; all in the named and library sets); phases containing one are
skipped for EP-C / EP-ASM (the per-configuration checks still run on the decided configurations).

## 5. Signatures
§1 FB-RISE_C and SAT_C (restated); §2 Lemma RET-FB, Corollary VIS, Theorem EP-C; §3 Lemma SAT-FB, Corollary SAT-FB1, Theorem FB-C′ with its
consequences; §5 remark: SIGN, on every game, under the standing SPEC premise 1E-N3 (P1) and Q-A. §4 Corollary EP-ASM: SIGN as an assembly,
its second term as an IMPLICATION from (Στ). FB-C′'s proof stands on its own, without REFEREE's FBC-N3 route (the Lead's question). §5's DEAD
guess confirmed dead on my own runs. No gap; notes N-EPC-1..6. REFEREE-2 successor 17 (Opus 5.5, D15).
