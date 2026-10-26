# R2-N5-GD: second-referee check of packet P-N5-GD (L-NEW box 43/44: Lemma G_D (a), (b), (c1), (c2), Lemma F1°_D, Lemma Wo_D, on every game). REFEREE-2 (successor 13), written 2026-10-26 01:39Z-01:5xZ (date -u)
Signature: (Opus 5.5, D15). Lead queue item 5 (Lead 01:18Z, its stamp: "P-N5-GD (docs/new/P-N5-GD-box43.md, sha1 b898ff82, pinned trunk
3c6f6c16, L-NEW 23)").
Object: docs/new/P-N5-GD-box43.md, `git show 3c6f6c16:docs/new/P-N5-GD-box43.md | sha1sum` -> b898ff8256bf444ef90d69eb3154f5fe16dddf10
(= the Lead's pin; = my tree), 149 lines, added at 205c9ed7 (L-NEW successor 23). No fixes file in my tree.
Background read (texts, not recalled): SPEC S1-S5, FIX 1-4; RESULTS R15 (a), R17 (a)-(c), R18 (c), (d) with docs/new/N5-1Oacyc-box24.md
l. 50-86 (the flat case, proved in place) and docs/new/N5-time-box21.md §2.2 (Lemma S (a)-(c)), R19 (a), (b), R21 (a), (c) with P-N5-X §1-§3,
R22 (a), R25 setting ((C1)-(C4)), R38 (a).
Independence: no REFEREE file on GD exists in my tree (`ls docs/referee | grep -i gd` -> empty at 01:43Z); none opened. No grep of
docs/agents/ or RESULTS for this packet. The lane's experiments/new/box43/f1d.py was not run or imported; its instances
experiments/new/box43/instances/*.pg and the file list experiments/new/box41/lib41.txt are inputs only.
Tools (own code, docs/referee-2/R2-N5-GD/): gd_check.py (on R2-N5-DUAL/dual_check.Runner = own SPEC N5 loop on si.py, and
R2-N5-RE/re_check.Game play values), box43.lst, run_all.sh, logs/.
Labels: PROVED (L-NEW 22, re-checked by L-NEW 23). Every game. Not a running-time bound; Δ1, Δ-RT and the R20 coarse port are NOT signed (§3).

## Verdicts (Opus 5.5, D15)
| statement | verdict | gaps / notes |
| --- | --- | --- |
| Lemma G_D (a) (every game, no hypothesis) | SIGN | — |
| Lemma G_D (b) (every game, under (h_D) at k) | SIGN | — |
| Lemma G_D (c1), (c2) (every game, under (h_D), (h3_D)) | SIGN | — |
| Lemma F1°_D (every game, no (h_D), (h3_D)) | SIGN | N-GD-1 (R18 (d) Lemma S (c) is quoted as an "iff"; only "⇒" is landed and only "⇒" is used) |
| Lemma Wo_D (every game, under (h_D) at k and k+1) | SIGN | — |
| §0 "class of the premises" (READING, referees to confirm) | CONFIRMED (each source proof read) | N-GD-2 |
| §2 port table | checked as a READING | — |
| §3 (Δ1, Δ-RT, R20 coarse port), §4 | not signed (as briefed) | — |
No statement is NOT SIGNED and no gap is open. No (P). TARGET.md diff: not a claim of TARGET.md §2 (structural lemmas; no running time).

## 1. Lemma G_D: SIGN
- (a) ✓. v ∈ F_D: v's (σ_k, τ_k)-play meets no vertex of D_k; at its Odd vertices σ̄_k = τ_k (definition of D_k), at its Even vertices both
  plays use σ_k; by induction the two plays are equal, so Ξ_k(v) = W_k(v).
- (b) ✓. Both plays follow π_v to u = u(v) (π_v's Odd vertices are outside D_k). For x ∈ π_v, x's (σ, τ)-play is π_v's suffix then u, and its
  honest play is the same path (HP_D). If u's honest or W-play met x after leaving u, it would continue along x's (honest resp. W-) play to
  u ∈ D_k, against (h_D) at u. So both plays from u avoid π_v; no vertex of π_v lies on the final cycle; iterated (V1) gives both equations.
  (v ∈ D_k: π_v = ∅, trivial.)
- (c1) ✓. Common cycle node c by (h3_D); π_v ⊕ T = (c, A_v ∪ P(T), |π_v| + ℓ(T)) with A_v ∩ P(T) = ∅ (T's play avoids π_v); the symmetric
  difference A_y Δ A_z and the length difference |π_y| − |π_z| do not depend on T, and VJ00's order on equal cycle nodes reads only these.
- (c2) ✓. F_D by (a); on R_D, lev(Ξ(u), W(u)) ≤ M_D ≤ L gives equal COARSE_L at u ((C2); M_D = ⊥ gives equality), and (C4) along π_v (each ⊕ a
  (V1) step, by (b)) carries it to v. (h3_D) is what makes M_D < ∞.
- Remark after (c) (different terminals): correctly left OPEN as Δ-RT; nothing in (c1), (c2) claims it.

## 2. Lemma F1°_D: SIGN
- Step 1 ✓: Ξ = W on F_D (G_D (a)); F_D is closed under σ_k and τ (a successor along a play avoiding D_k has a tail avoiding D_k; at an Odd
  x ∈ F_D, x ∉ D_k so τ(x) = σ̄(x) is that successor); 𝓕 := G_τ[F_D] is one-player (Odd fixed to τ in G_τ) and every vertex keeps a successor
  in F_D. F_D and τ are constant on I, so 𝓕 is one fixed game.
- Step 2 ✓: on F_D, Ξ_k = W_k = 𝓕's valuation of σ_k|F_D (plays stay in F_D).
- Step 3 ✓: σ_{k+1}(x) ∈ {σ_k(x)} ∪ Iσ_k(x), and σ_{k+1}(x) ∈ F_D by closure at k + 1 (k + 1 ∈ I), so σ_{k+1}|F_D uses 𝓕-improving edges only
  (step 2); any arena strategy ρ of 𝓕 extended by σ_{k+1} is an S4a-arena strategy in G_τ; S4a's output is a pointwise arena optimum in G_τ
  (R18 (d) Lemma S (c): "σ_{k+1} maximises V_{·,τ_k} pointwise over A(σ_k)", R17 (F1) on the one-player arena); so σ_{k+1}|F_D is a
  pointwise optimum of 𝓕's arena: R17's switch-best step.
- Step 4 ✓: in a phase τ_{k+1} = τ_k, so the fallback is Even's (FIX 3); S4a returned σ_k, so σ_k is a pointwise arena optimum (FBL-N (i)).
  A switched edge (x, z) from F_D: z ∈ F_D (closure at k + 1), it is a gate edge, Ξ_k(z) ▷ Ξ_k(σ_k x) = W_k(σ_k x), XW gives W_k(z) ▷ W_k(σ_k x),
  so by R18 (c)'s flat case the edge is flat. Several flat switches at distinct W-cycle nodes do not interact and change no value: this is
  proved in the flat-case text itself (N5-1Oacyc-box24 l. 72-77: "Each switched x is its own cycle node, and its new cycle consists of x and
  vertices of cycle node x. So different switched vertices do not interact"). R_D switches do not reach 𝓕. So F_D-values are unchanged and
  R17 Lemma P's invariant (current values only) survives.
- Steps 5-6 ✓: λ on F_D = λ_Ξ = λ_W, constant in the phase, so the 𝓕-run is in one λ-phase of 𝓕; R17 Lemma P + Theorem PH: ≤ |F_D| − 1
  value-changing switch-best steps; fallbacks are value-preserving on F_D; by step 1 these are exactly I's transitions with a Ξ-change on F_D.
- N-GD-1 (citation, not a gap): the premise row reads "R18 (d) Lemma S (c): S4a returns σ_k iff σ_k is a pointwise optimum of its arena". The
  landed text (RESULTS R18 (d); box 21 §2.2 (c)) is "N5's arena step maximises V_{·,τ_k} over the arena": S4a's OUTPUT is a pointwise
  optimum, which gives "S4a returns σ_k ⇒ σ_k is an optimum". The converse is not landed (S4a may return another optimum of equal values,
  by its tie-breaks). Step 3 and step 4 use only "⇒". Fixes-file line: drop "iff" (read "if S4a returns σ_k, σ_k is a pointwise optimum").

## 3. Lemma Wo_D: SIGN
- ✓. b := τ(u), the same at k and k + 1. (h_D) at j ∈ {k, k + 1}: u's W-play does not return to D_j after u, so u is not its own W-cycle node
  and b's W-play avoids D_j: b ∈ F_D at j; W_j(b) = Ξ_j(b) (G_D (a)), and b's honest play (= its W-play) avoids u. (V1): W_j(u) = u ⊕ Ξ_j(b).
  R15 (a): Ξ_{k+1}(b) ⊵ Ξ_k(b); (V2) with u on neither play: W_{k+1}(u) ⊵ W_k(u). No phase or (h3_D) used ✓.

## 4. The premises' class (§0 READING): CONFIRMED (N-GD-2)
Each premise is signed under a 𝒞^1O setting line. I read each proof for a one-Odd step:
- R15 (a): signed on every game (Lemma A = VJ00 Lemma 5.7) ✓.
- R17 (a)-(c): one-player games, any ✓.
- R18 (c) flat case: N5-1Oacyc-box24 l. 50-86, an argument on an arbitrary one-player arena at an arbitrary optimum (cases B1, B2 of R17's
  Lemma P, plus "flat switches change no valuation") ✓; nothing about o.
- R18 (d) Lemma S (a), (c): box 21 §2.2: (a) is VJ00 (11) on G and on G^d with Lemma R; (c) is R17 (F1) on the one-player arena ✓.
- R21 (a) XW: P-N5-X §1, VJ00 §5.2 Prop. 5.1, Lemma 5.2 (11), R17 (F1) on the dual ✓ (also checked in my R2-N5-1O, N-1O-4).
- R21 (c) FBL-N (i): P-N5-X §3 "(i) As in §2", i.e. §2's "τ is fixed and τ_{k+1} = τ_k (S4c switches Odd only if Iσ_k = ∅, and then τ changes)"
  and "S4a returned σ_k, so σ_k is a pointwise arena optimum (R18 (d))": SPEC FIX 3 and S4a's optimality only ✓.
None uses the one-Odd property; the packet's uses (to G_τ and its arenas, one-player on every game; XW on G_σ) are within their proofs' scope.

## 5. DATA (gd_check.py; own play values; S3 + random starts; every game)
| set | runs | states | states with D ≠ ∅ / |D| ≥ 2 | (h_D) / (h_D) ∧ (h3_D) states | G_D (b) vertices | (c1) pairs | (c2) levels | Wo_D checks | F1°_D intervals | violations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lib41.txt (412 files, any class) × 3 starts | 1,236 | 19,515 | 13,933 / 3,660 | 13,733 / 13,112 | 82,082 | 704,296 | 55,550 | 7,039 | 12,759 | 0 |
| R2-N5-KW/files.lst (503 𝒞^1O) × 2 | 1,006 | 17,733 | 12,378 / 0 | 14,708 / 14,097 | 108,344 | 994,543 | 48,541 | 8,420 | 10,746 | 0 |
| box-43 instances (dch16_n44, ret2_n7, retf_n6, tj17_n19, tx2_n8) × 5 | 25 | 277 | 200 / 142 | 143 / 134 | 398 | 1,022 | 237 | 28 | 218 | 0 |
| random 𝒞^kO (any owners) n 4-14, random starts | 20,000 | 54,685 | 28,848 / 14,242 | 32,815 / 30,608 | 12,179 | 5,760 | 55,642 | 225 | 51,968 | 0 |
G_D (a) is checked at every state of every run (all 92,210 states). (c2) is checked at EVERY level L with M_D ≤ L ≤ n − 1 (the packet's
script checks one level, max(M_D, −1)). Max Ξ-changes on F_D per D-crossing-free interval: 55 (x32_rand64.pg).
Mutation controls (lib41, S3): gda (G_D (a) asked on R_D) 6,999; c2 (L = M_D − 1) 4,266; wo (Wo_D asks for no strict rise) 36; f1 (F1°_D with
|F_D| − 2) does NOT bite: no interval in the data comes within 1 of max(0, |F_D| − 1), so that bound's tightness is not tested here.

## 6. Notes (none blocks a signature)
- N-GD-1 (citation): R18 (d) Lemma S (c) is landed as "S4a's output is a pointwise arena optimum"; the packet's "iff" overstates it; only
  "⇒" is used.
- N-GD-2 (premise class): confirmed for every premise listed in §0, each by reading its proof (§4). A landing note could record "proof
  game-general, checked by REFEREE-2 (R2-N5-GD §4)" against each of R18 (c) flat case, R18 (d) (a), (c), R21 (a), R21 (c) (i).

## 7. Honest limits
- The landed premises were not re-proved; their proofs were read for one-Odd steps only.
- F1°_D's bound is not approached in data (above). Wo_D is exercised mostly on 𝒞^1O files (8,420) and lib41 (7,039); 225 checks on random
  multi-Odd games.

## §C (2026-10-26 02:4xZ by date -u; REFEREE-2 successor 13, Opus 5.5, D15): comparison with REFEREE's R-N5-GD
Read after my report was pushed (ab4a5af0, on trunk): docs/referee/R-N5-GD.md as on origin/claude/referee at a50f6623 (sha1 6b55155c…,
REFEREE successor 11; not yet on my merged trunk 77b5c9a3). Lead 02:37Z.
| statement | REFEREE | REFEREE-2 | same? |
| --- | --- | --- | --- |
| G_D (a), (b), (c1), (c2) | SIGNED | SIGN | yes |
| F1°_D | SIGNED (GD-N2) | SIGN (N-GD-1) | yes |
| Wo_D | SIGNED (GD-N3 data) | SIGN | yes |
| premise class (§0 READING) | CONFIRMED (GD-N1) | CONFIRMED (N-GD-2) | yes |
| §2 port table | checked, correct | checked as a READING | yes |
| §3, §4 | not signed | not signed | yes |
- C.1 Joint gap map: empty.
  - GD-N1 = N-GD-1 (Lemma S (c) quoted as "iff"; only "⇒" landed and used), found independently, same fixes line.
  - REFEREE's premise table also lists R21 (c) FBL-N (ii) and R22 (a) step 1 as the two landed lemmas WITH a one-Odd step, noting the packet
    re-proves both in set form rather than citing them. I agree (my §2 step 4 and step 1 checks are those re-proofs); my N-GD-2 listed only
    the premises the packet cites. ACCEPTED as a useful addition for the landing note.
  - GD-N2 (F1°_D step 4: name the switched successor x*, not an arbitrary gate target z): ACCEPTED. My §2 already read the step that way
    ("a switched edge (x, z) from F_D: z ∈ F_D (closure at k + 1)"), so it is the same reading; the fixes line makes the text say it.
  - GD-N3 (DATA: Wo_D's conclusion also held at 66 transitions where (h_D) failed): ACCEPTED as data; my checker evaluated Wo_D only under
    its hypothesis, so I have no count there. Not a gap: the proof uses (h_D).
- C.2 Data: both own engines, different corpora; both 0 failures; both check G_D (c2) at every L ≥ M_D (REFEREE 1,984,737 + 37,476 level
  checks on lib41 (n ≤ 64) and 500 multi-Odd random games; mine 159,970 over lib41 (all 412), 503 𝒞^1O files, box-43 instances and 20,000
  random 𝒞^kO); the L = M_D − 1 mutation bites in both, at every state with M_D ≥ 0.
- C.3 Result: verdicts identical; nothing open. Fixes-file lines: GD-N1 = N-GD-1; GD-N2; premise-class note (N-GD-2 with REFEREE §1's two
  re-proved lemmas).
