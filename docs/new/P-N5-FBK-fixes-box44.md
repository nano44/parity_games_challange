# P-N5-FBK fixes (box 44 packet): verbatim quotes of the cited P-N5-2T statements
L-NEW successor 23 (Opus 5.5, D14/D18, L40), session_011WFfFqRNrU1a8LQwbwazZN. Written 2026-10-26 04:43Z by date -u, after the Lead's message of
04:40Z (Lead's stamp), which crossed the freeze of P-N5-FBK at 04:42Z: "quote PFZ-q (§2) and DIR (§4) verbatim from that file." FROZEN at push;
its sha1 is reported to the Lead.
- Object: packet docs/new/P-N5-FBK-box44.md, sha1 afd7c65a265053531171b66294811bbd9a801dd2 (l-new 9dd499d3). The packet is NOT edited; this
  file is its correction layer. No signed statement changes: the packet cites PFZ-q and DIR "exactly as stated"; the text below is that
  statement, copied verbatim.
- Source: docs/si/P-N5-2T-box16.md, sha1 fcb91130b1f93d041233c9def50614b4d0dc9a05 (l-si f6839fd3, pinned trunk cbb3b738).

## 1. P-N5-2T §2, Lemma PFZ-q, statement (verbatim, P-N5-2T lines 85-88)
Statement. Let q ∈ Q_c and let Θ be a q-run, with κ_Θ(q) the value of κ(q) on Θ. Let j ≥ 0, and let t ∈ Θ with t > f^Θ_j (any t ∈ Θ if
j = 0). Let z ∈ (U_c ∖ T) ∪ {q}, and let p be a simple path of G_c^q from z to q with ≤ j edges. Then
κ_t(z) ≥ κwt_c(p ∖ {q}) + κ_Θ(q).
This is FBRED κ-PFZ_D with "Q_c-run" weakened to "q-run", and with the range of N-FBRED-1.

## 2. P-N5-2T §4, Lemma DIR, statement (verbatim, P-N5-2T line 121), with its value set (line 115) and DIRECT (lines 53-54)
Statement. Let t > g_{|U_c|−1}, and let q ∈ Q_c be direct at t. Then κ_t(q) ∈ A_q.
- A_q := {κwt_c(q) + κopt_c(y) : y ∈ succ(q) ∩ U_c ∖ Q, κopt_c(y) defined} ∪ {κwt_c(q) : c ∈ succ(q)} ∪ Cyc_c. So |A_q| ≤ d_q + w_c.
  - DIRECT: q ∈ Q_c is direct at t if q lies on its own honest cycle at t, or its honest play at t visits c before any other vertex of
    Q_c.

## 3. How P-N5-FBK uses them (unchanged)
- SAT-k (FBK §2, "≥"): PFZ-q with z = y ∈ U_c ∖ T, Θ = Θ_p (a p-run), j = w_c = |U_c| − 1.
- FB-kT (FBK §3, step 2, h = 0): DIR at k_i > g_{n−1} ≥ g_{|U_c|−1}.
