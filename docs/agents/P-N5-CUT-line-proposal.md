# P-N5-CUT RESULTS-line proposal (lane text, verbatim; Lead copy for the referees)
Source: L-SI successor 31 message to the Lead, 2026-10-30 00:56:25Z (date -u), packet docs/si/P-N5-CUT-box43.md at l-si 2678f6c6 (sha1 d6519d3d72d67d25bafd21b7034092eaa4315457). Not yet checked by the Lead or a referee; referees check it symbol by symbol against §1-§8.

N5 on EVERY game: T ≤ 2n(n−1) + (n(n−1)+1)·(m_E·[1 + 2B* + (B*+1)·K] + SC* + O*), K := n(n−1) + (n(n−1)+1)(n−1)(m_E + REP* + 1), where B* = the largest number of Even S4c fallbacks plus τ-changing transitions inside one λ-run, REP* = the largest number of repeat late adoptions (a second or later late adoption of the same Even edge) inside one W-run, SC* = the largest number of W-silent plus own-cycle re-entries of Even edges in one λ-run, and O* = the largest number of τ-changing transitions inside one λ^U-run (Theorem CUT-RED, via Lemmas OPT-OFF, W-RETURN-G, LATE-SPLIT (first late adoptions ≤ m_E per W-run), WV-R and Corollary CUT-CHARGE) — a REDUCTION (none of B*, REP*, SC*, O* is bounded here; polynomial iff they are, Corollary CUT-POLY; not M3, not a TARGET.md claim; G-N5-TIME stays open).

Lead notes for the referees (not part of the line):
- Symbols to find defined in the line or carried: T, n, m_E, λ-run, W-run, λ^U-run, late adoption, re-entry, W-silent, own-cycle, τ-changing transition, S4c fallback.
- Standing premise (REFEREE 19 handover check, 01:12Z): R57 (b) (S1 returns an optimal counterstrategy realising Ξ) and G-N5T-1 are not named in the packet; OPT-OFF (i) uses the former. Expect an item.
- "polynomial iff they are": the converse direction must be justified or the word "iff" dropped.
