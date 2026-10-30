# R2-N5-LATEP: independent second-referee report on P-N5-LATEP (REFEREE-2 successor 22, Opus 5.5, D15)
Object: docs/si/P-N5-LATEP-box53.md @ l-si b63f2554 (sha1 b15223e53157d7d0a14767bb3c71dae07066a4da, 204 lines) and its line file
docs/si/P-N5-LATEP-line.txt (sha1 4a68934d832c483c5b28c552fd26526f7de4abea). Both re-hashed here from a detached worktree at b63f2554: match.
Independence: written before opening any docs/referee/ file (names-only count of «latep» in docs/referee/ at the start: 0). Working notes read
for context only: docs/si/N5-ADD-box50.md, N5-LATEP-box51.md, N5-TXCD-box52.md (l-si 170e5316). Landed sources re-read: RESULTS R88 (object
P-N5-GP-box31.md §3-§4, the FW-R* proof l. 143-156), R89 (line: W-run, SUCC-MON, LATE-RISE, GP*-RUN, R*-RISE), R90 (object P-N5-CUT-box43.md
§5-§8), L-NEW box 70 §3 (GXC). Owner rulings applied: D1 «Treat every such claim, including the fleet's own, as wrong until it passes the
gauntlet below.»; D18 «Clearly distinguish proven results from conjectures and open problems.»
Scope: every item is a lemma about one W-run of N5, a REDUCTION or a structural fact. Nothing here bounds a count; G-N5-TIME stays OPEN.
Not M3, not a step-4 pass, not a TARGET.md claim.

## 1. Verdict table
| § | item | verdict (Opus 5.5, D15) | gaps / notes |
| --- | --- | --- | --- |
| §2 | Definition LATE′, diff against R88 §4 | CHECKED: the diff is exactly the stated replacement of «t ∈ [a, τ)» by «t ∈ [max(a, p + 1), τ)» (quote verbatim, §3 below); LATE′ ⊆ R88-late, so R*′_T ≤ R*_T; REPEAT′ ⊆ P-N5-CUT §6 REPEAT, so REP′_F ≤ REP_F | none in the packet; the LINE's rendering is wrong (L-1, REQUIRED) |
| §3 | Corollary FW-R*′ | SIGNED | none. «verbatim» is accurate up to one added choice (τ := the first adoption after t), which is valid: N-1 |
| §4 | Lemma LATE-SPLIT′ (i), (ii) | SIGNED | none; N-2 (uniqueness of the leave is implicit) |
| §4 | Corollary CIRCLE′ (four inequalities and the equivalence) | SIGNED | none; the line files them under «Lemma LATE-SPLIT′» (L-3) |
| §5 | Lemma GAP-CLIMB | SIGNED | none; it sharpens R89 R*-RISE (N-3) |
| §6 | Proposition CHAIN (GXC_F ⊆ TXC_F ⊆ ZXC_F, ZXC_F(z) = TXC_F(z) ⊔ WZ_F(z), WZ_F(z) ≤ WCH_F(z)) | SIGNED | none; cross-reference «(§8 DATA)» in l. 111 should be §10 (N-4) |
| §7 | Lemma TXC-DESCENT (termination included) | SIGNED | none; N-5 (termination argument spelled out) |
| §7 | Corollary TXC-RED (and Σ_F LCT_F ≤ n(n − 1) per run) | SIGNED | none |
| §7 | composed bound l. 145 | SIGNED (arithmetic from §5, §6, TXC-RED) | none |
| §8 | READING on R90 with LATE′ (R1)-(R3) | not signed (READING); checked for consistency: (R1)-(R3) follow from §3-§4 and REP′* ≤ REP*; the box-40 remark needs j − 2 in the same W-run (N-6) | — |
| §9 | lane's symbol test of the line | DISAGREE in one row: «LATE′, p, t» is not correctly bound (L-1); three precision points (L-2, L-3, L-4) | see §4 |
| §10 | DATA | not signed; two DATA statements are wrong (N-7: lane txcd.py undercounts; N-8: «0 T4» / CNW) | — |

No gap in any proof. One REQUIRED fix in the line file (L-1). Everything else is a note.

## 2. The items, as I checked them
- §2. Every LATE′ adoption is R88-late: [max(a, p + 1), u) ⊆ [a, u). A REPEAT′ has an earlier LATE′ adoption, which is an earlier R88-late one,
  so it is a REPEAT of P-N5-CUT §6 (a late adoption that is not the edge's first late one). Hence REP′_F ≤ REP_F (my REPSUB check: 0).
- §3 FW-R*′. R88's proof (P-N5-GP §4, l. 151-156) shows, for k ≥ a + n − 1 with W_{k+1}(x) ≠ W_k(x), an Even y_i on x's ρ_{k+1}-play
  whose edge (y_i, y_{i+1}) is blocked at t = k − 1 − i ≥ a, and ρ_{t+1}(y_i) ≠ y_{i+1}. Some adoption of the edge lies in (t, k]; take τ the
  first. Its previous adoption p is not in (t, τ) (choice of τ) and is not t (ρ_{t+1}(y_i) ≠ y_{i+1}); so p < t, p + 1 ≤ t, and t ∈
  [max(a, p + 1), τ): LATE′. τ ≥ t + 1 gives k − τ ≤ i ≤ n − 2, so the charging (each τ charged by k ∈ [τ, τ + n − 2]) is unchanged. On W-runs
  by R89 GP*-RUN. Correct.
- §4 (ii). Blocked at t ∈ [p + 1, u) forces σ_t(y) ≠ z = σ_{p+1}(y): a leave in [p + 1, t − 1]. Since p is the previous adoption, y cannot return
  to z before u, so this leave is the only one in (p, u): k ≤ t − 1 (N-2). t_b := t ≤ u − 1 (not blocked at u: (y, z) ∈ Iσ_u by [S4a]). Chain
  W_{k+1}(z) ⊴ W_{k+1}(σ_{k+1} y) (OPT-OFF (ii), y off-cycle at k + 1) ⊴ W_{t_b}(σ_{t_b} y) (W-SUCC) ◁ W_{t_b}(z) (blocked). Correct.
  Checked on every blocked state t_b in [k + 1, u − 1] of every REPEAT′ with y off-cycle (LSP), with both links separately (LSP_opt,
  LSP_succ): 0 violations. Control: at own-cycle y the conclusion is not claimed; X′ = 0 in all my data, so that control never fired.
- §4 CIRCLE′. REP′ ≤ n_E R*′_T (one switch per Even vertex per transition); R*′_T ≤ m_E + REP′ (a LATE′ transition contains a FIRST′, ≤ one per
  edge, or a REPEAT′); REP′ ≤ X′ + Σ_z d_E(z)·WCH_F(z): for one edge consecutive REPEAT′s u₁ < u₂ have k₂ > p₂ ≥ u₁, so the intervals
  [k + 1, u − 1] are disjoint and the token (edge, last W(z)-change in [k + 1, t_b − 1]) is injective; a W(z)-change pays ≤ d_E(z) tokens. The
  equivalence uses Σ_z d_E(z) WCH_F(z) ≤ m_E·WCH_F and X′ ≤ REP′. Correct.
- §5 GAP-CLIMB. LATE-RISE (R89, on any t < u, landed) gives Ξ_u(z) ▷ Ξ_{t_b}(z); R15 monotonicity makes the first change s ∈ [t_b, u − 1] a
  strict rise. The gap chain Ξ_s(z) = Ξ_{t_b}(z) ⊴ Ξ_{t_b}(σ_{t_b} y) ⊴ W_{t_b}(σ_{t_b} y) ◁ W_{t_b}(z) ⊴ W_s(z) is correct (S2, XW, blocked,
  W-MON on F). Disjointness: t_b(u) ≥ p + 1 ≥ u′ + 1 for the previous LATE′ adoption u′ ≤ p. Correct.
- §6 CHAIN. Correct as written; both strictnesses occur in my data (X_GXCstrict, X_TXCstrict > 0).
- §7 TXC-DESCENT. At a non-terminal TXC event x: not T1 gives one cycle node c at s and s + 1, x ≠ c (else no climb); not T2 / not T3 give one
  successor y in all four plays; [V1] gives x ⊕ · with y's path to c avoiding x; strict [V2] with totality of ⊴ transfers ▷ (Ξ) and = (W,
  using not T4 and λ_W constant on F) to y. Termination (the item the Lead asked to watch): every vertex of z's (σ_{s+1}, σ̄_{s+1})-play
  shares the cycle node c, which lies on the play's cycle; the prefix from z up to the first visit of c is simple. If no terminal occurred
  before c, (c, s) would be a TXC event; c is not T1 (else it is terminal), so λ_Ξ(c) = c at s and s + 1, Ξ_s(c) = Ξ_{s+1}(c) = (c, ∅, 0):
  no climb. So a terminal occurs on the simple prefix: j exists and x_0, …, x_j are distinct. T2 at a λ_Ξ-fixed transition is GXC verbatim
  (x_j ∈ Z_s by CHAIN). Correct (N-5: the packet's «before any repetition» relies on c being reached on the simple prefix, which holds).
- §7 TXC-RED. At a λ_Ξ-fixed transition no T1 terminal exists, so every terminal is in GXC_F ∪ GATE_F ∪ CNW_F (T3 and T4 terminals are TXC
  events by the lemma); each (x, s) is the terminal of ≤ n events. λ_Ξ-changing transitions: ≤ n events each. Σ_F LCT_F ≤ n(n − 1): Ξ is
  non-decreasing on the whole run (R15; τ-steps do not change Ξ_σ), and a change of λ_Ξ(v) under ⊵ strictly raises the cycle node's reward
  ([S1-ord] compares the reward first). Correct.

## 3. Pinned checks re-run (detached worktree at b63f2554; my own extraction of si/check.sh l. 845-860, set -euo pipefail)
- «box 51»: PASS (xeng.py «state sequences identical: True» on tiedmut_so_th_n32_11; tied.py; latep.py on tiedmut, wdepth_K4_m16, fc_6).
- «box 52»: PASS (txcd.py on so_th_n32 and wdepth_K4_m16, the pinned strings).
- «box 53»: PASS (quotecheck «quotes=6 bad=0», mutated control fails).
- Exit status of the extracted script: 0.
- My own quote check (docs/referee-2/R2-N5-CORE/qcheck.py, packet read at b63f2554): tags 6, ok 6, miss 0; control SHIFT=1: ok 0, miss 6.

## 4. Strict symbol test of the line file (my own, every symbol and index, before reading the lane's §9 table)
| symbol | binder found | verdict |
| --- | --- | --- |
| F, W-run, W_t, λ_W, τ (constant on F) | «as in RESULTS R89: τ and λ_W constant on F, no S4c fallback» | bound |
| N5, SPEC S1-S5, R57 premise | named, landed | bound |
| σ_u, σ_k (Even strategy of state u) | not defined in the line; only through «N5 (SPEC S1-S5)» runs and R89's W_t := (σ_t, τ_t)-plays | bound by landed source (R89 binds σ_t in its own line); acceptable |
| Ξ_t, σ̄_t, Iσ_t, ⊴, ▷ | «as in SPEC S1-S2» | bound |
| λ_Ξ | «the cycle-node map of Ξ_t» | bound |
| BLOCKED | «as in RESULTS R88» | bound (R88's definition carries «t ∈ [a, b)»: L-1 below) |
| n, n_E, m_E, d_E(z) | defined in the line | bound |
| adoption at u, y, z, u | «an adoption of (y, z) at u: σ_{u+1}(y) = z ≠ σ_u(y)» | bound |
| LATE′, p, t | «blocked at some state t of F with p + 1 ≤ t < u, p its previous adoption in F (any t of F if none)» | NOT CORRECTLY BOUND: L-1 |
| REPEAT′, R*′_T, REP′_F | defined in the line | bound |
| X′_F, k, t (second use), off-cycle | «k the last k < u with σ_k(y) = z ≠ σ_{k+1}(y) and t a blocked state as in the definition of LATE′»; «off-cycle for τ (P-N5-CUT §2)» | bound; t is existential (any blocked state of the definition): harmless because λ_W is constant on F, but the line does not say «some» (L-4, precision) |
| WCH_F, WCH_F(z), W(z) | defined in the line | bound |
| Z_s, D_s, o | defined in the line | bound |
| s, «transitions of F» | «over the transitions s → s + 1 of F (s, s + 1 in F)» | bound; LCT_F sits inside that scope: bound |
| ZXC_F(z), TXC_F(z), WZ_F(z), GATE_F, CNW_F, LCT_F, x | defined in the line | bound |
| GXC_F, v | «the GXC events (v, s) of L-NEW box 70 §3 (docs/new/N5-SC-box70.md)» | bound only by an unrefereed lane working note, unpinned (L-2, precision) |
| TXC_F, ZXC_F as sets; set as number | defined in the line | bound |
| Lemma names | «(Lemma LATE-SPLIT′) R*′_T ≤ m_E + REP′_F, REP′_F ≤ n_E·R*′_T and REP′_F ≤ …» | these three are §4's Corollary CIRCLE′, not Lemma LATE-SPLIT′ (L-3, precision) |
- L-1 (REQUIRED). The line's LATE′ reads «blocked at some state t of F with p + 1 ≤ t < u, p its previous adoption in F (any t of F if none)».
  Read literally, the parenthetical replaces the whole constraint «p + 1 ≤ t < u» when there is no previous adoption, so an adoption of an
  edge blocked only at states ≥ u would be LATE′. The packet's §2 (l. 54-55) keeps «t ∈ [max(a, p + 1), τ)», i.e. t < u always, and every
  proof (§3: t < τ; §5: t_b < u) uses t < u. Fix: «… with p + 1 ≤ t < u, p its previous adoption in F (a ≤ t < u if there is none)».
  (Whether the literal reading changes counts: an edge blocked at some t > u and adopted at u. It would inflate R*′_T, and FW-R*′ would still
  hold, but REP′_F ≤ REP_F and «every LATE′ adoption is R88-late», on which §8 (R3) rests, would fail. The packet text is correct; only the
  line is wrong.)
- L-2 (precision). GXC is defined by reference to docs/new/N5-SC-box70.md, an unrefereed lane note with no commit pin. Either pin it
  (@170e5316, the quote tag the packet uses at l. 106) or inline the seven conditions (they fit in one clause).
- L-3 (precision). Rename «(Lemma LATE-SPLIT′)» to «(Lemma LATE-SPLIT′, Corollary CIRCLE′)» in the line, or move the three inequalities under
  «(Corollary CIRCLE′)», to match the packet's §0 and §4.
- L-4 (precision). «t a blocked state as in the definition of LATE′» → «for some blocked state t as in the definition of LATE′».
- With L-1 fixed, the line MATCHES the packet's §3-§7 statements (my diff, item by item: FW-R*′ = §3; the three CIRCLE′ inequalities = §4;
  GAP-CLIMB's per-edge form = §5 (its sum form and «z ∈ Z_s» are not in the line, which is a weakening, allowed); CHAIN = §6; TXC-RED and the
  LCT sum = §7. LATE-SPLIT′ (ii) and TXC-DESCENT themselves are not in the line; they are lemmas behind it.)

## 5. My own engine as a control (docs/referee-2/R2-N5-LATEP/latep_check.py)
- State loop: my lane's R2-N5-DUAL/dual_check.Runner (SPEC N5 written from S1-S5 + FIX 1-4 on si.py's Engine, read-only). W: my own play value
  (R2-N5-FRAME/frame_check.pval). The lane's odd/latep.py, txcd.py, tied.py and new/box21/n5x.py are NOT imported. Every definition is coded
  from the packet's text (header of the script). REPEAT′ as frozen (an earlier LATE′ adoption); the tool's REPP (any earlier adoption) is
  counted separately as REPA.
- Independent Ξ control (BF=9): at every state of 1,600 runs on 400 random games (n 5-9), Ξ_t(v) equals the minimum over ALL positional Odd
  strategies of the play value: 3,819 states, 0 mismatches. Every state of every run: Ξ_t = my play value of the (σ_t, σ̄_t)-plays (XIPLAY).
- Checks (each 0 on every set): XIPLAY, XW, XIMON, LCT (per vertex ≤ n − 1, transitions ≤ n(n − 1)), WMON, RSUB, FWR, FWP (FW-R*′), A2, C0,
  REPSUB, LSP (+ LSP_opt, LSP_succ), XSIL, CIR1-CIR3, GC, GTOK, GCE, GCS, INC (both inclusions, WZ ⊆ W-changes, WZ_F(z) ≤ WCH_F(z)), DESC, CYC,
  T2G, RED, BF.
- Sets run (frozen worktree; files mode with runs = 1 so that games without a start file are run from S3, the lanes' convention):
| set | runs | W-runs | max WCH | max R*_T | max R*′_T | max REP′ (frozen) | max REPA (tool REPP) | LATE′ (sum) | GAP-CLIMB tied / WZ | TXC | GXC | GATE | CNW | violations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| corpus odd/sbcg.lst (719 games, S3 start) | 719 | 5,419 | 159 | 17 | 17 | 3 (sum 4) | 9 (sum 40) | 1,104 | 1,003 / 101 | 14,739 | 191 | 2,464 | 71 | 0 |
| latew_K20_m32 (n 538, start file) | 1 | 1 | 700 | 640 | 640 | 570 | 570 | 641 | 639 / 2 | 3,941 | 0 | 2,221 | 0 | 0 |
| wdepth_K4_m32 (n 234, start file) | 1 | 1 | 140 | 68 | 68 | 45 | 45 | 69 | 67 / 2 | 248 | 0 | 125 | 0 | 0 |
| pins: tiedmut_so_th_n32_11, wdepth_K4_m16 (start + S3), so_th_n32, fc_6 (S3) | 6 | 60 | 76 | 36 | 36 | 21 | 21 | 70 | 64 / 6 | 470 | 0 | 149 | 0 | 0 |
| random n 5-9, BF=9 (400 games × 4 starts) | 1,600 | 3,638 | 2 | 0 | 0 | 0 | 0 | 0 | — | 29 | 0 | 0 | 1 | 0 |
| random n 10-40 (400 × 4) and n 40-80 (200 × 3) | 2,200 | 8,978 | 3 | 1 | 1 | 0 | 0 | 2 | — | 593 | 1 | 118 | 21 | 0 |
- The two random batches ran with the pre-freeze build of the script (REPEAT′ then counted as «any earlier adoption»); every other check is
  unchanged, and REP′ = REPA = 0 there, so the frozen definition changes nothing on them.
- Corpus split by kind: box-50 REPEATs (P-N5-CUT §6) 41 = 4 re-blocked + 37 stale (box 50 §6 reproduced); REP′ = 4 = the re-blocked ones
  (A2 0, X_A3 0); C0 0 (no stale REPEAT is LATE′). The tool's REPP exceeds REP′ on 14 W-runs (36 LATE′ adoptions whose earlier adoption of
  the edge was not LATE′). So §10's «REPP ≥ REP′» is right, and box 51 §5's «max REP′ 9» is the tool's REPP; the frozen REP′ maximum is 3.
- Agreement with the lane's tools (two different N5 loops, the same counts): on every set my R*_T, R*′_T, REPA (= the tool's REPP), WCH,
  LATE′ totals and tied GAP-CLIMB tokens equal latep.py's printed figures (pins and box 51 §5 table: corpus maxima WCH 159, R*_T 17, R*′_T 17,
  REPP 9, LATE′ 1,104, tied 1,003; latew 700 / 640 / 640 / 570 / 641; wdepth_K4_m16 RT 36, RTP 36, REPP 21, LP 37, TIEDG 35; tiedmut RTP 4,
  REPP 1, LP 6, TIEDG 4; fc_6 RT 4, RTP 3, REPP 0).
- Controls (expected to bite): X_noT3 (continue the descent through a gate: the next vertex is not a TXC event) and X_noT2 bite often, so T2
  and T3 are needed terminals; X_noT4 never bit (0 of the T4-only terminals): T4 is a safe terminal but I have no instance showing it is
  necessary (N-8).

## 6. Notes (N-items; none is a gap)
- N-1 (§3). «verbatim» holds for every line of R88's proof; the proof adds one choice, τ := the first adoption after t, and uses it twice
  (p ∉ (t, τ); k − τ ≤ i). Both are correct.
- N-2 (§4 (ii)). «the last leave k» is the only leave of z by y in (p, u): after a leave y cannot return to z before u, since p is the previous
  adoption. Worth one clause.
- N-3 (§5). GAP-CLIMB refines R89 Corollary R*-RISE (late adoptions of (y, z) ≤ Ξ(z)-changes in F): same LATE-RISE mechanism, with the climb
  located at a gap state of z and the intervals disjoint by LATE′ itself.
- N-4 (§6 l. 111). «(§8 DATA)» should be «(§10 DATA)».
- N-5 (§7). The termination argument is complete; «before any repetition» is justified because c lies on the play's cycle, so the simple prefix
  from z reaches c before any vertex repeats.
- N-6 (§8, READING). The box-40 remark («LATE re-entries are LATE′») reads the block at j − 2 inside the W-run containing j − 1. Box 40's
  (LATE) case is stated on a τ*-piece; j − 2 and j − 1 are in the same W-run only if the transition j − 2 → j − 1 keeps λ_W. Not signed; for a
  future packet it needs that hypothesis or the W-run version of the block.
- N-7 (§10 DATA). experiments/si/odd/txcd.py carries the W valuation across a τ-change with the OLD τ: at the end of each step it sets
  w0, wk0 := W(ns, t) (l. 58), not W(ns, nt). The first transition of the next W-run is then judged against a wrong W frame and is mostly
  dropped. My counts: so_th_n32 TXC 73 / gate terminals 16 (pinned: 63 / 15); tiedmut_so_th_n32_11 77 / 10 (box 52 table: 66 / 9); wdepth_K4_m16
  184 / 93 (pinned, unchanged: no τ-change matters there). A scratch copy of txcd.py with that line replaced by «w0, wk0 = W(ns, nt)»
  reproduces my figures exactly on all three (not committed; lane code is not edited). Corpus: TXC 14,739 (box 52: 14,526); terminals T1 292,
  T2 306, T3 14,136, T4 5 (§10: 356, 292, 13,878, 0). The pinned strings in «box 52» encode the undercount. DATA only; no proved item depends on it.
- N-8 (§10 DATA and box 52 §5). «0 T4» and «CNW is 0 in all data» are false as defined: CNW_F counts every TXC event at an own W-cycle node.
  Corpus: CNW 71 events; 5 descents end at a T4 terminal that is not T1-T3. Instance: n5-exhaustive/instances/b5_o11.pg from S3, W-run
  [5, 6]: Odd 7 has τ(7) = 7 (own W-cycle node, W(7) = (7, ∅, 0)) and σ̄(7) = 2 (a gate); Ξ(7) climbs from (4, 8, 2) to (4, 568, 5) when Even 2
  switches 4 → 8. Box 52's inference «a T4 vertex that is not also T1-T3 would appear as a failure, and there are none» is unsound: txcd.py
  walks through a T4 vertex, and the next vertex was a TXC event in all 5 cases (X_noT4 0 / 5).
- N-9 (wording only). §4's X′_F and the line's X′_F are «own-cycle» REPEAT′s; λ_W is constant on F, so «at some state of [k + 1, t_b]» is the
  same as «λ_W(y) = y». The packet could say so.

## DONE / FINDINGS / NEEDS
- DONE: this report; own checker docs/referee-2/R2-N5-LATEP/latep_check.py; pins «box 51», «box 52», «box 53» re-run at b63f2554 (PASS, exit 0);
  quote check 6 / 6 with a failing control.
- FINDINGS:
  1. §3 FW-R*′, §4 LATE-SPLIT′ and CIRCLE′, §5 GAP-CLIMB, §6 CHAIN, §7 TXC-DESCENT and TXC-RED: all SIGNED, no gap (Opus 5.5, D15).
  2. §2's diff against R88 §4 is exact; REP′_F ≤ REP_F holds by the frozen REPEAT′ definition.
  3. L-1 (REQUIRED, line file only): «(any t of F if none)» drops t < u; fix «(a ≤ t < u if there is none)».
  4. L-2 to L-4: precision in the line (GXC source unpinned; lemma name; «some t»).
  5. N-7: lane txcd.py undercounts TXC after τ-changes (W read with the old τ); §10's terminal counts and the «box 52» pins are low.
  6. N-8: CNW ≠ 0 and 5 T4-only terminals in the corpus; §10's «0 T4» is false; T4's necessity is not shown by any instance.
  7. DATA: under the frozen REPEAT′ the corpus has REP′ 4 (max 3 per W-run), equal to the re-blocked REPEATs; the tool's REPP (40, max 9) is
     the upper count §10 describes.
- NEEDS: Lead: route L-1 (required) and L-2..L-4, N-4, N-7, N-8 to L-SI for docs/si/P-N5-LATEP-fixes.md; the §C word after REFEREE 19's report.
