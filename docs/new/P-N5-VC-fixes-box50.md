# P-N5-VC fixes (box 50 packet; status changes only)
L-NEW successor 32 (Opus 5.5; D14, D18, L40). Written 2026-10-29 from 13:18Z (date -u). Lead's word 13:08Z (message to L-NEW): «append a
fixes item to the frozen packet: docs/new/P-N5-VC-fixes-box50.md, F1, "§4 CONJECTURE VC-N5 is FALSE (DLC_d, instance + sha1); Theorem
VC-BOUND and its converse stand". Message me the SHA. P-N5-VC stays deferred at the referees.» FROZEN at push; its sha1 is reported to the Lead.
- Object, FROZEN and not edited: docs/new/P-N5-VC-box50.md, sha1 078ad604cd232eed26a3fff7ad632852b0613e93 (l-new freeze 21f3285a), author
  L-NEW successor 31.
- No signed statement changes. §1-§2 (Lemma SS, Corollary SAUER, Theorem VC-BOUND (a)-(c), Corollary RANGE) are untouched. F1 changes the
  status of an item that is NOT to sign (§4).
- No referee has reported on P-N5-VC yet. Items from the referees' reports will go in a NEW file (P-N5-VC-fixes2-box50.md).
- Quotes. Every «…» below is verbatim at its tagged lines. They are checked by experiments/new/box49/quotecheck3.py, pinned in
  experiments/new/check.sh with their count, a shifted-line control and this file's sha1.

## F1. §4 CONJECTURE VC-N5 is FALSE; Theorem VC-BOUND and its converse stand
- Packet text: [Q docs/new/P-N5-VC-box50.md@21f3285a:120] «CONJECTURE VC-N5: dσ, dτ = O(1) on every game (with RANGE (i): N5 polynomial). OPEN.»
  and the status line [Q docs/new/P-N5-VC-box50.md@21f3285a:19] «a reduction; CONJECTURE VC-N5 (dσ, dτ = O(1)) OPEN."»
- Kill: [Q docs/new/N5-VCPHASE-box51.md@db1d3707:122-124] «Proposition DLC (PROVED, lane; premise: S4a computes an optimal strategy of the arena, VJ00). For every d ≥ 1, N5 on DLC_d (from SPEC S3) runs ONE phase of 2^(d+1) − 1 transitions, with no fallback, |D| = 0 and no Odd vertex. Its σ-family shatters the d edges (x_i, hA_i), so dσ(P) = dσ ≥ d > (log2 n − 1)/2»
  (docs/new/N5-VCPHASE-box51.md §3, proof by induction on t from SPEC S1-S5; L-NEW successor 32, unrefereed).
- Instances (generator experiments/new/box51/vcgad.py d; checker box51/dlccheck.py d, which regenerates the file and checks the trace formula at
  every state): experiments/new/box51/out/dlc_d4.pg (n 455, sha1 f77955fde03e36de8a1b3696523780368d28a184, phase VC 4, dlccheck PASS) and
  dlc_d5.pg (n 1897, sha1 345fae4c9644f63323c84846b0f85f10a78db837, 63 transitions, phase VC 5, dlccheck PASS). L-COMP's n5b gives the same
  state sequences (d = 2..5). The family is one-player, where N5 is already polynomial (RESULTS R17).
- New status of §4's first bullet: "CONJECTURE VC-N5 (dσ, dτ = O(1)): FALSE. DLC_d (N5-VCPHASE-box51 §3) has dσ ≥ d > (log2 n − 1)/2 in a single
  phase of a one-player game. The O(1) forms of VC-RUN and of VC-PHASE (N5-VC §6) are FALSE with it." The same replacement applies to
  "CONJECTURE VC-N5 (dσ, dτ = O(1)) OPEN" in the proposed RESULTS line: it reads "CONJECTURE VC-N5 (dσ, dτ = O(1)) FALSE (DLC_d)".
- What stands, unchanged: Theorem VC-BOUND (a)-(c) and Corollary RANGE are proved for every game and are not touched by DLC. On DLC_d,
  (a) gives I ≤ Φ_{d+1}(m) − 1, which is true and loose (I = 2^(d+1) − 1), and (c) gives dσ ≤ log2(I + 1) = d + 1, which DLC attains up to 1
  (d ≤ dσ ≤ d + 1). RANGE (ii) and (iii) bracket the route: (iii) forces only d = O(log n), and DLC_d shows that d = Θ(log n) occurs where N5
  is polynomial. So with a true VC bound the route gives at best (ii)'s quasi-polynomial bound (READING, N5-VCPHASE §5).
