# P-N5-EPR fixes (box 45 packet): the referees' gap and notes, written out
L-NEW successor 24 (Opus 5.5, D14/D18, L40). Written 2026-10-26 07:12Z by date -u, on the Lead's WORD of 07:09Z (Lead's stamp): "write
docs/new/P-N5-EPR-fixes-box45.md now, repairs only, and freeze it." FROZEN at push; its sha1 is reported to the Lead.
- Object: packet docs/new/P-N5-EPR-box45.md, sha1 8fecca797478d1a77564ac1c5b82d11e952559e0 (l-new 08abd9cb). The packet is NOT edited; this
  file is its correction layer, a record of the reports, not refereed text.
- Sources (by branch SHA):
  - REFEREE: docs/referee/R-N5-EPR.md (referee 3def3e11, successor 12): RESTRICT_E, EP-0, the consequence SIGNED; REPRO SIGNED with its last
    clause WITH GAP EPR-1; EP-k, EP-1 SIGNED WITH GAP EPR-1; notes EPR-N1, the standing premise. Addendum A (referee e18b4370): div_n8. §C
    (referee a0858144): one joint gap EPR-1 = G-EPR-1; REFEREE-2's (Στ) list check accepted as the sharper reading.
  - REFEREE-2: docs/referee-2/R2-N5-EPR.md (referee-2 796b4d36, successor 14): RESTRICT_E SIGN (N-EPR-1); REPRO's one-phase clause NOT SIGNED as
    stated (G-EPR-1); EP-0 SIGN (statement); EP-k (sum) SIGN; EP-k second part and EP-1 SIGN with "+ 1". Addendum A (referee-2 9a5692ad): div_n8.
    §C (referee-2 61022fe3): the same gap, found independently; nothing else open.
- Not a TARGET.md claim; G-N5-TIME stays open. The (Στ) premise check is the lane's audit in docs/new/N5-EPR-box45.md §9 (l-new bcca6c83,
  a198c9b9), going to the referees as packet P-N5-STAU; it is NOT signed here.

## 1. The joint gap and its repair
| gap | where in the packet | repaired text |
| --- | --- | --- |
| EPR-1 (REFEREE: "SIGNED WITH GAP") = G-EPR-1 (REFEREE-2: "NOT SIGNED as stated"), the same gap found independently | §2 Corollary REPRO, last clause: "and all of these states lie in ONE phase of that N5^τ run (λ′ = λ on them, by RESTRICT_E (i))"; its proof's last sentence; §3 EP-k second part; §3 EP-1 | The clause holds for the epoch's own states x, …, y and is FALSE at y′ = y + 1 (when y → y + 1 is in-phase on G): RESTRICT_E (i) needs σ̄_k = σ̄_E, and y + 1 ∉ E (σ̄\|Q changes there), so Ξ′ at (σ_{y+1}, τ) on G′_E may have other cycle nodes than Ξ_{y+1}. Read REPRO's last clause as: "the states (σ_x, τ), …, (σ_y, τ) lie in one phase of that N5^τ run; the transition from (σ_y, τ) to (σ_{y′}, τ) has its source in that phase and may leave it." Read EP-k's second part as: "len(E) ≤ 1 + the number of in-phase transitions of one phase of an N5^τ run on G′_E (started at (σ_x, τ))". Read EP-1's claim as: "len(E) ≤ T*(G′_E) + 1; in particular len(E) = O(m·Δ·n¹¹)". The orders of all bounds are unchanged; the sum part of EP-k (transitions of P = Σ_E len(E)) and the consequence X_SN^pre(E) ≤ len(E) are unaffected. |
- Witnesses (both reproduced on both engines): REFEREE: experiments/new/box44/instances/fb17_n32.pg (sha1 398e23e2eb18aac3c75af0b500a5d292f57a1d1e)
  from S3, epoch E = (26), D_E = {11}; at 27 σ̄(23) changes 4 → 18, τ and λ are unchanged on G, but λ′ at 27 ≠ λ_27 (cycle node 18 on G, 12 on
  G′_E, where 23 is forced to τ(23) = 4). REFEREE-2: docs/referee-2/R2-N5-EPR/instances/lamend_D0.pg (n 5, sha1 7f78faf7…, D_E = ∅; with
  lamend_D0.start: E = {1}, at state 2 λ′ = λ_W ≡ 4 ≠ λ ≡ 1) and lamend_D1.pg (n 7, sha1 80063b9f…, |D_E| = 1).
- Frequency (DATA): the epoch's last transition leaves the N5^τ phase on G′_E in 491 of 3,791 in-phase epoch ends (REFEREE) and 1,063 of 8,436
  (REFEREE-2), with |D_E| = 0 and 1 both frequent: the gap is not a corner case; the "+ 1" is needed.

## 2. Notes (no further gap)
| note(s) | where in the packet | line to read with the packet |
| --- | --- | --- |
| EPR-N1 (REFEREE) = REFEREE-2's EP-0 bullet under G-EPR-1 | §3 EP-0, proof | The statement stands (len(E) ≤ n + m); the proof must allow the exit transition. Read: the y − x transitions among x, …, y lie in one λ′-phase of the N5 (= N5^τ) run on the one-player G′_E (RESTRICT_E (i)); by R17 (e) at most one of them is a fallback, and a fallback leaves no improving edge, so if it occurs it is E's last transition and y → y + 1 is not in-phase on G (len(E) = y − x ≤ (n + m′ − 1) + 1); otherwise y − x ≤ n + m′ − 1 switch-best steps (R17 (c)) plus possibly the exit transition y → y + 1. Either way len(E) ≤ n + m′ ≤ n + m. |
| N-EPR-1 (REFEREE-2) = REFEREE §1 standing premise (both) | §1 RESTRICT_E (i), "Ξ′_k is S1's valuation on G′_E" | RESTRICT_E (i) rests on SPEC's standing requirement that S1's procedure returns an optimal counterstrategy (as 1E-N3; RESULTS R57), like every N5 result. A landing note. |
| (Στ)'s list (REFEREE-2 §3; accepted by REFEREE §C as the sharper reading) | §3 EP-1, premise (Στ) | REFEREE-2 checked the list item by item against R51 (a)'s per-phase citations (R18 (d) S (a), R21 (a), R48 (i), R50 (h)); R36 (c) and R47 (b) are rightly absent (not per-phase transition counts). Lane remark: "R49" in the R48 list is spurious (R48's RESULTS entry does not cite R49; the hit was the next heading); it only makes (Στ) ask for more, so EP-1 is unaffected. |

## 3. DATA (not proof)
- DIV occurs: experiments/new/box45/instances/div_n8.pg (n 8, sha1 4ed57ef2c1c92ee526ccd2683ae7c28b1caf5bfa) with div_n8.start (l-new 5d076f27):
  at an in-phase tie state with D = {3} (3 its own cycle node, W = Ξ), SPEC's own S4b on G′_E moves τ(3): 5 → 7, so SPEC N5 on G′_E leaves the
  phase while N5^τ keeps τ. Reproduced on both referees' engines (REFEREE Addendum A, REFEREE-2 Addendum A), with RESTRICT_E and REPRO holding
  (0 failures). So premise (Στ) IS exercised on some epochs; the packet's §5 sentence "premise (Στ) is NEVER EXERCISED" holds only for the
  packet's listed samples (and for both referees' own samples, DIV = 0). The variant N5^τ in REPRO is needed.
- CONJECTURE TIE-CYC (lane DATA, docs/new/N5-EPR-box45.md §7): at every recorded tie state (148 of 148), u is its own honest cycle node.

## 4. Status lines
- One joint gap (EPR-1 = G-EPR-1), repaired in §1 (an off-by-one at the epoch's last transition; orders unchanged). RESTRICT_E, EP-0, the sum part
  of EP-k and the consequence are signed as stated; REPRO, EP-k's second part and EP-1 are signed with the repair. EP-1 remains an IMPLICATION
  from (Στ); the premise check (lane audit §9) is not part of this file.
