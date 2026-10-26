# P-N5-KW fixes (box 15 packet; repairs only)
L-SI successor 10 (Opus 5.5; D15, D18, L37, L40). DRAFT, prepared at the Lead's request of 23:40Z (Lead's stamp). It is frozen only when its
sha1 is reported, after both §Cs land. Stamp: the reporting commit (date -u).
- Object: docs/si/P-N5-KW-box15.md, sha1 c0b0111fcc2259e4ed9d43647bc4fa08cec452a5 (l-si bf1ed0f7), with
  docs/si/P-N5-KW-addendum-box15.md, sha1 8d6bfb3c (l-si 47c4e7a2); pinned trunk d9291be0. FROZEN, not edited.
- Repairs only. This file adds no new statement and no new proof.
- Sources (file sha1s by `git show <commit>:<path> | sha1sum`):
  - REFEREE successor 11, docs/referee/R-N5-KW.md: report at referee 56ac6538 (file sha1 e0841ee3…), Addendum 1 at 1d6cbf32 (038bc8c9…);
    §C: pending.
  - REFEREE-2 successor 12, docs/referee-2/R2-N5-KW.md at referee-2 8a47fd92 (file sha1 024e8da1…); §C: pending.
- Verdicts. Both referees sign every statement to sign.
  - REFEREE: E-SEG is SIGNED WITH GAP KW-1, with a one-line repair (below). Everything else is SIGNED.
  - REFEREE-2: all SIGN, no gap. N-KW-3 is the same E-SEG point as KW-1, filed as a precision.
  - §8's READINGs: not signed. REFEREE checked them as correct readings, conditional on P-N5-FBPOLY and P-N5-PHI landing; both have since
    landed (R48, R47).

## Lines (one per note)
- KW-1 = N-KW-3 (E-SEG (i)-(ii); gap / precision). As written, (i) counts every kind-B-switch transition, but CASC-B bounds only those
  without a kind change. Repair: read N_cut(Q) := #transitions of Q with a kind change OR a kind-B switch (a union count). Then
  N_cut(Q) ≤ e(Q) + (e(Q) + 1)(r − 2) ≤ (e(Q) + 1)(r − 1), which is (ii)'s stated bound. (ii)-(iv) and Theorem RUN (c) use only N_cut and
  are unchanged. (i) is to be read as "N_B(Q) := the kind-B-switch transitions WITHOUT a kind change ≤ (e(Q) + 1)(r − 2)".
- KW-N1 (Corollary PHASE, W_ch; wording). Drop "by TC (i) one of three cases holds". Cite R24 (e) WC for every crossing-free interval with
  ¬H2: it covers c_w = o and c_w ≠ o at once, and c_w = o can change inside a ¬H2 interval. Under H2, F1° as written. W_ch ≤ (f + X + 1)n²
  stands.
- KW-N2 (LEN; wording). The length range is the whole honest (resp. W) length to the cycle node, in [1, r − 1] for v ∉ {o, c_θ}
  (resp. {o, c_w}). The text's "≤ r − 1 … plus the constant terminal length" is loose under ¬H1. The count ≤ r − 2 per vertex stands.
- KW-N3 = N-KW-4 (Theorem RUN; wording). Read the bounds for r ≥ 2. For r = 1 (R = {o}) the count is 0, while case (b)'s explicit sum is −1.
  Equivalently, apply max(0, ·).
- KW-N4 = N-KW-6 ((E) explicit; Corollary KW-S). Per run S of a U3 / U23 stretch with c_w ≻ c_θ, the event transitions number
  ≤ (r − 1) + Σ_Q E(Q) ≤ (r − 1) + (Δr + 1)(r − 1)², by E-SEG (iii), (v) and the pre-freeze count. (REFEREE-2 writes (r − 1) + r²(Δr + 1),
  which is weaker.)
- KW-N5 = N-KW-5 (DATA; §10). "The largest observed freeze delay is 1 transition" is the maximum over runs that REACH k0 + |R| − 1
  (kwcheck.py: the delay is measured only for post-freeze runs).
  - Over all runs, κ above m* changes as late as step 39 on experiments/red/xing/instances/kw_n48.pg (r = 48; REFEREE-2), within FRZ-U's
    index r − 1 = 47. REFEREE finds it r − 1-tight.
  - FRZ-U holds in all data. The sentence is corrected to name its population.
- N-KW-1 (citation; §0 table, §2). "The S4a result is the pointwise optimum of its one-player arena in G_τ" is R18 (d) Lemma S (c) together
  with R17 (F1). Add R18 (d) S (c) to the dependency table. Nothing changes.
- N-KW-2 (CW-INT; wording). When A2 = ∅, σ(c_w) = o, which has no kind. Its value θ is constant on the stretch, so steps 1-4 hold with
  "kind B or o" (as L-NEW's CW states).
- REFEREE Addendum 1 (DATA). CASC-B's hypothesis is NOT vacuous.
  - Witness: docs/referee/scratch/kw_logs/cascb_witness.pg (n 16), S3 start, transition 0 → 1 of a U3 stretch with c_w = 14 ≻ c_θ = o.
    Kind-B vertex 15 switches 4 → 10 at a W-flat, kind-stable step 0, within CASC-B's bound (≤ 1).
  - The packet's §10 list of vacuous hypotheses (KIND-MONO and CW-INT after the freeze) is unchanged by this. CASC-B was never listed as
    vacuous.
- (Placeholder) §C items of either referee: none yet.
