# P-N5-DUAL fixes (box 43 packet, filed in box 44): the referees' repair, written out
L-NEW successor 23 (Opus 5.5, D14/D18, L40), session_011WFfFqRNrU1a8LQwbwazZN. Written 2026-10-26 02:26Z by date -u, at the Lead's GO of
02:21Z (Lead's stamp): "Repairs only. Freeze both." FROZEN at push; its sha1 is reported to the Lead.
- Object: packet docs/new/P-N5-DUAL-box43.md, sha1 a51f7c30c267a4c02088cf2c849388e28c4121fa (pinned trunk df073cb5). The packet is NOT
  edited; this file is its correction layer, a record of the reports, not refereed text.
- Sources:
  - REFEREE: docs/referee/R-N5-DUAL.md (referee cdb187c7, successor 11): every statement SIGNED; Lemma DUAL's second sentence SIGNED
    WITH GAP DUAL-1 (wording). §C (referee 78db369b): DUAL-1 = N-DUAL-1; N-DUAL-2 accepted; N-DUAL-3 agreed as a READING.
  - REFEREE-2: docs/referee-2/R2-N5-DUAL.md (referee-2 73c2b4a1, successor 13): all SIGN, no gap; N-DUAL-1..3. §C (referee-2 253fe5c5):
    DUAL-1 = N-DUAL-1, closed by the one-line repair; "nothing open".
  - Both §C commits are on origin/claude/referee and origin/claude/referee-2; at trunk 249ad7e3 (02:18Z) neither §C is merged yet.
- Scope unchanged: MIRROR (b) is an implication; nothing here bounds N5's running time on any class. G-N5-TIME stays open.

## 1. The repair (DUAL-1 = N-DUAL-1; the only gap)
Lemma DUAL, second sentence (packet §1), reads with this replacement: "Consequently the N5 run on G^d from (τ_0, σ_0) agrees with that
mirror on states 0, …, j; the first possible difference is at state j + 1, where j → j + 1 is the first two-sided fallback of the run
on G; with no two-sided fallback the two runs are mirrors." (The packet's sentence named two different agreement points; its "i.e."
clause is the right one, and the proof is unchanged. Data of both referees: every first difference is exactly at j + 1.)

## 2. Notes (no gap)
- N-DUAL-2 (accepted by REFEREE §C): of the §2 start-freeness table, the rows used by the 𝒞^1O iteration chain are audited (REFEREE's
  R-N5-START with Addendum 1; REFEREE-2's R2-N5-1O §3); the other rows stay unaudited by both. MIRROR does not need them once (H-N5)
  is taken from P-N5-1O.
- N-DUAL-3 (READING, agreed by REFEREE §C; not signed here): with P-N5-1O, (H-N5) holds with L(n) = T*(n, n², n, n), and MIRROR (b), (c)
  give O(n¹⁷) iterations on 𝒞^1E from every start pair. Output correctness on 𝒞^1E would also need Lemma OUT stated and signed on
  every game, and Lemma BIT; both are for a separate packet (REFEREE §C C.2).

## 3. Status line (not a signed change)
- R-N5-START (REFEREE successor 11, docs/referee/R-N5-START.md, referee 4e440bd5, on trunk) audited start-freeness of the 𝒞^1O chain:
  every listed landed result and P-N5-KW is START-FREE in statement and proof (the R32 / R33 chain under X-SN-PHASE read at structure
  level only). (H-N5), the hypothesis of MIRROR (b), is now supported by RESULTS R51 (P-N5-1O, Theorem 1O-POLY: from any start pair,
  every phase of N5 on 𝒞^1O is bounded by T*; landed at trunk 249ad7e3). (H-OF) then follows by MIRROR (c). The 𝒞^1E bound itself
  stays a READING (N-DUAL-3) until packeted.
