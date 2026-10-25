# P-N5-OE fixes (box 32): the referees' repairs, written out
L-NEW successor 13 (Opus 5.5, D15/D18). Lead GO box 33 02:06Z (Lead's stamp; read 02:06Z). Written 2026-10-25 02:06Z onward by date -u.
- Object: packet docs/new/P-N5-OE-box32.md, pinned at trunk 361d18c, sha1 adeccd898ad1e4de6532fc3a77a9d600d8a0bc16 (re-checked at this
  commit: unchanged; `git diff 361d18c HEAD` on it is empty). The packet is NOT edited; this file is its correction layer.
- Sources: REFEREE docs/referee/R-N5-OE.md (5e98e33c); REFEREE-2 docs/referee-2/R2-N5-OE.md (ca6e5bd1); both on trunk 1d35e8e9. §C items,
  if any, follow in a later section or file when the Lead relays them.
- Rule: one line per item, then the repair written out. A line of my own is marked "L-NEW".

## 0. Verdicts and items
| statement | REFEREE (Opus 5.5, D15) | REFEREE-2 (Opus 5.5, D15) | items |
| --- | --- | --- | --- |
| §1 Lemma U-loc (any game, inside a phase) | SIGNED | SIGN | none |
| §2 Lemma OE (𝒞^1O) | SIGNED WITH GAPS OE-1, OE-2 (closed), OE-3 | SIGN (notes N-OE-1, N-OE-2, N-OE-3) | OE-1 = N-OE-1 (§1); OE-2 (§2); OE-3 (§3); N-OE-2 (§4); N-OE-3 (§5) |
| §3 Corollary OX (i)-(v) (𝒞^1O) | SIGNED (OX-1 wording) | SIGN (N-OE-3 for (iv)) | OX-1 (§6) |
| §3 Reading | not signed (not asked); note §3.6 | not signed; "correct as a reading" | §7 |

## 1. OE-1 = N-OE-1: the "In particular" sentence of Lemma OE
- The proof gives O_k ≤ E_k, so E_k = ⊥ ⇒ O_k = ⊥. It does not exclude a relevant σ̄(o) change of level ⊥ (a move between successors of
  equal Ξ_k-value, which P-N5-LP §1 counts as relevant when λ(o) ≠ o). Such tie moves occur off crossings (REFEREE: library 2, random 50);
  with E_k = ⊥ none was seen by either referee.
- Replace "In particular, if Even makes no relevant change, σ̄(o) makes no relevant change." by:
  "In particular, if Even makes no relevant change, σ̄(o) makes no relevant change of level ≠ ⊥ (O_k = ⊥)."
- The literal stronger sentence is DATA, not PROVED (0 counterexamples in both referees' data). Nothing in §3 uses it: (i) and (iii) use
  the used level, (ii) a level > M_k (both referees).

## 2. OE-2 (closed by REFEREE): CAP-1 at o lying on its honest cycle (¬H1)
- Step 1's citation "CAP-1 closure" reads: σ̄_k(o) is a FULL Ξ_k-minimiser over succ(o) whenever λ(o) ≠ o — REFEREE's case proof
  docs/referee/R-N5-FB.md §4.2, adopted by REFEREE-2 docs/referee-2/R2-N5-FB.md §C.3 (as in P-N5-SO-fixes §1). That proof does not assume o
  off a cycle, so it covers step 4 (¬H1, ℓ = −1), where o is on its honest cycle but is not its cycle node (REFEREE re-derivation,
  R-N5-OE §2.2). No text change in the packet's argument.
- Trap check (both referees): the minimiser property FAILS at λ(o) = o (REFEREE 102 of 527 states; REFEREE-2 420 of 3,177); OE never uses
  it there, because O_k is defined only for relevant changes, which need λ(o) ≠ o.

## 3. OE-3: step 3's comparison, with its rules cited
Replace "differ, are the same at k and k+1, and decide the comparison (the top difference is above E_k). At k, Ξ_k(x0) ◁ Ξ_k(x1) strictly
… So Ξ_{k+1}(x0) ◁ Ξ_{k+1}(x1)" by:
- At k, Ξ_k(x0) ◁ Ξ_k(x1) strictly (x0 a full minimiser, values differ). Since ℓ > E_k, (C2) makes their COARSE_{E_k} values differ, and
  (C1) gives COARSE_{E_k} Ξ_k(x0) ◁ COARSE_{E_k} Ξ_k(x1). By Lemma U-loc both coarse values are the same at k+1.
- If Ξ_{k+1}(x1) ⊴ Ξ_{k+1}(x0), then (C1) gives COARSE_{E_k} Ξ_{k+1}(x1) ⊴ COARSE_{E_k} Ξ_{k+1}(x0), against the strict coarse order
  (with (C3)). Since ⊴ is total, Ξ_{k+1}(x0) ◁ Ξ_{k+1}(x1): x1 is not a minimiser at k+1, against CAP-1 at k+1. (REFEREE.)

## 4. N-OE-2: step 3's "x0's honest play does not return to o", with its reason
Insert after "Case H1 at k":
- H1 says o lies on no honest cycle. x0's H_k-play is the tail of o's H_k-play (x0 = σ̄_k(o)); if it visited o, o would lie on the
  H_k-cycle of its own play, against H1. So x0's (σ_k, τ)-play equals its H_k-play and avoids o: x0 ∈ F_k = F_{k+1} (no crossing).
- x0's H_{k+1}-play agrees with its (σ_{k+1}, τ)-play up to the first visit of o, and that play never reaches o (x0 ∈ F_{k+1}); so the
  H_{k+1}-play avoids o. The R19 (a) citation is this one-line fact. (REFEREE-2; REFEREE gives the same direct argument.)
- Also (both referees): step 2 has a shorter reason. H_{k+1} is functional, so a visit of o before c would return to x1 = σ̄_{k+1}(o)
  before c and never reach c.

## 5. N-OE-3: the phase key of the cited results
- P-N5-OE's phase (from P-N5-LP) is (λ_Ξ, τ) constant, coarser than the key (λ_Ξ, λ_U, τ) of R21-R23 and R25. Each citation transfers
  (REFEREE-2, R2-N5-OE §4):
  - R25 (d) Theorem FB: P-N5-FB (docs/si/P-N5-FB-box7.md) l.47 "Only λ_Ξ and τ constant is used"; the proof uses nothing else.
  - R25 (e) J1 and CAP-1: statewise, or need only (λ_Ξ, τ).
  - R22 (b) TC (i) "H1 ⟺ λ_Ξ(o) ∈ F": statewise.
  - R19 (a): only as the one-line fact of §4.
- REFEREE-2's checker uses the coarse phase throughout, so its 0-failure data is on this reading.

## 6. OX-1: what f and T count
Add to Corollary OX, after the statement: "Here f (R25's in-phase fallback count) and T count transitions with both ends in the phase; a
phase-exit fallback adds at most 1 (R25 FB-2)." (REFEREE.)

## 7. Notes on the Reading (not signed; READING)
- REFEREE §3.6: "X ≡ Z up to a factor n" holds in the direction X ≤ (n − 1)(Z + 1) + Z (R23 LV′). Read the Reading's phrase as that
  inequality; it is the direction a bound on Z needs.
- REFEREE §3 (v) multiplied out: f ≤ 2n²(X + 1), so T = O(m·n⁵·(1 + X) + m·n³·K) ⊆ O(m·n⁵·(1 + X + K)).

## 8. Data notes (DATA, not proof)
- Both referees: 0 failures of U-loc, OE, CAP-1 (λ(o) ≠ o), OX (i)-(v) on the 234-file library (n ≤ 64), random 𝒞^1O and general
  games, and REFEREE-2's climbs (27,200 runs; 72,414 off-crossing relevant σ̄(o) changes, 4,598 ¬H1; 30,002 non-tame transitions, all
  crossings). jcl_zcl_cu_n48: J 17 = X 17 = ε 17 (tight), confirmed by both.
- Count differences against the packet's DATA (217 / 175 / 431 + 11 on 220 files vs 279 / 235 / 436 + 11 on 234 files): file selection
  (the library grew; c1o_list.py does not deduplicate successors). Same zero-exception statements, same 11 ¬H1 cases. Not a disagreement.
- Thin spots (both): wakes K = 1 in all data (nowake_cex_n32), so (iii)'s wake term is barely exercised; OE step 4's ℓ = −1 branch is
  checked only through its intermediate facts.

## 9. Labels after two signatures (D18/L40)
- PROVED (L-NEW successor 12; REFEREE and REFEREE-2, Opus 5.5, D15), pending CHECKER: Lemma U-loc on every game inside a phase; Lemma OE
  (with §1's wording) and Corollary OX (i)-(v) on 𝒞^1O, with §2-§6.
- OPEN: X and K per phase; G-N5-TIME. Not a TARGET.md claim, not a step-4 pass (TARGET.md section 1 untouched).

## 10. §C (both referees; added 2026-10-25 02:48Z by date -u, after R28 landed at trunk de7a635)
- Sources: REFEREE docs/referee/R-N5-OE.md §C (84748819); REFEREE-2 docs/referee-2/R2-N5-OE.md §C (ea6ad672). No verdict differs; neither
  referee found a counterexample or a false step.
- Joint gap map → this file:
| row | REFEREE | REFEREE-2 | status | here |
| --- | --- | --- | --- | --- |
| 1 | OE-1 | N-OE-1 | wording | §1 (level ≠ ⊥, equivalently ≥ −1) |
| 2 | OE-2 | accepted in §C | closed | §2 |
| 3 | OE-3 | N-OE-2 (step 3) | wording | §3 and §4 (REFEREE-2 merges them into one line) |
| 4 | — (missed, accepted in §C) | N-OE-3 | closed | §5 |
| 5 | OX-1 | accepted in §C | wording | §6 |
| note | 3.6 | accepted | reading | §7 |
- Corrections to this file from §C:
  - §1: the tie moves REFEREE counted off crossings (library 2: n5s_maxph_0, j8_n32; REFEREE-2 random 5) all have E_k ≠ ⊥. With E_k = ⊥
    both referees count 0. So the literal "In particular" sentence is unproved, not refuted.
  - §8: the count difference between the packet's DATA (220 files) and the referees' (234 files) is the trunk date of the lane's run;
    c1o_list.py today lists the same 234 files. REFEREE-2 withdrew its "no deduplication" explanation; strike it here too.
  - Data: on the 234-file library at the canonical start, three implementations give identical counts (REFEREE oe_probe.py, REFEREE-2
    logs1, the lane's oddlev.py): crossing-free relevant σ̄(o) changes 436 (H1) + 11 (¬H1); O_k > E_k 279, all at crossings; non-tame 235,
    all crossings.
- Labels (both §C.4): PROVED (L-NEW successor 12; REFEREE and REFEREE-2, Opus 5.5, D15): U-loc on every game inside a phase; OE (row 1's
  wording) and OX (i)-(v) on 𝒞^1O. LANDED as RESULTS R28 (Lead, trunk de7a635). OPEN: X and K per phase; G-N5-TIME.
