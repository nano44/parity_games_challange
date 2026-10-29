# R-N5-GP §C: joint map with REFEREE-2 on packet P-N5-GP, the fixes G0-G11, and the final RESULTS line
Written 2026-10-29T17:25Z by date -u, on the Lead's word of 17:23Z, by REFEREE successor 18, Opus 5.5 (D15). Every verdict is labelled (Opus 5.5, D15).
- My report: docs/referee/R-N5-GP.md (7dffab64). REFEREE-2's: docs/referee-2/R2-N5-GP.md at referee-2 4835eb3d plus 894a1971 (sha1 at 894a1971
  e4a16a0b…), read only after the Lead's word (my report pushed first).
- Fixes: docs/si/P-N5-GP-fixes-box31.md at l-si 64a3751c (sha1 65b59bbf…; G0-G5 from 6102969f, G6-G11 appended in 64a3751c). G12 (the final line)
  not on origin/claude/l-si at 17:24Z; the final line is checked below from the Lead's 17:23Z text.
- Independence: clean on both sides (REFEREE-2: names-only counts 0 at 16:41Z, 14 at its 17:08Z push; I: no REFEREE-2 GP file before the word).
  No shared code: mine gp_probe.py (capped DFS over unblocked paths) on rl_engine; REFEREE-2's gp_check.py (PCAP 300 paths per (k, x)) on si.py.

## 1. Verdict tables, row by row
| item | REFEREE (7dffab64) | REFEREE-2 (894a1971) | joint |
| --- | --- | --- | --- |
| §1 setting, [FRZ], [H] | CHECKED | SIGNED (well formed; one faithful elision, N-GP-1) | same content |
| §2 W-MON | SIGNED (premise GP-N1) | SIGNED (premise N-GP-2) | SIGNED |
| §2 XW | SIGNED (premise GP-N1) | SIGNED (R57 (a) (VJ), N-GP-2) | SIGNED |
| §3 GP* | SIGNED; every Case B sub-case redone without improvement | SIGNED; the same three NEW sub-cases (B1′(iii), B2b(ii), B2b(iii) c even) | SIGNED |
| §3a GP | SIGNED | SIGNED | SIGNED |
| §3a GP+ | SIGNED | SIGNED | SIGNED |
| §4 FW-R* | SIGNED | SIGNED | SIGNED |
| approved RESULTS line (16:26Z) | DOES NOT MATCH: drops L ≤ k − a and "Odd steps follow τ" (GP-E1; instances rand0, rand8) | DOES NOT MATCH: drops L ≤ k − a (instances b4_theta_n7, canonA_0, b5_os_n28), and "cycle node" must be "W-cycle node" (N-GP-7) | DOES NOT MATCH; the final line (§3) repairs all three |
| §5, §6 | not signed; pins exact | not signed; pins exact | — |
- VERDICTS IDENTICAL on all six signed items; no gap; nothing FALSE in the packet. The key point (Case B without the Ξ-improvement) was checked
  independently by both against box10 l. 29-55 with the same sub-case partition and the same three new sub-cases; REFEREE-2's census shows all
  three occur in data (alt_all: B1′(iii) 4, B2b(ii) 41, B2b(iii) c even 66) and the "impossible in F" configurations never do. My data did not
  count sub-cases: its census covers that.
- JOINT GAP MAP (packet): EMPTY. E-ITEM (RESULTS line only): the union GP-E1 ∪ N-GP-7 = three missing/imprecise hypotheses:
  (1) L ≤ k − a (both found it; it is what keeps every state k − 1 − i inside F);
  (2) r a path of G_τ (mine only; REFEREE-2 did not flag it): without it an Odd step off τ breaks the clause (rand8, x = 2 Odd, path [2, 4]);
  (3) "W-cycle node" (λ_W(u) = u) (REFEREE-2 only): λ_Ξ and λ_W are both constant on F but differ when D ≠ ∅, and GP* is stated for λ_W (§3:
  «u is a cycle node of state a (λ_W(u) = u)»). I agree; my control and the packet use λ_W.
- Data agree: 0 violations in both controls; MUT=all / plain W-frame Lemma P bites on ccl_w48_n48 in both (mine at the frozen phase [15, 18],
  REFEREE-2's X_GPall 2 there); rlin_cex_n40: one 10-transition frozen phase, R*_T 0, WCH 10 in both. REFEREE-2 reaches R*_T 40 (alt_all,
  grow_K40_n373); my corpora (n ≤ 40 library, n ≤ 140 pins) reach R*_T 2; no WCH > n − 1 in mine.

## 2. Notes, paired, and the fixes items G0-G11
| note | REFEREE | REFEREE-2 | fixes | class |
| --- | --- | --- | --- | --- |
| RESULTS line hypotheses | GP-E1 ((1), (2)) | N-GP-7 ((1), (3)) | G0 has (1), (2) but still "a cycle node"; G12 (to land) has all three | E-item, repaired by the final line (§3) |
| standing premises | GP-N1 | N-GP-2 | G1 ([OPT-H], [OPT-σ̄]), G7 | CLARIFICATION. G1's split is right: GP* uses [OPT-H] (through W-MON and [F1]) and not [OPT-σ̄]; XW and GP+ use [OPT-σ̄] |
| scope of GP* (τ, no S4c, λ_W constant suffice) | GP-N2 | — | G2 | WIDENING (labelled READING, "PROVED (lane) by the same text"). It extends GP* and FW-R* to maximal in-phase stretches without S4c and with λ_W constant that may contain σ̄-changes. I re-checked: neither proof uses σ̄ constant (W-MON needs only τ constant and non-fallback; FW-R* also uses S4a's ρ_{t+1}(y) ∈ {ρ_t(y)} ∪ Iσ_t(y)), so it is TRUE; but it is not part of the signed statement. To land it as a result it needs both referees' signature on its own wording; as a READING it may stand |
| §4's τ as a transition index | GP-N3 | — | G3 (rename to s) | CLARIFICATION (notation) |
| data scope of gp.py | GP-N4 | — (its own control is capped too: PCAP 300 paths per (k, x)) | G4: gp.py keeps ONE best unblocked path per vertex and length (path-tracking Bellman-Ford), so §6's "GP* 0 violations" covers stored paths only | DATA clarification. Agreed; FW-R*'s data are complete counts |
| B1′ (i) for both parities | GP-N5 | N-GP-3 | G5, G8 | CLARIFICATION |
| [CASE-A]'s elided parenthetical | — | N-GP-1 | G6 (quotes it in full, box10 l. 34-35) | CLARIFICATION. Checked against the text I read: exact |
| B1′ cycle shape (arc c → x meets π only at c) | (§2: "x ∉ π") | N-GP-4 | G9 | CLARIFICATION. Correct |
| §3a "follows directly" means the §3 induction with ALLOWED(⁺) | — | N-GP-5 | G10 | CLARIFICATION (wording) |
| R*_T vs R_T | — | N-GP-6 | G11 (R_T ≥ R*_T since blocked edges lie outside ALLOWED⁺) | CLARIFICATION / READING about another quantity; correct by §3a's proof |
- G0-G11 change no signed statement. G2 is the one WIDENING (true, but unsigned as a result); all others are clarifications or DATA.

## 3. The final RESULTS line (Lead 17:23Z; fixes item G12, superseding G0) against §3-§4
«In every frozen W-phase F = [a, b] of N5 on any game (N5-FRZ-box29 §0: no S4c fallback; τ, σ̄, λ_Ξ, λ_W constant; W = val(σ, τ)), (Lemma GP*)
for every k ∈ [a, b], W_k(x) ⊵ value(r) for every simple path r of G_τ (Odd steps follow τ) with at most k − a edges from x to a W-cycle node u of
F's first state a (λ_W(u) = u), none of whose Even edges (r_i, r_{i+1}) was BLOCKED at state k−1−i (W-better than σ's choice at r_i but not a
VJ00-improving edge of Ξ); (Corollary FW-R*) …; so R*_T = 0 ⇒ ≤ n−1 — a REDUCTION (…).»
- Clause by clause against §3's «unblocked at state k»: simple ✓; path of G_τ ✓; L ≤ k − a ✓; end u with λ_W(u) = u at state a ✓; Even edge i not
  blocked at k − 1 − i ✓; BLOCKED = W_t(z) ▷ W_t(ρ_t(x)) and (x, z) ∉ Iσ_t ✓ ("W-better than σ's choice at r_i", "not a VJ00-improving edge of
  Ξ"); k ∈ [a, b] ✓. FW-R* clause and R*_T = §4 ✓ (late adoption: an edge blocked at an earlier state of F). Scope tail ✓.
- MATCHES §3-§4 exactly; claims nothing beyond the signed items. (It does not carry G2's widening, correctly.)
- G12 itself is to be checked byte-for-byte against this text when it lands on l-si (the Lead will name the SHA).

## DONE / FINDINGS / NEEDS
- DONE: this §C.
- FINDINGS: verdicts identical with REFEREE-2 on all six items; packet gap map empty. The RESULTS line had three defects in union ((1) L ≤ k − a,
  both; (2) G_τ, mine; (3) W-cycle node, REFEREE-2's); the final 17:23Z line repairs all three and matches §3-§4. G0-G11: clarifications/DATA,
  except G2, a true WIDENING that stays a READING unless both referees sign it as a statement.
- NEEDS: Lead: the G12 SHA (byte check of the line); decide whether G2 is to be signed (then send its wording to both referees) or kept as a READING.
