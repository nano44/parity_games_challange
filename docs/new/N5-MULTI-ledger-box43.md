# N5 one-Odd ledger, full table (box 43 item 1; READING, unrefereed)
L-NEW successor 22, written 2026-10-25 ~22:25Z (date -u). Companion of docs/new/N5-MULTI-box43.md (§2 there is the summary and the
verdicts that matter). Label of every row: READING (a reading of the proof text, not a proof, not checked by a referee).
Provenance, stated plainly: the first pass over all 252 items was made by a read-only helper agent of this session on trunk eb273ebc;
L-NEW re-opened and confirmed the cited lines FBPOLY 100-102 (HP), RESULTS 802 (R18 (c)), 844 (Lemma G (b)), 2170 (P-FREEZE's G_U),
2342 (Φ-1O (a)) and KW42 115 (FO), and checked the verdicts of R15, R27 (d), R38 (a), R44 (a), R47 against the statements. Every
other row is the helper's reading as written; the "least sure" list at the end is the helper's own.
The 𝒞^1E column of the summary (MIRROR, docs/new/N5-MULTI-box43.md §1) is NOT in this table: every row here is about games with
several Odd choice vertices AND several Even choice vertices (the frontier); on 𝒞^1E all per-phase items transfer by Theorem MIRROR.
"<packet> nnn". Packet abbreviations: FBP = docs/new/P-N5-FBPOLY-box41.md; FX = docs/si/P-N5-FX-box14.md; KW15 = docs/si/N5-KW-box15.md;
KW42 = docs/new/N5-KW-box42.md; NH42 = docs/new/P-N5-NH-box42.md. Underlying signed packets opened to locate one-Odd uses:
Xp = docs/new/P-N5-X-box28.md; NH30 = docs/new/P-N5-NH-box30.md; FBp = docs/si/P-N5-FB-box7.md; CLSp = docs/si/P-N5-CLS-box8.md;
LPp = docs/new/P-N5-LP-box32.md; OEp = docs/new/P-N5-OE-box32.md; SOp = docs/new/P-N5-SO-box32.md; SNp = docs/new/P-N5-SN-box33.md;
SNf = docs/new/P-N5-SN-fixes-box33.md; L2p = docs/new/P-N5-L2-box34.md; TOGp = docs/new/P-N5-TOG-box35.md; U1p = docs/new/P-N5-U1-box31.md;
OUTp = docs/new/P-N5-OUT-box37.md; NEBp = docs/new/P-N5-NEB-box38.md.

## Verdict codes
- V   SURVIVES VERBATIM on general games (proof never uses one-Odd-choice).
- V1P one-player lemma: true verbatim for every one-player game, hence for G_τ (Odd fixed to τ) and G[X] of ANY game; it is not itself
      a statement about N5 on two-player games.
- I   SURVIVES WITH A PER-ODD-VERTEX INDEX (o → o_i; the use is local to one o_i).
- S   SURVIVES ONLY IN A SET FORM (my addition; neither V nor I): o or R must be replaced by a SET, e.g.
      D_k := {Odd u : σ̄_k(u) ≠ τ(u)} (the vertices where Odd's best reply disagrees with τ; it moves with σ even when τ is fixed),
      R_D := vertices whose (σ_k, τ)-play meets D_k, F_D := V ∖ R_D; or "all Odd choice vertices treated as terminals". Per-o_i fails
      because a vertex off R_i can still meet another o_j with σ̄ ≠ τ. Plausible from the proof text; NOT checked by anyone.
- F   FAILS as proved: the proof's own step uses globally that o is the only Odd choice vertex (key step quoted).
- FI  FAILS BY INHERITANCE: a premise is F (or FI); the item's own step may be fine.
- U   UNCLEAR from the text; what to check is named.

## The recurring one-Odd uses (named once, cited below)
- (HP) "honest play = (σ, τ)-play until the first visit of o": FBP 100-102 "(they use the same edge at every vertex other than o: σ_t
  at Even vertices, the forced edge at Odd vertices ≠ o)"; SNp 23 "On 𝒞^1O the H_k-graph and the (σ_k, τ)-graph agree everywhere
  except at o"; NH42 89 "Along π_v every Odd vertex is forced (o ∉ π_v), and σ̄ = τ off o". On general games they agree only until the
  first vertex of D_k, and D_k is not a fixed vertex.
- (RT) single route terminal: Lemma G (b) "under (h), on R, Ξ = π ⊕ θ and W = π ⊕ w" (RES 844-846). With several disagreement
  vertices the routes end at different terminals u with different pairs (Ξ(u), W(u)); the "same route order in both frames" step
  has no analogue.
- (FO) "Odd vertices other than o are forced, so their successor does not change" inside a proof step (e.g. FBp 173, OEp 30,
  TOGp 84, SNf 46, FBP 130/144/165/200, KW15 81-82, KW42 115/190, L2p 70/77).
- (TD) τ determined by τ(o): ≤ deg(o) Odd strategies (RES 2342-2343; R18 (c) RES 802). On general games the τ's form a ≺_{G^d}-chain
  of length up to h(≺_{G^d}) (R15 (c), (d)), not a product bound and not polynomial.
- (DO) counting by deg(o) / exits of o (d_o, REL, Y_t ⊆ succ(o)): on general games the analogue is per o_i but the θ_i are coupled.

## Ledger
| R / packet | item | setting (quote) | one-Odd use (quote + line) | verdict | premises |
| --- | --- | --- | --- | --- | --- |
| R15 | (a) Lemma A | RES 631 "for any non-empty unambiguous set I of improvements of σ" | none (VJ00 Lemma 5.7) | V | VJ00 5.7, Prop 5.4 cl. 2 |
| R15 | (b) Lemma B | RES 633 (same) | none | V | (a) |
| R15 | (c) Theorem (Ω, φ) | RES 636-639 "every non-empty switch of improvements goes strictly up in ≺" | none | V | (a), (b) |
| R15 | (d) N5 terminates; ≤ 4n(n−1) flat iterations | RES 640-643 "N5: every iteration applies Switch_I …" | none (G and G^d separately) | V | (a)-(c) |
| R16 | all | A_DTL | — | not N5, skip | — |
| R17 | (a) (V1)/(V2), (F1)/(F2) | RES 734 "H a one-player game (one player has out-degree 1 everywhere)" | none; it is a zero-choice class | V1P (used later as "(F1) in G_τ" on any game) | VJ00 §4-§5 |
| R17 | (b) Lemma P | RES 741 "in a λ-phase" of switch-best on one-player H | as a statement about N5 on two-player games it is FALSE: RES 756-757 "Lemma P's statement is FALSE for N5's Even moves inside a σ̄-segment (seg_r16, seg_n24)" | V1P (switch-best on G_τ only) | (a) |
| R17 | (c) Theorem PH | RES 743 | same as (b) | V1P | (b) |
| R17 | (d) Cor 1 | RES 745 "switch-best on one-player games" | none | V1P | (c) |
| R17 | (e) Cor 2: N5 < (n²−n+1)(n+m) | RES 747 "on a game in which one player has out-degree 1 everywhere" | needs Odd (or Even) choice-free; RES 757-758 "the count bound does not transfer (vc_g25 … 26 value-changing Even moves in one segment-phase at n = 25, one-player bound 24)" | F (for general games; true on one-player games) | (c), R15 |
| R17 | (f) Cor 3 (reading) | RES 750 | none | V1P (reading) | (c) |
| R17 | (g) §6 dependency list | RES 752 | none | V (meta) | — |
| R18 | (a) Proposition X | RES 785-786 "X := the vertices with no path to o (so G[X] has no Odd choice)"; RES 791 "any 𝒞^1O game" | X defined from o; uses that G[X] is one-player | S (X := vertices with no path to ANY Odd choice vertex; X is successor-closed and G[X] one-player; check that N5's S4a restricted to X is G[X]'s arena optimum). Likely vacuous on most general games. | R15 (d), R17 Cor 1 |
| R18 | (b) Cor X1 (reading, superseded) | RES 795 "on o-acyclic 𝒞^1O, θ = Ξ(o) and w = W(o)" | θ, w at the single o; o-acyclicity | F | (a), Lemma 2 |
| R18 | (c) Theorem (C_X + d)(B+1), conditional on (P) | RES 797 "on o-acyclic 𝒞^1O" | RES 802 "non-pure transitions number at most C_X + d − 1" (TD: τ has ≤ d values); RES 800 Lemma 2 θ = w then Lemma 3 Ξ = W (needs σ̄ ≠ τ only at o) | F | (a), R17 Cor 2, R36 (P) |
| R18 | (d) Lemma R (dual order reversed) | RES 803 | none | V | VJ00 |
| R18 | (d) Lemma S (a)-(b) | RES 804-805 "VJ00 (11) on G and on G^d" | none | V | VJ00 (11), R15 (a) |
| R18 | (d) Lemma S (c)-(d) | RES 805-807 "hold for S4a steps only" | none | V (S4a only) | SPEC S4a |
| R19 | (a) Lemma G (a) "off R, Ξ = W" | RES 840-842 "𝒞^1O … R := the vertices whose current play reaches o" | HP (σ̄ = τ off o) | S (true with R := R_D; false with R := R_i for one o_i) | — |
| R19 | (a) Lemma G (b)-(c) route form, "Iσ iff route-improving iff W-improving" | RES 844-846 "under (h), on R, Ξ = π ⊕ θ and W = π ⊕ w … the route order is the same" | RT + HP | F | (a) |
| R19 | (b) Lemma Wo | RES 847 "under (h) … τ(o) ∉ R, w = o ⊕ Ξ(τ(o)), and w_{k+1} ⊵ w_k" | W(τ(o)) = Ξ(τ(o)) needs τ(o) off the disagreement set (HP) | S (per o_i, but H2_i must be strengthened to τ(o_i) ∈ F_D) | G (a), R15 (a) |
| R19 | (c) Lemma RM | RES 848 "in a stretch with τ and θ constant and (h)" | route order = G (b) | FI | G (b) |
| R19 | (d) key step (SG) | RES 853-854 "a switched Even vertex y with λ_L(y) ≠ y gains strictly (on all games, not only 𝒞^1O)" | none | V | (V2), R15 |
| R19 | (d) Lemma RE | RES 850-853 "route_{E+1}(x) ▷ route_L(x) or θ_{E+1} ▷ θ_L" | routes to o, θ | U (statement is in RT terms; check P-N5-RE proof beyond (SG)) | (SG), G |
| R19 | (e) Corollary RE | RES 857 | as RE | U (inherits RE) | RE |
| R19 | (f) Lemma PIECE | RES 860-861 "the route game on R with o's frozen continuation as terminal and the o-free game on F" | RT; "o-free game on F" | F | G, R17 |
| R20 | (a) Lemma C | RES 888-889 "Setting as in R19 (𝒞^1O, θ, w, R, (h)) … u* := the most relevant vertex of P(θ) Δ P(w)" | COARSE(Ξ) = COARSE(W) everywhere needs one pair (θ, w): RT | F | G (b) |
| R20 | (b) FBL (u* ≠ none) | RES 892 | via C, routes | FI | C, G |
| R20 | (c) FBF | RES 896 "no vertex enters R" | via C | FI | C |
| R20 | (d) CR | RES 898 "R17's Lemma P / Theorem PH transcribed to the coarse order" | coarse order defined by u* of the single pair | FI | C, R17 |
| R20 | (e) Theorem XA | RES 901 | re-entry into R | FI | C, CR |
| R20 | (f) Corollary O(n³)/O(n⁵) | RES 903 | PIECE | FI | PIECE, CR, XA |
| R21 | (a) Lemma XW Ξ ⊴ W | RES 933 "(Odd's best reply σ̄_k is pointwise optimal in G_{σ_k})"; Xp 44-50 | none | V | VJ00 (11), R17 F1 on G^d |
| R21 | (b) Lemma EQ | RES 934 "(h) not assumed"; Xp 57-73 | none: at EQ states the gate is G_τ's improving set (Xp 61) | V | R17, R18 (c) flat case, R15 |
| R21 | (c) FBL-N (i) | RES 935; RES 1134 "takes FBL-N (i) directly from S4c + FIX 3, so it holds on every game (G-FB-2)" | none | V | SPEC S4c |
| R21 | (c) FBL-N (ii) | RES 936 "every gate edge from F is flat for W" | Xp 82 "x's (σ_k, τ)-play avoids o … (Lemma G (a))" | S (F := F_D) | G (a), XW, R18 (c) |
| R21 | (c) FBL-N (iii) | RES 936 "if H2 fails, no gate edge goes from F to R" | Xp 84 "z's W-play reaches o and then runs around o's W-cycle C … C ⊆ R_k" | U (needs (ii) in F_D form while R is R_i; check) | (ii) |
| R21 | (d) Lemma NF | RES 937 | Xp 105 "On 𝒞^1O, Odd chooses only at o, and σ̄ is pointwise optimal. So Ξ(v) = min over e of Ω_{σ, e}(v)" | F | FBL-N, G (c), EQ |
| R21 | (e) Lemma F1 | RES 938 | Xp 126 "a non-flat one would be a crossing (Lemma NF)"; Xp 116 "contains no vertex with an Odd choice (o ∉ F)" | FI (NF); superseded by F1° | NF, G (a), R17 |
| R21 | (f) Lemma F2 | RES 940 | Xp 52 XW1 "Under (h), Ξ_k ≠ W_k iff θ_k ≠ w_k" (RT), Xp 141 | F | XW, G, Wo |
| R21 | (g) Theorem X | RES 942 "inside one phase" | via F1, F2, NF, PIECE | FI | (b), (e), (f), NF, PIECE, R15 (d) |
| R21 | (h) Lemma FB-W | RES 946 | via R20 CR row | FI | R20 |
| R21 | (i) clarification of R19 (f) | RES 948 | θ-change at H1 | FI | PIECE |
| R22 | (a) Lemma F1° | RES 980-981 "Setting as in R21 (𝒞^1O …)"; RES 983 | NH30 37 "contains no vertex with an Odd choice (o ∉ F)", NH30 49 "forced Odd vertices have one successor"; the steps only need Ξ = W on F and 𝓕 ⊆ G_τ one-player | S (R := R_D, crossing := change of R_D; then every disagreement-set change is a "crossing"); check NH30 step 3 "no crossing ⇒ σ_{k+1} maps F into F" with R_D | G (a), FBL-N (ii), R17 |
| R22 | (b) Lemma TC | RES 985 "(i) H1 ⟺ λ_Ξ(o) ∈ F and H2 ⟺ τ(o) ∈ F" | NH30 60 "e* := σ̄(o) ∈ F: Odd chooses only at o" | F | G (a), F1° |
| R22 | (c) Lemma P3′ | RES 988 "(θ, w)-piece (both frames in route form …)" | RT (route game 𝓡*_w) | F | R20 (d) CR, G |
| R22 | (d) Corollary | RES 994 | via TC, F1°, R21 (i), R19 (b) | FI | TC, P3′ |
| R23 | (a) Step (K) | RES 1029 "at an S4c fallback inside a phase" | none (FBL-N (i): σ_k arena optimum in G_τ) | V | FBL-N (i) |
| R23 | (b) Lemma ACT | RES 1030 "at a transition with τ unchanged" | none beyond target o: pure (σ, τ)-reachability to {o} | I (target o_i; graph fact with τ fixed) | — |
| R23 | (c) LOOP + Cor | RES 1033 "inside a phase with H1 at k" | H1 (honest play from o) vs R ((σ,τ) reachability) | U (check P-N5-Z LOOP proof for HP) | ACT |
| R23 | (d) NOFE | RES 1035 "y on o's W-play" | from FBL-N (ii) (RES 1036) | U (needs FBL-N (ii) in F_D form) | FBL-N (ii) |
| R23 | (e) NOFL-E + Cor | RES 1037 "from a state with Ξ = W and H2" | — | U | EQ, FBL-N |
| R23 | (f) Lemma GAP | RES 1039 "with (h) at k … y ∈ R_k, z ∈ F_k: Ξ_k(σ_k y) ◁ Ξ_k(z) ⊴ W_k(σ_k y)" | Ξ(z) = W(z) for z ∈ F (G (a)) | S (needs z ∈ F_D; gate + Step (K) are generic) | G (a), (K), XW |
| R23 | (g) Lemma WM | RES 1041; RES 1134 "WM being transferred to every game by (F1) in G_τ (G-FB-3)" | none | V | R17 F1 |
| R23 | (h) Lemma LV′ | RES 1043 (signs of crossings) | none: sequence combinatorics on a set sequence | V (applies to R_i or R_D alike) | — |
| R23 | (i) Corollary Z | RES 1046 | via R21 (g) | FI | R21 (g), LV′ |
| R24 | (a) Lemma R | RES 1073 "in N5's S1 restriction step"; U1p 36-53 | none (engine statement about one arena) | V | VJ00 §6 |
| R24 | (b) Lemma TB | RES 1078; U1p 56 "Statement (any game; …)" | none | V | Lemma R |
| R24 | (c) Lemma CASC | RES 1082 "W-flat run (… of a piece …)" | U1p 95 "Forced Odd vertices never switch, and τ(o) is fixed"; route levels \|π_v\| | F | TB, G |
| R24 | (d) Theorem U1 | RES 1085 "a U1 piece" | U1p 131 "Ξ = π ⊕ θ and W = π ⊕ w with θ, w constant, and forced vertices never move" | F | CASC, P3′ repair |
| R24 | (e) Lemma WC | RES 1088 "on a crossing-free interval with ¬H2" | w on o's W-cycle, R constant | U (check P-N5-U1 §5) | R15 (a), EQ |
| R25 | (a) (T), COARSE-SI (a) | RES 1120 "on any game unless marked 𝒞^1O"; RES 1145 "hold on every game" | none | V | VJ00 Lemma 5.2, ENG-1 |
| R25 | (b) COARSE-SI (b), TAME | RES 1129 "every Odd switch of σ̄ at level ≤ M_k" | none (hypothesis is over all Odd switches) | V | (a) |
| R25 | (c) MONO, NOINF | RES 1130 | none | V | (b) |
| R25 | (d) Theorem FB + W-lowering Corollary | RES 1132-1135; RES 1145 | none | V | (b), (c), FBL-N (i), WM |
| R25 | (d) carries (C) clause | RES 1135 "on 𝒞^1O so are the carries (C)" | carries are '+−' reversals of R | U (statement per R_i makes sense; check FBp Corollary 166-168) | FB, R23 |
| R25 | (e) J1 | RES 1137 "a non-tame transition switches σ̄(o) at a level above M_k" | FBp 173 "every Odd u ≠ o has one successor, so σ̄_{k+1}(u) = σ̄_k(u)" (FO) | I (existential: a non-tame transition switches σ̄ at SOME o_i above M_k, by TAME's contrapositive) | TAME |
| R25 | (e) OFF | RES 1137 "a vertex leaving R̄ keeps its COARSE_{M_k} value" | FBp 176-178 "v's H_{k+1}-play avoids o … Odd vertices other than o are forced" | S (R̄ := honest reachability of the set of Odd vertices that switch above M_k) | (T) |
| R25 | (e) CAP (+ CAP-1) | RES 1138-1141 | FBp 181-184 at o: minimality of σ̄(o) + OFF | I (per o_i whose σ̄ switched above M_k; given OFF in S form) | J1, OFF |
| R25 | (f) Lemma A (proved part) | RES 1142 "On 𝒞^1O … at tame carries, L ≤ M_k" | carries of R | U | FB |
| R26 | (a) CASC-U2 | RES 1168-1172 "𝒞^1O; … U2: ¬H1 and c_θ := λ_Ξ(o) ≠ o" | RES 1175 "honest values on R are route functions with constant terminals θ and Ξ(c_θ)" (RT/HP) | F | R24 CASC, TB |
| R26 | (b) Corollary | RES 1177 | via (a) | FI | (a) |
| R26 | (c) CASC-U3 | RES 1179 "under ¬H2, o lies on its W-cycle o → A1 → c_w → A2 → o" | kinds via o's W-cycle; routes | F | R24 CASC, TB |
| R26 | (d) Corollary | RES 1188 | via (c) | FI | (c) |
| R27 | (a) Lemma U | RES 1224 "on any game unless marked 𝒞^1O"; RES 1270 | none | V | R25 TAME |
| R27 | (b) Lemma HI (+ Consequence, HI-1) | RES 1235 | none | V | U |
| R27 | (c) UL, GR, NU | RES 1238-1240 | none | V | U |
| R27 | (d) Theorem LP | RES 1241 "(any game)" | none | V | (a)-(c) |
| R27 | (e) Lemma DF′ | RES 1244 "On 𝒞^1O … then σ_{k+1}(y) ∈ R_{k+1}"; LPp 128-134 | LPp 133 "If a ∈ F_{k+1}: Ξ_{k+1}(a) = W_{k+1}(a) (R19 (a))" | S (conclusion σ_{k+1}(y) ∈ R_D; rest is (F1)/XW) | R17 F1, G (a), XW |
| R27 | (e) Lemma BAND | RES 1246 "both frames in route form" | LPp 138-143 route form, "c_w ∈ F ∪ {o} and routes stop before o" | F | G (b) |
| R27 | (e) Lemma WAKE | RES 1247 "a wake y: a → z has a, z ∈ R; … U1 piece" | via DF′ and route form | U (first half S via DF′; second half F) | DF′ |
| R27 | (f) Corollary LP′ | RES 1249-1251 "Via ε ≤ S_o, ρ ≤ 2f + S_o + 2X + K, J ≤ S_o by R25 J1" | S_o counts σ̄(o) only | U (J, ε re-index as Σ_i S_{o_i}; the ρ ≤ 2f + S_o + 2X + K step is in R/wake terms; check P-N5-LP §4) | LP, J1, FB |
| R27 | (g) Lemma TH | RES 1252 "per phase with λ_Ξ(o) ≠ o: Θ ≤ (n − 1) + n(X + 1) + X" | ¬H1 θ = (c_θ, ∅, d); H1 CAP-1 + F1°'s F-change at the exit | U (per o_i plausible only if F1° holds in S form and the exit lies in F_D) | CAP-1, F1°, R26 R-1 |
| R27 | (g) Lemma SO | RES 1255 "S_o ≤ Θ + (d_o − 1)(Θ + 1)" | SOp 39-40 "Every vertex on that path other than o has one successor in the graph G_σ … (Even: σ; Odd: forced)" (FO) | U (minimiser-set argument at o is local; the frozen-key step uses FO) | TB, Lemma R, (SG), R19 (d) |
| R27 | (h) Corollary XJ | RES 1258 | via TH, SO | U (inherits TH, SO, both U) | TH, SO, J1, FB |
| R28 | (a) Lemma U-loc | RES 1303 "(any game, inside a phase)" | none | V | U |
| R28 | (b) Lemma OE | RES 1305 "(𝒞^1O)"; RES 1300 "on 𝒞^1O, L_k = max(E_k, O_k)" | OEp 30 "the only possible relevant changes on that path are Even ones, of level ≤ E_k (Odd vertices on it are forced)"; OEp 14 | F | U-loc, CAP-1, TC (i) |
| R28 | (c) Corollary OX | RES 1312 | via OE | FI | OE, LP, FB, J1 |
| R29 | (a) (C5)-(C7) | RES 1348 | none (valuation algebra) | V | — |
| R29 | (a) Fact R | RES 1349 "r is non-increasing along a scope run" | r = lev(Ξ(o), W(o)); only XW + monotonicity at one vertex | I (any vertex v on a run with W(v) constant) | XW, R15 (a), (C5) |
| R29 | (a) Lemma CLU | RES 1349-1350 "re-proved from R23 (f)" | (h), routes | U (GAP is S; level ≤ r needs RT) | GAP |
| R29 | (b) Lemma TRANSFER | RES 1351 "(every game)" | none | V | — |
| R29 | (c) Lemma OFFGATE | RES 1353 "(𝒞^1O)"; RES 1355 "R̄ is R25 OFF's honest reachability, equal to the (σ, τ) one on 𝒞^1O: N-CLS-1" | N-CLS-1 is the one-Odd use | S (with OFF's honest-reachability R̄ of the switching Odd set) | OFF, TRANSFER |
| R29 | (d) Lemma CN | RES 1356 "(every game, inside a phase)" | none | V | — |
| R29 | (e) Lemma NL | RES 1358 "(𝒞^1O) … with (h) at j" | CLSp 98 "Lemma G (b) at j: Ξ_j(q) = π_q ⊕ θ_j"; CLSp 105 "The play avoids o (𝒞^1O), so every Odd vertex on it is forced" | F | G, WM, U |
| R29 | (f) Theorem CLS1 + Cor | RES 1360-1365 | uses R20 FBL (u* ≠ none) | FI | FBL, NL, Fact R |
| R30 | (a) Lemma OR | RES 1394-1397 "x0 := σ̄_k(o)"; RES 1399 | SNp 44 "On 𝒞^1O the relevant changes on that path are Even ones, of level ≤ E_k" | F | U-loc, CAP-1, OE |
| R30 | (b) Lemma TC-SPLIT | RES 1401 | SNp 58 "U-loc on x1's H_{k+1}-path (avoids o; only Even relevant changes)" | F | OR, U-loc |
| R30 | (c) R-STICK, 1st sentence | RES 1403 "every v ∈ R_s whose W-cycle node differs from λ(v) stays in R_{s+1}" | SNp 66-67 uses only "Off R, Ξ = W", WM, XW | S (true with R := R_D) | G (a), WM, XW |
| R30 | (c) R-STICK "hence if c_w(s) ≠ c_θ, R_s ⊆ R_{s+1}" | RES 1404 | SNp 62-63 "For v ∈ R_k: λ(v) = c_θ and the W-cycle node of v is c_w(k) (… the H_k-play agrees with it up to o …)" (HP) | F | 1st sentence |
| R30 | (c) Corollary SN-PREFIX | RES 1404-1407 | via the "hence" clause | FI | R-STICK hence, WM, XW |
| R30 | (d) Lemma H3H2 | RES 1408 | SNp 77 "its vertices' (σ, τ)-plays (equal to their honest plays, which avoid o)" (HP) | F | — |
| R30 | (e) Lemma LEAVE | RES 1409 | SNp 85 "R19 (a) under (h): Ξ_s(q) = π_q ⊕ θ_s, W_s(q) = π_q ⊕ w_s" (RT) | F | R-STICK, H3H2, G (b), U-loc |
| R30 | (f) Lemma H1-DROP | RES 1411 | SNf 46 "q_t is Even (every Odd vertex but o is forced)" | F | R15 (d), (C5) |
| R30 | (f) H1-KEEP, ABS-COUNT′ | RES 1412-1417 | SNf 57 "its relevant changes are Even ones"; d_o exits (DO) | FI | H1-DROP, OR |
| R30 | (g) Lemma WK | RES 1418 "a wake y: a → z (R27 (e))" | SNp 104 "By P-N5-LP Lemma WAKE's proof …" | U (G_τ choice-rule argument; inherits WAKE) | WAKE, Lemma R, TB |
| R30 | (h) Lemma ABS-L | RES 1421 "(premises R29 (e) NL and (f) CLS1's proof)" | absorptions at o | FI | NL, CLS1 |
| R31 | (a) Premise P-OPT | RES 1461 | none | V | SPEC S4a/S4c |
| R31 | (b) Lemma FBW | RES 1463 "(every game)"; RES 1482 | none | V | P-OPT, XW |
| R31 | (c) FBW-S, CLS2 | RES 1465 "(𝒞^1O) … with (h) at k, every gate has level ≤ max(r_k, −1)" | δ ≤ r_k needs lev(Ξ v, W v) ≤ r for all v (RT; cf. L2p 81-82) | F (FBW-S); CLS2 FI | FBW, G |
| R31 | (d) FLAT-ALL | RES 1468 "every v ∈ R̄_{k+1} lies in R̄_k with the same route to o" | routes, H1 at k+1 | FI | FBW-S, FBL, OFF, NL |
| R31 | (e) Lemma STRETCH | RES 1472 "(𝒞^1O)" | — (statement is about tails, not o) | U (check P-N5-FBW STRETCH for G/route use) | FBW, S4c |
| R31 | (f) Theorem PL, PL-S | RES 1475-1479 "(b) … an absorption; (c) D_M ≤ (d_o − 1) + REL_M" | OR (F), DO | FI | OR, STRETCH, FLAT-ALL |
| R32 | (a) NL-MF | RES 1513 | via NL | FI | NL |
| R32 | (b) Fact 0 | RES 1516 "λ(v) = c_θ ∈ F for v ∈ R̄" | HP | F | G |
| R32 | (b) Lemma ARENA | RES 1516-1518 | via Fact 0, RT | FI | Fact 0, G |
| R32 | (c) Lemma P^c_ℓ | RES 1519 "(R20's Lemma P^c with COARSE_ℓ, statewise Lemma C_ℓ …)" | Lemma C (RT) | FI | R20 C, CR |
| R32 | (d) FREEZE, RATCHET, BLOCK | RES 1523-1528 "COARSE_{ℓ−1}(θ) takes ≤ 2d_o values" | DO; P^c_ℓ | FI | P^c_ℓ, Fact 0 |
| R32 | (e) Theorem X-RUN | RES 1529 "≤ 13(d_o + 1)n³" | via FREEZE, ABS-COUNT′ | FI | FREEZE, R30 |
| R32 | (f) Theorem SUB | RES 1533 "R20's Lemma C, Lemma CR and Theorem XA hold with COARSE_ρ" | via R20 | FI | R20 |
| R33 | (a) Lemma H3-CONST | RES 1570 "at every H2 state c_w = λ(τ(o))" | L2p 45-46 "On F, W = Ξ (R19 (a))" at τ(o) | S (H2 must mean τ(o_i) ∈ F_D) | G (a) |
| R33 | (b) Lemma H2-STICK | RES 1572 | L2p 55 "its honest play agrees with its (σ_s, τ)-play up to o" (HP) | F | R-STICK, H3H2 |
| R33 | (c) Lemma G′ | RES 1574 | L2p 70 "(Odd vertices other than o are forced)"; L2p 77 "passes only forced Odd vertices" | F | — |
| R33 | (d) Theorem FREEZE′ | RES 1576 "(premise RESULTS R32 FREEZE …)" | via FREEZE, G′ | FI | R32, G′ |
| R33 | (e) Lemma R-CONST | RES 1578 "at every ¬H1 state of a phase, R̄ = U" | L2p 114, 119 "Up to that first visit it equals the (σ_k, τ)-play" (HP) | F | — |
| R33 | (f) H1-INT (a), (c) + ¬H1 part of (b) | RES 1579-1582 "the states with P(θ) = ∅ form one interval" | none: L2p 127-134 use only R15 (a), fixed cycle node, injective weight | I (holds for Ξ(v) at every vertex v whose cycle node is constant) | R15 (a) |
| R33 | (f) H1-INT (b), drop states | RES 1580 | L2p 131-132 "use R30 (f) H1-DROP" | FI | H1-DROP |
| R33 | (g) Theorem X-RUN′ | RES 1583 "(premise RESULTS R32 X-RUN …)" | via X-RUN | FI | R32 (e) |
| R34 | (a) Fact (F) | RES 1625 | none (VJ00 path values) | V | (V1) |
| R34 | (b) Lemma L-MONO | RES 1627 "for c = λ(o) ≠ o in a phase" | TOGp 45 "(this includes every Odd c, which has one successor)" | U (V when c is Even or forced; for an Odd-choice c the case split fails) | (F), R15 (a) |
| R34 | (c) Lemma Z-COUNT | RES 1629 | none: TOGp 60-63 per v ∈ U, monotone weight, injective | V (for any cycle-node class U) | R15 (a) |
| R34 | (d) Theorem TOGGLE | RES 1630 "so c ∈ V_E and σ(c) changes" | TOGp 84 "Odd vertices other than o have one successor and c ≠ o, so c ∈ V_E" (FO) | F | Z-COUNT, (F) |
| R34 | (e) TOGGLE-COUNT | RES 1632 "≤ T := \|U\|(n + 1) + n − 1" | via TOGGLE, L-MONO | FI | TOGGLE, L-MONO |
| R34 | (f) X-SN-PHASE | RES 1633 "(premise RESULTS R33 X-RUN′, hence R32)" | — | FI | R33 (g), TOGGLE-COUNT |
| R34 | (g) RESTARTS | RES 1637 "(premises … H2-STICK, H3-CONST and … H3H2)" | — | FI | H2-STICK, H3H2 |
| R35 | (a) RDROP, PL (c′), PL-S′ | RES 1666-1673 "(d_o − 1) + REL_M" | DO; R31 PL (b) absorption | FI | R31 PL, OR |
| R35 | (b) MINSET (a) | RES 1674 "COARSE_M(θ_t) is the minimum … over the exits x ∈ F_t, attained at σ̄_t(o)" | "x ∈ F_t" is HP-based | I (plausible with F_t replaced by "honest play avoids o_i", as for Y-FORM below) | CAP-1, G |
| R35 | (b) MINSET (b), (d), survivor (c) | RES 1675-1679 "members leave Mn only by entering R" | R vs F at o | U | MINSET (a), FREEZE/FLAT-ALL |
| R35 | (c) NO-RF-OLD + Cor | RES 1680 | scope-run machinery (NL, routes) | FI | NL, FLAT-ALL |
| R35 | (d) ENT-SHAPE (1)-(4), (5′) | RES 1684 | as (c), U-loc | FI | (c), U-loc |
| R36 | (a) Lemma B | RES 1726 | none | V | SPEC S1 |
| R36 | (b) Lemma M | RES 1729 | none | V | B |
| R36 | (c) Lemma P1 + P1′ | RES 1723-1724 "A ONE-PLAYER game is a game in which every non-Even vertex has one successor" | none | V1P | B, M |
| R36 | (d) hypothesis match | RES 1734-1736 "G[X], G_τ and G_τ[F_k]" | F_k is o's | V (for G[X], G_τ); G_τ[F_k] as a closed subgame needs only closedness | P1 |
| R37 | (a) R-SAME, BL-FORM | RES 1768 "the order of π ⊕ a against π′ ⊕ a … is the same for a ∈ {θ, w}" | RT | F | G (b) |
| R37 | (b) Lemma BL (a)-(e) | RES 1770 "at an in-phase THR S4c fallback k with (h) (x0 := σ̄_k(o))" | via BL-FORM; x0 at o | FI | BL-FORM, (P) |
| R37 | (c) Lemma CONF-MONO | RES 1773 "for closed F′ ⊆ F, Opt(G_τ[F′]) ⊴ Opt(G_τ[F])" | none (one-player monotonicity) | V1P | — |
| R37 | (c) FREE-FREEZE | RES 1773-1775 | needs BL (c) W = Opt(G_τ[F_k]) and Ξ = W on F | U (S form with F_D plausible; BL (c) is FI) | BL (c), (P) |
| R37 | (d) EQ-END | RES 1776 "(CONDITIONAL on CN-LAST …)" | scope run, θ = w | FI | CN-LAST, CLS2 |
| R37 | (e) MERGE′ | RES 1778 "x0" | RT | FI | G (b) |
| R37 | (f) EV, EV+ | RES 1782 | ENT setting | FI | FREE-FREEZE, BL |
| R37 | (g) TEV-RED′ | RES 1785 | ENT setting | FI | EV |
| R38 | (a) Remark KEY | RES 1825 "(every game)" | none | V | — |
| R38 | (b) Lemma WCH | RES 1827 "(𝒞^1O) … w_k ≠ w_{k+1} … either it is a crossing or Ξ_k(t0) ≠ Ξ_{k+1}(t0) for t0 := τ(o)" | w = o ⊕ Ξ(t0) via G (a) | S (needs t0 ∈ F_D); the count uses F1° (S) | G (a), F1° |
| R38 | (c) SCOPE-COUNT | RES 1830 "(premise RESULTS R34 (g) RESTARTS)" | — | FI | RESTARTS, WCH |
| R38 | (d) Lemma FB-INT | RES 1832-1833 "(every non-tame transition of a phase is a crossing: the proof of RESULTS R28 (c) (ii))" | via OE | FI | OE, R25 FB |
| R38 | (e) Corollary NH1-FB | RES 1834 "(premises R33 (e) R-CONST and R34 (e) TOGGLE-COUNT)" | — | FI | R-CONST, TOGGLE-COUNT |
| R38 | (f) Lemma CN-LAST | RES 1836 "(every game)" | none | V | — |
| R39 | (a) Lemma SPLIT | RES 1867-1871 "HN STATE has H1 ∧ ¬H2"; RES 1873 | OUTp 95 deps "R-STICK, H3H2's proof, ACT (i), FBL-N (iii)" | FI (H3H2 F, R-STICK hence F) | as listed |
| R39 | (b) Corollary EPOCH | RES 1875 "(premise FB-INT)" | — | FI | SPLIT, FB-INT |
| R39 | (c) Lemma F-FLAT | RES 1878 | OUTp 97 deps "FBL-N (ii)-(iii), G (a), (F), (V1), S (a), R15 (a)" | U (S form plausible; FBL-N (iii) U) | as listed |
| R39 | (d) FREEZE-STEP, TAIL | RES 1880 | OUTp 98 deps include SPLIT | FI | SPLIT |
| R39 | (e) NO-ENTRY-A | RES 1883 "(τ(o) = o, case A)" | OUTp 99 deps "XW, FBL-N (iii), (K), ACT (i), (V1), R15 (a), (d)" | U (deps are V/I/U; the HN setting itself uses TC (i)) | as listed |
| R39 | (f) NE-COUNT | RES 1887 | uses TOGGLE-COUNT | FI | NO-ENTRY-A, SPLIT, EPOCH, TOGGLE-COUNT |
| R39 | (g) CASE-B-LEN, W-SIDE | RES 1890 "(τ(o) = o, case B)" | OUTp 101 deps "XW, (K), (V1), KEY" | U (deps are all V; check the proof for HP in "R → R̄ gate" geometry) | XW, (K) |
| R40 | (a) Facts (Σ1)-(Σ6) | RES 1933-1940 "(from landed results)" | from CLS2, NL, (h) | FI | CLS2, NL |
| R40 | (b) FZ, BF | RES 1941 | (Σ) | FI | (a) |
| R40 | (c) RB, WALK | RES 1943 | routes | FI | (a), (b) |
| R40 | (d) CYC-EV | RES 1946 | (Σ) | FI | (a) |
| R40 | (e) TEV-FB | RES 1949 "x_k := σ̄_k(o)" | (Σ) | FI | (a) |
| R40 | (f) ENT-X, NJB-A, D1, PL-S″ | RES 1951 | via R37 EV+ | FI | R37 (f), (e) |
| R41 | (a) LV-SHAPE | RES 1993-1996 "SETTING (LV): k is an in-scope S4c fallback, THR at k" | (h), routes, x0 | FI | FBW-S, CLS2, routes |
| R41 | (b) LV-CN, LV-COUNT | RES 2001 | via LV-SHAPE (CN-LAST itself is V) | FI | LV-SHAPE, CN-LAST |
| R41 | (c) FLAT-ALL_{−1} | RES 2005 | as R31 (d) | FI | R31 (d) |
| R41 | (d) STRETCH_{−1} | RES 2007 | as R31 (e) | U | R31 (e) |
| R41 | (e) PL_{−1}, LV-PL | RES 2011 "D_{−1} ≤ (d_o − 1) + REL_{−1}"; absorption | DO, OR | FI | OR, (c), (d) |
| R42 | (a) Lemma RISE | RES 2054 "(S an HN stretch)" | NEBp 14 uses "SPLIT (a), F-FLAT" | FI (SPLIT) | SPLIT, F-FLAT |
| R42 | (b) Lemma HIGH-RISE | RES 2057 "(case A …)" | NEBp 15 "SEP-o" | U (check SEP-o in NEBp §0) | RISE |
| R42 | (c) Theorem NO-ENTRY-A′ | RES 2058 "(case A, c_w(a) = o, any τ(o))" | NEBp 16 "FBL-N target-o step" | U | FBL-N |
| R42 | (d) Lemma CASE-B-LEN′ | RES 2064 | NEBp 17 "none beyond §0" | U | §0 |
| R42 | (e) Lemma LOW-RISE′ | RES 2066 | NEBp 18 "SPLIT (a)" | FI | SPLIT |
| R42 | (f) Theorem BRK | RES 2070 | NEBp 19 "SPLIT, F-FLAT"; RES 2074 "by SPLIT (a)" | FI | SPLIT, RISE, (c)-(e) |
| R42 | (g) Corollary OUT-1 | RES 2076 "(τ(o) = o, cases A and B)" | — | FI | EPOCH, NE-COUNT, TOGGLE-COUNT |
| R43 | (a) STALE-GATE | RES 2117 "(every game)"; RES 2115 "(a) holds on every game" | none | V | — |
| R43 | (b) Corollary EV-G | RES 2119 | via FREE-FREEZE | U (inherits FREE-FREEZE) | R37 (c), R36 |
| R43 | (c) ENT-X_{−1} | RES 2121 | cites CYC-EV, R41 | FI | R40 (d), R41 |
| R43 | (d) LV-PL′ | RES 2124 | — | FI | (c), R41 |
| R43 | (e) Lemma SAND | RES 2125 "if t ≤ t′ … with r_t = −1, then COARSE_{−1}(θ_{t′}) = COARSE_{−1}(θ_t)" | only θ ↑, w constant, θ ⊴ w at one vertex | I (like Fact R; check proof) | XW, R15 (a), Fact R |
| R43 | (f) FLAT-ALL_{−1}^{none} | RES 2126 | as R31 (d) | FI | R31 (d) |
| R43 | (g) LV-NONE | RES 2128 | — | FI | (e), (f), R41 |
| R43 | (h) SCOPE-FB | RES 2129 | sum of R40 (f), (d), (g), R37 (d) | FI | as listed |
| R44 | (a) Lemma FB-ROUND | RES 2174 "for every Even v ∈ U ∖ {c_θ} and every successor x ∈ U of v"; FBP 113-120 (κ form) | none: (Aκ) FBP 89-92, (M1κ), (M2κ), S4c best target | V (for every cycle-node class U = λ⁻¹(c), not only c = c_θ) | (V1), R15 (a), S4c |
| R44 | (b) Theorem P-FREEZE | RES 2170-2171 "G_U … every Odd v ∈ U ∖ {o, c_θ} keeps its forced edge, and o and c_θ are sinks"; "on a θ-run" | FO in the graph G_U; single terminal o with constant θ | F (an S form with ALL Odd choice vertices of U as sinks and "run" = all their values constant looks provable, but then the number of such runs is the open count) | FB-ROUND |
| R44 | (c) LEN-TAIL, NO-CROSS-A | RES 2179-2180 | via P-FREEZE; case A, H1 | FI | P-FREEZE |
| R44 | (d) Lemma RISE′ | RES 2181 "(a re-proof of P-N5-NEB's RISE from landed results)" | HN stretch, R̄-rise | U (which landed results: check P-N5-PFZ §4) | — |
| R44 | (e) Theorem BRK-POLY | RES 2184 | — | FI | P-FREEZE, RISE′ |
| R44 | (f) P-FREEZE′, θ-LEN | RES 2186 | as (b) | FI | (b) |
| R44 | (g) Theorem BRK-POLY′ | RES 2189 | — | FI | (e), (f) |
| R45 | (a) Lemma Y-FORM | RES 2234 "at an H1 state t, σ̄_t(o) ∈ Y_t and M_t(o) = wt(o) + min_{y ∈ Y_t} M_t(y)"; Y_t := succ(o) ∩ U ∩ F_t (RES 2231) | FBP 152 "by (HP) (i) σ̄_t(o) ∈ F_t"; FBP 154 "let τ′ be Odd's strategy with τ′(o) = y (every other Odd vertex is forced)" | I (repair: Y_t := successors of o_i in U whose HONEST play avoids o_i, τ′ := σ̄_t except τ′(o_i) = y; Lemma S (a) then gives the same min form. Not verbatim.) | Lemma S (a), G (a), (Aκ) |
| R45 | (a) Y-FORM "at a ¬H1 state, P(θ_t) = ∅" | RES 2234 | none: FBP 107-110 (YB) | V (per vertex on its own honest cycle) | (V1) |
| R45 | (b) Lemma HAT-FREEZE | RES 2228-2230 "G_Û … every Odd v ∈ Û ∖ {c_θ} keeps its forced edge"; RES 2237 "No assumption on θ, H1, H2, τ(o) or c_w" | FBP 130 "z Odd: x is z's forced successor, so x = next_t(z)"; FBP 134 "z's honest play avoids o ((HP) …)" | F | FB-ROUND, (Aκ), (SP′) |
| R45 | (c) Theorem RHO-TAIL | RES 2239 "at most deg(o) transitions … change P(θ)" | HAT-FREEZE + DO | FI | HAT-FREEZE, Y-FORM |
| R45 | (d) Lemma BF-F | RES 2240 "with H1 ∧ ¬H2 at k and k+1 … v ∈ U ∩ F_{k+1}" | F_{k+1} of o | U (check P-N5-RHO §4 for FO/HP) | (Aκ) |
| R45 | (e) Theorem FREEZE-F | RES 2242-2245 "G[F_t ∩ U]" (defined RES 2231 with forced Odd edges) | FO in G[A]; deg(o) | F | BF-F |
| R45 | (f) Theorem RHO-HN | RES 2246 | — | FI | HAT-FREEZE, FREEZE-F |
| R45 | (g) Corollary HN-POLY | RES 2248 | — | FI | R44 (g), (f) |
| R46 | (a) T0U (a) "¬H2 iff t0 ∈ R_t" | RES 2280 | definitional per o | I | — |
| R46 | (a) T0U (b) "t0 ∈ U ∖ {o, c_θ}" | RES 2281 | t0 ∈ R ⇒ λ(t0) = c_θ (HP) | F | HP |
| R46 | (b) Lemma EV2-FB | RES 2282 "(SPLIT (a), RESULTS R39 (a))" | — | FI | SPLIT |
| R46 | (c) Lemma SG-EV | RES 2284 | — | U (S4a case is WM + XW + G (a), i.e. S; the fallback case unread) | WM, XW, G (a) |
| R46 | (d) Lemma T0-PIN | RES 2286 "(HAT-FREEZE (b), (c))" | — | FI | HAT-FREEZE |
| R46 | (e) Theorem NHN-BOUND | RES 2288 | — | FI | T0-PIN, TOGGLE-COUNT |
| R46 | (f) Remark H3-IN-HN | RES 2292 | via H3-CONST, T0U (b) | FI | H3-CONST, T0U (b) |
| R46 | (g) HN-POLY-ALL | RES 2295-2300 | — | FI | R44, R45, (e) |
| R47 | (a) Lemma Φ (a)-(c) | RES 2336 "(every game)" | none | V | R15 (a), (d), R18 (d) Lemma S (b), Lemma R |
| R47 | (b) Cor Φ-1O (a) τ changes ≤ d − 1 | RES 2342-2343 "(the τ's form a strict ≺_{G^d}-chain … so no τ repeats)" | TD: ≤ d distinct τ because τ is fixed by τ(o) | F (general: only "no τ repeats", chain length h(≺_{G^d}), exponential in general) | R15 (c), (d) on G^d |
| R47 | (b) Cor Φ-1O (b) phases ≤ n(n−1) + d | RES 2343 | via (a) | FI | (a), Φ |
| FBP | §0.3 (Aκ), (A0κ), (M1κ), (M2κ), (INJ), (SP′) | FBP 89-106 | none | V (any cycle-node class) | (V1), R15 (a) |
| FBP | §0.3 (HP) | FBP 100-102 "On 𝒞^1O the honest play and the (σ_t, τ)-play … agree until their first visit of o" | IS the one-Odd fact | F | — |
| FBP | §0.3 (YB) | FBP 107-110 | none | V (per vertex) | (SP′) |
| FBP | §1 κ-FB-ROUND | FBP 113-120 | none | V | (Aκ), (M1κ), (M2κ), S4c |
| FBP | §1 κ-HAT-FREEZE (a)-(c) | FBP 122-137; G_Û FBP 52-53 "every Odd v ∈ Û ∖ {c_θ} keeps its forced edge" | FBP 130 (FO), FBP 134 (HP) | F | κ-FB-ROUND, (HP), (SP′) |
| FBP | §1 κ-PFZ | FBP 139-146 "o ≠ c_θ … θ-run" | FBP 144 "z Odd (z ≠ o): x = next_t(z) (forced)"; o sole terminal | F | κ-FB-ROUND |
| FBP | §1 κ-Y-FORM | FBP 148-157 | FBP 152 (HP), FBP 154 "(every other Odd vertex is forced)" | I (same repair as R45 (a)) | Lemma S (a), G (a), (HP) |
| FBP | §2 EXIT-SWITCH | FBP 159-176 | FBP 165 "Odd w ≠ o: the forced edge" (next_{k+1}(w) = next_k(w) for unswitched w) | F (an S form with all Odd choice vertices of U in T may survive; unchecked) | (Aκ), (SP′), S4c |
| FBP | §3 FREEZE-EXIT | FBP 178-186 | via κ-HAT-FREEZE (a), κ-PFZ | FI | EXIT-SWITCH, κ-HAT-FREEZE, κ-PFZ |
| FBP | §4 CN-ONLY | FBP 188-213 | FBP 193 "(HP) (ii) … (HP) (i)"; FBP 198 "Every vertex of λ_k^{-1}(y) has an honest play avoiding o ((HP) (ii))"; FBP 200 "its Odd vertices are not o (o ∈ U), so they are forced" | F | FBL-N (ii), G (a), CN-LAST (V) |
| FBP | §5 THETA-AFTER | FBP 215-224 "κ_t(o) ∈ V_H … \|V_H\| ≤ deg_U(o)" | κ-HAT-FREEZE (c); DO | FI | κ-Y-FORM, κ-HAT-FREEZE (c) |
| FBP | §6 FB-POLY (a)-(d) | FBP 228-246 "f … of a phase of N5 on 𝒞^1O" | — | FI ((d) = CN-ONLY F) | §2-§5 |
| FX | §1 Corollary FX (a) | FX 30-42; FX 7 "SUBCLASS 𝒞^1O" | FX 39 "(iii) an S4a step with c_w(k) ≠ c_θ: by R-STICK, R_k ⊆ R_{k+1}" (the F "hence" clause) | FI | R30 (c) hence clause, X_SN def |
| FX | §1 Corollary FX (b) | FX 33 "(CONDITIONAL on FB-POLY.)" | — | FI | FB-POLY, R34 (f) |
| KW15 | §2 Lemma W-ONCE | KW15 55 "(PROVED, L-SI 10; any game)" | none: KW15 59-65 arena inclusion + (F1) in G_τ | V | R17 (F1), S4a |
| KW15 | §2 Corollary W-ONCE′ | KW15 66-68 | none (Lemma U is V) | V | W-ONCE, R27 (a) |
| KW15 | §3 Fact A | KW15 73-95 | KW15 81-82 "Every Odd vertex but o is forced, so v's honest play follows π_v" (also KW15 255-256, the lane's own flag) | F | G (b), R26 R-1 |
| KW15 | §3 Fact B | KW15 96-103 | via Fact A | FI | Fact A |
| KW15 | §3 Lemma FRZ-U | KW15 104-136 | Fact B; KW15 114 "a := x's unique successor = z for Odd x ≠ o" (FO) | F | Fact A/B, WM, (F1) |
| KW15 | §4 Corollary LEN | KW15 143-156 | via FRZ-U, Fact A | FI | FRZ-U |
| KW15 | §5 KIND-MONO, CASC-B, CW-INT, E-SEG | KW15 158-191 | via Fact A, R26; KW15 181 "c_w ∈ R is constant" | FI | Fact A, FRZ-U, R26 |
| KW15 | §6 Theorem RUN, §7, §8 Corollary PHASE | KW15 193-242 | — | FI | §2-§5, R27 TH/SO (U), F1° (S) |
| KW42 | §1 Lemma WLAG | KW42 18 "PROVED (every game)"; KW42 47-60 | none: (F1), WM, MONO | V | R17 (F1), R23 WM, R15 (a) |
| KW42 | §2 Lemma ABOVE-h | KW42 69-80; KW42 32 "all R-plays continue with o's play" | HP (via NH42 Lemma SW) | F | NH42 SW |
| KW42 | §2 Lemma CSTRICT | KW42 81-90 | via ABOVE-h | FI | ABOVE-h |
| KW42 | §3 Theorem KW-FREEZE (a)-(d) | KW42 92-148 | KW42 115 "Odd vertices of R ∖ {o} are forced" (FO); RT | F | R20 CR, CSTRICT, TB, WM |
| KW42 | §4 Corollary KW, Corollary NR′ | KW42 150-164 | — | FI | KW-FREEZE, F1° |
| KW42 | §5 Lemma PAR | KW42 177-181 | none: from XW at one vertex | V (for every vertex v: if λ_W(v) ≻ λ_Ξ(v) then λ_W(v) is even) | XW |
| KW42 | §5 Lemma H-PATH | KW42 185-193 | KW42 190 "(the honest play from c_θ is the cycle, and its Odd vertices other than o are forced)" | F | ABOVE-h |
| KW42 | §5 DIR, KC, CASC-B, CW, Theorem E-HI | KW42 194-254 | via ABOVE-h, H-PATH, NH42 SW | FI | as listed |
| NH42 | §1 Lemma SW | NH42 84-103 | NH42 89 "Along π_v every Odd vertex is forced (o ∉ π_v), and σ̄ = τ off o"; NH42 42 | F | TC (i) |
| NH42 | §2 Lemma ST | NH42 109-120 | via TC (F) | FI | TC |
| NH42 | §2 Lemma CL | NH42 122-145 | via TC, ST | FI | TC, ST |
| NH42 | §3 Lemma STR-COUNT | NH42 148-167 | (a) X-1 + SW step 3; (b) G (a) at τ(o) | FI | X-1, F1°, SW, WC |
| NH42 | §3 Lemma NR | NH42 168-188 | via P3′, U1, U2C, U3C | FI | R22 (c), R24 (d), R26 (b), (d) |
| NH42 | §4 Theorem NH (a)-(c) | NH42 190-219 | — | FI (its R15d step is V) | NR, STR-COUNT, THM-X, R15 (d) |

## Items I am LEAST sure about
1. Every S row (R18 (a), G (a), Wo, FBL-N (ii), F1°, GAP, OFF, DF′, OFFGATE, R-STICK 1st sentence, H3-CONST, WCH): the set form is my
   reading of the proof text; nobody has checked it. F1° in S form also makes every change of the disagreement set D_k a "crossing",
   which changes what X counts.
2. Y-FORM / κ-Y-FORM / MINSET (a) as I (per o_i with "honest play avoids o_i" in place of F): I checked the two-line argument
   (τ′ := σ̄ except at o_i, then Lemma S (a)) in my head only.
3. R34 (b) L-MONO: fine for Even c (TOGp 48-52); for an Odd-choice cycle node c the case split at TOGp 45 does not cover it.
4. J1 / CAP as I: J1's existential form follows from TAME; CAP per o_i needs OFF in S form.
5. R19 (d) RE and (e): statement is in route terms; I did not open P-N5-RE to see whether the proof uses RT beyond (SG).
6. R23 (c) LOOP, (d) NOFE, (e) NOFL-E, R24 (e) WC, R25 (d) carries, (f) Lemma A, R27 (f) LP′, (g) TH, SO, R31 (e) STRETCH,
   R39 (c), (e), (g), R42 (b)-(d), R44 (d), R45 (d), R46 (c), R35 (b) rest: packets not opened (or only their dependency tables);
   marked U.
7. R18 (a) S: needs a check that N5's Even step restricted to X is G[X]'s arena optimum when Odd's moves elsewhere change.
8. R36 (d) and R37 (c) CONF-MONO marked V/V1P: true as one-player facts; their USE in R37/R40 is on G_τ[F_k] with F_k of o.

## Counts (252 rows, R16 excluded; counted by awk on column 5)
- All: V 49, V1P 7, I 10, S 12, F 46, FI 97, U 31.
- RESULTS R15-R47 only: V 42, V1P 7, I 9, S 12, F 35, FI 80, U 31. Packets (FBP, FX, KW15, KW42, NH42): V 7, I 1, F 11, FI 17.
