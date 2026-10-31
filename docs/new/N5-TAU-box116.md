# N5-TAU (box 116): τ-stretches — the general bound is G-N5-TIME in disguise; on switchbestexp N5's τ never returns, while full Odd re-optimisation (ARSB, TBR) returns and re-arms
L-NEW successor 42, 2026-10-31 (date -u: after 16:15Z). Lead brief 16:15Z (box 116): bound N5's τ-stretches (S4b moves) per run, or the
Even carries re-armed per τ-stretch, starting from the switchbestexp traces.
Labels: PROVED (lane), DATA, READING, OPEN. No count is bounded here. G-N5-TIME stays OPEN. This is not M3 and not a TARGET.md claim.

## 0. Answer
- DATA, switchbestexp_N (N = 2..4; box115/taumv.py, faithful runs of box 115):
  - N5 moves τ exactly N times: one move per bit's Odd vertex, h_i: e_i → m_i (the escape from the bit cycle), top bit first, at
    consecutive transitions 12, 13, …, 11 + N.
  - No Odd vertex ever returns.
- DATA: the variants that re-arm the carry are exactly those whose Odd reply RETURNS to an earlier choice:

| N | ARSB: σ̄ changes / returns | TBR: τ changes / returns | N5: τ changes / returns |
| --- | --- | --- | --- |
| 2 | 4 / 2 | 4 / 2 | 2 / 0 |
| 3 | 11 / 8 | 11 / 8 | 3 / 0 |
| 4 | 26 / 22 | 24 / 20 | 4 / 0 |

- PROVED (lane) Lemma TAU-EQ (§1). For every family of games closed under taking duals, the following are equivalent:
  - N5 and its «Odd first» variant N5^OF (RESULTS R54) both have polynomially many iterations;
  - both have polynomially many τ-changing transitions.
  - So «bound τ-stretches per run» in general IS G-N5-TIME, for the pair N5 / N5^OF. It is not a smaller target.
- PROVED (lane) Lemma ODD-RETURN (§2), the mirror of L-SI's RETURN-CHARGE′: if Odd o leaves x at k1 and re-enters x at k2 > k1, then
  Odd's valuation Ξτ(x) on G^d strictly improves (for Odd) between k1 and k2.
  - Corollary: τ-changing transitions ≤ Odd switches ≤ Σ_o (deg(o) − 1) + Σ_(o, x) XCH^d_(run)(x), where XCH^d(x) counts the changes of
    Ξτ(x).
  - That is the mirror of the Even-side XI-CH core, again not smaller.
- READING (what forbids re-arming on switchbestexp):
  - ARSB / TBR set Odd's reply to the full best reply σ̄_k. That reply is not an Iτ-improvement of τ, so it can flip back (e_i ↔ m_i)
    with no rise of Odd's own valuation, and each flip re-arms Even's bit carry.
  - In N5 a flip back is a return of o to e_i. By ODD-RETURN it needs a strict rise of Ξτ(e_i) on G^d, and none comes, because Odd's
    valuation of the escape is already final.
  - So the property is: τ moves only along Odd's own improvements (S4b's arena τ ∪ Iτ), and returns are paid by dual Ξ-rises.
  - OPEN: turning this into a bound needs the dual XI-CH core, which is the same open core as the Even side.

## 1. Lemma TAU-EQ — PROVED (lane)
- Premises:
  - RESULTS R54 Lemma DUAL: the N5 run on G is the mirror of the N5^OF run on G^d (σ and τ exchanged).
  - SPEC S4: every non-final transition changes σ or τ. S4a / S4b, or S4c's fallback, changes at least one, and a transition with
    Iσ = Iτ = ∅ is the stop.
- Proof.
  - On G: iterations ≤ SCH_(N5)(G) + TCH_(N5)(G), where SCH / TCH count the σ- / τ-changing transitions.
  - By DUAL, SCH_(N5)(G) = TCH_(N5^OF)(G^d). The same holds with N5 and N5^OF exchanged.
  - So if TCH is polynomial for both algorithms on a dual-closed family, both have polynomially many iterations.
  - The converse holds because TCH ≤ iterations. □
- The τ-stretch target is therefore equivalent to G-N5-TIME as stated, not easier. Only per-structure versions (per λ-run, per W-run,
  re-arming per stretch) can be easier.

## 2. Lemma ODD-RETURN — PROVED (lane)
- Premises:
  - RESULTS R15 (a), (d) on the dual game: each N5 step applies Switch_I with ∅ ≠ I ⊆ Iτ to τ on G^d, so Ξτ is pointwise non-decreasing
    in the dual order ⊵^d (Lemma A).
  - SPEC S2 / S4b / S4c: every τ-switch at k goes to an edge of Iτ_k. S4b's arena is τ ∪ Iτ; S4c picks from Iτ; S4a leaves τ.
- Statement. If Odd o has τ_(k1)(o) = x, leaves x at k1, and has τ_(k2+1)(o) = x for some k2 > k1, then Ξτ_(k2)(x) ▷^d Ξτ_(k1)(x).
- Proof. This is the mirror of RETURN-CHARGE′ (L-SI box 51b §11, quoted in P-N5-WRUN fixes, cross-reads).
  - j ↦ Ξτ_j(τ_j(o)) is non-decreasing in ⊵^d.
    - Without a switch at j, use Lemma A.
    - With a switch a → b at j: Ξτ_(j+1)(b) ⊵^d Ξτ_j(b) ▷^d Ξτ_j(a).
  - Leaving x at k1 for y: Ξτ_(k1)(y) ▷^d Ξτ_(k1)(x).
  - Re-entering x at k2 from w: Ξτ_(k2)(x) ▷^d Ξτ_(k2)(w) ⊵^d Ξτ_(k1+1)(y) ⊵^d Ξτ_(k1)(y) ▷^d Ξτ_(k1)(x). □
- Corollary. Each return of o to x is charged to a transition in (k1, k2) at which Ξτ(x) changes, and distinct returns of o to x have
  disjoint windows. So returns of o to x ≤ XCH^d(x), and Odd switches ≤ Σ_o (deg(o) − 1) + Σ_o Σ_(x ∈ succ(o)) XCH^d(x).

## 3. DATA (box116/tauc.py; corpus = L-SI box 53's 1,132 games; comp54_n80 / n3cov_lean on box 113's repaired starts)
- τ-changing transitions: total 4,004.
  - Max 55, on red/usplit/instances/pp_K48_n449_dual (n 449, 56 iterations; τ moves at almost every step: a dual-side family).
  - Max relative 1.16n, on red/n5inj/instances/wide_h16 (n 32, 37).
- Odd switches: total 15,236. Max 356 (red/tcpert/instances/tcL_N12, n 492). Max at one vertex 13 (red/rec0/instances/nep24_n20).
- Odd returns: 2,963 in 281 runs. Max 145 (tcL_N12), max relative 0.87n (new/box54/out/d_hntop_n3).
- τ-changes made by S4c fallbacks: 36.
- So Odd returns are common in the corpus. switchbestexp's «0 returns» is a property of that family under N5, not a general law.

## 4. Next (READING)
- The two halves of every N5 run are now both known to be equivalent to G-N5-TIME by themselves:
  - W-runs: STAIR / ROOT reductions;
  - τ-stretches: TAU-EQ, via DUAL.
- A proof has to couple them. Example: an Even carry re-armed inside a τ-stretch must be paid by a τ-change or a source event (R97).
  - The switchbestexp contrast says the coupling exists there: Even's carry needs Odd returns, and N5's Odd returns cost dual Ξ-rises.
- Concrete OPEN target, CARRY-ODD (not stated as a conjecture until tested): in an N5 run, the number of times an Even pair (y, z) is
  re-entered at the same key, across τ-stretches, is ≤ poly(n) × (Odd returns + source events).
  - Test it on the corpus and on L-RED's builds before stating it.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/new/box116/ (tauc.py, runtau.sh, t_* corpus outputs); box115/taumv.py; box115/abl.py now prints Odd-reply
  changes / returns (ODDREPLY line).
- FINDINGS:
  - DATA: switchbestexp under N5 has τ moves = N, monotone, 0 returns; ARSB / TBR return 2 / 8 / 22 times.
  - PROVED (lane): TAU-EQ (the τ-stretch bound is G-N5-TIME via DUAL) and ODD-RETURN (returns are paid by dual Ξ-rises).
  - READING: what forbids re-arming is that τ moves only along Odd's improvements.
- NEEDS: Lead: route the coupling target CARRY-ODD (test first) or another box.
