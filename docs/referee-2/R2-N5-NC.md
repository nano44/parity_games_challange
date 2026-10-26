# R2-N5-NC: second-referee check of packet P-N5-NC (L-SI box 16: G_D-NC (b′), (c1′), (c2′); WM-G; P^c_L and CR-D; Corollary FRZ-U_D; every game). REFEREE-2 (successor 14), written 2026-10-26 05:3xZ-05:4xZ (date -u)
Signature: (Opus 5.5, D15). Lead's order 05:20Z (its stamp), queue item 2.
Object: docs/si/P-N5-NC-box16.md, `git show 8460897d:docs/si/P-N5-NC-box16.md | sha1sum` -> 2036e7c8a8c177ad842fc2e0dbc2899de2b8495f
(= the Lead's pin; = my tree), 189 lines (L-SI successor 11). No fixes file.
Background read (texts): RESULTS R55 (setting, (a)-(c)), R17 (a), R23 (g) and l. 1134; P-N5-GD (sha1 b898ff82 = R55's object) §0-§1 (the
proofs of G_D (b), (c1), (c2), l. 50-79); P-N5-FB-box7 §1 (lev, COARSE_L, (C1)-(C4)); SPEC S1, S2, S4a.
Independence: no docs/referee/ NC file (trunk and origin/claude/referee, name listing: none); none opened. The lane's
experiments/si/fb2o/gdnc.py not run or imported.
Tools (own code, docs/referee-2/R2-N5-NC/): nc_check.py (succ. 13's SPEC loop; W_k by si.Engine on G_τ; COARSE / lev from the definitions;
P^c_L by simple-path enumeration in G_τ), run_all.sh, logs/. Random start pairs throughout, as the Lead asked.
Labels: PROVED (L-SI 11; CR-D's statement L-SI 10), every game. Structural lemmas; no running-time bound; G-N5-TIME stays OPEN.

## Verdicts (Opus 5.5, D15)
| statement | verdict | notes |
| --- | --- | --- |
| §2 G_D-NC (b′) | SIGN | N-NC-2 (the one (h_D) use, replaced) |
| §2 G_D-NC (c1′), (c2′) | SIGN | N-NC-2 (R55's (c1), (c2) proofs use (h_D) only via G_D (b)) |
| §3 Lemma WM-G | SIGN | — |
| §3 Lemma P^c_L | SIGN | N-NC-3 (one unstated step in B1, supplied) |
| §3 Lemma CR-D | SIGN | — |
| §4 Corollary FRZ-U_D | SIGN | N-NC-4 (DATA: the freeze IS reached, with D ≠ ∅, but only under (h_D)) |
| §5, §6 | not signed (as briefed) | §6's "freeze vacuous in all data" is superseded by my data (N-NC-4) |
No gap. No (P). Notes N-NC-1..4. TARGET.md diff: no TARGET.md object claimed.

## 1. Quotes and premises
- Script (normalised substring search, split at "…"): R55 setting (both parts), R55 (a), (b), (c1)-(c2), R17 (F1), and R55's premise line
  "one-player statements, applied to G_τ, its arenas …, which are one-player on every game" occur verbatim in docs/RESULTS.md ✓; lev and
  COARSE_L verbatim in docs/si/P-N5-FB-box7.md ✓.
- N-NC-1 (wording): two quotes are not character-exact. (1) The quote of R55's proof of (b) joins three bullets of P-N5-GD l. 54-59 into
  one paragraph (content verbatim; bullet marks dropped). (2) The quote "(C1) … (C4) …" drops P-N5-FB-box7's parentheticals "(Definition.)"
  after (C2) and "(Σ ±2^rank is injective on sets)" after (C3) without an ellipsis. No content changes.
- R17 (a) (V1), (V2), (F1): one-player statements, game-general (R55's premise line) ✓. WM-G restates R23 (g) with its game-general proof ✓.

## 2. G_D-NC: SIGN
- (b′) ✓. N-NC-2: P-N5-GD's proof of G_D (b) (l. 53-59) uses (h_D) exactly once: "If u's honest play (resp. W-play) met x after leaving u,
  it would then follow x's play back to u ∈ D_k, against (h_D) at u." Under (NC) the same sentence closes: x ∈ π_v; x's honest play and
  W-play are the suffix of π_v from x, then u (HP_D: the Odd vertices of π_v are outside D_k, so σ̄_k = τ_k there); plays are positional;
  so u's play, after meeting x, returns to u, i.e. u lies on the cycle of its own play in that frame — what (NC) forbids, in each frame.
  The rest of the proof (both plays follow π_v to u; (V1) along π_v) uses no hypothesis ✓. (h_D) ⇒ (NC) ✓ (a vertex on its own cycle
  visits a D-vertex, itself, after leaving itself).
- (c1′), (c2′) ✓. P-N5-GD l. 65-75: (c1)'s proof uses (h_D) only via "A_v ∩ P(T) = ∅ (G_D (b): T's play avoids π_v)" and (h3_D) for the
  common cycle node; (c2)'s via "by G_D (b), Ξ_k(v) = π_v ⊕ Ξ_k(u) and W_k(v) = π_v ⊕ W_k(u)" and "both plays from u avoid π_v" ✓, plus
  (C2), (C4), lev ≤ M_D ≤ L, G_D (a) on F_D — no hypothesis. (b′) supplies both ✓.

## 3. WM-G, P^c_L, CR-D: SIGN
- WM-G ✓: σ_{k+1} is the pointwise optimum of the arena H_k of G_τ (SPEC S4a; my Runner computes exactly that), σ_k ∈ H_k, (F1) ✓.
- Setting ✓: on S (fallback-free, in one phase) τ is constant; (MON) by WM-G and (C1) ✓; (V2c) ✓ (different cycle nodes: x ⊕ keeps them and
  reward decides; same cycle node: (C4) adds x to both coarse sets or to neither, x in neither, so the symmetric difference is unchanged);
  by (ii) every W-cycle node u has Ω_k(u) = (u, ∅, 0) on S ✓.
- P^c_L, induction checked case by case:
  - base ✓; step: r = x → z → r′, r′ avoids x; IH at k for z ✓; a := σ_k(x) (Even) or τ(x) = z (Odd) ✓.
  - A1 (x ≠ λ_W(x)): (V1) Ω_k(x) = x ⊕ Ω_k(a) ✓; x ∉ P(value(r′)) (r′ avoids x), x ∉ P(Ω_k(a)) (if a's W-play passes x, x is on its own
    W-cycle below its node) ✓; value(r) = x ⊕ value(r′) ✓; IH + Case A give COARSE(value(r′)) ⪯ Ω^c_k(a), then (V2c), (C4), (MON) ✓.
  - A2 (x = λ_W(x)): x ≠ u ✓; reward(x) > reward(u) decides ✓; reward(x) < reward(u): a is on x's W-cycle, so Ω_k(a) has node x, and
    COARSE(value(r′)) ≻ Ω^c_k(a) ⪰ Ω^c_k(z) ⪰ COARSE(value(r′)) is a contradiction ✓; no tie (injective rewards) ✓.
  - B (Ω^c_k(z) ≻ Ω^c_k(a), x Even): by (i) and (Cstrict), Ξ_k(z) ▷ Ξ_k(σ_k x), so (x, z) ∈ Iσ_k (SPEC S2) and σ̂ := σ_k[x ↦ z] ∈ H_k ✓;
    S4a + (F1): Ω_{k+1}(x) ⊵ val_σ̂(x) ✓.
    - B1, x ∉ π, x not on c′'s W-cycle: x's σ̂-play is x then z's W-play (σ̂ = σ_k off x, and z's W-play avoids x) ✓; the chain via (C1), (C4),
      IH, (V2c) ✓.
    - B1, x ∉ π, x on c′'s W-cycle: a is x's successor on that cycle, P(Ω_k(a)) = ∅ ✓; same cycle node c′, so the strict coarse order means
      P(π) ∩ V_{>L} ≠ ∅ with an even top t ✓. N-NC-3: the packet does not say why x → z → π → c′ → (old arc c′ … x) → x is a SIMPLE cycle
      with top t. It is: π ends at its first arrival at c′; if π joined c′'s cycle at a vertex y on the arc from c′ to x, π would run
      through x before c′, against x ∉ π; so π meets the arc c′ … x only at c′. Arc vertices rank ≤ c′; x ranks below c′; t ∉ the old
      cycle (rank(t) > rank(c′)); so the top is t, reward(t) > reward(c′) (t even and above c′) ✓, and (F1) moves λ_W(x) off c′, against (ii) ✓.
    - B2, x ∈ π: λ_W(x) = c′ ✓; Z := x, z, π[z..x) is x's σ̂-cycle ✓; Ω_k(z) = π[z..x) ⊕ Ω_k(x) (vertices of π[z..x) that lie on c′'s cycle rank
      below c′ and add nothing) ✓; the coarse sets of Ω_k(z) and Ω_k(a) differ exactly by D ∩ V_{>L} (x ≠ c′: a's path is π[a..c′]; x = c′:
      P(Ω_k(a)) = ∅) ✓; strict ⇒ top t of D even ✓; vertices of Z outside D rank ≤ c′ (c′ ∉ Z unless x = c′) ✓; (F1) moves λ_W(x), against
      (ii) ✓.
- CR-D ✓: for t ≥ k_0 + n − 1, x's W-play at t is a simple path r_t of G_τ (≤ n − 1 edges) to λ_W(x), a W-cycle node at every state of S by
  (ii); Ω_t(x) = value(r_t) ✓; P^c_L at j = n − 1 (k_0 + n − 1 ≤ t is in S) and (MON) from k_0 + n − 1 to t; (C3) ✓.

## 4. FRZ-U_D: SIGN
(i) at each state is (c2′) with M_D ≤ max_S M_D ≤ L (M_D finite under (h3_D)) ✓. (ii): on F_D λ_W = λ_Ξ (R55 (a)); on R_D, (b′) factors both
plays through u(v), so λ_W(v) = λ_W(u(v)) = λ_Ξ(u(v)) = λ_Ξ(v) by (h3_D) ✓; λ_Ξ is constant on the phase ✓. CR-D applies ✓. Scope as stated ✓.

## 5. DATA (nc_check.py; own definitions; S3 (#0) and random start pairs)
| set | runs | states (NC / NC ∧ ¬h_D) | (b′) checks (NC ∧ ¬h_D) | (c1′) | (c2′) (all L ≥ max(M_D, −1)) | WM-G transitions | P^c_L checks (n ≤ 9) | CR-D freeze | FRZ freeze (D ≠ ∅) | violations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lib41.txt, S3 + 2 random | 1,236 | 19,551 (14,228 / 642) | 103,287 (17,232) | 840,181 | 285,619 | 11,247 | 11,570 | 0 | 4 (4) | 0 |
| R2-N5-KW/files.lst (𝒞^1O), S3 + 2 random | 1,509 | 24,435 (20,540 / 0) | 140,366 (0) | 1,281,426 | 336,156 | 15,722 | 24,127 | 0 | 5 (5) | 0 |
| lib2o_noref.lst, S3 + 3 random | 164 | 1,179 (993 / 197) | 4,279 (2,260) | 19,430 | 9,215 | 596 | 5,526 | 0 | 0 | 0 |
| box-43/44, S3 + 5 random | 60 | 638 (542 / 200) | 4,263 (2,678) | 21,662 | 5,191 | 232 | 1,530 | 0 | 0 | 0 |
| random 𝒞^2O n 5-12, 2 random pairs | 40,000 | 100,903 (68,776 / 1,619) | 29,509 (5,131) | 12,070 | 645,187 | 4,934 | 2,372,665 | 0 | 0 | 0 |
| random 𝒞^3O n 5-12, 2 random pairs | 20,000 | 53,833 (32,283 / 1,472) | 16,693 (5,077) | 6,489 | 300,282 | 1,971 | 1,123,994 | 0 | 0 | 0 |
| random 𝒞^kO n 2-5, 3 random pairs | 60,000 | 114,312 (81,998 / 261) | 6,772 (609) | 726 | 445,661 | 3,880 | 1,568,071 | 1,377 | 458 (0) | 0 |
- (b′), (c1′), (c2′) are exercised widely, including the case the lemma adds: 32,987 (b′) checks at states with (NC) ∧ ¬(h_D), 0 failures.
- N-NC-4 (DATA, the freeze): the packet's §6 says the freeze is vacuous in all its data. In mine it is REACHED:
  - FRZ-U_D on a natural instance with D ≠ ∅: experiments/red/so/instances/pftheta34_n32.pg from S3 (n 32): a fallback-free in-phase run
    with (NC) ∧ (h3_D) at every state lasts 3 states past n − 1; COARSE_L(W) = COARSE_L(Ξ) and frozen, as claimed (4 + 5 freeze checks in the
    two lists; the same run). (h_D) holds on it, so this is the case successor 10's CR-D′ already covered, not the new (NC) ∧ ¬(h_D) case.
  - CR-D's freeze (hypotheses (i), (ii) checked directly, per L) and FRZ on tiny random games (n 2-5): 1,377 and 458 freeze checks, all with
    D = ∅ there (one-player-like). 0 failures.
  - The freeze under (NC) ∧ ¬(h_D) is NOT reached in my data.
- P^c_L at every j (not only the freeze): 5.1 million checks, 0 failures.
- Mutation controls: b0 ((b′) without (NC)) fails 94,468 times on lib41 and 36,925 on the tiny set — (NC) is needed; pc1 (P^c_L with j + 1
  edges) fails 27,546 — the edge budget is tight; crd1 (freeze from k_0 + 1) fails 66 — n − 1 is not replaceable by 1.
- Reproduce: `sh docs/referee-2/R2-N5-NC/run_all.sh` (≈ 2 min); `NC_MUT=b0|pc1|crd1` for the controls.

## 6. Notes
- N-NC-1: two quotes not character-exact (bullets joined; parentheticals dropped without "…"); content verbatim.
- N-NC-2: the (h_D) → (NC) replacement checked at the one (h_D) use of R55 (b)'s proof; (c1), (c2) use (h_D) only via G_D (b).
- N-NC-3: P^c_L case B1 (x on c′'s W-cycle) needs "π meets the old arc only at c′" for the new cycle to be simple with top t; supplied
  above. One line for the fixes file.
- N-NC-4 (DATA): the freeze is reached (natural, D ≠ ∅, under (h_D); tiny games, D = ∅); not under (NC) ∧ ¬(h_D). §6's "vacuous" line is
  out of date.
