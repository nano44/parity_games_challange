# P-N5-GD fixes (box 43 packet, filed in box 44): the referees' notes, written out
L-NEW successor 23 (Opus 5.5, D14/D18, L40), session_011WFfFqRNrU1a8LQwbwazZN. Written 2026-10-26 02:46Z by date -u, at the Lead's order of
02:47Z (Lead's stamp): "repairs only: write the GD fixes file … and freeze it." FROZEN at push; its sha1 is reported to the Lead.
- Object: packet docs/new/P-N5-GD-box43.md, sha1 b898ff8256bf444ef90d69eb3154f5fe16dddf10 (l-new 205c9ed7). The packet is NOT edited; this
  file is its correction layer, a record of the reports, not refereed text. No signed statement changes.
- Sources:
  - REFEREE: docs/referee/R-N5-GD.md (referee a50f6623, successor 11): every statement SIGNED, no gap; premise class CONFIRMED; notes
    GD-N1..N3. §C (referee a639e39e, against R2 ab4a5af0): identical verdicts; GD-N1 = N-GD-1.
  - REFEREE-2: docs/referee-2/R2-N5-GD.md (referee-2 ab4a5af0, successor 13): all SIGN, no gap; premise class CONFIRMED; notes N-GD-1,
    N-GD-2. §C (referee-2 6e12b2bc): identical; "nothing open".
  - Both §Cs are on origin/claude/referee and origin/claude/referee-2 (cited by branch SHA).
- Scope unchanged: lemmas on every game; nothing bounds N5's running time on any class beyond 𝒞^1O ∪ 𝒞^1E. G-N5-TIME stays open.

## 1. Lines (no gap; notes only)
| note(s) | where in the packet | line to read with the packet |
| --- | --- | --- |
| GD-N1 = N-GD-1 (found independently) | §0 Premises, "R18 (d) Lemma S (c): S4a returns σ_k iff σ_k is a pointwise optimum of its arena" | Read "⇒" for "iff": the landed statement is "S4a's output is a pointwise arena optimum", so S4a returning σ_k makes σ_k a pointwise optimum of its arena. The converse depends on S1's tie-breaks and is not landed. Only "⇒" is used (F1°_D step 4). |
| GD-N2 (REFEREE; accepted by REFEREE-2) | §1 Lemma F1°_D, step 4, the sentence "Since k+1 ∈ I, z ∈ F_D." | Read: "x's switched successor x* := σ_{k+1}(x) lies in F_D (x ∈ F_D at k+1, and F_D is closed under σ_{k+1})." The argument concerns the target S4c actually takes, not an arbitrary gate target z. Every gate edge from F_D is flat (the preceding sentences), so x* is flat too; the conclusion (switched F_D vertices are own cycle nodes, flat switches into their own regions, no value change) stands. |
| GD-N3 (REFEREE; DATA only) | §1 Lemma Wo_D | DATA: in REFEREE's random games Wo_D's conclusion also held at all 66 transitions where (h_D) failed at k or k+1 (REFEREE-2's checker evaluated Wo_D only under (h_D)). The data do not show (h_D) necessary; the proof uses it (b ∈ F_D, u not its own W-cycle node). Not a gap; the statement is unchanged. |
| premise class: N-GD-2 + REFEREE §1 (recommended by both) | §0 Premises, "Class of the premises (READING …; referees to confirm)" | CONFIRMED by both referees, each by reading the source proofs: R15 (a), R17 (a)-(c), R18 (c) flat case, R18 (d) Lemma S (a) and (c) (in the "⇒" form), R21 (a) XW and R21 (c) FBL-N (i) are game-general (no one-Odd step; R17 and R18's flat case are one-player statements, applied to G_τ, its arenas and 𝓕, which are one-player on every game). Two landed lemmas DO have a genuine one-Odd step: R21 (c) FBL-N (ii) ("x's (σ_k, τ)-play avoids o, so σ_k(x) ∈ F_k") and R22 (a) F1° step 1 ("F contains no vertex with an Odd choice (o ∉ F)"). The packet does not cite either as a premise; it re-proves both in set form (F1°_D steps 1 and 4: closure of F_D and G_D (a); 𝓕 one-player because Odd is fixed to τ). REFEREE-2 suggests a landing note "proof game-general, checked by REFEREE-2 (R2-N5-GD §4)" against each of R18 (c) flat case, R18 (d) (a), (c), R21 (a), R21 (c) (i). |
