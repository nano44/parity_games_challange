# R126: the premises of L-SI box 40 §6 (Lemma FRESH-SPLIT). No kill. Every premise is bounded both by the λ-run length and by the boundaries inside the pair's span. So a polynomial-form kill IS an exponential N5 run, and a "≥ n³ on a growing family" kill needs a λ-run > n³ (best known ≈ n²/77). DATA: LATE ≤ 4, BA ≤ 4 per pair on the corpus; MIN 541 = 1.56n (carryobs K 12). READING + DATA
L-RED successor 31 (Opus 5.5; D1/D18), woken from park by the Lead 2026-10-30 00:09Z: "Your adversary job is the premises of L-SI's live
reduction ... l-si 94bb55db, docs/si/N5-CUT-box40.md §6, Lemma FRESH-SPLIT. G-N5-TIME ⇐ (BA) ∧ (LATE) ∧ MIN-QUAD (same-frame W) ∧
SIL/CYC poly ... 1. Try to KILL LATE-per-edge ... ≥ n³ on a growing family ... 2. MIN-QUAD. 3. BA ... If a kill fails, give the exact
obstruction ... the largest measured value per n with the generator SHA." Written 2026-10-30 from 00:13Z (date -u). Labels: READING /
DATA / OPEN. Not a TARGET.md claim; G-N5-TIME OPEN.

## 1. Counter (experiments/red/cut/cutsl.py, sha1 ed460f36d24c)
- A copy of L-SI's odd/cutsx.py at l-si 94bb55db. The classification code is unchanged line for line; `diff` against the original
  shows only the docstring, the ROOT path (LSI_ROOT, default /tmp/claude-0/lsi, a worktree of origin/claude/l-si at 94bb55db) and
  per-pair counters.
- Added, per pair (v, c) and λ-run:
  - maxLATEp: FR_LATE re-entries;
  - maxBAp: CUTRE + FR_GAIN0 + FR_SAME, i.e. #F + #G0 + #SAME = box 40's BA;
  - maxGp: non-guided transitions inside span(v, c), i.e. the boundaries;
  - the pair attaining maxLATEp, with its G.
- FR=1 throughout (box 40 §6's frame). VIOL = FR_LATE_V = 0 on every instance below.

## 2. READING: what bounds each premise (elementary, from box 40's own lemmas)
- Per pair and λ-run R, box 40 §2 (PROVED lane) gives three facts:
  - every FRESH re-entry's window contains its piece's opening boundary;
  - every F re-entry IS a boundary;
  - the windows of distinct re-entries are disjoint.
  LATE, G0 and SAME are subclasses of FRESH (§6). Hence
  LATE_R(v, c) + BA_R(v, c) ≤ FC_R(v, c) ≤ G_vc := #boundaries (Even fallbacks, τ-changing or non-S4a transitions) inside span(v, c).
  Trivially also LATE + BA ≤ ENT_R(v, c) ≤ |R|.
- Consequences.
  - (LATE) per edge, polynomial form: LATE ≤ ENT ≤ T. A super-polynomial LATE family is a super-polynomial N5 run, so a kill of the
    polynomial form is a kill of G-N5-TIME itself. The premise is implied by G-N5-TIME; it is not an independent weak point.
  - (LATE) "≥ n³ on a growing family": needs ENT ≥ n³ for one pair inside one λ-run, so |R| ≥ n³. The longest known λ-run is
    2K(m − 1) ≈ n²/77 (R124, bidir); R124 §2 and R125 give the obstruction to a third factor. Also LATE ≤ G_vc: one pair needs n³
    boundaries inside its span. The boundaries are Even fallbacks (FB-LIN data ≤ 0.79n per phase) and τ-changes (R111: ≤ Θ(n²) in one
    joint λ-run, dual runquad 264 at n 192).
  - (BA): BA ≤ G_vc. A BA kill is a kill of the boundary count inside one span: Even fallbacks (an FB-LIN / ρ-POLY kill) or τ-changes
    (the Odd half, COMPOSE-FREEZE (d)). Per the Lead's rule, these are the same kill, not two. The polynomial form is again implied by
    G-N5-TIME (BA ≤ T).
  - MIN-QUAD: min(PCH^span, WCH*^span) ≤ |span| ≤ |R| (one change per transition). A kill needs a λ-run > n² (R123 §3 / R124).
- So all four premises are dominated by the two per-λ-run quantities that R123-R125 attacked: the λ-run length, and the boundaries in
  it. The reduction re-expresses G-N5-TIME. Its only content beyond the target lies in the exponents: FC-LIN (FC ≤ n − 1) and MIN-QUAD's
  n².

## 3. DATA: largest measured values (cutsl.py FR=1; spanw.py for MIN; S3 start unless a .start is given)
| instance (generator / sha1) | n | iterations | boundaries in the run | maxLATEp | maxBAp | maxGp | max MIN | maxENT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| red/so/instances/rise_thin51_n40 (corpus max LATE per pair) | 40 | 78 | 7 | 4 (pair (17, 0), G 5) | 4 | 6 | (box 39: PCH 55, WCH 0) | 5 |
| red/so/instances/njb_reabs65_n48 (corpus max FR_LATE total, 21) | 48 | 70 | 29 | 2 (pair (1, 0), G 4) | 2 | 25 | not run | 3 |
| red/so/instances/rise_fb38_n48 | 48 | 53 | 38 | 1 | 1 | 25 | not run | 2 |
| red/ctl/instances/d_runquad_K8_m30_n192 (R111, 264 τ-changes) | 192 | 264 | 264 | 0 | 0 | 0 (σ constant: no Even pairs) | — | 0 |
| span/instances/bidir_K8_m32 (mkrb.py acabdcf6ef20) | 198 | 528 | 0 | 0 | 0 | 0 | not run | 8 |
| span/instances/spanobs_K12_m48 (spanobs.py ea22405e9d23) | 346 | 612 | 0 | 0 (L-SI box 40 addendum: all re-entries W-paid) | 0 | 0 | 22 | 12 |
| span/instances/carryobs_K12_m48 (carryobs.py 577c9b0529da) | 346 | 612 | 0 | 0 (L-SI addendum) | 0 | 0 | 541 = 1.56n (τ constant, so WCH* = WCH) | 13 |
- Corpus (L-SI odd/out/cutsx_corpus_fr.txt, 719 games): FR_LATE total per game ≤ 21. Per pair, on the four games with the largest
  totals (above), ≤ 4.
- MIN growth on my families: carryobs SEG = PCH^span = WCH^span = (K − 1)(m + 1) + 2 ≈ n²/200 (R123 §4); MIN-QUAD holds with a
  factor ≈ 200 to spare.

## 4. Obstruction for a LATE family linear in n or more (READING; what a design must do)
- A LATE re-entry of (v, c) needs, inside v's out-window:
  - (a) a boundary;
  - (b) after it, a piece [a, j] with W*(c) constant, (v, c) blocked at j − 2 (W*(c) ▷ W*(σ v), not Ξ-improving), and a Ξ-onset of c
    at j − 2 -> j − 1 with j − 1 > a.
- (b) is easy with an Odd observer c whose τ fixes W(c) (spanobs's yh): its Ξ crosses a threshold mid-wave while W(c) = W(h) is
  constant after the h-step. The leave is also easy (d -> θ -> h′, θ a marker between the q's: Ξ(d) tracks V_i).
- (a) is the obstruction: one boundary per cycle, placed after the h-step and at least two transitions before the onset.
  - A τ-change there needs an Odd clock ticking once per Even cycle in step with it: R113's coupling problem; R125 shows the reused
    gate version dies on U-stability.
  - A fallback there needs a moment at which every Even improving switch is W-blocked. mkr-type waves never stall, so this needs a
    W-closed gate that only a fallback opens. Its closed side must be W ≫ Ξ (a top-marker τ-route as in mkr's C_i), and τ-stable
    against its honest option (U-wise, by a better loop behind the honest option). That is mkr's own device, but REUSED once per
    cycle: R108 §4's re-close condition again. Not built.
  - Dense boundaries do not help. With a boundary at every transition (union with d_runquad), every FRESH re-entry has j − 1 = a and is
    G0, i.e. BA, not LATE; and BA ≤ ENT ≈ K per pair on these clocks.
- Even a working design gives LATE ≤ ENT ≈ (number of cycles) = O(n) per pair on two-factor clocks: linear, not n³.

## DONE / FINDINGS / NEEDS
- DONE: cut/cutsl.py (faithful copy of cutsx.py at 94bb55db plus per-pair counters); runs above; this note. No pin (no kill).
- FINDINGS:
  1. READING: LATE + BA ≤ FC ≤ G_vc (boundaries in the span), and ≤ ENT ≤ |R|. MIN ≤ |R|. A super-polynomial kill of any premise is an
     exponential N5 run. An n³ LATE kill needs a λ-run > n³. A BA kill = an FB-LIN / ρ-POLY kill or a τ-change (Odd half) kill
     (counted once).
  2. DATA: corpus max LATE per pair 4 and BA per pair 4 (rise_thin51_n40, n 40); my families 0 (no boundaries); max MIN 541 = 1.56n ≈
     n²/221 (carryobs_K12_m48).
  3. READING: a LATE-linear family needs one boundary per Even cycle at a set phase of the wave: a coupled Odd tick (R113, R125) or a
     reused fallback-only gate (R108 §4). Both are the known obstructions.
- NEEDS: none from the owner.
