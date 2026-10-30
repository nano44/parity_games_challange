# N5-SC (box 70): premise SC* of P-N5-CUT. W-silent re-entries are tied Ξ-climbs at gap vertices; with FB-LIN's Z-flat residue they fold into one count GXC
L-NEW successor 35 (Opus 5.5), D14 / D18, Lead reading L40. Lead's brief 2026-10-30 01:23Z (BOX 70: a lane proof that SC* of L-SI's frozen
P-N5-CUT is polynomial, ideally ≤ poly(n)·(B* + 1), or the exact obstruction and an instance; use LATE-W / LATE-PIECE / GAP-MON; quote L-SI's
definitions, do not re-define them). Written from ~01:35Z (date -u). Working note, unrefereed, not a TARGET.md claim. G-N5-TIME OPEN.
Labels: PROVED (lane) / CONJECTURE / DATA / DEAD / READING.
- Source read: l-si 2678f6c6, docs/si/P-N5-CUT-box43.md (frozen packet) §2-§4, §8. Its definitions are quoted, not restated.
- Tool: experiments/new/box70/silent.py. It re-implements the classes of P-N5-CUT §4 from the packet text. Validation against L-SI's
  cutsx.py totals (l-si experiments/si/odd/out/cutsx_corpus_fr.txt): S 42, C 4 on the 719-game corpus (box59/sbcg.lst), identical;
  u23sw64_n32 S 31; cw11_n24 C 3, F 12, FR 2. Runs: box70/silent_sbcg.txt (719), silent_alt.txt (alt_all, 413, with starts).

## 0. The premise, quoted
- [Q l-si 2678f6c6 docs/si/P-N5-CUT-box43.md §8] «SC* := max_R Σ_{(v, c)} (SIL_R(v, c) + CYC_R(v, c)) over Even edges.»
- [Q §4] «Classes. Every re-entry j − 1 → j of v into c in R is exactly one of: F — j − 1 → j is an Even S4c fallback; FR (FRESH) — an S4a step
  with no anchor; C — an anchor exists, q := the smallest, and v is its own cycle node for τ* at some state of [q, j]; P — otherwise, and W*(c)
  changes on [q, j]; S — the rest (silent: W*_j(σ_{j−1} v) = W*_j(c) by §3).» «SIL_R(v, c) := #S, CYC_R(v, c) := #C».
- [Q §3] «τ* := τ_{j−1}, [a, b] the τ*-piece containing j − 1, W* := W^{τ*}. An ANCHOR is a state q with max(s, a) ≤ q − 1 ≤ j − 2 and
  (v, c) ∈ H_{q−1}.» Lemma W-RETURN-G: «If an anchor q exists, v is off-cycle for τ* at every state of [q, j], and W*_t(c) is the same for all
  t ∈ [q, j], then W*_j(σ_{j−1} v) = W*_j(c).» Its proof's chain: «W*_q(c) ⊴ W*_q(σ_q v) … ⊴ W*_{j−1}(σ_{j−1} v) … ⊴ W*_j(σ_{j−1} v) ⊴ W*_j(σ_j v)
  = W*_j(c) … The ends are equal, so every link is an equality.»
- Z_t := {v : Ξ_t(v) ≠ W_t(v)} (P-N5-GAP §1, W_t read with τ_t).

## 1. DATA first
- S: 42 re-entries in 719 games. C: 4. Of 11,669 re-entries in all.
- Per (λ-run, edge): S ≤ 1 (u1t_cex_n32 and others), C ≤ 3 (cw11_n24). Per (piece, edge): S ≤ 1.
- SC* record: 31 in one λ-run of u23sw64_n32 (n 32, 16 iterations, 1 fallback). There all 31 re-entries are S, one per edge.
- Every one of the 42 S re-entries falls on a GLOBALLY W-flat transition (W*_{j−1} = W*_j at every vertex), and has v ∈ Z at j − 1 and j.

## 2. Lemma SIL-Z (PROVED, lane)
Let j − 1 → j be an S re-entry of v into c in the λ-run R (P-N5-CUT §4), with smallest anchor q, d := σ_{j−1}(v), and suppose v is not its own
Ξ-cycle node at j − 1 or at j. Then:
- (a) W*_{j−1}(d) = W*_j(d) = W*_j(c) = W*_{j−1}(c), and W*_j(v) = W*_{j−1}(v);
- (b) d ∈ Z_{j−1} and v ∈ Z_{j−1};
- (c) Ξ_j(v) ▷ Ξ_{j−1}(v).
Proof.
- (a) The class-S chain of W-RETURN-G is an equality throughout. Its links W*_{j−1}(σ_{j−1} v) ⊴ W*_j(σ_{j−1} v) ⊴ W*_j(c) give the first two
  equalities. "W*(c) is the same for all t ∈ [q, j]" with q ≤ j − 1 gives the third. Class S excludes C, so v is not its own W*-cycle node
  on [q, j]. By [V1] (P-N5-GAP §1), W*_t(v) = v ⊕ W*_t(σ_t v) at t = j − 1, j, and the two successor values are equal.
- (b) τ_{j−1} = τ*, so W_{j−1} = W*_{j−1}. j − 1 → j is an S4a step switching v to c ≠ d, so (v, c) ∈ Iσ_{j−1} ([S4a]) and Ξ_{j−1}(c) ▷
  Ξ_{j−1}(d) ([S2]). By XW, Ξ_{j−1}(c) ⊴ W*_{j−1}(c) = W*_{j−1}(d). So Ξ_{j−1}(d) ◁ W*_{j−1}(d), i.e. d ∈ Z_{j−1}.
  For v: Ξ_{j−1}(v) = v ⊕ Ξ_{j−1}(d) and W*_{j−1}(v) = v ⊕ W*_{j−1}(d), both plays avoid v ([V1], v off both cycles). [V2] strict gives
  Ξ_{j−1}(v) ◁ W*_{j−1}(v), so v ∈ Z_{j−1}.
- (c) Ξ_j(c) ⊵ Ξ_{j−1}(c) ▷ Ξ_{j−1}(d) ([R15], [S2]), and both plays avoid v at their times ([V1] at j − 1 for d, at j for c). [V2]:
  Ξ_j(v) = v ⊕ Ξ_j(c) ▷ v ⊕ Ξ_{j−1}(d) = Ξ_{j−1}(v). □
- So an S re-entry is a strict Ξ-climb at a gap vertex v whose W-value does not move: a TIED Ξ-CLIMB. (v ∈ Z_j is not claimed; DATA: it
  holds in all 42.)

## 3. Corollary SC-GXC and the fold with FB-LIN's residue (PROVED, lane)
Definition. A GXC EVENT is a pair (v, t) with v Even, σ_{t+1}(v) ≠ σ_t(v), τ_{t+1} = τ_t, λ_Ξ unchanged at t → t + 1, v ∈ Z_t,
Ξ_{t+1}(v) ▷ Ξ_t(v), and W_{t+1}(v) ⊴ W_t(v). GXC_R := the GXC events with t, t + 1 in the λ-run R.
- (i) Σ_{(v, c)} SIL_R(v, c) ≤ GXC_R + NC_R + NT_R. Here NC_R counts the S re-entries at which v is its own Ξ-cycle node at j − 1 or j, and
  NT_R those with τ_j ≠ τ_{j−1}. Proof: by SIL-Z, every other S re-entry j − 1 → j of v gives the GXC event (v, j − 1). A transition switches
  v to one target, so distinct re-entries give distinct events. □
- (ii) For a phase P (P-N5-GAP §1): ZF_P ≤ GXC_P + NZ_P, NZ_P := the Z-flat in-phase fallbacks whose switched vertices are all their own
  Ξ-cycle node at k or k + 1. Proof: a Z-flat fallback k → k + 1 that switches some v off its own Ξ-cycle at k and k + 1 has v ∈ Z_k
  and Ξ_{k+1}(v) ▷ Ξ_k(v) (P-N5-GAP SW-IN), and W_{k+1}(v) ⊴ W_k(v) (FB-W). That is a GXC event; distinct fallbacks give distinct t. □
- READING: P-N5-CUT's [P-SC] (its S part) and P-N5-GAP's ZF residue are the SAME kind of event: a strict Ξ-climb at a gap vertex whose W does
  not rise. That is one premise, GXC, in place of two, up to the own-cycle and τ-changing corrections NC, NT, NZ.
- DATA (silent.py): every S re-entry is a GXC event in both corpora (S-not-GXC 0 in 719 + 413 runs). Max GXC per λ-run: 64 = 2n
  (u23sw64_n32).

## 4. What is not proved, and the obstruction (READING / DATA)
- GXC itself is not bounded here. A GXC event is a strict Ξ-rise at v inside a λ-run while W(v) stays, i.e. a path-set / length rise of
  Ξ(v) toward a fixed ceiling W(v). That is the Ξ-route (RISE / P*) again.
- Why "≤ 1 S re-entry per (piece, edge)" (DATA: true everywhere) is not provable this way: for two S re-entries j₁ < j₂ of (v, c) in one
  piece, the second has its own leave s₂ ≥ j₁ as anchor. W-RETURN-G's chain then only forces Ξ_{j₂−1}(c) ▷ Ξ_{s₂}(c), a Ξ-rise of c
  (P-N5-FRAME LATE-RISE). Nothing forbids it.
- C (own-cycle) re-entries: 4 in 719 games, ≤ 3 per edge (cw11_n24, in a λ-run with 12 F re-entries). Not bounded here. OPT-OFF fails at own
  cycle nodes (P-N5-CUT §2's tog6b_n32 instance), so the W-chain gives nothing there.
- No kill of [P-SC]: on u23sw64_n32 SC* = 31 < m_E (one S re-entry per edge, B* = 1).
- Target for a proof (CONJECTURE, OPEN, not proposed for signing): S re-entries ≤ 1 per (piece, edge), so Σ SIL_R ≤ m_E·(B_R + 1). DATA
  supports it (0 counterexamples in 1132 runs).

## DONE / FINDINGS / NEEDS
- DONE: box70/silent.py, run.sh; silent_sbcg.txt (719), silent_alt.txt (413); this note; check.sh "box 70".
- FINDINGS:
  (1) DATA: SC* record 31 (u23sw64_n32), all S, one per edge. Every S re-entry sits on a globally W-flat transition with v in the gap.
  (2) PROVED (lane): Lemma SIL-Z. An S re-entry is a strict Ξ-climb at a gap vertex with W(v) fixed. Its successor d before the switch is
  also in the gap.
  (3) PROVED (lane): Corollary SC-GXC. Σ SIL_R ≤ GXC_R + NC_R + NT_R, and FB-LIN's Z-flat residue ZF_P ≤ GXC_P + NZ_P. So P-N5-CUT's
  [P-SC] (S part) and P-N5-GAP's ZF fold into one count GXC.
  (4) OPEN: GXC poly (Ξ-route); C re-entries; CONJECTURE "≤ 1 S per (piece, edge)" (0 / 1132 runs), which would give Σ SIL ≤ m_E(B* + 1).
- NEEDS: none from the owner.
