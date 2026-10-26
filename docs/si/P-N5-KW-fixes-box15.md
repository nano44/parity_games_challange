# P-N5-KW fixes (box 15 packet; repairs only)
L-SI successor 10 (Opus 5.5; D15, D18, L37, L40). Prepared at the Lead's request of 23:40Z; frozen at the Lead's GO of 00:04Z (Lead's stamps),
after both §Cs landed (trunk 6021ea55). Stamp: the commit (date -u).
- Object: docs/si/P-N5-KW-box15.md, sha1 c0b0111fcc2259e4ed9d43647bc4fa08cec452a5 (l-si bf1ed0f7), with
  docs/si/P-N5-KW-addendum-box15.md, sha1 8d6bfb3c (l-si 47c4e7a2); pinned trunk d9291be0. FROZEN, not edited.
- Repairs only. This file adds no new statement and no new proof.
- Sources (file sha1s by `git show <commit>:<path> | sha1sum`):
  - REFEREE successor 11, docs/referee/R-N5-KW.md: report at referee 56ac6538 (file sha1 e0841ee3…), Addendum 1 at 1d6cbf32 (038bc8c9…),
    §C at a6e50742 (6ad87c96…) with its one-line fix at 776281ac (b7c76299…).
  - REFEREE-2 successor 12, docs/referee-2/R2-N5-KW.md: report at referee-2 8a47fd92 (file sha1 024e8da1…), §C at 20fea7d7 (41f540d1…).
- Both §Cs: identical verdicts. Every statement to sign is signed by both. KW-1 = N-KW-3 is ONE finding, closed by the definitional repair
  below; with it, E-SEG is signed by both without a gap. No disagreement remains.
- Verdicts. Both referees sign every statement to sign.
  - REFEREE: E-SEG is SIGNED WITH GAP KW-1, with a one-line repair (below). Everything else is SIGNED.
  - REFEREE-2: all SIGN, no gap. N-KW-3 is the same E-SEG point as KW-1, filed as a precision.
  - §8's READINGs: not signed. REFEREE checked them as correct readings, conditional on P-N5-FBPOLY and P-N5-PHI landing; both have since
    landed (R48, R47).

## Lines (one per note)
- KW-1 = N-KW-3 (E-SEG (i)-(ii); one finding, closed by a definition). REFEREE's line, verbatim: "N_cut(Q) := #transitions of Q with a kind
  change or a kind-B switch (counted once); N_B(Q) := those without a kind change; (i) N_B ≤ (e+1)(r−2); (ii) N_cut ≤ (e+1)(r−1) − 1".
  - (i) as written, counting every kind-B-switch transition, is a bound the proof does not give. With the definitions above it holds.
  - (ii) follows: N_cut ≤ e + (e + 1)(r − 2) = (e + 1)(r − 1) − 1. E-SEG (iii)-(iv) and Theorem RUN (c) use only N_cut and are unchanged.
- KW-N1 (Corollary PHASE, W_ch; wording). Drop "by TC (i) one of three cases holds". Cite R24 (e) WC for every crossing-free interval with
  ¬H2: it covers c_w = o and c_w ≠ o at once, and c_w = o can change inside a ¬H2 interval. Under H2, F1° as written. W_ch ≤ (f + X + 1)n²
  stands.
- KW-N2 (LEN; wording). The length range is the whole honest (resp. W) length to the cycle node, in [1, r − 1] for v ∉ {o, c_θ}
  (resp. {o, c_w}). The text's "≤ r − 1 … plus the constant terminal length" is loose under ¬H1. The count ≤ r − 2 per vertex stands.
- KW-N3 = N-KW-4 (Theorem RUN; wording). Read the bounds for r ≥ 2. For r = 1 (R = {o}) the count is 0, while case (b)'s explicit sum is −1.
  Equivalently, apply max(0, ·).
- KW-N4 = N-KW-6 ((E) explicit; Corollary KW-S; REFEREE's sharper form, as both §Cs choose). Per run S of a U3 / U23 stretch with
  c_w ≻ c_θ, the event transitions number ≤ (r − 1) + (Δr + 1)(r − 1)², by E-SEG (iii), (v) and the pre-freeze count.
- KW-N5 = N-KW-5 (DATA; §10). The line "the largest observed freeze delay is 1 transition" is the maximum over runs that reach k0 + r − 1
  (kwcheck.py measures the delay only on those runs).
  - Over all runs the delay reaches the run length: on experiments/red/xing/instances/kw_n48.pg (r = 48), κ above m* changes up to the run's
    last transition (40 of 40 by REFEREE's count, 39 by REFEREE-2's index).
  - This is within FRZ-U's index r − 1 = 47, so FRZ-U holds in all data.
- N-KW-1 (citation; §0 table, §2). "The S4a result is the pointwise optimum of its one-player arena in G_τ" is R18 (d) Lemma S (c) together
  with R17 (F1). Add R18 (d) S (c) to the dependency table. Nothing changes.
- N-KW-2 (CW-INT; wording). When A2 = ∅, σ(c_w) = o, which has no kind. Its value θ is constant on the stretch, so steps 1-4 hold with
  "kind B or o" (as L-NEW's CW states). Accepted by REFEREE §C.2: CW-INT step 1 reads "σ(c_w) is kind B or o".
- REFEREE Addendum 1 (DATA). CASC-B's hypothesis is NOT vacuous.
  - Witness: docs/referee/scratch/kw_logs/cascb_witness.pg (n 16, sha1 3bda89ce…), S3 start, transition 0 → 1 of a U3 stretch with
    c_w = 14 ≻ c_θ = o. Kind-B vertex 15 switches 4 → 10 at a W-flat, kind-stable step 0, within CASC-B's bound (≤ 1).
  - REPRODUCED on REFEREE-2's SPEC trace (R2 §C.4).
  - REFEREE-2's own climbs also hit it: 10 cases with slack 0 (the bound is attained) and saved witnesses witness_cascb_13011 / 13012,
    which need the climb's evaluate().
  - The packet's §10 vacuity list (KIND-MONO and CW-INT after the freeze, E-SEG after f0) is confirmed vacuous on both referees' engines.
    CASC-B was never listed as vacuous.
- W-ONCE's hypothesis (DATA, REFEREE §C.3): REFEREE-2's climbs reach it 571 times, 0 violations.
