# N5-SPAN (box 38): R86's route redone with switch windows. Lemma SPAN, and why the window is the OUT-window
L-SI successor 30 (Opus 5.5), D15 / D18, Lead reading L40. Lead's message 2026-10-29 21:34Z (after L-RED R121, l-red 345b2da7): "restate
the target law in window form … matched resets and carries of c counted only inside the windows [entry of (v,c), next leave of v from c]
… Then check whether R86 (c)'s derivation (SW-RETURN, then LEN-MONO) can be redone with window counts." Working note, unrefereed, not a
TARGET.md claim. G-N5-TIME OPEN. Labels: PROVED (lane) / CONJECTURE / DATA / DEAD / READING.
- Tool: experiments/si/odd/win.py. Pins: R121 tobs_K8_m32 (sha1 80dd7685be50) and R120 wobs_K8_m32, copied read-only to
  experiments/si/odd/inst/red/. Corpus outputs: odd/out/win_corpus_{E,O}.txt. Pinned in si/check.sh «box 38».
- Fix a λ-run R (λ^U-run on G^d), a vertex v of the improving player and a target c of v.
  - In-windows: the transitions while σ(v) = c, from an entry into c to v's next leave of c.
  - Out-windows: from a leave of c to v's next re-entry into c (closed ones only).
  - Span(v, c): from v's first leave of c to its last re-entry into c.

## 1. Where SW-RETURN's charge sits (READING of R86 §2's proof, l. 75 of the packet)
- The packet's chain for an entry e, a leave s and a re-entry e′ is
  Ξ_{e′}(c) ▷ Ξ_{e′}(σ_{e′} v) ⊵ Ξ_{s+1}(σ_{s+1} v) ⊵ Ξ_s(σ_{s+1} v) ▷ Ξ_s(c).
- So the strict rise of Ξ(c) that pays for the re-entry lies between the LEAVE s and the RE-ENTRY e′: in an OUT-window. Nothing in the
  proof looks at c while v sits on it.
- The in-window form (Lead's [entry, next leave]) therefore counts exactly the changes the proof does not need. DEAD on R121:
  - tobs_K8_m32 (Even side): the pair (231, 198) has 248 MATCHED resets and PCH 263 inside one IN-window, n = 233.
  - The OUT-window and span maxima on the same run are MAT 7, PCH 14, carry segment 1.

## 2. Lemma SPAN (PROVED, lane): SW-RETURN + LEN-MONO, per pair, in the span
- Statement. On every λ-run R (λ^U-run on G^d), for every v of the improving player and every vertex c:
  ENT_R(v, c) ≤ n·(1 + PCH^span_R(v, c)).
  PCH^span_R(v, c) is the number of transitions inside span(v, c) at which P(Ξ c) changes.
- Proof.
  - Let K be the number of closed out-windows of (v, c). Then ENT_R(v, c) ≤ K + 1.
  - Each closed out-window [s, e′) contains a change of Ξ(c), by §1's chain (F-SW at s and at e′ − 1, F-MON, Ξ-SUCC; R86 §2).
  - The out-windows are pairwise disjoint and lie in the span.
  - (i) At most PCH^span of them contain a P-change of c: each P-change lies in at most one window.
  - (ii) The others contain only length changes of c. Each lies inside one P-block of c (a maximal stretch with P(Ξ c) constant).
    - Inside one P-block every change of Ξ(c) moves the length ℓ ∈ {0, …, n − 1} strictly in one direction (R86 §3, LEN-MONO's proof:
      F-MON, the cycle node fixed on R). So one block holds at most n − 1 disjoint windows each containing a change.
    - The span meets at most 1 + PCH^span blocks.
  - So K ≤ PCH^span + (n − 1)(1 + PCH^span), and ENT_R(v, c) ≤ 1 + K ≤ n(1 + PCH^span). □
- Rule-generic: it uses F-SW, F-MON and λ constant only (BARRIER-SI applies to anything built on it alone).
- The span version of COMPOSE (PROVED, lane, from R86 (c)'s first step and Lemma SPAN):
  Σ_v SW_R(v) = Σ_{(v, c)} ENT_R(v, c) ≤ Σ_{(v, c) ∈ E, ENT_R(v, c) > 0} n·(1 + PCH^span_R(v, c)).
  - No PCH of an observer enters. A vertex that is entered once and never left has an empty span; its term is n, while R86 (c)'s term
    is n·(PCH_R(c) + 1).
  - With R86 (d)'s bookkeeping (R47 (a): ≤ n(n − 1) λ-changing transitions per side), T ≤ 2n(n − 1) + (n(n − 1) + 1)·n·m·(1 + S*), where
    S* := the largest PCH^span over pairs and λ-runs (λ^U-runs). The constant is the same shape as COMPOSE-RUN.
- MATCH-Φ on the span. R85's proof bounds the P-changes of any contiguous stretch of c's P-sequence with c's cycle node fixed (R86 (e)'s
  premise, read on a sub-interval of a λ-run). So PCH^span ≤ (K(K+1)/2)(NM^span + 1) + NM^span, with NM^span the carries of c in the
  span. READING: the span is a contiguous interval of one λ-run, which is all MΦ's proof uses.

## 3. The span-form laws (CONJECTURES; DATA)
- CONJECTURE RESET-LIN-S: #MAT^span_R(v, c) ≤ n for every pair and λ-run (λ^U-run).
- CONJECTURE CARRY-SEG-S: ≤ n − 1 carries of c between consecutive MATCHED changes inside span(v, c).
- CONJECTURE PCH-QUAD-S: PCH^span ≤ n² + n. RESET-LIN-S ∧ CARRY-SEG-S imply it (box 35 §2 arithmetic).
- Composition: G-N5-TIME ⇐ PCH-QUAD-S (any polynomial suffices) by §2. That is O(n⁵ m) iterations: Lemma SPAN costs a factor n
  instead of COMPOSE's n·(PCH + 1).
- DATA:
  | instance | side | n | pairs | max ENT | SPAN_V | IN-window MAT / PCH / seg | OUT-window MAT / PCH / seg | span MAT / PCH / seg |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | tobs_K8_m32 (R121) | Even | 233 | 96 | 8 | 0 | 248 / 263 / 2 | 7 / 14 / 1 | 7 / 14 / 1 |
  | wobs_K8_m32 (R120) | Even | 231 | 95 | 8 | 0 | 7 / 14 / 1 | 7 / 14 / 1 | 7 / 14 / 1 |
  | fc_3 | Even | 85 | 136 | 3 | 0 | 1 / 12 / 12 | 1 / 8 / 8 | 1 / 8 / 8 |
- Corpus: §5.

## 4. Composition (one line each)
- §1: the window that R86's proof charges is the OUT-window; the in-window form is DEAD on R121 (248 at n 233).
- §2: Lemma SPAN makes R86's route observer-proof: Σ SW ≤ Σ_(v,c) n(1 + PCH^span(v, c)). R120 and R121 observers drop out
  (span MAT 7, PCH 14).
- §3: G-N5-TIME ⇐ PCH-QUAD-S (or RESET-LIN-S ∧ CARRY-SEG-S): the new target for L-RED.

## 5. Corpus (DATA; odd/sbcg.lst, 719 games per side, S3 start, 0 timeouts)
- Lemma SPAN: SPAN_V = 0 on both sides; OUTRISE_V = 0 (every closed out-window contains a change of Ξ(c)).
- Control: --mut drops LEN-MONO's factor n and fires.
  - It fires on red/n5inj/instances/returns_rt32.pg (Even), pair (12, 10): 2 entries, 0 span P-changes (a length-only re-entry).
  - SPAN1 counts the same failures: 1 (Even) and 4 (Odd: nep92_n40, lev74_n40, nep87_n40, r111_n80).
- RESET-LIN-S, CARRY-SEG-S: 0 failures on both sides. Maxima over pairs (max / n, then largest absolute):

  | side | form | MAT | PCH | carry segment |
  | --- | --- | --- | --- | --- |
  | Even | IN-window | 0.69 (x31_cu16); 21 (x31_cu32i, n 32) | 0.88 (x31_cu32i); 34 (rise_thin51_n40) | 0.19; 24 (switchbestexp_8, n 210) |
  | Even | OUT-window | 0.70 (rise_thin51_n40, 28 at n 40) | 1.38 (rise_thin51_n40, 55) | 0.38 (b5_os_n24); 17 (topfix_n10) |
  | Even | SPAN | 0.70 (rise_thin51_n40, 28) | 1.38 (55 at n 40) | 0.46 (b5_os_n24); 33 (topfix_n10, n 210) |
  | Odd | IN-window | 0.09 (wide_h16); 7 (tcS8_N9) | 0.31; 11 (tcL_N12) | 0.13; 9 (tcR4_N7) |
  | Odd | SPAN | 0.06 (mei_h8); 4 (tcS8_N9) | 0.16 (wide_h16); 8 (tcL_N12) | 0.16; 5 |
- PCH^span exceeds n on rise_thin51_n40 (55 at n 40): PCH-QUAD-S needs its n², not n. RESET-LIN-S has its largest ratio 0.70 there.

## 6. Windows in the W-frame, and the hntop_N family for W-VPOLY (Lead 21:41Z (1), (2))
- (1) W-ENT is already a window statement (READING of box 37 §2's proof).
  - The W-rise of w that pays for a re-entry lies in [k + 1, j]: from v's leave of w to v's re-entry, i.e. v's OUT-window.
  - So W-ENT holds with WCH counted only there: ENT_Q(v, w) ≤ 1 + WCH^out_Q(v, w) + SIL + CYC, and WCH^out ≤ WCH^span (windows are
    disjoint and lie in the span). PROVED (lane): the same proof, reading where the charged change sits.
  - With box 37 §5 (CN-W, LEN-MONO in W) per span this gives the observer-proof W form:
    CONJECTURE W-VPOLY-S: WCH^span_Q(v, w) ≤ n² per pair per guided stretch ⇒ |Q| ≤ m_E(1 + n²) + SIL + CYC.
  - An entered-and-never-left target contributes 1.
- (2) DATA, wret.py on hntop_N (red/seg/hnh1.py N topfix; N = 8 equals the pin red/seg/instances/hntop_n8, sha1 f71291a3; instances in
  experiments/si/odd/inst/hn/; output odd/out/wret_hntop.txt). Every run is ONE guided stretch; W-RETURN and OPT hold (0 violations).

  | N | n = 21N | stretch | max W-changes of one vertex (all) | max over pairs, span | max over pairs, out-windows | max switches of one vertex |
  | --- | --- | --- | --- | --- | --- | --- |
  | 2 | 42 | 33 | 15 | 13 | 13 | 13 |
  | 3 | 63 | 61 | 31 | 28 | 28 | 28 |
  | 4 | 84 | 95 | 51 | 48 | 47 | 47 |
  | 5 | 105 | 135 | 75 | 72 | 70 | 70 |
  | 6 | 126 | 181 | 103 | 100 | 97 | 97 |
  | 7 | 147 | 233 | 135 | 132 | 128 | 128 |
  | 8 | 168 | 291 | 171 | 168 | 163 | 163 |

  - Exact fits on all 7 sizes:
    - all-vertex count 2N² + 6N − 5;
    - out-window count 2N² + 5N − 5, equal to the most switches of one vertex. That is d_hntop's NM^U formula, box 34 §2.
  - The span count is 2N² + 6N − 8 for N ≥ 3 (N = 2: 13).
  - So W-changes of one vertex are Θ(N²) = Θ(n²/221). W-VLIN is dead, and W-VPOLY (≤ n²) holds with constant ≈ 1/220. No sign of
    super-quadratic growth.
  - Observers: tobs_K8_m32 and wobs_K8_m32 have all-vertex 17 / 16, span 13 / 13, out-window 8 / 8 (stretch 280 each). No inflation
    in the W-frame, because τ is frozen and the observer's W changes only with its fixed successor's.
- Composition: per guided stretch, the W route needs W-VPOLY-S. Its extremal family so far is H_n, quadratic; R120/R121 observers do
  not inflate it.

## DONE / FINDINGS / NEEDS
- DONE: odd/win.py; R121 pin copied; corpus runs; check.sh «box 38»; this note.
- FINDINGS:
  1. READING: SW-RETURN's rise lies in the out-window [leave, re-entry).
  2. DEAD: the in-window form (tobs_K8_m32: 248 at n 233).
  3. PROVED (lane): Lemma SPAN, ENT_R(v, c) ≤ n(1 + PCH^span_R(v, c)).
  4. Span COMPOSE: T = O(n³ m (1 + S*)).
  5. CONJECTURES RESET-LIN-S, CARRY-SEG-S, PCH-QUAD-S.
  6. §6: W-ENT in out-window form (PROVED lane); CONJECTURE W-VPOLY-S; hntop_N exact fits 2N²+6N−5 (all), 2N²+5N−5 (out-windows).
- NEEDS: none from the owner.
