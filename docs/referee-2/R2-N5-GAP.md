# R2-N5-GAP: REFEREE-2 report on packet P-N5-GAP (L-NEW box 69): the gap set {Ξ ≠ W} at in-phase fallbacks; FB-LIN as a reduction
Referee: REFEREE-2 successor 21, Opus 5.5 (D15, L37; D1 "Never downgrade the referee to save money"), independent second referee.
Written 2026-10-30 from 01:41Z (date -u).

**Object.**
- docs/new/P-N5-GAP-box69.md at l-new 28ceeadc: sha1 d67f8e04b54d5621ebecf27e7fe7151ce57793cd, 175 lines.
- Line proposal docs/new/P-N5-GAP-box69-line.txt at l-new 901f242d: sha1 f1c5c5d5f4ec824da68df6b56a0b60322fe1b0ec.
- Both are measured with `git show <rev>:<path> | sha1sum`, equal the Lead's figures, and are ancestors of origin/claude/l-new.
- Premises read: SPEC S1-S5 @ da3fa7fa; RESULTS R15 (a), (d), R17 (a), R21 (a), R38 (a), R57 (a) and its standing premise, R88; R17's object
  box10 [⊕], [V1], [V2].

**Independence.** `git ls-tree --name-only -r origin/claude/referee docs/referee/ | grep -ic gap`: 0 at 01:41Z and at push time (see commit). Names only; nothing
opened; no `git log` on origin/claude/referee. The lane's box66-box68 scripts were run only as the pinned blocks (check.sh l. 315-332, in a
detached worktree at 28ceeadc under `set -euo pipefail`; exit 0, three PASS lines; logs/pinned_check.txt). My control is my own code:
R2-N5-GAP/gap_check.py (on my lane's dual_check.Runner, SPEC N5 on si.py), case2u.py, gquote.py.

**Scope (D1, D18).** A REDUCTION of CONJECTURE FB-LIN. Σ_v WCH^S4a_P(v) and ZF_P are not bounded; FB-LIN and G-N5-TIME stay OPEN. Not a TARGET.md
claim.

## 0. Verdicts (all "(Opus 5.5, D15)")
| § | item | verdict |
| --- | --- | --- |
| 1 | setting, definitions, premises | well formed; 11/11 quotes verbatim (gquote.py; SHIFT=1 0/6 SPEC quotes) |
| 2.1 | Lemma XW | SIGNED (standing premise R57 (a) (VJ): N-GAP-1) |
| 2.2 | Lemma W-MON | SIGNED (standing SPEC premise of R57: S4a's σ_new is the optimum of H_t; N-GAP-1) |
| 2.3 | Lemma FB-W | SIGNED (same premise) |
| 2.4 | Lemma OPT-OFF | **SIGNED with gap G-GAP-1** (proof step). Case 2's «Ω_ρ(c) is \|π\| + 1 longer» and (ii)'s «longer wins, so u is odd» are false when the cycle node u lies on π (v on u's cycle, c's play meets u before v). The statement is TRUE: the repair (§2.4) is two lines, and the data show 0 violations. |
| 2.5 | Lemma W-SUCC | SIGNED (uses OPT-OFF's statement, which holds) |
| 3.1 | Lemma LATE-W | SIGNED |
| 3.2 | Corollary LATE-PIECE | SIGNED (CL's t′ should be fixed, e.g. as the earliest blocked state: N-GAP-3) |
| 4.1 | Lemma GAP-MON | SIGNED |
| 4.2 | Lemma SW-IN | SIGNED |
| 4.3 | Lemma Z-FLAT | SIGNED (a list of consequences, not a characterisation: N-GAP-5) |
| 4.4 | Lemma REOPEN-W, Corollary REOPEN-CHARGE | SIGNED |
| 5 | Theorem GAP-RED | SIGNED. The bullet after the proof overstates: FB-LIN (≤ n) does not follow from polynomial bounds, only a polynomial form does (N-GAP-4; not in the line) |
| 6 | DEAD, DATA, READING | not signed. Pinned blocks PASS. Lane DATA reproduced, except one run whose start file is invalid (§4) |
| — | line proposal f1c5c5d5 | MATCHES §2-§5. Every symbol is defined or cited; it claims nothing beyond. Precision only: name the standing premise; fix CL's window (N-GAP-3) |

One gap, G-GAP-1: a proof step of OPT-OFF, repaired here; the statement is not in doubt. Nothing FALSE. Notes N-GAP-1..N-GAP-7.

## 2. Carried lemmas
- **XW** ✓. σ̄_t is the pointwise minimum over Odd's replies (S1-Xi = R57 (a) (VJ)), and τ_t is one reply. Data XW: 0.
- **W-MON** ✓. σ_{t+1} is the optimum of the one-player game H_t (S4a; standing premise); σ_t ⊆ H_t; [F1]. The frame is τ_t. Data WM: 0.
- **FB-W** ✓.
  - S4c fires only if S4a's σ_new = σ_k, so σ_k is the optimum of H_k (Iσ_k ≠ ∅).
  - σ_{k+1} ∈ H_k, and τ_{k+1} = τ_k.
  - [F1] gives W_{k+1} ⊴ W_k.
  - Data FBW: 0 at every τ-fixed Even fallback.
- **OPT-OFF.**
  - Case 1 (the ρ-play from c avoids v) ✓. One wording point: "both plays avoid v" should be "both paths to the cycle node avoid v". When v
    lies on its own cycle, ρv's PLAY returns to v, but [V1] gives exactly the path condition [V2] needs (N-GAP-2).
  - Case 2 (the play from c visits v; π := the part before the first v; u := v's cycle node). The text assumes c's play meets v BEFORE u.
    The other sub-case is real: v on u's cycle, and c's play enters the cycle and meets u before v (u ∈ π). Then:
    - Ω_ρ(c) = (u, P_c, idx_π(u)) and Ω_ρ(ρv) = (u, ∅, ·), with P_c = S: «path sets differ exactly in S» still holds;
    - but «Ω_ρ(c) is |π| + 1 longer» is false (idx_π(u) < |π|);
    - and (ii)'s «longer wins, so u is odd» does not follow.
  - Instance (case2u.py, saved as case2u_inst.pg; n 3):
    - vertices 0 (Even, Ω 1, succ 0, 1, 2), 1 (Odd, Ω 2, succ 0, 1, 2), 2 (Even, Ω 1, succ 0, 1); τ(1) = 0;
    - Even's optimal reply ρ(0) = ρ(2) = 1;
    - v = 0 lies on the cycle 0 → 1 → 0 with cycle node u = 1 (even);
    - c = 2: π = (2, 1) ∋ u; Ω(c) = (1, ∅, 1) and Ω(ρv) = (1, ∅, 0): 1 longer, not |π| + 1 = 3.
  - Census over all checked configurations (pairs v, (v, c) with v not its own cycle node), with "u even" being where (ii)'s parity step
    fails:

    | where | u ∈ π | of which S = ∅, u even |
    | --- | --- | --- |
    | one-player games (onep) | 8,907 | 6,957 |
    | run states (S4a steps), sbcg | 17,139 | 15,355 |

  - **Repair (G-GAP-1):** split Case 1 / Case 2 by "the ρ-PATH from c to its cycle node avoids v" instead of "the play avoids v".
    - If u ∈ π, that path avoids v.
    - (i) is unchanged when S ≠ ∅: S's top is the top of Z and is even, so it contradicts [F1].
    - When S = ∅, Ω_ρ′(v) = v ⊕ Ω_ρ(c) (Z's top is u), and Ω_ρ(v) = v ⊕ Ω_ρ(ρv) [V1]; both paths avoid v, so [V2] gives the contradiction
      exactly as in Case 1.
    - With this split, Case 2 is "c's path meets v before u", where the packet's length and parity steps are correct.
  - **Statement:** TRUE. Data OO: 0 violations in 65,486 one-player checks (random one-player games, ρ = Even's optimal reply on G^d, ρ's
    optimality itself checked against random strategies, 31,500 checks) and 647,486 run checks (every S4a step on sbcg, ρ = σ_{t+1} in H_t).
  - The same statement is P-N5-CUT's OPT-OFF (ii), whose proof covers this sub-case (its Case 3).
  - Control X_OO_own (v its own cycle node) bites: the off-cycle premise is needed.
- **W-SUCC** ✓ (per step: W-MON, plus OPT-OFF in H_t at t + 1 with v not its own W-cycle node). Data WS: 0 on 473,219 checks (sbcg).

## 3. Late adoptions inside a piece
- **LATE-W** ✓. blocked at t′ ▷ ⊵ W-SUCC on [s + 1, t′] ⊵ OPT-OFF in H_s at s + 1 ((v, c) = (v, σ_s v), v off its own W-cycle at s + 1).
  Data LW: 0 for EVERY leave and EVERY later blocked state whose window has v off its own cycle (3,558 on sbcg; 2,417 on alt_all).
- **LATE-PIECE** ✓.
  - For i ≥ 2, the latest leave s_i > u_{i−1}: v holds c from u_{i−1} + 1, and any adoption between would be later. So the windows
    (s_i, t′_i] ⊆ (u_{i−1}, u_i] are disjoint.
  - LATE-W applies inside Q: s_i ≥ u_{i−1} + 1 ∈ Q and t′_i ≤ u_i ∈ Q. Otherwise the adoption is counted in CL.
  - CL depends on which blocked state t′ is taken as the window's end; any fixed choice works. I use the earliest (N-GAP-3).
  - At most one adoption is re-blocked vacuously: with no leave of c in Q before u, v never held c in Q.
  - Data LP: 0 (1,581 re-blocked adoptions on sbcg). Late adoptions that are not re-blocked (not counted by the corollary): X_LP_nore 38 on
    sbcg, 7 on alt_all.

## 4. The gap set, GAP-RED
- **GAP-MON** ✓: W_{k+1}(v) ⊴ W_k(v) = Ξ_k(v) ⊴ Ξ_{k+1}(v) ⊴ W_{k+1}(v) for v ∉ Z_k.
- **SW-IN** ✓.
  - w ∈ Iσ_k(v) gives b := Ξ_{k+1}(w) ⊵ Ξ_k(w) ▷ a := Ξ_k(σ_k v).
  - [V1] holds at k and at k + 1 (v is its own Ξ-cycle node at neither), and the paths of a and b avoid v. [V2] then gives v ⊕ b ▷ v ⊕ a.
  - GAP-MON excludes v ∉ Z_k.
  - Control X_SI_own: switched own-cycle-node vertices outside Z_k exist (31 on sbcg, 168 random), so the premise is needed.
- **Z-FLAT** ✓. Items (a)-(d) follow from GAP-MON, SW-IN, FB-W with R15, and the definition.
- **REOPEN-W, REOPEN-CHARGE** ✓.
- **GAP-RED** ✓.
  - Every in-phase transition is an S4a step or a τ-fixed Even fallback (checked at every in-phase transition).
  - |Z| ≥ 0; it drops by ≥ 1 at a non-Z-flat fallback; it rises by ≤ |Z_{k+1} ∖ Z_k| at an S4a step.
  - So f_P − ZF_P ≤ |Z_a| + RO_P. Then REOPEN-CHARGE.
  - Data GR, RC: 0 on every phase.
- **Data agreement with the lane (§6 DATA).** With the lane's corpus (alt_all 413 games + fb38_n48, pl130_n40, long121_n40; start file where
  present, else S3):
  - mine: 782 in-phase fallbacks, 56 Z-flat (= the lane's 56), 8,442 re-openings (all W-rises), GAP-MON 0;
  - the lane: 788 and 8,532.
  - The 6 fallbacks and 90 re-openings of difference come from red/n3/instances/comp54_n80, whose start file sets σ(11) = 51, a NON-EDGE.
    My checker validates start files and skips it. That run is not an N5 run (N-GAP-7).
  - nep22f_n64's 10 Z-flat fallbacks in one phase are reproduced (named.txt: max ZF 10). lend9_n8's 3 in-phase fallbacks with no |Z| drop are
    reproduced.
  - In no phase of any corpus does f_P exceed n (X_FBLIN 0; max f_P 38 on fb38_n48, n 48).
- Corpora (every log RESULT PASS, 0 violations of XW, WM, FBW, OO, WS, LW, LP, GM, SI, ZF, RW, RC, GR):
  - sbcg 719 games (S3);
  - alt_all 413 (pinned starts, and start-or-S3);
  - the named six with starts + S3 + random;
  - random 2,000 games n 5-14;
  - one-player random 10,500 games.

## 5. The line proposal (f1c5c5d5), clause by clause
- Setting: SPEC S1-S5; W_t; Z_t; phase (R38 (a)); in-phase; τ-fixed Even fallback (S4c with Iσ ≠ ∅); piece; blocked (R88). All match §1.
- XW, W-MON ("read with τ_t"), FB-W, OPT-OFF ("an optimal strategy ρ of a one-player game …"), W-SUCC: match §2. OPT-OFF's statement is true;
  G-GAP-1 is about the proof only.
- LATE-W, LATE-PIECE: match §3.
  - The parenthetical «blocked at some state of Q since v's latest leave of c in Q, or, if v has not left c in Q, at some earlier state of Q»
    = "re-blocked".
  - «CL_Q(v, c) those whose leave-to-block window has v as its own W-cycle node» should read "at some state", and fix the window's end
    (N-GAP-3). Precision.
- GAP-MON, SW-IN, Z-FLAT, REOPEN-W: match §4.
- GAP-RED: every symbol defined (f_P, RO_P, WCH^S4a_P, ZF_P). Matches §5.
- Scope tail: matches. The overstated §5 bullet (N-GAP-4) is NOT in the line.
- Precision: the standing SPEC premise of R57 (S1's procedure realises the VJ optimum) underlies XW, W-MON, FB-W and the use of OPT-OFF at S4a
  steps. The line may name it as R57's own line does (N-GAP-1).
- **Verdict on the line: MATCHES.** No required change.

## 6. Notes
- N-GAP-1 (standing premise). XW uses R57 (a) (VJ). W-MON, FB-W and W-SUCC's application of OPT-OFF use that S4a's σ_new (S1 on the dual of
  H) is the pointwise optimum of H and is realised by plays: the standing SPEC premise of R57 / R51 (d) (1E-N3), as in R88, R89 (FR-N1) and
  P-N5-CUT. Name it. G-N5T-1 (the code link) is used by no proof.
- N-GAP-2 (OPT-OFF Case 1 wording). "both plays avoid v" → "both paths to the cycle node avoid v" ([V1]).
- N-GAP-3 (LATE-PIECE). Fix the window [s + 1, t′] in CL, for instance t′ := the earliest blocked state in [s + 1, u]. The proof works for
  any fixed choice; the count depends on it.
- N-GAP-4 (§5's bullet). «CONJECTURE FB-LIN (≤ n in-phase fallbacks per phase) and any polynomial form of it follow from polynomial bounds …»
  is too strong for FB-LIN itself. Polynomial bounds on Σ WCH^S4a and ZF give a polynomial form. FB-LIN needs RO_P + ZF_P ≤ n − |Z_a|, or
  the like.
- N-GAP-5 (Z-FLAT). It is labelled a characterisation, but it states consequences only (no converse). Rename it or add the converse.
- N-GAP-6 (relation to P-N5-CUT). GAP's OPT-OFF is CUT's OPT-OFF (ii) in general one-player form. CUT's three-case proof is complete; GAP's
  two-case proof needs G-GAP-1's split. The two lanes could share one statement and proof.
- N-GAP-7 (DATA, start files). The lane's §6 counts include comp54_n80 run from a start file with a non-edge (11 → 51). This is the same
  trap noted for P-N5-CORE (successor 19, trap 1). Validate start files.

## 7. DONE / FINDINGS / NEEDS
- DONE: this report; docs/referee-2/R2-N5-GAP/{gap_check.py, case2u.py, case2u_inst.pg, gquote.py, named.lst, dataset3.lst, run_all.sh, logs/}.
- FINDINGS:
  - Twelve items SIGNED. OPT-OFF is SIGNED with gap G-GAP-1, a proof step: Case 2 misses the configuration u ∈ π. The repair is given and the
    statement holds (713k checks).
  - The line MATCHES.
  - The lane's DATA is reproduced, except one run from an invalid start (comp54_n80).
- NEEDS: Lead: route G-GAP-1 (repair text in §2) and N-GAP-1..7 to L-NEW. §C on your word after REFEREE 19's GAP report.
